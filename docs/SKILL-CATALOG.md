# Skill Catalog

Skills are grouped by source. Custom skills are created through `skill-creator`; public repository skills preserve upstream content and are updated through the sync script.

## Custom Skills (skill-creator)

10 skills.

| Skill | Description |
|---|---|
| `design-system-reader` | Read existing design sources and produce design context. Use this skill only for this exact lifecycle stage and output. |
| `design-validator` | Validate an approved product specification against a page layout specification. Use this skill only for this exact lifecycle stage and output. |
| `figma-screen-builder` | Build a Figma screen from an approved page layout specification. Use this skill only for this exact lifecycle stage and output. |
| `figma-to-frontend` | Implement an approved Figma screen in an existing frontend repository. Use this skill only for this exact lifecycle stage and output. |
| `frontend-context-reader` | Read a frontend repository and produce implementation context. Use this skill only for this exact lifecycle stage and output. |
| `frontend-design-validator` | Validate a running frontend against an approved Figma screen. Use this skill only for this exact lifecycle stage and output. |
| `information-architecture` | Convert a page inventory into an information architecture. Use this skill only for this exact lifecycle stage and output. |
| `page-inventory` | Convert an approved product specification into a page inventory. Use this skill only for this exact lifecycle stage and output. |
| `page-layout-designer` | Convert page requirements, flows, and design context into a page layout specification. Use this skill only for this exact lifecycle stage and output. |
| `user-flow` | Convert use cases and page inventory into user flows. Use this skill only for this exact lifecycle stage and output. |

## Public Repository: Matt Pocock/skills

7 skills.

| Skill | Description |
|---|---|
| `code-review` | "Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/spec asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to \"review since X\"." |
| `domain-modeling` | Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a CONTEXT.md, or recording or editing an ADR. |
| `grill-with-docs` | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| `prototype` | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should look like. |
| `research` | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a background agent. |
| `to-spec` | "Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed." |
| `to-tickets` | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edges as text in one file per ticket locally, or native blocking links on a real tracker). |

## Public Repository: obra/superpowers

12 skills.

| Skill | Description |
|---|---|
| `dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| `executing-plans` | Use when you have a written implementation plan to execute in a separate session with review checkpoints |
| `finishing-a-development-branch` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work |
| `receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation |
| `requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| `subagent-driven-development` | Use when executing implementation plans with independent tasks in the current session |
| `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| `test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code |
| `using-git-worktrees` | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback |
| `using-superpowers` | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions |
| `verification-before-completion` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always |
| `writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code |
