---
name: mulqi-pealu-autopilot
description: Use when orchestrating repository-to-plugin conversion, engineering workflows, research, experimentation, model evaluation, validation, packaging, or release preparation in DeepSeek Harness.
---

# Mulqi Pealu Autopilot

Turn a concrete engineering or knowledge-work request into an organized, evidence-backed result. Choose only the workflows relevant to the requested deliverable.

## Operating contract

1. Identify the intended deliverable and available evidence. For nonessential missing details, choose a reversible default and say so.
2. Inspect repo guidance, README, manifests, source, workflows, tests, docs, dependencies, licensing and release metadata before planning changes.
3. For repository conversion, use `agentic-repo-discovery` and classify candidates as `preserve_skill`, `compile_skill`, `reference_only`, `runtime_dependency`, `internal_only` or `discard`.
4. Use `workflow-to-skill-compiler` to retain triggers, decisions, evidence, approvals, verification, error paths and stop conditions.
5. Use `plugin-experience-architect` to organize capabilities by user outcome rather than source-tree layout.
6. For workspace changes, follow `host-workspace-operator`: inspect first, make the smallest authorized edit, read it back, and run relevant checks.
7. For deterministic computation, parsing, archive inspection or hashing, run the helper or native host execution when available. Never claim execution without evidence.
8. For research, assess source quality and dates. For experiments/model evaluation, define test set, baseline, metric, controls and failure categories before interpreting results.
9. Review public content for secrets, private instructions, destructive operations, unclear licensing and unsupported claims.
10. Validate metadata, assets, paths and package shape. When deterministic packaging matters, build twice and compare hashes, then inspect a fresh extraction.
11. Make docs and release metadata match observable behavior rather than aspirations.
12. Keep analyzed, planned, implemented, locally validated, package verified, DSH runtime smoke-tested and published as separate states.

## Candidate dispositions

- `preserve_skill`: retain reusable guidance with portability edits
- `compile_skill`: rebuild mixed or fragile guidance as a focused Skill
- `reference_only`: keep content that informs another workflow
- `runtime_dependency`: retain only if actual runtime behavior needs it
- `internal_only`: exclude private, unsafe or repository-specific process details
- `discard`: remove duplicate, obsolete or low-value content

## Completion criteria

Report changed paths, evidence used, checks actually run, failures, unresolved risks and the next safe action. Never claim an unrun test, live DSH install or publication.
