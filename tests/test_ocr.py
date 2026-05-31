from pathlib import Path
from unittest.mock import patch

import pytest

from extract_video_info.ocr import parse_languages, run_ocr


def test_parse_languages_accepts_commas_and_plus() -> None:
    assert parse_languages("rus,eng+jpn") == ["rus", "eng", "jpn"]


def test_parse_languages_handles_empty_value() -> None:
    assert parse_languages(None) == []
    assert parse_languages("") == []


def test_run_ocr_requires_explicit_language_download(tmp_path: Path) -> None:
    frame = tmp_path / "frame_0001.jpg"
    frame.write_bytes(b"not a real image")

    with (
        patch("extract_video_info.ocr.require_command"),
        patch("extract_video_info.ocr.available_tesseract_languages", return_value={"eng"}),
        pytest.raises(RuntimeError, match="--download-ocr-langs"),
    ):
        run_ocr([frame], tmp_path, languages="rus", every=1, start=0, fps=1)
