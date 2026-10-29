#!/usr/bin/env python3
"""Validate the DSH bundle structure and basic safe-path properties."""
from __future__ import annotations
import argparse,json,re
from pathlib import Path,PurePosixPath
REQUIRED=["package.json","cordis.patch.yml","index.js","icon.svg","README.md","LICENSE"]
def validate(root:Path)->dict:
 root=root.resolve();err=[];warn=[];m={}
 for n in REQUIRED:
  if not (root/n).is_file():err.append(f"missing required file: {n}")
 try:m=json.loads((root/"package.json").read_text(encoding="utf-8"))
 except Exception as e:err.append(f"invalid package.json: {e}")
 if m:
  if m.get("version")!="0.2.1-rc.2":err.append("package version must equal target 0.2.1-rc.2")
  if m.get("engines",{}).get("dsh")!=">=0.2.1-rc.2 <0.3.0":err.append("engines.dsh must target >=0.2.1-rc.2 <0.3.0")
  if m.get("dsh",{}).get("bundle",{}).get("patch")!="./cordis.patch.yml":err.append("dsh.bundle.patch must reference ./cordis.patch.yml")
  if m.get("exports",{}).get(".")!="./index.js":err.append("main export must be ./index.js")
 patch=(root/"cordis.patch.yml").read_text(encoding="utf-8") if (root/"cordis.patch.yml").exists() else ""
 if "mulqi-pealu-autopilot" not in patch or "@mulqizamzam/mulqi-pealu" not in patch:err.append("bundle patch must insert expected plugin row")
 fs=sorted((root/"skills").glob("*/SKILL.md")) if (root/"skills").exists() else [];dirs=[p.parent.name for p in fs]
 if len(dirs)!=9:err.append(f"expected 9 top-level Skills, found {len(dirs)}")
 if len(set(dirs))!=len(dirs):err.append("duplicate Skill directory")
 names=[]
 for p in fs:
  c=p.read_text(encoding="utf-8")
  if not c.startswith("---\n") or "\nname:" not in c or "\ndescription:" not in c:err.append(f"invalid frontmatter: {p.relative_to(root)}")
  hit=re.search(r"^name:\s*(.+?)\s*$",c,re.M)
  if hit:names.append(hit.group(1).strip().strip("'\""))
 if len(set(names))!=len(names):err.append("duplicate Skill name")
 for p in root.rglob("*"):
  rel=p.relative_to(root).as_posix()
  if p.is_symlink():err.append(f"symlink not allowed: {rel}")
  if "__pycache__" in p.parts or p.suffix in {".pyc",".pyo"}:err.append(f"transient bytecode: {rel}")
  if PurePosixPath(rel).is_absolute() or ".." in PurePosixPath(rel).parts:err.append(f"unsafe path: {rel}")
  if p.is_file() and p.suffix.lower() in {".pem",".key"}:err.append(f"potential private-key file: {rel}")
 try:
  icon=(root/"icon.svg").read_text(encoding="utf-8")
  if "<svg" not in icon or "viewBox=" not in icon:err.append("icon.svg must be SVG with viewBox")
  if re.search(r"https?://(?!www\.w3\.org/2000/svg)",icon):err.append("icon.svg must not contain remote resources")
 except Exception:pass
 return {"ok":not err,"name":m.get("name"),"version":m.get("version"),"skills":dirs,"errors":err,"warnings":warn}
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("root",type=Path,nargs="?",default=Path("."));ap.add_argument("--json",action="store_true");a=ap.parse_args();r=validate(a.root);print(json.dumps(r,indent=2,ensure_ascii=False));return 0 if r["ok"] else 1
if __name__=="__main__":raise SystemExit(main())
