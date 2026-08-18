---
name: design-spec-generator
description: Turn product source code, UI screenshots, website URLs, or brief/detailed product requirements into an implementation-ready DESIGN.md plus polished light and dark HTML design-system previews. Use this skill whenever a user asks to extract, infer, document, define, or generate a product design language, UI specification, design system, visual direction, style guide, or DESIGN folder for admin dashboards, mobile apps, portals, landing pages, AIGC products, data walls, or similar digital products, even when the input is incomplete or the user does not explicitly say "DESIGN.md".
---

# Design Spec Generator

Create a concrete design language from the best evidence the user provides, then make it inspectable in two standalone HTML previews. Treat source code, screenshots, URLs, and prose as different views of the same product rather than as separate workflows.

## Read first

Read [references/design-contract.md](references/design-contract.md) before writing any output. Read [references/product-archetypes.md](references/product-archetypes.md) after identifying the product shape. Use the closest archetype as a starting point, then adapt it to the actual product and audience.

## Output contract

Create one output directory in the user's requested location:

- If the user names the directory, preserve that name exactly.
- Otherwise, name it `DESIGN`.
- Put `DESIGN.md`, `preview.html`, and `preview-dark.html` directly inside it.
- Keep each preview self-contained: inline its CSS and small scripts so it opens directly from disk.
- Do not replace unrelated files already present in the output directory.

The three files form one system. Token names, values, component geometry, typography, and behavioral claims must agree across them.

## Workflow

### 1. Establish the evidence

Use every supplied input and record where confidence comes from.

- For source code, inspect design tokens, CSS variables, theme configuration, fonts, shared components, routes, layouts, icons, images, breakpoints, and representative product screens. Prefer shipped implementation over comments or stale documentation.
- For screenshots, inspect composition, density, spacing rhythm, color roles, typography hierarchy, component states, data presentation, navigation, imagery, and platform conventions. Distinguish measured observations from estimates.
- For a URL, inspect the rendered desktop and mobile experience when browsing tools are available. Check multiple representative areas, interaction states, loaded fonts/assets, and both themes when the site exposes them. If the URL cannot be reached, state that limitation in `Known Gaps` and continue from other evidence.
- For detailed requirements, translate brand attributes, audience, workflows, and constraints into explicit tokens and rules.
- For a short description, make a coherent art-direction choice instead of returning a generic template. Clearly list consequential assumptions in `Known Gaps`.

Do not invent claims such as an exact proprietary font, measured token, or existing dark theme when the evidence does not support them. Use practical fallbacks and label inferred choices.

### 2. Classify the product

Choose the closest primary archetype: backend admin, mobile app, portal/content site, landing page, AIGC product, or large-screen dashboard. A product can be hybrid; name one primary archetype and borrow only the patterns that support its workflows.

Define before styling:

1. Primary audience and repeated job
2. Information density and reading distance
3. Main navigation model
4. Highest-value action
5. Trust, accessibility, and platform constraints
6. Visual thesis in one sentence

These decisions prevent an operations console from becoming a marketing page or a mobile experience from becoming a compressed desktop layout.

### 3. Synthesize the design language

Build a restrained, recognizable system rather than a collection of trendy effects.

- Give colors semantic roles and accessible contrast relationships.
- Define a deliberate type hierarchy with available or credible fallback fonts.
- Use a compact spacing scale and explicit container/grid behavior.
- Specify radii, borders, elevation, focus, disabled, hover, pressed, loading, empty, error, and success states where relevant.
- Make component guidance product-specific. A data table, prompt composer, article rail, campaign CTA, and KPI tile should not share the same generic card treatment.
- Keep light and dark themes related but independently tuned. Dark mode is not a mechanical inversion.
- Avoid decorative effects that compete with the product's core information.

### 4. Write `DESIGN.md`

Follow the schema and section order in `references/design-contract.md`. Start with YAML frontmatter containing machine-readable tokens and reusable component definitions, then explain how and why to use them in Markdown.

Be specific enough that another coding agent can implement a new screen without guessing. Include values, states, responsive changes, and anti-patterns. Use prose for design intent and tables or concise lists for exact mappings.

### 5. Build both previews

Each preview is a visual acceptance test, not a decorative cover page.

- Place a realistic, archetype-specific product specimen in the first viewport.
- Include a navigable catalog for colors, typography, spacing, radius/elevation, controls, forms, and core product components.
- Demonstrate normal plus important interaction/semantic states.
- Use realistic domain copy and data rather than lorem ipsum.
- Add lightweight interactions when they clarify behavior, such as tabs, selected rows, a sidebar toggle, theme-independent filters, or prompt controls.
- Make layouts responsive at narrow mobile and wide desktop widths. Nothing may overlap, clip, or depend on viewport-scaled font sizes.
- Use semantic HTML, visible focus styles, labels, adequate contrast, and reduced-motion handling.
- Prefer CSS variables whose names match `DESIGN.md` tokens.
- Use the source project's icon library when available. Otherwise use text labels or official library icons with accessible names; do not improvise inconsistent symbols.
- Do not make the light and dark files byte-identical or change only `color-scheme`; tune surfaces, borders, shadows, and muted text for each theme.

The previews may present the design system as a product workbench, but they must still feel native to the product. Avoid a generic hero followed by unrelated cards.

### 6. Verify

Run:

```bash
python3 <skill-directory>/scripts/validate_output.py <output-directory>
```

Then inspect both HTML files in a browser at approximately 1440x900 and 390x844. Check the browser console, keyboard focus, responsive reflow, text containment, and visible differences between light and dark themes. Fix issues before reporting completion.

## Handling ambiguity

Proceed with explicit assumptions when they are reversible and do not change the product's purpose. Ask a question only when a missing decision would materially change the product category, brand identity, or required output location.

When inputs conflict, use this precedence unless the user says otherwise:

1. Explicit current requirements
2. Current rendered product behavior
3. Current source tokens and shared components
4. Screenshots
5. Existing prose documentation
6. Inference

Document meaningful conflicts and the chosen resolution in `Known Gaps`.

## Completion response

Report the output directory, the inferred product archetype, the evidence used, and validation performed. Mention unresolved gaps briefly; do not paste the entire design specification into chat.
