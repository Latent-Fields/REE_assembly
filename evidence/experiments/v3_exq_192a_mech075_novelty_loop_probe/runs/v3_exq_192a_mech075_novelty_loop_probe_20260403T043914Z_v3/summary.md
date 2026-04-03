# V3-EXQ-192a -- MECH-075 Hippocampal-VTA Novelty Loop Probe

**Status:** FAIL
**Claims:** MECH-075
**Decision:** inconclusive
**Seeds:** [42]
**Conditions:** NOVELTY_LOOP_ON vs NOVELTY_LOOP_OFF
**Warmup:** 1 eps x 5 steps  **Eval:** 1 eps x 5 steps
**Env:** CausalGridWorld size=10, 5 hazards, 5 resources nav_bias=0.25
**novelty_gain:** 2.0

## Design

MECH-075 asserts that BG perform dopaminergic gain/threshold setting on hippocampal attractor dynamics (Lisman & Grace 2005 novelty loop). The experiment tests whether z_world mismatch detection (hippocampal novelty) driving CEM proposal noise scaling (VTA-like dopaminergic modulation) improves exploration efficiency. NOVELTY_LOOP_ON scales CEM noise by (1 + gain * novelty_ema); NOVELTY_LOOP_OFF uses fixed noise. The manipulation targets the PROPOSAL distribution, not trajectory scoring (distinct from MECH-111).

## Pre-Registered Thresholds

C1: per-seed unique_cells_gap (ON-OFF) >= 3 (all seeds)
C2: per-seed hazard_discovery_gap (ON-OFF) >= 1 (all seeds)
C3: per-seed harm_delta (ON-OFF) <= 0.02 (all seeds)
C4: mean_novelty_signal_ON > 0.0001 (all seeds)

## Results

| Condition | cells | hazards_found | harm_rate | novelty | cem_scale |
|-----------|-------|---------------|-----------|---------|----------|
| NOVELTY_LOOP_ON  | 4.0 | 0.0 | 0.0000 | 0.012591 | 1.015 |
| NOVELTY_LOOP_OFF | 4.0 | 0.0 | 0.0000 | 0.012591 | 1.000 |

**per-seed cell_gap: [0]**
**per-seed hazard_gap: [0]**
**per-seed harm_delta: [0.0]**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: cell_gap >= 3 (all seeds) | FAIL | [0] |
| C2: hazard_gap >= 1 (all seeds) | FAIL | [0] |
| C3: harm_delta <= 0.02 (all seeds) | PASS | [0.0] |
| C4: novelty_signal > 0.0001 (all seeds) | PASS | [0.0125908] |

Criteria met: 2/4 -> **FAIL**

## Interpretation

MECH-075 NOT SUPPORTED: novelty loop does not produce measurable exploration improvement. E1 world-prediction error may be too uniform across z_world states, or CEM noise scaling has no effect on trajectory diversity at this gain level. Criteria: C1=False C2=False C3=True C4=True.

## Per-Seed Detail

NOVELTY_LOOP_ON:
  seed=42: cells=4 hazards=0 resources=1 harm_rate=0.0000 novelty=0.012591 cem_scale=1.015

NOVELTY_LOOP_OFF:
  seed=42: cells=4 hazards=0 resources=1 harm_rate=0.0000 novelty=0.012591

## Failure Notes

- C1 FAIL: per-seed cell_gap [0] < 3 -- novelty loop does not increase spatial coverage
- C2 FAIL: per-seed hazard_gap [0] < 1 -- novelty loop does not improve hazard discovery
