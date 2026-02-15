# Architecture Gap Register

Generated: `2026-02-15T08:42:36.287414Z`

This register highlights claims under structural pressure and flags where the evidence pattern suggests a **consider new structure** decision.

| gap_id | claim_id | status | conflict_ratio | lit_non_support_ratio | confidence_delta_lit_minus_exp | recurring_signatures | consider_new_structure | external_precedence_candidate | recommendation |
|---|---|---|---|---|---|---|---|---|---|
| `AGR-0001` | `MECH-058` | `candidate` | 0.933 | 0.333 | 0.299 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0002` | `MECH-060` | `candidate` | 0.913 | 0.5 | 0.321 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0003` | `MECH-059` | `candidate` | 0.857 | 0.5 | 0.289 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0004` | `MECH-056` | `candidate` | 0.643 | 0 | 0.171 | 5 | no | yes | `monitor_and_collect_targeted_evidence` |
| `AGR-0005` | `Q-011` | `candidate` | 0.5 | 1 | 0.375 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0006` | `IMPL-022` | `stable` | 0 | 1 | 0.662 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0007` | `Q-013` | `active` | 0 | 1 | 0.662 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0008` | `Q-014` | `active` | 0 | 1 | 0.662 | 0 | no | no | `monitor_and_collect_targeted_evidence` |

## Consider New Structure Queue

- `MECH-058` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.933; lit_non_support_ratio=0.333.
  - recurring_signatures: `mech058:anchor_separation_collapse`(12), `mech058:ema_drift_under_shift`(12), `mech058:latent_cluster_collapse`(10), `threshold:latent_prediction_error_mean`(5), `threshold:latent_prediction_error_p95`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.299
- `MECH-060` triggers=external_precedence_pressure, high_conflict_ratio, literature_non_support_pressure, recurring_failure_signatures; conflict_ratio=0.913; lit_non_support_ratio=0.5.
  - recurring_signatures: `mech060:postcommit_channel_contamination`(14), `mech060:attribution_reliability_break`(12), `mech060:precommit_channel_contamination`(10), `threshold:pre_commit_error_signal_to_noise`(5), `threshold:post_commit_error_attribution_gain`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.321
- `MECH-059` triggers=external_precedence_pressure, high_conflict_ratio, literature_non_support_pressure, recurring_failure_signatures; conflict_ratio=0.857; lit_non_support_ratio=0.5.
  - recurring_signatures: `mech059:uncertainty_metric_gaming_detected`(14), `mech059:calibration_slope_break`(10), `mech059:abstention_reliability_collapse`(6), `threshold:latent_prediction_error_mean`(5), `threshold:latent_uncertainty_calibration_error`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.289
