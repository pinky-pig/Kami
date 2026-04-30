---
name: republican-manuscript
description: 'Typeset Chinese professional documents in a republican-manuscript style: one-pagers, white papers, project proposals, formal letters, recommendation letters, reference letters, and slide decks. Style 1 uses a deep archive-blue outer frame, padded old-paper sheet, blue bordered title plaques, serif-led hierarchy, and stable print spacing. Chinese output uses 京華老宋体 (KingHwa_OldSong) + Source Han; v1 does not officially support English styling. Auto-triggers from natural requests such as "帮我生成一份白皮书", "生成一份项目方案", "帮我写一份推荐信", "写一封推荐函", "做一套汇报 slides", "做 PDF", "排版", "生成报告", "一页纸", "正式信件", "高质量文档", "好看的排版", "民国风", "文稿风", "档案风", and when raw Chinese content is handed over to be typeset or made presentable.'
---

# kami · 紙

**紙 · かみ** - the paper your deliverables land on.

This fork turns kami into a **民国文稿版**: deep archive-blue outer frame, padded old-paper sheet, blue bordered title plaques, serif-led hierarchy, and restrained editorial rhythm.

Part of `Kaku · Waza · Kami` - Kaku writes code, Waza drills habits, **Kami delivers documents**.

## V1 scope

- Officially supported: Chinese `one-pager`, `long-doc`, `letter`, `resume`, `portfolio`, `slides`
- `slides` is now a dual-output path: generate both `slides.pptx` and a Slidev online deck
- `slides_spec.py` is the single source of truth for slide content; `slides.py` and `slidev/render_from_spec.py` are renderers
- Visual standard: Style 1, `#243851` archive-blue frame + `#EBE5DD` old-paper base
- Typography contract: 京華老宋体 only serves Chinese display roles; Latin display falls back to Newsreader; readable body copy prefers `TsangerJinKai02-W04.ttf`, `Newsreader.woff2`, and `JetBrainsMono.woff2`
- Default visual-slot contract: image-heavy regions start as solid color placeholders; real images are optional, and chart-like content should prefer `assets/diagrams/*.html`
- Demo asset contract: generated mock images must land in `assets/demos/mock-assets/`; `assets/images/` is reserved for shared static theme assets
- `resume / portfolio` are **not a second visual system**. Their reference is `assets/demos/demo-long-doc.html`: inherit the same archive-blue outer frame, paper sheet, top tag, page number, and dossier rhythm; only the content blocks get reorganized for career / case-study use.
- Pending migration: English styling

## Natural prompt entry

No slash command is needed. If the user says any of the following, route directly:

- "帮我生成一份白皮书" -> `long-doc`
- "生成一份项目方案" / "做一页项目方案" -> `one-pager`
- "帮我写一份推荐信" / "写一封推荐函" -> `letter`
- "帮我排一份简历" / "生成简历" -> `resume`
- "帮我做作品集" / "生成 portfolio" -> `portfolio`
- "做一套汇报 slides" / "生成一个 Slides" -> `slides`
- "帮我把这些内容排版成好看的 PDF" -> infer the closest of `one-pager`, `long-doc`, `letter`, `resume`, `portfolio`

## Step 1 · Decide the language

**Prefer Chinese output.** If the user writes in Chinese, use the Chinese templates and Chinese references. If they ask for English, explain that v1's visual standard is Chinese-first and only the legacy English templates remain.

When ambiguous (e.g. a one-word command like "resume"), ask a one-liner rather than guess.

| User language | Templates | References | Cheatsheet |
|---|---|---|---|
| Chinese (primary) | `one-pager.html` / `long-doc.html` / `letter.html` / `resume.html` / `portfolio.html` | `references/*.md` | `CHEATSHEET.md` |
| English (legacy) | `*-en.html` | `references/*.en.md` | `CHEATSHEET.en.md` |

## Step 2 · Pick the document type

| User says | Document | CN template |
|---|---|---|
| "one-pager / 方案 / 项目方案 / 执行摘要" | One-Pager | `one-pager.html` |
| "white paper / 白皮书 / 长文 / 年度总结" | Long Doc | `long-doc.html` |
| "formal letter / 信件 / 正式信件 / 推荐信 / 推荐函 / reference letter / recommendation letter / memo" | Letter | `letter.html` |
| "resume / 简历 / 履历 / CV" | Resume | `resume.html` |
| "portfolio / 作品集 / 案例集 / 项目集" | Portfolio | `portfolio.html` |
| "slides / slide deck / 汇报 slides / 演示稿 / PPT" | Slides | `slides_spec.py` -> `slides.py` + `assets/templates/slidev/render_from_spec.py` |

For `resume / portfolio`, always treat `assets/demos/demo-long-doc.html` as the visual reference. They are dossier variants, not standalone magazine / web / SaaS layouts.

If the user asks for English, explain that v1's visual standard is Chinese-first and only the legacy English templates remain.

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
- 图片位默认保留纯色占位，不把“模型必须会生图”当前提。只有用户明确提供图片，或明确要求生成图片时，再把占位替换成 `<img>`。
- 只要视觉位本质上是在表达关系、流程、优先级，而不是摄影内容，就优先走 `assets/diagrams/` 里的 architecture / flowchart / quadrant，再考虑截图或插画。
- For "推荐信 / 推荐函", use `letter.html`; structure the body as relationship -> evidence -> fit -> clear recommendation. Use the three evidence boxes for concrete achievements, not generic praise.
- For `resume / portfolio`, keep the `demo-long-doc.html` chrome: archive-blue frame, paper sheet, dossier top tag, bottom-right page mark, and archival pacing. Rebuild section content as needed, but do not flatten them into a plain cream page with only a palette swap.
- For `slides`, edit `slides_spec.py` first. `slides.py` owns the `.pptx`, `assets/templates/slidev/render_from_spec.py` turns the same schema into `slides.md`, and Slidev builds the online deck from that generated markdown.

## Step 5 · Build & verify

```bash
python3 scripts/build.py --verify one-pager # verify content-filled Chinese demo
python3 scripts/build.py --verify long-doc
python3 scripts/build.py --verify letter
python3 scripts/build.py --verify resume
python3 scripts/build.py --verify portfolio
python3 scripts/build.py --check            # CSS rule violations only (fast, no build)
python3 scripts/build.py slides             # render slides.md from slides_spec.py + generate demo-slides.pptx + assets/demos/slides-online/
cd assets/templates/slidev && pnpm run dev  # local presenter / online preview at http://localhost:3030
```

`python3 scripts/build.py slides` 还会先从 `slides_spec.py` 渲染出 `assets/templates/slidev/slides.md`，然后再生成 `assets/demos/demo-slides.pptx` 和 Slidev 在线版 `assets/demos/slides-online/`。不要手改 `slides.md`，它是生成物。构建完成后还会额外在 `assets/demos/slides-online/` 内生成 `slides-online-preview.py` 和 `slides-online-preview.command`。如果要在本地浏览器里看构建后的静态 deck，用这两个入口之一；不要直接双击 `assets/demos/slides-online/index.html`，Chrome 下会因为 `file://` 的模块加载限制白屏。

如果需要生成 portfolio / slides 的 mock 图片、演示图片或临时视觉素材，一律写到 `assets/demos/mock-assets/`，并在重生成前清理该目录。不要把生成产物写回 `assets/images/`。
即使是 demo 生成脚本，`portfolio` 默认也必须保留纯色占位和 `assets/diagrams/` 视觉位；不要为了“更好看”就在首页或项目页自动塞大图。真实 `<img>` 只能在用户明确提供图片，或明确要求展示图片能力时再启用。

`--verify` now prefers content-filled demo HTMLs for the migrated Chinese trio. Visual anomalies (tag double rectangle, font fallback, page break issues) -> `production.md` / `production.en.md` Part 4.

## Fonts

**Chinese**
- Display serif: 京華老宋体v2.002.ttf (user-provided; only for large Chinese display roles)
- Readable body / UI: TsangerJinKai02-W04.ttf
- Fallback chain baked into templates: Source Han Serif SC -> Noto Serif CJK SC -> Songti SC -> Georgia

**Latin / English**
- Display + readable copy: Newsreader (Google Fonts, open source)
- Mono / route labels / page marks: JetBrains Mono
- Do not treat Inter as the manuscript default UI font anymore; hierarchy should be solved with scale, spacing, and case first

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
