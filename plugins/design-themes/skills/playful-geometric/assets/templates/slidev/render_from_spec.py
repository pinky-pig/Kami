#!/usr/bin/env python3
"""Render Slidev markdown from the shared Playful Geometric slide schema."""

from __future__ import annotations

from html import escape
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))

from slides_spec import DECK  # noqa: E402


OFFSET = {
    "white": "violet",
    "violet": "pink",
    "pink": "yellow",
    "yellow": "mint",
    "mint": "violet",
}


def text_to_html(value: str) -> str:
    return "<br />".join(escape(part) for part in value.split("\n"))


def contrast(fill_name: str) -> str:
    return "light" if fill_name == "violet" else "dark"


def sticker(inner: str, *, classes: str = "", fill: str = "white",
            offset: str | None = None, tilt: str | None = None) -> str:
    class_name = " ".join(
        part for part in (
            "sticker-shell",
            f"tone-{fill}",
            f"offset-{offset or OFFSET[fill]}",
            f"contrast-{contrast(fill)}",
            classes,
        )
        if part
    )
    style_attr = f' style="--tilt:{tilt};"' if tilt else ""
    return f'<div class="{class_name}"{style_attr}><div class="sticker-face">{inner}</div></div>'


def pill(value: str, *, tone: str = "yellow") -> str:
    return f'<div class="pill tone-{tone}">{escape(value)}</div>'


def header(slide: dict) -> str:
    return (
        f'<div class="stage-label">PLAYFUL GEOMETRIC | {escape(slide["section"])}</div>'
        f'<div class="stage-page">{slide["page"]:02d} / 05</div>'
    )


def decorations() -> str:
    return (
        '<div class="shape shape-blob"></div>'
        '<div class="shape shape-dot"></div>'
        '<div class="shape shape-triangle"></div>'
        '<div class="shape shape-stripe"></div>'
    )


def render_cover(slide: dict) -> str:
    first, second = slide["callouts"]
    hero = sticker(
        "".join(
            [
                pill(slide["eyebrow"]),
                f"<h1>{text_to_html(slide['title'])}</h1>",
                f"<p>{escape(slide['subtitle'])}</p>",
            ]
        ),
        classes="hero-shell",
        fill="white",
        offset="violet",
        tilt="-2deg",
    )
    note_one = sticker(
        f"<h3>{escape(first['title'])}</h3><p>{text_to_html(first['body'])}</p>",
        classes="cover-note",
        fill=first["fill"],
    )
    note_two = sticker(
        f"<h3>{text_to_html(second['title'])}</h3><p>{text_to_html(second['body'])}</p>",
        classes="cover-note note-secondary",
        fill=second["fill"],
        tilt="-2deg",
    )
    return (
        '<div class="geo-stage cover-stage">'
        + header(slide)
        + decorations()
        + '<div class="cover-grid">'
        + hero
        + f'<div class="cover-stack">{note_one}{note_two}</div>'
        + "</div></div>"
    )


def render_tokens(slide: dict) -> str:
    cards = []
    tilts = ("-2deg", "1.5deg", "-1deg", "2deg")
    for item, tilt in zip(slide["cards"], tilts, strict=True):
        cards.append(
            sticker(
                f'<div class="token-name">{escape(item["label"])}</div>',
                classes="token-card",
                fill=item["fill"],
                tilt=tilt,
            )
        )
    summary = sticker(
        f'<div class="summary-copy">{escape(slide["summary"])}</div>',
        classes="summary-banner",
        fill="white",
        offset="yellow",
    )
    return (
        '<div class="geo-stage tokens-stage">'
        + header(slide)
        + decorations()
        + f'<div class="section-head"><h2>{escape(slide["title"])}</h2></div>'
        + '<div class="token-grid">'
        + "".join(cards)
        + "</div>"
        + summary
        + "</div>"
    )


def render_grid(slide: dict) -> str:
    cards = []
    tilts = ("-1deg", "1deg", "-1.5deg", "1.5deg")
    for item, tilt in zip(slide["cards"], tilts, strict=True):
        cards.append(
            sticker(
                "".join(
                    [
                        f'<div class="mini-pill">{escape(item["badge"])}</div>',
                        f'<div class="capability-title">{escape(item["title"])}</div>',
                    ]
                ),
                classes="capability-card",
                fill=item["fill"],
                tilt=tilt,
            )
        )
    callout = sticker(
        f'<div class="cluster-copy">{escape(slide["callout"])}</div>',
        classes="cluster-card",
        fill="white",
        offset="pink",
        tilt="-6deg",
    )
    return (
        '<div class="geo-stage grid-stage">'
        + header(slide)
        + decorations()
        + f'<div class="section-head"><h2>{escape(slide["title"])}</h2></div>'
        + '<div class="grid-layout">'
        + '<div class="capability-grid">'
        + "".join(cards)
        + "</div>"
        + '<div class="callout-cluster">'
        + '<div class="cluster-orb"></div>'
        + '<div class="cluster-pill"></div>'
        + callout
        + "</div></div></div>"
    )


def render_outputs(slide: dict) -> str:
    rows = []
    tilts = ("-1deg", "1deg", "-0.5deg")
    for item, tilt in zip(slide["rows"], tilts, strict=True):
        rows.append(
            sticker(
                "".join(
                    [
                        f'<div class="output-name">{escape(item["name"])}</div>',
                        f'<div class="output-desc">{escape(item["desc"])}</div>',
                    ]
                ),
                classes="output-row",
                fill=item["fill"],
                tilt=tilt,
            )
        )
    return (
        '<div class="geo-stage outputs-stage">'
        + header(slide)
        + decorations()
        + f'<div class="section-head"><h2>{escape(slide["title"])}</h2></div>'
        + '<div class="output-stack">'
        + "".join(rows)
        + "</div></div>"
    )


def render_end(slide: dict) -> str:
    side = slide["side_note"]
    hero = sticker(
        "".join(
            [
                pill(slide["eyebrow"]),
                f"<h1>{text_to_html(slide['title'])}</h1>",
                f'<p class="ending-copy">{escape(slide["summary"])}</p>',
            ]
        ),
        classes="end-hero",
        fill="white",
        offset="yellow",
    )
    note = sticker(
        f"<h3>{escape(side['title'])}</h3><p>{text_to_html(side['body'])}</p>",
        classes="end-note",
        fill=side["fill"],
        offset="pink",
    )
    return (
        '<div class="geo-stage end-stage">'
        + header(slide)
        + decorations()
        + '<div class="end-layout">'
        + hero
        + f'<div class="end-side">{note}</div>'
        + "</div></div>"
    )


RENDERERS = {
    "cover": render_cover,
    "tokens": render_tokens,
    "grid": render_grid,
    "outputs": render_outputs,
    "end": render_end,
}


def main() -> None:
    frontmatter = """---
theme: default
title: Kami · Playful Geometric Edition
titleTemplate: '%s'
info: Online slide deck companion for playful-geometric.
colorSchema: light
canvasWidth: 1280
aspectRatio: 16/9
transition: fade
drawings: false
mdc: true
routerMode: hash
---
"""
    slides = [
        frontmatter,
        '<style>@import "./style.css";</style>',
        "<!-- Generated from slides_spec.py. Do not edit by hand. -->",
    ]
    for slide in DECK:
        slides.append(RENDERERS[slide["kind"]](slide))
        slides.append("---")
    output = "\n\n".join(slides[:-1]) + "\n"
    (ROOT / "slides.md").write_text(output, encoding="utf-8")
    print("✓ rendered slides.md from slides_spec.py")


if __name__ == "__main__":
    main()
