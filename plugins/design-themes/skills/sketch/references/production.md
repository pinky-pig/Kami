# Production

This theme uses the standard Kami generation path:

- HTML templates render to PDF through WeasyPrint.
- `slides_spec.py` is the shared content source for both slide renderers.
- `slides.py` renders to PPTX through python-pptx.
- `assets/templates/slidev/render_from_spec.py` renders Slidev markdown for the online deck.
- `scripts/build.py` verifies page count, fonts, token drift, and theme-specific structural rules.

## Build

```bash
python3 scripts/build.py --check
python3 scripts/build.py --verify one-pager
python3 scripts/build.py --verify long-doc
python3 scripts/build.py --verify letter
python3 scripts/build.py slides
cd assets/templates/slidev && pnpm run dev
```

## Sketch Rendering Notes

- Use handwritten fonts with explicit fallback.
- Use hard offset shadows instead of blur shadows.
- Use wobble radius values in CSS for HTML/PDF.
- PPTX cannot do the same wobble geometry exactly, so it should approximate the feel with rotations, thick outlines, tape, tacks, and note layering.
- Slidev should mirror the same note-wall composition rather than falling back to a regular web page flow.

## Slidev Output

`python3 scripts/build.py slides` now generates two slide deliverables:

- `assets/examples/slides.pptx`
- `assets/examples/slides-online/`

The Slidev source lives in:

```text
assets/templates/
  slides_spec.py
  slides.py
  slidev/
    package.json
    render_from_spec.py
    slides.md
    style.css
```

`slides.md` is generated from `slides_spec.py`. Edit the spec first, not the generated markdown.
