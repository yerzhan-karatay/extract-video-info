---
name: extract-video-info
description: Extract visible text, captions, spoken-text clues, named items, products, books, ratings, timestamps, and other facts from Instagram, TikTok, YouTube, and local video files. Use this repo-scoped adapter when Codex should use the canonical skill at skills/extract-video-info/SKILL.md.
---

# Extract Video Info Adapter

Use the canonical skill at `skills/extract-video-info/SKILL.md`.

If the user asks to extract information from a video URL or local video file, read that canonical skill, then run the package CLI:

```bash
python -m extract_video_info "<video-url-or-path>" --outdir work/video-evidence --fps 1
```
