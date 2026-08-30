# Pending Experiment Review

Generated: `2026-08-30T07:12:26Z`  
Last review: `2026-08-29T16:16:28Z`  
Pending: **7** item(s) -- 2 PASS, 5 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication; 2 diagnostic run(s) with no confirmed autopsy; 1 run(s) with a DEAD z_goal stream

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_961_mech144_ventral_valence_spatial_gradient_probe_20260829T160046Z_v3` | 2026-08-29T16:00 | MECH-144 | — |
| `v3_exq_960_mech143_dca1_value_free_map_probe_20260829T162515Z_v3` | 2026-08-29T16:25 | MECH-143 | — |
| `v3_exq_642a_blocked_agency_zblock_discriminative_20260829T185417Z_v3` | 2026-08-29T18:54 | (no claim tags) | — |
| `v3_exq_964_mech482_epistemic_deficit_validation_20260829T215030Z_v3` | 2026-08-29T21:50 | MECH-482 | — |
| `v3_exq_963_mech063ii_tonic_phasic_dissociation_retest_20260830T023012Z_v3` | 2026-08-30T02:30 | MECH-063, SD-069 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_936a_mech439_f_variance_share_rollout_clamp_fix_20260829T071510Z_v3` | 2026-08-29T07:15 | MECH-439 |
| `v3_exq_962_mech219_sd019b_behavioural_temporal_controllability_20260829T185419Z_v3` | 2026-08-29T18:54 | MECH-219, SD-019b |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_642a_blocked_agency_zblock_discriminative_20260829T185417Z_v3` | FAIL | z_block_integrator_no_rise |
| `v3_exq_964_mech482_epistemic_deficit_validation_20260829T215030Z_v3` | FAIL | accumulator_live_but_never_changes_committed_action |

## Dead z_goal stream (interpret before trusting a z_goal readout)

**This is a record, not a gate.** No claim status, confidence or `v3_pending` changes on account of it, and the runs below are scored exactly as they would be otherwise. It is here so the condition is seen at review time instead of only by whoever opens the raw manifest.

Each run below reports `z_goal_stream.writer_defect: true`: the agent was stepped, but `REEAgent.update_z_goal` -- the **sole** z_goal writer in the substrate -- was never called. z_goal therefore sat at zero-init for the whole run, `GoalState.is_active()` returned False throughout, and every consumer received `current_z_goal=None` on every tick: the E3 goal term, MECH-293 ghost probes, MECH-288's slow BOCPD scale, MECH-189 super-ordinal anchors, the SD-057 incentive bank, the MECH-295 liking->approach bridge and the frontopolar counterfactual read all silently no-opped. Nothing raises. The usual cause is a driver that hand-rolls its inner loop and omits the call (V3-EXQ-626, whose five criteria were all keyed on a z_goal that never left zero; V3-EXQ-830, caught only because its readiness gate happened to name an ad-hoc `zgoal_present_frac`).

**A result that does not read z_goal is unaffected** -- V3-EXQ-816's harness carries no defect for its own question. Judge each run by whether its criteria depend on a live z_goal; if they do, the run measured something other than what it claimed to.

**`active_frac` is NOT the signal and must not be read as one.** A zero fraction is legitimate and common -- a goal-OFF parity arm, a negative control (V3-EXQ-626b's ARM_NO_BENEFIT), and a correctly-wired run whose `GoalState` benefit gate never opened because the agent met no resource all read 0.0 correctly. `writer_calls == 0` is what separates the defect from those, and it is the only thing flagged here. A run with **no** `z_goal_stream` block is UNMEASURED, not zero, and never appears below -- which is almost the whole historical corpus (the runtime backstop landed in ree-v3 `d6d1da96d9`, 2026-07-27). Full interpretation rules: ree-v3 `experiments/_lib/z_goal_stream.py`.

| Run ID | Status | Ticks | writer_calls | active_frac | GoalState |
|--------|--------|-------|--------------|-------------|-----------|
| `v3_exq_642a_blocked_agency_zblock_discriminative_20260829T185417Z_v3` | FAIL | 14400 | **0** | 1.000 | live |

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
