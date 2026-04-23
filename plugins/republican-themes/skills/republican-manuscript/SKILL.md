---
name: republican-manuscript
description: 'Typeset Chinese professional documents in a republican-manuscript style: one-pagers, white papers, project proposals, formal letters, recommendation letters, reference letters, and slide decks. Style 1 uses a deep archive-blue outer frame, padded old-paper sheet, blue bordered title plaques, serif-led hierarchy, and stable print spacing. Chinese output uses 京華老宋体 (KingHwa_OldSong) + Source Han; v1 does not officially support English styling. Auto-triggers from natural requests such as "帮我生成一份白皮书", "生成一份项目方案", "帮我写一份推荐信", "写一封推荐函", "做一套汇报 slides", "做 PDF", "排版", "生成报告", "一页纸", "正式信件", "高质量文档", "好看的排版", "民国风", "文稿风", "档案风", and when raw Chinese content is handed over to be typeset or made presentable.'
---

# kami · 紙

**紙 · かみ** - the paper your deliverables land on.

This fork turns kami into a **民国文稿版**: deep archive-blue outer frame, padded old-paper sheet, blue bordered title plaques, serif-led hierarchy, and restrained editorial rhythm.

Part of `Kaku · Waza · Kami` - Kaku writes code, Waza drills habits, **Kami delivers documents**.

## V1 scope

- Officially supported: Chinese `one-pager`, `long-doc`, `letter`, `slides`
- Visual standard: Style 1, `#243851` archive-blue frame + `#EBE5DD` old-paper base
- Pending migration: English styling, resume, portfolio

## Natural prompt entry

No slash command is needed. If the user says any of the following, route directly:

- "帮我生成一份白皮书" -> `long-doc`
- "生成一份项目方案" / "做一页项目方案" -> `one-pager`
- "帮我写一份推荐信" / "写一封推荐函" -> `letter`
- "做一套汇报 slides" / "生成一个 Slides" -> `slides`
- "帮我把这些内容排版成好看的 PDF" -> infer the closest of `one-pager`, `long-doc`, `letter`

## Step 1 · Decide the language

**Prefer Chinese output.** If the user writes in Chinese, use the Chinese templates and Chinese references. If they ask for English, explain that v1's visual standard is Chinese-first and only the legacy English templates remain.

When ambiguous (e.g. a one-word command like "resume"), ask a one-liner rather than guess.

| User language | Templates | References | Cheatsheet |
|---|---|---|---|
| Chinese (primary) | `one-pager.html` / `long-doc.html` / `letter.html` | `references/*.md` | `CHEATSHEET.md` |
| English (legacy) | `*-en.html` | `references/*.en.md` | `CHEATSHEET.en.md` |

## Step 2 · Pick the document type

| User says | Document | CN template |
|---|---|---|
| "one-pager / 方案 / 项目方案 / 执行摘要" | One-Pager | `one-pager.html` |
| "white paper / 白皮书 / 长文 / 年度总结" | Long Doc | `long-doc.html` |
| "formal letter / 信件 / 正式信件 / 推荐信 / 推荐函 / reference letter / recommendation letter / memo" | Letter | `letter.html` |
| "slides / slide deck / 汇报 slides / 演示稿 / PPT" | Slides | `slides.py` |

If the user asks for `resume / portfolio / English`, say those paths are still not the official v1 target of this fork.

If unsure, ask a one-liner about the scenario rather than guess.

### Diagrams (primitives, not a 7th doc type)

When the user asks for **a diagram inside** a long-doc / portfolio / slide (not a standalone document), route to `assets/diagrams/` rather than a template:

| User says | Diagram | Template |
|---|---|---|
| "架构图 / architecture / 系统图 / components diagram" | Architecture | `assets/diagrams/architecture.html` |
| "流程图 / flowchart / 决策流 / branching logic" | Flowchart | `assets/diagrams/flowchart.html` |
| "象限图 / quadrant / 优先级矩阵 / 2×2 matrix" | Quadrant | `assets/diagrams/quadrant.html` |

Read `references/diagrams.md` / `diagrams.en.md` before drawing - it has the selection guide, kami token map, and the AI-slop anti-pattern table. Extract the `<svg>` block from the template and drop it into a `<figure>` inside long-doc / portfolio.

Before drawing, always ask: **would a well-written paragraph teach the reader less than this diagram?** If no, don't draw.

## Step 2.5 · Distill raw content (if applicable)

Skip this step if the user already provides structured content (clear sections, bullet points, metrics in place).

When the user hands over **raw material** (meeting notes, brain dump, existing doc in different format, chat transcript, scattered points):

1. **Extract**: pull out every factual claim, number, date, name, and action item
2. **Classify**: map each extract to the target template's sections (see `references/writing.md` for section structure per doc type)
3. **Gap-check**: list what the template needs but the raw content doesn't have - present as a compact table
4. **Ask once**: share the gap table with the user. Do not guess to fill gaps.

Example gap-check:

| Template needs | Found | Missing |
|---|---|---|
| 4 metric cards | "8 years", "50-person team" | 2 more quantifiable results |
| 3-5 core projects | 2 mentioned | at least 1 more with outcome |

Then proceed to Step 3 with structured, distilled content.

---

## Step 3 · Load the right amount of spec

Pick the tier that matches the task. Default to the lowest tier that covers the work.

| Tier | When | Read |
|---|---|---|
| **Content-only** | Updating text, swapping bullets, tuning copy inside the migrated Chinese templates. CSS stays untouched. | `CHEATSHEET.md` only |
| **Layout tweak** | Adjusting spacing, moving sections, changing font size within spec. CSS touched. | `CHEATSHEET.md` + template (tokens already inline) |
| **New document** | Building from scratch or from raw content. | Full design spec + writing spec + template |
| **Troubleshoot** | Rendering bug, font issue, page overflow. | `production.md` (+ design spec if CSS is the cause) |
| **Diagram** | Embedding SVG in a doc. | `diagrams.md` only (has its own token map) |

You can always escalate mid-task if the work turns out to need more than the initial tier.

The full spec files for reference:
- Design: `references/design.md` (CN primary) / `references/design.en.md` (legacy EN)
- Writing: `references/writing.md` / `writing.en.md`
- Production: `references/production.md` / `production.en.md`
- Diagrams: `references/diagrams.md` / `diagrams.en.md`

## Step 4 · Fill content into the template

- Copy the template into your working directory; don't write HTML from scratch
- **CSS stays untouched**, only edit the body
- Content follows `writing.md` / `writing.en.md`: data over adjectives, distinctive phrasing over industry clichés
- For "推荐信 / 推荐函", use `letter.html`; structure the body as relationship -> evidence -> fit -> clear recommendation. Use the three evidence boxes for concrete achievements, not generic praise.

## Step 5 · Build & verify

```bash
python3 scripts/build.py --verify one-pager # verify content-filled Chinese demo
python3 scripts/build.py --verify long-doc
python3 scripts/build.py --verify letter
python3 scripts/build.py --check            # CSS rule violations only (fast, no build)
python3 scripts/build.py slides             # generate the republican-manuscript slide deck
```

`--verify` now prefers content-filled demo HTMLs for the migrated Chinese trio. Visual anomalies (tag double rectangle, font fallback, page break issues) -> `production.md` / `production.en.md` Part 4.

## Fonts

**Chinese**
- Main serif: 京華老宋体v2.002.ttf (user-provided; keep license aligned with the font source)
- Fallback chain baked into templates: Source Han Serif SC -> Noto Serif CJK SC -> Songti SC -> Georgia

**English**
- Main serif: Newsreader (Google Fonts, open source) - used for both headlines and body
- Sans: Inter (open source) - used for UI elements only (labels, eyebrows, meta)
- Fallback: Charter (macOS) / Georgia (cross-platform), Helvetica Neue / system-ui

Font files next to HTML and `@font-face` relative paths is the most stable setup.

## Feedback protocol

When the user gives **vague visual feedback** ("looks off", "不对劲", "spacing weird", "too cramped", "not elegant"):

Do not guess. Ask back using kami vocabulary, with current values included.

| User says | Ask about |
|---|---|
| "太挤了" / "too cramped" | Which element? Line-height (current: X)? Padding (current: Y)? Page margin? |
| "太松了" / "too loose" | Same direction, reversed |
| "颜色不对" / "color feels wrong" | Which element? Archive blue too heavy? Paper base too white? The gray too digital? |
| "不够好看" / "not polished" | Font rendering? Alignment? Whitespace distribution? Hierarchy unclear? |
| "看着不专业" / "unprofessional" | Content wording? Or layout (alignment, consistency)? |

Template response: "X is currently set to Y. Would you like (a) [specific alternative within spec] or (b) [another option]?"

Never say "I'll adjust the spacing" without naming the exact property and its new value.

---

## When not to use this skill

- User explicitly wants Material / Fluent / Tailwind default - different design language
- Need dark / cyberpunk / futurist aesthetic (this is deliberately anti-future)
- Need saturated multi-color (this has one accent)
- Need cartoon / animation / illustration style (this is editorial)
- Web dynamic app UI (this is for print / static documents)

---

Next: **apply Step 3's tier table to decide what to read**, then copy the matching template and start filling.
