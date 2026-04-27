# 质量检查清单（Checklist）

这个清单来自"一人公司"分享 PPT 的真实迭代过程。每一条都是踩过坑之后总结的，按重要性排序。

生成 PPT 前，先通读一遍；生成后，逐项自检。

---

## 🔴 P0 · 一定不能犯的错

### 0. 生成前必须通过的类名校验(最重要)

**现象**：直接把 layouts.md 的骨架粘到新 HTML,结果样式全部丢失——大标题变成非衬线、数据大字报字体小得像正文、pipeline 多页糊成一坨、图片堆到浏览器底部。

**根因**：如果 `template.html` 的 `<style>` 里没有这些类的定义,浏览器就 fallback 到默认样式。

**做法**：
- **生成 PPT 前,必须先 `Read` `assets/template.html`**,确认 layouts.md 里用到的类都已定义
- 最常见遗漏的类:`h-hero / h-xl / h-sub / h-md / lead / meta-row / stat-card / stat-label / stat-nb / stat-unit / stat-note / pipeline-section / pipeline-label / pipeline / step / step-nb / step-title / step-desc / grid-2-7-5 / grid-2-6-6 / grid-2-8-4 / grid-3-3 / frame / img-cap / callout-src`
- 如果某个类确实缺了,**在 template.html 的 `<style>` 里补上**,不要在每页 inline 重写
- 生成后打开浏览器,如果看到"大标题是非衬线"或"pipeline 步骤挤在一行",几乎 100% 是这个问题

### 1. 不要用 emoji 作图标

**现象**：在中式杂志风格里用 emoji（🎯 💡 ✅）会立刻破坏格调。

**做法**：用 Lucide 图标库，CDN 方式引用：

```html
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
...
<i data-lucide="target" class="ico-md"></i>
...
<script>lucide.createIcons();</script>
```

常用图标名：`target / palette / search-check / compass / share-2 / crown / check-circle / x-circle / plus / arrow-right / grid-2x2 / network`

### 2. 图片只允许裁底部，左右和顶部绝对不能切

**现象**：用 `aspect-ratio` 撑图，网格会在父容器不足时堆叠或切掉图片关键信息（比如截图上部的标题栏）。

**做法**：图片容器用**固定 height + overflow hidden**，图片走 `object-fit:cover + object-position:top`：

```html
<figure class="frame-img" style="height:26vh">
  <img src="screenshot.png">
</figure>
```

CSS 里 `.frame-img img` 已经预设 `object-position:top`，只裁底。

**绝不用这种写法**（会在网格中撑破容器）：

```html
<!-- 坏例 -->
<figure class="frame-img" style="aspect-ratio: 16/9">...</figure>
```

**例外**：单张主视觉（非网格内）可以用 `aspect-ratio + max-height`，因为父容器会兜底。

### 2b. 默认输出必须保持单一黑色模式

**现象**:PPT / HTML / PDF 一页黑色、一页亮色,像在用颜色切换硬造节奏。

**根因**:沿用了原始 deck 的 light / dark 交替规划。这个 skill 的生产输出现在默认走稳定黑色主题,节奏应来自标题尺度、留白、规则线、组件密度和页面结构。

**做法**:
- 默认只使用 `dark` / `hero dark`
- 不要在同一份产物中穿插 `light` 页
- 如果用户明确要求亮色,必须做成全亮模式,不能黑白混排

### 2b-2. 全黑色也要有节奏

**现象**:所有页面虽然都是黑色,但字号、密度和组件完全一样,读起来像连续表格。

**根因**:把“主题节奏”误解成颜色切换,没有用 Guizang 的 editorial 结构做起伏。

**做法**:
- **生成前画"版式节奏表"**:标出 cover / stat / body / divider / quote / close,而不是标颜色
- **硬规则**:连续 3 页不能使用同一种内容密度;8 页 deck 至少有 cover、正文密集页、转场页、收束页
- **生成后自检**:`grep 'class="slide' index.html`,确认默认输出没有 `light`

### 2c. chrome 和 kicker 不要写同一句话

**现象**:左上角 `.chrome` 写"Design First · 设计先行",同一页里 `.kicker` 又写"Phase 01 · 设计阶段"——同义翻译,AI 味浓。

**做法**:
- **chrome = 杂志页眉 / 导航标签**:跨多页可相同(如 "Act II · Workflow"、"Data · Result"、"lukew.com · 2026.04")
- **kicker = 本页独一份的引导句**:短、有钩子、是大标题的"小前缀"(如 "BUT"、"一个人,做了什么。"、"The Question")
- 一个描述栏目,一个描述这一页——绝不互相翻译

### 3. 大标题字号不能超过屏宽 / 单字数

**现象**：中文大标题字号设太大（比如 13vw），结果每行只容 1 个字，强制换行非常难看。

**做法**：
- `h-hero`（最大）：10vw，**且标题长度 ≤ 5 字**
- `h-xl`（次大）：6vw-7vw
- 长标题用 `<br>` 手工断行，不要依赖自动换行
- 必要时加 `white-space:nowrap`

**示例**：`我不是程序员。`（6 字）用 `h-xl` 7.2vw + nowrap，一行排完。

### 4. 字体分工：标题衬线、正文非衬线

**做法**：
- 大标题、重点 quote、数字大字 → **TsangerJinKai02 + Newsreader serif stack**
- 正文、描述、pipeline 步骤名 → **TsangerJinKai02 + Newsreader serif stack**
- 元数据、代码、标签 → **JetBrains Mono**

不要使用 `KingHwa_OldSong` / 京華老宋体；那会把 Guizang 输出拉回 manuscript 气质。

### 4b. 图片不要用 `align-self:end` 贴底

**现象**：左文右图布局里,为了让右列图片和左列 callout 底部对齐,在 `<figure>` 上加 `align-self:end`。结果:
- 如果父容器不是 grid(比如类名没定义),`align-self` 完全失效,图片掉到文档流最下面被浏览器底栏遮挡
- 即使是 grid,图片会在 cell 里贴底,低分屏上仍然被 `.foot` 和 `#nav` 圆点遮挡

**做法**:
- 图文混排**必须用 `.frame.grid-2-7-5`**(或 `.grid-2-6-6`/`.grid-2-8-4`)
- 右列 `<figure class="frame-img">` 用 **标准比例 16/10 或 4/3 + max-height:56vh**,自然贴顶即可
- 要让左列 callout 看起来"贴底",给**左列**加 flex column + `justify-content:space-between`,不要动右列

### 4c. 图片不要用原图奇葩比例

**现象**:`aspect-ratio: 2592/1798` 这种从原图复制的比例,在不同屏幕下撑出奇怪的空白或溢出。

**做法**:无论原图什么比例,占位器固定用标准比例 **16/10 / 4/3 / 3/2 / 1/1 / 16/9**。图片自动 `object-fit:cover + object-position:top`,顶部不裁,底部裁掉一点无伤大雅。

### 5. 不要给图片加厚边框 / 阴影

**现象**：为了"高级感"加了强阴影或黑框，瞬间变成商务 PPT。

**做法**：最多 1-4px 的微圆角 + **极淡的底噪**（已在模板里）。不要加 `box-shadow`，不要加 `border`（除非 1px 极淡的灰）。

---

## 🟡 P1 · 排版节奏

### 6. Hero 页和非 hero 页要交替

**推荐节奏**（25-30 页）：
```
Hero Cover → Act Divider (hero) → 3-4 pages non-hero → Act Divider (hero)
→ 4-5 pages non-hero → Hero Question → ... → Hero Close
```

连续 2 页以上 hero 会让人疲劳，连续 4 页以上 non-hero 会让节奏死。

### 7. 大字报页和密集页要交替

大字报（big numbers / hero question）和密集页（pipeline / image grid）交替出现，听众眼睛才不累。

### 8. 同一概念的英文/中文用法要统一

**现象**：一会儿写 "Skills"，一会儿写 "技能"，一会儿写 "薄承载厚技能"，全篇不一致。

**做法**：
- 术语优先用**英文单词**（Skills / Harness / Pipeline / Workflow），这些都是圈内熟悉词
- **别硬翻译**，硬翻译反而生硬
- 整个 deck 里同一个词 1 个写法

### 9. 底部 chrome 的页码要一致

用 `XX / 总页数` 的格式（比如 `05 / 27`）。**不要在右上角加动态页码**（会和 `.chrome` 重复）。

---

## 🟢 P2 · 视觉打磨

### 10. WebGL 背景的遮罩透明度

**dark hero**：遮罩 12-15%（WebGL 明显透出）
**light hero**：遮罩 16-20%（WebGL 隐约可见，不抢字）
**普通 light/dark 页**：遮罩 92-95%（几乎不透）

如果页面文字非常少（hero question），遮罩可以再薄些；如果正文密集，必须加厚遮罩确保可读。

### 11. Light hero 的 shader 不能有强中心点

**现象**：Spiral Vortex、径向涟漪在 light 主题下太显眼，像 Windows 98 屏保。

**做法**：light hero 用 FBM 域扭曲驱动的无中心流动，底色保持银/纸色（接近 #F0F0F0 / #FBF8F3），彩虹偏色 subtle（0.05 以下）。

### 12. Dark hero 允许更多视觉冲击

Dark hero 可以用 Holographic Dispersion（钛金色散）等带中心结构的 shader，因为黑底能容纳更多视觉信息。

### 13. 左文右图的对齐

- 左列的文字组 `justify-content:space-between`：标题贴顶，引用框贴底
- 右列图片 `align-self:end`：和左列的底部元素对齐
- 网格整体 `align-items:start`（不是 `center` / `end`）

### 14. 图片的微弱圆角

所有 `.frame-img` 和 `.frame-img img` 都加 `border-radius:4px`，视觉上"柔和"但不软。**不要超过 8px**，否则像消费 app UI。

---

## 🔵 P3 · 操作细节

### 15. 图片路径用相对路径

图片放在 `images/` 文件夹下，HTML 里用相对路径 `images/xxx.png`，不要用绝对路径。

### 16. 页码在 `.chrome` 里写死

JS 会动态算总页数并扩展底部翻页圆点，但 `.chrome` 里的 `XX / N` 是写死的。加页/删页时要手工改 N。

### 17. 翻页导航要保留

模板默认支持：← → / 滚轮 / 触屏滑动 / 底部圆点 / Home·End。不要删 JS 里的导航逻辑。

### 18. 不要用 `height:100vh` 硬设，用 `min-height:80vh`

`100vh` 会让内容刚好卡满屏幕，但浏览器工具栏、标签栏会吃掉一部分高度，导致内容溢出。用 `min-height:80vh + align-content:center` 更稳。

---

## 🧪 最终自检清单

生成完 PPT 后，逐项对照这个清单（勾一下）：

```
预检(生成前)
  □ 已读过 template.html 的 <style>,确认所需类都存在
  □ 已决定每页用哪个 Layout(1-10)
  □ 已画出"版式节奏表":每页明确 cover / stat / body / divider / quote / close
  □ 默认输出没有 `light` 页面,全程使用 dark / hero dark
  □ `<title>` 已改为实际 deck 标题(grep "[必填]" 应无结果)

内容
  □ 每一幕的页数比例合理(不会头重脚轻)
  □ 没有使用 emoji 作图标
  □ Skills / Harness 等术语用法统一
  □ 每页的 kicker + 标题 + 正文 三级信息清晰

排版
  □ 所有大标题没有出现 1 字 1 行的换行
  □ 图片网格用 height:Nvh 而非 aspect-ratio
  □ 图片只裁底部，顶部和左右完整
  □ 衬线/非衬线字体分工符合模板
  □ Pipeline 多组之间有明显分隔

视觉
  □ hero 页和 non-hero 页交替
  □ WebGL 背景在 hero 页可见
  □ 图片有微弱圆角
  □ 没有沉重的阴影和边框

交互
  □ ← → 翻页正常
  □ 底部圆点数量与总页数匹配
  □ chrome 里的页码和实际页号一致
  □ ESC 键触发索引视图（如果保留）
```

全勾完，才是合格的 PPT。
