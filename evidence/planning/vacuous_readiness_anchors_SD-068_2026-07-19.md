# Vacuous readiness anchors in the SD-068 driver family

Recorded 2026-07-19. Session `gracious-hermann-65e9b1`. ree-v3 `main`.

Companion to the 591-family record in `infant_substrate_plan.md`
(`infant_substrate:GAP-14` governance_2026_07_18) and to
`failure_autopsy_SD-068-rem-fanout-cluster_2026-07-18.md`.

## What this is

On 2026-07-19 (session `cranky-payne-c2c8f5`, ree-v3 `adc1c1b20e`) `assert_anchor_reachable`
guards were added to 6 SD-068 drivers, closing their anchor-reachability warnings. Those
guards test a FLOOR -- can the known-positive reference clear the gate. They say nothing
about a gate that is too EASY.

`experiments/_lib/readiness_anchor.py` documents this under "THE MIRROR FAILURE THIS GUARD
DOES *NOT* CATCH": a VACUOUS anchor -- one almost nothing can fail -- is the exact mirror of
the 778d defect and is equally a mislabel. 778d over-fails and blames the substrate; a
vacuous anchor under-fails and lets a run emit a confident verdict on an untrained channel.
`assert_anchor_reachable` will happily certify a vacuous anchor as reachable, and its error
message ("widen the predicate or lower the gate") is precisely BACKWARDS for one.

Four independent agents flagged the same smell while wiring the guards, unprompted. This
note is the audit of that smell. **No SD-068 experiment was re-run or re-queued.**

## The discriminator used

Per `readiness_anchor.py`, a global-max / range / existence form is CORRECT when the anchor
asks "does this exist at all / is the channel non-degenerate" (`v3_exq_730_q080a...`
`max_perm_peak > 0.0` and `v3_exq_669b_mech329...` `max_anchor >= 2` are named as correct
uses). The defect is rule 3: an anchor that purports to certify POPULATION READINESS while
scoring a different statistic from the one the load-bearing criterion routes on, at a floor
orders below that criterion's own gate (591: floor 0.20 vs criterion 0.994).

Mitigating factor across all six: every one aggregates over seeds with `all(...)`
(fraction 1.0), the strictest possible quantifier. The weakness is in the per-cell FLOOR,
never in the quantifier. None is vacuous in the pure existence-quantifier sense.

## Findings

| # | Driver | Anchor | Floor | Observed | Verdict |
|---|---|---|---|---|---|
| 1 | `..._consolidation_staged_damage_diagnostic.py:77` | `intact_readouts_nondegenerate` | `1e-9` | 0.5 / ~5.4e3 | **(b) rule-3 defect -- RECORDED, not fixed** |
| 2 | `..._consolidation_staging_power_diagnostic.py:93` | same | `1e-9` | same | **(b) rule-3 defect -- RECORDED, not fixed** |
| 3 | `..._sws_content_scored_readout_diagnostic.py:160` | `injected_arm_sws_sigma_slope_supra_floor` | `1e-6` | 0.323 | (a) denominator gate -- comment in place |
| 4 | `..._null_content_control_diagnostic.py:157` | `injected_arm_sigma_slope_supra_floor` | `1e-6` | ~0.0967 | (a) denominator gate -- comment in place |
| 5 | `..._rem_gen_gain_content_scale_diagnostic.py:149` | `control_input_corruption_range_supra_floor` | `0.05` | 1.5646-2.4458 | (a) existence gate -- declaration corrected |
| 6 | `..._sws_content_scored_readout_diagnostic.py:176/177` | `LADDER_SIGNAL_RATIO` / `LADDER_SPREAD_FLOOR` | `3.0` / `0.01` | 6.83 / 0.111 | healthy (~1 order); prose/code mismatch corrected |

### (b) The one genuine rule-3 instance: `intact_readouts_nondegenerate` (#1, #2)

Floor `1e-9` on `sws_signal_power` and `rem_clean_variance` at sigma=0, against recorded
readouts of ~5.4e3 and ~0.5. Headroom ~1e12x and ~5e8x -- worse than the 591 exemplar.

**Raising the floor would not repair it, and this is the point.** Two facts, both verified
in code:

1. **C1 is scale-invariant to the gated quantity.** The load-bearing criterion is C1
   (monotone degradation, `MONOTONE_CORR_FLOOR = 0.5`, `SPAN_FLOOR = 1e-3`), computed on
   `H._normalise_degradation(errs)` -- a min-max rescale to [0,1] over each phase's OWN
   sigma series (`consolidation_lesion_harness.py:1256-1272`). Any constant scale factor
   cancels. C1 mathematically cannot be affected by the raw levels this anchor gates.
2. **It does no denominator-protection work either.** The divide-by-almost-zero guards in
   `_phase_error_frac` are separate inline `> 1e-12` literals applied at EVERY sigma, not
   `INTACT_SIGNAL_FLOOR`, which is consulted only at sigma=0 and only by `_intact_ok`.

So the anchor's sole consumer is the readiness certification itself, scoring a statistic its
criterion is invariant to. That is rule 3 in its strongest form: not a mis-calibrated gate
but a mis-specified one. There is no floor value that makes it a readiness precondition
for C1.

**Not fixed in place.** Both drivers have already run. `0bfbb42` licenses in-place repair of
a mis-declared STATISTIC ("the fix is to report the COUNT, never to weaken `met`"); it does
not license moving a gate, which changes what already-recorded evidence MEANS. And here the
correct repair is not a new threshold at all -- it is a different anchor, on a statistic C1
actually routes on. That is a new EXQ letter, not an edit. The 591 precedent
("recorded but NOT fixed -- lineage blocked, all five already ran") applies directly.

**What WAS fixed in place**, on `0bfbb42`'s own terms -- the drivers' comments asserted the
enormous headroom as REASSURANCE ("no plausible seed-level jitter approaches the gate",
"seed-level jitter cannot flip it"). That is the defect read backwards, and it is a
mis-declaration of what the anchor establishes. Both comments now state the vacuity, and
`readiness_anchor.py:56-58` already warns against exactly this misreading.

### (a) Legitimate denominator gates: the `1e-6` slope floors (#3, #4)

Verified in shipped code, not merely claimed in prose: the injected-arm sigma-slope is the
literal DENOMINATOR of `null_slope_ratio_<phase> = |null_slope| / |injected_slope|`
(`consolidation_lesion_harness.py:1674-1692`), and C1 in both drivers routes on that ratio
(`NULL_SLOPE_RATIO_CEILING = 0.25`). Rule 3's statistic-identity requirement is met. A
divide-by-almost-zero tripwire BELONGS orders below the working range; the ~5-order gap is
correct design, not a smell.

Two caveats now recorded at each constant:
- `met: true` means only "the ratio was computable" -- never "the substrate was ready" in
  any stronger sense. A governance reader should not over-read it.
- The floor is largely REDUNDANT. The harness already fails the same denominator closed at
  `NULL_MIN_INJECTED_SLOPE = 1e-9` (`:1409`), reporting the phase UNAVAILABLE rather than
  scoring it. The 1e-6 anchor adds only 3 orders over a guard that already exists.

Both marked `load_bearing: False` in their manifests, which is correct.

### (a) Legitimate existence gate, mis-declared: corruption range (#5)

Floor `0.05` on the sigma-sweep RANGE of `rem_gen_input_rel_corruption`, against recorded
ranges of 1.5646-2.4458 (~31x-49x). Tightest margin of the six, and the author had ALREADY
recorded its vacuity in-file (`:194-202`), self-classifying it as the mirror of 778d.

Kept as (a) for a specific reason: `_slope_of` degenerates SILENTLY, returning `0.0` rather
than UNAVAILABLE when `den = sum((x-mx)^2) <= 1e-12`
(`consolidation_lesion_harness.py:1215`). A collapsed x-spread would therefore be scored as
a genuine zero gain. Guarding the x-range is what catches that -- real work, correctly
shaped as an existence check.

**Declaration corrected in place** (`0bfbb42` template): the comment claimed the range is
"the same statistic the gain routes on". It is not -- it is that statistic's INPUT (the
x-axis of the fit), while C1 routes on the mean per-seed delta of the fitted gain. The
existence form is sanctioned by `readiness_anchor.py`; citing it as a rule-3 same-statistic
gate is the overclaim. Floor untouched.

Also recorded: the `0.05` shared with `GAIN_SEPARATION_ABS_FLOOR` is COINCIDENTAL --
different quantities in different units, neither derived from the other, and they should not
be refactored into one constant.

### Healthy, with a prose/code mismatch corrected (#6)

`LADDER_SIGNAL_RATIO = 3.0` vs 6.83 observed and `LADDER_SPREAD_FLOOR = 0.01` vs 0.111 are
both within ~1 order -- the best-calibrated gates in the family, and 3.0 is explicitly
pre-registered ("chosen as a conventional bar BEFORE the real run, not fitted").

The module docstring called both "RELATIVE tests". C3(b) is ABSOLUTE, and on a SIGNED range
(`max(pos) - min(pos)`, no `abs()`, unlike C3(a)). Corrected in place -- a mis-declaration
of what the shipped predicate tests, squarely `0bfbb42`'s class.

## Out of scope, flagged not fixed

`v3_exq_sd068_sws_content_scored_readout_diagnostic.py:362` -- C1 gates on the raw
`null_slope_ratio_sws` and does **not** consult `content_contingent_sws`, so it does not
inherit the harness's null-degeneracy guard (`n_distinct < NULL_MIN_NULL_SERIES_DISTINCT`)
for the gated phase. This concerns C1, not an anchor, and the run has already executed.
Worth a look when that lineage next gets a letter.

## Constraint honoured

`experiments/v3_exq_sd068_rem_unpaired_null_diagnostic.py` (778d) remains UNGUARDED and
retains its anchor-reachability warning. It is the live regression specimen for
`tests/contracts/test_anchor_reachability_lint.py` a11/a14. Not touched.
