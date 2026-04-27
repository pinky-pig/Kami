---
name: sketch
description: 'Typeset Chinese professional documents in a hand-drawn Sketch document style: one-pagers, white papers, project proposals, formal letters, reports, PDFs, HTML documents, and slide decks. Uses the Kami build pipeline, but the visible layout/content system must be prompt-native Sketch: warm paper background, wobbly borders, handwritten typography, hard offset shadows, tape and thumbtack details, note-card collage composition, and red/blue marker accents.'
---

# Kami · Sketch

Use this skill when the user wants a Chinese professional document rendered as **手绘草图 / Sketch / Hand-Drawn**.

This skill keeps only the production surface: HTML templates, WeasyPrint PDF output, PPTX generation, fonts, build checks, and document routing. The visible result must not become a neat modern editorial layout with just a different palette. Sketch output must feel like a wall of notes and napkin diagrams: **纸张纹理 / 手写字体 / wobble 边框 / 硬偏移阴影 / tape 与图钉 / 轻微旋转**.

`slides` 现在是双产物路径：同一份 Sketch 内容要同时交付 `slides.pptx` 和 Slidev 在线 deck。

## V1 Scope

- Officially supported: Chinese `one-pager`, `long-doc`, `letter`, `slides`
- Visual standard: 把 Kami 文档输出变成有纸感、有手写气、有草图协作感的文件。
- Original website prompt source: `prompts.md` is kept for reference; use `references/design.md` as the print-document spec

## Natural Prompt Entry

Route here when the user asks for this theme explicitly:

- "用手绘草图风格做一份项目方案" -> `one-pager`
- "把这份白皮书排成 sketch 风" -> `long-doc`
- "推荐信做成手绘 note 风" -> `letter`
- "做一套 sketch slides" -> `slides`
- "帮我把这些内容排版成好看的 PDF" + mentions `sketch` / `hand-drawn` / `手绘草图` -> infer the closest doc type

## Step 1 · Decide Language

Prefer Chinese output. If the user writes in Chinese, use Chinese templates and Chinese references.

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

## Step 4 · Fill Content Into The Template

- Copy the matching template into the working directory; do not write HTML from scratch
- Keep the theme CSS unless the user asks for a visual adjustment
- Use warm paper background, dotted grain, and note-board composition
- Use irregular border-radius values instead of clean geometric corners
- Use hard offset shadows only; never soft blur shadow
- Use handwritten / marker-feel typography, with Chinese handwritten fallback
- Use red correction-marker and blue ballpoint accents sparingly
- Rewrite raw content into sketch units: taped title card, thumbtack note, yellow sticky metric, dashed divider, checklist, proof notes
- Do not compress long content into one-pager. One-pager budget: 1 title, 1 subtitle, 3 metrics max, 2 content cards max
- Follow `references/writing.md`: concrete facts over generic enthusiasm

## Step 5 · Build & Verify

```bash
python3 scripts/build.py --verify one-pager
python3 scripts/build.py --verify long-doc
python3 scripts/build.py --verify letter
python3 scripts/build.py slides
cd assets/templates/slidev && pnpm run dev
python3 scripts/build.py --check
```

`python3 scripts/build.py slides` 会先从 `slides_spec.py` 渲染 `assets/templates/slidev/slides.md`，再同时生成 `assets/examples/slides.pptx` 和 `assets/examples/slides-online/`。不要手改 `slides.md`，它是生成物。

## Feedback Protocol

When the user gives vague visual feedback, ask back using this theme vocabulary: **手写感强度、纸张纹理、wobble 程度、贴纸数量、红蓝笔强调比例、版面倾斜感**.

## When Not To Use

- User asks for a polished corporate, archival, brutalist, or soft-ui theme
- User wants a dynamic web app UI rather than print/static documents
- The requested visual direction depends on: 完全对齐、干净直角、柔焦阴影、无纸感背景、严肃金融气质
