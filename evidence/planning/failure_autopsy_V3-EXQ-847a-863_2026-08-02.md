# Failure Autopsy: V3-EXQ-847a + V3-EXQ-863 (ARC-062/MECH-309, GOV-FANOUT-1 family)

**Generated:** 2026-08-02T22:10:21Z
**Scope:** cluster (2 targets, same GOV-FANOUT-1 lineage, both landed today)
**Status:** confirmed
**Read alongside:** `failure_autopsy_V3-EXQ-847_2026-08-01.md` (847's original denominator-bug diagnosis, whose recommended fixed-forward redesign 847a is), `failure_autopsy_V3-EXQ-851_2026-08-01.md` (+ its 2026-08-01T21:19:59Z addendum), `failure_autopsy_V3-EXQ-858_2026-08-02.md`, `failure_autopsy_V3-EXQ-859_2026-08-01.md`, and `evidence/planning/arc_062_conversion_fanout_2026-07-29.md` (the portfolio design doc, including its "active_frac denominator sweep" 2026-08-02 addendum).

## 0. Pending-review flags and dry-run gate

- `v3_exq_847a_arc062_pd_context_modeswitch_committed_class_divergence_20260802T182826Z_v3` — listed in `pending_review.md` "FAIL (action required)", `(no claim tags)`.
- `v3_exq_863_arc062_lateral_pfc_route_mech448_449_full_replication_20260802T121313Z_v3` — listed in both "PASS (verify & close)" and "Diagnostic adjudication required (self-route unverified)" with self-route label `mixed_partial_result_needs_expert_review` flagged `vacuous_pass`.
- `check_dry_run_citations.py` on both run_ids: **0 dry cited, 2 clean.** Both `validate_recording.py`: OK, always-core complete, 0 gaps.

## 1. Facts

### 1a. V3-EXQ-847a (Leg P-D, H4: measurement aliasing — context-conditioned mode-switch)

**Design.** Fixed-forward redesign of V3-EXQ-847, whose autopsy (2026-08-01) confirmed a genuine denominator bug: 847's `demotion_active_ticks`/`nogo_active_ticks` numerator counted only fresh-select ticks while the denominator (`n_p2_ticks`) counted all ticks including held/latched ones — a basis mismatch, not the same defect as 851/858's carry-forward convention. 847a supersedes 847 (`supersedes: V3-EXQ-847` in the manifest) with the corrected denominator, and layers a **new context-partitioned readout** on the same matched stack: 654j-equivalent SP-CEM + GAP-A + MECH-448 demotion + MECH-449 active No-Go on both arms; swept variable `use_candidate_rule_field` (ARM_ON vs ARM_OFF). Primary DV (H4 discriminator, new): paired-by-seed lift in `tv_context_divergence` (TV distance between reef-context and open-context committed-class distributions), restricted to seeds `context_scorable` in both arms.

**Outcome: FAIL.** `interpretation_label: context_divergence_not_greater_arm_on_measurement_aliasing_ruled_out`. Readiness: **C1 = true** (all of C1a–g hold, including the corrected C1e/C1f and the new C1g context-partition-adequacy gate) — unlike 851/858, this run hit no duty-cycle artifact:

| Gate | Value |
|---|---|
| C1e demotion active_frac (ON) | **1.0** (excluded_count_mean 22.16 OFF / 22.25 ON) |
| C1f nogo active_frac (ON) | **1.0** (suppressed_per_tick_mean 6.52 OFF / 6.29 ON) |
| C1g context-scorable seeds | 2/3 both arms |

Primary DV (C2_context): paired lift on the 2 context-scorable seeds — seed42 **−0.0246**, seed43 **−0.0244** — both negative (wrong direction) and far below the 0.05-nat margin. Secondary pooled DV (C2_pooled) also fails (1/3 seeds clear, need 2). Manipulation-check (negative control): within-class representative entropy ARM_OFF 1.598 vs ARM_ON 1.553 — as expected, essentially unmoved (the rule bias is class-keyed and cannot move within-class selection), confirming the CRF manipulation is real and measured correctly even though the primary DV is null (`lateral_pfc_bias_abs_mean` 0.060 OFF vs 0.082 ON — nonzero, differentiated).

### 1b. V3-EXQ-863 (route_source isolation, full-budget replication of V3-EXQ-859)

**Design.** Full P0=200/P1=90/P2=60 episode budget (matching 851's own schedule exactly; 859 used a cheap P0=10/P2=10, no P1). Two arms differ **only** in `modulatory_channel_route_source` ('lateral_pfc' vs 'none'); `use_modulatory_channel_routing`, `use_candidate_rule_field`, `use_lateral_pfc_analog`, `lateral_pfc_train_rule_bias_head` all True on **both** arms — so `agent.lateral_pfc` is computed and trained identically on both arms; route_source controls only whether the computed bias reaches the modulatory accumulator. Tracks MECH-448 (`f_eligibility_demotion_active_frac` + `excluded_count_mean`) and MECH-449 (`go_nogo_active_frac` + `suppressed_per_tick_mean`) engagement, using the **same fresh-select-only convention as 859** (not 851/858's all-ticks-with-carry-forward convention).

**Outcome: PASS**, `interpretation_label: mixed_partial_result_needs_expert_review`, flagged `vacuous_pass` in `pending_review.md` because `criteria_non_degenerate` reads `mech448_ablation_discriminates: false` and `mech449_ablation_discriminates: false` — neither mechanism's live/dead status differs between arms.

**The raw per-seed data are bit-identical between arms, to 6 decimal places, on every logged MECH-448/449 field, on all 3 seeds:**

| seed | arm | demot_active_frac | excl_mean | nogo_active_frac | nogo_supp_mean |
|---|---|---|---|---|---|
| 42 | LPFC | 1.0 | 14.976911 | 1.0 | 0.0 |
| 42 | NONE | 1.0 | 14.976911 | 1.0 | 0.0 |
| 43 | LPFC | 1.0 | 15.801869 | 1.0 | 0.0 |
| 43 | NONE | 1.0 | 15.801869 | 1.0 | 0.0 |
| 44 | LPFC | 1.0 | 16.831294 | 1.0 | 0.0 |
| 44 | NONE | 1.0 | 16.831294 | 1.0 | 0.0 |

MECH-448 is robustly live in both arms (majority true, 3/3 seeds each). MECH-449's `active_frac` reads 1.0 in both arms but `suppressed_per_tick_mean` is exactly 0.0 in every cell — under this run's own "live" criterion that requires nonzero suppression, MECH-449 reads dead in both arms (majority false, 0/3 each), symmetrically.

## 2. Reading the bit-identical result — informative, not ambiguous

The driver's own docstring states plainly why bit-identical arms are the **expected** result if route_source has no causal effect on this readout: `'none'` matches no routing branch, leaving `channel_route_bias=None` — "bit-identical to routing being off" per the code's own comment — while every other config element (seed, env, CRF training, everything upstream of the accumulator) is identical between arms. Under fixed seeds, if `channel_route_bias` does not perturb the trajectory or the MECH-448/449 readouts specifically, the two arms are not merely *expected to be similar* — they are expected to be **exactly identical**, because nothing else differs. That is exactly what was measured, on all 3 seeds, both mechanisms.

This directly answers the two readings 859 left undistinguished (per its own docstring and the 863 driver's restatement of them):
- **(a) route_source has no causal effect on MECH-448/449 at all** — now confirmed, at **full training budget**, not just 859's cheap ~45-minute probe.
- **(b) route_source's effect is training-duration-dependent** — **ruled out**: if the effect only emerged with more training, 863's full-budget arms would have diverged; they did not, to 6 decimal places.

This closes the exact question 859's autopsy left open, and it retroactively corroborates 851's own addendum (2026-08-01T21:19:59Z): 851/858 found MECH-448/449 "collapsed" or duty-cycle-reduced specifically under `lateral_pfc` routing with no `'none'` comparator run alongside; 863 now shows that comparator produces identical statistics. Whatever drove 851's 0.24–0.58 duty-cycle range and 858's near-identical seed-correlated pattern (858's own data: seed43 sits at ~0.24 on **every** f_weight rung, seed44 at ~0.78–0.84 on every rung) is **seed-correlated, not manipulation-correlated** — consistent with both 851's `lateral_pfc`-only design and 858's `f_weight`-swept design showing the same per-seed duty-cycle fingerprint regardless of which variable was manipulated. This was already the working hypothesis from the rung-invariance in 858's own table; 863 now supplies the missing negative-manipulation control that makes it a confirmed reading rather than an inference.

**MECH-449's `suppressed_per_tick_mean == 0.0` under the fresh-select convention (vs 851/858's nonzero 1.5–13.1 under the all-ticks-with-carry-forward convention) is a separate, genuine measurement-convention discrepancy, not resolved by this autopsy.** It is plausible that most suppression events land on held/latched ticks that the carry-forward convention credits and the fresh-select convention excludes by construction — but this autopsy did not verify that mechanistically. Flagged as a follow-up note (Section 5), not a blocker to the routing below, since it does not change the route-source-isolation conclusion (both arms show the same 0.0, symmetrically).

## 3. Claim-layer mapping

Both runs carry `claim_ids: []` by design — diagnostic legs of the GOV-FANOUT-1 ARC-062/MECH-309 portfolio, matching 851/858/859's own convention (a diagnostic run in this family is explicitly not meant to move claim confidence directly; it resolves which hypothesis the *next* evidence-purpose run should target). ARC-062 (`candidate`, `v3_pending`) and MECH-309 (`candidate`, `v3_pending`) remain the eventual targets; MECH-448 (`candidate`) and MECH-449 (`provisional`) are the mechanisms under instrumentation, not directly under test themselves.

## 4. Biological-reference triage

Not separately load-bearing for either target — both are instrumentation/measurement-methodology diagnostics within an already-triaged portfolio (851/858/859's own autopsies established the biological framing: lateral-PFC rule-apprehension routing modulating F-eligibility demotion and Go/No-Go opponency, an SD-033a/CRF-lineage construct). Nothing in this autopsy's findings bears on whether the biological translation itself is sound — the question resolved here is purely instrumental (did the compound readiness gate / route-source manipulation work as intended).

## 5. Four-layer diagnosis

| Layer | 847a | 863 |
|---|---|---|
| Claim alignment | n/a (`claim_ids=[]`, pre-registered informative-null branch) | n/a (`claim_ids=[]`, diagnostic) |
| Biological reference | not load-bearing | not load-bearing |
| Prerequisites | present — C1a–g all hold cleanly | present — sample-adequacy precondition holds (min n_p2_fresh_select=1144 ≥ 600 floor) |
| Implementation | correct — corrected denominator confirmed working (active_frac=1.0 both arms, no artifact) | correct — route_source wiring behaves exactly as the driver's own docstring predicts for a null-causal-path |
| Environment | same seeds as 851/858/859-lineage | same seeds (42/43/44) as 851/859 |
| Measurement | adequate — context-partition DV correctly instrumented, negative control confirms manipulation is real | **measurement-convention discrepancy noted** (fresh-select vs all-ticks-carry-forward for MECH-449 suppression magnitude) — does not affect this run's own conclusion |
| Integration | isolated, single manipulation (CRF ON/OFF) | isolated, single manipulation (route_source) — cleanly isolates from 851/858's confounded readiness-gate readings |
| Scale | adequate (350 episodes/cell, matching 851's own budget) | adequate — full budget confirms result is not a short-probe artifact |

## 6. Learning extracted

1. **H4 (measurement aliasing via context-conditioned mode-switch) is refuted.** The weak marginal committed-class-entropy reading across this GOV-FANOUT-1 campaign is not explained by a context-gated regime split that the pooled DV was blind to — 847a tested this directly, with a clean readiness pass and a clean (negative-direction) DV failure on both scorable seeds.
2. **Route_source (`lateral_pfc` vs `none`) has no causal effect on MECH-448/449 engagement, confirmed at two budget scales.** This closes 859's open question and rules out training-duration-dependence as an alternative explanation.
3. **851/858's duty-cycle variation is a seed effect, not a manipulation effect** — corroborated (not just inferred) now that a true negative-manipulation control (863) shows zero divergence between arms while individual seeds still carry their own duty-cycle fingerprint.
4. **A driver's own conservative "needs expert review" self-route can still be a clean, informative result** — 863's `criteria_non_degenerate: false` on both mechanisms is not an ambiguous muddle; bit-identical arms are the mechanistically expected signature of a genuine null effect, and the driver correctly avoided auto-asserting that without human confirmation (which this autopsy now supplies).
5. **A prior autopsy's addendum can be validated by a later, differently-designed run** — 851's addendum (predicting 858's outcome) and now 863's independent route-source isolation both point the same direction, strengthening confidence in the "compound-gate/seed-correlated-duty-cycle" reading over the "genuine substrate collapse" reading it superseded.

## 7. Routing (user-confirmed 2026-08-02)

**847a — evidence_direction: `non_contributory`** (concur with the manifest's own self-route as-is; no correction needed). **epistemic_category: `standard`** — a clean, well-instrumented, pre-registered informative null. **Routing: no further action on H4** — it is refuted and closed within this campaign; the remaining live explanations for the ARC-062/MECH-309 conversion ceiling are H2 (F-dominance, per 858's suggestive 2/3-seed near-miss, still pending the duty-cycle-gate-spec fix reprocessing) and H-observation-interface (H3's replacement per the 719a→724→732→732a chain, already resolved elsewhere per the design doc's P-C section).

**863 — evidence_direction: `non_contributory`** (matches `claim_ids=[]` framing — diagnostic, does not itself move any claim). **epistemic_category: `standard`**, correcting the implicit framing behind the `vacuous_pass` flag: this is not an unresolved ambiguity needing a human tie-break between conflicting readings — it is a clean, symmetric, bit-identical null that **confirms** reading (a) over reading (b) (Section 2). Recommend the `evidence_quality_note` read: *"Route_source ('lateral_pfc' vs 'none') produces bit-identical MECH-448/449 statistics at full training budget (350 episodes/cell), confirming V3-EXQ-859's short-probe finding and ruling out training-duration-dependence. 851/858's apparent duty-cycle variation under `lateral_pfc` is not a route_source effect."*

**Routing: no re-run needed for either target.** Both cleanly answer the question they were built for. **Follow-up (not chipped — this session's own routing is `/failure-autopsy` work, reported inline per CLAUDE.md Session Land Protocol step 6):**
- When the already-landed `duty_cycle_readiness.py` fix (`chip-20260802-fanout1-dutycycle-gate-spec-fix`, ree-v3 `f9f923e34c`) is next applied to reprocess 851/858's suppressed C2 results (magnitude-when-active scoring, dropping the `active_frac` conjunct), read the reprocessed H2 (F-dominance) verdict alongside this autopsy's confirmation that route_source is not a confound in that family's readiness gates.
- The MECH-449 fresh-select-vs-all-ticks-carry-forward suppression-magnitude discrepancy (Section 2) is worth a small, standalone check by whoever next touches this family's shared readout convention — not urgent, does not block any current routing.

**Re-derive brake:** does not apply — `claim_ids=[]` on both targets, matching 851/858/859's own convention (no claim to brake against).

**Granularity-debt recurrence trigger:** checked via `granularity_debt_cluster.py ARC-062` and `MECH-309` conceptually against this family's history (851/858/859/847/847a/863 are all diagnostic-purpose, `claim_ids=[]`) — no target in this family reads `weakened` against either claim (all are `non_contributory` by design), so the trigger does not fire. This is a well-tracked standing GOV-FANOUT-1 investigation converging toward H2/H-observation-interface, not new granularity debt.

**GOV-FANOUT-1 hypothesis-space ledger:** no pre-existing entry for this ARC-062/MECH-309 fanout family in `hypothesis_space_registry.v1.json` was found (checked all 19 existing questions — none match ARC-062/MECH-309/"conversion"/"fanout"/"lateral"). This family predates or was never routed through the Step 9b registration mechanism. Not retroactively backfilled in full by this autopsy (out of scope for a 2-target diagnosis to reconstruct H1–H4's entire multi-week history correctly) — flagged as a gap for whoever next runs a GOV-FANOUT-1 leg in this family or governance's own audit sweep.

## 8. Remaining backlog (reported inline, not chipped — `/failure-autopsy` work)

Per user direction, this session scoped to the ARC-062/MECH-309 pair above. The following autopsy-eligible targets from today's regenerated `pending_review.md` remain **unaudited** as of this session's close:

**Claim-tagged FAILs:**
- `v3_exq_848a_arc005_precision_only_decoupled_ladder_calibrated` (ARC-005)
- `v3_exq_108b_mech135_inv088_zworld_disambiguation` (INV-088, MECH-135) — note: a pre-registered hypothesis-space question `inv088_evaluator_degeneracy_cause` already exists in `hypothesis_space_registry.v1.json` for this exact claim pair; whoever autopsies this should resolve it there per Step 9b.
- `v3_exq_870a_mech480_dacc_execution_gain_dissociation` (MECH-480)
- `v3_exq_862a_q040c_dacc_pe_weight_delta_correlation` (Q-040)
- `v3_exq_869a_mech267_mode_conditioning_content_persistence_retest` (MECH-267)
- `v3_exq_867a_mech321_harm_aware_selection_hazard_tuned` (MECH-321)

**Unclaimed-manifest FAILs (claim tags may need re-derivation, not necessarily "no claim intended"):**
- `v3_exq_876_mech025_doing_mode_causal_signal` (mixed)
- `v3_exq_877_mech072_discriminator_gate_full` (weakens)
- `v3_exq_871a_mech090_commit_latch_persistence_diagnostic` (non_contributory)
- `v3_exq_873_mech322_sleep_replay_carveout` (unknown)
- `v3_exq_861a_mech180_mech122_spindle_content_selection_validation` (non_contributory) — **also flagged in the "Dead z_goal stream" section**: `z_goal_stream.writer_defect: true`, `writer_calls: 0` for the whole 38,959-tick run. Whoever autopsies this must first determine whether this run's own FAIL criteria depended on a live z_goal before drawing any MECH-180/MECH-122 conclusion — per the pending_review header, a run whose criteria don't read z_goal is unaffected, but one that does measured something other than what it claimed.

**Not this skill's remit:**
- `v3_v3_exq_870_runner_error` (ERROR, V3-EXQ-870, ree-cloud-4) — routes to `/diagnose-errors`, not `/failure-autopsy`.

None of the above were read in enough depth by this session to state a diagnosis; flagging them here rather than guessing.
