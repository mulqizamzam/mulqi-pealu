---
name: submission-pack-builder
description: Use when a plugin has passed relevant local checks and needs an evidence-backed release or reviewer packet.
---

# Release Evidence Pack Builder

Do not use release copy to hide technical gaps.

## Preconditions

Require an exact source ref/version, reviewed public Skills, known runtime target, relevant tests, manifest/path validation, reproducible package evidence where promised, license/attribution review and clear runtime-smoke status.

## Build the packet

Record:
- exact source ref and version
- architecture and user-facing purpose
- public Skills, helper scripts and dependencies
- excluded capabilities and reasons
- package file list and SHA-256
- checks actually run and results
- installation, upgrade and uninstall instructions
- security, privacy, license and compatibility notes
- direct, indirect and negative acceptance prompts
- unresolved warnings and manual smoke checks

## Status discipline

Use truthful statuses such as `planned`, `implemented`, `locally_validated`, `package_verified`, `runtime_smoke_tested` or `published`. Never treat them as synonyms.

For DSH bundle distribution, validate `package.json`'s `dsh.bundle.patch` contract and ensure the patch inserts the expected plugin row. A local ZIP does not prove DSH accepted, enabled or rendered the plugin.
