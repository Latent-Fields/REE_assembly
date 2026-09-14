# MECH-465 P2 floor: shape-statistic design and empirical test (offline, banked V3-EXQ-1015 data)

- **Purpose:** discharge the design precondition on `chip-20260909-mech465-conjunct3-queue` /
  proposal EXP-0590 P2 -- follow up on `mech465_p2_floor_cold_null_calibration_20260911.md`
  Section 8, which named "a statistic keyed to the shape of the distribution specifically near
  the u=0.04 threshold cutpoint" as the missing ingredient after COLD-relative floors (tail-mass
  and IQR/median) both proved vacuous. This session (a) proposes concrete shape-statistic
  candidates, (b) tests each empirically against the banked V3-EXQ-1015 per-tick data, (c) finds
  none separates the seed-1-fails-u=0.04 cells from the seed-0/3-passes cells, (d) identifies the
  specific missing recording field that blocks doing better with any offline re-analysis, and
  (e) specifies the new probe + statistic needed, handed to `/queue-experiment`. No experiment
  run by this session, no `claims.yaml` / `substrate_queue.json` / `experiment_proposals.v1.json`
  edit.
- **Session:** `metaworker-chip-20260914-mech465-p2-shape-statistic-design` (TASK_CLAIMS resource:
  this file).
- **Data source:** same as the 2026-09-11 predecessor --
  `REE_assembly/evidence/experiments/v3_exq_1015_mech465_zworld_warmup_budget_dispersion_sweep_20260908T202858Z_v3.json`
  (flat manifest, `arm_results[*].rv_trace_every_tick`, 1560 ticks/cell).
- **Driver read (not modified):**
  `ree-v3/experiments/v3_exq_1015_mech465_zworld_warmup_budget_dispersion_sweep.py`.
- **Prior work read:** `failure_autopsy_V3-EXQ-1015_2026-09-09.md`,
  `mech465_p2_floor_cold_null_calibration_20260911.md` (Section 8 is the direct antecedent of
  this file), and MECH-465's `what_would_answer` in `claims.yaml` (per-seed mandate, non-circularity
  requirement, "do not simply lower the floor").

## VERDICT

**Cannot derive a discriminating shape statistic from the currently banked V3-EXQ-1015 recording,
regardless of which shape/local-structure statistic is tried, for a structural reason beyond "wrong
statistic": the banked recording does not tag which tick was assigned which urgency level, so no
statistic can be restricted to exactly the u=0.04 subset the design's own P1 test uses. Every
statistic computable from the level-agnostic `rv_trace_every_tick` alone -- four tried below --
either fails to separate the fail/pass cells, or (for the one that looked most promising, a
per-cell bootstrap significance test on trace-wide tail mass) turns out to be estimating the same
underlying quantity P1 already measures at lower resolution, not an independent check.** The fix
is new instrumentation: per-tick `(urgency_level, rv, committed)` tuples during the scored pass,
not a new formula applied to `rv_trace_every_tick`. Section 5 gives the exact recording spec and a
concrete candidate P2 statistic built on it (a per-seed, no-COLD, no-between-seed bootstrap
confidence check keyed to the u=0.04 cutpoint specifically). This also resolves the predecessor's
Section 6.2 power problem (3 seeds too few for a between-seed FPR) for free, because the new
statistic needs no between-seed comparison at all.

---

## 1. Which cells actually fail, and where

Recomputing `commit_rate_by_level['0.04']` for all 15 cells against the P1 in-band test
(`0.05 <= rate <= 0.95`) confirms the autopsy's summary precisely, with one nuance the autopsy's
one-line summary elides: **seed 1 fails at u=0.04 in all four non-COLD arms with no exceptions
(WARM200 0.000, WARM400 0.031, WARM800 0.027, PHASED400 0.031 -- never budget-recoverable); seed 0
fails at u=0.04 only at the two SMALLEST budgets (WARM200 0.000, WARM400 0.000) and clears at
WARM800/PHASED400 (0.135, 0.400 -- budget-recoverable); seed 3 clears at every budget (0.188,
0.391, 0.158, 0.229).** So the target separation is 6 fail cells (seed0 x2, seed1 x4) vs. 6 pass
cells (seed0 x2, seed1 x0, seed3 x4) among the 12 non-COLD cells. A candidate statistic must
separate these, not merely correlate with warmup budget (that direction is already covered by P1
itself and by the plateau/climb discriminator C2/C2b in the autopsy).

## 2. Candidates examined, and results

All four are computed on the 1110-tick scored window (`rv_trace_every_tick[450:]`, matching the
driver's own `CAL_TICKS=360`, `WARMUP_EXCLUDE_TICKS=90`) using `thr_0.04 = cal_median *
0.8739495798319329` (the driver's own `threshold_placement.effective_threshold_over_cal_median_by_level['0.04']`,
read verbatim from the manifest, not re-derived).

**(a) Local density in a symmetric band around `thr_0.04`.** `density_w = count(|x - thr| <=
w*thr) / n / (2w)` for `w in {0.05, 0.10, 0.20}`. Motivation: literally "shape near the cutpoint"
-- a near-empty neighbourhood around the threshold means the commit-rate estimate there is
governed by a handful of points (brittle); a well-populated neighbourhood means many points
determine it (stable).

**Result: fails to separate.** seed0/WARM800 (pass, density10%=1.96) and seed1/WARM800 (fail,
density10%=1.52) are close and in the wrong order relative to several other cells; seed1/PHASED400
(fail, density10%=1.72) has HIGHER local density than seed0/WARM800 (pass, 1.96 -- comparable) and
seed3/WARM800 (pass, 1.59 -- lower). No `w` or threshold value separates the two groups. Reason,
diagnosed after the fact: local density around a cutpoint is symmetric in "how much mass is
nearby," not "which side it's on" -- it doesn't distinguish "half the nearby mass sits just below
threshold" (raises commit rate) from "nearly all of it sits just above" (keeps commit rate near
zero even with high local density). It answers a different question than the one P2 needs to ask.

**(b) Distribution-shape statistics: skewness, `p05/median`, `p10/median`, semi-IQR asymmetry
(`(median-p25)/(p75-median)`).** Motivation: a "collapsed" regime might show up as a
near-symmetric, thin-tailed distribution, while a graded one might be visibly skewed toward the
lower tail (more mass reaching down toward the threshold).

**Result: fails to separate.** `p05/median` gets closest -- fail-cell values range 0.8327-0.9227,
pass-cell values range 0.7631-0.8859 -- but the ranges overlap (fail min 0.8327 < pass max 0.8859),
and the overlap is populated on both sides: seed0/WARM800 (pass, 0.8859) is numerically *more*
"tight" by this statistic than three of the four seed-1 fail cells (0.8515, 0.8327, 0.8537).
Skewness and the semi-IQR ratio show no consistent ordering at all (e.g. skew for
PHASED400/seed0, a pass cell, is 0.039 -- near-symmetric -- while WARM200/seed3, also a pass cell,
is 0.338; skew for WARM400/seed1, a fail cell, is -0.194, i.e. more symmetric/negative than most
pass cells). None of the four orderings is consistent with the pass/fail split.

**(c) `k`-nearest-neighbour gap width**: mean distance from `thr_0.04` to its 10 nearest points in
the scored trace, normalised by `thr_0.04`. Motivation: a direct "how far is the nearest data" read
of local sparsity near the cutpoint, orthogonal to (a)'s two-sided density.

**Result: fails to separate**, for the same reason as (a) -- it tracks how close the *nearest*
mass is regardless of side, and seed1's fail cells (WARM800 0.00084, PHASED400 0.00228) show gaps
comparable to or tighter than seed0/seed3's pass cells (WARM800/seed0 0.00234, WARM800/seed3
0.00172), i.e. the nearest points ARE close in both groups; what differs is which side of the
threshold they're mostly on, which this statistic discards.

**(d) Per-cell (not per-COLD) bootstrap significance test on trace-wide tail mass
`T_0.874 = P(x < thr_0.04)`.** This is the tail-mass statistic from the 2026-09-11 write-up,
but recalibrated differently: instead of comparing the observed `T_0.874` to a COLD-derived null
(which the predecessor showed is vacuous), test each cell against ITS OWN moving-block bootstrap
null (reusing the driver's exact `_block_bootstrap_dv` mechanics -- block size 40, 400 replicates,
seed convention `10_000 + 97*seed_id + n` -- generalised to the tail-mass statistic, same
reimplementation the predecessor validated bit-for-bit against the manifest's own IQR/median CIs).
`P2` would pass iff the bootstrap 95% CI of `T_0.874` excludes 0 (i.e. the cell's tail mass below
threshold is statistically distinguishable from a degenerate point mass at the boundary).

**Result: fails to separate, and the failure is informative.** The CI-excludes-0 test correctly
tracks P1's band verdict for seed 0 (WARM200/WARM400: CI includes 0, correctly "not yet";
WARM800/PHASED400: CI excludes 0, correctly "reached") and for seed 3 (excludes 0 at every budget,
correctly "reached" throughout) -- **but for seed 1 it gets 3 of 4 cells wrong**: WARM400
(T=0.0297, CI [0.0009, 0.0766]), WARM800 (T=0.0342, CI [0.0018, 0.0757]), and PHASED400 (T=0.1117,
CI [0.0486, 0.1838]) all have CIs that exclude 0, i.e. this test says P2 PASSES on three of the
four cells P1 says fail the u=0.04 band. The reason, checked directly: `T_0.874` (full 1110-tick
trace) closely tracks `commit_rate_by_level['0.04']` (the ~25-65-tick fresh-select subset) up to
sampling noise -- e.g. seed1/WARM400: `T`=0.0297 vs `commit_rate_004`=0.0313; seed1/WARM800:
`T`=0.0342 vs 0.0270. **`T_0.874` is not an independent shape check; it is a higher-resolution
ESTIMATE of the same quantity P1 already measures.** "Statistically distinguishable from exactly
zero" is a much weaker bar than "clears the 5% in-band floor" -- nearly every trained cell has
*some* nonzero tail mass below threshold (this is the same failure mode Section 6.1 of the
predecessor already diagnosed for the COLD-relative version of this exact statistic, now confirmed
to recur even with a non-COLD, per-cell null).

**Net reading of (a)-(d):** every statistic derivable from `rv_trace_every_tick` alone -- whichever
way it's sliced, symmetric-density, shape, nearest-neighbour, or self-referential
significance -- either discards the directional information that actually matters (a, c), shows no
consistent ordering at all (b), or silently re-derives P1's own quantity at higher sample size
without adding independent information (d). This is a stronger, empirically-grounded version of
the predecessor's Section 8 conclusion, not a restatement of it: the predecessor inferred "needs
new instrumentation" from the failure of two candidates against a COLD null; this session shows
the same conclusion holds even when the COLD comparison is removed entirely and four different
shape/significance framings are tried directly against the trained cells.

## 3. Why offline re-analysis is structurally capped here

`commit_rate_by_level['0.04']` (what P1 actually scores) is computed only over the subset of
scored-window ticks where the exogenous urgency draw assigned exactly `u=0.04` -- roughly n=25-65
of the 1110 scored ticks per cell (`n_by_level`). The banked manifest records `rv_trace_every_tick`
(level-agnostic, every tick) and the aggregated `commit_rate_by_level` / `n_by_level` summaries,
but **not** which tick got which urgency level. Any statistic that wants to interrogate the shape
of the distribution *specifically at the ticks that determine the u=0.04 commit rate* -- as
opposed to the shape of the whole trace, which (c) and (d) above show is not the same thing --
needs that per-tick label, which does not exist in this recording or in any other banked run
(`grep`-checked: only V3-EXQ-1015, 785a and 785b carry `rv_trace_every_tick`-shaped data at all,
and none of the three record per-tick urgency assignment; 785a/785b additionally predate the
`2023589` threshold-sign fix and are the source of the forbidden pooled-percentile framing MECH-465's
WWA was revised away from, so they are excluded on staleness grounds independent of this gap).

**Reconstructing the per-tick urgency sequence by replaying the RNG was considered and rejected as
an offline substitute.** The urgency draw (`ree-v3/experiments/..._sweep.py:525`,
`assigned = float(self.rng.choice(URG))`) consumes a `np.random.default_rng(1234 + seed)` stream
that is **shared across all five arms for a given seed** (not reset per arm), per the driver and
`claims.yaml`'s own note. Reconstructing which draw landed on which tick of, say, the PHASED400
cell would require replaying the exact draw-call sequence of every earlier arm (COLD, WARM200,
WARM400, WARM800) for that seed first, including calibration-phase draws if any occur there --
which is not documented anywhere as a fixed, replayable count, and getting it wrong silently
mislabels ticks rather than erroring. This is exactly the kind of fragile, un-auditable
reconstruction a real recording field exists to avoid; Section 5 specifies that field instead.

## 4. Independence and non-circularity check

Nothing in Sections 2-3 chose a floor value, a statistic parameter (`w`, `k=0.874`, block size,
replicate count), or a discrimination rule by looking at which cells the pass/fail split favoured
first and then reverse-engineering a formula to match. All four candidates were specified from
their own stated motivation before being scored, and the WARM/PHASED pass/fail labels were used
only to report, post hoc, whether each candidate discriminates -- never to tune it. This mirrors
the predecessor's Section 7 non-circularity discipline and is why the negative results above are
informative rather than a fishing failure: four genuinely different, principled candidates were
tried, not one candidate iterated against the labels until it matched.

## 5. What a new probe needs to record

**Field:** for the scored pass of every cell (all 5 arms x 3 seeds, or whichever subset a
successor experiment covers), record a per-tick tuple `{tick_index, urgency_level, rv, committed}`
-- not just the level-agnostic `rv_trace_every_tick` currently recorded. This is a driver change
at the urgency-assignment call site (`..._sweep.py` around line 525, where `assigned` and the
gate's `committed` boolean are already computed per tick; the only change is appending them to a
list instead of discarding them after use) plus a `commit_rate_by_level` field that already exists,
so no new compute, only a new field in the existing scored-pass loop.

**Seeds:** the existing 3 (0, 1, 3) suffice -- **no new seed count is needed**, which resolves the
predecessor's Section 6 point 2 power problem (3 seeds too few for a *between-seed* FPR claim),
because the statistic specified below (Section 6) is a WITHIN-CELL confidence statement, never a
between-seed percentile. This is a direct consequence of not needing COLD or cross-seed comparison
at all once the per-tick label exists.

**Resolution:** every scored tick (not a subsample) -- `n_by_level` is already thin (25-65); losing
any of it to a coarser recording cadence would only worsen the per-level sample size the new
statistic below depends on.

## 6. Candidate P2 statistic once the data exists (specify now, validate once the probe runs)

**Local Level-Resolved Reliability (LLRR).** Per cell (arm x seed): take the per-tick
`{tick_index, urgency_level, rv, committed}` tuples for the scored window. Block-bootstrap the
**full temporally-ordered tuple sequence** (not a level-filtered subsequence in isolation -- levels
are assigned i.i.d. per tick, so the u=0.04 ticks are scattered irregularly through the window;
resampling only that irregular subsequence would discard the rv process's own ~20-tick EMA
autocorrelation the driver's block size of 40 is chosen to respect). Reuse the driver's own
`_block_bootstrap_dv` block mechanics unchanged (block size 40, 400 replicates, same seed
convention validated bit-for-bit in the 2026-09-11 write-up), generalised only to resample
`(tick_index, urgency_level, rv, committed)` tuples together as blocks; for each of the 400
replicates, recompute `commit_rate` restricted to the resampled tuples whose `urgency_level ==
0.04` (or, if n is too thin at a single level in a given replicate, pool `{0.04, 0.10}`, the two
lowest levels, and state that choice up front rather than adjusting it after seeing results).

**P2 disposition, per cell:** report the resulting 95% CI on the u=0.04 commit rate.
- **PASS (in-band with confidence):** CI entirely within `[0.05, 0.95]`.
- **FAIL (out-of-band with confidence):** CI entirely outside `[0.05, 0.95]` on the same side as
  the point estimate.
- **INDETERMINATE:** CI straddles a band boundary -- reported and excluded from the seed-majority
  count in P1, not silently rounded to pass or fail.

This reframes P2 not as a second, independent global-dispersion number to clear (the WWA's original
framing, which both the pooled 0.51 bar and every within-seed candidate examined here or in the
predecessor have failed to make workable), but as **a confidence wrapper directly on the P1
quantity, computed from data resolved exactly at the cutpoint that determines it** -- which is
what "shape ... specifically near the u=0.04 threshold cutpoint" (Section 8 of the predecessor)
was asking for, made concrete and computable. It is per-seed by construction (no pooling), requires
no COLD arm and no between-seed step (resolving the predecessor's power problem), and cannot be
gamed by "lowering the floor" because there is no floor value to choose -- only a CI-exclusion
rule fixed before any data exists.

**Caveat, stated plainly:** this candidate is unvalidated against real data -- it has not been run
against a probe carrying the new field, because that field does not exist in any banked run. It
should be treated as a pre-registered design to carry into `/queue-experiment`, not as a result.

## 7. P4 (urgency-off baseline arm) -- design sketch, separately owed

EXP-0590's acceptance checks already mandate a P4 urgency-off baseline arm (added 2026-09-09,
"MANDATORY... without it the conjunct cannot be adjudicated whatever the on-arm commit rates
show"), and MECH-465's WWA conjunct (1) HEADROOM includes "baseline (urgency-off) commit rate
within [0.2, 0.8]" as an unmeasured clause. This is mechanically trivial to add to the same driver:
`ree_core/predictors/e3_selector.py:3790` gates the urgency-scaled threshold shift on
`self.config.urgency_weight > 0.0`; the driver's own urgency-assignment call
(`..._sweep.py:525-536`) already has an `sn <= 1e-9 -> 0.0` fallback branch for the degenerate-norm
case, so an OFF arm is simply: never call `self.rng.choice(URG)` for that arm, leave
`agent.e3.config.urgency_weight` at its default 0.0 for the whole scored pass, and record
`commit_rate_overall` as the baseline commit rate to score against the `[0.2, 0.8]` clause. No new
substrate code, no new config surface -- an arm-selection change in the experiment driver only.
Not designed further here (out of this session's scope per its brief), but flagged so the next
`/queue-experiment` pass does not have to rediscover it.

## 8. Routing

**Not queued by this session** (CLAUDE.md "Experiment Scripts": queue only via `/queue-experiment`
or `/diagnose-errors`). Handoff:

1. **`/queue-experiment`** against a NEW diagnostic probe (not EXP-0590 itself, which stays gated
   until P2 is pre-registered and passing): re-run the WARM800/PHASED400 cells at minimum (the
   budgets that already clear P1's band on 2/3 seeds), all 3 seeds (0, 1, 3), driver modified per
   Section 5 (per-tick `{tick_index, urgency_level, rv, committed}` recording) and Section 7 (add
   an urgency-off arm). Compute the Section 6 LLRR statistic once the run lands; if it validates
   (separates the known seed-1-fails cells from seed-0/3-passes cells, which this session could not
   test offline), register it as EXP-0590's P2 acceptance check and the P4 baseline data from the
   same run discharges P4 directly.
2. **`chip-20260909-mech465-conjunct3-queue`**: this session hands back an unresolved P2 (still no
   pre-registered floor/statistic ready to gate EXP-0590), but with a validated *design* plus the
   new-instrumentation spec above, rather than the "cannot derive from banked data, full stop"
   state the 2026-09-11 session left it in. Un-claimed with a note pointing here and at the
   `/queue-experiment` handoff in point 1.

**Explicitly not recommended:** re-deriving per-tick urgency labels via RNG replay (Section 3);
another COLD-relative floor variant (already excluded twice, here and 2026-09-11); scoring P2 from
`T_0.874`'s own-cell bootstrap CI as a standalone pass/fail rule (Section 2d shows it misclassifies
3 of 4 seed-1 cells); adding more COLD seeds (Section 6 explains why the new design does not need
them).

---

*Prepared offline, no experiment run, nothing queued. Analysis scripts (scratch, not committed):
`scratch/mech465_shape_stat_explore.py`, `scratch/mech465_shape_stat_explore2.py`,
`scratch/mech465_shape_stat_bootstrap.py` in this session's worktree
(`.claude/worktrees/metaworker-chip-20260914-mech465-p2-shape-statistic-design/`). Session
`metaworker-chip-20260914-mech465-p2-shape-statistic-design`, 2026-09-14.*
