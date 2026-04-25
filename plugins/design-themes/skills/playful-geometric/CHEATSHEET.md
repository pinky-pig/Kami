# kami · 趣味几何风格速查

## 范围

- 正式支持：中文 `one-pager`、`long-doc`、`letter`、`slides`
- 风格目标：稳定网格 / 几何贴纸 / 明亮色彩 / 友好硬阴影
- 模板能力：沿用稳定的 HTML / PDF / PPTX / diagram / build pipeline；版面和内容格式必须是 Playful Geometric 原生

## 十六条铁律

1. 文档不是网页 prompt 的直接粘贴；必须转译成 A4 / slides 可打印版式
2. 只继承生产流程，不继承旧主题的版式、题签、外框和内容节奏
3. 主风格信号：稳定网格 / primitive shapes / 几何贴纸 / 明亮色彩 / 友好硬阴影
4. 内容网格要稳，装饰可以活；标题和卡片用圆润 sans，正文保持可读。
5. Tag 背景必须是实色 hex，不用 `rgba()`
6. 结构和正文清晰度优先于装饰
7. 页面可输出为 PDF；不要依赖浏览器-only 动效表达核心信息
8. 不要混入旧主题的深色题签、厚重外框、档案卡片或民国报刊符号
9. 必须保留黑色贴纸边框，但每个组件最多一层黑边
10. 禁止外框套内框；页面只保留一个大圆角纸面和一层黑边
11. 圆角统一：内容块 16-18pt，标签 999pt；不要直角、小圆角、缺角混在一起
12. 指标卡、标签、短 callout、PPT 卡片标题必须居中
13. PDF 模块必须有明显色块，不要只剩白底线框
14. 禁止在圆角卡片内使用深色横条标题；标题用透明容器 + 居中文本 + 黄色 pill，不要负 margin 顶到卡片边缘
15. 偏移边框必须是硬边：黑色主边框 + 彩色偏移层 + 偏移层外侧黑边；不要用柔和阴影冒充
16. One-pager 不许硬塞：最多 3 个指标、2 个内容卡、一条短 timeline 或一条短 remark；超出就改 `long-doc`

## 自然语言触发

| 用户说 | 路由 |
|---|---|
| 用趣味几何风格做一份项目方案 | `one-pager.html` |
| 把这份白皮书排成 Playful Geometric | `long-doc.html` |
| 推荐信做成趣味几何风 | `letter.html` |
| 做一套 Playful Geometric slides | `slides.py` |
| 帮我把这些内容排版成好看的 PDF | 先判断 `one-pager` / `long-doc` / `letter` |

## 色板

| 角色 | Hex | 用途 |
|---|---|---|
| Parchment | `#FFFDF5` | 页面底 |
| Ivory | `#FFFFFF` | 卡片 / 内容浮层 |
| Brand | `#8B5CF6` | 主强调 |
| Frame | `#1E293B` | 页面结构 / 外框 |
| Rule | `#1E293B` | 分隔线 / 边框 |
| Tag | `#FBBF24` | 标签底 |
| Accent 1 | `#8B5CF6` | 主题强调 |
| Accent 2 | `#F472B6` | 次强调 |
| Accent 3 | `#34D399` | 装饰 / 轮换强调 |
| Near Black | `#1E293B` | 主文字 |
| Body | `#334155` | 次级正文 |
| Muted | `#64748B` | 注释 / 元信息 |

## 常用命令

```bash
python3 scripts/build.py --verify one-pager
python3 scripts/build.py --verify long-doc
python3 scripts/build.py --verify letter
python3 scripts/build.py slides
python3 scripts/build.py --check
```

一句话：**生产流程沿用 Kami，内容骨架必须改写成 hero sticker、side bubble、metric chips、proof pops、checklist 和 action pop。**
