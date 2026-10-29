---
name: agentic-repo-discovery
description: Use when a repository contains Skills, agents, prompts, workflows, commands, runbooks, or scripts and you need to find reusable capabilities and set public distribution boundaries.
---

# Agentic Repository Discovery

Discover repeatable user jobs before designing a plugin or automated workflow.

## Procedure

1. Read repository instructions and the main README.
2. Inventory manifests, Skills, agent definitions, prompts, commands, playbooks, scripts, tests, CI, app/MCP integration files, licenses and release assets.
3. Run `scripts/analyze_repo.py <repo> --json` if available. Treat its results as signals, not semantic truth.
4. Inspect high-value candidates in context. Trace each from trigger to inputs, decisions, actions, verification, failure handling and completion condition.
5. Assign each candidate one disposition: `preserve_skill`, `compile_skill`, `reference_only`, `runtime_dependency`, `internal_only`, or `discard`.
6. Flag secrets, personal paths, internal-only instructions, destructive actions, hidden telemetry, unclear licensing, credential use and unsupported claims.
7. Recommend architecture from actual behavior, not the presence of a config filename alone.
8. Deliver a conversion brief before writing configuration.

## Output

Include repository/ref inspected, jobs found, dispositions and reasons, proposed Skill grouping, dependencies, public exclusions, missing evidence and next actions. Do not generate a manifest before the package boundary is clear.
