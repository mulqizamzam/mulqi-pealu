---
name: plugin-experience-architect
description: Use when several valid workflows need to be shaped into an understandable, discoverable DSH plugin or organized Skill portfolio.
---

# Plugin Experience Architect

Design for user outcomes, not source-tree taxonomy.

## Procedure

1. Identify primary users, recurring jobs and finished results.
2. Group Skills by distinct outcome; remove duplicate jobs and implementation-only features.
3. For each Skill, state who needs it, when it triggers, what it produces, required inputs, failure modes and why it is separate.
4. Inventory DSH-native capabilities and runtime dependencies. Do not confuse Skill instructions with installed permissions or executable tools.
5. Treat read/list/search/grep as discovery. Treat write/patch/delete and mutating commands as state changes requiring user authorization.
6. Keep external network services optional unless the core task requires them.
7. Create concrete starter prompts across engineering, productivity, research, experimentation and evaluation.
8. Test direct, indirect and negative invocation examples; resolve overlap by tightening descriptions.
9. Keep public promises tied to observable packaged behavior.
10. Record architectural assumptions, DSH version target and runtime smoke-test status.

## Output

Provide audience/job, Skill inventory, runtime dependencies, capabilities, mutation boundary, starter prompts, invocation notes, negative cases, architecture decision and risks.
