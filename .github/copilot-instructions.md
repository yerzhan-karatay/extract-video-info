# GitHub Copilot Instructions

This repository contains a cross-platform Python CLI and Agent Skill for extracting evidence from social videos.

Use `skills/extract-video-info/SKILL.md` as the source of truth for extraction workflows. Keep `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `.cursor/rules/extract-video-info.mdc` as short adapters that point to the canonical skill.

For user-facing install instructions, use `docs/agent-install-prompts.md`.

Development commands:

- Install: `python -m pip install -e ".[dev]"`
- Test: `python -m pytest`
- Lint: `python -m ruff check .`
- Format: `python -m ruff format .`

Implementation rules:

- Keep Python code cross-platform; avoid shell-only assumptions.
- Treat social-platform access as unstable. Automated tests should use local fixtures, not live Instagram/TikTok/YouTube downloads.
- Do not bypass platform access controls.
- Do not commit generated evidence, downloaded media, cookies, credentials, OCR output, or local environment files.
