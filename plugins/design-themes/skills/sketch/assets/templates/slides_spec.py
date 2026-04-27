#!/usr/bin/env python3
"""Shared slide schema for the Sketch PPTX and Slidev renderers."""

from __future__ import annotations


DECK = [
    {
        "kind": "cover",
        "page": 1,
        "section": "NOTE WALL",
        "title": "把文档贴成\n草图墙",
        "subtitle": "纸张纹理、手写字体、wobble 边框、硬偏移阴影。看起来像 brainstorm 现场，而不是 polished 年报。",
        "sticky": {
            "label": "Now",
            "body": "不做直线排版。\n做一面工作板。",
        },
    },
    {
        "kind": "tokens",
        "page": 2,
        "section": "TOKENS",
        "title": "四种手绘信号",
        "cards": [
            {"label": "Paper", "fill": "card", "rotation": -2.0, "attachment": "tape", "dot": "ink"},
            {"label": "Post-it", "fill": "note", "rotation": 1.8, "attachment": "tack", "dot": "ink"},
            {"label": "Red Marker", "fill": "card", "rotation": -1.0, "attachment": "tape", "dot": "accent"},
            {"label": "Blue Pen", "fill": "card", "rotation": 2.0, "attachment": "tack", "dot": "secondary"},
        ],
        "summary": "Warm paper + handwritten type + hard offset shadow + small rotation.",
    },
    {
        "kind": "system",
        "page": 3,
        "section": "SYSTEM",
        "title": "不是换色，是换工作现场",
        "cards": [
            {
                "label": "No straight lines",
                "body": "有点歪，有点手写，像刚刚钉上去。",
                "fill": "card",
                "rotation": -2.4,
                "attachment": "tape",
            },
            {
                "label": "Tape / tack",
                "body": "有点歪，有点手写，像刚刚钉上去。",
                "fill": "note",
                "rotation": 1.2,
                "attachment": "tack",
            },
            {
                "label": "Hard shadow",
                "body": "有点歪，有点手写，像刚刚钉上去。",
                "fill": "card",
                "rotation": -1.2,
                "attachment": "",
            },
        ],
        "summary": "所有重点模块都应该像卡片，不像软件面板。",
    },
    {
        "kind": "outputs",
        "page": 4,
        "section": "OUTPUTS",
        "title": "PDF 与 PPT 共用手绘语言",
        "rows": [
            {
                "name": "One-pager",
                "desc": "taped hero + side note + 3 stickies",
                "fill": "card",
                "rotation": -1.4,
                "attachment": "tape",
                "offset": 0.0,
            },
            {
                "name": "Long-doc",
                "desc": "pin-board cover + article sheet + fact notes",
                "fill": "note",
                "rotation": 1.1,
                "attachment": "",
                "offset": 0.2,
            },
            {
                "name": "Letter",
                "desc": "header board + dashed subject + proof notes",
                "fill": "card",
                "rotation": -0.8,
                "attachment": "tack",
                "offset": 0.0,
            },
        ],
    },
    {
        "kind": "end",
        "page": 5,
        "section": "FINAL",
        "title": "不是改配色。\n是整面换成手绘草稿。",
        "summary": "Warm. Human. Playful. Deliberately unfinished.",
        "sticky": {
            "label": "Messy",
            "body": "on purpose",
        },
    },
]

TOTAL_SLIDES = len(DECK)
