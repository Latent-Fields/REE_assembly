# V3-EXQ-141 -- MECH-111 Novelty/Curiosity Drive Discriminative Pair

**Status:** FAIL
**Claims:** MECH-111
**Decision:** hybridize
**Seeds:** [42, 123]
**Conditions:** NOVELTY_DRIVE_ON vs NOVELTY_DRIVE_ABLATED
**Warmup:** 200 eps x 200 steps  **Eval:** 50 eps x 200 steps
**Env:** CausalGridWorld size=10, 5 hazards, 5 resources nav_bias=0.3
**novelty_bonus_weight:** 0.1

## Design

MECH-111 asserts E1 prediction-error surprise at moderate magnitudes generates intrinsic positive valence (curiosity/novelty drive). The experiment compares NOVELTY_DRIVE_ON (E1 EMA bonus active) against NOVELTY_DRIVE_ABLATED (no bonus) across 2 matched seeds. Key test: does the drive increase exploration (entropy, cell coverage) without increasing harm (curiosity-surprise is safe, not alarm-surprise)?

## Pre-Registered Thresholds

C1: per-seed entropy_gap (ON-ABLATED) >= 0.1 (both seeds)
C2: per-seed cell_gap (ON-ABLATED) >= 3 (both seeds)
C3: per-seed harm_delta (ON-ABLATED) <= 0.02 (both seeds)
C4: novelty_ema_ON > 1e-06 both seeds (signal non-zero)
C5: n_harm_min >= 10 both conditions (data quality)

## Results

| Condition | entropy | novel_cells | harm_rate |
|-----------|---------|-------------|----------|
| NOVELTY_DRIVE_ON      | -0.0000 | 50.5 | 0.0000 |
| NOVELTY_DRIVE_ABLATED | -0.0000 | 50.5 | 0.0000 |

**per-seed entropy_gap: [0.0, 0.0]**
**per-seed cell_gap: [0, 0]**
**per-seed harm_delta: [0.0, 0.0]**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: entropy_gap >= 0.1 (both seeds) | FAIL | [0.0, 0.0] |
| C2: cell_gap >= 3 (both seeds) | FAIL | [0, 0] |
| C3: harm_delta <= 0.02 (both seeds) | PASS | [0.0, 0.0] |
| C4: novelty_ema_ON > 1e-06 (both seeds) | PASS | [0.0001059, 0.0001483] |
| C5: n_harm_min >= 10 | FAIL | 0 |

Criteria met: 2/5 -> **FAIL**

## Interpretation

MECH-111 NOT SUPPORTED: novelty bonus does not produce measurable exploration increase. E1 error may be too uniform across states, or the EMA is not feeding back into E3 selection effectively. Criteria: C1=False C2=False C3=True C4=True C5=False.

## Per-Seed Detail

NOVELTY_DRIVE_ON:
  seed=42: entropy=-0.0000 cells=53 harm_rate=0.0000 novelty_ema=0.00011
  seed=123: entropy=-0.0000 cells=48 harm_rate=0.0000 novelty_ema=0.00015

NOVELTY_DRIVE_ABLATED:
  seed=42: entropy=-0.0000 cells=53 harm_rate=0.0000
  seed=123: entropy=-0.0000 cells=48 harm_rate=0.0000

## Failure Notes

- C1 FAIL: per-seed entropy_gap [0.0, 0.0] < 0.1 -- novelty bonus does not produce measurable entropy increase
- C2 FAIL: per-seed cell_gap [0, 0] < 3 -- novelty drive does not increase novel cell coverage
- C5 FAIL: n_harm_min=0 < 10 -- insufficient harm contacts; increase nav_bias or eval episodes
