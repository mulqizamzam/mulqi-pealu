---
name: workflow-to-skill-compiler
description: Use when a runbook, command, prompt chain, agent instruction, or team process must become a portable Skill while preserving decision logic and verification gates.
---

# Workflow-to-Skill Compiler

Compile behavior, not file shape.

## Compilation rules

1. Define one repeatable user job per Skill; split unrelated work and merge near-duplicates.
2. Trace trigger, inputs, decision points, actions, approval gates, evidence, error paths and completion condition.
3. Write discovery metadata describing when to invoke the Skill.
4. Keep the main Skill focused on execution; move large references into `references/` and deterministic helpers into `scripts/`.
5. Remove private aliases, absolute paths, undocumented dependencies and assumptions tied to one agent product.
6. Preserve human approval, security boundaries, tests and stop conditions.
7. Prefer DSH-native tools for workspace access. Add runtime dependencies only where observed behavior requires them.
8. Use capability-oriented language instead of hard-coded tool IDs unless the host contract requires them.
9. Separate discovery (read/search/list) from mutation (write/patch/delete or mutating commands).
10. Review public distribution before packaging and document excluded content.

## Required output

For every compiled Skill, provide name/description, intended trigger, inputs, ordered procedure, decisions, failure paths, output contract, dependencies, verification requirements and safety boundary.

## Reject compilation if

- it is only a prompt pasted into a file
- it lacks clear triggers or completion criteria
- it relies on files unavailable after install
- it drops approval or verification gates
- near-duplicate Skills differ only by name
- metadata is too broad to route correctly
- it claims tools or permissions the host does not provide
