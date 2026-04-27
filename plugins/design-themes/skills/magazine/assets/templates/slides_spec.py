#!/usr/bin/env python3
"""Shared Guizang Magazine slide schema for PPTX and Slidev renderers."""

from __future__ import annotations

from typing import Any


DECK: list[dict[str, Any]] = [
    {
        "kind": "cover",
        "theme": "dark",
        "page": 1,
        "chrome_left": "GUIZANG MAGAZINE",
        "chrome_mid": "SLIDE DEMO",
        "chrome_right": "ACT 00",
        "foot_left": "EDITORIAL SYSTEM",
        "foot_right": "VOL. 01",
        "page_text": "01 / 08",
        "kicker": "EDITORIAL SYSTEM",
        "title": "把 AI 文档\n排成真正的新主题",
        "body": "Guizang 的重点不是一层纸感，也不是一套颜色，而是 chrome、hero、组件、留白和节奏共同组成的出版语言。",
        "meta": [
            {
                "label": "Formats",
                "value": "HTML / PDF / PPTX",
                "note": "一个主题，多个出口",
            },
            {
                "label": "Typography",
                "value": "Serif / Sans / Mono",
                "note": "标题、正文、元信息分层",
            },
            {
                "label": "Rhythm",
                "value": "Dark Editorial",
                "note": "全套输出保持单一黑色模式",
            },
        ],
        "quote": {
            "text": "主题是系统，不是调色板。",
            "source": "GUIZANG PRINCIPLE",
        },
    },
    {
        "kind": "shift",
        "theme": "dark",
        "page": 2,
        "chrome_left": "WHAT CHANGED",
        "chrome_mid": "SYSTEM NOT PALETTE",
        "chrome_right": "ACT I",
        "foot_left": "LANGUAGE SHIFT",
        "foot_right": "02 / 08",
        "kicker": "NOT A RECOLOR",
        "title": "这次重做的，是版式语法",
        "body": "旧版本的问题在于保留了 manuscript 的 framed page、plaque block 和 archive card 母结构。现在换成了更接近 Guizang 原版 deck 的 headline、stat spread、rowline 和 chapter rhythm。",
        "stats": [
            {"label": "HERO", "value": "01", "note": "封面和幕封负责拉开节奏"},
            {"label": "COMPONENTS", "value": "06", "note": "stat / rowline / pillar / quote"},
            {"label": "SURFACES", "value": "03", "note": "dark theme / editorial card"},
            {"label": "DELIVERABLES", "value": "05", "note": "核心模板同步改造"},
        ],
        "rows": [
            {
                "title": "Chrome",
                "body": "页眉页脚回到杂志导航语义，而不是文档边框装饰。",
                "tag": "META",
            },
            {
                "title": "Hierarchy",
                "body": "标题由衬线负责冲击，正文交给 sans，元信息交给 mono。",
                "tag": "TYPE",
            },
            {
                "title": "Rhythm",
                "body": "HTML / PDF / PPT 都有 hero 页与正文页的明显节奏切换。",
                "tag": "FLOW",
            },
        ],
    },
    {
        "kind": "rhythm",
        "theme": "dark",
        "page": 3,
        "chrome_left": "RHYTHM",
        "chrome_mid": "HERO / NON-HERO",
        "chrome_right": "ACT I",
        "foot_left": "EDITORIAL BREATHING",
        "foot_right": "03 / 08",
        "kicker": "LAYOUT RHYTHM",
        "title": "封面、转场、正文，不再长得一样",
        "body": "Guizang 的阅读体验来自版式密度变化：hero 页负责仪式感，正文页负责信息密度，章节页负责呼吸和转场。",
        "panel": {
            "label": "ACT DIVIDER",
            "caption": "HERO PAGE",
        },
        "quote": {
            "text": "如果每一页都像正文，读者就不会记得章节转换。",
            "source": "PACING RULE",
        },
        "pillars": [
            {"index": "01", "title": "Hero", "body": "大标题、少量文字、承担记忆点。"},
            {"index": "02", "title": "Body", "body": "rowline、stat、正文段落承担信息。"},
            {"index": "03", "title": "Act", "body": "章节页负责切换呼吸和视角。"},
        ],
    },
    {
        "kind": "pipeline",
        "theme": "dark",
        "page": 4,
        "chrome_left": "PIPELINE",
        "chrome_mid": "FROM INPUT TO OUTPUT",
        "chrome_right": "ACT II",
        "foot_left": "PRODUCTION METHOD",
        "foot_right": "04 / 08",
        "kicker": "DELIVERY CHAIN",
        "title": "脚手架只管生成，主题自己决定长相",
        "body": "republican-manuscript 只能保留目录和构建方法；真正决定产物气质的是 Guizang 自己的 layout grammar。",
        "steps": [
            {"index": "01", "title": "Route", "body": "判断文档类型与语言。"},
            {"index": "02", "title": "Compose", "body": "把内容压进 Guizang 组件。"},
            {"index": "03", "title": "Build", "body": "导出 HTML / PDF / PPTX。"},
            {"index": "04", "title": "Verify", "body": "页数、字体、占位符一起检查。"},
        ],
        "rows": [
            {
                "title": "AGENTS.md",
                "body": "严格禁止把 manuscript 当成视觉参考继续套壳。",
                "tag": "RULE",
            },
            {
                "title": "templates",
                "body": "HTML、PDF、PPT 都重新改为 Guizang-native 结构。",
                "tag": "OUTPUT",
            },
            {
                "title": "demos",
                "body": "演示文件也同步用新节奏重生成，不再沿用旧样张。",
                "tag": "DEMO",
            },
        ],
    },
    {
        "kind": "divider",
        "theme": "dark",
        "page": 5,
        "chrome_left": "ACT DIVIDER",
        "chrome_mid": "ONE LANGUAGE / MANY OUTPUTS",
        "chrome_right": "ACT III",
        "foot_left": "TRANSITION PAGE",
        "foot_right": "05 / 08",
        "kicker": "ACT III",
        "title": "同一种语言\n不同出口",
        "body": "HTML、PDF、PPTX 不需要长得完全一样，但它们必须能被认出属于同一个主题系统。",
        "pillars": [
            {"index": "HTML", "title": "文档页", "body": "章节、正文、引用与导航。"},
            {"index": "PDF", "title": "纸面版", "body": "页数控制、阅读密度与导出。"},
            {"index": "PPTX", "title": "演示版", "body": "hero、转场与讲述节奏。"},
        ],
        "quote": {
            "text": "主题的一致性，来自层级和节奏，而不是每处都复制同一个卡片。",
            "source": "SYSTEM CONSISTENCY",
        },
    },
    {
        "kind": "components",
        "theme": "dark",
        "page": 6,
        "chrome_left": "COMPONENTS",
        "chrome_mid": "GUIZANG GRAMMAR",
        "chrome_right": "ACT III",
        "foot_left": "CORE PARTS",
        "foot_right": "06 / 08",
        "kicker": "CORE COMPONENTS",
        "title": "现在这套 deck 用什么说话",
        "pillars": [
            {
                "index": "01",
                "title": "Chrome / Foot",
                "body": "用页眉页脚做导航语义，建立杂志感，而不是外框。",
            },
            {
                "index": "02",
                "title": "Serif / Sans / Mono",
                "body": "标题冲击、正文承载、元信息节奏，各有明确角色。",
            },
            {
                "index": "03",
                "title": "Stat / Rowline / Pillar",
                "body": "数字页、表格式正文和并列观点页，构成可复用组件库。",
            },
        ],
        "quote": {
            "text": "组件不是装饰集合，而是内容被组织的方式。",
            "source": "LAYOUT SYSTEM",
        },
    },
    {
        "kind": "deliverables",
        "theme": "dark",
        "page": 7,
        "chrome_left": "DELIVERABLES",
        "chrome_mid": "THEME COVERAGE",
        "chrome_right": "ACT IV",
        "foot_left": "SHIPPING NOW",
        "foot_right": "07 / 08",
        "kicker": "OUTPUTS",
        "title": "这套新主题已经覆盖的交付件",
        "body": "不只是 core trio。简历、作品集和中英 deck 也同步切到 Guizang 的 editorial 语法，避免同一 skill 内部风格断层。",
        "rows": [
            {
                "title": "One-Pager",
                "body": "hero headline + stat spread + editorial blocks + callout",
                "tag": "HTML",
            },
            {
                "title": "Long Doc",
                "body": "cover / overview / problem / method / conclusion / appendix",
                "tag": "PDF",
            },
            {
                "title": "Letter",
                "body": "subject block + correspondence body + evidence sidebar",
                "tag": "DOC",
            },
            {
                "title": "Resume",
                "body": "identity hero + metrics + timeline + open source spread",
                "tag": "CV",
            },
            {
                "title": "Portfolio",
                "body": "editorial cover + case spreads + selected works + contact",
                "tag": "BOOK",
            },
        ],
        "panel": {
            "label": "DEMO BUNDLE",
            "caption": "HTML / PDF / PPTX",
        },
    },
    {
        "kind": "close",
        "theme": "dark",
        "page": 8,
        "chrome_left": "END",
        "chrome_mid": "SYSTEM COMPLETE",
        "chrome_right": "ACT V",
        "foot_left": "GUIZANG MAGAZINE",
        "foot_right": "08 / 08",
        "kicker": "FINAL LINE",
        "title": "主题是系统，\n不是换色版。",
        "body": "真正的新主题，必须在 HTML、PDF、PPTX 和 demo 里都能一眼认出来，而不是只有 palette 不一样。",
        "quote": {
            "text": "如果结果还像旧主题，那就说明它还没有被重做。",
            "source": "AGENTS RULE",
        },
    },
]

TOTAL_SLIDES = len(DECK)
