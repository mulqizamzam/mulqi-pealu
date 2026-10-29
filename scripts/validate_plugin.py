#!/usr/bin/env python3
"""Validate the DSH bundle structure and basic safe-path properties."""
from __future__ import annotations
import argparse,json,re
from pathlib import Path,PurePosixPath
REQUIRED=["package.json","cordis.patch.yml","index.js","icon.svg","README.md","LICENSE"]
def validate(root:Path)->dict:
 root=root.resolve();errors=[];warnings=[];manifest={}
 for name in REQUIRED:
  if not (root/name).is_file():errors.append(f"missing required file: {name}")
 try:manifest=json.loads((root/"package.json").read_text(encoding="utf-8"))
 except Exception as e:errors.append(f"invalid package.json: {e}")
 if manifest:
  if manifest.get("version")!="0.2.1-rc.2":errors.append("package version must equal target 0.2.1-rc.2")
  if manifest.get("engines",{}).get("dsh")!=">=0.2.1-rc.2 <0.3.0":errors.append("engines.dsh must target >=0.2.1-rc.2 <0.3.0")
  if manifest.get("dsh",{}).get("bundle",{}).get("patch")!="./cordis.patch.yml":errors.append("dsh.bundle.patch must reference ./cordis.patch.yml")
  if manifest.get("exports",{}).get(".")!="./index.js":errors.append("main export must be ./index.js")
 patch=(root/"cordis.patch.yml").read_text(encoding="utf-8") if (root/"cordis.patch.yml").exists() else ""
 if "mulqi-pealu-autopilot" not in patch or "@mulqizamzam/mulqi-pealu" not in patch:errors.append("bundle patch must insert expected plugin row")
 skill_files=sorted((root/"skills").glob("*/SKILL.md")) if (root/"skills").exists() else [];skill_dirs=[p.parent.name for p in skill_files]
 if len(skill_dirs)!=9:errors.append(f"expected 9 top-level Skills, found {len(skill_dirs)}")
 if len(set(skill_dirs))!=len(skill_dirs):errors.append("duplicate Skill directory")
 names=[]
 for p in skill_files:
  c=p.read_text(encoding="utf-8")
  if not c.startswith("---\n") or "\nname:" not in c or "\ndescription:" not in c:errors.append(f"invalid frontmatter: {p.relative_to(root)}")
  m=re.search(r"^name:\s*(.+?)\s*$",c,re.M)
  if m:names.append(m.group(1).strip().strip("'\""))
 if len(set(names))!=len(names):errors.append("duplicate Skill name")
 for p in root.rglob("*"):
  rel=p.relative_to(root).as_posix()
  if p.is_symlink():errors.append(f"symlink not allowed: {rel}")
  if "__pycache__" in p.parts or p.suffix in {".pyc",".pyo"}:errors.append(f"transient bytecode: {rel}")
  if PurePosixPath(rel).is_absolute() or ".." in PurePosixPath(rel).parts:errors.append(f"unsafe path: {rel}")
  if p.is_file() and p.suffix.lower() in {".pem",".key"}:errors.append(f"potential private-key file: {rel}")
 try:
  icon=(root/"icon.svg").read_text(encoding="utf-8")
  if "<svg" not in icon or "viewBox=" not in icon:errors.append("icon.svg must be SVG with viewBox")
  if re.search(r"https?://(?!www\.w3\.org/2000/svg)",icon):errors.append("icon.svg must not contain remote resources")
 except Exception:pass
 return {"ok":not errors,"name":manifest.get("name"),"version":manifest.get("version"),"skills":skill_dirs,"errors":errors,"warnings":warnings}
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("root",type=Path,nargs="?",default=Path("."));ap.add_argument("--json",action="store_true");a=ap.parse_args();r=validate(a.root);print(json.dumps(r,indent=2,ensure_ascii=False));return 0 if r["ok"] else 1
if __name__=="__main__":raise SystemExit(main())
