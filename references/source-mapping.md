# Source-to-port mapping

Source project: [ChatGPT/Codex Plugin Autopilot](https://github.com/imMamdouhaboammar/chatgpt-codex-plugin-autopilot)

| Source capability | Ported path | Disposition |
|---|---|---|
| chatgpt-codex-plugin-autopilot | skills/mulqi-pealu-autopilot | Compiled and retargeted to DSH; release gates retained |
| agentic-repo-discovery | skills/agentic-repo-discovery | Preserved and adapted |
| workflow-to-skill-compiler | skills/workflow-to-skill-compiler | Preserved and adapted |
| plugin-experience-architect | skills/plugin-experience-architect | Preserved and adapted |
| host-workspace-operator | skills/host-workspace-operator | Preserved; host-native assumptions generalized |
| sandbox-python-executor | skills/sandbox-python-executor | Preserved; execution references adapted |
| plugin-brand-identity-designer | skills/plugin-brand-identity-designer | Preserved and retargeted |
| plugin-directory-listing-writer | skills/plugin-directory-listing-writer | Preserved for DSH docs and metadata |
| submission-pack-builder | skills/submission-pack-builder | Preserved with DSH-specific release evidence states |

## Exclusions

- OpenAI-specific `.codex-plugin/plugin.json`, `agents/openai.yaml`, directory-submission fields and screenshot requirements are not valid DSH bundle configuration.
- ChatGPT/Codex-only host assumptions and undocumented manifest fields were rewritten for DSH.
- The original GitHub Action, npm/Bun installer and release pipeline were not mirrored verbatim because they target the source project's distribution architecture. DSH-specific helper scripts and CI were added.
- No external runtime service or MCP server was added; the portable workflows do not require one.
