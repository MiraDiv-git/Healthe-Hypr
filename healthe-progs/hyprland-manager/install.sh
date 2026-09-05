#!/bin/bash
set -e
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd -P)"

if [ "$EUID" -eq 0 ]; then
    echo "Error: Do not run this script as root directly. It will ask for sudo when needed."
    exit 1
fi

echo "-> Installing dependencies"
sudo pacman -S --needed --noconfirm base-devel nano git python

if ! command -v yay &> /dev/null; then
    mkdir -p "$SCRIPT_DIR/deps"
    git clone https://aur.archlinux.org/yay.git "$SCRIPT_DIR/deps/yay"
    (
        cd "$SCRIPT_DIR/deps/yay"
        makepkg -si --noconfirm -r
    )
fi

echo "-> Installing Healthe Hypr CLI"
sudo install -Dm755 "$SCRIPT_DIR/hypr/main.py" "/usr/bin/hypr"

echo "-> Cleaning up..."
if [ -d "$SCRIPT_DIR/deps" ]; then
    rm -rf "$SCRIPT_DIR/deps"
fi

echo "-> Installed successfully"
