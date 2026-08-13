# Pending Experiment Review

Generated: `2026-08-13T06:09:54Z`  
Last review: `2026-08-12T18:24:49Z`  
Pending: **10** item(s) -- 0 PASS, 9 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 1 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_910a_mech489_defensive_orienting_decision_retest_20260810T213616Z_v3` | 2026-08-10T21:36 | MECH-489 | — |
| `v3_exq_914_mech236_hippocampal_zgoal_channel_ablation_20260811T065911Z_v3` | 2026-08-11T06:59 | MECH-236 | — |
| `v3_exq_603t_instrumental_avoidance_scheduled_external_hazard_20260811T173724Z_v3` | 2026-08-11T17:37 | MECH-357 | — |
| `v3_exq_919_mech321_harm_aware_selection_unconditional_wholeepisode_20260811T225107Z_v3` | 2026-08-11T22:51 | MECH-321 | — |
| `v3_exq_228d_arc032_theta_phase_weighted_readout_20260811T234236Z_v3` | 2026-08-11T23:42 | ARC-032 | — |
| `v3_exq_922_sd016_mech151_152_arc041_production_combo_20260812T035119Z_v3` | 2026-08-12T03:51 | ARC-041, MECH-150, MECH-151, MECH-152 | — |
| `v3_exq_436e_sd017_mech166_occupied_slot_retest_20260812T221724Z_v3` | 2026-08-12T22:17 | ARC-045, MECH-166, SD-017 | — |
| `v3_exq_467e_mech266_mode_stickiness_behavioural_20260813T001847Z_v3` | 2026-08-13T00:18 | MECH-266, SD-032a | — |
| `v3_exq_464e_mech266_competing_goals_behavioural_20260813T020141Z_v3` | 2026-08-13T02:01 | MECH-266, SD-032a | — |

## Needs diagnosis (ERROR manifests -> /diagnose-errors)

These are durable ERROR-class result manifests on disk -- most commonly a runner-synthesized record for a crash-before-manifest (a script that exited non-zero before writing any manifest; incident V3-EXQ-654e). They are scoring-neutral (no claim tags) so they never weight claim confidence, but each is a real code crash that needs `/diagnose-errors` and a re-queue under a NEW letter. Mark discussed by adding the **manifest stem** (filename minus `.json`) to `discussed_experiment_dirs`.

| Outcome | Manifest stem | Queue ID | Machine | Summary |
|---------|---------------|----------|---------|---------|
| ERROR | `v3_v3_exq_926_runner_error_20260813T045041Z_v3` | V3-EXQ-926 | ree-cloud-2 | Non-zero exit code 1; no runner sentinel (stdout-derived 'PASS' not trusted on c |

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
