# AGENTS.md

This file defines **repo-level non-negotiable rules** for anyone creating or modifying themes in this repository.

## Core Rule

When creating a new theme, you may reuse **only the production method** from `plugins/republican-themes/skills/republican-manuscript`:

- directory scaffold
- build / verify pipeline
- file naming conventions
- output flow for HTML / PDF / PPTX / demos / examples

You may **not** reuse its visual architecture as the new theme itself.

## Absolutely Forbidden

It is strictly forbidden to create a "new theme" that is actually just `republican-manuscript` with different colors.

That includes:

- keeping the same page structure and only changing color tokens
- keeping the same layout rhythm and only changing borders/backgrounds
- keeping the same PPT slide composition and only changing palette
- keeping the same HTML component structure and only renaming the theme
- keeping the same typography hierarchy and only swapping accent colors
- keeping the same PDF composition and only replacing decorative details

If the result still visibly reads as `republican-manuscript`, the task is a failure.

## Required Interpretation

`republican-manuscript` is a **generation skeleton**, not a design reference.

For every new theme:

1. The **theme source reference** defines the visual system.
2. The scaffold only defines how files are organized and generated.
3. Layout, component structure, typography, spacing, page rhythm, and slide composition must be rebuilt to match the new theme.

## Theme Source Must Win

If the target theme is based on a source like `guizang-magazine`, then the generated outputs must follow that source theme across all deliverables:

- HTML templates
- PDF rendering
- PPTX slides
- demos
- examples

This means the following must be theme-native, not manuscript-native:

- layout system
- composition
- title treatment
- body text strategy
- metadata style
- component language
- section rhythm
- visual density
- spacing logic
- image treatment
- cover / chapter / quote / data-card patterns

## Definition Of Done For A New Theme

A new theme is only acceptable if:

- it is visually and structurally distinct from `republican-manuscript`
- it can be recognized as the target theme without being told its name
- its PPT, PDF, and HTML all share the new theme's own design language
- demos are also regenerated in the new theme rather than inherited from old ones

## If Unsure

If there is any doubt whether a change is "new theme" or merely "recolored manuscript", stop and treat it as incorrect.

Do not ship it.
