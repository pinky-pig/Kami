#!/usr/bin/env python3
"""Prompt-native Sketch slide deck generator."""

from __future__ import annotations

import zipfile
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.xmlchemy import OxmlElement
from pptx.util import Inches, Pt


PAPER = RGBColor(0xFD, 0xFB, 0xF7)
INK = RGBColor(0x2D, 0x2D, 0x2D)
MUTED = RGBColor(0xE5, 0xE0, 0xD8)
ACCENT = RGBColor(0xFF, 0x4D, 0x4D)
BLUE = RGBColor(0x2D, 0x5D, 0xA1)
NOTE = RGBColor(0xFF, 0xF9, 0xC4)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

HEADING_FONT = "Marker Felt"
BODY_FONT = "Noteworthy"
FONT_EA = "LXGW WenKai"
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
M = Inches(0.55)


def apply_typeface(run, latin_font=BODY_FONT, ea_font=FONT_EA):
    run.font.name = latin_font
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
    latin.set("typeface", latin_font)
    ea = OxmlElement("a:ea")
    ea.set("typeface", ea_font)
    cs = OxmlElement("a:cs")
    cs.set("typeface", latin_font)
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
                text = text.replace('<a:latin typeface="+mn-lt"/>', f'<a:latin typeface="{BODY_FONT}"/>')
                text = text.replace('<a:latin typeface="+mj-lt"/>', f'<a:latin typeface="{HEADING_FONT}"/>')
                text = text.replace('<a:latin typeface="Calibri"/>', f'<a:latin typeface="{BODY_FONT}"/>')
                text = text.replace('<a:ea typeface=""/>', f'<a:ea typeface="{FONT_EA}"/>')
                data = text.encode("utf-8")
            dst.writestr(item, data)
    tmp.replace(path)


def shape(slide, kind, left, top, width, height, fill, line=INK, weight=2.3, rotation=0):
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
         bold=False, align=PP_ALIGN.LEFT, valign=MSO_ANCHOR.TOP,
         line_spacing=1.0, latin_font=BODY_FONT, ea_font=FONT_EA):
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
    apply_typeface(run, latin_font=latin_font, ea_font=ea_font)
    return box


def dots(slide):
    for row in range(8):
        for col in range(16):
            x = Inches(0.35 + col * 0.82)
            y = Inches(0.28 + row * 0.92)
            shape(slide, MSO_SHAPE.OVAL, x, y, Inches(0.045), Inches(0.045), MUTED, line=None)


def note_card(slide, left, top, width, height, *, fill=WHITE, rotation=0, tape=False, tack=False):
    shadow = shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.08), top + Inches(0.08), width, height, INK, line=None, rotation=rotation)
    card = shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height, fill, line=INK, weight=2.4, rotation=rotation)
    if tape:
        tape_shape = shape(slide, MSO_SHAPE.RECTANGLE, left + width / 2 - Inches(0.38), top - Inches(0.12), Inches(0.76), Inches(0.18), MUTED, line=INK, weight=1.1, rotation=rotation - 6)
        tape_shape.fill.fore_color.rgb = MUTED
    if tack:
        shape(slide, MSO_SHAPE.OVAL, left + width / 2 - Inches(0.07), top - Inches(0.06), Inches(0.14), Inches(0.14), ACCENT, line=INK, weight=1.4)
    return shadow, card


def scribble(slide, x1, y1, x2, y2, color=BLUE):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, x1, y1, x2, y2)
    c.line.color.rgb = color
    c.line.width = Pt(2.4)
    return c


def bg(slide, page, section):
    shape(slide, MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H, PAPER, line=None)
    dots(slide)
    text(slide, f"SKETCH | {section}", M, Inches(0.22), Inches(4.1), Inches(0.2), size=8, color=BLUE, bold=True, latin_font=HEADING_FONT)
    text(slide, f"{page:02d} / 05", SLIDE_W - Inches(1.5), Inches(0.22), Inches(0.95), Inches(0.2), size=8, color=INK, bold=True, align=PP_ALIGN.RIGHT, latin_font=HEADING_FONT)


def slide_cover(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bg(s, 1, "NOTE WALL")
    note_card(s, M, Inches(1.0), Inches(7.2), Inches(4.55), fill=WHITE, rotation=-2, tape=True)
    text(s, "把文档贴成\n草图墙", M + Inches(0.42), Inches(1.78), Inches(5.9), Inches(1.2), size=38, bold=True, line_spacing=0.92, latin_font=HEADING_FONT)
    text(s, "纸张纹理、手写字体、wobble 边框、硬偏移阴影。看起来像 brainstorm 现场，而不是 polished 年报。", M + Inches(0.42), Inches(3.48), Inches(5.8), Inches(0.62), size=14, color=INK, line_spacing=1.15)
    note_card(s, Inches(8.8), Inches(1.35), Inches(3.1), Inches(1.55), fill=NOTE, rotation=2, tack=True)
    text(s, "Now", Inches(9.2), Inches(1.72), Inches(0.9), Inches(0.25), size=18, color=ACCENT, bold=True, latin_font=HEADING_FONT, align=PP_ALIGN.CENTER)
    text(s, "不做直线排版。\n做一面工作板。", Inches(9.1), Inches(2.05), Inches(2.45), Inches(0.55), size=16, bold=True, latin_font=HEADING_FONT, align=PP_ALIGN.CENTER)
    scribble(s, Inches(7.35), Inches(3.15), Inches(8.95), Inches(2.25))


def slide_tokens(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bg(s, 2, "TOKENS")
    text(s, "四种手绘信号", M, Inches(0.9), Inches(6.8), Inches(0.4), size=28, bold=True, latin_font=HEADING_FONT)
    cards = [
        ("Paper", WHITE, -2),
        ("Post-it", NOTE, 1.8),
        ("Red Marker", WHITE, -1),
        ("Blue Pen", WHITE, 2),
    ]
    for i, (label, fill, rot) in enumerate(cards):
        x = M + Inches(2.95) * i
        note_card(s, x, Inches(2.0), Inches(2.35), Inches(2.1), fill=fill, rotation=rot, tape=i % 2 == 0, tack=i % 2 == 1)
        text(s, label, x + Inches(0.24), Inches(2.55), Inches(1.9), Inches(0.3), size=16, bold=True, align=PP_ALIGN.CENTER, latin_font=HEADING_FONT)
        color = [INK, INK, ACCENT, BLUE][i]
        shape(s, MSO_SHAPE.OVAL, x + Inches(0.93), Inches(3.23), Inches(0.5), Inches(0.5), color, line=INK, weight=1.5)
    text(s, "Warm paper + handwritten type + hard offset shadow + small rotation.", M, Inches(5.35), Inches(8.5), Inches(0.24), size=13, color=INK)


def slide_system(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bg(s, 3, "SYSTEM")
    text(s, "不是换色，是换工作现场", M, Inches(0.92), Inches(8.4), Inches(0.42), size=28, bold=True, latin_font=HEADING_FONT)
    items = [
        ("No straight lines", WHITE, -2.4, True, False),
        ("Tape / tack", NOTE, 1.2, False, True),
        ("Hard shadow", WHITE, -1.2, False, False),
    ]
    for i, (label, fill, rot, tape, tack) in enumerate(items):
        x = M + Inches(3.9) * i
        note_card(s, x, Inches(1.95), Inches(3.0), Inches(2.45), fill=fill, rotation=rot, tape=tape, tack=tack)
        text(s, label, x + Inches(0.26), Inches(3.05), Inches(2.45), Inches(0.34), size=18, bold=True, align=PP_ALIGN.CENTER, latin_font=HEADING_FONT)
        text(s, "有点歪，有点手写，像刚刚钉上去。", x + Inches(0.22), Inches(3.72), Inches(2.48), Inches(0.34), size=11.5, color=INK, align=PP_ALIGN.CENTER)
    scribble(s, Inches(1.85), Inches(5.5), Inches(11.25), Inches(5.25), color=ACCENT)
    text(s, "所有重点模块都应该像卡片，不像软件面板。", Inches(2.0), Inches(5.02), Inches(9.4), Inches(0.26), size=13, color=ACCENT, bold=True, align=PP_ALIGN.CENTER, latin_font=HEADING_FONT)


def slide_outputs(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bg(s, 4, "OUTPUTS")
    text(s, "PDF 与 PPT 共用手绘语言", M, Inches(0.9), Inches(8.8), Inches(0.42), size=28, bold=True, latin_font=HEADING_FONT)
    rows = [
        ("One-pager", "taped hero + side note + 3 stickies"),
        ("Long-doc", "pin-board cover + article sheet + fact notes"),
        ("Letter", "header board + dashed subject + proof notes"),
    ]
    fills = [WHITE, NOTE, WHITE]
    rots = [-1.4, 1.1, -0.8]
    for i, (name, desc) in enumerate(rows):
        y = Inches(1.9 + i * 1.28)
        note_card(s, M + Inches(0.2 if i == 1 else 0), y, Inches(10.9), Inches(0.82), fill=fills[i], rotation=rots[i], tape=i == 0, tack=i == 2)
        text(s, name, M + Inches(0.34), y + Inches(0.22), Inches(2.0), Inches(0.2), size=15.5, bold=True, latin_font=HEADING_FONT)
        text(s, desc, M + Inches(2.75), y + Inches(0.23), Inches(6.8), Inches(0.2), size=12.2, color=INK)


def slide_end(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bg(s, 5, "FINAL")
    note_card(s, M, Inches(1.25), Inches(7.8), Inches(3.5), fill=WHITE, rotation=-2, tape=True)
    text(s, "不是改配色。\n是整面换成手绘草稿。", M + Inches(0.42), Inches(1.95), Inches(6.9), Inches(1.0), size=34, bold=True, line_spacing=0.92, latin_font=HEADING_FONT)
    note_card(s, Inches(9.1), Inches(1.65), Inches(2.45), Inches(1.2), fill=NOTE, rotation=2, tack=True)
    text(s, "Messy\non purpose", Inches(9.36), Inches(1.96), Inches(1.95), Inches(0.46), size=15, bold=True, align=PP_ALIGN.CENTER, latin_font=HEADING_FONT)
    text(s, "Warm. Human. Playful. Deliberately unfinished.", M + Inches(0.46), Inches(3.68), Inches(6.5), Inches(0.26), size=14, color=BLUE, bold=True, latin_font=HEADING_FONT)


def main():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    for fn in (slide_cover, slide_tokens, slide_system, slide_outputs, slide_end):
        fn(prs)
    out = Path(__file__).resolve().parent / "output.pptx"
    prs.save(out)
    patch_theme_fonts(str(out))


if __name__ == "__main__":
    main()
