# Failure Autopsy — V3-EXQ-713 (bounded parity controller validation)

- **Generated (UTC):** 2026-07-05T09:28:06Z
- **Scope:** single (with cluster read of the 709→710→711→713 arbitration lineage)
- **Status:** confirmed (user-adjudicated 2026-07-05, interactive gate)
- **Run:** `v3_exq_713_bounded_parity_controller_validation_20260704T223603Z_v3` — **FAIL**
- **Claims tested:** MECH-439, ARC-108, ARC-110
- **Manifest self-route:** `bounded_parity_win_but_does_not_convert_ceiling_intrinsic_weakens_arc108_arc110` (MECH-439 supports; ARC-108 weakens; ARC-110 weakens)
- **Confirmed adjudication:** **non_contributory** for all three (does NOT weaken ARC-108/ARC-110; NARROW corroboration only for MECH-439). **Re-derive brake FIRED (11th MECH-439 / 8th ARC-108 substrate_ceiling/non_contributory reading).** Route = selection-face (MECH-448) conversion path; a same-level arbitration-reweighting re-letter is REFUSED.

---

## 1. Facts (no interpretation)

713 is the sanctioned successor the **V3-EXQ-711 confirmed autopsy routed to**: 711's raw-scalar ascending gain (20x forward × 5x plasticity) compounded through the plastic `M_cross` loop and RAN AWAY (M_cross range peak 4897.8; w_eff[limbic] 10–2274× w_eff[motor]) — a limbic *monopoly*, not a fair win. The 711 autopsy's routed build was "a bounded/normalized ascending gain + a saturation guard on the win-gate." 713 built exactly that: a **target-parity controller** (`use_ascending_parity_controller`) that solves a per-step forward gain so w_eff[limbic] is lifted toward but **hard-capped at** `PARITY_CEILING_RATIO × w_eff[motor]`, plus an anti-windup clamp on ascending M_cross maturation. So 713 is a redesign of a **different mechanism** (the controller) on a **newly-built substrate**, not a raw-gain re-letter — it is the *allowed* build path out of the 711 brake, `experiment_purpose=evidence`.

**Two arms** (only swept factor `use_ascending_parity_controller`):
- `A_ASCENDING_OFF` = the 709 ceiling baseline (limbic reached motor effective weight on ~1/4 divergent seeds).
- `A_ASCENDING_ON` = identical + bounded parity controller (the mechanism under test).

**Readiness preconditions — ALL 8 MET, non-degenerately:**

| Precondition | measured | threshold | met |
|---|---|---|---|
| enough_divergent_seeds | 4 | ≥3 | ✅ |
| loops_carry_live_cross_loop_variance | 1.0 | 1.0 | ✅ |
| named_channel_routing_live (limbic routed range) | 1.414 | 0.001 | ✅ |
| learned_cross_loop_weights_moved (M_cross off init) | 0.169 | 1e-6 | ✅ |
| **limbic_loop_parity_win (fair band win, not saturated)** | **4** | **≥3** | ✅ |
| **no_saturation_blowup** | **0** | **0** | ✅ |
| learning_engaged_finer_channels | 0.00144 | 1e-4 | ✅ |
| candidate_pool_divergent (per-seed majority) | 0.0259* | 0.05 | ✅ |

\*aggregate scalar shown; gate is per-seed majority.

**Load-bearing criterion:** `C1_learned_strict_above_static` — **passed: FALSE.** `criteria_non_degenerate.preconditions_met = true` and every non-degeneracy guard true (`limbic_loop_parity_win`, `no_saturation_blowup`, `crf_matured`).

**Failed criterion class:** discrimination (`C1` learned-strict-above-static), under a **validly measured** (non-degenerate) arbitration.

## 2. The pivotal difference from 709 / 711

For the **first time in the 709→711→713 arbitration lineage the conversion question was validly measured.** In 709 the limbic loop was sub-threshold (coupling ~0.03, never won); in 711 it was a saturated runaway (10–2274× monopoly). Both were `non_contributory` because the win-gate was met **degenerately or not at all** — the conversion "was not measured." 713 delivers a **fair, bounded, non-saturated parity win on 4/4 divergent seeds** (`no_saturation_blowup = 0`), and C1 **still** fails. The "not validly measured" escape hatch that shielded MECH-439/ARC-108/ARC-110 in 709/711 **does not apply here.** A fair limbic parity win at the cross-loop-arbitration face does not convert committed-action diversity.

## 3. Claim-layer map

| Claim | Type / status | epistemic_category | Did the test let it express itself? |
|---|---|---|---|
| MECH-439 (F-dominance committed-selection variance monopoly) | mechanism_hypothesis / candidate | substrate_ceiling | Yes — F-dominance persisted through a fair limbic parity win. Manifest "supports" is treated as NARROW corroboration only (single-arena FAIL cannot establish global intrinsicness). |
| ARC-108 (learned cross-loop gating architecture) | architectural_commitment / candidate | substrate_conditional | Partially — the *arbitration-reweighting* realization of ARC-108 was exercised fairly and did not convert; but ARC-108's architectural assertion (learned gating is real + load-bearing) is not thereby falsified. |
| ARC-110 (loop-segregation architecture) | architectural_commitment / candidate | substrate_conditional | Partially — segregation is live; the existing NARROW 707b single-arena-artefact weakens is unchanged and stands. |

## 4. Biological-reference triage

- Closest reference: Haber (2000) striato-nigro-striatal ascending **spiral** — a graded, bounded, parity-*restoring* modulation. The 711 raw scalar had the *symbol* of the spiral without its bounding dependency; 713's parity controller supplies the bound. So 713's controller is now a **faithful** translation of the bounded-spiral mechanism, and it demonstrably works (fair win, no monopoly). This is a positive engineering datum for the controller (MECH-439-adjacent mechanism).
- The failure is therefore **not** a missing-controller signature (that dependency is now present). It is a **level** signature: making a non-motor loop win the *cross-loop arbitration* (reweighting the [3,3] `M_cross` matrix) is not the same operation as demoting F at the *within-loop eligibility/selection* face. Biologically the committed-action selection happens at the striatal Go/No-Go eligibility layer (MECH-448 rank-preserving F→eligibility demotion, MECH-449 Go/No-Go governance) — **downstream** of cross-loop arbitration.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | Architecture not falsified; the *arbitration-reweighting realization* is what failed to convert. |
| Biological reference | clear | Bounded spiral (Haber 2000) now faithfully translated and working; conversion happens at the selection/eligibility face, not the arbitration face. |
| Prerequisites / dependencies | present (arbitration) / built-elsewhere (selection) | Controller dependency now present. The conversion substrate (MECH-448 selection-face) is BUILT and already lifted the ceiling on the GAP-A foraging substrate. |
| Implementation completeness | complete | Parity controller landed 2026-07-04; fair win delivered 4/4 seeds. |
| Environment adequacy | adequate | segregated-loop substrate live; divergent candidate pool present (4 seeds). |
| Measurement adequacy | adequate | First non-degenerate measurement of arbitration-level conversion (band-win + saturation guard). |
| Integration adequacy | coupled | loops + learned arbitration + controller coupled and live. |
| Scale / capacity | adequate | not the binding constraint. |

**Dominant diagnosis:** the cross-loop-**arbitration-reweighting** route to committed-action conversion is **exhausted** — sub-threshold (709), runaway (711), and now fair-bounded (713) all fail. Recommended `epistemic_category`: **substrate_ceiling** (level-mismatch: conversion lives at the selection/eligibility face, not the arbitration face).

## 6. Cluster read (709 → 710 → 711 → 713)

| Exp | Mechanism built | Win-gate outcome | Converted? | Read |
|---|---|---|---|---|
| 709 | learned [3,3] cross-loop arbitration | limbic ≥ motor on 1/4 seeds (~0.03, too weak) | not measured | substrate_not_ready |
| 710 | disinhibitory soft-competitive settling | F sharpens over collapsed single selector | no (entropy fell) | single-arena ceiling corroboration |
| 711 | raw-scalar ascending spiral gain | saturated monopoly 10–2274× | no (entropy fell) | degenerate; missing controller |
| **713** | **bounded parity controller** | **fair band win 4/4, no saturation** | **no (C1 fail)** | **arbitration route exhausted; conversion is selection-face** |

**This is one structural property, not four independent bugs:** across a weak, a saturated, and now a fair-bounded arbitration reweighting, a non-motor loop winning the *cross-loop arbitration* does not convert committed-action diversity. The convergence across three structurally-different controllers is the load-bearing signal, and it triangulates against the **selection-face** program (`f_dominance_conversion_ceiling` / MECH-448), which is BUILT and already **lifted** the ceiling on the GAP-A foraging substrate — i.e., the conversion route is the eligibility/selection face, not arbitration reweighting.

## 7. Learning extracted

1. The 711 "missing controller" gap is **closed** — a bounded target-parity controller delivers a fair, non-saturated limbic parity win (4/4 divergent seeds). Positive engineering datum.
2. A fair arbitration-level parity win, **validly measured for the first time**, does **not** convert committed-action diversity. This **exhausts** the cross-loop-arbitration-reweighting route (weak → runaway → fair-bounded all fail).
3. Level-mismatch finding: committed-action conversion is a **selection/eligibility-face** operation (MECH-448 rank-preserving F→eligibility demotion, already lifting on GAP-A), **not** a cross-loop arbitration-reweighting operation. 713 is positive triangulation for the selection-face route.
4. This does **not** weaken ARC-108/ARC-110 as architectural commitments (segregated loops + learned gating remain biologically real and load-bearing); it closes one *realization* of their conversion route.

## 8. Repair pathway / routing (user-confirmed 2026-07-05)

- **Routing:** `implement-substrate` per the re-derive brake — but the conversion substrate (selection-face `f_dominance_conversion_ceiling` / MECH-448) is **already built and lifting on GAP-A**. Concrete forward motion is therefore the **selection-face behavioural-retest path already queued** (654h / 485i / 445h / 625e), which validates whether MECH-448's GAP-A ceiling-lift converts behaviourally. No new selection-face *build* is owed by this run.
- **REFUSED:** another arbitration-level parity re-letter (any 713x that re-tunes `use_ascending_parity_controller` / gain magnitude / parity ceiling against the same v4_loop_segregation substrate). A redesign of a *different* mechanism (new EXQ, different claim_ids) or a commitment-free read remains allowed; another letter circling the arbitration ceiling is not.
- **substrate_queue:** `amend` `v4_loop_segregation` with the 713 terminal failure_record (arbitration-reweighting route exhausted); the conversion route of record is `f_dominance_conversion_ceiling` (MECH-448), no new build owed there.
- **pending_retest_after_substrate:** true — via the selection-face path. Paired non_contributory + pending_retest per the illusory-conflict-resolution rule; the remaining conversion "supports" are the MECH-448 GAP-A selection-face results (single program), retests not yet scored.

### Draft evidence_quality_note text (governance to write — do not write here)

**MECH-439** (append): `CORROBORATION 2026-07-05 (confirmed failure_autopsy_V3-EXQ-713_2026-07-05): V3-EXQ-713 (BOUNDED PARITY-CONTROLLER validation -- the 711-autopsy-routed controller build; new EXQ, new mechanism) FAIL / non_degenerate=True. For the FIRST time in the 709->711->713 arbitration lineage the conversion question was VALIDLY measured: the bounded target-parity controller delivered a FAIR band parity win on 4/4 divergent seeds with no_saturation_blowup=0 (the 711 monopoly is repaired) -- and C1 (learned strict-above static) STILL failed. The manifest self-routes MECH-439 "supports (ceiling intrinsic)"; the confirmed autopsy adjudicates NARROW corroboration only (narrow_supports_flag): a single-arena FAIL cannot establish global intrinsicness. NEW load-bearing datum: a fair arbitration-level parity win does NOT convert -> the cross-loop-arbitration-reweighting route is EXHAUSTED (weak 709 / runaway 711 / fair-bounded 713 all fail); committed-action conversion is a SELECTION/ELIGIBILITY-face operation (MECH-448 rank-preserving F->eligibility demotion, already LIFTING on the GAP-A foraging substrate), not an arbitration-reweighting operation. Re-derive brake FIRES (11th MECH-439 substrate_ceiling/non_contributory reading); a same-level arbitration parity re-letter is REFUSED; route = the already-built selection-face (MECH-448) behavioural-retest path (654h/485i/445h/625e). non_contributory: does NOT weaken MECH-439. pending_retest_after_substrate.`

**ARC-108** (append): `UPDATE 2026-07-05 (confirmed failure_autopsy_V3-EXQ-713_2026-07-05): V3-EXQ-713 (bounded parity-controller validation, tagged ARC-108) FAIL / non_degenerate=True. The manifest self-routes ARC-108 "weakens"; the confirmed autopsy REJECTS the decisive weakens. The bounded controller (the 711-autopsy-routed build) delivered a FAIR non-saturated limbic parity win (4/4 divergent seeds, no_saturation_blowup=0) -- so unlike 709 (sub-threshold) and 711 (saturated), the learned-gating-at-the-arbitration route was exercised NON-DEGENERATELY -- and it did NOT convert (C1 fail). This EXHAUSTS the cross-loop-arbitration-reweighting realization of ARC-108's learned gating, but does NOT weaken ARC-108 as an architectural commitment (learned gating remains real + load-bearing; the conversion route is the downstream selection/eligibility face, MECH-448, already lifting on GAP-A). non_contributory. Re-derive brake FIRES (8th ARC-108 substrate_ceiling/non_contributory reading); same-level arbitration parity re-queue REFUSED; route = selection-face (MECH-448) behavioural retests. pending_retest_after_substrate.`

**ARC-110** (append): `UPDATE 2026-07-05 (confirmed failure_autopsy_V3-EXQ-713_2026-07-05): V3-EXQ-713 (bounded parity-controller validation, tagged ARC-110) FAIL / non_degenerate=True. The manifest self-routes ARC-110 "weakens"; the confirmed autopsy adjudicates non_contributory. A fair, bounded, non-saturated limbic parity win across the segregated loops did NOT convert committed diversity -- corroborating that loop segregation is necessary-but-not-sufficient and that the conversion route is a WORKING selection-face demotion (MECH-448), not cross-loop arbitration reweighting. This does NOT add a second weakens; ARC-110's existing NARROW 707b single-arena-artefact weakens is UNCHANGED and STANDS unretired. non_contributory. Re-derive brake FIRES (3rd ARC-110 substrate_ceiling/non_contributory reading); same-level arbitration re-queue REFUSED; route = selection-face (MECH-448) behavioural retests. pending_retest_after_substrate.`

## 9. Key rule checks

- Ran-to-completion FAIL → in scope. Self-route treated as hypothesis, not verdict (rejected the decisive weakens; accepted narrow corroboration for MECH-439).
- lit_conf / exp_conf not blended.
- non_contributory paired with `pending_retest_after_substrate` + explicit note that the remaining conversion supports are a single program (MECH-448 GAP-A selection-face, retests unscored) — illusory-conflict-resolution guard honoured.
- Re-derive brake is a hard gate: routed to implement-substrate (selection-face) and REFUSED a same-level arbitration re-letter; `re_derive_brake.fired = true` stamped on all three targets.
- Analysis + handoff only: no edits to claims.yaml, manifests, review_tracker, or substrate_queue — governance applies.
