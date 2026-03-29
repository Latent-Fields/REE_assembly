# V3-EXQ-130 -- MECH-096 Dual-Stream Observation Routing Discriminative Pair

**Status:** FAIL
**Claims:** MECH-096
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Conditions:** THREE_STREAM_ON vs THREE_STREAM_ABLATED
**Warmup:** 400 eps  **Eval:** 50 eps
**Env:** CausalGridWorldV2 size=6, 4 hazards, nav_bias=0.4

## Design

THREE_STREAM_ON: dedicated encoder heads per stream;
body_obs -> z_self (dorsal-equivalent),
world_obs -> z_world (ventral-equivalent),
harm_obs routed via SD-010 harm encoder (lateral-equivalent).

THREE_STREAM_ABLATED: all streams merged before encoding;
cat(world_obs, harm_obs, body_obs) -> single z_merged encoder;
no dedicated stream routing -- encoder must discover structure unsupervised.

## Pre-Registered Thresholds

C1: gap_on >= 0.04 in all seeds  (THREE_STREAM_ON harm eval above floor)
C2: per-seed delta (ON - ABLATED) >= 0.02 in all seeds  (stream routing adds >=2pp)
C3: gap_ablated >= 0.0  (ablation learns something; data quality)
C4: n_harm_eval_min >= 20  (sufficient harm events in eval)
C5: no fatal errors

## Results

| Condition | gap (avg) | mean_harm | mean_safe | cosine_sim |
|-----------|-----------|-----------|-----------|------------|
| THREE_STREAM_ON      | 0.0153 | 0.5218 | 0.5065 | -0.0743 |
| THREE_STREAM_ABLATED | 0.0194 | 0.5217 | 0.5023 | -0.2223 |

**delta_gap (ON - ABLATED): -0.0041**

Diagnostic: cosine_sim(z_self, z_world) -- lower = cleaner stream separation
  THREE_STREAM_ON: -0.0743  |  THREE_STREAM_ABLATED: -0.2223

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: gap_on >= 0.04 (all seeds) | FAIL | 0.0153 |
| C2: per-seed delta >= 0.02 (all seeds) | FAIL | [-0.0013, -0.0069] |
| C3: gap_ablated >= 0.0 | PASS | 0.0194 |
| C4: n_harm_min >= 20 | PASS | 533 |
| C5: no fatal errors | PASS | -- |

Criteria met: 3/5 -> **FAIL**

## Interpretation

MECH-096 NOT supported at V3 proxy level: gap_on=0.0153 (C1 FAIL), delta=-0.0041 (C2 FAIL). Dedicated stream routing does not produce a detectable improvement in harm_eval discrimination at this training scale. Note: this V3 proxy conflates the stream-routing mechanism with the underlying quality of z_world -- a FAIL here may reflect insufficient warmup rather than a genuine claim refutation. The merged encoder baseline may also be too powerful at this model scale (world_dim=32): the advantage of dedicated heads may only emerge at larger capacity.

## Per-Seed

THREE_STREAM_ON:
  seed=42: gap=0.0138 n_harm=580 cosine_sim=-0.0503
  seed=123: gap=0.0168 n_harm=533 cosine_sim=-0.0983

THREE_STREAM_ABLATED:
  seed=42: gap=0.0151 n_harm=580 cosine_sim=-0.1250
  seed=123: gap=0.0237 n_harm=533 cosine_sim=-0.3197

## Failure Notes

- C1 FAIL: THREE_STREAM_ON gap below 0.04 in seeds [42, 123] -- dedicated routing does not produce a discriminative harm signal
- C2 FAIL: per-seed deltas [-0.0013, -0.0069] < 0.02 -- dedicated stream routing does not add >=2pp over merged input
