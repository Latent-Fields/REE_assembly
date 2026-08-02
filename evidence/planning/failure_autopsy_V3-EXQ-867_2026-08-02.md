# Failure Autopsy: V3-EXQ-867 (MECH-321 harm-aware selection, task effect)

**Generated:** 2026-08-02T10:50:16Z | **Status:** confirmed | **Scope:** single

## Facts

- Run: `v3_exq_867_mech321_harm_aware_selection_task_effect_20260802T031937Z_v3`, FAIL, claim MECH-321.
- Successor to V3-EXQ-844 (confirmed `failure_autopsy_V3-EXQ-844_2026-08-01`), which found MECH-321's abort mechanism engages correctly (C2 passes) but `_apply_policy_decomposition` had no harm-valence signal and no ranked-selection step -- a code-verified structural gap.
- That gap was CLOSED 2026-08-01 (chip-20260801-hazard-aware-decomp-build): `SD-hazard-aware-policy-decomposition` implemented (`PolicyDecomposition.harm_bias()` Stage 1 graded + `.select_harm_aware_leaves()` Stage 2 categorical override), default-off/bit-identical, 32 pre-existing + 11 new contracts pass. `substrate_queue.json` entry status=`implemented`, ready=true.
- 867 is the first behavioural-effect test: ARM_SELECTION_OFF vs ARM_SELECTION_ON (harm-aware selection on), both arms with MECH-321's abort mechanism ON (844's own axis held fixed). Design explicitly anticipated this exact failure mode in its own docstring: "a below-floor reading here must self-route `substrate_not_ready_requeue`... never a C1 verdict on a manipulation that never engaged."
- Result: P0 precondition `harm_bias_engages` FAILED for ARM_SELECTION_ON. `decomp_n_harm_bias_nonzero=0` and `decomp_n_harm_override_fires=0` in **every one of 12 per-seed rows** (6 seeds x 2 arms). The 3 `both_decompose` seeds (3/71/89) show identical `off_decomp_n_decomposed_midexec`/`on_decomp_n_decomposed_midexec` and zero abort-count delta; the 3 `neither_decompose` seeds show `action_sequences_identical: true`. `n_windowed_pairs=0`.
- Self-route: `manipulation_inert_or_unmatched` (readiness gates besides harm_bias_engages all green; no seed showed a resulting action-sequence divergence). Correctly diagnosed by the driver's own design, not a mislabel.
- Config carries no hazard-density overlay keys (`scheduled_external_hazard_*`, `limb_damage_enabled` all absent) -- run used the default baseline env, matching the already-documented SD-037/V3-EXQ-620 finding that the untuned "fishtank baseline" produces near-zero z_harm_a signal (all 6 measured quantities pooled to 0.0 across 3 seeds).

## Claim-layer mapping

MECH-321: `pending_retest_after_substrate: true` (comment: "awaiting SD-hazard-aware-policy-decomposition build") -- 867 IS that retest, but the retest could not run because the ENVIRONMENT, not the substrate, was not ready. The test did not let the claim express itself in either direction.

## Biological-reference triage

Threat-modulated defensive path-selection (Fanselow/Mobbs, per 844's lit-pull) -- reference is already established and unchanged. No new biology gap; this is a pure environment-density issue.

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | manipulation never engaged; not weighted either direction |
| Biological reference | clear | unchanged from 844 |
| Prerequisites | present | SD-hazard-aware-policy-decomposition implemented+ready |
| Implementation | complete | harm_bias()/select_harm_aware_leaves() wired, contracts pass |
| Environment | **inadequate** | no hazard-density tuning; z_harm_a_norm never cleared threat_floor=0.1 |
| Measurement | adequate | precondition design correctly caught the inert manipulation |
| Integration | n/a | |
| Scale | n/a | |

## Learning extracted

1. The build closed 844's gap correctly -- the readiness design worked exactly as intended.
2. Building a mechanism does not guarantee the environment presents its triggering condition; environment-adequacy is a distinct readiness axis from implementation-completeness.
3. SD-029's scheduled_external_hazard overlay (already built, specified in SD-037 Phase 1b) is the known fix -- no new code needed.

## Routing

**epistemic_category:** `environment_adequacy_defect` | **evidence_direction:** `non_contributory` | **routing:** `/queue-experiment` 867a with SD-029 hazard-density overlay applied, plus a cheap preflight assertion (`decomp_n_harm_bias_nonzero>0` in a pilot rollout) before the full 6-seed design runs. No substrate build needed (`recommended_substrate_queue_entry.action = "none"`).

**User gate (2026-08-02):** Approved as recommended.
