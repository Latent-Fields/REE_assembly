# Closure-Plan Drift Report

Generated: 2026-06-10T07:13:59Z

This report flags closure_plan nodes whose `owner_exq` has reached a terminal state (manifest landed and / or failure_autopsy artifact present) but whose `status` is still non-terminal. Nodes that self-tag as Case 3 (legitimately non-terminal pending upstream substrate or successor EXQs) and nodes whose owner_exq manifest is non-contributory / superseded / inconclusive are recorded under Suppressed instead, not Drifted. A separate date-aware section, `Stale since last update`, flags non-terminal nodes (including suppressed ones) where a later-lettered owner_exq sibling reached terminal state or a confirmed failure_autopsy touching the node's `unblocks_claims` post-dates the node's `last_updated` -- the class of staleness that hid goal_pipeline:GAP-2 on 2026-06-03. The report also flags plans missing a top-level `closure_plan.last_updated` field.

Warn-only -- this script never blocks the governance pipeline.

## Drifted nodes (0)

_None._

## Suppressed (legitimately non-terminal) (9)

Nodes whose `owner_exq` reached a terminal state but where suppression rules say the node is legitimately non-terminal (Case-3 self-tag or non-contributory manifest evidence_direction). Listed here for audit; not counted as drift.

| plan | node | status | owner_exq | suppress reason |
|------|------|--------|-----------|-----------------|
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-B` | in-progress | V3-EXQ-654a QUEUED 2026-06-09 (priority 250, machine any; supersedes V3-EXQ-654) -- the gated re-run on the landed cross-episode rule-persistence amend (ree-v3 main 9797e84). Single-variable ARM_OFF vs ARM_ON with crf_persist_rules_across_episode_reset=True (matured pool clears the C1c 0.30 floor), a frozen-encoder P1 trained-bias-head REINFORCE phase (GAP-D), and a propagation non-vacuity precondition (ARM_ON bias != ARM_OFF, else substrate_not_ready_requeue); committed-class entropy PRIMARY DV. PREDECESSOR V3-EXQ-654 TERMINAL FAIL 2026-06-09T08:18Z (non_contributory, confirmed failure_autopsy_V3-EXQ-654_2026-06-09): C1c readiness FAIL (CandidateRuleField cold-started per episode) gated out the C2 falsifier DV -- NOT a falsification. | manifest_evidence_direction=non_contributory |
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-H` | partial | V3-EXQ-604c PASS 2026-06-07 closed the Q-044/MECH-314-family GAP-A-ready leg; V3-EXQ-544/545/544a historical diagnostics; Q-045/MECH-313/MECH-260 leg awaits behavioral_diversity_isolation:GAP-C / V3-EXQ-603i; GAP-B successor still owed | case_3_self_tag |
| commitment_closure_plan.md | `commitment_closure:GAP-4` | in-progress | V3-EXQ-460b..468b (Phase 4/5 *b cohort; MECH-342 ecological = V3-EXQ-629) | case_3_self_tag |
| commitment_closure_plan.md | `commitment_closure:GAP-8` | in-progress | V3-EXQ-485d (trained-OFC-head substrate-readiness diagnostic; the deferred trained-head arm, queued 2026-06-09; predecessors V3-EXQ-485c + V3-EXQ-485b representation-level MECH-263 functional-signature diagnostics, both PASS reviewed 2026-06-04, NOT a supersession lineage) | case_3_self_tag |
| self_attribution_plan.md | `self_attribution:GAP-1` | blocked | V3-EXQ-445h | case_3_self_tag |
| sleep_substrate_plan.md | `sleep_substrate:GAP-2` | upstream-blocked | V3-EXQ-265a | case_3_self_tag |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-A` | in-progress | V3-EXQ-649 PASS 2026-06-07T13:14Z (GAP-A shared-channel substrate-readiness VALIDATED READY; consumed cand_world_summaries spread 0.090>=0.05 floor); V3-EXQ-567 (PASS); V3-EXQ-569 + V3-EXQ-573 (non_contributory); V3-EXQ-570 + V3-EXQ-571 + V3-EXQ-609 diagnostics landed; V3-EXQ-544a completed_supports 2026-05-30; V3-EXQ-569c claimed 2026-05-30; V3-EXQ-569f QUEUED 2026-06-09 (R1.b FP-2 matched-entropy action-contrastive behavioural falsifier on the 649-validated candidate_summary_source=e2_world_forward stack; supersedes 569d; ree-v3 db812e6) | manifest_evidence_direction=non_contributory |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-B` | partial | V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41Z (MECH-341 within-class-representative-diversity retest on the GAP-A-ready/authority-ready stack; within_class_rep_cond_entropy PRIMARY DV, swept 4.862 vs legacy 4.781 nats; supersedes 614e). Governance folded into claims.yaml 2026-06-10 (MECH-341 supports, v3_pending HELD). Predecessor: V3-EXQ-614e autopsy applied 2026-06-07 (non_contributory substrate_ceiling; GAP-A blocker moved upstream); V3-EXQ-649 GAP-A readiness PASS | case_3_self_tag |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-C` | in-progress | V3-EXQ-603k (Stage-H harm-pathway training; queued 2026-06-09; owns the PRIMARY nav/survival-competence leg this node waits on). Predecessors absorbed: V3-EXQ-603i TERMINAL FAIL 2026-06-08 (non_contributory substrate_ceiling, autopsied + applied /governance 2026-06-09T04:30Z) surfaced two co-equal substrate gaps -- PRIMARY nav/survival-competence ceiling (-> 603k) + SECONDARY safety-half starvation, the latter now closed at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (safety-half trained-signal; safety_signal 0.89; claim_ids=[]). Prior 603a/b/c/f/g/h lineage non_contributory substrate-ceiling | manifest_evidence_direction=non_contributory |

## Stale since last update -- review (0)

_None._

## Plans missing `closure_plan.last_updated` (0)

_None._

