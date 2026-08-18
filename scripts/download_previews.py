#!/usr/bin/env python3
"""Collect DESIGN.md and light/dark previews from a Git repository."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import contextmanager
from html.parser import HTMLParser
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen


DEFAULT_REPOSITORY = "https://github.com/VoltAgent/awesome-design-md.git"
DEFAULT_SOURCE_DIR = Path("design-md")
DEFAULT_OUTPUT_DIR = Path.cwd() / "design-md"
URL_PATTERN = re.compile(r"https?://[^\s<>\"']+")
USER_AGENT = "Mozilla/5.0 (compatible; design-repository-collector/2.0)"
REQUIRED_NAMES = ("DESIGN.md", "preview.html", "preview-dark.html")


class PreviewFrameParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.sources: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag.lower() != "iframe":
            return
        source = dict(attrs).get("src")
        if source and is_preview_url(source):
            self.sources.append(source)


def is_preview_url(url: str) -> bool:
    path = urlsplit(url).path.rstrip("/")
    return re.search(r"/preview(?:-dark)?(?:\.html)?$", path) is not None


def is_dark_preview(url: str) -> bool:
    return urlsplit(url).path.rstrip("/").endswith(
        ("/preview-dark", "/preview-dark.html")
    )


def extract_urls(markdown: str) -> list[str]:
    return [
        match.group(0).rstrip(".,;:!?)]")
        for match in URL_PATTERN.finditer(markdown)
    ]


def request_bytes(url: str, timeout: float) -> tuple[bytes, str]:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=timeout) as response:
        return response.read(), response.geturl()


def dark_variant(light_url: str) -> str:
    parts = urlsplit(light_url)
    path = parts.path.rstrip("/")
    if path.endswith("/preview.html"):
        path = f"{path[:-len('/preview.html')]}/preview-dark.html"
    elif path.endswith("/preview"):
        path = f"{path[:-len('/preview')]}/preview-dark"
    else:
        raise ValueError(f"Cannot derive dark preview URL from {light_url}")
    return urlunsplit(parts._replace(path=path))


def discover_preview_urls(
    readme: Path | None, slug: str, timeout: float
) -> tuple[str, str]:
    if readme is None:
        markdown_urls = [f"https://getdesign.md/{quote(slug, safe='.')}/design-md"]
    else:
        markdown_urls = extract_urls(readme.read_text(encoding="utf-8"))

    preview_urls = [url for url in markdown_urls if is_preview_url(url)]
    light_url = next(
        (url for url in preview_urls if not is_dark_preview(url)), None
    )
    dark_url = next((url for url in preview_urls if is_dark_preview(url)), None)

    if light_url is None:
        detail_url = next(
            (
                url
                for url in markdown_urls
                if urlsplit(url).path.rstrip("/").endswith("/design-md")
            ),
            None,
        )
        if detail_url is None:
            raise ValueError("README contains no design-md or preview URL")

        page_bytes, final_url = request_bytes(detail_url, timeout)
        parser = PreviewFrameParser()
        parser.feed(page_bytes.decode("utf-8", errors="replace"))
        discovered = [urljoin(final_url, source) for source in parser.sources]
        light_url = next(
            (url for url in discovered if not is_dark_preview(url)), None
        )
        dark_url = next(
            (url for url in discovered if is_dark_preview(url)), dark_url
        )

    if light_url is None:
        raise ValueError("Design page contains no light preview iframe")
    if dark_url is None:
        dark_url = dark_variant(light_url)
    return light_url, dark_url


def atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    try:
        temporary.write_bytes(content)
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def looks_like_html(content: bytes) -> bool:
    prefix = content[:2048].decode("utf-8", errors="ignore").lower()
    return "<html" in prefix or "<!doctype html" in prefix


def is_local_repository(value: str) -> bool:
    return Path(value).expanduser().exists()


@contextmanager
def checkout_repository(repository: str, ref: str | None) -> Iterator[Path]:
    if is_local_repository(repository):
        root = Path(repository).expanduser().resolve()
        if not root.is_dir():
            raise ValueError(f"Repository path is not a directory: {root}")
        yield root
        return

    if shutil.which("git") is None:
        raise RuntimeError("git is required to read a remote repository")

    with TemporaryDirectory(prefix="design-repository-") as temporary_root:
        destination = Path(temporary_root) / "repository"
        command = ["git", "clone", "--depth", "1"]
        if ref:
            command.extend(("--branch", ref))
        command.extend((repository, str(destination)))
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            detail = result.stderr.strip() or result.stdout.strip()
            raise RuntimeError(f"git clone failed: {detail}")
        yield destination


def find_design_directories(source_root: Path) -> list[Path]:
    if not source_root.is_dir():
        raise ValueError(f"Source directory does not exist: {source_root}")
    directories = sorted(
        design_file.parent
        for design_file in source_root.rglob("DESIGN.md")
        if ".git" not in design_file.parts
    )
    if not directories:
        raise ValueError(f"No DESIGN.md files found below {source_root}")
    return directories


def destination_for(
    source_root: Path, design_directory: Path, output_root: Path
) -> Path:
    relative = design_directory.relative_to(source_root)
    if relative == Path("."):
        relative = Path(design_directory.name)
    return output_root / relative


def collect_design(
    source_root: Path,
    design_directory: Path,
    output_root: Path,
    timeout: float,
    repo_only: bool,
) -> tuple[str, tuple[str, ...]]:
    destination = destination_for(source_root, design_directory, output_root)
    relative = destination.relative_to(output_root).as_posix()
    actions: list[str] = []
    outputs = {
        "DESIGN.md": (design_directory / "DESIGN.md").read_bytes(),
    }
    actions.append("DESIGN.md:repository")

    missing_previews: list[str] = []
    for name in ("preview.html", "preview-dark.html"):
        source_file = design_directory / name
        if source_file.is_file():
            outputs[name] = source_file.read_bytes()
            actions.append(f"{name}:repository")
        else:
            missing_previews.append(name)

    if missing_previews:
        if repo_only:
            raise ValueError(
                "repository is missing " + ", ".join(missing_previews)
            )
        readme = design_directory / "README.md"
        light_url, dark_url = discover_preview_urls(
            readme if readme.is_file() else None,
            design_directory.name,
            timeout,
        )
        urls = {
            "preview.html": light_url,
            "preview-dark.html": dark_url,
        }
        for name in missing_previews:
            content, final_url = request_bytes(urls[name], timeout)
            if not looks_like_html(content):
                raise ValueError(f"Downloaded preview is not HTML: {final_url}")
            outputs[name] = content
            actions.append(f"{name}:download")

    for name in REQUIRED_NAMES:
        if name not in outputs:
            raise RuntimeError(f"Collection did not resolve {relative}/{name}")
    for name, content in outputs.items():
        atomic_write(destination / name, content)
    return relative, tuple(actions)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Collect DESIGN.md, preview.html, and preview-dark.html from a "
            "remote Git repository or local working tree."
        )
    )
    parser.add_argument(
        "repository",
        nargs="?",
        default=DEFAULT_REPOSITORY,
        help=f"Git URL or local repository path (default: {DEFAULT_REPOSITORY})",
    )
    parser.add_argument("--ref", help="Remote branch or tag to clone")
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=DEFAULT_SOURCE_DIR,
        help="Directory containing design folders inside the repository",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Collected output root (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        metavar="NAME",
        help="Collect only this design name or relative path; repeatable",
    )
    parser.add_argument(
        "--repo-only",
        action="store_true",
        help="Do not download previews missing from the repository",
    )
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--workers", type=int, default=8)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.workers < 1:
        print("error: --workers must be greater than zero", file=sys.stderr)
        return 2
    if args.timeout <= 0:
        print("error: --timeout must be greater than zero", file=sys.stderr)
        return 2

    output_root = args.output_dir.expanduser().resolve()
    failures: list[tuple[str, Exception]] = []

    try:
        with checkout_repository(args.repository, args.ref) as repository_root:
            source_root = (repository_root / args.source_dir).resolve()
            try:
                source_root.relative_to(repository_root.resolve())
            except ValueError as error:
                raise ValueError("--source-dir must stay inside the repository") from error

            directories = find_design_directories(source_root)
            if args.only:
                selected = set(args.only)
                directories = [
                    directory
                    for directory in directories
                    if directory.name in selected
                    or directory.relative_to(source_root).as_posix() in selected
                ]
                if not directories:
                    raise ValueError(
                        "No designs matched --only: " + ", ".join(args.only)
                    )

            worker_count = min(args.workers, len(directories))
            with ThreadPoolExecutor(max_workers=worker_count) as executor:
                futures = {
                    executor.submit(
                        collect_design,
                        source_root,
                        directory,
                        output_root,
                        args.timeout,
                        args.repo_only,
                    ): directory.relative_to(source_root).as_posix()
                    for directory in directories
                }
                for future in as_completed(futures):
                    slug = futures[future]
                    try:
                        relative, actions = future.result()
                        print(f"collected: {relative} ({', '.join(actions)})")
                    except (OSError, HTTPError, URLError, RuntimeError, ValueError) as error:
                        failures.append((slug, error))
                        print(f"failed: {slug}: {error}", file=sys.stderr)
    except (OSError, RuntimeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    succeeded = len(directories) - len(failures)
    print(f"summary: {succeeded}/{len(directories)} designs collected")
    if failures:
        print(
            "failed designs: " + ", ".join(slug for slug, _ in failures),
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
