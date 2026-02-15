# Governance Agenda

Generated: `2026-02-15T15:32:10.348345Z`

## Cycle Status

| step | status | command |
|---|---|---|
| `task_inbox_sync` | `ok` | `/opt/local/bin/python3 evidence/planning/scripts/sync_task_inbox.py` |
| `thought_sweep` | `ok` | `/opt/local/bin/python3 docs/thoughts/scripts/thought_sweep.py` |
| `adjudication_cascade` | `ok` | `/opt/local/bin/python3 evidence/planning/scripts/apply_adjudication_cascade.py --decision-statuses applied` |
| `evidence_build` | `ok` | `/opt/local/bin/python3 evidence/experiments/scripts/build_experiment_indexes.py` |
| `structure_review` | `ok` | `/opt/local/bin/python3 evidence/planning/scripts/build_structure_review_dossiers.py` |
| `connectome_pull` | `ok` | `/opt/local/bin/python3 evidence/planning/scripts/build_connectome_literature_pull.py` |

## Discussion Checkpoints

### Autonomy Triage

| work_item | tier | gate_status | recommendation | rollback_ready | decision_needed |
|---|---|---|---|---|---|
| `governance_maintenance_pipeline` | `AUTO` | `PASS` | `execute` | `yes` | `no` |
| `adjudication_cascade_application` | `AUTO` | `PASS` | `execute_no_pending_actions` | `yes` | `no` |
| `weekly_dispatch_export` | `AUTO_WITH_APPROVAL` | `PASS` | `approve_dispatch` | `yes` | `yes` |
| `promotion_demotion_and_conflict_resolution` | `HUMAN_ONLY` | `FAIL` | `review_decision_queue_and_conflicts` | `n/a` | `yes` |
| `architecture_structure_adjudication` | `HUMAN_ONLY` | `FAIL` | `review_structure_dossiers_and_model_adjudication` | `n/a` | `yes` |

Open decision items: `weekly_dispatch_export`, `promotion_demotion_and_conflict_resolution`, `architecture_structure_adjudication`.

1. Thought Intake: 0 unprocessed thought(s).
2. Conflict Resolution: 8 conflict item(s).
- `ARC-018` conflict_types=directional
- `MECH-033` conflict_types=directional
- `MECH-056` conflict_types=directional, source_disagreement, mixed_evidence
- `MECH-058` conflict_types=directional, mixed_evidence
- `MECH-059` conflict_types=directional, mixed_evidence
- `MECH-060` conflict_types=directional, source_disagreement, mixed_evidence
- `Q-011` conflict_types=directional
- `Q-017` conflict_types=directional, source_disagreement
3. Governance Decisions: 5 recommendation queue item(s).
- `MECH-056` decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `MECH-058` decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `MECH-059` decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `MECH-060` decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `Q-011` decision=Promotion review: candidate -> provisional; recommendation=`promote_to_provisional`
4. Manual Carryover: 0 open item(s), 1 total.
- source: `evidence/planning/manual_carryover_items.v1.json`
5. Architecture Structure: 5 consider-new-structure item(s), 10 total register item(s).
- `MECH-056` conflict_ratio=0.941; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `MECH-058` conflict_ratio=0.939; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `MECH-060` conflict_ratio=0.937; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `Q-017` conflict_ratio=0.897; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `MECH-059` conflict_ratio=0.704; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
6. Structure Dossiers: 5 dossier(s), 5 marked consider-new-structure.
- dossier index: `evidence/planning/structure_review/latest/INDEX.md`
7. Connectome Literature Pull: 5 queued claim(s), 5 high-priority.
- connectome queue: `evidence/planning/CONNECTOME_LITERATURE_PULL.md`
- `MECH-056` pull_id=`CPULL-0001`
- `MECH-058` pull_id=`CPULL-0002`
- `MECH-060` pull_id=`CPULL-0003`
- `Q-017` pull_id=`CPULL-0004`
- `MECH-059` pull_id=`CPULL-0005`
8. Model Adjudication: 5 external-precedence candidate(s), 5 anti-lock-in review item(s).
- allowed outcomes: retain_ree,hybridize,adopt_jepa_structure,retire_ree_claim
- temporary override mode: `jepa_internal_proxy_override`
- `MECH-056` external_precedence_candidate=yes; delta_lit_minus_exp=0.297
- `MECH-058` external_precedence_candidate=yes; delta_lit_minus_exp=0.361
- `MECH-060` external_precedence_candidate=yes; delta_lit_minus_exp=0.330
- `Q-017` external_precedence_candidate=yes; delta_lit_minus_exp=0.355
- `MECH-059` external_precedence_candidate=yes; delta_lit_minus_exp=0.221
9. Adjudication Cascade: 0 action(s), 0 claim update(s), 0 dependent reopen(s).
- patch queue: `evidence/planning/ADJUDICATION_CASCADE_PATCH_QUEUE.md`
10. Evidence Dispatch: 34 high-priority proposal(s), 34 total.
- ree-experiments-lab: total=5, experimental=5, literature_review=0
- ree-v2: total=29, experimental=29, literature_review=0
11. Maintenance: 0 unlinked evidence run(s), 0 warning(s).
