# Pending Experiment Review

Generated: `2026-09-25T05:21:43Z`  
Last review: `2026-09-25T05:21:26Z`  
Scanned: 2991 claim_evidence entries considered (3015 already reviewed), 4887 manifest file(s) on disk.  
Pending: **1** item(s) -- 0 PASS, 1 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication; 1 evidence PASS/FAIL flagged degenerate (route to /failure-autopsy)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_1095_mech439_operator_on_conversion_falsifier_20260925T040330Z_v3` | 2026-09-25T04:03 | MECH-439 | — |

## Evidence PASS/FAIL flagged degenerate (route to /failure-autopsy)

These `experiment_purpose: "evidence"` results carry a manifest-level `non_degenerate: false` (or a `false` entry in `non_degenerate_per_claim`) -- the driver's own pre-registered non-degeneracy check on its load-bearing criterion failed. The indexer already excludes them from scoring (`scoring_excluded: "degenerate"`), but nothing else routes them for review: `_compute_adjudication` only fires for `experiment_purpose` in {diagnostic, baseline}, so an evidence-purpose degenerate PASS/FAIL sails into the plain PASS/FAIL table above with no flag (confirmed: V3-EXQ-1007). **Route to `/failure-autopsy` (it accepts a PASS target too); do not verify-and-close.**

| Run ID | Status | Claims | Degeneracy reason |
|--------|--------|--------|--------------------|
| `v3_exq_1095_mech439_operator_on_conversion_falsifier_20260925T040330Z_v3` | FAIL | MECH-439 | The conversion contrast was not validly evaluated: instrument_ok=True control_distinct=True noise_control_lifts=False an |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- ERROR manifests (crash-before-manifest / runner ERROR record): run `/diagnose-errors`, re-queue under a NEW letter, then add the manifest stem to `discussed_experiment_dirs`
- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).
- Diagnostic (`experiment_purpose: "diagnostic"`), no confirmed autopsy: ALL diagnostic PASS/FAIL results require a confirmed `/failure-autopsy` target before governance marks them reviewed -- not only ones the indexer flagged untrustworthy. Run `/failure-autopsy` (accepts a PASS target too), then mark reviewed once confirmed.
- Reviewed FAIL with no confirmed autopsy (blind-spot net): a claim-tagged, non-diagnostic FAIL that is already `reviewed` but was never autopsied. Run `/failure-autopsy` on it; the row clears automatically once a CONFIRMED autopsy target covers the run_id. Do NOT re-mark it reviewed to silence it (it is already reviewed -- that is the blind spot). Legacy such runs are grandfathered in `fail_autopsy_grandfather.json` and never listed; do not hand-edit that file.
- Recorded (non-gating) preconditions: nothing to clear. The run is reviewed and closed by the normal PASS/FAIL route above; the recorded finding is an audit trail to read alongside the result, not a flag to adjudicate.
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
