#!/usr/bin/env python3
"""Inspect ZIP entries for path traversal, symlinks and duplicate names."""
from __future__ import annotations
import argparse,json,stat,zipfile
from pathlib import Path,PurePosixPath
def inspect(path:Path)->dict:
 err=[];seen=set();items=[]
 try:
  with zipfile.ZipFile(path) as z:
   for inf in z.infolist():
    n=inf.filename;p=PurePosixPath(n)
    if n in seen:err.append(f"duplicate entry: {n}")
    seen.add(n)
    if p.is_absolute() or ".." in p.parts or "\\" in n:err.append(f"unsafe path: {n}")
    if stat.S_ISLNK(inf.external_attr>>16):err.append(f"symlink entry: {n}")
    if n.startswith("/") or (p.parts and p.parts[0].endswith(":")):err.append(f"absolute path: {n}")
    items.append(n)
 except Exception as e:err.append(f"cannot inspect ZIP: {e}")
 return {"ok":not err,"archive":str(path),"entry_count":len(items),"entries":items,"errors":err}
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("archive",type=Path);ap.add_argument("--json",action="store_true");a=ap.parse_args();r=inspect(a.archive);print(json.dumps(r,indent=2,ensure_ascii=False));return 0 if r["ok"] else 1
if __name__=="__main__":raise SystemExit(main())
