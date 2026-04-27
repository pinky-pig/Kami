#!/usr/bin/env python3
"""Shared slide schema for the Neo-Brutalism PPTX and Slidev renderers."""

from __future__ import annotations


DECK = [
    {
        "kind": "cover",
        "page": 1,
        "section": "LOUD COVER",
        "eyebrow": "KAMI DEMO",
        "title": "把 AI 文档\n排成粗野海报",
        "strapline": "RAW STRUCTURE / HARD SHADOW / HIGH SATURATION / NO SOFTNESS",
        "hero_tone": "red",
        "stickers": [
            {"tone": "yellow", "text": "NO OLD\nFRAME", "text_tone": "ink"},
            {"tone": "black", "text": "STICKER\nCOLLAGE", "text_tone": "paper"},
        ],
    },
    {
        "kind": "tokens",
        "page": 2,
        "section": "TOKENS",
        "title": "颜色必须大声",
        "cards": [
            {"name": "RED", "tone": "red", "text_tone": "ink"},
            {"name": "YELLOW", "tone": "yellow", "text_tone": "ink"},
            {"name": "VIOLET", "tone": "violet", "text_tone": "ink"},
            {"name": "BLACK", "tone": "black", "text_tone": "paper"},
        ],
        "summary": "没有柔和渐变，没有灰色过渡。每个色块都像贴在墙上的 DIY 海报。",
    },
    {
        "kind": "composition",
        "page": 3,
        "section": "COMPOSITION",
        "title": "有组织的混乱",
        "hero": {"tone": "paper", "text": "60/40\nASYMMETRY", "text_tone": "ink"},
        "stickers": [
            {"tone": "yellow", "text": "ROTATED BADGES", "text_tone": "ink"},
            {"tone": "violet", "text": "HARD\nSHADOWS", "text_tone": "ink"},
        ],
    },
    {
        "kind": "outputs",
        "page": 4,
        "section": "OUTPUTS",
        "title": "PDF 与 PPT 都要像 zine，不像表格",
        "rows": [
            {
                "name": "ONE-PAGER",
                "desc": "loud hero / marquee / rotated cards",
                "tone": "red",
                "rotation": -1.0,
                "text_tone": "ink",
            },
            {
                "name": "LONG-DOC",
                "desc": "poster cover / blocky toc / proof column",
                "tone": "yellow",
                "rotation": 0.0,
                "text_tone": "ink",
            },
            {
                "name": "LETTER",
                "desc": "raw subject bar / massive title / evidence sticker",
                "tone": "violet",
                "rotation": 1.0,
                "text_tone": "ink",
            },
        ],
    },
    {
        "kind": "end",
        "page": 5,
        "section": "FINAL",
        "title": "不是换色。\n是换成反精致海报。",
        "hero_tone": "yellow",
        "badge": {"tone": "red", "text": "ANTI\nBORING", "text_tone": "paper"},
    },
]

TOTAL_SLIDES = len(DECK)
