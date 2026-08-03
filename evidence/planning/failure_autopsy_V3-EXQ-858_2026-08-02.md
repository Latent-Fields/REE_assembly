# Failure Autopsy: V3-EXQ-858 (ARC-062/MECH-309, GOV-FANOUT-1 Leg P-B, F-weight attenuation ladder)

**Generated:** 2026-08-02T09:49:33Z
**Run:** `v3_exq_858_arc062_pb_fweight_attenuation_ladder_committed_class_entropy_20260802T023831Z_v3`
**Queue ID:** V3-EXQ-858
**Claim IDs:** none (`claim_ids=[]` by design — diagnostic, brake-exempt, matching V3-EXQ-851/859's own convention)
**Status:** confirmed
**Flagged in `pending_review.md`** as "Diagnostic adjudication required (self-route unverified)" — `precondition_unmet`.
**Read alongside:** `failure_autopsy_V3-EXQ-851_2026-08-01.md` (structural template, including its 2026-08-01T21:19:59Z addendum, which predicted this run's outcome before it landed) and `failure_autopsy_V3-EXQ-859_2026-08-01.md` (short-budget diagnostic that left the question ambiguous)

## 1. Facts

**Design.** GOV-FANOUT-1 Leg P-B (H2: F-dominance, downstream of selection). Structural descendant of V3-EXQ-851 (Leg P-A): same matched stack (SP-CEM, GAP-A candidate summaries, MECH-448 rank-preserving F→eligibility demotion, MECH-449 active Go/No-Go opponency, CRF/LateralPFCAnalog rule-apprehension with `lateral_pfc`-routed channel), but sweeps `agent.e3.config.f_weight` across a 4-rung ladder {1.0, 0.5, 0.25, 0.0} instead of 851's ON/OFF `use_candidate_rule_field` split, with CRF held ON as a matched constant at every rung. Primary DV: paired-by-seed committed-class entropy (C2: F000 vs F100 lift, margin 0.05 nats, ≥2/3 seeds required). 3 seeds (42/43/44), matching V3-EXQ-851's own seeds.

**Outcome:** FAIL. Self-route: `substrate_not_ready_requeue`. `elapsed_seconds: 50037` (~13.9 hours). Confirmed non-dry via `check_dry_run_citations.py`.

**Readiness (8 sub-gates, C1a-h; C1_holds requires all 8 to hold on all 4 rungs at majority-of-seeds-per-rung):**

| Gate | Holds (all rungs)? |
|---|---|
| C1a class_axis_exercisable | true |
| C1b gapa_consumed_summary_divergence | true |
| C1c crf_differentiated_matured | true |
| C1d propagation_non_vacuity | true |
| **C1e mech448_demotion_lever_live_and_excluding** | **false (0/3 seeds at F100/F050, 1/3 at F025, 2/3 at F000)** |
| **C1f mech449_active_nogo_live_and_suppressing** | **false (identical pattern to C1e)** |
| **C1g lateral_pfc_route_range_supra_floor_and_sample_adequate** | **false (1/3 at F100, 0/3 at every other rung)** |
| C1h f_weight_knob_live | true |

**C2 (primary, load-bearing):** committed-class entropy lift F000 − F100, per seed: seed42 **+0.0903** (clears 0.05 margin), seed43 **−0.0032** (flat/null), seed44 **+0.0484** (just under the 0.05 margin). `C2_n_lift_seeds=1` of the required 2 — FAIL on its own count-based criterion, but suppressed behind the C1 readiness gate regardless.

## 2. This is the same compound-gate artifact 851's addendum already predicted — now confirmed directly

**851's autopsy (2026-08-01) found C1e/C1f/C1g all "measured 0.0" and initially read this as MECH-448/449 being completely dead under `lateral_pfc` routing.** A same-day addendum (2026-08-01T21:19:59Z, written *before* 858 had landed) corrected this: the "0.0" is a compound-gate artifact — the precondition requires `active_frac ≥ 0.8` **and** `excluded_count/suppressed > 0` **simultaneously on every rung**, but the raw per-seed data showed the mechanisms genuinely engaged (excluded_count 17–29, suppression 1.5–12.2 — matching the healthy V3-EXQ-654j baseline in *magnitude*) at a **reduced duty cycle** (24–58% of P2 ticks, not the ~100% seen under `cand_world_summary` routing). The addendum explicitly named V3-EXQ-858 as the run that would supply the missing full-budget confirmation of this prediction.

**858's raw per-cell data confirms it exactly.** Pulling `f_eligibility_demotion_active_frac`, `f_eligibility_excluded_count_mean`, `go_nogo_active_frac`, and `go_nogo_suppressed_per_tick_mean` from all 12 seed×rung cells:

| seed | f_wt | demot_frac | excl_mean | nogo_frac | nogo_supp |
|---|---|---|---|---|---|
| 42 | 1.0 | 0.643 | 17.80 | 0.643 | 1.84 |
| 43 | 1.0 | 0.240 | 28.04 | 0.240 | 13.06 |
| 44 | 1.0 | 0.778 | 24.11 | 0.778 | 7.73 |
| 42 | 0.5 | 0.632 | 18.10 | 0.632 | 1.67 |
| 43 | 0.5 | 0.242 | 28.99 | 0.242 | 13.13 |
| 44 | 0.5 | 0.619 | 23.51 | 0.619 | 7.57 |
| 42 | 0.25 | 0.609 | 18.11 | 0.609 | 1.74 |
| 43 | 0.25 | 0.241 | 27.80 | 0.241 | 11.95 |
| 44 | 0.25 | 0.808 | 21.62 | 0.808 | 5.88 |
| 42 | 0.0 | 0.843 | 18.51 | 0.843 | 2.02 |
| 43 | 0.0 | 0.243 | 27.96 | 0.243 | 11.99 |
| 44 | 0.0 | 0.808 | 21.62 | 0.808 | 5.88 |

**`active_frac` never drops below 0.24 in a single cell, and `excluded_count_mean`/`nogo_supp` sit squarely in 851's own "when active" range (17.0–28.3 / 1.5–12.2).** No seed clears the 0.8 floor on *all four rungs simultaneously* (seed 43 never exceeds 0.243 on any rung; seed 42 clears 0.8 only at F000; seed 44 clears it at F025/F000 but not F100/F050) — which is exactly why the compound AND-across-rungs-AND-across-seeds count reads 0.0, despite every single cell showing a robustly live mechanism. This is not a substrate-readiness failure; it is a specification defect in how "live on every rung" is being counted.

**C1g (lateral_pfc route range) is a genuinely different, more real finding.** `modulatory_channel_route_range_mean` is sub-floor (<0.01) in 9 of 12 cells, and even where "active" the magnitude sits right at the floor (0.0116, 0.0435). This is not a duty-cycle artifact — the injected channel's magnitude itself looks marginal at every rung.

**CORRECTION (2026-08-03, `failure_autopsy_V3-EXQ-863-route-decomp-gate_2026-08-02`):** the sentence above originally cited this as "corroborating 851's own §5 observation of a near-zero-range injected channel that could still be destabilizing downstream candidate scoring/selection dynamics." That citation does not hold: 851's near-zero `modulatory_channel_route_range_mean` (and 863's, and 859's) is now traced to a confirmed code defect — `agent.py`'s `lateral_pfc`/`curiosity`/`gated_policy`/`mech295` routing channels are populated only when the unrelated diagnostic flag `agent.e3.e3_score_decomp_enabled` is set, which 851/859/863's driver scripts never do, so `channel_route_bias` stayed `None` on literally every cell of those three runs (route range/active_frac exactly `0.0`, not "near-zero"). That is qualitatively different from this run's finding: **858's driver correctly sets `agent.e3.e3_score_decomp_enabled = True` (line 694), so its channel genuinely engages** — the 9-of-12-cells sub-floor reading here is real, independent evidence of a weak (not absent) injected signal, standing on 858's own data rather than on 851's now-explained non-engagement. This does not change 858's own conclusion (still a genuinely different, more real finding than the C1e/C1f duty-cycle artifact above) — only the corroborating citation to 851 is withdrawn.

## 3. The suppressed C2 result is worth surfacing, not discarding

Because C1_holds is false, the driver's self-route discards C2 entirely behind `substrate_not_ready_requeue`. Given the corrected reading above (MECH-448/449 genuinely engaged, not dead), C2's own result is informative: **2 of 3 seeds show a positive committed-class-entropy lift in the H-f-dominance-predicted direction** (seed42 +0.090 nats, clearing the margin; seed44 +0.048, just under it), with seed43 flat/slightly negative (−0.003). This is a near-miss in the predicted direction, not a null — worth weighing alongside V3-EXQ-863 (the `route_source='none'` comparator, already queued but deprioritized) rather than treated as uninformative.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | `claim_ids=[]` by design |
| Biological reference | not load-bearing | diagnostic |
| Prerequisites | present | candidate-generation, CRF, f_weight-knob machinery all confirmed live (C1a-d, C1h all hold) |
| Implementation | correctly wired | reuses 851's structural machinery verbatim per the driver's own note |
| Environment | same seeds as 851 | rules out seed variance as an explanation |
| **Measurement** | **under-instrumented / test-design defect** | the C1e/C1f compound gate (all-rungs-simultaneous AND active_frac≥0.8 AND excluded/suppressed>0) reads a robustly-engaged mechanism as "dead" because duty cycle alone, not magnitude, drives the "0.0" reading |
| Integration | same causal candidate as 851 (route-source / duty-cycle interaction) | mechanism for the duty-cycle reduction itself still not identified |
| Scale | C2 underpowered at n=3 seeds for a near-miss effect | 2/3 in the predicted direction, 1/3 clears the formal margin |

## 5. Learning extracted

1. **A compound AND-across-rungs precondition can read a robustly-engaged mechanism as completely dead** if duty cycle (not magnitude) varies across seeds/rungs and no single seed simultaneously clears the floor everywhere — the same failure class 851's addendum diagnosed, now confirmed to recur identically in a structural descendant.
2. **A prior autopsy's addendum can correctly predict a not-yet-run experiment's outcome** — 851's addendum (written before 858 landed) named the exact pattern 858 would show; this is worth treating as a validated diagnostic method for this GOV-FANOUT-1 lineage, not a one-off coincidence.
3. **C1g (route-range) and C1e/C1f (demotion/no-go) are diagnostically distinct** even though all three read "0.0" under the same driver: C1g looks like a genuine near-zero-magnitude signal, while C1e/C1f are duty-cycle artifacts at preserved magnitude. Lumping all three into one "substrate not ready" verdict obscures this difference.
4. A suppressed C2 result behind a misfiring readiness gate can still carry information (here: a 2/3-seeds-positive near-miss) that a blind "requeue, don't read the data" response would discard.

## 6. Routing (user-confirmed 2026-08-02)

**User confirmed:** category `measurement_test_design_defect` (matching 851's own classification), fix the gate spec; surface the C2 near-miss as suggestive pending V3-EXQ-863.

**Recommended `epistemic_category`:** `measurement_test_design_defect` (not `substrate_ceiling` — the mechanisms are demonstrably live at preserved magnitude; this is a scoring-specification defect).

**Recommended routing: `/queue-experiment`** — recommend the GOV-FANOUT-1 P-A/P-B/P-C/P-D readiness-gate specification (851, 858, and any future legs sharing this template) be amended to score C1e/C1f as duty-cycle **magnitude when active** (i.e., `excluded_count_mean`/`nogo_supp` conditioned on active ticks) rather than an AND-across-4-rungs simultaneous floor, which no single seed can be expected to clear when duty cycle itself varies 0.24–0.84 across seeds. This is a driver/spec fix, not a re-run of the same design. C1g should be treated as a separate, standing concern about the `lateral_pfc` channel's injected magnitude, worth a small targeted check independent of this ladder.

**Do not requeue V3-EXQ-858's own design as-is** — a fresh run under the same compound-gate spec would very likely reproduce "0.0" again for the same specification reason, wasting another ~14-hour allocation. V3-EXQ-863 (already queued, `route_source='none'` comparator) should be allowed to complete and be read alongside this run and the corrected gate spec once available.

Re-derive brake: this autopsy's own recommended category (`measurement_test_design_defect`) is not `substrate_ceiling`. `claim_ids=[]`, matching 851/859's own convention — brake does not apply (no claim to brake against). Consistent with 851's own routing.

Granularity-debt recurrence trigger: checked via `granularity_debt_cluster.py ARC-062` / `MECH-309` — large prior history (mostly `substrate_ceiling`, `intact` alignment), no target reads `weakened`. Does not fire; this is a well-tracked standing GOV-FANOUT-1 investigation, not new granularity debt.
