from __future__ import annotations

import json
import sys
from pathlib import Path

from .tools import run_command


def is_url(value: str) -> bool:
    return value.startswith(("http://", "https://"))


def ytdlp_command() -> list[str]:
    return [sys.executable, "-m", "yt_dlp"]


def dump_metadata(source: str, outdir: Path) -> dict:
    result = run_command(ytdlp_command() + ["--dump-json", "--no-warnings", "--no-playlist", source])
    output = result.stdout
    metadata_path = outdir / "metadata.json"
    metadata_path.write_text(output, encoding="utf-8")
    lines = [line for line in output.splitlines() if line.strip()]
    return json.loads(lines[-1]) if lines else {}


def download_video(source: str, outdir: Path) -> Path:
    output_template = str(outdir / "video.%(ext)s")
    result = run_command(
        ytdlp_command()
        + [
            "--no-warnings",
            "--no-playlist",
            "--merge-output-format",
            "mp4",
            "-o",
            output_template,
            "--print",
            "after_move:filepath",
            source,
        ]
    )

    for line in reversed([line.strip() for line in result.stdout.splitlines() if line.strip()]):
        candidate = Path(line).expanduser()
        if candidate.exists():
            return candidate.resolve()

    candidates = sorted(outdir.glob("video.*"), key=lambda path: path.stat().st_mtime, reverse=True)
    if not candidates:
        raise RuntimeError("yt-dlp completed but no downloaded video file was found")
    return candidates[0].resolve()
