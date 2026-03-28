# V3-EXQ-117 -- ARC-024 Harm-Benefit Opposing Gradient Discriminative Pair

**Status:** FAIL
**Claims:** ARC-024
**Proposal:** EXP-0014 / EVB-0011
**Seeds:** [42, 123]
**Warmup:** 400 eps  **Eval:** 40 eps  **Steps/ep:** 200

## Design

Discriminative pair testing BOTH harm and benefit gradient arms of ARC-024:
  GRADIENT_PAIR: use_proxy_fields=True -- hazard_field_view + resource_field_view.
                  E3.harm_eval trained on harm events. Benefit probe (linear on z_world) trained on benefit events.
  FLAT_CONTROL:  use_proxy_fields=False -- binary contact signals only.
                  No approach events; no proximity gradient.

Background: EXQ-107 (5 seeds, 200 warmup) FAIL on C1 (gap_harm=0.003 vs 0.08).
  This experiment uses 400 warmup, 2 matched seeds, reduced C1/C2 threshold (0.04),
  and adds benefit gradient (C2) and opposing cosine test (C3).

## Pre-Registered Thresholds

C1 (harm gradient): gap_harm_approach_none >= 0.04 GRADIENT, both seeds
C2 (benefit gradient): gap_benefit_approach_none >= 0.04 GRADIENT, both seeds
C3 (opposing cosine, supporting): cos_sim(harm_dir, benefit_dir) <= -0.1 >= 1 seed
C4 (data quality): n_harm_approach >= 20 AND n_benefit_approach >= 20 per seed
PASS: C1_both AND C2_both AND C4

## Results Summary

| Metric | GRADIENT_PAIR | FLAT_CONTROL |
|--------|--------------|-------------|
| gap_harm_approach_none (mean) | 0.0120 | nan |
| gap_benefit_approach_none (mean) | nan | nan |
| cosine_sim(harm_dir, benefit_dir) (mean) | nan | N/A |

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: harm gap >= 0.04 (both seeds) | FAIL | 0.0120 (pass_count=0/2) |
| C2: benefit gap >= 0.04 (both seeds) | FAIL | nan (pass_count=0/2) |
| C3: cosine <= -0.1 (>=1 seed, supporting) | FAIL | nan (pass_count=0/2) |
| C4: data quality (both seeds) | FAIL | pass_count=0/2 |

**PASS = C1_both AND C2_both AND C4 -> FAIL**

## Per-Seed Results

| Condition | Seed | gap_harm | gap_benefit | cosine_sim | n(harm_app/ben_app/none) |
|-----------|------|----------|-------------|------------|-------------------------|
| GRADIENT_PAIR | 42 | 0.0132 | nan | nan | 198/0/128 |
| FLAT_CONTROL | 42 | nan | nan | nan | 0/0/572 |
| GRADIENT_PAIR | 123 | 0.0109 | nan | nan | 222/0/128 |
| FLAT_CONTROL | 123 | nan | nan | nan | 0/0/554 |

## Interpretation

ARC-024 NOT SUPPORTED: Neither harm gradient (mean_gap=0.0120 vs threshold 0.04) nor benefit gradient (mean_gap=nan vs threshold 0.04) detected in z_world at 400 warmup episodes.

## Failure Notes

- C1 FAIL seed=42: gap_harm_approach=0.0132 < 0.04 -- harm gradient not detected in GRADIENT_PAIR
- C1 FAIL seed=123: gap_harm_approach=0.0109 < 0.04 -- harm gradient not detected in GRADIENT_PAIR
- C2 FAIL seed=42: gap_benefit_approach=nan < 0.04 -- benefit gradient not detected in GRADIENT_PAIR
- C2 FAIL seed=123: gap_benefit_approach=nan < 0.04 -- benefit gradient not detected in GRADIENT_PAIR
- C4 FAIL seed=42: n_harm_approach=198 n_benefit_approach=0 (both need >=20) -- insufficient approach events
- C4 FAIL seed=123: n_harm_approach=222 n_benefit_approach=0 (both need >=20) -- insufficient approach events
