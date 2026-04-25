---
name: neo-brutalism
description: 'Typeset Chinese professional documents in a Neo-Brutalism document style: one-pagers, white papers, project proposals, formal letters, recommendation letters, reports, PDFs, HTML documents, and slide decks. Uses the Kami build pipeline, but the visible layout/content system must be prompt-native Neo-Brutalism: thick black strokes, high-saturation color blocking, hard ink shadows, rotated sticker layers, halftone/grid textures, and DIY zine composition. Auto-triggers from natural requests such as "用新粗野主义风格", "Neo-Brutalism theme", "做 PDF", "生成报告", "一页纸", "白皮书", "推荐信", "项目方案", "做一套汇报 slides", and when raw Chinese content is handed over to be typeset in this theme.'
---

# Kami · Neo-Brutalism

Use this skill when the user wants a Chinese professional document rendered as **新粗野主义 / Neo-Brutalism** rather than a quiet archival or editorial style.

This skill keeps only the production surface: HTML templates, WeasyPrint PDF output, PPTX generation, diagrams, fonts, build checks, and document routing. The visible result must not keep old frame/page composition. Neo-Brutalism output must use **黑色粗框 / 高饱和色块 / 硬阴影 / 贴纸拼贴 / DIY zine composition**.

## V1 Scope

- Officially supported: Chinese `one-pager`, `long-doc`, `letter`, `slides`
- Visual standard: 把 Kami 文档输出变成高对比、厚黑边、硬阴影、贴纸拼贴感的新粗野主义文件。
- Legacy retained: English, resume, and portfolio templates remain available but are not the primary target
- Original website prompt source: `prompts.md` is kept for reference; use `references/design.md` as the print-document spec

## Natural Prompt Entry

No slash command is needed. Route here when the user asks for this theme explicitly:

- "用新粗野主义风格做一份项目方案" -> `one-pager`
- "把这份白皮书排成 Neo-Brutalism" -> `long-doc`
- "推荐信做成新粗野主义风" -> `letter`
- "做一套 Neo-Brutalism slides" -> `slides`
- "帮我把这些内容排版成好看的 PDF" + mentions `neo-brutalism` / `Neo-Brutalism` / `新粗野主义` -> infer the closest doc type

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
- Rewrite raw content into neo-brutalist units: loud hero, marquee strip, rotated evidence cards, proof sticker, poster cover, blocky TOC, raw subject bar
- Follow `references/writing.md`: data over adjectives, specific evidence over generic praise
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

When the user gives vague visual feedback, ask back using this theme vocabulary: **边框厚度、硬阴影偏移、高饱和色块比例、贴纸旋转角度、黑白反差**.

Template response: "当前 X 是 Y。要改成 (a) [specific Neo-Brutalism option] or (b) [specific quieter option]?"

## When Not To Use

- User asks for a quiet archival or editorial theme
- User wants a dynamic web app UI rather than print/static documents
- User wants a different named design system that conflicts with Neo-Brutalism
- The requested visual direction depends on: 柔和阴影、玻璃拟态、细灰线、低对比 SaaS 卡片
