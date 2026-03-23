# V3-EXQ-077 -- ARC-024 Asymptotic Proxy Structure Discriminative Pair

**Status:** PASS
**Claims:** ARC-024
**Decision:** retain_ree
**Seeds:** [42, 7]
**alpha_world:** 0.9  (SD-008)
**Warmup:** 350 eps  **Eval:** 50 eps

## Pre-Registered Thresholds

C1: gap_approach_GRADIENT > 0.06
C2: gap_approach_CONTACT  < 0.02
C3: delta_approach_gap    > 0.04
C4: gap_contact_GRADIENT  > 0.04

## Results

| Condition | gap_approach | gap_contact | mean_none | mean_approach |
|-----------|-------------|-------------|-----------|---------------|
| GRADIENT     | 0.1968 | 0.1738 | 0.3817 | 0.5785 |
| CONTACT_ONLY | -0.0881 | -0.0292 | 0.5501 | 0.4619 |

**delta_approach_gap (GRADIENT - CONTACT_ONLY): +0.2850**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: gap_approach_GRADIENT > 0.06 | PASS | 0.1968 |
| C2: gap_approach_CONTACT < 0.02  | PASS | -0.0881 |
| C3: delta_approach_gap > 0.04    | PASS | 0.2850 |
| C4: gap_contact_GRADIENT > 0.04  | PASS | 0.1738 |

Criteria met: 4/4 -> **PASS**

## Interpretation

ARC-024 SUPPORTED: gradient harm signals before contact enable E3 to learn asymptotic proxy detection. GRADIENT condition shows approach gap 0.1968 vs CONTACT_ONLY -0.0881. z_world encodes the harm gradient; contact-only training does not produce approach sensitivity. Harm signals have asymptotic proxy structure in world latent space as claimed.

## Per-Seed

GRADIENT:
  seed=42: gap_approach=0.2010 gap_contact=0.1889 n_approach=858 train_approach=5523
  seed=7: gap_approach=0.1927 gap_contact=0.1587 n_approach=830 train_approach=5689

CONTACT_ONLY:
  seed=42: gap_approach=-0.0782 gap_contact=-0.0133 n_approach=1758
  seed=7: gap_approach=-0.0981 gap_contact=-0.0450 n_approach=1673

