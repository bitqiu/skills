#!/usr/bin/env python3
"""Validate the deterministic parts of a design-spec-generator output."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


REQUIRED_FILES = ("DESIGN.md", "preview.html", "preview-dark.html")
REQUIRED_SECTIONS = (
    "Overview",
    "Colors",
    "Typography",
    "Layout",
    "Components",
    "Responsive Behavior",
    "Accessibility",
    "Known Gaps",
)
REQUIRED_FRONTMATTER_KEYS = (
    "version",
    "name",
    "description",
    "colors",
    "typography",
    "rounded",
    "spacing",
    "components",
)
PLACEHOLDERS = re.compile(r"\b(?:TODO|TBD|lorem ipsum)\b|\[insert\b|__\w+__", re.I)


class PreviewParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: set[str] = set()
        self.has_viewport = False
        self.has_lang = False
        self.has_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.add(tag)
        values = dict(attrs)
        if tag == "html" and values.get("lang"):
            self.has_lang = True
        if tag == "meta" and values.get("name", "").lower() == "viewport":
            self.has_viewport = True
        if tag == "title":
            self.has_title = True


def frontmatter(text: str) -> str | None:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", text, re.S)
    return match.group(1) if match else None


def validate_design(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    yaml = frontmatter(text)
    if yaml is None:
        errors.append("DESIGN.md must begin with delimited YAML frontmatter")
    else:
        for key in REQUIRED_FRONTMATTER_KEYS:
            if not re.search(rf"(?m)^{re.escape(key)}:\s*", yaml):
                errors.append(f"DESIGN.md frontmatter is missing '{key}'")
    for section in REQUIRED_SECTIONS:
        if not re.search(rf"(?m)^## {re.escape(section)}\s*$", text):
            errors.append(f"DESIGN.md is missing '## {section}'")
    if len(re.findall(r"#[0-9a-fA-F]{6}\b", text)) < 8:
        errors.append("DESIGN.md should define at least eight concrete hex colors")
    if PLACEHOLDERS.search(text):
        errors.append("DESIGN.md contains placeholder text")
    return errors


def validate_preview(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    parser = PreviewParser()
    parser.feed(text)
    if not re.match(r"\s*<!doctype html>", text, re.I):
        errors.append(f"{path.name} is missing an HTML5 doctype")
    if not parser.has_lang:
        errors.append(f"{path.name} must set the html lang attribute")
    if not parser.has_viewport:
        errors.append(f"{path.name} is missing a viewport meta tag")
    if not parser.has_title:
        errors.append(f"{path.name} is missing a title")
    for tag in ("style", "main", "section", "button"):
        if tag not in parser.tags:
            errors.append(f"{path.name} should contain a <{tag}> element")
    if "--" not in text:
        errors.append(f"{path.name} should expose design tokens as CSS custom properties")
    if "@media" not in text:
        errors.append(f"{path.name} should include responsive CSS")
    if ":focus" not in text and ":focus-visible" not in text:
        errors.append(f"{path.name} should define a visible focus state")
    if PLACEHOLDERS.search(text):
        errors.append(f"{path.name} contains placeholder text")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()
    root = args.output_directory.expanduser().resolve()

    errors: list[str] = []
    if not root.is_dir():
        errors.append(f"Output directory does not exist: {root}")
    else:
        for name in REQUIRED_FILES:
            path = root / name
            if not path.is_file():
                errors.append(f"Missing required file: {name}")
        if not errors:
            errors.extend(validate_design(root / "DESIGN.md"))
            errors.extend(validate_preview(root / "preview.html"))
            errors.extend(validate_preview(root / "preview-dark.html"))
            if (root / "preview.html").read_bytes() == (root / "preview-dark.html").read_bytes():
                errors.append("Light and dark previews must not be identical")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed: {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
