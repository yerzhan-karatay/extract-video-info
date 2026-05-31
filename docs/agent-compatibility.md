# Agent Compatibility

This repo uses one canonical skill plus thin adapters.

## Source of Truth

`skills/extract-video-info/SKILL.md` is the canonical workflow. Update it first when the extraction process changes.

Use `docs/agent-install-prompts.md` when a user wants a copy-paste prompt for Codex, Claude Code, Cursor, Gemini, Copilot, or another agent to install or use this project.

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
- Cursor Rules: https://cursor.com/docs
- Gemini context files: https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html
- GitHub Copilot repository instructions: https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot
- GitHub Copilot agent skills: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills
- AGENTS.md: https://agents.md
- Python `pyproject.toml`: https://packaging.python.org/en/latest/specifications/pyproject-toml/
- GitHub Python Actions: https://docs.github.com/en/actions/tutorials/build-and-test-code/building-and-testing-python
