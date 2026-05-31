---
name: extract-video-info
description: Use the repository's Extract Video Info workflow to prepare evidence and extract structured facts from Instagram, TikTok, YouTube, and local video files.
---

# Extract Video Info

This is the GitHub Copilot project-skill adapter. Use the canonical skill in `skills/extract-video-info/SKILL.md` for the full workflow, references, and helper script.

Quick path:

```bash
python -m extract_video_info "<video-url-or-path>" --outdir work/video-evidence --fps 1
```

If the package is not installed but this repository is checked out, run:

```bash
python skills/extract-video-info/scripts/prepare_video_evidence.py "<video-url-or-path>" --outdir work/video-evidence --fps 1
```

Always inspect the generated contact sheets and key frames before returning names, titles, ratings, or other extracted facts.

Do not commit generated evidence, downloaded media, cookies, credentials, OCR output, or frame sheets.
