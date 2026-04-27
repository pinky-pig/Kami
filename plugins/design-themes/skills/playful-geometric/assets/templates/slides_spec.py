#!/usr/bin/env python3
"""Shared slide schema for the Playful Geometric PPTX and Slidev renderers."""

from __future__ import annotations


DECK = [
    {
        "kind": "cover",
        "page": 1,
        "section": "FRONT STICKER",
        "eyebrow": "KAMI DEMO",
        "title": "把 AI 文档\n排成几何贴纸",
        "subtitle": "Stable Grid, Wild Decoration. 内容保持清楚，周围用圆、三角、pill、斜纹和硬偏移阴影制造开心的触感。",
        "callouts": [
            {
                "fill": "mint",
                "title": "No stale frame",
                "body": "不用旧式页框，\n只保留稳定结构。",
            },
            {
                "fill": "pink",
                "title": "Primitive\nShapes",
                "body": "圆、三角、pill、\n斜纹轮流出场。",
            },
        ],
    },
    {
        "kind": "tokens",
        "page": 2,
        "section": "TOKENS",
        "title": "明亮色彩，像贴纸盒",
        "cards": [
            {"label": "Violet", "fill": "violet"},
            {"label": "Pink", "fill": "pink"},
            {"label": "Amber", "fill": "yellow"},
            {"label": "Mint", "fill": "mint"},
        ],
        "summary": "颜色不是给旧方框换皮，而是轮流成为 sticker、badge、shadow、shape。",
    },
    {
        "kind": "grid",
        "page": 3,
        "section": "STABLE GRID",
        "title": "稳定网格，野生装饰",
        "cards": [
            {"badge": "01", "title": "Hero Card", "fill": "white"},
            {"badge": "02", "title": "Side Bubble", "fill": "mint"},
            {"badge": "03", "title": "Metric Sticker", "fill": "yellow"},
            {"badge": "04", "title": "Action Pop", "fill": "pink"},
        ],
        "callout": "结构稳定，装饰可以玩。",
    },
    {
        "kind": "outputs",
        "page": 4,
        "section": "OUTPUTS",
        "title": "PDF 与 PPT 使用同一套几何语言",
        "rows": [
            {
                "name": "One-pager",
                "desc": "hero sticker + metric chips + action pop",
                "fill": "white",
            },
            {
                "name": "Long-doc",
                "desc": "cover stickers + bouncy toc + proof sidebar",
                "fill": "mint",
            },
            {
                "name": "Letter",
                "desc": "speech bubble title + proof pops + rounded body",
                "fill": "pink",
            },
        ],
    },
    {
        "kind": "end",
        "page": 5,
        "section": "FINAL",
        "eyebrow": "STICKER MODE",
        "title": "不是换色。\n是换成贴纸世界。",
        "summary": "Friendly. Tactile. Pop. Energetic.",
        "side_note": {
            "fill": "white",
            "title": "Keep it bright",
            "body": "Grid first,\njoy second.",
        },
    },
]


TOTAL_SLIDES = len(DECK)
