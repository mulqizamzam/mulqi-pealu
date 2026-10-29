---
name: mulqi-pealu-autopilot
description: Use when orchestrating repository-to-plugin conversion, engineering workflows, research, experimentation, model evaluation, validation, packaging, or release preparation in DeepSeek Harness.
---

# Mulqi Pealu Autopilot

## Goal

Turn a concrete engineering or knowledge-work request into an organized, evidence-backed result in the current DSH workspace. Choose only the workflows that help complete the requested job; do not force plugin packaging into unrelated tasks.

## Operating contract

1. Identify the intended deliverable and available evidence. When a nonessential detail is missing, choose a reversible default and state it.
2. Inspect repository instructions, README, manifests, source, workflows, tests, docs, dependencies, license and release metadata before planning code or plugin changes.
3. For repository conversions, use `agentic-repo-discovery` and classify candidates as `preserve_skill`, `compile_skill`, `reference_only`, `runtime_dependency`, `internal_only`, or `discard`.
4. Compile selected behavior through `workflow-to-skill-compiler`. Preserve triggers, decisions, evidence, approvals, verification, error paths and stop conditions.
5. Use `plugin-experience-architect` to group workflows by user outcome and separate core features from implementation details.
6. For workspace changes, follow `host-workspace-operator`: inspect first, make the smallest authorized change, read the result back, and run relevant checks.
7. When results depend on local computation, file processing, archive checks or hashing, run local Python helpers or host-native execution when available. Never say a command ran without evidence.
8. For research, assess source quality and dates. For experiments and model evaluation, define test set, baseline, metric, controls and failure categories before interpreting results.
9. Review public content for secrets, private instructions, unsafe destructive operations, unclear licensing and unsupported claims.
10. Validate structure, metadata, assets and paths; package twice when determinism matters; compare outputs and inspect a clean extraction.
11. Write documentation and release metadata based on actual behavior, not aspirational claims.
12. Keep these states distinct: analyzed, planned, implemented, locally validated, package verified, DSH runtime smoke-tested and published.

## Candidate dispositions

| Disposition | Meaning |
|---|---|
| `preserve_skill` | Keep reusable workflow guidance with small portability edits |
| `compile_skill` | Rebuild a mixed or fragile workflow into a task-specific Skill |
| `reference_only` | Keep documentation or examples that inform another workflow |
| `runtime_dependency` | Keep only when required by runtime behavior |
| `internal_only` | Exclude private, unsafe or repository-specific process details |
| `discard` | Remove duplicate, obsolete or low-value material |

## Completion criteria

Deliver changed paths, evidence, checks actually run, failures, unresolved risks and next safe action. For code or packages, include exact paths and repeatable validation commands. Never claim an unrun test, live DSH install or publication.
