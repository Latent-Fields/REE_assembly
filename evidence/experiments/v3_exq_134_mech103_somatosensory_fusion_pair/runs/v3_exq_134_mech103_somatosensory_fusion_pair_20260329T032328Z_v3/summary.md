# V3-EXQ-134 -- MECH-103 Multimodal Exteroceptive Fusion (Somatosensory Channel)

**Status:** FAIL
**Claims:** MECH-103
**Proposal:** EXP-0030 / EVB-0022
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Conditions:** FUSION_ON vs FUSION_ABLATED
**Warmup:** 400 eps  **Eval:** 50 eps
**Env:** CausalGridWorldV2 size=6, 4 hazards, nav_bias=0.4
**Somatosensory channel:** SOMA_DIM=8 (contact-force + near-surface vibration; FUSION_ON informative; FUSION_ABLATED zeros)
**Replication of:** EXQ-128 (auditory channel) -- distinct second modality

## Pre-Registered Thresholds

C1: gap_fusion_on >= 0.04 in all seeds  (FUSION_ON harm eval above floor)
C2: per-seed delta (ON - ABLATED) >= 0.02 in all seeds  (soma modality adds >=2pp)
C3: gap_fusion_ablated >= 0.0  (ablation learns something; data quality)
C4: n_harm_eval_min >= 20  (sufficient harm events in eval)
C5: no fatal errors

## Results

| Condition | gap (avg) | mean_harm | mean_safe |
|-----------|-----------|-----------|----------|
| FUSION_ON      | 0.0218 | 0.5265 | 0.5047 |
| FUSION_ABLATED | 0.0218 | 0.5265 | 0.5047 |

**delta_gap (FUSION_ON - FUSION_ABLATED): +0.0001**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: gap_on >= 0.04 (all seeds) | FAIL | 0.0218 |
| C2: per-seed delta >= 0.02 (all seeds) | FAIL | [-0.0, 0.0001] |
| C3: gap_ablated >= 0.0 | PASS | 0.0218 |
| C4: n_harm_min >= 20 | PASS | 533 |
| C5: no fatal errors | PASS | -- |

Criteria met: 3/5 -> **FAIL**

## Interpretation

MECH-103 NOT supported (somatosensory channel): gap_on=0.0218 (C1 FAIL), delta=+0.0001 (C2 FAIL). Informative somatosensory channel does not produce a detectable improvement in z_world harm discrimination at this training scale.

## Per-Seed

FUSION_ON:
  seed=42: gap=0.0219 n_harm=580
  seed=123: gap=0.0217 n_harm=533

FUSION_ABLATED:
  seed=42: gap=0.0219 n_harm=580
  seed=123: gap=0.0216 n_harm=533

## Failure Notes

- C1 FAIL: FUSION_ON gap below 0.04 in seeds [42, 123] -- z_world does not encode harm even with somatosensory input
- C2 FAIL: per-seed deltas ['-0.0000', '0.0001'] < 0.02 -- somatosensory fusion does not add >=2pp over single-modality
