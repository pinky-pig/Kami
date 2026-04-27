#!/usr/bin/env python3
"""Render a Sketch Slidev deck from the shared slide schema."""

from __future__ import annotations

from html import escape
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))

from slides_spec import DECK, TOTAL_SLIDES  # noqa: E402


PX_PER_INCH = 96


def px(value: float) -> str:
    return f"{value * PX_PER_INCH:.2f}px"


def box(left: float, top: float, width: float, height: float, *, rotation: float | None = None) -> str:
    style = f"left:{px(left)};top:{px(top)};width:{px(width)};height:{px(height)};"
    if rotation is not None:
        style += f"--rot:{rotation:.2f}deg;"
    return style


def text_to_html(text: str) -> str:
    return "<br />".join(escape(part) for part in text.split("\n"))


def header(slide: dict) -> str:
    return (
        f'<div class="board-label">SKETCH | {escape(slide["section"])}</div>'
        f'<div class="board-page">{slide["page"]:02d} / {TOTAL_SLIDES:02d}</div>'
    )


def scribble(class_name: str, left: float, top: float, width: float, rotation: float, color: str = "secondary") -> str:
    return (
        f'<div class="scribble {class_name} {color}" '
        f'style="left:{px(left)};top:{px(top)};width:{px(width)};--rot:{rotation:.2f}deg;"></div>'
    )


def card(
    inner: str,
    left: float,
    top: float,
    width: float,
    height: float,
    *,
    fill: str = "card",
    rotation: float = 0.0,
    attachment: str = "",
    extra_class: str = "",
) -> str:
    classes = ["paper-card", f"tone-{fill}"]
    if attachment:
        classes.append(attachment)
    if extra_class:
        classes.append(extra_class)
    joined = " ".join(classes)
    return f'<section class="{joined}" style="{box(left, top, width, height, rotation=rotation)}">{inner}</section>'


def render_cover(slide: dict) -> str:
    body = [
        '<div class="sketch-board cover-board">',
        header(slide),
        scribble("cover-link", 7.35, 3.10, 1.72, -17.0),
        card(
            (
                '<div class="hero-card-inner">'
                f'<h1 class="hero-title">{text_to_html(slide["title"])}</h1>'
                f'<p class="hero-subtitle">{escape(slide["subtitle"])}</p>'
                "</div>"
            ),
            0.55,
            1.00,
            7.20,
            4.55,
            fill="card",
            rotation=-2.0,
            attachment="tape",
            extra_class="hero-card",
        ),
        card(
            (
                '<div class="sticky-inner center">'
                f'<div class="sticky-label accent">{escape(slide["sticky"]["label"])}</div>'
                f'<div class="sticky-copy">{text_to_html(slide["sticky"]["body"])}</div>'
                "</div>"
            ),
            8.80,
            1.35,
            3.10,
            1.55,
            fill="note",
            rotation=2.0,
            attachment="tack",
            extra_class="corner-sticky",
        ),
        "</div>",
    ]
    return "".join(body)


def render_tokens(slide: dict) -> str:
    body = ['<div class="sketch-board">', header(slide)]
    body.append(f'<div class="slide-title" style="{box(0.55, 0.90, 6.80, 0.40)}">{escape(slide["title"])}</div>')
    for index, item in enumerate(slide["cards"]):
        left = 0.55 + 2.95 * index
        inner = (
            '<div class="token-card-inner">'
            f'<div class="token-name">{escape(item["label"])}</div>'
            f'<div class="token-dot {escape(item["dot"])}"></div>'
            "</div>"
        )
        body.append(
            card(
                inner,
                left,
                2.00,
                2.35,
                2.10,
                fill=item["fill"],
                rotation=item["rotation"],
                attachment=item["attachment"],
                extra_class="token-card",
            )
        )
    body.append(f'<div class="summary-copy" style="{box(0.55, 5.35, 8.60, 0.28)}">{escape(slide["summary"])}</div>')
    body.append("</div>")
    return "".join(body)


def render_system(slide: dict) -> str:
    body = ['<div class="sketch-board">', header(slide)]
    body.append(f'<div class="slide-title" style="{box(0.55, 0.92, 8.40, 0.40)}">{escape(slide["title"])}</div>')
    for index, item in enumerate(slide["cards"]):
        left = 0.55 + 3.90 * index
        inner = (
            '<div class="system-card-inner">'
            f'<div class="system-name">{escape(item["label"])}</div>'
            f'<div class="system-body">{escape(item["body"])}</div>'
            "</div>"
        )
        body.append(
            card(
                inner,
                left,
                1.95,
                3.00,
                2.45,
                fill=item["fill"],
                rotation=item["rotation"],
                attachment=item["attachment"],
                extra_class="system-card",
            )
        )
    body.append(scribble("system-line", 1.85, 5.38, 9.45, -1.6, color="accent"))
    body.append(f'<div class="system-summary" style="{box(2.00, 4.98, 9.40, 0.28)}">{escape(slide["summary"])}</div>')
    body.append("</div>")
    return "".join(body)


def render_outputs(slide: dict) -> str:
    body = ['<div class="sketch-board">', header(slide)]
    body.append(f'<div class="slide-title" style="{box(0.55, 0.90, 8.80, 0.40)}">{escape(slide["title"])}</div>')
    for index, row in enumerate(slide["rows"]):
        top = 1.90 + 1.28 * index
        left = 0.55 + row["offset"]
        inner = (
            '<div class="output-row-inner">'
            f'<div class="output-name">{escape(row["name"])}</div>'
            f'<div class="output-desc">{escape(row["desc"])}</div>'
            "</div>"
        )
        body.append(
            card(
                inner,
                left,
                top,
                10.90,
                0.82,
                fill=row["fill"],
                rotation=row["rotation"],
                attachment=row["attachment"],
                extra_class="output-row",
            )
        )
    body.append("</div>")
    return "".join(body)


def render_end(slide: dict) -> str:
    body = [
        '<div class="sketch-board end-board">',
        header(slide),
        card(
            (
                '<div class="hero-card-inner">'
                f'<h1 class="hero-title small">{text_to_html(slide["title"])}</h1>'
                f'<p class="closing-copy">{escape(slide["summary"])}</p>'
                "</div>"
            ),
            0.55,
            1.25,
            7.80,
            3.50,
            fill="card",
            rotation=-2.0,
            attachment="tape",
            extra_class="hero-card end-hero",
        ),
        card(
            (
                '<div class="sticky-inner center">'
                f'<div class="sticky-copy">{escape(slide["sticky"]["label"])}</div>'
                f'<div class="sticky-copy">{escape(slide["sticky"]["body"])}</div>'
                "</div>"
            ),
            9.10,
            1.65,
            2.45,
            1.20,
            fill="note",
            rotation=2.0,
            attachment="tack",
            extra_class="closing-sticky",
        ),
        "</div>",
    ]
    return "".join(body)


RENDERERS = {
    "cover": render_cover,
    "tokens": render_tokens,
    "system": render_system,
    "outputs": render_outputs,
    "end": render_end,
}


def main() -> None:
    frontmatter = """---
theme: default
title: Kami · Sketch
titleTemplate: '%s'
info: Online slide deck companion for the Sketch skill.
colorSchema: light
canvasWidth: 1280
aspectRatio: 16/9
transition: fade
drawings: false
mdc: true
routerMode: hash
---
"""
    slides = [frontmatter, "<!-- Generated from slides_spec.py. Do not edit by hand. -->"]
    for slide in DECK:
        slides.append(RENDERERS[slide["kind"]](slide))
        slides.append("---")
    output = "\n\n".join(slides[:-1]) + "\n"
    (ROOT / "slides.md").write_text(output, encoding="utf-8")
    print("✓ rendered slides.md from slides_spec.py")


if __name__ == "__main__":
    main()
