# Closure-Plan Drift Report

Generated: 2026-06-09T17:59:31Z

This report flags closure_plan nodes whose `owner_exq` has reached a terminal state (manifest landed and / or failure_autopsy artifact present) but whose `status` is still non-terminal. Nodes that self-tag as Case 3 (legitimately non-terminal pending upstream substrate or successor EXQs) and nodes whose owner_exq manifest is non-contributory / superseded / inconclusive are recorded under Suppressed instead, not Drifted. A separate date-aware section, `Stale since last update`, flags non-terminal nodes (including suppressed ones) where a later-lettered owner_exq sibling reached terminal state or a confirmed failure_autopsy touching the node's `unblocks_claims` post-dates the node's `last_updated` -- the class of staleness that hid goal_pipeline:GAP-2 on 2026-06-03. The report also flags plans missing a top-level `closure_plan.last_updated` field.

Warn-only -- this script never blocks the governance pipeline.

## Drifted nodes (0)

_None._

## Suppressed (legitimately non-terminal) (9)

Nodes whose `owner_exq` reached a terminal state but where suppression rules say the node is legitimately non-terminal (Case-3 self-tag or non-contributory manifest evidence_direction). Listed here for audit; not counted as drift.

| plan | node | status | owner_exq | suppress reason |
|------|------|--------|-----------|-----------------|
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-B` | in-progress | V3-EXQ-654 TERMINAL FAIL 2026-06-09T08:18Z (non_contributory, confirmed failure_autopsy_V3-EXQ-654_2026-06-09): C1c readiness FAIL (CandidateRuleField cold-started per episode) gated out the C2 falsifier DV -- NOT a falsification. NEXT: /implement-substrate amend ree_core/policy/candidate_rule_field.py cross-episode rule persistence (impl target ARC-063), then re-queue 654a with a trained-bias-head P1 arm + propagation non-vacuity precondition. | manifest_evidence_direction=non_contributory |
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-H` | partial | V3-EXQ-604c PASS 2026-06-07 closed the Q-044/MECH-314-family GAP-A-ready leg; V3-EXQ-544/545/544a historical diagnostics; Q-045/MECH-313/MECH-260 leg awaits behavioral_diversity_isolation:GAP-C / V3-EXQ-603i; GAP-B successor still owed | case_3_self_tag |
| commitment_closure_plan.md | `commitment_closure:GAP-4` | in-progress | V3-EXQ-460b..468b (Phase 4/5 *b cohort; MECH-342 ecological = V3-EXQ-629) | case_3_self_tag |
| commitment_closure_plan.md | `commitment_closure:GAP-8` | in-progress | V3-EXQ-485c + V3-EXQ-485b (co-equal sibling diagnostics, both PASS, reviewed 2026-06-04; representation-level MECH-263 functional-signature validation -- 485c task-role discrimination + 485b devaluation sensitivity; NOT a supersession lineage) | case_3_self_tag |
| goal_pipeline_plan.md | `goal_pipeline:GAP-4` | in-progress | V3-EXQ-490k TERMINAL 2026-06-04 (modulatory-sufficiency argmin-flip probe; ran PASS/probe_ran but non_contributory per confirmed failure_autopsy_V3-EXQ-490k -- ROW_2_fires_but_never_flips, mech295_bias_range_mean=0.0 so argmin cannot flip BY CONSTRUCTION; reviewed /governance 2026-06-04 pm); NEXT successor V3-EXQ-490L on enriched substrate with a pre-registered mech295_bias_range_mean>0 guard. Prior: V3-EXQ-490j TERMINAL 2026-05-31 (severed-bridge baseline; modulatory-not-necessary established at substrate-firing layer; supersedes 490i); lineage V3-EXQ-490g (FAIL 2026-05-29 cohort autopsy), V3-EXQ-490h FAIL silent-drop 2026-05-30 (runner bug 41c3411), V3-EXQ-490i (superseded by 490j) | case_3_self_tag |
| self_attribution_plan.md | `self_attribution:GAP-1` | blocked | V3-EXQ-445h | case_3_self_tag |
| sleep_substrate_plan.md | `sleep_substrate:GAP-2` | upstream-blocked | V3-EXQ-265a | case_3_self_tag |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-A` | in-progress | V3-EXQ-649 PASS 2026-06-07T13:14Z (GAP-A shared-channel substrate-readiness VALIDATED READY; consumed cand_world_summaries spread 0.090>=0.05 floor); V3-EXQ-567 (PASS); V3-EXQ-569 + V3-EXQ-573 (non_contributory); V3-EXQ-570 + V3-EXQ-571 + V3-EXQ-609 diagnostics landed; V3-EXQ-544a completed_supports 2026-05-30; V3-EXQ-569c claimed 2026-05-30 | manifest_evidence_direction=non_contributory |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-B` | partial | V3-EXQ-614e autopsy applied 2026-06-07 (non_contributory substrate_ceiling; GAP-A blocker moved upstream); V3-EXQ-649 GAP-A readiness PASS; MECH-341 GAP-A-ready retest owed, not queued | case_3_self_tag |

## Stale since last update -- review (0)

_None._

## Plans missing `closure_plan.last_updated` (0)

_None._

