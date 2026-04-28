"""Build a JKFM uniform spec-sheet mockup PNG for supplier briefs."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent / "jkfm_uniform_mockup.png"

# Brand colours
GREEN = (27, 67, 50)        # #1B4332 forest green
GOLD = (201, 168, 76)       # #C9A84C
CHARCOAL = (54, 69, 79)     # #36454F
BLACK = (20, 20, 20)
HIVIS = (255, 200, 0)
HIVIS_TAPE = (220, 220, 220)
WHITE = (255, 255, 255)
PAPER = (248, 247, 243)
INK = (30, 30, 30)
GRID = (210, 210, 210)
MUTED = (120, 120, 120)

W, H = 2000, 2600
img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


def text(xy, s, size=24, bold=False, fill=INK, anchor="la"):
    d.text(xy, s, font=font(size, bold), fill=fill, anchor=anchor)


def polo(cx, cy, scale, body_color, sleeve="short", logo_text="JKFM",
         logo_color=GOLD, label=""):
    """Draw a polo shirt centred at (cx, cy)."""
    s = scale
    # Body torso (trapezoid-ish)
    body = [
        (cx - 180 * s, cy - 200 * s),  # shoulder L
        (cx + 180 * s, cy - 200 * s),  # shoulder R
        (cx + 220 * s, cy + 280 * s),  # hem R
        (cx - 220 * s, cy + 280 * s),  # hem L
    ]
    d.polygon(body, fill=body_color, outline=BLACK, width=2)

    # Sleeves
    if sleeve == "short":
        sleeve_l = [(cx - 180 * s, cy - 200 * s),
                    (cx - 320 * s, cy - 150 * s),
                    (cx - 290 * s, cy - 40 * s),
                    (cx - 160 * s, cy - 90 * s)]
        sleeve_r = [(cx + 180 * s, cy - 200 * s),
                    (cx + 320 * s, cy - 150 * s),
                    (cx + 290 * s, cy - 40 * s),
                    (cx + 160 * s, cy - 90 * s)]
    else:  # long
        sleeve_l = [(cx - 180 * s, cy - 200 * s),
                    (cx - 320 * s, cy - 150 * s),
                    (cx - 360 * s, cy + 240 * s),
                    (cx - 270 * s, cy + 260 * s),
                    (cx - 230 * s, cy - 40 * s),
                    (cx - 160 * s, cy - 90 * s)]
        sleeve_r = [(cx + 180 * s, cy - 200 * s),
                    (cx + 320 * s, cy - 150 * s),
                    (cx + 360 * s, cy + 240 * s),
                    (cx + 270 * s, cy + 260 * s),
                    (cx + 230 * s, cy - 40 * s),
                    (cx + 160 * s, cy - 90 * s)]
    d.polygon(sleeve_l, fill=body_color, outline=BLACK, width=2)
    d.polygon(sleeve_r, fill=body_color, outline=BLACK, width=2)

    # Collar
    collar = [(cx - 60 * s, cy - 200 * s),
              (cx - 40 * s, cy - 130 * s),
              (cx + 40 * s, cy - 130 * s),
              (cx + 60 * s, cy - 200 * s)]
    d.polygon(collar, fill=body_color, outline=BLACK, width=2)
    # Neckline opening
    d.polygon([(cx - 40 * s, cy - 200 * s),
               (cx - 28 * s, cy - 132 * s),
               (cx + 28 * s, cy - 132 * s),
               (cx + 40 * s, cy - 200 * s)], fill=PAPER, outline=BLACK, width=1)

    # Placket
    d.line([(cx, cy - 132 * s), (cx, cy - 30 * s)], fill=BLACK, width=2)
    # Buttons
    for i in range(3):
        by = cy - 110 * s + i * 35 * s
        d.ellipse([cx - 6, by - 6, cx + 6, by + 6], fill=PAPER, outline=BLACK)

    # Embroidery patch on left chest (viewer's right because mirrored garment view... use viewer-left = wearer-right; convention: show on viewer-left for wearer's left chest)
    patch_cx = cx - 100 * s
    patch_cy = cy - 60 * s
    pw, ph = 100 * s, 36 * s
    d.rectangle([patch_cx - pw / 2, patch_cy - ph / 2,
                 patch_cx + pw / 2, patch_cy + ph / 2],
                outline=logo_color, width=2)
    text((patch_cx, patch_cy), logo_text, size=int(28 * s), bold=True,
         fill=logo_color, anchor="mm")

    # Label below
    if label:
        text((cx, cy + 320 * s), label, size=22, bold=True, anchor="ma")


def jacket(cx, cy, scale, body_color, logo_text="JKFM", label=""):
    s = scale
    body = [
        (cx - 220 * s, cy - 220 * s),
        (cx + 220 * s, cy - 220 * s),
        (cx + 260 * s, cy + 320 * s),
        (cx - 260 * s, cy + 320 * s),
    ]
    d.polygon(body, fill=body_color, outline=BLACK, width=2)

    # Long sleeves
    sleeve_l = [(cx - 220 * s, cy - 220 * s),
                (cx - 360 * s, cy - 170 * s),
                (cx - 380 * s, cy + 280 * s),
                (cx - 290 * s, cy + 290 * s),
                (cx - 250 * s, cy - 60 * s),
                (cx - 200 * s, cy - 110 * s)]
    sleeve_r = [(cx + 220 * s, cy - 220 * s),
                (cx + 360 * s, cy - 170 * s),
                (cx + 380 * s, cy + 280 * s),
                (cx + 290 * s, cy + 290 * s),
                (cx + 250 * s, cy - 60 * s),
                (cx + 200 * s, cy - 110 * s)]
    d.polygon(sleeve_l, fill=body_color, outline=BLACK, width=2)
    d.polygon(sleeve_r, fill=body_color, outline=BLACK, width=2)

    # Stand collar
    d.rectangle([cx - 70 * s, cy - 240 * s, cx + 70 * s, cy - 200 * s],
                fill=body_color, outline=BLACK, width=2)
    # Centre zip
    d.line([(cx, cy - 200 * s), (cx, cy + 320 * s)], fill=GOLD, width=3)
    # Zip teeth marks
    for i in range(20):
        zy = cy - 195 * s + i * 25 * s
        d.line([(cx - 4, zy), (cx + 4, zy)], fill=GOLD, width=1)

    # Chest patch pocket outline (subtle)
    d.rectangle([cx + 60 * s, cy - 100 * s, cx + 200 * s, cy + 30 * s],
                outline=MUTED, width=1)

    # Logo on left chest
    patch_cx = cx - 130 * s
    patch_cy = cy - 60 * s
    pw, ph = 120 * s, 40 * s
    d.rectangle([patch_cx - pw / 2, patch_cy - ph / 2,
                 patch_cx + pw / 2, patch_cy + ph / 2],
                outline=GOLD, width=2)
    text((patch_cx, patch_cy), logo_text, size=int(30 * s), bold=True,
         fill=GOLD, anchor="mm")

    if label:
        text((cx, cy + 360 * s), label, size=22, bold=True, anchor="ma")


def pants(cx, cy, scale, color, label=""):
    s = scale
    # Waistband
    d.rectangle([cx - 160 * s, cy - 280 * s, cx + 160 * s, cy - 240 * s],
                fill=color, outline=BLACK, width=2)
    # Left leg
    d.polygon([(cx - 160 * s, cy - 240 * s),
               (cx - 10 * s, cy - 240 * s),
               (cx - 30 * s, cy + 320 * s),
               (cx - 140 * s, cy + 320 * s)],
              fill=color, outline=BLACK, width=2)
    # Right leg
    d.polygon([(cx + 10 * s, cy - 240 * s),
               (cx + 160 * s, cy - 240 * s),
               (cx + 140 * s, cy + 320 * s),
               (cx + 30 * s, cy + 320 * s)],
              fill=color, outline=BLACK, width=2)
    # Cargo pockets
    d.rectangle([cx - 130 * s, cy - 100 * s, cx - 50 * s, cy + 0 * s],
                outline=BLACK, width=2)
    d.rectangle([cx + 50 * s, cy - 100 * s, cx + 130 * s, cy + 0 * s],
                outline=BLACK, width=2)
    if label:
        text((cx, cy + 360 * s), label, size=22, bold=True, anchor="ma")


def hivis(cx, cy, scale, label=""):
    s = scale
    body = [
        (cx - 200 * s, cy - 220 * s),
        (cx + 200 * s, cy - 220 * s),
        (cx + 220 * s, cy + 240 * s),
        (cx - 220 * s, cy + 240 * s),
    ]
    d.polygon(body, fill=HIVIS, outline=BLACK, width=2)
    # Reflective tape bands
    d.rectangle([cx - 220 * s, cy - 60 * s, cx + 220 * s, cy - 30 * s],
                fill=HIVIS_TAPE, outline=BLACK, width=1)
    d.rectangle([cx - 220 * s, cy + 60 * s, cx + 220 * s, cy + 90 * s],
                fill=HIVIS_TAPE, outline=BLACK, width=1)
    # Centre zip
    d.line([(cx, cy - 220 * s), (cx, cy + 240 * s)], fill=BLACK, width=2)
    # Neck cutout
    d.polygon([(cx - 60 * s, cy - 220 * s),
               (cx - 30 * s, cy - 160 * s),
               (cx + 30 * s, cy - 160 * s),
               (cx + 60 * s, cy - 220 * s)], fill=PAPER, outline=BLACK, width=2)
    # Logo on left chest
    patch_cx = cx - 110 * s
    patch_cy = cy - 110 * s
    pw, ph = 100 * s, 32 * s
    d.rectangle([patch_cx - pw / 2, patch_cy - ph / 2,
                 patch_cx + pw / 2, patch_cy + ph / 2],
                outline=BLACK, width=2)
    text((patch_cx, patch_cy), "JKFM", size=int(24 * s), bold=True,
         fill=BLACK, anchor="mm")
    if label:
        text((cx, cy + 280 * s), label, size=22, bold=True, anchor="ma")


def swatch(x, y, w, h, color, label, hex_code):
    d.rectangle([x, y, x + w, y + h], fill=color, outline=BLACK, width=1)
    text((x, y + h + 8), label, size=18, bold=True)
    text((x, y + h + 32), hex_code, size=16, fill=MUTED)


# ==================== HEADER ====================
d.rectangle([0, 0, W, 130], fill=GREEN)
text((60, 40), "JKFM UNIFORM — SUPPLIER MOCKUP BRIEF", size=44, bold=True,
     fill=GOLD)
text((60, 92), "JK Facilities Management Pty Ltd  |  Melbourne  |  Two-tier kit",
     size=22, fill=PAPER)

# ==================== COLOUR PALETTE ====================
text((60, 160), "1. COLOUR PALETTE", size=28, bold=True)
d.line([(60, 200), (W - 60, 200)], fill=GRID, width=1)
swatch(60, 220, 180, 100, GREEN, "Forest Green", "#1B4332  (body)")
swatch(280, 220, 180, 100, GOLD, "JKFM Gold", "#C9A84C  (embroidery)")
swatch(500, 220, 180, 100, CHARCOAL, "Charcoal", "#36454F  (pants — Tier 1)")
swatch(720, 220, 180, 100, BLACK, "Black", "#141414  (jackets, pants — Tier 2)")
swatch(940, 220, 180, 100, HIVIS, "Hi-Vis Yellow", "AS/NZS 4602  (vest only)")

# ==================== TIER 1 ====================
text((60, 410), "2. TIER 1 — KARAN + FM STAFF (client-facing)", size=28, bold=True)
d.line([(60, 450), (W - 60, 450)], fill=GRID, width=1)

polo(280, 700, 0.95, GREEN, "short", label="Polo — Short Sleeve\nForest Green / Gold embroidery")
polo(720, 700, 0.95, GREEN, "long", label="Polo — Long Sleeve\nForest Green / Gold embroidery")
jacket(1180, 700, 0.95, BLACK, label="Softshell Jacket\nBlack / Gold embroidery")
pants(1620, 700, 0.95, CHARCOAL, label="Stretch Chino / Cargo\nCharcoal — no branding")

# ==================== TIER 2 ====================
text((60, 1280), "3. TIER 2 — CLEANING CREW (durable, washable)", size=28, bold=True)
d.line([(60, 1320), (W - 60, 1320)], fill=GRID, width=1)

polo(280, 1570, 0.95, GREEN, "short", label="Polo — Short Sleeve\nForest Green / Gold embroidery")
hivis(720, 1570, 0.95, label="Hi-Vis Vest (over polo)\nReflective tape — plant rooms")
pants(1180, 1570, 0.95, BLACK, label="Cargo Work Pants\nBlack — durable ripstop")
# Apron square
ax, ay = 1620, 1570
d.rectangle([ax - 180, ay - 220, ax + 180, ay + 220], fill=BLACK, outline=BLACK, width=2)
# Apron neck strap
d.line([(ax - 80, ay - 220), (ax - 60, ay - 280)], fill=BLACK, width=4)
d.line([(ax + 80, ay - 220), (ax + 60, ay - 280)], fill=BLACK, width=4)
d.arc([ax - 60, ay - 310, ax + 60, ay - 250], 180, 360, fill=BLACK, width=4)
# Apron ties
d.line([(ax - 180, ay - 60), (ax - 280, ay - 40)], fill=BLACK, width=4)
d.line([(ax + 180, ay - 60), (ax + 280, ay - 40)], fill=BLACK, width=4)
# Apron logo
text((ax, ay - 60), "JKFM", size=36, bold=True, fill=GOLD, anchor="mm")
text((ax, ay + 280), "Utility Apron (optional)\nBlack / Gold print", size=22,
     bold=True, anchor="ma")

# ==================== BRANDING SPEC ====================
text((60, 2120), "4. BRANDING — EMBROIDERY (NOT HEAT-TRANSFER)", size=28, bold=True)
d.line([(60, 2160), (W - 60, 2160)], fill=GRID, width=1)

specs = [
    ("Logo file format", "Vector — .ai / .eps / .svg (will be supplied)"),
    ("Thread colour", "Madeira Classic 1024 (Old Gold) or equivalent"),
    ("Left-chest placement", "80mm wide, centred 90mm down from shoulder seam, 100mm in from centre"),
    ("Cleaning tier — back print", '"JKFM Cleaning Services" + phone, 250mm wide, between shoulder blades'),
    ("Tier differentiation", "FM = polo + chino, Cleaning = polo + cargo + hi-vis vest"),
    ("Sample order", "1 of each garment + size run before bulk — confirm thread colour in person"),
]
y = 2200
for k, v in specs:
    text((80, y), "•", size=22, bold=True)
    text((110, y), k + ":", size=22, bold=True)
    text((520, y), v, size=22)
    y += 50

# Footer
d.rectangle([0, H - 60, W, H], fill=GREEN)
text((60, H - 38), "Send to: Total Image Group  |  Cargo Crew  |  The Uniform Edit  —  request matching quotes",
     size=20, bold=True, fill=GOLD, anchor="lm")

img.save(OUT, "PNG", optimize=True)
print(str(OUT))
