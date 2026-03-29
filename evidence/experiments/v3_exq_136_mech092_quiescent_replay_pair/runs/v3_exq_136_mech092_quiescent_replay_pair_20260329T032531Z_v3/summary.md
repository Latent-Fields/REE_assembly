# V3-EXQ-136 -- MECH-092 Quiescent Replay Discriminative Pair

**Status:** FAIL
**Claims:** MECH-092
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Conditions:** QUIESCENT_REPLAY_ON vs QUIESCENT_REPLAY_ABLATED
**Warmup:** 400 eps  **Eval:** 50 eps
**Env:** CausalGridWorldV2 size=6, 4 hazards, nav_bias=0.40
**quiescence_k:** 10 (consecutive non-harm steps to trigger replay)
**n_replay_steps:** 8  **replay_batch:** 16

## Pre-Registered Thresholds

C1: gap_replay_on >= 0.04 in all seeds  (QUIESCENT_REPLAY_ON harm eval above floor)
C2: per-seed delta (ON - ABLATED) >= 0.02 in all seeds  (quiescent consolidation adds >=2pp)
C3: gap_ablated >= 0.0  (ablation learns something; data quality)
C4: n_harm_eval_min >= 20  (sufficient harm events in eval)
C5: n_quiescent_triggers_min >= 15  (manipulation check: quiescent windows fire)

## Results

| Condition | gap (avg) | mean_harm | mean_safe |
|-----------|-----------|-----------|----------|
| QUIESCENT_REPLAY_ON      | 0.0185 | 0.5256 | 0.5071 |
| QUIESCENT_REPLAY_ABLATED | 0.0153 | 0.5218 | 0.5065 |

**delta_gap (ON - ABLATED): +0.0032**
**n_quiescent_triggers (ON, min across seeds): 6**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: gap_on >= 0.04 (all seeds) | FAIL | 0.0185 |
| C2: per-seed delta >= 0.02 (all seeds) | FAIL | [-0.0027, 0.0092] |
| C3: gap_ablated >= 0.0 | PASS | 0.0153 |
| C4: n_harm_min >= 20 | PASS | 533 |
| C5: n_quiescent_triggers_min >= 15 | FAIL | 6 |

Criteria met: 2/5 -> **FAIL**

## Interpretation

C5 FAIL: quiescent replay triggered only 6 times (threshold=15). With nav_bias=0.40 the agent frequently approaches hazards, reducing quiescent window duration. The quiescent mechanism may need higher nav_bias or lower quiescence_k to accumulate enough idle windows. Harm_eval gap (C1 {'PASS' if c1_pass else 'FAIL'}).

## Per-Seed

QUIESCENT_REPLAY_ON:
  seed=42: gap=0.0110 n_harm=549 n_quiescent_triggers=6
  seed=123: gap=0.0260 n_harm=556 n_quiescent_triggers=10

QUIESCENT_REPLAY_ABLATED:
  seed=42: gap=0.0138 n_harm=580
  seed=123: gap=0.0168 n_harm=533

## Failure Notes

- C1 FAIL: QUIESCENT_REPLAY_ON gap below 0.04 in seeds [42, 123] -- harm_eval_head not learning meaningful representation even with quiescent replay
- C2 FAIL: per-seed deltas ['-0.0027', '0.0092'] < 0.02 -- quiescent consolidation does not add >=2pp over online-only training
- C5 FAIL: n_quiescent_triggers_min=6 < 15 -- quiescent replay fired too rarely (manipulation check fail); consider reducing quiescence_k (currently 10)
