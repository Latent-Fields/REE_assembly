# Failure Autopsy: V3-EXQ-853 (GOV-FANOUT-1 H2 leg, SD-076/MECH-204)

**Generated:** 2026-08-01T12:54:47Z
**Run:** `v3_exq_850_mech204_sd076_h2_exposure_budget_probe_20260801T005937Z_v3`
**Queue ID:** V3-EXQ-853
**Claim IDs:** SD-076
**Status:** confirmed (user gate passed 2026-08-01)

## Time-sensitivity

EVB-0454's SD-076 decision deadline is **2026-08-03T20:50:36Z** (~2 days from this autopsy). This is the H2 leg of the 794a GOV-FANOUT-1 3-hypothesis portfolio; H1 (V3-EXQ-850) was already autopsied (alive, partial F1-damping signal). H3's `/lit-pull` (commit `e84240108d`) is **already complete** — a sibling autopsy (V3-EXQ-850, generated 2026-08-01T10:37:54Z) incorrectly stated it had "not yet started"; it actually landed 2026-08-01T00:07:47Z, ~10.5 hours earlier. This autopsy corrects that record.

## 1. Facts

**Design.** Single-axis extension of 794a: N_TRAIN_EPS raised 30 → 150 (5x), everything else (INFL_LO=0.6, INFL_HI=0.8, F1 recalibration ON, Phase 7 broadcast OFF) held constant. Tests H2 ("insufficient training exposure" explains why 794a's full-loop rv reduction reached only ~half the repair smoke's demonstrated reduction).

**Outcome:** FAIL. `non_degenerate: false`. Self-route: `substrate_not_ready_requeue`.

**Preconditions:**
| Precondition | Arm | Measured | Threshold | Met |
|---|---|---|---|---|
| rv_live | both | 0.496 / 0.496 | 1e-6 | ✅ |
| f1_recalib_engaged | both | 0.0013 / 0.0012 | 1e-4 | ✅ |
| inflation_lowers_rv | both | 3.95e-5 / 6.42e-5 | 1e-4 | ❌ |
| dose_levels_separated | both | 2.48e-5 | 1e-4 | ❌ |

**Criteria (both non-load-bearing-scored due to gate failure):**
- C1 (closure ≥ 0.30): LO closure 0.217, HI closure 0.122 — both FAIL
- C2 (plateau < 0.10): neither qualifies as plateau either (0.217, 0.122 are both above 0.10) — FAIL
- C3 (dose-response monotone, non-load-bearing): PASS (LO rv 0.003680 > HI rv 0.003655)

**The critical trend — dose separation across training budget:**
| Source | N_TRAIN_EPS | \|rv(LO) − rv(HI)\| |
|---|---|---|
| Repair-validation smoke | n/a (4000-step direct EMA) | 4.35e-4 |
| V3-EXQ-794a (full loop) | 30 | 1.28e-4 |
| V3-EXQ-853 (this run) | 150 | **2.48e-5** |

This is monotonic and *shrinking*, not growing, as training extends — the opposite of H2's prediction.

## 2. Claim-layer mapping

SD-076 (candidate, `epistemic_category: standard`, `implementation_phase: v3`). This run is `experiment_purpose: diagnostic`, excluded from claim-weight scoring by convention (matches sibling H1/V3-EXQ-850). No claim status change from this run alone.

## 3. Biological-reference triage

Not the load-bearing layer for this diagnostic (same convention as H1's own autopsy). The biological magnitude/timescale question is H3's remit, addressed by the commissioned `/lit-pull` (see below) — read alongside, not duplicated here.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (diagnostic, correctly excluded) | |
| Biological reference | not load-bearing here | see lit-pull for H3 |
| Prerequisites | present | SD-076 repair + MECH-204 F1 recalibration both confirmed live |
| Implementation | complete | 5x budget ran cleanly |
| Environment | **confounded** | N_TRAIN_EPS jointly controls exposure (H2 axis) AND F1-firing count (H1 axis, K=1 fires once/episode) |
| Measurement | gate correctly fires; direction is the informative part | shrinking separation is a real, monotonic 3-point trend, not noise |
| Integration | coupled | more F1 firings (150 vs 30) is the leading explanation for shrinkage |
| Scale | not the limiting factor | 5x is generous; more of the same looks likely to shrink separation further |

## 5. Why "substrate not ready" is the wrong read

The self-route framing implies more compute would help. The data argues the opposite: three points (smoke → 794a → this run) show dose separation shrinking by roughly 3.4x then again by ~5.2x as training extends. If H2 (insufficient exposure) were correct, more exposure should let the asymmetric EMA "catch up" toward the smoke's larger separation — instead the full-loop system is converging toward a *shared* asymptote regardless of dose, which is the signature you'd expect if a homeostatic process (F1/REM recalibration, scaling in lockstep with N_TRAIN_EPS at K=1) increasingly dominates over the static dose parameter at longer horizons. That reasoning favors H1, not H2.

## 6. The design confound

N_TRAIN_EPS is not a clean single-axis manipulation for H2: SleepLoopManager fires the F1 recalibration cycle once per episode (K=1), so raising N_TRAIN_EPS from 30→150 also raises the F1-firing count from 30→150 in lockstep. Any observed effect of "more N_TRAIN_EPS" is inseparable from "more F1 firings." A clean H2 probe should vary `STEPS_PER_EP` (episode length) instead, which raises total waking exposure without touching firing count.

## 7. H3 lit-pull — already complete, correcting the record

Commit `e84240108d` (2026-08-01T00:07:47Z), 5 entries across `targeted_review_sd_076` and `targeted_review_connectome_mech_204`. Net read: Baranski 1994/2007 find no significant waking calibration drift under acute sleep deprivation; Boardman 2024 shows the acute regime is specifically where drift is *least* likely (chronic restriction is where it appears) — both nudge away from H3 and toward H2. Jones et al 2006 (overconfidence emerges ~19h into wakefulness) offers partial counter-support that a real drift phenomenon exists at all, with a construct-mismatch caveat. van der Helm et al 2011 supports MECH-204's general REM-recalibration architecture (noradrenergic, not serotonergic — caveat noted). **Net: H3 weakened, not eliminated.**

This creates a genuine three-way tension: the literature leans toward H2 remaining plausible in principle (drift-with-exposure is a real phenomenon in humans), while this run's own direct substrate measurement argues against H2 specifically for the asymmetric-EMA + F1-recalibration combination as currently wired. Both readings are defensible; they are not talking about the same thing (general biological plausibility of exposure-dependent drift vs. this specific substrate's empirical behavior under an exposure manipulation).

## 8. Learning extracted

1. The readiness gates correctly detected a genuine saturation signature, but the self-route's implicit interpretation ("needs more compute") doesn't match the direction of the trend.
2. N_TRAIN_EPS is a confounded manipulation for H2 in this substrate — cannot cleanly discriminate H2 from H1.
3. The observed shrinkage in dose separation favors H1 over H2, so this run should shift portfolio weight away from H2, not sit neutral.
4. Always re-check `git log` for a fanout's sibling-leg state before writing "not yet started" — a lit-pull can land between two autopsy sessions on the same tree.

## 9. Routing (user-confirmed)

**Evidence direction: `weakens`** (not neutral) — user confirmed 2026-08-01.

**Routing: `/queue-experiment`** — a redesigned H2 probe varying `STEPS_PER_EP` instead of `N_TRAIN_EPS` to decouple exposure from F1-firing count. User confirmed chipping this now despite the tight deadline (unlikely to land before 2026-08-03T20:50:36Z, but keeps the option open).

**No further `/lit-pull` needed** — H3's lit-pull is already complete; user confirmed not to duplicate it.

## 10. Hypothesis-space ledger update

Registry qid `mech204-sd076-calibration-loop-drift-source-exposure-gap`:
- **H2** resolved: state `alive`, `evidence_direction: weakens`, `non_degenerate: false`, `met_elimination_bar: false` (per GOV-FROZEN-1's state-mapping table — a non-degenerate-false run cannot clear the elimination bar even with a directionally clear reading).
- **H3** resolved via the lit-pull (not a run): state `alive`, `evidence_direction: weakens`, `resolved_utc: 2026-08-01T00:07:47Z` (the lit-pull commit's committer date, which precedes this autopsy — correct pre-registration/resolution ordering).
- Decision block updated: none of H1/H2/H3 confirmed or eliminated; EVB-0454 needs synthesis across genuine three-way residual uncertainty, not a clean winner.

`check_hypothesis_space_integrity.py`: 1 pre-existing advisory flag (unrelated time-series drop from 2026-07-29→30 on a different question), 0 flags introduced by this edit.
