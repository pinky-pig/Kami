# Design System · Newsprint

## 设计宣言

这一版 Kami 的目标是使用稳定生成能力，输出真正的 **新闻纸 / Newsprint** 文档系统。

**新闻纸底 / 黑色网格 / 头版标题 / 分栏导语 / 边栏事实盒 / 少量红色强调。**

这不是把 `prompts.md` 的网站设计原样搬进 PDF，而是把它转译成 A4、正式信件、长文和 PPTX 都能稳定输出的印刷版式。

## V1 范围

- 正式迁移：中文 `one-pager`、`long-doc`、`letter`、`slides`
- 继承：模板驱动、token 驱动、WeasyPrint 友好、构建校验
- 暂缓：把英文、简历、作品集完全重写成主风格

## 八条铁律

1. 只继承生产流程，不继承旧 manuscript 的版面结构和内容格式
2. 主风格信号必须一眼可见：新闻纸底 / 黑色网格 / 头版标题 / 分栏导语 / 边栏事实盒 / 少量红色强调
3. `prompts.md` 只作风格来源，不直接决定文档结构
4. 中文正文必须可读，装饰不能压过信息
5. Tag / 面板 / 图表底色使用实色 hex，避免 `rgba()`
6. PDF 输出优先，不能依赖 hover / motion 才成立
7. slides 和 HTML/PDF 使用同一组色彩语义
8. 不混入旧主题的深蓝档案外框、牌匾题签或档案卡片节奏

## 色彩系统

```css
--parchment:  #F9F9F7;
--ivory:      #FFFFFF;
--brand:      #111111;
--near-black: #111111;
--dark-warm:  #404040;
--charcoal:   #525252;
--olive:      #737373;
--stone:      #737373;
```

Additional implementation colors:

| Token | Hex | Role |
|---|---|---|
| frame | `#111111` | page frame / structural edge |
| rule | `#111111` | rules and borders |
| tag | `#111111` | tag backgrounds |
| accent | `#CC0000` | primary style accent |
| accent2 | `#E5E5E0` | secondary style accent |
| accent3 | `#F5F5F5` | tertiary style accent |

## 字体与层级

全局字体栈固定为 `"TsangerJinKai02", "Newsreader", "Source Serif 4", "Source Han Serif SC", "Noto Serif CJK SC", "Charter", Georgia, "Times New Roman", serif`。标题、正文、元信息都使用这套 serif 栈；黑色规则线比装饰更重要。

## 组件语言

- One-pager: treat the page as a front-page brief: masthead, deck, lede, four metrics, column story, editor's note
- Long-doc: treat each page as an article spread: section masthead, lede, two-column reading rhythm, sidebars, tables, pull quotes
- Letter: treat the letter as a correspondence column: title strip, sender block, subject deck, evidence sidebar, signature column
- Slides: use the same tokens as HTML, with newspaper-sheet frames, rule lines, data columns, and sidebar cards

## Avoid

圆角卡片、软阴影、渐变、玻璃效果、大面积彩色 UI.

## Feedback Vocabulary

When the user says "不对劲" or "不像", ask about: **栏线密度、头版标题强度、黑色规则线、纸纹强度、红色强调比例**.
