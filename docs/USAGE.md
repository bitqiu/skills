# Usage Guide

## Discover available skills

List the active skills in the repository:

```sh
./scripts/list-skills.sh
```

Read the source and description of a specific skill:

```sh
cat skills/page-inventory/SKILL.md
```

The catalog groups every active skill by source:

```text
docs/SKILL-CATALOG.md
```

## Choose a skill by required output

Start with the artifact you need, then select the skill that owns that transformation:

| Need | Skill |
|---|---|
| Page inventory | `page-inventory` |
| Navigation hierarchy | `information-architecture` |
| User flow | `user-flow` |
| Existing design context | `design-system-reader` |
| Page layout specification | `page-layout-designer` |
| Design validation report | `design-validator` |
| Figma screen | `figma-screen-builder` |
| Frontend repository context | `frontend-context-reader` |
| Frontend implementation | `figma-to-frontend` |
| Visual validation report | `frontend-design-validator` |

Use an upstream skill when the requirement belongs to its documented responsibility. Do not invoke an upstream skill merely because it is available.

## Run a complete product flow

For a new product or major feature, follow the staged workflow:

```text
Idea
  → grill-with-docs
  → domain-modeling (optional)
  → research (optional)
  → prototype (optional)
  → to-spec
  → page-inventory
  → information-architecture
  → user-flow
  → design-system-reader
  → page-layout-designer
  → design-validator
  → figma-screen-builder
  → frontend-context-reader
  → figma-to-frontend
  → test-driven-development
  → frontend-design-validator
  → code-review
  → verification-before-completion
```

Optional stages should be added only when their input is needed. For example, skip `prototype` when the design question is already answered.

## Use one skill at a time

Provide the skill with its required input and ask for its single output. For example:

```text
Use page-inventory to convert this approved product spec into a page inventory.
Do not define navigation, user flows, layouts, Figma, or frontend code.
```

Then pass the resulting artifact to the next skill:

```text
Use information-architecture with this page inventory to define page hierarchy,
parent-child relationships, and navigation grouping.
```

This keeps responsibility boundaries explicit and makes each artifact reviewable.

## Handle validation results

Validators report findings only. When `design-validator` or `frontend-design-validator` returns `FAIL`:

1. Read and address each reported issue in the owning builder skill.
2. Run the validator again.
3. Continue only after the report reaches the required status.

Do not ask a validator to edit Figma or source code.

## Use custom skills in another project

Install the curated set:

```sh
./scripts/install.sh
```

Point the installer at a project-specific directory when needed:

```sh
SKILLS_HOME="$HOME/.codex/skills/my-project" ./scripts/install.sh
```

Enable only the skills required by that project. The upstream checkouts and repository documentation are authoring and maintenance resources, not mandatory runtime dependencies.

## Maintain the repository

After changing the curated set or workflows:

```sh
./scripts/validate-skills.sh
./scripts/list-skills.sh
```

For custom skill changes, follow `docs/CONTRIBUTING-SKILLS.md` and use `skill-creator` for create, review, update, and optimization operations.
