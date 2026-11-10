#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Generate the snowflake-textured panel backgrounds for Christmas Night.

The stock panel-background SVGs from the installed default theme (LGPL) are
used as the base. Their center piece is a 32x32 tile that KSvg repeats
across the panel (the stock file already contains hint-tile-center), so
snowflake artwork added to that tile stays crisp at any panel width.
"""

import gzip
import xml.etree.ElementTree as ET
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parents[1]
THEME_DIR = REPO_DIR / "desktoptheme" / "christmas-night"
DEFAULT_DIR = Path("/usr/share/plasma/desktoptheme/default")

VARIANTS = ["widgets", "opaque/widgets", "solid/widgets", "translucent/widgets"]

FROST = "#f2f6fb"
GOLD = "#ecb858"

FLAKES = [
    # (offset in tile, radius, color, opacity, stroke width)
    ((9, 11), 4.5, FROST, 0.10, 1.1),
    ((24, 23), 3.5, GOLD, 0.14, 1.0),
]

SVG_NS = "http://www.w3.org/2000/svg"


def snowflake(cx, cy, radius, color, opacity, width):
    group = ET.Element("g", {
        "stroke": color,
        "stroke-width": str(width),
        "stroke-linecap": "round",
        "stroke-linejoin": "round",
        "fill": "none",
        "opacity": str(opacity),
    })
    for angle in (0, 60, 120, 180, 240, 300):
        arm = ET.SubElement(group, "g", {"transform": f"rotate({angle} {cx} {cy})"})
        ET.SubElement(arm, "line", {
            "x1": f"{cx:.2f}", "y1": f"{cy:.2f}",
            "x2": f"{cx:.2f}", "y2": f"{cy - radius:.2f}",
        })
        branch_y = cy - radius * 0.6
        ET.SubElement(arm, "line", {
            "x1": f"{cx:.2f}", "y1": f"{branch_y:.2f}",
            "x2": f"{cx - radius * 0.3:.2f}", "y2": f"{cy - radius * 0.9:.2f}",
        })
        ET.SubElement(arm, "line", {
            "x1": f"{cx:.2f}", "y1": f"{branch_y:.2f}",
            "x2": f"{cx + radius * 0.3:.2f}", "y2": f"{cy - radius * 0.9:.2f}",
        })
    return group


def inject(svg_bytes):
    seen_uris = set()
    for event, (prefix, uri) in _iter_namespaces(svg_bytes):
        if uri in seen_uris:
            continue
        seen_uris.add(uri)
        ET.register_namespace(prefix, uri)

    root = ET.fromstring(svg_bytes)

    center_group = None
    for element in root.iter(f"{{{SVG_NS}}}g"):
        if element.get("id") == "center":
            center_group = element
            break
    if center_group is None:
        raise ValueError("no center group found")

    tile = None
    for rect in center_group.iter(f"{{{SVG_NS}}}rect"):
        if (rect.get("class") == "ColorScheme-Background"
                and rect.get("width") == "32" and rect.get("height") == "32"):
            tile = rect
            break
    if tile is None:
        raise ValueError("no 32x32 background tile found in center group")

    tile_x = float(tile.get("x", "0"))
    tile_y = float(tile.get("y", "0"))
    for (offset_x, offset_y), radius, color, opacity, width in FLAKES:
        center_group.append(
            snowflake(tile_x + offset_x, tile_y + offset_y, radius, color, opacity, width))

    return ET.tostring(root, encoding="utf-8")


def _iter_namespaces(svg_bytes):
    import io
    for event, data in ET.iterparse(io.BytesIO(svg_bytes), events=["start-ns"]):
        yield event, data

def main():
    for variant in VARIANTS:
        source = DEFAULT_DIR / variant / "panel-background.svgz"
        with gzip.open(source, "rb") as handle:
            svg_bytes = handle.read()
        result = inject(svg_bytes)
        target = THEME_DIR / variant / "panel-background.svgz"
        target.parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(target, "wb") as handle:
            handle.write(result)
        print(f"wrote {target}")


if __name__ == "__main__":
    main()
