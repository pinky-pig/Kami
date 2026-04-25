---
name: newsprint
description: 'Typeset Chinese professional documents in a Newsprint document style: one-pagers, white papers, project proposals, formal letters, recommendation letters, reports, PDFs, HTML documents, and slide decks. Uses the Kami build pipeline, but the layout/content system must be native Newsprint: newspaper sheet, masthead, column grid, deck/lede, sidebar facts, data columns, black rules, and sparse red editorial marks. Auto-triggers from natural requests such as "用新闻纸风格", "Newsprint theme", "做 PDF", "生成报告", "一页纸", "白皮书", "推荐信", "项目方案", "做一套汇报 slides", and when raw Chinese content is handed over to be typeset in this theme.'
---

# Kami · Newsprint

Use this skill when the user wants a Chinese professional document rendered as **新闻纸 / Newsprint** instead of the Republican manuscript or newspaper styles.

This skill keeps only the production surface from the old manuscript pipeline: HTML templates, WeasyPrint PDF output, PPTX generation, diagrams, fonts, build checks, and document routing. The visible result must not keep manuscript composition. Newsprint output must use **新闻纸底 / 黑色网格 / 头版标题 / 分栏导语 / 边栏事实盒 / 少量红色强调**.

## V1 Scope

- Officially supported: Chinese `one-pager`, `long-doc`, `letter`, `slides`
- Visual standard: 把 Kami 文档输出变成高密度、强网格、严肃可信的新闻纸 / 出版物版面
- Legacy retained: English, resume, and portfolio templates are compatibility assets only; do not choose them as default Newsprint output
- Original website prompt source: `prompts.md` is kept for reference; use `references/design.md` as the print-document spec

## Natural Prompt Entry

No slash command is needed. Route here when the user asks for this theme explicitly:

- "用新闻纸风格做一份项目方案" -> `one-pager`
- "把这份白皮书排成 Newsprint" -> `long-doc`
- "推荐信做成新闻纸风" -> `letter`
- "做一套 Newsprint slides" -> `slides`
- "帮我把这些内容排版成好看的 PDF" + mentions `newsprint` / `Newsprint` / `新闻纸` -> infer the closest doc type

## Step 1 · Decide Language

Prefer Chinese output. If the user writes in Chinese, use Chinese templates and Chinese references. If they ask for English, explain that v1 is Chinese-first and English templates are legacy-compatible.

| User language | Templates | References | Cheatsheet |
|---|---|---|
| Chinese (primary) | `one-pager.html` / `long-doc.html` / `letter.html` / `slides.py` | `references/*.md` | `CHEATSHEET.md` |
| English (legacy) | `*-en.html` | `references/*.en.md` | `CHEATSHEET.en.md` |

## Step 2 · Pick Document Type

| User says | Document | CN template |
|---|---|---|
| "one-pager / 方案 / 项目方案 / 执行摘要" | One-Pager | `one-pager.html` |
| "white paper / 白皮书 / 长文 / 年度总结" | Long Doc | `long-doc.html` |
| "formal letter / 信件 / 推荐信 / 推荐函 / memo" | Letter | `letter.html` |
| "slides / slide deck / 汇报 slides / 演示稿 / PPT" | Slides | `slides.py` |

## Step 3 · Load The Right Spec

| Tier | When | Read |
|---|---|---|
| Content-only | Filling existing template text. CSS untouched. | `CHEATSHEET.md` |
| Layout tweak | Adjusting spacing, section order, or visual density. | `CHEATSHEET.md` + template |
| New document | Building from raw content or from scratch. | `references/design.md` + `references/writing.md` + template |
| Troubleshoot | Rendering bug, font issue, page overflow. | `references/production.md` |
| Diagram | Embedding a diagram inside a doc. | `references/diagrams.md` |

## Step 4 · Fill Content Into The Template

- Copy the matching template into the working directory; do not write HTML from scratch
- Keep the theme CSS unless the user asks for a visual adjustment
- Follow `references/writing.md`: data over adjectives, specific evidence over generic praise
- Rewrite raw content into Newsprint units: masthead, deck, lede, column story, sidebar fact box, data column, editor's note
- For recommendation letters, use `letter.html` and structure the body as relationship -> evidence -> fit -> clear recommendation

## Step 5 · Build & Verify

```bash
python3 scripts/build.py --verify one-pager
python3 scripts/build.py --verify long-doc
python3 scripts/build.py --verify letter
python3 scripts/build.py slides
python3 scripts/build.py --check
```

## Feedback Protocol

When the user gives vague visual feedback, ask back using this theme vocabulary: **栏线密度、头版标题强度、黑色规则线、纸纹强度、红色强调比例**.

Template response: "当前 X 是 Y。要改成 (a) [specific Newsprint option] or (b) [specific quieter option]?"

## When Not To Use

- User asks for `republican-manuscript` or `republican-newspaper`
- User wants a dynamic web app UI rather than print/static documents
- User wants a different named design system that conflicts with Newsprint
- The requested visual direction depends on: 圆角卡片、软阴影、渐变、玻璃效果、大面积彩色 UI
