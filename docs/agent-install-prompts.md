# Agent Install Prompts

These prompts are intended for users who want their coding agent to install or use Extract Video Info without manually reading every adapter file first.

Replace `<target-video-url-or-path>` with a public video URL or local file path when you want the agent to perform an extraction.

## Universal Prompt

```text
Please install and use Extract Video Info from https://github.com/yerzhan-karatay/extract-video-info.

Clone the repository into a normal local development folder if it is not already available. Use the adapter that matches your environment, and treat skills/extract-video-info/SKILL.md as the source of truth. If plugin installation is unavailable, use the repository checkout directly.

Verify the install with:
- python -m pip install -e ".[dev]"
- python -m extract_video_info --help

When extracting from <target-video-url-or-path>, write temporary evidence under work/ and do not commit cookies, credentials, downloaded media, frames, OCR output, or generated evidence files.
```

## Codex Prompt

```text
Please install the Extract Video Info Codex skill/plugin from https://github.com/yerzhan-karatay/extract-video-info.

Prefer .codex-plugin/plugin.json and skills/extract-video-info/SKILL.md. If this Codex environment cannot install plugins directly, clone the repo and use the skill from skills/extract-video-info/SKILL.md in place.

After installing, verify:
- python -m pip install -e ".[dev]"
- python -m extract_video_info --help

For video extraction tasks, keep generated evidence in work/ and never commit cookies, credentials, downloaded media, OCR output, or frame sheets.
```

## Claude Code Prompt

```text
Please install or load the Claude Code plugin from https://github.com/yerzhan-karatay/extract-video-info.

Use .claude-plugin/plugin.json and the canonical skill at skills/extract-video-info/SKILL.md. If plugin installation is unavailable, clone the repository and follow the skill file directly.

Verify:
- python -m pip install -e ".[dev]"
- python -m extract_video_info --help

Do not commit generated media, cookies, credentials, OCR output, or evidence directories.
```

## Cursor Prompt

```text
Please add Extract Video Info from https://github.com/yerzhan-karatay/extract-video-info to this Cursor workspace.

Use .cursor/rules/extract-video-info.mdc as the Cursor rule and skills/extract-video-info/SKILL.md as the canonical workflow. If needed, clone the repository and reference it from the current workspace.

Verify:
- python -m pip install -e ".[dev]"
- python -m extract_video_info --help
```

## Gemini or Generic Agent Prompt

```text
Please use Extract Video Info from https://github.com/yerzhan-karatay/extract-video-info.

Read AGENTS.md, GEMINI.md if relevant, and skills/extract-video-info/SKILL.md. Clone the repository if it is not already available. Use the Python CLI for evidence preparation and visually verify generated frames before returning extracted facts.

Keep all temporary evidence in work/ and do not commit private media, cookies, credentials, OCR output, or generated evidence.
```
