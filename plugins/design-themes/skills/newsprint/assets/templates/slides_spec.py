#!/usr/bin/env python3
"""Shared slide schema for the Newsprint PPTX and Slidev renderers."""

from __future__ import annotations

from typing import Any


DECK: list[dict[str, Any]] = [
    {
        "kind": "cover",
        "page": 1,
        "section": "FRONT PAGE",
        "label": "Breaking",
        "title": "把 AI 文档\n排成出版物版面",
        "body": "Newsprint 不应该是旧主题换色，而是一整套报纸式信息组织：头版标题、导语、分栏、边栏事实盒、反黑版块和少量红色编辑标记。",
        "edition": "EDITION\nVOL. 1.0\nKAMI NEWSROOM",
        "note": "新闻纸底 / 12 栏栅格 / 高对比字体 / collapsed borders / no rounded corners",
    },
    {
        "kind": "grid",
        "page": 2,
        "section": "LAYOUT SYSTEM",
        "title": "12 栏，不是方框套方框",
        "body": "Prompt 要求的 visible structure 来自分栏和共享边线。页面不再有厚重外框，也不再用牌匾包标题。",
        "columns": [
            {"index": 1, "tone": "muted"},
            {"index": 2, "tone": "muted"},
            {"index": 3, "tone": "muted"},
            {"index": 4, "tone": "paper"},
            {"index": 5, "tone": "paper"},
            {"index": 6, "tone": "paper"},
            {"index": 7, "tone": "paper"},
            {"index": 8, "tone": "paper"},
            {"index": 9, "tone": "muted"},
            {"index": 10, "tone": "muted"},
            {"index": 11, "tone": "muted"},
            {"index": 12, "tone": "muted"},
        ],
        "hero_label": "Hero 8 Col",
        "side_label": "Side 4 Col",
        "note": "Collapsed grid borders: container has left/top, cells add right/bottom.",
    },
    {
        "kind": "components",
        "page": 3,
        "section": "COMPONENT LANGUAGE",
        "title": "组件像报纸栏目，不像档案卡片",
        "cards": [
            {
                "tag": "Unit 01",
                "title": "Masthead",
                "body": "大标题和版面信息同屏出现，建立出版物身份。",
            },
            {
                "tag": "Unit 02",
                "title": "Lede",
                "body": "第一段直接给结论，支持 drop cap 和 justify 正文。",
            },
            {
                "tag": "Unit 03",
                "title": "Sidebar",
                "body": "反黑事实盒承担强调，不靠一堆厚边框。",
            },
        ],
        "ticker": "TICKER | KEY FIGURE 47% | EDITORIAL RED ONLY WHEN IT MATTERS | NO SOFT SHADOWS",
    },
    {
        "kind": "typography",
        "page": 4,
        "section": "TYPOGRAPHIC DRAMA",
        "label": "Display",
        "title": "Massive serif\nheadlines",
        "body": "正文不是装进框里的说明文字，而是报纸式 column copy。需要时使用首字下沉、紧凑行距、明确的 metadata 和极少量红色。",
        "drop_cap": "A",
        "drop_text": "drop cap creates editorial rhythm without adding decorative frames.",
    },
    {
        "kind": "inverted",
        "page": 5,
        "section": "INVERTED SECTION",
        "panel_label": "How It Works",
        "title": "反黑版块\n替代厚重外框",
        "body": "Prompt 明确要求至少一个 inverted section。它是新闻纸风格的重音，而不是旧主题的深色框架。",
        "steps": [
            {
                "number": "01",
                "title": "Route",
                "body": "用报纸单元组织内容，而不是把旧模块重新涂黑。",
            },
            {
                "number": "02",
                "title": "Rewrite",
                "body": "用报纸单元组织内容，而不是把旧模块重新涂黑。",
            },
            {
                "number": "03",
                "title": "Typeset",
                "body": "用报纸单元组织内容，而不是把旧模块重新涂黑。",
            },
        ],
    },
    {
        "kind": "outputs",
        "page": 6,
        "section": "OUTPUTS",
        "title": "同一套新闻纸语言覆盖 PDF 与 PPT",
        "rows": [
            {
                "name": "ONE-PAGER",
                "desc": "头版 brief：masthead / ticker / hero / data / sidebar",
            },
            {
                "name": "LONG-DOC",
                "desc": "跨页 report：cover / contents / article spread / data column",
            },
            {
                "name": "LETTER",
                "desc": "correspondence desk：byline / subject / letter body / evidence column",
            },
        ],
    },
    {
        "kind": "end",
        "page": 7,
        "section": "FINAL",
        "title": "不是换色。\n是换版面逻辑。",
        "panel": "NO RADIUS\nNO SOFT SHADOW\nNO PLAQUES\nNO MANUSCRIPT FRAME",
        "tagline": "All the News That's Fit to Print.",
    },
]

TOTAL_SLIDES = len(DECK)
DISPLAY_TOTAL = 8
