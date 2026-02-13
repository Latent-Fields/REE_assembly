# Governance Agenda

Generated: `2026-02-13T15:32:39.703236Z`

## Cycle Status

| step | status | command |
|---|---|---|
| `evidence_build` | `ok` | `/opt/local/bin/python3 evidence/experiments/scripts/build_experiment_indexes.py` |
| `architecture_trace_audit` | `ok` | `/opt/local/bin/python3 evidence/planning/scripts/architecture_trace_audit.py` |

## Discussion Checkpoints

1. Thought Intake: 0 unprocessed thought(s).
2. Conflict Resolution: 2 conflict item(s).
- `MECH-056` conflict_types=directional
- `Q-011` conflict_types=directional, mixed_evidence
3. Governance Decisions: 2 recommendation queue item(s).
- `MECH-056` decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `Q-011` decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
4. Evidence Dispatch: 4 high-priority proposal(s), 26 total.
- REE_assembly: total=14, experimental=0, literature_review=14
- ree-experiments-lab: total=2, experimental=2, literature_review=0
- ree-v1-minimal: total=10, experimental=10, literature_review=0
5. Experiment Understanding: 2 high-priority experimental brief(s) in `evidence/planning/EXPERIMENT_BRIEFS.md`.
6. Environment Qualification: declared_runs=10, qualified_runs=0, drift_alerts=0 (`evidence/experiments/environment_drift.md`).
7. Architecture Trace: issues=25, unowned_edges=1, trace_breaks=1, suggested_stubs=6 (`evidence/planning/ARCHITECTURE_TRACE_AUDIT.md`).
- `ISS-UNOWNED-EDGE-IFACE-EDGE-022` [unowned_edges]
- `ISS-TRACE-BREAK-SOCIAL-OTHER_MODEL` [trace_breaks]
- `ISS-OPEN-UNOWNED-OPEN-003` [open_sections_unowned]
- `ISS-DEP-LINK-GAP-IFACE-EDGE-001` [dependency_link_gaps]
- `ISS-DEP-LINK-GAP-IFACE-EDGE-002` [dependency_link_gaps]
- `ISS-DEP-LINK-GAP-IFACE-EDGE-003` [dependency_link_gaps]
- `ISS-DEP-LINK-GAP-IFACE-EDGE-004` [dependency_link_gaps]
- `ISS-DEP-LINK-GAP-IFACE-EDGE-020` [dependency_link_gaps]
- `ISS-DEP-LINK-GAP-IFACE-EDGE-022` [dependency_link_gaps]
8. Maintenance: 0 unlinked evidence run(s), 0 warning(s).
