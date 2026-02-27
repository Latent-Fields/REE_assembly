# Architecture Gap Register

Generated: `2026-02-27T12:20:14.545668Z`
Evidence scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

This register highlights claims under structural pressure and flags where the evidence pattern suggests a **consider new structure** decision.

| gap_id | claim_id | status | conflict_ratio | lit_non_support_ratio | confidence_delta_lit_minus_exp | recurring_signatures | consider_new_structure | external_precedence_candidate | recommendation |
|---|---|---|---|---|---|---|---|---|---|
| `AGR-0001` | `MECH-058` | `candidate` | 0.816 | 0.2 | 0.289 | 2 | yes | yes | `escalate_architecture_decision` |
| `AGR-0002` | `Q-017` | `active` | 0.808 | 0.2 | 0.288 | 3 | yes | yes | `escalate_architecture_decision` |
| `AGR-0003` | `MECH-060` | `provisional` | 0.8 | 0.2 | 0.271 | 3 | yes | yes | `escalate_architecture_decision` |
| `AGR-0004` | `ARC-003` | `active` | 1 | 0 | 0.147 | 3 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0005` | `MECH-057` | `candidate` | 1 | 0 | -0.521 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0006` | `Q-012` | `candidate` | 1 | 0 | -0.499 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0007` | `MECH-040` | `provisional` | 0.889 | 0 | -0.549 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0008` | `MECH-046` | `provisional` | 0.889 | 0 | -0.549 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0009` | `Q-015` | `active` | 0.889 | 0 | -0.549 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0010` | `ARC-018` | `provisional` | 0.8 | 0 | 0.163 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0011` | `MECH-061` | `active` | 0.8 | 0 | -0.611 | 3 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0012` | `MECH-033` | `provisional` | 0.727 | 0 | 0.123 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0013` | `Q-001` | `active` | 0.727 | 0 | -0.165 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0014` | `Q-002` | `active` | 0.727 | 0 | -0.165 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0015` | `Q-003` | `active` | 0.727 | 0 | -0.165 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0016` | `Q-004` | `active` | 0.727 | 0 | -0.165 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0017` | `Q-005` | `active` | 0.727 | 0 | -0.165 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0018` | `Q-006` | `active` | 0.727 | 0 | -0.165 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0019` | `ARC-007` | `active` | 0.667 | 0 | -0.649 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0020` | `Q-007` | `active` | 0.667 | 0 | -0.197 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0021` | `Q-013` | `active` | 0.615 | 0 | -0.694 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0022` | `Q-014` | `active` | 0.615 | 0 | -0.694 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0023` | `MECH-056` | `provisional` | 0.435 | 0 | -0.068 | 5 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0024` | `MECH-059` | `active` | 0.415 | 0 | -0.077 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0025` | `MECH-062` | `stable` | 0 | 0 | -0.955 | 2 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0026` | `Q-016` | `active` | 0 | 0 | -0.954 | 2 | no | no | `monitor_and_collect_targeted_evidence` |

## Consider New Structure Queue

- `MECH-058` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.816; lit_non_support_ratio=0.2.
  - recurring_signatures: `mech058:anchor_separation_collapse`(36), `mech058:ema_drift_under_shift`(10)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.289
  - escalation_required: yes; route directly to architecture decision checkpoint.
  - atomic_split_recommended: yes; split into narrower subclaims before broad reruns.
- `Q-017` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.808; lit_non_support_ratio=0.2.
  - recurring_signatures: `q017:control_axis_stability_drop`(36), `q017:control_axis_entropy_collapse`(36), `q017:control_axis_policy_loss_spike`(26)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.288
  - escalation_required: yes; route directly to architecture decision checkpoint.
  - atomic_split_recommended: yes; split into narrower subclaims before broad reruns.
- `MECH-060` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.8; lit_non_support_ratio=0.2.
  - recurring_signatures: `mech060:postcommit_channel_contamination`(36), `mech060:attribution_reliability_break`(36), `mech060:commitment_reversal_spike`(36)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.271
  - saturation_guard: engaged; recent_window_used=12, unique_signature_sets=2, unique_directions=2
  - escalation_required: yes; route directly to architecture decision checkpoint.
  - atomic_split_recommended: yes; split into narrower subclaims before broad reruns.
