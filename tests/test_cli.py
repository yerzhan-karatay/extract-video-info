from __future__ import annotations

import argparse

import pytest

from extract_video_info.cli import build_parser, validate_args


def parse_args(*args: str) -> argparse.Namespace:
    return build_parser().parse_args(list(args))


def test_validate_args_accepts_defaults() -> None:
    validate_args(parse_args("video.mp4"))


def test_validate_args_rejects_invalid_fps() -> None:
    with pytest.raises(ValueError, match="fps"):
        validate_args(parse_args("video.mp4", "--fps", "0"))


def test_parser_accepts_ocr_languages() -> None:
    args = parse_args("video.mp4", "--ocr-langs", "rus,eng", "--ocr-every", "3", "--download-ocr-langs")

    assert args.ocr_langs == "rus,eng"
    assert args.ocr_every == 3
    assert args.download_ocr_langs is True
