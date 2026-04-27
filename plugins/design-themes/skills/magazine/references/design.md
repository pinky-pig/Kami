# Design System · Guizang Magazine

## 设计宣言

这一版 Kami 的目标，不是继续做“纸本文稿”，而是把稳定的文档生产系统换成 **歸藏式电子杂志文档**：

**serif 大标题、sans 正文、mono 元信息、细规则线、深浅节奏、电子墨水反差。**

它不是网页 swipe deck 的逐页截图版，也不是把 deck 原样压扁到 A4 上。我们做的是：

- 保留 Kami 的模板驱动与稳定页数
- 把 `guizang-ppt-skill` 的视觉语法转译到文档与 PPTX

## V1 范围

- 正式迁移：中文 `one-pager`、`long-doc`、`letter`、`slides`
- 兼容保留：`resume`、`portfolio`、英文模板
- 参考源：`references/guizang-source/`

---

## 八条铁律

1. 保留 Kami 文档骨架，只替换视觉语言
2. 字体分工固定：serif = 标题；sans = 正文；mono = 元信息
3. 不默认接受任意色值，只从 5 套预设主题中挑选
4. 版式层级靠字号、字族、留白和规则线，不靠重装饰
5. 页眉与 kicker 语义必须分离，不能重复表述
6. 图片必须 top-safe，宁可裁底部，也别裁掉关键主体
7. 同一份文档要有明暗 / 强弱节奏，避免整份都一个语气
8. 输出优先级始终是：可读、稳定、可导出 PDF / PPTX

---

## 1. 主题预设

默认主题跟随 `references/themes.md`，建议把 `墨水经典` 作为默认。

### 默认 token

```css
--ink:        #0a0a0b;
--paper:      #f1efea;
--paper-tint: #e8e5de;
--ink-tint:   #18181a;
```

### 使用原则

- `ink` 不是单纯“黑色”，而是有一点温度的电子墨
- `paper` 不是纯白，而是偏暖的杂志纸感
- `paper-tint` 和 `ink-tint` 只用来做细层级，不抢正文

### 5 套主题的文档映射

| 主题 | 适用 |
|---|---|
| 墨水经典 | 通用默认、商业与产品类 |
| 靛蓝瓷 | 技术、AI、数据、研究报告 |
| 森林墨 | 文化、内容、行业观察 |
| 牛皮纸 | 历史、人文、叙事型文档 |
| 沙丘 | 品牌、作品集、设计类交付 |

---

## 2. 字体系统

### 角色划分

| 角色 | 用法 |
|---|---|
| Serif Display | 主标题、章节标题、引语、关键数字 |
| Sans Body | 正文、说明、信件主体、表格解释 |
| Mono Meta | 页眉、页脚、标签、页码、日期、短 metadata |

### 当前实现策略

为了兼容本仓库已有字体与 PDF 构建链路：

- display / body 统一使用 `"TsangerJinKai02", "Newsreader", "Source Serif 4", "Source Han Serif SC", "Noto Serif CJK SC", "Charter", Georgia, "Times New Roman", serif`
- mono 使用 `JetBrains Mono`
- 默认色彩模式为全黑色 Guizang；只有用户明确指定亮色时才生成亮色版本
- 不再使用 `KingHwa_OldSong`；Guizang 的字体信号来自 serif / sans / mono 的职责分工，而不是民国文稿式中文宋体

即使不是逐字复刻 `guizang-ppt-skill` 的字体文件，也必须复刻它的**字体职责分工**。

### 层级建议

| 角色 | 字号 |
|---|---|
| Hero / Cover 标题 | 28-40 pt |
| H1 | 20-26 pt |
| H2 | 14-18 pt |
| Lead | 11.5-13 pt |
| Body | 9.5-11 pt |
| Meta | 7.5-9 pt |

---

## 3. 版式语言

### 3.1 页眉页脚

Guizang 风格最稳定的信号之一是 **chrome / foot**：

- 顶部：栏目、阶段、页号、日期
- 底部：项目名、章节名、收束性标签

在文档模板里不必完全照搬横向 deck，但应保留：

- mono 小字
- uppercase / tracking
- 左右对位
- 细规则线

### 3.2 标题系统

- `kicker`：本页独有的钩子短句
- `headline`：真正主标题
- `lead`：一段比正文更大的引导文本

禁止：

- 页眉和 kicker 写同一句话
- 主标题像公文标题一样堆满 20 个字
- lead 写成模板废话

### 3.3 规则线

Guizang 感很大一部分来自**细规则线**。

规则：

- 用细线，不用厚黑框
- 用于 section 分隔、卡片起始线、页眉页脚秩序
- 线是结构，不是装饰

### 3.4 卡片与区块

适合 Guizang 风格的卡片是：

- 薄边 / 顶部分隔线
- 大数字 + 小标签
- 轻底色或纸色层级

不适合的是：

- 大圆角 SaaS 卡片
- 浮夸阴影
- 拟物纸张纹理堆叠

---

## 4. 文档类型映射

### One-Pager

- 页首必须有强标题和 metadata
- 适合 3-4 个数据卡 + 2-3 个正文区块
- 第一眼读到 headline，第二眼读到 metrics

### Long Doc

- 封面要像杂志专题扉页
- 章节之间需要明显节奏变化
- TOC / section opener / summary 都应有 editorial 感

### Letter

- 形式必须正式，但语气不必官样
- 主题栏、寄件信息、正文区三者应层级清楚
- 适合用 mono metadata 提升“编辑过”的感觉

### Resume

- 名字就是封面
- 联系方式与核心 metrics 用 mono + serif 对比
- 项目经历像专题条目，不像机械表格

### Portfolio

- 以封面、项目序号、大图和项目 metadata 为主
- 让“项目标题 + 类型 + 时间”成为统一重复语言

### Slides

- 直接继承 deck 的 cover / divider / numbers / quote / pipeline 节奏
- PPTX 应该是这个 theme 最像原始 Guizang skill 的输出面

---

## 5. 该避免什么

- 民国档案框
- 报纸剪报符号
- 厚边粗框
- 低质量渐变装饰
- 表面高级但信息层级混乱的空设计

一句话：**像一本被认真编辑过的杂志，而不是像一张被认真装饰过的海报。**
