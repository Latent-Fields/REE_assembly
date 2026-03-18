# V3-EXQ-005 -- MECH-069 Error Signal Scale Separation

**Status:** PASS
**Episodes:** 200 x 200 steps, RANDOM policy
**Hazards:** 8 (num_hazards)
**Seed:** 0

## MECH-069 Prediction

E1 (sensory prediction), E2 (motor-sensory), and E3 (harm/goal) error signals
are incommensurable in scale and temporal structure. They cannot be combined by
a fixed scalar lambda without corrupting the independent signal content of each.

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: scale_ratio > 5.0 (max/min mean loss) | PASS | 42466.00 |
| C2: abs(corr(E1, E3)) < 0.3 | PASS | 0.000 |
| C3: abs(corr(E2w, E3)) < 0.3 | PASS | 0.140 |
| C4: Harm events > 100 | PASS | 538 |
| C5: No fatal errors | PASS | 0 |
| C6: n_E3_measurements >= 50 | PASS | 4792 |

## Loss Channel Statistics

| Channel | Mean | Std | CV (std/mean) |
|---|---|---|---|
| E1 (sensory prediction) | 0.00000 | 0.00000 | 0.00 |
| E2w (world_forward) | 0.00002 | 0.00014 | 8.91 |
| E3 (harm BCE) | 0.66772 | 0.02925 | 0.04 |

**Scale ratio (max/min mean):** 42466.00

## Pairwise Correlations (at steps where E3 fired)

| Pair | Pearson r | Incommensurable? |
|---|---|---|
| corr(E1, E3) | 0.000 | YES |
| corr(E2w, E3) | 0.140 | YES |

Total harm events: 538 | E3 measurements: 4792

Criteria met: 6/6 -> **PASS**
