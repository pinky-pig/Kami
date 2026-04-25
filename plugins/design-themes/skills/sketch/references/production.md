# Production

This theme uses the standard Kami generation path:

- HTML templates render to PDF through WeasyPrint.
- `slides.py` renders to PPTX through python-pptx.
- `scripts/build.py` verifies page count, fonts, token drift, and theme-specific structural rules.

## Build

```bash
python3 scripts/build.py --check
python3 scripts/build.py --verify one-pager
python3 scripts/build.py --verify long-doc
python3 scripts/build.py --verify letter
python3 scripts/build.py slides
```

## Sketch Rendering Notes

- Use handwritten fonts with explicit fallback.
- Use hard offset shadows instead of blur shadows.
- Use wobble radius values in CSS for HTML/PDF.
- PPTX cannot do the same wobble geometry exactly, so it should approximate the feel with rotations, thick outlines, tape, tacks, and note layering.
