# V3-EXQ-876a -- MECH-025: Action-Doing Mode Convergence Redesign

**Overall Status:** PASS  (30/30 criteria across 5 seeds)
**Claim:** MECH-025 -- action-doing mode produces a distinct (convergent) internal causal signature
**Redesign of:** V3-EXQ-876 (measurement_test_design_defect per
  failure_autopsy_mech025-cluster-876-671b_2026-08-03 -- C1's predicted sign
  contradicted the claim's own cited literature)
**Fresh seeds (disjoint from V3-EXQ-876's [42,123,7,99,256], per GOV-REUSE-1 anti-circularity):** [11, 17, 29, 53, 71]
**BreathOscillator:** period=50, amplitude=0.3, duration=10

## Per-Seed Results

| Seed | Status | Criteria | doing_mode_delta | n_committed | n_uncommitted | wf_r2 | harm_std | precision_ratio |
|------|--------|----------|-------------------|-------------|-----------------|-------|----------|-----------------|
| 11 | PASS | 6/6 | -0.1789 | 9817 | 183 | 0.9443 | 0.1053 | 363256.62 |
| 17 | PASS | 6/6 | -0.0022 | 9838 | 162 | 0.9665 | 0.1319 | 328263.76 |
| 29 | PASS | 6/6 | -0.1340 | 9177 | 171 | 0.9188 | 0.0920 | 167271.21 |
| 53 | PASS | 6/6 | -0.0464 | 1315 | 190 | 0.9844 | 0.0689 | 0.00 |
| 71 | PASS | 6/6 | -0.0960 | 9815 | 185 | 0.9558 | 0.1449 | 345732.74 |

## Aggregate Metrics

| Metric | Value |
|--------|-------|
| doing_mode_delta (mean) | -0.0915 |
| committed_step_count (mean) | 7992 |
| uncommitted_step_count (mean) | 178 |
| world_forward_r2 (mean) | 0.9540 |
| harm_pred_std (mean) | 0.1086 |
| sweep_step_count (mean) | 1586 |
| precision_ratio (mean, NON-GATING) | 240904.87 |

