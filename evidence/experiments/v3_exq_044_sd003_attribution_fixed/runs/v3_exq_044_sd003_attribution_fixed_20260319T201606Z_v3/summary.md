# V3-EXQ-044 — SD-003 Trajectory Attribution (Fixed Sequential Training)

**Status:** FAIL
**Claims:** SD-003, MECH-102
**World:** CausalGridWorldV2 (body=12, world=250)
**alpha_world:** 0.9 (SD-008)  |  **Seed:** 0
**Predecessors:** EXQ-041 PASS (ThetaBuffer), EXQ-042 PASS (terrain training)
**Fixes:** EXQ-043 FAIL (E3 calibration collapse from simultaneous training)

## Design: Sequential Training Phases

**EXQ-043 failure mechanism:** Terrain_prior training shifts data distribution seen by
E3.harm_eval — agent navigates toward objectives through hazard gradients, making
approach states dominate harm_buf_pos. E3 collapses to uniform-high output.

**Fix:** Three sequential phases with no cross-contamination:

| Phase | Episodes | What trains | Policy |
|---|---|---|---|
| P1: Terrain | 400 | terrain_prior + E2.world_forward + E1 | E3-guided |
| P2: E3 calib | 200 | E3.harm_eval only | Random (balanced) |
| P3: Eval | 100 | Frozen | E3-guided |

## Terrain Training (Phase 1)

| Phase | terrain_loss |
|---|---|
| Initial (first 100 eps) | 0.2236 |
| Final (last 100 eps) | 0.0000 |

## Attribution Results (Phase 3)

| Transition Type | causal_sig | n |
|---|---|---|
| none | 0.0000 | 19559 |
| approach | 0.0000 | 424 |
| contact | 0.0000 | 17 |

approach − none gap: -0.0000
contact − approach gap: -0.0000

## E3 Calibration (Phase 3)

| Type | mean harm_eval |
|---|---|
| none | 0.5003 |
| approach | 0.5002 |
calibration_gap_approach: -0.0001

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: causal_sig_approach > causal_sig_none | FAIL | 0.0000 vs 0.0000 |
| C2: causal_sig_contact > causal_sig_approach (MECH-102) | FAIL | 0.0000 vs 0.0000 |
| C3: causal_sig_approach > 0.001 | FAIL | 0.0000 |
| C4: cal_gap_approach > 0.03 (E3 calibrated) | FAIL | -0.0001 |
| C5: n_approach_eval >= 30 | PASS | 424 |
| C6: mean_harm_eval_none < 0.1 (calibration gate) | FAIL | 0.5003 |

Criteria met: 1/6 → **FAIL**

## Failure Notes

- C6 FAIL (calibration gate): mean_harm_eval_none=0.5003 >= 0.1. E3 collapsed again — trajectory attribution results are INVALID. Check Phase 2 calibration balance.
- C1 FAIL: causal_sig_approach=0.0000 <= causal_sig_none=0.0000
- C2 FAIL: causal_sig_contact=0.0000 <= causal_sig_approach=0.0000 (MECH-102 escalation absent)
- C3 FAIL: causal_sig_approach=0.0000 <= 0.001 (trajectory scores don't diverge near hazards)
- C4 FAIL: cal_gap_approach=-0.0001 <= 0.03 (E3 not calibrated)
