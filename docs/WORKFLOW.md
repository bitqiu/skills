# Skills Workflow

This repository separates product engineering into lifecycle stages. Each skill performs one transformation; files under `workflows/` orchestrate them.

## 1. Idea to Spec

1. `grill-with-docs`: clarify goals, constraints, and unknowns.
2. Use `domain-modeling` when terminology or domain entities need alignment.
3. Use `research` when high-trust evidence is required, and record the findings.
4. Use `prototype` when a throwaway experiment can answer a high-risk design question.
5. `to-spec`: turn the agreed discussion into an actionable specification.

## 2. Spec to Design

1. `page-inventory`: specification → page inventory.
2. `information-architecture`: page inventory → information architecture.
3. `user-flow`: use cases and page inventory → user flows.
4. `design-system-reader`: existing design sources → design context.
5. `page-layout-designer`: page requirements, flows, and design context → page layout specification.
6. `design-validator`: check the specification against the layout and report only PASS, WARNING, or FAIL.
7. On PASS, use `figma-screen-builder` to create the Figma screen. On FAIL, return to layout design.

## 3. Design to Frontend

1. `frontend-context-reader`: read framework, routing, components, tokens, APIs, and test conventions.
2. `figma-to-frontend`: implement the approved Figma screen using the frontend context.
3. Apply Superpowers practices for TDD, debugging, and code review.
4. `frontend-design-validator`: compare the running page with Figma and produce a visual validation report.
5. On visual validation failure, return to `figma-to-frontend` for correction.
6. Run `verification-before-completion` before delivery.

## 4. Feature Development

`grill-with-docs` → `to-spec` → optionally `to-tickets` for large features → `writing-plans` → `using-git-worktrees` → `subagent-driven-development` → `test-driven-development` → `requesting-code-review` → `verification-before-completion` → `finishing-a-development-branch`.

## 5. Skill Authoring and Maintenance

Search for existing capabilities → prove the gap → write `.skill-drafts/<name>.md` → use `skill-creator` to create or update exactly one skill → review through `skill-creator` → run boundary tests → register the skill → validate the repository.

`skill-creator` belongs to the authoring toolchain and does not participate in the product lifecycle.
