# Failure autopsy -- V3-EXQ-1047 (MECH-482)

Status: confirmed (user gate 2026-09-17)
Generated: 2026-09-17T17:57:22Z
Run: `v3_exq_1047_mech482_amplified_readout_ladder_20260917T025403Z_v3`
Purpose: diagnostic | Outcome: PASS | Direction: non_contributory
bears_on: `orienting_epistemic_deficit_v3_plan:ORNT-2`

## 0. Headline

**The run's self-routed label is NOT SUSTAINED.** The manifest routes
`deficit_readout_magnitude_limited` ("H-MAG SUPPORTED: the real readout's own ORDERING moves
the COMMITTED E3 selection once amplified to the rail"). The run's own cells refute it. The
honest label is the driver's own `inconclusive_controls_did_not_separate` branch.

This matters because 1047 is the spike that `failure_autopsy_V3-EXQ-964b_2026-09-16`
pre-registered as the `live_gate` for the registry question `mech482_deficit_selection_authority`.
Acted on as self-routed, it would have closed that question as decided and routed a gain build
on evidence where a value-shuffled control outperforms the real readout.

## 1. Facts

Dry-run gate: CLEAN. Recording: `validate_recording.py` OK, 0 always-core gaps.
substrate_hash `5c5bd966...`, machine `DLAPTOP-4.local`, 3 seeds [71,101,202],
elapsed 8663.7 s. Note `substrate_commit.dirty` = true.

Gain ladder k in {1,10,40,100} at SHIPPED `curiosity_bias_scale` = 0.1
(`RAIL_RANGE` = 0.2, `RAIL_FRACTION` = 0.95, so "at rail" means >= 0.19).
All 8 preconditions met. Positive control `ARM_VERIFY_LIFT_S10` fires 3/3 at every rung.
Self-yoked control 0.0 divergence over 60 compared ticks.

### Seeds firing, by rung (committed selection divergence > 1e-9)

| rung | real | synthetic | permuted | real separates above BOTH? |
|---|---|---|---|---|
| k=1 | 0 | 0 | 0 | no -- all silent |
| k=10 | 0 | 1 | **2** | no -- permuted fires on a MAJORITY, real fires zero |
| k=40 | 2 | 1 | 1 | no -- union(controls) == real's firing set exactly |
| k=100 (rail rung) | 2 | 2 | 1 | no -- equal seed counts, larger control divergences |

### At the rail rung, per seed

| seed | real range | at rail (>=0.19) | real fires | synthetic fires | permuted fires |
|---|---|---|---|---|---|
| 71 | 0.200000 | YES | 0.00000 | 0.00000 | 0.00000 |
| 101 | 0.183872 | no | 0.01042 | **0.03125** (3x) | 0.00000 |
| 202 | 0.200000 | YES | 0.03030 | **0.06061** (2x) | **0.12121** (4x) |

Conditioned on reachable flips at k=100 the real arm converts **2/26 (7.7%)** against
synthetic **19.2%** and permuted **15.4%**. **No cell at any rung has the real arm above
both controls.**

## 2. Why the PASS carries almost no information

`outcome` is set by a four-branch chain (driver L855-905). **Three of the four branches emit
PASS.** FAIL requires only a red precondition or no rung at the rail. `C0_instrument_gate`
is `sum(p["met"] for p in preconditions)` against `len(preconditions)` -- the criterion and
its own pass predicate are the same quantity -- and
`criteria_non_degenerate["C0_instrument_gate"]` is a **hard-coded literal `True`** (L998).

`F_MAG` (driver L847-853) is `real_seeds_firing >= majority`. **It contains no control term.**
It is satisfied by the real arm alone. "Firing" is one diverged committed tick above a
`DIVERGENCE_FLOOR` of 1e-9 -- the two firing seeds carried exactly **one tick each** (1/96 and
1/33).

The driver already contains the correct branch. Its `inconclusive` text states the collapse
mechanism verbatim: "compute_score_bias pins every railed candidate at +/- curiosity_bias_scale
... so at high saturation the real, synthetic and permuted vectors all collapse toward the SAME
railed pattern and the three arms stop being distinguishable BY CONSTRUCTION rather than by
finding." Branch ORDER is what let the control-free `F_MAG` pre-empt it.

## 3. Two draft claims WITHDRAWN at the Step 7c pass

Recorded rather than deleted, so a later session knows they were tested and did not hold.

1. **"The at-rail and firing seed sets are disjoint" -- WITHDRAWN, false.** At-rail is
   {71, 202}, firing is {101, 202}; the intersection is **{202}**. The defensible statement is
   that no seed MAJORITY is both at-rail and firing -- the intersection is one seed carrying
   one tick.
2. **"`real_clamp_saturated_frac` 0.53125 provably destroys the ordering" -- WITHDRAWN as
   stated.** That figure is a maximum over ticks AND over seeds, occurring on seed **71**,
   which fires 0/28. Per-seed maxima are 0.53125 / 0.03125 / 0.25. The clamp-collapse mechanism
   remains live and the driver names it, but this number does not establish it at the firing
   cells.

Neither withdrawal touches the refutation, which rests on the control contrast in section 1.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | the run does not test MECH-482's own signatures |
| Biological reference | partial | LC-NE orienting; elementwise clamp is not a biological gain mechanism |
| Prerequisites | present | 8/8 gates; positive control 3/3 at every rung |
| Implementation | complete | harness works; the defect is the finding criterion |
| Environment | adequate | -- |
| Measurement | **under-instrumented AND misleading** | control-free F_MAG; 1e-9 floor; PASS on 3 of 4 branches |
| Integration | isolated | -- |
| Scale | 3 seeds | the majority rests on two seeds x one tick each |

**Failure-location summary (GOV-FAILLOC-1): MEASURES.** Measurement adequacy is NOT
established, so REE FAILED is unavailable by the table's own threshold. Single-bucket
MEASURES; the run says nothing about MECH-482 in either direction.

## 5. Re-derive brake -- FIRES

**MECH-482 literal count = 3** (964, 964a, 964b) against a threshold of 2 -- **already at
threshold WITHOUT this target.** The gate is `>=`, so whether 1047 itself counts is moot.

The producer releases stamped by 964a and 964b are **inoperative** under R3 clause 3: both owe
an `amend`, and `sd_epistemic_deficit_multitarget_readiness` is `implemented_pending_validation`,
not IMPLEMENTED/VALIDATED, so the landed-release does not take.

964b released this brake by explicit user decision at its own gate. **This is the second
consecutive gate at which it has been reached and the first at which it has been allowed to
fire** (user decision, Step 8, 2026-09-17).

- **REFUSED:** a further same-claim lettered re-test of the SD-102 readout's selection
  consequence against the same substrate.
- **NOT REFUSED:** a different-mechanism redesign under a new EXQ number with different
  `claim_ids`.
- **Route:** `implement-substrate` on `sd_epistemic_deficit_multitarget_readiness`.

**Cost of firing, recorded rather than hidden:** the instrument defect in section 2 stays
UNREPAIRED while the build proceeds. The next run on this claim risks reproducing the same
uninterpretable result unless the build itself addresses the control-free criterion.

## 6. Fan-out -- recorded but GATED

H-mag and H-pat both remain **ALIVE**; neither is resolved. The registry question's
`live_gate` ("H-mag vs H-pat spike scores") is **UNMET**, and the question does **not** become
decidable.

Both legs are EXISTING legs on the EXISTING question. This autopsy opens no leg and performs
no Mode A growth -- the probes below re-specify how the same two legs are discriminated, so no
growth event is owed.

| hypothesis | axis | probe sketch | declared null |
|---|---|---|---|
| H-mag | measurement | re-run the ladder with a CONTROL-BEARING criterion: real > max(synthetic, permuted) on a seed majority, at the highest rung whose `real_clamp_saturated_frac` is below a pre-registered ceiling | real does not exceed both controls |
| H-pat | representation | score the readout's cross-candidate ordering directly against E3's runner-up structure (rank correlation on near-tie ticks), independent of gain | zero rank correlation |

**GATED behind the substrate build.** The brake fired; this portfolio is not licensed to run
before that build lands.

## 7. Step 7b / 7c

- **7b:** 0 fires. C5 and C7 `inapplicable` -- "could not look", not "no fire".
- **7c: CONTESTED.** Model `claude-opus-5` -- the SESSION model, **not** cross-model
  (`claude-fable-5-1` returned HTTP 429 monthly spend limit twice; re-spawned once on the
  session model per Step 7c). Same-model pass: shares the drafter's priors. Findings accepted:
  D1 and D2 (the two withdrawals in section 3), D3 (the brake question was posed at the wrong
  level -- claim-level count already 3, which changed the routing), D4 (a `fanout_recommendation`
  was owed and missing). The refutation direction was independently re-derived by the pass and
  **strengthened**: the strongest steelman (k=40, below saturation, real 2 vs controls 1/1) dies
  on firing-set identity -- union(controls) equals real's set exactly.

## 8. Routing

`implement-substrate` on `sd_epistemic_deficit_multitarget_readiness`. Substrate entry:
`amend`, severity unchanged at `degrading`, adding the failure record. Same-claim re-queue
REFUSED per section 5.

Per-claim disposition and the `-> stamp this artifact` citation change are in the companion
`.json`. `/governance` applies them.
