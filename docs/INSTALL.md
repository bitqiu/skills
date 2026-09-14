# Installation Guide

## Requirements

- Git
- POSIX Shell (macOS, Linux, or WSL)
- Python 3 (used by repository validation and lock-file updates)

## Install from the Repository

Run this command from the repository root:

```sh
./scripts/install.sh
```

The default destination is `$HOME/.codex/skills/product-engineering`. Choose another destination with:

```sh
SKILLS_HOME="$HOME/.codex/skills/product-engineering" ./scripts/install.sh
```

The installer copies the curated skills in the flat `skills/` namespace and runs `validate-skills.sh` first. To replace an existing installation:

```sh
FORCE=1 ./scripts/install.sh
```

## Manual Installation

Copy only the required skill directories from `skills/` to your Agent platform's Skills directory. Keep each directory name identical to the `name` in its `SKILL.md`. Do not copy `.skill-drafts/`, `registry/`, or `workflows/` into the runtime directory.

The upstream repositories are sources, not complete runtime dependencies. Import or enable an upstream skill only when a project workflow requires it.

## Update Upstream Sources

```sh
./scripts/sync-upstream.sh
```

The script fetches the latest commits from Matt Pocock/skills and obra/superpowers and updates `UPSTREAM.lock.json`. It updates the upstream checkouts only; it does not import every upstream skill into the active namespace. Review the curated set and copy only the required skills before reinstalling:

```sh
FORCE=1 ./scripts/install.sh
```

## Verify the Installation

```sh
./scripts/validate-skills.sh
./scripts/list-skills.sh
```

A `PASS` result and a list of skill paths confirm that the repository content is valid.
