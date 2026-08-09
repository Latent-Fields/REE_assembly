# Failure Autopsy — MECH-075 VTA (ventral, V3-EXQ-903) / LC (dorsal, V3-EXQ-905) cluster

**Generated:** 2026-08-09T05:43:28Z
**Scope:** cluster
**Status:** confirmed (interactive gate run 2026-08-09 — user confirmed reclassifying V3-EXQ-905's filed `weakens` to `measurement_test_design_defect`)

## 1. Facts

MECH-075's `what_would_answer` text already separates dorsal (LC-arousal) and ventral (VTA-RPE) into independently falsifiable sub-hypotheses with distinct CONFIRMING/FALSIFYING criteria. Both probes were queued same-day (2026-08-08) in direct response to a governance flag naming both as the missing experiments.

### V3-EXQ-903 — ventral (VTA-RPE), first attempt ever
Signed ARC-108 `delta_t` (habenula-decommit path) gates CEM proposal noise via the MECH-267 `mode_noise_scale["rpe_gated"]` hook, narrowing shape `1/(1+RPE_GAIN*|delta_t|_ema)`. P0a (grounding, Pearson floor 0.15) + P0b (|delta_t| floor 0.001) as seed-majority preconditions; C2 basin-narrowing >=15% load-bearing.

Per-seed: only seed 7 passes P0a/P0b (corr +0.674, |dt| 0.0187); seeds 42/123 show *negative* grounding correlation (-0.04, -0.08). The manifest's top-level `preconditions[].met: true` reflects a seed-mean dominated by seed 7 and is not the operative gate — `summary.n_p0a_pass=1/3` correctly fails majority. Seed 7's apparent pass coincides with ~25x fewer eval samples (292 vs 6774-7956) than the other seeds, consistent with near-immediate episode termination — a plausible sampling confound, not confirmed grounding success. Failed criterion: precondition (readiness), majority-gate correctly not met. C2 never fairly tested.

### V3-EXQ-905 — dorsal (LC-arousal), 5th attempt, 1st non-degenerate one
Script-local `LCArousalState` (novelty via `F.mse_loss(reduction="sum")`, ~32x prior scripts' magnitude) feeds the same MECH-267 hook (`mode_noise_scale["lc_arousal"]`), widening shape `1 + LC_GAIN*arousal_ema`, `LC_GAIN=2.0`. P0 (signal-magnitude floor) PASSED (0.00428, 4.3x floor) — corrects the signal-magnitude defect of all three prior attempts (EXQ-192a/209/230). C1 (manipulation check) PASSED. C2 (basin-width widening >=15%, load-bearing) **FAILED, 0/3 seeds** — per-seed gaps `[-1.7e-8, +4.1e-9, +3.9e-8]` against basin widths ~0.0134-0.0152, i.e. relative gap ~1e-6, essentially numerical noise, sign-inconsistent.

**Calibration trace** (`ree_core/hippocampal/module.py:_compute_mode_noise_scale`): `mode_scale = 1 + LC_GAIN * arousal_ema`. At the observed eval-phase `arousal_ema` range (0.0022-0.0029) and `LC_GAIN=2.0`, `mode_scale ~= 1.0044-1.0057` — a 0.4-0.6% increase in CEM proposal std, nowhere close to plausibly producing a 15%-scale basin-width change. `LC_GAIN=2.0` is exactly the `novelty_gain=2.0` value on record in claims.yaml's prior MECH-075 `evidence_quality_note` as the constant used (and never revisited) by the original, already-failed EXQ-192a design. The sibling 903 script, by contrast, explicitly derives `RPE_GAIN=50.0` from the observed |delta_t| magnitude to land `mode_scale` in a "decisive ~0.5-0.91" range. 905's own docstring carries no equivalent derivation.

`criteria_non_degenerate.C2: true` only asserts the arms aren't pinned/identical (they vary, in both directions) — it cannot distinguish "no effect" from "effect too small to detect at this gain."

Dry-run check: both clean (`check_dry_run_citations.py`).

## 2. Claim-layer mapping

MECH-075 claim text (`docs/claims/claims.yaml`) already bifurcates dorsal/ventral into separately falsifiable sub-hypotheses. A clean FAIL on one leg does not, by the claim's own text, weigh against the other. A 2026-08-08 GOVERNANCE FLAG block in claims.yaml explicitly named both missing experiments — both landed same day.

## 3. Biological-reference triage

Literature is present and substantial (`evidence/literature/targeted_review_connectome_mech_075/`, 4 entries, + `targeted_review_hippocampal_dopamine_gain/`) — not a formal-import-with-no-lit-backing case.

**Ventral/VTA-RPE**: Duszkiewicz et al. 2018 (conf 0.70) — VTA fires on learned-expectation-filtered novelty, drives schema/semantic consolidation (generalization). Direct conceptual support for a reinforcement/valence-narrowing role. Clear.

**Dorsal/LC-arousal**: Kempadoo 2016, Galvez-Marquez 2022 (dorsal HPC memory-updating gating via D1/D5, mixed/supports 0.78-0.80); Lemon & Manahan-Vaughan 2006 (conf 0.82) — D1/D5 bidirectionally gates LTP/LTD *threshold*, a plasticity-timescale construct, not a decision-time CEM-candidate-spread construct. The REE operationalization (momentary candidate diversity at proposal time) is a licensed translation from the claim's own pre-registered text, but is one inference step removed from the literature's demonstrated mechanism — a real, worth-naming construct-validity gap that compounds with the calibration finding above (even granting the construct mapping, the applied gain was too weak to move it).

## 4. Four-layer diagnosis

### V3-EXQ-903 (ventral)
| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | test could not run fairly — readiness never established at majority level |
| Biological reference | clear | VTA/RPE -> narrowing schema-convergence |
| Prerequisites | immature | benefit/harm heads start random-init behind ARC-030 warmup |
| Implementation | partial | phased training correct in design, reliable grounding in only 1/3 seeds |
| Environment | possible confound | seed 7's ~25x smaller eval sample suggests a qualitatively different, hazard-dominated short-horizon regime |
| Measurement | under-instrumented | episode length/termination cause not recorded |
| Integration | isolated | not yet exercised against downstream selection |
| Scale/capacity | likely insufficient | 150 total episodes split ~75/75 warmup/head-grounding |

### V3-EXQ-905 (dorsal)
| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (test underpowered, not fair) | P0+C1 genuinely passed; C2 tested at an effect size far below detection threshold |
| Biological reference | partial | anatomy clear; "widening = CEM candidate spread" is one inferential step from the LTP/LTD-threshold literature |
| Prerequisites | present | MECH-267 hook real, wired production machinery |
| Implementation | complete but miscalibrated | gain application correctly wired end-to-end; LC_GAIN inherited unchanged from an already-failed design, never re-derived |
| Environment | adequate | same validated dorsal terrain as EXQ-230 |
| Measurement | adequate | basin-width metric reuses production methodology |
| Integration | coupled, stable | — |
| Scale/capacity | adequate | 150 warmup, 50 eval episodes/seed |

## 5. Cluster pattern

Not N independent bugs; also not one clean substrate ceiling. Both runs route neuromodulatory-signal-conditioned gain through the identical shared mechanism (MECH-267 `mode_noise_scale` on CEM proposal `ao_std`). The recurring structural property is methodological, not biological: **gain constants gating CEM proposal noise off small-magnitude (O(1e-3 to 1e-2)) EMA signals must be re-derived per probe from the observed signal distribution** — 903's author did this (RPE_GAIN=50, reasoned to 0.5-0.91x); 905's did not (LC_GAIN=2.0, inherited unchanged from the already-failed EXQ-192a). The narrowing-vs-widening direction asymmetry is itself well-grounded biologically and is not itself suspicious. Secondarily, 903 has a distinct seed-heterogeneous readiness-failure shape (one anomalous "pass" seed with a ~25x smaller effective sample).

## 6. Re-derive brake / granularity-debt recurrence

`granularity_debt_cluster.py MECH-075`: 8 targets across 2 grandfathered files (4 distinct runs, EXQ-192a x2, EXQ-230 x2), alignment distribution 4 intact / 0 weakened / 4 unstamped — no prior `weakened` target, all `precondition_unmet`. Under this autopsy's adjudication, neither 903 nor 905 reads `weakened` either (903 = genuine precondition FAIL; 905 reclassified to measurement_test_design_defect). **Re-derive brake: zero prior `substrate_ceiling` reads for MECH-075 — does not fire.** Granularity-debt trigger does not fire (no `weakened` target) — though MECH-075's own text already treats dorsal/ventral as separately falsifiable, so a future `/claim-synthesis` split would mostly formalize an already-latent structure, at low urgency.

## 7. Routing (confirmed)

**V3-EXQ-903** — `epistemic_category: standard`, `evidence_direction: inconclusive`. Routing: `/queue-experiment` same-question re-run (letter suffix), recording per-seed episode-length/termination-cause, increasing seed count / POSCTRL episodes to reduce small-sample correlation volatility. `recommended_substrate_queue_entry.action: none`.

**V3-EXQ-905** — **reclassified per user confirmation**: `epistemic_category: measurement_test_design_defect` (not `substrate_ceiling`, not a claim-level `weakens`), `evidence_direction: non_contributory` (was filed `weakens`). Routing: `/queue-experiment` same-question re-run with `LC_GAIN` recalibrated against the observed `arousal_ema` distribution (target `mode_scale` ~1.1-1.3, by analogy with 903's own derivation). `recommended_substrate_queue_entry.action: none`, `severity: degrading`, `substrate_paths: ["ree-v3/experiments/v3_exq_905_mech075_dorsal_lc_arousal_probe.py"]` (script-local gain constant, not a shared substrate defect).

**Step 9b**: no existing hypothesis-space qid names MECH-075. No `fanout_recommendation` was emitted (this is a calibration-defect reclassification, not a GOV-FANOUT-1 discrimination portfolio). Registration deferred — not minted in this pass.

## 8. Evidence quality notes (for governance to apply)

**V3-EXQ-903:**
> V3-EXQ-903 FAIL (2026-08-08): First attempt at MECH-075 ventral/VTA-RPE leg. Self-routed `substrate_not_ready_requeue`, confirmed correct on adjudication: P0 readiness passed in only 1/3 seeds (seed 7), with the other two showing negative grounding correlation (-0.04, -0.08). The top-level manifest `preconditions[].met: true` reflects a seed-mean statistic dominated by seed 7 and should not be read as "readiness cleared" — the seed-majority gate (`summary.n_p0a_pass=1`) is authoritative and correctly failed. Seed 7's apparent pass coincides with ~25x fewer eval samples than the other seeds, consistent with near-immediate episode termination — a plausible sampling confound, not confirmed training success. Uninformative about the ventral-leg claim; re-queue with per-seed episode-termination recording before trusting a future P0 read.

**V3-EXQ-905:**
> V3-EXQ-905 FAIL (2026-08-08): First non-degenerate manipulation test of the MECH-075 dorsal/LC-arousal leg — P0 and C1 both cleanly passed, correcting the signal-magnitude defect of all three prior attempts (EXQ-192a/209/230). C2 (basin-width widening) failed with near-zero, sign-inconsistent gaps (relative gap ~1e-6 against a 15% floor). Traced to substrate code: the manipulation gain LC_GAIN=2.0 — inherited unchanged from the already-failed EXQ-192a novelty_gain=2.0 — produces only a ~0.4-0.6% CEM-proposal-noise increase at the observed post-fix arousal_ema magnitude, an order of magnitude too small to plausibly produce a 15%-scale basin-width change. Reads as an underpowered manipulation (test-design gap), not a falsification: epistemic_category reclassified from the filed `weakens` to `measurement_test_design_defect`. Re-queue with LC_GAIN recalibrated against the observed EMA distribution (target mode_scale ~1.1-1.3) before this criterion can be considered fairly tested.
