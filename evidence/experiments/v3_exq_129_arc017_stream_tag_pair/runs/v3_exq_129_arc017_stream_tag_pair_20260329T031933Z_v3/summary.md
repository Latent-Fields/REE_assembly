# V3-EXQ-129 -- ARC-017 Sensory Stream Tag Discriminative Pair

**Status:** FAIL
**Claims:** ARC-017
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Conditions:** TYPED_TAGS_ON vs TYPED_TAGS_ABLATED
**Warmup:** 400 eps  **Eval:** 50 eps
**Env:** CausalGridWorldV2 size=6, 4 hazards, nav_bias=0.4

## Design

TYPED_TAGS_ON: world_obs -> z_world encoder exclusively;
harm_obs routed to z_harm encoder (ARC-017 typed separation).
TYPED_TAGS_ABLATED: cat(world_obs, harm_obs) -> single z_world encoder;
no typed routing -- harm channel information merged into world encoder input.

## Pre-Registered Thresholds

C1: gap_typed >= 0.04 in all seeds  (TYPED_TAGS_ON harm eval above floor)
C2: per-seed delta (TYPED - ABLATED) >= 0.02 in all seeds  (typed routing adds >=2pp)
C3: gap_ablated >= 0.0  (ablation learns something; data quality)
C4: n_harm_eval_min >= 20  (sufficient harm events in eval)
C5: no fatal errors

## Results

| Condition | gap (avg) | mean_harm | mean_safe |
|-----------|-----------|-----------|----------|
| TYPED_TAGS_ON      | 0.0153 | 0.5218 | 0.5065 |
| TYPED_TAGS_ABLATED | 0.0257 | 0.5256 | 0.4999 |

**delta_gap (TYPED - ABLATED): -0.0104**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: gap_typed >= 0.04 (all seeds) | FAIL | 0.0153 |
| C2: per-seed delta >= 0.02 (all seeds) | FAIL | [-0.0098, -0.011] |
| C3: gap_ablated >= 0.0 | PASS | 0.0257 |
| C4: n_harm_min >= 20 | PASS | 533 |
| C5: no fatal errors | PASS | -- |

Criteria met: 3/5 -> **FAIL**

## Interpretation

ARC-017 NOT supported at V3 proxy level: gap_typed=0.0153 (C1 FAIL), delta=-0.0104 (C2 FAIL). Typed stream separation does not produce a detectable improvement in harm_eval discrimination at this training scale. Note: this V3 proxy conflates the typed-routing mechanism with the underlying quality of z_world -- a FAIL here may reflect insufficient warmup rather than a genuine claim refutation.

## Per-Seed

TYPED_TAGS_ON:
  seed=42: gap=0.0138 n_harm=580 world_obs_dim=250
  seed=123: gap=0.0168 n_harm=533 world_obs_dim=250

TYPED_TAGS_ABLATED:
  seed=42: gap=0.0236 n_harm=580 world_obs_dim=301
  seed=123: gap=0.0278 n_harm=533 world_obs_dim=301

## Failure Notes

- C1 FAIL: TYPED_TAGS_ON gap below 0.04 in seeds [42, 123] -- typed routing does not produce a discriminative z_world
- C2 FAIL: per-seed deltas [-0.0098, -0.011] < 0.02 -- typed stream separation does not add >=2pp over merged input
