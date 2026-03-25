# REE-v2 Cutover Readiness Report

Generated: `2026-03-25T05:20:48.001577Z`

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

- ree-v2 handoff: `/Users/dgolden/Documents/GitHub/REE_Working/ree-v2/evidence/planning/weekly_handoff/latest.md` @ `a5aa2724cb13` generated `2026-02-25T17:15:21Z`
- ree-v2 handoff: `/Users/dgolden/Documents/GitHub/REE_Working/ree-v2/evidence/planning/weekly_handoff/latest.md` @ `e9a1d98566a0` generated `2026-02-22T20:55:30Z`
- ree-v1-minimal handoff: `/Users/dgolden/Documents/GitHub/REE_Working/ree-v1-minimal/evidence/planning/weekly_handoff/latest.md` @ `a8ddcfd4d5af` generated `2026-02-21T15:12:23Z`
- ree-v1-minimal handoff: `/Users/dgolden/Documents/GitHub/REE_Working/ree-v1-minimal/evidence/planning/weekly_handoff/latest.md` @ `9a7fac5385c6` generated `2026-02-21T15:12:23Z`
- ree-experiments-lab handoff: `/Users/dgolden/Documents/GitHub/REE_Working/ree-experiments-lab/evidence/planning/weekly_handoff/latest.md` @ `b82d3b301369` generated `2026-02-25T19:18:52.980871Z`
- ingestion report: `/Users/dgolden/Documents/GitHub/REE_Working/REE_assembly/evidence/planning/handoff_sync_reports/20260225T195113Z_handoff_sync_report.json`
- ingestion report: `/Users/dgolden/Documents/GitHub/REE_Working/REE_assembly/evidence/planning/handoff_sync_reports/20260225T185910Z_handoff_sync_report.json`

## Rollback Instructions

- If routing is flipped and rollback is needed: set `repo_routing.experimental_default_repo` back to `ree-v1-minimal` in `evidence/planning/planning_criteria.v1.yaml`, then regenerate planning outputs.
