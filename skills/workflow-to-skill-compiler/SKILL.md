---
name: workflow-to-skill-compiler
description: Use when converting a runbook, command, prompt chain, agent instruction or team process into a portable Skill while preserving decision logic and verification gates.
---

# Workflow-to-Skill Compiler

1. Define one repeatable user job per Skill; split unrelated work and merge near-duplicates.
2. Trace trigger, inputs, decisions, actions, approvals, evidence, error paths and completion criteria.
3. Write metadata that explains when to invoke the Skill.
4. Keep the main `SKILL.md` focused on execution; move deep references to `references/` and deterministic helpers to `scripts/`.
5. Remove private aliases, absolute paths, undocumented dependencies and assumptions tied to one agent product.
6. Preserve human approval, security boundaries, tests and stop conditions.
7. Prefer DSH-native workspace tools; add runtime dependencies only when behavior genuinely requires them.
8. Separate discovery (read/search/list) from mutation (write/patch/delete or state-changing commands).
9. Review public distribution and document exclusions.

Reject a compilation that merely pastes a prompt, lacks triggers/completion criteria, drops approval gates, relies on unavailable files, duplicates another Skill under a new name, or claims tools/permissions the host does not provide.

Output: name/description, trigger, inputs, ordered procedure, decision points, failures, output contract, dependencies, verification and safety boundary.
