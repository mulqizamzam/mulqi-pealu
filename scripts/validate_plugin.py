#!/usr/bin/env python3
"""Validate DSH bundle metadata, Skill frontmatter and safe package paths."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path, PurePosixPath

REQUIRED = ["package.json", "cordis.patch.yml", "index.js", "icon.svg", "README.md", "LICENSE"]

def validate(root: Path) -> dict:
    root = root.resolve()
    errors, warnings, manifest = [], [], {}
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"missing required file: {name}")
    try:
        manifest = json.loads((root / "package.json").read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid package.json: {exc}")
    if manifest:
        if manifest.get("version") != "0.2.1-rc.2":
            errors.append("package version must equal target 0.2.1-rc.2")
        if manifest.get("engines", {}).get("dsh") != ">=0.2.1-rc.2 <0.3.0":
            errors.append("engines.dsh must target >=0.2.1-rc.2 <0.3.0")
        if manifest.get("dsh", {}).get("bundle", {}).get("patch") != "./cordis.patch.yml":
            errors.append("dsh.bundle.patch must reference ./cordis.patch.yml")
        if manifest.get("exports", {}).get(".") != "./index.js":
            errors.append("main export must be ./index.js")
    patch_path = root / "cordis.patch.yml"
    patch = patch_path.read_text(encoding="utf-8") if patch_path.exists() else ""
    if "mulqi-pealu-autopilot" not in patch or "@mulqizamzam/mulqi-pealu" not in patch:
        errors.append("bundle patch must insert expected plugin row")

    skill_files = sorted((root / "skills").glob("*/SKILL.md")) if (root / "skills").exists() else []
    skill_dirs = [path.parent.name for path in skill_files]
    if len(skill_dirs) != 9:
        errors.append(f"expected 9 top-level Skills, found {len(skill_dirs)}")
    if len(set(skill_dirs)) != len(skill_dirs):
        errors.append("duplicate Skill directory")
    skill_names = []
    for path in skill_files:
        content = path.read_text(encoding="utf-8")
        if not content.startswith("---\n") or "\nname:" not in content or "\ndescription:" not in content:
            errors.append(f"invalid Skill frontmatter: {path.relative_to(root)}")
        match = re.search(r"^name:\s*(.+?)\s*$", content, re.M)
        if match:
            skill_names.append(match.group(1).strip().strip("'\""))
    if len(set(skill_names)) != len(skill_names):
        errors.append("duplicate Skill name")

    for path in root.rglob("*"):
        rel = path.relative_to(root).as_posix()
        if any(part in {"__pycache__", ".git", "dist", "build", "venv", ".venv", "node_modules"} for part in path.parts):
            continue
        if path.is_symlink():
            errors.append(f"symlink not allowed: {rel}")
        if path.suffix in {".pyc", ".pyo"}:
            errors.append(f"transient bytecode: {rel}")
        if PurePosixPath(rel).is_absolute() or ".." in PurePosixPath(rel).parts:
            errors.append(f"unsafe path: {rel}")
        if path.is_file() and path.suffix.lower() in {".pem", ".key"}:
            errors.append(f"potential private-key file: {rel}")
    try:
        icon = (root / "icon.svg").read_text(encoding="utf-8")
        if "<svg" not in icon or "viewBox=" not in icon:
            errors.append("icon.svg must be SVG with viewBox")
        if re.search(r"https?://(?!www\.w3\.org/2000/svg)", icon):
            errors.append("icon.svg must not contain remote resources")
    except Exception:
        pass
    return {"ok": not errors, "name": manifest.get("name"), "version": manifest.get("version"),
            "skills": skill_dirs, "errors": errors, "warnings": warnings}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?", default=Path("."))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = validate(args.root)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["ok"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
