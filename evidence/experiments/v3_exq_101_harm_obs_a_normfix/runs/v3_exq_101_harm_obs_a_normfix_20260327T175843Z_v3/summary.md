# V3-EXQ-101 -- SD-011 / ARC-016 harm_obs_a Normalization Fix Validation

**Status:** FAIL
**Claims:** SD-011, ARC-016
**Supersedes:** V3-EXQ-100b (RAW_EMA_FAIL: hazard_max normalization bug)
**Fix:** Removed per-step division by hazard_field.max() in harm_obs_a EMA update.
         Now uses raw field values clipped to [0, 1].

## Diagnosis: EMA_STILL_BROKEN

## Phase 0: Raw harm_obs_a (no encoder) -- after normfix

| Metric | HIGH (6 hazards) | LOW (2 hazards) | Criterion |
|--------|-----------------|-----------------|-----------|
| harm_obs_a mean | 0.2014 | 0.2751 | high > low * 1.1 (C1) |
| harm_obs_a autocorr_lag10 | 0.060 | -0.094 | > 0.3 (C2) |
| harm_obs_s autocorr_lag10 | 0.096 | -- | reference |

| Criterion | Result |
|-----------|--------|
| C1: raw density response | FAIL |
| C2: raw autocorr > 0.3 | FAIL |

## Phase 1: Encoder output (after training)

| Metric | HIGH (6 hazards) | LOW (2 hazards) | Criterion |
|--------|-----------------|-----------------|-----------|
| z_harm_a mean norm | 1.0909 | 1.4952 | high > low * 1.1 (C3) |
| z_harm_a autocorr_lag10 | -0.008 | -- | > z_harm_s (C4) |
| z_harm_s autocorr_lag10 | 0.061 | -- | reference |

| Criterion | Result |
|-----------|--------|
| C3: encoder density | FAIL |
| C4: encoder autocorr | FAIL |
| C5: no fatal errors | PASS |

Criteria met: 1/5 -> **FAIL**

## Failure Notes

- C1 FAIL: harm_obs_a still not responding to density after normfix (high=0.2014 vs low=0.2751)
- C2 FAIL: raw autocorr=0.060 still < 0.3 after normfix
- C3 FAIL: z_harm_a encoder not density-sensitive (high=1.0909 vs low=1.4952)
- C4 FAIL: z_harm_a autocorr=-0.008 not > z_harm_s autocorr=0.061
