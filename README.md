# Extract Video Info

Extract Video Info is a cross-platform Python CLI and Agent Skill for preparing evidence from social videos so an AI agent can extract visible text and structured facts reliably.

Created and maintained by [Yerzhan Karatayev](https://github.com/yerzhan-karatay).

It was built for tasks like:

- "List the books mentioned in this Instagram Reel."
- "Extract every product name and rating from this TikTok."
- "Summarize the onscreen slide text in this YouTube Short."
- "Create frame sheets and OCR hints from this local video file."

The project intentionally separates two layers:

- `extract-video-info`: a Python CLI that downloads/probes videos, extracts frames, creates contact sheets, and optionally runs OCR.
- `skills/extract-video-info/SKILL.md`: the canonical Agent Skill workflow that tells Codex, Claude, Cursor, Gemini, Copilot, and other agents how to use the evidence without guessing.

## Install

Python 3.10+ is required.

```bash
python -m pip install git+https://github.com/yerzhan-karatay/extract-video-info.git
```

For development from a checkout:

```bash
git clone https://github.com/yerzhan-karatay/extract-video-info.git
cd extract-video-info
python -m pip install -e ".[dev]"
```

External tools:

- Required: `ffmpeg` and `ffprobe`
- Optional for OCR: `tesseract`

Examples:

```bash
# macOS
brew install ffmpeg tesseract

# Ubuntu/Debian
sudo apt-get install ffmpeg tesseract-ocr

# Windows with winget
winget install Gyan.FFmpeg UB-Mannheim.TesseractOCR
```

## CLI Usage

Prepare evidence from a public URL or local file:

```bash
extract-video-info "https://www.instagram.com/reel/..." --outdir work/video-evidence --fps 1
```

Run from source without installing:

```bash
python -m extract_video_info "video.mp4" --outdir work/video-evidence --fps 1
```

Add OCR hints:

```bash
extract-video-info "video.mp4" --outdir work/video-evidence --fps 1 --ocr-langs rus,eng
```

If the requested Tesseract language data is not installed locally, install it with your OS package manager or explicitly allow a download into the output directory:

```bash
extract-video-info "video.mp4" --outdir work/video-evidence --fps 1 --ocr-langs rus,eng --download-ocr-langs
```

Outputs include:

- `metadata.json`: source metadata from `yt-dlp` or local-file metadata.
- `ffprobe.json`: video stream details.
- `frames/`: sampled review frames.
- `sheets/`: contact sheets generated with Pillow.
- `ocr.txt`: optional Tesseract OCR output.
- `evidence_summary.md`: review guide with paths and timing formulas.

## Agent Skill Usage

The canonical skill lives at:

```text
skills/extract-video-info/SKILL.md
```

Use that file as the source of truth. Adapter files in this repo point back to it instead of duplicating the full workflow.

Supported surfaces:

| Agent/tool | Files included |
| --- | --- |
| OpenAI Codex | `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`, `.agents/skills/extract-video-info/SKILL.md`, `skills/extract-video-info/SKILL.md` |
| Claude Code | `.claude-plugin/plugin.json`, `skills/extract-video-info/SKILL.md`, `CLAUDE.md` |
| Cursor | `.cursor/rules/extract-video-info.mdc` |
| Gemini / Antigravity-style agents | `GEMINI.md`, `AGENTS.md`, `skills/extract-video-info/SKILL.md` |
| GitHub Copilot | `.github/copilot-instructions.md`, `.github/skills/extract-video-info/SKILL.md`, `AGENTS.md` |
| Generic agents | `AGENTS.md`, `skills/extract-video-info/SKILL.md` |

## Copy-Paste Agent Install Prompts

For an agent-assisted install, copy a prompt from [docs/agent-install-prompts.md](docs/agent-install-prompts.md). The prompts ask the agent to clone or install this repository, use the correct adapter for its environment, verify the CLI, and avoid committing generated media, cookies, credentials, OCR output, or evidence files.

## Platform Access Policy

This project does not bypass access controls.

Supported inputs are:

- Public video URLs that `yt-dlp` can access.
- User-provided local video files.
- Authenticated downloads only when the user has legitimate access and explicitly chooses to provide cookies or credentials to their own tooling.

Never commit cookies, credentials, downloaded videos, generated frames, OCR output, or evidence directories. The repository `.gitignore` excludes common local evidence and credential patterns, but users should still inspect `git status` before publishing.

Live social-platform download behavior can change without warning. CI tests use local fixtures and do not depend on Instagram, TikTok, or YouTube being reachable.

## Development

```bash
python -m pip install -e ".[dev]"
python -m pytest
python -m ruff check .
python -m ruff format --check .
```

## Repository Layout

```text
src/extract_video_info/          Python CLI package
skills/extract-video-info/       Canonical Agent Skill
.codex-plugin/                   Codex plugin manifest
.claude-plugin/                  Claude Code plugin manifest
.agents/                         Codex repo skill and marketplace adapters
.cursor/rules/                   Cursor project rule adapter
.github/                         Copilot instructions, CI, issue templates
docs/                            Agent compatibility and install prompt notes
```

## License

MIT. See `LICENSE`.
