#!/bin/bash
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd -P)"

echo "-> Creating ~/.local/share/konsole folder"
mkdir -p ~/.local/share/konsole
echo "-> Copying Hypr.profile for Konsole"
cp "$SCRIPT_DIR/../config/konsole/Hypr.profile" ~/.local/share/konsole/Hypr.profile
echo "-> Setting Hypr.profile as default"
kwriteconfig6 --file konsolerc --group General --key DefaultProfile Hypr.profile
echo "-> Success"
