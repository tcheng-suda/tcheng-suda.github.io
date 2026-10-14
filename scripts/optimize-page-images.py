#!/usr/bin/env python3
"""Regenerate page WebP assets on macOS (sips + cwebp from brew install webp)."""
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
if not shutil.which("cwebp"):
    raise SystemExit("Install the WebP encoder first: brew install webp")


def convert(source, destination, max_edge=None):
    dimensions = subprocess.check_output([
        "sips", "-g", "pixelWidth", "-g", "pixelHeight", str(source)
    ], text=True)
    width = int(re.search(r"pixelWidth: (\d+)", dimensions).group(1))
    height = int(re.search(r"pixelHeight: (\d+)", dimensions).group(1))
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="page-image-") as temp:
        resized = Path(temp) / "image.png"
        command = ["sips", "-s", "format", "png"]
        if max_edge and max(width, height) > max_edge:
            command += ["-Z", str(max_edge)]
        subprocess.run(command + [str(source), "--out", str(resized)],
                       check=True, capture_output=True)
        subprocess.run(["cwebp", "-quiet", "-q", "85", "-m", "6",
                        str(resized), "-o", str(destination)], check=True)


def portrait(match):
    source, alt = match.groups()
    # Resolve original sources on subsequent runs as well.
    stem = Path(source).stem
    if source.startswith("/images/people-previews/"):
        candidates = [p for p in (ROOT / "images").glob(stem + ".*")
                      if p.suffix.lower() in {".jpg", ".jpeg", ".png"}]
        if len(candidates) != 1:
            raise SystemExit(f"Cannot uniquely resolve original portrait: {stem}")
        original = candidates[0]
    else:
        original = ROOT / source.lstrip("/")
    destination = ROOT / "images" / "people-previews" / (stem + ".webp")
    # Cards display 100 x 100 pixels; 300 pixels preserves detail on Retina screens.
    convert(original, destination, max_edge=300)
    return (f'<img src="/images/people-previews/{destination.name}" alt="{alt}" '
            'width="100" height="100" loading="lazy" decoding="async">')


page = ROOT / "about.md"
content, count = re.subn(r'<img src="(/images/[^\"]+)" alt="([^\"]+)"[^>]*>',
                         portrait, page.read_text())
if not count:
    raise SystemExit("No portraits found; check about.md")
page.write_text(content)
for name in ["oaao", "oaao-d2"]:
    convert(ROOT / "images" / (name + ".png"),
            ROOT / "images" / "covers" / (name + ".webp"))
print(f"Generated {count} portrait previews and two cover images")
