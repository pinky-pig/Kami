# Theme Production Contract

This document defines the shared production contract for all theme skills in this repository.

It complements [AGENTS.md](/Users/wangwenbo/Desktop/demo/kami/AGENTS.md): themes may reuse the production method from `republican-manuscript`, but they may not inherit its visual architecture.

## Purpose

The goal is to keep the generation surface stable across themes while allowing each theme to have its own visual system.

Stability here means:

- the same directory scaffold
- the same target names
- the same build and verify entry points
- the same artifact naming rules
- the same generated-vs-source boundaries

Variation here means:

- layout system
- component language
- typography
- spacing logic
- page rhythm
- slide composition
- image treatment
- theme references and tokens

## Scope

This contract applies to every skill under `plugins/*/skills/*`.

## 1. Directory Contract

Every theme skill should expose this base scaffold:

```text
<theme-skill>/
  SKILL.md
  README.md
  CHEATSHEET.md
  HANDOFF.md
  assets/
    templates/
    fonts/
    images/
    diagrams/           # optional if no diagram targets are implemented
    demos/
    examples/           # optional local build output for non-demo targets
  references/
  scripts/
```

Rules:

- `assets/templates/` stores editable source templates.
- `assets/demos/` is the canonical user-facing demo bundle.
- `assets/examples/` is allowed for local build outputs and compatibility targets, but it is not the canonical destination for the primary `slides` demo flow.
- Generated files must never replace source files except where generation is explicitly part of the contract, such as `assets/templates/slidev/slides.md`.

## 2. Target Contract

### Required core targets

Every theme must support these target names:

- `one-pager`
- `long-doc`
- `letter`
- `slides`

These four targets define the minimum shared production surface.

### Optional compatibility targets

Themes may additionally support these targets:

- `resume`
- `portfolio`
- `one-pager-en`
- `long-doc-en`
- `letter-en`
- `resume-en`
- `portfolio-en`
- `slides-en`
- `diagram-architecture`
- `diagram-flowchart`
- `diagram-quadrant`

Rules:

- Optional targets are allowed to be absent.
- If an optional target exists, it must use the shared target name and shared filename convention.
- A theme must not invent a different name for an equivalent shared target.

## 3. Template Contract

The editable source-of-truth files should follow this model:

- `assets/templates/one-pager.html`
- `assets/templates/long-doc.html`
- `assets/templates/letter.html`
- `assets/templates/slides_spec.py`
- `assets/templates/slides.py`
- `assets/templates/slidev/render_from_spec.py`
- `assets/templates/slidev/slides.md`

Rules:

- `slides_spec.py` is the single content source for the shared `slides` target.
- `slides.py` renders the PPTX output from that shared spec.
- `assets/templates/slidev/render_from_spec.py` renders Slidev markdown from that same spec.
- `assets/templates/slidev/slides.md` is generated output and must not be hand-edited.
- Theme-specific visuals must live in the editable templates and theme assets, not in post-build manual edits.

## 4. Build CLI Contract

Every theme must support these entry points in `scripts/build.py`:

```bash
python3 scripts/build.py
python3 scripts/build.py <target>
python3 scripts/build.py slides
python3 scripts/build.py --check
python3 scripts/build.py --sync
python3 scripts/build.py --verify
python3 scripts/build.py --verify <target>
```

Rules:

- `python3 scripts/build.py` builds all supported targets for that theme.
- `python3 scripts/build.py <target>` builds one supported target.
- `--check` scans production templates for contract violations.
- `--sync` checks token drift for the files declared as sync targets.
- `--verify` performs full verification for the theme's supported core targets.
- Extra theme-specific commands are allowed, but only as additive extensions. They must not replace the shared CLI.

Examples of acceptable additive commands:

- `--check-fonts`
- `--install-fonts`
- theme-specific demo generation helpers

## 5. Artifact Path Contract

### Core HTML/PDF outputs

For direct template builds, the default machine outputs may be written to `assets/examples/`.

Examples:

- `assets/examples/one-pager.pdf`
- `assets/examples/long-doc.pdf`
- `assets/examples/letter.pdf`

### Canonical demo outputs

The canonical user-facing demo bundle belongs under `assets/demos/`.

Required demo artifacts for the core surface:

- `assets/demos/demo-one-pager.html`
- `assets/demos/demo-one-pager.pdf`
- `assets/demos/demo-long-doc.html`
- `assets/demos/demo-long-doc.pdf`
- `assets/demos/demo-letter.html`
- `assets/demos/demo-letter.pdf`
- `assets/demos/demo-slides.pptx`
- `assets/demos/slides-online/`

Optional demo artifacts:

- `assets/demos/index.html`
- PNG previews
- theme-specific CSS or helper assets
- demo resume or portfolio artifacts

### Slides-specific contract

For the shared `slides` target, the canonical outputs are:

- `assets/demos/demo-slides.pptx`
- `assets/demos/slides-online/`
- `assets/demos/slides-online/slides-online-preview.py`
- `assets/demos/slides-online/slides-online-preview.command`

Rules:

- `slides` should not canonically emit to `assets/examples/slides.pptx`.
- `slides` should not canonically emit to `assets/examples/slides-online/`.
- Legacy `assets/examples/slides*` paths may be cleaned during migration, but they should not remain the documented final destination for the primary demo flow.

## 6. Verification Contract

Rules:

- `--verify` must cover the supported core targets.
- If content-filled demo HTML exists for a core target, verification should prefer that demo file over placeholder-heavy template source.
- `--verify slides` should be supported when slide-specific verification exists.
- Theme-specific validation is allowed, but it should hang off the shared verify surface rather than creating a separate incompatible verification story.

Recommended verify sources for the core trio:

- `assets/demos/demo-one-pager.html`
- `assets/demos/demo-long-doc.html`
- `assets/demos/demo-letter.html`

## 7. Demo Contract

Rules:

- Demos must be regenerated in the target theme's own design language.
- Demo content may differ by theme, but demo filenames and locations should stay stable.
- A theme may have extra demo-generation helpers, but the outputs must still land in the shared locations.
- Demo HTML, PDF, PPTX, and Slidev artifacts must read as one theme system, not mixed lineage.

## 8. Allowed Theme Variation

These may vary freely by theme:

- design tokens
- page grid and spacing system
- title and metadata treatment
- component set and section rhythm
- font stack
- image treatment
- slide layout language
- diagram rendering style
- content voice and supporting references

These may vary only additively:

- extra validation commands
- extra demo-generation scripts
- optional compatibility targets
- extra fonts and install helpers

These must not vary:

- core target names
- shared build entry points
- canonical demo path for the primary `slides` flow
- the fact that `slides_spec.py` is the shared source of truth
- the generated status of `slidev/slides.md`

## 9. Current Repo Deviations

As of 2026-04-28, the repo is not fully aligned to this target contract.

### Divergences that should be normalized

- `plugins/republican-themes/skills/republican-manuscript` still documents and emits the primary `slides` flow under `assets/examples/` instead of the canonical `assets/demos/` flow.
- `plugins/design-themes/skills/sketch` still documents and emits the primary `slides` flow under `assets/examples/`.
- `plugins/design-themes/skills/sketch` does not currently expose the broader compatibility surface used by several other themes, and it also lacks demo-backed verify sources for the core trio.

### Divergences that are acceptable only as additive extensions

- `plugins/republican-themes/skills/republican-newspaper` adds font-management and slide-font verification commands.
- `plugins/design-themes/skills/magazine` adds a separate `scripts/generate_demos.py` pipeline.

These extensions are acceptable only if they preserve the shared entry points and shared output locations.

## 10. Migration Checklist

When normalizing an existing theme, use this checklist:

1. Keep the theme's visual system intact; change only the production contract surface.
2. Move the canonical `slides` outputs to `assets/demos/demo-slides.pptx` and `assets/demos/slides-online/`.
3. Move Slidev preview helpers into `assets/demos/slides-online/`.
4. Ensure `slides_spec.py -> slides.py + slidev/render_from_spec.py` remains the only shared content path for slides.
5. Keep `python3 scripts/build.py --check`, `--sync`, and `--verify` working.
6. Add demo-backed verify sources for `one-pager`, `long-doc`, and `letter` when curated demos exist.
7. If a theme omits optional targets, document that omission explicitly in `README.md` and `SKILL.md`.
8. Regenerate demos after any path migration so the demo bundle and docs stay in sync.

## 11. Decision Rule

If a difference changes:

- target names
- output paths
- build entry points
- verify entry points
- source-of-truth files

then it is a production-contract divergence, not a theme difference.

If a difference changes:

- composition
- typography
- tokens
- spacing
- visual density
- deck layout
- page rhythm

then it is a theme difference and should remain theme-specific.
