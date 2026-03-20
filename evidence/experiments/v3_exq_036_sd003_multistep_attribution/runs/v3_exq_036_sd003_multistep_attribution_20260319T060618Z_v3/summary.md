# V3-EXQ-036 — SD-003 Multi-Step Attribution (k=5) on CausalGridWorldV2

**Status:** FAIL
**Claims:** SD-003, ARC-024, MECH-071
**World:** CausalGridWorldV2 (proximity_scale=0.05)
**alpha_world:** 0.9  (SD-008)
**k_rollout:** 5
**Seed:** 0
**Predecessor:** EXQ-030b (4/5 FAIL — causal_sig_approach=0.003149 < 0.005)

## Root Cause Analysis and Fix

**EXQ-030b C3 FAIL — 1-step causal_sig too small:**
Single-step E2.world_forward produces nearly identical next-states for all actions.
Agent moves 1 cell/step in 12×12 grid → hazard_field_view changes ~1/12 of full range.
E3(E2(z, a_actual)) ≈ E3(E2(z, a_cf)) → causal_sig ≈ noise.

**Fix: k=5-step rollout with shared random tail:**
Only the first action (a_0) differs. Remaining k-1 actions are sampled identically
for actual and all counterfactuals. After 5 steps, different a_0 choices have
propagated their position difference through E2's world model, amplifying proximity gaps.

## Attribution Results (k=5-step)

| Transition Type | causal_sig | n |
|---|---|---|
| none (locomotion)    | -0.040958 | 76 |
| hazard_approach      | 0.003067 | 747 |
| env_caused_hazard    | 0.010359 | 20 |
| agent_caused_hazard  | 0.004424 | 41 |

- **world_forward R²**: 0.9472
- **attribution_gap** (approach − env): -0.007292

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: attribution_gap > 0 | FAIL | -0.007292 |
| C2: causal_sig_approach > causal_sig_none | PASS | 0.003067 vs -0.040958 |
| C3: causal_sig_approach > 0.01 (minimum k-step signal) | FAIL | 0.003067 |
| C4: world_forward_r2 > 0.05 | PASS | 0.9472 |
| C5: n_approach >= 50 | PASS | 747 |

Criteria met: 3/5 → **FAIL**

## Failure Notes

- C1 FAIL: attribution_gap=-0.007292 <= 0
- C3 FAIL: causal_sig_approach=0.003067 <= 0.01
