from __future__ import annotations

from pathlib import Path

from extract_video_info.report import summarize_metadata, summarize_probe, write_summary


def test_summarize_metadata_uses_known_fields() -> None:
    lines = summarize_metadata(
        {
            "id": "abc",
            "title": "Example",
            "ignored": "nope",
            "duration": 12.5,
        }
    )

    assert "- id: abc" in lines
    assert "- title: Example" in lines
    assert "- duration: 12.5" in lines
    assert all("ignored" not in line for line in lines)


def test_summarize_probe_prefers_video_stream() -> None:
    lines = summarize_probe(
        {
            "format": {"duration": "20.0"},
            "streams": [
                {"codec_type": "audio"},
                {"codec_type": "video", "width": 1080, "height": 1920, "r_frame_rate": "30/1"},
            ],
        }
    )

    assert "- width: 1080" in lines
    assert "- height: 1920" in lines
    assert "- r_frame_rate: 30/1" in lines
    assert "- duration: 20.0" in lines


def test_write_summary_creates_review_document(tmp_path: Path) -> None:
    frame = tmp_path / "frames" / "frame_0001.jpg"
    frame.parent.mkdir()
    frame.write_bytes(b"fake")
    summary = write_summary(
        tmp_path,
        source="video.mp4",
        video=Path("video.mp4"),
        metadata={"title": "Example"},
        probe={"streams": [{"codec_type": "video", "width": 100, "height": 200}]},
        frames=[frame],
        sheets=[
            {
                "sheet": "sheet.jpg",
                "frame_start": 1,
                "frame_end": 1,
                "approx_time_start_seconds": 0.0,
                "approx_time_end_seconds": 0.0,
            }
        ],
        ocr_path=None,
        fps=1.0,
        start=0.0,
    )

    text = summary.read_text(encoding="utf-8")
    assert "Video Evidence Summary" in text
    assert "- title: Example" in text
    assert "sheet.jpg" in text
    assert "OCR not requested" in text
