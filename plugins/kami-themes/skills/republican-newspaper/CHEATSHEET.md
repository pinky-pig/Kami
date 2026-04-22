# kami · 民国报纸风格速查

一页纸速查。填模板、调细节前先看这里。完整规范在 `references/design.md`。

## V1 范围

- 正式支持：中文 `one-pager`、`long-doc`、`letter`、`slides`
- 风格目标：民国报纸、报纸特刊、号外、剪报拼贴
- 暂不主推：英文模板、简历、作品集

## 八条铁律

1. 页面是旧报纸底 `#E8DFC9` + 黑墨 `#161411`，不用深蓝外框
2. 强调靠黑色反白条、竖排题名、细框线，不靠彩色高亮
3. 唯一强色是印章红 `#B7352A`，一页最多一处主红印
4. 中文 serif 统一使用京華老宋体；报头、大题、竖排题名优先 serif
5. 正文可以密排分栏，但 line-height 不低于 1.35
6. 框线使用 `0.45pt-1pt` 黑/暖灰实线，禁 `rgba()`
7. 图片必须灰度、低对比、像新闻证据，不做现代 hero 图
8. 装饰只做报头、日期栏、反白栏目条、剪报框、邮戳/印章，不做杂乱海报

## 自然语言触发

| 用户说 | 路由 |
|---|---|
| 做成民国报纸风 / 旧报纸风 | 先判断文档类型 |
| 生成一份报纸特刊 / 做一版号外 | `one-pager.html` |
| 把白皮书排成旧报纸 / 深度报道 | `long-doc.html` |
| 家书特刊 / 推荐信做成报纸风 | `letter.html` |
| 民国报纸风 slides | `slides.py` |

## 色板

| 角色 | Hex | 用途 |
|---|---|---|
| Newsprint | `#E8DFC9` | 主纸底 |
| Paper Light | `#F8F1DD` | 浅纸高光 |
| Paper Deep | `#DED4BD` | 纸张暗部 |
| Panel Fill | `#F5EBD3` | 剪报块 / 信息框 |
| Ink | `#161411` | 报头、主标题、主框线 |
| Near Black | `#1F1B16` | 正文主墨色 |
| Warm Dark | `#3E382E` | 次级正文 |
| Column Gray | `#514A3F` | 密集正文 / 表格 |
| Caption Gray | `#6A6257` | 注释、日期 |
| Faded Ink | `#8A8173` | 淡元信息 |
| Rule Warm | `#B9AA91` | 次框线 |
| Seal Red | `#B7352A` | 印章 / 邮戳 |

## 字号（印刷品 pt）

| 角色 | 字号 | 字重 | line-height |
|---|---|---|---|
| Masthead | 36-54 | 500 | 1.05 |
| Vertical Title | 26-40 | 500 | 1.10 |
| Headline | 18-28 | 500 | 1.12 |
| Section Banner | 10-13 | 500 | 1.25 |
| Body Lead | 10.5-12 | 400 | 1.45 |
| Body | 9.2-10.2 | 400 | 1.42-1.50 |
| Body Dense | 8.4-9.2 | 400 | 1.35-1.42 |
| Caption | 7.5-8.5 | 400 | 1.35 |
| Dateline | 7-8 | 400/500 | 1.25 |

## 页面边距（A4）

| 文档 | 框架 |
|---|---|
| One-Pager | `@page margin: 0`，旧报纸满页；内容外框约 9-11mm，内部 10-12mm |
| Long Doc | 每页一个 `.folio`，报纸底 + 细黑内框 + 页脚报号 |
| Letter | 信件像剪报/家书特刊，左或右可放竖排题名 |

## 常用 CSS 片段

### 报纸页

```css
@page {
  size: A4;
  margin: 0;
  background: var(--newsprint);
}

.folio {
  position: relative;
  min-height: 276mm;
  padding: 11mm;
  background:
    url("../images/paper-overlay.png") center / 70mm auto repeat,
    linear-gradient(135deg, var(--paper-light), var(--newsprint) 52%, var(--paper-deep));
}

.folio::before {
  content: "";
  position: absolute;
  inset: 6mm;
  border: 0.9pt solid var(--ink);
}
```

### 报头 / Masthead

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

### 反白栏目条

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

## 决策速查

| 想做 | 怎么做 |
|---|---|
| 大标题 | 报头式横排或竖排，serif 500，黑墨 |
| 分隔内容 | 细黑线 / 双线 / 剪报框 |
| 栏目标题 | 黑底白字反白条 |
| 重点证据 | 放进窄栏、边栏、剪报块 |
| 图片 | grayscale + 低对比 + 细边框 |
| 日期 | 小号 dateline，可横排或竖排 |
| 破色 | 一枚红印，不扩散到按钮/标签 |
| 空白太多 | 加分栏、边栏、报头线，不加现代卡片 |

不在表里，就回到一句话：**像一份可信的旧报纸特刊，不像复古海报。**
