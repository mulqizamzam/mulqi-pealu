---
name: agentic-repo-discovery
description: Use when a repository contains Skills, agents, prompts, workflows, commands, runbooks or scripts and you need to find reusable capabilities and set public distribution boundaries.
---

# Agentic Repository Discovery

1. Read repository instructions and the main README.
2. Inventory manifests, Skills, agents, prompts, commands, playbooks, scripts, tests, CI, app/MCP files, license and release assets.
3. Run `scripts/analyze_repo.py <repo> --json` when available. Treat rankings as heuristics, not semantic truth.
4. Trace strong candidates through trigger, inputs, decisions, actions, verification, errors and completion criteria.
5. Assign each candidate a disposition: `preserve_skill`, `compile_skill`, `reference_only`, `runtime_dependency`, `internal_only` or `discard`.
6. Flag secrets, personal paths, internal instructions, destructive actions, hidden telemetry, unclear licensing, credential use and unsupported claims.
7. Recommend architecture from actual behavior, not a filename alone.
8. Deliver a conversion brief before generating configuration.

The brief must name repository/ref, reusable jobs, dispositions with reasons, Skill grouping, dependencies, public exclusions, evidence gaps and next actions.
