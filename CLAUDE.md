# Claude Instructions

Use the canonical skill at `skills/extract-video-info/SKILL.md` for video information extraction tasks.

This repository can also be loaded as a Claude Code plugin from the repo root because it contains `.claude-plugin/plugin.json` and `skills/extract-video-info/SKILL.md`.

For user-facing install instructions, use `docs/agent-install-prompts.md`.

Development commands:

- `python -m pip install -e ".[dev]"`
- `python -m pytest`
- `python -m ruff check .`
- `python -m ruff format .`
