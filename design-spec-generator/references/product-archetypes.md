# Product Archetypes

Choose one primary archetype to set density, navigation, first-viewport composition, and core components. Hybrid products can borrow secondary patterns, but the primary workflow should remain unmistakable.

## Backend admin

**Audience and rhythm:** Operators repeat high-frequency tasks, scan exceptions, compare records, and need predictable placement. Favor quiet chrome, compact hierarchy, and restrained color.

**Primary shell:** Persistent sidebar or top navigation, page header with scoped actions, filters, table/work queue, detail drawer or split pane.

**Preview specimen:** Show a credible operational screen with summary metrics, filters, a dense table, status chips, pagination, row selection, and a detail/action region. Make keyboard focus and bulk-action states visible.

**Core components:** Data table, filter bar, command/search, form sections, status/alerts, audit activity, pagination, drawers/modals.

**Avoid:** Marketing heroes, equal-weight cards for every datum, giant headings, excessive rounded containers, and color on every metric.

## Mobile app

**Audience and rhythm:** One-handed, interrupted use with a narrow viewport and platform expectations. Prioritize reachability, safe areas, large targets, and progressive disclosure.

**Primary shell:** App bar, scrollable content, bottom navigation or a focused task flow, sheets for secondary actions.

**Preview specimen:** Present a centered phone viewport plus a token/component catalog around or below it. Show at least one realistic screen and one interaction state such as a sheet, segmented control, composer, or confirmation.

**Core components:** App bar, bottom nav, lists, cards only where grouped content needs boundaries, sheets, inputs, toggles, empty/loading/offline states.

**Avoid:** Shrinking desktop tables, hover-only interactions, targets under 44px, and important controls outside thumb reach.

## Portal or content site

**Audience and rhythm:** Readers browse, search, orient, and compare content. Optimize hierarchy, wayfinding, readability, and content freshness.

**Primary shell:** Global header, category navigation, search, lead content, article/resource grid or index, footer taxonomy.

**Preview specimen:** Show a realistic portal home or index with lead story/resource, secondary rail, filters/categories, metadata, and reading states.

**Core components:** Header/search, breadcrumbs, content cards/list rows, metadata, tags, pagination, article typography, related content.

**Avoid:** Treating every section as a floating card, weak link differentiation, overly wide text measures, and image crops that hide the subject.

## Landing page

**Audience and rhythm:** Visitors must understand the literal offer, trust it, and act. Give the actual product or service immediate visual presence.

**Primary shell:** Concise navigation, full-width hero with real product/place/person imagery or an actual interactive product scene, proof, capabilities, comparison/details, CTA, footer.

**Preview specimen:** Show the landing experience rather than a component gallery in the first viewport; leave a visible hint of the next section. Keep the headline literal and put value propositions in supporting copy.

**Core components:** Navigation, primary/secondary CTA, proof strip, feature evidence, testimonial, pricing or conversion form, footer.

**Avoid:** Split hero cards, abstract gradient illustrations, vague slogan-only headlines, stock-like media, and endless card grids.

## AIGC product

**Audience and rhythm:** Users iterate between intent, generation, review, and refinement. The interface must make model state, cost, progress, provenance, and recoverability legible.

**Primary shell:** Workspace navigation, prompt/composer, configuration controls, generation canvas/results, history/versions, inspector.

**Preview specimen:** Show a working generation workspace with prompt input, model/mode selection, attached context, queued/generating/completed states, output preview, and revision/history controls.

**Core components:** Prompt composer, model selector, parameter controls, upload/context chips, generation state, result gallery/canvas, version history, safety/error notices.

**Avoid:** A chat bubble as the only interaction model, hiding cost or progress, irreversible regeneration, and decorative "AI" gradients without functional meaning.

## Large-screen dashboard

**Audience and rhythm:** Viewers scan from a distance, often without direct interaction, to detect changes and anomalies. Legibility and stable spatial memory beat component variety.

**Primary shell:** Persistent title/time/status band, KPI tier, dominant trend/geospatial/process view, ranked exceptions, system health/footer ticker.

**Preview specimen:** Use a fixed-ratio dashboard stage that scales within the browser without reordering its central story. Show realistic data, units, timestamps, thresholds, and alert severity.

**Core components:** KPI blocks, time-series and categorical charts, map/process topology where appropriate, alert rail, legend, last-updated/status indicators.

**Avoid:** Tiny labels, low-contrast hairlines, interaction-dependent meaning, too many chart types, continuous motion, and fluid reflow that destroys the intended composition.

## Cross-archetype selection test

Use the question "What does the user do repeatedly?" as the tie-breaker:

- Act on records: backend admin
- Complete a focused task in hand: mobile app
- Find and read: portal
- Understand and convert: landing page
- Prompt, generate, evaluate, refine: AIGC
- Monitor and detect: large-screen dashboard
