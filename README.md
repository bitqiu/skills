# Product Engineering Skills Repository

A maintainable, single-responsibility skills repository for the complete product engineering lifecycle.

Matt Pocock/skills and obra/superpowers are upstream sources only. This repository selects individual skills according to project requirements and workflows; it does not use either repository wholesale.

**Idea → Product Spec → UX → Design → Figma → Frontend → QA → Verification → Ship**

## Skill Layers

### Matt Pocock

Public skills for discovery, specification, domain modeling, research, prototyping, and code review.

### Custom Skills

Repository-owned skills for UX, design context, page layout, Figma bridging, frontend context, frontend implementation, and visual QA. Every custom skill is created and maintained through `skill-creator`.

### Superpowers

Public skills for planning, implementation discipline, TDD, debugging, parallel work, code review, verification, and shipping.

### skill-creator

`skill-creator` is part of the Skill Authoring Toolchain. It is used to create, update, review, and optimize custom skills. It is not part of the product lifecycle.

## Documentation

- [Skill Catalog](docs/SKILL-CATALOG.md): skills grouped by source with descriptions.
- [Workflow](docs/WORKFLOW.md): the complete lifecycle and routing rules.
- [Installation](docs/INSTALL.md): installation, updates, and verification.
- [Architecture](docs/ARCHITECTURE.md): repository structure and design principles.
- [Upstream Policy](docs/UPSTREAM-POLICY.md): how upstream skills are selected and maintained.
- [Skill Boundaries](docs/SKILL-BOUNDARIES.md): responsibility boundaries.
- [Contributing Skills](docs/CONTRIBUTING-SKILLS.md): custom skill authoring rules.

## Quick Start

Install all active skills:

```sh
./scripts/install.sh
```

Install to a custom directory:

```sh
SKILLS_HOME="$HOME/.codex/skills/product-engineering" ./scripts/install.sh
```

Update public repository skills:

```sh
./scripts/sync-upstream.sh
```

Validate the repository:

```sh
./scripts/validate-skills.sh
```
