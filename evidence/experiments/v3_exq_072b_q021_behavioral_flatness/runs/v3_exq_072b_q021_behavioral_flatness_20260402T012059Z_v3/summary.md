# V3-EXQ-072b -- Q-021 Behavioral Flatness Diagnostic

**Status:** FAIL
**Claims:** Q-021
**Seed:** 42  **Warmup:** 200 eps  **Eval:** 50 eps

## Conditions

| Condition | resource_visit_rate | policy_entropy | n_resource_events |
|---|---|---|---|
| NoGo-only (A) | 0.0000 | -0.0000 | 0 |
| Competitive (B) | 0.0000 | -0.0000 | 0 |
| Random baseline | 0.0000 | 1.3858 | 0 |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: nogo <= random+0.02 (flatness present) | PASS | 0.0000 vs 0.0200 |
| C2: competitive >= nogo+0.05 (Go channel helps) | FAIL | 0.0000 vs 0.0500 |
| C3: entropy gap >= 0.10 (diversity difference) | FAIL | 0.0000 |
| C4: nogo resource events <= comp*0.80 | PASS | 0 vs 0.0 |

Criteria met: 2/4 -> **FAIL**

## Interpretation

Q-021 PARTIAL: Some behavioral flatness signal detected but below threshold. Longer training or stronger harm signal may be needed.

## Failure Notes

- C2 FAIL: comp resource_rate=0.0000 < nogo+0.05=0.0500
- C3 FAIL: entropy gap=0.0000 < 0.10
