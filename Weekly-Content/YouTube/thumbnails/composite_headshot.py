#!/usr/bin/env python3
"""
Composite headshot into all 12 YouTube thumbnails.
Usage: python3 composite_headshot.py <headshot_path>

The headshot will be cropped to head+shoulders, edge-blended
into the left side of each thumbnail, replacing the placeholder.
"""

import sys
import os
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageOps

THUMB_DIR = os.path.dirname(os.path.abspath(__file__))


def create_fade_mask(width, height, fade_start_pct=0.65):
    """Create a left-to-right gradient mask for edge blending."""
    mask = Image.new("L", (width, height), 255)
    draw = ImageDraw.Draw(mask)
    fade_start = int(width * fade_start_pct)
    for x in range(fade_start, width):
        alpha = int(255 * (1.0 - (x - fade_start) / (width - fade_start)))
        draw.line([(x, 0), (x, height)], fill=alpha)
    return mask


def create_bottom_fade(width, height, fade_pct=0.15):
    """Create bottom edge fade."""
    mask = Image.new("L", (width, height), 255)
    draw = ImageDraw.Draw(mask)
    fade_start = int(height * (1 - fade_pct))
    for y in range(fade_start, height):
        alpha = int(255 * (1.0 - (y - fade_start) / (height - fade_start)))
        draw.line([(0, y), (width, y)], fill=alpha)
    return mask


def prepare_headshot(headshot_path, target_width, target_height, colorize=None):
    """
    Load and prepare headshot for compositing.
    - Crop to upper body (head + shoulders)
    - Resize to target dimensions
    - Create edge-blending mask
    - Optionally add color tint
    """
    img = Image.open(headshot_path).convert("RGBA")

    # Crop to head and shoulders (top 85% of image, center horizontally)
    w, h = img.size
    crop_top = 0
    crop_bottom = int(h * 0.90)
    crop_left = int(w * 0.05)
    crop_right = int(w * 0.95)
    img = img.crop((crop_left, crop_top, crop_right, crop_bottom))

    # Resize to fill target area
    img = img.resize((target_width, target_height), Image.LANCZOS)

    # Increase contrast slightly
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.2)

    # Create combined fade mask (right edge + bottom edge)
    right_fade = create_fade_mask(target_width, target_height, fade_start_pct=0.60)
    bottom_fade = create_bottom_fade(target_width, target_height, fade_pct=0.12)

    # Combine masks
    combined_mask = Image.new("L", (target_width, target_height))
    for x in range(target_width):
        for y in range(target_height):
            r_val = right_fade.getpixel((x, y))
            b_val = bottom_fade.getpixel((x, y))
            combined_mask.putpixel((x, y), min(r_val, b_val))

    # Apply tint if requested
    if colorize:
        r_tint, g_tint, b_tint = colorize
        tinted = Image.new("RGBA", img.size)
        for x in range(img.width):
            for y in range(img.height):
                pr, pg, pb, pa = img.getpixel((x, y))
                # Blend original with tint (30% tint)
                blend = 0.25
                nr = int(pr * (1 - blend) + r_tint * blend)
                ng = int(pg * (1 - blend) + g_tint * blend)
                nb = int(pb * (1 - blend) + b_tint * blend)
                tinted.putpixel((x, y), (nr, ng, nb, pa))
        img = tinted

    return img, combined_mask


def prepare_headshot_fast(headshot_path, target_width, target_height, tint_color=None):
    """
    Fast version using numpy-free approach.
    Loads headshot, crops, resizes, and creates alpha mask for blending.
    """
    img = Image.open(headshot_path).convert("RGB")

    # Crop to head and shoulders
    w, h = img.size
    crop_box = (int(w * 0.05), 0, int(w * 0.95), int(h * 0.90))
    img = img.crop(crop_box)

    # Resize
    img = img.resize((target_width, target_height), Image.LANCZOS)

    # Boost contrast
    img = ImageEnhance.Contrast(img).enhance(1.15)
    img = ImageEnhance.Brightness(img).enhance(1.05)

    # Apply optional color tint via overlay blend
    if tint_color:
        overlay = Image.new("RGB", img.size, tint_color)
        img = Image.blend(img, overlay, 0.15)

    # Convert to RGBA
    img = img.convert("RGBA")

    # Create fade mask for right edge
    mask = Image.new("L", (target_width, target_height), 255)
    draw = ImageDraw.Draw(mask)

    # Right edge fade (starts at 60% of width)
    fade_start = int(target_width * 0.58)
    for x in range(fade_start, target_width):
        alpha = int(255 * (1.0 - (x - fade_start) / (target_width - fade_start)) ** 1.5)
        draw.line([(x, 0), (x, target_height)], fill=alpha)

    # Bottom edge fade (last 10%)
    bottom_start = int(target_height * 0.88)
    for y in range(bottom_start, target_height):
        alpha_b = int(255 * (1.0 - (y - bottom_start) / (target_height - bottom_start)))
        for x in range(target_width):
            current = mask.getpixel((x, y))
            mask.putpixel((x, y), min(current, alpha_b))

    return img, mask


def composite_into_thumbnail(thumb_path, headshot_img, mask, x_offset=0, y_offset=0):
    """Composite the headshot into an existing thumbnail."""
    thumb = Image.open(thumb_path).convert("RGBA")

    # Create a layer with the headshot
    layer = Image.new("RGBA", thumb.size, (0, 0, 0, 0))
    layer.paste(headshot_img, (x_offset, y_offset))

    # Apply mask to the layer
    full_mask = Image.new("L", thumb.size, 0)
    full_mask.paste(mask, (x_offset, y_offset))

    # Composite
    result = Image.composite(layer, thumb, full_mask)

    # Save as RGB PNG
    result = result.convert("RGB")
    result.save(thumb_path, quality=95)
    return thumb_path


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 composite_headshot.py <headshot_image_path>")
        print("\nThe headshot will be composited into all 12 thumbnails.")
        sys.exit(1)

    headshot_path = sys.argv[1]
    if not os.path.exists(headshot_path):
        print(f"Error: Headshot not found at {headshot_path}")
        sys.exit(1)

    print(f"Loading headshot: {headshot_path}")

    # Define thumbnail configs: (filename, headshot_width, headshot_height, x, y, tint)
    configs = [
        # Video 1: AI + Retirement
        ("video1-thumb-a.png", 520, 650, 10, 50, (10, 15, 40)),
        ("video1-thumb-b.png", 510, 640, 10, 60, (15, 10, 35)),
        ("video1-thumb-c.png", 500, 640, 0, 50, (5, 20, 45)),
        # Video 2: Fear/Warning
        ("video2-thumb-a.png", 520, 650, 10, 50, (30, 5, 5)),
        ("video2-thumb-b.png", 500, 620, 0, 70, (15, 15, 25)),
        ("video2-thumb-c.png", 490, 620, 0, 70, (20, 5, 10)),
        # Video 3: Wealth Transfer
        ("video3-thumb-a.png", 510, 640, 0, 50, (15, 10, 5)),
        ("video3-thumb-b.png", 500, 620, 0, 70, (10, 15, 30)),
        ("video3-thumb-c.png", 500, 640, 0, 50, (5, 5, 15)),
        # Video 4: AI Money Guide
        ("video4-thumb-a.png", 500, 640, 0, 50, (10, 30, 60)),
        ("video4-thumb-b.png", 500, 640, 0, 50, (15, 25, 50)),
        ("video4-thumb-c.png", 500, 640, 0, 50, (10, 20, 45)),
    ]

    for filename, hw, hh, x, y, tint in configs:
        thumb_path = os.path.join(THUMB_DIR, filename)
        if not os.path.exists(thumb_path):
            print(f"  Skipping {filename} (not found)")
            continue

        print(f"  Processing {filename}...", end=" ")
        headshot_img, mask = prepare_headshot_fast(headshot_path, hw, hh, tint_color=tint)
        composite_into_thumbnail(thumb_path, headshot_img, mask, x, y)
        print("done")

    print("\nAll thumbnails updated with headshot!")
    print(f"Output: {THUMB_DIR}")


if __name__ == "__main__":
    main()
