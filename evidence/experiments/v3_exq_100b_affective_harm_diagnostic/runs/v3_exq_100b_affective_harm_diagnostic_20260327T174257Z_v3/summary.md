# V3-EXQ-100b -- SD-011 / ARC-016 Affective Harm Stream Diagnostic

**Status:** FAIL
**Claims:** SD-011, ARC-016
**Supersedes:** V3-EXQ-100 (C2 negative autocorrelation anomaly)
**Design:** Two-phase: raw harm_obs_a diagnostic + encoder quality check

## Diagnosis: RAW_EMA_FAIL

## Phase 0: Raw harm_obs_a (no encoder)

| Metric | HIGH (6 hazards) | LOW (2 hazards) | Criterion |
|--------|-----------------|-----------------|-----------|
| harm_obs_a mean | 0.1308 | 0.1973 | high > low * 1.1 (C1) |
| harm_obs_a autocorr_lag10 | 0.069 | -0.063 | > 0.3 (C2) |
| harm_obs_s autocorr_lag10 | 0.096 | -- | reference |

| Criterion | Result |
|-----------|--------|
| C1: raw density response | FAIL |
| C2: raw autocorr > 0.3 | FAIL |

## Phase 1: Encoder output (after training)

| Metric | HIGH (6 hazards) | LOW (2 hazards) | Criterion |
|--------|-----------------|-----------------|-----------|
| z_harm_a mean norm | 0.7423 | 1.0883 | high > low * 1.1 (C3) |
| z_harm_a autocorr_lag10 | -0.004 | -- | > z_harm_s (C4) |
| z_harm_s autocorr_lag10 | 0.061 | -- | reference |

| Criterion | Result |
|-----------|--------|
| C3: encoder density | FAIL |
| C4: encoder autocorr | FAIL |
| C5: no fatal errors | PASS |

Criteria met: 1/5 -> **FAIL**

## Failure Notes

- C1 FAIL: raw harm_obs_a NOT responding to density (high=0.1308 vs low=0.1973) -- root cause: CausalGridWorldV2 EMA not generating density-sensitive signal
- C2 FAIL: raw harm_obs_a autocorr=0.069 (< 0.3) -- EMA not providing temporal persistence
- C3 FAIL: z_harm_a encoder output not density-sensitive (high=0.7423 vs low=1.0883) -- encoder degenerates despite healthy input
- C4 FAIL: z_harm_a autocorr=-0.004 not > z_harm_s autocorr=0.061 -- encoder not preserving temporal stability
