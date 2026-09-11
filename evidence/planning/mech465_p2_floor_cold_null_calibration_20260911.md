# MECH-465 P2 floor: COLD-null calibration attempt (offline, banked V3-EXQ-1015 data)

- **Purpose:** discharge the design precondition on `chip-20260909-mech465-conjunct3-queue` /
  proposal EXP-0590 -- register a per-seed P2 (dispersion-floor) statistic that is derived
  **independently of V3-EXQ-1015's own pass/fail split** (the 785a pooled 0.51 figure is void;
  the run's own lower-tail-mass number quoted in the autopsy is circular). No experiment run,
  nothing queued, no `claims.yaml` / `substrate_queue.json` / `experiment_proposals.v1.json`
  edit. Pure offline re-analysis of already-banked `rv_trace_every_tick` data from
  `v3_exq_1015_mech465_zworld_warmup_budget_dispersion_sweep_20260908T202858Z_v3`.
- **Session:** `mech465-p2floor-0911` (TASK_CLAIMS resource:
  `REE_assembly/evidence/planning/mech465_p2_floor_cold_null_calibration_20260911.md`).
- **Data source:**
  `REE_assembly/evidence/experiments/v3_exq_1015_mech465_zworld_warmup_budget_dispersion_sweep_20260908T202858Z_v3.json`
  (the flat manifest; the run-pack `manifest.json` is thin per the autopsy and was not used).
- **Driver read (not modified):**
  `ree-v3/experiments/v3_exq_1015_mech465_zworld_warmup_budget_dispersion_sweep.py` and
  `ree-v3/experiments/_lib/baselines/mech465_zworld_warmup_dispersion.py`.

## VERDICT

**Cannot derive a credible, discriminating per-seed P2 floor from the banked COLD-arm data.**
A COLD-null-calibrated floor is computable and non-circular (it never reads the WARM/PHASED
pass/fail split), but every version tried -- the autopsy's own candidate tail-mass statistic
at its recorded cutpoint, that same statistic at eight other cutpoints, and the original
IQR/median dispersion statistic -- turns out to be cleared by **every one of the 12 WARM/PHASED
cells on every seed**, including every seed-1 cell the autopsy says fails the P1-band clause.
The floor exists but is vacuous: it cannot separate the cells the design needs separated. See
Section 5 for why, Section 6 for the power problem layered on top, and Section 7 for what is
actually missing.

---

## 1. Cell inventory

15 cells (5 arms x seeds {0, 1, 3}), each carrying a 1560-tick `rv_trace_every_tick` (calibration
360 ticks + scored pass 1200 ticks). All 15 are `gate_green: true` in the manifest.

```
COLD/seed0       trace_len=1560   WARM200/seed0    trace_len=1560   WARM400/seed0    trace_len=1560
COLD/seed1       trace_len=1560   WARM200/seed1    trace_len=1560   WARM400/seed1    trace_len=1560
COLD/seed3       trace_len=1560   WARM200/seed3    trace_len=1560   WARM400/seed3    trace_len=1560
WARM800/seed0    trace_len=1560   PHASED400/seed0  trace_len=1560
WARM800/seed1    trace_len=1560   PHASED400/seed1  trace_len=1560
WARM800/seed3    trace_len=1560   PHASED400/seed3  trace_len=1560
```

The DV's scored window is `rv_trace_every_tick[CAL_TICKS + WARMUP_EXCLUDE_TICKS :]` =
`rv_trace_every_tick[360+90:]` = the last **1110** ticks (`CAL_TICKS=360`,
`WARMUP_EXCLUDE_TICKS=90`, both from `_lib/baselines/mech465_zworld_warmup_dispersion.py`).
Recomputing `IQR(rv)/median(rv)` over that exact window against every one of the 15 cells'
recorded `rv_iqr_over_med` and `rv_med` fields matches **bit-for-bit** (e.g. COLD/seed0:
recomputed 0.00994999709407005 vs manifest 0.00994999709407005; `rv_med`
0.006150595218243833 both). This confirms the window and statistic used below are exactly the
ones the driver itself uses, not a re-derivation that merely resembles it.

## 2. The statistic, exact definition

Two statistics are examined, both computed on the 1110-tick scored-window trace `x`:

- **DV (the driver's own P2 statistic):** `IQR(x) / median(x)` (`np.percentile(x,75) -
  np.percentile(x,25)) / np.median(x)`.
- **Tail-mass `T_k` (the autopsy's candidate, `failure_autopsy_V3-EXQ-1015_2026-09-09.md`
  lines ~87-90):** `T_k = P(x_i < k * median(x))`, i.e. the fraction of the 1110 ticks whose
  running-variance falls below `k` times the trace's *own* median. `k = 0.874` is on record
  there ("the lower-tail mass P(rv < 0.874*median)"), and is exactly
  `(1 + u_min) / (1 + U_MID) = 1.04 / 1.19` -- the ratio the driver uses to place the
  *effective commitment threshold* at the lowest urgency level relative to the *calibration*
  median. Recomputing `T_0.874` on the scored-window trace (not the calibration trace) for
  WARM800/seed0 and WARM800/seed1 reproduces the autopsy's own figures exactly: 0.032432 and
  0.120721 respectively, confirming this is the statistic being referenced.

**Keeping k=0.874 vs changing it:** kept as the primary candidate because it is the value
already on record and it is not an arbitrary choice (it is the design's own lowest-urgency
threshold ratio, so it has a stated arithmetic justification independent of any fitted floor).
Section 5 also reports `T_k` at eight other cutpoints (0.50-0.99) as a sensitivity/diagnostic
sweep -- not because 0.874 is in doubt as a choice, but because the COLD-null result at 0.874
turns out to be degenerate (Section 4), and the sweep is needed to characterise *why* rather
than just report a null result.

## 3. Bootstrap procedure: reused, not reinvented

The driver's own `_block_bootstrap_dv` (`v3_exq_1015_..._sweep.py` lines 356-376) is a
moving-block bootstrap: resample the 1110-tick trace in blocks of `BOOT_BLOCK_TICKS=40`
(rv is an alpha-0.05 EMA with ~20-tick memory, so an i.i.d. bootstrap would understate sampling
error), concatenate `ceil(1110/40)=28` resampled blocks with replacement, truncate to length
1110, and compute the statistic on the resampled series; repeat `BOOT_REPLICATES=400` times
with `np.random.default_rng(seed)`, `seed = 10_000 + 97*seed_id + len(arm_id)`.

It is hardcoded to `IQR/median`. Rather than inventing a new resampler, I **reimplemented it
faithfully**, generalised only to accept an arbitrary statistic function, keeping the exact
same block size, replicate count, and RNG seeding convention (so a "COLD" bootstrap for a given
seed_id resolves to the identical PRNG stream the driver itself would use for an IQR/median
bootstrap on that same cell). **Validation of the reimplementation:** running it with the
original `IQR/median` statistic on all three COLD cells reproduces the manifest's own recorded
`rv_iqr_over_med_ci95` and `rv_iqr_over_med_boot_se` **exactly** (bit-for-bit, e.g. seed 3:
CI [0.03163678104949433, 0.061576164562283875], SE 0.007910104405479608, both matching the
manifest to full float precision). The generalisation to the tail-mass statistic is therefore
running the identical resampling mechanics the driver already validated, with only the summary
function swapped.

## 4. COLD null: tail-mass statistic (k=0.874) -- degenerate

`T_0.874` computed directly on COLD's own scored-window trace (no resampling) is **exactly
0.0000 for all three seeds** (0/1110 ticks fall more than 12.6% below the trace's own median).
Running the full 400-replicate block bootstrap per seed gives 400/400 finite replicates, **every
one of which is also exactly 0.0000** -- COLD's dispersion is so tight (IQR/median 0.0099-0.0425)
that no block-resampled reconstruction of the trace ever produces a value 12.6% below its
median either. Consequently:

| FPR | floor(T), seed 0 | floor(T), seed 1 | floor(T), seed 3 |
|---|---|---|---|
| 10% (p90) | 0.0000 | 0.0000 | 0.0000 |
| 5% (p95) | 0.0000 | 0.0000 | 0.0000 |
| 1% (p99) | 0.0000 | 0.0000 | 0.0000 |

The floor is **identical across every tested FPR** because the null distribution is a point
mass at zero -- there is no percentile to choose between. This is a real, non-circular result
(it never touches WARM/PHASED data), but it is uninformative on its face: every one of the 12
WARM/PHASED cells has an observed `T_0.874` strictly greater than 0 (range 0.0000 to 0.2333;
only WARM200/seed1 also happens to read exactly 0), so a floor of 0.0000 is cleared trivially by
nearly the entire sweep regardless of seed or arm, including the cells the autopsy itself
labels as failing the P1-band clause (e.g. WARM800/seed1, T=0.1207, clears a floor of 0 just as
easily as WARM800/seed0, T=0.0324, does).

**Sensitivity sweep across k** (observed COLD `T_k`, no resampling, seeds 0/1/3):

| k | seed0 | seed1 | seed3 |
|---|---|---|---|
| 0.99 | 0.0784 | 0.2072 | 0.3622 |
| 0.95 | 0.0000 | 0.0000 | 0.0126 |
| 0.90 | 0.0000 | 0.0000 | 0.0000 |
| 0.874 | 0.0000 | 0.0000 | 0.0000 |
| 0.85 / 0.80 / 0.70 / 0.60 / 0.50 | 0.0000 | 0.0000 | 0.0000 |

The statistic only leaves zero once `k` is pushed to within ~1-5% of 1.0 -- i.e. once the
cutpoint is calibrated to COLD's *own* near-point-mass width rather than to any
warmup-independent, design-motivated ratio. That does not rescue the approach: at `k=0.99` the
"floor" would just be re-deriving COLD's own shape, with no connection to the u=0.04 threshold
ratio that motivated 0.874 in the first place, and no reason to think it transfers to a warmed
regime's very different distribution shape.

## 5. COLD null: IQR/median (the original DV) -- non-degenerate but still uninformative

Unlike the tail-mass statistic, COLD's own DV values are non-zero and vary by seed (0.0099,
0.0185, 0.0425 for seeds 0/1/3), so its block-bootstrap null is a genuine, non-degenerate
distribution:

| seed | observed DV | boot mean | boot SD | p95 | p99 |
|---|---|---|---|---|---|
| 0 | 0.0099 | 0.0100 | 0.0013 | 0.0122 | 0.0135 |
| 1 | 0.0185 | 0.0183 | 0.0026 | 0.0229 | 0.0243 |
| 3 | 0.0425 | 0.0439 | 0.0079 | 0.0588 | 0.0634 |

Checking every one of the 12 WARM/PHASED cells against its **own seed's** p95 and p99 floor:

**every single cell clears both**, by a wide margin -- e.g. seed1/WARM800 (DV 0.1518) clears its
own p95 floor (0.0229) by 6.6x, and seed1/WARM200 (DV 0.0995) -- the very cell the autopsy notes
misses the P1-band clause at every budget -- clears it by 4.3x. The margin never comes close to
zero for any seed x arm combination in this sweep. So a COLD-calibrated DV floor, exactly like
the tail-mass floor, provides **no separating power** between the "seed 1 misses 5/6 P1-band
levels" cells and the "seed 0/3 reach 6/6" cells -- both groups clear a COLD-relative dispersion
floor equally trivially.

## 6. Power statement (honest)

Two independent problems, not one:

1. **The statistic/reference mismatch (Sections 4-5) is not a small-sample artefact** -- it
   would not be fixed by more COLD seeds. COLD's dispersion sits roughly one to two orders of
   magnitude below *every* trained cell in this sweep, on every seed, for both statistics
   tried. Any floor calibrated as "clears COLD's own sampling noise" is going to sit far below
   the entire population of trained-cell values, because the manipulation (warmup) moves the
   statistic 3-27x regardless of which seed reaches the P1-band clause. The floor answers "is
   this cell measurably different from an untrained one?" (yes, always, trivially) rather than
   the design's actual question ("is this cell's dispersion big enough that its P1-band pattern
   is trustworthy, as opposed to seed 1's apparent shortfall?").
2. **Separately, and compounding it: 3 seeds is too few to responsibly calibrate ANY per-seed
   floor at a stated FPR against a *between-seed* null even if the statistic were well
   chosen.** The percentiles reported above (p90/95/99, or p95/99 for the DV) are all drawn from
   **within-trace block-bootstrap resampling of a single realised 1110-tick series per seed**
   (28 blocks per trace, given rv's ~20-tick EMA memory) -- they characterise the *sampling
   precision* of that one seed's own statistic, not the *population* variability of what a
   degenerate/untrained regime's dispersion could plausibly be across seeds. With only 3
   independent seed realisations, there is no empirical basis for a between-seed percentile at
   all (the smallest non-trivial empirical percentile obtainable from n=3 draws is ~33%), so a
   1% or 5% FPR claim would be describing the wrong axis of uncertainty -- it is measurement
   precision dressed up as a false-positive rate. This problem would remain even if Section 4's
   degeneracy and Section 5's separating-power failure were both fixed.

**Conclusion on power:** with the COLD arm's seed count and the statistics tried, this is not
"a floor with a wide but usable CI" -- it is "too few seeds, and the wrong statistic axis, to
calibrate a per-seed floor at a credible FPR." Reporting a numeric floor here (0.0000 for the
tail-mass statistic, or the DV p95 values above) would carry false precision.

## 7. Independence check

Nothing in Sections 3-6's *derivation* of the null distributions or the candidate floors reads
`rv_iqr_over_med`, `commit_rate_by_level`, `levels_in_p1_band`, or any other field from the
WARM200/WARM400/WARM800/PHASED400 cells, and no WARM/PHASED value was used to choose `k`, the
block size, the replicate count, or the FPR levels tested. The only place WARM/PHASED values
appear is Sections 4-5's post-hoc discrimination check ("does the floor, once fixed from COLD
alone, actually separate anything?") -- run strictly *after* each floor was already computed,
used only to report that the floor is cleared by everything, and never fed back into any floor
value reported above. This satisfies the non-circularity requirement the claim's
`what_would_answer` states and that GFLAG-0238 / the autopsy flagged as violated by the 785a
pooled 0.51 figure and by the run's own lower-tail-mass number.

**Is COLD contaminated as a structural control?** No evidence of that. It runs the identical
harness, identical per-seed RNG streams (`np.random.default_rng(1234+seed)` for the urgency
draws, shared across all five arms for a given seed), identical calibration/recalibration
procedure, and identical scored-window length -- differing only in `p0a_episodes=p0b_episodes=0`.
It is a legitimate structural negative control for "does warmup move the dispersion statistic
at all" (it does, by 3-27x, on every seed). It is simply **not powered to answer the sharper
question this design needs answered**: which of two already-warmed regimes has a dispersion
level *trustworthy enough that its P1-band pattern isn't noise*. That is a mismatch between the
control and the question, not a defect in the control itself.

## 8. What is actually missing (for the "cannot derive" branch)

1. **More COLD-arm seeds** (order of tens, not 3) would be needed before any COLD-calibrated
   floor could claim a credible between-seed FPR at all -- but per Section 6.1 this would still
   not fix the separating-power problem, because COLD's dispersion is categorically smaller than
   any trained cell's regardless of seed count.
2. **A different kind of statistic than "trace-level dispersion magnitude relative to an
   untrained baseline."** Since a COLD-relative floor (tail-mass or IQR/median, at any FPR
   tried) is cleared by every trained cell on every seed, whatever separates seed 1's cells
   (5/6 P1-band levels, always missing at u=0.04) from seed 0/3's (6/6) is not captured by
   overall trace dispersion versus COLD. A candidate worth building (not attempted here, and
   explicitly out of this task's scope -- it would need new instrumentation, not banked data):
   a statistic keyed to the *shape* of the distribution specifically near the u=0.04 threshold
   cutpoint (e.g. a local density or a seed-relative percentile-crossing statistic), rather than
   a global dispersion ratio compared to an unrelated baseline arm.
3. **The urgency-off baseline arm** the pre-flight and the autopsy both already flag as missing
   from conjunct (1) is a separate, independently-owed gap; it is not fixed or touched by this
   task and remains outstanding regardless of this finding.

Until (2) in particular is addressed, no per-seed P2 floor calibrated against COLD -- with any
seed count -- would be expected to discriminate the seed-1-vs-seed-0/3 pattern that motivated
looking for a floor in the first place.

---

*Prepared offline, no experiment run, nothing queued. Analysis script (scratchpad, not
committed):
`/private/tmp/claude-501/-Users-dgolden-REE-Working/eda43c28-4da2-4e23-bdd2-c329e232aa5d/scratchpad/mech465_p2_floor_cold_null.py`.
Session `mech465-p2floor-0911`, 2026-09-11.*
