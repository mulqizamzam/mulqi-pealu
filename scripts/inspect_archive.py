#!/usr/bin/env python3
"""Inspect ZIP entries for path traversal, symlinks and duplicate names."""
from __future__ import annotations
import argparse,json,stat,zipfile
from pathlib import Path,PurePosixPath
def inspect(path:Path)->dict:
 errors=[];seen=set();entries=[]
 try:
  with zipfile.ZipFile(path) as z:
   for info in z.infolist():
    name=info.filename;pure=PurePosixPath(name)
    if name in seen:errors.append(f"duplicate entry: {name}")
    seen.add(name)
    if pure.is_absolute() or ".." in pure.parts or "\\" in name:errors.append(f"unsafe path: {name}")
    if stat.S_ISLNK(info.external_attr>>16):errors.append(f"symlink entry: {name}")
    if name.startswith("/") or (pure.parts and pure.parts[0].endswith(":")):errors.append(f"absolute path: {name}")
    entries.append(name)
 except Exception as e:errors.append(f"cannot inspect ZIP: {e}")
 return {"ok":not errors,"archive":str(path),"entry_count":len(entries),"entries":entries,"errors":errors}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument("archive",type=Path);p.add_argument("--json",action="store_true");a=p.parse_args();r=inspect(a.archive);print(json.dumps(r,indent=2,ensure_ascii=False));return 0 if r["ok"] else 1
if __name__=="__main__":raise SystemExit(main())
