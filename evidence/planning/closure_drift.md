# Closure-Plan Drift Report

Generated: 2026-06-01T06:18:38Z

This report flags closure_plan nodes whose `owner_exq` has reached a terminal state (manifest landed and / or failure_autopsy artifact present) but whose `status` is still non-terminal. Nodes that self-tag as Case 3 (legitimately non-terminal pending upstream substrate or successor EXQs) and nodes whose owner_exq manifest is non-contributory / superseded / inconclusive are recorded under Suppressed instead, not Drifted. The report also flags plans missing a top-level `closure_plan.last_updated` field.

Warn-only -- this script never blocks the governance pipeline.

## Drifted nodes (0)

_None._

## Suppressed (legitimately non-terminal) (4)

Nodes whose `owner_exq` reached a terminal state but where suppression rules say the node is legitimately non-terminal (Case-3 self-tag or non-contributory manifest evidence_direction). Listed here for audit; not counted as drift.

| plan | node | status | owner_exq | suppress reason |
|------|------|--------|-----------|-----------------|
| commitment_closure_plan.md | `commitment_closure:GAP-4` | in-progress | V3-EXQ-592d | case_3_self_tag |
| self_attribution_plan.md | `self_attribution:GAP-1` | blocked | V3-EXQ-445h | case_3_self_tag |
| sleep_substrate_plan.md | `sleep_substrate:GAP-2` | upstream-blocked | V3-EXQ-265a | case_3_self_tag |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-B` | partial | V3-EXQ-614b (queued 2026-05-31T12:32Z via /queue-experiment; 3-arm behavioural re-run on SD-056-amended substrate, supersedes V3-EXQ-614a; 5 SD-056 amend lever flags applied uniformly across all 3 arms: e2_action_contrastive_multistep_enabled=True h=5, e2_rollout_output_norm_clamp_enabled=True ratio=2.0, e2_action_contrastive_enabled=True weight=0.01; same env_kwargs + acceptance criteria as 614a; 4-row interpretation grid copied verbatim + header note that under amended substrate PASS via C1 is now the load-bearing target since 614a established PASS via C2+C3); V3-EXQ-614a (queued 2026-05-30 via /diagnose-errors cluster-absorb post 41c3411 runner fix; 3-arm behavioural falsifier, same script as 614); V3-EXQ-608 (P2 PASS); V3-EXQ-611 FAIL 2026-05-27T13:02Z (C1 substrate-readiness false: entropy_max_abs << gap range + stratified_fired=0 committed-only); V3-EXQ-611c PASS 2026-05-29T18:45Z (6-arm retune, supersedes V3-EXQ-611b manifest-recovery; C1 stratified_fires=true all OPT2/BOTH arms; C3 selected-class diversity=true all 6 arms; C4 monotone in scale=true; R2c_readiness=true all arms; C2 entropy_bonus_scale_commensurate=false but interpretation grid routes PASS_with_C1_and_C3 directly to behavioural successor); V3-EXQ-614 LOST to manifest-pipeline silent-drop cluster 2026-05-29T19:13:19Z (coordinator status=completed + zero results-table row, same signature as V3-EXQ-490h / V3-EXQ-592b autopsied 2026-05-30T06:02Z; runner-side fix ree-v3 commit 41c3411 already landed) | case_3_self_tag |

## Plans missing `closure_plan.last_updated` (0)

_None._

