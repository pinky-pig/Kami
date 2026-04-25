# Kami · Guizang Magazine

A Kami document theme for **歸藏杂志风 / 电子墨水风** output.

This skill is built from the `republican-manuscript` production scaffold, but the style system is re-authored from [`op7418/guizang-ppt-skill`](https://github.com/op7418/guizang-ppt-skill):

- magazine-style hierarchy
- electronic-ink contrast
- serif display + sans body + mono metadata
- curated theme presets
- editorial rhythm across HTML / PDF / PPTX

## Supports

- Chinese one-pager: `assets/templates/one-pager.html`
- Chinese long document / white paper: `assets/templates/long-doc.html`
- Chinese formal letter / recommendation letter: `assets/templates/letter.html`
- Chinese slide deck: `assets/templates/slides.py`
- Compatibility templates: `resume`, `portfolio`, English variants

## Visual Target

把 Kami 文档输出变成一套像歸藏 deck 延展出来的文档系统，而不是只会做横向 PPT。

Theme signal:

- **杂志页眉页脚**
- **大标题 + 小 kicker**
- **mono 元信息**
- **细规则线**
- **深浅节奏**
- **电子墨水质感**

## Source Of Truth

Original Guizang PPT references are preserved here:

- `references/guizang-source/template.html`
- `references/guizang-source/components.md`
- `references/guizang-source/layouts.md`
- `references/guizang-source/themes.md`
- `references/guizang-source/checklist.md`

For day-to-day document production, load:

- `SKILL.md`
- `CHEATSHEET.md`
- `references/design.md`
- `references/themes.md`

## Build

```bash
python3 scripts/build.py one-pager
python3 scripts/build.py long-doc
python3 scripts/build.py letter
python3 scripts/build.py slides
python3 scripts/build.py --check
python3 scripts/build.py --verify
```

## Theme Presets

Default preset is `墨水经典`. Other supported presets:

1. `靛蓝瓷`
2. `森林墨`
3. `牛皮纸`
4. `沙丘`

The goal is to keep the Guizang aesthetic intact, so arbitrary freehand color mixing is discouraged.
