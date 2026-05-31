# AGENTS.md

## Project

Extract Video Info is a cross-platform Python CLI plus Agent Skill for preparing evidence from Instagram, TikTok, YouTube, and local video files. The canonical reusable workflow is `skills/extract-video-info/SKILL.md`.

Created and maintained by Yerzhan Karatayev: https://github.com/yerzhan-karatay

## Repository Navigation

- Public overview and manual install: `README.md`
- Copy-paste install prompts for agents: `docs/agent-install-prompts.md`
- Agent compatibility matrix: `docs/agent-compatibility.md`
- Canonical extraction workflow: `skills/extract-video-info/SKILL.md`
- Python package source: `src/extract_video_info/`
- Tests: `tests/`

## Development Commands

- Install for development: `python -m pip install -e ".[dev]"`
- Run tests: `python -m pytest`
- Lint: `python -m ruff check .`
- Format: `python -m ruff format .`
- Run CLI from source: `python -m extract_video_info "<video-url-or-path>" --outdir work/video-evidence --fps 1`

## External Tools

- `ffmpeg` and `ffprobe` are required for video probing and frame extraction.
- `tesseract` is optional and only required when `--ocr-langs` is used.
- Network URL downloads are handled by `yt-dlp`; tests should not depend on live social-platform access unless explicitly marked/manual.

## Agent Guidance

- Keep `skills/extract-video-info/SKILL.md` as the source of truth. Adapter files should point to it rather than duplicate the full workflow.
- Preserve cross-platform behavior. Avoid POSIX-only shell assumptions in Python code.
- Do not bypass platform access controls. Support public URLs, user-provided local files, or user-authorized authenticated downloads only.
- Do not commit generated evidence, downloaded media, cookies, credentials, OCR output, or local environment files.
- Before committing code changes, run tests and formatting/lint checks when available.
