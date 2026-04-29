# Governance Agenda

Generated: `2026-04-29T06:06:28.768427Z`

## Cycle Status

| step | status | command |
|---|---|---|
| `task_inbox_sync` | `ok` | `/opt/local/bin/python3 evidence/planning/scripts/sync_task_inbox.py` |
| `thought_sweep` | `ok` | `/opt/local/bin/python3 docs/thoughts/scripts/thought_sweep.py` |
| `adjudication_cascade` | `ok` | `/opt/local/bin/python3 evidence/planning/scripts/apply_adjudication_cascade.py --decision-statuses approved,applied` |
| `evidence_build` | `ok` | `/opt/local/bin/python3 evidence/experiments/scripts/build_experiment_indexes.py` |
| `thought_adjudication_bridge` | `ok` | `/opt/local/bin/python3 evidence/planning/scripts/build_thought_adjudication_bridge.py` |
| `structure_review` | `ok` | `/opt/local/bin/python3 evidence/planning/scripts/build_structure_review_dossiers.py` |
| `human_decision_briefs` | `ok` | `/opt/local/bin/python3 evidence/planning/scripts/build_human_decision_briefs.py` |
| `connectome_pull` | `ok` | `/opt/local/bin/python3 evidence/planning/scripts/build_connectome_literature_pull.py` |
| `convergence_intake_queue` | `ok` | `/opt/local/bin/python3 evidence/planning/scripts/build_convergence_intake_queue.py` |

## Discussion Checkpoints

### Autonomy Triage

| work_item | tier | gate_status | recommendation | rollback_ready | decision_needed |
|---|---|---|---|---|---|
| `governance_maintenance_pipeline` | `AUTO` | `PASS` | `execute` | `yes` | `no` |
| `adjudication_cascade_application` | `AUTO` | `PASS` | `execute_no_pending_actions` | `yes` | `no` |
| `weekly_dispatch_export` | `AUTO_WITH_APPROVAL` | `PASS` | `approve_dispatch` | `yes` | `yes` |
| `convergence_packet_review_queue` | `AUTO_WITH_APPROVAL` | `PASS` | `all_packets_adjudicated` | `yes` | `no` |
| `promotion_demotion_and_conflict_resolution` | `HUMAN_ONLY` | `FAIL` | `review_decision_queue_and_conflicts` | `n/a` | `yes` |
| `architecture_structure_adjudication` | `HUMAN_ONLY` | `PASS` | `no_action_required` | `n/a` | `no` |

Open decision items: `weekly_dispatch_export`, `promotion_demotion_and_conflict_resolution`.

1. Thought Intake: 13 unprocessed thought(s).
- context: `docs/thoughts/SWEEP_REPORT.md`, `docs/thoughts/thought_sweep.v1.json`
- `2026-04-16_language_system_development_and_affective_expression_lateralisation.md`
- `2026-04-17_attention_coverage_audit.md`
- `2026-04-17_invariant_types_governance.md`
- `2026-04-20_analysis_of_missing_pieces_and_work_to_do.md`
- `2026-04-20_modes.md`
- `2026-04-20_ocd1.md`
- `2026-04-20_ocd2.md`
- `2026-04-20_ocd3.md`
- `2026-04-20_ocd4.md`
- `2026-04-23_binding.md`
- `2026-04-23_path_integral_constraints_search.md`
- `2026-04-28_action_object_type_abstraction.md`
- `2026-04-28_action_policy_and_multi_goal.md`
1a. Thought-Adjudication Bridge: 3 candidate item(s); approved_pending_apply=0.
- context: `evidence/planning/THOUGHT_ADJUDICATION_BRIDGE.md`, `evidence/planning/thought_adjudication_bridge.v1.json`
- `Q-025` (open question; ethics / axiom forbidden actions; see `docs/architecture/five_axioms_foundations.md`); reason=`no_decision_for_thought_enriched_claim`; action=`open_decision_lane_for_thought_enriched_claim`
- `Q-026` (open question; ethics / axiom required actions; see `docs/architecture/five_axioms_foundations.md`); reason=`no_decision_for_thought_enriched_claim`; action=`open_decision_lane_for_thought_enriched_claim`
- `Q-028` (open question; ethics / axiom conflict resolution; see `docs/architecture/five_axioms_foundations.md`); reason=`no_decision_for_thought_enriched_claim`; action=`open_decision_lane_for_thought_enriched_claim`
2. Conflict Resolution: 68 conflict item(s).
- context: `evidence/experiments/conflicts.md`, `evidence/planning/ARCHITECTURE_GAP_REGISTER.md`
- `ARC-007` (architecture commitment; hippocampus / path memory; see `docs/architecture/hippocampal_systems.md#arc-007`); conflict_types=directional, source_disagreement, mixed_evidence
- `ARC-016` (architecture commitment; cognitive modes / control plane regimes; see `docs/architecture/modes_of_cognition.md#arc-016`); conflict_types=directional, source_disagreement, mixed_evidence
- `ARC-018` (architecture commitment; hippocampus / rollout viability mapping; see `docs/architecture/hippocampal_systems.md#arc-018`); conflict_types=directional, mixed_evidence
- `ARC-024` (architecture_hypothesis; world / harm benefit asymptotic proxy structure; see `docs/architecture/five_axioms_foundations.md`); conflict_types=directional, mixed_evidence
- `ARC-026` (architecture_hypothesis; ethics / love expands under intelligence; see `docs/architecture/five_axioms_foundations.md`); conflict_types=directional, mixed_evidence
- `ARC-029` (architecture commitment; cognitive modes / behavioral consequence of commitment; see `docs/architecture/modes_of_cognition.md#arc-029`); conflict_types=directional, source_disagreement
- `ARC-030` (architecture_hypothesis; architecture / approach avoidance symmetry; see `docs/architecture/approach_avoidance_symmetry.md#arc-030`); conflict_types=directional, source_disagreement, mixed_evidence
- `ARC-032` (architecture_hypothesis; architecture / theta frontal hippocampal goal; see `docs/architecture/approach_avoidance_symmetry.md#arc-032`); conflict_types=directional, source_disagreement, mixed_evidence
- `ARC-033` (architecture commitment; harm stream / sensory discriminative forward model; see `docs/claims/claims.yaml`); conflict_types=directional, mixed_evidence
- `ARC-038` (architecture commitment; hippocampus / waking consolidation mode; see `docs/claims/claims.yaml`); conflict_types=directional, source_disagreement
3. Architecture-Epoch Applicability: enabled=True; considered=2873; applicable=2571; stale=302; claims_with_stale=37.
- context: `evidence/planning/architecture_epoch_applicability.v1.json`, `evidence/planning/planning_criteria.v1.yaml`
- `MECH-060` (mechanism hypothesis; commitment / dual error channels pre post commit; see `docs/architecture/agency_responsibility_flow.md#mech-060`) stale_entries=42; stale_ratio=0.875
- `MECH-058` (mechanism hypothesis; latent stack / e1 e2 timescale separation; see `docs/architecture/agency_responsibility_flow.md#mech-058`) stale_entries=35; stale_ratio=0.946
- `MECH-059` (mechanism hypothesis; precision / confidence channel separate from prediction error; see `docs/architecture/agency_responsibility_flow.md#mech-059`) stale_entries=26; stale_ratio=0.812
- `Q-017` (open question; control plane / minimal orthogonal axis set; see `docs/architecture/control_plane.md#q-017`) stale_entries=21; stale_ratio=0.778
- `MECH-056` (mechanism hypothesis; residue / trajectory first placement; see `docs/architecture/residue_geometry.md#mech-056`) stale_entries=20; stale_ratio=0.741
- `MECH-057` (no registry metadata found; see `docs/claims/claims.yaml`) stale_entries=12; stale_ratio=0.923
- `MECH-061` (mechanism hypothesis; commitment / boundary token error reclassification; see `docs/architecture/e3.md#mech-061`) stale_entries=9; stale_ratio=0.562
- `MECH-033` (mechanism hypothesis; hippocampus / kernel chaining interface; see `docs/architecture/hippocampal_systems.md#mech-033`) stale_entries=8; stale_ratio=0.258
- `ARC-018` (architecture commitment; hippocampus / rollout viability mapping; see `docs/architecture/hippocampal_systems.md#arc-018`) stale_entries=7; stale_ratio=0.2
- `ARC-003` (architecture commitment; E3 / trajectory commitment; see `docs/architecture/e3.md#arc-003`) stale_entries=5; stale_ratio=1.0
4. Governance Decisions: 86 recommendation queue item(s).
- context: `evidence/experiments/promotion_demotion_recommendations.md`, `evidence/decisions/decision_log.v1.jsonl`
- `ARC-026` (architecture_hypothesis; ethics / love expands under intelligence; see `docs/architecture/five_axioms_foundations.md`); decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `ARC-030` (architecture_hypothesis; architecture / approach avoidance symmetry; see `docs/architecture/approach_avoidance_symmetry.md#arc-030`); decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `ARC-032` (architecture_hypothesis; architecture / theta frontal hippocampal goal; see `docs/architecture/approach_avoidance_symmetry.md#arc-032`); decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `ARC-038` (architecture commitment; hippocampus / waking consolidation mode; see `docs/claims/claims.yaml`); decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `ARC-041` (architecture commitment; architecture / frontal cue weighting circuit; see `docs/architecture/frontal_cue_integration.md`); decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `ARC-042` (architecture commitment; architecture / staged developmental phases; see `docs/architecture/vmPFC.md`); decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `ARC-051` (architecture_hypothesis; goal / emergent hierarchy; see `docs/claims/claims.yaml`); decision=Hold — V3 substrate required before meaningful evidence can be collected; recommendation=`hold_pending_v3_substrate`
- `ARC-058` (architecture commitment; harm stream / shared forward trunk; see `evidence/literature/targeted_review_pain_predictive_coding_substrate/synthesis.md`); decision=Hold — V3 substrate required before meaningful evidence can be collected; recommendation=`hold_pending_v3_substrate`
- `ARC-060` (architecture_hypothesis; goal / explicit unresolved goal hierarchy; see `docs/architecture/ghost_goal_search.md`); decision=Hold — V3 substrate required before meaningful evidence can be collected; recommendation=`hold_pending_v3_substrate`
- `INV-054` (invariant; psychiatric / depressive maintenance loop; see `docs/claims/claims.yaml`); decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
5. Human Decision Briefs: 13 claim brief(s).
- context: `/Users/dgolden/REE_Working/REE_assembly/evidence/decisions/human_decision_briefs/latest/INDEX.md`, `evidence/decisions/HUMAN_DECISION_GLOSSARY.md`
- weekly dispatch brief: `/Users/dgolden/REE_Working/REE_assembly/evidence/decisions/human_decision_briefs/2026-04-29/WEEKLY_DISPATCH.md`
6. Manual Carryover: 1 open item(s), 2 total.
- context: `evidence/planning/manual_carryover_items.v1.json`, `evidence/planning/task_inbox.md`
- `MCI-0002` owner=`` summary=Queue V3-EXQ-325e (SD-032c AIC drive-dependence, supersedes V3-EXQ-325d) once V3-EXQ-476 passes and the MECH-269 V_s invalidation circuit is validated end-to-end. Action: flip `VS_CIRCUIT_READY=True` in `ree-v3/experiments/v3_exq_325e_sd032c_aic_drive_dependence.py`, then add a queue entry (claim_ids=[SD-032c, SD-021], experiment_purpose=evidence, supersedes=v3_exq_325d_sd032c_aic_descending_modulation, estimated_minutes=~240, machine_affinity=any). Reason for gate: without V_s-driven mode-switch variation, the MECH-090 bistable commit latch keeps the agent committed for every eval tick and `safe_ratio` returns the 1.0 empty-uncommitted fallback, making C1/C4b untestable. Root-cause diagnosis of EXQ-325d bit-identical `aic_salience_mean` is documented in the new script's docstring (drive_level never fed into `update_z_goal`; single-ablation arm hit both AIC knobs simultaneously; urgency threshold unreachable pre-V_s).
7. Architecture Structure: 0 consider-new-structure item(s), 41 total register item(s).
- context: `evidence/planning/ARCHITECTURE_GAP_REGISTER.md`, `evidence/planning/structure_review/latest/ACTIVE_INDEX.md`
- backlog mode guards: saturation_holds=0, escalation_required=0
8. Structure Dossiers: 0 active dossier(s), 79 archived dossier(s), 0 active marked consider-new-structure.
- context: `evidence/planning/structure_review/latest/ACTIVE_INDEX.md`, `evidence/planning/structure_review/latest/ARCHIVE_INDEX.md`
9. Connectome Literature Pull: 6 queued claim(s), 6 high-priority, 0 completed.
- context: `evidence/planning/CONNECTOME_LITERATURE_PULL.md`, `evidence/planning/connectome_pull_state.v1.json`
- `ARC-016` (architecture commitment; cognitive modes / control plane regimes; see `docs/architecture/modes_of_cognition.md#arc-016`); pull_id=`CPULL-0001`
- `MECH-025` (mechanism hypothesis; cognitive modes / action doing precision; see `docs/architecture/modes_of_cognition.md#mech-025`); pull_id=`CPULL-0002`
- `MECH-026` (mechanism hypothesis; cognitive modes / ready vigilance; see `docs/architecture/modes_of_cognition.md#mech-026`); pull_id=`CPULL-0003`
- `MECH-029` (mechanism hypothesis; default mode / reflective ethics; see `docs/architecture/default_mode.md#mech-029`); pull_id=`CPULL-0004`
- `MECH-030` (mechanism hypothesis; sleep / modes consolidation; see `docs/architecture/sleep.md#mech-030`); pull_id=`CPULL-0005`
- `MECH-047` (mechanism hypothesis; control plane / precommitment mode manager; see `docs/architecture/mode_manager.md#mech-047`); pull_id=`CPULL-0006`
10. Convergence Intake: enabled=True; total=10; valid=10; invalid=0; gate_ready=10; gate_failures=0; placeholder_evidence=0; implementation_plans=10.
- context: `evidence/planning/CONVERGENCE_INTAKE_QUEUE.md`, `evidence/planning/convergence_intake_queue.v1.json`
- required gates: `primary_sources_verified`, `source_content_mode_defined`, `source_license_id_defined`, `source_license_review_verified`, `copied_content_attribution_defined`, `separation_tests_defined`, `falsifiability_defined`, `rollback_plan_defined`, `falsification_plan_complete`, `conflict_review_completed`, `mechanism_probe_ids_defined`, `benchmark_acceptance_criteria_defined`, `non_lexical_probation_window_configured`, `non_lexical_rollback_conditions_defined`, `non_lexical_adapter_patch_refs_defined`, `no_placeholder_evidence_tokens`
- blast radius counts: `interface`=10
- packet=`CPKT-ACTIVE-INFERENCE-20260223` source=`active-inference` status=`proposed` blast=`interface` gate_ready=true gate_failures=0 impl=`in_progress` probes=1 bench=1 claims=5
- packet=`CPKT-DNC-20260223` source=`dnc` status=`proposed` blast=`interface` gate_ready=true gate_failures=0 impl=`in_progress` probes=1 bench=1 claims=5
- packet=`CPKT-DREAMDOJO-20260223` source=`dreamdojo` status=`proposed` blast=`interface` gate_ready=true gate_failures=0 impl=`in_progress` probes=1 bench=1 claims=5
- packet=`CPKT-DREAMER-V3-20260223` source=`dreamer-v3` status=`proposed` blast=`interface` gate_ready=true gate_failures=0 impl=`in_progress` probes=1 bench=1 claims=5
- packet=`CPKT-GNN-PLANNING-20260223` source=`gnn-planning` status=`proposed` blast=`interface` gate_ready=true gate_failures=0 impl=`in_progress` probes=1 bench=1 claims=5
- packet=`CPKT-JEPA-2026-0001` source=`jepa` status=`proposed` blast=`interface` gate_ready=true gate_failures=0 impl=`in_progress` probes=2 bench=2 claims=9
- packet=`CPKT-MULTIMODAL-AGENTS-20260223` source=`multimodal-agents` status=`proposed` blast=`interface` gate_ready=true gate_failures=0 impl=`in_progress` probes=1 bench=1 claims=5
- packet=`CPKT-MUZERO-20260223` source=`muzero` status=`proposed` blast=`interface` gate_ready=true gate_failures=0 impl=`in_progress` probes=1 bench=1 claims=5
- packet=`CPKT-RAG-20260223` source=`rag` status=`proposed` blast=`interface` gate_ready=true gate_failures=0 impl=`in_progress` probes=1 bench=1 claims=5
- packet=`CPKT-RT-2-20260223` source=`rt-2` status=`proposed` blast=`interface` gate_ready=true gate_failures=0 impl=`in_progress` probes=1 bench=1 claims=5
11. Model Adjudication: 0 external-precedence candidate(s), 0 anti-lock-in review item(s).
- context: `evidence/planning/planning_criteria.v1.yaml`, `evidence/planning/ARCHITECTURE_GAP_REGISTER.md`
- allowed outcomes: retain_ree,hybridize,retire_ree_claim
12. Adjudication Cascade: 0 action(s), 0 claim update(s), 0 dependent reopen(s).
- context: `evidence/planning/ADJUDICATION_CASCADE_PATCH_QUEUE.md`, `evidence/decisions/adjudication_cascade_state.v1.json`
13. Evidence Dispatch: 88 high-priority proposal(s), 207 total.
- context: `evidence/planning/experiment_proposals.v1.json`
- approval state: approved_for_cycle=false; latest_status=`missing`; latest_recommendation=``; latest_timestamp_utc=``
- REE_assembly: total=21, experimental=0, literature_review=9
- ree-v3: total=186, experimental=185, literature_review=0
14. Maintenance: 17 unlinked evidence run(s), 0 warning(s).
- context: `evidence/experiments/claim_evidence.v1.json`, `evidence/experiments/TODOs.md`
