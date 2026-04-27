#!/usr/bin/env python3
"""Render a Neo-Brutalism Slidev deck from the shared slide schema."""

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


def panel(
    inner: str,
    left: float,
    top: float,
    width: float,
    height: float,
    *,
    tone: str = "paper",
    rotation: float = 0.0,
    text_tone: str = "ink",
    extra_class: str = "",
) -> str:
    classes = ["neo-panel", f"tone-{tone}", f"text-{text_tone}"]
    if extra_class:
        classes.append(extra_class)
    joined = " ".join(classes)
    return f'<section class="{joined}" style="{box(left, top, width, height, rotation=rotation)}">{inner}</section>'


def pill(value: str, *, tone: str = "yellow") -> str:
    return f'<div class="neo-pill tone-{tone}">{escape(value)}</div>'


def header(slide: dict) -> str:
    return (
        '<div class="edge-dots edge-dots-top"></div>'
        '<div class="edge-dots edge-dots-bottom"></div>'
        '<div class="bg-chip bg-chip-red"></div>'
        '<div class="bg-chip bg-chip-yellow"></div>'
        f'<div class="neo-label">NEO BRUTALISM | {escape(slide["section"])}</div>'
        f'<div class="neo-page">{slide["page"]:02d} / {TOTAL_SLIDES:02d}</div>'
    )


def render_cover(slide: dict) -> str:
    hero = panel(
        (
            '<div class="cover-panel-content">'
            f'{pill(slide["eyebrow"], tone="yellow")}'
            f'<h1 class="cover-title">{text_to_html(slide["title"])}</h1>'
            f'<p class="cover-strap">{escape(slide["strapline"])}</p>'
            "</div>"
        ),
        0.55,
        1.05,
        7.60,
        3.90,
        tone=slide["hero_tone"],
        rotation=-1.2,
        extra_class="hero-panel",
    )
    first, second = slide["stickers"]
    sticker_a = panel(
        f'<div class="sticker-copy">{text_to_html(first["text"])}</div>',
        8.95,
        1.35,
        3.00,
        1.25,
        tone=first["tone"],
        rotation=2.0,
        text_tone=first["text_tone"],
        extra_class="sticker-panel center-copy",
    )
    sticker_b = panel(
        f'<div class="sticker-copy">{text_to_html(second["text"])}</div>',
        8.75,
        3.35,
        3.25,
        1.35,
        tone=second["tone"],
        rotation=-3.0,
        text_tone=second["text_tone"],
        extra_class="sticker-panel center-copy",
    )
    return f'<div class="neo-stage cover-stage">{header(slide)}{hero}{sticker_a}{sticker_b}</div>'


def render_tokens(slide: dict) -> str:
    parts = [f'<div class="neo-stage tokens-stage">{header(slide)}']
    parts.append(f'<div class="section-title" style="{box(0.55, 1.02, 5.80, 0.45)}">{escape(slide["title"])}</div>')
    for index, card in enumerate(slide["cards"]):
        left = 0.55 + 2.95 * index
        parts.append(
            panel(
                (
                    '<div class="token-card-inner">'
                    f'<div class="token-name">{escape(card["name"])}</div>'
                    '<div class="token-rule"></div>'
                    "</div>"
                ),
                left,
                2.10,
                2.42,
                2.05,
                tone=card["tone"],
                rotation=-2.0 + index,
                text_tone=card["text_tone"],
                extra_class="token-card center-copy",
            )
        )
    parts.append(f'<div class="support-copy" style="{box(0.55, 5.22, 8.70, 0.34)}">{escape(slide["summary"])}</div>')
    parts.append("</div>")
    return "".join(parts)


def render_composition(slide: dict) -> str:
    hero = slide["hero"]
    first, second = slide["stickers"]
    parts = [f'<div class="neo-stage composition-stage">{header(slide)}']
    parts.append(f'<div class="section-title" style="{box(0.55, 0.94, 5.90, 0.45)}">{escape(slide["title"])}</div>')
    parts.append(
        panel(
            f'<div class="composition-hero">{text_to_html(hero["text"])}</div>',
            0.55,
            1.80,
            5.20,
            3.20,
            tone=hero["tone"],
            rotation=1.0,
            text_tone=hero["text_tone"],
            extra_class="composition-panel",
        )
    )
    parts.append(
        panel(
            f'<div class="badge-copy">{text_to_html(first["text"])}</div>',
            7.10,
            1.55,
            4.10,
            1.25,
            tone=first["tone"],
            rotation=-2.0,
            text_tone=first["text_tone"],
            extra_class="composition-sticker center-copy",
        )
    )
    parts.append(
        panel(
            f'<div class="sticker-copy">{text_to_html(second["text"])}</div>',
            7.55,
            3.35,
            3.70,
            1.35,
            tone=second["tone"],
            rotation=3.0,
            text_tone=second["text_tone"],
            extra_class="composition-sticker center-copy",
        )
    )
    parts.append("</div>")
    return "".join(parts)


def render_outputs(slide: dict) -> str:
    parts = [f'<div class="neo-stage outputs-stage">{header(slide)}']
    parts.append(f'<div class="section-title wide" style="{box(0.55, 1.02, 9.20, 0.45)}">{escape(slide["title"])}</div>')
    for index, row in enumerate(slide["rows"]):
        top = 2.05 + 1.22 * index
        parts.append(
            panel(
                (
                    '<div class="output-row-inner">'
                    f'<div class="output-name">{escape(row["name"])}</div>'
                    f'<div class="output-desc">{escape(row["desc"])}</div>'
                    "</div>"
                ),
                0.55,
                top,
                10.60,
                0.78,
                tone=row["tone"],
                rotation=row["rotation"],
                text_tone=row["text_tone"],
                extra_class="output-row",
            )
        )
    parts.append("</div>")
    return "".join(parts)


def render_end(slide: dict) -> str:
    badge = slide["badge"]
    hero = panel(
        f'<div class="end-title">{text_to_html(slide["title"])}</div>',
        0.55,
        1.30,
        8.20,
        3.00,
        tone=slide["hero_tone"],
        rotation=-2.0,
        extra_class="end-hero",
    )
    side = panel(
        f'<div class="badge-copy large">{text_to_html(badge["text"])}</div>',
        9.25,
        1.55,
        2.55,
        2.25,
        tone=badge["tone"],
        rotation=8.0,
        text_tone=badge["text_tone"],
        extra_class="end-badge center-copy",
    )
    return f'<div class="neo-stage end-stage">{header(slide)}{hero}{side}</div>'


RENDERERS = {
    "cover": render_cover,
    "tokens": render_tokens,
    "composition": render_composition,
    "outputs": render_outputs,
    "end": render_end,
}


def main() -> None:
    frontmatter = """---
theme: default
title: Kami · Neo-Brutalism
titleTemplate: '%s'
info: Online slide deck companion for the Neo-Brutalism skill.
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
