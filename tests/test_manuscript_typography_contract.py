from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "plugins" / "republican-themes" / "skills" / "republican-manuscript" / "assets" / "templates"
SLIDEV_STYLE = TEMPLATES / "slidev" / "style.css"
BUILD_SCRIPT = ROOT / "plugins" / "republican-themes" / "skills" / "republican-manuscript" / "scripts" / "build.py"
DIAGRAMS = ROOT / "plugins" / "republican-themes" / "skills" / "republican-manuscript" / "assets" / "diagrams"


class ManuscriptTypographyContractTests(unittest.TestCase):
    def test_core_chinese_templates_define_tsanger_readable_font(self) -> None:
        for name in ("one-pager.html", "letter.html", "long-doc.html"):
            with self.subTest(template=name):
                text = (TEMPLATES / name).read_text(encoding="utf-8")
                self.assertIn('font-family: "TsangerReadableCn";', text)
                self.assertIn('--reading-text: "TsangerReadableCn", "Newsreader"', text)

    def test_resume_template_uses_display_and_ui_font_split(self) -> None:
        text = (TEMPLATES / "resume.html").read_text(encoding="utf-8")
        self.assertIn('font-family: "KamiDisplayCn";', text)
        self.assertIn('font-family: "TsangerReadableCn";', text)
        self.assertIn("unicode-range:", text)
        self.assertIn('--display-serif: "KamiDisplayCn", "Newsreader"', text)
        self.assertIn('--ui-sans: "TsangerReadableCn", "Newsreader"', text)
        self.assertIn("font-family: var(--ui-sans);", text)

    def test_long_doc_template_uses_kinghwa_for_large_display_titles(self) -> None:
        text = (TEMPLATES / "long-doc.html").read_text(encoding="utf-8")
        kinghwa_stack = 'font-family: "KingHwa_OldSong", "Source Han Serif SC", "Noto Serif CJK SC", "Songti SC", serif;'
        self.assertGreaterEqual(text.count(kinghwa_stack), 4)

    def test_portfolio_template_uses_readable_body_stack(self) -> None:
        text = (TEMPLATES / "portfolio.html").read_text(encoding="utf-8")
        self.assertIn('font-family: "KamiDisplayCn";', text)
        self.assertIn('font-family: "TsangerReadableCn";', text)
        self.assertIn('--body-serif: "TsangerReadableCn", "Newsreader"', text)
        self.assertIn("font-family: var(--body-serif);", text)
        self.assertIn("font-family: var(--display-serif);", text)
        self.assertNotIn("font-family: var(--ui-sans);", text)

    def test_slidev_titles_use_cjk_scoped_display_font(self) -> None:
        text = SLIDEV_STYLE.read_text(encoding="utf-8")
        self.assertIn('font-family: "KamiDisplayCn";', text)
        self.assertIn('font-family: "KamiTsanger";', text)
        self.assertIn('font-family: "KamiDisplayCn", "KamiNewsreader", serif;', text)

    def test_english_templates_drop_inter_and_keep_newsreader_stack(self) -> None:
        for name in ("one-pager-en.html", "letter-en.html", "long-doc-en.html", "portfolio-en.html", "resume-en.html"):
            with self.subTest(template=name):
                text = (TEMPLATES / name).read_text(encoding="utf-8")
                self.assertNotIn("Inter.woff2", text)
                self.assertNotIn('font-family: "Inter"', text)
                self.assertIn('--sans:  "Newsreader"', text)

    def test_build_verify_treats_newsreader_as_only_primary_english_font(self) -> None:
        text = BUILD_SCRIPT.read_text(encoding="utf-8")
        self.assertIn('EN_PRIMARY_FONTS = {"Newsreader"}', text)

    def test_build_verify_recognizes_tsanger_as_primary_chinese_font(self) -> None:
        text = BUILD_SCRIPT.read_text(encoding="utf-8")
        self.assertIn('"KingHwa_OldSong"', text)
        self.assertIn('"KamiDisplayCn"', text)
        self.assertIn('"TsangerJinKai02-W04"', text)
        self.assertIn('"TsangerReadableCn"', text)
        self.assertIn('"Tsanger"', text)

    def test_build_verify_prefers_filled_demo_sources_for_resume_and_portfolio(self) -> None:
        text = BUILD_SCRIPT.read_text(encoding="utf-8")
        self.assertIn('"resume": ("demo-resume.html", ROOT / "assets" / "demos")', text)
        self.assertIn('"portfolio": ("demo-portfolio.html", ROOT / "assets" / "demos")', text)

    def test_diagram_templates_drop_inter_stack(self) -> None:
        for name in ("architecture.html", "flowchart.html", "quadrant.html"):
            with self.subTest(template=name):
                text = (DIAGRAMS / name).read_text(encoding="utf-8")
                self.assertNotIn("Inter", text)
                self.assertIn("Newsreader", text)


if __name__ == "__main__":
    unittest.main()
