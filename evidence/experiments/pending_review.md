# Pending Experiment Review

Generated: `2026-08-09T05:55:14Z`  
Last review: `2026-08-09T05:32:14Z`  
Pending: **10** item(s) -- 2 PASS, 7 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 1 ERROR manifest(s); 1 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_899_arc030_mech307_g0_readiness_20260808T214833Z_v3` | 2026-08-08T21:48 | (no claim tags) | — |
| `v3_exq_903_mech075_ventral_vta_rpe_probe_20260808T222748Z_v3` | 2026-08-08T22:27 | MECH-075 | — |
| `v3_exq_603r_instrumental_avoidance_combined_fix_retest_20260808T230931Z_v3` | 2026-08-08T23:09 | MECH-357 | — |
| `v3_exq_905_mech075_dorsal_lc_arousal_probe_20260808T232406Z_v3` | 2026-08-08T23:24 | MECH-075 | — |
| `v3_exq_902_sd048_default_scale_calibration_sweep_20260809T002118Z_v3` | 2026-08-09T00:21 | SD-048 | — |
| `v3_exq_190a_mech022_hypothesis_injection_probe_wellpowered_20260809T002451Z_v3` | 2026-08-09T00:24 | MECH-022 | — |
| `v3_exq_228b_arc032_theta_bypass_onboarded_20260809T030541Z_v3` | 2026-08-09T03:05 | ARC-032 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_244b_mech165_replay_diversity_validation_v3` | 2026-08-09T00:20 | MECH-165 |
| `v3_exq_906_full_stack_observational_fishtank_20260809T003857Z_v3` | 2026-08-09T00:38 | (no claim tags) |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_906_full_stack_observational_fishtank_20260809T003857Z_v3` | PASS | full_stack_observational_showcase_live | **vacuous_pass** |

## Needs diagnosis (ERROR manifests -> /diagnose-errors)

These are durable ERROR-class result manifests on disk -- most commonly a runner-synthesized record for a crash-before-manifest (a script that exited non-zero before writing any manifest; incident V3-EXQ-654e). They are scoring-neutral (no claim tags) so they never weight claim confidence, but each is a real code crash that needs `/diagnose-errors` and a re-queue under a NEW letter. Mark discussed by adding the **manifest stem** (filename minus `.json`) to `discussed_experiment_dirs`.

| Outcome | Manifest stem | Queue ID | Machine | Summary |
|---------|---------------|----------|---------|---------|
| ERROR | `v3_v3_exq_821a_runner_error_20260808T111711Z_v3` | V3-EXQ-821a | ree-cloud-3 | Non-zero exit code 1; no runner sentinel (stdout-derived 'FAIL' not trusted on c |

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
