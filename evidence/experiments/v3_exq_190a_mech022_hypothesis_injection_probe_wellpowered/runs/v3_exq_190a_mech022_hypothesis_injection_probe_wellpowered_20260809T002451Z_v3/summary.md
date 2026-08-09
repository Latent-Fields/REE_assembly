# V3-EXQ-190a -- MECH-022 Hypothesis Injection Probe (well-powered)

**Status:** FAIL
**Claims:** MECH-022
**Supersedes:** V3-EXQ-190
**Decision:** retire_ree_claim
**Seeds:** [42, 123, 7]
**Conditions:** HYPOTHESIS_INJECTION_ON vs HYPOTHESIS_INJECTION_OFF
**Warmup:** 220 eps x 200 steps  **Eval:** 100 eps x 200 steps
**Env:** CausalGridWorld size=10, 5 hazards, 5 resources nav_bias=0.4

## Design

Well-powered successor to V3-EXQ-190 (C4 FAILed at n_harm_min=0). Same claim test (paired INJECTION_ON vs INJECTION_OFF, same thresholds), with nav_bias raised 0.25->0.4, eval_episodes raised 50->100, warmup raised 150->220, and seeds extended from 2 to 3. See module docstring for the calibration that ruled out hazard density as the bottleneck.

## Pre-Registered Thresholds

C1: per-seed harm_gap (OFF-ON) >= 0.005 (all seeds)
C2: per-seed residue_gap (OFF-ON) >= 0 (all seeds, directional)
C3: per-seed traj_gap (ON-OFF) < 0 (all seeds, lower=better)
C4: n_harm_min >= 10 both conditions (data quality)
C5: proposal score_var > 1e-06 in INJECTION_ON (non-degenerate)

## Results

| Condition | harm_rate | mean_residue | mean_traj_score |
|-----------|-----------|--------------|----------------|
| INJECTION_ON  | 0.0441 | 38.8646 | 370.6874 |
| INJECTION_OFF | 0.0426 | 38.7915 | 337.5920 |

**per-seed harm_gap (OFF-ON): [0.00252, -0.00706, -7e-05]**
**per-seed residue_gap (OFF-ON): [-0.70879, 0.246, 0.24361]**
**per-seed traj_gap (ON-OFF): [-6.64691, -35.23424, 141.16721]**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: harm_gap >= 0.005 (all seeds) | FAIL | [0.00252, -0.00706, -7e-05] |
| C2: residue_gap >= 0 (all seeds) | FAIL | [-0.70879, 0.246, 0.24361] |
| C3: traj_gap < 0 (all seeds) | FAIL | [-6.64691, -35.23424, 141.16721] |
| C4: n_harm_min >= 10 | PASS | 148 |
| C5: score_var > 1e-06 (INJECTION_ON) | PASS | [0.24083433, 1.95657337, 75.91165455] |

Criteria met: 2/5 -> **FAIL**

## Interpretation

MECH-022 NOT SUPPORTED, well-powered read (n_harm_min=148 >= 10 across 3 seeds): hippocampal injection does not produce measurable improvement over random proposals at this training scale, and this is no longer a data-quality artifact as it was in V3-EXQ-190. Criteria: C1=False C2=False C3=False C4=True C5=True.

## Per-Seed Detail

INJECTION_ON:
  seed=42: harm_rate=0.0436 residue=39.1676 traj_score=118.7691 cells=62 score_var=0.240834
  seed=123: harm_rate=0.0457 residue=37.4292 traj_score=151.1805 cells=61 score_var=1.956573
  seed=7: harm_rate=0.0431 residue=39.9969 traj_score=842.1126 cells=64 score_var=75.911655

INJECTION_OFF:
  seed=42: harm_rate=0.0461 residue=38.4588 traj_score=125.4160 cells=64
  seed=123: harm_rate=0.0387 residue=37.6752 traj_score=186.4148 cells=64
  seed=7: harm_rate=0.0430 residue=40.2405 traj_score=700.9454 cells=64

## Failure Notes

- C1 FAIL: per-seed harm_gap (OFF-ON) [0.00252, -0.00706, -7e-05] < 0.005 -- hippocampal injection does not reduce harm rate vs random baseline
- C2 FAIL: per-seed residue_gap (OFF-ON) [-0.70879, 0.246, 0.24361] -- injection does not reduce accumulated residue
- C3 FAIL: per-seed traj_gap (ON-OFF) [-6.64691, -35.23424, 141.16721] -- E3 does not rate hippocampal proposals higher than random
