#!/usr/bin/env python3
"""Render a Newsprint Slidev deck from the shared slide schema."""

from __future__ import annotations

from html import escape
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))

from slides_spec import DECK, DISPLAY_TOTAL  # noqa: E402


PX_PER_INCH = 96
SLIDE_W = 13.333
M = 0.45


def px(value: float) -> str:
    return f"{value * PX_PER_INCH:.2f}px"


def box(left: float, top: float, width: float, height: float) -> str:
    return f"left:{px(left)};top:{px(top)};width:{px(width)};height:{px(height)};"


def text_to_html(text: str) -> str:
    return "<br />".join(escape(part) for part in text.split("\n"))


def base_frame(slide: dict) -> str:
    rule_width = SLIDE_W - 2 * M
    return "".join(
        [
            f'<div class="fixed-box folio-label" style="{box(M, 0.28, 3.40, 0.18)}">VOL. 01 | {escape(slide["section"])}</div>',
            f'<div class="fixed-box folio-brand" style="{box(4.15, 0.20, 5.00, 0.35)}">THE NEWSPRINT REVIEW</div>',
            f'<div class="fixed-box folio-page" style="{box(SLIDE_W - 2.20, 0.28, 1.75, 0.18)}">PAGE {slide["page"]:02d} / {DISPLAY_TOTAL:02d}</div>',
            f'<div class="fixed-box rule-thick" style="{box(M, 0.72, rule_width, 0.04)}"></div>',
            f'<div class="fixed-box rule-thin" style="{box(M, 6.78, rule_width, 0.01)}"></div>',
        ]
    )


def label_box(value: str, left: float, top: float, width: float, tone: str = "red") -> str:
    return (
        f'<div class="fixed-box label-box {tone}" style="{box(left, top, width, 0.28)}">'
        f"{escape(value)}"
        "</div>"
    )


def component_card(card: dict, left: float) -> str:
    return (
        f'<section class="fixed-box component-card" style="{box(left, 2.05, 3.65, 1.75)}">'
        f'<div class="card-tag">{escape(card["tag"])}</div>'
        f'<h3 class="card-title">{escape(card["title"])}</h3>'
        f'<p class="card-body">{escape(card["body"])}</p>'
        "</section>"
    )


def render_cover(slide: dict) -> str:
    parts = [
        '<div class="news-shell"><div class="news-sheet">',
        base_frame(slide),
        label_box(slide["label"], M, 0.95, 1.05),
        f'<h1 class="fixed-box cover-title" style="{box(M, 1.42, 8.15, 2.35)}">{text_to_html(slide["title"])}</h1>',
        f'<div class="fixed-box rule-v" style="{box(8.85, 0.90, 0.01, 5.72)}"></div>',
        f'<p class="fixed-box cover-copy" style="{box(9.15, 1.18, 3.35, 1.35)}">{escape(slide["body"])}</p>',
        f'<div class="fixed-box edition-box" style="{box(9.15, 3.00, 3.35, 1.42)}">{text_to_html(slide["edition"])}</div>',
        f'<div class="fixed-box mid-rule" style="{box(M, 4.25, 8.10, 0.01)}"></div>',
        f'<div class="fixed-box cover-note" style="{box(M, 4.52, 8.00, 0.50)}">{escape(slide["note"])}</div>',
        "</div></div>",
    ]
    return "".join(parts)


def render_grid(slide: dict) -> str:
    cell_w = (SLIDE_W - 2 * M) / 12
    cells = []
    for item in slide["columns"]:
        tone = "muted" if item["tone"] == "muted" else "paper"
        left = cell_w * (item["index"] - 1)
        cells.append(
            f'<div class="grid-cell tone-{tone}" style="{box(left, 0, cell_w, 2.70)}">'
            f'<div class="grid-index">{item["index"]}</div>'
            "</div>"
        )
    parts = [
        '<div class="news-shell"><div class="news-sheet">',
        base_frame(slide),
        f'<h2 class="fixed-box slide-title" style="{box(M, 1.08, 5.40, 0.78)}">{escape(slide["title"])}</h2>',
        f'<p class="fixed-box body-copy" style="{box(6.00, 1.18, 5.95, 0.55)}">{escape(slide["body"])}</p>',
        f'<div class="fixed-box grid-frame" style="{box(M, 2.12, SLIDE_W - 2 * M, 2.70)}">{"".join(cells)}</div>',
        label_box(slide["hero_label"], M + 0.15, 2.30, 1.35, "dark"),
        label_box(slide["side_label"], M + cell_w * 8 + 0.15, 2.30, 1.35, "red"),
        f'<div class="fixed-box note-copy" style="{box(M, 5.22, 8.30, 0.30)}">{escape(slide["note"])}</div>',
        "</div></div>",
    ]
    return "".join(parts)


def render_components(slide: dict) -> str:
    cards = [component_card(card, M + 3.65 * idx) for idx, card in enumerate(slide["cards"])]
    parts = [
        '<div class="news-shell"><div class="news-sheet">',
        base_frame(slide),
        f'<h2 class="fixed-box slide-title wide" style="{box(M, 1.05, 8.70, 0.65)}">{escape(slide["title"])}</h2>',
        "".join(cards),
        f'<div class="fixed-box ticker-band" style="{box(M, 4.45, SLIDE_W - 2 * M, 0.46)}">'
        f'<div class="ticker-copy">{escape(slide["ticker"])}</div>'
        "</div>",
        "</div></div>",
    ]
    return "".join(parts)


def render_typography(slide: dict) -> str:
    parts = [
        '<div class="news-shell"><div class="news-sheet">',
        base_frame(slide),
        label_box(slide["label"], M, 1.02, 1.00),
        f'<h1 class="fixed-box display-title" style="{box(M, 1.42, 6.25, 2.20)}">{text_to_html(slide["title"])}</h1>',
        f'<div class="fixed-box rule-v" style="{box(7.05, 1.00, 0.01, 5.45)}"></div>',
        f'<p class="fixed-box body-copy serif" style="{box(7.38, 1.42, 4.90, 1.25)}">{escape(slide["body"])}</p>',
        f'<div class="fixed-box drop-cap" style="{box(7.38, 3.15, 0.65, 0.70)}">{escape(slide["drop_cap"])}</div>',
        f'<p class="fixed-box drop-line" style="{box(8.00, 3.38, 4.30, 0.40)}">{escape(slide["drop_text"])}</p>',
        "</div></div>",
    ]
    return "".join(parts)


def render_inverted(slide: dict) -> str:
    steps = []
    for idx, item in enumerate(slide["steps"]):
        x = 6.10 + 2.15 * idx
        steps.append(
            "".join(
                [
                    f'<div class="fixed-box step-number" style="{box(x, 1.55, 1.40, 0.45)}">{escape(item["number"])}</div>',
                    f'<div class="fixed-box step-rule" style="{box(x, 2.12, 1.68, 0.01)}"></div>',
                    f'<div class="fixed-box step-title" style="{box(x, 2.38, 1.70, 0.28)}">{escape(item["title"])}</div>',
                    f'<p class="fixed-box step-copy" style="{box(x, 2.90, 1.70, 0.70)}">{escape(item["body"])}</p>',
                ]
            )
        )
    parts = [
        '<div class="news-shell"><div class="news-sheet">',
        base_frame(slide),
        f'<section class="fixed-box inverted-panel" style="{box(M, 1.05, 5.20, 5.35)}"></section>',
        label_box(slide["panel_label"], M + 0.30, 1.35, 1.55),
        f'<h2 class="fixed-box inverted-title" style="{box(M + 0.30, 1.95, 4.40, 1.40)}">{text_to_html(slide["title"])}</h2>',
        f'<p class="fixed-box inverted-copy" style="{box(M + 0.30, 4.15, 4.35, 0.80)}">{escape(slide["body"])}</p>',
        "".join(steps),
        "</div></div>",
    ]
    return "".join(parts)


def render_outputs(slide: dict) -> str:
    rows = []
    top = 2.05
    for idx, row in enumerate(slide["rows"]):
        y = top + 1.08 * idx
        rows.append(f'<div class="fixed-box row-rule" style="{box(M, y, SLIDE_W - 2 * M, 0.01)}"></div>')
        rows.append(
            f'<div class="fixed-box output-name" style="{box(M + 0.15, y + 0.22, 2.00, 0.20)}">{escape(row["name"])}</div>'
        )
        rows.append(
            f'<div class="fixed-box output-copy" style="{box(2.75, y + 0.18, 8.70, 0.28)}">{escape(row["desc"])}</div>'
        )
    rows.append(f'<div class="fixed-box row-rule" style="{box(M, top + 3.24, SLIDE_W - 2 * M, 0.01)}"></div>')
    parts = [
        '<div class="news-shell"><div class="news-sheet">',
        base_frame(slide),
        f'<h2 class="fixed-box slide-title wide" style="{box(M, 1.08, 8.60, 0.70)}">{escape(slide["title"])}</h2>',
        "".join(rows),
        "</div></div>",
    ]
    return "".join(parts)


def render_end(slide: dict) -> str:
    parts = [
        '<div class="news-shell"><div class="news-sheet">',
        base_frame(slide),
        f'<h1 class="fixed-box end-title" style="{box(M, 1.25, 8.60, 2.10)}">{text_to_html(slide["title"])}</h1>',
        f'<div class="fixed-box end-panel" style="{box(9.15, 1.30, 3.10, 3.70)}">{text_to_html(slide["panel"])}</div>',
        f'<div class="fixed-box end-tagline" style="{box(M, 4.35, 6.40, 0.45)}">{escape(slide["tagline"])}</div>',
        "</div></div>",
    ]
    return "".join(parts)


RENDERERS = {
    "cover": render_cover,
    "grid": render_grid,
    "components": render_components,
    "typography": render_typography,
    "inverted": render_inverted,
    "outputs": render_outputs,
    "end": render_end,
}


def main() -> None:
    frontmatter = """---
theme: default
title: Kami · Newsprint
titleTemplate: '%s'
info: Online slide deck companion for the Newsprint skill.
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
