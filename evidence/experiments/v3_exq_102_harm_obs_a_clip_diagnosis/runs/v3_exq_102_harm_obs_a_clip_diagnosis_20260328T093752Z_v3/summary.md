# V3-EXQ-102 -- SD-011 harm_obs_a Clip vs Raw Density Diagnostic

**Status:** FAIL
**Claims:** SD-011
**Supersedes:** V3-EXQ-101 (EMA_STILL_BROKEN after normfix)
**Seeds:** [42, 43, 44, 45, 46]  **Steps/seed/condition:** 300

## Diagnosis: CLIP_SATURATION

Hypotheses tested:
- H1 PLACEMENT_CONFOUND: seed=42 first-2-hazards placement biases single-seed test
- H2 CLIP_SATURATION: [0,1] clip destroys additive density info (cells near 2+ hazards cap)

## Phase 0: Multi-seed Density Response (N=5 seeds x 300 steps)

| Metric | HIGH (6 hazards) | LOW (2 hazards) | Criterion |
|--------|-----------------|-----------------|-----------|
| Grid-wide field mean | 1.7754 | 0.5900 | high > low * 2.5 (C1) |
| Local CLIPPED hazard dims | 0.2215 | 0.2422 | high > low * 1.1 (C2) |
| Local RAW hazard dims | 1.6488 | 0.5516 | high > low * 1.1 (C3) |
| Resource dims | 0.1722 | 0.3144 | reference only |

| Criterion | Result | Interpretation |
|-----------|--------|----------------|
| C1: field scales with n_hazards | PASS | field construction |
| C2: clipped local density | FAIL | clip approach |
| C3: raw local density | PASS | raw (no-clip) approach |

## Phase 1: Temporal Persistence

| Metric | Value | Criterion |
|--------|-------|-----------|
| harm_obs_a norm autocorr_lag10 | 0.014 | > 0.3 (C4) |

| Criterion | Result |
|-----------|--------|
| C4: temporal persistence | FAIL |
| C5: no fatal errors | PASS |

Criteria met: 3/5 -> **FAIL**

## Failure Notes

- C2 FAIL: clipped local hazard dims not density-responsive (HIGH=0.2215 LOW=0.2422, ratio=0.91x < 1.1x)
- C4 FAIL: harm_obs_a norm autocorr=0.014 < 0.3 -- EMA not providing temporal persistence on agent trajectory

## Per-Seed Results

| Seed | Grid HIGH | Grid LOW | Clip HIGH | Clip LOW | Raw HIGH | Raw LOW |
|------|-----------|----------|-----------|----------|----------|---------|
| 42 | 1.7544 | 0.5806 | 0.2361 | 0.2538 | 1.6304 | 0.5608 |
| 43 | 1.7892 | 0.5890 | 0.2066 | 0.2537 | 1.6180 | 0.5527 |
| 44 | 1.7785 | 0.6039 | 0.2130 | 0.2437 | 1.6894 | 0.6089 |
| 45 | 1.7799 | 0.5825 | 0.2200 | 0.2093 | 1.6699 | 0.4892 |
| 46 | 1.7751 | 0.5937 | 0.2320 | 0.2507 | 1.6364 | 0.5466 |

