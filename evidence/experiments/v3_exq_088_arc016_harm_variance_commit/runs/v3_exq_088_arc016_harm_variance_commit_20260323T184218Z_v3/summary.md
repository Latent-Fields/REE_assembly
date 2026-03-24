# V3-EXQ-088 -- ARC-016: Harm Variance Commit Signal

**Status:** FAIL
**Claims:** ARC-016
**Replaces:** EXQ-038 (FAIL: z_world variance indistinguishable across danger levels)

## Architectural Reframe (ARC-016)

Old commit signal: `running_variance < commit_threshold` (z_world prediction error EMA)
New commit signal: `var(harm_scores_across_candidates) < commit_threshold`

"Do I know what harm each trajectory leads to?" rather than "Is the world stable?"

Biological parallel: ACC conflict monitoring fires when response options have similar
predicted outcomes -- not when the world is quiet, but when the agent's decision is
confident (low variance across options -> commit).

## Sweep Results

| hazard_harm | harm_var_mean | commit_rate |
|-------------|---------------|-------------|
| 0.005 | 0.000053 | 1.000 |
| 0.01 | 0.000055 | 1.000 |
| 0.02 | 0.000054 | 1.000 |
| 0.05 | 0.000054 | 1.000 |
| 0.1 | 0.000055 | 1.000 |

- Pearson r(hazard_harm, harm_var_mean): 0.5812
- harm_var CV at mid level: 0.4123

## PASS Criteria

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: harm_var increases at >= 3 transitions | FAIL | 2/4 |
| C2: Pearson r > 0.6 | FAIL | 0.5812 |
| C3: harm_var CV > 0.10 | PASS | 0.4123 |
| C4: commit_rate[low] > commit_rate[high] | FAIL | 1.000 vs 1.000 |
| C5: no fatal errors | PASS | - |

Criteria met: 2/5 -> **FAIL**

## Failure Notes

- C1 FAIL: harm_var increases at only 2/4 transitions. harm_var_means: ['0.000053', '0.000055', '0.000054', '0.000054', '0.000055']
- C2 FAIL: Pearson r=0.581 <= 0.6. Harm variance not scaling with danger.
- C4 FAIL: commit_rate[low=0.005]=1.000 <= commit_rate[high=0.1]=1.000
