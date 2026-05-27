# Closure-Plan Drift Report

Generated: 2026-05-27T17:42:18Z

This report flags closure_plan nodes whose `owner_exq` has reached a terminal state (manifest landed and / or failure_autopsy artifact present) but whose `status` is still non-terminal. It also flags plans missing a top-level `closure_plan.last_updated` field.

Warn-only -- this script never blocks the governance pipeline.

## Drifted nodes (13)

| plan | node | status | owner_exq | node last_updated | terminal signal |
|------|------|--------|-----------|-------------------|-----------------|
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-B` | in-progress | V3-EXQ-543l | 2026-05-27 | manifest `evidence/experiments/v3_exq_543l_arc062_mode_separation_gap_b_falsifier_20260526T023059Z_v3.json` + autopsy `evidence/planning/failure_autopsy_V3-EXQ-543l_2026-05-27.json` |
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-D` | in-progress | V3-EXQ-598 | 2026-05-27 | manifest `evidence/experiments/v3_exq_598_gap1_sd033a_bias_head_trainable_ablation_20260521T070715Z_v3.json` |
| commitment_closure_plan.md | `commitment_closure:GAP-1` | in-progress | V3-EXQ-598b | 2026-05-27 | manifest `evidence/experiments/v3_exq_598b_gap1_sd033a_bias_head_trainable_ablation_20260527T120345Z_v3.json` |
| commitment_closure_plan.md | `commitment_closure:GAP-4` | partial | V3-EXQ-592 | 2026-05-21 | manifest `evidence/experiments/v3_exq_592_gap11_pilot_committed_mode_curriculum/v3_exq_592_gap11_pilot_committed_mode_curriculum_20260521T104724Z_v3.json` |
| infant_substrate_plan.md | `infant_substrate:GAP-11` | in-progress | V3-EXQ-588b | 2026-05-21 | manifest `evidence/experiments/v3_exq_588b_goal_seeding_pipeline_diagnostic/v3_exq_588b_goal_seeding_pipeline_diagnostic_20260521T053758Z_v3.json` |
| infant_substrate_plan.md | `infant_substrate:GAP-12` | in-progress | V3-EXQ-589 | 2026-05-17 | manifest `evidence/experiments/v3_exq_589_isef003_microhabitat_latent_diversity/v3_exq_589_isef003_microhabitat_latent_diversity_20260518T134905Z_v3.json` |
| infant_substrate_plan.md | `infant_substrate:GAP-13` | in-progress | V3-EXQ-590 | 2026-05-17 | manifest `evidence/experiments/v3_exq_590_isef004_novelty_bonus_goldilocks/v3_exq_590_isef004_novelty_bonus_goldilocks_20260525T084057Z_v3.json` |
| infant_substrate_plan.md | `infant_substrate:GAP-14` | blocked | V3-EXQ-591 | 2026-05-27 | manifest `evidence/experiments/v3_exq_591_isef005_curriculum_vs_flat/v3_exq_591_isef005_curriculum_vs_flat_20260526T184231Z_v3.json` + autopsy `evidence/planning/failure_autopsy_V3-EXQ-591_2026-05-27.json` |
| self_attribution_plan.md | `self_attribution:GAP-1` | blocked | V3-EXQ-445h | 2026-05-11 | manifest `evidence/experiments/v3_exq_445h_sd032b_dacc_reef/v3_exq_445h_sd032b_dacc_reef_20260508T063313Z_v3.json` |
| sleep_substrate_plan.md | `sleep_substrate:GAP-2` | upstream-blocked | V3-EXQ-265a | 2026-05-24 | manifest `evidence/experiments/v3_exq_265a_sd017_sleep_phase_methods_validation_phase2_20260509T201256Z_v3.json` |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-A` | partial | V3-EXQ-567 (done) + V3-EXQ-569 (queued, matched-noise control) | 2026-05-26 | manifest `evidence/experiments/v3_exq_567_wpb_natural_entropy_sp_cem_20260515T212425Z_v3.json` |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-B` | in_progress | V3-EXQ-608 (P2 PASS); V3-EXQ-611 (P3 substrate-readiness diagnostic queued); B_only / ablate_B / ALL_ON behavioural falsifier TBD | 2026-05-27 | manifest `evidence/experiments/v3_exq_608_mech341_e3_score_collapse_diagnostic_20260526T025832Z_v3.json` |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-D` | in_progress | V3-EXQ-550 (manifest landed FAIL/supports MECH-269); V3-EXQ-601 (MECH-269b validation PASS 2026-05-21); R4-rule application pending governance | 2026-05-26 | manifest `evidence/experiments/v3_exq_550_zgoal_monostrategy_falsifier/v3_exq_550_zgoal_monostrategy_falsifier_20260511T201859Z_v3.json` |

## Plans missing `closure_plan.last_updated` (6)

- `evidence/planning/commitment_closure_plan.md`
- `evidence/planning/goal_pipeline_plan.md`
- `evidence/planning/self_attribution_plan.md`
- `evidence/planning/sd033_governance_plan.md`
- `evidence/planning/sleep_substrate_plan.md`
- `evidence/planning/behavioral_diversity_isolation_plan.md`

