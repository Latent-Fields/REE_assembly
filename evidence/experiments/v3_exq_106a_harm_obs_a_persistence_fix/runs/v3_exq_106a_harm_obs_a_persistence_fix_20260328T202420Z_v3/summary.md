# V3-EXQ-106a -- SD-011 harm_obs_a Temporal Persistence (episode-reset fix)

**Status:** PASS
**Claims:** SD-011
**Supersedes:** V3-EXQ-106 (C4 FAIL: autocorr=0.070; episode-reset destroyed persistence)
**Seeds:** [42]  **Steps/seed/condition:** 60

## Fix Applied

CausalGridWorldV2.harm_obs_a_ema moved from reset() to __init__(). Now persists across
episode boundaries, as intended for a homeostatic/affective accumulator.
Expected autocorr at lag 10 = (1-0.05)^10 ~ 0.60 >> threshold 0.3.

## Results

| Metric | HIGH (6 hazards) | LOW (2 hazards) | Criterion |
|--------|--------------|-------------|-----------|
| Grid-wide field mean | 1.7655 | 0.5901 | HIGH > LOW * 2.5x (C1) |
| Local raw hazard | 1.8796 | 0.5768 | HIGH > LOW * 1.1x (C3) |
| EMA dim-0 mean | 0.6979 | 0.3867 | reference |
| Autocorr lag10 | 0.5111 | 0.5987 | > 0.3 (C4) |

| Criterion | Result |
|-----------|--------|
| C1: field scales with n_hazards | PASS |
| C3: raw density responsive | PASS |
| C4: temporal persistence | PASS |
| C5: no fatal errors | PASS |

Criteria met: 4/4 -> **PASS**


## Per-Seed Results

| Seed | Grid HIGH | Grid LOW | Raw HIGH | Raw LOW | AC HIGH | AC LOW |
|------|-----------|----------|----------|---------|---------|--------|
| 42 | 1.7655 | 0.5901 | 1.8796 | 0.5768 | 0.5111 | 0.5987 |
