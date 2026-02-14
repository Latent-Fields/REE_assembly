# REE-v2 Cutover Readiness Report

Generated: `2026-02-14T18:26:37.999925Z`

## Decision

- decision: `NO_CUTOVER`
- routing_change_applied: `False`

## Gate Results

| gate_id | status |
| --- | --- |
| `v2_ci_gates_all_pass` | `PASS` |
| `v2_required_claim_coverage` | `PASS` |
| `no_unresolved_contract_drift_signatures` | `PASS` |
| `no_p0_blocker_text_in_latest_v2_handoff` | `PASS` |
| `overlap_sanity_direction_conflicts_resolved` | `FAIL` |

## Blockers (Prioritized)

### P0 - Unresolved overlap direction conflicts between ree-v2 and ree-v1-minimal for MECH-056/058/059/060.

Evidence:
- `[{"claim_id": "MECH-056", "ree_v2_direction": "supports", "ree_v1_direction": "mixed", "delta": "different", "unresolved_conflict": true}, {"claim_id": "MECH-058", "ree_v2_direction": "supports", "ree_v1_direction": "mixed", "delta": "different", "unresolved_conflict": true}, {"claim_id": "MECH-059", "ree_v2_direction": "supports", "ree_v1_direction": "mixed", "delta": "different", "unresolved_conflict": true}, {"claim_id": "MECH-060", "ree_v2_direction": "supports", "ree_v1_direction": "mixed", "delta": "different", "unresolved_conflict": true}]`
Remediation actions:
- Run a matched-seed, matched-condition parity cycle in both repos for MECH-056/058/059/060 (minimum 3 seeds per condition) and publish side-by-side delta table in weekly handoffs.
- Require two consecutive Thursday governance cycles where overlap deltas are resolved (or explicitly adjudicated) before cutover.
- If conflicts remain, dispatch targeted falsification to ree-experiments-lab and withhold routing flip.

## Overlap Direction Deltas (ree-v2 vs ree-v1-minimal)

| claim_id | ree_v2_direction | ree_v1_direction | delta | unresolved_conflict |
| --- | --- | --- | --- | --- |
| `MECH-056` | `supports` | `mixed` | `different` | `true` |
| `MECH-058` | `supports` | `mixed` | `different` | `true` |
| `MECH-059` | `supports` | `mixed` | `different` | `true` |
| `MECH-060` | `supports` | `mixed` | `different` | `true` |

## Input Snapshots Used

- ree-v2 handoff: `/Users/dgolden/Documents/GitHub/ree-v2/evidence/planning/weekly_handoff/latest.md` @ `65d51ffa9c66` generated `2026-02-14T18:16:43Z`
- ree-v2 handoff: `/Users/dgolden/Documents/GitHub/ree-v2/evidence/planning/weekly_handoff/latest.md` @ `9162187427ba` generated `2026-02-14T17:37:56Z`
- ree-v1-minimal handoff: `/Users/dgolden/Documents/GitHub/ree-v1-minimal/evidence/planning/weekly_handoff/latest.md` @ `6bcb466b273c` generated `2026-02-14T03:00:00Z`
- ree-v1-minimal handoff: `/Users/dgolden/Documents/GitHub/ree-v1-minimal/evidence/planning/weekly_handoff/latest.md` @ `a1cb5fee15a9` generated `2026-02-14T03:00:00Z`
- ingestion report: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/handoff_sync_reports/20260214T161714Z_handoff_sync_report.json`
- ingestion report: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/handoff_sync_reports/20260214T160012Z_handoff_sync_report.json`

## Rollback Instructions

- No routing change was applied in this decision path.
- If routing is flipped later and rollback is needed: set repo_routing.experimental_default_repo back to ree-v1-minimal in evidence/planning/planning_criteria.v1.yaml and regenerate planning outputs.

## Additional Risks

- `P1` Latest ree-v2 handoff still lists operational blocker text. (note: Not all blocker text is tagged P0, but unresolved operational blockers increase cutover risk.)
- `P1` At least one of the two latest ingestion-cycle reports contains repo-level sync errors. (note: Most recent report is healthy, but prior cycle instability should be monitored.)
