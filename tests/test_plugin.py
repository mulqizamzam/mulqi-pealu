import json,tempfile,unittest,zipfile
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from analyze_repo import analyze
from validate_plugin import validate
from package_plugin import build
from inspect_archive import inspect
ROOT=Path(__file__).resolve().parents[1]
class PluginTests(unittest.TestCase):
 def test_manifest_targets_dsh(self):
  m=json.loads((ROOT/"package.json").read_text());self.assertEqual(m["version"],"0.2.1-rc.2");self.assertEqual(m["engines"]["dsh"],">=0.2.1-rc.2 <0.3.0")
 def test_validator_passes(self):
  r=validate(ROOT);self.assertTrue(r["ok"],r["errors"])
 def test_nine_skills(self):self.assertEqual(len(list((ROOT/"skills").glob("*/SKILL.md"))),9)
 def test_analyzer_missing_path(self):self.assertFalse(analyze(ROOT/"missing-test-directory")["ok"])
 def test_analyzer_current_repo(self):
  r=analyze(ROOT);self.assertTrue(r["ok"]);self.assertGreater(r["files_scanned"],0)
 def test_deterministic_package(self):
  with tempfile.TemporaryDirectory() as d:
   a=Path(d)/"a.zip";b=Path(d)/"b.zip";build(ROOT,a);build(ROOT,b);self.assertEqual(a.read_bytes(),b.read_bytes())
 def test_archive_inspection(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"ok.zip"
   with zipfile.ZipFile(p,"w") as z:z.writestr("hello.txt","ok")
   self.assertTrue(inspect(p)["ok"])
 def test_archive_traversal_detection(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"bad.zip"
   with zipfile.ZipFile(p,"w") as z:z.writestr("../escape.txt","bad")
   self.assertFalse(inspect(p)["ok"])
if __name__=="__main__":unittest.main()
