# V3-EXQ-876 -- MECH-025: Action-Doing Mode Causal Signal

**Overall Status:** FAIL  (26/30 criteria across 5 seeds)
**Claim:** MECH-025 -- action-doing mode produces distinct internal (causal) signature
**Prior invalidated attempts:** V3-EXQ-050, V3-EXQ-050b, V3-EXQ-199 (instrument
  defects: wrong commitment field read as a cache or a torn-down flag; missing
  update_residue call left running_variance frozen during eval)
**Fix:** SelectionResult.committed (not cache/torn-down field) +
  agent.update_residue() every eval tick + BreathOscillator
**Seeds:** [42, 123, 7, 99, 256]
**BreathOscillator:** period=50, amplitude=0.3, duration=10

## Per-Seed Results

| Seed | Status | Criteria | doing_mode_delta | n_committed | n_uncommitted | wf_r2 | harm_std |
|------|--------|----------|-------------------|-------------|-----------------|-------|----------|
| 42 | FAIL | 5/6 | -0.0315 | 9818 | 182 | 0.9876 | 0.1030 |
| 123 | FAIL | 5/6 | -0.0664 | 903 | 165 | 0.9815 | 0.1262 |
| 7 | FAIL | 5/6 | -0.0810 | 5091 | 216 | 0.9173 | 0.0637 |
| 99 | FAIL | 5/6 | -0.0869 | 2596 | 201 | 0.9576 | 0.0418 |
| 256 | PASS | 6/6 | +0.0025 | 8520 | 182 | 0.9433 | 0.0671 |

## Aggregate Metrics

| Metric | Value |
|--------|-------|
| doing_mode_delta (mean) | -0.0527 |
| committed_step_count (mean) | 5386 |
| uncommitted_step_count (mean) | 189 |
| world_forward_r2 (mean) | 0.9575 |
| harm_pred_std (mean) | 0.0804 |
| sweep_step_count (mean) | 988 |

## Failure Notes

- seed 42: C1 FAIL: doing_mode_delta=-0.0315 <= 0.002
- seed 123: C1 FAIL: doing_mode_delta=-0.0664 <= 0.002
- seed 7: C1 FAIL: doing_mode_delta=-0.0810 <= 0.002
- seed 99: C1 FAIL: doing_mode_delta=-0.0869 <= 0.002
