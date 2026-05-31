from __future__ import annotations

from pathlib import Path

from PIL import Image

from extract_video_info.sheets import make_contact_sheets


def make_frame(path: Path, color: tuple[int, int, int]) -> None:
    image = Image.new("RGB", (40, 60), color)
    image.save(path)


def test_make_contact_sheets_creates_expected_sheet(tmp_path: Path) -> None:
    frames_dir = tmp_path / "frames"
    frames_dir.mkdir()
    frames = []
    for index, color in enumerate([(255, 0, 0), (0, 255, 0), (0, 0, 255)], start=1):
        frame = frames_dir / f"frame_{index:04d}.jpg"
        make_frame(frame, color)
        frames.append(frame)

    sheets = make_contact_sheets(frames, tmp_path, cols=2, rows=2, gap=4, start=10.0, fps=1.0)

    assert len(sheets) == 1
    assert sheets[0]["frame_start"] == 1
    assert sheets[0]["frame_end"] == 3
    assert sheets[0]["approx_time_start_seconds"] == 10.0
    assert sheets[0]["approx_time_end_seconds"] == 12.0
    assert Path(sheets[0]["sheet"]).exists()


def test_make_contact_sheets_splits_chunks(tmp_path: Path) -> None:
    frames_dir = tmp_path / "frames"
    frames_dir.mkdir()
    frames = []
    for index in range(5):
        frame = frames_dir / f"frame_{index + 1:04d}.jpg"
        make_frame(frame, (index * 20, index * 20, index * 20))
        frames.append(frame)

    sheets = make_contact_sheets(frames, tmp_path, cols=2, rows=2, gap=0, start=0.0, fps=2.0)

    assert len(sheets) == 2
    assert sheets[0]["frame_end"] == 4
    assert sheets[1]["frame_start"] == 5
    assert sheets[1]["approx_time_start_seconds"] == 2.0
