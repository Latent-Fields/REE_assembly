# V3-EXQ-137 -- MECH-097 Peripersonal Space Commit Locus Discriminative Pair

**Status:** FAIL
**Claims:** MECH-097
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Conditions:** PPS_LOCUS_ON vs PPS_LOCUS_ABLATED
**Warmup:** 400 eps  **Eval:** 50 eps
**Env:** CausalGridWorldV2 size=6, 4 hazards, nav_bias=0.45

## Experimental Design

PPS_LOCUS_ON: harm_eval_head receives cat(z_world, pps_feature)
  pps_feature = max hazard_field intensity in central 3x3 of 5x5 view
PPS_LOCUS_ABLATED: harm_eval_head receives z_world only

## Pre-Registered Thresholds

C1: gap_locus_on >= 0.04 in all seeds  (PPS_LOCUS_ON harm eval above floor)
C2: per-seed delta (ON - ABLATED) >= 0.02 in all seeds  (PPS adds >=2pp)
C3: gap_ablated >= 0.0  (ablation learns something; data quality)
C4: n_harm_eval_min >= 20  (sufficient harm events in eval)
C5: n_approach_contacts_min >= 10  (manipulation check: proximity events fired)

## Results

| Condition | gap (avg) | mean_harm | mean_safe |
|-----------|-----------|-----------|----------|
| PPS_LOCUS_ON      | 0.0030 | 0.5401 | 0.5372 |
| PPS_LOCUS_ABLATED | 0.0079 | 0.5234 | 0.5155 |

**delta_gap (ON - ABLATED): -0.0050**
**n_approach_contacts (min across all cells): 535**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: gap_on >= 0.04 (all seeds) | FAIL | 0.0030 |
| C2: per-seed delta >= 0.02 (all seeds) | FAIL | [-0.0083, -0.0016] |
| C3: gap_ablated >= 0.0 | PASS | 0.0079 |
| C4: n_harm_min >= 20 | PASS | 535 |
| C5: n_approach_contacts_min >= 10 | PASS | 535 |

Criteria met: 3/5 -> **FAIL**

## Interpretation

MECH-097 V3 proxy NOT supported: gap_on=0.0030 (C1 FAIL), delta=-0.0050 (C2 FAIL). Peripersonal space proximity encoding does not demonstrate improvement in harm eval quality at this training scale.

## Per-Seed

PPS_LOCUS_ON:
  seed=42: gap=0.0038 n_harm=545 n_approach_contacts=545
  seed=123: gap=0.0021 n_harm=535 n_approach_contacts=535

PPS_LOCUS_ABLATED:
  seed=42: gap=0.0121 n_harm=545 n_approach_contacts=545
  seed=123: gap=0.0037 n_harm=535 n_approach_contacts=535

## Failure Notes

- C1 FAIL: PPS_LOCUS_ON gap below 0.04 in seeds [42, 123] -- harm_eval_head not learning harm representation even with PPS feature
- C2 FAIL: per-seed deltas ['-0.0083', '-0.0016'] < 0.02 -- PPS feature does not add >=2pp over ablated condition
