# kami · 新粗野主义风格速查

## 范围

- 正式支持：中文 `one-pager`、`long-doc`、`letter`、`slides`
- 风格目标：黑色粗框 / 高饱和色块 / 硬阴影 / 贴纸拼贴
- 模板能力：沿用稳定的 HTML / PDF / PPTX / diagram / build pipeline；版面和内容格式必须是 Neo-Brutalism 原生

## 八条铁律

1. 文档不是网页 prompt 的直接粘贴；必须转译成 A4 / slides 可打印版式
2. 只继承生产流程，不继承旧主题的版式、题签、外框和内容节奏
3. 主风格信号：黑色粗框 / 高饱和色块 / 硬阴影 / 贴纸拼贴 / DIY zine composition
4. 中文默认用重字重 sans，标题和数字尽量粗；不要使用旧 serif 文稿字体。
5. Tag 背景必须是实色 hex，不用 `rgba()`
6. 结构和正文清晰度优先于装饰
7. 页面可输出为 PDF；不要依赖浏览器-only 动效表达核心信息
8. 不要混入旧主题的深色题签、厚重框页、档案卡片或民国报刊符号

## 自然语言触发

| 用户说 | 路由 |
|---|---|
| 用新粗野主义风格做一份项目方案 | `one-pager.html` |
| 把这份白皮书排成 Neo-Brutalism | `long-doc.html` |
| 推荐信做成新粗野主义风 | `letter.html` |
| 做一套 Neo-Brutalism slides | `slides.py` |
| 帮我把这些内容排版成好看的 PDF | 先判断 `one-pager` / `long-doc` / `letter` |

## 色板

| 角色 | Hex | 用途 |
|---|---|---|
| Parchment | `#FFFDF5` | 页面底 |
| Ivory | `#FFFFFF` | 卡片 / 内容浮层 |
| Brand | `#000000` | 主强调 |
| Frame | `#000000` | 页面结构 / 外框 |
| Rule | `#000000` | 分隔线 / 边框 |
| Tag | `#FFD93D` | 标签底 |
| Accent 1 | `#FF6B6B` | 主题强调 |
| Accent 2 | `#FFD93D` | 次强调 |
| Accent 3 | `#C4B5FD` | 装饰 / 轮换强调 |
| Near Black | `#000000` | 主文字 |
| Body | `#000000` | 次级正文 |
| Muted | `#1F1F1F` | 注释 / 元信息 |

## 常用命令

```bash
python3 scripts/build.py --verify one-pager
python3 scripts/build.py --verify long-doc
python3 scripts/build.py --verify letter
python3 scripts/build.py slides
python3 scripts/build.py --check
```

一句话：**生产流程沿用 Kami，内容骨架必须改写成 loud hero、marquee strip、rotated cards、proof sticker、poster cover 和 blocky TOC。**
