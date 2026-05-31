# OCR Languages

The CLI supports `--ocr-langs`, for example:

```bash
extract-video-info video.mp4 --outdir work/video-evidence --ocr-langs rus,eng
```

If Tesseract has no local data for a requested language, install the language package locally or explicitly allow a download into the task output directory:

```bash
extract-video-info video.mp4 --outdir work/video-evidence --ocr-langs rus,eng --download-ocr-langs
```

Useful Tesseract language codes:

- `eng`: English
- `rus`: Russian
- `jpn`: Japanese
- `kaz`: Kazakh
- `deu`: German
- `fra`: French
- `spa`: Spanish

OCR is noisy on moving video, angled covers, stylized fonts, and low-contrast overlays. Use OCR to find candidate frames, then inspect high-resolution stills.
