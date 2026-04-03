# V3-EXQ-206 -- INV-043: Ethical Capacity Proxy Probe

**Status:** PASS
**Claim:** INV-043 -- REE architecture enables but does not guarantee ethical development
**Experiment purpose:** diagnostic (proxy -- INV-043 requires multi-agent substrate)
**Seeds:** [0, 1, 2]

## Proxy Design

INV-043 requires multi-agent caregiving substrate not available in V3.
This proxy tests whether harm evaluation machinery develops differently under:
- PROBE_RICH: trained with harm-rich data (4 hazards, positive harm events)
- PROBE_SPARSE: trained with harm-absent data (0 hazards, no positive events)
Both probes use the same shared HarmEncoder. Evaluated on same RICH test set.

## Results by Seed

| Seed | r2_rich | r2_sparse | delta | n_harm_test | n_train_harm_rich | n_train_harm_sparse |
|------|---------|----------|-------|------------|------------------|---------------------|
| 0 | 0.0799 | -8.3828 | 8.4627 | 467 | 1015 | 303 |
| 1 | 0.1284 | -4.0958 | 4.2243 | 506 | 978 | 304 |
| 2 | 0.1170 | -5.3989 | 5.5159 | 481 | 981 | 306 |


## Aggregate

| Metric | Mean | Std |
|--------|------|-----|
| r2_rich | 0.1084 | 0.0207 |
| r2_sparse | -5.9592 | 1.7944 |
| delta (rich - sparse) | 6.0676 | 1.7738 |

## PASS Criteria

| Criterion | Value | Required | Result |
|-----------|-------|---------|--------|
| C1 r2_rich | 0.1084 | > 0.1 | PASS |
| C2 r2_sparse | -5.9592 | < 0.05 | PASS |
| C3 delta | 3/3 seeds | >= 2 | PASS |
| C4 n_harm_test | 3/3 seeds | == 3 | PASS |

Criteria met: 4/4 -> **PASS**

