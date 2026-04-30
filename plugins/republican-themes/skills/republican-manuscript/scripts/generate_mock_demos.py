#!/usr/bin/env python3
"""Generate mock republican-manuscript demos for Tesla / Elon content."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from weasyprint import HTML


ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "assets" / "templates"
DEMOS = ROOT / "assets" / "demos"
DEMO_IMAGES = DEMOS / "mock-assets"
FONTS = ROOT / "assets" / "fonts"
BUILD = ROOT / "scripts" / "build.py"

PLACEHOLDER = re.compile(r"\{\{[^}]+\}\}")

PARCHMENT = (243, 239, 235)
PAPER = (235, 229, 221)
NAVY = (36, 56, 81)
NAVY_SOFT = (77, 91, 109)
INK = (35, 34, 34)
STONE = (139, 135, 130)
RULE = (208, 199, 187)


def contains_cjk(text: str) -> bool:
    return any("\u3400" <= char <= "\u9fff" for char in text)


def load_font(candidates: tuple[Path, ...], size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in candidates:
        if candidate.exists():
            try:
                return ImageFont.truetype(str(candidate), size=size)
            except OSError:
                continue
    return ImageFont.load_default()


def load_display_font(text: str, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    if contains_cjk(text):
        return load_font((FONTS / "京華老宋体v2.002.ttf", FONTS / "TsangerJinKai02-W04.ttf"), size)
    return load_font((FONTS / "TsangerJinKai02-W04.ttf", FONTS / "京華老宋体v2.002.ttf"), size)


def load_readable_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    return load_font((FONTS / "TsangerJinKai02-W04.ttf", FONTS / "京華老宋体v2.002.ttf"), size)


def fill_placeholders(text: str, replacements: dict[str, str | list[str]]) -> str:
    counters: dict[str, int] = {}

    def repl(match: re.Match[str]) -> str:
        key = match.group(0)
        if key not in replacements:
            raise ValueError(f"Missing replacement for {key}")
        value = replacements[key]
        if isinstance(value, list):
            idx = counters.get(key, 0)
            if idx >= len(value):
                raise ValueError(f"Not enough replacements for {key}")
            counters[key] = idx + 1
            return value[idx]
        return value

    filled = PLACEHOLDER.sub(repl, text)
    remaining = PLACEHOLDER.findall(filled)
    if remaining:
        raise ValueError(f"Unfilled placeholders remain: {remaining[:10]}")
    return filled


def render_pdf(html_path: Path, pdf_path: Path) -> None:
    HTML(str(html_path), base_url=str(html_path.parent)).write_pdf(str(pdf_path))


def render_preview_png(pdf_path: Path, png_path: Path) -> None:
    pdftoppm = shutil.which("pdftoppm")
    if not pdftoppm:
        return
    subprocess.run(
        [pdftoppm, "-png", "-r", "160", "-singlefile", str(pdf_path), str(png_path.with_suffix(""))],
        check=True,
        capture_output=True,
        text=True,
    )


def clear_demo_outputs() -> None:
    for path in (
        DEMOS / "demo-long-doc.html",
        DEMOS / "demo-long-doc.pdf",
        DEMOS / "demo-long-doc.png",
        DEMOS / "demo-one-pager.html",
        DEMOS / "demo-one-pager.pdf",
        DEMOS / "demo-resume.html",
        DEMOS / "demo-resume.pdf",
        DEMOS / "demo-resume.png",
        DEMOS / "demo-portfolio.html",
        DEMOS / "demo-portfolio.pdf",
        DEMOS / "demo-slides.pptx",
    ):
        if path.exists():
            path.unlink()
    slides_online = DEMOS / "slides-online"
    if slides_online.exists():
        for child in sorted(slides_online.rglob("*"), reverse=True):
            if child.is_file() or child.is_symlink():
                child.unlink()
            else:
                child.rmdir()
        slides_online.rmdir()
    if DEMO_IMAGES.exists():
        for child in sorted(DEMO_IMAGES.rglob("*"), reverse=True):
            if child.is_file() or child.is_symlink():
                child.unlink()
            else:
                child.rmdir()
        DEMO_IMAGES.rmdir()


def make_mock_scene(path: Path, title: str, subtitle: str, accent: tuple[int, int, int], footer: str) -> None:
    width, height = 1600, 900
    image = Image.new("RGB", (width, height), PARCHMENT)
    draw = ImageDraw.Draw(image)
    title_font = load_display_font(title, 68)
    subtitle_font = load_readable_font(34)
    small_font = load_readable_font(24)

    for y in range(height):
        mix = y / max(height - 1, 1)
        r = int(PARCHMENT[0] * (1 - mix) + PAPER[0] * mix)
        g = int(PARCHMENT[1] * (1 - mix) + PAPER[1] * mix)
        b = int(PARCHMENT[2] * (1 - mix) + PAPER[2] * mix)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    draw.rectangle((40, 40, width - 40, height - 40), outline=NAVY, width=4)
    draw.rectangle((58, 58, width - 58, height - 58), outline=NAVY_SOFT, width=2)
    draw.rectangle((90, 110, 790, 310), fill=NAVY)
    draw.rectangle((110, 130, 770, 290), outline=(243, 239, 235), width=3)
    draw.text((145, 155), title, font=title_font, fill=PARCHMENT)
    draw.text((148, 248), subtitle, font=subtitle_font, fill=(213, 222, 231))

    draw.rounded_rectangle((880, 150, 1480, 640), radius=18, outline=NAVY_SOFT, width=3, fill=(246, 241, 232))
    draw.line((930, 585, 1260, 340), fill=accent, width=8)
    draw.line((1260, 340, 1390, 430), fill=NAVY, width=8)
    draw.ellipse((910, 545, 960, 595), fill=NAVY)
    draw.ellipse((1235, 315, 1285, 365), fill=accent)
    draw.ellipse((1365, 405, 1415, 455), fill=NAVY_SOFT)

    draw.rounded_rectangle((160, 430, 760, 720), radius=14, outline=RULE, width=2, fill=(247, 242, 234))
    draw.rectangle((180, 458, 730, 490), fill=accent)
    draw.text((200, 518), "MOCK VISUAL", font=small_font, fill=NAVY)
    draw.text((200, 566), footer, font=subtitle_font, fill=INK)
    draw.text((200, 626), "全部图片为内部演示素材，用于验证 portfolio 与 slides 的图片位布局。", font=small_font, fill=STONE)

    draw.text((1120, 700), "Tesla Mock Asset", font=small_font, fill=STONE)
    image.save(path)


def create_mock_images() -> None:
    DEMO_IMAGES.mkdir(parents=True, exist_ok=True)
    make_mock_scene(
        DEMO_IMAGES / "mock-tesla-factory.png",
        "得州 + 上海",
        "双工厂协同扩产示意",
        (166, 79, 51),
        "Factory switch / Yield / Buffer / Ramp",
    )
    make_mock_scene(
        DEMO_IMAGES / "mock-tesla-robotaxi.png",
        "Robotaxi Pilot",
        "城市调度与车内体验 mock 图",
        (104, 112, 83),
        "Dispatch / Charge / Clean / Safety loop",
    )
    make_mock_scene(
        DEMO_IMAGES / "mock-tesla-energy.png",
        "Megapack Pipeline",
        "储能项目交付版图与节拍",
        (78, 110, 129),
        "Grid storage / Pipeline / Margin / Throughput",
    )
    make_mock_scene(
        DEMO_IMAGES / "mock-tesla-optimus.png",
        "Optimus Internal Use",
        "厂内搬运与巡检场景 mock 图",
        (132, 101, 71),
        "Handling / Inspection / Shift coverage / Labor relief",
    )


def generate_one_pager() -> None:
    text = (TEMPLATES / "one-pager.html").read_text(encoding="utf-8")
    filled = fill_placeholders(
        text,
        {
            "{{文档标题}}": "Tesla 2027 一页纸",
            "{{英文眉题 · 如 COMPANY BRIEF / PROJECT DOSSIER}}": "TESLA COMPANY BRIEF",
            "{{文档主标题，两行内，动词 + 名词结构最好}}": "把 Tesla 从\n车企看成平台",
            "{{一行副标题 / 一句核心论点}}": "给投委会的 mock 执行摘要",
            "{{档案标签 · 如 Archive Note}}": "Archive Note",
            "{{项目 / 公司 / 主题名称}}": "Tesla, Inc. · 2027 Growth Story",
            "{{版本 / 状态}}": "Mock / V1.0",
            "{{日期 YYYY.MM.DD}}": "2026.04.28",
            "{{文档分类}}": "公司简报",
            "{{40-70 字核心导语。用 <span class=\"hl\">关键词</span> 点出判断，让读者立刻知道这份一页纸的主张。}}": "判断核心不是 Tesla 能卖出多少辆车，而是它能否把 <span class=\"hl\">制造、软件、储能、机器人</span> 四条曲线压到同一张经营报表里。",
            "{{栏目标题 1}}": "为什么现在看 Tesla",
            "{{短 bullet：事实 / 数据 / 判断}}": "成熟车型提供现金流，新平台负责打开下一轮毛利结构。",
            "{{短 bullet：带 <span class=\"hl\">关键数字</span> 的论据}}": "Mock 口径下，储能在手项目达 <span class=\"hl\">438GWh</span>，足以对冲部分汽车周期波动。",
            "{{短 bullet：下一步或风险}}": "最大风险不是需求，而是工厂切线、自动驾驶监管和电池分配。",
            "{{栏目标题 2}}": "接下来 18 个月",
            "{{英文小标题}}": ["What Changed", "What Matters"],
            "{{1-2 句概括。}}": [
                "市场过去把 Tesla 视为高波动汽车股，但 2027 年更合理的视角是多业务平台公司。",
                "真正需要跟踪的不是单月销量，而是 Robotaxi 试点、Megapack 节拍和 Optimus 厂内部署是否同步兑现。",
            ],
            "{{指标说明}}": ["年化交付目标", "储能在手储备", "Robotaxi 试点城市", "Optimus 厂内部署"],
            "{{数字}}": ["620 万", "438 GWh", "12 城", "1.8 万"],
            "{{短 bullet}}": [
                "整车交付负责现金流，软件收入负责拉高生命周期价值。",
                "储能业务决定季度波动是否可被磨平。",
                "机器人先证明工厂内价值，再去讲外部市场。",
            ],
            "{{Timeline / Roadmap}}": "Roadmap",
            "{{阶段 / 年份 1}}": "2026 H2",
            "{{阶段标题}}": ["Factory Switch", "Pilot Launch", "Scale Review"],
            "{{一句解释}}": [
                "得州与上海分工明确，新平台切线不牺牲成熟车型节奏。",
                "Robotaxi 先在高密度城市跑通调度、充电、清洁闭环。",
                "Megapack 与 Optimus 的兑现节奏开始进入同一张经营看板。",
            ],
            "{{阶段 / 年份 2}}": "2027 H1",
            "{{阶段 / 年份 3}}": "2027 H2",
            "{{关键里程碑 / 核心事项}}": "五个检查点 / 风险前瞻",
            "{{事项 1：一句话}}": "工厂切线期良率是否稳定爬坡",
            "{{事项 2：一句话}}": "Robotaxi 可用时长能否跑出正向运营杠杆",
            "{{事项 3：一句话}}": "Megapack 项目是否形成季度稳定节拍",
            "{{事项 4：一句话}}": "Optimus 是否先在自家工厂替代重复工时",
            "{{关键引用 / 核心 takeaway / 重要提示。}}": "Tesla 的价值不再取决于一款爆款车，而取决于多条业务曲线是否被统一调度。",
            "{{补充说明：为什么这句话重要。}}": "如果四条曲线分别独立讲故事，市场会只给汽车股估值；只有它们共享制造、算力与软件资产时，平台叙事才成立。",
            "{{公开 / 内部 / 机密级别}}": "INTERNAL MOCK / DEMO USE ONLY",
            "{{页码 / 联系方式}}": "01 / tesla-mock@kami.local",
        },
    )
    html_path = DEMOS / "demo-one-pager.html"
    pdf_path = DEMOS / "demo-one-pager.pdf"
    html_path.write_text(filled, encoding="utf-8")
    render_pdf(html_path, pdf_path)


def generate_long_doc() -> None:
    text = (TEMPLATES / "long-doc.html").read_text(encoding="utf-8")
    filled = fill_placeholders(
        text,
        {
            "{{文档标题}}": "Tesla 2027 平台化增长白皮书",
            "{{WHITE PAPER · INTERNAL EDITION}}": "WHITE PAPER · INTERNAL EDITION",
            "{{文档分类}}": "经营白皮书",
            "{{公开级别 / 内部公开版}}": "内部演示版 / Mock Data",
            "{{Archive Knowledge System}}": "TESLA PLATFORM DOSSIER",
            "{{文档主标题<br>可以两行}}": "Tesla 2027 平台化增长<br>与资源调度白皮书",
            "{{副标题：一句话说清这份白皮书解决什么问题、为谁而写。}}": "给投委会与经营团队的一份判断文档：为什么马斯克正在把整车、Robotaxi、储能、Optimus 与 AI 算力压进同一套经营系统。",
            "{{团队 / 部门}}": "Strategy / Capital Allocation",
            "{{专题 / 项目}}": "Tesla · Musk Operating Model",
            "{{V1.0}}": "V1.0",
            "{{2026.04}}": "2026.04",
            "{{封面注记：本文档聚焦哪几个问题，读者读完能获得什么判断。}}": "本文聚焦 Tesla 未来 18 个月最关键的四条曲线：制造切线、Robotaxi 试点、Megapack 交付节拍与 Optimus 厂内部署。读完以后，读者应能判断 Tesla 是否值得被继续按单一车企估值。",
            "{{作者 / 团队}}": "Kami Demo Desk",
            "{{发布方 / 机构}}": "Republican Manuscript Skill",
            "{{示意页数}}": "6 页",
            "{{一段 2-3 句话的大论点开场。用 <span class=\"hl\">关键词高亮</span> 抓住读者注意力，让读者读这一段就理解整份文档。}}": "Tesla 下一阶段最重要的不是再多卖几辆车，而是能否把 <span class=\"hl\">制造、软件、储能、机器人</span> 四条增长曲线放进同一张经营报表。马斯克真正下注的是资源调度能力，而不是单个爆款产品。",
            "{{Takeaway 1：一句话，可量化}}": "Mock 口径下，两地工厂合计年化产能已到 <span class=\"hl\">5.8M</span>，目标是把交付能力推进到 <span class=\"hl\">6.2M</span> 而不牺牲良率。",
            "{{Takeaway 2：有数据的洞察}}": "储能在手项目储备达到 <span class=\"hl\">438GWh</span>，说明 Tesla 已经拥有能平滑整车周期波动的第二现金流引擎。",
            "{{Takeaway 3：对未来的判断}}": "如果 Robotaxi 试点城市、Megapack 节拍与 Optimus 厂内部署能在 2027 年同步兑现，Tesla 将更像平台型经营体而非单一汽车股。",
            "{{用一段话说明为什么现在需要这份文档，以及决策者读完以后应该采取什么行动。}}": "现在需要这份文档，是因为市场仍然用汽车行业的线性框架理解 Tesla，但公司内部资源分配已经明显转向平台逻辑。决策者读完以后，不应只盯交付量，而应把工厂切线效率、城市运营能力、储能节拍和机器人内部替代率并列跟踪。",
            "{{列出 3 个核心问题：范围、方法、交付标准。}}": "1. Tesla 的四条增长曲线是否真的共享同一套资源池？<br>2. 哪些指标最能提前暴露平台叙事能否成立？<br>3. 未来 18 个月管理层应该按什么顺序验证这些假设？",
            "{{章节导语：这一章要解决什么问题，为什么重要。}}": "这一章要解决的问题是：为什么 Tesla 不能再被简单地看作一家高波动汽车公司。只有先把业务结构理解对，后面的估值和执行判断才不会偏掉。",
            "{{3-5 行段落，铺陈当前状况。用 <span class=\"hl\">具体数据</span> 而不是形容词。}}": "过去一年里，Tesla 的经营重心已经明显扩展到整车之外。Mock 口径下，整车年化交付能力约 <span class=\"hl\">5.8M</span>，储能在手储备达到 <span class=\"hl\">438GWh</span>，Robotaxi 首波试点规划覆盖 <span class=\"hl\">12 个城市</span>，Optimus 厂内部署目标来到 <span class=\"hl\">18k</span> 台。这四组数字放在一起看，才是马斯克当前真正的资源分配图。",
            "{{陈述具体问题，说明它如何影响交付、效率或判断质量。}}": "核心问题在于，外部观察者仍然倾向于只看交车数，而内部最稀缺的资源其实是电池、算力、产线窗口与管理带宽。如果继续用单一整车指标来评估 Tesla，就会低估储能和 Robotaxi 对现金流与估值框架的重塑，也会误判工厂切线期的真实风险。",
            "{{一段重要引用或核心观察。和正文语气略有不同，给读者呼吸节奏。}}": "Tesla 最关键的竞争力不是某个产品点，而是把多条复杂曲线压进同一套 operating system；谁只看单月销量，谁就会错过真正的杠杆。",
            "{{来源 / 人物}}": "Mock 经营观察",
            "{{日期}}": "2026.04.30",
            "{{维度 1}}": "年化交付能力",
            "{{数据}}": ["5.8M", "6.2M", "438GWh", "520GWh"],
            "{{差距}}": ["+0.4M，且切线期良率不能失稳", "+82GWh，且电池分配不能挤压整车节拍"],
            "{{维度 2}}": "储能在手储备",
            "{{章节导语：说明研究方法和最重要的发现。}}": "本章说明我们如何把 Tesla 的多业务经营拆开再重新拼回去。最重要的发现是：四条曲线看似分散，实际上都在争夺同一组共享资产。",
            "{{描述资料来源、访谈范围、样本口径或分析方法。}}": "文档采用 mock 研究口径，综合了 Tesla 公开叙事、Musk 的经营风格、工厂与储能业务节拍假设，以及当前模板中已有的演示数据。分析方法不是预测季度财报，而是观察电池、工厂、城市运营和算力如何被共同调度。",
            "{{如需代码或规则示例，放在这里；不需要时删除整个 pre。}}": "board = {\n  'factory_switch': ['yield', 'buffer_days', 'rework_rate'],\n  'robotaxi_ops': ['active_hours', 'charge_turnaround', 'safety_events'],\n  'energy_pipeline': ['booked_gwh', 'delivery_window', 'battery_allocation'],\n  'optimus_internal': ['units', 'hours_replaced', 'station_coverage'],\n}",
            "{{标题}}": ["共享资产比业务线本身更重要", "兑现顺序决定叙事能否成立"],
            "{{一段论述，包含 <span class=\"hl\">具体数字 / 具体比例</span>。}}": "Tesla 当前最稀缺的资产不是品牌，而是可被复用的共享底座。以 mock 口径看，储能在手 <span class=\"hl\">438GWh</span>、Robotaxi 试点 <span class=\"hl\">12 城</span>、Optimus 内部目标 <span class=\"hl\">18k 台</span>，都要与整车交付共用电池、算力、产线和运营带宽。平台逻辑一旦成立，外部估值锚点就会发生变化。",
            "{{一段论述，说明原因和影响。}}": "真正决定 Tesla 叙事是否成立的，不是每条业务各自讲得多大，而是兑现顺序是否合理。如果先把 Robotaxi 扩到过多城市、或过早把 Optimus 推向外部市场，管理复杂度会先于经营杠杆爆发；反过来，若先稳住工厂切线和储能节拍，再逐步放开城市运营与机器人场景，平台故事会更可信。",
            "{{对执行者最重要的一句提醒。}}": "执行上最忌讳四条线同时求最大化，正确顺序应该是先稳工厂与储能，再放大 Robotaxi，最后把 Optimus 的内部样板外溢出去。",
            "{{一句话总结结论，下面展开建议。}}": "结论很简单：Tesla 值不值得被重新估值，取决于共享资产是否真的被高效复用。",
            "{{结论 1}}": "管理层应把工厂切线效率视为平台叙事的起点，而不是单纯制造问题。",
            "{{结论 2}}": "储能业务的稳定节拍，是判断 Tesla 是否能穿越整车周期波动的关键缓冲器。",
            "{{结论 3}}": "Robotaxi 与 Optimus 只有在内部运营逻辑跑通后，才值得被当作独立增长曲线放大。",
            "{{基于结论的具体可执行建议。}}": "建议把月度经营看板改成四组并列指标：工厂良率 / 交付缓冲天数，Robotaxi 活跃车次 / 充电周转，Megapack 在手储备 / 完工率，Optimus 替代工时 / 场景覆盖率。只有把这些指标放到同一张表里，管理层才能及时识别资源错配。",
            "{{如果读者要做一件事，是什么？具体到可以周一早上就开始行动。}}": "周一早上就把 Tesla 的经营周报从“单一交付视图”改成“共享资产视图”：要求每条业务线在同一页上报电池占用、算力占用、产线窗口与运营带宽，先看冲突，再谈增长。",
            "{{附录摘要或参考资料说明。}}": "附录可继续扩展为：Tesla 主要业务线术语表、Musk 风格的资源调度原则、以及 Robotaxi / Megapack / Optimus 三条曲线的分季度验证清单。当前版本保留为演示样例，用于验证 republican-manuscript 的白皮书生成链路。",
        },
    )
    html_path = DEMOS / "demo-long-doc.html"
    pdf_path = DEMOS / "demo-long-doc.pdf"
    png_path = DEMOS / "demo-long-doc.png"
    html_path.write_text(filled, encoding="utf-8")
    render_pdf(html_path, pdf_path)
    render_preview_png(pdf_path, png_path)


def generate_resume() -> None:
    text = (TEMPLATES / "resume.html").read_text(encoding="utf-8")
    filled = fill_placeholders(
        text,
        {
            "{{姓名}}": "伊隆·马斯克",
            "{{变量}}": "实际内容",
            "{{别名/英文名}}": "Elon Musk",
            "{{岗位定位，如\"AI / Agent 工程\"}}": "产品 / 工程 / 资本配置",
            "{{GITHUB_URL}}": "https://github.com/elonmusk-mock",
            "{{GITHUB_ID}}": "elonmusk-mock",
            "{{X_URL}}": "https://x.com/elonmusk",
            "{{X_ID}}": "elonmusk",
            "{{PHONE}}": "+1 737 555 0147",
            "{{EMAIL}}": "elon.mock@tesla-demo.ai",
            "{{年龄}}": "55",
            "{{城市}}": "奥斯汀",
            "{{数字}}": ["6", "4", "22", "14"],
            "{{单位}}": ["家公司", "条增长曲线", "年一线管理", "万名直接员工"],
            "{{标签}}": ["核心业务矩阵", "制造 / 软件 / 能源 / 机器人", "连续经营周期", "跨区域组织规模"],
            "{{80 字以内。建议结构：现任职位 + 级别 + 时长。团队构成（人数、梯队、协作方）。长期演进方向。核心沉淀领域（4-6 个方向）。}}": "现任 Tesla / SpaceX / xAI 多业务负责人。长期把资本配置、产品定义、制造执行与 AI 叙事压到同一张经营报表里。",
            "{{起始时间}}": "2004",
            "{{关键里程碑}}": "从多项目创始人切换到平台型经营者",
            "{{年份}}": ["2004", "2019", "2025"],
            "{{阶段标题}}": ["进入 Tesla", "上海工厂成型", "AI / 机器人并线"],
            "{{一句解释这一步的意义}}": [
                "从单点创业者转向长期经营者，开始把产品定义与资本效率联动考虑。",
                "证明高密度制造与本地供应链可以在极短周期内跑出规模效率。",
                "把自动驾驶、算力、机器人和储能并入同一套资源调度体系。",
            ],
            "{{项目名}}": [
                "Tesla 经营平台",
                "Robotaxi 试点业务",
                "Optimus 厂内部署",
                "Fleet API Toolkit",
                "Dojo Capacity Planner",
                "Megapack Config Studio",
                "Factory Ops Notebook",
                "Vehicle Data Replay",
                "Energy Tender Model",
            ],
            "{{项目类型}}": ["制造 / 软件 / 零售一体化", "自动驾驶运营", "工业机器人"],
            "{{角色定位，如\"方向主导\"}}": "方向主导",
            "{{~60 字：项目是什么 + 为什么做 + 你的位置}}": "负责把 Tesla 从单一整车增长模型，切成制造、软件、能源与机器人四条协同曲线，并亲自定义优先级。",
            "{{~80 字：技术方案 / 关键决策 / 执行路径}}": "推动成熟车型稳现金流，新平台承接成本下探；同时把工厂软件、充电网络、FSD 数据闭环与电池产能当成共享资产来排布。",
            "{{~100 字：数据为王。<span class=\"hl\">关键数字</span> 高亮 1-2 处。}}": "Mock 口径下，年度交付目标提升至 <span class=\"hl\">620 万辆</span>，并把储能在手储备推进到 <span class=\"hl\">438GWh</span>，使资本市场开始用平台视角而非单一车企视角看待 Tesla。",
            "{{角色定位}}": "业务架构 owner",
            "{{~60 字}}": "把 Robotaxi 从功能演示推进成城市级试点业务，关注的不是炫技而是可调度、可清洁、可充电、可复购。",
            "{{~80 字}}": "先跑封闭区域和固定路线，再按城市密度逐步放开；把安全事件、充电周转和高峰调度写进同一套日运营指标中。",
            "{{~100 字，含 <span class=\"hl\">关键数字</span>}}": "Mock 口径下，首波试点覆盖 <span class=\"hl\">12 个城市</span>，高峰时段车辆利用率达到 <span class=\"hl\">72%</span>，让自动驾驶收入开始与活跃车次直接相关。",
            "{{角色}}": "场景 owner",
            "{{项目背景和定位}}": "把 Optimus 从概念机推进到厂内真正可部署的搬运与巡检工具，优先证明内部价值，而不是先讲对外销量。",
            "{{执行路径}}": "优先替代夜班搬运、重复分拣和工站巡检，把机器人能力演进反向写进产线和物料标准化改造中。",
            "{{可量化结果，含 <span class=\"hl\">关键数字</span>}}": "Mock 口径下，厂内部署规模达到 <span class=\"hl\">1.8 万台</span>，替代 <span class=\"hl\">23%</span> 的重复工时，为后续外部工业客户建立可信案例。",
            "{{时间跨度}}": "2015 — 2026",
            "{{一句副标题}}": "把公开技术资产视为品牌与招聘飞轮的一部分",
            "{{一句自我定位}}": "不是最传统意义上的开源作者，但持续用公开工具、公开接口与公开方法论放大工程影响力",
            "{{简述开发者身份：设计审美 / 独立完成流程 / 跨语言实战 / 用户反馈}}": "强调从 API、产能规划、运维工具到外部开发者体验的一体化经营。",
            "{{STARS_TOTAL}}": "182k",
            "{{FORKS_TOTAL}}": "26k",
            "{{FOLLOWERS_TOTAL}}": "94k",
            "{{URL}}": [
                "https://github.com/tesla-mock/fleet-api-toolkit",
                "https://github.com/tesla-mock/dojo-capacity-planner",
                "https://github.com/tesla-mock/megapack-config-studio",
                "https://github.com/tesla-mock/factory-ops-notebook",
                "https://github.com/tesla-mock/vehicle-data-replay",
                "https://github.com/tesla-mock/energy-tender-model",
                "https://x.com/elonmusk",
                "https://tesla-mock.ai/notes/factory-switch",
                "https://tesla-mock.ai/notes/robotaxi-unit-economics",
                "https://tesla-mock.ai/talks/robotaxi-pilot-day",
                "https://tesla-mock.ai/talks/optimus-factory-ops",
            ],
            "{{语言 + 核心定位 + 平台}}": "Python / TypeScript · Fleet API 开发生态 · Tesla 开发者平台",
            "{{STARS}}": ["48k", "39k", "28k", "21k", "17k", "11k"],
            "{{描述}}": [
                "把工厂算力排布、模型训练节拍与车端上线窗口放进同一份 capacity board。",
                "面向储能投标团队的快速配置器，用来模拟项目规模、毛利与交付窗口。",
                "厂长与运营负责人共用的周报 notebook，把良率、周转与返工统一到单页视图。",
                "用于回放车端异常与自动驾驶事件的内部分析工具，帮助压缩定位时间。",
                "把储能项目报价、排产和电池分配约束联动建模的 mock 工具。",
            ],
            "{{亮点 TAG}}": "PUBLIC TOOLING",
            "{{这个项目的独特故事：开源时机 / 传播范围 / 知名人物推荐等}}": "公开接口与 mock tooling 帮助 Tesla 在招聘、开发者生态和供应商协同上持续获得额外杠杆。",
            "{{时间}}": ["2024", "2025", "2026"],
            "{{事件标题}}": ["押注厂内机器人先于家庭机器人", "把 Robotaxi 当作运营业务而非功能 feature", "在储能周期里优先要可预测节拍"],
            "{{具体做了什么判断或行动，为什么证明判断力}}": "先用内部场景证明单位替代工时，再决定是否向外部客户扩张，避免把机器人过早推向消费叙事。",
            "{{具体做了什么判断或行动}}": [
                "要求团队把调度、充电、清洁和安全事件闭环一起设计，防止自动驾驶只停留在车端能力展示。",
                "在电池供给紧张时，把储能项目和整车业务放进同一张分配表，优先保留更稳的交付节拍。",
            ],
            "{{平台}}": "X",
            "{{HANDLE}}": "elonmusk",
            "{{粉丝数}}": "2.1 亿",
            "{{博客 / 周刊 / 其他内容产品简介}}": "持续输出产品发布、工厂进展、AI 判断与资本市场沟通，是最强的对外 narrative channel 之一。",
            "{{副标题}}": ["Factory / AI / Energy", "Product / Operations"],
            "{{文章标题}}": ["为什么工厂切线速度比销量更重要", "Robotaxi 的单位经济性应该怎么看"],
            "{{日期}}": ["2026.02", "2025.11", "2025.09", "2026.03"],
            "{{浏览量 / 赞数 / 影响力指标}}": "阅读 860 万 · 收藏 12 万 · 二次引用 4.3 万",
            "{{浏览量 / 赞数}}": "阅读 540 万 · 点赞 8.7 万",
            "{{演讲标题}}": ["把 Robotaxi 做成调度业务", "Optimus 为什么先在厂里工作"],
            "{{主办方 / 地点}}": ["Tesla AI Day · Austin", "Manufacturing Summit · Shanghai"],
            "{{能力 1<br>标签}}": "资本配置",
            "{{能力 2<br>标签}}": "产品定义",
            "{{能力 3<br>标签}}": "制造执行",
            "{{能力 4<br>标签}}": "叙事管理",
            "{{能力 5<br>标签}}": "组织切换",
            "{{描述。至少 <span class=\"em-brand\">1 处强调</span>}}": [
                "擅长把多条增长曲线压到同一张经营报表，用 <span class=\"em-brand\">资源调度</span> 而不是单点 KPI 来做判断。",
                "能把抽象方向翻译成产品路线图，把 <span class=\"em-brand\">功能、成本、节拍</span> 三个维度同时纳入定义。",
                "熟悉从工艺、产线到供应链的联动，强调 <span class=\"em-brand\">切线效率与良率爬坡</span> 的优先级。",
                "对外沟通不是简单营销，而是把复杂经营逻辑转成 <span class=\"em-brand\">投资者可读的 narrative</span>。",
                "敢于在周期切换期重组团队与优先级，用 <span class=\"em-brand\">组织结构服务业务结构</span>。",
            ],
            "{{学校}}": "宾夕法尼亚大学",
            "{{学院}}": "经济学 / 物理学",
            "{{专业}}": "双学位",
            "{{一句判断性描述，如\"放弃保研直接就业\"}}": "毕业后直接进入连续创业与长期经营",
            "{{起止时间}}": "1990 — 1995",
        },
    )
    html_path = DEMOS / "demo-resume.html"
    pdf_path = DEMOS / "demo-resume.pdf"
    png_path = DEMOS / "demo-resume.png"
    html_path.write_text(filled, encoding="utf-8")
    render_pdf(html_path, pdf_path)
    render_preview_png(pdf_path, png_path)


def generate_portfolio() -> None:
    text = (TEMPLATES / "portfolio.html").read_text(encoding="utf-8")
    filled = fill_placeholders(
        text,
        {
            "{{年份 或 领域标签 · 如 \"Selected Works 2023–2026\"}}": "Selected Works 2024–2026",
            "{{名字}}": "Elon Musk",
            "{{名字<br>Portfolio}}": "Elon Musk<br>Portfolio",
            "{{一句自我描述 / 作品集主题}}": "以制造、软件、能源与机器人为主轴的产品与工程作品叙事",
            "{{专业 / 角色}}": "Product / Engineering / Capital Allocation",
            "{{所在地}}": "Austin, Texas",
            "{{EMAIL}}": "elon.mock@tesla-demo.ai",
            "{{网站 / 社交链接}}": "tesla-mock.ai · x.com/elonmusk",
            "{{一句自我定位的 headline}}": "把难以经营的复杂系统，整理成可复用的平台能力",
            "{{2-3 行的自我介绍引言。serif 字体，斜体感，不写太 sales。\n    用自己的语言描述你关心什么、擅长什么。}}": "我长期关注那些需要同时处理资本密度、制造节拍与软件速度的问题。真正让我感兴趣的，不是单个产品爆发，而是能否把多条曲线压进同一套 operating system。",
            "{{一段关于你过往经历的概述。}}": "过去二十年，我持续在汽车、航天、能源与 AI 基础设施之间切换角色，但方法始终一致：先定义关键瓶颈，再把产品、工厂、供应链和叙事连成一体。",
            "{{一段关于你当前的关注点 / 方法论。}}": "当前重点是把 Robotaxi、Megapack 与 Optimus 放进同一套资源调度逻辑里。我的方法不是追求每条线都最激进，而是让每条线都能为下一条线释放杠杆。",
            "{{项目类型 · 如 \"Product Design\" / \"Open Source\"}}": "Mobility Platform / Operations",
            "{{项目名称}}": ["Tesla Robotaxi Fleet OS", "Optimus Factory Deployment"],
            "{{一句话描述这个项目做了什么}}": "把自动驾驶、调度、充电与城市运营，整理成可复制的 Robotaxi 业务模板。",
            "{{时间 · 如 \"2025.04 — 2026.02\"}}": "2025.04 — 2026.12",
            "{{标签 1}}": "Robotaxi",
            "{{标签 2}}": "Fleet Ops",
            "{{标签 3}}": "Autonomy",
            "{{为什么做这个项目？要解决什么问题？谁是用户？}}": "如果自动驾驶只能卖车端功能，它的商业天花板会非常低。这个项目的目的，是把驾驶能力变成持续运营业务，用户包括通勤乘客、车队运营者和城市试点团队。",
            "{{怎么做的？关键决策、设计考量、技术方案。}}": "关键决定是先跑高密度城市的小范围运营，而不是一开始追求大范围覆盖。所有调度、充电、清洁与异常处置都被视为产品的一部分，而不是后勤环节。",
            "{{结果是什么？<span class=\"hl\">数据</span>、反馈、影响。}}": "Mock 口径下，Robotaxi 试点覆盖 <span class=\"hl\">12 个城市</span>，高峰时段车辆利用率达到 <span class=\"hl\">72%</span>，并把自动驾驶收入从一次性售价切换到持续运营收入。",
            "{{数字}}": ["12", "72%", "18k"],
            "{{标签}}": ["试点城市", "高峰利用率", "厂内部署", "工业替代率", "部署节拍"],
            "{{项目类型}}": "Industrial Robotics",
            "{{一句话描述}}": "让 Optimus 先在自家工厂替代重复劳动，再把经验外溢到工业客户。",
            "{{时间}}": "2025.08 — 2026.12",
            "{{背景}}": "Optimus 如果一开始就直接讲家庭机器人，会陷入体验不稳定与单位经济性不清晰的问题。因此它更适合作为厂内搬运、分拣、巡检设备切入。",
            "{{方法}}": "先用夜班搬运与工站巡检场景建立标准作业，再把机器人能力写回工位、物料与安全规则中，让部署过程本身变成工厂优化的一部分。",
            "{{结果}}": "Mock 口径下，厂内部署规模提升到 <span class=\"hl\">1.8 万台</span>，重复工时替代比例达到 <span class=\"hl\">23%</span>，为后续外部工业销售建立可信样板。",
            "{{作品标题}}": ["Megapack Pipeline Control", "Factory Switch Dashboard", "Dojo Capacity Ledger"],
            "{{一句描述}}": [
                "把储能项目排产、交付窗口与电池分配放在一张图里看。",
                "把平台切线期的良率、库存与返工压缩成管理层单页。",
                "用于平衡训练算力投资、模型节拍和车端上线窗口的内部账本。",
            ],
            "{{链接 / 状态}}": ["Internal Mock", "Planning", "Operator View"],
            "{{欢迎联系的一句话 · 如 \"期待新的合作机会\"}}": "如果你也在经营高资本密度的复杂系统，欢迎交流。",
            "{{电话}}": "+1 737 555 0147",
            "{{URL}}": ["https://tesla-mock.ai", "https://x.com/elonmusk", "https://x.com/elonmusk"],
            "{{其他平台}}": "X",
            "{{ID}}": "elonmusk",
        },
    )
    # Portfolio demos must preserve the template contract: placeholders first,
    # diagrams when the visual is really a chart/flow/relationship, and real
    # images only when the caller explicitly opts into them.
    html_path = DEMOS / "demo-portfolio.html"
    pdf_path = DEMOS / "demo-portfolio.pdf"
    html_path.write_text(filled, encoding="utf-8")
    render_pdf(html_path, pdf_path)


def build_slides() -> None:
    subprocess.run([sys.executable, str(BUILD), "slides"], check=True, cwd=str(ROOT))


def main() -> None:
    DEMOS.mkdir(parents=True, exist_ok=True)
    clear_demo_outputs()
    create_mock_images()
    generate_one_pager()
    generate_long_doc()
    generate_resume()
    generate_portfolio()
    build_slides()
    print("✓ Generated manuscript mock demos")


if __name__ == "__main__":
    main()
