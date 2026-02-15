# Architecture Gap Register

Generated: `2026-02-15T19:47:52.735849Z`

This register highlights claims under structural pressure and flags where the evidence pattern suggests a **consider new structure** decision.

| gap_id | claim_id | status | conflict_ratio | lit_non_support_ratio | confidence_delta_lit_minus_exp | recurring_signatures | consider_new_structure | external_precedence_candidate | recommendation |
|---|---|---|---|---|---|---|---|---|---|
| `AGR-0001` | `Q-017` | `active` | 0.967 | 0 | 0.357 | 3 | yes | yes | `consider_new_structure` |
| `AGR-0002` | `MECH-058` | `candidate` | 0.947 | 0.2 | 0.356 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0003` | `MECH-060` | `candidate` | 0.944 | 0.333 | 0.336 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0004` | `ARC-007` | `active` | 0.857 | 0 | 0.22 | 2 | yes | yes | `consider_new_structure` |
| `AGR-0005` | `MECH-056` | `candidate` | 0.85 | 0.111 | 0.224 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0006` | `ARC-003` | `active` | 0.667 | 0 | 0.305 | 0 | no | yes | `monitor_and_collect_targeted_evidence` |
| `AGR-0007` | `MECH-040` | `provisional` | 0.667 | 0 | 0.33 | 0 | no | yes | `monitor_and_collect_targeted_evidence` |
| `AGR-0008` | `MECH-046` | `provisional` | 0.667 | 0 | 0.305 | 0 | no | yes | `monitor_and_collect_targeted_evidence` |
| `AGR-0009` | `MECH-061` | `candidate` | 0.667 | 0 | 0.277 | 0 | no | yes | `monitor_and_collect_targeted_evidence` |
| `AGR-0010` | `Q-012` | `active` | 0.667 | 0.333 | 0.319 | 0 | no | yes | `monitor_and_collect_targeted_evidence` |
| `AGR-0011` | `Q-013` | `active` | 0.667 | 1 | -0.013 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0012` | `Q-014` | `active` | 0.667 | 1 | -0.013 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0013` | `Q-015` | `active` | 0.667 | 0 | 0.277 | 0 | no | yes | `monitor_and_collect_targeted_evidence` |
| `AGR-0014` | `ARC-018` | `provisional` | 0.6 | 0.167 | 0.329 | 0 | no | yes | `monitor_and_collect_targeted_evidence` |
| `AGR-0015` | `MECH-033` | `provisional` | 0.6 | 0.167 | 0.324 | 0 | no | yes | `monitor_and_collect_targeted_evidence` |
| `AGR-0016` | `MECH-059` | `candidate` | 0.588 | 0.333 | 0.163 | 5 | no | yes | `monitor_and_collect_targeted_evidence` |
| `AGR-0017` | `Q-011` | `candidate` | 0.333 | 1 | 0.483 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0018` | `IMPL-022` | `stable` | 0 | 1 | -0.163 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0019` | `Q-016` | `active` | 0 | 0 | -0.166 | 2 | no | no | `monitor_and_collect_targeted_evidence` |

## Consider New Structure Queue

- `Q-017` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.967; lit_non_support_ratio=0.
  - recurring_signatures: `q017:control_axis_stability_drop`(24), `q017:control_axis_entropy_collapse`(24), `q017:control_axis_policy_loss_spike`(16)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.357
- `MECH-058` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.947; lit_non_support_ratio=0.2.
  - recurring_signatures: `mech058:anchor_separation_collapse`(33), `mech058:ema_drift_under_shift`(19), `mech058:latent_cluster_collapse`(10), `threshold:latent_prediction_error_mean`(5), `threshold:latent_prediction_error_p95`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.356
- `MECH-060` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.944; lit_non_support_ratio=0.333.
  - recurring_signatures: `mech060:postcommit_channel_contamination`(40), `mech060:attribution_reliability_break`(38), `mech060:commitment_reversal_spike`(26), `mech060:precommit_channel_contamination`(10), `threshold:pre_commit_error_signal_to_noise`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.336
- `ARC-007` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.857; lit_non_support_ratio=0.
  - recurring_signatures: `ledger_editing`(3), `domination_lock_in`(3)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.22
- `MECH-056` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.85; lit_non_support_ratio=0.111.
  - recurring_signatures: `stop:ledger_edit_detected_count>0`(46), `ledger_editing`(41), `stop:domination_lock_in_events>0`(38), `domination_lock_in`(32), `stop:explanation_policy_divergence_rate>0.05`(30)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.224
