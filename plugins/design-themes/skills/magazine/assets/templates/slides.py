#!/usr/bin/env python3
"""Guizang Magazine Chinese slide deck."""

from __future__ import annotations

from pptx.util import Inches

from slides_common import (
    CONTENT_LEFT,
    add_body,
    add_kicker,
    add_line,
    add_title,
    image_panel,
    meta_stack,
    new_presentation,
    new_slide,
    patch_theme_fonts,
    pillar_card,
    pipeline_step,
    quote_panel,
    rowline,
    stat_card,
)
from slides_spec import DECK


def make_slide(prs, spec: dict):
    return new_slide(
        prs,
        spec.get("theme", "dark"),
        chrome_left=spec["chrome_left"],
        chrome_mid=spec.get("chrome_mid", ""),
        chrome_right=spec.get("chrome_right", ""),
        foot_left=spec.get("foot_left", ""),
        foot_right=spec.get("foot_right", ""),
        page_text=spec.get("page_text", ""),
    )


def render_cover(prs, spec: dict) -> None:
    slide, theme = make_slide(prs, spec)
    add_kicker(slide, theme, spec["kicker"], CONTENT_LEFT, Inches(1.0), Inches(5.8))
    add_title(slide, theme, spec["title"], CONTENT_LEFT, Inches(1.32), Inches(6.9), size=38)
    add_body(
        slide,
        theme,
        spec["body"],
        CONTENT_LEFT,
        Inches(2.72),
        Inches(6.3),
        Inches(0.82),
        size=12.2,
        color=theme.muted,
    )
    for index, item in enumerate(spec["meta"]):
        meta_stack(
            slide,
            theme,
            Inches(9.2),
            Inches(1.2 + 1.16 * index),
            Inches(2.9),
            item["label"],
            item["value"],
            item.get("note", ""),
        )
    quote = spec["quote"]
    quote_panel(slide, theme, CONTENT_LEFT, Inches(5.3), Inches(6.8), quote["text"], quote["source"])


def render_shift(prs, spec: dict) -> None:
    slide, theme = make_slide(prs, spec)
    add_kicker(slide, theme, spec["kicker"], CONTENT_LEFT, Inches(1.0), Inches(5.0))
    add_title(slide, theme, spec["title"], CONTENT_LEFT, Inches(1.28), Inches(7.0), size=30)
    add_body(
        slide,
        theme,
        spec["body"],
        CONTENT_LEFT,
        Inches(1.98),
        Inches(7.2),
        Inches(0.7),
        size=11.0,
        color=theme.fg,
    )
    for left, item in zip((0.9, 3.72, 6.54, 9.36), spec["stats"], strict=True):
        stat_card(slide, theme, Inches(left), Inches(3.02), Inches(2.45), item["label"], item["value"], item["note"])
    for top, item in zip((5.08, 5.58, 6.08), spec["rows"], strict=True):
        rowline(slide, theme, CONTENT_LEFT, Inches(top), Inches(11.2), item["title"], item["body"], item["tag"])


def render_rhythm(prs, spec: dict) -> None:
    slide, theme = make_slide(prs, spec)
    add_kicker(slide, theme, spec["kicker"], CONTENT_LEFT, Inches(1.0), Inches(5.2))
    add_title(slide, theme, spec["title"], CONTENT_LEFT, Inches(1.28), Inches(6.4), size=31)
    add_body(
        slide,
        theme,
        spec["body"],
        CONTENT_LEFT,
        Inches(2.18),
        Inches(6.2),
        Inches(0.6),
        size=11.2,
        color=theme.muted,
    )
    panel = spec["panel"]
    image_panel(slide, theme, Inches(7.95), Inches(1.3), Inches(4.1), Inches(2.8), panel["label"], panel["caption"])
    quote = spec["quote"]
    quote_panel(slide, theme, CONTENT_LEFT, Inches(4.42), Inches(5.6), quote["text"], quote["source"])
    for left, item in zip((7.95, 9.42, 10.89), spec["pillars"], strict=True):
        pillar_card(slide, theme, Inches(left), Inches(4.66), Inches(1.2), item["index"], item["title"], item["body"])


def render_pipeline(prs, spec: dict) -> None:
    slide, theme = make_slide(prs, spec)
    add_kicker(slide, theme, spec["kicker"], CONTENT_LEFT, Inches(1.0), Inches(4.8))
    add_title(slide, theme, spec["title"], CONTENT_LEFT, Inches(1.28), Inches(7.4), size=30)
    add_body(
        slide,
        theme,
        spec["body"],
        CONTENT_LEFT,
        Inches(1.96),
        Inches(7.0),
        Inches(0.58),
        size=10.8,
    )
    for left, width, item in zip((0.95, 3.95, 6.95, 9.95), (2.5, 2.5, 2.5, 2.2), spec["steps"], strict=True):
        pipeline_step(slide, theme, Inches(left), Inches(3.35), Inches(width), item["index"], item["title"], item["body"])
    add_line(slide, Inches(1.48), Inches(3.43), Inches(8.9), theme.line, 0.7)
    for top, item in zip((5.42, 5.92, 6.42), spec["rows"], strict=True):
        rowline(slide, theme, CONTENT_LEFT, Inches(top), Inches(11.2), item["title"], item["body"], item["tag"])


def render_divider(prs, spec: dict) -> None:
    slide, theme = make_slide(prs, spec)
    add_kicker(slide, theme, spec["kicker"], Inches(1.0), Inches(1.28), Inches(3.0))
    add_title(slide, theme, spec["title"], Inches(1.0), Inches(1.72), Inches(7.0), size=40)
    add_body(
        slide,
        theme,
        spec["body"],
        Inches(1.0),
        Inches(3.42),
        Inches(6.4),
        Inches(0.76),
        size=11.2,
        color=theme.muted,
    )
    for left, item in zip((8.35, 9.75, 11.15), spec["pillars"], strict=True):
        pillar_card(slide, theme, Inches(left), Inches(2.0), Inches(1.15), item["index"], item["title"], item["body"])
    quote = spec["quote"]
    quote_panel(slide, theme, Inches(1.0), Inches(5.1), Inches(11.0), quote["text"], quote["source"])


def render_components(prs, spec: dict) -> None:
    slide, theme = make_slide(prs, spec)
    add_kicker(slide, theme, spec["kicker"], CONTENT_LEFT, Inches(1.0), Inches(5.0))
    add_title(slide, theme, spec["title"], CONTENT_LEFT, Inches(1.28), Inches(6.4), size=31)
    for left, item in zip((0.92, 4.88, 8.84), spec["pillars"], strict=True):
        pillar_card(slide, theme, Inches(left), Inches(2.6), Inches(3.45), item["index"], item["title"], item["body"])
    quote = spec["quote"]
    quote_panel(slide, theme, CONTENT_LEFT, Inches(5.28), Inches(11.0), quote["text"], quote["source"])


def render_deliverables(prs, spec: dict) -> None:
    slide, theme = make_slide(prs, spec)
    add_kicker(slide, theme, spec["kicker"], CONTENT_LEFT, Inches(1.0), Inches(4.0))
    add_title(slide, theme, spec["title"], CONTENT_LEFT, Inches(1.28), Inches(7.0), size=30)
    add_body(
        slide,
        theme,
        spec["body"],
        CONTENT_LEFT,
        Inches(1.96),
        Inches(7.6),
        Inches(0.64),
        size=10.8,
    )
    for top, item in zip((3.02, 3.5, 3.98, 4.46, 4.94), spec["rows"], strict=True):
        rowline(slide, theme, CONTENT_LEFT, Inches(top), Inches(11.2), item["title"], item["body"], item["tag"])
    panel = spec["panel"]
    image_panel(slide, theme, Inches(8.1), Inches(5.52), Inches(3.95), Inches(1.48), panel["label"], panel["caption"])


def render_close(prs, spec: dict) -> None:
    slide, theme = make_slide(prs, spec)
    add_kicker(slide, theme, spec["kicker"], Inches(1.0), Inches(1.42), Inches(4.0))
    add_title(slide, theme, spec["title"], Inches(1.0), Inches(1.8), Inches(7.2), size=40)
    add_body(
        slide,
        theme,
        spec["body"],
        Inches(1.0),
        Inches(3.56),
        Inches(6.6),
        Inches(0.8),
        size=11.8,
        color=theme.muted,
    )
    quote = spec["quote"]
    quote_panel(slide, theme, Inches(1.0), Inches(5.2), Inches(10.8), quote["text"], quote["source"])


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


def main():
    prs = new_presentation()
    for spec in DECK:
        RENDERERS[spec["kind"]](prs, spec)
    prs.save("output.pptx")
    patch_theme_fonts("output.pptx")
    print("✓ Saved output.pptx")


if __name__ == "__main__":
    main()
