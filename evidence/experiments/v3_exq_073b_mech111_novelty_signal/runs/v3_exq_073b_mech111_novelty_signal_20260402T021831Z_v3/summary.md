# V3-EXQ-073b -- MECH-111 Novelty Signal

**Status:** FAIL
**Claims:** MECH-111
**Seed:** 42  **Warmup:** 150  **Eval:** 50
**novelty_bonus_weight:** 0.1

## Results

| Metric | NoveltyOFF | NoveltyON | Delta |
|---|---|---|---|
| policy_entropy | -0.0000 | -0.0000 | +0.0000 |
| novel_cell_visits | 52 | 52 | +0 |
| harm_rate | 0.0000 | 0.0000 | +0.0000 |
| novelty_ema_at_eval | -- | 0.000069 | -- |

## PASS Criteria

| Criterion | Result |
|---|---|
| C1: entropy gap >= 0.10 | FAIL |
| C2: cell coverage gap >= 3 | FAIL |
| C3: harm delta <= 0.02 | PASS |
| C4: novelty_ema > 0 | PASS |

Criteria met: 2/4 -> **FAIL**

## Interpretation

MECH-111 PARTIAL: Some exploratory signal present but below threshold. Novelty weight or training duration may need adjustment.

## Failure Notes

- C1 FAIL: entropy gap=0.0000 < 0.10
- C2 FAIL: cell coverage gap=0 < 3
