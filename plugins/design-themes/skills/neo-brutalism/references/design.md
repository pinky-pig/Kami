# Design System · Neo-Brutalism

## 设计宣言

这一版 Kami 的目标是把原 `republican-manuscript` 的稳定文档能力换成 **新粗野主义 / Neo-Brutalism** 视觉系统。

**黑色粗框 / 高饱和色块 / 硬阴影 / 贴纸拼贴。**

这不是把 `prompts.md` 的网站设计原样搬进 PDF，而是把它转译成 A4、正式信件、长文和 PPTX 都能稳定输出的印刷版式。

## V1 范围

- 正式迁移：中文 `one-pager`、`long-doc`、`letter`、`slides`
- 继承：模板驱动、token 驱动、WeasyPrint 友好、构建校验
- 暂缓：把英文、简历、作品集完全重写成主风格

## 八条铁律

1. 保留 Kami 文档骨架，视觉层替换为 Neo-Brutalism
2. 主风格信号必须一眼可见：黑色粗框 / 高饱和色块 / 硬阴影 / 贴纸拼贴
3. `prompts.md` 只作风格来源，不直接决定文档结构
4. 中文正文必须可读，装饰不能压过信息
5. Tag / 面板 / 图表底色使用实色 hex，避免 `rgba()`
6. PDF 输出优先，不能依赖 hover / motion 才成立
7. slides 和 HTML/PDF 使用同一组色彩语义
8. 不混入旧的民国文稿深蓝档案外框

## 色彩系统

```css
--parchment:  #FFFDF5;
--ivory:      #FFFFFF;
--brand:      #000000;
--near-black: #000000;
--dark-warm:  #000000;
--charcoal:   #171717;
--olive:      #1F1F1F;
--stone:      #000000;
```

Additional implementation colors:

| Token | Hex | Role |
|---|---|---|
| frame | `#000000` | page frame / structural edge |
| rule | `#000000` | rules and borders |
| tag | `#FFD93D` | tag backgrounds |
| accent | `#FF6B6B` | primary style accent |
| accent2 | `#FFD93D` | secondary style accent |
| accent3 | `#C4B5FD` | tertiary style accent |

## 字体与层级

中文默认用重字重 sans，标题和数字尽量粗；保留 KingHwa 字体文件只是为了兼容旧模板。

## 组件语言

- One-pager: make the first page carry the strongest theme signal
- Long-doc: repeat the frame/panel language per page without increasing page overflow risk
- Letter: keep the body formal; style lives in title treatment, evidence boxes, and signature block
- Slides: use the same tokens as HTML, with theme-specific cover/title and card treatments

## Avoid

柔和阴影、玻璃拟态、细灰线、低对比 SaaS 卡片.

## Feedback Vocabulary

When the user says "不对劲" or "不像", ask about: **边框厚度、硬阴影偏移、高饱和色块比例、贴纸旋转角度、黑白反差**.
