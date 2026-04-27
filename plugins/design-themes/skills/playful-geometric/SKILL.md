---
name: playful-geometric
description: 'Typeset Chinese professional documents in a Playful Geometric document style: one-pagers, white papers, project proposals, formal letters, recommendation letters, reports, PDFs, HTML documents, and slide decks. Uses the Kami build pipeline, but the visible layout/content system must be prompt-native Playful Geometric: stable grid, primitive shapes, sticker cards, rounded bubbles, bright color rotation, pattern fills, and hard offset shadows. Auto-triggers from natural requests such as "用趣味几何风格", "Playful Geometric theme", "做 PDF", "生成报告", "一页纸", "白皮书", "推荐信", "项目方案", "做一套汇报 slides", and when raw Chinese content is handed over to be typeset in this theme.'
---

# Kami · Playful Geometric

Use this skill when the user wants a Chinese professional document rendered as **趣味几何 / Playful Geometric** instead of the Republican manuscript or newspaper styles.

This skill keeps only the production surface: HTML templates, WeasyPrint PDF output, PPTX generation, diagrams, fonts, build checks, and document routing. The visible result must not keep old frame/page composition. Playful Geometric output must use **稳定网格 / 几何贴纸 / primitive shapes / 明亮色彩 / 友好硬阴影**.

`slides` 现在是双产物路径：同一份 Playful Geometric 内容要同时交付 `assets/demos/demo-slides.pptx` 和 Slidev 在线 deck。

## V1 Scope

- Officially supported: Chinese `one-pager`, `long-doc`, `letter`, `slides`
- Visual standard: 把 Kami 文档输出变成友好、明亮、几何感强、有贴纸触感的现代文件。
- Important correction: this theme must keep playful black sticker borders, but must not inherit old frame systems. Use rounded sticker cards, speech bubbles, primitive shape decoration, and visible PDF color fills instead of nested outlines.
- Legacy retained: English, resume, and portfolio templates remain available but are not the primary target
- Original website prompt source: `prompts.md` is kept for reference; use `references/design.md` as the print-document spec

## Natural Prompt Entry

No slash command is needed. Route here when the user asks for this theme explicitly:

- "用趣味几何风格做一份项目方案" -> `one-pager`
- "把这份白皮书排成 Playful Geometric" -> `long-doc`
- "推荐信做成趣味几何风" -> `letter`
- "做一套 Playful Geometric slides" -> `slides`
- "帮我把这些内容排版成好看的 PDF" + mentions `playful-geometric` / `Playful Geometric` / `趣味几何` -> infer the closest doc type

## Step 1 · Decide Language

Prefer Chinese output. If the user writes in Chinese, use Chinese templates and Chinese references. If they ask for English, explain that v1 is Chinese-first and English templates are legacy-compatible.

| User language | Templates | References | Cheatsheet |
|---|---|---|
| Chinese (primary) | `one-pager.html` / `long-doc.html` / `letter.html` / `slides_spec.py` -> `slides.py` + `slidev` | `references/*.md` | `CHEATSHEET.md` |
| English (legacy) | `*-en.html` | `references/*.en.md` | `CHEATSHEET.en.md` |

## Step 2 · Pick Document Type

| User says | Document | CN template |
|---|---|---|
| "one-pager / 方案 / 项目方案 / 执行摘要" | One-Pager | `one-pager.html` |
| "white paper / 白皮书 / 长文 / 年度总结" | Long Doc | `long-doc.html` |
| "formal letter / 信件 / 推荐信 / 推荐函 / memo" | Letter | `letter.html` |
| "slides / slide deck / 汇报 slides / 演示稿 / PPT" | Slides | `slides_spec.py` -> `slides.py` + `assets/templates/slidev/render_from_spec.py` |

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
- Do not add extra nested boxes around content. Prefer sticker cards, floating bubbles, colored panels, and primitive shapes.
- Do not use dark title bars inside rounded cards. Section headers use pill labels, floating badges, or shape-backed headings.
- Use offset-border layers, not soft shadows: every featured panel should render as `black border + colored hard offset + black outer edge`, using crisp layered offsets that survive WeasyPrint PDF output.
- For HTML/PDF, implement offset borders with an actual wrapper (`outer offset shell` + inner `.sticker-face`). Do not rely on pseudo-elements or multi-layer `box-shadow` for core visual structure.
- Rewrite raw content into playful units: hero sticker, side bubble, metric chips, proof pops, checklist, action pop.
- Center metric cards, labels, short callouts, and PPT card titles; keep long paragraphs left-aligned.
- For PDF output, make sure panels have visible violet/pink/amber/mint fills, not only outlines.
- For PPT output, avoid dark outer frames and square bars inside rounded panels. Use rounded panels, one black sticker border, colored fills, and centered titles.
- Do not compress long content into one-pager. One-pager budget: 1 title, 1 subtitle, 3 metrics max, 2 evidence cards max, one short timeline or one short remark. If content exceeds that, route to `long-doc`.
- Follow `references/writing.md`: data over adjectives, specific evidence over generic praise
- For recommendation letters, use `letter.html` and structure the body as relationship -> evidence -> fit -> clear recommendation

## Step 5 · Build & Verify

```bash
python3 scripts/build.py --verify one-pager
python3 scripts/build.py --verify long-doc
python3 scripts/build.py --verify letter
python3 scripts/build.py slides
cd assets/templates/slidev && pnpm run dev
python3 scripts/build.py --check
```

`python3 scripts/build.py slides` 会先从 `slides_spec.py` 渲染 `assets/templates/slidev/slides.md`，再同时生成 `assets/demos/demo-slides.pptx` 和 `assets/demos/slides-online/`。不要手改 `slides.md`，它是生成物；预览脚本位于 `assets/demos/slides-online/` 内。

## Feedback Protocol

When the user gives vague visual feedback, ask back using this theme vocabulary: **几何装饰数量、圆角大小、彩色强调轮换、硬阴影颜色、内容网格稳定度**.

Template response: "当前 X 是 Y。要改成 (a) [specific Playful Geometric option] or (b) [specific quieter option]?"

## When Not To Use

- User asks for `republican-manuscript` or `republican-newspaper`
- User wants a dynamic web app UI rather than print/static documents
- User wants a different named design system that conflicts with Playful Geometric
- The requested visual direction depends on: 灰暗单色、过度商务、无表情极简、复杂装饰压住正文
