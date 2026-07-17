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

echo "--- Step 0b: Claim phase-consistency (warn-only: phase-label-follows-dependency) ---"
# Surfaces v3 build commitments that depend on v4+ claims (reclassification
# candidates) per docs/architecture/claim_phase_provenance.md. Report-only; does
# not edit claims.yaml. Promote to --strict (blocking) once the backlog is
# adjudicated -- same trajectory validate_claims.py took. Never blocks today.
"$PYTHON" scripts/check_claim_phase_consistency.py --warn || true

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

echo "--- Step 3c-pre: Closure-plan frontmatter strict-YAML lint (warn-only) ---"
# Catches an unquoted prose scalar (a stray ': ' in owner_exq / resume_condition /
# governance_* etc.) that parses under the snapshot's stale on-disk artifact but
# FAILS the strict yaml.safe_load the live explorer uses, silently dropping the
# whole plan to frontmatter_pending. Incident 2026-06-19 (commit 4c0313b052).
"$PYTHON" scripts/check_plan_frontmatter.py || true

echo "--- Step 3c-quater: Closure-map dangling-link check (warn-only) ---"
# Flags depends_on / cross_plan_link targets that are neither a node id nor a plan
# id -- typos that silently drop edges from closure.html instead of erroring.
# Incident 2026-06-20 (object_representation:OBJ-1 missing _v4; mirror_modelling vs
# mirror_modelling_other_self_v5), found only by manual audit. Exits non-zero on any
# dangling ref (excluding the one exempt sleep_substrate:GAP-2 back-pointer); kept
# warn-only here -- run `python scripts/check_closure_links.py` directly as a strict
# gate. Promote to blocking once the closure frontmatter is stable.
"$PYTHON" scripts/check_closure_links.py || true

echo "--- Step 3c-pre-heal: Self-heal status-plane drift (SHP-3; re-stamp in place, NO commit) ---"
# status_history_plane:SHP-3. Closes the SHP-3 automation gap: check_closure_drift's
# status-plane section only REPORTED drift (a collapsed node whose stored two-plane
# `live:` head fell out of step with the re-projection). This re-stamps every
# fully-collapsed drifted plan IN PLACE via shp2_collapse_plan.py (the ONE projection
# path), so the Step 3c report below reflects the post-heal state. Runs BEFORE 3c on
# purpose. Deliberately does NOT git-add/commit -- it leaves the edited *_plan.md in
# the working tree for a human to review + commit pathspec-limited (the derive-only /
# no-trunk-writer-auto-commit posture + CLAUDE.md dropped-file discipline). A drifted
# plan that still has un-collapsed blob nodes is SKIPPED (collapse-migration stays a
# human step) and surfaced with its manual command. Exits 0 always (a hint, never a
# gate). PROMOTES/DEMOTES NOTHING; edits only derived live:/join: blocks.
"$PYTHON" scripts/heal_status_plane_drift.py || true

echo "--- Step 3c: Closure-plan drift check (warn-only) ---"
"$PYTHON" scripts/check_closure_drift.py

echo "--- Step 3c-tris: Inter-governance workset regen + drift check (warn-only) ---"
"$PYTHON" scripts/generate_inter_governance_workset.py
"$PYTHON" scripts/check_workset_drift.py

echo "--- Step 3c-bis: Closure-status snapshot (server-free rollup) ---"
"$PYTHON" scripts/generate_closure_snapshot.py

echo "--- Step 3c-bis-6: Scientific Progress Dashboard rollup (Build/Prove/Narrow/Decide) ---"
# DERIVE-ONLY sibling of the closure snapshot. Joins the FROZEN hypothesis-space
# registry against the autopsy/manifest/evidence/substrate/closure data to build
# evidence/planning/hypothesis_space.v1.json (+ append-only time series) for the
# /progress dashboard. Runs AFTER the closure snapshot so Dimension 2 embeds the
# fresh closure %. Never a gate; exits 0. NO write-back to claims.yaml/closure/scorer.
"$PYTHON" scripts/build_hypothesis_space.py || true

echo "--- Step 3c-bis-6b: Hypothesis-space integrity audit (anti-Goodhart, warn-only) ---"
# Sibling of check_closure_drift.py. Flags un-backed surviving-count drops,
# post-hoc enlargement of a frozen initial set, and confirmed nodes lacking a
# passed control. Advisory, non-blocking; exits 0.
"$PYTHON" scripts/check_hypothesis_space_integrity.py || true

echo "--- Step 3c-bis-2: Current-front routing doc (SHP-6; derives docs/CURRENT_FRONT.md) ---"
# SHORT, LIVE-ONLY front doc the Session-Startup entry docs route to (fixes the
# status_history_plane 'Failure A -- routing'). Derived from insights_report.md +
# the closure snapshot just produced; regenerable, PROMOTES/DEMOTES NOTHING.
"$PYTHON" scripts/generate_current_front.py

echo "--- Step 3c-bis-3: Retire abandoned manual status docs (SHP-7; regenerates stubs) ---"
# Owns the 3 docs that had NO generator and rotted silently (GOVERNANCE_STATE.md,
# REE_overview.md, index.md) -- regenerates them GENERATED-marked + timestamped so a
# cold-start reader can't mistake stale hand-prose for current state. Must run BEFORE
# Step 9 apply_nav_frontmatter.py (which owns these docs' nav frontmatter + preserves
# the body written here). PROMOTES/DEMOTES NOTHING.
"$PYTHON" scripts/generate_status_stubs.py

echo "--- Step 3c-bis-4: Promote status-plane history (SHP-3; snapshot log + committed sidecars) ---"
# status_history_plane:SHP-3. Appends a CHANGE-ONLY status_snapshot/v1 projection
# record per node (the derived live head at this run's timestamp) onto the
# append-only evidence/planning/status_history/status_snapshot.v1.jsonl, and
# regenerates the committed per-plan *_history.md sidecars under
# status_history/history/ (server-free human view). Change-only append (a stable
# run with no new events appends ZERO records) mirrors the state-change heartbeat
# design that retired the git-history-bloating liveness tick. Shares the ONE
# projection path with project_status_head.py (SHP-1) + check_closure_drift.py.
# PROMOTES/DEMOTES NOTHING; edits no *_plan.md, no claims.yaml.
"$PYTHON" scripts/promote_status_history.py

echo "--- Step 3c-bis-5: Claims live_status drift check (SHP-4; warn-only) ---"
# status_history_plane:SHP-4. Doc-status-plane analog of the closure-plan drift
# check, for the per-claim live_status block in claims.yaml. Re-derives each claim's
# live_status: the STATUS-PLANE reading (reading/as_of/needs_review) as a pure fn of
# status+v3_pending+epistemic_category, PLUS the SHP-4 event-provenance sub-block
# (live_status.evidence: from/as_of/verdict) re-projected from the append-only event
# log via project_status_head (the ONE projection path). Warns when the STORED block
# differs from the re-derivation (the stamper scripts/apply_live_status.py was not
# re-run since a claim's status moved / a new event landed, or the block was
# hand-edited). Mirror of Step 9c's claims_doc_drift.py, but deliberately WARN-ONLY
# (no --strict) -- UNLIKE the SHP-5 doc stamper at Step 9b, apply_live_status.py is
# NOT run in this pipeline: it WRITES high-contention claims.yaml, which the
# derive-only governance pipeline must not do (heartbeat-autostash rule + derive-only
# invariant), and it stays a claimed manual op. A --strict gate here would abort
# governance the moment any claim's status changes or a new event lands. When this
# report shows HARD reading-drift, an operator re-stamps by running
# `scripts/apply_live_status.py` under a TASK_CLAIMS claim on docs/claims/claims.yaml.
# (Event-provenance drift is warn-only even in --strict -- it fluctuates as the fleet
# produces evidence.) PROMOTES/DEMOTES NOTHING; edits no claims.yaml.
"$PYTHON" scripts/claims_live_status_drift.py || true

echo "--- Step 3d: Brain region map drift check (warn-only) ---"
"$PYTHON" scripts/validate_brain_region_map.py || true

echo "--- Step 3e: Substrate-ceiling mapping + exhaustion audit (warn-only) ---"
# Reports the substrate_ceiling partition (mapped / parked / self-handled /
# may-have-lifted / orphaned) AND the GOV-CEIL-1 ceiling-exhaustion overlay
# (>=N confirmed ceiling autopsies with no richer-substrate win -> surface for
# user-approved demotion at governance Step 6a-v). Read-only; never edits
# claims.yaml. Warn-only here -- run with --strict for a blocking CI gate.
"$PYTHON" scripts/check_substrate_ceiling_audit.py || true

echo "--- Step 3f: Diagnostic-chain recurrence audit (GOV-DIAG-1, warn-only) ---"
# Diagnostic-side analog of the claim-keyed re-derive brake / GOV-CEIL-1. Counts
# confirmed pure-diagnostic (claim_ids=[]) no-verdict failure autopsies grouped by
# their bears_on work-stream token; a token with >=N (default 3) hits surfaces a
# "diagnostic-chain recurrence -- question may be mis-posed, not under-powered"
# overlay (governance Step 6a-v-ter). Catches the claim_ids=[] chains that
# accumulate ZERO on every claim-keyed counter. Read-only; promotes/demotes
# nothing. Warn-only here -- run with --strict for a blocking CI gate.
"$PYTHON" scripts/check_diagnostic_chain_recurrence.py || true

echo "--- Step 3g: Granularity-debt recurrence audit (GOV-GRAN-1, warn-only) ---"
# The THIRD claim-keyed recurrence sibling and the standing-scan complement to the
# REACTIVE granularity-debt trigger in the /failure-autopsy skill. GOV-CEIL-1 (3e)
# catches SAME-wall ceiling recurrence (-> demotion); GOV-DIAG-1 (3f) catches
# claimless mis-posed-question chains (-> re-pose). This catches claim-keyed
# DIFFERENT-signature recurrence: >=N no-verdict NON-ceiling autopsies circling one
# claim in structurally different ways -> the claim is too COARSE (several claims)
# -> /claim-synthesis decomposition. Surfaces two things a human autopsy author can
# miss: P0 a DROPPED HANDOFF (an autopsy fired the trigger / routed to
# /claim-synthesis but no claim_synthesis_<claim>_*.md exists -- the "relies on a
# human doing the next step" reliability hole, made mechanical), and P1 an
# UNFLAGGED recurrence spread across sessions no one author saw together. This is
# the too-COARSE analog of the non-degeneracy net (which catches the inverse,
# too-FINE / degenerate-criterion, with standing code). Excludes substrate_ceiling
# hits (GOV-CEIL-1's lane) + already-metabolized claims (decomposition_note /
# existing claim_synthesis doc / suppressed epistemic_category). Read-only;
# promotes/demotes nothing; response is a human decision at Step 6a-v-quater. Run
# with --strict for a blocking CI gate.
"$PYTHON" scripts/check_granularity_debt_recurrence.py || true

echo "--- Step 4/7: Rebuilding claims.json for site tooltips ---"
"$PYTHON" scripts/build_claims_json.py

echo "--- Step 4a: Rebuilding epistemic overlay (posteriors + emergent_from alarm) ---"
# Derive-only Phase-1 overlay (Option C + C-slice of D): joins the Beta
# posteriors in claim_evidence.v1.json (Step 2) with the emergent_from edges in
# claims.yaml -> docs/assets/data/epistemic_overlay.json. Promotes/demotes
# nothing. Plan: evidence/planning/epistemic_overlay_plan.md.
"$PYTHON" scripts/build_epistemic_overlay.py || true

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

echo "--- Step 8: Rebuilding static site visualizations (brain map snapshot + fishtank) ---"
"$PYTHON" scripts/build_site_visualizations.py

echo "--- Step 9: Left-nav tidiness (hide unplaced docs; warn on titled leaks) ---"
# Self-maintaining sidebar: re-stamps known pages and hides any new titled-but-
# unplaced doc so plan/design docs never leak raw into the menu. --check first so
# a genuine leak is loud in the log even though the run also auto-hides it.
"$PYTHON" docs/apply_nav_frontmatter.py --check || echo "  (nav leak above will be auto-hidden by the stamping run)"
"$PYTHON" docs/apply_nav_frontmatter.py

echo "--- Step 9b: Stamp claims.yaml-derived status frontmatter on architecture docs (SHP-5) ---"
# Companion to the nav stamper: derives status:/status_asof:/status_claim: frontmatter
# from claims.yaml for every architecture doc that names a claim id, and retires the
# boilerplate hand-typed **Status:** body lines (prose lines are kept -- razor). MUST run
# AFTER the nav stamper (both own the frontmatter block; nav preserves the status_* keys,
# so the pair composes either way). Idempotent; PROMOTES/DEMOTES NOTHING.
"$PYTHON" docs/apply_status_frontmatter.py

echo "--- Step 9c: Claims-doc status drift check (blocking gate: --strict) ---"
# Mirror of the closure-plan drift check (Step 3c), for the doc-status plane: flags docs
# whose status has fallen out of step with claims.yaml (hard frontmatter drift, plus soft
# review buckets for residual hand-line contradictions). Promoted to a blocking gate
# 2026-07-10 once the REVIEW backlog cleared (SHP-5): --strict exits 1 on HARD frontmatter
# drift only (frontmatter != claims.yaml-derived), which aborts the pipeline under
# `set -e`. The soft REVIEW/INFO buckets never fail --strict; they stay report-only in
# evidence/planning/claims_doc_drift.md.
"$PYTHON" scripts/claims_doc_drift.py --strict

echo "--- Step 10: Refreshing the goblin tale's campaign stanza (from closure snapshot) ---"
# Updates ONLY the CAMPAIGN_STATE marker block in docs/ree_for_my_parents.md
# (and the private canonical tale if present). Never writes an episode; never
# names the soul. Depends on the Step 3c-bis closure snapshot.
"$PYTHON" scripts/update_goblin_tale.py

echo ""
echo "Done. Check evidence/experiments/pending_review.md for experiments awaiting review."
echo "After editing claims.yaml, re-run step 4: python scripts/build_claims_json.py"
