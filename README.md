# Mulqi Pealu — DeepSeek Harness Workflow Autopilot

[![DSH](https://img.shields.io/badge/DeepSeek%20Harness-0.2.1--rc.2-0b806f)](https://github.com/deepseek-ai/deepseek-harness)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-0.2.1--rc.2-5965f2)](./package.json)

**Mulqi Pealu** is a community-maintained DeepSeek Harness (DSH) workflow plugin for turning repositories and agentic workflows into organized, documented, verified deliverables. It brings together engineering workflows, productivity methods, research, experimentation, model evaluation, branding, release preparation and deterministic packaging.

> **Compatibility target:** DeepSeek Harness `0.2.1-rc.2` (`>=0.2.1-rc.2 <0.3.0`).
>
> **Not an official DeepSeek product.** The plugin gives the agent workflow guidance and local helper scripts. It does not grant new filesystem permissions, bypass approvals or silently install packages.

## What you can do

- **Discover workflows:** inspect repository structure, agent instructions, Skills, commands, playbooks, tests and tool/runtime dependencies.
- **Plan a conversion:** classify reusable components, record exclusions, identify risks and choose a maintainable target architecture.
- **Compile workflows:** convert repeatable tasks into portable Skills while preserving decisions, approvals, verification and stop conditions.
- **Work with repositories safely:** search and read before writes, make focused changes, and run appropriate tests when available.
- **Research and compare:** formulate questions, assess source quality, separate evidence from interpretation, and record uncertainty.
- **Experiment and evaluate models:** define hypotheses, datasets, baselines, metrics, controls, failure categories and reproducible reports.
- **Prepare delivery:** draft user-facing metadata, documentation, release notes and reviewer checklists.
- **Verify and package:** use Python helpers to inspect files, validate manifests and safe paths, build repeatable ZIP archives, and calculate SHA-256 checksums.

## Included workflows

The source portfolio's nine separate workflow jobs are retained and adapted:

| Skill | Main job |
|---|---|
| `mulqi-pealu-autopilot` | Orchestrate discovery → planning → execution → verification → packaging |
| `agentic-repo-discovery` | Find reusable repository workflows and define public boundaries |
| `workflow-to-skill-compiler` | Compile focused Skills without losing decision logic |
| `plugin-experience-architect` | Design a coherent user-facing plugin experience |
| `host-workspace-operator` | Apply safe read/search/write/test practices when host tools exist |
| `sandbox-python-executor` | Require execution evidence for deterministic tasks |
| `plugin-brand-identity-designer` | Create a task-specific visual identity and validate assets |
| `plugin-directory-listing-writer` | Write accurate product metadata and discovery prompts |
| `submission-pack-builder` | Build an evidence-led reviewer/release packet |

## For beginners: install DSH first

DSH is a separate application. Follow the official setup instructions in the [DeepSeek Harness repository](https://github.com/deepseek-ai/deepseek-harness). The upstream README documents the supported Node.js runtime and Web launch command.

Example quick start:

```bash
npx @deepseek-ai/dsh web
```

## Install this plugin in DSH

### Option A — DSH Web UI repository source

1. Start DSH and open its Web UI.
2. Open **Settings → Plugins → repository source** (the exact label may vary by build).
3. Add this source: `github:mulqizamzam/mulqi-pealu#main`.
4. Confirm it and check the plugin panel/logs if it does not appear.

The repository-source route uses DSH's plugin-console mechanism and is distinct from installing an npm bundle; availability depends on the DSH build/profile.

### Option B — install as a bundle from a terminal

```bash
git clone https://github.com/mulqizamzam/mulqi-pealu.git
cd mulqi-pealu
dsh plugin --profile web add "link:$(pwd)"
```

Or install directly from GitHub:

```bash
dsh plugin --profile web add "github:mulqizamzam/mulqi-pealu#main"
```

Restart the DSH Web UI so the bundle is reloaded. This requires a working DSH CLI/profile and a supported Node.js runtime. If DSH asks to approve build scripts, inspect the proposed scripts before approving them.

### Uninstall

For the bundle install path:

```bash
dsh plugin --profile web remove @mulqizamzam/mulqi-pealu
```

For the repository-source path, remove its row under **Settings → Plugins → repository source**.

## How to use it

After installation, ask DSH for the outcome you need. Example prompts:

- “Analyze this repository for reusable agent workflows. Return candidate dispositions, risks and a recommended architecture before making changes.”
- “Convert this runbook into a portable Skill. Preserve decision points, approvals, tests and stop conditions.”
- “Design a reproducible experiment comparing two models. Specify baseline, dataset, metrics, controls and report template.”
- “Review these evaluation results. Separate measured results from interpretation and state the limitations.”
- “Audit this plugin package, fix only authorized issues, run available validators and report actual evidence.”
- “Prepare professional README, release notes and installation instructions for this project.”

For repository work, open the intended workspace in DSH first and specify which files may be modified. Skill instructions are not permission grants; follow DSH approvals and workspace/tool restrictions.

## Local helper scripts

The repository includes dependency-free Python 3 helpers for repeatable local tasks:

```bash
# Analyze a target repository
python3 scripts/analyze_repo.py /path/to/target --json

# Validate this plugin's structure and safe paths
python3 scripts/validate_plugin.py . --json

# Build a deterministic ZIP archive plus SHA256SUMS
python3 scripts/package_plugin.py . --out dist

# Inspect an existing ZIP
python3 scripts/inspect_archive.py dist/mulqi-pealu-0.2.1-rc.2.zip --json
```

These helpers are local utilities, not remote services. Review code before running them on an unfamiliar target. Structural validation does not prove every Skill works on every DSH release.

## Validation and release workflow

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_plugin.py . --json
python3 scripts/package_plugin.py . --out dist
python3 scripts/inspect_archive.py dist/mulqi-pealu-0.2.1-rc.2.zip --json
```

GitHub Actions runs checks on pushes and pull requests. Deterministic builds should produce identical archive bytes and SHA-256 values from unchanged inputs.

## Capability boundaries

- File operations depend on capabilities DSH provides in the current session. Skills cannot create tools or permissions.
- Network research depends on configured DSH web/search tools.
- Validation and packaging require Python 3 locally.
- Model evaluation requires test cases/data and transparent scoring rules; confident prose is not a substitute for measurement.
- Bundle activation performs no outbound requests or telemetry.
- DSH is evolving quickly. Verify runtime behavior before upgrading beyond the target range.

## Attribution

This project adapts workflow guidance from [ChatGPT/Codex Plugin Autopilot](https://github.com/imMamdouhaboammar/chatgpt-codex-plugin-autopilot), licensed under MIT. See [NOTICE](./NOTICE) and [LICENSE].

## Contributing

Keep changes focused, add tests for new behavior, use safe reproducible examples, and state exactly which checks were run. Do not claim a live DSH runtime smoke test unless one was performed.
