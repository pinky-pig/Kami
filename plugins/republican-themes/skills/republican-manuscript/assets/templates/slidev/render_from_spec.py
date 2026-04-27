#!/usr/bin/env python3
"""Render Slidev markdown from the shared slide schema."""

from __future__ import annotations

from html import escape
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))

from slides_spec import DECK  # noqa: E402


PX_PER_INCH = 96


def px(value: float) -> str:
    return f"{value * PX_PER_INCH:.2f}px"


def box(left: float, top: float, width: float, height: float) -> str:
    return f"left:{px(left)};top:{px(top)};width:{px(width)};height:{px(height)};"


def text_to_html(text: str) -> str:
    return "<br />".join(escape(part) for part in text.split("\n"))


def footer(slide: dict) -> str:
    return (
        '<div class="folio-footer">'
        f"<span>{escape(slide['section'])}</span>"
        f"<span>{slide['page']:02d} / 08</span>"
        "</div>"
    )


def section_header(slide: dict) -> str:
    return "".join(
        [
            f'<div class="fixed-box section-kicker" style="{box(0.70, 0.58, 2.40, 0.20)}">{slide["number"]:02d} · SECTION</div>',
            f'<div class="fixed-box section-title" style="{box(0.70, 0.92, 5.70, 0.55)}">{escape(slide["title"])}</div>',
            f'<div class="fixed-box section-rule" style="{box(0.70, 1.55, 4.20, 0.02)}"></div>',
            f'<div class="fixed-box section-lede" style="{box(7.00, 0.90, 4.80, 0.76)}">{text_to_html(slide["lede"])}</div>',
        ]
    )


def metric_card(metric: dict, left: float, top: float, width: float) -> str:
    return (
        f'<div class="fixed-box metric-card" style="{box(left, top, width, 1.18)}">'
        f'<div class="metric-value">{escape(metric["value"])}</div>'
        f'<div class="metric-label">{escape(metric["label"])}</div>'
        f'<div class="metric-note">{escape(metric["note"])}</div>'
        "</div>"
    )


def flow_metric_card(metric: dict) -> str:
    return (
        '<div class="metric-card flow-metric-card">'
        f'<div class="metric-value">{escape(metric["value"])}</div>'
        f'<div class="metric-label">{escape(metric["label"])}</div>'
        f'<div class="metric-note">{escape(metric["note"])}</div>'
        "</div>"
    )


def archive_card(card: dict, left: float, top: float, width: float, height: float) -> str:
    label_html = f'<div class="archive-label">{escape(card["label"])}</div>' if card.get("label") else ""
    with_label = " with-label" if card.get("label") else ""
    return (
        f'<div class="fixed-box archive-card{with_label}" style="{box(left, top, width, height)}">'
        f"{label_html}"
        f"<h3>{escape(card['title'])}</h3>"
        f"<p>{text_to_html(card['body'])}</p>"
        "</div>"
    )


def swatch_card(swatch: dict, left: float, top: float) -> str:
    return (
        f'<div class="fixed-box swatch-card" style="{box(left, top, 2.20, 2.35)}">'
        f'<div class="swatch-box" style="background:{escape(swatch["fill"])};"></div>'
        f"<h3>{escape(swatch['name'])}</h3>"
        f'<div class="hex">{escape(swatch["hex"])}</div>'
        f'<div class="use">{escape(swatch["use"])}</div>'
        "</div>"
    )


def prompt_row(prompt: dict, top: float) -> str:
    return (
        f'<div class="fixed-box prompt-row" style="{box(1.00, top, 8.70, 0.48)}">'
        f'<div class="text">“{escape(prompt["text"])}”</div>'
        f'<div class="prompt-route">{escape(prompt["route"])}</div>'
        "</div>"
    )


def render_cover(slide: dict) -> str:
    hero = [
        '<div class="cover-page">',
        '<div class="cover-main">',
        '<div class="title-plaque cover-plaque">',
        f'<div class="kicker">{escape(slide["kicker"])}</div>',
        f"<h1>{text_to_html(slide['title'])}</h1>",
        f"<p>{escape(slide['subtitle'])}</p>",
        "</div>",
        '<div class="cover-side">',
        f'<div class="cover-copy">{text_to_html(slide["body"])}</div>',
        '<div class="cover-metrics">',
        flow_metric_card(slide["metrics"][0]),
        flow_metric_card(slide["metrics"][1]),
        "</div>",
        "</div>",
        "</div>",
        f'<div class="cover-meta">{escape(slide["meta"])}</div>',
        "</div>",
    ]
    body = [
        "".join(hero),
        footer(slide),
    ]
    return '<div class="folio-shell"><div class="folio-sheet">' + "".join(body) + "</div></div>"


def render_principle(slide: dict) -> str:
    cards = []
    x0 = 0.72
    for idx, card in enumerate(slide["cards"]):
        cards.append(archive_card(card, x0 + 2.87 * idx, 2.05, 2.52, 2.45))
    cards.append(f'<div class="fixed-box principle-summary" style="{box(1.30, 5.26, 10.00, 0.45)}">{escape(slide["summary"])}</div>')
    return '<div class="folio-shell"><div class="folio-sheet">' + section_header(slide) + "".join(cards) + footer(slide) + "</div></div>"


def render_visual(slide: dict) -> str:
    parts = [section_header(slide)]
    for idx, swatch in enumerate(slide["swatches"]):
        parts.append(swatch_card(swatch, 0.78 + 2.80 * idx, 2.15))
    parts.append(
        f'<div class="fixed-box archive-card callout-card" style="{box(1.20, 5.05, 10.50, 0.88)}">'
        f"<h3>{escape(slide['callout']['title'])}</h3>"
        f"<p>{escape(slide['callout']['body'])}</p>"
        "</div>"
    )
    parts.append(footer(slide))
    return '<div class="folio-shell"><div class="folio-sheet">' + "".join(parts) + "</div></div>"


def render_templates(slide: dict) -> str:
    parts = [section_header(slide)]
    positions = [
        (0.75, 2.03),
        (4.55, 2.03),
        (8.35, 2.03),
        (2.65, 3.65),
        (6.45, 3.65),
    ]
    for card, (left, top) in zip(slide["cards"], positions, strict=True):
        parts.append(archive_card(card, left, top, 3.36, 1.22))
    parts.append(footer(slide))
    return '<div class="folio-shell"><div class="folio-sheet">' + "".join(parts) + "</div></div>"


def render_prompts(slide: dict) -> str:
    parts = [section_header(slide)]
    for idx, prompt in enumerate(slide["prompts"]):
        parts.append(prompt_row(prompt, 2.0 + 0.72 * idx))
    parts.append(
        f'<div class="fixed-box auto-banner" style="{box(10.12, 2.00, 1.40, 3.38)}">{text_to_html(slide["banner"])}</div>'
    )
    parts.append(footer(slide))
    return '<div class="folio-shell"><div class="folio-sheet">' + "".join(parts) + "</div></div>"


def render_density(slide: dict) -> str:
    parts = [section_header(slide)]
    metric_xs = [0.95, 3.48, 6.01, 8.54]
    for metric, left in zip(slide["metrics"], metric_xs, strict=True):
        parts.append(metric_card(metric, left, 2.08, 2.20))
    bullets = "".join(f"<li>{escape(item)}</li>" for item in slide["bullets"])
    parts.append(f'<ul class="fixed-box bullet-list" style="{box(1.10, 4.25, 10.60, 1.20)}">{bullets}</ul>')
    parts.append(footer(slide))
    return '<div class="folio-shell"><div class="folio-sheet">' + "".join(parts) + "</div></div>"


def render_delivery(slide: dict) -> str:
    parts = [section_header(slide)]
    for idx, step in enumerate(slide["steps"]):
        parts.append(archive_card(step, 0.90 + 2.86 * idx, 2.70, 2.35, 1.28))
    commands = "\n".join(slide["commands"])
    parts.append(f'<pre class="fixed-box pipeline-code" style="{box(1.30, 5.20, 9.80, 0.78)}"><code>{escape(commands)}</code></pre>')
    parts.append(footer(slide))
    return '<div class="folio-shell"><div class="folio-sheet">' + "".join(parts) + "</div></div>"


def render_end(slide: dict) -> str:
    body = (
        f'<div class="fixed-box closing" style="{box(1.00, 1.85, 10.80, 3.80)}">'
        f"<h1>{escape(slide['title'])}</h1>"
        '<div class="closing-rule"></div>'
        f"<p>{escape(slide['body'])}</p>"
        f'<div class="meta">{escape(slide["meta"])}</div>'
        "</div>"
    )
    return '<div class="folio-shell"><div class="folio-sheet">' + body + footer(slide) + "</div></div>"


RENDERERS = {
    "cover": render_cover,
    "principle": render_principle,
    "visual-language": render_visual,
    "templates": render_templates,
    "natural-prompts": render_prompts,
    "density": render_density,
    "delivery": render_delivery,
    "end": render_end,
}


def main() -> None:
    frontmatter = """---
theme: default
title: Kami · Republican Manuscript Edition
titleTemplate: '%s'
info: Online slide deck companion for republican-manuscript.
colorSchema: light
canvasWidth: 1280
aspectRatio: 16/9
transition: fade
drawings: false
mdc: true
routerMode: hash
---
"""
    slides = [frontmatter]
    slides.append("<!-- Generated from slides_spec.py. Do not edit by hand. -->")
    for slide in DECK:
        renderer = RENDERERS[slide["kind"]]
        slides.append(renderer(slide))
        slides.append("---")
    output = "\n\n".join(slides[:-1]) + "\n"
    (ROOT / "slides.md").write_text(output, encoding="utf-8")
    print("✓ rendered slides.md from slides_spec.py")


if __name__ == "__main__":
    main()
