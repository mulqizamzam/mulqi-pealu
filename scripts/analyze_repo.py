#!/usr/bin/env python3
"""Dependency-free, read-only repository workflow analyzer."""
from __future__ import annotations
import argparse,json
from pathlib import Path
MARKERS={"SKILL.md","AGENTS.md","CLAUDE.md"}
HINTS=("workflow","playbook","prompt","agent","command","skill","eval","experiment","research")
IGNORE={".git","node_modules",".venv","venv","__pycache__","dist","build",".next"}
def analyze(root:Path)->dict:
 root=root.resolve()
 if not root.is_dir():return {"ok":False,"errors":[f"not a directory: {root}"],"root":str(root),"candidates":[]}
 cand=[];inv=[]
 for p in sorted(root.rglob("*")):
  if any(x in IGNORE for x in p.parts) or p.is_symlink() or p.is_dir():continue
  rel=p.relative_to(root).as_posix();inv.append(rel);score=2 if p.name in MARKERS else 0
  score+=sum(1 for h in HINTS if h in p.name.lower() or h in rel.lower())
  if p.name in {"package.json","pyproject.toml","requirements.txt","action.yml","action.yaml","plugin.json","cordis.patch.yml"}:score+=2
  if p.suffix.lower() in {".md",".yaml",".yml",".json",".toml",".py",".sh",".ts",".js"} and score:cand.append({"path":rel,"score":score,"reason":"workflow or runtime metadata signal"})
 cand.sort(key=lambda x:(-x["score"],x["path"]))
 return {"ok":True,"root":str(root),"files_scanned":len(inv),"architecture_recommendation":"skills-plus-local-helpers","candidates":cand,"inventory_summary":{"readmes":[p for p in inv if Path(p).name.lower().startswith("readme")][:100],"skill_files":[p for p in inv if Path(p).name=="SKILL.md"][:200],"agent_files":[p for p in inv if Path(p).name in {"AGENTS.md","CLAUDE.md"}][:200],"workflow_files":[p for p in inv if ".github/workflows/" in p][:100],"test_files":[p for p in inv if "test" in Path(p).name.lower()][:200]},"note":"Heuristic signals only; inspect context and public-distribution safety before conversion."}
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("repository",type=Path);ap.add_argument("--json",action="store_true");a=ap.parse_args();r=analyze(a.repository);print(json.dumps(r,indent=2,ensure_ascii=False));return 0 if r.get("ok") else 2
if __name__=="__main__":raise SystemExit(main())
