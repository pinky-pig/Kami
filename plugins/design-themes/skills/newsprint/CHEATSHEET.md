# kami · 新闻纸风格速查

## 范围

- 正式支持：中文 `one-pager`、`long-doc`、`letter`、`slides`
- 风格目标：新闻纸底 / 黑色网格 / 出版物层级 / 少量红色强调
- 模板能力：沿用稳定的 HTML / PDF / PPTX / diagram / build pipeline；版面和内容格式必须是 Newsprint 原生

## 八条铁律

1. 文档不是网页 prompt 的直接粘贴；必须转译成 A4 / slides 可打印版式
2. 只继承生产流程，不继承 manuscript 的版式、题签、档案卡片和内容节奏
3. 主风格信号：新闻纸底 / 黑色网格 / 头版标题 / 分栏导语 / 边栏事实盒 / 少量红色强调
4. 字体统一使用 `"TsangerJinKai02", "Newsreader", "Source Serif 4", "Source Han Serif SC", "Noto Serif CJK SC", "Charter", Georgia, "Times New Roman", serif`
5. Tag 背景必须是实色 hex，不用 `rgba()`
6. 结构和正文清晰度优先于装饰
7. 页面可输出为 PDF；不要依赖浏览器-only 动效表达核心信息
8. 不要混入旧主题的深蓝档案题签、厚重外框、牌匾标题或民国报刊符号

## 自然语言触发

| 用户说 | 路由 |
|---|---|
| 用新闻纸风格做一份项目方案 | `one-pager.html` |
| 把这份白皮书排成 Newsprint | `long-doc.html` |
| 推荐信做成新闻纸风 | `letter.html` |
| 做一套 Newsprint slides | `slides.py` |
| 帮我把这些内容排版成好看的 PDF | 先判断 `one-pager` / `long-doc` / `letter` |

## 色板

| 角色 | Hex | 用途 |
|---|---|---|
| Parchment | `#F9F9F7` | 页面底 |
| Ivory | `#FFFFFF` | 卡片 / 内容浮层 |
| Brand | `#111111` | 主强调 |
| Frame | `#111111` | 页面结构 / 外框 |
| Rule | `#111111` | 分隔线 / 边框 |
| Tag | `#111111` | 标签底 |
| Accent 1 | `#CC0000` | 主题强调 |
| Accent 2 | `#E5E5E0` | 次强调 |
| Accent 3 | `#F5F5F5` | 装饰 / 轮换强调 |
| Near Black | `#111111` | 主文字 |
| Body | `#404040` | 次级正文 |
| Muted | `#737373` | 注释 / 元信息 |

## 常用命令

```bash
python3 scripts/build.py --verify one-pager
python3 scripts/build.py --verify long-doc
python3 scripts/build.py --verify letter
python3 scripts/build.py slides
python3 scripts/build.py --check
```

一句话：**生产流程沿用 Kami，内容骨架必须改写成头版标题、导语、分栏正文、边栏事实盒和编辑注记。**
