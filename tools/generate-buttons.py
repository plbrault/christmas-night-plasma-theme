#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Generate the aurorae button SVGs for the Christmas Night theme.

Each button SVG is a 132x44 canvas holding six 22x22 cells, one per state
(active, hover, pressed, inactive, hover-inactive, pressed-inactive).
Aurorae crops each state by element id and renders it at the configured
button size, so cell positions on the canvas do not matter, they only
keep the source files readable.
"""

from pathlib import Path

THEME_DIR = Path(__file__).resolve().parents[1] / "aurorae" / "ChristmasNight"

SNOW = "#f2f6fb"
SNOW_DIM = "#b6c0cc"

STATES = [
    ("active-center", 0, 0, "base"),
    ("hover-center", 22, 0, "hover"),
    ("pressed-center", 44, 0, "pressed"),
    ("inactive-center", 66, 0, "inactive"),
    ("hover-inactive-center", 88, 0, "inactive-hover"),
    ("pressed-inactive-center", 110, 0, "inactive-pressed"),
]

FILL = {
    "close": {"base": "#c9494f", "hover": "#e25a60", "pressed": "#8f353a"},
    "minimize": {"base": "#3f8f60", "hover": "#4aa06e", "pressed": "#2d6444"},
    "maximize": {"base": "#c99e44", "hover": "#ecb858", "pressed": "#8a6a2c"},
    "restore": {"base": "#c99e44", "hover": "#ecb858", "pressed": "#8a6a2c"},
    "alldesktops": {"base": "#4a7ba6", "hover": "#5f96c4", "pressed": "#35587a"},
    "keepabove": {"base": "#4a7ba6", "hover": "#5f96c4", "pressed": "#35587a"},
    "keepbelow": {"base": "#4a7ba6", "hover": "#5f96c4", "pressed": "#35587a"},
    "shade": {"base": "#4a7ba6", "hover": "#5f96c4", "pressed": "#35587a"},
    "help": {"base": "#4a7ba6", "hover": "#5f96c4", "pressed": "#35587a"},
}

FILL["inactive"] = "#4a525e"
FILL["inactive-hover"] = "#5a6472"
FILL["inactive-pressed"] = "#3c434d"


def strokes(color):
    return (f'stroke="{color}" stroke-width="1.6" stroke-linecap="round" '
            f'stroke-linejoin="round" fill="none"')


def snowflake(color):
    arms = []
    for angle in (0, 60, 120, 180, 240, 300):
        arms.append(
            f'  <g transform="rotate({angle} 11 11)" {strokes(color)}>\n'
            '    <line x1="11" y1="11" x2="11" y2="4.8"/>\n'
            '    <line x1="11" y1="6.4" x2="9.5" y2="4.9"/>\n'
            '    <line x1="11" y1="6.4" x2="12.5" y2="4.9"/>\n'
            '  </g>'
        )
    return "\n".join(arms)


def glyph(name, color):
    if name == "close":
        return f'<path d="M 7.4,7.4 L 14.6,14.6 M 14.6,7.4 L 7.4,14.6" {strokes(color)}/>'
    if name == "minimize":
        return f'<path d="M 7,11 H 15" {strokes(color)}/>'
    if name == "maximize":
        return (f'<rect x="6.6" y="6.6" width="8.8" height="8.8" rx="1.6" '
                f'{strokes(color)}/>')
    if name == "restore":
        return (
            f'<path d="M 9.6,6.2 H 15.8 V 12.4" {strokes(color)}/>\n'
            f'  <rect x="6.2" y="9.4" width="7.2" height="7.2" rx="1.4" '
            f'{strokes(color)}/>'
        )
    if name == "alldesktops":
        return snowflake(color)
    if name == "keepabove":
        return (
            f'<path d="M 6.8,11.6 L 11,7.6 L 15.2,11.6" {strokes(color)}/>\n'
            f'  <path d="M 6.8,15.4 L 11,11.4 L 15.2,15.4" {strokes(color)}/>'
        )
    if name == "keepbelow":
        return (
            f'<path d="M 6.8,7.6 L 11,11.6 L 15.2,7.6" {strokes(color)}/>\n'
            f'  <path d="M 6.8,11.4 L 11,15.4 L 15.2,11.4" {strokes(color)}/>'
        )
    if name == "shade":
        return (
            f'<path d="M 7,7.4 H 15" {strokes(color)}/>\n'
            f'  <path d="M 7.4,15 L 11,11.2 L 14.6,15" {strokes(color)}/>'
        )
    if name == "help":
        return (
            f'<path d="M 8.4,8.6 A 2.6,2.6 0 1 1 11.6,11.9 C 10.9,12.4 10.7,12.9 10.7,13.6" '
            f'{strokes(color)}/>\n'
            f'  <circle cx="10.7" cy="16.2" r="0.95" fill="{color}" stroke="none"/>'
        )
    raise ValueError(name)


def button_svg(name):
    parts = [
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
        f'<!-- Christmas Night aurorae button: {name} -->',
        '<svg width="132" height="44" viewBox="0 0 132 44" version="1.1"',
        '     xmlns="http://www.w3.org/2000/svg">',
    ]
    for state_id, cell_x, cell_y, state in STATES:
        if state.startswith("inactive"):
            fill = FILL[state]
            glyph_color = SNOW_DIM
        else:
            fill = FILL[name][state]
            glyph_color = SNOW
        parts.append(
            f'  <g id="{state_id}" transform="translate({cell_x},{cell_y})">\n'
            f'    <circle cx="11" cy="11" r="9" fill="{fill}"/>\n'
            f'    {glyph(name, glyph_color)}\n'
            f'  </g>'
        )
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def main():
    for name in FILL:
        if name.startswith("inactive"):
            continue
        path = THEME_DIR / f"{name}.svg"
        path.write_text(button_svg(name))
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
