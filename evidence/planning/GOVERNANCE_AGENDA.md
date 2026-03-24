# Governance Agenda

Generated: `2026-03-24T16:58:40.699039Z`

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

1. Thought Intake: 4 unprocessed thought(s).
- context: `docs/thoughts/SWEEP_REPORT.md`, `docs/thoughts/thought_sweep.v1.json`
- `2026-03-14_self_world_latent_split_sd003_limitation.md`
- `2026-03-17_sd003_benefit_signal_gap.md`
- `2026-03-17_three_stream_reafference.md`
- `2026-03-24_COHERENCE_MULTICONSTRAINT_HIPPOCAMPAL_NAVIGATION_CONVERGENCE.md`
1a. Thought-Adjudication Bridge: 0 candidate item(s); approved_pending_apply=0.
- context: `evidence/planning/THOUGHT_ADJUDICATION_BRIDGE.md`, `evidence/planning/thought_adjudication_bridge.v1.json`
2. Conflict Resolution: 17 conflict item(s).
- context: `evidence/experiments/conflicts.md`, `evidence/planning/ARCHITECTURE_GAP_REGISTER.md`
- `ARC-007` (architecture commitment; hippocampus / path memory; see `docs/architecture/hippocampal_systems.md#arc-007`); conflict_types=directional
- `ARC-016` (architecture commitment; cognitive modes / control plane regimes; see `docs/architecture/modes_of_cognition.md#arc-016`); conflict_types=directional, mixed_evidence
- `ARC-018` (architecture commitment; hippocampus / rollout viability mapping; see `docs/architecture/hippocampal_systems.md#arc-018`); conflict_types=directional
- `ARC-024` (architecture_hypothesis; world / harm benefit asymptotic proxy structure; see `docs/architecture/five_axioms_foundations.md`); conflict_types=directional, mixed_evidence
- `MECH-033` (mechanism hypothesis; hippocampus / kernel chaining interface; see `docs/architecture/hippocampal_systems.md#mech-033`); conflict_types=directional
- `MECH-071` (mechanism hypothesis; e3 / harm eval calibration gradient asymmetry; see `docs/architecture/sd_003_experiment_design.md#mech-071`); conflict_types=directional, mixed_evidence
- `MECH-089` (mechanism hypothesis; multirate / fast to slow temporal batching; see `docs/architecture/control_plane_heartbeat.md#mech-089`); conflict_types=directional, mixed_evidence
- `MECH-090` (mechanism hypothesis; control plane / commitment gated policy output; see `docs/architecture/control_plane_heartbeat.md#mech-090`); conflict_types=directional, mixed_evidence
- `MECH-093` (mechanism hypothesis; affective / z beta e3 update rate modulation; see `docs/architecture/control_plane_heartbeat.md#mech-093`); conflict_types=directional, source_disagreement, mixed_evidence
- `MECH-095` (mechanism hypothesis; tpj / agency detection comparator; see `docs/thoughts/2026-03-14_self_world_latent_split_sd003_limitation.md`); conflict_types=directional, source_disagreement, mixed_evidence
3. Architecture-Epoch Applicability: enabled=True; considered=1776; applicable=453; stale=1323; claims_with_stale=40.
- context: `evidence/planning/architecture_epoch_applicability.v1.json`, `evidence/planning/planning_criteria.v1.yaml`
- `MECH-060` (mechanism hypothesis; commitment / dual error channels pre post commit; see `docs/architecture/agency_responsibility_flow.md#mech-060`) stale_entries=184; stale_ratio=0.995
- `MECH-056` (mechanism hypothesis; residue / trajectory first placement; see `docs/architecture/residue_geometry.md#mech-056`) stale_entries=174; stale_ratio=0.989
- `MECH-059` (mechanism hypothesis; precision / confidence channel separate from prediction error; see `docs/architecture/agency_responsibility_flow.md#mech-059`) stale_entries=172; stale_ratio=0.994
- `MECH-058` (mechanism hypothesis; latent stack / e1 e2 timescale separation; see `docs/architecture/agency_responsibility_flow.md#mech-058`) stale_entries=167; stale_ratio=0.988
- `Q-017` (open question; control plane / minimal orthogonal axis set; see `docs/architecture/control_plane.md#q-017`) stale_entries=128; stale_ratio=1.0
- `Q-016` (open question; commitment / tri loop conflict arbitration policy; see `docs/architecture/e3.md#q-016`) stale_entries=115; stale_ratio=1.0
- `MECH-062` (mechanism hypothesis; commitment / tri loop gate coordination; see `docs/architecture/e3.md#mech-062`) stale_entries=46; stale_ratio=1.0
- `MECH-057` (no registry metadata found; see `docs/claims/claims.yaml`) stale_entries=21; stale_ratio=0.955
- `MECH-033` (mechanism hypothesis; hippocampus / kernel chaining interface; see `docs/architecture/hippocampal_systems.md#mech-033`) stale_entries=16; stale_ratio=0.762
- `Q-013` (open question; uncertainty / deterministic vs stochastic jepa calibration; see `docs/architecture/agency_responsibility_flow.md#q-013`) stale_entries=15; stale_ratio=1.0
4. Governance Decisions: 14 recommendation queue item(s).
- context: `evidence/experiments/promotion_demotion_recommendations.md`, `evidence/decisions/decision_log.v1.jsonl`
- `ARC-007` (architecture commitment; hippocampus / path memory; see `docs/architecture/hippocampal_systems.md#arc-007`); decision=Hold — V3 substrate required before meaningful evidence can be collected; recommendation=`hold_pending_v3_substrate`
- `ARC-023` (architecture commitment; basal ganglia / three loop thalamic heartbeat; see `docs/architecture/control_plane_heartbeat.md#arc-023`); decision=Hold — V3 substrate required before meaningful evidence can be collected; recommendation=`hold_pending_v3_substrate`
- `MECH-025` (mechanism hypothesis; cognitive modes / action doing; see `docs/architecture/modes_of_cognition.md#mech-025`); decision=Hold — V3 substrate required before meaningful evidence can be collected; recommendation=`hold_pending_v3_substrate`
- `MECH-072` (mechanism hypothesis; residue / foreseeable harm gating reduces false attribution; see `docs/architecture/sd_003_experiment_design.md#mech-072`); decision=Hold — V3 substrate required before meaningful evidence can be collected; recommendation=`hold_pending_v3_substrate`
- `MECH-091` (mechanism hypothesis; control plane / salient event cycle resync; see `docs/architecture/control_plane_heartbeat.md#mech-091`); decision=Hold — V3 substrate required before meaningful evidence can be collected; recommendation=`hold_pending_v3_substrate`
- `MECH-092` (mechanism hypothesis; hippocampal / quiescent offline replay; see `docs/architecture/control_plane_heartbeat.md#mech-092`); decision=Hold — V3 substrate required before meaningful evidence can be collected; recommendation=`hold_pending_v3_substrate`
- `MECH-093` (mechanism hypothesis; affective / z beta e3 update rate modulation; see `docs/architecture/control_plane_heartbeat.md#mech-093`); decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `MECH-095` (mechanism hypothesis; tpj / agency detection comparator; see `docs/thoughts/2026-03-14_self_world_latent_split_sd003_limitation.md`); decision=Conflict resolution before promotion; recommendation=`hold_candidate_resolve_conflict`
- `MECH-096` (mechanism hypothesis; observation encoder / dual stream routing; see `docs/thoughts/2026-03-14_self_world_latent_split_sd003_limitation.md`); decision=Hold — V3 substrate required before meaningful evidence can be collected; recommendation=`hold_pending_v3_substrate`
- `MECH-097` (mechanism hypothesis; peripersonal space / commit locus; see `docs/thoughts/2026-03-14_self_world_latent_split_sd003_limitation.md`); decision=Hold — V3 substrate required before meaningful evidence can be collected; recommendation=`hold_pending_v3_substrate`
5. Human Decision Briefs: 0 claim brief(s).
- context: `/Users/dgolden/Documents/GitHub/REE_Working/REE_assembly/evidence/decisions/human_decision_briefs/latest/INDEX.md`, `evidence/decisions/HUMAN_DECISION_GLOSSARY.md`
- weekly dispatch brief: `/Users/dgolden/Documents/GitHub/REE_Working/REE_assembly/evidence/decisions/human_decision_briefs/2026-03-24/WEEKLY_DISPATCH.md`
6. Manual Carryover: 0 open item(s), 1 total.
- context: `evidence/planning/manual_carryover_items.v1.json`, `evidence/planning/task_inbox.md`
7. Architecture Structure: 0 consider-new-structure item(s), 9 total register item(s).
- context: `evidence/planning/ARCHITECTURE_GAP_REGISTER.md`, `evidence/planning/structure_review/latest/ACTIVE_INDEX.md`
- backlog mode guards: saturation_holds=0, escalation_required=0
8. Structure Dossiers: 0 active dossier(s), 79 archived dossier(s), 0 active marked consider-new-structure.
- context: `evidence/planning/structure_review/latest/ACTIVE_INDEX.md`, `evidence/planning/structure_review/latest/ARCHIVE_INDEX.md`
9. Connectome Literature Pull: 6 queued claim(s), 6 high-priority, 0 completed.
- context: `evidence/planning/CONNECTOME_LITERATURE_PULL.md`, `evidence/planning/connectome_pull_state.v1.json`
- `ARC-016` (architecture commitment; cognitive modes / control plane regimes; see `docs/architecture/modes_of_cognition.md#arc-016`); pull_id=`CPULL-0001`
- `MECH-025` (mechanism hypothesis; cognitive modes / action doing; see `docs/architecture/modes_of_cognition.md#mech-025`); pull_id=`CPULL-0002`
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
13. Evidence Dispatch: 28 high-priority proposal(s), 103 total.
- context: `evidence/planning/experiment_proposals.v1.json`
- approval state: approved_for_cycle=false; latest_status=`missing`; latest_recommendation=``; latest_timestamp_utc=``
- REE_assembly: total=50, experimental=0, literature_review=50
- ree-experiments-lab: total=9, experimental=9, literature_review=0
- ree-v2: total=35, experimental=35, literature_review=0
- unknown: total=9, experimental=3, literature_review=0
14. Maintenance: 1 unlinked evidence run(s), 0 warning(s).
- context: `evidence/experiments/claim_evidence.v1.json`, `evidence/experiments/TODOs.md`
