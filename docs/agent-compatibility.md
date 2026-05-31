# Agent Compatibility

This repo uses one canonical skill plus thin adapters.

## Source of Truth

`skills/extract-video-info/SKILL.md` is the canonical workflow. Update it first when the extraction process changes.

Use `docs/agent-install-prompts.md` when a user wants a copy-paste prompt for Codex, Claude Code, Cursor, Gemini, Copilot, OpenClaw, Vellum, ZeroClaw, Manus, Perplexity Computer, Claude Cowork, Hermes, or another agent to install or use this project.

Use `docs/agent-support.md` for the support matrix and support-level definitions.

Use `llms.txt` as the compact repository index for agents that first look for machine-readable project context.

## Adapters

| Surface | File or folder | Purpose |
| --- | --- | --- |
| Agent Skills standard | `skills/extract-video-info/SKILL.md` | Portable skill definition with scripts and references. |
| OpenAI Codex plugin | `.codex-plugin/plugin.json` | Points Codex plugin packaging at `./skills/`. |
| OpenAI Codex repo skill | `.agents/skills/extract-video-info/SKILL.md` | Repo-scoped adapter for Codex skill discovery. |
| OpenAI Codex marketplace | `.agents/plugins/marketplace.json` | Local marketplace entry for testing/installing this repo as a plugin. |
| Claude Code plugin | `.claude-plugin/plugin.json` | Lets Claude Code discover the root `skills/` folder as plugin content. |
| Claude context | `CLAUDE.md` | Short repo guidance for Claude sessions. |
| Cursor | `.cursor/rules/extract-video-info.mdc` | Project rule that points to the canonical skill. |
| Gemini | `GEMINI.md` | Project context that points to the canonical skill. |
| GitHub Copilot | `.github/copilot-instructions.md` | Repository custom instructions for Copilot. |
| GitHub Copilot agent skills | `.github/skills/extract-video-info/SKILL.md` | Thin adapter for Copilot's project skill directory convention. |
| OpenClaw | `AGENTS.md` | Workspace-level context file for OpenClaw-style agents. |
| Vellum | `skills/extract-video-info/SKILL.md` | Skill folder with canonical instructions. |
| ZeroClaw | `AGENTS.md` | Prompt/context adapter for a configurable local agent runtime. |
| Manus | `docs/agent-install-prompts.md` | Prompt-based install and usage path. |
| Perplexity Computer / Spaces | `docs/agent-install-prompts.md` | Prompt/custom-instructions path. |
| Claude Cowork | `.claude-plugin/plugin.json`, `CLAUDE.md` | Plugin and instructions path. |
| Hermes and similar autonomous agents | `AGENTS.md`, `docs/agent-install-prompts.md` | Generic shell-capable agent path. |
| Generic coding agents | `AGENTS.md` | Shared project instructions and test commands. |

## Why This Shape

- OpenAI Codex documents skills as directories with `SKILL.md` plus optional `scripts/`, `references/`, `assets/`, and `agents/openai.yaml`; plugins are the distribution unit for reusable skills.
- Claude Code plugins use `.claude-plugin/plugin.json` and support `skills/<name>/SKILL.md` at the plugin root.
- GitHub recommends README, license, contribution, code-of-conduct, and security files for healthy public repositories.
- GitHub Actions supports matrix testing across operating systems and Python versions.
- Python packaging supports console scripts through `[project.scripts]` in `pyproject.toml`.

Reference links:

- OpenAI Codex Skills: https://developers.openai.com/codex/skills
- OpenAI Codex Plugins: https://developers.openai.com/codex/plugins/build
- Claude Code Skills: https://code.claude.com/docs/en/skills
- Claude Code Plugins: https://code.claude.com/docs/en/plugins
- Claude Cowork customization: https://claude.com/resources/tutorials/customize-claude-cowork
- Cursor Rules: https://cursor.com/docs
- Gemini context files: https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html
- GitHub Copilot repository instructions: https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot
- GitHub Copilot agent skills: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills
- OpenClaw multi-agent workspaces: https://docs.openclaw.ai/concepts/multi-agent
- Vellum skills and tools: https://www.vellum.ai/docs/key-concepts/skills-and-tools
- ZeroClaw docs: https://docs.zeroclawlabs.ai/en/
- Perplexity Agent API prompt guide: https://docs.perplexity.ai/docs/agent-api/prompt-guide
- Perplexity Spaces: https://www.perplexity.ai/help-center/en/articles/10352961-what-are-spaces
- AGENTS.md: https://agents.md
- Python `pyproject.toml`: https://packaging.python.org/en/latest/specifications/pyproject-toml/
- GitHub Python Actions: https://docs.github.com/en/actions/tutorials/build-and-test-code/building-and-testing-python
