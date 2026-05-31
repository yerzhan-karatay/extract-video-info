from __future__ import annotations

import shutil
from pathlib import Path

from PIL import Image


def make_contact_sheets(
    frames: list[Path],
    outdir: Path,
    *,
    cols: int,
    rows: int,
    gap: int,
    start: float,
    fps: float,
    background: tuple[int, int, int] = (255, 255, 255),
) -> list[dict]:
    sheets_dir = outdir / "sheets"
    if sheets_dir.exists():
        shutil.rmtree(sheets_dir)
    sheets_dir.mkdir(parents=True, exist_ok=True)

    if not frames:
        return []

    capacity = max(1, cols * rows)
    sheet_maps: list[dict] = []

    for offset in range(0, len(frames), capacity):
        chunk = frames[offset : offset + capacity]
        images = [Image.open(frame).convert("RGB") for frame in chunk]
        try:
            frame_width = max(image.width for image in images)
            frame_height = max(image.height for image in images)
            sheet_width = cols * frame_width + (cols + 1) * gap
            sheet_height = rows * frame_height + (rows + 1) * gap
            sheet = Image.new("RGB", (sheet_width, sheet_height), background)

            for index, image in enumerate(images):
                row = index // cols
                col = index % cols
                x = gap + col * (frame_width + gap)
                y = gap + row * (frame_height + gap)
                sheet.paste(image, (x, y))

            sheet_number = len(sheet_maps) + 1
            sheet_path = sheets_dir / f"sheet_{sheet_number:03d}.jpg"
            sheet.save(sheet_path, quality=90, optimize=True)
        finally:
            for image in images:
                image.close()

        frame_start = offset + 1
        frame_end = offset + len(chunk)
        sheet_maps.append(
            {
                "sheet": str(sheet_path),
                "frame_start": frame_start,
                "frame_end": frame_end,
                "approx_time_start_seconds": round(start + (frame_start - 1) / fps, 3),
                "approx_time_end_seconds": round(start + (frame_end - 1) / fps, 3),
            }
        )

    return sheet_maps
