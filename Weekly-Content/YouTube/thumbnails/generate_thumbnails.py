#!/usr/bin/env python3
"""Generate 12 YouTube thumbnails for the corrected content strategy.
Topics: Retirement & Wealth, Contrarian / Anti-Wall Street positioning."""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os
import math

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
WIDTH, HEIGHT = 1280, 720


def get_font(size, bold=True):
    """Get the best available font."""
    font_paths = [
        "/System/Library/Fonts/Supplemental/Impact.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial Bold.ttf",
        "/System/Library/Fonts/SFCompact.ttf",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except Exception:
                continue
    return ImageFont.load_default()


def get_bold_font(size):
    return get_font(size)


def draw_text_with_outline(draw, position, text, font, fill, outline_color="black", outline_width=3):
    x, y = position
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx * dx + dy * dy <= outline_width * outline_width:
                draw.text((x + dx, y + dy), text, font=font, fill=outline_color)
    draw.text(position, text, font=font, fill=fill)


def create_gradient_bg(width, height, color1, color2):
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    for i in range(height):
        ratio = i / height
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    return img


def draw_chart_line(draw, x_start, y_start, x_end, y_end, color, width=3):
    points = []
    steps = 20
    for i in range(steps + 1):
        t = i / steps
        x = x_start + (x_end - x_start) * t
        progress = t ** 0.6
        noise = math.sin(t * 12) * 8
        y = y_start - (y_start - y_end) * progress + noise
        points.append((x, y))
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=color, width=width)


def add_vignette(img, strength=0.6):
    width, height = img.size
    vignette = Image.new("L", (width, height), 255)
    draw = ImageDraw.Draw(vignette)
    for i in range(50):
        alpha = int(255 * (1 - (i / 50) * strength))
        offset = i * max(width, height) // 100
        draw.ellipse([-offset, -offset, width + offset, height + offset], fill=alpha)
    black = Image.new("RGB", img.size, (0, 0, 0))
    result = Image.composite(img, black, vignette)
    return result


# ============================================================
# VIDEO 1: Wall Street Lied to You
# ============================================================

def video1_thumb_a():
    """$412,000 WALL ST LIED - intense/knowing look, red text, dark bg."""
    img = create_gradient_bg(WIDTH, HEIGHT, (15, 10, 20), (30, 15, 35))
    draw = ImageDraw.Draw(img)

    # Subtle downward chart in background (losses)
    for offset in range(4):
        draw_chart_line(draw, 600, 150 + offset, 1200, 600 + offset, (60, 20, 20), 2)

    # Placeholder space for headshot (left 40%)

    # Main text
    font_huge = get_bold_font(140)
    font_large = get_bold_font(80)
    font_med = get_bold_font(48)

    draw_text_with_outline(draw, (540, 80), "$412K", font_huge, (255, 50, 50), outline_width=5)

    # White divider
    draw.rectangle([540, 250, 1220, 256], fill=(255, 50, 50))

    draw_text_with_outline(draw, (540, 280), "WALL ST", font_large, (255, 255, 255), outline_width=4)
    draw_text_with_outline(draw, (540, 380), "LIED", font_large, (255, 255, 255), outline_width=4)

    # "EXPOSED" badge
    draw.rounded_rectangle([540, 500, 770, 570], radius=12, fill=(255, 50, 50))
    font_badge = get_bold_font(44)
    draw.text((560, 510), "EXPOSED", font=font_badge, fill=(255, 255, 255))

    img = add_vignette(img, 0.4)
    img.save(os.path.join(OUTPUT_DIR, "video1-thumb-a.png"), quality=95)
    print("Created: video1-thumb-a.png")


def video1_thumb_b():
    """THEY LIED + EXPOSED badge - yellow text, dark bg."""
    img = create_gradient_bg(WIDTH, HEIGHT, (15, 10, 15), (30, 20, 30))
    draw = ImageDraw.Draw(img)

    font_huge = get_bold_font(130)
    font_large = get_bold_font(90)

    draw_text_with_outline(draw, (540, 60), "THEY", font_huge, (255, 230, 0), outline_width=5)
    draw_text_with_outline(draw, (540, 200), "LIED", font_huge, (255, 230, 0), outline_width=5)

    # Red EXPOSED badge
    draw.rounded_rectangle([540, 370, 850, 460], radius=15, fill=(220, 30, 30))
    font_badge = get_bold_font(60)
    draw.text((565, 378), "EXPOSED", font=font_badge, fill=(255, 255, 255))

    # Subtitle
    font_med = get_bold_font(42)
    draw_text_with_outline(draw, (540, 500), "YOUR ADVISOR", font_med, (200, 200, 200), outline_width=2)
    draw_text_with_outline(draw, (540, 555), "KNEW THE WHOLE TIME", font_med, (255, 100, 100), outline_width=2)

    img = add_vignette(img, 0.4)
    img.save(os.path.join(OUTPUT_DIR, "video1-thumb-b.png"), quality=95)
    print("Created: video1-thumb-b.png")


def video1_thumb_c():
    """$412K + YOUR ADVISOR crossed out - stern look."""
    img = create_gradient_bg(WIDTH, HEIGHT, (10, 15, 35), (20, 25, 55))
    draw = ImageDraw.Draw(img)

    font_huge = get_bold_font(140)
    font_large = get_bold_font(70)

    draw_text_with_outline(draw, (520, 60), "$412K", font_huge, (255, 50, 50), outline_width=5)

    # "YOUR ADVISOR" with strikethrough
    draw_text_with_outline(draw, (520, 240), "YOUR", font_large, (180, 180, 180), outline_width=3)
    draw_text_with_outline(draw, (520, 330), "ADVISOR", font_large, (180, 180, 180), outline_width=3)
    # Strikethrough line
    draw.line([(520, 290), (900, 290)], fill=(255, 50, 50), width=6)
    draw.line([(520, 380), (930, 380)], fill=(255, 50, 50), width=6)

    # "EXPOSED" text below
    font_med = get_bold_font(55)
    draw_text_with_outline(draw, (520, 450), "THE TRUTH", font_med, (255, 230, 0), outline_width=3)

    # Red accent bar
    draw.rectangle([520, 530, 900, 536], fill=(255, 50, 50))

    img = add_vignette(img, 0.4)
    img.save(os.path.join(OUTPUT_DIR, "video1-thumb-c.png"), quality=95)
    print("Created: video1-thumb-c.png")


# ============================================================
# VIDEO 2: Rule Change Warning ($143,000)
# ============================================================

def video2_thumb_a():
    """$143K GONE - concerned, red tones, warning stripes."""
    img = create_gradient_bg(WIDTH, HEIGHT, (30, 5, 5), (50, 10, 15))
    draw = ImageDraw.Draw(img)

    # Warning stripes at top
    for i in range(0, WIDTH, 60):
        draw.polygon([(i, 0), (i + 30, 0), (i + 15, 20), (i - 15, 20)], fill=(200, 30, 30))

    font_huge = get_bold_font(140)
    font_large = get_bold_font(100)
    font_med = get_bold_font(48)

    draw_text_with_outline(draw, (560, 100), "$143K", font_huge, (255, 50, 50), outline_width=5)
    draw_text_with_outline(draw, (560, 280), "GONE", font_large, (255, 255, 255), outline_width=4)

    draw.rectangle([560, 420, 1200, 430], fill=(255, 50, 50))

    draw_text_with_outline(draw, (560, 450), "YOUR RETIREMENT", font_med, (200, 200, 200), outline_width=2)
    draw_text_with_outline(draw, (560, 510), "IS AT RISK", font_med, (255, 100, 100), outline_width=2)

    img = add_vignette(img, 0.5)
    img.save(os.path.join(OUTPUT_DIR, "video2-thumb-a.png"), quality=95)
    print("Created: video2-thumb-a.png")


def video2_thumb_b():
    """NEW RULE - govt building silhouette, yellow text."""
    img = create_gradient_bg(WIDTH, HEIGHT, (15, 15, 25), (25, 25, 45))
    draw = ImageDraw.Draw(img)

    # Government building silhouette
    bldg_color = (40, 40, 60)
    draw.rectangle([700, 350, 1250, 700], fill=bldg_color)
    for cx in range(730, 1250, 65):
        draw.rectangle([cx, 250, cx + 25, 350], fill=bldg_color)
    draw.polygon([(680, 250), (975, 100), (1270, 250)], fill=bldg_color)
    draw.ellipse([900, 30, 1050, 130], fill=bldg_color)

    # Red "NEW RULE" badge
    draw.rounded_rectangle([520, 80, 860, 180], radius=15, fill=(220, 30, 30))
    font_badge = get_bold_font(64)
    draw.text((545, 90), "NEW RULE", font=font_badge, fill=(255, 255, 255))

    font_huge = get_bold_font(100)
    font_large = get_bold_font(70)

    draw_text_with_outline(draw, (520, 220), "YOUR", font_large, (255, 230, 0), outline_width=3)
    draw_text_with_outline(draw, (520, 310), "RETIRE", font_huge, (255, 230, 0), outline_width=4)
    draw_text_with_outline(draw, (520, 430), "MENT", font_huge, (255, 230, 0), outline_width=4)

    draw.rounded_rectangle([520, 570, 700, 630], radius=10, fill=(220, 30, 30))
    font_yr = get_bold_font(42)
    draw.text((540, 577), "2026", font=font_yr, fill=(255, 255, 255))

    img = add_vignette(img, 0.4)
    img.save(os.path.join(OUTPUT_DIR, "video2-thumb-b.png"), quality=95)
    print("Created: video2-thumb-b.png")


def video2_thumb_c():
    """2026 CHANGE - crumbling dollar, red/dark."""
    img = create_gradient_bg(WIDTH, HEIGHT, (20, 5, 10), (40, 10, 20))
    draw = ImageDraw.Draw(img)

    # Large crumbling dollar sign
    font_dollar = get_bold_font(300)
    draw_text_with_outline(draw, (830, 100), "$", font_dollar, (80, 20, 20), outline_width=2)
    draw.line([(900, 100), (950, 250), (880, 350), (960, 500)], fill=(255, 50, 50), width=4)
    draw.line([(920, 150), (870, 300), (940, 400)], fill=(200, 30, 30), width=3)

    font_huge = get_bold_font(110)
    font_large = get_bold_font(60)

    draw_text_with_outline(draw, (500, 80), "2026", font_huge, (255, 50, 50), outline_width=4)
    draw_text_with_outline(draw, (500, 220), "CHANGE", font_huge, (255, 255, 255), outline_width=4)

    # Warning triangle
    tri_x, tri_y = 550, 400
    draw.polygon([(tri_x, tri_y + 80), (tri_x + 40, tri_y), (tri_x + 80, tri_y + 80)],
                fill=(255, 200, 0), outline=(0, 0, 0), width=3)
    font_excl = get_bold_font(50)
    draw.text((tri_x + 27, tri_y + 15), "!", font=font_excl, fill=(0, 0, 0))

    draw_text_with_outline(draw, (650, 410), "PROTECT", font_large, (255, 200, 200), outline_width=2)
    draw_text_with_outline(draw, (650, 485), "YOURSELF", font_large, (255, 200, 200), outline_width=2)

    img = add_vignette(img, 0.5)
    img.save(os.path.join(OUTPUT_DIR, "video2-thumb-c.png"), quality=95)
    print("Created: video2-thumb-c.png")


# ============================================================
# VIDEO 3: $84 Trillion Wealth Transfer
# ============================================================

def video3_thumb_a():
    """$84 TRILLION NOT INVITED - urgent, gold text."""
    img = create_gradient_bg(WIDTH, HEIGHT, (15, 10, 5), (35, 25, 10))
    draw = ImageDraw.Draw(img)

    # Gold shimmer behind text
    for r in range(60, 0, -3):
        intensity = int(30 * (60 - r) / 60)
        draw.ellipse([850 - r * 3, 200 - r, 850 + r * 3, 200 + r],
                     fill=(intensity, int(intensity * 0.8), 0))

    font_huge = get_bold_font(120)
    font_large = get_bold_font(80)

    draw_text_with_outline(draw, (540, 60), "$84", font_huge, (255, 215, 0), outline_width=5)
    draw_text_with_outline(draw, (540, 200), "TRILLION", font_large, (255, 215, 0), outline_width=4)

    draw.rectangle([540, 310, 1220, 316], fill=(255, 215, 0))

    draw_text_with_outline(draw, (540, 340), "NOT", font_large, (255, 255, 255), outline_width=3)
    draw_text_with_outline(draw, (540, 440), "INVITED", font_large, (255, 255, 255), outline_width=3)

    # Red "X" mark
    draw.line([(1080, 350), (1200, 470)], fill=(255, 50, 50), width=8)
    draw.line([(1200, 350), (1080, 470)], fill=(255, 50, 50), width=8)

    img = add_vignette(img, 0.4)
    img.save(os.path.join(OUTPUT_DIR, "video3-thumb-a.png"), quality=95)
    print("Created: video3-thumb-a.png")


def video3_thumb_b():
    """WALL STREET'S SECRET - yellow text, money flow arrows."""
    img = create_gradient_bg(WIDTH, HEIGHT, (10, 15, 30), (20, 30, 55))
    draw = ImageDraw.Draw(img)

    # Money flow arrows in background
    arrow_color = (60, 80, 120)
    for y_pos in range(100, 700, 120):
        for x_pos in range(600, 1280, 80):
            draw.polygon([(x_pos, y_pos), (x_pos + 30, y_pos - 15),
                         (x_pos + 30, y_pos - 5), (x_pos + 60, y_pos - 5),
                         (x_pos + 60, y_pos + 5), (x_pos + 30, y_pos + 5),
                         (x_pos + 30, y_pos + 15)], fill=arrow_color)

    font_huge = get_bold_font(90)
    font_large = get_bold_font(80)

    draw_text_with_outline(draw, (530, 80), "WALL ST", font_huge, (255, 230, 0), outline_width=4)
    draw_text_with_outline(draw, (530, 200), "SECRET", font_huge, (255, 230, 0), outline_width=4)

    draw.rectangle([530, 320, 1150, 326], fill=(255, 255, 255))

    draw_text_with_outline(draw, (530, 350), "$84 TRILLION", font_large, (255, 255, 255), outline_width=3)
    draw_text_with_outline(draw, (530, 460), "EXPOSED", font_large, (255, 100, 100), outline_width=3)

    img = add_vignette(img, 0.4)
    img.save(os.path.join(OUTPUT_DIR, "video3-thumb-b.png"), quality=95)
    print("Created: video3-thumb-b.png")


def video3_thumb_c():
    """$84T YOUR SHARE? - massive gold text, red ACT NOW."""
    img = create_gradient_bg(WIDTH, HEIGHT, (5, 5, 15), (15, 15, 35))
    draw = ImageDraw.Draw(img)

    font_massive = get_bold_font(200)
    font_large = get_bold_font(80)

    draw_text_with_outline(draw, (520, 30), "$84T", font_massive, (255, 215, 0), outline_width=6)

    draw.rectangle([520, 260, 1240, 270], fill=(255, 215, 0))

    draw_text_with_outline(draw, (520, 290), "YOUR", font_large, (255, 255, 255), outline_width=4)
    draw_text_with_outline(draw, (520, 390), "SHARE?", font_large, (255, 255, 255), outline_width=4)

    # Red urgency badge
    draw.rounded_rectangle([520, 520, 820, 600], radius=12, fill=(220, 30, 30))
    font_badge = get_bold_font(50)
    draw.text((555, 532), "ACT NOW", font=font_badge, fill=(255, 255, 255))

    img = add_vignette(img, 0.4)
    img.save(os.path.join(OUTPUT_DIR, "video3-thumb-c.png"), quality=95)
    print("Created: video3-thumb-c.png")


# ============================================================
# VIDEO 4: Retirement Catch-Up Guide
# ============================================================

def video4_thumb_a():
    """CATCH UP AT 50 - confident, green+yellow, dark blue bg."""
    img = create_gradient_bg(WIDTH, HEIGHT, (10, 20, 45), (20, 35, 70))
    draw = ImageDraw.Draw(img)

    # Upward chart in background
    for offset in range(4):
        draw_chart_line(draw, 500, 650 - offset, 1250, 150 + offset, (0, 120, 60), 3)

    font_huge = get_bold_font(120)
    font_large = get_bold_font(90)

    draw_text_with_outline(draw, (520, 60), "CATCH", font_huge, (0, 230, 100), outline_width=5)
    draw_text_with_outline(draw, (520, 190), "UP", font_huge, (0, 230, 100), outline_width=5)

    # Yellow "AT 50" badge
    draw.rounded_rectangle([520, 340, 750, 420], radius=12, fill=(255, 210, 0))
    font_badge = get_bold_font(56)
    draw.text((545, 350), "AT 50", font=font_badge, fill=(0, 0, 0))

    # Subtitle
    font_med = get_bold_font(42)
    draw_text_with_outline(draw, (520, 460), "THE PLAYBOOK", font_med, (200, 200, 200), outline_width=2)

    img = add_vignette(img, 0.3)
    img.save(os.path.join(OUTPUT_DIR, "video4-thumb-a.png"), quality=95)
    print("Created: video4-thumb-a.png")


def video4_thumb_b():
    """START HERE - green arrow, RETIREMENT PLAYBOOK."""
    img = create_gradient_bg(WIDTH, HEIGHT, (10, 20, 40), (20, 35, 65))
    draw = ImageDraw.Draw(img)

    font_huge = get_bold_font(90)
    font_large = get_bold_font(70)
    font_med = get_bold_font(42)

    draw_text_with_outline(draw, (520, 50), "RETIRE", font_huge, (255, 255, 255), outline_width=4)
    draw_text_with_outline(draw, (520, 150), "MENT", font_huge, (255, 255, 255), outline_width=4)

    # Green arrow with "START HERE"
    arrow_points = [
        (520, 300), (780, 300), (780, 255), (880, 330), (780, 405), (780, 360), (520, 360)
    ]
    draw.polygon(arrow_points, fill=(0, 200, 80))
    font_arrow = get_bold_font(44)
    draw.text((540, 307), "START HERE", font=font_arrow, fill=(255, 255, 255))

    draw_text_with_outline(draw, (520, 440), "PLAYBOOK", font_large, (0, 200, 100), outline_width=3)

    # "50+" circle
    cx, cy, cr = 1100, 530, 65
    draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=(255, 210, 0))
    font_age = get_bold_font(50)
    draw.text((cx - 32, cy - 25), "50+", font=font_age, fill=(0, 0, 0))

    img = add_vignette(img, 0.3)
    img.save(os.path.join(OUTPUT_DIR, "video4-thumb-b.png"), quality=95)
    print("Created: video4-thumb-b.png")


def video4_thumb_c():
    """THE PLAYBOOK - OVER 50 badge, checkmark, resolute look."""
    img = create_gradient_bg(WIDTH, HEIGHT, (10, 15, 35), (20, 30, 60))
    draw = ImageDraw.Draw(img)

    # Large checkmark in background
    check_color = (40, 60, 90)
    draw.line([(850, 400), (950, 520), (1200, 200)], fill=check_color, width=25)

    font_huge = get_bold_font(100)
    font_large = get_bold_font(75)

    draw_text_with_outline(draw, (520, 50), "THE", font_huge, (255, 255, 255), outline_width=4)
    draw_text_with_outline(draw, (520, 160), "PLAY", font_huge, (255, 255, 255), outline_width=4)
    draw_text_with_outline(draw, (520, 270), "BOOK", font_huge, (255, 255, 255), outline_width=4)

    # Yellow "OVER 50" badge
    draw.rounded_rectangle([520, 400, 780, 470], radius=12, fill=(255, 210, 0))
    font_badge = get_bold_font(48)
    draw.text((540, 408), "OVER 50", font=font_badge, fill=(0, 0, 0))

    # Green verified badge
    draw.rounded_rectangle([520, 510, 730, 570], radius=10, fill=(0, 180, 80))
    font_check = get_bold_font(36)
    draw.text((535, 523), "VERIFIED", font=font_check, fill=(255, 255, 255))

    img = add_vignette(img, 0.3)
    img.save(os.path.join(OUTPUT_DIR, "video4-thumb-c.png"), quality=95)
    print("Created: video4-thumb-c.png")


# ============================================================
# Generate all thumbnails
# ============================================================

if __name__ == "__main__":
    print(f"Output directory: {OUTPUT_DIR}")
    print("-" * 50)

    video1_thumb_a()
    video1_thumb_b()
    video1_thumb_c()
    video2_thumb_a()
    video2_thumb_b()
    video2_thumb_c()
    video3_thumb_a()
    video3_thumb_b()
    video3_thumb_c()
    video4_thumb_a()
    video4_thumb_b()
    video4_thumb_c()

    print("-" * 50)
    print(f"All 12 thumbnails generated in: {OUTPUT_DIR}")
