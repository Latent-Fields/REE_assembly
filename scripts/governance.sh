#!/usr/bin/env bash
# governance.sh — full REE_assembly governance pipeline
#
# Usage (from REE_assembly root):
#   bash scripts/governance.sh        # V3: build indexes, review list, rebuild site data
#   bash scripts/governance.sh --v2   # V2: also sync from ../ree-v2/ first
#
# Steps:
#   1. [V2 only] Sync V2 experiment results from ree-v2 into run-pack format
#   2. Build all evidence indexes (experiments, literature, planning, recommendations)
#   3. Generate pending_review.md
#   4. Rebuild claims.json for GitHub Pages hover tooltips
#
# Note: V3 experiments write run packs directly to evidence/experiments/ — no sync needed.

set -euo pipefail
cd "$(dirname "$0")/.."

PYTHON="${PYTHON:-/opt/local/bin/python3}"

V2=0
for arg in "$@"; do
  case $arg in
    --v2) V2=1 ;;
    *) echo "Unknown argument: $arg" >&2; exit 1 ;;
  esac
done

echo "=== REE Governance Pipeline ==="

if [ "$V2" -eq 1 ]; then
  echo "--- Step 1/4: Syncing V2 results from ree-v2/ ---"
  "$PYTHON" evidence/experiments/scripts/sync_v2_results.py
else
  echo "--- Step 1/4: Skipping V2 sync (V3 mode) ---"
fi

echo "--- Step 1b: Syncing V3 flat JSON results to run-pack format ---"
"$PYTHON" evidence/experiments/scripts/sync_v3_results.py

echo "--- Step 2/4: Building experiment indexes ---"
"$PYTHON" evidence/experiments/scripts/build_experiment_indexes.py

echo "--- Step 3/4: Generating pending review list ---"
"$PYTHON" scripts/generate_pending_review.py

echo "--- Step 4/5: Rebuilding claims.json for site tooltips ---"
"$PYTHON" scripts/build_claims_json.py

echo "--- Step 5/5: Rebuilding contributor ledger ---"
"$PYTHON" contributors/build_contributions.py

echo ""
echo "Done. Check evidence/experiments/pending_review.md for experiments awaiting review."
echo "After editing claims.yaml, re-run step 4: python scripts/build_claims_json.py"
