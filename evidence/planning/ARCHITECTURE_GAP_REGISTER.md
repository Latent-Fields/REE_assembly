# Architecture Gap Register

Generated: `2026-02-14T20:53:08.829966Z`

This register highlights claims under structural pressure and flags where the evidence pattern suggests a **consider new structure** decision.

| gap_id | claim_id | status | conflict_ratio | lit_non_support_ratio | confidence_delta_lit_minus_exp | recurring_signatures | consider_new_structure | external_precedence_candidate | recommendation |
|---|---|---|---|---|---|---|---|---|---|
| `AGR-0001` | `MECH-058` | `candidate` | 0.923 | 0.333 | 0.296 | 3 | yes | yes | `consider_new_structure` |
| `AGR-0002` | `MECH-060` | `candidate` | 0.9 | 0.5 | 0.318 | 3 | yes | yes | `consider_new_structure` |
| `AGR-0003` | `MECH-059` | `candidate` | 0.833 | 0.5 | 0.281 | 3 | yes | yes | `consider_new_structure` |
| `AGR-0004` | `MECH-056` | `candidate` | 0.545 | 0 | 0.131 | 5 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0005` | `Q-011` | `candidate` | 0.5 | 1 | 0.374 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0006` | `IMPL-022` | `stable` | 0 | 1 | 0.662 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0007` | `Q-013` | `active` | 0 | 1 | 0.662 | 0 | no | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0008` | `Q-014` | `active` | 0 | 1 | 0.662 | 0 | no | no | `monitor_and_collect_targeted_evidence` |

## Consider New Structure Queue

- `MECH-058` triggers=external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures; conflict_ratio=0.923; lit_non_support_ratio=0.333.
  - recurring_signatures: `mech058:anchor_separation_collapse`(12), `mech058:ema_drift_under_shift`(12), `mech058:latent_cluster_collapse`(10)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.296
- `MECH-060` triggers=external_precedence_pressure, high_conflict_ratio, literature_non_support_pressure, recurring_failure_signatures; conflict_ratio=0.9; lit_non_support_ratio=0.5.
  - recurring_signatures: `mech060:postcommit_channel_contamination`(14), `mech060:attribution_reliability_break`(12), `mech060:precommit_channel_contamination`(10)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.318
- `MECH-059` triggers=external_precedence_pressure, high_conflict_ratio, literature_non_support_pressure, recurring_failure_signatures; conflict_ratio=0.833; lit_non_support_ratio=0.5.
  - recurring_signatures: `mech059:uncertainty_metric_gaming_detected`(14), `mech059:calibration_slope_break`(10), `mech059:abstention_reliability_collapse`(6)
  - external_precedence_candidate: yes; delta_lit_minus_exp=0.281
