# Architecture Gap Register

Generated: `2026-02-15T21:38:13.992121Z`

This register highlights claims under structural pressure and flags where the evidence pattern suggests a **consider new structure** decision.

| gap_id | claim_id | status | conflict_ratio | lit_non_support_ratio | confidence_delta_lit_minus_exp | recurring_signatures | consider_new_structure | external_precedence_candidate | recommendation |
|---|---|---|---|---|---|---|---|---|---|
| `AGR-0001` | `MECH-060` | `candidate` | 0.895 | 0.308 | 0.325 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0002` | `MECH-056` | `candidate` | 0.892 | 0.111 | 0.247 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0003` | `MECH-058` | `candidate` | 0.891 | 0.222 | 0.333 | 5 | yes | yes | `consider_new_structure` |
| `AGR-0004` | `ARC-003` | `active` | 0.889 | 0 | 0.191 | 3 | yes | yes | `consider_new_structure` |
| `AGR-0005` | `MECH-061` | `candidate` | 0.889 | 0 | 0.163 | 3 | yes | yes | `consider_new_structure` |
| `AGR-0006` | `Q-017` | `active` | 0.879 | 0.125 | 0.356 | 3 | yes | yes | `consider_new_structure` |
| `AGR-0007` | `MECH-040` | `provisional` | 0.8 | 0 | 0.28 | 2 | yes | yes | `consider_new_structure` |
| `AGR-0008` | `MECH-046` | `provisional` | 0.8 | 0 | 0.255 | 2 | yes | yes | `consider_new_structure` |
| `AGR-0009` | `Q-012` | `active` | 0.8 | 0.333 | 0.269 | 2 | yes | yes | `consider_new_structure` |
| `AGR-0010` | `Q-013` | `active` | 0.8 | 1 | 0.047 | 2 | yes | no | `consider_new_structure` |
| `AGR-0011` | `Q-014` | `active` | 0.8 | 1 | 0.047 | 2 | yes | no | `consider_new_structure` |
| `AGR-0012` | `Q-015` | `active` | 0.8 | 0 | 0.227 | 2 | yes | yes | `consider_new_structure` |
| `AGR-0013` | `MECH-057` | `candidate` | 0.769 | 0.429 | 0.274 | 2 | yes | yes | `consider_new_structure` |
| `AGR-0014` | `ARC-007` | `active` | 0.727 | 0 | 0.13 | 2 | yes | yes | `consider_new_structure` |
| `AGR-0015` | `ARC-018` | `provisional` | 0.714 | 0.167 | 0.279 | 2 | yes | yes | `consider_new_structure` |
| `AGR-0016` | `MECH-033` | `provisional` | 0.714 | 0.167 | 0.274 | 2 | yes | yes | `consider_new_structure` |
| `AGR-0017` | `Q-001` | `active` | 0.8 | 0 | -0.155 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0018` | `Q-002` | `active` | 0.8 | 0 | -0.155 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0019` | `Q-003` | `active` | 0.8 | 0 | -0.155 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0020` | `Q-004` | `active` | 0.8 | 0 | -0.155 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0021` | `Q-005` | `active` | 0.8 | 0 | -0.155 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0022` | `Q-006` | `active` | 0.8 | 0 | -0.155 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0023` | `Q-007` | `active` | 0.8 | 0 | -0.155 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0024` | `Q-008` | `active` | 0.8 | 0 | -0.155 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0025` | `Q-009` | `active` | 0.8 | 0 | -0.155 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0026` | `Q-010` | `legacy` | 0.8 | 0 | -0.155 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0027` | `MECH-059` | `candidate` | 0.588 | 0.333 | 0.164 | 5 | no | yes | `monitor_and_collect_targeted_evidence` |
| `AGR-0028` | `Q-011` | `provisional` | 0.333 | 1 | 0.483 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0029` | `IMPL-022` | `stable` | 0 | 1 | -0.163 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0030` | `Q-016` | `active` | 0 | 0 | -0.166 | 2 | no | no | `monitor_and_collect_targeted_evidence` |

## Consider New Structure Queue

- `MECH-060` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.895; lit_non_support_ratio=0.308.
  - recurring_signatures: `mech060:postcommit_channel_contamination`(40), `mech060:attribution_reliability_break`(38), `mech060:commitment_reversal_spike`(26), `mech060:precommit_channel_contamination`(10), `threshold:pre_commit_error_signal_to_noise`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.325
- `MECH-056` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.892; lit_non_support_ratio=0.111.
  - recurring_signatures: `stop:ledger_edit_detected_count>0`(46), `ledger_editing`(41), `stop:domination_lock_in_events>0`(38), `domination_lock_in`(32), `stop:explanation_policy_divergence_rate>0.05`(30)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.247
- `MECH-058` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.891; lit_non_support_ratio=0.222.
  - recurring_signatures: `mech058:anchor_separation_collapse`(33), `mech058:ema_drift_under_shift`(19), `mech058:latent_cluster_collapse`(10), `threshold:latent_prediction_error_mean`(5), `threshold:latent_prediction_error_p95`(5)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.333
- `ARC-003` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.889; lit_non_support_ratio=0.
  - recurring_signatures: `mech060:postcommit_channel_contamination`(4), `mech060:attribution_reliability_break`(4), `mech060:commitment_reversal_spike`(4)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.191
- `MECH-061` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.889; lit_non_support_ratio=0.
  - recurring_signatures: `mech060:postcommit_channel_contamination`(4), `mech060:attribution_reliability_break`(4), `mech060:commitment_reversal_spike`(4)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.163
- `Q-017` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.879; lit_non_support_ratio=0.125.
  - recurring_signatures: `q017:control_axis_stability_drop`(24), `q017:control_axis_entropy_collapse`(24), `q017:control_axis_policy_loss_spike`(16)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.356
- `MECH-040` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.8; lit_non_support_ratio=0.
  - recurring_signatures: `ledger_editing`(4), `domination_lock_in`(3)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.28
- `MECH-046` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.8; lit_non_support_ratio=0.
  - recurring_signatures: `ledger_editing`(4), `domination_lock_in`(3)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.255
- `Q-012` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.8; lit_non_support_ratio=0.333.
  - recurring_signatures: `ledger_editing`(4), `domination_lock_in`(3)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.269
- `Q-013` triggers=high_conflict_ratio, literature_non_support_pressure, recurring_failure_signatures; conflict_ratio=0.8; lit_non_support_ratio=1.
  - recurring_signatures: `ledger_editing`(4), `domination_lock_in`(3)
- `Q-014` triggers=high_conflict_ratio, literature_non_support_pressure, recurring_failure_signatures; conflict_ratio=0.8; lit_non_support_ratio=1.
  - recurring_signatures: `ledger_editing`(4), `domination_lock_in`(3)
- `Q-015` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.8; lit_non_support_ratio=0.
  - recurring_signatures: `ledger_editing`(4), `domination_lock_in`(3)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.227
- `MECH-057` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.769; lit_non_support_ratio=0.429.
  - recurring_signatures: `ledger_editing`(4), `domination_lock_in`(4)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.274
- `ARC-007` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.727; lit_non_support_ratio=0.
  - recurring_signatures: `ledger_editing`(4), `domination_lock_in`(3)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.13
- `ARC-018` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.714; lit_non_support_ratio=0.167.
  - recurring_signatures: `ledger_editing`(4), `domination_lock_in`(3)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.279
- `MECH-033` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.714; lit_non_support_ratio=0.167.
  - recurring_signatures: `ledger_editing`(4), `domination_lock_in`(3)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.274
