# Failure Autopsy — V3-EXQ-774 (MECH-173 REM-suppression precision recalibration)

- **Generated (UTC):** 2026-07-17T17:20:00Z
- **Run:** `v3_exq_774_mech173_rem_suppression_precision_calibration_20260717T152554Z_v3`
- **Queue:** V3-EXQ-774 · **Backlog:** EVB-0116 (IGW-20260717-207) · **Machine:** ree-cloud-2 (linux-x86_64-py3.10), 6173 s
- **Purpose:** DIAGNOSTIC (excluded from confidence/conflict scoring) · **Claim tested:** MECH-173
- **Scope:** single · **Status:** confirmed (user-confirmed 2026-07-17)

## 1. Self-route being adjudicated

Manifest `interpretation.label = mixed_inconclusive`, `evidence_direction = inconclusive`, `status = FAIL`.
The self-route is a *hypothesis*; this autopsy is the diagnostic-adjudication gate. **Adjudicated reading: `substrate_ceiling`** (see §5).

## 2. Facts (no interpretation)

Recording: always-core complete — `ree-v3/validate_recording.py` → OK (recording_schema, substrate_hash, machine/machine_class, elapsed_seconds, config, seeds all present). **No recording gap.**

**Preconditions (P0 readiness) — all MET:**
| Precondition | Measured | Threshold | Met |
|---|---|---|---|
| rv_live_all_arms | 0.4917 | 1e-6 | ✓ |
| recalib_engaged_full_sleep (mean per-cycle \|Δrv\|) | 0.000537 | 0.0001 | ✓ |
| recalib_fired_full_sleep_cycles | 20 | 1 | ✓ |

**Load-bearing criteria:**
| Criterion | Load-bearing | Passed |
|---|---|---|
| delta_recalib_positive_significant | yes | **FAIL** |
| selectivity_sws_null | yes | **PASS** |
| suppressed_arm_absolutely_overconfident | yes | **FAIL** |

**Per-arm aggregates (overconfidence_index; +=overconfident, −=humble):**
`FULL_SLEEP −0.2097`, `SWS_SUPPRESSED −0.2097`, `REM_SUPPRESSED −0.00015`, `RECALIB_OFF −0.00092`.
`arm_calibration_ratio`: FULL 1.291, SWS 1.291, REM 1.0001, RECALIB_OFF 1.0009.
`arm_true_error_ref`: all ≈ 0.00495 (FULL/RECALIB/SWS 0.0049517, REM 0.0049449).

**Paired deltas vs FULL_SLEEP (positive = MECH-173 direction):**
| Delta | per-seed [1803, 7964, 6890] | mean | sd | significant_positive |
|---|---|---|---|---|
| recalib_off − full | [0.00066, 0.00207, 0.6237] | 0.2088 | 0.2934 | **no** |
| rem_suppressed − full | [0.00120, 0.00203, 0.6255] | 0.2096 | 0.2941 | **no** |
| sws_suppressed − full | [2.3e-8, 2.0e-9, 2.8e-5] | 9.5e-6 | 1.3e-5 | (null) |

`cross_arm_spread` 0.2096 · `suppressed_absolutely_overconfident` False · `accuracy_dissociation` True · `accuracy_spread_relative` 0.0014 (tol 0.25) · `readiness_ok` True · `non_degenerate` True.

**Convergence heterogeneity (the decisive structure):** per training logs, seeds **1803 & 7964 converge fast** (rv → ~0.004, precision saturates at the F1 setpoint ceiling ~250 within 5 episodes) → **zero recalibration headroom → ~zero delta**. Seed **6890 converges slow** (rv 0.176 → 0.017, precision only ~60 at ep 30) → **full MECH-173 effect (+0.62)**. Effect magnitude tracks convergence headroom; the aggregate is a 1-of-3-seed signal.

Expected vs observed: MECH-173 predicts REM/recalibration suppression *raises overconfidence* (precision high while accuracy degrades). Observed: suppression raises confidence *in the correct direction* but only from "humble" (−0.21) toward "calibrated" (~0), never into absolute overconfidence, and only where convergence left headroom. **Which criterion failed: a discrimination + an absolute criterion** (`delta_recalib_positive_significant` and `suppressed_arm_absolutely_overconfident`), with the negative-control/selectivity criterion (`selectivity_sws_null`) **passing** — the substrate-ceiling fingerprint.

## 3. Claim-layer mapping

**MECH-173** (`mechanism_hypothesis`, status `candidate`; `depends_on` INV-048, MECH-123, INV-047, MECH-168): "REM-suppressing medications selectively impair MECH-123 precision recalibration → accelerate the earliest dementia prodrome: overconfident contextual attributions before overt memory loss." Diagnostic → not scored.

Did the test let the claim express itself? **Partially — capped by the substrate.** The direction (suppression → less humility), the accuracy dissociation (confidence shifts while true error held constant), and the REM-selectivity (SWS null) are all claim-*consistent*. But the *absolute* overconfidence signature the claim actually asserts is architecturally unexpressable on the current substrate (§5). This is **not** a falsification — it is a discovered prerequisite. MECH-173 remains `candidate`.

## 4. Biological-reference triage

- **Closest mechanism:** REM-phase precision recalibration against a *cumulative* uncertainty reference (Hobson AIM; Walker & Stickgold sleep-dependent precision; 5-HT withdrawal during REM defining the setpoint). Clinical existence proof: MCI prodrome = subjective normalcy + objective deficit (confidence decoupled from accuracy).
- **Lit status: PRESENT.** `evidence/literature/targeted_review_rem_precision_recalibration_timing/` (5 entries + SYNTHESIS, landed 2026-05-09) already adjudicated the read-site: choice (a) read `serotonin._persistent_zero_point` (the F1 cumulative reference) is dominant; (c) dual-arm preserved (Laukkonen-Friston-Chandaria 2025); (b)/(d)/F2 discarded. **No new lit-pull owed.**
- **Formal-import check / divergence (load-bearing):** the built F1 consumer models the *corrector* (a low-pass setpoint filter pulling running_variance toward the persistent zero-point) but not the *error it corrects*. In brains, waking confidence is inflated by recency/salience/reward and REM recalibration corrects that inflation against a cumulative-accuracy reference. The current substrate has (i) no waking confidence-inflation source and (ii) a setpoint anchored to a *lagging function of the agent's own running_variance* rather than to an independent accuracy signal. So removing the corrector can only remove humility, never expose overconfidence — exactly "what happens biologically if the dependency the mechanism exists to correct is absent."

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | Not falsified; direction + dissociation + selectivity are claim-consistent; the test could not fully express the claim (ceiling). |
| Biological reference | partial | Corrector modeled; missing the confidence-inflation source + accuracy anchor it corrects. Lit present. |
| Prerequisites | partial | MECH-204 GAP-1 F1 built & fired; the Phase-7/Option-B accuracy-anchored/broadcast arm + a waking inflation source are absent. |
| Implementation | partial | Symbol of recalibration present and engaged; functional role (correcting accuracy-decoupled overconfidence) cannot manifest without the inflation source. |
| Environment | too easy / converges too fast | Forward-model error → ~0.004 and precision saturates ~250 within ~5 episodes on 2/3 seeds → no recalibration headroom. A non-converging / perpetually-novel test-bed is a secondary lever on the significance-masking (not on the absolute-overconfidence impossibility). |
| Measurement | adequate | Load-bearing statistic continuous & variance-bearing (767/768 lesson honoured); accuracy dissociation independently instrumented; captured direction, dissociation, selectivity correctly. Not blind. |
| Integration | coupled | Arms differ only in intended knobs; SWS-null confirms clean coupling / no generic sleep-disruption artefact. |
| Scale / capacity | binding constraint | The F1 setpoint ceiling (accuracy-lagging anchor + fast convergence) is what caps expression. |

**Why the self-route missed `substrate_ceiling`:** its `substrate_ceiling_recalibration_subthreshold` branch gates on cross-arm *spread* < NONDEGEN_FLOOR (0.05). This ceiling does **not** collapse the spread to zero — it makes the spread *seed-dependent* (one headroom seed carries all the signal), so spread = 0.21 cleared the degeneracy gate while the substrate is still ceiling-limited. The spread-based degeneracy test is the wrong instrument for a *convergence-gated* ceiling; the honest adjudicated category is `substrate_ceiling`.

**Recommended `epistemic_category`:** `substrate_ceiling`. **Recommended `evidence_direction`:** keep `inconclusive` (diagnostic; no MECH-173 confidence weight).

## 6. Learning extracted

1. The built MECH-204 F1 recalibration produces MECH-173's *direction* (suppression removes epistemic humility) with accuracy-dissociation and REM-selectivity intact — but cannot produce *absolute* overconfidence, because the setpoint is a lagging low-pass of the agent's own running_variance and there is no waking confidence-inflation source for it to correct.
2. Two distinct failures (non-significance, no absolute overconfidence) share one architectural root (the accuracy-lagging F1 setpoint) — significance is *convergence-headroom-masked* (effect present only on the one seed that never reached the precision ceiling).
3. This is the `sleep_substrate_plan.md` **Phase 7 / Option B resume trigger**: a downstream MECH-204 consumer FAILing in a way forensic analysis attributes to "F1 alone insufficient" rather than another substrate gap. Its lit-pull dependency is already satisfied (read `_persistent_zero_point`, choice (a)).
4. A longer training budget would *worsen* the ceiling (more seeds saturate); the fixes are architectural (accuracy-anchored recalibration + inflation source) and, secondarily, a non-converging test-bed to preserve headroom.
5. Diagnostic self-route logic note: a `spread < floor` degeneracy gate cannot detect a convergence-gated ceiling; a future diagnostic in this family should gate on per-seed headroom (or condition significance on distance-to-ceiling), not on aggregate cross-arm spread alone.

## 7. Repair pathway

Node class: `complicated (buildable)` for the substrate build (the Phase-7/Option-B design is fully spec'd and lit-adjudicated — a named build, no open read-site question). Route: **`/implement-substrate`**, action **amend MECH-204**.

- Amend the `MECH-204` substrate_queue entry with the V3-EXQ-774 failure record and flag the Phase-7/Option-B resume trigger fired; governance materialises + reconciles the current V4-deferral of Phase 7 against the fresh trigger.
- Build target: an accuracy-anchored recalibration arm (Phase 7 Option B — broadcast read of `serotonin._persistent_zero_point` at `select_action()`, additive E3-score bias scaled by `rem_precision_broadcast_gain`, run alongside F1) **plus** a waking confidence-inflation source so removing recalibration can expose absolute overconfidence. Pair with a non-converging / perpetually-novel test-bed (or difficulty schedule) so recalibration headroom persists across seeds.
- After the substrate lands, a *new evidence* experiment (new EXQ number, `experiment_purpose=evidence`) can re-test MECH-173 as scored support. Do **not** re-run V3-EXQ-774 blind under a longer budget.

**Re-derive brake:** N=0 prior MECH-173 `substrate_ceiling`/`non_contributory` autopsies → **does not fire** (this is the first; N=1 < threshold 2). No requeue-refusal forced. **GOV-FANOUT-1:** not a discrimination bottleneck (single spec'd build; read-site already lit-adjudicated) → no fanout.

**`pending_retest_after_substrate`: true.** MECH-173 stays `candidate`; its remaining case is single-pathway (this one diagnostic) — no illusory-conflict-resolution risk since nothing is being demoted.

### Draft `evidence_quality_note` (governance to write on MECH-173)
> V3-EXQ-774 (diagnostic, excluded from scoring) adjudicated `substrate_ceiling` (failure_autopsy 2026-07-17): the built MECH-204 F1 precision-recalibration produces MECH-173's direction (suppression removes epistemic humility) with accuracy-dissociation and REM-selectivity intact, but cannot express absolute overconfidence — the F1 setpoint is a lagging low-pass of the agent's own running_variance with no waking confidence-inflation source to correct, and precision saturates before the recalibration lever gains headroom (effect present on 1/3 seeds only). Not falsification; a discovered prerequisite. Fires the sleep_substrate_plan Phase 7 / Option B resume trigger (accuracy-anchored / broadcast recalibration; read `_persistent_zero_point`, lit choice (a), already adjudicated). pending_retest_after_substrate.
