from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "plugins" / "republican-themes" / "skills" / "republican-manuscript" / "assets" / "templates"


class ManuscriptTemplatePreviewContractTests(unittest.TestCase):
    def test_resume_template_keeps_long_doc_page_chrome(self) -> None:
        text = (TEMPLATES / "resume.html").read_text(encoding="utf-8")
        self.assertIn("@page {", text)
        self.assertIn("margin: 0;", text)
        self.assertIn("background: #243851;", text)
        self.assertIn(".topline {", text)
        self.assertIn(".blue-tag {", text)
        self.assertIn(".page-no {", text)
        self.assertIn("KAMI DOC ·", text)

    def test_resume_template_increases_content_padding_beyond_frame_lines(self) -> None:
        text = (TEMPLATES / "resume.html").read_text(encoding="utf-8")
        self.assertIn("padding: 7.5mm 10mm 6.5mm;", text)
        self.assertIn("inset: 3.2mm;", text)
        self.assertIn("inset: 5.5mm;", text)
        self.assertIn("top: 3.2mm;", text)
        self.assertIn("right: 3.2mm;", text)
        self.assertIn("bottom: 3.2mm;", text)
        self.assertIn("left: 3.2mm;", text)
        self.assertIn("top: 5.5mm;", text)
        self.assertIn("right: 5.5mm;", text)
        self.assertIn("bottom: 5.5mm;", text)
        self.assertIn("left: 5.5mm;", text)

    def test_portfolio_template_keeps_placeholder_visual_slots(self) -> None:
        text = (TEMPLATES / "portfolio.html").read_text(encoding="utf-8")
        self.assertIn(".project-hero {", text)
        self.assertIn(".project-visuals-2col {", text)
        self.assertIn(".project-results {", text)
        self.assertIn("[项目主图占位", text)
        self.assertIn("[左图]", text)
        self.assertIn("[右图]", text)

    def test_portfolio_outer_container_keeps_one_pager_style_inner_frame_lines(self) -> None:
        text = (TEMPLATES / "portfolio.html").read_text(encoding="utf-8")
        self.assertIn("width: calc(210mm - (var(--frame-gap) * 2));", text)
        self.assertIn("margin: var(--frame-gap) auto 0;", text)
        self.assertIn("background: var(--frame-blue);", text)
        self.assertIn(".cover::before,", text)
        self.assertIn("section.about::before,", text)
        self.assertIn("section.project::before,", text)
        self.assertIn(".cover::after,", text)
        self.assertIn("section.contact::after {", text)
        self.assertIn("border: 1pt solid var(--frame-blue);", text)
        self.assertIn("border: 0.45pt solid var(--blue-soft);", text)
        self.assertIn("top: 6mm;", text)
        self.assertIn("right: 6mm;", text)
        self.assertIn("bottom: 6mm;", text)
        self.assertIn("left: 6mm;", text)
        self.assertIn("top: 8.5mm;", text)
        self.assertIn("right: 8.5mm;", text)
        self.assertIn("bottom: 8.5mm;", text)
        self.assertIn("left: 8.5mm;", text)

    def test_long_doc_template_keeps_smaller_outer_blue_frame_with_visible_inner_lines(self) -> None:
        text = (TEMPLATES / "long-doc.html").read_text(encoding="utf-8")
        self.assertIn(".folio {", text)
        self.assertIn("padding: 7mm;", text)
        self.assertIn("min-height: 283mm;", text)
        self.assertIn("top: 4.5mm;", text)
        self.assertIn("right: 4.5mm;", text)
        self.assertIn("bottom: 4.5mm;", text)
        self.assertIn("left: 4.5mm;", text)
        self.assertIn("top: 7.1mm;", text)
        self.assertIn("right: 7.1mm;", text)
        self.assertIn("bottom: 7.1mm;", text)
        self.assertIn("left: 7.1mm;", text)
        self.assertIn("border: 1.05pt solid var(--frame-blue);", text)
        self.assertIn("border: 0.55pt solid var(--blue-soft);", text)

    def test_long_doc_cover_keeps_main_block_vertically_centered(self) -> None:
        text = (TEMPLATES / "long-doc.html").read_text(encoding="utf-8")
        self.assertIn(".cover {", text)
        self.assertIn(".cover > .content:first-child {", text)
        self.assertIn("display: flex;", text)
        self.assertIn("flex-direction: column;", text)
        self.assertIn("flex: 1;", text)
        self.assertIn("margin-top: auto;", text)
        self.assertIn("margin-bottom: auto;", text)

    def test_resume_and_portfolio_docs_state_long_doc_is_the_reference(self) -> None:
        skill = (ROOT / "plugins" / "republican-themes" / "skills" / "republican-manuscript" / "SKILL.md").read_text(encoding="utf-8")
        cheatsheet = (ROOT / "plugins" / "republican-themes" / "skills" / "republican-manuscript" / "CHEATSHEET.md").read_text(encoding="utf-8")
        readme = (ROOT / "plugins" / "republican-themes" / "skills" / "republican-manuscript" / "README.md").read_text(encoding="utf-8")
        for text in (skill, cheatsheet, readme):
            self.assertIn("resume / portfolio", text)
            self.assertIn("demo-long-doc.html", text)


if __name__ == "__main__":
    unittest.main()
