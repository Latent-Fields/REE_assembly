# V3-EXQ-049e — MECH-090: Two-Condition Beta Gate Test

**Status:** PASS
**Claim:** MECH-090 — beta gate holds E3 policy output during committed action, releases when uncommitted
**Design:** Two-condition — trained agent (C1/C3) vs fresh agent (C2/C4)
**alpha_world:** 0.9  |  **Warmup:** 400 eps  |  **Eval:** 50 eps/condition  |  **Seed:** 0

## Design Rationale

Single-agent eval (EXQ-049d) cannot test C2: once trained, the agent is permanently
committed (variance ~0). A fresh agent starts at precision_init=0.5 > commit_threshold=0.40,
so it is persistently uncommitted without any artificial variance manipulation.
No hysteresis is needed: both conditions are at stable extremes of the variance distribution.

## Condition A — Trained Agent

| Metric | Value |
|--------|-------|
| Final running_variance (post-train) | 0.000003 |
| Mean committed fraction (train) | 1.000 |
| Committed steps (eval) | 10000 |
| Uncommitted steps (eval) | 0 |
| committed_hold_concordance | 1.000 |
| hold_count | 10347 |

## Condition B — Fresh Agent

| Metric | Value |
|--------|-------|
| precision_init (= running_variance) | 0.500000 |
| Committed steps (eval) | 0 |
| Uncommitted steps (eval) | 321 |
| uncommitted_release_concordance | 1.000 |
| propagation_count | 50 |

## PASS Criteria

| Criterion | Source | Result | Value |
|---|---|---|---|
| C1: trained committed_hold_concordance > 0.6 | Cond A | PASS | 1.000 |
| C2: fresh uncommitted_release_concordance > 0.5 | Cond B | PASS | 1.000 |
| C3: trained hold_count > 0 | Cond A | PASS | 10347 |
| C4: fresh propagation_count > 0 | Cond B | PASS | 50 |
| C5: No fatal errors | Both | PASS | 0 |

Criteria met: 5/5 → **PASS**

