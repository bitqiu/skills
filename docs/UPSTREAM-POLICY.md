# Upstream Skill Policy

Matt Pocock/skills and obra/superpowers are upstream sources, not complete runtime dependencies. This repository imports only the skills required by its product workflows.

## Selection Rules

- Start with the user requirement and the lifecycle stage.
- Search the current repository and both upstream repositories for an existing capability.
- Reuse an upstream skill when it covers the required responsibility without boundary conflicts.
- Add an upstream skill to `skills/` only when a workflow needs it.
- Prefer composition through `workflows/` over importing broad or overlapping capabilities.
- Do not copy `brainstorming` or `writing-skills` into the active namespace by default.
- Do not modify upstream `SKILL.md` files; record source and commit in the registry and lock file.

## Current Curated Set

The active namespace contains a curated subset selected for the workflows in this repository. The list can change when requirements change. Updating an upstream checkout does not automatically import every upstream skill.

After changing the curated set, update `registry/skills.yaml`, `UPSTREAM.lock.json`, and the relevant workflow documentation, then run `./scripts/validate-skills.sh`.
