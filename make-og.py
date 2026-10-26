#!/usr/bin/env python3
"""Generate a 1200x630 OG share card for Meridiano matching the site's brand."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (19, 18, 17)          # #131211 dark bg
ACCENT = (244, 120, 37)    # #f47825 orange
FG = (226, 223, 221)       # #e2dfdd light text
MUTED = (150, 145, 140)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# subtle radial glow behind the mark
for r in range(260, 60, -4):
    a = int(28 * (1 - r / 260))
    d.ellipse([W - 300 - r, 90 - r, W - 300 + r, 90 + r], fill=(244, 120, 37, 0) if False else (244, 120, 37))
# simpler: draw a soft orange circle
d.ellipse([W - 360, 30, W - 40, 350], fill=(244, 120, 37))

# compass mark (recreate favicon geometry) in white on the orange circle
cx, cy, R = W - 200, 190, 120
d.ellipse([cx - R, cy - R, cx + R, cy + R], fill=(19, 18, 17))
d.ellipse([cx - R, cy - R, cx + R, cy + R], outline=FG, width=10)
lw = 10
d.line([cx, cy - R + 20, cx, cy + R - 20], fill=FG, width=lw)
d.line([cx - R + 20, cy, cx + R - 20, cy], fill=FG, width=lw)
d.line([cx - R + 40, cy - R + 40, cx + R - 40, cy + R - 40], fill=FG, width=lw)
d.line([cx + R - 40, cy - R + 40, cx - R + 40, cy + R - 40], fill=FG, width=lw)
d.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], fill=FG)

# title
def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

serif = font("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 96)
sans = font("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
sansb = font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 44)

d.text((90, 120), "Meridiano", font=serif, fill=FG)
d.text((90, 250), "AI-powered news briefings, curated", font=sans, fill=MUTED)
d.text((90, 310), "from the feeds that matter to you.", font=sans, fill=MUTED)

# tagline pill
d.rounded_rectangle([90, 400, 470, 470], radius=35, fill=ACCENT)
d.text((120, 410), "meridiano.app", font=sansb, fill=(19, 18, 17))

img.save("public/og-image.png")
print("saved public/og-image.png", img.size)
