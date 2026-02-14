# Architecture Gap Register

Generated: `2026-02-14T19:58:26.615968Z`

This register highlights claims under structural pressure and flags where the evidence pattern suggests a **consider new structure** decision.

| gap_id | claim_id | status | conflict_ratio | lit_non_support_ratio | recurring_signatures | consider_new_structure | recommendation |
|---|---|---|---|---|---|---|---|
| `AGR-0001` | `MECH-060` | `candidate` | 0.9 | 0.5 | 3 | yes | `consider_new_structure` |
| `AGR-0002` | `MECH-059` | `candidate` | 0.833 | 0.5 | 3 | yes | `consider_new_structure` |
| `AGR-0003` | `MECH-058` | `candidate` | 0.923 | 0.333 | 3 | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0004` | `MECH-056` | `candidate` | 0.545 | 0 | 5 | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0005` | `Q-011` | `candidate` | 0.5 | 1 | 0 | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0006` | `IMPL-022` | `stable` | 0 | 1 | 0 | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0007` | `Q-013` | `active` | 0 | 1 | 0 | no | `monitor_and_collect_targeted_evidence` |
| `AGR-0008` | `Q-014` | `active` | 0 | 1 | 0 | no | `monitor_and_collect_targeted_evidence` |

## Consider New Structure Queue

- `MECH-060` triggers=high_conflict_ratio, literature_non_support_pressure, recurring_failure_signatures; conflict_ratio=0.9; lit_non_support_ratio=0.5.
  - recurring_signatures: `mech060:postcommit_channel_contamination`(14), `mech060:attribution_reliability_break`(12), `mech060:precommit_channel_contamination`(10)
- `MECH-059` triggers=high_conflict_ratio, literature_non_support_pressure, recurring_failure_signatures; conflict_ratio=0.833; lit_non_support_ratio=0.5.
  - recurring_signatures: `mech059:uncertainty_metric_gaming_detected`(14), `mech059:calibration_slope_break`(10), `mech059:abstention_reliability_collapse`(6)
