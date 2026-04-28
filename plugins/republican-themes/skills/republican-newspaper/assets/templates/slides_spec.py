#!/usr/bin/env python3
"""Shared slide deck schema for the PPTX and Slidev newspaper renderers."""

from __future__ import annotations

from typing import Any


DECK: list[dict[str, Any]] = [
    {
        "kind": "cover",
        "section": "REPUBLICAN NEWSPAPER EDITION",
        "page": 1,
        "kicker": "KAMI · 特刊 DEMO",
        "title": "把 AI 文档\n排成报纸号外",
        "subtitle": "黑色铅字 / 旧报纸底 / 剪报框线",
        "body": "Just tell Claude what you need:\n“帮我生成一份白皮书” / “生成一份项目方案” / “帮我写一份推荐信” / “做一套汇报 slides”",
        "metrics": [
            {"value": "05", "label": "demo set", "note": "docs + slides"},
            {"value": "01", "label": "visual rule", "note": "black ink"},
        ],
        "meta": "2026.04 · Kami Fork",
    },
    {
        "kind": "principle",
        "section": "METHOD",
        "page": 2,
        "number": 1,
        "title": "生成原理",
        "lede": "好看的本质不是每次重新设计，而是把内容填进稳定模板。",
        "cards": [
            {"label": "STEP 01", "title": "路由", "body": "先判断语言与文档类型：one-pager、long-doc、letter、slides。"},
            {"label": "STEP 02", "title": "整理", "body": "把 raw material 拆成事实、数字、判断和行动，而不是直接堆文字。"},
            {"label": "STEP 03", "title": "填充", "body": "使用固定骨架承载内容，避免 AI 每次自由发挥版式。"},
            {"label": "STEP 04", "title": "校验", "body": "构建脚本检查页数、字体、占位符与 CSS 约束。"},
        ],
        "summary": "固定版式 + design token + 字体层级 + 构建校验",
    },
    {
        "kind": "visual-language",
        "section": "DESIGN TOKENS",
        "page": 3,
        "number": 2,
        "title": "民国报纸视觉语言",
        "lede": "不做复古海报，不做彩色杂志，只把专业文档整理成可信的报纸特刊。",
        "swatches": [
            {"name": "Black Ink", "fill": "#161411", "hex": "#161411", "use": "报头 / 框线 / 反白条"},
            {"name": "Newsprint", "fill": "#E8DFC9", "hex": "#E8DFC9", "use": "正文纸面"},
            {"name": "Clipping", "fill": "#F5EBD3", "hex": "#F5EBD3", "use": "剪报块"},
            {"name": "Warm Rule", "fill": "#B9AA91", "hex": "#B9AA91", "use": "细线和分隔"},
        ],
        "callout": {
            "title": "装饰边界",
            "body": "只允许报头、日期线、反白栏目条、剪报框和一枚红印；不加入现代渐变和彩色杂志图。",
        },
    },
    {
        "kind": "templates",
        "section": "TEMPLATES",
        "page": 4,
        "number": 3,
        "title": "现在能生成什么",
        "lede": "中文 v1 的正式能力聚焦三类高频文档，简历和作品集已保留为补充样例。",
        "cards": [
            {"label": "1 PAGE", "title": "One-Pager", "body": "公司介绍、项目方案、执行摘要。重点是 30 秒抓住核心。"},
            {"label": "MULTI", "title": "Long Doc", "body": "白皮书、长文报告、年度总结。强调章节结构与证据链。"},
            {"label": "1 PAGE", "title": "Letter", "body": "正式信件、推荐信、推荐函。关系、证据、匹配、推荐。"},
            {"label": "DEMO", "title": "Resume", "body": "固定坐标版简历样例，适合验证黑框报纸式布局。"},
            {"label": "DEMO", "title": "Portfolio", "body": "作品集样例，保留更多视觉叙事与项目卡片。"},
        ],
    },
    {
        "kind": "natural-prompts",
        "section": "NATURAL PROMPTS",
        "page": 5,
        "number": 4,
        "title": "不用 slash command",
        "lede": "用户只要说任务，skill 根据意图选择模板。输出是文档，不是聊天里的格式建议。",
        "prompts": [
            {"text": "帮我生成一份白皮书", "route": "long-doc"},
            {"text": "生成一份项目方案", "route": "one-pager"},
            {"text": "帮我写一份推荐信", "route": "letter"},
            {"text": "帮我把这些内容排版成好看的 PDF", "route": "infer"},
            {"text": "做一套汇报 slides", "route": "slides"},
        ],
        "banner": "AUTO\nTRIGGER",
    },
    {
        "kind": "density",
        "section": "LAYOUT RHYTHM",
        "page": 6,
        "number": 5,
        "title": "排版骨架不变",
        "lede": "我们换的是时代气质，不是阅读效率。信息密度、留白与页数约束仍然可控。",
        "metrics": [
            {"value": "1", "label": "one-pager", "note": "严格单页"},
            {"value": "1", "label": "letter", "note": "严格单页"},
            {"value": "3", "label": "demo long-doc", "note": "章节展开"},
            {"value": "500+", "label": "check rules", "note": "字体 / CSS / 占位符"},
        ],
        "bullets": [
            "旧纸底不是装饰图，而是稳定色块。",
            "题签和细线负责时代感，正文仍按专业文档阅读。",
            "配置 serif 字体用于报纸气质，功能文字保持清晰。",
        ],
    },
    {
        "kind": "delivery",
        "section": "DELIVERY",
        "page": 7,
        "number": 6,
        "title": "交付链路",
        "lede": "生成不止是写文件，还要让 PDF/PPTX 和预览资产都能被检查。",
        "steps": [
            {"label": "01", "title": "HTML / PPTX", "body": "内容进入固定模板"},
            {"label": "02", "title": "Build", "body": "生成交付文件"},
            {"label": "03", "title": "Verify", "body": "检查页数、字体、占位符"},
            {"label": "04", "title": "Preview", "body": "导出 demo 预览"},
        ],
        "commands": [
            ".venv/bin/python scripts/build.py --verify one-pager",
            ".venv/bin/python scripts/build.py --check",
            ".venv/bin/python scripts/build.py slides",
        ],
    },
    {
        "kind": "end",
        "section": "END",
        "page": 8,
        "title": "好看的本质是稳定",
        "body": "固定版式 · design token · 字体层级 · 构建校验",
        "meta": "Kami · Republican Newspaper Edition",
    },
]


DISPLAY_TOTAL = len(DECK)
DECK_BY_KIND: dict[str, dict[str, Any]] = {slide["kind"]: slide for slide in DECK}
