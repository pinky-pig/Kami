#!/usr/bin/env python3
"""Render a Guizang Magazine Slidev deck from the shared slide schema."""

from __future__ import annotations

from html import escape
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))

from slides_spec import DECK, TOTAL_SLIDES  # noqa: E402


def text_to_html(text: str) -> str:
    return "<br />".join(escape(part) for part in text.split("\n"))


def chrome(slide: dict) -> str:
    middle = ""
    if slide.get("chrome_mid"):
        middle = (
            '<span class="chrome-sep"></span>'
            f'<span>{escape(slide["chrome_mid"])}</span>'
        )
    return (
        '<div class="mag-chrome mag-chrome-top">'
        '<div class="chrome-group">'
        f'<span>{escape(slide["chrome_left"])}</span>'
        f"{middle}"
        "</div>"
        f'<div class="chrome-group chrome-right"><span>{escape(slide.get("chrome_right", ""))}</span></div>'
        "</div>"
    )


def footer(slide: dict) -> str:
    right_parts: list[str] = []
    if slide.get("foot_right"):
        right_parts.append(f"<span>{escape(slide['foot_right'])}</span>")
    if slide.get("page_text"):
        right_parts.append('<span class="chrome-sep"></span>')
        right_parts.append(f"<span>{escape(slide['page_text'])}</span>")
    right_html = "".join(right_parts)
    return (
        '<div class="mag-chrome mag-chrome-bottom">'
        f'<div class="chrome-group"><span>{escape(slide.get("foot_left", ""))}</span></div>'
        f'<div class="chrome-group chrome-right">{right_html}</div>'
        "</div>"
    )


def meta_stack(item: dict) -> str:
    note = f'<div class="meta-note">{escape(item["note"])}</div>' if item.get("note") else ""
    return (
        '<section class="meta-stack">'
        f'<div class="meta-label">{escape(item["label"])}</div>'
        f'<div class="meta-value">{escape(item["value"])}</div>'
        f"{note}"
        "</section>"
    )


def stat_card(item: dict) -> str:
    return (
        '<section class="stat-card">'
        f'<div class="stat-label">{escape(item["label"])}</div>'
        f'<div class="stat-value">{escape(item["value"])}</div>'
        f'<div class="stat-note">{escape(item["note"])}</div>'
        "</section>"
    )


def rowline(item: dict) -> str:
    return (
        '<div class="rowline">'
        f'<div class="rowline-title">{escape(item["title"])}</div>'
        f'<div class="rowline-body">{escape(item["body"])}</div>'
        f'<div class="rowline-tag">{escape(item["tag"])}</div>'
        "</div>"
    )


def pillar(item: dict) -> str:
    return (
        '<section class="pillar-card">'
        f'<div class="pillar-index">{escape(item["index"])}</div>'
        f'<div class="pillar-title">{escape(item["title"])}</div>'
        f'<div class="pillar-body">{escape(item["body"])}</div>'
        "</section>"
    )


def quote_panel(quote: dict, extra_class: str = "") -> str:
    classes = f"quote-panel {extra_class}".strip()
    return (
        f'<section class="{classes}">'
        f'<div class="quote-copy">{escape(quote["text"])}</div>'
        f'<div class="quote-source">{escape(quote["source"])}</div>'
        "</section>"
    )


def panel_card(panel: dict, extra_class: str = "") -> str:
    classes = f"frame-card {extra_class}".strip()
    return (
        f'<section class="{classes}">'
        f'<div class="frame-label">{escape(panel["label"])}</div>'
        f'<div class="frame-caption">{escape(panel["caption"])}</div>'
        "</section>"
    )


def story_head(slide: dict, include_body: bool = True, title_class: str = "section-title") -> str:
    body = f'<p class="section-body">{text_to_html(slide["body"])}</p>' if include_body and slide.get("body") else ""
    return (
        '<div class="story-head">'
        f'<div class="slide-kicker">{escape(slide["kicker"])}</div>'
        f'<h1 class="{title_class}">{text_to_html(slide["title"])}</h1>'
        f"{body}"
        "</div>"
    )


def render_cover(slide: dict) -> str:
    return (
        '<div class="mag-shell cover-shell">'
        f"{chrome(slide)}"
        '<div class="cover-grid">'
        '<div class="cover-copy">'
        f"{story_head(slide, include_body=True, title_class='hero-title')}"
        "</div>"
        '<div class="meta-column">'
        + "".join(meta_stack(item) for item in slide["meta"])
        + "</div>"
        "</div>"
        f"{quote_panel(slide['quote'], 'cover-quote')}"
        f"{footer(slide)}"
        "</div>"
    )


def render_shift(slide: dict) -> str:
    return (
        '<div class="mag-shell">'
        f"{chrome(slide)}"
        f"{story_head(slide)}"
        '<div class="stat-grid">'
        + "".join(stat_card(item) for item in slide["stats"])
        + "</div>"
        '<div class="rowline-list">'
        + "".join(rowline(item) for item in slide["rows"])
        + "</div>"
        f"{footer(slide)}"
        "</div>"
    )


def render_rhythm(slide: dict) -> str:
    return (
        '<div class="mag-shell">'
        f"{chrome(slide)}"
        '<div class="rhythm-grid">'
        '<div class="rhythm-copy">'
        f"{story_head(slide)}"
        "</div>"
        f"{panel_card(slide['panel'], 'hero-frame')}"
        "</div>"
        '<div class="bottom-grid">'
        f"{quote_panel(slide['quote'])}"
        '<div class="pillar-grid pillar-grid-tight">'
        + "".join(pillar(item) for item in slide["pillars"])
        + "</div>"
        "</div>"
        f"{footer(slide)}"
        "</div>"
    )


def pipeline_step(item: dict) -> str:
    return (
        '<section class="step-card">'
        f'<div class="step-index">{escape(item["index"])}</div>'
        f'<div class="step-title">{escape(item["title"])}</div>'
        f'<div class="step-body">{escape(item["body"])}</div>'
        "</section>"
    )


def render_pipeline(slide: dict) -> str:
    return (
        '<div class="mag-shell">'
        f"{chrome(slide)}"
        f"{story_head(slide)}"
        '<div class="step-grid">'
        + "".join(pipeline_step(item) for item in slide["steps"])
        + "</div>"
        '<div class="timeline-rule"></div>'
        '<div class="rowline-list">'
        + "".join(rowline(item) for item in slide["rows"])
        + "</div>"
        f"{footer(slide)}"
        "</div>"
    )


def render_divider(slide: dict) -> str:
    return (
        '<div class="mag-shell divider-shell">'
        f"{chrome(slide)}"
        '<div class="divider-grid">'
        '<div class="divider-copy">'
        f"{story_head(slide, title_class='hero-title large')}"
        "</div>"
        '<div class="pillar-grid pillar-grid-slim">'
        + "".join(pillar(item) for item in slide["pillars"])
        + "</div>"
        "</div>"
        f"{quote_panel(slide['quote'], 'wide-quote')}"
        f"{footer(slide)}"
        "</div>"
    )


def render_components(slide: dict) -> str:
    return (
        '<div class="mag-shell">'
        f"{chrome(slide)}"
        f"{story_head(slide, include_body=False)}"
        '<div class="pillar-grid pillar-grid-wide">'
        + "".join(pillar(item) for item in slide["pillars"])
        + "</div>"
        f"{quote_panel(slide['quote'], 'wide-quote')}"
        f"{footer(slide)}"
        "</div>"
    )


def render_deliverables(slide: dict) -> str:
    return (
        '<div class="mag-shell">'
        f"{chrome(slide)}"
        f"{story_head(slide)}"
        '<div class="coverage-grid">'
        '<div class="rowline-list coverage-list">'
        + "".join(rowline(item) for item in slide["rows"])
        + "</div>"
        f"{panel_card(slide['panel'], 'coverage-panel')}"
        "</div>"
        f"{footer(slide)}"
        "</div>"
    )


def render_close(slide: dict) -> str:
    return (
        '<div class="mag-shell close-shell">'
        f"{chrome(slide)}"
        '<div class="close-copy">'
        f"{story_head(slide, title_class='hero-title large')}"
        "</div>"
        f"{quote_panel(slide['quote'], 'close-quote')}"
        f"{footer(slide)}"
        "</div>"
    )


RENDERERS = {
    "cover": render_cover,
    "shift": render_shift,
    "rhythm": render_rhythm,
    "pipeline": render_pipeline,
    "divider": render_divider,
    "components": render_components,
    "deliverables": render_deliverables,
    "close": render_close,
}


def main() -> None:
    frontmatter = f"""---
theme: default
title: Kami · Guizang Magazine
titleTemplate: '%s'
info: Online slide deck companion for the Guizang Magazine skill.
colorSchema: dark
canvasWidth: 1280
aspectRatio: 16/9
transition: fade
drawings: false
mdc: true
routerMode: hash
---
"""
    slides = [frontmatter]
    slides.append(f"<!-- Generated from slides_spec.py ({TOTAL_SLIDES} slides). Do not edit by hand. -->")
    for slide in DECK:
        slides.append(RENDERERS[slide["kind"]](slide))
        slides.append("---")
    output = "\n\n".join(slides[:-1]) + "\n"
    (ROOT / "slides.md").write_text(output, encoding="utf-8")
    print("✓ rendered slides.md from slides_spec.py")


if __name__ == "__main__":
    main()
