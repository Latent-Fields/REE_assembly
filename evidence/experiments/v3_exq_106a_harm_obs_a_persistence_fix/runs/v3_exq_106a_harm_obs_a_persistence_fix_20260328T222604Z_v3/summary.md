# V3-EXQ-106a -- SD-011 harm_obs_a Temporal Persistence (episode-reset fix)

**Status:** PASS
**Claims:** SD-011
**Supersedes:** V3-EXQ-106 (C4 FAIL: autocorr=0.070; episode-reset destroyed persistence)
**Seeds:** [42, 43, 44, 45, 46]  **Steps/seed/condition:** 500

## Fix Applied

CausalGridWorldV2.harm_obs_a_ema moved from reset() to __init__(). Now persists across
episode boundaries, as intended for a homeostatic/affective accumulator.
Expected autocorr at lag 10 = (1-0.05)^10 ~ 0.60 >> threshold 0.3.

## Results

| Metric | HIGH (6 hazards) | LOW (2 hazards) | Criterion |
|--------|--------------|-------------|-----------|
| Grid-wide field mean | 1.7785 | 0.5900 | HIGH > LOW * 2.5x (C1) |
| Local raw hazard | 1.9064 | 0.6340 | HIGH > LOW * 1.1x (C3) |
| EMA dim-0 mean | 0.9620 | 0.6005 | reference |
| Autocorr lag10 | 0.6092 | 0.6495 | > 0.3 (C4) |

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
| 42 | 1.7741 | 0.5858 | 1.9332 | 0.5931 | 0.6092 | 0.7357 |
| 43 | 1.7788 | 0.5907 | 1.8586 | 0.6316 | 0.6092 | 0.6166 |
| 44 | 1.7854 | 0.5993 | 1.9967 | 0.6875 | 0.6092 | 0.5466 |
| 45 | 1.7796 | 0.5840 | 1.8955 | 0.5876 | 0.6092 | 0.6649 |
| 46 | 1.7747 | 0.5903 | 1.8479 | 0.6704 | 0.6092 | 0.6835 |
