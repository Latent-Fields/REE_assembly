# Governance Agenda

Generated: `2026-02-21T17:40:43.417321Z`

## Cycle Status

| step | status | command |
|---|---|---|
| `task_inbox_sync` | `ok` | `/opt/local/bin/python3 evidence/planning/scripts/sync_task_inbox.py` |
| `thought_sweep` | `ok` | `/opt/local/bin/python3 docs/thoughts/scripts/thought_sweep.py` |
| `adjudication_cascade` | `ok` | `/opt/local/bin/python3 evidence/planning/scripts/apply_adjudication_cascade.py --decision-statuses approved,applied` |
| `evidence_build` | `ok` | `/opt/local/bin/python3 evidence/experiments/scripts/build_experiment_indexes.py` |
| `structure_review` | `ok` | `/opt/local/bin/python3 evidence/planning/scripts/build_structure_review_dossiers.py` |
| `human_decision_briefs` | `ok` | `/opt/local/bin/python3 evidence/planning/scripts/build_human_decision_briefs.py` |
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
- context: `docs/thoughts/SWEEP_REPORT.md`, `docs/thoughts/thought_sweep.v1.json`
2. Conflict Resolution: 24 conflict item(s).
- context: `evidence/experiments/conflicts.md`, `evidence/planning/ARCHITECTURE_GAP_REGISTER.md`
- `ARC-003` (architecture commitment; E3 / trajectory commitment; see `docs/architecture/e3.md#arc-003`); conflict_types=directional
- `ARC-007` (architecture commitment; hippocampus / path memory; see `docs/architecture/hippocampal_systems.md#arc-007`); conflict_types=directional
- `ARC-018` (architecture commitment; hippocampus / rollout viability mapping; see `docs/architecture/hippocampal_systems.md#arc-018`); conflict_types=directional
- `MECH-033` (mechanism hypothesis; hippocampus / kernel chaining interface; see `docs/architecture/hippocampal_systems.md#mech-033`); conflict_types=directional
- `MECH-040` (mechanism hypothesis; control plane / safety baseline volatility; see `docs/architecture/control_plane.md#mech-040`); conflict_types=directional
- `MECH-046` (mechanism hypothesis; control plane / amygdala mode priors; see `docs/architecture/control_plane.md#mech-046`); conflict_types=directional
- `MECH-056` (mechanism hypothesis; residue / trajectory first placement; see `docs/architecture/residue_geometry.md#mech-056`); conflict_types=directional, source_disagreement
- `MECH-057` (mechanism hypothesis; agentic extension / control completion requirement; see `docs/architecture/agency_responsibility_flow.md#mech-057`); conflict_types=directional
- `MECH-058` (mechanism hypothesis; jepa substrate / ema target anchor timescale separation; see `docs/architecture/agency_responsibility_flow.md#mech-058`); conflict_types=directional, mixed_evidence
- `MECH-059` (mechanism hypothesis; precision / confidence channel separate from prediction error; see `docs/architecture/agency_responsibility_flow.md#mech-059`); conflict_types=directional, mixed_evidence
3. Architecture-Epoch Applicability: enabled=True; considered=1257; applicable=872; stale=385; claims_with_stale=25.
- context: `evidence/planning/architecture_epoch_applicability.v1.json`, `evidence/planning/planning_criteria.v1.yaml`
- `MECH-060` (mechanism hypothesis; commitment / dual error channels pre post commit; see `docs/architecture/agency_responsibility_flow.md#mech-060`) stale_entries=81; stale_ratio=0.45
- `MECH-059` (mechanism hypothesis; precision / confidence channel separate from prediction error; see `docs/architecture/agency_responsibility_flow.md#mech-059`) stale_entries=67; stale_ratio=0.394
- `MECH-058` (mechanism hypothesis; jepa substrate / ema target anchor timescale separation; see `docs/architecture/agency_responsibility_flow.md#mech-058`) stale_entries=66; stale_ratio=0.4
- `MECH-056` (mechanism hypothesis; residue / trajectory first placement; see `docs/architecture/residue_geometry.md#mech-056`) stale_entries=51; stale_ratio=0.349
- `Q-016` (open question; commitment / tri loop conflict arbitration policy; see `docs/architecture/e3.md#q-016`) stale_entries=38; stale_ratio=0.33
- `Q-017` (open question; control plane / minimal orthogonal axis set; see `docs/architecture/control_plane.md#q-017`) stale_entries=28; stale_ratio=0.222
- `MECH-057` (mechanism hypothesis; agentic extension / control completion requirement; see `docs/architecture/agency_responsibility_flow.md#mech-057`) stale_entries=7; stale_ratio=0.438
- `ARC-018` (architecture commitment; hippocampus / rollout viability mapping; see `docs/architecture/hippocampal_systems.md#arc-018`) stale_entries=5; stale_ratio=0.333
- `MECH-033` (mechanism hypothesis; hippocampus / kernel chaining interface; see `docs/architecture/hippocampal_systems.md#mech-033`) stale_entries=5; stale_ratio=0.312
- `MECH-900` (no registry metadata found; see `docs/claims/claims.yaml`) stale_entries=3; stale_ratio=1.0
4. Governance Decisions: 7 recommendation queue item(s).
- context: `evidence/experiments/promotion_demotion_recommendations.md`, `evidence/decisions/decision_log.v1.jsonl`
- `MECH-056` (mechanism hypothesis; residue / trajectory first placement; see `docs/architecture/residue_geometry.md#mech-056`); decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `MECH-057` (mechanism hypothesis; agentic extension / control completion requirement; see `docs/architecture/agency_responsibility_flow.md#mech-057`); decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `MECH-058` (mechanism hypothesis; jepa substrate / ema target anchor timescale separation; see `docs/architecture/agency_responsibility_flow.md#mech-058`); decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `MECH-059` (mechanism hypothesis; precision / confidence channel separate from prediction error; see `docs/architecture/agency_responsibility_flow.md#mech-059`); decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `MECH-060` (mechanism hypothesis; commitment / dual error channels pre post commit; see `docs/architecture/agency_responsibility_flow.md#mech-060`); decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `MECH-061` (mechanism hypothesis; commitment / boundary token error reclassification; see `docs/architecture/e3.md#mech-061`); decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `MECH-062` (mechanism hypothesis; commitment / tri loop gate coordination; see `docs/architecture/e3.md#mech-062`); decision=Promotion review: provisional -> stable; recommendation=`promote_to_stable`
5. Human Decision Briefs: 10 claim brief(s).
- context: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/decisions/human_decision_briefs/latest/INDEX.md`, `evidence/decisions/HUMAN_DECISION_GLOSSARY.md`
- weekly dispatch brief: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/decisions/human_decision_briefs/2026-02-21/WEEKLY_DISPATCH.md`
6. Manual Carryover: 0 open item(s), 1 total.
- context: `evidence/planning/manual_carryover_items.v1.json`, `evidence/planning/task_inbox.md`
7. Architecture Structure: 6 consider-new-structure item(s), 27 total register item(s).
- context: `evidence/planning/ARCHITECTURE_GAP_REGISTER.md`, `evidence/planning/structure_review/latest/ACTIVE_INDEX.md`
- backlog mode guards: saturation_holds=0, escalation_required=3
- `MECH-060` (mechanism hypothesis; commitment / dual error channels pre post commit; see `docs/architecture/agency_responsibility_flow.md#mech-060`); conflict_ratio=0.875; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `MECH-058` (mechanism hypothesis; jepa substrate / ema target anchor timescale separation; see `docs/architecture/agency_responsibility_flow.md#mech-058`); conflict_ratio=0.871; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `Q-017` (open question; control plane / minimal orthogonal axis set; see `docs/architecture/control_plane.md#q-017`); conflict_ratio=0.848; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `MECH-057` (mechanism hypothesis; agentic extension / control completion requirement; see `docs/architecture/agency_responsibility_flow.md#mech-057`); conflict_ratio=0.769; trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures
- `Q-013` (open question; uncertainty / deterministic vs stochastic jepa calibration; see `docs/architecture/agency_responsibility_flow.md#q-013`); conflict_ratio=0.727; trigger_signals=high_conflict_ratio,literature_non_support_pressure,recurring_failure_signatures
- `Q-014` (open question; invariance / ethical relevance blind spot risk; see `docs/architecture/agency_responsibility_flow.md#q-014`); conflict_ratio=0.727; trigger_signals=high_conflict_ratio,literature_non_support_pressure,recurring_failure_signatures
8. Structure Dossiers: 6 active dossier(s), 49 archived dossier(s), 6 active marked consider-new-structure.
- context: `evidence/planning/structure_review/latest/ACTIVE_INDEX.md`, `evidence/planning/structure_review/latest/ARCHIVE_INDEX.md`
9. Connectome Literature Pull: 7 queued claim(s), 7 high-priority, 5 completed.
- context: `evidence/planning/CONNECTOME_LITERATURE_PULL.md`, `evidence/planning/connectome_pull_state.v1.json`
- `MECH-026` (mechanism hypothesis; cognitive modes / ready vigilance; see `docs/architecture/modes_of_cognition.md#mech-026`); pull_id=`CPULL-0003`
- `MECH-029` (mechanism hypothesis; default mode / reflective ethics; see `docs/architecture/default_mode.md#mech-029`); pull_id=`CPULL-0004`
- `MECH-030` (mechanism hypothesis; sleep / modes consolidation; see `docs/architecture/sleep.md#mech-030`); pull_id=`CPULL-0005`
- `MECH-047` (mechanism hypothesis; control plane / precommitment mode manager; see `docs/architecture/mode_manager.md#mech-047`); pull_id=`CPULL-0006`
- `MECH-057` (mechanism hypothesis; agentic extension / control completion requirement; see `docs/architecture/agency_responsibility_flow.md#mech-057`); pull_id=`CPULL-0010`
- `Q-013` (open question; uncertainty / deterministic vs stochastic jepa calibration; see `docs/architecture/agency_responsibility_flow.md#q-013`); pull_id=`CPULL-0011`
- `Q-014` (open question; invariance / ethical relevance blind spot risk; see `docs/architecture/agency_responsibility_flow.md#q-014`); pull_id=`CPULL-0012`
10. Model Adjudication: 4 external-precedence candidate(s), 4 anti-lock-in review item(s).
- context: `evidence/planning/planning_criteria.v1.yaml`, `evidence/planning/ARCHITECTURE_GAP_REGISTER.md`
- allowed outcomes: retain_ree,hybridize,adopt_jepa_structure,retire_ree_claim
- temporary override mode: `jepa_internal_proxy_override`
- `MECH-060` (mechanism hypothesis; commitment / dual error channels pre post commit; see `docs/architecture/agency_responsibility_flow.md#mech-060`); external_precedence_candidate=yes; delta_lit_minus_exp=0.301
- `MECH-058` (mechanism hypothesis; jepa substrate / ema target anchor timescale separation; see `docs/architecture/agency_responsibility_flow.md#mech-058`); external_precedence_candidate=yes; delta_lit_minus_exp=0.311
- `Q-017` (open question; control plane / minimal orthogonal axis set; see `docs/architecture/control_plane.md#q-017`); external_precedence_candidate=yes; delta_lit_minus_exp=0.316
- `MECH-057` (mechanism hypothesis; agentic extension / control completion requirement; see `docs/architecture/agency_responsibility_flow.md#mech-057`); external_precedence_candidate=yes; delta_lit_minus_exp=0.285
11. Adjudication Cascade: 0 action(s), 0 claim update(s), 0 dependent reopen(s).
- context: `evidence/planning/ADJUDICATION_CASCADE_PATCH_QUEUE.md`, `evidence/decisions/adjudication_cascade_state.v1.json`
12. Evidence Dispatch: 23 high-priority proposal(s), 25 total.
- context: `evidence/planning/experiment_proposals.v1.json`
- REE_assembly: total=1, experimental=0, literature_review=1
- ree-experiments-lab: total=15, experimental=15, literature_review=0
- ree-v2: total=9, experimental=9, literature_review=0
13. Maintenance: 0 unlinked evidence run(s), 0 warning(s).
- context: `evidence/experiments/claim_evidence.v1.json`, `evidence/experiments/TODOs.md`
