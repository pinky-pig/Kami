from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

THEME_BUILD_SCRIPTS = {
    "republican-manuscript": ROOT / "plugins" / "republican-themes" / "skills" / "republican-manuscript" / "scripts" / "build.py",
    "sketch": ROOT / "plugins" / "design-themes" / "skills" / "sketch" / "scripts" / "build.py",
}

THEME_SLIDEV_PACKAGES = {
    "republican-manuscript": ROOT / "plugins" / "republican-themes" / "skills" / "republican-manuscript" / "assets" / "templates" / "slidev" / "package.json",
    "sketch": ROOT / "plugins" / "design-themes" / "skills" / "sketch" / "assets" / "templates" / "slidev" / "package.json",
}


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module for {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class SlideOutputContractTests(unittest.TestCase):
    def test_slides_primary_outputs_land_in_demos(self) -> None:
        for theme_name, script_path in THEME_BUILD_SCRIPTS.items():
            with self.subTest(theme=theme_name):
                module = load_module(theme_name.replace("-", "_"), script_path)
                self.assertEqual(
                    module.slide_pptx_output("slides"),
                    module.ROOT / "assets" / "demos" / "demo-slides.pptx",
                )
                self.assertEqual(
                    module.slide_online_output("slides"),
                    module.ROOT / "assets" / "demos" / "slides-online",
                )

    def test_slidev_preview_helpers_are_written_inside_output_dir(self) -> None:
        for theme_name, script_path in THEME_BUILD_SCRIPTS.items():
            with self.subTest(theme=theme_name):
                module = load_module(theme_name.replace("-", "_"), script_path)
                with tempfile.TemporaryDirectory() as tmpdir:
                    out_dir = Path(tmpdir) / "slides-online"
                    out_dir.mkdir(parents=True, exist_ok=True)
                    helper = module.write_slidev_preview_helper(out_dir)
                    launcher = module.write_slidev_preview_command(helper)
                    self.assertEqual(helper.parent, out_dir)
                    self.assertEqual(launcher.parent, out_dir)
                    self.assertEqual(helper.name, "slides-online-preview.py")
                    self.assertEqual(launcher.name, "slides-online-preview.command")

    def test_slidev_build_script_targets_demos_output_dir(self) -> None:
        for theme_name, package_path in THEME_SLIDEV_PACKAGES.items():
            with self.subTest(theme=theme_name):
                package = json.loads(package_path.read_text(encoding="utf-8"))
                self.assertIn("build", package["scripts"])
                self.assertIn("../../demos/slides-online", package["scripts"]["build"])


if __name__ == "__main__":
    unittest.main()
