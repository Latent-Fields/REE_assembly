# V3-EXQ-199 -- MECH-025: Action-Doing Mode Probe (BreathOscillator)

**Overall Status:** FAIL  (8/10 criteria across 2 seeds)
**Claim:** MECH-025 -- action-doing mode produces distinct internal signature
**Supersedes:** V3-EXQ-050b
**Key change:** BreathOscillator (MECH-108) creates periodic uncommitted windows
**Seeds:** [42, 123]
**BreathOscillator:** period=50, amplitude=0.3, duration=10

## Per-Seed Results

| Seed | Status | Criteria | doing_mode_delta | n_uncommitted | wf_r2 | harm_std |
|------|--------|----------|-----------------|---------------|-------|----------|
| 42 | FAIL | 4/5 | -0.1534 | 634 | 0.9873 | 0.2182 |
| 123 | FAIL | 4/5 | -0.0180 | 9224 | 0.9734 | 0.1516 |

## Aggregate Metrics

| Metric | Value |
|--------|-------|
| doing_mode_delta (mean) | -0.0857 |
| uncommitted_step_count (mean) | 4929 |
| world_forward_r2 (mean) | 0.9803 |
| harm_pred_std (mean) | 0.1849 |
| sweep_step_count (mean) | 920 |

## Failure Notes

- seed 42: C1 FAIL: doing_mode_delta=-0.1534 <= 0.002
- seed 123: C1 FAIL: doing_mode_delta=-0.0180 <= 0.002
