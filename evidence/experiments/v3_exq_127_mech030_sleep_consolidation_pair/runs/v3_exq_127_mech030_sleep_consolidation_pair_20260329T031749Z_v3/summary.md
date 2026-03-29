# V3-EXQ-127 -- MECH-030 Sleep Consolidation Discriminative Pair

**Status:** FAIL
**Claims:** MECH-030
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Conditions:** REPLAY_ON vs REPLAY_ABLATED
**Warmup:** 400 eps  **Eval:** 50 eps
**Env:** CausalGridWorldV2 size=6, 4 hazards, nav_bias=0.35
**n_replay_steps:** 10  **replay_batch:** 32

## Pre-Registered Thresholds

C1: gap_replay_on >= 0.04 in all seeds  (REPLAY_ON harm eval above floor)
C2: per-seed delta (ON - ABLATED) >= 0.02 in all seeds  (consolidation adds >= 2pp)
C3: gap_replay_ablated >= 0.0  (ablation learns something; data quality)
C4: n_harm_eval_min >= 20  (sufficient harm events in eval)
C5: no fatal errors

## Results

| Condition | gap (avg) | mean_harm | mean_safe |
|-----------|-----------|-----------|----------|
| REPLAY_ON      | 0.0014 | 0.5717 | 0.5703 |
| REPLAY_ABLATED | 0.0158 | 0.5165 | 0.5007 |

**delta_gap (REPLAY_ON - REPLAY_ABLATED): -0.0144**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: gap_on >= 0.04 (all seeds) | FAIL | 0.0014 |
| C2: per-seed delta >= 0.02 (all seeds) | FAIL | [-0.0178, -0.011] |
| C3: gap_ablated >= 0.0 | PASS | 0.0158 |
| C4: n_harm_min >= 20 | PASS | 547 |
| C5: no fatal errors | PASS | -- |

Criteria met: 3/5 -> **FAIL**

## Interpretation

MECH-030 V3 proxy NOT supported: gap_on=0.0014 (C1 FAIL), delta=-0.0144 (C2 FAIL). harm_eval_head does not demonstrate improvement from offline consolidation at this training scale.

## Per-Seed

REPLAY_ON:
  seed=42: gap=0.0016 n_harm=561
  seed=123: gap=0.0012 n_harm=556

REPLAY_ABLATED:
  seed=42: gap=0.0195 n_harm=547
  seed=123: gap=0.0121 n_harm=560

## Failure Notes

- C1 FAIL: REPLAY_ON gap below 0.04 in seeds [42, 123] -- harm_eval_head not learning meaningful representation even with consolidation
- C2 FAIL: per-seed deltas ['-0.0178', '-0.0110'] < 0.02 -- consolidation does not add >= 2pp over online-only training
