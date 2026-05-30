# Closure-Plan Drift Report

Generated: 2026-05-30T11:44:39Z

This report flags closure_plan nodes whose `owner_exq` has reached a terminal state (manifest landed and / or failure_autopsy artifact present) but whose `status` is still non-terminal. It also flags plans missing a top-level `closure_plan.last_updated` field.

Warn-only -- this script never blocks the governance pipeline.

## Drifted nodes (2)

| plan | node | status | owner_exq | node last_updated | terminal signal |
|------|------|--------|-----------|-------------------|-----------------|
| self_attribution_plan.md | `self_attribution:GAP-1` | blocked | V3-EXQ-445h | 2026-05-30 | manifest `evidence/experiments/v3_exq_445h_sd032b_dacc_reef/v3_exq_445h_sd032b_dacc_reef_20260508T063313Z_v3.json` |
| sleep_substrate_plan.md | `sleep_substrate:GAP-2` | upstream-blocked | V3-EXQ-265a | 2026-05-30 | manifest `evidence/experiments/v3_exq_265a_sd017_sleep_phase_methods_validation_phase2_20260509T201256Z_v3.json` |

## Plans missing `closure_plan.last_updated` (0)

_None._

