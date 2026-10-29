---
name: submission-pack-builder
description: Use when a plugin has passed local checks and needs an evidence-backed release or reviewer packet.
---

# Release Evidence Pack Builder

Do not use release copy to conceal technical gaps.

## Preconditions
Require exact source ref/version, reviewed public Skills, known runtime target, relevant tests, manifest/path validation, reproducible packaging where promised, licensing/attribution review and an explicit runtime-smoke status.

## Packet contents
- source ref, version and architecture
- user-facing purpose, Skills, helper scripts and dependencies
- excluded capabilities and reasons
- archive inventory and SHA-256
- checks actually run and results
- installation, upgrade and uninstall instructions
- security, privacy, license and compatibility notes
- direct/indirect/negative acceptance prompts
- unresolved warnings and manual smoke checks

Use truthful states: `planned`, `implemented`, `locally_validated`, `package_verified`, `runtime_smoke_tested` or `published`.

For DSH bundles, verify `package.json`'s `dsh.bundle.patch` contract and expected plugin row. A valid ZIP does not prove DSH enabled or rendered it.
