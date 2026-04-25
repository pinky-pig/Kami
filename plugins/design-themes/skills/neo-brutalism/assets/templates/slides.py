#!/usr/bin/env python3
"""Prompt-native Neo Brutalism slide deck generator."""

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
BLACK = RGBColor(0x00, 0x00, 0x00)
RED = RGBColor(0xFF, 0x6B, 0x6B)
YELLOW = RGBColor(0xFF, 0xD9, 0x3D)
VIOLET = RGBColor(0xC4, 0xB5, 0xFD)
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
    latin = OxmlElement("a:latin"); latin.set("typeface", font)
    ea = OxmlElement("a:ea"); ea.set("typeface", FONT_EA)
    cs = OxmlElement("a:cs"); cs.set("typeface", font)
    r_pr.append(latin); r_pr.append(ea); r_pr.append(cs)


def patch_theme_fonts(pptx_path: str):
    path = Path(pptx_path)
    tmp = path.with_suffix(".tmp.pptx")
    with zipfile.ZipFile(path, "r") as src, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as dst:
        for item in src.infolist():
            data = src.read(item.filename)
            if item.filename == "ppt/theme/theme1.xml":
                text_xml = data.decode("utf-8")
                text_xml = text_xml.replace('<a:latin typeface="+mn-lt"/>', f'<a:latin typeface="{FONT}"/>')
                text_xml = text_xml.replace('<a:latin typeface="+mj-lt"/>', f'<a:latin typeface="{FONT}"/>')
                text_xml = text_xml.replace('<a:latin typeface="Calibri"/>', f'<a:latin typeface="{FONT}"/>')
                text_xml = text_xml.replace('<a:ea typeface=""/>', f'<a:ea typeface="{FONT_EA}"/>')
                text_xml = text_xml.replace('script="Hans" typeface="宋体"', f'script="Hans" typeface="{FONT_EA}"')
                data = text_xml.encode("utf-8")
            dst.writestr(item, data)
    tmp.replace(path)


def shape(slide, kind, left, top, width, height, fill, line=None, weight=3, rotation=0):
    s = slide.shapes.add_shape(kind, left, top, width, height)
    s.fill.solid(); s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line; s.line.width = Pt(weight)
    s.rotation = rotation
    s.shadow.inherit = False
    return s


def text(slide, value, left, top, width, height, *, size=16, color=BLACK,
         bold=True, align=PP_ALIGN.LEFT, valign=MSO_ANCHOR.TOP, line_spacing=1.0):
    box = slide.shapes.add_textbox(left, top, width, height)
    frame = box.text_frame
    frame.clear(); frame.word_wrap = True
    frame.margin_left = 0; frame.margin_right = 0; frame.margin_top = 0; frame.margin_bottom = 0
    frame.vertical_anchor = valign
    p = frame.paragraphs[0]; p.alignment = align; p.line_spacing = line_spacing
    run = p.add_run(); run.text = value
    run.font.size = Pt(size); run.font.bold = bold; run.font.color.rgb = color
    apply_typeface(run)
    return box


def bg(slide, page, section):
    shape(slide, MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H, CREAM)
    for x in [1.0, 2.35, 3.7, 5.05, 6.4, 7.75, 9.1, 10.45, 11.8]:
        shape(slide, MSO_SHAPE.OVAL, Inches(x), Inches(0.25), Inches(0.04), Inches(0.04), BLACK)
        shape(slide, MSO_SHAPE.OVAL, Inches(x), Inches(6.9), Inches(0.04), Inches(0.04), BLACK)
    shape(slide, MSO_SHAPE.RECTANGLE, Inches(-0.5), Inches(0.95), Inches(2.3), Inches(1.15), RED, BLACK, 3, rotation=-8)
    shape(slide, MSO_SHAPE.RECTANGLE, SLIDE_W - Inches(2.3), Inches(5.55), Inches(1.75), Inches(1.0), YELLOW, BLACK, 3, rotation=12)
    text(slide, f"NEO BRUTALISM | {section}", M, Inches(0.25), Inches(4.2), Inches(0.18), size=8)
    text(slide, f"{page:02d} / 05", SLIDE_W - Inches(1.6), Inches(0.25), Inches(1.0), Inches(0.18), size=8, align=PP_ALIGN.RIGHT)


def block(slide, left, top, width, height, fill=WHITE, rotation=0, shadow=True):
    if shadow:
        shape(slide, MSO_SHAPE.RECTANGLE, left + Inches(0.12), top + Inches(0.12), width, height, BLACK, None, rotation=rotation)
    return shape(slide, MSO_SHAPE.RECTANGLE, left, top, width, height, fill, BLACK, 4, rotation=rotation)


def badge(slide, value, left, top, fill=YELLOW, width=Inches(1.65), rotation=0):
    block(slide, left, top, width, Inches(0.34), fill, rotation=rotation, shadow=True)
    text(slide, value, left + Inches(0.08), top + Inches(0.09), width - Inches(0.16), Inches(0.12), size=7, align=PP_ALIGN.CENTER)


def slide_cover(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, 1, "LOUD COVER")
    block(s, M, Inches(1.05), Inches(7.6), Inches(3.9), RED, rotation=-1.2)
    badge(s, "KAMI DEMO", M + Inches(0.35), Inches(1.38), YELLOW)
    text(s, "把 AI 文档\n排成粗野海报", M + Inches(0.45), Inches(1.92), Inches(6.8), Inches(1.55), size=43, line_spacing=0.86)
    text(s, "RAW STRUCTURE / HARD SHADOW / HIGH SATURATION / NO SOFTNESS", M + Inches(0.5), Inches(3.9), Inches(6.4), Inches(0.25), size=11)
    block(s, Inches(8.95), Inches(1.35), Inches(3.0), Inches(1.25), YELLOW, rotation=2)
    text(s, "NO OLD\nFRAME", Inches(9.28), Inches(1.68), Inches(2.3), Inches(0.55), size=20, align=PP_ALIGN.CENTER, line_spacing=0.9)
    block(s, Inches(8.75), Inches(3.35), Inches(3.25), Inches(1.35), BLACK, rotation=-3)
    text(s, "STICKER\nCOLLAGE", Inches(9.05), Inches(3.68), Inches(2.65), Inches(0.55), size=19, color=WHITE, align=PP_ALIGN.CENTER, line_spacing=0.9)


def slide_tokens(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, 2, "TOKENS")
    text(s, "颜色必须大声", M, Inches(1.05), Inches(5.5), Inches(0.5), size=32)
    for i, (name, fill) in enumerate([("RED", RED), ("YELLOW", YELLOW), ("VIOLET", VIOLET), ("BLACK", BLACK)]):
        x = M + Inches(2.95) * i
        block(s, x, Inches(2.1), Inches(2.42), Inches(2.05), fill, rotation=(-2 + i))
        text(s, name, x, Inches(2.86), Inches(2.42), Inches(0.28), size=19, color=WHITE if name == "BLACK" else BLACK, align=PP_ALIGN.CENTER)
    text(s, "没有柔和渐变，没有灰色过渡。每个色块都像贴在墙上的 DIY 海报。", M, Inches(5.2), Inches(8.6), Inches(0.35), size=15)


def slide_layout(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, 3, "COMPOSITION")
    text(s, "有组织的混乱", M, Inches(0.95), Inches(5.5), Inches(0.5), size=32)
    block(s, M, Inches(1.8), Inches(5.2), Inches(3.2), WHITE, rotation=1)
    text(s, "60/40\nASYMMETRY", M + Inches(0.35), Inches(2.35), Inches(4.4), Inches(0.9), size=34, line_spacing=0.82)
    block(s, Inches(7.1), Inches(1.55), Inches(4.1), Inches(1.25), YELLOW, rotation=-2)
    text(s, "ROTATED BADGES", Inches(7.38), Inches(1.95), Inches(3.45), Inches(0.25), size=18, align=PP_ALIGN.CENTER)
    block(s, Inches(7.55), Inches(3.35), Inches(3.7), Inches(1.35), VIOLET, rotation=3)
    text(s, "HARD\nSHADOWS", Inches(7.9), Inches(3.68), Inches(3.0), Inches(0.55), size=22, align=PP_ALIGN.CENTER, line_spacing=0.9)


def slide_outputs(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, 4, "OUTPUTS")
    text(s, "PDF 与 PPT 都要像 zine，不像表格", M, Inches(1.05), Inches(8.8), Inches(0.5), size=30)
    rows = [("ONE-PAGER", "loud hero / marquee / rotated cards"),
            ("LONG-DOC", "poster cover / blocky toc / proof column"),
            ("LETTER", "raw subject bar / massive title / evidence sticker")]
    for i, (name, desc) in enumerate(rows):
        y = Inches(2.05 + i * 1.22)
        block(s, M, y, Inches(10.6), Inches(0.78), [RED, YELLOW, VIOLET][i], rotation=(-1 + i))
        text(s, name, M + Inches(0.25), y + Inches(0.22), Inches(2.3), Inches(0.22), size=16)
        text(s, desc, M + Inches(3.0), y + Inches(0.23), Inches(6.7), Inches(0.22), size=13)


def slide_end(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, 5, "FINAL")
    block(s, M, Inches(1.3), Inches(8.2), Inches(3.0), YELLOW, rotation=-2)
    text(s, "不是换色。\n是换成反精致海报。", M + Inches(0.45), Inches(1.85), Inches(7.25), Inches(1.1), size=38, line_spacing=0.86)
    block(s, Inches(9.25), Inches(1.55), Inches(2.55), Inches(2.25), RED, rotation=8)
    text(s, "ANTI\nBORING", Inches(9.55), Inches(2.05), Inches(2.0), Inches(0.65), size=22, align=PP_ALIGN.CENTER, line_spacing=0.9)


def main():
    prs = Presentation(); prs.slide_width = SLIDE_W; prs.slide_height = SLIDE_H
    for fn in (slide_cover, slide_tokens, slide_layout, slide_outputs, slide_end):
        fn(prs)
    out = Path(__file__).resolve().parent / "output.pptx"
    prs.save(out); patch_theme_fonts(str(out))


if __name__ == "__main__":
    main()
