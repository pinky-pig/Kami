# Design System · Playful Geometric

## 设计宣言

这一版 Kami 的目标是使用稳定生成能力，输出真正的 **趣味几何 / Playful Geometric** 文档系统。

**稳定网格 / 几何贴纸 / 明亮色彩 / 友好硬阴影。**

这不是把 `prompts.md` 的网站设计原样搬进 PDF，而是把它转译成 A4、正式信件、长文和 PPTX 都能稳定输出的印刷版式。

## V1 范围

- 正式迁移：中文 `one-pager`、`long-doc`、`letter`、`slides`
- 继承：模板驱动、token 驱动、WeasyPrint 友好、构建校验
- 暂缓：把英文、简历、作品集完全重写成主风格

## 十六条铁律

1. 保留 Kami 文档骨架，视觉层替换为 Playful Geometric
2. 主风格信号必须一眼可见：稳定网格 / 几何贴纸 / 明亮色彩 / 友好硬阴影
3. `prompts.md` 只作风格来源，不直接决定文档结构
4. 中文正文必须可读，装饰不能压过信息
5. Tag / 面板 / 图表底色使用实色 hex，避免 `rgba()`
6. PDF 输出优先，不能依赖 hover / motion 才成立
7. slides 和 HTML/PDF 使用同一组色彩语义
8. 不混入旧的民国文稿深蓝档案外框
9. 黑色边框是 Playful Geometric 的贴纸边，必须保留；但每个组件最多一层黑边
10. 不使用“外框套内框”的 manuscript 框页系统；页面只保留一个大圆角纸面和一层黑边
11. 内容块圆角统一在 16-18pt，标签/pill 才使用 999pt；不要混用直角、缺角和小圆角
12. 有色块或卡片里的标题、指标、标签必须居中；长正文可以左对齐
13. PDF 中的模块必须有可见色块填充，不能只靠黑线或浅灰边框表达结构
14. 禁止在圆角卡片里放 manuscript 式深色横条标题；`.section-head`、`.timeline-title`、`.compact-list .head`、`.subject-head` 等都必须是透明标题区 + 居中 yellow pill，不能用负 margin 把直角条贴到圆角边缘
15. 偏移边框是核心风格信号：主卡片黑边 + 右下彩色硬偏移 + 偏移层外侧黑边，PDF 中也必须可见
16. One-pager 不是压缩垃圾桶：默认最多 3 个指标、2 个内容卡、1 个 timeline 或 remark；超出信息量必须拆到 long-doc

## 色彩系统

```css
--parchment:  #FFFDF5;
--ivory:      #FFFFFF;
--brand:      #8B5CF6;
--near-black: #1E293B;
--dark-warm:  #334155;
--charcoal:   #475569;
--olive:      #64748B;
--stone:      #64748B;
```

Additional implementation colors:

| Token | Hex | Role |
|---|---|---|
| frame | `#1E293B` | page frame / structural edge |
| rule | `#1E293B` | rules and borders |
| tag | `#FBBF24` | tag backgrounds |
| accent | `#8B5CF6` | primary style accent |
| accent2 | `#F472B6` | secondary style accent |
| accent3 | `#34D399` | tertiary style accent |

## 字体与层级

内容网格要稳，装饰可以活；标题和卡片用圆润 sans，正文保持可读。

## 组件语言

- One-pager: make the first page carry the strongest theme signal
- Long-doc: repeat the frame/panel language per page without increasing page overflow risk
- Letter: keep the body formal; style lives in title treatment, evidence boxes, and signature block
- Slides: use the same tokens as HTML, with theme-specific cover/title and card treatments

### HTML / PDF rules

- Use one rounded paper surface; disable folio/sheet inner frame pseudo-elements.
- Use black borders as sticker edges, not archive frames. One component = one black border; no nested border inside the same component.
- Use crisp offset-border layers: black main border, colored hard offset, and a black edge around the offset layer. Do not use soft drop shadows.
- For HTML/PDF, implement the offset as actual nested DOM (`outer offset shell` + `.sticker-face`), not as pure pseudo-elements or multi-layer `box-shadow`; those are not stable enough in WeasyPrint.
- Prefer colored panels: violet, pink, amber, mint, and white.
- Use hard shadows as colored offsets, not as dark manuscript borders.
- Center text in metric cards, side cards, labels, table headers, and short callouts.
- Internal card headers are not dark rectangles. Keep them transparent and centered; use amber pill labels for English/kicker text.
- Keep long paragraphs left-aligned for reading.
- If a one-pager starts to need more than 3 metrics or 2 content cards, choose `long-doc` instead of shrinking font sizes or packing extra boxes.

### PPT rules

- Slides use cream backgrounds with geometric decorations; do not use a dark outer frame.
- All cards and title panels are rounded rectangles with one black border.
- Use violet/pink/amber/mint fills across slides, not mostly white panels.
- Do not use manuscript-style double borders, title plaques with inner rules, or archive labels.
- Do not place square dark bars inside rounded PPT cards; use a small rounded amber label or centered heading instead.

## Avoid

灰暗单色、过度商务、无表情极简、复杂装饰压住正文.

## Feedback Vocabulary

When the user says "不对劲" or "不像", ask about: **几何装饰数量、圆角大小、彩色强调轮换、硬阴影颜色、内容网格稳定度**.
