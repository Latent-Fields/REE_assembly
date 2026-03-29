# V3-EXQ-131 -- ARC-023 Multi-Rate Heartbeat Discriminative Pair

**Status:** FAIL
**Claims:** ARC-023
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Conditions:** MULTIRATE_ON vs MULTIRATE_ABLATED
**Warmup:** 400 eps  **Eval:** 50 eps
**E3 heartbeat rate:** every 5 steps (MULTIRATE_ON only)
**Env:** CausalGridWorldV2 size=6, 4 hazards, nav_bias=0.4

## Design

ARC-023 asserts three BG-like loops operate at characteristic thalamic heartbeat rates.
Functional restatement: E3 (deliberation loop) operates at a slower rate than E1/E2.

MULTIRATE_ON: E3 harm_eval trains/evaluates on averaged z_world over 5-step chunks.
E1 and E2 update every step as usual.
E3 heartbeat fires every 5 steps (time-multiplexed SD-006 phase 1 proxy).

MULTIRATE_ABLATED: E3 harm_eval trains/evaluates per step.
All loops update at the same rate -- no rate separation.

## Pre-Registered Thresholds

C1: gap_on >= 0.04 in all seeds  (MULTIRATE_ON harm eval above floor)
C2: per-seed delta (ON - ABLATED) >= 0.02 in all seeds  (rate separation adds >=2pp)
C3: gap_ablated >= 0.0  (ablation learns something; data quality)
C4: n_harm_eval_min >= 20  (sufficient harm events in eval)
C5: no fatal errors

## Results

| Condition | gap (avg) | mean_harm | mean_safe | var_harm_eval |
|-----------|-----------|-----------|-----------|---------------|
| MULTIRATE_ON      | -0.0000 | 0.4999 | 0.5000 | 0.000000 |
| MULTIRATE_ABLATED | 0.0153 | 0.5218 | 0.5065 | 0.002760 |

**delta_gap (ON - ABLATED): -0.0153**

Diagnostic: var_harm_eval -- lower variance in MULTIRATE_ON indicates more stable
E3 heartbeat integration (less per-step noise).
  MULTIRATE_ON: 0.000000  |  MULTIRATE_ABLATED: 0.002760

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: gap_on >= 0.04 (all seeds) | FAIL | -0.0000 |
| C2: per-seed delta >= 0.02 (all seeds) | FAIL | [-0.0139, -0.0168] |
| C3: gap_ablated >= 0.0 | PASS | 0.0153 |
| C4: n_harm_min >= 20 | PASS | 103 |
| C5: no fatal errors | PASS | -- |

Criteria met: 3/5 -> **FAIL**

## Interpretation

ARC-023 NOT supported at V3 proxy level: gap_on=-0.0000 (C1 FAIL), delta=-0.0153 (C2 FAIL). Rate-separated E3 does not produce a detectable improvement in harm_eval discrimination at this training scale. The synchronous time-multiplexed proxy may not capture the full benefit of async rate separation (SD-006 phase 2 required). Note: the chunk-averaging approach used here (mean z_world over K steps) is a conservative proxy -- the benefit of heartbeat synchronization may require the full async E3 implementation to manifest clearly.

## Per-Seed

MULTIRATE_ON:
  seed=42: gap=-0.0001 n_harm=109 var_harm_eval=0.000000
  seed=123: gap=0.0000 n_harm=103 var_harm_eval=0.000000

MULTIRATE_ABLATED:
  seed=42: gap=0.0138 n_harm=580 var_harm_eval=0.001202
  seed=123: gap=0.0168 n_harm=533 var_harm_eval=0.004317

## Failure Notes

- C1 FAIL: MULTIRATE_ON gap below 0.04 in seeds [42, 123] -- rate-separated E3 does not produce a discriminative harm signal
- C2 FAIL: per-seed deltas [-0.0139, -0.0168] < 0.02 -- rate separation does not add >=2pp over same-rate E3
