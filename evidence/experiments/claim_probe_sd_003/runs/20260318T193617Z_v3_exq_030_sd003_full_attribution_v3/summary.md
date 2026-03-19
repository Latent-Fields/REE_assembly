# V3-EXQ-030 — SD-003 Full Attribution on CausalGridWorldV2

**Status:** FAIL
**Claims:** SD-003, ARC-024, MECH-071
**World:** CausalGridWorldV2 (proximity_scale=0.05)
**alpha_world:** 0.9  (SD-008)
**Seed:** 0

## What This Tests

The complete SD-003 attribution pipeline on a gradient world:
  z_world_actual = E2.world_forward(z_world, a_actual)
  z_world_cf     = E2.world_forward(z_world, a_cf)
  causal_sig     = E3(z_world_actual) - E3(z_world_cf)

Does E2 predict action-conditional futures near hazards? Does the causal
signature distinguish agent-caused approach from environment-caused hazard?

EXQ-029 confirmed E3 detects gradients. This tests whether E2 models them.

## Attribution Results

| Transition | world_delta | causal_sig | n |
|---|---|---|---|
| none (locomotion)    | 0.2162 | -0.0726 | 101 |
| hazard_approach      | 0.2139 | 0.0055 | 832 |
| env_caused_hazard    | 0.2111 | -0.0158 | 13 |
| agent_caused_hazard  | 0.2136 | 0.0069 | 33 |

- **world_forward R²**: 0.9495  (PASS > 0.05)
- **attribution_gap** (approach - env): 0.0213  (PASS > 0)

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: delta_approach > delta_none (action-conditional near hazard) | FAIL | 0.2139 vs 0.2162 |
| C2: attribution_gap > 0 (agent > env attribution) | PASS | 0.0213 |
| C3: causal_sig_approach > 0.02 (positive attribution signal) | FAIL | 0.0055 |
| C4: world_forward_r2 > 0.05 (E2 learned world dynamics) | PASS | 0.9495 |
| C5: n_approach >= 50 | PASS | 832 |

Criteria met: 3/5 → **FAIL**

## Failure Notes

- C1 FAIL: delta_approach(0.2139) <= delta_none(0.2162)
- C3 FAIL: causal_sig_approach=0.0055 <= 0.02
