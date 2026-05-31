from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .downloader import download_video, dump_metadata, is_url
from .ocr import run_ocr
from .report import write_summary
from .sheets import make_contact_sheets
from .tools import CommandError
from .video import extract_frames, probe_video


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="extract-video-info",
        description="Prepare reviewable evidence from a social video URL or local video file.",
    )
    parser.add_argument("source", help="Instagram/TikTok/YouTube URL or local video path")
    parser.add_argument("--outdir", default="work/video-evidence", help="Output directory for evidence")
    parser.add_argument("--fps", type=float, default=1.0, help="Frame sampling rate")
    parser.add_argument("--frame-width", type=int, default=360, help="Scaled review frame width")
    parser.add_argument("--start", type=float, default=0.0, help="Start time in seconds")
    parser.add_argument("--duration", type=float, default=None, help="Duration in seconds")
    parser.add_argument("--sheet-cols", type=int, default=5, help="Contact sheet columns")
    parser.add_argument("--sheet-rows", type=int, default=5, help="Contact sheet rows")
    parser.add_argument("--sheet-gap", type=int, default=4, help="Contact sheet gap in pixels")
    parser.add_argument("--no-sheets", action="store_true", help="Extract frames without creating contact sheets")
    parser.add_argument("--ocr-langs", default=None, help="Comma-separated Tesseract language codes, such as rus,eng")
    parser.add_argument("--ocr-every", type=int, default=1, help="OCR every Nth sampled frame")
    parser.add_argument(
        "--download-ocr-langs",
        action="store_true",
        help="Download missing Tesseract language data into the output directory",
    )
    return parser


def validate_args(args: argparse.Namespace) -> None:
    if args.fps <= 0:
        raise ValueError("--fps must be greater than 0")
    if args.frame_width <= 0:
        raise ValueError("--frame-width must be greater than 0")
    if args.sheet_cols <= 0 or args.sheet_rows <= 0:
        raise ValueError("--sheet-cols and --sheet-rows must be greater than 0")
    if args.sheet_gap < 0:
        raise ValueError("--sheet-gap cannot be negative")


def prepare_evidence(args: argparse.Namespace) -> Path:
    validate_args(args)
    outdir = Path(args.outdir).expanduser().resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    if is_url(args.source):
        metadata = dump_metadata(args.source, outdir)
        video = download_video(args.source, outdir)
    else:
        video = Path(args.source).expanduser().resolve()
        if not video.exists():
            raise FileNotFoundError(f"Local video not found: {video}")
        metadata = {"source_type": "local_file", "path": str(video)}
        (outdir / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    probe = probe_video(video, outdir)
    frames = extract_frames(
        video,
        outdir,
        fps=args.fps,
        frame_width=args.frame_width,
        start=args.start,
        duration=args.duration,
    )
    if not frames:
        raise RuntimeError("No frames were extracted")

    sheets = []
    if not args.no_sheets:
        sheets = make_contact_sheets(
            frames,
            outdir,
            cols=args.sheet_cols,
            rows=args.sheet_rows,
            gap=args.sheet_gap,
            start=args.start,
            fps=args.fps,
        )

    ocr_path = run_ocr(
        frames,
        outdir,
        languages=args.ocr_langs,
        every=args.ocr_every,
        start=args.start,
        fps=args.fps,
        download_missing=args.download_ocr_langs,
    )
    return write_summary(
        outdir,
        source=args.source,
        video=video,
        metadata=metadata,
        probe=probe,
        frames=frames,
        sheets=sheets,
        ocr_path=ocr_path,
        fps=args.fps,
        start=args.start,
    )


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        summary = prepare_evidence(args)
    except (CommandError, FileNotFoundError, RuntimeError, ValueError) as exc:
        print(f"extract-video-info: error: {exc}", file=sys.stderr)
        return 1

    outdir = summary.parent
    frames_count = len(list((outdir / "frames").glob("frame_*.jpg")))
    sheets_count = len(list((outdir / "sheets").glob("sheet_*.jpg"))) if (outdir / "sheets").exists() else 0
    print(f"[OK] Summary: {summary}")
    print(f"[OK] Frames: {outdir / 'frames'} ({frames_count} files)")
    if sheets_count:
        print(f"[OK] Sheets: {outdir / 'sheets'} ({sheets_count} files)")
    if (outdir / "ocr.txt").exists():
        print(f"[OK] OCR: {outdir / 'ocr.txt'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
