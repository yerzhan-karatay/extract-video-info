---
name: extract-video-info
description: Extract visible text, captions, spoken-text clues, named items, products, books, ratings, timestamps, and other facts from Instagram Reels, TikTok videos, YouTube videos or Shorts, and local video files. Use when a user asks for structured information from a video, such as a list of books mentioned, onscreen text, product names, visible ratings, creator captions, or an evidence-backed summary.
---

# Extract Video Info

## Overview

Use this skill to turn a social video URL or local video file into reviewable evidence, then extract the requested facts with visual verification. Prefer metadata, subtitles, OCR hints, frame sheets, and high-resolution stills over guessing.

## Workflow

1. Identify the requested output fields. Examples: book titles and authors, product names, ratings, timestamps, visible captions, spoken claims, or all onscreen text.
2. Create a task-local output directory. Use `work/` for temporary evidence and `outputs/` only for final user-facing deliverables.
3. Prepare evidence with the CLI from the repository root or from an installed package:

```bash
python -m extract_video_info "<video-url-or-path>" --outdir work/video-evidence --fps 1
```

If the package is not installed and this skill is being used from a source checkout, run the bundled wrapper:

```bash
python skills/extract-video-info/scripts/prepare_video_evidence.py "<video-url-or-path>" --outdir work/video-evidence --fps 1
```

For non-English visible text, pass OCR languages when known:

```bash
python -m extract_video_info "<video-url-or-path>" --outdir work/video-evidence --fps 1 --ocr-langs rus,eng
```

If the requested Tesseract language data is not installed locally, install it with the OS package manager or explicitly allow a download into the task output directory:

```bash
python -m extract_video_info "<video-url-or-path>" --outdir work/video-evidence --fps 1 --ocr-langs rus,eng --download-ocr-langs
```

4. Read `metadata.json`, `ffprobe.json`, `evidence_summary.md`, and subtitle files first if available. Captions/descriptions often contain context that frame OCR alone misses.
5. Inspect every contact sheet and key frame with the available image-viewing tool. Treat OCR as a hint; verify names visually on the frame when possible.
6. Extract full-resolution stills for hard-to-read moments:

```bash
ffmpeg -hide_banner -loglevel error -ss <seconds> -i work/video-evidence/video.mp4 -frames:v 1 -q:v 2 work/video-evidence/keyframe_<seconds>.jpg
```

7. If exact spelling matters, verify uncertain titles/names against public web sources, official publisher/product pages, or the creator caption. Clearly mark unresolved uncertainty.
8. Return a concise structured answer. Include the source URL/path, extracted items, and confidence notes only where needed.

## Platform Notes

- Use the same CLI for public Instagram, TikTok, and YouTube URLs; it delegates downloading to `yt-dlp`.
- If a platform blocks anonymous download, do not bypass private access. Ask the user for an uploaded/downloaded video file, or ask whether they want to use authenticated browser cookies when they have legitimate access.
- Never commit cookies, credential files, downloaded videos, frame sheets, OCR output, or generated evidence. Keep them under ignored task-local directories such as `work/`.
- For YouTube, check subtitles or auto-captions when spoken content matters. See `references/platform-notes.md`.
- For Instagram and TikTok, assume most useful text may be burned into the video. Frame sheets and high-resolution stills are usually the main evidence.

## Extraction Quality Rules

- Do not infer a complete list from a partial contact sheet. Cover the whole video duration.
- De-duplicate repeated frames of the same item, but preserve distinct editions if visible differences matter.
- For books, products, or named entities, prefer output columns like `title`, `author/brand`, `rating`, `timestamp`, and `evidence/confidence`.
- Preserve original-language titles when visible. Add translations only if the user asks or if they help disambiguate.
- Mention access, download, OCR, subtitle, or visual-inspection failures plainly.

## References

- `references/platform-notes.md`: platform commands, subtitle extraction, OCR language notes, and troubleshooting.
- `references/ocr-languages.md`: common Tesseract language codes and installation notes.
