#!/usr/bin/env bash
#
# run_governance.sh -- Python-path-portable wrapper around scripts/governance.sh.
#
# Why this exists: scripts/governance.sh defaults PYTHON to the Mac MacPorts
# interpreter (/opt/local/bin/python3, which carries torch 2.10.0). That path
# does not exist in the Cowork Linux sandbox, so a raw `bash scripts/governance.sh`
# there dies at Step 0 with "No such file or directory". The governance pipeline
# scripts are pure-data (no torch), so any python3 on PATH runs them correctly.
#
# This wrapper picks the right interpreter automatically:
#   1. An explicit PYTHON=... in the environment always wins.
#   2. Otherwise the Mac MacPorts python if present (keeps Mac behaviour identical).
#   3. Otherwise the first python3 on PATH (the Cowork sandbox / generic Linux).
#
# Usage (from REE_assembly/, or anywhere):
#   bash scripts/run_governance.sh            # full V3 governance pipeline
#   bash scripts/run_governance.sh --v2       # any flags pass straight through
#   PYTHON=/usr/bin/python3 bash scripts/run_governance.sh   # force an interpreter
#
set -uo pipefail

# Resolve the REE_assembly root from this script's location (scripts/ -> ..).
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$HERE" || { echo "ERROR: cannot cd to REE_assembly root ($HERE)" >&2; exit 1; }

# 1/2/3 interpreter selection.
if [ -z "${PYTHON:-}" ]; then
  if [ -x /opt/local/bin/python3 ]; then
    PYTHON=/opt/local/bin/python3
  else
    PYTHON="$(command -v python3 || true)"
  fi
fi

if [ -z "${PYTHON:-}" ] || ! "$PYTHON" -c 'import sys' >/dev/null 2>&1; then
  echo "ERROR: no usable python3 found. Set PYTHON=/path/to/python3 and retry." >&2
  exit 1
fi

echo "run_governance: PYTHON=$PYTHON ($("$PYTHON" --version 2>&1))"
echo "run_governance: cwd=$HERE"

# PYTHONUNBUFFERED=1 so step-by-step progress shows immediately when the output
# is redirected to a log (block buffering otherwise hides later steps).
exec env PYTHON="$PYTHON" PYTHONUNBUFFERED=1 bash scripts/governance.sh "$@"
