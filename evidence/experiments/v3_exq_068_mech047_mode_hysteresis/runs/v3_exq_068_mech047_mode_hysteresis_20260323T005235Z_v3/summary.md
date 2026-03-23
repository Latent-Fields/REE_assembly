# V3-EXQ-068 -- MECH-047: Mode Manager Hysteresis

**Status:** FAIL
**Claim:** MECH-047 -- commitment mode persists after incentive removal (mode hysteresis)
**Design:** Agent H (Phase A: high-hazard -> Phase B: low-hazard) vs Agent C (low-hazard only)
**alpha_world:** 0.9  |  **Phase A:** 200 eps  |  **Phase B:** 100 eps  |  **Seed:** 0

## Design Rationale

Memoryless commitment: as soon as hazards are reduced, commitment_rate should drop
immediately. Hysteresis predicts a decay lag. We measure this by counting steps until
a 20-step rolling commitment_rate window drops to the control baseline. If hysteresis
exists, this count exceeds 20.

## Results

| Metric | Value |
|--------|-------|
| Phase A commitment_rate | 0.999 |
| Phase A final running_variance | 0.000002 |
| Phase B final running_variance | 0.000001 |
| Agent H beta_gate_mean (eval) | 1.0000 |
| Agent C beta_gate_mean (eval) | 1.0000 |
| Agent H commit_rate (eval) | 1.000 |
| Agent C commit_rate (eval) | 1.000 |
| hysteresis_decay_steps | 20 |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: hysteresis_decay_steps > 20 | FAIL | 20 |
| C2: beta_post_commit > beta_control * 1.1 | FAIL | 1.0000 vs 1.1000 |
| C3: phase_a_commit_rate > 0.3 (commitment established) | PASS | 0.999 |
| C4: No fatal errors | PASS | 0 |

Criteria met: 2/4 -> **FAIL**

## Failure Notes

- C1 FAIL: hysteresis_decay_steps=20 <= 20
- C2 FAIL: beta_h_mean=1.0000 <= beta_c_mean*1.1=1.1000
