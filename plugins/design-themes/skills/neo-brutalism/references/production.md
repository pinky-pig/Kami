# Production（生成 · 验证 · 排错）

这份文档覆盖 kami 的工程执行：从 HTML/Python 模板到 PDF/PPTX/Slidev 成品的完整流程。分四部分：**HTML -> PDF** · **Slides 双产物（PPTX + Slidev）** · **验证与调试** · **15 条踩坑**。

---

## Part 1 · HTML -> PDF（WeasyPrint）

### 安装

```bash
pip install weasyprint pypdf --break-system-packages --quiet
```

Linux 初次使用可能需要：
```bash
apt install -y libpango-1.0-0 libpangoft2-1.0-0 fonts-noto-cjk
```

### 生成

```python
from weasyprint import HTML
HTML('doc.html').write_pdf('output.pdf')
```

**注意 CWD**：HTML 里 `@font-face { src: url("xxx.ttf") }` 是相对路径，必须在**包含字体文件的目录**执行。

```bash
cd /path/to/html-and-font
python3 -c "from weasyprint import HTML; HTML('doc.html').write_pdf('out.pdf')"
```

### 字体处理

**最稳的做法**：字体文件和 HTML 同目录，`@font-face` 用相对路径。

```html
<style>
@font-face {
  font-family: "KingHwa_OldSong";
  src: url("京華老宋体v2.002.ttf");
}
body { font-family: "KingHwa_OldSong", serif; }
</style>
```

**商业字体不可得时**，fallback 链已内嵌在所有模板里：
```css
font-family: "KingHwa_OldSong",
             "Source Han Serif SC", "Noto Serif CJK SC",
             "Songti SC", Georgia, serif;
```

**字体 fallback 影响页数**：换字体必须重新跑页数验证。溢出时优先调 `font-size`，再调 margin，最后砍内容。

### 页面规格

```css
@page {
  size: A4;                  /* 或 210mm 297mm / A4 landscape / 13in 10in */
  margin: 20mm 22mm;
  background: #f5f4ed;       /* 背景延伸到 margin 外，避免打印白边 */
}
```

### 页眉页脚

```css
@page {
  @top-right {
    content: counter(page);
    font-family: serif; font-size: 9pt; color: #87867f;
  }
  @bottom-center {
    content: "{{文档名}} · {{作者}}";
    font-size: 8.5pt; color: #87867f;
  }
}

@page:first {
  @top-right { content: ""; }
  @bottom-center { content: ""; }
}
```

### WeasyPrint 支持矩阵

| 支持良好 | 支持有限 | 不支持 |
|---|---|---|
| CSS Grid / Flexbox | CSS filter / transform（部分） | JavaScript |
| `@page` 规则 | inline SVG（部分属性） | `position: sticky` |
| `@font-face` | gradient（性能差，少用） | CSS 动画 / transition |
| `break-before` / `break-inside: avoid` | | |
| CSS 变量 `var(--name)` | | |
| 伪元素 `::before` `::after` | | |

---

## Part 2 · Slides 双产物（python-pptx + Slidev）

Neo-Brutalism 的 slides 现在走**单一内容源 + 双渲染器**：

- `assets/templates/slides_spec.py`：共享 slide schema
- `assets/templates/slides.py`：生成 `assets/demos/demo-slides.pptx`
- `assets/templates/slidev/render_from_spec.py`：生成 `assets/templates/slidev/slides.md`
- `assets/templates/slidev/`：通过 Slidev build 到 `assets/demos/slides-online/`

视觉上，PPTX 和在线 deck 都必须继续保持 Neo-Brutalism 的 **黑色粗框 / 高饱和色块 / 硬阴影 / 贴纸拼贴**，不能退回安静排版。

### 安装

```bash
pip install python-pptx --break-system-packages --quiet
```

在线 deck 额外需要：

```bash
cd assets/templates/slidev
pnpm install
```

### 尺寸

- **16:9 宽屏**（推荐）：13.33 × 7.5 inch
- **4:3 传统**：10 × 7.5 inch
- **安全区**：四周 0.5 inch 不放内容，底部额外 0.3 inch 给页码

### 色板（1:1 对应 design.md / slides.py）

```python
from pptx.dml.color import RGBColor

CREAM   = RGBColor(0xFF, 0xFD, 0xF5)
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
BLACK   = RGBColor(0x00, 0x00, 0x00)
RED     = RGBColor(0xFF, 0x6B, 0x6B)
YELLOW  = RGBColor(0xFF, 0xD9, 0x3D)
VIOLET  = RGBColor(0xC4, 0xB5, 0xFD)
```

### 字号（屏幕投影优先易读性，比 PDF 大）

| 角色 | 字号 | 字体 |
|---|---|---|
| Title | 38-44pt | Sans 700-900 |
| Subtitle | 24pt | Sans 400 |
| H2 章节 | 30-32pt | Sans 700-900 |
| H3 小标题 | 18-22pt | Sans 700 |
| Body | 13-18pt | Sans 400-700 |
| Label / Eyebrow | 7-12pt | Sans / Mono 700 |
| Footer | 8-12pt | Sans / Mono 700 |

中文字体栈：
- 主字体：`Inter` -> `Source Han Sans SC` -> `PingFang SC` -> `微软雅黑`
- 在线 deck 小标签可用：`JetBrains Mono`

### 5 张标准版式

1. **封面页**：红色大底 panel + 黄色 badge + 右侧高饱和贴纸
2. **Tokens 页**：四色卡片并列，强调 theme palette 本身就是内容
3. **Composition 页**：一张白卡配两张旋转 sticker，表现 60/40 非对称和硬阴影
4. **Outputs 页**：三条彩色粗框 row，说明 PDF / 长文 / 信件的共通语言
5. **结束页**：黄色大 panel + 红色 badge，句子必须像海报口号

### 脚本骨架

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN

CREAM = RGBColor(0xff, 0xfd, 0xf5)
RED   = RGBColor(0xff, 0x6b, 0x6b)
# ... 其他色见上表
SANS  = "Source Han Sans SC"

prs = Presentation()
prs.slide_width  = Inches(13.33)
prs.slide_height = Inches(7.5)

def blank_slide():
    """空白页，cream 底"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = CREAM
    bg.line.fill.background(); bg.shadow.inherit = False
    return slide

def add_text(slide, text, left, top, width, height,
             font=SANS, size=18, bold=False, italic=False,
             color=RGBColor(0x14,0x14,0x13), align=PP_ALIGN.LEFT):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]; p.alignment = align
    run = p.add_run(); run.text = text
    run.font.name = font; run.font.size = Pt(size)
    run.font.bold = bold; run.font.italic = italic
    run.font.color.rgb = color
    return tb

def add_line(slide, left, top, width, color=RED, weight_pt=1):
    line = slide.shapes.add_connector(1, left, top, left + width, top)
    line.line.color.rgb = color; line.line.width = Pt(weight_pt)
    return line

# 封面
s = blank_slide()
add_text(s, "文档标题", Inches(1.5), Inches(3), Inches(10.33), Inches(1),
         font=SANS, size=44, bold=True)
add_line(s, Inches(1.5), Inches(4), Inches(2), color=RED, weight_pt=4)
add_text(s, "副标题 · 副说明", Inches(1.5), Inches(4.2), Inches(10.33), Inches(0.6), font=SANS, size=18)

prs.save('output.pptx')
```

完整版见 `assets/templates/slides.py`，共享内容源见 `assets/templates/slides_spec.py`，在线 deck 渲染器见 `assets/templates/slidev/render_from_spec.py`。

### 在线 deck 文件流

```bash
python3 scripts/build.py slides
```

输出：

- `assets/demos/demo-slides.pptx`
- `assets/demos/slides-online/`
- `assets/demos/slides-online/slides-online-preview.py`
- `assets/demos/slides-online/slides-online-preview.command`

### PPT 注意事项

1. **一页一个核心信息**：超过 3 段文字就拆分
2. **不用自带 Template**：PowerPoint default 的冷蓝灰会削弱 Neo-Brutalism 的黑边和高饱和色块
3. **动画**：不加。Neo-Brutalism slides 是海报式静态构图，不靠 motion 讲故事
4. **导出 PDF**：分享时推荐导出 PDF，跨机器一致性比 .pptx 高
   - macOS：Keynote 打开 -> Export to PDF
   - Linux：`libreoffice --headless --convert-to pdf output.pptx`

---

## Part 3 · 验证与调试

### 必跑三步（每次改动）

```bash
# 1. 生成
python3 -c "from weasyprint import HTML; HTML('doc.html').write_pdf('out.pdf')"

# 2. 页数
python3 -c "from pypdf import PdfReader; print(len(PdfReader('out.pdf').pages))"

# 3. 视觉检查（怀疑视觉问题时）
pdftoppm -png -r 300 out.pdf inspect
```

**不验证不算改完**。

### 字体是否加载成功

```bash
pdffonts output.pdf
```

输出里如果看到 `DejaVuSerif` / `Bitstream Vera`，说明指定字体没生效，走到了系统兜底。正确应该看到 `KingHwa_OldSong` 或 `Source Han Serif SC`。

### 一键生成 + 验证脚本

```python
#!/usr/bin/env python3
"""生成并验证 PDF"""
import sys
from weasyprint import HTML
from pypdf import PdfReader

html_file = sys.argv[1] if len(sys.argv) > 1 else 'doc.html'
pdf_file  = sys.argv[2] if len(sys.argv) > 2 else 'output.pdf'
max_pages = int(sys.argv[3]) if len(sys.argv) > 3 else 0

HTML(html_file).write_pdf(pdf_file)
n = len(PdfReader(pdf_file).pages)
print(f'✓ {pdf_file}, {n} pages')

if max_pages and n > max_pages:
    print(f'✗ Exceeded limit ({n} > {max_pages})')
    sys.exit(1)
```

项目脚本 `scripts/build.py` 是这段的产品化版本。

### 高分辨率视觉检查

```bash
pdftoppm -png -r 160 output.pdf preview         # 标准
pdftoppm -png -r 300 output.pdf preview         # 排查细节 bug
pdftoppm -png -r 400 output.pdf preview         # 极致细节（tag 双层等）
```

### 生成多版本

```python
for variant, vars_css in [
    ('light', '--bg: #f5f4ed;'),
    ('dark',  '--bg: #141413;'),
]:
    custom = base.replace('{{VARS}}', f':root {{ {vars_css} }}')
    HTML(string=custom).write_pdf(f'out-{variant}.pdf')
```

---

## Part 4 · 15 条踩坑

每一条都是真实踩出来的。遇到视觉异常立刻来这里查。

### 1. Tag / Badge 双层矩形 bug（最坑）

**症状**：PDF 放大看背景色 tag，出现内外两层矩形。手机预览器尤其明显。

**根因**：WeasyPrint 渲染 `rgba(..., 0.xx)` 时，**padding 区域**和**字形像素区域**分别做透明度计算，字形 anti-alias 让周围透明度叠加更深，形成视觉第二层。

**解法**：Tag 背景必须用实色 hex，禁用 rgba。

```css
/* ❌ */ .tag { background: rgba(201, 100, 66, 0.18); }
/* ✅ */ .tag { background: #E4ECF5; }
```

**rgba -> 实色对照表**（底 parchment `#f5f4ed` + 前景油墨蓝 `#1B365D`）：

| rgba 透明度 | 等效实色 hex |
|---|---|
| 0.08 | `#EEF2F7` |
| 0.14 | `#E4ECF5` |
| **0.18** | **`#E4ECF5`** ← 默认 |
| 0.22 | `#ead3c7` |
| 0.30 | `#D6E1EE` |

公式：`实色通道 = 底 + (前景 - 底) × 透明度`。其他底色要重算。

**想要"呼吸感"**：用 CSS linear-gradient（整张 tag 栅格化为位图，不走逐像素合成）：

```css
.tag {
  background: linear-gradient(to right, #D6E1EE, #E4ECF5 70%, #EEF2F7);
}
```

**美学教训**：工程上 gradient 能做出笔刷感，审美上往往**用力过猛**。实战优先级：极淡实色 `#EEF2F7` > 稍浓实色 `#E4ECF5` > 慎用 gradient。如果读者第一眼看到的是背景形状而不是字，就过度了。

### 2. 薄边框 + 圆角 = 双圈 bug

**症状**：`border: 0.4pt solid ...` + `border-radius: 2pt` 放大后两条平行线。

**根因**：WeasyPrint 对 < 1pt border + 圆角，分别 stroke 内外 path，薄宽度没法重合。

**解法**三选一：
1. 改用背景填充（首选，设计语言一致）
2. border ≥ 1pt
3. 去掉 border-radius

### 3. 2 页硬约束溢出

适用于 resume、one-pager 等页数受限的文档。

**常见诱因**：字体 fallback、新增内容、字号意外增大、line-height 从 1.4 -> 1.6。

**诊断**：`pdffonts output.pdf` 看实际加载字体。

**解法（按优先级）**：
1. 删冗余副词（"深入研究" -> "研究"）
2. 合并同义数据
3. 砍次要项
4. 减小 section 间距（慎用）
5. 最后手段：字号降 0.1-0.2pt

**不要做**：去掉封面/教育/Timeline 这类结构性内容，砍高亮（简历会变死气）。

### 4. 字体 fallback 导致页数不一致

**症状**：本机 2 页，CI/服务器 4 页。

**根因**：字体文件没和 HTML 同目录/未系统安装。

**解法**：

```bash
# 把 .ttf 放 HTML 同目录
cp 京華老宋体v2.002.ttf workspace/

# 或系统安装（Linux）
apt install fonts-noto-cjk
mkdir -p ~/.fonts && cp *.ttf ~/.fonts/ && fc-cache -f
```

### 5. 中英文紧贴

**症状**：`125.4k GitHub Stars` 看起来 k 和 G 太贴。

**错误解法**：手动加 `&nbsp;` / `margin-left: 2mm`（影响对齐）。

**正确解法**：独立 span + flex gap：

```html
<div class="metric">
  <span class="metric-value">125.4k</span>
  <span class="metric-label">GitHub Stars</span>
</div>
```
```css
.metric { display: flex; align-items: baseline; gap: 6pt; }
```

### 6. 全角 vs 半角空格

- **中文之间**：全角空格 `　`（U+3000）+ `·` + 空格
- **英文之间**：半角空格 + `·` + 空格
- **中英混排**：flex gap 优先，不加空格

### 7. 千分位 · 百分号 · 箭头

| ✅ | ❌ |
|---|---|
| `5,000+` | `5000+` / `5，000+`（全角逗号） |
| `90%` | `90 %`（前有空格） |
| `->` | `->` / `-&gt;` |

自查：
```bash
grep -oE '->|->|⟶|⇒' doc.html | sort | uniq -c
grep -oE '[0-9]{4,}' doc.html | sort -u
```

### 8. 高亮过多 / 过少

- 一行 4-5 个橙字 -> 视觉疲劳
- 整节没高亮 -> 扁平

**规则**：每行 ≤ 2 处，每节至少 1 处，只高亮**可量化的数字或独特表达**。

合理区间：文档总字数 ÷ 高亮数 ≈ 80-150 字/高亮。

### 9. `height: 100vh` 不工作

**症状**：想做满屏封面，`height: 100vh` 没效果。

**根因**：WeasyPrint 的 @page 语境下 viewport 单位不准。

**解法**：

```css
.cover {
  min-height: 257mm;    /* A4 高 297 - 上下 margin 40 */
  display: flex; flex-direction: column; justify-content: center;
}
```

### 10. break-inside 在 flex 容器里失效

**解法**：给 flex item 额外包一层 block 容器：

```html
<div class="row">
  <div class="card-wrapper"><div class="card">...</div></div>
</div>
```
```css
.row { display: flex; }
.card-wrapper { break-inside: avoid; }
```

### 11. 首页不要页码

```css
@page:first {
  @top-right { content: ""; }
}
```

### 12. 打印留白边

**症状**：打印四周有白边（即使 background 设置了）。

**根因**：默认 WeasyPrint 的 `@page background` 只延伸到 page 区域。

**解法**：

```css
@page {
  size: A4; margin: 20mm;
  background: #f5f4ed;    /* 让背景延伸到 margin 外 */
}
```

### 13. 图片模糊

**症状**：PDF 里图片发虚。

**根因**：按原始像素渲染。A4 @ 300 dpi 需要 2480 × 3508 像素。

**解法**：嵌入图要用 2-3x 源。

### 14. 验证闭环（兜底）

```bash
python3 -c "from weasyprint import HTML; HTML('doc.html').write_pdf('out.pdf')"
python3 -c "from pypdf import PdfReader; print(len(PdfReader('out.pdf').pages))"
pdftoppm -png -r 300 out.pdf inspect    # 视觉怀疑时
```

**不验证不算改完**。

### 15. SVG marker `orient="auto"` 不生效

**症状**：SVG 里用 `<marker orient="auto">` 或 `orient="auto-start-reverse"` 的箭头，所有方向都指向右（marker 的默认绘制方向），不随路径切线旋转。

**根因**：WeasyPrint 的 SVG 渲染不支持 marker 的 `orient="auto"` 属性。marker 永远按 0° 绘制。

**解法**：不用 `<marker>`，手动在每个箭头端点画 chevron `<path>`，方向写死。

```xml
<!-- ❌ marker 箭头：WeasyPrint 全部朝右 -->
<defs>
  <marker id="a" orient="auto" ...>
    <path d="M2 1L8 5L2 9" .../>
  </marker>
</defs>
<path d="M 440 52 Q 568 52 568 244" marker-end="url(#a)"/>

<!-- ✅ 手绘 chevron：每个方向单独写 -->
<path d="M 440 52 Q 568 52 568 244" fill="none" stroke="#5e5d59" stroke-width="1.5"/>
<path d="M 560 236 L 568 244 L 576 236" fill="none" stroke="#5e5d59" stroke-width="1.5"
      stroke-linecap="round" stroke-linejoin="round"/>
```

四个方向的 chevron 模板（tip 在端点，arm 长度 8px）：

| 方向 | chevron path |
|---|---|
| ↓ | `M (x-8) (y-8) L x y L (x+8) (y-8)` |
| ← | `M (x+8) (y-8) L x y L (x+8) (y+8)` |
| ↑ | `M (x-8) (y+8) L x y L (x+8) (y+8)` |
| → | `M (x-8) (y-8) L x y L (x-8) (y+8)` |
