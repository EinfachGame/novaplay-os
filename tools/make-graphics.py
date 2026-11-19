#!/usr/bin/env python3
"""NovaPlay OS – erzeugt alle Grafiken (Hintergründe, Boot-Animation, Bootmenü).

Aufruf (aus dem Projektordner):  python3 tools/make-graphics.py
Braucht: Python 3 + Pillow  (pip install pillow)
Farben ändern: einfach unten bei FARBEN die Werte anpassen.
"""
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

# ---------------- FARBEN ----------------
PURPLE = (168, 85, 255)
CYAN = (0, 220, 255)
PINK = (255, 60, 200)
BG_TOP = (6, 4, 18)
BG_BOTTOM = (22, 10, 48)
WHITE = (245, 240, 255)
# ----------------------------------------

ROOT = Path(__file__).resolve().parent.parent / "profile"
SHARE = ROOT / "airootfs/usr/share/wallpapers"
PLY = ROOT / "airootfs/usr/share/plymouth/themes/novaplay"
SHARE.mkdir(parents=True, exist_ok=True)
PLY.mkdir(parents=True, exist_ok=True)


def font(size, bold=True):
    names = ["DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"]
    for base in ["/usr/share/fonts/truetype/dejavu", "/usr/share/fonts/TTF", "/usr/share/fonts/dejavu"]:
        for n in names:
            p = Path(base) / n
            if p.exists():
                return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


def gradient(w, h, top, bottom):
    img = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(1, h - 1)
        d.line([(0, y), (w, y)], fill=tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3)))
    return img


def add_glow(img, shapes_fn, blur, strength=1.0):
    """Zeichnet Formen zweimal: weichgezeichnet (Leuchten) + scharf."""
    w, h = img.size
    layer = Image.new("RGB", (w, h), (0, 0, 0))
    shapes_fn(ImageDraw.Draw(layer))
    glow = layer.filter(ImageFilter.GaussianBlur(blur))
    if strength != 1.0:
        glow = Image.eval(glow, lambda v: min(255, int(v * strength)))
    out = ImageChops.add(img, glow)
    return ImageChops.add(out, layer)


def stars(img, n, seed, maxy=1.0):
    rnd = random.Random(seed)
    d = ImageDraw.Draw(img)
    w, h = img.size
    for _ in range(n):
        x, y = rnd.randrange(w), rnd.randrange(int(h * maxy))
        b = rnd.randint(80, 255)
        r = rnd.choice([1, 1, 1, 2])
        d.ellipse([x - r, y - r, x + r, y + r], fill=(b, b, min(255, b + 30)))


def logo_mark(size):
    """NovaPlay-Symbol: Play-Dreieck in einem Neon-Sechseck, transparent."""
    s = size
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    lay = Image.new("RGB", (s, s), (0, 0, 0))
    d = ImageDraw.Draw(lay)
    c = s / 2
    r = s * 0.40
    hexa = [(c + r * math.cos(math.radians(a)), c + r * math.sin(math.radians(a))) for a in range(-90, 270, 60)]
    d.line(hexa + [hexa[0]], fill=PURPLE, width=max(3, s // 28), joint="curve")
    tri = [(c - r * 0.32, c - r * 0.45), (c - r * 0.32, c + r * 0.45), (c + r * 0.5, c)]
    d.polygon(tri, fill=CYAN)
    glow = lay.filter(ImageFilter.GaussianBlur(s / 18))
    comb = ImageChops.add(glow, lay)
    alpha = comb.convert("L").point(lambda v: min(255, v * 2))
    img = Image.merge("RGBA", (*comb.split(), alpha))
    return img


def wordmark(text, size, color=WHITE, glow=PURPLE):
    f = font(size)
    tmp = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    l, t, r, b = tmp.textbbox((0, 0), text, font=f)
    pad = size // 2
    w, h = r - l + pad * 2, b - t + pad * 2
    lay = Image.new("RGB", (w, h), (0, 0, 0))
    ImageDraw.Draw(lay).text((pad - l, pad - t), text, font=f, fill=glow)
    g = lay.filter(ImageFilter.GaussianBlur(size / 7))
    sharp = Image.new("RGB", (w, h), (0, 0, 0))
    ImageDraw.Draw(sharp).text((pad - l, pad - t), text, font=f, fill=color)
    comb = ImageChops.add(g, sharp)
    alpha = comb.convert("L").point(lambda v: min(255, v * 2))
    return Image.merge("RGBA", (*comb.split(), alpha))


def synth_grid(img, horizon, color, spacing=40, fade=True):
    w, h = img.size

    def draw(d):
        for i in range(-40, 41):
            d.line([(w / 2 + i * spacing * 0.6, horizon), (w / 2 + i * spacing * 9, h)], fill=color, width=2)
        y, step = horizon, 6
        while y < h:
            d.line([(0, y), (w, y)], fill=color, width=2)
            step *= 1.28
            y += int(step)

    return add_glow(img, draw, 6, 0.8)


def sun(img, cx, cy, r):
    w, h = img.size
    sunl = Image.new("RGB", (w, h), (0, 0, 0))
    d = ImageDraw.Draw(sunl)
    for y in range(int(cy - r), int(cy + r)):
        t = (y - (cy - r)) / (2 * r)
        col = tuple(int(PINK[i] + (PURPLE[i] - PINK[i]) * t) for i in range(3))
        half = math.sqrt(max(0, r * r - (y - cy) ** 2))
        # Retro-Streifen in der unteren Hälfte
        if t > 0.5 and int((y - cy) / (r * 0.07)) % 2 == 0:
            continue
        d.line([(cx - half, y), (cx + half, y)], fill=col)
    glow = sunl.filter(ImageFilter.GaussianBlur(r * 0.35))
    return ImageChops.add(ImageChops.add(img, glow), sunl)


def mountains(img, horizon, seed, color):
    w, h = img.size
    rnd = random.Random(seed)
    d = ImageDraw.Draw(img)
    pts = [(0, horizon)]
    x = 0
    while x < w:
        x += rnd.randint(w // 30, w // 12)
        pts.append((x, horizon - rnd.randint(int(h * 0.03), int(h * 0.16))))
    pts += [(w, horizon), (0, horizon)]
    d.polygon(pts, fill=color)
    return img


# ===================== Hintergrundbilder =====================
def wallpaper_synthwave(w=3840, h=2160):
    img = gradient(w, h, BG_TOP, BG_BOTTOM)
    stars(img, 900, 1, 0.6)
    horizon = int(h * 0.64)
    img = sun(img, w / 2, horizon - h * 0.12, h * 0.24)
    img = mountains(img, horizon, 7, (14, 6, 34))
    floor = gradient(w, h - horizon, (16, 6, 40), (4, 2, 12))
    img.paste(floor, (0, horizon))
    img = synth_grid(img, horizon, PURPLE, 60)
    wm = wordmark("NOVAPLAY", 230)
    img.paste(wm, ((w - wm.width) // 2, int(h * 0.08)), wm)
    return img


def wallpaper_hex(w=3840, h=2160):
    img = gradient(w, h, (4, 6, 16), (10, 6, 30))
    r = 90
    dx, dy = r * 1.5, r * math.sqrt(3)
    rnd = random.Random(3)

    def draw(d):
        col = 0
        x = -r
        while x < w + r:
            y = -r + (dy / 2 if col % 2 else 0)
            while y < h + r:
                pts = [(x + r * 0.92 * math.cos(math.radians(a)), y + r * 0.92 * math.sin(math.radians(a))) for a in range(0, 360, 60)]
                dist = math.hypot((x - w * 0.72) / w, (y - h * 0.5) / h)
                b = max(0.0, 1 - dist * 2.2)
                if b > 0.05:
                    c = CYAN if rnd.random() < 0.15 else PURPLE
                    d.line(pts + [pts[0]], fill=tuple(int(v * b) for v in c), width=3)
                y += dy
            x += dx
            col += 1

    img = add_glow(img, draw, 10, 1.2)
    lm = logo_mark(900)
    img.paste(lm, (int(w * 0.72 - 450), int(h * 0.5 - 450)), lm)
    wm = wordmark("NOVAPLAY", 170)
    img.paste(wm, (int(w * 0.08), int(h * 0.42)), wm)
    sub = wordmark("PLAY WITHOUT LIMITS", 60, CYAN, CYAN)
    img.paste(sub, (int(w * 0.08) + 40, int(h * 0.42) + wm.height - 40), sub)
    return img


def wallpaper_minimal(w=3840, h=2160):
    img = gradient(w, h, (3, 3, 8), (12, 6, 24))
    stars(img, 500, 9)

    def draw(d):
        cx, cy = w / 2, h / 2
        for i, (rad, c) in enumerate([(620, PURPLE), (700, CYAN), (780, PINK)]):
            start = 200 + i * 70
            d.arc([cx - rad, cy - rad, cx + rad, cy + rad], start, start + 250, fill=c, width=8)

    img = add_glow(img, draw, 25, 1.4)
    lm = logo_mark(700)
    img.paste(lm, (w // 2 - 350, h // 2 - 350), lm)
    return img


# ===================== Boot-Animation (Plymouth) =====================
def plymouth_theme():
    n, s = 48, 200
    for i in range(n):
        img = Image.new("RGB", (s, s), (0, 0, 0))
        lay = Image.new("RGB", (s, s), (0, 0, 0))
        d = ImageDraw.Draw(lay)
        a = i * 360 / n
        # zwei gegenläufige Neon-Bögen
        d.arc([20, 20, s - 20, s - 20], a, a + 110, fill=PURPLE, width=9)
        d.arc([20, 20, s - 20, s - 20], a + 180, a + 290, fill=CYAN, width=9)
        d.arc([48, 48, s - 48, s - 48], -a * 1.5, -a * 1.5 + 70, fill=PINK, width=5)
        glow = lay.filter(ImageFilter.GaussianBlur(7))
        img = ImageChops.add(ImageChops.add(img, glow), lay)
        alpha = img.convert("L").point(lambda v: min(255, v * 2))
        Image.merge("RGBA", (*img.split(), alpha)).save(PLY / f"throbber-{i + 1:04d}.png")
    # Logo + Schriftzug als "Wasserzeichen" in der Bildschirmmitte
    lm = logo_mark(260)
    wm = wordmark("NOVAPLAY", 70)
    W = max(lm.width, wm.width)
    out = Image.new("RGBA", (W, lm.height + wm.height - 20), (0, 0, 0, 0))
    out.paste(lm, ((W - lm.width) // 2, 0), lm)
    out.paste(wm, ((W - wm.width) // 2, lm.height - 20), wm)
    out.save(PLY / "watermark.png")
    # Grafiken für Passwortabfrage (falls je gebraucht)
    e = Image.new("RGBA", (300, 36), (0, 0, 0, 0))
    ImageDraw.Draw(e).rounded_rectangle([0, 0, 299, 35], 10, fill=(20, 12, 40, 255), outline=PURPLE, width=2)
    e.save(PLY / "entry.png")
    b = Image.new("RGBA", (14, 14), (0, 0, 0, 0))
    ImageDraw.Draw(b).ellipse([1, 1, 12, 12], fill=CYAN)
    b.save(PLY / "bullet.png")
    lk = Image.new("RGBA", (32, 36), (0, 0, 0, 0))
    dl = ImageDraw.Draw(lk)
    dl.arc([6, 0, 25, 22], 180, 360, fill=WHITE, width=4)
    dl.rounded_rectangle([2, 14, 29, 35], 4, fill=PURPLE)
    lk.save(PLY / "lock.png")
    lk.save(PLY / "capslock.png")


# ===================== Bootmenü (BIOS, 640x480) =====================
def syslinux_splash():
    w, h = 640, 480
    img = gradient(w, h, BG_TOP, BG_BOTTOM)
    stars(img, 80, 4, 0.55)
    horizon = int(h * 0.68)
    img = sun(img, w / 2, horizon - 30, 70)
    floor = gradient(w, h - horizon, (16, 6, 40), (4, 2, 12))
    img.paste(floor, (0, horizon))
    img = synth_grid(img, horizon, PURPLE, 14)
    return img


if __name__ == "__main__":
    print("Erzeuge Hintergrundbilder ...")
    wallpaper_synthwave().save(SHARE / "novaplay-synthwave.png", optimize=True)
    wallpaper_hex().save(SHARE / "novaplay-hex.png", optimize=True)
    wallpaper_minimal().save(SHARE / "novaplay-minimal.png", optimize=True)
    print("Erzeuge Boot-Animation ...")
    plymouth_theme()
    print("Erzeuge Bootmenü-Bild ...")
    syslinux_splash().save(ROOT / "syslinux/splash.png")
    print("Fertig.")
