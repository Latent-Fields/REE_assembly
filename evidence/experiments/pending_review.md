# Pending Experiment Review

Generated: `2026-08-25T18:02:47Z`  
Last review: `2026-08-22T13:23:53Z`  
Pending: **8** item(s) -- 5 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 1 ERROR manifest(s); 2 diagnostic self-route(s) flagged for adjudication; 4 diagnostic run(s) with no confirmed autopsy; 4 run(s) with a DEAD z_goal stream

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_861g_inv050_mech180_h3_substrate_pin_f810969_20260822T175951Z_v3` | 2026-08-22T17:59 | INV-050, MECH-180 | — |
| `v3_exq_861h_inv050_mech180_contextmemory_write_lock_control_20260822T222844Z_v3` | 2026-08-22T22:28 | INV-050, MECH-180 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_910b_mech489_orienting_decision_at_override_tick_retest_20260822T235826Z_v3` | 2026-08-22T23:58 | MECH-489 |
| `v3_exq_946_contextmemory_write_address_informativeness_diagnostic_20260823T075019Z_v3` | 2026-08-23T07:50 | (no claim tags) |
| `v3_exq_861f_inv050_mech180_h1_measurement_rng_isolation_20260823T210058Z_v3` | 2026-08-23T21:00 | INV-050, MECH-180 |
| `v3_exq_861f_inv050_mech180_h1_measurement_rng_isolation_20260824T023853Z_v3` | 2026-08-24T02:38 | INV-050, MECH-180 |
| `v3_exq_948_observation_interface_re_representation_probe_20260825T142115Z_v3` | 2026-08-25T14:21 | (no claim tags) |

## Diagnostic adjudication required (self-route unverified)

These diagnostic/baseline runs carry a self-routed `interpretation.label`, but the indexer flagged it as untrustworthy: `precondition_unmet` (a declared precondition's `met` is false -- the self-route's premise did not hold) or `vacuous_pass` (an overall PASS rests on a degenerate criterion). The label must NOT drive a governance action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / close-or-route a thought-intake) until adjudicated -- run `/failure-autopsy` on the run (it accepts a flagged PASS target too). See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.

| Run ID | Status | Self-route label | Adjudication |
|--------|--------|------------------|--------------|
| `v3_exq_946_contextmemory_write_address_informativeness_diagnostic_20260823T075019Z_v3` | PASS | context_informative_address_found_at_operating_point | **vacuous_pass** |
| `v3_exq_948_observation_interface_re_representation_probe_20260825T142115Z_v3` | PASS | observation_interface_confirmed_re_representation_lifts_competence | **vacuous_pass** |

## Diagnostic -- autopsy required (no confirmed adjudication)

Every `experiment_purpose: "diagnostic"` result (PASS or FAIL) needs a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before governance marks it reviewed or applies anything from it -- not only the ones the indexer flagged untrustworthy above. A diagnostic's self-routed reading is a hypothesis about what it found, not a verdict; only the autopsy's four-layer diagnosis confirms it. This list is broader than 'Diagnostic adjudication required' above: it fires on `experiment_purpose` alone, regardless of `adjudication` flag or whether the result visibly routes a decision.

| Run ID | Status | Self-route label |
|--------|--------|-------------------|
| `v3_exq_946_contextmemory_write_address_informativeness_diagnostic_20260823T075019Z_v3` | PASS | context_informative_address_found_at_operating_point |
| `v3_exq_861f_inv050_mech180_h1_measurement_rng_isolation_20260823T210058Z_v3` | PASS | third_drive_independent_seed_replication_confirmed |
| `v3_exq_861f_inv050_mech180_h1_measurement_rng_isolation_20260824T023853Z_v3` | PASS | third_drive_independent_seed_replication_confirmed |
| `v3_exq_948_observation_interface_re_representation_probe_20260825T142115Z_v3` | PASS | observation_interface_confirmed_re_representation_lifts_competence |

## Dead z_goal stream (interpret before trusting a z_goal readout)

**This is a record, not a gate.** No claim status, confidence or `v3_pending` changes on account of it, and the runs below are scored exactly as they would be otherwise. It is here so the condition is seen at review time instead of only by whoever opens the raw manifest.

Each run below reports `z_goal_stream.writer_defect: true`: the agent was stepped, but `REEAgent.update_z_goal` -- the **sole** z_goal writer in the substrate -- was never called. z_goal therefore sat at zero-init for the whole run, `GoalState.is_active()` returned False throughout, and every consumer received `current_z_goal=None` on every tick: the E3 goal term, MECH-293 ghost probes, MECH-288's slow BOCPD scale, MECH-189 super-ordinal anchors, the SD-057 incentive bank, the MECH-295 liking->approach bridge and the frontopolar counterfactual read all silently no-opped. Nothing raises. The usual cause is a driver that hand-rolls its inner loop and omits the call (V3-EXQ-626, whose five criteria were all keyed on a z_goal that never left zero; V3-EXQ-830, caught only because its readiness gate happened to name an ad-hoc `zgoal_present_frac`).

**A result that does not read z_goal is unaffected** -- V3-EXQ-816's harness carries no defect for its own question. Judge each run by whether its criteria depend on a live z_goal; if they do, the run measured something other than what it claimed to.

**`active_frac` is NOT the signal and must not be read as one.** A zero fraction is legitimate and common -- a goal-OFF parity arm, a negative control (V3-EXQ-626b's ARM_NO_BENEFIT), and a correctly-wired run whose `GoalState` benefit gate never opened because the agent met no resource all read 0.0 correctly. `writer_calls == 0` is what separates the defect from those, and it is the only thing flagged here. A run with **no** `z_goal_stream` block is UNMEASURED, not zero, and never appears below -- which is almost the whole historical corpus (the runtime backstop landed in ree-v3 `d6d1da96d9`, 2026-07-27). Full interpretation rules: ree-v3 `experiments/_lib/z_goal_stream.py`.

| Run ID | Status | Ticks | writer_calls | active_frac | GoalState |
|--------|--------|-------|--------------|-------------|-----------|
| `v3_exq_861g_inv050_mech180_h3_substrate_pin_f810969_20260822T175951Z_v3` | FAIL | 84915 | **0** | 0.000 | live |
| `v3_exq_861h_inv050_mech180_contextmemory_write_lock_control_20260822T222844Z_v3` | FAIL | 53795 | **0** | 0.000 | live |
| `v3_exq_861f_inv050_mech180_h1_measurement_rng_isolation_20260823T210058Z_v3` | PASS | 54229 | **0** | 0.000 | live |
| `v3_exq_861f_inv050_mech180_h1_measurement_rng_isolation_20260824T023853Z_v3` | PASS | 54229 | **0** | 0.000 | live |

## Needs diagnosis (ERROR manifests -> /diagnose-errors)

These are durable ERROR-class result manifests on disk -- most commonly a runner-synthesized record for a crash-before-manifest (a script that exited non-zero before writing any manifest; incident V3-EXQ-654e). They are scoring-neutral (no claim tags) so they never weight claim confidence, but each is a real code crash that needs `/diagnose-errors` and a re-queue under a NEW letter. Mark discussed by adding the **manifest stem** (filename minus `.json`) to `discussed_experiment_dirs`.

| Outcome | Manifest stem | Queue ID | Machine | Summary |
|---------|---------------|----------|---------|---------|
| ERROR | `v3_v3_exq_944a_runner_error_20260822T151058Z_v3` | V3-EXQ-944a | ree-cloud-3 | Non-zero exit code 1; no runner sentinel (stdout-derived 'PASS' not trusted on c |

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
