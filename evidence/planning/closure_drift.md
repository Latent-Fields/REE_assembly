# Closure-Plan Drift Report

Generated: 2026-05-30T07:01:14Z

This report flags closure_plan nodes whose `owner_exq` has reached a terminal state (manifest landed and / or failure_autopsy artifact present) but whose `status` is still non-terminal. It also flags plans missing a top-level `closure_plan.last_updated` field.

Warn-only -- this script never blocks the governance pipeline.

## Drifted nodes (7)

| plan | node | status | owner_exq | node last_updated | terminal signal |
|------|------|--------|-----------|-------------------|-----------------|
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-B` | blocked | V3-EXQ-543l | 2026-05-29 | manifest `evidence/experiments/v3_exq_543l_arc062_mode_separation_gap_b_falsifier_20260526T023059Z_v3.json` + autopsy `evidence/planning/failure_autopsy_V3-EXQ-543l_2026-05-27.json` |
| infant_substrate_plan.md | `infant_substrate:GAP-11` | blocked | V3-EXQ-588b | 2026-05-29 | manifest `evidence/experiments/v3_exq_588b_goal_seeding_pipeline_diagnostic/v3_exq_588b_goal_seeding_pipeline_diagnostic_20260521T053758Z_v3.json` |
| infant_substrate_plan.md | `infant_substrate:GAP-13` | blocked | V3-EXQ-590 | 2026-05-29 | manifest `evidence/experiments/v3_exq_590_isef004_novelty_bonus_goldilocks/v3_exq_590_isef004_novelty_bonus_goldilocks_20260525T084057Z_v3.json` |
| infant_substrate_plan.md | `infant_substrate:GAP-14` | blocked | V3-EXQ-591 | 2026-05-29 | manifest `evidence/experiments/v3_exq_591_isef005_curriculum_vs_flat/v3_exq_591_isef005_curriculum_vs_flat_20260526T184231Z_v3.json` + autopsy `evidence/planning/failure_autopsy_V3-EXQ-591_2026-05-27.json` |
| self_attribution_plan.md | `self_attribution:GAP-1` | blocked | V3-EXQ-445h | 2026-05-29 | manifest `evidence/experiments/v3_exq_445h_sd032b_dacc_reef/v3_exq_445h_sd032b_dacc_reef_20260508T063313Z_v3.json` |
| sleep_substrate_plan.md | `sleep_substrate:GAP-2` | upstream-blocked | V3-EXQ-265a | 2026-05-29 | manifest `evidence/experiments/v3_exq_265a_sd017_sleep_phase_methods_validation_phase2_20260509T201256Z_v3.json` |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-B` | in_progress | V3-EXQ-608 (P2 PASS); V3-EXQ-611 FAIL 2026-05-27T13:02Z (C1 substrate-readiness false: entropy_max_abs << gap range + stratified_fired=0 committed-only); V3-EXQ-611c PASS 2026-05-29T18:45Z (6-arm retune, supersedes V3-EXQ-611b manifest-recovery; C1 stratified_fires=true all OPT2/BOTH arms; C3 selected-class diversity=true all 6 arms; C4 monotone in scale=true; R2c_readiness=true all arms; C2 entropy_bonus_scale_commensurate=false but interpretation grid routes PASS_with_C1_and_C3 directly to behavioural successor); V3-EXQ-614 LOST to manifest-pipeline silent-drop cluster 2026-05-29T19:13:19Z (coordinator status=completed + zero results-table row, same signature as V3-EXQ-490h / V3-EXQ-592b autopsied 2026-05-30T06:02Z; runner-side fix ree-v3 commit 41c3411 already landed); V3-EXQ-614a re-queue via /diagnose-errors cluster-absorb 2026-05-30 (same 3-arm script, post 41c3411 runner fix) | 2026-05-30 | manifest `evidence/experiments/v3_exq_608_mech341_e3_score_collapse_diagnostic_20260526T025832Z_v3.json` |

## Plans missing `closure_plan.last_updated` (0)

_None._

