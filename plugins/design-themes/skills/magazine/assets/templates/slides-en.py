#!/usr/bin/env python3
"""Guizang Magazine English slide deck."""

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


def slide_cover(prs):
    slide, theme = new_slide(
        prs,
        "dark",
        chrome_left="GUIZANG MAGAZINE",
        chrome_mid="SLIDE DEMO",
        chrome_right="ACT 00",
        foot_left="EDITORIAL SYSTEM",
        foot_right="VOL. 01",
        page_text="01 / 08",
    )
    add_kicker(slide, theme, "EDITORIAL SYSTEM", CONTENT_LEFT, Inches(1.0), Inches(5.8))
    add_title(slide, theme, "A real new theme,\nnot a recolor", CONTENT_LEFT, Inches(1.32), Inches(6.9), size=38)
    add_body(
        slide,
        theme,
        "What defines Guizang is not a paper tint. It is the magazine chrome, the hero rhythm, and the way components organize meaning across HTML, PDF, and PPTX.",
        CONTENT_LEFT,
        Inches(2.72),
        Inches(6.5),
        Inches(0.82),
        size=12.1,
        color=theme.muted,
    )
    meta_stack(slide, theme, Inches(9.2), Inches(1.2), Inches(2.9), "Formats", "HTML / PDF / PPTX", "one language, many surfaces")
    meta_stack(slide, theme, Inches(9.2), Inches(2.36), Inches(2.9), "Type", "Serif / Sans / Mono", "roles stay stable")
    meta_stack(slide, theme, Inches(9.2), Inches(3.52), Inches(2.9), "Rhythm", "Dark Editorial", "one stable dark mode")
    quote_panel(slide, theme, CONTENT_LEFT, Inches(5.3), Inches(6.8), "A theme is a system, not a palette.", "GUIZANG PRINCIPLE")


def slide_shift(prs):
    slide, theme = new_slide(
        prs,
        "dark",
        chrome_left="WHAT CHANGED",
        chrome_mid="SYSTEM NOT PALETTE",
        chrome_right="ACT I",
        foot_left="LANGUAGE SHIFT",
        foot_right="02 / 08",
    )
    add_kicker(slide, theme, "NOT A RECOLOR", CONTENT_LEFT, Inches(1.0), Inches(5.0))
    add_title(slide, theme, "The rewrite is structural", CONTENT_LEFT, Inches(1.28), Inches(7.0), size=30)
    add_body(
        slide,
        theme,
        "The old issue was not color. It was inherited manuscript architecture: framed pages, plaque blocks, and archive cards. The new deck swaps in Guizang-native headline, stat, rowline, and act-divider grammar.",
        CONTENT_LEFT,
        Inches(1.98),
        Inches(7.5),
        Inches(0.72),
        size=10.8,
        color=theme.fg,
    )
    stat_card(slide, theme, Inches(0.9), Inches(3.02), Inches(2.45), "HERO", "01", "memory pages and section breaks")
    stat_card(slide, theme, Inches(3.72), Inches(3.02), Inches(2.45), "COMPONENTS", "06", "stat, rowline, pillar, quote")
    stat_card(slide, theme, Inches(6.54), Inches(3.02), Inches(2.45), "SURFACES", "03", "dark theme, editorial card")
    stat_card(slide, theme, Inches(9.36), Inches(3.02), Inches(2.45), "OUTPUTS", "05", "core templates rewritten")
    rowline(slide, theme, CONTENT_LEFT, Inches(5.08), Inches(11.2), "Chrome", "Headers and footers return to navigation rather than decorative frames.", "META")
    rowline(slide, theme, CONTENT_LEFT, Inches(5.58), Inches(11.2), "Hierarchy", "Serif carries impact, sans carries body, mono carries metadata.", "TYPE")
    rowline(slide, theme, CONTENT_LEFT, Inches(6.08), Inches(11.2), "Rhythm", "HTML, PDF, and PPTX now share visible hero and body pacing.", "FLOW")


def slide_rhythm(prs):
    slide, theme = new_slide(
        prs,
        "dark",
        chrome_left="RHYTHM",
        chrome_mid="HERO / NON-HERO",
        chrome_right="ACT I",
        foot_left="EDITORIAL BREATHING",
        foot_right="03 / 08",
    )
    add_kicker(slide, theme, "LAYOUT RHYTHM", CONTENT_LEFT, Inches(1.0), Inches(5.2))
    add_title(slide, theme, "Cover, divider, body:\nthree different jobs", CONTENT_LEFT, Inches(1.28), Inches(6.6), size=30)
    add_body(
        slide,
        theme,
        "Guizang works because strong pages and dense pages alternate. Hero slides stage the memory, body slides carry the facts, and act pages let the deck breathe.",
        CONTENT_LEFT,
        Inches(2.16),
        Inches(6.3),
        Inches(0.64),
        size=11.0,
        color=theme.muted,
    )
    image_panel(slide, theme, Inches(7.95), Inches(1.3), Inches(4.1), Inches(2.8), "ACT DIVIDER", "HERO PAGE")
    quote_panel(slide, theme, CONTENT_LEFT, Inches(4.42), Inches(5.7), "If every page behaves like a body page, the reader never feels a turn.", "PACING RULE")
    pillar_card(slide, theme, Inches(7.95), Inches(4.66), Inches(1.2), "01", "Hero", "Large title, fewer words, stronger recall.")
    pillar_card(slide, theme, Inches(9.42), Inches(4.66), Inches(1.2), "02", "Body", "Rowlines, stats, and argument density.")
    pillar_card(slide, theme, Inches(10.89), Inches(4.66), Inches(1.2), "03", "Act", "Breathing room and chapter transition.")


def slide_pipeline(prs):
    slide, theme = new_slide(
        prs,
        "dark",
        chrome_left="PIPELINE",
        chrome_mid="FROM INPUT TO OUTPUT",
        chrome_right="ACT II",
        foot_left="PRODUCTION METHOD",
        foot_right="04 / 08",
    )
    add_kicker(slide, theme, "DELIVERY CHAIN", CONTENT_LEFT, Inches(1.0), Inches(4.8))
    add_title(slide, theme, "The scaffold builds.\nThe theme decides the look.", CONTENT_LEFT, Inches(1.28), Inches(7.5), size=30)
    add_body(
        slide,
        theme,
        "The manuscript skill is allowed to contribute file organization and build flow only. Guizang itself has to define the composition, typography, and rhythm.",
        CONTENT_LEFT,
        Inches(1.96),
        Inches(7.3),
        Inches(0.64),
        size=10.7,
    )
    pipeline_step(slide, theme, Inches(0.95), Inches(3.35), Inches(2.5), "01", "Route", "Choose document type and language.")
    pipeline_step(slide, theme, Inches(3.95), Inches(3.35), Inches(2.5), "02", "Compose", "Pour content into Guizang components.")
    pipeline_step(slide, theme, Inches(6.95), Inches(3.35), Inches(2.5), "03", "Build", "Export HTML, PDF, and PPTX.")
    pipeline_step(slide, theme, Inches(9.95), Inches(3.35), Inches(2.2), "04", "Verify", "Check pages, fonts, and placeholders.")
    add_line(slide, Inches(1.48), Inches(3.43), Inches(8.9), theme.line, 0.7)
    rowline(slide, theme, CONTENT_LEFT, Inches(5.42), Inches(11.2), "AGENTS.md", "The repository now explicitly forbids shipping recolored manuscript themes.", "RULE")
    rowline(slide, theme, CONTENT_LEFT, Inches(5.92), Inches(11.2), "Templates", "HTML, PDF, and PPT layouts were rebuilt around Guizang grammar.", "OUTPUT")
    rowline(slide, theme, CONTENT_LEFT, Inches(6.42), Inches(11.2), "Demos", "Preview artifacts are regenerated in the new system, not inherited.", "DEMO")


def slide_divider(prs):
    slide, theme = new_slide(
        prs,
        "dark",
        chrome_left="ACT DIVIDER",
        chrome_mid="ONE LANGUAGE / MANY OUTPUTS",
        chrome_right="ACT III",
        foot_left="TRANSITION PAGE",
        foot_right="05 / 08",
    )
    add_kicker(slide, theme, "ACT III", Inches(1.0), Inches(1.28), Inches(3.0))
    add_title(slide, theme, "One language,\nmany outputs", Inches(1.0), Inches(1.72), Inches(7.0), size=40)
    add_body(
        slide,
        theme,
        "The files do not need to look identical. They do need to look recognizably related.",
        Inches(1.0),
        Inches(3.42),
        Inches(6.2),
        Inches(0.64),
        size=11.0,
        color=theme.muted,
    )
    pillar_card(slide, theme, Inches(8.35), Inches(2.0), Inches(1.15), "HTML", "Docs", "Navigation, chapter pacing, editorial copy.")
    pillar_card(slide, theme, Inches(9.75), Inches(2.0), Inches(1.15), "PDF", "Pages", "Density, print structure, export fidelity.")
    pillar_card(slide, theme, Inches(11.15), Inches(2.0), Inches(1.15), "PPTX", "Deck", "Hero, transitions, spoken pacing.")
    quote_panel(slide, theme, Inches(1.0), Inches(5.1), Inches(11.0), "Consistency comes from hierarchy and rhythm, not from cloning one card everywhere.", "SYSTEM CONSISTENCY")


def slide_components(prs):
    slide, theme = new_slide(
        prs,
        "dark",
        chrome_left="COMPONENTS",
        chrome_mid="GUIZANG GRAMMAR",
        chrome_right="ACT III",
        foot_left="CORE PARTS",
        foot_right="06 / 08",
    )
    add_kicker(slide, theme, "CORE COMPONENTS", CONTENT_LEFT, Inches(1.0), Inches(5.0))
    add_title(slide, theme, "What the new deck speaks with", CONTENT_LEFT, Inches(1.28), Inches(6.4), size=31)
    pillar_card(slide, theme, Inches(0.92), Inches(2.6), Inches(3.45), "01", "Chrome / Foot", "Navigation metadata builds the magazine frame without old border furniture.")
    pillar_card(slide, theme, Inches(4.88), Inches(2.6), Inches(3.45), "02", "Serif / Sans / Mono", "Impact, body, and metadata each keep a stable voice.")
    pillar_card(slide, theme, Inches(8.84), Inches(2.6), Inches(3.45), "03", "Stat / Rowline / Pillar", "Reusable blocks for evidence, comparison, and argument.")
    quote_panel(slide, theme, CONTENT_LEFT, Inches(5.28), Inches(11.0), "Components are not ornaments. They are the way content gets arranged.", "LAYOUT SYSTEM")


def slide_deliverables(prs):
    slide, theme = new_slide(
        prs,
        "dark",
        chrome_left="DELIVERABLES",
        chrome_mid="THEME COVERAGE",
        chrome_right="ACT IV",
        foot_left="SHIPPING NOW",
        foot_right="07 / 08",
    )
    add_kicker(slide, theme, "OUTPUTS", CONTENT_LEFT, Inches(1.0), Inches(4.0))
    add_title(slide, theme, "The rewritten theme now covers", CONTENT_LEFT, Inches(1.28), Inches(7.0), size=30)
    add_body(
        slide,
        theme,
        "Not just the core trio. Resume, portfolio, and the English deck now move with the same Guizang editorial logic so the skill no longer fractures internally.",
        CONTENT_LEFT,
        Inches(1.96),
        Inches(7.8),
        Inches(0.68),
        size=10.7,
    )
    rowline(slide, theme, CONTENT_LEFT, Inches(3.02), Inches(11.2), "One-Pager", "hero headline, stat spread, editorial blocks, callout", "HTML")
    rowline(slide, theme, CONTENT_LEFT, Inches(3.5), Inches(11.2), "Long Doc", "cover, overview, problem, method, conclusion, appendix", "PDF")
    rowline(slide, theme, CONTENT_LEFT, Inches(3.98), Inches(11.2), "Letter", "subject block, body column, evidence sidebar", "DOC")
    rowline(slide, theme, CONTENT_LEFT, Inches(4.46), Inches(11.2), "Resume", "identity hero, metrics, timeline, open-source spread", "CV")
    rowline(slide, theme, CONTENT_LEFT, Inches(4.94), Inches(11.2), "Portfolio", "editorial cover, case spreads, selected works, contact", "BOOK")
    image_panel(slide, theme, Inches(8.1), Inches(5.52), Inches(3.95), Inches(1.48), "DEMO BUNDLE", "HTML / PDF / PPTX")


def slide_close(prs):
    slide, theme = new_slide(
        prs,
        "dark",
        chrome_left="END",
        chrome_mid="SYSTEM COMPLETE",
        chrome_right="ACT V",
        foot_left="GUIZANG MAGAZINE",
        foot_right="08 / 08",
    )
    add_kicker(slide, theme, "FINAL LINE", Inches(1.0), Inches(1.42), Inches(4.0))
    add_title(slide, theme, "If it still looks old,\nit is not rewritten.", Inches(1.0), Inches(1.8), Inches(7.3), size=38)
    add_body(
        slide,
        theme,
        "A real new theme should be recognizable across HTML, PDF, PPTX, and demos without being told its name.",
        Inches(1.0),
        Inches(3.58),
        Inches(6.4),
        Inches(0.72),
        size=11.7,
        color=theme.muted,
    )
    quote_panel(slide, theme, Inches(1.0), Inches(5.2), Inches(10.8), "The point is not to decorate the scaffold. The point is to replace the visual architecture.", "AGENTS RULE")


def main():
    prs = new_presentation()
    slide_cover(prs)
    slide_shift(prs)
    slide_rhythm(prs)
    slide_pipeline(prs)
    slide_divider(prs)
    slide_components(prs)
    slide_deliverables(prs)
    slide_close(prs)
    prs.save("output.pptx")
    patch_theme_fonts("output.pptx")
    print("✓ Saved output.pptx")


if __name__ == "__main__":
    main()
