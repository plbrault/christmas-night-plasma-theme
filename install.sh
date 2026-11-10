#!/usr/bin/env bash
# Installs the Christmas Night theme into the user's Plasma data directories.
set -euo pipefail

TARGET_DIR="${XDG_DATA_HOME:-$HOME/.local/share}"

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

python3 tools/generate-panel.py

mkdir -p "$TARGET_DIR/plasma/desktoptheme"
mkdir -p "$TARGET_DIR/plasma/look-and-feel"
mkdir -p "$TARGET_DIR/aurorae/themes"
mkdir -p "$TARGET_DIR/color-schemes"

rm -rf "$TARGET_DIR/plasma/desktoptheme/christmas-night"
cp -r desktoptheme/christmas-night "$TARGET_DIR/plasma/desktoptheme/"

rm -rf "$TARGET_DIR/plasma/look-and-feel/com.plbrault.christmasnight"
cp -r lookandfeel/com.plbrault.christmasnight "$TARGET_DIR/plasma/look-and-feel/"

rm -rf "$TARGET_DIR/aurorae/themes/ChristmasNight"
cp -r aurorae/ChristmasNight "$TARGET_DIR/aurorae/themes/"

cp colorscheme/ChristmasNight.colors "$TARGET_DIR/color-schemes/"

echo "Installed to $TARGET_DIR."
echo "Apply it with: plasma-apply-lookandfeel -a com.plbrault.christmasnight"
