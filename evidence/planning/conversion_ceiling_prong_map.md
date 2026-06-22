# Conversion-Ceiling Prong Map (instance #1 of `prong_map_pattern.md`)

- **Registered:** 2026-06-22
- **Campaign node:** `conversion_ceiling_campaign` (see `conversion_ceiling_campaign_plan.md`)
- **Owning substrate entry:** `f_dominance_conversion_ceiling` (substrate_queue.json) — its 6-rung `fallback_ladder` is the lever inventory; this map is the parallel-campaign view over it.
- **Problem:** per-candidate diversity exists at the proposer/scoring layer but collapses at committed action (`committed_action_class_entropy ~ 0`). Four mechanistically-distinct roots share this symptom (root taxonomy: `conversion_ceiling_phase0_synthesis_2026-06-18.md`). Root B (F-dominance, MECH-439) is the umbrella; the faces below are parallel surfaces.

## Standing rationale (why the full-stack test, not more letters)

The selection face is now **exhausted lever-by-lever**: Factor A inert (689a), **Factor B refuted (689c, 2026-06-21)**, demotion fails C2 alone (654i), Go/No-Go fails C2 alone (654j). Per the assembly-vs-closure principle, per-lever C2 failures are **not** a verdict that the ceiling is unliftable — they motivate the hypothesis that conversion is **emergent from the assembled stack**, and/or that the true bottleneck is a *different face* (commit-duration, root C). The campaign's real test is the **co-armed full-stack arm**, not another isolated falsifier.

## Faces (one module each — this is what enables parallelism)

| Face | Module | Role |
|---|---|---|
| Selection | `ree-v3/ree_core/predictors/e3_selector.py` | which action class wins the committed argmin |
| Commit-duration | commitment-closure-control-plane + `agent.py` latch + `ree_core/policy/natural_commit_urgency.py` | how long F latches a commit (de-commit authority) |
| Valuation input | `OFCAnalog` / `agent.ofc` | the value signal feeding F |

## Prong inventory (mapped to lifecycle)

| Prong | Face | Flag | State | Own-face validation | Composition-readiness gap |
|---|---|---|---|---|---|
| **P1 — Factor B** (gap-scaled commit-T) | selection | `use_gap_scaled_commit_temperature` | **REFUTED** at own face (689c FAIL) | 689c FAIL — C_PRIMARY 1/3, C_GAPBLIND_B 0/3 | **DROPPED** from full-stack |
| **P-dem — MECH-448 demotion** | selection | `use_f_eligibility_demotion` | **face-validated** (689d PASS) | 689d PASS (0.938 vs 0.371) | needs P-dem x P-gng interaction characterized |
| **P-gng — MECH-449 Go/No-Go** | selection | `use_go_nogo_constitution` | **face-validated** (689g PASS 3/3) | 689g PASS | needs P-dem x P-gng interaction characterized |
| **P-floor — adaptive floor** | selection | `use_f_eligibility_adaptive_floor` | face-validated (689e PASS) | 689e PASS | matched-stack constant (carried with demotion) |
| **P-comp — demotion x Go/No-Go composition** | selection | (both flags ON) | **design** (own experiment — decision 2026-06-22) | *to build*: do they compound or cancel at C2? | IS the within-face composition characterization gate |
| **P2 — Root C de-commit** (MECH-445/446) | commit-duration | (de-commit lever; not yet a stable flag) | **design / PARKED** | *to build then validate*: pre/post-closure occupancy DV | blocked on the closure-exclusive de-commit eval substrate build |
| **P3 — OFC valuation decouple** (SD-033b/MECH-263) | valuation | `use_ofc_devaluation_head` | **build in flight** (V3-EXQ-485m running, cloud-4) | await 485m result -> face-validate | await 485m |
| P4 — candidate-differentiated affect | valuation | (per-candidate modulatory variance) | design (643 autopsy seed) | not yet specified | not on critical path |
| P5 — rungs 3-5 (divisive-norm / output-null / QD archive) | selection | (various) | V4-leaning, recoupable to V3 if required | not yet | not yet |

## Composition matrix

- **Across faces** (selection <-> commit-duration <-> valuation): **compose clean** — different modules, co-armable, no collision. Concurrent runs allowed now.
- **Within the selection face** (demotion x Go/No-Go [x floor]): **interaction unknown -> must characterize** (P-comp, its own experiment). We know Factor A x Factor B *cancelled* (689a); we do **not** know whether demotion and Go/No-Go compound or cancel at C2. This is the main open selection-face question now that Factor B is dead.

## Full-stack target arm — the real test of MECH-309 / ARC-062

- **Matched stack ON both arms** (each lever included only once composition-ready): demotion + Go/No-Go + adaptive-floor + [root-C de-commit, once built+validated] + [OFC-decouple, once 485m validates]. **Factor B excluded (refuted).**
- **Swept variable:** `use_candidate_rule_field` (the GAP-B rule-apprehension bias). **DV:** committed-class entropy (C2).
- **Baseline (per-prong discipline):** the composite carries its **own dedicated all-stack-ON / swept-var-OFF** control. No shared frozen baseline.
- **PASS** -> the assembled substrate converts -> supports MECH-309/ARC-062, closes `behavioral_diversity_isolation:GAP-I`.
- **FAIL** -> leave-one-out ablation across the included faces to localize the missing/blocking face.

## Critical path (post-689c)

1. **P-comp** (demotion x Go/No-Go composition at C2) — runnable **now** (uses only built+face-validated levers); the main live selection-face question.
2. **P3** (OFC) — 485m **running**; folds in on validation.
3. **P2 (root C)** — the **live V3 critical path**: build the closure-exclusive de-commit eval substrate (dissociates natural-commit from closure-de-commit) -> face-validate -> include. This is the long pole and, post-689c, the most likely true bottleneck (commit-duration, not selection).
4. **Full-stack arm** assembled once P-comp + P3 + P2 are composition-ready.

## Cross-refs

- substrate_queue `f_dominance_conversion_ceiling` `fallback_ladder` (rungs 1-6; rung 6 = root C, tagged PARALLEL).
- `conversion_ceiling_phase0_synthesis_2026-06-18.md` (four-root taxonomy + campaign status ladder).
- Autopsies: `failure_autopsy_V3-EXQ-654i_2026-06-22` (demotion C2 fail), `failure_autopsy_V3-EXQ-654j_2026-06-22` (Go/No-Go C2 fail), `failure_autopsy_V3-EXQ-460j_2026-06-21` (root C park), and the 689c Factor-B refutation reconcile.
- **Reverse wiring (landed 2026-06-22):** substrate_queue `f_dominance_conversion_ceiling` now carries `prong_map` + `campaign_plan` fields pointing back here (the parallel-campaign view is discoverable from the lever inventory). This was deferred in the formalization pass while a concurrent session held a claim on substrate_queue.json reconciling the 689c Factor-B routing (that reconcile landed at `a0fc6893de`); the back-pointer was then added.
