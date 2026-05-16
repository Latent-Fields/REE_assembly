#!/usr/bin/env bash
# governance.sh — full REE_assembly governance pipeline
#
# Usage (from REE_assembly root):
#   bash scripts/governance.sh        # V3: build indexes, review list, rebuild site data
#   bash scripts/governance.sh --v2   # V2: also sync from ../ree-v2/ first
#
# Steps:
#   1. [V2 only] Sync V2 experiment results from ree-v2/ into run-pack format
#   1b. Sync V3 flat JSON results to run-pack format
#   2. Build all evidence indexes (experiments, literature, planning, recommendations)
#   3. Generate pending_review.md
#   4. Rebuild claims.json for GitHub Pages hover tooltips
#   5. Rebuild claim dependency process dashboard data
#   6. Rebuild contributor ledger
#   7. Refresh governance_agenda.v1.json timestamps (keeps explorer banner current)
#
# Note: V3 experiments write run packs directly to evidence/experiments/ -- no sync needed.

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

echo "--- Step 0: Validating claims.yaml (strict) ---"
if ! "$PYTHON" scripts/validate_claims.py --strict; then
  echo "" >&2
  echo "ERROR: validate_claims.py --strict failed. Fix claims.yaml before running governance." >&2
  exit 1
fi

if [ "$V2" -eq 1 ]; then
  echo "--- Step 1/7: Syncing V2 results from ree-v2/ ---"
  "$PYTHON" evidence/experiments/scripts/sync_v2_results.py
else
  echo "--- Step 1/7: Skipping V2 sync (V3 mode) ---"
fi

echo "--- Step 1b: Syncing V3 flat JSON results to run-pack format ---"
"$PYTHON" evidence/experiments/scripts/sync_v3_results.py

echo "--- Step 2/7: Building experiment indexes ---"
"$PYTHON" evidence/experiments/scripts/build_experiment_indexes.py

echo "--- Step 3/7: Generating pending review list ---"
"$PYTHON" scripts/generate_pending_review.py

echo "--- Step 3b: Generating Option E shadow recommendations ---"
"$PYTHON" scripts/generate_option_e_shadow.py

echo "--- Step 4/7: Rebuilding claims.json for site tooltips ---"
"$PYTHON" scripts/build_claims_json.py

echo "--- Step 4b: Backward traceability check (G2) ---"
if ! "$PYTHON" scripts/check_backward_traceability.py; then
  echo "" >&2
  echo "WARNING: check_backward_traceability.py found developmental claims missing from" >&2
  echo "         docs/architecture/developmental_needs_register.md." >&2
  echo "         Re-run with --warn-only for informational output without blocking." >&2
  echo "         To suppress: add the claim to the register or run with SKIP_TRACEABILITY=1" >&2
  if [ "${SKIP_TRACEABILITY:-0}" = "1" ]; then
    echo "         SKIP_TRACEABILITY=1 set -- continuing despite warnings." >&2
  else
    exit 1
  fi
fi

echo "--- Step 5/7: Rebuilding claim dependency process dashboard data ---"
"$PYTHON" scripts/build_claim_dependency_process.py

echo "--- Step 6/7: Rebuilding contributor ledger ---"
"$PYTHON" contributors/build_contributions.py

echo "--- Step 7/7: Refreshing governance_agenda.v1.json timestamps ---"
"$PYTHON" scripts/refresh_governance_agenda_timestamp.py

echo ""
echo "Done. Check evidence/experiments/pending_review.md for experiments awaiting review."
echo "After editing claims.yaml, re-run step 4: python scripts/build_claims_json.py"
