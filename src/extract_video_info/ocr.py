from __future__ import annotations

import os
import subprocess
import urllib.request
from pathlib import Path

from .tools import require_command


def parse_languages(value: str | None) -> list[str]:
    if not value:
        return []
    return [lang.strip() for lang in value.replace("+", ",").split(",") if lang.strip()]


def available_tesseract_languages() -> set[str]:
    result = subprocess.run(
        ["tesseract", "--list-langs"],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        return set()
    lines = [line.strip() for line in (result.stdout + "\n" + result.stderr).splitlines()]
    return {line for line in lines if line and not line.startswith("List of available")}


def download_tesseract_language(lang: str, tessdata_dir: Path) -> Path:
    tessdata_dir.mkdir(parents=True, exist_ok=True)
    target = tessdata_dir / f"{lang}.traineddata"
    if target.exists():
        return target
    url = f"https://github.com/tesseract-ocr/tessdata/raw/main/{lang}.traineddata"
    urllib.request.urlretrieve(url, target)
    return target


def run_ocr(
    frames: list[Path],
    outdir: Path,
    *,
    languages: str | None,
    every: int,
    start: float,
    fps: float,
    download_missing: bool = False,
) -> Path | None:
    langs = parse_languages(languages)
    if not langs:
        return None

    require_command("tesseract", "Install Tesseract or omit --ocr-langs.")
    available = available_tesseract_languages()
    env = os.environ.copy()
    missing = sorted(lang for lang in langs if lang not in available)
    if missing and not download_missing:
        missing_list = ", ".join(missing)
        raise RuntimeError(
            f"Missing Tesseract language data: {missing_list}. "
            "Install the language package locally or rerun with --download-ocr-langs."
        )
    if missing:
        tessdata_dir = outdir / "tessdata"
        for lang in missing:
            download_tesseract_language(lang, tessdata_dir)
        env["TESSDATA_PREFIX"] = str(tessdata_dir)

    ocr_path = outdir / "ocr.txt"
    language_arg = "+".join(langs)
    every = max(1, every)
    with ocr_path.open("w", encoding="utf-8") as handle:
        for index, frame in enumerate(frames, start=1):
            if (index - 1) % every != 0:
                continue
            result = subprocess.run(
                ["tesseract", str(frame), "stdout", "-l", language_arg, "--psm", "6"],
                text=True,
                capture_output=True,
                env=env,
                check=False,
            )
            text = result.stdout.strip()
            if text:
                approx_time = start + (index - 1) / fps
                handle.write(f"## {frame.name} approx {approx_time:.2f}s\n{text}\n\n")
    return ocr_path
