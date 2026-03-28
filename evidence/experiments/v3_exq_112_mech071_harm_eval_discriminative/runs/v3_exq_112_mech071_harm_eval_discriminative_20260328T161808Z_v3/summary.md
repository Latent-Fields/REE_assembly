# V3-EXQ-112 -- MECH-071 harm_eval Trained vs Random Discriminative Pair

**Status:** FAIL
**Claims:** MECH-071
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Grid:** 6x6, 4 hazards, use_proxy_fields=True (ARC-024)
**Train:** 200 eps  **Eval:** 60 eps  **nav_bias:** 0.4

## Pre-Registered Thresholds

C1: calib_gap_trained >= 0.08
C2: calib_gap_random  <= 0.04
C3: delta_calibration_gap >= 0.05
C4: harm_eval_contact > harm_eval_approach > harm_eval_none (trained)
C5: n_approach >= 10 AND n_agent_hazard >= 5

## Results

| Head | calib_gap (agent-none) | harm_pred_std |
|------|------------------------|---------------|
| TRAINED | 0.0091 | 0.0352 |
| RANDOM  | 0.0000 | 0.0004 |

**delta_calibration_gap: +0.0091**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: calib_gap_trained >= 0.08 | FAIL | 0.0091 |
| C2: calib_gap_random <= 0.04  | PASS | 0.0000 |
| C3: delta >= 0.05             | FAIL | 0.0091 |
| C4: graded model (contact > approach > none) | FAIL | False |
| C5: n_approach>=10, n_agent>=5 | PASS | approach=573, agent=16 |

seeds passed: 0/2  criteria met: 2/5  -> **FAIL**

## Interpretation

MECH-071 NOT SUPPORTED: Trained head calibration_gap=0.0091 fails to meet threshold. Either z_world does not encode sufficient proximity structure for E3 to learn harm gradients, or the training procedure is insufficient. Consider whether ARC-024 proxy fields are providing the expected gradient structure.

## Per-Seed

  seed=42: calib_trained=-0.0036 calib_random=-0.0000 delta=-0.0036 graded=False n_approach=587 n_agent=16
  seed=123: calib_trained=0.0219 calib_random=0.0000 delta=0.0218 graded=False n_approach=573 n_agent=20

## Failure Notes

- C1 FAIL: calib_gap_trained=0.0091 < 0.08 (trained head cannot detect harm gradient -- MECH-071 not supported)
- C3 FAIL: delta=0.0091 < 0.05 (training adds marginal signal above random baseline)
- C4 FAIL: graded model not monotonic (contact > approach > none) in all seeds -- harm gradient not graded in z_world
