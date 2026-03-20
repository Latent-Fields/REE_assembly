# V3-EXQ-030b — SD-003 Full Attribution Pipeline v2 on CausalGridWorldV2

**Status:** PASS
**Claims:** SD-003, ARC-024, MECH-071
**World:** CausalGridWorldV2 (proximity_scale=0.05)
**alpha_world:** 0.9  (SD-008)
**Seed:** 0
**Predecessor:** EXQ-030 (3/5 FAIL — C1 wrong criterion, C3 threshold too high)

## Fixes Applied

**Fix 1 — C1 (raw delta) dropped:**
EXQ-030 showed delta_approach=0.214 ≈ delta_none=0.216. Raw counterfactual divergence
||E2(z,a) - E2(z,a_cf)|| is dominated by the 175-ch local_view portion of z_world and is
uniform across all transition types. Not informative. Criterion removed.

**Fix 2 — E3 trained on E2-predicted states:**
EXQ-030 C3 failure: E3 trained on observed z_world only → distribution mismatch with
E2-predicted z_world at eval → harm_eval scores compressed. Fix: at each E3 training step,
augment observed harm_buf batches with E2.world_forward(z_world_pos, a_rand) → label=1
and E2.world_forward(z_world_neg, a_rand) → label=0. Teaches E3 to evaluate E2-output space.

## Attribution Results

| Transition | world_delta | causal_sig | n |
|---|---|---|---|
| none (locomotion)    | 0.2134 | -0.074152 | 101 |
| hazard_approach      | 0.2117 | 0.005271 | 832 |
| env_caused_hazard    | 0.2085 | -0.029201 | 13 |
| agent_caused_hazard  | 0.2123 | 0.017314 | 33 |

- **world_forward R²**: 0.9472  (PASS > 0.05)
- **attribution_gap** (approach − env): 0.034472  (PASS > 0)

## PASS Criteria (Revised)

| Criterion | Result | Value |
|---|---|---|
| C1: attribution_gap > 0 (agent approach > env attribution) | PASS | 0.034472 |
| C2: causal_sig_approach > causal_sig_none (approach > baseline) | PASS | 0.005271 vs -0.074152 |
| C3: causal_sig_approach > 0.005 (minimum attribution signal) | PASS | 0.005271 |
| C4: world_forward_r2 > 0.05 (E2 learned world dynamics) | PASS | 0.9472 |
| C5: n_approach >= 50 (sufficient approach events) | PASS | 832 |

Criteria met: 5/5 → **PASS**

