# Mulqi Pealu — DeepSeek Harness Workflow Autopilot

[![DSH](https://img.shields.io/badge/DeepSeek%20Harness-0.2.1--rc.2-0b806f)](https://github.com/deepseek-ai/deepseek-harness)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

**Mulqi Pealu** is a community-maintained workflow toolkit for DeepSeek Harness (DSH). It helps turn repositories, team processes and agentic workflows into organized, documented and verifiable deliverables. Its scope includes software engineering, productivity workflows, source-based research, experimentation, model evaluation, packaging and release preparation.

> **Target:** DSH `0.2.1-rc.2` (`>=0.2.1-rc.2 <0.3.0`). This is a community project, not an official DeepSeek product.

## Features

- Discover reusable workflows in a repository and classify them before conversion.
- Compile focused Skills while preserving decisions, approval gates, tests and stop conditions.
- Plan a coherent plugin and document the capabilities and runtime dependencies.
- Apply safe workspace practices: inspect and search first, make minimal authorized edits, then verify.
- Structure research with source quality, dates, evidence and explicit uncertainty.
- Design reproducible experiments and model-evaluation plans with baselines, datasets, metrics, controls and error categories.
- Prepare professional product descriptions, README files, release notes and reviewer evidence.
- Analyze repository shape, validate package metadata and safe paths, create deterministic ZIP files and calculate SHA-256 checksums.

## Included Skills

| Skill | Purpose |
|---|---|
| `mulqi-pealu-autopilot` | Orchestrate discovery, planning, execution, verification and packaging |
| `agentic-repo-discovery` | Find reusable repository workflows and public-distribution boundaries |
| `workflow-to-skill-compiler` | Convert runbooks and prompts into portable Skills |
| `plugin-experience-architect` | Organize a coherent plugin experience and Skill portfolio |
| `host-workspace-operator` | Guide safe repository and workspace operations |
| `sandbox-python-executor` | Require actual execution evidence for deterministic tasks |
| `plugin-brand-identity-designer` | Create and check product-specific icon and brand assets |
| `plugin-directory-listing-writer` | Write accurate metadata, prompts and user documentation |
| `submission-pack-builder` | Compile release/reviewer evidence without overstating readiness |

## 1. Before installing: set up DSH

Follow the setup steps and version requirements in the [official DeepSeek Harness repository](https://github.com/deepseek-ai/deepseek-harness). The DSH CLI documentation describes `dsh web` as the Web profile launcher and `dsh plugin --profile <name>` as the package manager for a profile.

## 2. Install this bundle

From a terminal with a working DSH CLI/profile:

```bash
dsh plugin --profile web add "github:mulqizamzam/mulqi-pealu#main"
```

For a local checkout:

```bash
git clone https://github.com/mulqizamzam/mulqi-pealu.git
cd mulqi-pealu
dsh plugin --profile web add "link:$(pwd)"
```

After installation, restart the DSH Web UI when hot reload is unavailable or reports `restart-required`. Review any requested build-script approval before accepting it.

**Alternative: repository Skills.** DSH can also discover on-disk Skills from `.agents/skills` and `.dsh/skills` in the project workspace. To use the Skills directly in a workspace, copy the desired Skill directories to one of those supported roots, e.g. `.agents/skills/`; this route uses DSH's filesystem Skill provider and does not install a bundle.

## 3. Use it

Ask the agent for an outcome, and name the target workspace or repo when relevant. Example prompts:

- “Analyze this repository for reusable agent workflows. Return a disposition table, risks and a recommended architecture before editing.”
- “Convert this runbook into a portable Skill. Preserve decision points, approvals, tests and stop conditions.”
- “Plan a reproducible experiment comparing two models. Specify dataset, baseline, metrics, controls and report format.”
- “Review these evaluation results. Separate measured results from interpretation and explain the limits.”
- “Audit this plugin package and run the available validation checks. Report actual command results and unresolved risks.”
- “Write a professional README for beginners, including install, use, update and uninstall instructions.”

For repository changes, open the intended workspace first and specify which files may be changed. Skills are instructions, not permission grants; obey DSH approval and sandbox controls.

## 4. Local helper tools

Python 3 is required for these local CLI helpers:

```bash
# Read-only heuristic repository inventory
python3 scripts/analyze_repo.py /path/to/repository --json

# Validate the plugin's file structure and DSH manifest
python3 scripts/validate_plugin.py . --json

# Build a deterministic ZIP and SHA256SUMS
python3 scripts/package_plugin.py . --out dist

# Inspect a ZIP for path traversal, duplicate paths and symlinks
python3 scripts/inspect_archive.py dist/mulqi-pealu-0.2.1-rc.2.zip --json
```

The analyzer is heuristic; it does not determine semantic value by itself. Structural validation and packaging do not prove a Skill works at runtime in every DSH build.

## 5. Uninstall

To remove the bundle from a profile:

```bash
dsh plugin --profile web remove @mulqizamzam/mulqi-pealu
```

If you copied Skill directories into `.agents/skills` or `.dsh/skills`, remove those copied directories manually instead.

## Validation

Run from the repository root:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_plugin.py . --json
python3 scripts/package_plugin.py . --out dist
python3 scripts/inspect_archive.py dist/mulqi-pealu-0.2.1-rc.2.zip --json
```

GitHub Actions is configured to execute unit tests, structural validation and archive checks on pushes and pull requests.

## Boundaries

- Repository and shell operations depend on the host tools and permissions DSH provides; this package does not grant extra access.
- Web-based research depends on an enabled DSH web/search capability.
- Experiments and model evaluation need actual test cases/data and clearly defined scoring rules.
- Bundle activation performs no outbound requests or telemetry.
- Verify the behavior before upgrading beyond the stated DSH compatibility target.

## Attribution

This port adapts workflow guidance from [ChatGPT/Codex Plugin Autopilot](https://github.com/imMamdouhaboammar/chatgpt-codex-plugin-autopilot), licensed under MIT. See [NOTICE](./NOTICE) and [LICENSE].
