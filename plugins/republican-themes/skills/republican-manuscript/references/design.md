# Design System

## 设计宣言

这一版 kami 的目标，不再是“现代 editorial 的暖米纸”，而是**民国文稿感**：

**深蓝外框、旧纸内页、明显 padding、档案蓝题签、克制留白。**

它仍然继承原版 kami 的优势：固定模板、清晰层级、稳定页数和 WeasyPrint 友好的实现方式。变化只发生在视觉语言层，不改变“模板驱动 + token 驱动 + 构建校验”的核心方法。

这不是报纸复刻，也不是海报拟物。它更像一份经过整理的馆藏文稿或机构档案：安静、节制、可靠。

## V1 范围

- 正式迁移：中文 `one-pager`、`long-doc`、`letter`
- 沿用：现有字体策略、模板骨架、页数校验
- 暂缓：英文主题化、竖排正文、印章贴图、纹理图片、重装饰元素

---

## 八条铁律

1. 页面使用深蓝外框 `#243851` 包住旧纸内页 `#EBE5DD`，不用纯白
2. 全文唯一主强调色是档案蓝 `#243851`
3. 中性灰保持纸本暖灰倾向，拒绝现代冷蓝灰
4. 仍保留 serif 主导的标题秩序，中文 serif 统一使用京華老宋体
5. Serif 字重固定 500，不用粗黑体
6. 行距延续原版：标题 1.1-1.3，正文 1.4-1.55
7. Tag 和边框使用实色，不用 `rgba()`
8. 装饰仅限蓝色题签、双线内框、档案边框，不做大面积拟物

---

## 1. 色彩系统

### 主调 · Brand

```css
--brand:       #243851;  /* 档案蓝 */
--brand-light: #4D5B6D;  /* 细双线 / 次强调 */
--seal-red:    #B6675E;  /* 预留色，v1 默认不用 */
```

**使用规则**：

- `--brand` 是全文唯一高彩色，也是外框和题签主色
- Style 1 允许页外框和题签使用大面积蓝色，但正文区仍保持克制
- `--brand-light` 只用于第二道细线、题签边、次级分隔
- `--seal-red` 仅作为未来扩展位，不放进默认模板正文

### 画布 · Paper

```css
--parchment:   #EBE5DD;  /* 旧纸底 */
--ivory:       #F3EFEB;  /* 浅纸浮层 */
--border:      #D0C7BB;  /* 主边框 */
--border-soft: #DDD5CB;  /* 次边框 */
```

设计重点不是把纸做旧，而是把底色调到“像保存良好的旧纸”。因此：

- 不用纹理图片
- 不用噪点遮罩
- 不做发黄过重的拟物脏污
- 只靠底色、细线和留白制造时代感

### 文字色

```css
--near-black: #232222;  /* 主文字 */
--dark-warm:  #4A4947;  /* 次级正文 */
--charcoal:   #5A5856;  /* 表格、密集正文 */
--olive:      #666361;  /* 导语、说明 */
--stone:      #8B8782;  /* 日期、元信息 */
```

规则只有一条：**像纸上的墨，不像屏幕上的灰。**

### Tag 实色

Tag 继续沿用“实色替代半透明”原则。v1 推荐：

| 档位 | Hex |
|---|---|
| 淡 | `#E4E9EE` |
| 中 | `#DCE3EA` |
| 默认 | `#D5DEE7` |
| 强 | `#CFD8E2` |
| 深 | `#C3CDD8` |

禁止：

```css
background: rgba(36, 56, 81, 0.18);
```

---

## 2. 字体系统

### 字体栈

v1 不增加任何字体依赖，继续使用原 repo 字体：

```css
/* 中文 serif */
"KingHwa_OldSong", "Source Han Serif SC", "Noto Serif CJK SC", "Songti SC", Georgia, serif;

/* 中文 sans / UI */
"Source Han Sans SC", "Noto Sans CJK SC", "PingFang SC", Arial, sans-serif;

/* 英文 serif / mono */
"Newsreader", Georgia, serif;
"JetBrains Mono", Consolas, monospace;
```

### 字重与层级

| 角色 | 字号 | 字重 | line-height |
|---|---|---|---|
| Display | 34-40 pt | 500 | 1.10 |
| H1 | 20-24 pt | 500 | 1.20 |
| H2 | 14-16 pt | 500 | 1.25 |
| H3 | 12-13 pt | 500 | 1.30 |
| Body Lead | 11-12 pt | 400 | 1.55 |
| Body | 9.5-10.5 pt | 400 | 1.55 |
| Body Dense | 9-9.2 pt | 400 | 1.40 |
| Caption | 8.5-9 pt | 400 | 1.45 |
| Label | 7.5-8 pt | 600 | 1.35 |

原则不变：

- 靠字号制造存在感，不靠 bold
- 目录、眉题、时间标签可以更疏朗
- 正文不要过度模拟旧报刊字距

---

## 3. 间距与版式

### 基础单位

依然以 `4pt` 为基础节奏：

| 尺度 | 值 | 用途 |
|---|---|---|
| xs | 2-3 pt | 行内微调 |
| sm | 4-5 pt | tag、注记 |
| md | 8-10 pt | 组件内部 |
| lg | 16-20 pt | 组件之间 |
| xl | 24-32 pt | section 标题前后 |
| 2xl | 40-60 pt | 大 section 之间 |

### Style 1 页面框架

Style 1 不再依赖 `@page margin` 营造边距，而是用深蓝画布承载纸张：

| 文档类型 | 外框 | 内页 |
|---|---|---|
| One-Pager | `@page margin: 0`，body padding 约 `10.5mm` | `.folio` padding 约 `13mm`，内容必须 1 页 |
| Long Doc | 每页一个 `.folio`，body/folio 外框约 `10.5mm` | `.sheet` padding 约 `13-14mm`，每页都有内双线 |
| Letter | `@page margin: 0`，body padding 约 `11mm` | `.folio` padding 约 `15mm`，正文装入档案框 |

### 版式原则

- 保留 kami 原有骨架，不重写信息结构
- 民国感来自细节，不来自大幅改版
- 每页允许一套统一框页装饰：深蓝外框、内双线、蓝色题签
- 段落、表格、指标卡仍以现代清晰性为先

---

## 4. 组件语言

### 框页系统

最重要的新视觉信号。适用于所有已迁移中文模板：

```css
@page {
  size: A4;
  margin: 0;
  background: var(--brand);
}

body {
  width: 210mm;
  min-height: 297mm;
  padding: 10.5mm;
  background: var(--brand);
}

.folio {
  position: relative;
  min-height: 276mm;
  padding: 13mm;
  background: linear-gradient(135deg, #F6F1E8 0%, var(--parchment) 48%, #EFE5D8 100%);
}
```

### 蓝色题签

适用于：

- 页首 header
- 章节标题
- 信件主题栏

```css
.title-plaque {
  position: relative;
  background: var(--brand);
  color: var(--ivory);
  padding: 12pt 14pt;
}

.title-plaque::after {
  content: "";
  position: absolute;
  inset: 8pt;
  border: 0.45pt solid #D5DEE7;
}
```

### 引文 / 旁注

保留左侧竖线结构，但改为双线：

```css
.quote {
  position: relative;
  border-left: 1.2pt solid var(--brand);
  padding-left: 16pt;
  color: var(--olive);
}

.quote::before {
  content: "";
  position: absolute;
  left: 4pt;
  top: 0;
  bottom: 0;
  width: 0.35pt;
  background: var(--brand-light);
}
```

### 信息块

```css
.panel {
  background: var(--ivory);
  border: 1pt solid var(--brand);
  padding: 10pt 14pt;
}
```

不使用：

- 大圆角卡片
- 厚重阴影
- 与档案蓝无关的彩色填充

### 表格

- 表头可使用档案蓝反白，正文行保持浅纸底
- 主分隔线用 `--brand`
- 行间线用 `--border-soft` 或暖纸灰
- 不要引入第二套高饱和色

### Tag

继续小而克制，不要变成 UI badge：

```css
.tag {
  background: #D5DEE7;
  color: var(--brand);
  font-size: 8pt;
  font-weight: 500;
  padding: 1pt 6pt;
  border-radius: 3pt;
}
```

---

## 5. 文档类型建议

### One-Pager

- 最适合体现“深蓝外框 + 蓝色题签”
- 指标卡改为清晰边框卡，但仍保持单页密度
- 时间线和引语区使用档案框，不做贴图装饰

### Long Doc

- 封面使用深蓝标题牌 + 右侧档案卡
- 目录和章节页每页都有统一框页系统
- 摘要块、注释块用浅纸底 + 深蓝边框

### Letter

- 支持正式信件、推荐信、推荐函
- 信头使用蓝色函件题签 + 右侧寄件人卡
- 保持首行缩进与正文节奏
- 推荐信用三格 evidence box 写具体事实，避免空泛称赞

---

## 6. 生产约束

### 必须继续遵守

- `@page background` 与页面背景同色
- 不在 tag / border 上使用 `rgba()`
- 不改变字体依赖与相对路径
- 不打破 one-pager / letter 的页数约束

### 不做的事

- 不加入纹理图片
- 不做竖排正文
- 不做章印贴图
- 不把每个组件都做成“复古道具”

---

## 7. 一句话判断标准

如果一页看起来像“被认真整理过的机构文稿”，它就是对的。

如果它更像海报、杂志封面、婚礼请柬或复古滤镜，它就偏了。
