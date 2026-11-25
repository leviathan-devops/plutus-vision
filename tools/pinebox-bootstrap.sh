#!/usr/bin/env bash
# pinebox-bootstrap.sh - rebuild the Pinebox IDE on a fresh cloud container (root, Ubuntu 24.04, no display).
# Measured working 2026-11-25. Idempotent. Usage: tools/pinebox-bootstrap.sh [/path/to/pinebox.zip-extract/ship-approved-v2]
# After it prints READY:  export PATH=$HOME/.local/bin:$PATH XDG_RUNTIME_DIR=/run/user/0
#                         pinebox shot --session plutus-main --out /abs/frame.png
set -uo pipefail
S="${1:-/home/user/inputs/pinebox/ship-approved-v2}"
[ -d "$S/src/pinebox-cli" ] || { echo "REFUSED: no pinebox package at $S (unzip pinebox.zip to /home/user/inputs/pinebox first)"; exit 1; }
export DEBIAN_FRONTEND=noninteractive PATH="$HOME/.local/bin:$PATH" XDG_RUNTIME_DIR=/run/user/0
mkdir -p -m 700 "$XDG_RUNTIME_DIR"
need=""; for b in weston Xwayland xdotool tmux rsync xclip Xvfb ss xdpyinfo jq gcc; do command -v $b >/dev/null || need=1; done
if [ -n "$need" ]; then
  apt-get update -qq
  apt-get install -y -qq weston xwayland xdotool tmux rsync xclip xvfb imagemagick poppler-utils iproute2 procps psmisc lsof \
    x11-utils x11-xserver-utils xauth wmctrl x11-apps openbox libxcb1-dev pkg-config libxcb-icccm4-dev libxcb-ewmh-dev jq build-essential >/dev/null
fi
mkdir -p ~/.omp/agent/extensions ~/.local/share ~/.local/bin
rsync -a "$S/src/cu-v2/" ~/.omp/agent/extensions/computer-use-v2/
rsync -a "$S/src/pinebox-ext/" ~/.omp/agent/extensions/pinebox/
rsync -a --exclude node_modules --exclude runtime --exclude store "$S/src/pinebox-cli/" ~/.local/share/pinebox/
mkdir -p ~/.local/share/pinebox/data ~/.local/share/pinebox/tools
rsync -a "$S/src/pinebox-cloud/dist-web/data/bars/" ~/.local/share/pinebox/data/tv-bars/     # the TradingView bar store (DXY/EURUSD/GBPUSD x 15/30/60/240)
cp "$S/src/tools/harvest-tv.mjs" ~/.local/share/pinebox/tools/ 2>/dev/null || true
~/.omp/agent/extensions/computer-use-v2/helpers/build.sh >/dev/null
ln -sf ~/.omp/agent/extensions/computer-use-v2/computer ~/.local/bin/computer
ln -sf ~/.local/share/pinebox/pinebox ~/.local/bin/pinebox
( cd ~/.local/share/pinebox/fork/pine-ide/pine-station && [ -d node_modules/pinets ] || npm ci --omit=dev --no-audit --no-fund >/dev/null )
B=~/.local/share/pinebox/runtime/chrome; BV="$(cat ~/.local/share/pinebox/BROWSER_VERSION)"
if [ ! -x "$B/chrome-linux/chrome.real" ]; then
  T="$(mktemp -d)"; ( cd "$T" && npx --yes @puppeteer/browsers@2 install "chromium@$BV" --path "$T/b" >/dev/null )
  mkdir -p "$B"; mv "$(dirname "$(find "$T/b" -path '*chrome-linux/chrome' -type f | head -1)")" "$B/chrome-linux"; printf '%s' "$BV" > "$B/.version"
  # root in a container: Chromium refuses to start without --no-sandbox, and pinebox has no flag for it -> a wrapper
  mv "$B/chrome-linux/chrome" "$B/chrome-linux/chrome.real"
  printf '#!/bin/bash\nexec "$(dirname "$(readlink -f "$0")")/chrome.real" --no-sandbox "$@"\n' > "$B/chrome-linux/chrome"; chmod +x "$B/chrome-linux/chrome"
fi
computer doctor | tail -1
pinebox list --session plutus-main | grep -q '"id"' || pinebox up --session plutus-main --adapter xvfb --pair DXY --tf 1H | tail -3
