# V3-EXQ-190 -- MECH-022 Hypothesis Injection Probe

**Status:** FAIL
**Claims:** MECH-022
**Decision:** inconclusive
**Seeds:** [42, 123]
**Conditions:** HYPOTHESIS_INJECTION_ON vs HYPOTHESIS_INJECTION_OFF
**Warmup:** 150 eps x 200 steps  **Eval:** 50 eps x 200 steps
**Env:** CausalGridWorld size=10, 5 hazards, 5 resources nav_bias=0.25

## Design

MECH-022 asserts hippocampal systems inject hypotheses gated by the control plane. This experiment compares INJECTION_ON (full HippocampalModule CEM proposals) against INJECTION_OFF (random trajectory proposals, same E3 evaluation) across 2 matched seeds. Key test: does terrain-guided hypothesis injection produce measurably better trajectories and lower harm?

## Pre-Registered Thresholds

C1: per-seed harm_gap (OFF-ON) >= 0.005 (both seeds)
C2: per-seed residue_gap (OFF-ON) >= 0 (both seeds, directional)
C3: per-seed traj_gap (ON-OFF) < 0 (both seeds, lower=better)
C4: n_harm_min >= 10 both conditions (data quality)
C5: proposal score_var > 1e-06 in INJECTION_ON (non-degenerate)

## Results

| Condition | harm_rate | mean_residue | mean_traj_score |
|-----------|-----------|--------------|----------------|
| INJECTION_ON  | 0.0000 | 17.9514 | 6692.8874 |
| INJECTION_OFF | 0.0115 | 18.2402 | 7049.1804 |

**per-seed harm_gap (OFF-ON): [0.0062, 0.01678]**
**per-seed residue_gap (OFF-ON): [0.55854, 0.01905]**
**per-seed traj_gap (ON-OFF): [-716.42758, 3.84157]**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: harm_gap >= 0.005 (both seeds) | PASS | [0.0062, 0.01678] |
| C2: residue_gap >= 0 (both seeds) | PASS | [0.55854, 0.01905] |
| C3: traj_gap < 0 (both seeds) | FAIL | [-716.42758, 3.84157] |
| C4: n_harm_min >= 10 | FAIL | 0 |
| C5: score_var > 1e-06 (INJECTION_ON) | PASS | [0.00801603, 1.48e-06] |

Criteria met: 3/5 -> **FAIL**

## Interpretation

INCONCLUSIVE: insufficient harm contacts (n_harm_min=0 < 10). Cannot evaluate MECH-022. Increase nav_bias or eval episodes.

## Per-Seed Detail

INJECTION_ON:
  seed=42: harm_rate=0.0000 residue=18.0443 traj_score=13166.0496 cells=50 score_var=0.008016
  seed=123: harm_rate=0.0000 residue=17.8586 traj_score=219.7252 cells=51 score_var=0.000001

INJECTION_OFF:
  seed=42: harm_rate=0.0062 residue=18.6028 traj_score=13882.4771 cells=64
  seed=123: harm_rate=0.0168 residue=17.8776 traj_score=215.8837 cells=64

## Failure Notes

- C3 FAIL: per-seed traj_gap (ON-OFF) [-716.42758, 3.84157] -- E3 does not rate hippocampal proposals higher than random
- C4 FAIL: n_harm_min=0 < 10 -- insufficient harm contacts; increase nav_bias or eval episodes
