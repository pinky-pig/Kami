#!/usr/bin/env python3
"""Guizang Magazine Chinese slide deck."""

from __future__ import annotations

from pptx.util import Inches

from slides_common import (
    CONTENT_LEFT,
    CONTENT_RIGHT,
        SLIDE_W,
    add_body,
    add_kicker,
    add_line,
    add_text,
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
    add_title(slide, theme, "把 AI 文档\n排成真正的新主题", CONTENT_LEFT, Inches(1.32), Inches(6.9), size=38)
    add_body(
        slide,
        theme,
        "Guizang 的重点不是一层纸感，也不是一套颜色，而是 chrome、hero、组件、留白和节奏共同组成的出版语言。",
        CONTENT_LEFT,
        Inches(2.72),
        Inches(6.3),
        Inches(0.82),
        size=12.2,
        color=theme.muted,
    )
    meta_stack(slide, theme, Inches(9.2), Inches(1.2), Inches(2.9), "Formats", "HTML / PDF / PPTX", "一个主题，多个出口")
    meta_stack(slide, theme, Inches(9.2), Inches(2.36), Inches(2.9), "Typography", "Serif / Sans / Mono", "标题、正文、元信息分层")
    meta_stack(slide, theme, Inches(9.2), Inches(3.52), Inches(2.9), "Rhythm", "Dark Editorial", "全套输出保持单一黑色模式")
    quote_panel(slide, theme, CONTENT_LEFT, Inches(5.3), Inches(6.8), "主题是系统，不是调色板。", "GUIZANG PRINCIPLE")


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
    add_title(slide, theme, "这次重做的，是版式语法", CONTENT_LEFT, Inches(1.28), Inches(7.0), size=30)
    add_body(
        slide,
        theme,
        "旧版本的问题在于保留了 manuscript 的 framed page、plaque block 和 archive card 母结构。现在换成了更接近 Guizang 原版 deck 的 headline、stat spread、rowline 和 chapter rhythm。",
        CONTENT_LEFT,
        Inches(1.98),
        Inches(7.2),
        Inches(0.7),
        size=11.0,
        color=theme.fg,
    )
    stat_card(slide, theme, Inches(0.9), Inches(3.02), Inches(2.45), "HERO", "01", "封面和幕封负责拉开节奏")
    stat_card(slide, theme, Inches(3.72), Inches(3.02), Inches(2.45), "COMPONENTS", "06", "stat / rowline / pillar / quote")
    stat_card(slide, theme, Inches(6.54), Inches(3.02), Inches(2.45), "SURFACES", "03", "dark theme / editorial card")
    stat_card(slide, theme, Inches(9.36), Inches(3.02), Inches(2.45), "DELIVERABLES", "05", "核心模板同步改造")
    rowline(slide, theme, CONTENT_LEFT, Inches(5.08), Inches(11.2), "Chrome", "页眉页脚回到杂志导航语义，而不是文档边框装饰。", "META")
    rowline(slide, theme, CONTENT_LEFT, Inches(5.58), Inches(11.2), "Hierarchy", "标题由衬线负责冲击，正文交给 sans，元信息交给 mono。", "TYPE")
    rowline(slide, theme, CONTENT_LEFT, Inches(6.08), Inches(11.2), "Rhythm", "HTML / PDF / PPT 都有 hero 页与正文页的明显节奏切换。", "FLOW")


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
    add_title(slide, theme, "封面、转场、正文，不再长得一样", CONTENT_LEFT, Inches(1.28), Inches(6.4), size=31)
    add_body(
        slide,
        theme,
        "Guizang 的阅读体验来自版式密度变化：hero 页负责仪式感，正文页负责信息密度，章节页负责呼吸和转场。",
        CONTENT_LEFT,
        Inches(2.18),
        Inches(6.2),
        Inches(0.6),
        size=11.2,
        color=theme.muted,
    )
    image_panel(slide, theme, Inches(7.95), Inches(1.3), Inches(4.1), Inches(2.8), "ACT DIVIDER", "HERO PAGE")
    quote_panel(slide, theme, CONTENT_LEFT, Inches(4.42), Inches(5.6), "如果每一页都像正文，读者就不会记得章节转换。", "PACING RULE")
    pillar_card(slide, theme, Inches(7.95), Inches(4.66), Inches(1.2), "01", "Hero", "大标题、少量文字、承担记忆点。")
    pillar_card(slide, theme, Inches(9.42), Inches(4.66), Inches(1.2), "02", "Body", "rowline、stat、正文段落承担信息。")
    pillar_card(slide, theme, Inches(10.89), Inches(4.66), Inches(1.2), "03", "Act", "章节页负责切换呼吸和视角。")


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
    add_title(slide, theme, "脚手架只管生成，主题自己决定长相", CONTENT_LEFT, Inches(1.28), Inches(7.4), size=30)
    add_body(
        slide,
        theme,
        "republican-manuscript 只能保留目录和构建方法；真正决定产物气质的是 Guizang 自己的 layout grammar。",
        CONTENT_LEFT,
        Inches(1.96),
        Inches(7.0),
        Inches(0.58),
        size=10.8,
    )
    pipeline_step(slide, theme, Inches(0.95), Inches(3.35), Inches(2.5), "01", "Route", "判断文档类型与语言。")
    pipeline_step(slide, theme, Inches(3.95), Inches(3.35), Inches(2.5), "02", "Compose", "把内容压进 Guizang 组件。")
    pipeline_step(slide, theme, Inches(6.95), Inches(3.35), Inches(2.5), "03", "Build", "导出 HTML / PDF / PPTX。")
    pipeline_step(slide, theme, Inches(9.95), Inches(3.35), Inches(2.2), "04", "Verify", "页数、字体、占位符一起检查。")
    add_line(slide, Inches(1.48), Inches(3.43), Inches(8.9), theme.line, 0.7)
    rowline(slide, theme, CONTENT_LEFT, Inches(5.42), Inches(11.2), "AGENTS.md", "严格禁止把 manuscript 当成视觉参考继续套壳。", "RULE")
    rowline(slide, theme, CONTENT_LEFT, Inches(5.92), Inches(11.2), "templates", "HTML、PDF、PPT 都重新改为 Guizang-native 结构。", "OUTPUT")
    rowline(slide, theme, CONTENT_LEFT, Inches(6.42), Inches(11.2), "demos", "演示文件也同步用新节奏重生成，不再沿用旧样张。", "DEMO")


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
    add_title(slide, theme, "同一种语言\n不同出口", Inches(1.0), Inches(1.72), Inches(7.0), size=40)
    add_body(
        slide,
        theme,
        "HTML、PDF、PPTX 不需要长得完全一样，但它们必须能被认出属于同一个主题系统。",
        Inches(1.0),
        Inches(3.42),
        Inches(6.4),
        Inches(0.76),
        size=11.2,
        color=theme.muted,
    )
    pillar_card(slide, theme, Inches(8.35), Inches(2.0), Inches(1.15), "HTML", "文档页", "章节、正文、引用与导航。")
    pillar_card(slide, theme, Inches(9.75), Inches(2.0), Inches(1.15), "PDF", "纸面版", "页数控制、阅读密度与导出。")
    pillar_card(slide, theme, Inches(11.15), Inches(2.0), Inches(1.15), "PPTX", "演示版", "hero、转场与讲述节奏。")
    quote_panel(slide, theme, Inches(1.0), Inches(5.1), Inches(11.0), "主题的一致性，来自层级和节奏，而不是每处都复制同一个卡片。", "SYSTEM CONSISTENCY")


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
    add_title(slide, theme, "现在这套 deck 用什么说话", CONTENT_LEFT, Inches(1.28), Inches(6.4), size=31)
    pillar_card(slide, theme, Inches(0.92), Inches(2.6), Inches(3.45), "01", "Chrome / Foot", "用页眉页脚做导航语义，建立杂志感，而不是外框。")
    pillar_card(slide, theme, Inches(4.88), Inches(2.6), Inches(3.45), "02", "Serif / Sans / Mono", "标题冲击、正文承载、元信息节奏，各有明确角色。")
    pillar_card(slide, theme, Inches(8.84), Inches(2.6), Inches(3.45), "03", "Stat / Rowline / Pillar", "数字页、表格式正文和并列观点页，构成可复用组件库。")
    quote_panel(slide, theme, CONTENT_LEFT, Inches(5.28), Inches(11.0), "组件不是装饰集合，而是内容被组织的方式。", "LAYOUT SYSTEM")


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
    add_title(slide, theme, "这套新主题已经覆盖的交付件", CONTENT_LEFT, Inches(1.28), Inches(7.0), size=30)
    add_body(
        slide,
        theme,
        "不只是 core trio。简历、作品集和中英 deck 也同步切到 Guizang 的 editorial 语法，避免同一 skill 内部风格断层。",
        CONTENT_LEFT,
        Inches(1.96),
        Inches(7.6),
        Inches(0.64),
        size=10.8,
    )
    rowline(slide, theme, CONTENT_LEFT, Inches(3.02), Inches(11.2), "One-Pager", "hero headline + stat spread + editorial blocks + callout", "HTML")
    rowline(slide, theme, CONTENT_LEFT, Inches(3.5), Inches(11.2), "Long Doc", "cover / overview / problem / method / conclusion / appendix", "PDF")
    rowline(slide, theme, CONTENT_LEFT, Inches(3.98), Inches(11.2), "Letter", "subject block + correspondence body + evidence sidebar", "DOC")
    rowline(slide, theme, CONTENT_LEFT, Inches(4.46), Inches(11.2), "Resume", "identity hero + metrics + timeline + open source spread", "CV")
    rowline(slide, theme, CONTENT_LEFT, Inches(4.94), Inches(11.2), "Portfolio", "editorial cover + case spreads + selected works + contact", "BOOK")
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
    add_title(slide, theme, "主题是系统，\n不是换色版。", Inches(1.0), Inches(1.8), Inches(7.2), size=40)
    add_body(
        slide,
        theme,
        "真正的新主题，必须在 HTML、PDF、PPTX 和 demo 里都能一眼认出来，而不是只有 palette 不一样。",
        Inches(1.0),
        Inches(3.56),
        Inches(6.6),
        Inches(0.8),
        size=11.8,
        color=theme.muted,
    )
    quote_panel(slide, theme, Inches(1.0), Inches(5.2), Inches(10.8), "如果结果还像旧主题，那就说明它还没有被重做。", "AGENTS RULE")


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
