# Pending Experiment Review

Generated: `2026-08-12T21:10:24Z`  
Last review: `2026-08-12T18:24:49Z`  
Pending: **7** item(s) -- 0 PASS, 6 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication; 1 reviewed FAIL(s) with no confirmed autopsy

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_910a_mech489_defensive_orienting_decision_retest_20260810T213616Z_v3` | 2026-08-10T21:36 | MECH-489 | — |
| `v3_exq_914_mech236_hippocampal_zgoal_channel_ablation_20260811T065911Z_v3` | 2026-08-11T06:59 | MECH-236 | — |
| `v3_exq_603t_instrumental_avoidance_scheduled_external_hazard_20260811T173724Z_v3` | 2026-08-11T17:37 | MECH-357 | — |
| `v3_exq_919_mech321_harm_aware_selection_unconditional_wholeepisode_20260811T225107Z_v3` | 2026-08-11T22:51 | MECH-321 | — |
| `v3_exq_228d_arc032_theta_phase_weighted_readout_20260811T234236Z_v3` | 2026-08-11T23:42 | ARC-032 | — |
| `v3_exq_922_sd016_mech151_152_arc041_production_combo_20260812T035119Z_v3` | 2026-08-12T03:51 | ARC-041, MECH-150, MECH-151, MECH-152 | — |

## Reviewed FAIL with no confirmed autopsy (blind-spot net)

These are claim-tagged, non-diagnostic, terminal **FAIL** runs that were marked reviewed in `review_tracker.json` but carry NO confirmed `/failure-autopsy` target. Being marked reviewed does NOT exempt a FAIL from autopsy. `load_pending_entries` drops every reviewed run_id, so without this net a claim-tagged FAIL can be marked reviewed with no diagnosis and vanish from every other section -- the ARC-017 V3-EXQ-129/135 pair sat in exactly this state for ~131 days (run 2026-03-29, first adjudicated 2026-08-07, caught only because a /thought-digestion deferral note named it by hand). Run `/failure-autopsy` on each run below (accepts the pair together); once a CONFIRMED autopsy target exists the row clears automatically on the next generate. Legacy runs already in this state when the net was installed are grandfathered in `fail_autopsy_grandfather.json` and are NOT listed here.

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_914_mech236_hippocampal_zgoal_channel_ablation_20260811T055126Z_v3` | 2026-08-11T05:51 | MECH-236 |

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
