#!/usr/bin/env bash
# Build a single-file distributable binary for ree_tray.py using PyInstaller.
#
# Output:
#   dist/ree_tray          (Linux / Mac binary)
#   dist/ree_tray.exe      (Windows, when run under Windows)
#
# Usage:
#   cd REE_assembly/tray
#   bash build_tray.sh
#
# Requirements:
#   pip install pyinstaller pystray Pillow requests

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

# Install deps if not already present
echo "[build_tray] Checking dependencies ..."
python3 -m pip install --quiet pyinstaller pystray Pillow requests

echo "[build_tray] Building ree_tray ..."

python3 -m PyInstaller \
    --onefile \
    --windowed \
    --name ree_tray \
    --clean \
    ree_tray.py

echo ""
echo "[build_tray] Done. Binary is at: ${SCRIPT_DIR}/dist/ree_tray"
echo ""
echo "Run it:"
echo "  ./dist/ree_tray"
echo ""
echo "To connect to a remote host:"
echo "  REE_TRAY_HOST=192.168.1.10:8000 ./dist/ree_tray"
