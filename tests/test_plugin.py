import json, tempfile, unittest, zipfile
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from analyze_repo import analyze
from validate_plugin import validate
from package_plugin import build
from inspect_archive import inspect
ROOT = Path(__file__).resolve().parents[1]

class PluginTests(unittest.TestCase):
    def test_manifest_targets_dsh(self):
        manifest = json.loads((ROOT / "package.json").read_text())
        self.assertEqual(manifest["version"], "0.2.1-rc.2")
        self.assertEqual(manifest["engines"]["dsh"], ">=0.2.1-rc.2 <0.3.0")

    def test_validator_passes(self):
        report = validate(ROOT)
        self.assertTrue(report["ok"], report["errors"])

    def test_nine_skills(self):
        self.assertEqual(len(list((ROOT / "skills").glob("*/SKILL.md"))), 9)

    def test_skill_frontmatter_names_are_unique(self):
        from validate_plugin import validate
        report = validate(ROOT)
        self.assertEqual(report["skills"], sorted(report["skills"]))

    def test_analyzer_missing_path(self):
        self.assertFalse(analyze(ROOT / "missing-test-directory")["ok"])

    def test_analyzer_current_repo(self):
        report = analyze(ROOT)
        self.assertTrue(report["ok"])
        self.assertGreater(report["files_scanned"], 0)

    def test_deterministic_package(self):
        with tempfile.TemporaryDirectory() as directory:
            first, second = Path(directory) / "first.zip", Path(directory) / "second.zip"
            build(ROOT, first)
            build(ROOT, second)
            self.assertEqual(first.read_bytes(), second.read_bytes())

    def test_archive_inspection(self):
        with tempfile.TemporaryDirectory() as directory:
            archive = Path(directory) / "ok.zip"
            with zipfile.ZipFile(archive, "w") as zf:
                zf.writestr("hello.txt", "ok")
            self.assertTrue(inspect(archive)["ok"])

    def test_archive_traversal_detection(self):
        with tempfile.TemporaryDirectory() as directory:
            archive = Path(directory) / "bad.zip"
            with zipfile.ZipFile(archive, "w") as zf:
                zf.writestr("../escape.txt", "bad")
            self.assertFalse(inspect(archive)["ok"])

if __name__ == "__main__":
    unittest.main()
