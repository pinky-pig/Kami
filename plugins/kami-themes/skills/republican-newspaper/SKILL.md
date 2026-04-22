---
name: republican-newspaper
description: 'Typeset Chinese professional documents in a Republican-era newspaper and special-issue style: old newspaper front pages, special editions, one-pagers, white papers, project proposals, letters, recommendation letters, reports, and slide decks. Uses cream newsprint, dense column grids, black ink rules, vertical mastheads, reverse black labels, grayscale photos, clipping frames, datelines, postal marks, and a restrained red seal accent. Auto-triggers from natural requests such as "做成民国报纸风", "旧报纸风", "报纸特刊", "号外", "新闻版", "家书特刊", "燕京时报", "战时报纸", "铅印报纸", "民国风排版", "帮我把内容排成报纸", and when raw Chinese content is handed over to be made into a newspaper-like PDF or deck.'
---

# Kami · 民国报纸

Use this skill when the user wants a Chinese document to feel like a **民国报纸 / 报纸特刊 / 旧报刊剪报** rather than a modern report.

The visual target comes from `assets/reference-images/style-2-*.{jpg,png}`: cream newsprint, black ink, vertical mastheads, dense columns, clipping boxes, grayscale photos, postal marks, and one red seal as the only strong color.

## V1 Scope

- Officially supported: Chinese `one-pager`, `long-doc`, `letter`, `slides`
- Visual standard: Style 2, old newspaper / special issue
- Pending migration: English styling, resume, portfolio

## Natural Prompt Entry

No slash command is needed. If the user asks for any of these, route here:

- "做成民国报纸风" / "旧报纸风" -> infer document type
- "生成一份报纸特刊" / "做一版号外" -> `one-pager`
- "做一份项目新闻版 / 项目特刊" -> `one-pager` or `long-doc`
- "帮我把这份白皮书排成旧报纸" -> `long-doc`
- "写一封家书特刊 / 推荐信做成报纸风" -> `letter`
- "做一套民国报纸风 slides" -> `slides`

## Step 1 · Decide Language

Prefer Chinese output. If the user writes in Chinese, use Chinese templates and Chinese references. If they ask for English, explain that v1 is Chinese-first and English templates remain legacy.

| User language | Templates | References | Cheatsheet |
|---|---|---|---|
| Chinese (primary) | `one-pager.html` / `long-doc.html` / `letter.html` / `slides.py` | `references/*.md` | `CHEATSHEET.md` |
| English (legacy) | `*-en.html` | `references/*.en.md` | `CHEATSHEET.en.md` |

## Step 2 · Pick Document Type

| User says | Document | CN template | Newspaper interpretation |
|---|---|---|---|
| "号外 / 特刊 / 一版报纸 / 项目新闻版" | One-Pager | `one-pager.html` | single front page |
| "白皮书 / 长文 / 年度总结 / 深度报道" | Long Doc | `long-doc.html` | multi-page special issue |
| "家书 / 正式信件 / 推荐信 / 推荐函" | Letter | `letter.html` | letter clipping / correspondence special |
| "slides / 汇报 slides / 演示稿" | Slides | `slides.py` | editorial slide deck |

If unsure, ask one concise question about the use case instead of guessing.

## Step 3 · Load The Right Spec

Pick the lowest tier that covers the work.

| Tier | When | Read |
|---|---|---|
| Content-only | Filling existing template text. CSS untouched. | `CHEATSHEET.md` |
| Layout tweak | Adjusting spacing, columns, frames, vertical labels. | `CHEATSHEET.md` + template |
| New document | Building from raw content or from scratch. | `references/design.md` + `references/writing.md` + template |
| Troubleshoot | Rendering bug, font issue, page overflow. | `references/production.md` |
| Diagram | Embedding a diagram inside a doc. | `references/diagrams.md` |

Reference images are in `assets/reference-images/`; use them only for visual orientation, not as pasted decoration.

## Step 4 · Newspaper Distillation

When raw material is loose notes, turn it into newspaper structure before filling the template:

1. **Masthead**: 4-8 Chinese characters, e.g. `家书特刊`, `项目号外`, `燕京时报`
2. **Dateline**: date, place, issue identity
3. **Lead story**: the one thing the reader must remember
4. **Sidebars**: 2-4 evidence boxes, quotes, timelines, figures
5. **Visual evidence**: grayscale photo, clipping frame, envelope/stamp motif, or simple diagram
6. **Closing rail**: action, recommendation, or next step

Do not invent facts for "news flavor". The newspaper style is a layout voice, not permission to fabricate.

## Step 5 · Visual Rules

- Use cream newsprint, not pure white
- Use black ink and warm grays; no archive blue
- One red seal is allowed; do not add more accent colors
- Prefer thin black frames, double rules, reverse black labels, vertical headline strips
- Dense columns are welcome, but readability wins over imitation
- Photos must be grayscale / low-contrast, not colorful hero imagery
- Avoid modern cards, rounded SaaS panels, gradients, glass effects, and oversized whitespace

## Step 6 · Build & Verify

PPTX fonts are configured in `assets/fonts/fonts.json`. Do not duplicate font family names inside scripts; read this config before checking, installing, or patching slide font slots.

```bash
python3 scripts/build.py --verify one-pager
python3 scripts/build.py --verify long-doc
python3 scripts/build.py --verify letter
python3 scripts/build.py --check-fonts
python3 scripts/build.py --verify slides
python3 scripts/build.py --check
```

If running from the repo root:

```bash
python3 plugins/kami-themes/skills/republican-newspaper/scripts/build.py --check
```

## Feedback Protocol

When the user says "不够报纸", "太现代", "太空", or "不像民国", ask using newspaper vocabulary:

| User says | Ask about |
|---|---|
| "不够报纸" | masthead strength, column density, black rule weight, vertical title strips |
| "太现代" | rounded corners, whitespace, modern cards, colored accents |
| "太挤" | body column width, line-height, sidebar density |
| "太旧/太脏" | paper tone, photo contrast, texture strength |

Template response: "当前 X 是 Y。要改成 (a) [specific newspaper option] or (b) [specific quieter option]?"

## When Not To Use

- User wants clean modern SaaS / Material / Tailwind default
- User wants the calmer archive manuscript look; use `republican-manuscript`
- User needs full-color magazine, poster, cartoon, cyberpunk, or heavily illustrated style
- User needs a dynamic web app UI rather than print/static documents
