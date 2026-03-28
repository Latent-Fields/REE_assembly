# V3-EXQ-107 -- ARC-024 Gradient vs Flat Proxy Structure

**Status:** FAIL
**Claims:** ARC-024
**Seeds:** [0, 1, 2, 3, 4]
**Warmup:** 200 eps  **Eval:** 50 eps  **Steps/ep:** 60

## Design

Two conditions matched on seeds:
  GRADIENT: use_proxy_fields=True -- body_obs=12, world_obs=250,
            includes hazard_field_view and resource_field_view.
  FLAT:     use_proxy_fields=False -- body_obs=10, world_obs=200,
            binary contact harm only, no proximity gradient.

## Pre-Registered Thresholds

C1 (pre-contact gradient): gap_approach_none >= 0.08 (GRADIENT)
C2 (AUC quality):          harm_eval_auc >= 0.6 (GRADIENT)
C3 (discriminative):       GRADIENT_auc > FLAT_auc + 0.05 (supporting)
PASS: C1 AND C2

## Results

| Metric | GRADIENT | FLAT |
|--------|----------|------|
| gap_approach_none (mean +/- sem) | 0.0030 +/- 0.0011 | N/A |
| harm_eval_auc (mean +/- sem)     | 0.6477 +/- 0.0138 | 0.5010 +/- 0.0086 |

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: gap >= 0.08            | FAIL | 0.0030 |
| C2: AUC >= 0.6            | PASS | 0.6477 |
| C3: disc >= 0.05 (support) | PASS | 0.1467 |

**PASS = C1 AND C2 -> FAIL**

## Event Counts (total across seeds)

GRADIENT: approach=1298 contact=195 none=843
FLAT:     contact=451

## Interpretation

ARC-024 NOT SUPPORTED: z_world fails to encode pre-contact gradient. gap_approach_none=0.0030 < 0.08. Gradient fields in obs do not propagate into z_world latent structure at current training scale (200 episodes).

## Failure Notes

- C1 FAIL: gradient gap_approach_none=0.0030 < 0.08 -- z_world does not encode pre-contact gradient structure
