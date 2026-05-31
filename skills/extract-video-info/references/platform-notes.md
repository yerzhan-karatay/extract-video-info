# Platform Notes

## Download and Access

- Public Instagram, TikTok, YouTube, and YouTube Shorts URLs usually work through `yt-dlp`, but all three platforms can change access rules.
- For Instagram, try the canonical `/reel/<id>/`, `/p/<id>/`, or `/tv/<id>/` URL if the original shared URL fails.
- When authenticated access is required, ask the user for an uploaded local video or explicit permission to use browser cookies. Do not attempt to access private content without user authorization, and never store cookies inside the repository.

## YouTube Subtitles

When spoken content matters, try subtitles before audio transcription:

```bash
yt-dlp --skip-download --write-subs --write-auto-subs --sub-lang "en.*,ru.*,ja.*,kk.*" --sub-format vtt "<youtube-url>"
```

Use subtitles as evidence, but still verify visible onscreen text from frames when the request is about titles, labels, slides, signs, products, or books.

## Review Pattern

1. Read metadata and caption.
2. Scan all contact sheets for distinct items or text changes.
3. Extract full-resolution stills for ambiguous frames.
4. OCR high-value frames if visual reading is not enough. Download missing OCR language data only when explicitly requested.
5. Search public sources only for exact spelling or author/brand confirmation.
6. Return the requested list with uncertainty notes.
