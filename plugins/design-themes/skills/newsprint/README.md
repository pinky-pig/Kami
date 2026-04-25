# Kami · Newsprint

A Kami document theme for **新闻纸 / Newsprint** output.

It uses the stable Kami document production pipeline, but the visible output is a native Newsprint system: newspaper sheet, masthead, column grid, lede, sidebar facts, black rules, and sparse red editorial marks.

## Supports

- Chinese one-pager: `assets/templates/one-pager.html`
- Chinese long document / white paper: `assets/templates/long-doc.html`
- Chinese formal letter / recommendation letter: `assets/templates/letter.html`
- Chinese slide deck: `assets/templates/slides.py`

## Visual Target

把 Kami 文档输出变成高密度、强网格、严肃可信的新闻纸 / 出版物版面。

Theme signal: **新闻纸底 / 黑色网格 / 出版物层级 / 少量红色强调**.

## Build

```bash
python3 scripts/build.py --verify one-pager
python3 scripts/build.py --verify long-doc
python3 scripts/build.py --verify letter
python3 scripts/build.py slides
python3 scripts/build.py --check
```

`prompts.md` is kept as the original web-design prompt source. For document production, load `SKILL.md`, `CHEATSHEET.md`, and `references/design.md`.
