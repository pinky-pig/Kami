# Design System

## 设计宣言

这一版 kami 的目标是 **民国报纸感**：

**旧报纸底、黑色铅字、竖排题名、密集分栏、剪报框线、灰度照片、红印章点睛。**

它继承原版 kami 的模板驱动与构建校验，但视觉语言从“馆藏文稿”切换到“报纸特刊 / 号外 / 剪报拼版”。最终输出应该像一份可信的旧报刊材料，而不是复古海报。

参考图来自 `assets/reference-images/style-2-*`：

- `style-2-1.jpg`: 总览，包含报头、邮戳、剪报、信封、邮票、红印
- `style-2-2.png`: 家书特刊与留白型信件版式
- `style-2-4.png`: 密集剪报网格、黑底反白栏目、红印章
- `style-2-5.png`: 战时报纸式头版、竖排日期与密集正文

## V1 范围

- 正式迁移：中文 `one-pager`、`long-doc`、`letter`、`slides`
- 沿用：现有字体文件、模板骨架、页数校验
- 暂缓：英文主题化、简历、作品集、复杂撕纸/邮票齿孔拟物

---

## 八条铁律

1. 页面用旧报纸底 `#E8DFC9`，不用纯白，也不用深蓝外框
2. 主视觉只有黑墨 `#161411` + 暖灰纸色，拒绝现代冷灰
3. 唯一强色是印章红 `#B7352A`，一页最多一处主红印
4. 报头、大题、竖排题名由 serif 主导，中文 serif 使用京華老宋体
5. 正文可以分栏密排，但 line-height 不低于 `1.35`
6. 线条必须是实色黑/暖灰，禁止 `rgba()`
7. 图片必须灰度化、低对比，像新闻证据，不像现代 hero
8. 装饰只做报头、日期栏、黑底反白条、剪报框、邮戳/红印，不做杂乱拼贴海报

---

## 1. 色彩系统

### 纸张 · Newsprint

```css
--newsprint:  #E8DFC9;  /* 主旧报纸底 */
--paper-light:#F8F1DD;  /* 纸张高光 */
--paper-deep: #DED4BD;  /* 纸张暗部 */
--panel-fill: #F5EBD3;  /* 剪报块 / 信息框 */
--rule-warm:  #B9AA91;  /* 次级框线 */
```

设计重点是“保存过的旧报纸”，不是脏污废纸：

- 可使用轻纸纹
- 不做过重泛黄
- 不做撕裂边、污渍、水印式拟物
- 纸底必须能承受密集小字

### 墨色 · Ink

```css
--ink:        #161411;  /* 报头 / 主框线 / 黑底反白条 */
--near-black: #1F1B16;  /* 正文主墨色 */
--dark-warm:  #3E382E;  /* 次级正文 */
--charcoal:   #514A3F;  /* 密集正文 / 表格 */
--olive:      #6A6257;  /* 说明 / 注释 */
--stone:      #8A8173;  /* 日期 / 元信息 */
```

规则：**像铅印油墨，不像屏幕纯黑。**

### 红印 · Seal

```css
--seal-red: #B7352A;
```

红色只用于：

- 方形印章
- 邮戳 / 发行标记
- 极少量落款符号

禁止把红色用于普通 tag、按钮、标题高亮、表格热区。

---

## 2. 字体系统

### 字体栈

```css
/* 中文 serif */
"KingHwa_OldSong", "Source Han Serif SC", "Noto Serif CJK SC", "Songti SC", Georgia, serif;

/* 中文 sans / UI */
"Source Han Sans SC", "Noto Sans CJK SC", "PingFang SC", Arial, sans-serif;

/* mono */
"JetBrains Mono", Consolas, monospace;
```

### 字重与层级

| 角色 | 字号 | 字重 | line-height |
|---|---:|---:|---:|
| Masthead | 36-54 pt | 500 | 1.05 |
| Vertical Title | 26-40 pt | 500 | 1.10 |
| Headline | 18-28 pt | 500 | 1.12 |
| Section Banner | 10-13 pt | 500 | 1.25 |
| Body Lead | 10.5-12 pt | 400 | 1.45 |
| Body | 9.2-10.2 pt | 400 | 1.42-1.50 |
| Body Dense | 8.4-9.2 pt | 400 | 1.35-1.42 |
| Caption | 7.5-8.5 pt | 400 | 1.35 |
| Dateline | 7-8 pt | 400/500 | 1.25 |

原则：

- 报头靠字号、字距、框线建立权威，不靠 bold
- 竖排题名用于标题、日期栏、侧边标语，不用于长正文
- 正文密度可以高于文稿主题，但不可牺牲阅读

---

## 3. 版式系统

### 页面框架

| 文档类型 | 报纸解释 | 结构 |
|---|---|---|
| One-Pager | 头版 / 号外 | 大报头 + lead story + 2-4 个剪报栏 |
| Long Doc | 多页特刊 | 每章像连续报道，可带版号 / 栏目名 |
| Letter | 家书特刊 / 通信剪报 | 竖排题名 + 正文函件 + 证据框 |
| Slides | 报刊编辑部 deck | 每页像一张报纸版面或剪报板 |

### 分栏

- One-pager: 2-3 栏，允许一个大 lead story 跨栏
- Long-doc: 2 栏正文优先，章节开头可单栏
- Letter: 正文横排优先，左/右侧可放竖排题名
- Sidebars: 用窄栏承载数据、人物、时间线、引用

### 留白

报纸风不是越满越好。推荐留白：

- 报头下方留 `8-14pt`
- 剪报框内 padding `7-11pt`
- 栏间距 `9-14pt`
- 页外边距 `9-12mm`

---

## 4. 组件语言

### 报头 · Masthead

```css
.masthead {
  font-family: var(--serif);
  font-size: 42pt;
  line-height: 1.05;
  letter-spacing: 2pt;
  color: var(--ink);
  border-bottom: 1.2pt solid var(--ink);
}
```

适用于 `家书特刊`、`燕京时报`、`项目号外` 等 4-8 字标题。

### 日期线 · Dateline

```css
.dateline {
  font-size: 7.5pt;
  letter-spacing: 0.8pt;
  color: var(--dark-warm);
  border-bottom: 0.45pt solid var(--rule-warm);
}
```

内容包含日期、地点、期号、发行说明。不要写无意义英文小字。

### 黑底反白栏目条

```css
.reverse-label {
  display: inline-block;
  background: var(--ink);
  color: var(--paper-light);
  padding: 2pt 6pt;
  font-size: 9pt;
  letter-spacing: 1pt;
}
```

用于栏目名，例如 `一封家书胜过千言万语`、`见字速归`、`战火纷飞 笔墨传情`。

### 竖排题名

```css
.vertical-title {
  writing-mode: vertical-rl;
  text-orientation: upright;
  font-family: var(--serif);
  font-size: 30pt;
  line-height: 1.12;
  color: var(--ink);
}
```

适合标题和边栏，正文不大段竖排。

### 剪报框

```css
.clipping {
  background: var(--panel-fill);
  border: 0.75pt solid var(--ink);
  padding: 8pt 10pt;
}

.clipping + .clipping {
  margin-top: 8pt;
}
```

圆角默认 `0`。如果必须柔和，半径不超过 `2pt`。

### 灰度照片

```css
.news-photo {
  filter: grayscale(1) contrast(0.92);
  border: 0.55pt solid var(--ink);
}
```

照片是新闻证据，不是装饰主角。

### 红印

```css
.seal {
  display: inline-grid;
  place-items: center;
  width: 34pt;
  height: 34pt;
  border: 1.4pt solid var(--seal-red);
  color: var(--seal-red);
  font-family: var(--serif);
}
```

一页主红印最多一个。长文每章不重复盖章。

---

## 5. 文档类型模式

### One-Pager · 头版 / 号外

结构：

1. 报头：4-8 字 masthead
2. 日期线：地点、日期、期号
3. Lead headline：最重要的论点
4. 2-4 个剪报框：数据、证据、路线图、引用
5. 红印或发行标记：一处即可

### Long Doc · 多页特刊

结构：

1. 封面像报纸头版
2. 目录像版面索引
3. 每章像一版专题报道
4. 关键图表放进剪报框
5. 页脚保留版号 / 日期

### Letter · 家书特刊

结构：

1. 竖排题名：如 `家书抵万金`
2. 黑底反白短句
3. 正文函件
4. 证据 / 推荐理由剪报框
5. 红印落款

---

## 6. 禁区

- 不用蓝色、紫色、霓虹色
- 不用现代渐变、glass、SaaS 圆角卡片
- 不做大面积插画或彩色 hero
- 不把每个元素都旋转成“拼贴”
- 不牺牲信息清晰度去模仿旧报纸的拥挤

---

## 7. 交付检查

- [ ] 页面第一眼能看出报头/特刊身份
- [ ] 没有档案蓝遗留
- [ ] 强调色只有红印一处
- [ ] 正文密度高但可读
- [ ] 线条是实色，没有 `rgba()`
- [ ] 图片灰度化
- [ ] 不是复古海报，而是可读的报纸特刊
