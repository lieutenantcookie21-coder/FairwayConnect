#!/usr/bin/env python3
"""Generate FairwayConnect app icons (flag on a green) with PIL."""
from PIL import Image, ImageDraw

GREEN = (10, 110, 58)
DARK = (7, 80, 42)
WHITE = (255, 255, 255)
RED = (203, 17, 45)

def make(size, path):
    img = Image.new("RGB", (size, size), GREEN)
    d = ImageDraw.Draw(img)
    s = size / 100.0  # work in a 100x100 coordinate space

    # subtle darker "fairway stripe" diagonal
    d.polygon([(0, 100 * s), (100 * s, 0), (100 * s, 35 * s), (0, 100 * s)], fill=DARK)

    # putting green (light ellipse near bottom)
    d.ellipse([18 * s, 62 * s, 82 * s, 88 * s], fill=(46, 158, 95))

    # hole
    d.ellipse([44 * s, 72 * s, 56 * s, 78 * s], fill=DARK)

    # flagstick
    d.rectangle([48.5 * s, 22 * s, 51.5 * s, 75 * s], fill=WHITE)

    # flag
    d.polygon([(51.5 * s, 22 * s), (78 * s, 30 * s), (51.5 * s, 38 * s)], fill=RED)

    # golf ball
    d.ellipse([28 * s, 76 * s, 36 * s, 84 * s], fill=WHITE)

    img.save(path)
    print(f"wrote {path} ({size}x{size})")

if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "icons")
    os.makedirs(out, exist_ok=True)
    for size, name in [(1024, "icon-1024.png"), (512, "icon-512.png"),
                       (192, "icon-192.png"), (180, "icon-180.png")]:
        make(size, os.path.join(out, name))
