# V3-EXQ-630 -- ARC-029 / MECH-090: Across-tick nav_competence (ecological)

**Status:** FAIL  (4/5 incl C5)
**Claims:** ARC-029, MECH-090
**Design:** 3-arm eval (OFF / NAV_COMP_ON / BOTH_ON) on shared trained weights;
degrade/recover env (SD-022 scheduled all-limb injection + env-emitted readiness).

## Results (averaged across seeds)

| Arm | committed_rate_ready | committed_rate_degraded |
|---|---|---|
| ARM_0 OFF baseline | 1.0000 | 0.0000 |
| ARM_2 NAV_COMP_ON | 1.0000 | 0.0356 |
| ARM_3 BOTH_ON | (ready) | 0.0304 |

| Metric | Value |
|---|---|
| ARM_2 suppress_delta (ready - degraded) | 0.9644 |
| ARM_0 baseline_delta (abs) | 1.0000 |
| nav-gate blocks (NAV / BOTH) | 668 / 829 |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1 gate fires (>=1 nav block) | PASS | nav=668 both=829 |
| C2 suppress-on-degrade (>= 0.15) | PASS | 0.9644 |
| C3 admit-on-recover (ready >= 0.1) | PASS | 1.0000 |
| C4 OFF-baseline null (< 0.15) | FAIL | 1.0000 |
| C5 composed at least as strict | PASS | both_deg=0.0304 nav_deg=0.0356 |

PASS = C1 AND C2 AND C3 AND C4 -> **FAIL**

## Failure / Routing Notes

- C4 FAIL: ARM_0 baseline_delta=1.0000 >= 0.15: commitment is readiness-conditioned even with the gate OFF -> damage->commitment confound -> /diagnose-errors
