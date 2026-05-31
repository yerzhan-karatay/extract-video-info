# Gemini Instructions

For tasks that ask to extract visible text, captions, OCR hints, named entities, books, products, ratings, or timestamps from social videos, use `skills/extract-video-info/SKILL.md`.

For user-facing install instructions, use `docs/agent-install-prompts.md`.

Run the CLI from the repository root with:

```bash
python -m extract_video_info "<video-url-or-path>" --outdir work/video-evidence --fps 1
```

Keep adapters short and preserve `skills/extract-video-info/SKILL.md` as the source of truth.
