from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


def summarize_metadata(metadata: dict) -> list[str]:
    keys = ["id", "title", "description", "uploader", "channel", "upload_date", "duration", "webpage_url", "path"]
    return [f"- {key}: {metadata[key]}" for key in keys if metadata.get(key) is not None]


def summarize_probe(probe: dict) -> list[str]:
    video_stream = next((stream for stream in probe.get("streams", []) if stream.get("codec_type") == "video"), {})
    fmt = probe.get("format", {})
    lines = []
    for key in ["width", "height", "r_frame_rate", "duration"]:
        value = video_stream.get(key) or fmt.get(key)
        if value is not None:
            lines.append(f"- {key}: {value}")
    return lines


def write_summary(
    outdir: Path,
    *,
    source: str,
    video: Path,
    metadata: dict,
    probe: dict,
    frames: list[Path],
    sheets: list[dict],
    ocr_path: Path | None,
    fps: float,
    start: float,
) -> Path:
    summary = outdir / "evidence_summary.md"
    lines = [
        "# Video Evidence Summary",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        f"Source: {source}",
        f"Video file: {video}",
        "",
        "## Metadata",
        "",
        *summarize_metadata(metadata),
        "",
        "## Video Probe",
        "",
        *summarize_probe(probe),
        "",
        "## Frames",
        "",
        f"- Extracted frames: {len(frames)}",
        f"- Sampling fps: {fps:g}",
        f"- First sampled time: {start:g}s",
        "- Approximate time formula: start + (frame_index - 1) / fps",
        "",
        "## Contact Sheets",
        "",
    ]
    if sheets:
        for sheet in sheets:
            lines.append(
                f"- {sheet['sheet']}: frames {sheet['frame_start']}-{sheet['frame_end']}, "
                f"approx {sheet['approx_time_start_seconds']}-{sheet['approx_time_end_seconds']}s"
            )
    else:
        lines.append("- No sheets created.")

    lines += [
        "",
        "## OCR",
        "",
        f"- OCR output: {ocr_path}" if ocr_path else "- OCR not requested.",
        "",
        "## Suggested Review",
        "",
        "1. Inspect every contact sheet for distinct visible text or item changes.",
        "2. Extract full-resolution stills for hard-to-read frames with `ffmpeg`.",
        "3. Treat OCR as candidate text and verify against the frame.",
        "4. Use public web verification only to resolve exact spellings or authors/brands.",
    ]
    summary.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return summary
