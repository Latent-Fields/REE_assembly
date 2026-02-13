# Experiment Index: trajectory_integrity

Generated: `2026-02-13T15:04:06.549584Z`

- Experiment profile: `experiment.md`
- Stop criteria: `../../stop_criteria.v1.yaml`
- Environment qualification: `../../environment_qualification.v1.yaml`

## Runs

| run_id | timestamp_utc | status | environment | key metrics | deltas vs previous | stop-criteria hits | summary |
|---|---|---|---|---|---|---|---|
| `exp_0005_20260213T090639999186Z` | `2026-02-13T09:06:39.999186Z` | **FAIL** | legacy-trajectory-integrity-proposal-exp-0005 v=legacy-d39241ebcad5 tier=legacy (missing-metrics) | - | - | - | [`summary`](runs/exp_0005_20260213T090639999186Z/summary.md) / [`manifest`](runs/exp_0005_20260213T090639999186Z/manifest.json) / [`metrics`](runs/exp_0005_20260213T090639999186Z/metrics.json) |
| `exp_0005_20260213T090639951474Z` | `2026-02-13T09:06:39.951474Z` | PASS | legacy-trajectory-integrity-proposal-exp-0005 v=legacy-d39241ebcad5 tier=legacy (missing-metrics) | - | - | - | [`summary`](runs/exp_0005_20260213T090639951474Z/summary.md) / [`manifest`](runs/exp_0005_20260213T090639951474Z/manifest.json) / [`metrics`](runs/exp_0005_20260213T090639951474Z/metrics.json) |
| `exp_0003_20260213T090639905363Z` | `2026-02-13T09:06:39.905363Z` | **FAIL** | legacy-trajectory-integrity-proposal-exp-0003 v=legacy-d39241ebcad5 tier=legacy (missing-metrics) | - | - | - | [`summary`](runs/exp_0003_20260213T090639905363Z/summary.md) / [`manifest`](runs/exp_0003_20260213T090639905363Z/manifest.json) / [`metrics`](runs/exp_0003_20260213T090639905363Z/metrics.json) |
| `exp_0003_20260213T090639857099Z` | `2026-02-13T09:06:39.857099Z` | PASS | legacy-trajectory-integrity-proposal-exp-0003 v=legacy-d39241ebcad5 tier=legacy (missing-metrics) | - | - | - | [`summary`](runs/exp_0003_20260213T090639857099Z/summary.md) / [`manifest`](runs/exp_0003_20260213T090639857099Z/manifest.json) / [`metrics`](runs/exp_0003_20260213T090639857099Z/metrics.json) |
| `2026-02-13T070000Z_dummy-fail` | `2026-02-13T07:00:00Z` | **FAIL** | legacy-trajectory-integrity-trajectory-integrity-stress v=legacy-222222222222 tier=stress (missing-metrics) | fatal_error_count=0<br>ledger_edit_detected_count=2<br>explanation_policy_divergence_rate=0.14<br>domination_lock_in_events=1 | fatal_error_count:+0<br>ledger_edit_detected_count:+2<br>explanation_policy_divergence_rate:+0.122<br>domination_lock_in_events:+1 | ledger_edit_detected_count > 0.0 (value=2); explanation_policy_divergence_rate > 0.05 (value=0.14); domination_lock_in_events > 0.0 (value=1) | [`summary`](runs/2026-02-13T070000Z_dummy-fail/summary.md) / [`manifest`](runs/2026-02-13T070000Z_dummy-fail/manifest.json) / [`metrics`](runs/2026-02-13T070000Z_dummy-fail/metrics.json) |
| `2026-02-13T060000Z_dummy-pass` | `2026-02-13T06:00:00Z` | PASS | legacy-trajectory-integrity-trajectory-integrity-smoke v=legacy-111111111111 tier=toy (missing-metrics) | fatal_error_count=0<br>ledger_edit_detected_count=0<br>explanation_policy_divergence_rate=0.018<br>domination_lock_in_events=0 | - | - | [`summary`](runs/2026-02-13T060000Z_dummy-pass/summary.md) / [`manifest`](runs/2026-02-13T060000Z_dummy-pass/manifest.json) / [`metrics`](runs/2026-02-13T060000Z_dummy-pass/metrics.json) |
