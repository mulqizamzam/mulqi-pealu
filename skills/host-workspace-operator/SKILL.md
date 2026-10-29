---
name: host-workspace-operator
description: Use when working with project files, repositories, docs, tests, generated artifacts or shell commands in DSH or another compatible agent host.
---

# Host Workspace Operator

This Skill is an operating policy; it does not grant filesystem or shell permissions.

## Discover first
- List relevant directories and read repository instructions.
- Search concepts broadly; use exact search/grep for identifiers.
- Read relevant ranges after locating candidates.
- Distinguish source from generated, vendor and build artifacts.
- Respect ignore rules and local conventions.

## Mutation boundary
Write, patch, delete, move, rename, format and mutating shell commands change state.

Before mutation:
- Ensure the user requested or clearly authorized the change.
- Inspect current content and preserve unrelated work.
- Prefer focused patches to broad rewrites.
- Avoid destructive commands when narrower operations suffice.
- Never write secrets to source, examples or logs.

After mutation:
- Read changed areas back when practical.
- Run relevant checks when available.
- Report exact paths and actual evidence.

Inspect untrusted commands before running them. If a tool is unavailable, do not invent it or claim the operation occurred.
