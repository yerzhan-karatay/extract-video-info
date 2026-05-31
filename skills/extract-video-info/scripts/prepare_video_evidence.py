#!/usr/bin/env python3
"""Run the Extract Video Info CLI from a source checkout or installed package."""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    repo_src = Path(__file__).resolve().parents[3] / "src"
    if repo_src.exists():
        sys.path.insert(0, str(repo_src))

    try:
        from extract_video_info.cli import main as cli_main
    except ModuleNotFoundError as exc:
        raise SystemExit(
            "extract-video-info is not installed and the source package was not found. "
            'Install it with `python -m pip install ".[dev]"` from the repository root.'
        ) from exc

    return cli_main()


if __name__ == "__main__":
    raise SystemExit(main())
