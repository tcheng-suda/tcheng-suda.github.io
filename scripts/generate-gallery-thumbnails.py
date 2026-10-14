#!/usr/bin/env python3
"""Regenerate gallery thumbnails with macOS sips; no Python packages needed."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
gallery = ROOT / "gallery.md"
output = ROOT / "images" / "thumbnails"
output.mkdir(parents=True, exist_ok=True)


def thumbnail(match):
    source, alt = match.groups()
    destination = output / (Path(source).stem + ".jpg")
    subprocess.run([
        "sips", "-s", "format", "jpeg", "-s", "formatOptions", "78",
        "-Z", "960", str(ROOT / source.lstrip("/")),
        "--out", str(destination),
    ], check=True, capture_output=True)
    dimensions = subprocess.check_output([
        "sips", "-g", "pixelWidth", "-g", "pixelHeight", str(destination)
    ], text=True)
    width = re.search(r"pixelWidth: (\d+)", dimensions).group(1)
    height = re.search(r"pixelHeight: (\d+)", dimensions).group(1)
    return (
        f'<a href="{source}" target="_blank" rel="noopener">'
        f'<img src="/images/thumbnails/{destination.name}" alt="{alt}" '
        f'width="{width}" height="{height}" loading="lazy" decoding="async"></a>'
    )


content = gallery.read_text()
content, count = re.subn(
    r'<a href="(/images/[^\"]+)"[^>]*><img [^>]*alt="([^\"]+)"[^>]*></a>',
    thumbnail, content,
)
if not count:
    raise SystemExit("No gallery images found")
gallery.write_text(content)
print(f"Generated {count} thumbnails (maximum edge: 960 pixels)")
