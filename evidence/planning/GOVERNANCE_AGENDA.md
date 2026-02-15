# Governance Agenda

Generated: `2026-02-15T21:38:14.189781Z`

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
2. Conflict Resolution: 27 conflict item(s).
- `ARC-003` conflict_types=directional
- `ARC-007` conflict_types=directional
- `ARC-018` conflict_types=directional
- `MECH-033` conflict_types=directional
- `MECH-040` conflict_types=directional
- `MECH-046` conflict_types=directional
- `MECH-056` conflict_types=directional, source_disagreement
- `MECH-057` conflict_types=directional
- `MECH-058` conflict_types=directional, mixed_evidence
- `MECH-059` conflict_types=directional, mixed_evidence
3. Architecture-Epoch Applicability: enabled=True; considered=836; applicable=451; stale=385; claims_with_stale=26.
- report: `evidence/planning/architecture_epoch_applicability.v1.json`
- `MECH-060` stale_entries=81; stale_ratio=0.686
- `MECH-059` stale_entries=67; stale_ratio=0.62
- `MECH-058` stale_entries=66; stale_ratio=0.641
- `MECH-056` stale_entries=51; stale_ratio=0.607
- `Q-016` stale_entries=38; stale_ratio=0.514
- `Q-017` stale_entries=28; stale_ratio=0.418
- `MECH-057` stale_entries=7; stale_ratio=0.438
- `Q-011` stale_entries=5; stale_ratio=0.833
- `ARC-018` stale_entries=5; stale_ratio=0.357
- `MECH-033` stale_entries=5; stale_ratio=0.357
4. Governance Decisions: 6 recommendation queue item(s).
- `MECH-056` decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `MECH-057` decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `MECH-058` decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `MECH-059` decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `MECH-060` decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `MECH-061` decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
5. Manual Carryover: 0 open item(s), 1 total.
- source: `evidence/planning/manual_carryover_items.v1.json`
6. Architecture Structure: 16 consider-new-structure item(s), 30 total register item(s).
- `MECH-060` conflict_ratio=0.895; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `MECH-056` conflict_ratio=0.892; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `MECH-058` conflict_ratio=0.891; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `ARC-003` conflict_ratio=0.889; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `MECH-061` conflict_ratio=0.889; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `Q-017` conflict_ratio=0.879; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `MECH-040` conflict_ratio=0.8; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `MECH-046` conflict_ratio=0.8; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `Q-012` conflict_ratio=0.8; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `Q-013` conflict_ratio=0.8; trigger_signals=high_conflict_ratio,literature_non_support_pressure,recurring_failure_signatures
7. Structure Dossiers: 16 dossier(s), 16 marked consider-new-structure.
- dossier index: `evidence/planning/structure_review/latest/INDEX.md`
8. Connectome Literature Pull: 16 queued claim(s), 16 high-priority.
- connectome queue: `evidence/planning/CONNECTOME_LITERATURE_PULL.md`
- `MECH-060` pull_id=`CPULL-0001`
- `MECH-056` pull_id=`CPULL-0002`
- `MECH-058` pull_id=`CPULL-0003`
- `ARC-003` pull_id=`CPULL-0004`
- `MECH-061` pull_id=`CPULL-0005`
- `Q-017` pull_id=`CPULL-0006`
- `MECH-040` pull_id=`CPULL-0007`
- `MECH-046` pull_id=`CPULL-0008`
- `Q-012` pull_id=`CPULL-0009`
- `Q-013` pull_id=`CPULL-0010`
9. Model Adjudication: 15 external-precedence candidate(s), 15 anti-lock-in review item(s).
- allowed outcomes: retain_ree,hybridize,adopt_jepa_structure,retire_ree_claim
- temporary override mode: `jepa_internal_proxy_override`
- `MECH-060` external_precedence_candidate=yes; delta_lit_minus_exp=0.325
- `MECH-056` external_precedence_candidate=yes; delta_lit_minus_exp=0.247
- `MECH-058` external_precedence_candidate=yes; delta_lit_minus_exp=0.333
- `ARC-003` external_precedence_candidate=yes; delta_lit_minus_exp=0.191
- `MECH-061` external_precedence_candidate=yes; delta_lit_minus_exp=0.163
- `Q-017` external_precedence_candidate=yes; delta_lit_minus_exp=0.356
- `MECH-040` external_precedence_candidate=yes; delta_lit_minus_exp=0.280
- `MECH-046` external_precedence_candidate=yes; delta_lit_minus_exp=0.255
- `Q-012` external_precedence_candidate=yes; delta_lit_minus_exp=0.269
- `Q-015` external_precedence_candidate=yes; delta_lit_minus_exp=0.227
10. Adjudication Cascade: 0 action(s), 0 claim update(s), 0 dependent reopen(s).
- patch queue: `evidence/planning/ADJUDICATION_CASCADE_PATCH_QUEUE.md`
11. Evidence Dispatch: 27 high-priority proposal(s), 27 total.
- ree-experiments-lab: total=26, experimental=26, literature_review=0
- ree-v2: total=1, experimental=1, literature_review=0
12. Maintenance: 0 unlinked evidence run(s), 0 warning(s).
