# Handoff · Newsprint

This theme keeps the stable document production workflow, but its visual and content system must stay native to `newsprint`.

## Included

- `SKILL.md`: runtime routing and build workflow
- `CHEATSHEET.md`: quick visual rules
- `references/design.md`: print-document theme spec
- `references/writing.md`: copied Kami writing workflow
- `references/production.md`: copied production/debugging notes
- `assets/templates/`: HTML and PPTX source templates
- `scripts/build.py`: build, verify, sync, and CSS checks
- `prompts.md`: original website-oriented prompt source, kept for traceability

## Maintenance

When changing theme colors, update `references/tokens.json`, the `:root` tokens in `one-pager.html` / `long-doc.html` / `letter.html`, and color constants in `slides.py`.
