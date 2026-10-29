---
name: sandbox-python-executor
description: Use when deterministic parsing, calculations, repository checks, transformations, archive inspection, packaging or hashing need real execution evidence.
---

# Deterministic Python Executor

Use local Python to produce evidence, not to simulate results in prose.

Appropriate tasks include parsing JSON manifests/reports, checking path duplicates and traversal, computing SHA-256, inspecting/creating ZIP files, running dependency-free validators and reproducing deterministic failures.

Rules:
1. Use Python 3 when available and execution materially improves correctness.
2. Inspect unfamiliar scripts before executing them.
3. Keep reads read-only unless changes are authorized.
4. Do not assume local network access.
5. Never expose environment secrets.
6. Report runtime, command, exit status, findings, artifact paths and hashes where relevant.
7. If execution is unavailable, do not claim tests, packaging, hashes or transformations ran.

This is an execution policy, not a remote-code-execution service. DSH tools and local permissions remain authoritative.
