#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Generates the aktujo brand kit: master SVGs, PNG exports, favicon.ico, the website's head icons and the apps' icons.

The mark is a document folder – *aktujo*, Esperanto for a container of documents – with a sheet in it and a keyhole
in its front: documents kept, and kept private. One accent, sealing-wax red. The wordmark is set in Space Mono Bold
(SIL OFL) with a block cursor in the accent. The wordmark is turned into outlines here (fontTools), so it
needs no font where it is shown.

Needs rsvg-convert (Homebrew: librsvg) and fontTools (pip install fonttools). Run from anywhere:
    python3 generate.py
Edit this file, not the exports.
"""
import os
import shutil

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

from brandkit import export, ico, render, svg, write

HERE = os.path.dirname(os.path.abspath(__file__))
NAME = "aktujo"
TAGLINE = "Your documents, kept safe – end to end"

NIGHT = "#0D1117"         # near-black – backgrounds
PAPER = "#E6EDF3"         # text and strokes on dark
INK = "#14202B"             # text and strokes on light
ACCENT = "#B3262B"       # the one accent, sealing-wax red, on dark
ACCENT_DARK = "#9E1F24"  # the accent on light backgrounds
STEEL = "#5B7083"           # rules, secondary
REED = "#8B949E"            # muted text
GRID = "#1C232B"           # faint grid on dark
MONO = "'Space Mono', ui-monospace, 'SF Mono', Menlo, 'DejaVu Sans Mono', Consolas, monospace"

DARK = dict(face=PAPER, accent=ACCENT, bg=NIGHT)
LIGHT = dict(face=INK, accent=ACCENT_DARK, bg="#FFFFFF")

# --- mark (drawn in a 100×100 box) -----------------------------------------------------------------------------------

MARK_BOX = "0 0 100 100"
KEYHOLE = "M50 55 A7 7 0 0 1 54 67.7 L56 77 H44 L46 67.7 A7 7 0 0 1 50 55 Z"   # cut out of the folder (even-odd)


def mark(p=DARK, keyhole=True):
    """A sheet in a folder with a tab; the keyhole is a hole, so any background shows through it."""
    hole = f" {KEYHOLE}" if keyhole else ""
    return (f'<rect x="26" y="12" width="48" height="36" fill="none" stroke="{p["face"]}" stroke-width="6"/>'
            f'<path d="M10 36 H38 L44 44 H90 V88 H10 Z{hole}" fill="{p["accent"]}" fill-rule="evenodd"/>')


def flat_mark(color):
    return mark(dict(face=color, accent=color))


def small_mark(p=DARK):
    """16–48 px: heavier sheet, larger folder, no keyhole."""
    return (f'<rect x="24" y="8" width="52" height="46" fill="none" stroke="{p["face"]}" stroke-width="10"/>'
            f'<path d="M6 34 H38 L45 43 H94 V92 H6 Z" fill="{p["accent"]}"/>')


def placed(body, cx, cy, width, box=100):
    k = width / box
    return f'<g transform="translate({cx} {cy}) scale({k:.4f}) translate({-box / 2} {-box / 2})">{body}</g>'


def icon(rounded=True, small=False):
    r = 160 if rounded else 0
    body = small_mark() if small else mark()
    return svg("0 0 1024 1024", f'<rect width="1024" height="1024" rx="{r}" fill="{NIGHT}"/>'
               + placed(body, 512, 512, 800 if small else 720))


def mac_icon(small=False):
    """macOS app icon: the body 824 px of 1024 with a transparent margin, as Apple's icon grid has it; the small mark at
    16 and 32 px."""
    body = placed(small_mark(), 512, 512, 640) if small else placed(mark(), 512, 512, 580)
    return svg("0 0 1024 1024", f'<rect x="100" y="100" width="824" height="824" rx="185" fill="{NIGHT}"/>' + body)


# --- wordmark (Space Mono Bold as outlines, 80 px, baseline at y = 80) -----------------------------------------------

SIZE = 80
FONT = os.path.join(HERE, "fonts", "SpaceMono-Bold.ttf")


def name_outline(color):
    """The name as one path in the font's outlines. Returns the path and its advance width."""
    f = TTFont(FONT)
    gs, cmap, hmtx = f.getGlyphSet(), f.getBestCmap(), f["hmtx"]
    k, x, d = SIZE / f["head"].unitsPerEm, 0.0, ""
    for ch in NAME:
        g = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (k, 0, 0, -k, x, 80)))
        d += pen.getCommands()
        x += hmtx[g][0] * k
    return f'<path d="{d}" fill="{color}"/>', x


ADVANCE = SIZE * 0.6


def wordmark_body(p=DARK):
    """The name and a block cursor in the accent. Returns the body and its width."""
    path, w = name_outline(p["face"])
    body = path + f'<rect x="{w + 2:.0f}" y="26" width="{ADVANCE * 0.8:.0f}" height="58" fill="{p["accent"]}"/>'
    return body, w + 2 + ADVANCE * 0.8


def wordmark(p=DARK):
    body, width = wordmark_body(p)
    return svg(f"-8 10 {width + 16:.0f} 90", body)


def lockup(p=DARK):
    body, width = wordmark_body(p)
    return svg(f"-4 2 {width + 140:.0f} 106",placed(mark(p), 50, 55, 92) + f'<g transform="translate(122 0)">{body}</g>')


def social():
    """1280×640: GitHub social preview, link previews – terminal style."""
    body, _ = wordmark_body(DARK)
    grid = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="640" stroke="{GRID}"/>' for x in range(0, 1281, 64)) + \
           "".join(f'<line x1="0" y1="{y}" x2="1280" y2="{y}" stroke="{GRID}"/>' for y in range(0, 641, 64))
    return svg("0 0 1280 640", f'<rect width="1280" height="640" fill="{NIGHT}"/>{grid}'
               + placed(mark(), 260, 320, 300) +
               f'<text x="480" y="200" font-family="{MONO}" font-size="26" fill="{REED}">$ {NAME} --about</text>'
               f'<g transform="translate(476 220) scale(1.3)">{body}</g>' +
               "".join(f'<text x="480" y="{404 + 38 * i}" font-family="{MONO}" font-size="28" fill="{PAPER}">{line}</text>'
                       for i, line in enumerate((TAGLINE.replace(" – ", " –\n") if len(TAGLINE) > 40 else TAGLINE).split("\n"))) +
               f'<text x="480" y="504" font-family="{MONO}" font-size="24" fill="{REED}">// free software · a falkOSS project</text>',
               (1280, 640))


def favicon():
    """The small mark, transparent: paper on dark tabs, ink on light ones."""
    style = (f'<style>.f{{stroke:{PAPER}}}.c{{fill:{ACCENT}}}'
             f'@media (prefers-color-scheme: light){{.f{{stroke:{INK}}}.c{{fill:{ACCENT_DARK}}}}}</style>')
    body = small_mark().replace(f'stroke="{PAPER}"', 'class="f"').replace(f'fill="{ACCENT}"', 'class="c"')
    return svg(MARK_BOX, style + body)


def main():
    kit = {
        "icon": icon(),
        "icon-square": icon(rounded=False),
        "icon-small": icon(small=True),
        "mark-on-dark": svg(MARK_BOX, mark(DARK)),
        "mark-on-light": svg(MARK_BOX, mark(LIGHT)),
        "mark-black": svg(MARK_BOX, flat_mark("#000000")),
        "mark-white": svg(MARK_BOX, flat_mark("#FFFFFF")),
        "wordmark-on-dark": wordmark(DARK),
        "wordmark-on-light": wordmark(LIGHT),
        "lockup-on-dark": lockup(DARK),
        "lockup-on-light": lockup(LIGHT),
        "social": social(),
        "favicon": favicon(),
    }
    export(HERE, NAME, kit, NIGHT)
    apps()


def no_alpha(path):
    """The App Store refuses icons with an alpha channel; rsvg-convert writes RGB when nothing is transparent."""
    with open(path, "rb") as f:
        color = f.read(26)[25]
    assert color == 2, f"{path}: alpha channel"


def apps():
    """The apps' icons, named and placed as the Flutter runners of aktujo/apps expect them (copied there)."""
    svg_dir, png_dir, apps_dir = (os.path.join(HERE, d) for d in ("svg", "png", "apps"))
    if os.path.isdir(apps_dir):
        shutil.rmtree(apps_dir)
    s = lambda key: os.path.join(svg_dir, f"{NAME}-{key}.svg")
    write(s("icon-macos"), mac_icon())
    write(s("icon-macos-small"), mac_icon(small=True))
    for size in (16, 32, 64, 128, 256, 512, 1024):
        render(s("icon-macos-small" if size <= 32 else "icon-macos"),
               os.path.join(apps_dir, "macos", f"app_icon_{size}.png"), size)
    for point, scales in (("20x20", (1, 2, 3)), ("29x29", (1, 2, 3)), ("40x40", (1, 2, 3)), ("60x60", (2, 3)),
                          ("76x76", (1, 2)), ("83.5x83.5", (2,)), ("1024x1024", (1,))):
        for k in scales:
            dst = os.path.join(apps_dir, "ios", f"Icon-App-{point}@{k}x.png")
            render(s("icon-square"), dst, round(float(point.split("x")[0]) * k))
            no_alpha(dst)
    for density, size in (("mdpi", 48), ("hdpi", 72), ("xhdpi", 96), ("xxhdpi", 144), ("xxxhdpi", 192)):
        render(s("icon"), os.path.join(apps_dir, "android", f"mipmap-{density}", "ic_launcher.png"), size)
    big = os.path.join(apps_dir, "windows", "icon-256.png")
    render(s("icon"), big, 256)
    small = [(n, os.path.join(png_dir, "icon-small", f"{NAME}-icon-small-{n}.png")) for n in (16, 32, 48)]
    ico(os.path.join(apps_dir, "windows", "app_icon.ico"), small + [(256, big)])
    os.remove(big)
    print("app icons written to", apps_dir)


if __name__ == "__main__":
    main()
