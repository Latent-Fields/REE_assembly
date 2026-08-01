# Failure Autopsy: V3-EXQ-860 (GOV-FANOUT-1 H2 leg, confound-corrected redesign) — URGENT

**Generated:** 2026-08-01T18:17:37Z
**Run:** `v3_exq_860_mech204_sd076_h2_steps_per_ep_probe_20260801T142420Z_v3`
**Queue ID:** V3-EXQ-860
**Claim IDs:** SD-076
**Status:** confirmed
**Supersedes:** V3-EXQ-853 (`v3_exq_850_..._h2_exposure_budget_probe`, the confounded predecessor)
**Deadline:** EVB-0454 SD-076 decision, **2026-08-03T20:50:36Z** (~2 days from this autopsy)

## 1. Facts

**Design.** This is exactly the redesign the V3-EXQ-853 autopsy recommended: N_TRAIN_EPS held at 794a's original **30** (so F1/REM recalibration fires exactly 30 times, unchanged from 794a and the sibling H1 leg — decoupling the confound), and `STEPS_PER_EP` raised **200→1000 (5x)** instead, reaching the SAME total exposure (30,000 waking steps) as 853's own 5x `N_TRAIN_EPS` change, but via a clean single axis.

**Outcome:** FAIL. `non_degenerate: false`. Label: `substrate_not_ready_requeue`.

**Preconditions:**
| Precondition | LO | HI | Threshold | Met |
|---|---|---|---|---|
| rv_live | 0.496 | 0.496 | 1e-6 | ✅ |
| f1_recalib_engaged | 0.0066 | 0.0059 | 1e-4 | ✅ |
| **inflation_lowers_rv** | **-2.76e-4** | **-1.46e-4** | 1e-4 | ❌ (wrong-signed) |
| dose_levels_separated | 1.30e-4 | 1.30e-4 | 1e-4 | ✅ (first pass in this lineage) |

## 2. Two distinct findings — do not conflate them

### Finding A: the closure-fraction comparison (decisive, gate-independent)

| Run | Design | LO closure | HI closure |
|---|---|---|---|
| V3-EXQ-853 | N_TRAIN_EPS 30→150 (confounded: also 5x F1 firings) | **21.7%** | **12.2%** |
| V3-EXQ-860 (this run) | STEPS_PER_EP 200→1000 (F1 firings fixed at 30) | **2.9%** | **2.5%** |

This is a **simple three-point magnitude fact** (rv_final vs 794a's own vs the repair smoke's) that does not depend on the sign of `inflation_lowers_rv` or any other precondition. With the F1-firing-count confound properly removed — holding it fixed at 30 while still reaching the same total exposure via longer episodes — closure collapses from 12–22% down to 2.5–2.9%. Since the *only* design difference between 853 and 860 is which axis absorbed the 5x exposure increase, this is a clean controlled comparison: **F1-firing count (H1's axis), not raw exposure duration (H2's axis), was responsible for 853's partial closure.**

### Finding B: the wrong-signed `inflation_lowers_rv` (a separate, new puzzle)

`inflation_lowers_rv` measures `wci_symmetric_rv_ref_final − rv_final_after_training`. In 850 and 853, this was small and **positive**-but-sub-threshold. Here it's **negative** in both arms — the inflated `rv_final` ended up *above* the substrate's own live un-inflated counterfactual, the opposite of the intended direction. This is a qualitatively new failure shape, not merely a smaller version of the old one, and is what formally triggers this run's `non_degenerate: false` self-route.

Reading `ree_core/predictors/e3_selector.py`'s `update_running_variance`/`_apply_wci_rv_floor`: the inflated and counterfactual EMAs are both advanced every tick from the same `error_var`, but the inflated path's effective alpha depends asymmetrically on whether error is improving or worsening *relative to its own current estimate*. At 5x more within-episode ticks before the once-per-episode F1 reset, there is more room for these two paths to diverge in ways not previously observed at the original 200-step episode length. The magnitude is small (~1–3×10⁻⁴, similar scale to the old sub-threshold readings) — this is a subtle sign inversion, not a dramatic blowup.

**This does not undermine Finding A.** The closure-fraction comparison is unaffected by which way `inflation_lowers_rv`'s sign points; it is a separate precondition about a different (though related) question.

## 3. Claim-layer mapping

SD-076 (candidate). This diagnostic run is excluded from claim-confidence scoring by convention (matches 850/853's own precedent), but its *content* is decision-relevant for the EVB-0454 retain/hybridize/retire call on SD-076/MECH-204.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear per the formal gate, but Finding A is robust and gate-independent | |
| Biological reference | not load-bearing | see the complete lit-pull for H3 |
| Prerequisites | present | F1 recalibration confirmed live and firing-count-matched to 794a |
| Implementation | complete, exactly the recommended redesign | |
| Environment | adequate | same family as 794a/850/853 |
| Measurement | two distinct findings of different character (see above) | |
| Integration | coupled | F1 firing count isolated as the sole difference from 794a |
| Scale | 5x exposure via episode length, matched total budget to 853 | |

## 5. Why this is decision-relevant now

The V3-EXQ-853 autopsy already argued (from a confounded design) that H2 looked weaker than H1. This run removes the confound and finds the effect nearly vanishes — a materially stronger and cleaner argument against H2 than 853 alone provided. Combined with H1's still-alive partial signal (V3-EXQ-850) and H3's lit-pull-based weakening (not elimination), the portfolio picture for EVB-0454 is now: **H1 is the best-supported of the three by process of elimination, though none is formally confirmed or eliminated.**

## 6. Learning extracted

1. A properly confound-decoupled comparison collapsing 853's partial closure to near-zero is strong, clean evidence for attributing 853's signal to F1-firing count rather than raw exposure.
2. A formally non-degenerate (gate-failed) run can still contain a robust, gate-independent, highly informative comparison — don't discard the whole run because one precondition failed for an unrelated reason.
3. A precondition failing *wrong-signed* rather than *sub-threshold* at a materially different parameter regime is worth flagging as a structurally distinct puzzle, not folded into the same bucket as prior sub-threshold readings.

## 7. Routing

**Evidence direction: `weakens`** (H2, more strongly than 853) — recommended, pending user confirmation.

**Routing: `/queue-experiment`** — a small, separate diagnostic on the wrong-signed `inflation_lowers_rv` puzzle (instrument the rv/wci_symmetric_rv_ref trajectory *within* the longer episode, not just at its end), which should NOT block using Finding A for the EVB-0454 decision.

**Also recommend:** mark V3-EXQ-853's `evidence_direction` as `superseded` (it is the confounded predecessor this run was built to correct) rather than continuing to co-weight it with this cleaner result — a recommendation for `/governance` to apply, not applied here.

Re-derive brake: 0 prior `substrate_ceiling` autopsies for SD-076 — does not fire.
