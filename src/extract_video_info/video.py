from __future__ import annotations

import json
import shutil
from pathlib import Path

from .tools import require_command, run_command


def probe_video(video: Path, outdir: Path) -> dict:
    require_command("ffprobe", "Install FFmpeg and make sure ffprobe is on PATH.")
    result = run_command(
        [
            "ffprobe",
            "-v",
            "error",
            "-print_format",
            "json",
            "-show_format",
            "-show_streams",
            str(video),
        ]
    )
    (outdir / "ffprobe.json").write_text(result.stdout, encoding="utf-8")
    return json.loads(result.stdout)


def extract_frames(
    video: Path,
    outdir: Path,
    *,
    fps: float,
    frame_width: int,
    start: float = 0.0,
    duration: float | None = None,
) -> list[Path]:
    require_command("ffmpeg", "Install FFmpeg and make sure ffmpeg is on PATH.")
    frames_dir = outdir / "frames"
    if frames_dir.exists():
        shutil.rmtree(frames_dir)
    frames_dir.mkdir(parents=True, exist_ok=True)

    command = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"]
    if start > 0:
        command += ["-ss", f"{start:g}"]
    command += ["-i", str(video)]
    if duration is not None:
        command += ["-t", f"{duration:g}"]
    command += [
        "-vf",
        f"fps={fps:g},scale={frame_width}:-1",
        "-q:v",
        "3",
        str(frames_dir / "frame_%04d.jpg"),
    ]
    run_command(command)
    return sorted(frames_dir.glob("frame_*.jpg"))


def extract_still(video: Path, output: Path, *, timestamp: float) -> Path:
    require_command("ffmpeg", "Install FFmpeg and make sure ffmpeg is on PATH.")
    output.parent.mkdir(parents=True, exist_ok=True)
    run_command(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-ss",
            f"{timestamp:g}",
            "-i",
            str(video),
            "-frames:v",
            "1",
            "-q:v",
            "2",
            str(output),
        ]
    )
    return output
