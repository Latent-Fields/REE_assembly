# REE-v2 Cutover Readiness Report

Generated: `2026-02-15T11:20:50.536340Z`

## Decision

- decision: `NO_CUTOVER`
- routing_change_applied: `false`

## Gate Results

| gate_id | status |
| --- | --- |
| `v2_ci_gates_all_pass` | `PASS` |
| `v2_required_claim_coverage` | `PASS` |
| `no_unresolved_contract_drift_signatures` | `PASS` |
| `no_p0_blocker_text_in_latest_v2_handoff` | `PASS` |
| `overlap_sanity_adjudicated_or_resolved` | `PASS` |

## Overlap Adjudication

| claim_id | ree_v2_direction | ree_v1_direction | status |
| --- | --- | --- | --- |
| `MECH-056` | `mixed` | `mixed` | `resolved` |
| `MECH-058` | `mixed` | `mixed` | `resolved` |
| `MECH-059` | `mixed` | `mixed` | `resolved` |
| `MECH-060` | `mixed` | `mixed` | `resolved` |

## Blockers (Prioritized)

- none
## Input Snapshots Used

- ree-v2 handoff: `/Users/dgolden/Documents/GitHub/ree-v2/evidence/planning/weekly_handoff/latest.md` @ `03c825ddeb98` generated `2026-02-15T08:36:04Z`
- ree-v2 handoff: `/Users/dgolden/Documents/GitHub/ree-v2/evidence/planning/weekly_handoff/latest.md` @ `4ab69172f0c2` generated `2026-02-14T18:32:05Z`
- ree-v1-minimal handoff: `/Users/dgolden/Documents/GitHub/ree-v1-minimal/evidence/planning/weekly_handoff/latest.md` @ `4c16ed05f596` generated `2026-02-14T20:00:00Z`
- ree-v1-minimal handoff: `/Users/dgolden/Documents/GitHub/ree-v1-minimal/evidence/planning/weekly_handoff/latest.md` @ `0a964c6b3484` generated `2026-02-14T03:00:00Z`
- ree-experiments-lab handoff: `/Users/dgolden/Documents/GitHub/ree-experiments-lab/evidence/planning/weekly_handoff/latest.md` @ `b3478d565a35` generated `2026-02-15T09:56:11.530965Z`
- ingestion report: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/handoff_sync_reports/20260215T112045Z_handoff_sync_report.json`
- ingestion report: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/handoff_sync_reports/20260215T111152Z_handoff_sync_report.json`

## Rollback Instructions

- If routing is flipped and rollback is needed: set `repo_routing.experimental_default_repo` back to `ree-v1-minimal` in `evidence/planning/planning_criteria.v1.yaml`, then regenerate planning outputs.
