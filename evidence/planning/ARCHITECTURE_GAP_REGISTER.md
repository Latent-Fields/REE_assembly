# Architecture Gap Register

Generated: `2026-02-15T14:41:04.678072Z`

This register highlights claims under structural pressure and flags where the evidence pattern suggests a **consider new structure** decision.

| gap_id | claim_id | status | conflict_ratio | lit_non_support_ratio | confidence_delta_lit_minus_exp | recurring_signatures | consider_new_structure | external_precedence_candidate | recommendation |
|---|---|---|---|---|---|---|---|---|---|
| `AGR-0001` | `MECH-058` | `candidate` | 0.957 | 0.333 | 0.308 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0002` | `MECH-060` | `candidate` | 0.931 | 0.429 | 0.328 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0003` | `MECH-059` | `candidate` | 0.884 | 0.5 | 0.301 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0004` | `Q-017` | `active` | 0.75 | 0 | 0.275 | 2 | yes | yes | `consider_new_structure` |
| `AGR-0005` | `MECH-056` | `candidate` | 0.643 | 0 | 0.171 | 5 | no | yes | `monitor_and_collect_targeted_evidence` |
| `AGR-0006` | `Q-011` | `candidate` | 0.5 | 1 | 0.375 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0007` | `IMPL-022` | `stable` | 0 | 1 | 0.662 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0008` | `Q-013` | `active` | 0 | 1 | 0.662 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0009` | `Q-014` | `active` | 0 | 1 | 0.662 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0010` | `Q-016` | `active` | 0 | 0 | -0.167 | 1 | no | no | `monitor_and_collect_targeted_evidence` |

## Consider New Structure Queue

- `MECH-058` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.957; lit_non_support_ratio=0.333.
  - recurring_signatures: `mech058:anchor_separation_collapse`(12), `mech058:ema_drift_under_shift`(12), `mech058:latent_cluster_collapse`(10), `threshold:latent_prediction_error_mean`(5), `threshold:latent_prediction_error_p95`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.308
- `MECH-060` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.931; lit_non_support_ratio=0.429.
  - recurring_signatures: `mech060:postcommit_channel_contamination`(19), `mech060:attribution_reliability_break`(17), `mech060:precommit_channel_contamination`(10), `threshold:pre_commit_error_signal_to_noise`(5), `threshold:post_commit_error_attribution_gain`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.328
- `MECH-059` triggers=external_precedence_pressure, high_conflict_ratio, literature_non_support_pressure, recurring_failure_signatures; conflict_ratio=0.884; lit_non_support_ratio=0.5.
  - recurring_signatures: `mech059:uncertainty_metric_gaming_detected`(14), `mech059:calibration_slope_break`(10), `mech059:abstention_reliability_collapse`(6), `threshold:latent_prediction_error_mean`(5), `threshold:latent_uncertainty_calibration_error`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.301
- `Q-017` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.75; lit_non_support_ratio=0.
  - recurring_signatures: `q017:control_axis_stability_drop`(3), `q017:control_axis_entropy_collapse`(3)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.275
