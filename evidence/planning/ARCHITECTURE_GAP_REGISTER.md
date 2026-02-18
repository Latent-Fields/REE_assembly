# Architecture Gap Register

Generated: `2026-02-18T19:44:26.545366Z`

This register highlights claims under structural pressure and flags where the evidence pattern suggests a **consider new structure** decision.

| gap_id | claim_id | status | conflict_ratio | lit_non_support_ratio | confidence_delta_lit_minus_exp | recurring_signatures | consider_new_structure | external_precedence_candidate | recommendation |
|---|---|---|---|---|---|---|---|---|---|
| `AGR-0001` | `MECH-060` | `candidate` | 0.875 | 0.308 | 0.309 | 5 | yes | yes | `escalate_architecture_decision` |
| `AGR-0002` | `MECH-058` | `candidate` | 0.87 | 0.222 | 0.317 | 5 | yes | yes | `escalate_architecture_decision` |
| `AGR-0003` | `Q-017` | `active` | 0.845 | 0.125 | 0.325 | 3 | yes | yes | `escalate_architecture_decision` |
| `AGR-0004` | `MECH-057` | `candidate` | 0.769 | 0.429 | 0.279 | 2 | yes | yes | `consider_new_structure` |
| `AGR-0005` | `Q-013` | `active` | 0.727 | 1 | 0.02 | 2 | yes | no | `consider_new_structure` |
| `AGR-0006` | `Q-014` | `active` | 0.727 | 1 | 0.02 | 2 | yes | no | `consider_new_structure` |
| `AGR-0007` | `MECH-056` | `candidate` | 0.726 | 0.111 | 0.182 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0008` | `ARC-003` | `active` | 0.889 | 0 | 0.196 | 3 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0009` | `MECH-061` | `candidate` | 0.8 | 0 | 0.233 | 3 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0010` | `Q-012` | `active` | 0.8 | 0.333 | 0.275 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0011` | `MECH-040` | `provisional` | 0.727 | 0 | 0.235 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0012` | `MECH-046` | `provisional` | 0.727 | 0 | 0.21 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0013` | `Q-001` | `active` | 0.727 | 0 | -0.182 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0014` | `Q-002` | `active` | 0.727 | 0 | -0.182 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0015` | `Q-003` | `active` | 0.727 | 0 | -0.182 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0016` | `Q-004` | `active` | 0.727 | 0 | -0.182 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0017` | `Q-005` | `active` | 0.727 | 0 | -0.182 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0018` | `Q-006` | `active` | 0.727 | 0 | -0.182 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0019` | `Q-015` | `active` | 0.727 | 0 | 0.183 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0020` | `ARC-018` | `provisional` | 0.667 | 0.167 | 0.234 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0021` | `Q-007` | `active` | 0.667 | 0 | -0.214 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0022` | `MECH-033` | `provisional` | 0.625 | 0.167 | 0.189 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0023` | `ARC-007` | `active` | 0.615 | 0 | 0.075 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0024` | `MECH-059` | `candidate` | 0.605 | 0.333 | 0.169 | 5 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0025` | `IMPL-022` | `stable` | 0 | 1 | -0.157 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0026` | `MECH-062` | `provisional` | 0 | 0 | -0.168 | 1 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0027` | `Q-016` | `active` | 0 | 0 | -0.166 | 2 | no | no | `monitor_and_collect_targeted_evidence` |

## Consider New Structure Queue

- `MECH-060` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.875; lit_non_support_ratio=0.308.
  - recurring_signatures: `mech060:postcommit_channel_contamination`(52), `mech060:attribution_reliability_break`(50), `mech060:commitment_reversal_spike`(38), `mech060:precommit_channel_contamination`(10), `threshold:pre_commit_error_signal_to_noise`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.309
  - saturation_guard: engaged; recent_window_used=12, unique_signature_sets=2, unique_directions=2
  - escalation_required: yes; route directly to architecture decision checkpoint.
- `MECH-058` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.87; lit_non_support_ratio=0.222.
  - recurring_signatures: `mech058:anchor_separation_collapse`(45), `mech058:ema_drift_under_shift`(21), `mech058:latent_cluster_collapse`(10), `threshold:latent_prediction_error_mean`(5), `threshold:latent_prediction_error_p95`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.317
  - saturation_guard: engaged; recent_window_used=12, unique_signature_sets=2, unique_directions=2
  - escalation_required: yes; route directly to architecture decision checkpoint.
- `Q-017` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.845; lit_non_support_ratio=0.125.
  - recurring_signatures: `q017:control_axis_stability_drop`(36), `q017:control_axis_entropy_collapse`(36), `q017:control_axis_policy_loss_spike`(26)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.325
  - saturation_guard: engaged; recent_window_used=12, unique_signature_sets=2, unique_directions=2
  - escalation_required: yes; route directly to architecture decision checkpoint.
- `MECH-057` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.769; lit_non_support_ratio=0.429.
  - recurring_signatures: `ledger_editing`(4), `domination_lock_in`(4)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.279
- `Q-013` triggers=high_conflict_ratio, literature_non_support_pressure, recurring_failure_signatures; conflict_ratio=0.727; lit_non_support_ratio=1.
  - recurring_signatures: `ledger_editing`(4), `domination_lock_in`(3)
- `Q-014` triggers=high_conflict_ratio, literature_non_support_pressure, recurring_failure_signatures; conflict_ratio=0.727; lit_non_support_ratio=1.
  - recurring_signatures: `ledger_editing`(4), `domination_lock_in`(3)
- `MECH-056` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.726; lit_non_support_ratio=0.111.
  - recurring_signatures: `ledger_editing`(67), `stop:ledger_edit_detected_count>0`(59), `domination_lock_in`(48), `stop:domination_lock_in_events>0`(46), `explanation_policy_divergence`(37)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.182
