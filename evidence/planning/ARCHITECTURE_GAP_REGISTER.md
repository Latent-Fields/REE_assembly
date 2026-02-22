# Architecture Gap Register

Generated: `2026-02-21T17:40:42.838182Z`

This register highlights claims under structural pressure and flags where the evidence pattern suggests a **consider new structure** decision.

| gap_id | claim_id | status | conflict_ratio | lit_non_support_ratio | confidence_delta_lit_minus_exp | recurring_signatures | consider_new_structure | external_precedence_candidate | recommendation |
|---|---|---|---|---|---|---|---|---|---|
| `AGR-0001` | `MECH-060` | `candidate` | 0.875 | 0.308 | 0.301 | 5 | yes | yes | `mandatory_decision_checkpoint` |
| `AGR-0002` | `MECH-058` | `candidate` | 0.871 | 0.222 | 0.311 | 5 | yes | yes | `mandatory_decision_checkpoint` |
| `AGR-0003` | `Q-017` | `active` | 0.848 | 0.125 | 0.316 | 3 | yes | yes | `escalate_architecture_decision` |
| `AGR-0004` | `MECH-057` | `candidate` | 0.769 | 0.429 | 0.285 | 2 | yes | yes | `consider_new_structure` |
| `AGR-0005` | `Q-013` | `active` | 0.727 | 1 | 0.026 | 2 | yes | no | `consider_new_structure` |
| `AGR-0006` | `Q-014` | `active` | 0.727 | 1 | 0.026 | 2 | yes | no | `consider_new_structure` |
| `AGR-0007` | `ARC-003` | `active` | 0.889 | 0 | 0.202 | 3 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0008` | `MECH-061` | `candidate` | 0.8 | 0 | 0.239 | 3 | no | no | `mandatory_decision_checkpoint` |
| `AGR-0009` | `Q-012` | `active` | 0.8 | 0.333 | 0.281 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0010` | `MECH-040` | `provisional` | 0.727 | 0 | 0.241 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0011` | `MECH-046` | `provisional` | 0.727 | 0 | 0.216 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0012` | `Q-001` | `active` | 0.727 | 0 | -0.177 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0013` | `Q-002` | `active` | 0.727 | 0 | -0.177 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0014` | `Q-003` | `active` | 0.727 | 0 | -0.177 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0015` | `Q-004` | `active` | 0.727 | 0 | -0.177 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0016` | `Q-005` | `active` | 0.727 | 0 | -0.177 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0017` | `Q-006` | `active` | 0.727 | 0 | -0.177 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0018` | `Q-015` | `active` | 0.727 | 0 | 0.189 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0019` | `ARC-018` | `provisional` | 0.667 | 0.167 | 0.24 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0020` | `Q-007` | `active` | 0.667 | 0 | -0.209 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0021` | `MECH-056` | `candidate` | 0.648 | 0.111 | 0.154 | 5 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0022` | `MECH-033` | `provisional` | 0.625 | 0.167 | 0.195 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0023` | `ARC-007` | `active` | 0.615 | 0 | 0.081 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0024` | `MECH-059` | `candidate` | 0.566 | 0.333 | 0.147 | 5 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0025` | `IMPL-022` | `stable` | 0 | 1 | -0.151 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0026` | `MECH-062` | `provisional` | 0 | 0 | -0.17 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0027` | `Q-016` | `active` | 0 | 0 | -0.169 | 2 | no | no | `monitor_and_collect_targeted_evidence` |

## Consider New Structure Queue

- `MECH-060` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.875; lit_non_support_ratio=0.308.
  - recurring_signatures: `mech060:postcommit_channel_contamination`(64), `mech060:attribution_reliability_break`(62), `mech060:commitment_reversal_spike`(50), `mech060:precommit_channel_contamination`(10), `threshold:pre_commit_error_signal_to_noise`(7)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.301
  - escalation_required: yes; route directly to architecture decision checkpoint.
  - mandatory_decision_checkpoint: yes; deadline=2026-02-24T17:40:42.838182Z; required_outcomes=retain_ree|hybridize|adopt_jepa_structure|retire_ree_claim
  - atomic_split_recommended: yes; split into narrower subclaims before broad reruns.
- `MECH-058` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.871; lit_non_support_ratio=0.222.
  - recurring_signatures: `mech058:anchor_separation_collapse`(57), `mech058:ema_drift_under_shift`(25), `mech058:latent_cluster_collapse`(10), `threshold:latent_prediction_error_mean`(7), `threshold:latent_prediction_error_p95`(7)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.311
  - escalation_required: yes; route directly to architecture decision checkpoint.
  - mandatory_decision_checkpoint: yes; deadline=2026-02-24T17:40:42.838182Z; required_outcomes=retain_ree|hybridize|adopt_jepa_structure|retire_ree_claim
  - atomic_split_recommended: yes; split into narrower subclaims before broad reruns.
- `Q-017` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.848; lit_non_support_ratio=0.125.
  - recurring_signatures: `q017:control_axis_stability_drop`(48), `q017:control_axis_entropy_collapse`(48), `q017:control_axis_policy_loss_spike`(34)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.316
  - escalation_required: yes; route directly to architecture decision checkpoint.
  - atomic_split_recommended: yes; split into narrower subclaims before broad reruns.
- `MECH-057` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.769; lit_non_support_ratio=0.429.
  - recurring_signatures: `ledger_editing`(4), `domination_lock_in`(4)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.285
  - atomic_split_recommended: yes; split into narrower subclaims before broad reruns.
- `Q-013` triggers=high_conflict_ratio, literature_non_support_pressure, recurring_failure_signatures; conflict_ratio=0.727; lit_non_support_ratio=1.
  - recurring_signatures: `ledger_editing`(4), `domination_lock_in`(3)
  - atomic_split_recommended: yes; split into narrower subclaims before broad reruns.
- `Q-014` triggers=high_conflict_ratio, literature_non_support_pressure, recurring_failure_signatures; conflict_ratio=0.727; lit_non_support_ratio=1.
  - recurring_signatures: `ledger_editing`(4), `domination_lock_in`(3)
  - atomic_split_recommended: yes; split into narrower subclaims before broad reruns.
