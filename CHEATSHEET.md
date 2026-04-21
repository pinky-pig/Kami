# kami · 民国文稿风格速查

一页纸速查。填模板、调细节前先看这里。完整规范在 `references/design.md`。

## V1 范围

- 正式支持：中文 `one-pager`、`long-doc`、`letter`
- 风格目标：深蓝外框、旧纸内页、明显 padding、蓝色题签、档案式边框
- 暂不主推：英文模板、简历、作品集、slides

## 八条铁律

1. 页面是 `#243851` 深蓝外框 + `#EBE5DD` 旧纸内页，不用纯白
2. 强调色只有档案蓝 `#243851`
3. 中性灰偏纸本暖灰，不用现代 SaaS 冷灰
4. 中文 serif 统一使用京華老宋体，sans 仍只承担标签、元信息等功能文字
5. Serif 字重固定 500，不用 bold
6. 行距：标题 1.1-1.3 / 密排 1.4-1.45 / 阅读 1.5-1.55
7. Tag 背景必须实色 hex，禁 `rgba()`
8. 装饰只做蓝色题签、双线内框、档案边框，不做高拟物海报

## 自然语言触发

| 用户说 | 路由 |
|---|---|
| 帮我生成一份白皮书 | `long-doc.html` |
| 生成一份项目方案 / 做一页项目方案 | `one-pager.html` |
| 帮我写一份推荐信 / 写一封推荐函 | `letter.html` |
| 帮我把这些内容排版成好看的 PDF | 先判断 `one-pager` / `long-doc` / `letter` |

## 色板

| 角色 | Hex | 用途 |
|---|---|---|
| Parchment | `#EBE5DD` | 旧纸内页 |
| Ivory | `#F3EFEB` | 浮层浅纸 |
| Border | `#D0C7BB` | 分隔线 / 边框 |
| Border Soft | `#DDD5CB` | 更淡的表格线 / 次分隔 |
| **Brand** | **`#243851`** | **外框、标题牌、强调数字、题签** |
| Brand Light | `#4D5B6D` | 双线细边 / 次强调 |
| Near Black | `#232222` | 主文字 |
| Dark Warm | `#4A4947` | 次级正文 |
| Charcoal | `#5A5856` | 表格表头 / 较重正文 |
| Olive | `#666361` | 说明、导语、副文本 |
| Stone | `#8B8782` | 日期、元信息 |
| Seal Red | `#B6675E` | 预留色，v1 默认不用 |

## Tag 实色

| 档位 | Hex | 用途 |
|---|---|---|
| 淡 | `#E4E9EE` | 极弱标注 |
| 中 | `#DCE3EA` | 轻标签 |
| 默认 | `#D5DEE7` | 默认 tag |
| 强 | `#CFD8E2` | 多标签并排时加区分 |
| 深 | `#C3CDD8` | 需要更强反差时 |

## 字号（印刷品 pt）

| 角色 | 字号 | 字重 | line-height |
|---|---|---|---|
| Display | 34-40 | 500 | 1.10 |
| H1 | 20-24 | 500 | 1.20 |
| H2 | 14-16 | 500 | 1.25 |
| H3 | 12-13 | 500 | 1.30 |
| Body Lead | 11-12 | 400 | 1.55 |
| Body | 9.5-10.5 | 400 | 1.55 |
| Body Dense | 9-9.2 | 400 | 1.40 |
| Caption | 8.5-9 | 400 | 1.45 |
| Label | 7.5-8 | 600 | 1.35 |

## 间距（4pt 基）

| 级 | 值 | 用途 |
|---|---|---|
| xs | 2-3 pt | 同行内 |
| sm | 4-5 pt | tag padding |
| md | 8-10 pt | 组件内部 |
| lg | 16-20 pt | 组件之间 |
| xl | 24-32 pt | section 标题 margin |
| 2xl | 40-60 pt | 大 section 之间 |

## 页面边距（A4）

| 文档 | 上右下左 |
|---|---|
| One-Pager | `@page margin: 0`，深蓝外框；内页约 10.5mm 外 padding + 13mm 内容 padding |
| Long Doc | `@page margin: 0`，每页深蓝外框；内页约 10.5mm 外 padding + 13mm 内容 padding |
| Letter | `@page margin: 0`，深蓝外框；内页约 11mm 外 padding + 15mm 内容 padding |

## 常用 CSS 片段

### 风格 1 框页

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

### Tag

```css
.tag {
  background: #D5DEE7;
  color: var(--brand);
  font-size: 8pt;
  font-weight: 500;
  padding: 1pt 5pt;
  border-radius: 3pt;
}
```

### 引文 / 旁注

```css
.quote {
  position: relative;
  border-left: 1.2pt solid var(--brand);
  padding: 4pt 0 4pt 16pt;
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

### 框题 / 信息块

```css
.panel {
  background: var(--ivory);
  border: 0.4pt solid var(--border);
  border-radius: 2pt;
  padding: 10pt 14pt;
}
```

## 决策速查

| 想做 | 怎么做 |
|---|---|
| 大标题 | serif 500，必要时两行，靠字号不靠粗体 |
| 章节开始 | 蓝色题签 / 档案框 + 大留白 |
| 强调数字 | `color: var(--brand)`，不要粗体 |
| 分隔内容 | `0.45pt` 纸灰分隔线，别用粗黑线 |
| 引用 / 旁注 | 左双线，不用大色块 |
| 信息块 | 浅纸底 + 深蓝边框 |
| 中文正文 | serif 或 sans 跟模板既有规则走，别混杂太多样式 |
| 装饰 | 最多一处“题签感”，别扩散到整页 |

不在表里，就回到一句话：**版式骨架沿用 kami，时代气质交给深蓝外框、旧纸内页和档案题签。**
