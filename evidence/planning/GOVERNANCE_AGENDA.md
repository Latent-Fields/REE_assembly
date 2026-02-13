# Governance Agenda

Generated: `2026-02-13T16:34:49.736081Z`

## Cycle Status

| step | status | command |
|---|---|---|
| `thought_sweep` | `ok` | `/opt/local/bin/python3 docs/thoughts/scripts/thought_sweep.py` |
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
4. Evidence Dispatch: 4 high-priority proposal(s), 28 total.
- REE_assembly: total=15, experimental=0, literature_review=15
- ree-experiments-lab: total=1, experimental=1, literature_review=0
- ree-v1-minimal: total=12, experimental=12, literature_review=0
5. Experiment Understanding: 2 high-priority experimental brief(s) in `evidence/planning/EXPERIMENT_BRIEFS.md`.
6. Environment Qualification: declared_runs=14, qualified_runs=0, drift_alerts=0 (`evidence/experiments/environment_drift.md`).
7. Architecture Trace: issues=21, unowned_edges=0, trace_breaks=0, suggested_stubs=2 (`evidence/planning/ARCHITECTURE_TRACE_AUDIT.md`).
- `ISS-DEP-LINK-GAP-IFACE-EDGE-001` [dependency_link_gaps]
- `ISS-DEP-LINK-GAP-IFACE-EDGE-002` [dependency_link_gaps]
- `ISS-DEP-LINK-GAP-IFACE-EDGE-003` [dependency_link_gaps]
- `ISS-DEP-LINK-GAP-IFACE-EDGE-004` [dependency_link_gaps]
8. Maintenance: 0 unlinked evidence run(s), 0 warning(s).
