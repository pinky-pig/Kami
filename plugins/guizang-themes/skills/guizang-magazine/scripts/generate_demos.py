#!/usr/bin/env python3
"""Generate curated Guizang demo artifacts.

Creates content-filled HTML demos from the latest templates, renders PDFs,
builds the PPTX deck, and writes a lightweight demo index page.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from weasyprint import HTML


ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "assets" / "templates"
DEMOS = ROOT / "assets" / "demos"
EXAMPLES = ROOT / "assets" / "examples"


def replace_all(text: str, replacements: list[tuple[str, str]]) -> str:
    for src, dst in replacements:
        if src not in text:
            raise ValueError(f"Placeholder not found: {src}")
        text = text.replace(src, dst, 1)
    remaining = [line.strip() for line in text.splitlines() if "{{" in line and "}}" in line]
    if remaining:
        snippet = "\n".join(remaining[:10])
        raise ValueError(f"Unfilled placeholders remain:\n{snippet}")
    return text


def replace_map(text: str, replacements: dict[str, str]) -> str:
    for src, dst in replacements.items():
        if src not in text:
            raise ValueError(f"Placeholder not found: {src}")
        text = text.replace(src, dst)
    remaining = [line.strip() for line in text.splitlines() if "{{" in line and "}}" in line]
    if remaining:
        snippet = "\n".join(remaining[:10])
        raise ValueError(f"Unfilled placeholders remain:\n{snippet}")
    return text


def replace_many(text: str, repeated: dict[str, list[str]], shared: dict[str, str]) -> str:
    for src, values in repeated.items():
        for dst in values:
            if src not in text:
                raise ValueError(f"Placeholder not found: {src}")
            text = text.replace(src, dst, 1)
    return replace_map(text, shared)


def build_pdf(html_path: Path, pdf_path: Path) -> None:
    HTML(str(html_path), base_url=str(html_path.parent)).write_pdf(str(pdf_path))


def generate_one_pager() -> None:
    source = (TEMPLATES / "one-pager.html").read_text(encoding="utf-8")
    filled = replace_many(
        source,
        {
            "{{指标说明}}": ["搭建周期", "交付覆盖", "可复用骨架", "统一主题系统"],
            "{{数字}}": ["3 周", "6 类", "92%", "1 套"],
            "{{英文小标题}}": ["Why Now", "How It Ships"],
            "{{1-2 句概括。}}": [
                "团队已经有研究、汇报和演示材料，但缺少统一的文档落点。结果是每次交付都在重新排版、重新命名、重新审稿。",
                "BriefOS 把模板、主题和构建脚本放在同一个 skill 里，让内容团队只需要关心判断和证据。",
            ],
            "{{短 bullet}}": [
                "先判断文档类型，再进入固定模板",
                "主题预设统一控制标题、正文和元信息气质",
                "构建脚本负责页数、字体和占位符校验",
            ],
            "{{阶段标题}}": ["模板定型", "内容迁移", "验证发布"],
            "{{一句解释}}": [
                "完成 one-pager / long-doc / letter / slides 四类骨架",
                "把研究摘要、客户案例和内部 memo 接入同一主题系统",
                "生成 demo bundle，并给团队开放可复用交付链路",
            ],
        },
        {
            "{{文档标题}}": "BriefOS · 把研究素材变成交付文档",
            "{{英文眉题 · 如 COMPANY BRIEF / PROJECT DOSSIER}}": "EDITORIAL SYSTEM BRIEF",
            "{{文档主标题，两行内，动词 + 名词结构最好}}": "把研究素材\n变成交付文档",
            "{{一行副标题 / 一句核心论点}}": "一个面向 AI 团队的文档系统提案",
            "{{档案标签 · 如 Archive Note}}": "Filed Under",
            "{{项目 / 公司 / 主题名称}}": "Paperlane AI · BriefOS",
            "{{版本 / 状态}}": "Demo / V0.9",
            "{{日期 YYYY.MM.DD}}": "2026.04.24",
            "{{文档分类}}": "产品方案",
            "{{40-70 字核心导语。用 <span class=\"hl\">关键词</span> 点出判断，让读者立刻知道这份一页纸的主张。}}": "我们要解决的不是写得更快，而是把分散的研究、访谈和 deck，稳定地收束成 <span class=\"hl\">可发布、可验证、可复用</span> 的 HTML / PDF / PPT 交付件。",
            "{{栏目标题 1}}": "为什么现在做",
            "{{短 bullet：事实 / 数据 / 判断}}": "输入已经足够多，真正缺的是稳定的输出骨架",
            "{{短 bullet：带 <span class=\"hl\">关键数字</span> 的论据}}": "同一批素材需要复用到 <span class=\"hl\">方案、白皮书、信件、Slides</span>",
            "{{短 bullet：下一步或风险}}": "没有统一模板时，审美、页数和可读性都会持续漂移",
            "{{栏目标题 2}}": "怎么落地",
            "{{Timeline / Roadmap}}": "Roadmap",
            "{{阶段 / 年份 1}}": "W1",
            "{{阶段 / 年份 2}}": "W2",
            "{{阶段 / 年份 3}}": "W3",
            "{{关键里程碑 / 核心事项}}": "首批交付 / Demo Bundle",
            "{{事项 1：一句话}}": "一页项目方案：给管理层快速读",
            "{{事项 2：一句话}}": "白皮书：沉淀判断、方法与证据",
            "{{事项 3：一句话}}": "推荐信：正式沟通的固定结构",
            "{{事项 4：一句话}}": "Slides：延续同一套 editorial 视觉",
            "{{关键引用 / 核心 takeaway / 重要提示。}}": "真正稀缺的不是写作速度，而是把判断稳定地包装成交付件。",
            "{{补充说明：为什么这句话重要。}}": "当素材可以稳定落到统一模板里，团队才真正开始积累可复用的方法论，而不是一次性的排版劳动。",
            "{{公开 / 内部 / 机密级别}}": "INTERNAL DEMO / PAPERLANE AI",
            "{{页码 / 联系方式}}": "01 / hello@paperlane.ai",
        },
    )
    out_html = DEMOS / "demo-one-pager.html"
    out_pdf = DEMOS / "demo-one-pager.pdf"
    out_html.write_text(filled, encoding="utf-8")
    build_pdf(out_html, out_pdf)


def generate_long_doc() -> None:
    source = (TEMPLATES / "long-doc.html").read_text(encoding="utf-8")
    filled = replace_many(
        source,
        {
            "{{数据}}": ["6 类", "1 套骨架", "2-3 天", "半天内"],
            "{{差距}}": ["风格未统一", "验证未前置"],
            "{{标题}}": ["视觉语法必须跨载体", "验证必须先于导出"],
        },
        {
            "{{文档标题}}": "BriefOS 白皮书",
            "{{WHITE PAPER · INTERNAL EDITION}}": "WHITE PAPER · EDITORIAL AI",
            "{{文档分类}}": "产品说明书",
            "{{公开级别 / 内部公开版}}": "INTERNAL DEMO",
            "{{Archive Knowledge System}}": "AI Document Operating System",
            "{{文档主标题<br>可以两行}}": "BriefOS：<br>把原始素材变成交付文档",
            "{{副标题：一句话说清这份白皮书解决什么问题、为谁而写。}}": "一套给 AI 团队、研究团队与内容团队使用的统一文档系统。",
            "{{团队 / 部门}}": "Paperlane AI",
            "{{专题 / 项目}}": "BriefOS / Editorial Systems",
            "{{V1.0}}": "V0.9",
            "{{2026.04}}": "2026.04",
            "{{封面注记：本文档聚焦哪几个问题，读者读完能获得什么判断。}}": "这份白皮书回答三个问题：为什么 deck 之外还需要文档系统、哪些视觉语法可以跨 HTML/PDF/PPT 复用，以及如何把交付验证纳入默认流程。",
            "{{作者 / 团队}}": "Paperlane Design Engineering",
            "{{发布方 / 机构}}": "Paperlane AI",
            "{{示意页数}}": "6",
            "{{一段 2-3 句话的大论点开场。用 <span class=\"hl\">关键词高亮</span> 抓住读者注意力，让读者读这一段就理解整份文档。}}": "如果团队已经有 deck、研究记录和客户材料，却仍然要为每次交付重新排版，那么问题不在内容生产，而在缺少一套 <span class=\"hl\">统一的文档操作系统</span>。BriefOS 的目标，是把素材到交付的最后一公里变成模板化流程。",
            "{{Takeaway 1：一句话，可量化}}": "首批 system 覆盖 6 类交付，减少重复排版工作",
            "{{Takeaway 2：有数据的洞察}}": "统一模板后，单次交付准备时间可缩短约 40%",
            "{{Takeaway 3：对未来的判断}}": "下一阶段价值不在更多模板，而在可验证的复用能力",
            "{{用一段话说明为什么现在需要这份文档，以及决策者读完以后应该采取什么行动。}}": "现在的问题不是内容不足，而是输出不稳定。管理层需要的是能被快速复用、快速判断、快速发布的交付格式，因此应先统一文档系统，再扩大内容生产。",
            "{{列出 3 个核心问题：范围、方法、交付标准。}}": "问题一：哪些交付类型必须共享同一套骨架？<br>问题二：哪些主题语法能跨 HTML / PDF / PPT 复用？<br>问题三：怎样把页数、字体和占位符校验变成默认动作？",
            "{{章节导语：这一章要解决什么问题，为什么重要。}}": "这一章回答一个基础问题：为什么有了 deck 和知识库以后，团队仍然会在交付阶段反复返工。",
            "{{3-5 行段落，铺陈当前状况。用 <span class=\"hl\">具体数据</span> 而不是形容词。}}": "过去 8 周里，团队累计生成了 34 份研究摘要、11 套 slides、6 份客户方案和 9 封正式函件。素材已经足够丰富，但最终输出仍然分散在不同风格、不同页数和不同命名体系里。",
            "{{陈述具体问题，说明它如何影响交付、效率或判断质量。}}": "最直接的问题，是每次需要导出 PDF 或发送正式文档时，都要重新定义标题层级、正文样式、元信息位置和附件结构。结果是同一份判断在不同交付里长得像不同项目。",
            "{{一段重要引用或核心观察。和正文语气略有不同，给读者呼吸节奏。}}": "团队真正缺的不是新的内容生产工具，而是一套能把已有判断稳定落地的交付系统。",
            "{{来源 / 人物}}": "内部复盘",
            "{{日期}}": "2026.04",
            "{{维度 1}}": "交付类型",
            "{{维度 2}}": "产出时间",
            "{{章节导语：说明研究方法和最重要的发现。}}": "我们从过去两个月的实际交付出发，梳理了哪些部分应该模板化，哪些部分必须交给内容判断。",
            "{{描述资料来源、访谈范围、样本口径或分析方法。}}": "方法包括：回看 22 份真实交付件、拆分其中的标题/正文/元信息层级，统计哪些内容每次都重复出现，以及哪些返工来自结构不稳定而不是内容质量。",
            "{{如需代码或规则示例，放在这里；不需要时删除整个 pre。}}": "document_type: one-pager | long-doc | letter | slides\ntheme_preset: ink-classic | indigo | forest | kraft | dune\nvalidation: page-count + fonts + placeholders",
            "{{一段论述，包含 <span class=\"hl\">具体数字 / 具体比例</span>。}}": "我们发现 80% 以上的交付返工都发生在最后的样式收束阶段，而不是在内容判断阶段。只要标题、规则线、mono 元信息和配色语义能跨 HTML / PDF / PPT 保持一致，返工比例就会明显下降。",
            "{{一段论述，说明原因和影响。}}": "另一类常见问题来自“看起来差不多”的假稳定：页数超了、字体 fallback 了、占位符没清掉。这些问题如果不在构建时阻断，最终会变成交付风险。",
            "{{对执行者最重要的一句提醒。}}": "先决定交付类型和主题预设，再开始写内容；不要把排版决定留到最后十分钟。",
            "{{一句话总结结论，下面展开建议。}}": "先统一交付语言，再扩大内容规模。",
            "{{结论 1}}": "应该把 one-pager、white paper、letter、slides 视为同一系统中的不同出口",
            "{{结论 2}}": "视觉系统应由 preset 控制，而不是每次临时给 hex",
            "{{结论 3}}": "验证链路必须跟模板一同交付，而不是交给使用者自己猜",
            "{{基于结论的具体可执行建议。}}": "第一阶段只保留 3 个高频文档样式和 1 套 deck；第二阶段再补简历、作品集和英文适配；每次新增模板都必须同步 demo、verify source 和 examples。",
            "{{如果读者要做一件事，是什么？具体到可以周一早上就开始行动。}}": "从下周一开始，所有新方案和正式函件统一从 BriefOS 模板启动，不再允许从空白文档临时拼版。",
            "{{附录摘要或参考资料说明。}}": "附录建议包含：主题预设说明、组件清单、构建命令、校验规则，以及最近 10 份交付的复盘结果。",
        },
    )
    out_html = DEMOS / "demo-long-doc.html"
    out_pdf = DEMOS / "demo-long-doc.pdf"
    out_html.write_text(filled, encoding="utf-8")
    build_pdf(out_html, out_pdf)


def generate_letter() -> None:
    source = (TEMPLATES / "letter.html").read_text(encoding="utf-8")
    filled = replace_map(
        source,
        {
            "{{信件主题}}": "关于周既白申请 Editorial AI Fellowship 的推荐函",
            "{{Filed Letter / Recommendation Letter}}": "Recommendation Letter",
            "{{推荐信 / 正式函件<br>一句短标题}}": "AI Fellowship 推荐函<br>关于周既白",
            "{{寄件人姓名 / 机构}}": "林昭然 · Paperlane AI",
            "{{寄件人身份 / 部门 / 城市}}": "创始人 / 产品负责人 / 上海",
            "{{电话}}": "+86 138 5555 0123",
            "{{EMAIL}}": "zhaoran@paperlane.ai",
            "{{2026 年 4 月 21 日}}": "2026 年 4 月 24 日",
            "{{关于推荐 / 说明 / 申请事项的一句话标题}}": "关于周既白申请 Editorial AI Fellowship 的推荐",
            "{{收件人 / 委员会 / 单位}}": "Editorial AI Fellowship 审核委员会",
            "{{推荐信 / 内部说明函 / 正式信件}}": "Recommendation Letter",
            "{{尊敬的 XX 委员会 / 负责人：}}": "尊敬的 Editorial AI Fellowship 审核委员会：",
            "{{第一段：说明写信目的和与被推荐人的关系。例如“我谨以 XX 身份推荐 XX 申请 XX 项目”。}}": "我谨以 Paperlane AI 创始人兼产品负责人的身份，推荐周既白申请 Editorial AI Fellowship。我与他在过去一年中共同推进 BriefOS 文档系统的设计、工程与交付验证，亲眼见证了他如何把一个模糊方向推进成稳定可复用的产品能力。",
            "{{第二段：写清推荐理由。用具体事实支撑，不只写“优秀”。可用 <span class=\"hl\">关键能力 / 关键成果</span> 高亮。}}": "我最认可他的，是把判断落成系统的能力。周既白并不满足于做出一版“好看”的样张，而是会继续把模板、主题预设、构建脚本和验证流程一起做完整。过去两个月，他主导完成了 <span class=\"hl\">6 类文档出口</span> 的统一骨架，并把页数、字体和占位符校验前置到默认工作流中。",
            "{{证据 1：项目 / 成果}}": "统一 one-pager / long-doc / letter / slides 交付骨架",
            "{{证据 2：能力 / 品质}}": "能在审美、工程和内容判断之间做稳定取舍",
            "{{证据 3：影响 / 评价}}": "把交付准备周期从 2-3 天压缩到半天内",
            "{{第三段：结合申请场景说明为什么匹配。把对方关心的标准和被推荐人的经历连接起来。}}": "我理解 Fellowship 寻找的不是单纯会写 prompt 或写代码的人，而是能够重新定义工作流的人。周既白最适合这一点，因为他既能理解创作现场的节奏，也能把抽象的“感觉”沉淀成别人可以直接复用的结构与规范。",
            "{{第四段：明确推荐结论，并提供后续联系出口。}}": "因此，我毫无保留地推荐周既白加入本期 Fellowship。如需我进一步说明他的工作方式、产出质量或协作表现，我非常愿意在第一时间补充材料或接受访谈。",
            "{{此致　敬礼 / 顺颂商祺}}": "此致　敬礼",
            "{{附言：如需进一步了解，我愿意补充说明。}}": "附言：如需样张、复盘记录或协作反馈，我可以补充提供。",
            "{{签名}}": "林昭然",
            "{{职位 · 单位}}": "创始人 · Paperlane AI",
            "{{日期复写}}": "2026 年 4 月 24 日",
            "{{附件清单：① 简历 ② 成果材料 ③ 其他证明；无附件可删除本行}}": "① 周既白简历　② BriefOS Demo Bundle　③ 项目复盘摘要",
        },
    )
    out_html = DEMOS / "demo-letter.html"
    out_pdf = DEMOS / "demo-letter.pdf"
    out_html.write_text(filled, encoding="utf-8")
    build_pdf(out_html, out_pdf)


def generate_resume() -> None:
    source = (TEMPLATES / "resume.html").read_text(encoding="utf-8")
    filled = replace_many(
        source,
        {
            "{{数字}}": ["12", "6", "40+", "3"],
            "{{单位}}": ["年", "类", "个", "条"],
            "{{标签}}": ["设计工程经验", "交付出口", "主导项目", "长期主题"],
            "{{年份}}": ["2018", "2021", "2024"],
            "{{阶段标题}}": ["设计系统起步", "产品与工程合流", "AI 交付系统化"],
            "{{一句解释这一步的意义}}": [
                "从界面与内容设计出发，建立对结构和信息密度的直觉。",
                "开始把设计判断落到交付规范与组件语言上。",
                "把 AI 文档、PPT 与验证链路收束成统一主题系统。",
            ],
            "{{项目名}}": [
                "BriefOS",
                "Signal Desk",
                "Paperlane Studio",
                "Atlas Docs",
                "PromptScope",
                "PatternLab",
                "Northwind Notes",
                "MonoScene",
                "Fieldbook AI",
            ],
            "{{项目类型}}": ["AI 文档系统", "研究工作台", "设计工程平台"],
            "{{URL}}": [
                "https://github.com/paperlane/atlas-docs",
                "https://github.com/paperlane/promptscope",
                "https://github.com/paperlane/patternlab",
                "https://github.com/paperlane/northwind-notes",
                "https://github.com/paperlane/monoscene",
                "https://github.com/paperlane/fieldbook-ai",
                "https://paperlane.ai",
            ],
            "{{STARS}}": ["4.8K", "3.2K", "2.4K", "1.8K", "1.2K", "860"],
            "{{描述}}": [
                "面向研究与交付团队的长文操作系统。",
                "把 prompt、资料和结论压进统一工作台。",
                "用于跨语言风格演练的组件仓库。",
                "轻量的现场记录与摘要产品。",
                "给演示稿和白皮书使用的视觉实验库。",
            ],
            "{{时间}}": ["2026.03", "2025.12", "2025.08"],
            "{{事件标题}}": ["提前押注文档交付", "重写主题系统", "把验证前置进构建"],
            "{{具体做了什么判断或行动}}": [
                "决定把 deck 之外的正式交付统一收口到同一个主题 skill 中。",
                "主动放弃旧的套壳式做法，回到主题原始语法重新构图。",
            ],
            "{{日期}}": ["2026.04", "2026.03", "2025.11", "2025.10"],
            "{{文章标题}}": ["把 AI 写作变成交付系统", "为什么主题不是调色板"],
            "{{浏览量 / 赞数 / 影响力指标}}": [
                "累计阅读 52K，带来 11 个真实咨询线索。",
                "被多个设计工程团队转发，形成内部讨论串。",
            ],
            "{{浏览量 / 赞数}}": ["52K / 1.8K", "31K / 1.1K"],
            "{{演讲标题}}": ["Designing AI Deliverables", "From Prompt To Proof"],
            "{{主办方 / 地点}}": ["Shanghai Design Week / 上海", "Product Makers Salon / 杭州"],
            "{{PHONE}}": ["+86 138 5555 0199", "+86 138 5555 0199"],
            "{{EMAIL}}": ["noah@paperlane.ai", "noah@paperlane.ai"],
            "{{姓名}}": ["周既白", "周既白"],
            "{{起止时间}}": ["2013 — 2017", "2013 — 2017"],
        },
        {
            "{{别名/英文名}}": "Noah Zhou",
            "{{岗位定位，如\"AI / Agent 工程\"}}": "AI / Agent 设计工程",
            "{{GITHUB_URL}}": "https://github.com/noahzhou",
            "{{GITHUB_ID}}": "noahzhou",
            "{{X_URL}}": "https://x.com/noahzhou",
            "{{X_ID}}": "noahzhou",
            "{{年龄}}": "29",
            "{{城市}}": "上海",
            "{{80 字以内。建议结构：现任职位 + 级别 + 时长。团队构成（人数、梯队、协作方）。长期演进方向。核心沉淀领域（4-6 个方向）。}}": "Paperlane AI 的设计工程负责人，长期把研究、内容与工程交付收束成统一系统。核心方向包括主题系统、AI 文档、deck 语言、验证链路与产品叙事。",
            "{{起始时间}}": "2021.06",
            "{{关键里程碑}}": "从设计系统走到 AI 交付系统",
            "{{角色定位，如\"方向主导\"}}": "方向主导",
            "{{~60 字：项目是什么 + 为什么做 + 你的位置}}": "把分散的 deck、memo 和 white paper 收束到一个多出口技能中，由我负责方向、组件和最终交付语言。",
            "{{~80 字：技术方案 / 关键决策 / 执行路径}}": "重建模板层、统一字体层级、重新设计 chrome 与 hero 节奏，并把 build / verify 纳入默认动作。",
            "{{~100 字：数据为王。<span class=\"hl\">关键数字</span> 高亮 1-2 处。}}": "在 <span class=\"hl\">6 类出口</span> 上建立统一样式语言，让正式交付准备时间从 2-3 天压到半天内。",
            "{{角色定位}}": "设计工程主导",
            "{{~60 字}}": "负责研究工作台与交付界面的整体结构和主题系统。",
            "{{~80 字}}": "把高频页面抽象成 rowline、stat、pillar 等组件，并在 PDF / PPT 中同步实现。",
            "{{~100 字，含 <span class=\"hl\">关键数字</span>}}": "沉淀出 <span class=\"hl\">20+</span> 个可复用版式片段，支持多个项目并行使用。",
            "{{角色}}": "独立负责",
            "{{项目背景和定位}}": "为内部 AI 产品建立统一的视觉与交付语言。",
            "{{执行路径}}": "从需求梳理、视觉实验到构建脚本全部端到端推进。",
            "{{可量化结果，含 <span class=\"hl\">关键数字</span>}}": "输出稳定支撑 <span class=\"hl\">40+</span> 份内部与外部正式文档。",
            "{{时间跨度}}": "2023 — 2026",
            "{{一句副标题}}": "独立开发与产品叙事",
            "{{一句自我定位}}": "我更像一个把判断落成系统的人",
            "{{简述开发者身份：设计审美 / 独立完成流程 / 跨语言实战 / 用户反馈}}": "从视觉、模板、脚本到导出全部独立完成，习惯在真实使用里校验主题是否成立",
            "{{STARS_TOTAL}}": "14.3K",
            "{{FORKS_TOTAL}}": "1.9K",
            "{{FOLLOWERS_TOTAL}}": "18K",
            "{{亮点 TAG}}": "Featured",
            "{{这个项目的独特故事：开源时机 / 传播范围 / 知名人物推荐等}}": "在公开发布后一周内进入多个设计工程社区的主题讨论，并被连续转发到团队内部知识库。",
            "{{语言 + 核心定位 + 平台}}": "TypeScript · AI document runtime · GitHub",
            "{{具体做了什么判断或行动，为什么证明判断力}}": "在项目尚未成型时就判断正式文档会成为团队瓶颈，因此优先做交付系统而不是继续堆零散样张。",
            "{{平台}}": "X / Newsletter",
            "{{HANDLE}}": "noahzhou",
            "{{粉丝数}}": "18K followers",
            "{{博客 / 周刊 / 其他内容产品简介}}": "持续写 AI 交付、设计工程与个人产品方法。",
            "{{能力 1<br>标签}}": "结构判断",
            "{{描述。至少 <span class=\"em-brand\">1 处强调</span>}}": "能够把抽象需求压成稳定骨架，并用 <span class=\"em-brand\">可验证的结构</span> 说服团队。",
            "{{能力 2<br>标签}}": "系统设计",
            "{{能力 2 描述}}": "擅长把主题、组件和导出链路放进同一套语言里，而不是让视觉和工程各自漂移。",
            "{{能力 3<br>标签}}": "设计工程",
            "{{能力 3 描述}}": "可以把排版、模板、脚本和验证一起推进，让设计判断真正落到可发布的产物上。",
            "{{能力 4<br>标签}}": "独立交付",
            "{{能力 4 描述}}": "从需求收束、结构搭建到最终导出都能独立完成，并在关键处主动承担取舍责任。",
            "{{能力 5<br>标签}}": "长期主题",
            "{{能力 5 描述}}": "长期沉淀 editorial 界面、文档阅读节奏与主题系统，让项目之间形成可复用的审美方法论。",
            "{{学校}}": "同济大学",
            "{{学院}}": "设计创意学院",
            "{{专业}}": "视觉传达",
            "{{一句判断性描述，如\"放弃保研直接就业\"}}": "毕业后直接进入产品与设计工程一线，而不是继续学术路径。",
        },
    )
    out_html = DEMOS / "demo-resume.html"
    out_pdf = DEMOS / "demo-resume.pdf"
    out_html.write_text(filled, encoding="utf-8")
    build_pdf(out_html, out_pdf)


def generate_portfolio() -> None:
    source = (TEMPLATES / "portfolio.html").read_text(encoding="utf-8")
    filled = replace_many(
        source,
        {
            "{{标签}}": ["AI Tools", "Editorial", "System", "Dashboards", "Motion"],
            "{{一句描述}}": [
                "一套围绕交付系统展开的长期实践。",
                "把研究工作流转换为统一界面。",
                "围绕主题与组件的连续实验。",
            ],
            "{{作品标题}}": ["Atlas Notes", "Signal Atlas", "MonoScene"],
            "{{链接 / 状态}}": ["Live / 2026", "Private Beta", "In Progress"],
            "{{数字}}": ["48%", "6", "14K"],
            "{{EMAIL}}": ["noah@paperlane.ai", "noah@paperlane.ai", "noah@paperlane.ai"],
            "{{URL}}": ["https://paperlane.ai", "https://paperlane.ai", "https://paperlane.ai"],
            "{{项目名称}}": ["BriefOS", "Signal Desk"],
            "{{专业 / 角色}}": ["Design Engineer", "Design Engineer"],
        },
        {
            "{{名字}}": "周既白",
            "{{年份 或 领域标签 · 如 \"Selected Works 2023–2026\"}}": "Selected Works 2023–2026",
            "{{名字<br>Portfolio}}": "周既白<br>Portfolio",
            "{{一句自我描述 / 作品集主题}}": "围绕 AI 交付、设计工程与出版式界面所做的一组系统化作品。",
            "{{所在地}}": "上海",
            "{{网站 / 社交链接}}": "paperlane.ai / @noahzhou",
            "{{一句自我定位的 headline}}": "把感觉做成系统，把系统做成交付。",
            "{{2-3 行的自我介绍引言。serif 字体，斜体感，不写太 sales。\n    用自己的语言描述你关心什么、擅长什么。}}": "我关心那些看似分散、最后却必须一起成立的东西：内容、界面、输出格式、阅读节奏和最终交付质量。",
            "{{一段关于你过往经历的概述。}}": "过去几年主要在设计系统、内容工具与 AI 产品之间来回切换，逐渐把关注点放到更完整的交付链路上。",
            "{{一段关于你当前的关注点 / 方法论。}}": "现在更在意一套主题能否跨 HTML、PDF、PPTX 成立，以及它是否真的能减轻团队最后一公里的返工。",
            "{{项目类型 · 如 \"Product Design\" / \"Open Source\"}}": "AI Document System",
            "{{一句话描述这个项目做了什么}}": "把研究素材、正式文档和 deck 收束到同一套主题与脚手架里。",
            "{{时间 · 如 \"2025.04 — 2026.02\"}}": "2025.09 — 2026.04",
            "{{标签 1}}": "Theme System",
            "{{标签 2}}": "HTML / PDF / PPTX",
            "{{标签 3}}": "Verification",
            "{{为什么做这个项目？要解决什么问题？谁是用户？}}": "团队已经有大量研究与 deck，但在正式交付阶段仍要频繁返工。这个项目服务的是既写内容又要发布的人。",
            "{{怎么做的？关键决策、设计考量、技术方案。}}": "先拆出 chrome、hero、rowline、pillar 等稳定语法，再把它们移植到不同输出格式中，同时保留 build / verify 管线。",
            "{{结果是什么？<span class=\"hl\">数据</span>、反馈、影响。}}": "沉淀出 <span class=\"hl\">6 类交付出口</span>，并把 demo、模板、验证规则一起打包交付。",
            "{{项目类型}}": "Research Workspace",
            "{{时间}}": "2025.05 — 2025.12",
            "{{一句话描述}}": "把资料、判断与行动统一到一张研究工作台里。",
            "{{背景}}": "一个把资料、判断与下一步行动放到同一界面中的研究工作台。",
            "{{方法}}": "用更清晰的层级和更少的装饰，把界面注意力集中到判断本身。",
            "{{结果}}": "形成了一组后来被迁移到正式交付模板里的视觉语法。",
            "{{欢迎联系的一句话 · 如 \"期待新的合作机会\"}}": "如果你也在做设计工程、AI 产品或内容交付系统，欢迎交流。",
            "{{电话}}": "+86 138 5555 0199",
            "{{其他平台}}": "X",
            "{{ID}}": "noahzhou",
        },
    )
    out_html = DEMOS / "demo-portfolio.html"
    out_pdf = DEMOS / "demo-portfolio.pdf"
    out_html.write_text(filled, encoding="utf-8")
    build_pdf(out_html, out_pdf)


def generate_index() -> None:
    html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>Guizang Magazine Demo Bundle</title>
  <style>
    :root {
      --ink: #0a0a0b;
      --paper: #f1efea;
      --paper-deep: #e8e5de;
      --rule: #c7beb0;
      --copy: #18181a;
      --muted: #68635f;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      min-height: 100vh;
      padding: 48px;
      background: linear-gradient(180deg, #f6f3ee 0%, var(--paper) 100%);
      color: var(--copy);
      font-family: "SF Mono", "JetBrains Mono", Menlo, monospace;
    }
    .wrap {
      max-width: 1100px;
      margin: 0 auto;
      border: 1px solid var(--ink);
      background: rgba(255,255,255,0.45);
    }
    header {
      padding: 28px 28px 22px;
      background: var(--ink);
      color: var(--paper);
    }
    h1 {
      font-family: Georgia, "Times New Roman", serif;
      font-size: 42px;
      line-height: 1.05;
      margin-bottom: 12px;
    }
    .sub {
      font-size: 13px;
      line-height: 1.6;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      opacity: 0.78;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 18px;
      padding: 22px;
    }
    .card {
      border-top: 3px solid var(--ink);
      border-bottom: 1px solid var(--rule);
      background: #fbf8f2;
      padding: 18px 18px 16px;
    }
    .kicker {
      color: var(--muted);
      font-size: 11px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      margin-bottom: 10px;
    }
    .title {
      font-family: Georgia, "Times New Roman", serif;
      font-size: 30px;
      line-height: 1.1;
      margin-bottom: 10px;
    }
    .desc {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 14px;
      line-height: 1.6;
      color: var(--copy);
      margin-bottom: 14px;
    }
    .links a {
      display: inline-block;
      margin-right: 12px;
      margin-bottom: 8px;
      color: var(--ink);
      text-decoration: none;
      border-bottom: 1px solid var(--ink);
      font-size: 13px;
    }
    footer {
      padding: 0 22px 22px;
      color: var(--muted);
      font-size: 12px;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="sub">Guizang Magazine / Demo Bundle / 2026.04</div>
      <h1>Demo Bundle</h1>
      <div class="sub">Latest curated artifacts generated from the current skill.</div>
    </header>
    <section class="grid">
      <article class="card">
        <div class="kicker">One-Pager</div>
        <div class="title">把研究素材变成交付文档</div>
        <div class="desc">一页项目方案，展示标题层级、数字卡、时间线和 editorial metadata。</div>
        <div class="links">
          <a href="./demo-one-pager.html">HTML</a>
          <a href="./demo-one-pager.pdf">PDF</a>
        </div>
      </article>
      <article class="card">
        <div class="kicker">White Paper</div>
        <div class="title">BriefOS 白皮书</div>
        <div class="desc">多页长文样张，覆盖封面、目录、摘要、正文、表格、callout 与建议页。</div>
        <div class="links">
          <a href="./demo-long-doc.html">HTML</a>
          <a href="./demo-long-doc.pdf">PDF</a>
        </div>
      </article>
      <article class="card">
        <div class="kicker">Formal Letter</div>
        <div class="title">推荐函样张</div>
        <div class="desc">正式函件 demo，展示 mono 元信息、信件主题栏、正文与 evidence block。</div>
        <div class="links">
          <a href="./demo-letter.html">HTML</a>
          <a href="./demo-letter.pdf">PDF</a>
        </div>
      </article>
      <article class="card">
        <div class="kicker">Slides</div>
        <div class="title">Guizang Slides Demo</div>
        <div class="desc">PPTX deck，延续同一套标题、卡片、章节和 theme preset 语言。</div>
        <div class="links">
          <a href="./demo-slides.pptx">PPTX</a>
        </div>
      </article>
      <article class="card">
        <div class="kicker">Resume</div>
        <div class="title">Design Engineer Resume</div>
        <div class="desc">两页履历样张，展示 identity hero、metrics、projects、open-source spread 与 public signal。</div>
        <div class="links">
          <a href="./demo-resume.html">HTML</a>
          <a href="./demo-resume.pdf">PDF</a>
        </div>
      </article>
      <article class="card">
        <div class="kicker">Portfolio</div>
        <div class="title">Editorial Portfolio</div>
        <div class="desc">多页案例集样张，覆盖 cover、about、case spread、selected works 与 contact 页。</div>
        <div class="links">
          <a href="./demo-portfolio.html">HTML</a>
          <a href="./demo-portfolio.pdf">PDF</a>
        </div>
      </article>
    </section>
    <footer>Generated by scripts/generate_demos.py</footer>
  </div>
</body>
</html>
"""
    (DEMOS / "index.html").write_text(html, encoding="utf-8")


def build_slides_demo() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build.py"), "slides"],
        check=True,
        cwd=str(ROOT.parent.parent.parent.parent),
    )
    shutil.copy2(EXAMPLES / "slides.pptx", DEMOS / "demo-slides.pptx")


def main() -> None:
    DEMOS.mkdir(parents=True, exist_ok=True)
    generate_one_pager()
    generate_long_doc()
    generate_letter()
    generate_resume()
    generate_portfolio()
    build_slides_demo()
    generate_index()
    print("✓ Generated curated demo bundle under assets/demos")


if __name__ == "__main__":
    main()
