---
name: guizang-magazine
description: 'Typeset Chinese professional documents and slide decks in a Guizang-inspired editorial magazine style: one-pagers, white papers, project proposals, formal letters, recommendation letters, resumes, portfolios, PDFs, HTML documents, and PPTX slide decks. The production pipeline comes from Kami republican-manuscript, but the visual system is derived from op7418/guizang-ppt-skill: electronic magazine, electronic-ink contrast, serif display headlines, sans body copy, mono metadata, curated theme presets, and editorial rhythm. Auto-triggers from natural requests such as "用歸藏风格", "杂志风", "电子墨水风", "做 PDF", "生成报告", "做一页项目方案", "做一套汇报 slides", "做个简历", "做作品集", and when raw Chinese content is handed over to be typeset into a polished deliverable.'
---

# Kami · Guizang Magazine

Use this skill when the user wants a document or slide deck that feels like **电子杂志 × 电子墨水 × 编辑部版式**, rather than archive-blue manuscript or newspaper styling.

This skill keeps the **Kami production surface** intact:

- HTML templates for document types
- WeasyPrint PDF output
- PPTX generation through `slides.py`
- build / verify / token sync scripts

What changes is the entire visual language. The source style comes from [`op7418/guizang-ppt-skill`](https://github.com/op7418/guizang-ppt-skill):

- serif-led display hierarchy
- sans-serif body copy
- mono chrome / metadata
- curated theme presets instead of arbitrary hex colors
- editorial rhythm instead of bureaucratic framing

## V1 Scope

- Officially supported: Chinese `one-pager`, `long-doc`, `letter`, `slides`
- Compatibility retained: `resume`, `portfolio`, English templates, diagrams
- Visual target: **杂志页眉页脚 / 大标题 / 数据卡 / 细规则线 / 深浅节奏 / 电子墨水质感**
- Default color mode: **全黑色 Guizang**. Do not alternate black and light pages inside one PPT / HTML / PDF. Use light mode only when the user explicitly asks for it.

## Natural Prompt Entry

No slash command is needed. Route here when the user asks for this feel explicitly:

- "用歸藏风格做一份项目方案" -> `one-pager`
- "把这份白皮书排成杂志风" -> `long-doc`
- "推荐信做成电子墨水风" -> `letter`
- "做一套 Guizang 风格 slides" -> `slides`
- "帮我做个杂志风简历 / 作品集" -> `resume` / `portfolio`

If the request is simply "做个好看的 PDF / PPT", choose this skill when the desired tone is closer to:

- 杂志
- 演讲 deck
- 编辑部排版
- 电子墨水
- Monocle / Stripe Press 一类的克制 editorial

## Step 1 · Decide Document Type

| User says | Document | Template |
|---|---|---|
| "方案 / 一页纸 / 项目提案 / 执行摘要" | One-Pager | `one-pager.html` |
| "白皮书 / 长文 / 年度总结 / 研究报告" | Long Doc | `long-doc.html` |
| "正式信件 / 推荐信 / 推荐函 / memo" | Letter | `letter.html` |
| "简历 / resume / CV" | Resume | `resume.html` |
| "作品集 / portfolio / case study deck" | Portfolio | `portfolio.html` |
| "slides / PPT / 演示稿 / 汇报 deck" | Slides | `slides.py` |

## Step 2 · Pick A Theme Preset

Do **not** accept arbitrary hex values by default. Use the curated presets from [references/themes.md](/Users/wangwenbo/Desktop/demo/kami/plugins/guizang-themes/skills/guizang-magazine/references/themes.md):

1. `墨水经典`
2. `靛蓝瓷`
3. `森林墨`
4. `牛皮纸`
5. `沙丘`

Default to `墨水经典` unless the content clearly suggests another preset.

For document work, map them like this:

| Preset | Best for |
|---|---|
| 墨水经典 | 通用商业文档、默认方案、第一版 |
| 靛蓝瓷 | AI / 技术 / 数据 / 研究类 |
| 森林墨 | 内容、文化、非虚构、可持续 |
| 牛皮纸 | 人文、历史、阅读、叙事型简历 |
| 沙丘 | 设计、品牌、作品集、创意 deck |

## Step 3 · Load The Right Spec

| Tier | When | Read |
|---|---|---|
| Content-only | 只填正文，不动 CSS | `CHEATSHEET.md` |
| Layout tweak | 需要调版式 / 间距 / 栏目节奏 | `CHEATSHEET.md` + `references/design.md` |
| New document | 从零排一份 PDF / PPT / HTML | `references/design.md` + `references/writing.md` |
| Slide-specific | 做 PPTX / 理解杂志 deck 的节奏 | `references/components.md` + `references/layouts.md` + `references/themes.md` |
| Troubleshoot | 溢出、字体、断页、图片比例问题 | `references/production.md` + `references/checklist.md` |

Original Guizang source files are preserved under:

- `references/guizang-source/template.html`
- `references/guizang-source/components.md`
- `references/guizang-source/layouts.md`
- `references/guizang-source/themes.md`
- `references/guizang-source/checklist.md`

## Step 4 · Fill Content Into The Template

- Copy the closest template instead of writing HTML from scratch
- Keep the shared visual system consistent across HTML, PDF, and PPTX
- Respect the font split:
  - `"TsangerJinKai02", "Newsreader", "Source Serif 4", "Source Han Serif SC", "Noto Serif CJK SC", "Charter", Georgia, "Times New Roman", serif` for display, body, quotes, and key numbers
  - mono for metadata / labels / chrome
- Do not use `KingHwa_OldSong` / 京華老宋体 in this skill.
- Prefer editorial hierarchy over decorative panels

When filling content:

- Title should read like a magazine headline, not a bureaucracy heading
- Kicker and metadata should not repeat the same meaning
- Metrics should be short, scannable, and numerically explicit
- Use strong section rhythm: cover / evidence / transition / summary

## Step 5 · Build & Verify

```bash
python3 scripts/build.py one-pager
python3 scripts/build.py long-doc
python3 scripts/build.py letter
python3 scripts/build.py slides
python3 scripts/build.py --check
python3 scripts/build.py --verify
```

## Feedback Vocabulary

When the user gives vague visual feedback, ask back in Guizang vocabulary:

- **标题气压**: headline too weak / too loud
- **纸墨反差**: dark-mode ink contrast, not black/light page alternation
- **栏线密度**: rule line density
- **元信息存在感**: mono metadata too strong / too faint
- **章节节奏**: too many similar pages in a row
- **图片裁切**: top-safe / bottom-crop balance

## When Not To Use

- User explicitly wants republican manuscript / newspaper styling
- User wants high-saturation brutalism or playful geometric
- User needs dynamic web UI rather than printable/static output
- User wants arbitrary brand colors injected everywhere

Next: pick the document type, lock the preset, then fill the nearest template.
