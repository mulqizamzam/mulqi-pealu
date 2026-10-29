#!/usr/bin/env python3
"""Create a deterministic ZIP archive plus SHA-256 checksum file."""
from __future__ import annotations
import argparse,hashlib,json,stat,zipfile
from pathlib import Path
EXCLUDES={".git","__pycache__","node_modules","dist","build",".venv","venv"}
def build(root:Path,out:Path)->dict:
 root=root.resolve();out=out.resolve();out.parent.mkdir(parents=True,exist_ok=True);entries=[]
 for p in sorted(root.rglob("*")):
  if not p.is_file() or p.is_symlink():continue
  rel=p.relative_to(root)
  if any(part in EXCLUDES for part in rel.parts) or p.suffix in {".pyc",".pyo"}:continue
  if p==out or out in p.parents:continue
  entries.append((p,rel.as_posix()))
 with zipfile.ZipFile(out,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p,rel in entries:
   info=zipfile.ZipInfo(rel,date_time=(2020,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=(stat.S_IFREG|0o644)<<16;info.create_system=3;z.writestr(info,p.read_bytes())
 digest=hashlib.sha256(out.read_bytes()).hexdigest();sums=out.parent/"SHA256SUMS";sums.write_text(f"{digest}  {out.name}\n",encoding="utf-8")
 return {"ok":True,"archive":str(out),"sha256":digest,"bytes":out.stat().st_size,"entries":len(entries),"checksums":str(sums)}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument("root",type=Path,nargs="?",default=Path("."));p.add_argument("--out",type=Path,default=Path("dist"));a=p.parse_args();out=a.out
 if out.exists() and out.is_dir():out=out/"mulqi-pealu-0.2.1-rc.2.zip"
 elif out.suffix.lower()!=".zip":out=out/"mulqi-pealu-0.2.1-rc.2.zip"
 print(json.dumps(build(a.root,out),indent=2,ensure_ascii=False))
if __name__=="__main__":main()
