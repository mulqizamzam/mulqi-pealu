---
name: sandbox-python-executor
description: Use when deterministic parsing, calculations, repository checks, transformations, archive inspection, packaging, or hashing need real execution evidence.
---

# Deterministic Python Executor

Use local Python to produce evidence, not to simulate a result in prose.

## Appropriate tasks

- Parse and compare JSON manifests or reports.
- Inventory paths and check duplicates, traversal, symlinks and sensitive file patterns.
- Compute SHA-256 digests.
- Inspect or create ZIP archives deterministically.
- Run dependency-free validators and targeted tests.
- Reproduce deterministic errors with small fixtures.

## Rules

1. Use Python 3 when available and execution materially improves correctness.
2. Inspect unfamiliar scripts before executing them.
3. Keep reads read-only unless the task authorizes mutations.
4. Do not assume network access from the local execution environment.
5. Never expose environment secrets in output.
6. State runtime, command, exit status, relevant findings, generated paths and hashes when applicable.
7. If execution is unavailable, do not claim tests, packaging, hashes or transformations were run.

## Boundary

This is an execution policy, not a remote code-execution service. DSH capabilities and local permissions still control what can run.
