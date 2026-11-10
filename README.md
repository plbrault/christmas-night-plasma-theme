# Christmas Night — a KDE Plasma theme

A dark and cozy winter-night theme for KDE Plasma 6: deep night-blue panels,
snow-white text, and warm pine green, cranberry and gold accents.

The wallpaper is intentionally left untouched — this theme only covers the
plasma theme colors, the application color scheme and the window decoration.

## Contents

| Component | What it is | Package id |
| --- | --- | --- |
| Look & Feel | Glue package that applies everything at once | `com.plbrault.christmasnight` |
| Plasma theme | Colors for panels, widgets, tooltips and popups (SVGs are inherited from the stock `default` theme) | `christmas-night` |
| Color scheme | Night blues and snow white for applications | `ChristmasNight` |
| Aurorae decoration | Frosted night-blue titlebars with a gold top edge and colored snowflake-era buttons | `ChristmasNight` |

The button glyph palette: cranberry (close), pine green (minimize), gold
(maximize/restore), frost blue with a snowflake (all desktops), chevrons
(keep above / keep below), shade and help.

## Install

```
./install.sh
```

This copies the packages into `~/.local/share` (`plasma/desktoptheme`,
`plasma/look-and-feel`, `aurorae/themes` and `color-schemes`).

## Apply

Apply everything at once:

```
plasma-apply-lookandfeel -a com.plbrault.christmasnight
```

Or apply components individually:

```
plasma-apply-desktoptheme christmas-night
plasma-apply-colorscheme ChristmasNight
```

and pick `Christmas Night` in `System Settings → Colors & Themes → Window Decorations`.
Applying the global theme through `System Settings → Colors & Themes → Global Theme` works too.

The look-and-feel package sets the Breeze Dark icon theme, since dark panels
need dark icons. It does not set a wallpaper, a splash screen or a cursor
theme, so those stay as they are.

## Uninstall

```
./uninstall.sh
```

## License

Copyright © 2026 Pier-Luc Brault <pier-luc@brault.me>

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
