#!/usr/bin/env python3
"""Shared slide schema for republican-newspaper PPTX and Slidev renderers."""

from __future__ import annotations

from typing import Any


DECK: list[dict[str, Any]] = [
    {
        "kind": "front-page",
        "section": "FRONT PAGE",
        "page": 1,
        "masthead": "项目号外",
        "masthead_sub": "旧报纸底 / 黑色铅字 / 竖排题名 / 剪报拼版",
        "issue_mark_title": "号外",
        "issue_mark_note": "KAMI 2026",
        "dateline_left": "上海 · 2026.04.28 · 编辑部特刊",
        "dateline_right": "内部演示材料 · 第 01 期",
        "rail_kicker": "头版",
        "rail_title": "报纸号外",
        "rail_date": "二〇二六\n四月",
        "lead_label": "头条 / 编辑按",
        "headline": "不是换色，而是换成报纸自己的版面逻辑。",
        "lead": "这次修订的目标，不是把 republican-manuscript 的 PPT 换成旧纸色，而是把 slides 的布局系统彻底切到 republican-newspaper 自己的报纸语法。",
        "lead_columns": [
            "PPTX 现在直接使用报头、日期线、竖排题名、跨栏 lead、剪报侧栏、灰度图片区和红印规则。",
            "Slidev 也不再沿用 manuscript 的牌匾封面、双线内框和居中卡片，而是用同一份报纸 schema 渲染成头版、特刊页、通信页和编辑台页。",
        ],
        "photo_caption": "灰度图片区可用于人物照、地图、票据、剪报证据；它是新闻证据位，不是现代 hero 图。",
        "side_cards": [
            {
                "tag": "版面变化",
                "title": "报头先行",
                "body": "先立版名、issue mark 和 dateline，再展开正文。",
            },
            {
                "tag": "组件变化",
                "title": "Lead + Sidebars",
                "body": "主文跨栏，数字、步骤和判断进入 clipping。",
            },
            {
                "tag": "红印规则",
                "seal": "红印",
                "body": "整页只保留一处主红印，强调仍以黑底反白条为主。",
            },
        ],
    },
    {
        "kind": "component-sheet",
        "section": "CLIPPING BOARD",
        "page": 2,
        "title": "组件来自报纸模板，不来自 manuscript",
        "lede": "one-pager、long-doc、letter 的组件各有位置：masthead、reverse label、vertical rail、clipping、timeline、action list。",
        "cards": [
            {
                "tag": "COMP 01",
                "title": "Masthead",
                "body": "报头先定义期刊身份，再定义正文层级。",
            },
            {
                "tag": "COMP 02",
                "title": "Vertical Rail",
                "body": "竖排题名和日期栏只做边栏，不把整段正文竖排。",
            },
            {
                "tag": "COMP 03",
                "title": "Clipping",
                "body": "事实、数据、步骤和引用都进入剪报框。",
            },
            {
                "tag": "COMP 04",
                "title": "Action List",
                "body": "页尾用时间线、行动框和 footer 收束阅读。",
            },
        ],
        "stats": [
            {"value": "2-3", "label": "正文栏数", "note": "one-pager / special issue"},
            {"value": "1", "label": "主红印", "note": "每页最多一处"},
            {"value": "0", "label": "圆角依赖", "note": "默认保持直角裁切"},
        ],
        "timeline": [
            {"label": "报头", "body": "版名、期号、日期线先出现"},
            {"label": "头条", "body": "lead story 跨栏承担主判断"},
            {"label": "剪报", "body": "事实与行动进入 clipping"},
        ],
        "action_title": "编辑动作",
        "action_body": "如果信息太多，先加栏、加边栏、加 rule；不要回退到 manuscript 的中轴牌匾和均分卡片。",
    },
    {
        "kind": "special-issue",
        "section": "SPECIAL ISSUE",
        "page": 3,
        "tag": "WHITE PAPER · INTERNAL EDITION",
        "meta": "专题白皮书 / 深度报道",
        "title": "长文像连续报道，\n不是 deck 拉长",
        "subtitle": "封面建立专题身份，目录用 toc items 收束，章页再切成 header band + 双栏文章。",
        "filed_under": "Research Desk\nProduct Desk",
        "version": "V1.1\n2026.04",
        "cover_note": "长文的节奏来自报头题签、目录条目、引文框和 panel，不再借用 manuscript 的档案牌匾封面。",
        "cover_meta": "作者：Kami 编辑部\n发布：Republican Themes\n结构：封面 / 目录 / 章节 / 附录",
        "toc": [
            {"num": "01", "title": "执行摘要", "page": "03"},
            {"num": "02", "title": "背景与问题定义", "page": "04"},
            {"num": "03", "title": "方法与发现", "page": "06"},
            {"num": "04", "title": "结论与建议", "page": "09"},
        ],
    },
    {
        "kind": "article-spread",
        "section": "CHAPTER PAGE",
        "page": 4,
        "chapter": "CHAPTER 02",
        "title": "章页用双栏、边栏和引文推进阅读",
        "lede": "章节页保留报刊 header band，再把正文放回双栏与 side panel。报纸感来自阅读组织，而不是做旧边框。",
        "columns": [
            "第一栏负责把背景、判断和上下文讲完整。行距可以比 manuscript 更密，但仍保持 1.42 以上，确保连续阅读不挤死。",
            "第二栏继续展开方法、证据和影响，把主题推进成连续报道，而不是每页只摆一句口号。必要时可插入小表格、引用框或 code clipping。",
        ],
        "panel_title": "边栏证据",
        "panel_body": "把数字、结论和行动拉进 panel，让正文主线保持流动。",
        "bullets": [
            "章号 + 标题先出现在 header band",
            "正文双栏推进，栏间用细 rule 分开",
            "panel / quote / table 都是报纸式证据位",
        ],
        "quote": "报纸感来自信息组织，不来自把页面做旧。",
        "cite": "Production Rule · Republican Newspaper",
    },
    {
        "kind": "correspondence",
        "section": "FILED LETTER",
        "page": 5,
        "plaque_label": "Filed Letter",
        "plaque_value": "通信剪报 / 正式函件",
        "sender_org": "Paperlane Editorial Desk",
        "sender_meta": "主编室 / 上海\n+86 138 5555 0123\neditor@paperlane.ai\n日期：2026 年 4 月 28 日",
        "subject_title": "关于将 republican-newspaper 独立成报纸版面体系的说明",
        "recipient": "主题维护与设计团队",
        "category": "设计修订说明",
        "salutation": "各位同事：",
        "paragraphs": [
            "这次修订的重点，是把 republican-newspaper 的 slides 从 manuscript 逻辑中剥离出来，让它和现有 letter / one-pager / long-doc 保持同一个报纸系统。",
            "这意味着版面不再依赖深色外框、居中大牌匾和均分卡片，而是切回通信剪报、subject head、正文函件框、证据列表和 footer 的结构。",
            "用户以后无论要做正式函件、专题长文还是 deck，看到的都应该是同一套报纸语法，而不是 manuscript 的骨架被旧纸色覆盖。",
        ],
        "evidence": [
            "报头与日期线重新定义 slide 封面",
            "long-doc 结构进入专题页与章页",
            "letter 结构进入 correspondence slide",
        ],
        "regards": "此致　敬礼",
        "closing_note": "如需继续统一英文版或 resume / portfolio，可在此基础上继续迁移。",
        "signature": "Kami 编辑部",
        "signature_meta": "Republican Themes\n2026 年 4 月 28 日",
        "attachments": "附件：① 报纸版面 schema ② Slidev renderer ③ PPTX renderer",
    },
    {
        "kind": "routing-desk",
        "section": "ROUTING DESK",
        "page": 6,
        "desk_name": "编辑台路由",
        "desk_sub": "用户只说任务，skill 负责判断该走哪种报纸版面。",
        "wires": [
            {"prompt": "帮我生成一份报纸特刊", "route": "one-pager", "note": "头版 / 号外"},
            {"prompt": "把这份白皮书排成旧报纸", "route": "long-doc", "note": "多页专题"},
            {"prompt": "写一封家书特刊", "route": "letter", "note": "通信剪报"},
            {"prompt": "做一套民国报纸风 slides", "route": "slides", "note": "编辑部 deck"},
            {"prompt": "把这些内容排成好看的 PDF", "route": "infer", "note": "先判类型再分版"},
        ],
        "routing_rules": [
            "先判内容类型，再判版式密度",
            "红印只作为破色，不作为普通标签",
            "竖排题名只用于边栏和标题带，不用于长正文",
        ],
        "stamp_title": "编辑印",
        "stamp_note": "自然语言触发\n不依赖 slash command",
    },
    {
        "kind": "production-desk",
        "section": "PRODUCTION DESK",
        "page": 7,
        "title": "构建链路也要像报社排版一样稳定",
        "lede": "生产方法可以复用，但版式不能借用 manuscript。输出现在同时覆盖 PPTX 和 Slidev。",
        "steps": [
            {"tag": "01", "title": "Schema", "body": "报纸内容先写进 slides_spec.py。"},
            {"tag": "02", "title": "PPTX", "body": "slides.py 用 newspaper 组件渲染屏幕版。"},
            {"tag": "03", "title": "Slidev", "body": "render_from_spec.py 用同一 schema 渲染 HTML 版。"},
            {"tag": "04", "title": "Verify", "body": "build.py 统一产出 demo-slides.pptx 与 slides-online。"},
        ],
        "commands": [
            "python3 scripts/build.py slides",
            "python3 scripts/build.py --verify slides",
            "python3 assets/demos/slides-online/slides-online-preview.py",
        ],
        "checks": [
            "不残留 archive blue",
            "不回退 manuscript plaque",
            "在线预览与 PPT 内容同构",
        ],
    },
    {
        "kind": "final-edition",
        "section": "FINAL EDITION",
        "page": 8,
        "masthead": "终刊",
        "masthead_sub": "旧报纸底 / 黑色铅字 / 竖排题名 / 剪报拼版",
        "final_title": "报纸主题要有\n自己的版面语法",
        "final_lede": "republican-themes 可以复用 manuscript 的生成骨架，但 PPTX 和 Slidev 的布局、组件、节奏与视觉层级必须完全属于自己的主题系统。",
        "edition_panel": "NO MANUSCRIPT PLAQUE\nNO ARCHIVE FRAME\nUSE MASTHEAD / DATELINE /\nCLIPPING / BODY FRAME",
        "closing_line": "像一份可信的旧报刊材料，而不是换色后的馆藏文稿。",
    },
]


DISPLAY_TOTAL = len(DECK)
