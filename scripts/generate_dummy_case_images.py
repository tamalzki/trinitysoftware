#!/usr/bin/env python3
"""Generate anonymized case-study PNGs with dummy data only (no real client figures or names).

Does not overwrite aag-maritime.png — that asset stays as the real marketing site screenshot.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "images" / "cases"
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial.ttf"


def load_font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size)


def rounded_rect(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    fill: str | tuple[int, int, int],
    radius: int = 8,
) -> None:
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle((x0, y0, x1, y1), radius=radius, fill=fill)


def draw_demo_badge(img: Image.Image, draw: ImageDraw.ImageDraw, w: int) -> None:
    font = load_font(11)
    label = "Illustrative UI · demo data"
    tw = draw.textlength(label, font=font)
    pad_x, pad_y = 10, 6
    x1, y1 = w - 16, 14
    x0 = int(x1 - tw - pad_x * 2)
    y0 = y1
    y1 = y0 + 22
    rounded_rect(draw, (x0, y0, x1, y1), fill=(30, 41, 39))
    draw.text((x0 + pad_x, y0 + 4), label, fill=(180, 230, 220), font=font)


def jm_rosel(w: int, h: int) -> Image.Image:
    img = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(img)
    sw = 220
    rounded_rect(draw, (0, 0, sw, h), fill=(15, 23, 42))
    f_sm, f_md, f_lg = load_font(11), load_font(13), load_font(15)
    y = 24
    draw.text((20, y), "Demo Fleet Co.", fill=(148, 163, 184), font=f_sm)
    y += 28
    for item in ("Dashboard", "Trips", "Expenses", "Payroll", "Reports"):
        draw.text((20, y), item, fill=(226, 232, 240), font=f_md)
        y += 34
    draw.text((20, h - 44), "User: demo.admin", fill=(100, 116, 139), font=f_sm)

    hx = sw + 28
    draw.text((hx, 20), "Operations overview", fill=(15, 23, 42), font=load_font(22))
    draw.text((hx, 52), "Sample metrics for portfolio — not live data.", fill=(100, 116, 139), font=f_sm)

    # stat cards
    cx = hx
    for i, (lab, val) in enumerate(
        (
            ("Active trips", "12"),
            ("Pending", "3"),
            ("Fuel (demo)", "₱45,200"),
        )
    ):
        x0 = cx + i * 200
        rounded_rect(draw, (x0, 88, x0 + 180, 168), fill=(255, 255, 255), radius=10)
        draw.rectangle((x0, 88, x0 + 180, 92), fill=(59, 130, 246))
        draw.text((x0 + 14, 104), lab, fill=(100, 116, 139), font=f_sm)
        draw.text((x0 + 14, 124), val, fill=(15, 23, 42), font=load_font(20))

    # table header
    ty = 196
    rounded_rect(draw, (hx, ty, w - 28, ty + 36), fill=(241, 245, 249))
    cols = ("Trip ID", "Route", "Status", "Amount (demo)")
    xs = [hx + 12, hx + 160, hx + 420, hx + 620]
    for x, c in zip(xs, cols):
        draw.text((x, ty + 10), c, fill=(71, 85, 105), font=f_md)
    rows = [
        ("TRP-1001", "Hub A → Hub B", "Open", "₱12,340"),
        ("TRP-1002", "Hub C → Hub A", "Closed", "₱8,900"),
        ("TRP-1003", "Hub B → Hub D", "Open", "₱15,000"),
    ]
    ry = ty + 40
    for r in rows:
        rounded_rect(draw, (hx, ry, w - 28, ry + 40), fill=(255, 255, 255))
        for x, cell in zip(xs, r):
            draw.text((x, ry + 12), cell, fill=(51, 65, 85), font=f_sm)
        ry += 44

    draw_demo_badge(img, draw, w)
    return img


def divinejm(w: int, h: int) -> Image.Image:
    img = Image.new("RGB", (w, h), (245, 247, 250))
    draw = ImageDraw.Draw(img)
    sw = 200
    rounded_rect(draw, (0, 0, sw, h), fill=(248, 250, 252))
    f_sm, f_md = load_font(10), load_font(12)
    y = 16
    draw.text((14, y), "Sample Foods (demo)", fill=(71, 85, 105), font=f_md)
    y += 26
    for item in ("Dashboard", "Finished products", "Production", "Sales", "Reports"):
        draw.text((14, y), item, fill=(51, 65, 85), font=f_sm)
        y += 26
    hx = sw + 16
    draw.text((hx, 16), "Finished products", fill=(15, 23, 42), font=load_font(18))
    draw.text((hx, 44), "Placeholder list — figures are fictional.", fill=(100, 116, 139), font=f_sm)
    rounded_rect(draw, (hx, 72, w - 16, 112), fill=(59, 130, 246))
    draw.text((hx + 12, 86), "+ Add sample product", fill=(255, 255, 255), font=f_sm)

    ty = 124
    rounded_rect(draw, (hx, ty, w - 16, ty + 32), fill=(226, 232, 240))
    headers = ("Product (demo)", "Type", "Stock", "Min")
    xs = [hx + 8, hx + 220, hx + 360, hx + 460]
    for x, t in zip(xs, headers):
        draw.text((x, ty + 8), t, fill=(71, 85, 105), font=f_sm)
    rows = [
        ("SKU-DEMO-01", "Mfg", "120", "20"),
        ("SKU-DEMO-02", "Mfg", "45", "30"),
        ("SKU-DEMO-03", "Mfg", "8", "15"),
        ("SKU-DEMO-04", "Mfg", "200", "40"),
    ]
    ry = ty + 36
    for i, r in enumerate(rows):
        bg = (254, 242, 242) if i == 0 else (255, 251, 235) if i == 1 else (255, 255, 255)
        rounded_rect(draw, (hx, ry, w - 16, ry + 36), fill=bg)
        for x, cell in zip(xs, r):
            draw.text((x, ry + 10), cell, fill=(51, 65, 85), font=f_sm)
        ry += 38
    draw_demo_badge(img, draw, w)
    return img


def angie(w: int, h: int) -> Image.Image:
    img = Image.new("RGB", (w, h), (236, 253, 245))
    draw = ImageDraw.Draw(img)
    sw = 188
    rounded_rect(draw, (0, 0, sw, h), fill=(17, 94, 89))
    f_sm, f_md = load_font(10), load_font(12)
    y = 18
    draw.text((14, y), "Demo: Inventory · Sales · Finance", fill=(167, 243, 208), font=f_sm)
    y += 28
    for item in ("Dashboard", "Daily cashflow", "Inventory", "Reports"):
        draw.text((14, y), item, fill=(240, 253, 250), font=f_md)
        y += 26
    hx = sw + 14
    draw.text((hx, 14), "Daily cash (sample)", fill=(6, 78, 59), font=load_font(17))
    draw.text((hx, 42), "All amounts are placeholder values.", fill=(5, 150, 105), font=f_sm)
    rounded_rect(draw, (hx, 70, hx + 280, 130), fill=(255, 255, 255))
    draw.text((hx + 14, 82), "Available (demo)", fill=(100, 116, 139), font=f_sm)
    draw.text((hx + 14, 100), "₱20,000.00", fill=(5, 150, 105), font=load_font(22))

    ty = 148
    rounded_rect(draw, (hx, ty, w - 16, h - 20), fill=(255, 255, 255))
    draw.text((hx + 10, ty + 10), "Entries (fictional)", fill=(15, 23, 42), font=f_md)
    rows = [("INCOME", "Line item A (demo)", "₱500.00"), ("INCOME", "Line item B (demo)", "₱320.00")]
    ry = ty + 40
    for r in rows:
        draw.text((hx + 14, ry), r[0], fill=(5, 150, 105), font=f_sm)
        draw.text((hx + 120, ry), r[1], fill=(51, 65, 85), font=f_sm)
        draw.text((w - 120, ry), r[2], fill=(15, 23, 42), font=f_sm)
        ry += 28
    draw_demo_badge(img, draw, w)
    return img


def citipower(w: int, h: int) -> Image.Image:
    img = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(img)
    sw = 224
    rounded_rect(draw, (0, 0, sw, h), fill=(30, 41, 59))
    f_sm, f_md = load_font(11), load_font(13)
    y = 20
    draw.text((16, y), "Demo Electronics Portal", fill=(148, 163, 184), font=f_sm)
    y += 28
    for item in ("Products", "Purchase orders", "Inventory", "Sales"):
        draw.text((16, y), item, fill=(226, 232, 240), font=f_md)
        y += 32
    hx = sw + 24
    draw.text((hx, 20), "Products & stock (sample)", fill=(15, 23, 42), font=load_font(20))
    draw.text((hx, 54), "SKUs and quantities are not real.", fill=(100, 116, 139), font=f_sm)
    ty = 96
    rounded_rect(draw, (hx, ty, w - 32, ty + 40), fill=(226, 232, 240))
    for i, t in enumerate(("SKU (demo)", "On hand", "Status")):
        draw.text((hx + 16 + i * 280, ty + 12), t, fill=(71, 85, 105), font=f_md)
    rows = [
        ("PART-DEMO-001", "240", "OK"),
        ("PART-DEMO-002", "18", "Low"),
        ("PART-DEMO-003", "90", "OK"),
    ]
    ry = ty + 48
    for r in rows:
        rounded_rect(draw, (hx, ry, w - 32, ry + 44), fill=(255, 255, 255))
        draw.text((hx + 16, ry + 14), r[0], fill=(30, 41, 59), font=f_sm)
        draw.text((hx + 300, ry + 14), r[1], fill=(30, 41, 59), font=f_sm)
        draw.text((hx + 560, ry + 14), r[2], fill=(22, 163, 74), font=f_sm)
        ry += 50
    draw_demo_badge(img, draw, w)
    return img


def ronnie_aircon(w: int, h: int) -> Image.Image:
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    sw = 210
    rounded_rect(draw, (0, 0, sw, h), fill=(241, 245, 249))
    f_sm, f_md = load_font(11), load_font(13)
    y = 18
    draw.text((14, y), "Sample HVAC Services (demo)", fill=(71, 85, 105), font=f_md)
    y += 30
    for item in ("Inventory", "Serial #", "Service jobs", "Installments"):
        draw.text((14, y), item, fill=(51, 65, 85), font=f_sm)
        y += 30
    hx = sw + 20
    draw.text((hx, 18), "Equipment & serials (fictional)", fill=(15, 23, 42), font=load_font(19))
    draw.text((hx, 50), "Serial numbers below are placeholders.", fill=(100, 116, 139), font=f_sm)
    ty = 88
    headers = ("Unit (demo)", "Serial", "Job status")
    xs = [hx + 10, hx + 320, hx + 560]
    rounded_rect(draw, (hx, ty, w - 24, ty + 36), fill=(226, 232, 240))
    for x, t in zip(xs, headers):
        draw.text((x, ty + 10), t, fill=(71, 85, 105), font=f_md)
    rows = [
        ("Split-type A", "SN-DEMO-7X9K2", "Scheduled"),
        ("Cassette B", "SN-DEMO-4M1P8", "Done"),
        ("Window C", "SN-DEMO-2Q5R1", "Open"),
    ]
    ry = ty + 42
    for r in rows:
        rounded_rect(draw, (hx, ry, w - 24, ry + 42), fill=(248, 250, 252))
        for x, cell in zip(xs, r):
            draw.text((x, ry + 13), cell, fill=(30, 41, 59), font=f_sm)
        ry += 46
    draw_demo_badge(img, draw, w)
    return img


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    gens = [
        ("jm-rosel.png", jm_rosel, 1400, 617),
        ("divinejm.png", divinejm, 1024, 520),
        ("angie.png", angie, 1024, 536),
        ("citipower.png", citipower, 1400, 729),
        ("ronnie-aircon.png", ronnie_aircon, 1400, 731),
    ]
    for name, fn, width, height in gens:
        im = fn(width, height)
        path = OUT / name
        im.save(path, "PNG", optimize=True)
        print(f"Wrote {path} ({width}x{height})")
    print("Skipped aag-maritime.png (use real marketing screenshot).")


if __name__ == "__main__":
    main()
