#!/usr/bin/env bash
# governance.sh — full REE_assembly governance pipeline
#
# Usage (from REE_assembly root):
#   bash scripts/governance.sh        # V3: build indexes, review list, rebuild site data
#   bash scripts/governance.sh --v2   # V2: also sync from ../ree-v2/ first
#
# Steps:
#   0-pre. Open a TASK_CLAIMS entry covering evidence/ for the run's duration, so
#          the runner heartbeat's `git pull --rebase --autostash` cannot stash the
#          half-written derived-artifact set. Released by an exit trap on every
#          path (success, failure, Ctrl-C). See the block above Step 0-pre.
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

# ---------------------------------------------------------------------------
# Autostash guard: hold a TASK_CLAIMS entry for the duration of the regen.
#
# THE HAZARD. A full regen rewrites ~1050-1190 derived files (per-experiment
# INDEX.md, claim_evidence.v1.json, the evidence/planning/ registries, the docs
# stubs) over several minutes. The runner heartbeat
# (ree-v3/runner_remote_control.py:push_heartbeat) does
# `git pull --rebase --autostash` against REE_assembly every minute. Land one of
# those mid-regen and the ENTIRE half-written set is stashed, with no error
# reaching the running pipeline -- it just carries on writing into a tree that
# was swept out from under it.
#
# Not hypothetical: five such stash entries were sitting in the REE_assembly
# stash list on 2026-07-28, dated 07-22, 07-26 (x2) and 07-27 (x2), of 1063 /
# 1120 / 1130 / 1186 / 1186 files (triage:
# evidence/planning/ree_assembly_orphaned_autostash_triage.md). All seven
# entries there were harmless ONLY because this pipeline is idempotent -- rerun
# it and the artifacts come back. It turns harmful the moment a regen is
# committed *from* such a stash, or a half-written set is popped over a good one.
#
# THE FIX. runner_remote_control._active_claim_on_evidence_dir() already skips
# the heartbeat push entirely whenever an active TASK_CLAIMS.json claim names a
# resource under `evidence/` or `docs/claims/`. Nothing about a governance run
# opened such a claim, so the one existing mitigation was never engaged. This
# opens one for the run's duration.
#
# WHY THE RESOURCE STRINGS BELOW MATCH. The REE_assembly guard runs
# _active_claim_on_paths(..., ("evidence/", "docs/claims/")) with anchored=False
# -- a plain SUBSTRING test (`p in res`) against each active claim's `resources`,
# with no age bound. `REE_assembly/evidence/` therefore matches on `evidence/`.
# One matching resource is enough (the skip is all-or-nothing for the whole
# push); docs/ and contributors/ are listed because the regen genuinely writes
# them, not because the match needs them.
#
# WHY task_claim.py RATHER THAN A HAND-EDIT. It appends the entry and commits it
# in the SAME step, so the claim never sits dirty in a shared working tree for
# the next session's whole-file read-modify-write to sweep (CLAUDE.md
# "Read-modify-write contamination"). No --push: the heartbeat reads the local
# working-tree TASK_CLAIMS.json, so the claim only has to exist here to be
# honoured, and pushing mid-regen would add a network failure mode for nothing.
#
# WHY THE TRAP. The REE_assembly guard has NO max_age_hours, so a leftover
# `active` entry gates the heartbeat push indefinitely. A crashed or
# Ctrl-C'd regen must therefore still release it -- hence EXIT (covers `set -e`
# aborts, the Step 4b/9c blocking gates, and any explicit exit) plus INT and
# TERM, which re-raise so the caller still sees the right 128+N status. A
# SIGKILL or a power cut is the residual hole: the entry is left `active` under
# an obviously-machine session_id (`governance-sh-<host>`) so a human reading
# TASK_CLAIMS.json can recognise and clear it, and CLAUDE.md's 6-hour staleness
# rule applies to it like any other claim.
# ---------------------------------------------------------------------------
GOV_CLAIM_HOST="$(hostname -s 2>/dev/null || echo unknown-host)"
GOV_CLAIM_SESSION_ID="governance-sh-${GOV_CLAIM_HOST}"
# Resolved ONCE, here, rather than at each call site: the helpers below run from
# an exit trap, and a `cd` anywhere in the pipeline body would otherwise silently
# re-resolve `..` to the wrong directory and skip the release.
GOV_UMBRELLA="$(cd .. && pwd)"
GOV_CLAIM_PY="$GOV_UMBRELLA/scripts/task_claim.py"
GOV_CLAIM_HELD=0

gov_claim_open() {
  if [ ! -f "$GOV_CLAIM_PY" ]; then
    # Not under the REE_Working umbrella (hub / cloud worker / standalone
    # checkout). Those have no TASK_CLAIMS.json, so the heartbeat guard is
    # inert there anyway -- warn and carry on rather than blocking a regen.
    echo "  (no $GOV_CLAIM_PY -- running WITHOUT an autostash claim guard)" >&2
    return 0
  fi
  # HELD is armed BEFORE the call, not after it. task_claim.py writes the entry
  # to disk and only then commits it, so a Ctrl-C landing inside that window
  # leaves an `active` entry on disk -- already gating the heartbeat -- while
  # `open` exits non-zero. Arming afterwards left exactly that entry orphaned
  # (observed while testing this guard: SIGINT during the open's git commit ->
  # claim active, uncommitted, never closed). Arm first; the close is guarded on
  # what is actually on disk, so an open that wrote nothing still closes nothing.
  GOV_CLAIM_HELD=1
  if "$PYTHON" "$GOV_CLAIM_PY" open \
        --session-id "$GOV_CLAIM_SESSION_ID" \
        --session-label "governance.sh regen (automated)" \
        --task "Governance pipeline regen: rewrites the derived evidence/docs artifact set; holds this claim so the runner heartbeat autostash cannot stash a half-written regen." \
        --resources \
          REE_assembly/evidence/ \
          REE_assembly/docs/ \
          REE_assembly/contributors/; then
    :
  else
    # Fail OPEN, matching the guard's own posture: an unclaimable regen is
    # still a regen worth running, just an unprotected one.
    echo "WARNING: could not open the TASK_CLAIMS autostash guard -- continuing" >&2
    echo "         UNPROTECTED. A heartbeat pull may stash this regen mid-write." >&2
  fi
}

# True when an `active` entry for this session_id is on disk RIGHT NOW. The
# close is guarded on this rather than on the in-memory flag alone, so it
# releases an entry written by an interrupted `open`, and skips cleanly when
# the open wrote nothing at all.
gov_claim_is_active() {
  "$PYTHON" - "$GOV_UMBRELLA/TASK_CLAIMS.json" "$GOV_CLAIM_SESSION_ID" <<'PYEOF'
import json, sys
try:
    claims = json.load(open(sys.argv[1]))["claims"]
except Exception:
    sys.exit(1)
sys.exit(0 if any(c.get("session_id") == sys.argv[2]
                  and c.get("status") == "active" for c in claims) else 1)
PYEOF
}

gov_claim_close() {
  local rc="${1:-0}" note
  [ "$GOV_CLAIM_HELD" = "1" ] || return 0
  GOV_CLAIM_HELD=0   # re-entrancy guard: EXIT still fires after INT/TERM
  [ -f "$GOV_CLAIM_PY" ] || return 0
  gov_claim_is_active || return 0
  if [ "$rc" = "0" ]; then
    note="governance.sh regen completed (exit 0) on ${GOV_CLAIM_HOST}. Lock claim only"
  else
    note="governance.sh regen ABORTED (exit ${rc}) on ${GOV_CLAIM_HOST}; claim released by the exit trap. Lock claim only"
  fi
  note="${note}; the pipeline is derive-only and commits nothing -- derived artifacts are left in the working tree for review."
  # --closed-at, not --not-landed: this entry is a LOCK held for the regen
  # window, not a unit of work, and there is no landing commit for it to carry
  # the committer date of. Stamping every routine regen "NOT LANDED:" would
  # burn the signal that flags genuinely unlanded work.
  "$PYTHON" "$GOV_CLAIM_PY" close \
      --session-id "$GOV_CLAIM_SESSION_ID" \
      --closed-at "$(date -u +"%Y-%m-%dT%H:%M:%SZ")" \
      --completion-note "$note" \
    || echo "WARNING: failed to close TASK_CLAIMS claim $GOV_CLAIM_SESSION_ID -- clear it by hand (it gates the runner heartbeat push)." >&2
}

gov_on_exit() {
  local rc=$?
  gov_claim_close "$rc"
  # Explicit: an `exit` inside an EXIT trap sets the final status and does not
  # re-enter the trap, so the caller still sees the pipeline's own status
  # rather than the claim helper's.
  exit "$rc"
}

gov_on_signal() {
  local sig="$1"
  gov_claim_close "$((128 + $2))"
  trap - "$sig" EXIT
  kill -"$sig" $$      # re-raise under the default handler: correct 128+N status
}

trap gov_on_exit EXIT
trap 'gov_on_signal INT 2' INT
trap 'gov_on_signal TERM 15' TERM

echo "=== REE Governance Pipeline ==="

echo "--- Step 0-pre: Opening TASK_CLAIMS autostash guard ---"
gov_claim_open

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

echo "--- Step 3c-quinquies: Plan Status-table vs frontmatter sync (warn-only) ---"
# Flags a plan whose markdown "Status table" row disagrees with its own YAML
# frontmatter node: missing/orphan row, status mismatch, or a row 'Last updated'
# OLDER than the node's. The drift is one-directional by construction -- THIS
# step (and every other governance step) writes governance_<date> keys into the
# node record and bumps last_updated, and nothing obliges anyone to touch the
# parallel markdown table, which is nonetheless what each plan labels "the resume
# primitive" and what a cold-start session reads first. Measured 2026-07-29: six
# plans described completed work as outstanding, node record current in all six.
# Reconcile the ROW, never the node. Warn-only (--exit-nonzero to gate).
"$PYTHON" scripts/check_plan_status_table_sync.py --quiet-notes || true

echo "--- Step 3c-sexies: Manifest degeneracy annotation vs its own arm data (warn-only) ---"
# Cross-checks each manifest's arm-degeneracy ANNOTATION against the per-seed arm
# DATA in the SAME file -- the one thing no other check does, because every other
# consumer trusts the annotation. Two directions: arms bit-identical on every
# comparable metric yet unflagged (the confirmed 2026-07-30 V3-EXQ-673 MECH-171
# incident, eabe9c453b: three manifests asserted in prose that their arms differed
# while per_seed_comparisons showed ARM_A==ARM_B==ARM_C on every metric for every
# seed -- introduced 2026-07-20, survived ten days, caught only because a human
# read the note beside the numbers); and non_degenerate:false set on an
# arm-identity justification the data contradicts, which de-weights real evidence.
# Scoring-harmless in that instance only because `degenerate` and
# `non_contributory` are both scoring_excluded -- the same error on a scored
# direction mints a scored entry out of a vacuous run. Detection only: a finding
# needs a /failure-autopsy adjudication of WHY the arms collapsed, never a
# mass-set of the flag. Warn-only (--exit-nonzero to gate).
"$PYTHON" scripts/check_manifest_degeneracy_consistency.py --quiet-notes || true

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

# GOV-CAT-1 -- the DATA-QUALITY sibling of the three recurrence scans above.
# Those three ask what a set of verdicts MEANS; this one asks whether the verdict
# was RECORDED at all. Both the re-derive brake rule R3 and GOV-CEIL-1's ceiling
# overlay key on targets[].recommended_epistemic_category and silently SKIP a
# target where it is absent or null -- so an autopsy that genuinely reached a
# ceiling reading but never stamped the field is uncounted by the very machinery
# built to act on it, with nothing anywhere reporting the omission. Confirmed
# 2026-07-20: 27/336 confirmed targets (12 claim-tagged) across 11 files had no
# category, the two most recent 3 and 1 days old -- ongoing, not historical.
# Backfilling from each companion .md moved seven claims' ceiling counts; none
# crossed N=3, but that was luck. The settled convention is that the ARTIFACTS
# are the source of truth and the fix direction is the artifact -- do NOT widen
# R3 or GOV-CEIL-1 to tolerate a missing field. Read-only; --strict for a
# blocking CI gate.
"$PYTHON" scripts/check_epistemic_category_completeness.py || true

echo "--- Step 3h: Unapplied confirmed-autopsy recommendations (GOV-APPLY-1, warn-only) ---"
# The FIFTH sibling, and the one that closes the already-reviewed blind spot. The
# other four ask what a set of verdicts MEANS (3e/3f/3g) or whether the verdict was
# RECORDED (GOV-CAT-1); this asks whether it was ever APPLIED.
#
# THE GAP: /governance discovers autopsy recommendations by walking pending_review.md
# and looking up a confirmed failure_autopsy_*.json per surfaced run_id (SKILL.md Step
# 2 item 5). A run already in review_tracker.json:reviewed_run_ids is ABSENT from
# pending_review.md, so that lookup never runs. The cycle assumes adjudication precedes
# review -- false for every RE-adjudication, and a corpus sweep re-opens reviewed runs
# BY CONSTRUCTION. Confirmed 2026-07-20: failure_autopsy_V3-EXQ-604c's demotion of
# MECH-314b/314c/Q-044 was confirmed, landed, and invisible; it survived THREE routing
# attempts before being caught by hand. An unapplied demotion does not stay neutral --
# it decays into a positive claim (IGW-20260720-020 went on asserting the withdrawn
# reading). Diagnosis: intra_run_substrate_divergence_sweep_2026-07-20.md sec 10.
#
# Keys on per_claim_recommendation[].change (machine-readable "a change is owed") and
# reports its own coverage, rather than inferring change-owed from a category compare
# -- that alternative was measured at 338 mismatches, overwhelmingly NOT defects (an
# affirming autopsy legitimately recommends a category the claim layer never mirrors).
# Read-only; promotes/demotes nothing. --strict for a blocking CI gate.
"$PYTHON" scripts/check_unapplied_autopsy_recommendations.py || true

echo "--- Step 3i: Dry-run adjudication leak (GOV-DRY-1, warn-only) ---"
# The SIXTH sibling, and the only one that asks whether a verdict rests on evidence
# that DOES NOT EXIST. The others ask what a set of verdicts MEANS (3e/3f/3g),
# whether it was RECORDED (GOV-CAT-1), or whether it was APPLIED (3h).
#
# THE GAP: a `--dry-run` smoke is a truncated budget emitted to prove a driver runs;
# its metrics are truncation artifacts. The SCORING path has been gated since
# cb7298c1c4 (converter + indexer + pending-review buckets). Nothing gated the
# ADJUDICATION path -- a /failure-autopsy or /governance session could read a dry
# manifest and reason over its metrics as evidence, and did: confirmed twice, in
# OPPOSITE directions, six hours apart on 2026-05-19 for V3-EXQ-543i, where the
# correct 01:13Z "vacuous truncation artifact" diagnosis was overwritten at 07:06Z
# by a basin-nondeterminism narrative built entirely on the smoke, over a real-run
# set with ZERO variance -- which then propagated into substrate_queue.json as an
# acceptance bar any future ARC-062 fix must clear. Diagnosis:
# evidence/planning/dry_run_smoke_in_autopsy_audit_2026-07-28.md; corpus sweep:
# evidence/planning/dry_run_stamped_manifest_sweep_2026-07-28.md.
#
# check_dry_run_citations.py made the check AVAILABLE and the two skills REQUIRE it,
# but that is skill prose -- it holds only while every session remembers. The audit's
# own closing finding is that this defect was caught and patched per-instance at
# least FOUR times without the pipeline being fixed: a correct local diagnosis does
# not survive on its own, only a gate does.
#
# Sweeps confirmed failure_autopsy_*.json + substrate_queue.json for dry-run
# citations, and reports dry manifests carrying an ASSERTING stamp (a direction, a
# directional per-claim entry, or any epistemic_category). Quarantine stamps
# (superseded / non_contributory) are the CORRECT response to a smoke and are never
# reported -- flagging them would fire on 19 of 36 dry run_ids forever while telling
# governance to undo the right thing. Reuses check_dry_run_citations.build_index()
# rather than re-implementing detection. Excludes what the 2026-07-28 audit + sweep
# already adjudicated (still printed, never hidden); future adjudications use the
# in-band, hit-scoped `dry_run_citation_metabolized` marker. Read-only; every write
# it recommends is governance's. --strict for a blocking CI gate.
"$PYTHON" scripts/check_dry_run_adjudication_leak.py || true

echo "--- Step 3j: Skill-improvement recurrence audit (GOV-SKILL-1, warn-only) ---"
# The SEVENTH sibling, and the first that audits the SKILLS themselves rather
# than the claims registry. The others ask what a set of verdicts MEANS
# (3e/3f/3g), whether the verdict was RECORDED (GOV-CAT-1), whether it was
# APPLIED (3h), or whether it rests on evidence that DOES NOT EXIST (GOV-DRY-1).
# This one asks whether a non-outcome LESSON (a reusable code bug, a
# methodology caveat, a schema-legibility gap -- roughly half of every
# autopsy's `learning_extracted[]`, per the 2026-08-01 scoping session) keeps
# recurring across independent autopsies/review cycles without ever being
# folded into a skill checklist. Standing counterpart to the same session's
# two REACTIVE, single-incident additions (`/queue-experiment` Step 3.5,
# `/governance` Step 2b) -- see
# evidence/planning/skill_improvement_audit_scoping_2026-08-01.md.
#
# Self-flagged-repeat keyword/regex detection over `learning_extracted[]` +
# review_tracker.json prose (recurring/twice/same signature/PROCESS
# recurrence/third instance/etc), clustered by a cheap token-overlap
# heuristic, threshold-gated (>=2 independent files, OR a single entry citing
# >=2 distinct run ids, OR a strong self-flag phrase -- see the module
# docstring "design decisions" for the full calibration). NEVER auto-edits a
# SKILL.md -- read-only over the corpus, its only writes are its own pointer
# state (incremental-scan bookkeeping) and an optional markdown proposal a
# human reviews. Pointer-based incremental (only re-parses autopsy files whose
# mtime changed since the last sweep) with cross-run accumulation, so
# threshold counting stays correct across separate invocations. Read-only;
# promotes/demotes nothing; --strict for a blocking CI gate.
"$PYTHON" scripts/check_skill_improvement_recurrence.py || true

echo "--- Step 3k: Substrate-path overlap audit (GOV-SUBPATH-1, warn-only) ---"
# The EIGHTH standing scan, and the backward half of the /queue-experiment Step 2.5c consumer
# gate. Step 2.5c stops a NEW experiment from being queued against a severity: corrupting
# substrate_queue entry's substrate_paths; this scan is the mirror -- it finds evidence that
# ALREADY ran against substrate a later autopsy proved corrupts results, even when that
# evidence belongs to a claim the original autopsy never mentioned (unblocks_claims is
# claim-scoped, not code-scoped, so nothing else would ever surface this).
#
# THE GAP: every existing forward gate (/queue-experiment Step 2.5/2.5b, GOV-CEIL-1/GOV-DIAG-1)
# is keyed to the CURRENT experiment's OWN target claim/SD. None of them ask whether a driver
# script imports a code path some OTHER, unrelated claim's autopsy already flagged as broken.
# Design: evidence/planning/substrate_defect_gate_plan_2026-08-07.md.
#
# For every still-open severity: corrupting substrate_queue entry, lists completed runs (via
# the flat + runs/ manifest index, not just the originating claim's own results) whose driver
# script (ree-v3/experiments/<experiment_type>.py) imports one of the entry's substrate_paths
# and completed AFTER the entry's added_utc. Read-only; never edits a manifest or
# substrate_queue.json. Warn-only, always exits 0 unless --strict -- a human decides whether to
# re-review; this only surfaces the candidates.
"$PYTHON" scripts/check_substrate_path_overlap.py || true

echo "--- Step 3l: Citation staleness scan (GFLAG-0010, warn-only) ---"
# Confirmed incident: SD-087/SD-020/SD-086 cited config.py:2306,
# agent.py:8636-8642, and e3_selector.py:1038/:2766 in claims.yaml -- all
# drifted 190-1150 lines from the real locations, found only because a
# session happened to manually diff cited line numbers against ree-v3 HEAD
# during an unrelated review (GFLAG-0010, resolved 2026-08-08). Scans every
# string in every claim for file.py:LINE citations and flags one whose line
# number now exceeds the cited file's current length at HEAD, or whose file
# is no longer tracked in any known repo. Content drift (in-bounds but now
# pointing at the wrong thing) is out of scope by design -- this only checks
# what is mechanically checkable without understanding the cited code.
# Warn-only, always exits 0 unless --exit-nonzero -- a human decides whether
# a flagged citation needs fixing; this only surfaces the candidates.
"$PYTHON" scripts/check_citation_staleness.py || true

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

echo "--- Step 8a: Rebuilding public Development Map projection ---"
# Reader-facing projection over the generated live-front, progress, claim, and
# archive records. Derive-only; it does not alter a claim, a status, or a plan.
"$PYTHON" scripts/build_development_map.py

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
