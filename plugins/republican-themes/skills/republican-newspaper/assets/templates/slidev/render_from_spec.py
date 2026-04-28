#!/usr/bin/env python3
"""Render newspaper-native Slidev markdown from the shared slide schema."""

from __future__ import annotations

from html import escape
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))

from slides_spec import DECK, DISPLAY_TOTAL  # noqa: E402


def join_classes(*parts: str) -> str:
    return " ".join(part for part in parts if part)


def text_to_html(text: str) -> str:
    return "<br />".join(escape(part) for part in text.split("\n"))


def footer(slide: dict) -> str:
    return (
        '<footer class="edition-footer sans">'
        f"<span>{escape(slide['section'])}</span>"
        f"<span>{slide['page']:02d} / {DISPLAY_TOTAL:02d}</span>"
        "</footer>"
    )


def wrap_slide(slide: dict, body: str, *, extra_shell_class: str = "", extra_sheet_class: str = "") -> str:
    kind = slide["kind"]
    shell_classes = join_classes("news-shell", f"{kind}-slide", extra_shell_class)
    sheet_classes = join_classes("news-sheet", f"{kind}-sheet", extra_sheet_class)
    return (
        f'<div class="{shell_classes}">'
        f'<article class="{sheet_classes}">'
        f"{body}"
        f"{footer(slide)}"
        "</article>"
        "</div>"
    )


def reverse_label(text: str, extra_class: str = "") -> str:
    classes = join_classes("reverse-label", "sans", extra_class)
    return f'<div class="{classes}">{escape(text)}</div>'


def issue_mark(title: str, note: str, extra_class: str = "") -> str:
    classes = join_classes("issue-mark", extra_class)
    note_html = f'<span class="sans">{escape(note)}</span>' if note else ""
    return f'<div class="{classes}"><b>{escape(title)}</b>{note_html}</div>'


def clipping(title: str, body: str, *, tag: str | None = None, seal: str | None = None, extra_class: str = "") -> str:
    classes = join_classes("clipping", extra_class)
    tag_html = f'<div class="clip-tag sans">{escape(tag)}</div>' if tag else ""
    title_html = f'<h3 class="clip-title">{escape(title)}</h3>' if title else ""
    if seal:
        body_html = (
            '<div class="clip-seal-row">'
            f'<div class="seal">{escape(seal)}</div>'
            f'<p class="clip-copy sans">{text_to_html(body)}</p>'
            "</div>"
        )
    else:
        body_html = f'<p class="clip-copy sans">{text_to_html(body)}</p>'
    return f'<section class="{classes}">{tag_html}{title_html}{body_html}</section>'


def stat_card(stat: dict) -> str:
    return (
        '<div class="stat-card">'
        f'<div class="stat-value">{escape(stat["value"])}</div>'
        f'<div class="stat-label sans">{escape(stat["label"])}</div>'
        f'<div class="stat-note sans">{escape(stat["note"])}</div>'
        "</div>"
    )


def toc_item(item: dict) -> str:
    return (
        '<div class="toc-item">'
        f'<div class="toc-num mono">{escape(item["num"])}</div>'
        f'<div class="toc-title">{escape(item["title"])}</div>'
        f'<div class="toc-page mono">{escape(item["page"])}</div>'
        "</div>"
    )


def front_page_density_class(slide: dict) -> str:
    text_blocks = [
        slide["headline"],
        slide["lead"],
        slide["photo_caption"],
        *slide["lead_columns"],
        *(card.get("title", "") for card in slide["side_cards"]),
        *(card["body"] for card in slide["side_cards"]),
    ]
    density_score = sum(len(block.replace(" ", "")) for block in text_blocks)
    classes: list[str] = []
    if density_score >= 150:
        classes.append("compact-front-page")
    if len(slide["headline"].replace(" ", "")) >= 16:
        classes.append("balanced-front-headline")
    return " ".join(classes)


def render_front_page(slide: dict) -> str:
    side_cards = "".join(
        clipping(card.get("title", ""), card["body"], tag=card["tag"], seal=card.get("seal"), extra_class="side-clipping")
        for card in slide["side_cards"]
    )
    body = (
        '<header class="front-header">'
        '<div class="masthead-row">'
        '<div class="masthead-block">'
        f'<div class="masthead-name">{escape(slide["masthead"])}</div>'
        f'<div class="masthead-sub sans">{escape(slide["masthead_sub"])}</div>'
        "</div>"
        f'{issue_mark(slide["issue_mark_title"], slide["issue_mark_note"])}'
        "</div>"
        '<div class="dateline sans">'
        f'<span>{escape(slide["dateline_left"])}</span>'
        f'<span>{escape(slide["dateline_right"])}</span>'
        "</div>"
        "</header>"
        '<section class="front-layout">'
        '<aside class="vertical-rail">'
        f'<div class="rail-kicker sans">{escape(slide["rail_kicker"])}</div>'
        f'<div class="vertical-title">{escape(slide["rail_title"])}</div>'
        f'<div class="rail-date sans">{text_to_html(slide["rail_date"])}</div>'
        "</aside>"
        '<section class="lead-story">'
        f'{reverse_label(slide["lead_label"])}'
        f'<h1 class="front-headline">{escape(slide["headline"])}</h1>'
        f'<p class="lead-copy">{escape(slide["lead"])}</p>'
        '<div class="lead-columns">'
        f'<p class="body-copy sans">{escape(slide["lead_columns"][0])}</p>'
        f'<p class="body-copy sans">{escape(slide["lead_columns"][1])}</p>'
        "</div>"
        '<div class="front-bottom">'
        '<div class="news-photo"><span class="photo-stamp sans">PHOTO PLATE</span></div>'
        f'<p class="caption sans">{escape(slide["photo_caption"])}</p>'
        "</div>"
        "</section>"
        f'<aside class="side-stack">{side_cards}</aside>'
        "</section>"
    )
    return wrap_slide(slide, body, extra_sheet_class=front_page_density_class(slide))


def render_component_sheet(slide: dict) -> str:
    cards_html = "".join(
        clipping(card["title"], card["body"], tag=card["tag"], extra_class="component-clipping")
        for card in slide["cards"]
    )
    stats_html = "".join(stat_card(stat) for stat in slide["stats"])
    timeline_html = "".join(
        '<div class="timeline-item">'
        f'<div class="timeline-label">{escape(item["label"])}</div>'
        f'<p class="timeline-copy sans">{escape(item["body"])}</p>'
        "</div>"
        for item in slide["timeline"]
    )
    body = (
        '<section class="sheet-head">'
        f'<h1 class="sheet-title">{escape(slide["title"])}</h1>'
        f'<p class="sheet-lede sans">{escape(slide["lede"])}</p>'
        "</section>"
        f'<section class="component-cards">{cards_html}</section>'
        '<section class="component-lower">'
        '<div class="component-left">'
        f'<div class="stats-strip">{stats_html}</div>'
        f'<div class="timeline-board">{timeline_html}</div>'
        "</div>"
        f'{clipping(slide["action_title"], slide["action_body"], tag="编辑规则", extra_class="action-clipping")}'
        "</section>"
    )
    return wrap_slide(slide, body)


def render_special_issue(slide: dict) -> str:
    toc_html = "".join(toc_item(item) for item in slide["toc"])
    body = (
        '<section class="special-topline">'
        f'{reverse_label(slide["tag"], "special-tag")}'
        f'<div class="special-meta sans">{escape(slide["meta"])}</div>'
        "</section>"
        '<section class="special-hero">'
        '<div class="cover-plaque">'
        f'<h1 class="cover-title">{text_to_html(slide["title"])}</h1>'
        f'<p class="cover-subtitle sans">{escape(slide["subtitle"])}</p>'
        "</div>"
        '<div class="special-side">'
        f'{clipping("", slide["filed_under"], tag="Filed Under", extra_class="meta-clipping")}'
        f'{clipping("", slide["version"], tag="Version", extra_class="meta-clipping")}'
        "</div>"
        "</section>"
        '<section class="cover-note-row">'
        f'<p class="cover-note sans">{escape(slide["cover_note"])}</p>'
        f'<div class="cover-meta sans">{text_to_html(slide["cover_meta"])}</div>'
        "</section>"
        f'<section class="toc-strip">{toc_html}</section>'
    )
    return wrap_slide(slide, body)


def render_article_spread(slide: dict) -> str:
    bullets_html = "".join(f"<li>{escape(item)}</li>" for item in slide["bullets"])
    body = (
        '<section class="header-band">'
        f'<div class="chapter-mark sans">{escape(slide["chapter"])}</div>'
        '<div class="article-band">'
        f'<h1 class="article-title">{escape(slide["title"])}</h1>'
        f'<p class="article-lede sans">{escape(slide["lede"])}</p>'
        "</div>"
        "</section>"
        '<section class="article-body">'
        '<div class="columns-two">'
        f'<p class="body-copy sans">{escape(slide["columns"][0])}</p>'
        '<div class="column-rule"></div>'
        f'<p class="body-copy sans">{escape(slide["columns"][1])}</p>'
        "</div>"
        '<aside class="article-side">'
        f'{clipping(slide["panel_title"], slide["panel_body"], tag="SIDE PANEL", extra_class="panel-clipping")}'
        f'<ul class="bullet-trail sans">{bullets_html}</ul>'
        '<div class="quote-box">'
        '<div class="quote-rule"></div>'
        f'<div class="quote-copy">{escape(slide["quote"])}</div>'
        f'<div class="quote-cite sans">{escape(slide["cite"])}</div>'
        "</div>"
        "</aside>"
        "</section>"
    )
    return wrap_slide(slide, body)


def render_correspondence(slide: dict) -> str:
    paragraphs_html = "".join(f'<p class="letter-paragraph">{escape(paragraph)}</p>' for paragraph in slide["paragraphs"])
    evidence_html = "".join(f'<div class="evidence-chip sans">{escape(item)}</div>' for item in slide["evidence"])
    body = (
        '<section class="correspondence-top">'
        '<div class="tag-plaque">'
        f'<div class="plaque-label sans">{escape(slide["plaque_label"])}</div>'
        f'<div class="plaque-value">{escape(slide["plaque_value"])}</div>'
        "</div>"
        f'{clipping(slide["sender_org"], slide["sender_meta"], tag="寄件人", extra_class="sender-clipping")}'
        "</section>"
        '<section class="subject-card">'
        '<div class="subject-head">'
        '<div class="subject-head-main">函件主题</div>'
        '<div class="subject-head-sub sans">Formal Correspondence</div>'
        "</div>"
        '<div class="subject-body">'
        f'<h1 class="subject-title">{escape(slide["subject_title"])}</h1>'
        '<div class="subject-meta sans">'
        f'<span>致：{escape(slide["recipient"])}</span>'
        f'<span>分类：{escape(slide["category"])}</span>'
        "</div>"
        "</div>"
        "</section>"
        '<section class="body-frame">'
        '<div class="body-frame-content">'
        f'<div class="salutation">{escape(slide["salutation"])}</div>'
        f"{paragraphs_html}"
        f'<div class="evidence-list">{evidence_html}</div>'
        '<div class="sign-row">'
        '<div class="sign-left">'
        f'<div class="regards">{escape(slide["regards"])}</div>'
        f'<div class="closing-note sans">{escape(slide["closing_note"])}</div>'
        "</div>"
        '<div class="sign-right">'
        f'<div class="signature">{escape(slide["signature"])}</div>'
        f'<div class="signature-meta sans">{text_to_html(slide["signature_meta"])}</div>'
        "</div>"
        "</div>"
        "</div>"
        "</section>"
        f'<div class="attachment-bar sans">{escape(slide["attachments"])}</div>'
    )
    return wrap_slide(slide, body)


def render_routing_desk(slide: dict) -> str:
    wires_html = "".join(
        '<div class="wire-row">'
        f'<div class="wire-prompt">“{escape(item["prompt"])}”</div>'
        f'<div class="route-tag mono">{escape(item["route"])}</div>'
        f'<div class="wire-note sans">{escape(item["note"])}</div>'
        "</div>"
        for item in slide["wires"]
    )
    rules_html = "".join(f"<li>{escape(item)}</li>" for item in slide["routing_rules"])
    body = (
        '<section class="sheet-head">'
        f'<h1 class="sheet-title">{escape(slide["desk_name"])}</h1>'
        f'<p class="sheet-lede sans">{escape(slide["desk_sub"])}</p>'
        "</section>"
        '<section class="routing-layout">'
        f'<div class="wire-list">{wires_html}</div>'
        '<div class="routing-side">'
        '<section class="clipping rules-panel">'
        '<div class="clip-tag sans">ROUTING RULES</div>'
        '<h3 class="clip-title">触发原则</h3>'
        f'<ul class="rules-list sans">{rules_html}</ul>'
        "</section>"
        '<section class="stamp-card">'
        f'{issue_mark(slide["stamp_title"], "", "stamp-mark")}'
        f'<div class="stamp-note sans">{text_to_html(slide["stamp_note"])}</div>'
        "</section>"
        "</div>"
        "</section>"
    )
    return wrap_slide(slide, body)


def render_production_desk(slide: dict) -> str:
    steps_html = "".join(
        clipping(step["title"], step["body"], tag=step["tag"], extra_class="step-clipping")
        for step in slide["steps"]
    )
    checks_html = "".join(f'<div class="check-card">{escape(item)}</div>' for item in slide["checks"])
    commands = "\n".join(slide["commands"])
    body = (
        '<section class="sheet-head">'
        f'<h1 class="sheet-title">{escape(slide["title"])}</h1>'
        f'<p class="sheet-lede sans">{escape(slide["lede"])}</p>'
        "</section>"
        f'<section class="production-steps">{steps_html}</section>'
        '<section class="commands-band">'
        '<div class="band-label mono">印务命令</div>'
        f'<pre class="commands-code mono"><code>{escape(commands)}</code></pre>'
        "</section>"
        f'<section class="check-grid">{checks_html}</section>'
    )
    return wrap_slide(slide, body)


def render_final_edition(slide: dict) -> str:
    body = (
        '<header class="final-header">'
        f'<div class="masthead-name final-masthead">{escape(slide["masthead"])}</div>'
        f'<div class="masthead-sub sans">{escape(slide["masthead_sub"])}</div>'
        "</header>"
        '<section class="final-layout">'
        '<div class="final-main">'
        f'<h1 class="final-title">{text_to_html(slide["final_title"])}</h1>'
        f'<p class="final-lede sans">{escape(slide["final_lede"])}</p>'
        "</div>"
        f'<div class="edition-panel mono">{text_to_html(slide["edition_panel"])}</div>'
        "</section>"
        f'<div class="final-closing">{escape(slide["closing_line"])}</div>'
    )
    return wrap_slide(slide, body)


RENDERERS = {
    "front-page": render_front_page,
    "component-sheet": render_component_sheet,
    "special-issue": render_special_issue,
    "article-spread": render_article_spread,
    "correspondence": render_correspondence,
    "routing-desk": render_routing_desk,
    "production-desk": render_production_desk,
    "final-edition": render_final_edition,
}


def main() -> None:
    frontmatter = """---
theme: default
title: Kami · Republican Newspaper Edition
titleTemplate: '%s'
info: Online slide deck companion for republican-newspaper.
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
