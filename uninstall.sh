#!/usr/bin/env bash
# Removes the Christmas Night theme from the user's Plasma data directories.
set -euo pipefail

TARGET_DIR="${XDG_DATA_HOME:-$HOME/.local/share}"

rm -rf "$TARGET_DIR/plasma/desktoptheme/christmas-night"
rm -rf "$TARGET_DIR/plasma/look-and-feel/com.plbrault.christmasnight"
rm -rf "$TARGET_DIR/aurorae/themes/ChristmasNight"
rm -f "$TARGET_DIR/color-schemes/ChristmasNight.colors"

echo "Removed. If it was active, switch to another theme in System Settings."
