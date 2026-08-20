# Failure autopsy -- V3-EXQ-939 (MECH-303 proximity-gated contextual-safety vigilance release)

- **Generated (UTC):** 2026-08-20T02:39:17Z
- **Scope:** single
- **Status:** confirmed (user gate 2026-08-20)
- **Session:** failure-autopsy-multi-20260819
- **Dry-run gate:** manifest checked, top-level `dry_run` absent -- not a smoke.

## 1. The headline

**The run's self-route is wrong, and a real result was discarded by a defective gate.**

`interpretation.label` is `substrate_not_ready_requeue` and `degeneracy_reason` reads:
*"substrate not ready: unmet readiness precondition(s) arm_A_release_rate_positive_control
-- the mechanism could not express itself, so nothing was measured."*

That sentence is contradicted by the manifest's own data. The mechanism expressed
itself cleanly, in the designed 2x2 shape:

| arm | context | prox_thresh | mean release_rate | num_safety_steps |
|---|---|---|---|---|
| A_safe_gate_natural | safe (nh=0) | 0.25 | **0.43889** | 240 |
| B_safe_gate_forced_closed | safe | 0.0 | **0.0** | 0 |
| C_hazard_gate_natural | hazard (nh=8) | 0.25 | **0.0** | 6 |
| D_hazard_gate_forced_open | hazard | 2.0 | **0.45** | 240 |

All three pre-registered DVs **passed**, each clearing the 0.34 margin by ~0.10:

| DV | load-bearing | gap | margin | passed |
|---|---|---|---|---|
| DV1_accumulation_necessity (A-B) | no | 0.43889 | 0.34 | yes |
| DV2_accumulation_is_the_cause (D-C) | **yes** | 0.45 | 0.34 | yes |
| DV3_gate_natural_context_appropriate (A-C) | **yes** | 0.43889 | 0.34 | yes |

`criteria_non_degenerate` is true on all three. DV3 -- which the driver's own
docstring names as *"the genuinely non-analytic one ... It could have come out
either way"* -- cleared at 0.4389.

The run was voided by **one precondition missing by 0.0067**.

## 2. The defective gate -- three independent faults, all verified in source

`arm_A_release_rate_positive_control`: measured **0.333333** vs threshold **0.34**,
offending cell `A_safe_gate_natural::seed1`.

**(F1) It aggregates by MIN while the DVs it guards aggregate by MEAN.**
- DVs: `rel = {a: _mean([r["release_rate"] for r in rows(a)])}`
  (`v3_exq_939...py:539`)
- Control: `"met": all(r["release_rate"] >= READINESS_FLOOR for r in a_rows)`
  (`:561`) -- i.e. min >= floor.

Same statistic (`release_rate`, so the V3-EXQ-643 same-statistic rule is met in
letter), but the gate is **strictly harsher than the criterion it guards**. At the
DVs' own aggregation the control passes with margin 0.099 (0.4389 vs 0.34); at min
it fails by 0.0067. The docstring's stated intent is a *best-case* check
(*"arm A's OWN release_rate -- best case"*, *"the substrate cannot express the
mechanism even at its best"*); the implementation reads the **worst** cell.

**(F2) The threshold is unreachable on the measurement lattice.**
`N_TEST_TRIALS = 30` (`:198`) and `release_rate = released / max(N_TEST_TRIALS, 1)`
(`:435`), so release_rate is quantised to multiples of 1/30 = 0.03333. Around the
floor: 10/30 = 0.33333 **fails**, 11/30 = 0.36667 **passes**. **No cell can ever
land in [0.3334, 0.3666].** The effective floor is 11/30 = 0.3667, not 0.34 -- a
silent 7.8% tightening. Seed 1 scored exactly 10/30 and missed by **0.2 of a single
trial**; one more release event in 30 would have flipped the entire run's verdict.

**(F3) The driver's own seed tolerance is dead code.**
`MIN_VALID_SEEDS = 4` (`:204`, *"seeds clearing readiness needed for a non-vacuous
verdict"*) is a pre-registered tolerance for up to 2 failing seeds of 6. It computed
`n_valid_seeds = 5 >= 4` -- pass. But `readiness_ok = all(p["met"] ...)` (`:585`) and
P1's `met` is `all(cells >= floor)` over **the same rows, the same statistic and the
same floor** (`:586`). So if every seed clears, the tolerance is moot; if any seed
fails, `readiness_ok` is already False. **`n_valid_seeds >= MIN_VALID_SEEDS` can
never bind**, and the `n_valid_seeds < MIN_VALID_SEEDS` branch (`:614`) is
unreachable. The driver pre-registered a 2-of-6 tolerance and then vetoed it with a
zero-tolerance conjunction. This run is the worked example: the tolerance said
"valid", the conjunction said "not ready", and the conjunction won.

**A fourth, structural observation.** `DV_MARGIN = 0.34` is described as
*"764's registered margin"* -- a margin a **difference** must clear. `READINESS_FLOOR`
reuses the same 0.34 as a floor an **absolute rate** must clear. Those are different
quantities and there is no principled reason they should share a number. Because arm
B is forced closed at exactly 0.0, requiring `release_A >= 0.34` is very nearly a
restatement of `release_A - release_B >= 0.34` -- so P1 is close to redundant with
DV1, evaluated at a harsher aggregation and an unreachable threshold.

## 3. Substrate readiness -- the claim the self-route makes is false

`SD-MECH303-THRESHOLD-SOURCING` in `substrate_queue.json`:
`status_phase: **validated**`, implemented 2026-08-14 (`ree-v3` `b257e7ad14`), and
its sole `failure_record` item (V3-EXQ-917) already marked `resolved` on
2026-08-16. Its resolution note states the residual gate-layer validation *"is
discharged by the owed MECH-303 behavioural retest, not by another substrate item"*.

**V3-EXQ-939 IS that retest** -- its queue entry says so. The substrate it declares
unready is built and validated, and 939's own P3/P4 reproduce the build smoke
(proximity 0.0 safe vs 0.887 hazard). All four `depends_on` (SD-011, SD-012,
ARC-007, MECH-304) are implemented per `ree-v3/CLAUDE.md`.

**One unexplained observation, recorded rather than resolved:** the queue entry's
full-scale 1-seed calibration reported A release **0.900** and D **1.000**; realised
was A 0.439 (max 0.50) and D 0.45 -- roughly **half**, at identical config and a
single driver commit. The calibration sat far clear of the floor; the realised
distribution straddles it. Nothing in the manifest explains the drop, and with n=30
binomial trials per cell and an arm-A spread of 0.3333-0.5000 (range ~5 trials), a
min-based gate at the centre of that spread is fragile by construction.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | MECH-303 was not tested to a recorded verdict, but not because the claim failed to express itself -- it did. |
| Biological reference | clear | Contextual safety learning / proximity-gated vigilance release; not a formal-definition import. Not at issue in this run. |
| Prerequisites | **present** | SD-MECH303-THRESHOLD-SOURCING validated 2026-08-14; all four `depends_on` implemented. |
| Implementation | complete | The mechanism produced the designed 2x2 dissociation. |
| Environment | adequate | P3/P4 reproduce the build smoke exactly. |
| Measurement | **misleading** | The readiness gate is mis-aggregated (F1), mis-thresholded off the lattice (F2), and carries dead tolerance code (F3). |
| Integration | n/a | |
| Scale / capacity | borderline | n=30 trials/cell gives a 1/30 lattice; arm-A per-seed spread 0.3333-0.5000. |

### Failure-location summary (GOV-FAILLOC-1)

- **MECHANISM FAILED:** not_established -- the mechanism worked.
- **MEASURES FAILED:** **established** -- the gate, not the substrate.
- **ENVIRONMENT FAILED:** not_established.
- **REE FAILED:** false.

**Net classification: MEASURES FAILED (single bucket).** This is the one target in
this batch with a clean single-bucket read.

## 5. Recurrence

Re-derive brake **does not fire**: MECH-303 ceiling hits **0** under R1-R3 (the sole
confirmed autopsy target naming MECH-303 -- V3-EXQ-930 -- is stamped `standard`).
Granularity-debt trigger does not fire (1 target, alignment `unclear`, no
`weakened`).

**Explicitly do NOT stamp `substrate_ceiling` on this run.** It would take MECH-303
from 0 to 1 and arm the brake against the next MECH-303 retest -- on a reading this
autopsy finds to be false. The named upstream would be a substrate entry whose only
open failure record is already resolved.

## 6. Routing -- CONFIRMED at the user gate (2026-08-20)

**BOTH: re-score now, and queue a confirming re-run.** (User selected the
conservative option over the recommended re-score-only.)

1. **`governance` -- re-score the existing manifest.** The pre-registered DVs all
   passed at their own aggregation on a validated substrate. Record the result as
   **provisional** evidence for MECH-303 rather than discarding a completed 530 s run.
2. **`queue-experiment` -- V3-EXQ-939a**, same question, alphabetic suffix, whose
   only substantive change is the repaired gate:
   - align the control's aggregation with the DVs it guards (mean), **or** keep min
     and justify it explicitly as a deliberately harsher gate;
   - put the floor **on the 1/30 lattice** (11/30 = 0.3667 if the intent is "clears
     10/30", or lower the trial count dependency);
   - remove or wire up `MIN_VALID_SEEDS` so the pre-registered tolerance is real;
   - explain or eliminate the ~2x calibration-to-realised gap.
3. **`evidence_direction: non_contributory`** stands for the manifest as it is --
   correct as a value, but for a **different reason** than the manifest gives: the
   gate was defective, not the substrate.
4. `epistemic_category: standard`. `recommended_substrate_queue_entry.action: none`.

### Double-counting guard (binding on governance)

Routing 1 and routing 2 answer **the same question with the same design**. They are
**not independent evidence** and must not both be counted toward MECH-303's
supports. When 939a reports, it **supersedes** the re-scored 939 reading; the
re-score exists to stop a completed result being lost in the interim, not to add a
second confirmation. Record `supersedes: v3_exq_939_...` on the 939a manifest.

## 7. Learning extracted

1. **A readiness gate must not be harsher than the criterion it guards.** The
   V3-EXQ-643 same-statistic rule is necessary but not sufficient -- it constrains
   the *statistic* and says nothing about the *aggregation*. F1 satisfies the rule
   in letter and inverts it in spirit. This is a generalisable gap in how that rule
   is currently stated.
2. **A threshold must lie on the measurement's achievable lattice.** With n discrete
   trials, any floor not a multiple of 1/n silently rounds up to the next reachable
   value. 0.34 on a 1/30 lattice is really 0.3667.
3. **A pre-registered tolerance that a later conjunction can veto is not a
   tolerance.** Check that each declared guard has a reachable state in which it is
   the binding constraint; if it has none, it is decoration.
4. **"The mechanism could not express itself" is a claim about data and must be
   checked against the data.** Here the same manifest that asserts it also contains
   the clean 2x2 that refutes it.
