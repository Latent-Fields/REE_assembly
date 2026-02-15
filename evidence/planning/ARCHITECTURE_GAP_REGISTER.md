# Architecture Gap Register

Generated: `2026-02-15T15:32:10.207390Z`

This register highlights claims under structural pressure and flags where the evidence pattern suggests a **consider new structure** decision.

| gap_id | claim_id | status | conflict_ratio | lit_non_support_ratio | confidence_delta_lit_minus_exp | recurring_signatures | consider_new_structure | external_precedence_candidate | recommendation |
|---|---|---|---|---|---|---|---|---|---|
| `AGR-0001` | `MECH-056` | `candidate` | 0.941 | 0.111 | 0.297 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0002` | `MECH-058` | `candidate` | 0.939 | 0.2 | 0.361 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0003` | `MECH-060` | `candidate` | 0.937 | 0.333 | 0.33 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0004` | `Q-017` | `active` | 0.897 | 0 | 0.355 | 3 | yes | yes | `consider_new_structure` |
| `AGR-0005` | `MECH-059` | `candidate` | 0.704 | 0.333 | 0.221 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0006` | `Q-011` | `candidate` | 0.333 | 1 | 0.482 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0007` | `IMPL-022` | `stable` | 0 | 1 | 0.662 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0008` | `Q-013` | `active` | 0 | 1 | 0.662 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0009` | `Q-014` | `active` | 0 | 1 | 0.662 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0010` | `Q-016` | `active` | 0 | 0 | -0.167 | 2 | no | no | `monitor_and_collect_targeted_evidence` |

## Consider New Structure Queue

- `MECH-056` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.941; lit_non_support_ratio=0.111.
  - recurring_signatures: `stop:ledger_edit_detected_count>0`(26), `stop:domination_lock_in_events>0`(22), `ledger_editing`(21), `stop:explanation_policy_divergence_rate>0.05`(18), `domination_lock_in`(16)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.297
- `MECH-058` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.939; lit_non_support_ratio=0.2.
  - recurring_signatures: `mech058:anchor_separation_collapse`(21), `mech058:ema_drift_under_shift`(15), `mech058:latent_cluster_collapse`(10), `threshold:latent_prediction_error_mean`(5), `threshold:latent_prediction_error_p95`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.361
- `MECH-060` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.937; lit_non_support_ratio=0.333.
  - recurring_signatures: `mech060:postcommit_channel_contamination`(28), `mech060:attribution_reliability_break`(26), `mech060:commitment_reversal_spike`(14), `mech060:precommit_channel_contamination`(10), `threshold:pre_commit_error_signal_to_noise`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.33
- `Q-017` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.897; lit_non_support_ratio=0.
  - recurring_signatures: `q017:control_axis_stability_drop`(12), `q017:control_axis_entropy_collapse`(12), `q017:control_axis_policy_loss_spike`(8)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.355
- `MECH-059` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.704; lit_non_support_ratio=0.333.
  - recurring_signatures: `mech059:uncertainty_metric_gaming_detected`(20), `mech059:abstention_reliability_collapse`(12), `mech059:calibration_slope_break`(10), `threshold:latent_prediction_error_mean`(5), `threshold:latent_uncertainty_calibration_error`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.221
