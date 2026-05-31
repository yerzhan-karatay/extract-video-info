# Contributing

Thanks for helping improve Extract Video Info.

## Setup

```bash
python -m pip install -e ".[dev]"
```

Install external tools if you want to run end-to-end video extraction:

- `ffmpeg`
- `ffprobe`
- Optional: `tesseract`

## Checks

Run before opening a pull request:

```bash
python -m pytest
python -m ruff check .
python -m ruff format --check .
```

## Guidelines

- Keep Python code cross-platform. Do not depend on shell features that only work on one OS.
- Keep live social-platform tests manual or opt-in. Default CI should use local fixtures.
- Keep `skills/extract-video-info/SKILL.md` as the source of truth for the agent workflow.
- Keep adapters short and update them only when discovery or install behavior changes.
- Do not add behavior that bypasses platform access controls.
