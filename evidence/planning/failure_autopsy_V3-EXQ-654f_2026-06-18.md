# Failure Autopsy — V3-EXQ-654f (arc_062_rule_apprehension:GAP-B behavioural falsifier)

- **Generated (UTC):** 2026-06-18T06:04:07Z
- **Status:** confirmed
- **Scope:** single (cross-claim convergence with GAP-A surfaced)
- **Run:** `v3_exq_654f_arc062_gapb_rule_apprehension_behavioural_falsifier_20260618T005228Z_v3` (ree-cloud-1)
- **Queue:** V3-EXQ-654f, `experiment_purpose=evidence`, `supersedes=V3-EXQ-654e`
- **Claims tested:** MECH-309, ARC-062 (bears-on ARC-063)
- **Outcome:** FAIL / `non_contributory` (per-claim MECH-309 + ARC-062 both `non_contributory`); reviewed /governance 2026-06-18, weights nothing.
- **Self-route label (under `result.interpretation`):** `shared_selection_authority_conversion_ceiling_route_implement_substrate`

## Headline

**The CRF-gate calibration amend WORKED.** This is reading **(a)** of the pre-registered
disambiguation: `crf_frac_active` cleared the 0.30 floor at full behavioural scale, the
conflict-gate lockout the 654d autopsy diagnosed is gone, the differentiated pool matures,
and propagation is non-vacuous — but committed-class entropy still did not lift, because the
residual blocker is the **shared selection-authority conversion ceiling** that
`behavioral_diversity_isolation:GAP-A` owns (failure_autopsy_569g/569h/682). Not (b)
(frac_active stayed 0.0 — refuted), not (c) (a precondition failed — refuted; all five C1
preconditions met).

## 1. Facts (no interpretation)

C1 (non-vacuity) = **TRUE**, all five preconditions met:

| Precondition | 654d (prior) | 654f (this run, ARM_ON seeds 42/43/44) | Gate |
|---|---|---|---|
| committed-class axis exercisable | met | frac_pre_ge2 = 1.0 (3/3) | ≥0.30 ✅ |
| GAP-A consumed-summary divergence | met (2/3) | 2/3 arms (seed 43 below, majority rule passes) | ✅ |
| `crf_frac_active` (matured pool clears gate) | **0.0 all seeds** | **0.869 / 0.968 / 0.828** | ≥0.30 ✅ |
| propagation non-vacuity (ARM_ON bias ≠ ARM_OFF) | 0.0 | 0.0517 / 0.0415 / 0.0203 | >0.001 ✅ |
| within-ARM_ON rule_state counterfactual nonzero | False | True (3/3) | ✅ |

Supporting CRF telemetry (ARM_ON): `crf_mean_n_active` 2.27/2.05/3.04; `crf_n_minted_total`
16/14/15; `crf_differentiated` True; `crf_max_pairwise_rule_dist` 1.711; `crf_mean_n_matched`
2.86/2.18/3.81 (vs 654d's 7.08/7.29/8.70 **all gated out**). The amend levers
(`crf_mature_context_match_threshold=0.7` + `crf_tolerance_conflict_cap=3` +
`crf_maintenance_couple_to_theta=True`) reproduced the C20–C24 contract behaviour (isolated
crowded-pool frac_active 0.000→0.98) at full scale.

C2 (PRIMARY — committed-class entropy lift) = **FALSE**:
- `C2_paired_lifts_by_seed` = {42: 0.0, 43: -0.001919, 44: 0.000415}; 0/3 cleared the +0.05-nat
  margin (need ≥2/3).
- ARM_ON committed-class entropy 1.041051 ≈ ARM_OFF 1.041553.
- `committed_class_counts` near byte-identical between arms (seed 44: OFF {0:317,2:474,4:172} vs
  ON {0:318,2:473,4:172}).
- ARM_ON `mean_lateral_pfc_bias_abs` is **lower** than ARM_OFF (seed 42: 0.0483 vs 0.1000;
  seed 43: 0.0238 vs 0.0653) — the rule_state reaches and *changes* the bias, but the change
  does not move the F-dominated committed argmax.

Failed criterion: **discrimination** (C2), with the negative-control axis (within-class-rep
entropy ARM_ON≈ARM_OFF) behaving as designed.

## 2. The load-bearing finding

654f cleanly **dissociates** the two GAP-B blockers that were confounded through 654d:
1. **CRF conflict-gate lockout — FIXED** (the crf-availability-maintenance amend; frac_active
   0.83–0.97, ruled out as the blocker).
2. **Shared selection-authority conversion ceiling — the residual blocker** (the channel range
   reaches the E3 accumulator but does not move the F-dominated committed argmin; F ≈ 88–89% of
   E3 variance per V3-EXQ-571). This is the *same* mechanism `behavioral_diversity_isolation:GAP-A`
   diagnosed in 569g/569h/682.

**Critical routing fact:** 654f armed the **superseded** conversion lever — `ARM_STD_G2`
(additive `modulatory_authority_normalize_basis=std` + `authority_gain=2.0` +
`use_modulatory_channel_routing` + `source=cand_world_summary`). GAP-A established
V3-EXQ-569h FAIL (additive ARM_STD_G2 cleared committed-action diversity on only 1/3 seeds) and
that the **TOP-K shortlist conversion** is the fix that works — **V3-EXQ-569i PASS/supports**
(2026-06-17; "diversity reaches committed action"; ARC-065 promoted stable). 654f used the old
lever only because it was queued (as 654e) on 2026-06-17 *before* the 569i top-k validation
landed. 654f therefore reproduces, for the rule_state channel, exactly the additive ceiling
GAP-A diagnosed and then solved.

## 3. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | C2 never adjudicated MECH-309/ARC-062 (gated by the conversion ceiling). |
| Biological reference | clear | Collins & Frank 2014 / Mansouri rule persistence (CRF maturation, achieved); the conversion ceiling is the BG/PFC selection-authority question GAP-A owns. |
| Prerequisites | CRF now present; conversion substrate (top-k shortlist) now present **but not armed in 654f** | The single remaining gap is wiring the validated lever. |
| Implementation completeness | complete (CRF) / wrong lever wired (conversion) | 654f used additive ARM_STD_G2, not the 569i top-k shortlist. |
| Environment | adequate | SD-054 bipartite, foraging-competent stack. |
| Measurement | adequate | committed-class entropy is the correct class-keyed DV (within-class-rep is the negative control). |
| Integration | coupled, ceiling at the argmax | bias reaches accumulator, doesn't move the F-dominated commit. |
| Scale | adequate | 200-ep P0; pool matured. |

Recommended `epistemic_category`: **substrate_ceiling** (unchanged). Recommended
`evidence_direction`: **non_contributory** per-claim (already set). Pair with
`pending_retest_after_substrate` (already set). **NO weakens.**

## 4. Manifest emit gap (script-emit hygiene; not a self-route-before-populate, not a regression)

- The script writes `interpretation_label` + `interpretation` **only inside the `result` dict**
  (`ree-v3/experiments/v3_exq_654f...py:1373-1374`); the returned manifest dict (lines 1495-1589)
  has **no top-level** `interpretation`/`interpretation_label`. The **entire 654 lineage**
  (654/654a/654b/654c/654d) shares this shape.
- The indexer reads `manifest.get("interpretation")` at the **top level**
  (`build_experiment_indexes.py:782`) → `None` → empty surfaced label. (For
  `experiment_purpose="evidence"`, `_compute_adjudication` also returns `"n/a"` at line 228.)
- So the governance "interpretation block is empty (label None)" reading is a **top-level read of
  a result-nested block** — the run *did* self-route and *did* fully populate the block; the
  blocker letter (C1-met/C2-fail shared conversion ceiling) IS self-reported under `result`.
- **Recommended fix (chip spawned):** mirror the two keys at the manifest top level (two extra
  keys in the returned dict; low-risk). Routes through `/queue-experiment` (script edit). This
  autopsy does not apply it.

## 5. Granularity-debt recurrence check

This is the ~6th autopsy on the 654 target (654→654a→654b→654c→654d→654f). Per the user's
2026-06-16 re-confirmation, this is **substrate-maturation, not claim-granularity debt** — and
654f corroborates: it is a single localized failure signature that has now *resolved at the CRF
locus*, leaving one shared conversion blocker rather than multiple distinct failure shapes
circling a coarse claim. **No `/claim-synthesis`.**

## 6. Routing (user-confirmed at the interactive gate)

**`/queue-experiment` a 654g successor** porting the GAP-B committed-class-entropy falsifier onto
the **569i-validated TOP-K shortlist conversion config** (`use_modulatory_shortlist_then_modulate`
+ `modulatory_shortlist_mode=top_k` + `modulatory_shortlist_k`), keeping the entire (now-working)
CRF stack constant (mature + maintenance + persist + e2-context + trained-bias-head P1). NOT a
further CRF amend (CRF is done — C1 fully met). NOT the additive ARM_STD_G2 lever (superseded by
569i). Retain the C1c readiness precondition (`crf_frac_active>=0.30`, self-route
substrate_not_ready_requeue) and the conversion-ceiling off-ramp (C1 holds / C2 absent →
non_contributory, NOT a falsification, NO weakens).

Plus: **chip spawned** for the manifest top-level interpretation-mirror emit fix.

MECH-309 / ARC-062 / ARC-063 stay **candidate / substrate_ceiling / v3_pending /
pending_retest_after_substrate** — NOT weakened. GAP-B node `resume_condition` refined to the
654g-on-top-k path (node not held by another active session).
