# REE-v2 Cutover Readiness Report

Generated: `2026-02-14T18:40:02.908150Z`

## Decision

- decision: `CUTOVER_DONE`
- routing_change_applied: `true`

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

- ree-v2 handoff: `/Users/dgolden/Documents/GitHub/ree-v2/evidence/planning/weekly_handoff/latest.md` @ `4ab69172f0c2` generated `2026-02-14T18:32:05Z`
- ree-v2 handoff: `/Users/dgolden/Documents/GitHub/ree-v2/evidence/planning/weekly_handoff/latest.md` @ `65d51ffa9c66` generated `2026-02-14T18:16:43Z`
- ree-v1-minimal handoff: `/Users/dgolden/Documents/GitHub/ree-v1-minimal/evidence/planning/weekly_handoff/latest.md` @ `6bcb466b273c` generated `2026-02-14T03:00:00Z`
- ree-v1-minimal handoff: `/Users/dgolden/Documents/GitHub/ree-v1-minimal/evidence/planning/weekly_handoff/latest.md` @ `a1cb5fee15a9` generated `2026-02-14T03:00:00Z`
- ree-experiments-lab handoff: `/Users/dgolden/Documents/GitHub/ree-experiments-lab/evidence/planning/weekly_handoff/latest.md` @ `451bb65d54d2` generated `2026-02-14T16:15:10.582563Z`
- ingestion report: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/handoff_sync_reports/20260214T161714Z_handoff_sync_report.json`
- ingestion report: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/handoff_sync_reports/20260214T160012Z_handoff_sync_report.json`

## Rollback Instructions

- Set `repo_routing.experimental_default_repo` to `ree-v1-minimal` in `evidence/planning/planning_criteria.v1.yaml`.
- Run `python3 evidence/experiments/scripts/build_experiment_indexes.py`.
- Run `python3 evidence/planning/scripts/run_governance_cycle.py`.
- Run `python3 evidence/planning/scripts/emit_weekly_dispatches.py`.
