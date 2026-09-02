# Pending Experiment Review

Generated: `2026-09-02T12:48:23Z`  
Last review: `2026-09-02T12:48:15Z`  
Pending: **5** item(s) -- 1 PASS, 3 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 1 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication; 1 diagnostic run(s) with no confirmed autopsy

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_395_mech220_harm_hub_dry_20260413T074905Z` | 20260413T074928Z | MECH-220 | — |
| `v3_exq_395_mech220_harm_hub_dry_20260413T075033Z` | 20260413T075102Z | MECH-220 | — |
| `v3_exq_395_mech220_harm_hub_dry_20260413T075133Z` | 20260413T075203Z | MECH-220 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_472_sd011_platform_stability_pilot_20260421T183651Z_v3` | 2026-04-21T18:36 | SD-011 |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_472_sd011_platform_stability_pilot_20260421T183651Z_v3` | PASS | — |

## Unclaimed manifests (PASS/FAIL with no claim tags)

These manifests are on disk with PASS/FAIL but their run_id is absent from `claim_evidence.v1.json`. Common causes: substrate-readiness or environment-probe diagnostics that intentionally tag no claims, or runs the runner mis-logged as ERROR/UNKNOWN while the manifest landed cleanly. Mark discussed by adding the **manifest stem** (filename minus `.json`) to `discussed_experiment_dirs` -- queue_id-level marking is unsafe here, see header docstring.

| Result | Manifest stem | Experiment type | Queue ID | Direction |
|--------|---------------|-----------------|----------|-----------|
| PASS | `v3_exq_976_sd_e1_item2_rollout_consistency_validation_20260902T114700Z_v3` | v3_exq_976_sd_e1_item2_rollout_consistency_validation | V3-EXQ-976 | non_contributory |

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
