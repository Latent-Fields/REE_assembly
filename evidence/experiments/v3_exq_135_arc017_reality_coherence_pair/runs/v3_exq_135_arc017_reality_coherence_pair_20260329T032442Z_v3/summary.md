# V3-EXQ-135 -- ARC-017 Reality-Coherence Lane Discriminative Pair

**Status:** FAIL
**Claims:** ARC-017
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Conditions:** REALITY_COHERENCE_ON vs REALITY_COHERENCE_ABLATED
**Warmup:** 400 eps  **Eval:** 50 eps
**Env:** CausalGridWorldV2 size=6, 4 hazards, nav_bias=0.4

## Design

REALITY_COHERENCE_ON: world encoder trains only on REAL env observations;
the reality-coherence provenance constraint is preserved.
REALITY_COHERENCE_ABLATED: world encoder also trains on noise-perturbed
replay of past world_obs (imagined inputs, noise_std=0.1);
provenance constraint is violated (real and imagined treated equivalently).
Evaluation uses ONLY real env observations in both conditions.

Complementary to V3-EXQ-129 (stream-type routing facet of ARC-017).
This experiment tests the reality-coherence facet of ARC-017.

## Pre-Registered Thresholds

C1: gap_on >= 0.04 in all seeds  (REALITY_COHERENCE_ON above floor)
C2: per-seed delta (ON - ABLATED) >= 0.02 in all seeds  (reality grounding adds >=2pp)
C3: gap_ablated >= 0.0  (ablation learns something; data quality)
C4: n_harm_eval_min >= 20  (sufficient harm events in eval)
C5: n_replay_contam_min >= 50  (manipulation check: ablation received imagined inputs)

## Results

| Condition | gap (avg) | mean_harm | mean_safe |
|-----------|-----------|-----------|----------|
| REALITY_COHERENCE_ON      | 0.0153 | 0.5218 | 0.5065 |
| REALITY_COHERENCE_ABLATED | 0.0151 | 0.5286 | 0.5135 |

**delta_gap (ON - ABLATED): +0.0002**
**n_replay_contamination_min (ablated): 30176**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: gap_on >= 0.04 (all seeds) | FAIL | 0.0153 |
| C2: per-seed delta >= 0.02 (all seeds) | FAIL | [-0.0021, 0.0026] |
| C3: gap_ablated >= 0.0 | PASS | 0.0151 |
| C4: n_harm_min >= 20 | PASS | 533 |
| C5: n_replay_contam_min >= 50 | PASS | 30176 |

Criteria met: 3/5 -> **FAIL**

## Interpretation

ARC-017 reality-coherence lane NOT supported at V3 proxy level: gap_on=0.0153 (C1 FAIL), delta=+0.0002 (C2 FAIL). Grounding the encoder to real observations only does not produce a detectable improvement in harm_eval discrimination vs replay-contaminated encoder at this training scale. Note: this is a V3 proxy -- the full ARC-017 reality-coherence mechanism requires hippocampal trace provenance tracking which is only partially approximated by this noise-perturbation proxy.

## Per-Seed

REALITY_COHERENCE_ON:
  seed=42: gap=0.0138 n_harm=580
  seed=123: gap=0.0168 n_harm=533

REALITY_COHERENCE_ABLATED:
  seed=42: gap=0.0159 n_harm=557 n_replay_contam=30176
  seed=123: gap=0.0143 n_harm=544 n_replay_contam=30452

## Failure Notes

- C1 FAIL: REALITY_COHERENCE_ON gap below 0.04 in seeds [42, 123] -- reality-grounded encoder does not produce discriminative z_world
- C2 FAIL: per-seed deltas [-0.0021, 0.0026] < 0.02 -- reality-coherence constraint does not add >=2pp over replay-contaminated encoder
