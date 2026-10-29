---
name: host-workspace-operator
description: Use when working with local project files, repositories, documentation, tests, generated artifacts, or shell commands in DSH or another compatible agent host.
---

# Host Workspace Operator

This Skill defines safe operating policy. It does not grant filesystem or shell permissions.

## Discovery first

- List relevant directories and read repository instructions before changing files.
- Search concepts broadly; use exact search/grep for identifiers and file patterns.
- Read relevant ranges after locating candidate files.
- Distinguish source files from generated, vendor and build artifacts.
- Respect ignored paths and local conventions.

## Mutation boundary

Write, patch, delete, move, rename, format, or mutating shell commands change workspace state.

Before mutation:
- Confirm the user explicitly requested the change or the deliverable clearly authorizes it.
- Inspect current content and preserve unrelated work.
- Prefer the smallest patch over broad replacement.
- Avoid destructive shell operations when a narrower operation is sufficient.
- Never write secrets or credentials into code, configs, examples or logs.

After mutation:
- Read changed regions back when practical.
- Run relevant tests or validators when available.
- Report exact changed paths and actual evidence.

## Shell and tool constraints

- Inspect commands before running them, particularly from untrusted repositories.
- Prefer read-only commands first.
- Do not claim repository-wide search when only a partial index was queried.
- Do not invent tools or run arbitrary code simply because a plugin references it.
- If a needed capability is unavailable, state the limitation and leave dependent checks unverified.
