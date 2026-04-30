#!/usr/bin/env python3
"""Shared slide deck schema for PPTX and Slidev renderers.

`image` is optional for any visual-heavy slide. When omitted, both renderers
fall back to a solid placeholder panel so the skill can initialize a usable
template even when the calling model cannot generate images.

For chart-like visuals, prefer `diagram = "architecture" | "flowchart" |
"quadrant"` plus copy that points the user to `assets/diagrams/*.html`,
rather than inventing a pseudo-chart screenshot.
"""

from __future__ import annotations

from typing import Any


DECK: list[dict[str, Any]] = [
    {
        "kind": "cover",
        "section": "TESLA 2027 MOCK BRIEFING",
        "page": 1,
        "kicker": "KAMI · REPUBLICAN MANUSCRIPT DEMO",
        "title": "Tesla 2027\n增长与产能叙事",
        "subtitle": "Robotaxi / Energy / Optimus / AI Infrastructure",
        "body": "此 deck 用 republican-manuscript skill 生成。\n全部数据与图片均为 mock，用于验证 PPTX / Slidev 双产物路径。",
        "metrics": [
            {"value": "04", "label": "growth bets", "note": "车 / 能源 / 算力 / 机器人"},
            {"value": "08", "label": "slides", "note": "dual-output deck"},
        ],
        "meta": "2026.04 · Mock Data · Internal Demo",
    },
    {
        "kind": "principle",
        "section": "INVESTMENT THESIS",
        "page": 2,
        "number": 1,
        "title": "核心判断",
        "lede": "Tesla 的下一阶段估值不再只由整车交付驱动，而是由制造、软件、能源与机器人四条曲线共同决定。",
        "cards": [
            {"label": "BET 01", "title": "Robotaxi", "body": "把 FSD 资产从一次性卖车收入，转换成持续运营收入。"},
            {"label": "BET 02", "title": "Energy", "body": "储能业务用更稳定的交付节奏，平衡汽车周期波动。"},
            {"label": "BET 03", "title": "Factory OS", "body": "上海与得州工厂共享工艺、软件和供应链缓冲带。"},
            {"label": "BET 04", "title": "Optimus", "body": "机器人先在自家工厂落地，再逐步外溢到物流与服务。"},
        ],
        "summary": "四条曲线共用电池、算力、软件与工厂资产。",
    },
    {
        "kind": "image-focus-factory",
        "section": "OPERATIONS",
        "page": 3,
        "number": 2,
        "title": "上海与得州进入同屏扩产期",
        "lede": "Mock 逻辑：一个工厂守住成本，一个工厂承接新平台切换，产能结构比单纯冲量更重要。",
        "image": "mock-tesla-factory.png",
        "caption": "Mock visual · 双工厂协同示意",
        "metrics": [
            {"value": "5.8M", "label": "年化产能", "note": "两地产线合计"},
            {"value": "41d", "label": "在制周转", "note": "切换期目标"},
        ],
        "bullets": [
            "上海继续承担成熟车型与出口任务，稳定现金流与交付节奏。",
            "得州优先给新平台、Robotaxi 版本与下一代低成本总装工艺。",
            "核心不是绝对产能，而是切换效率、良率爬坡与供应链缓冲。 ",
        ],
    },
    {
        "kind": "image-focus-robotaxi",
        "section": "AUTONOMY",
        "page": 4,
        "number": 3,
        "title": "Robotaxi 不是一辆车，而是一套调度业务",
        "lede": "Mock 逻辑：Robotaxi 的关键变量是上路城市、可用时长、调度效率和安全冗余，不只是硬件 BOM。",
        "image": "mock-tesla-robotaxi.png",
        "caption": "Mock visual · 城市内 Robotaxi 运营舱",
        "metrics": [
            {"value": "12", "label": "pilot cities", "note": "首波试点城市"},
            {"value": "72%", "label": "utilization", "note": "高峰时段车辆利用"},
        ],
        "bullets": [
            "先把封闭区域和固定路线跑顺，再扩大到开放路网。",
            "运营系统要同时解决调度、充电、清洁和安全事件闭环。",
            "软件收入开始与里程、活跃车次和城市密度直接相关。",
        ],
    },
    {
        "kind": "image-focus-energy",
        "section": "ENERGY",
        "page": 5,
        "number": 4,
        "title": "储能业务负责把增长波动磨平",
        "lede": "Mock 逻辑：储能给 Tesla 带来的不是更性感的叙事，而是更可预测的交付节奏与更厚的项目储备。",
        "image": "mock-tesla-energy.png",
        "caption": "Mock visual · Megapack 项目交付版图",
        "metrics": [
            {"value": "438GWh", "label": "booked pipeline", "note": "在手项目储备"},
            {"value": "31%", "label": "gross margin", "note": "项目组合口径"},
        ],
        "bullets": [
            "储能订单周期长，但一旦排产稳定，现金流的可见度远高于整车业务。",
            "电池分配不再只是车与车之间的竞争，而是车与电网项目之间的配置问题。",
            "投资者会开始用项目完工率，而不只是交车数，来判断季度表现。",
        ],
    },
    {
        "kind": "image-focus-optimus",
        "section": "ROBOTICS",
        "page": 6,
        "number": 5,
        "title": "Optimus 先证明工厂价值，再讲外部市场",
        "lede": "Mock 逻辑：机器人最先成立的场景不是家庭，而是 Tesla 自己的搬运、分拣、巡检和夜班替代。",
        "image": "mock-tesla-optimus.png",
        "caption": "Mock visual · Optimus 在厂内搬运与巡检",
        "metrics": [
            {"value": "18k", "label": "internal units", "note": "厂内部署节拍"},
            {"value": "23%", "label": "labor hours", "note": "重复工时替代"},
        ],
        "bullets": [
            "第一阶段看单位替代工时，而不是对外销量。",
            "机器人能力演进会反过来倒逼工厂物料标准化与工站重构。",
            "只有先在自家场景跑通，外部客户才会把它视为工业设备而不是演示品。",
        ],
    },
    {
        "kind": "templates",
        "section": "CHECKPOINTS",
        "page": 7,
        "number": 6,
        "title": "未来 18 个月看这五个检查点",
        "lede": "如果这五个点依次兑现，Tesla 的叙事会从单一汽车股，切换到多业务平台公司。",
        "cards": [
            {"label": "Q3", "title": "Factory Switch", "body": "新平台切线期间的良率、库存与现金转换。"},
            {"label": "Q4", "title": "Robotaxi Pilot", "body": "首批城市能否跑出稳定运营天数与乘客复购。"},
            {"label": "Q1", "title": "Megapack Throughput", "body": "储能交付是否形成季度级稳定节拍。"},
            {"label": "Q2", "title": "Optimus Internal Use", "body": "厂内替代工时是否可量化并形成标准方案。"},
            {"label": "Q2", "title": "AI Cost Curve", "body": "算力投入是否沉淀成更高的软件附加值。"},
        ],
    },
    {
        "kind": "end",
        "section": "END",
        "page": 8,
        "title": "先看兑现节奏，再看叙事想象力",
        "body": "Mock 数据 · Mock 图片 · Manuscript 版式 · PPTX / Slidev 双交付",
        "meta": "Tesla 2027 Mock Briefing · Generated with Kami",
    },
]


DECK_BY_KIND: dict[str, dict[str, Any]] = {slide["kind"]: slide for slide in DECK}
