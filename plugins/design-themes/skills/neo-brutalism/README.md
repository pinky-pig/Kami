# Kami · Neo-Brutalism

A Kami document theme for **新粗野主义 / Neo-Brutalism** output.

It uses the stable Kami document production pipeline, but the visible output is a prompt-native Neo-Brutalism system: thick black strokes, high-saturation color blocking, hard ink shadows, rotated sticker layers, halftone/grid textures, and DIY zine composition.

## Supports

- Chinese one-pager: `assets/templates/one-pager.html`
- Chinese long document / white paper: `assets/templates/long-doc.html`
- Chinese formal letter / recommendation letter: `assets/templates/letter.html`
- Chinese slide deck: `assets/templates/slides.py`

## Visual Target

把 Kami 文档输出变成高对比、厚黑边、硬阴影、贴纸拼贴感的新粗野主义文件。

Theme signal: **黑色粗框 / 高饱和色块 / 硬阴影 / 贴纸拼贴**.

## Build

```bash
python3 scripts/build.py --verify one-pager
python3 scripts/build.py --verify long-doc
python3 scripts/build.py --verify letter
python3 scripts/build.py slides
python3 scripts/build.py --check
```

`prompts.md` is kept as the original web-design prompt source. For document production, load `SKILL.md`, `CHEATSHEET.md`, and `references/design.md`.
