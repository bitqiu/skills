# DESIGN Output Contract

This contract captures the reference collection's common structure: machine-readable YAML tokens first, followed by an implementation-oriented narrative and matching light/dark component catalogs.

## Directory shape

```text
<requested-name-or-DESIGN>/
├── DESIGN.md
├── preview.html
└── preview-dark.html
```

Do not add a README as a substitute for any required file. Put supporting explanation in `DESIGN.md` and keep the previews self-contained.

## `DESIGN.md` frontmatter

Begin with valid YAML delimited by `---`. Use this top-level shape:

```yaml
---
version: "1.0"
name: "[Product or concept] design system"
description: "[One compact paragraph describing the visual thesis, product shape, density, signature color, typography, surface behavior, and defining interaction pattern.]"
product:
  archetype: "backend-admin | mobile-app | portal | landing-page | aigc | large-screen"
  audience: "[primary audience]"
  platform: "[web, iOS, Android, responsive web, display wall, or hybrid]"
themes:
  default: light
  supported: [light, dark]
colors:
  primary: "#000000"
  primary-hover: "#000000"
  primary-active: "#000000"
  on-primary: "#ffffff"
  canvas: "#ffffff"
  surface-1: "#ffffff"
  surface-2: "#f5f5f5"
  ink: "#111111"
  ink-muted: "#666666"
  hairline: "#dddddd"
  focus: "#000000"
  success: "#000000"
  warning: "#000000"
  danger: "#000000"
typography:
  display:
    fontFamily: "[family and fallbacks]"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  heading:
    fontFamily: "[family and fallbacks]"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  body:
    fontFamily: "[family and fallbacks]"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label:
    fontFamily: "[family and fallbacks]"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px
spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 80px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 10px 16px
  text-input:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 10px 12px
---
```

Extend the token set to fit the product. Avoid token aliases that have no defined source. Use quoted strings when YAML could reinterpret a value, especially hex colors, font stacks, and values containing braces.

## Required Markdown sections

Use this order. Rename a subsection when product language calls for it, but do not omit the underlying concern.

### `## Overview`

State the visual thesis, product archetype, audience, density, signature motifs, and evidence basis. Explain what makes the system distinct in a few concrete paragraphs.

### `## Colors`

Cover brand/accent, canvas and surfaces, text, borders, semantic colors, focus, overlays, and dark-theme mapping. For each important color give the token, value, role, and restrictions.

### `## Typography`

Define font families and fallbacks, hierarchy, weights, sizes, line heights, letter spacing, numeric treatment, and language-specific considerations. Explain font substitution when the preferred face is unavailable.

### `## Layout`

Define spacing scale, grid, containers, navigation dimensions, density, alignment, safe areas, and whitespace philosophy. Include the product's primary screen shell.

### `## Elevation & Depth`

Define surface hierarchy, borders, shadows, overlays, sticky regions, modals, and when not to add depth.

### `## Shapes`

Define radius scale, control geometry, icon sizing/stroke, image treatment, charts, and any signature shape language.

### `## Components`

Document navigation, buttons, forms, cards/containers, feedback, and at least three core product-specific components. Include relevant default, hover, focus, active/selected, disabled, loading, empty, error, and success behavior.

### `## Do's and Don'ts`

Give concrete guardrails. Prefer paired rules such as "Use a single accent for the primary action" and "Do not color every metric tile." Avoid vague advice like "make it modern."

### `## Responsive Behavior`

Define breakpoints or device classes, touch targets, collapse/reflow strategy, type and spacing changes, tables/charts, imagery, and navigation. Large-screen products should include minimum operating resolution and distance-viewing rules.

### `## Accessibility`

Cover contrast, focus, keyboard access, reduced motion, target sizes, status communication beyond color, text scaling, and chart/data alternatives.

### `## Iteration Guide`

Explain what can evolve without losing the identity and which few traits should remain stable.

### `## Known Gaps`

List unavailable evidence, inferred choices, contradictions, unverified states, and assets/fonts that need confirmation. Write `None identified` only when all important claims were verified.

## Preview contract

Both HTML files should use the same information architecture:

1. Sticky or compact catalog navigation
2. First-viewport product specimen showing the real interaction model
3. Color roles and contrast pairings
4. Typography hierarchy
5. Controls and forms with states
6. Core product-specific components
7. Spacing, shape, border, and elevation tokens
8. Responsive behavior summary

The page must be useful at `390px`, `768px`, `1024px`, and `1440px` widths. Use stable grid tracks, `minmax()`, `aspect-ratio`, and explicit control dimensions where dynamic content could otherwise shift layout.

`preview.html` demonstrates the light theme. `preview-dark.html` demonstrates a separately tuned dark theme. Preserve brand identity, component geometry, and hierarchy between them while adjusting canvas, surfaces, borders, shadows, text, images, and data colors for the viewing environment.

## Quality bar

- All color strings are valid CSS colors and all referenced tokens exist.
- The frontmatter and prose agree with both previews.
- Content is specific to the named product and contains no `TODO`, placeholder token, or lorem ipsum.
- The first viewport is a usable product specimen, not a marketing explanation of the files.
- UI text fits its container at mobile and desktop sizes.
- Controls expose hover/focus/disabled or selected states where meaningful.
- No nested decorative card stacks or gratuitous gradient/orb decoration.
- Preview files open directly without a build step.
