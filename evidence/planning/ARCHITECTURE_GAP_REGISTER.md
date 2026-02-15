# Architecture Gap Register

Generated: `2026-02-15T15:37:22.224857Z`

This register highlights claims under structural pressure and flags where the evidence pattern suggests a **consider new structure** decision.

| gap_id | claim_id | status | conflict_ratio | lit_non_support_ratio | confidence_delta_lit_minus_exp | recurring_signatures | consider_new_structure | external_precedence_candidate | recommendation |
|---|---|---|---|---|---|---|---|---|---|
| `AGR-0001` | `MECH-056` | `candidate` | 0.966 | 0.111 | 0.259 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0002` | `MECH-058` | `candidate` | 0.959 | 0.2 | 0.354 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0003` | `MECH-060` | `candidate` | 0.953 | 0.333 | 0.325 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0004` | `Q-017` | `active` | 0.944 | 0 | 0.345 | 3 | yes | yes | `consider_new_structure` |
| `AGR-0005` | `MECH-059` | `candidate` | 0.69 | 0.333 | 0.213 | 5 | no | yes | `monitor_and_collect_targeted_evidence` |
| `AGR-0006` | `Q-011` | `candidate` | 0.333 | 1 | 0.482 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0007` | `IMPL-022` | `stable` | 0 | 1 | 0.662 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0008` | `Q-013` | `active` | 0 | 1 | 0.662 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0009` | `Q-014` | `active` | 0 | 1 | 0.662 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0010` | `Q-016` | `active` | 0 | 0 | -0.167 | 2 | no | no | `monitor_and_collect_targeted_evidence` |

## Consider New Structure Queue

- `MECH-056` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.966; lit_non_support_ratio=0.111.
  - recurring_signatures: `stop:ledger_edit_detected_count>0`(31), `ledger_editing`(26), `stop:domination_lock_in_events>0`(26), `stop:explanation_policy_divergence_rate>0.05`(21), `domination_lock_in`(20)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.259
- `MECH-058` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.959; lit_non_support_ratio=0.2.
  - recurring_signatures: `mech058:anchor_separation_collapse`(24), `mech058:ema_drift_under_shift`(16), `mech058:latent_cluster_collapse`(10), `threshold:latent_prediction_error_mean`(5), `threshold:latent_prediction_error_p95`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.354
- `MECH-060` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.953; lit_non_support_ratio=0.333.
  - recurring_signatures: `mech060:postcommit_channel_contamination`(31), `mech060:attribution_reliability_break`(29), `mech060:commitment_reversal_spike`(17), `mech060:precommit_channel_contamination`(10), `threshold:pre_commit_error_signal_to_noise`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.325
- `Q-017` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.944; lit_non_support_ratio=0.
  - recurring_signatures: `q017:control_axis_stability_drop`(15), `q017:control_axis_entropy_collapse`(15), `q017:control_axis_policy_loss_spike`(10)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.345
