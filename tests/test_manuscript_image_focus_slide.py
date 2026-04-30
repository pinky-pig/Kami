from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SLIDEV_RENDER = ROOT / "plugins" / "republican-themes" / "skills" / "republican-manuscript" / "assets" / "templates" / "slidev" / "render_from_spec.py"
PPT_RENDER = ROOT / "plugins" / "republican-themes" / "skills" / "republican-manuscript" / "assets" / "templates" / "slides.py"
SLIDEV_STYLE = ROOT / "plugins" / "republican-themes" / "skills" / "republican-manuscript" / "assets" / "templates" / "slidev" / "style.css"
MOCK_DEMOS = ROOT / "plugins" / "republican-themes" / "skills" / "republican-manuscript" / "scripts" / "generate_mock_demos.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module for {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    sys.path.insert(0, str(path.parent))
    spec.loader.exec_module(module)
    return module


class ManuscriptImageFocusSlideTests(unittest.TestCase):
    def test_slidev_renderer_supports_image_focus_slide(self) -> None:
        module = load_module("manuscript_render_from_spec", SLIDEV_RENDER)
        slide = {
            "kind": "image-focus",
            "section": "OPERATIONS",
            "page": 3,
            "number": 2,
            "title": "Mock Tesla 工厂扩产",
            "lede": "图片型 slide 需要真实图片路径。",
            "image": "mock-tesla-factory.png",
            "caption": "Mock visual",
            "metrics": [
                {"value": "12", "label": "产线", "note": "双班倒"},
                {"value": "48h", "label": "周转", "note": "从冲压到总装"},
            ],
            "bullets": ["工厂一体化布局", "供应链缓冲带前移", "为 Robotaxi 预留产能"],
        }
        html = module.render_image_focus(slide)
        self.assertIn("../../demos/mock-assets/mock-tesla-factory.png", html)
        self.assertIn("image-focus-visual", html)
        self.assertIn("Mock Tesla 工厂扩产", html)

    def test_slidev_renderer_falls_back_to_placeholder_when_image_is_missing(self) -> None:
        module = load_module("manuscript_render_from_spec_placeholder", SLIDEV_RENDER)
        slide = {
            "kind": "image-focus",
            "section": "OPERATIONS",
            "page": 3,
            "number": 2,
            "title": "Factory OS",
            "lede": "没有真实图片时，也要稳定产出模板。",
            "diagram": "quadrant",
            "visual_title": "优先使用现有 diagrams",
            "visual_note": "优先嵌入 assets/diagrams/quadrant.html 的 SVG；没有图就继续保留纯色占位。",
            "caption": "unused",
            "metrics": [
                {"value": "12", "label": "产线", "note": "双班倒"},
                {"value": "48h", "label": "周转", "note": "从冲压到总装"},
            ],
            "bullets": ["工厂一体化布局", "供应链缓冲带前移", "为 Robotaxi 预留产能"],
        }
        html = module.render_image_focus(slide)
        self.assertIn("image-focus-placeholder", html)
        self.assertIn("DIAGRAM SLOT", html)
        self.assertIn("assets/diagrams/quadrant.html", html)

    def test_ppt_renderer_resolves_demo_images_from_assets_demos(self) -> None:
        module = load_module("manuscript_slides", PPT_RENDER)
        self.assertEqual(
            module.asset_image_path("mock-tesla-factory.png"),
            module.Path(module.__file__).resolve().parent.parent / "demos" / "mock-assets" / "mock-tesla-factory.png",
        )

    def test_ppt_renderer_splits_display_and_body_east_asian_fonts(self) -> None:
        module = load_module("manuscript_slides_font_roles", PPT_RENDER)
        self.assertNotEqual(module.SERIF, module.SANS)
        self.assertEqual(module.latin_font(module.SERIF), "Newsreader")
        self.assertEqual(module.east_asian_font(module.SERIF), module.SERIF_EA)
        self.assertEqual(module.latin_font(module.SANS), "Newsreader")
        self.assertEqual(module.SANS_EA, "TsangerJinKai02-W04")
        self.assertEqual(module.east_asian_font(module.SANS), module.SANS_EA)

    def test_ppt_renderer_supports_placeholder_when_image_is_missing(self) -> None:
        module = load_module("manuscript_slides_placeholder", PPT_RENDER)
        slide = {
            "kind": "image-focus-placeholder",
            "section": "OPERATIONS",
            "page": 3,
            "number": 2,
            "title": "Factory OS",
            "lede": "没有真实图片时，也要稳定产出模板。",
            "diagram": "flowchart",
            "visual_title": "优先使用现有 diagrams",
            "visual_note": "优先嵌入 assets/diagrams/flowchart.html 的 SVG；没有图就继续保留纯色占位。",
            "metrics": [
                {"value": "12", "label": "产线", "note": "双班倒"},
                {"value": "48h", "label": "周转", "note": "从冲压到总装"},
            ],
            "bullets": ["工厂一体化布局", "供应链缓冲带前移", "为 Robotaxi 预留产能"],
        }
        module.DECK_BY_KIND[slide["kind"]] = slide
        prs = module.Presentation()
        prs.slide_width = module.SLIDE_W
        prs.slide_height = module.SLIDE_H
        module.slide_image_focus(prs, slide["kind"])
        self.assertEqual(len(prs.slides), 1)
        self.assertGreater(len(prs.slides[0].shapes), 0)

    def test_ppt_cover_uses_lower_centered_hero_offsets(self) -> None:
        module = load_module("manuscript_slides_cover", PPT_RENDER)
        self.assertEqual(module.COVER_PLAQUE_TOP, module.INNER_Y + module.Inches(1.78))
        self.assertEqual(module.COVER_COPY_TOP, module.INNER_Y + module.Inches(2.02))
        self.assertEqual(module.COVER_METRIC_TOP, module.INNER_Y + module.Inches(3.84))

    def test_slidev_cover_centers_main_block_with_auto_margins(self) -> None:
        text = SLIDEV_STYLE.read_text(encoding="utf-8")
        self.assertIn(".cover-main {", text)
        self.assertIn("margin-top: auto;", text)
        self.assertIn("margin-bottom: auto;", text)

    def test_mock_demo_generator_places_generated_images_under_demos(self) -> None:
        text = MOCK_DEMOS.read_text(encoding="utf-8")
        self.assertIn('DEMO_IMAGES = DEMOS / "mock-assets"', text)
        self.assertIn("def load_readable_font", text)
        self.assertIn('FONTS / "TsangerJinKai02-W04.ttf"', text)

    def test_mock_demo_generator_clears_long_doc_outputs(self) -> None:
        text = MOCK_DEMOS.read_text(encoding="utf-8")
        start = text.index("def clear_demo_outputs()")
        end = text.index("\ndef make_mock_scene(", start)
        clear_fn = text[start:end]
        self.assertIn('DEMOS / "demo-long-doc.html"', clear_fn)
        self.assertIn('DEMOS / "demo-long-doc.pdf"', clear_fn)
        self.assertIn('DEMOS / "demo-long-doc.png"', clear_fn)

    def test_mock_demo_generator_generates_long_doc_demo(self) -> None:
        text = MOCK_DEMOS.read_text(encoding="utf-8")
        self.assertIn("def generate_long_doc()", text)
        start = text.index("def generate_long_doc()")
        end = text.index("\ndef generate_resume()", start)
        long_doc_fn = text[start:end]
        self.assertIn('TEMPLATES / "long-doc.html"', long_doc_fn)
        self.assertIn('DEMOS / "demo-long-doc.html"', long_doc_fn)
        self.assertIn('DEMOS / "demo-long-doc.pdf"', long_doc_fn)
        self.assertIn('DEMOS / "demo-long-doc.png"', long_doc_fn)
        self.assertIn("Tesla", long_doc_fn)
        self.assertIn("generate_long_doc()", text[text.index("def main() -> None:"):])

    def test_mock_demo_generator_keeps_portfolio_placeholders_by_default(self) -> None:
        text = MOCK_DEMOS.read_text(encoding="utf-8")
        start = text.index("def generate_portfolio()")
        end = text.index("\ndef build_slides()", start)
        portfolio_fn = text[start:end]
        self.assertIn('TEMPLATES / "portfolio.html"', portfolio_fn)
        self.assertNotIn('<img src="./mock-assets/', portfolio_fn)
        self.assertNotIn("mock-tesla-robotaxi.png", portfolio_fn)
        self.assertNotIn("mock-tesla-factory.png", portfolio_fn)
        self.assertNotIn("mock-tesla-optimus.png", portfolio_fn)


if __name__ == "__main__":
    unittest.main()
