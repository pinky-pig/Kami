# Kami · Playful Geometric

A Kami document theme for **趣味几何 / Playful Geometric** output.

It uses the stable Kami document production pipeline, but the visible output is a prompt-native Playful Geometric system: stable grid, primitive shapes, sticker cards, rounded bubbles, bright color rotation, pattern fills, and hard offset shadows.

## Supports

- Chinese one-pager: `assets/templates/one-pager.html`
- Chinese long document / white paper: `assets/templates/long-doc.html`
- Chinese formal letter / recommendation letter: `assets/templates/letter.html`
- Chinese slide deck: `assets/templates/slides.py`

## Visual Target

把 Kami 文档输出变成友好、明亮、几何感强、有贴纸触感的现代文件。

Theme signal: **稳定网格 / 几何贴纸 / 明亮色彩 / 友好硬阴影**.

## Build

```bash
python3 scripts/build.py --verify one-pager
python3 scripts/build.py --verify long-doc
python3 scripts/build.py --verify letter
python3 scripts/build.py slides
python3 scripts/build.py --check
```

`prompts.md` is kept as the original web-design prompt source. For document production, load `SKILL.md`, `CHEATSHEET.md`, and `references/design.md`.
