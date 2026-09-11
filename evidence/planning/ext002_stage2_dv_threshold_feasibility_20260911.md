# EXT-002 stage 2: DV threshold feasibility and revisit-volume risk from banked data

**Produced:** 2026-09-11T15:38:43Z, read-only pass against banked manifests only (no runs).
**For:** chip `chip-20260909-ext002-latching-stage2` (proposes queueing a 27-38h cloud run for
stage 2 of the 983-lineage / EXT-002 latching-repertoire spike). Pre-flight verdict was AMBER
(`science_chip_preflight_verdicts_20260910.md`) on exactly the two questions answered here.

## VERDICT

**Not derivable from banked data -- and the reason it is not derivable is the same reason the
revisit-volume risk is real.** Do not pre-register a numeric stage-2 DV threshold from what is
banked today. Recommend: either (a) run a short, cheap calibration pass (not the full 27-38h
lineage run) whose only purpose is to bank the new DV on a handful of seeds and set the bar from
that, or (b) accept that stage 2's readiness precondition (not the DV itself) is the correct place
to certify per the 983a routing note's own P7-style "DV-freedom certification under a control
policy before training" -- but note that even the *readiness* gate (revisit_denominator) has a
material, non-hypothetical chance of failing again, for the same structural reason.

---

## 1. Manifest inventory

Found and read in full:

- `REE_assembly/evidence/experiments/v3_exq_983a_ext002_residue_error_persistence_headroom_20260905T141459Z_v3.json`
  -- the residue-freeze ablation (A0_INTACT vs A1_RESIDUE_FROZEN), 8 seeds, `outcome: FAIL`,
  `non_degenerate: false` (vacuous -- every arm RED on preconditions `revisit_denominator` and
  `revisit_outcome_heterogeneity`). This is the ONLY banked run that measured per-(arm,seed)
  revisit counts and erred-key counts; it is the sole empirical basis for both questions below.
- `REE_assembly/evidence/experiments/v3_exq_1014_ext002_lineage_e3_latching_repertoire_spike_20260908T223415Z_v3.json`
  -- stage-1 spike, same 8 seeds, `outcome: PASS`, `non_degenerate: true`. Confirms the casualty
  set (same 6 seeds excluded by 983a's completion gate) and gives per-seed harm/steps context
  (`readout.survival_latching_association`) but does **not** measure revisits to erred keys at
  all -- it is a different instrument (fresh-decision action-class histogram), not a source for
  the stage-2 DV.
- `REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-1014_2026-09-09.md` (+ .json) -- the
  confirmed diagnostic that ratified stage 2 and carries the per-seed table (harm-on-held,
  harm/held-tick, mean steps) cited in the task brief.
- `REE_assembly/evidence/planning/science_chip_preflight_verdicts_20260910.md` -- durable copy of
  the AMBER verdict this note is resolving.
- `ree-v3/experiments/v3_exq_983a_ext002_residue_error_persistence_headroom.py` -- read for the
  precondition/gate mechanics (`build_gate`, `analyse`, `FLOOR_REVISIT_DENOMINATOR_P4 = 4.5`,
  `FLOOR_STEPS_REALIZED_FRAC = 0.60`, `CEILING_HARM_RATE_TRAINING_COMPLETE = 0.35`,
  `MIN_POOLED_SEEDS = 2`).
- `ree-v3/experiments/v3_exq_1014_ext002_lineage_e3_latching_repertoire_spike.py` -- confirmed
  (grep) it does not compute revisit statistics; not a source for the DV.

Not found / could not check: no other `v3_exq_983*` or `v3_exq_1014*` manifest exists under
`REE_assembly/evidence/experiments/` (single run each, confirmed by directory listing). No banked
run anywhere computes "fresh-decision revisits to erred keys **per unit exposure**" -- the exact
statistic stage 2 needs. `grep -r MIN_POOLED_SEEDS ree-v3/` returns 0 hits outside the 983a
docstring/constant itself -- confirming the chip's own claim that this is a stage-2-only term with
no existing implementation to inspect.

---

## 2. The DV, precisely, and what banked data does and does not contain

Stage 2's DV per 983a's ratified routing_note (carried verbatim into the 1014 autopsy, Section
1c): **"fresh-decision revisits to erred keys per unit exposure, early vs late, A0 minus A1."**

983a's own `decline` statistic (`repeat_rate_early - repeat_rate_late`, where `repeat_rate_*` is
the mean **outcome** (0/1: did this revisit repeat the harm) of `n_revisits_early/late` events) is
explicitly barred from reuse -- it is a REPEAT-RATE DV (conditional harm probability given a
revisit occurred), not a REVISIT-AVOIDANCE DV (how often the agent revisits an erred key at all).
The two are different statistics built from the same underlying event log:

- 983a's barred DV needs `revisit_events` to exist at all (it conditions on a revisit happening)
  and asks "does the outcome improve."
- Stage 2's DV needs no revisit outcome -- it asks "does the RATE of revisiting fall," i.e. it is
  a normalized COUNT (`n_revisits_early / exposure_early` vs `n_revisits_late / exposure_late`),
  not a conditional-outcome rate.

**No banked manifest computes the normalized-count form.** 983a records the raw ingredients
(`n_revisits_early`, `n_revisits_late`, `n_distinct_erred_keys`, `realized_total_steps`) but never
divides by exposure -- `repeat_rate_early/late` in the banked JSON is NOT this DV, it is the
barred one. Building the stage-2 DV from banked data therefore requires deriving it, not reading
it off a field.

### 2a. A constructed proxy, for illustration only

Using `rate = n_revisits_{early,late} / (realized_total_steps // 2)` as the natural per-unit-
exposure normalization (the early/late split 983a already uses), and restricting to the only two
seeds that would actually survive stage 2's own completion gate (`floor_steps_realized_frac=0.60`,
`ceiling_harm_rate_train=0.35` -- see Section 4, these are the seeds a control-arm calibration
must be computed over, since they are the population stage 2 will actually draw from):

| seed | arm | realized steps | rev_early | rev_late | rate_early | rate_late | decline-analog (early-late) |
|---|---|---|---|---|---|---|---|
| 456 | A1_RESIDUE_FROZEN (control) | 21465 | 105 | 92 | 0.009784 | 0.008572 | **+0.001212** |
| 31 | A1_RESIDUE_FROZEN (control) | 22000 | 0 | 0 | 0.0 | 0.0 | **0.0** (0/0, degenerate) |

A "control-arm range" over these two points is `[0.0, 0.0012]` -- and the lower bound is not a
real measurement, it is `0/0` on a seed that never generated an erred key. This is not a credible
basis for a pre-registered floor, for three independent reasons (not just "small n"):

1. **n = 2, and one of the two data points is degenerate by construction**, not merely noisy.
   Seed 31's harm rate is 0.015 (essentially no hazard contact across 22,000 steps) -- there is no
   erred key to revisit, so its "rate" is not a small measurement of a real quantity, it is the
   absence of the phenomenon. A range whose floor is a non-event is not a headroom range in the
   sense 983's own C1 threshold used one (see 2b).
2. **The one non-degenerate point (456) is a single run, single seed.** 983's original C1
   threshold (0.04) was itself derived from ONE predecessor run's control-arm range
   (`predecessor_control_range: 0.0467896501434286`, from `v3_exq_983` per the 983a manifest's
   `dv_headroom_gate`) -- already a thin basis, criticized nowhere in the record but structurally
   the same "n=1 run" problem. Stacking a *second* thin derivation (proxy DV, n=2 seeds, 1 of which
   is void) on top of a lineage that already leans on a single-run range compounds rather than
   fixes the problem.
3. **The proxy is not independent of the comparison stage 2 will make.** Stage 2's own primary
   contrast is A0 minus A1 on this same statistic. Calibrating the threshold from A1 alone (the
   only arm with a clean "no residue effect possible" interpretation) is the right *design*
   instinct (matches how 983's C1 was calibrated against the frozen control), but with the
   population collapsed to 2 seeds the "range" is really just "whatever 456 happened to do,"
   which is indistinguishable from post-hoc curve-fitting to the one seed that will very likely
   also be *in* the actual pooled run. Seed 456 (or a seed statistically like it) is one of the
   `MIN_POOLED_SEEDS=3` stage 2 needs to draw -- so a threshold set from its own control-arm value
   is not independent of the run it would gate.

**Conclusion on question 1: no credible numeric bar is derivable from banked data.** What is
missing is not more arithmetic on the existing 8 seeds -- it is banked measurement of this DV on a
larger, independently-drawn sample of completion-gate-surviving seeds, which does not exist yet
because the DV itself has never been computed by any driver script.

---

## 3. Why "cannot derive a bar" and "revisit-volume risk" are the same finding

Section 2's proxy calculation only had two data points to work with because 983a's own completion
gate (which stage 2 inherits, per the routing note's re-use of the same gate machinery) already
filtered the 8-seed draw down to 2 survivors -- and the very property that lets a seed survive
(low, sustained harm rate; near-full episode length) is the same property that suppresses erred-key
generation. A seed cannot revisit an erred key it has never produced. So the population stage 2
is defined to draw from is structurally biased toward the low-revisit tail, which is exactly what
starves both the DV calibration (Section 2) and the readiness precondition (Section 4).

---

## 4. Per-seed revisit-volume table (banked, all 8 pinned seeds, both arms)

Indexed seed-major by `(seed, arm_id)`, read directly from `arm_results` -- never assumed
positional. Completion gate = `steps_realized_frac >= 0.60 AND harm_rate_train <= 0.35` (983a's
own constants). Revisit floor = 983a's `FLOOR_REVISIT_DENOMINATOR_P4 = 4.5`, applied here **per
(seed, arm) cell** for illustration (983a's actual gate takes the MIN across all POOLED cells, see
below -- a single failing cell fails the whole precondition).

| seed | arm | harm_rate | steps_frac | completion gate | erred keys | revisited keys | revisits early | revisits late | cell clears 4.5 floor |
|---|---|---|---|---|---|---|---|---|---|
| 7 | A0_INTACT | 0.4674 | 0.1157 | fail | 9 | 7 | 73 | 75 | pass |
| 7 | A1_RESIDUE_FROZEN | 0.4889 | 0.1110 | fail | 10 | 8 | 67 | 85 | pass |
| 11 | A0_INTACT | 0.1319 | 0.4750 | fail | 9 | 7 | 234 | 230 | pass |
| 11 | A1_RESIDUE_FROZEN | 0.1313 | 0.4720 | fail | 7 | 6 | 233 | 234 | pass |
| 17 | A0_INTACT | 0.4751 | 0.1084 | fail | 6 | 5 | 52 | 55 | pass |
| 17 | A1_RESIDUE_FROZEN | 0.4732 | 0.1101 | fail | 6 | 5 | 51 | 58 | pass |
| 23 | A0_INTACT | 0.9870 | 0.0559 | fail | 5 | 2 | 53 | 54 | pass |
| 23 | A1_RESIDUE_FROZEN | 0.9870 | 0.0559 | fail | 5 | 2 | 53 | 54 | pass |
| **31** | A0_INTACT | 0.0150 | 1.0000 | **PASS** | 0 | 0 | 0 | 0 | **FAIL** |
| **31** | A1_RESIDUE_FROZEN | 0.0150 | 1.0000 | **PASS** | 0 | 0 | 0 | 0 | **FAIL** |
| 42 | A0_INTACT | 0.8196 | 0.0595 | fail | 3 | 3 | 52 | 55 | pass |
| 42 | A1_RESIDUE_FROZEN | 0.8196 | 0.0595 | fail | 4 | 3 | 52 | 54 | pass |
| 123 | A0_INTACT | 0.7647 | 0.0742 | fail | 8 | 6 | 55 | 58 | pass |
| 123 | A1_RESIDUE_FROZEN | 0.7695 | 0.0759 | fail | 8 | 8 | 54 | 60 | pass |
| **456** | A0_INTACT | 0.0212 | 0.9598 | **PASS** | 8 | 7 | 104 | 102 | pass |
| **456** | A1_RESIDUE_FROZEN | 0.0204 | 0.9757 | **PASS** | 9 | 6 | 105 | 92 | pass |

**Headline pattern:** of the 8 pinned seeds, **only 2 (456, 31) survive the completion gate** --
the same 2 that 983a itself pooled, and the same 2 that 1014 found were the only non-casualties
(1014's own per-seed table: seed 456 mean_steps 194.9, harm/held-tick 0.012; seed 31 mean_steps
200.0, harm/held-tick 0.011 -- both effectively "constant mover" profiles). **Of those 2 survivors,
one (seed 31) has ZERO erred keys and therefore zero revisits in either arm** -- it clears the
completion gate precisely because it almost never touches a hazard, which also means it can never
generate the event the DV is built to measure.

**Naive, unconditional read (all 8 seeds, per-cell):** 7/8 seeds (14/16 cells) clear the 4.5
revisit floor -- this reads as reassuring and is the wrong number to use.

**Conditional read (only the seeds stage 2 will actually retain):** of the 2 completion-gate
survivors, **1 of 2 (50%) fails the revisit floor outright (0 < 4.5), and it does so on BOTH
arms simultaneously.** 983a's actual gate takes the MIN across all pooled cells (`build_gate`,
`_min("n_revisits_early")` over the pooled set) -- so this one seed alone was sufficient to drag
983a's own `revisit_denominator` precondition to `measured: 0.0`, failing against the 4.5 floor
and making the entire run vacuous (`non_degenerate: false`, "No arm passed its gate... this run is
NOT a refutation"). This is not a hypothetical failure mode -- **it already happened, in the one
banked run that tried this exact population.**

**Extrapolation to stage 2's draw (uncertain, small-sample, stated as such):** stage 2 raises
`MIN_POOLED_SEEDS` from 983a's 2 to 3, and per the 1014 autopsy's own pricing, only ~1/8 freshly
drawn seeds are expected to clear the completion gate (so ~12-24 draws for 3 survivors, ~27-38h).
If the ~50% split observed here (1 of 2 survivors being revisit-degenerate) is even roughly
representative of the survivor population's composition -- both 456 and 31 are "constant-mover"
profiles by 1014's own classification, so there is no known confound making 31 an outlier among
survivors -- then drawing 3 survivors carries a non-trivial chance (illustratively, `1-0.5^3 =
87.5%` under a naive iid assumption, which should be read as directional, not exact, given n=2)
that **at least one of the 3 pooled seeds reproduces seed 31's zero-revisit profile**, and if the
same min-across-pooled-cells gate structure is reused for the revisit-volume precondition, that
one seed fails the whole run regardless of how well the other two behave.

---

## 5. Answers

**(1) Can a defensible numeric threshold be pre-registered for stage 2's DV?**
No. Not derivable from banked data. No banked run has ever computed the per-unit-exposure
revisit-avoidance statistic; the two seeds that would calibrate it (the only ones matching stage
2's actual draw population) give a "range" of `[0.0, 0.0012]` where the floor is a non-event
(zero erred keys), not a measurement -- and the one live data point (seed 456) is not independent
of the pooled run stage 2 will actually run, since a seed statistically like it is expected to be
in that pool. This is a "cannot" finding in the MECH-465 sense: well-evidenced, not a shrug.

**(2) Quantify the revisit-volume risk.**
Of the 8 banked seeds, only 2 clear the completion gate stage 2 inherits, and one of those 2 has
zero erred keys and zero revisits in either arm -- reproducing, in the one banked run that tried
this population, the exact P4 `revisit_denominator` failure the task brief flagged as a known
prior failure. The unconditional "7/8 seeds have plenty of revisits" reading is true but
irrelevant, because those 6 non-surviving seeds will never be in stage 2's pool. If the observed
50% degenerate-seed rate among survivors is representative, most 3-seed draws will include at
least one revisit-degenerate seed, which is enough (under 983a's own min-across-pooled-cells gate
logic) to make the entire 27-38h run vacuous, exactly as 983a itself was.

---

## 6. Recommendation

**Derivable but the revisit-volume risk makes the 27-38h spend unwise until X**, where X is
specifically: (a) bank the new per-unit-exposure DV on at least ~6-8 freshly drawn
completion-gate-surviving seeds via a short, cheap calibration-only run (not the full lineage
run) so a real control-arm range exists, and (b) decide, before queueing, whether the
revisit-volume precondition will be a min-across-pooled-cells gate (983a's structure, which a
single seed-31-like draw defeats) or a majority/median-across-pooled-cells gate (more robust to
exactly this failure mode, at the cost of being a new precondition design not yet red-teamed).
Queueing the full 27-38h run today, with no threshold and the same brittle gate structure that
already produced one vacuous run on this exact population, risks spending the entire budget on a
second vacuous result.

---

*Claim: `ext002-dvthreshold-0911`. Resources: this file only. No writes to
`ree-v3/experiment_queue.json`, `ree-v3/experiments/`, `claims.yaml`, or `substrate_queue.json`.*
