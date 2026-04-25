#!/usr/bin/env python3
"""Prompt-native Playful Geometric slide deck generator."""

from __future__ import annotations

import zipfile
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.xmlchemy import OxmlElement
from pptx.util import Inches, Pt


CREAM = RGBColor(0xFF, 0xFD, 0xF5)
INK = RGBColor(0x1E, 0x29, 0x3B)
TEXT = RGBColor(0x33, 0x41, 0x55)
MUTED = RGBColor(0x64, 0x74, 0x8B)
LINE = RGBColor(0xE2, 0xE8, 0xF0)
VIOLET = RGBColor(0x8B, 0x5C, 0xF6)
PINK = RGBColor(0xF4, 0x72, 0xB6)
YELLOW = RGBColor(0xFB, 0xBF, 0x24)
MINT = RGBColor(0x34, 0xD3, 0x99)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

FONT = "Inter"
FONT_EA = "Source Han Sans SC"
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
M = Inches(0.55)


def apply_typeface(run, font=FONT):
    run.font.name = font
    r_pr = run._r.get_or_add_rPr()
    for tag in (
        "{http://schemas.openxmlformats.org/drawingml/2006/main}latin",
        "{http://schemas.openxmlformats.org/drawingml/2006/main}ea",
        "{http://schemas.openxmlformats.org/drawingml/2006/main}cs",
    ):
        for child in list(r_pr):
            if child.tag == tag:
                r_pr.remove(child)
    latin = OxmlElement("a:latin")
    latin.set("typeface", font)
    ea = OxmlElement("a:ea")
    ea.set("typeface", FONT_EA)
    cs = OxmlElement("a:cs")
    cs.set("typeface", font)
    r_pr.append(latin)
    r_pr.append(ea)
    r_pr.append(cs)


def patch_theme_fonts(pptx_path: str):
    path = Path(pptx_path)
    tmp = path.with_suffix(".tmp.pptx")
    with zipfile.ZipFile(path, "r") as src, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as dst:
        for item in src.infolist():
            data = src.read(item.filename)
            if item.filename == "ppt/theme/theme1.xml":
                text = data.decode("utf-8")
                text = text.replace('<a:latin typeface="+mn-lt"/>', f'<a:latin typeface="{FONT}"/>')
                text = text.replace('<a:latin typeface="+mj-lt"/>', f'<a:latin typeface="{FONT}"/>')
                text = text.replace('<a:latin typeface="Calibri"/>', f'<a:latin typeface="{FONT}"/>')
                text = text.replace('<a:ea typeface=""/>', f'<a:ea typeface="{FONT_EA}"/>')
                text = text.replace('script="Hans" typeface="宋体"', f'script="Hans" typeface="{FONT_EA}"')
                data = text.encode("utf-8")
            dst.writestr(item, data)
    tmp.replace(path)


def shape(slide, kind, left, top, width, height, fill, line=None, weight=1.5, rotation=0):
    s = slide.shapes.add_shape(kind, left, top, width, height)
    s.fill.solid()
    s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(weight)
    s.rotation = rotation
    s.shadow.inherit = False
    return s


def text(slide, value, left, top, width, height, *, size=16, color=INK,
         bold=False, align=PP_ALIGN.LEFT, valign=MSO_ANCHOR.TOP, line_spacing=1.0):
    box = slide.shapes.add_textbox(left, top, width, height)
    frame = box.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.margin_left = 0
    frame.margin_right = 0
    frame.margin_top = 0
    frame.margin_bottom = 0
    frame.vertical_anchor = valign
    p = frame.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    run = p.add_run()
    run.text = value
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    apply_typeface(run)
    return box


def line(slide, x1, y1, x2, y2, color=INK, weight=2):
    c = slide.shapes.add_connector(1, x1, y1, x2, y2)
    c.line.color.rgb = color
    c.line.width = Pt(weight)
    return c


def bg(slide, page, section):
    shape(slide, MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H, CREAM)
    shape(slide, MSO_SHAPE.OVAL, Inches(-0.7), Inches(-0.55), Inches(2.3), Inches(2.3), YELLOW)
    shape(slide, MSO_SHAPE.OVAL, SLIDE_W - Inches(1.55), Inches(0.72), Inches(0.8), Inches(0.8), PINK)
    shape(slide, MSO_SHAPE.ISOSCELES_TRIANGLE, SLIDE_W - Inches(1.4), SLIDE_H - Inches(1.2), Inches(0.9), Inches(0.9), MINT, rotation=18)
    text(slide, f"PLAYFUL GEOMETRIC | {section}", M, Inches(0.28), Inches(4.2), Inches(0.18), size=8, color=MUTED, bold=True)
    text(slide, f"{page:02d} / 07", SLIDE_W - Inches(1.6), Inches(0.28), Inches(1.05), Inches(0.18), size=8, color=MUTED, bold=True, align=PP_ALIGN.RIGHT)


def sticker(slide, left, top, width, height, fill=WHITE, shadow=LINE, radius=True):
    kind = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shape(slide, kind, left + Inches(0.08), top + Inches(0.08), width, height, shadow)
    return shape(slide, kind, left, top, width, height, fill, INK, 2)


def badge(slide, value, left, top, fill=YELLOW, width=Inches(1.55)):
    sticker(slide, left, top, width, Inches(0.34), fill, INK)
    text(slide, value, left + Inches(0.08), top + Inches(0.095), width - Inches(0.16), Inches(0.12), size=7.5, color=INK, bold=True, align=PP_ALIGN.CENTER)


def slide_cover(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bg(s, 1, "FRONT STICKER")
    sticker(s, M, Inches(1.05), Inches(7.75), Inches(3.75), WHITE, VIOLET)
    badge(s, "KAMI DEMO", M + Inches(0.35), Inches(1.35), YELLOW)
    text(s, "把 AI 文档\n排成几何贴纸", M + Inches(0.45), Inches(1.92), Inches(6.75), Inches(1.55), size=44, color=INK, bold=True, line_spacing=0.9)
    text(s, "Stable Grid, Wild Decoration. 内容保持清楚，周围用圆、三角、pill、斜纹和硬阴影制造开心的触感。", M + Inches(0.5), Inches(3.75), Inches(6.3), Inches(0.5), size=13, color=TEXT, line_spacing=1.15)
    sticker(s, Inches(8.95), Inches(1.35), Inches(3.2), Inches(1.25), MINT, INK)
    text(s, "No stale frame", Inches(9.18), Inches(1.72), Inches(2.7), Inches(0.25), size=16, color=INK, bold=True, align=PP_ALIGN.CENTER)
    sticker(s, Inches(9.15), Inches(3.0), Inches(2.75), Inches(1.55), PINK, INK)
    text(s, "Primitive\nShapes", Inches(9.45), Inches(3.38), Inches(2.1), Inches(0.55), size=19, color=INK, bold=True, align=PP_ALIGN.CENTER)


def slide_tokens(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bg(s, 2, "TOKENS")
    text(s, "明亮色彩，像贴纸盒", M, Inches(1.05), Inches(6.5), Inches(0.5), size=30, bold=True)
    colors = [("Violet", VIOLET), ("Pink", PINK), ("Amber", YELLOW), ("Mint", MINT)]
    for i, (name, color) in enumerate(colors):
        x = M + Inches(2.95) * i
        sticker(s, x, Inches(2.05), Inches(2.45), Inches(2.1), color, INK)
        text(s, name, x, Inches(2.85), Inches(2.45), Inches(0.28), size=18, color=WHITE if name == "Violet" else INK, bold=True, align=PP_ALIGN.CENTER)
    text(s, "颜色不是给旧方框换皮，而是轮流成为 sticker、badge、shadow、shape。", M, Inches(5.15), Inches(8.6), Inches(0.35), size=14, color=TEXT)


def slide_grid(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bg(s, 3, "STABLE GRID")
    text(s, "稳定网格，野生装饰", M, Inches(0.95), Inches(5.8), Inches(0.5), size=30, bold=True)
    left, top = M, Inches(1.9)
    w, h = Inches(3.55), Inches(1.7)
    for i, (title, fill) in enumerate([("Hero Card", WHITE), ("Side Bubble", MINT), ("Metric Sticker", YELLOW), ("Action Pop", PINK)]):
        x = left + Inches(3.0) * (i % 2)
        y = top + Inches(2.05) * (i // 2)
        sticker(s, x, y, w, h, fill, INK)
        badge(s, f"0{i+1}", x + Inches(0.22), y + Inches(0.22), VIOLET, Inches(0.65))
        text(s, title, x + Inches(0.28), y + Inches(0.76), w - Inches(0.56), Inches(0.32), size=18, bold=True, align=PP_ALIGN.CENTER)
    shape(s, MSO_SHAPE.OVAL, Inches(8.7), Inches(2.0), Inches(2.2), Inches(2.2), YELLOW)
    shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.0), Inches(4.55), Inches(3.5), Inches(0.75), VIOLET, None, rotation=-7)
    text(s, "结构稳定，装饰可以玩。", Inches(8.05), Inches(3.1), Inches(3.25), Inches(0.45), size=23, bold=True, align=PP_ALIGN.CENTER)


def slide_outputs(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bg(s, 4, "OUTPUTS")
    text(s, "PDF 与 PPT 使用同一套几何语言", M, Inches(1.05), Inches(8.8), Inches(0.5), size=30, bold=True)
    rows = [("One-pager", "hero sticker + metric chips + action pop"),
            ("Long-doc", "cover stickers + bouncy toc + proof sidebar"),
            ("Letter", "speech bubble title + proof pops + rounded body")]
    for i, (name, desc) in enumerate(rows):
        y = Inches(2.0 + i * 1.25)
        sticker(s, M, y, Inches(10.8), Inches(0.8), [WHITE, MINT, PINK][i], INK)
        text(s, name, M + Inches(0.35), y + Inches(0.22), Inches(2.2), Inches(0.22), size=16, bold=True)
        text(s, desc, M + Inches(3.0), y + Inches(0.23), Inches(6.8), Inches(0.22), size=13, color=TEXT)


def slide_end(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bg(s, 5, "FINAL")
    sticker(s, M, Inches(1.3), Inches(8.2), Inches(3.0), WHITE, YELLOW)
    text(s, "不是换色。\n是换成贴纸世界。", M + Inches(0.45), Inches(1.85), Inches(7.25), Inches(1.1), size=38, bold=True, line_spacing=0.9)
    shape(s, MSO_SHAPE.OVAL, Inches(9.35), Inches(1.55), Inches(2.45), Inches(2.45), PINK)
    shape(s, MSO_SHAPE.ISOSCELES_TRIANGLE, Inches(9.1), Inches(4.1), Inches(1.1), Inches(1.1), MINT, rotation=-15)
    text(s, "Friendly. Tactile. Pop. Energetic.", M + Inches(0.5), Inches(3.55), Inches(6.8), Inches(0.35), size=16, color=TEXT)


def main():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    for fn in (slide_cover, slide_tokens, slide_grid, slide_outputs, slide_end):
        fn(prs)
    out = Path(__file__).resolve().parent / "output.pptx"
    prs.save(out)
    patch_theme_fonts(str(out))


if __name__ == "__main__":
    main()
