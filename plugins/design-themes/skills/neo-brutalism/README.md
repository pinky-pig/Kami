# Kami · Neo-Brutalism

A Kami document theme for **新粗野主义 / Neo-Brutalism** output.

It is a full copy of the `republican-manuscript` document production pipeline with a different visual system: HTML templates, WeasyPrint PDF generation, PPTX slides, diagrams, examples, fonts, and validation scripts are all present.

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
