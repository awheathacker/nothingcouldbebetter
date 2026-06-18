#!/usr/bin/env python3
"""Generate placeholder gradient images for nothingcouldbebetter site."""
from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = "/home/greyphilosophy/projects/nothingcouldbebetter/backend/static/images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_gradient_image(filename, width, height, color_start, color_end):
    """Create a smooth gradient image."""
    img = Image.new('RGB', (width, height), color_start)
    pixels = img.load()
    for x in range(width):
        for y in range(height):
            t = (x / width) * 0.6 + (y / height) * 0.4
            r = int(color_start[0] * (1-t) + color_end[0] * t)
            g = int(color_start[1] * (1-t) + color_end[1] * t)
            b = int(color_start[2] * (1-t) + color_end[2] * t)
            pixels[x, y] = (r, g, b)
    img.save(filename)
    print(f"Created: {filename} ({width}x{height})")

# Dark void themed gradient images
configs = [
    ("hero_nebula.png", 1024, 512, (10, 8, 30), (25, 15, 50)),
    ("void_bg.png", 1024, 1024, (8, 6, 22), (18, 12, 40)),
    ("stars_gallery.png", 1024, 512, (6, 10, 28), (14, 15, 45)),
    ("void_avatar.png", 256, 256, (15, 12, 35), (25, 18, 50)),
    ("forum_header.png", 1024, 200, (12, 8, 28), (20, 14, 42)),
    ("match_background.png", 1024, 300, (14, 10, 32), (22, 16, 48)),
]

for fname, w, h, c1, c2 in configs:
    create_gradient_image(os.path.join(OUTPUT_DIR, fname), w, h, c1, c2)

print("\nDone. Placeholder gradient images created.")
