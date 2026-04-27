# guizang-magazine 交接文档

给维护当前主题 skill 的人看。使用时优先读 `SKILL.md`、`CHEATSHEET.md`、`references/design.md`。

## 一句话定位

把 Kami 的文档生产能力切成 **歸藏杂志风 / 电子墨水风**：继续生成 HTML / PDF / PPTX，但视觉语言改成编辑部式层级、mono 元信息、serif 大标题和 5 套预设主题。

## 来源关系

- 生产链路：来自 `plugins/republican-themes/skills/republican-manuscript`
- 风格来源：来自 `https://github.com/op7418/guizang-ppt-skill`
- 原始参考快照：`references/guizang-source/`

这个 skill 的目标不是复制一个网页 swipe deck，而是把 deck 的视觉语言转译到：

- A4 one-pager
- 多页长文
- 正式信件
- 简历
- 作品集
- PPTX slides

## 文件职责

| 文件 | 作用 |
|---|---|
| `SKILL.md` | 触发词、工作流、适用边界 |
| `README.md` | 外部说明 |
| `CHEATSHEET.md` | 快速视觉规则 |
| `references/design.md` | 文档版式总规范 |
| `references/writing.md` | 写作与节奏规则 |
| `references/themes.md` | 5 套主题预设 |
| `references/components.md` | Guizang deck 组件语言 |
| `references/layouts.md` | Guizang deck 布局骨架 |
| `references/checklist.md` | 交付前自检 |
| `references/guizang-source/` | 原始仓库快照，便于回溯 |
| `assets/templates/*.html` / `slides.py` | 实际生产模板 |
| `scripts/build.py` | 构建与检查 |

## 改动原则

1. 不要退回到民国文稿的深蓝档案框
2. 不要退回到报纸 theme 的剪报和竖排符号
3. 不要随便接受自定义 hex，优先走 5 套预设
4. 标题、正文、元信息三层字体分工必须稳定
5. 视觉信号来自层级、留白、规则线和节奏，不来自花哨装饰
6. 任何改动都要考虑 PDF 和 PPTX 两端是否还能成立

## 高风险点

1. `build.py --verify` 若使用内容 demo，必须保证 demo 文件同步更新
2. 图片比例不要随手写奇怪 `aspect-ratio`
3. PPTX 里中文字体和拉丁字体是分槽的，修改 `slides.py` 时要注意
4. 页眉 `chrome` 和 `kicker` 很容易写成重复语义
5. 主题节奏不能整套都只有浅页

## 推荐维护动作

### 调颜色

- 先改 `references/themes.md`
- 再改 `references/tokens.json`
- 最后同步 HTML / PPTX 里的默认色

### 调样式

- 先回看 `references/guizang-source/template.html`
- 确认这是 deck 风格的延展，而不是另一套无关设计

### 改模板

- 尽量保留模板结构，只换视觉层
- 如果新增结构，优先抽象成可复用的 class，而不是全靠 inline style

## 验证

```bash
python3 scripts/build.py one-pager
python3 scripts/build.py long-doc
python3 scripts/build.py letter
python3 scripts/build.py slides
python3 scripts/build.py --check
```

如果要检查某次视觉调整是否破坏产物，优先看：

- 页数是否溢出
- 字体是否 fallback
- mono 元信息是否 still readable
- 大标题是否还保持第一眼识别
