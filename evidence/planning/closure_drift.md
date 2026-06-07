# Closure-Plan Drift Report

Generated: 2026-06-07T04:29:30Z

This report flags closure_plan nodes whose `owner_exq` has reached a terminal state (manifest landed and / or failure_autopsy artifact present) but whose `status` is still non-terminal. Nodes that self-tag as Case 3 (legitimately non-terminal pending upstream substrate or successor EXQs) and nodes whose owner_exq manifest is non-contributory / superseded / inconclusive are recorded under Suppressed instead, not Drifted. A separate date-aware section, `Stale since last update`, flags non-terminal nodes (including suppressed ones) where a later-lettered owner_exq sibling reached terminal state or a confirmed failure_autopsy touching the node's `unblocks_claims` post-dates the node's `last_updated` -- the class of staleness that hid goal_pipeline:GAP-2 on 2026-06-03. The report also flags plans missing a top-level `closure_plan.last_updated` field.

Warn-only -- this script never blocks the governance pipeline.

## Drifted nodes (0)

_None._

## Suppressed (legitimately non-terminal) (6)

Nodes whose `owner_exq` reached a terminal state but where suppression rules say the node is legitimately non-terminal (Case-3 self-tag or non-contributory manifest evidence_direction). Listed here for audit; not counted as drift.

| plan | node | status | owner_exq | suppress reason |
|------|------|--------|-----------|-----------------|
| commitment_closure_plan.md | `commitment_closure:GAP-4` | in-progress | V3-EXQ-460b..468b (Phase 4/5 *b cohort; MECH-342 ecological = V3-EXQ-629) | case_3_self_tag |
| commitment_closure_plan.md | `commitment_closure:GAP-8` | in-progress | V3-EXQ-485c + V3-EXQ-485b (co-equal sibling diagnostics, both PASS, reviewed 2026-06-04; representation-level MECH-263 functional-signature validation -- 485c task-role discrimination + 485b devaluation sensitivity; NOT a supersession lineage) | case_3_self_tag |
| goal_pipeline_plan.md | `goal_pipeline:GAP-4` | in-progress | V3-EXQ-490k TERMINAL 2026-06-04 (modulatory-sufficiency argmin-flip probe; ran PASS/probe_ran but non_contributory per confirmed failure_autopsy_V3-EXQ-490k -- ROW_2_fires_but_never_flips, mech295_bias_range_mean=0.0 so argmin cannot flip BY CONSTRUCTION; reviewed /governance 2026-06-04 pm); NEXT successor V3-EXQ-490L on enriched substrate with a pre-registered mech295_bias_range_mean>0 guard. Prior: V3-EXQ-490j TERMINAL 2026-05-31 (severed-bridge baseline; modulatory-not-necessary established at substrate-firing layer; supersedes 490i); lineage V3-EXQ-490g (FAIL 2026-05-29 cohort autopsy), V3-EXQ-490h FAIL silent-drop 2026-05-30 (runner bug 41c3411), V3-EXQ-490i (superseded by 490j) | case_3_self_tag |
| self_attribution_plan.md | `self_attribution:GAP-1` | blocked | V3-EXQ-445h | case_3_self_tag |
| sleep_substrate_plan.md | `sleep_substrate:GAP-2` | upstream-blocked | V3-EXQ-265a | case_3_self_tag |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-B` | partial | V3-EXQ-614d (terminal 2026-06-03: PASS C1/C3, FAIL C2; diagnostic/scoring-excluded; supersedes 614c; reviewed 2026-06-03 -- within-class temperature lever ACTIVE but ZERO committed-action authority; see governance_2026_06_03); V3-EXQ-614c (queued 2026-06-01 via /implement-substrate amend session; 4-arm within-class temperature sweep stratified_within_class_temperature in {None=legacy, 0.5, 1.0, 2.0} on SD-056-amended baseline; cross-plan beneficiary arc_062_rule_apprehension:GAP-B); V3-EXQ-614b FAIL_no_criterion 2026-05-31 (C1=False structural degeneracy + C2=0.087 below threshold + C3=True ALL_ON 0.800 nats; per-claim non_contributory on MECH-341 + ARC-065 via /governance; routed to amend per failure_autopsy_V3-EXQ-616 Sections 7 + 10 contingent path); V3-EXQ-614b (queued 2026-05-31T12:32Z via /queue-experiment; 3-arm behavioural re-run on SD-056-amended substrate, supersedes V3-EXQ-614a; 5 SD-056 amend lever flags applied uniformly across all 3 arms: e2_action_contrastive_multistep_enabled=True h=5, e2_rollout_output_norm_clamp_enabled=True ratio=2.0, e2_action_contrastive_enabled=True weight=0.01; same env_kwargs + acceptance criteria as 614a; 4-row interpretation grid copied verbatim + header note that under amended substrate PASS via C1 is now the load-bearing target since 614a established PASS via C2+C3); V3-EXQ-614a (queued 2026-05-30 via /diagnose-errors cluster-absorb post 41c3411 runner fix; 3-arm behavioural falsifier, same script as 614); V3-EXQ-608 (P2 PASS); V3-EXQ-611 FAIL 2026-05-27T13:02Z (C1 substrate-readiness false: entropy_max_abs << gap range + stratified_fired=0 committed-only); V3-EXQ-611c PASS 2026-05-29T18:45Z (6-arm retune, supersedes V3-EXQ-611b manifest-recovery; C1 stratified_fires=true all OPT2/BOTH arms; C3 selected-class diversity=true all 6 arms; C4 monotone in scale=true; R2c_readiness=true all arms; C2 entropy_bonus_scale_commensurate=false but interpretation grid routes PASS_with_C1_and_C3 directly to behavioural successor); V3-EXQ-614 LOST to manifest-pipeline silent-drop cluster 2026-05-29T19:13:19Z (coordinator status=completed + zero results-table row, same signature as V3-EXQ-490h / V3-EXQ-592b autopsied 2026-05-30T06:02Z; runner-side fix ree-v3 commit 41c3411 already landed) | case_3_self_tag |

## Stale since last update -- review (0)

_None._

## Plans missing `closure_plan.last_updated` (0)

_None._

