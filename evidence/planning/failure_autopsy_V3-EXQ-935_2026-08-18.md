# Failure autopsy -- V3-EXQ-935 (MECH-266 / SD-032a)

- **Generated (UTC):** 2026-08-18T01:14:28Z
- **Scope:** single
- **Status:** confirmed (Step 8 interactive gate cleared 2026-08-18)
- **Target:** `v3_exq_935_mech266_margin_normalised_cap_rule_20260817T075758Z_v3`
- **Queue ID:** V3-EXQ-935 -- `experiment_purpose: diagnostic`, outcome **FAIL**
- **Claims tagged:** MECH-266, SD-032a
- **Session:** `cranky-driscoll-126a36`

## Headline

**The run's own pre-registered acceptance function returns PASS at two r values inside its own
pre-registered sweep.** It returns FAIL only at `R_STAR = 2.25`, a constant imported from
V3-EXQ-934. The self-route `cap_recalibration_is_seed_idiosyncratic` (H-IDIO) is **refuted by the
run's own designated aliasing control**, which the driver built precisely to prevent this
misreading and then never consulted.

## 1. Dry-run gate (Step 2a)

`scripts/check_dry_run_citations.py` over every run this autopsy cites:
`v3_exq_935_...`, `v3_exq_934_...`, `v3_exq_936_...` -> **0 dry cited, 0 dry in named families,
0 ambiguous, 3 clean, 0 unknown** (exit 0). No smoke enters any denominator below. The real-run
denominator for every fraction quoted here is **5 seeds** (42, 43, 44, 45, 46), all guard-passing.

`validate_experiments.py --checks dry_run_unreachable_criterion` is silent on this driver; the
manual read of its dry-run reduction block found no criterion gated on an unreachable episode
index (the sweep is cell-structured, not episode-index-gated).

## 2. Facts (no interpretation)

### 2a. Recording provenance

`ree-v3/validate_recording.py`: **OK -- complete, 0 always-core gaps, 0 thin-pack drops,
0 schema warnings.** `substrate_hash`, `substrate_commit`, `machine`, `machine_class`, `config`,
`seeds`, `elapsed_seconds` all present. No recording-debt finding. Run: `ree-worker-1`,
`linux-x86_64-py3.10-torch2.12.0+cpu`, 18.9h wall clock, start ~2026-08-16T13:01Z.

### 2b. What the run measured

Per seed: train one curriculum agent; run frozen-policy eval cells on clones.
`ARM_CALIB` at `cap = CAP_REF = 0.75` yields that seed's `baseline_margin` m_seed
(**measured in-run**, not imported). `ARM_NORM` cells at `cap = r * m_seed` for
r in {1.85, 2.05, 2.25, 2.45, 2.65}. `ARM_ABS` control at a fixed `cap = 1.75`.
DV = `fraction_in_external_task`; "graded" = occupancy strictly inside (0.10, 0.90).

Pre-registered criteria (all thresholds constants in the driver):

- **C1** [load-bearing] -- at the single r = R_STAR, ARM_NORM occupancy graded on
  >= `MIN_FRACTION` = 2/3 of guard-passing seeds. A **common-rule** test.
- **C2** [load-bearing] -- C1 restricted to out-of-sample seeds (45, 46), >= 1/2.
- **C3** [load-bearing] -- strictly more seeds grade under ARM_NORM at R_STAR than under
  ARM_ABS at 1.75, same seeds, same run.
- **Gate:** `PASS iff C1 AND C3 AND (C2 OR C2 scoped out)` -- plain AND, recorded explicitly.

`R_STAR = 2.25`, pre-registered, derived as the mean of three r values banked by V3-EXQ-934
(2.224 / 2.278 / 2.229 = 2.244, rounded). Deliberately the mean, not a value chosen to make any
seed clear the band.

### 2c. Readiness anchors -- all cleared

| Anchor | measured | threshold | met |
|---|---|---|---|
| `contact_non_vacuity` (foraging guard) | 1.00 (5/5) | 0.667 | yes |
| `margin_ready` (drive engages) | 1.00 (5/5) | 0.667 | yes |
| `calib_ready` (calibration statistic alive) | 1.00 (5/5) | 0.667 | yes |
| `r_star_measured` | 1.00 (5/5) | -- | yes |
| `manipulation_landed` | true | -- | yes |

**No precondition was unmet.** This is not a starved run and not a `precondition_unmet` case.

### 2d. Scored result

`c1_rule_grades_at_r_star: false` (2/5 = 0.40 vs 0.667) -> `rule_supported: false` -> **FAIL**,
self-route `cap_recalibration_is_seed_idiosyncratic`,
`route_reason: no_common_normalised_rule_outperformed_the_best_absolute_cap`.

**C2 passed** (`c2_rule_generalises_out_of_sample: true`, 1/2 >= 0.5) and
**C3 passed** (`c3_beats_best_absolute_cap: true`, 2 graded normalised vs 0 graded absolute).
**C1 is the only failing criterion.**

### 2e. The full sweep -- the fact the routing did not read

Occupancy at every swept r (graded band 0.10 < occ < 0.90; `MIN_FRACTION` = 2/3):

| r | s42 | s43 | s44 | s45 | s46 | C1 n/5 | C1 | C2 oos | C3 | **GATE** |
|---|---|---|---|---|---|---|---|---|---|---|
| 1.85 | 1.000 | 0.555 | 1.000 | 1.000 | 0.986 | 1/5 | fail | 0/2 fail | 1>0 pass | FAIL |
| 2.05 | 1.000 | 0.597 | 1.000 | 0.998 | 0.916 | 1/5 | fail | 0/2 fail | 1>0 pass | FAIL |
| **2.25** | 1.000 | 0.448 | 0.990 | 0.925 | 0.837 | 2/5 | fail | 1/2 pass | 2>0 pass | **FAIL** <- R_STAR |
| **2.45** | 1.000 | 0.289 | 0.721 | 0.781 | 0.562 | **4/5** | **pass** | **2/2 pass** | **4>0 pass** | **PASS** |
| **2.65** | 1.000 | 0.124 | 0.656 | 0.281 | 0.204 | **4/5** | **pass** | **2/2 pass** | **4>0 pass** | **PASS** |
| ABS (cap 1.75) | 1.000 | 0.000 | 1.000 | 0.000 | 0.000 | 0/5 | -- | -- | -- | -- |

The C1 count is **monotone in r**: 1/5, 1/5, 2/5, 4/5, 4/5. Occupancy is monotone decreasing in r
**within every seed**. At r = R_STAR the occupancy ordering across seeds
(0.448 < 0.837 < 0.925 < 0.990 < 1.000) is **strictly monotone in `baseline_margin`**
(0.3217 < 0.3549 < 0.3623 < 0.7851 < 0.8139). The residual after normalisation is **completely
systematic**, not idiosyncratic: the ratio rule *under-corrects*, so higher-margin agents need a
larger multiplier.

`graded_at_some_r_fraction_INFO_ONLY: 0.8`, `occupancy_varies_across_r: true`,
`margin_varies_across_r: true`, `manipulation_landed: true`.

### 2f. Mode accounting

Sound: `mode_step_counts` sums to `total_steps` in **35/35 cells**, and
`fraction_in_external_task` reproduces `external_task / total_steps` exactly. The DV is
well-formed.

Two scope facts worth recording: `internal_replay` and `offline_consolidation` are **0 in all 35
cells** -- the "mixed regime" is strictly a two-mode split (`external_task` vs
`internal_planning`), not a four-mode regime. And seed 42 is **flat at occupancy 1.000 with
`n_switches: 0` across the entire sweep** (caps 0.75 -> 2.157, a 2.9x range): its margin falls
monotonically 0.8139 -> 0.6115, so the cap does move the continuous signal, but the arbitration
threshold is never crossed. Seed 42 is the sole non-grader and its required r lies **above the top
of the tested sweep**.

## 3. Claim-layer mapping

### MECH-266 (`mechanism_hypothesis`, status `provisional`, `pending_retest_after_substrate: true`)

Asymmetric mode hysteresis -- a Schmitt trigger with per-mode `(enter_threshold, exit_threshold)`
pairs, `exit < enter` for stable modes; over-binding (OCD axis) = `exit -> 0`, under-binding
(depression axis) = the asymmetry collapsing. `depends_on: [SD-032a, MECH-259, SD-033]`.

**V3-EXQ-935 contains no asymmetric-threshold arm at all.** It sweeps a single symmetric
`affinity_input_cap`. The Schmitt trigger was never instantiated, so the claim could not express
itself. This is a *calibration run upstream of any MECH-266 test* -- its purpose is to make the
arbitration produce a graded regime so that a MECH-266 over-binding test becomes runnable.
`non_contributory` is correct and is **UPHELD**.

Tag accuracy: MECH-266 is inherited from the 464/467/934 lineage and is **peripheral** on this
run. Recorded as such in `recommended_epistemic_category_per_claim` so the re-derive brake does
not attribute a ceiling reading to a claim this run did not exercise.

### SD-032a (`design_decision`, status `stable`)

The mode register with enter-threshold logic. The driver stamps `weakens` from the branch
`elif (all readiness anchors met) -> weakens  # "no rule generalises"`. That comment is false on
this run's data: a rule **does** generalise, at r = 2.45 and r = 2.65, on 4/5 seeds including 2/2
out-of-sample.

On the substance, the register performed **better here than anywhere else in this lineage**:
graded, non-degenerate occupancy spanning 0.124-0.925 with **15-26 genuine switches per cell** on
4 of 5 seeds, across a clean monotone dose-response. Crucially this does **not** depend on the
post-hoc r -- the register also alternates at R_STAR = 2.25 (seed 43: 26 switches; seed 45: 10;
seed 46: 15). The V3-EXQ-934 autopsy already recommended `supports` for SD-032a on narrower
grounds (one seed, at the argmax crossing); 935 extends that to 4/5 seeds under a common rule.

**Recommend `weakens` -> `supports`** (narrow, diagnostic; SD-032a is excluded from confidence
scoring as a diagnostic result).

## 4. Biological-reference triage

**Closest reference mechanism:** gain control in cortico-basal-ganglia salience arbitration.
MECH-266's own hysteresis content is well-grounded -- six entries in
`targeted_review_connectome_mech_266` (Fallon 2016, O'Reilly 2006, Cools 2019, Cools & D'Esposito
2011, Cools 2008, Collins & Frank 2014 OPAL). That lit is **present** and is not what this run
tested.

**The divergence is one level down, in the gain stage.** `SalienceCoordinator.tick()`
(`ree_core/cingulate/salience_coordinator.py:455-467`) applies a **hard clip**:

```python
if affinity_cap is not None:
    value = max(-affinity_cap, min(affinity_cap, value))
```

per input signal, before its per-mode weight, while `external_task_bias` is added to the
`external_task` logit **unclamped**. So the cap sets a ratio between a clipped signal
contribution and an unclipped bias -- a ratio that is only meaningful relative to how large that
agent's signal happens to be.

Biological gain control in this role is **divisive normalisation** (Carandini & Heeger's canonical
normalisation computation; in BG, via lateral inhibition / FSI-mediated pooling), which is
**scale-free by construction**. Hard clipping is a formal engineering device, not a biological
translation, and it is *scale-sensitive by construction*.

**This is load-bearing, not a caveat.** Every difficulty this run encountered is the predictable
consequence of that substitution: the bimodal `baseline_margin` distribution, the per-agent
saturation, the need for a free per-agent constant at all, and the fact that a *ratio* rule
under-corrects (a clip does not divide, so dividing the threshold cannot fully undo it). A
normalising gain stage would remove the free parameter entirely -- there would be no r to
pre-register. **No lit entry exists for the normalisation question.** -> `/lit-pull` commission.

**Missing-dependency signature check:** the failure does *not* resemble a missing biological
dependency. All readiness anchors cleared and the manipulation produced a clean dose-response. It
resembles a correctly-working mechanism read through a mis-centred constant.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** (both) | MECH-266's Schmitt trigger never instantiated (no asymmetric arm); SD-032a's register performed as specified and better than at any prior point in the lineage. |
| Biological reference | **partial** -- divergence found, load-bearing | Hard clipping where biology uses divisive normalisation. MECH-266 hysteresis lit present (6 entries); normalisation lit **absent**. |
| Prerequisites | **present** | 5/5 on contact, margin engagement, calibration statistic, r_star cell, manipulation landed. |
| Implementation completeness | **partial** | The cap is implemented and functional (clean monotone dose-response). MECH-266's `exit_threshold` asymmetry is not implemented. The clamp is clipping, not normalisation. |
| Environment adequacy | **adequate** | Curriculum produced foraging competence and an engaged external_task drive on 5/5 seeds. |
| Measurement adequacy | **under-instrumented / misleading** -- DOMINANT | Four defects, section 5a. |
| Integration adequacy | **coupled but unstable** | seed->margin basin assignment did not reproduce across a 3-commit substrate move (section 5b). |
| Scale / capacity | **adequate, sweep truncated at the top** | Graded window's lower edge is r ~ 2.45; the top of the sweep (2.65) still grades 4/5, so the upper edge is **unmeasured**. Seed 42 needs r > 2.65, untested. |

### 5a. The measurement defects (dominant layer)

1. **The aliasing control was computed but excluded from the routing.** The driver's own docstring
   states H-KNIFE ("the rule is right but the r is slightly wrong") is *"distinguished from H-IDIO
   by the r-sweep below -- WITHOUT the sweep, 'C1 failed' would alias 'wrong rule' with 'right
   rule, slightly wrong r'."* The sweep was run and recorded. The routing then never reads it:
   `some_r_frac` is `graded_at_some_r_fraction_INFO_ONLY` and there is **no H-KNIFE branch** --
   H-IDIO is a bare `else` fall-through. The instrument built to prevent exactly this misreading
   was not wired to the verdict.
2. **`route_reason` is factually false.** It asserts
   `no_common_normalised_rule_outperformed_the_best_absolute_cap`, but
   `c3_beats_best_absolute_cap: true` -- the normalised rule graded 2 seeds against the absolute
   cap's 0. The string is hardcoded on a branch that assumed C3 was the failing criterion; C1 was.
   (Directly parallel to the false `external_task_mode_not_occupied` reason recorded against this
   same lineage on 2026-08-13.)
3. **`R_STAR` was imported from a basis that did not reproduce.** See 5b.
4. **The reachability exemption claims a substrate identity the manifest refutes.**
   `ANCHOR_REACHABILITY_EXEMPT` states every threshold "was cleared by V3-EXQ-934 **on this exact
   substrate**". 934 ran at `6f46a703` (`substrate_hash f53db12d...`); 935 at `d85ac805`
   (`substrate_hash 921d0af6...`) -- three `ree_core` commits apart (MECH-091 phase_reset
   triggers, MECH-357 credit-eligibility windowing, preservation auto-fire), touching `agent.py`,
   `infralimbic_avoidance_gate.py`, `config.py`.

**Note the INFO_ONLY marking was a defensible design choice, and this is not a reversal of it.**
Scoring each seed's *own* best r would reproduce the per-seed best-point weakness 935 exists to
correct. The defect is narrower: a *single common* r drawn from the pre-registered sweep is not a
per-seed best point, and the routing had no branch for it. The fix is a new branch, not a change
to what C1 scores.

### 5b. The reproducibility finding

`baseline_margin` per seed, 934 vs 935 (both measured in-run at `cap = 0.75`):

| seed | V3-EXQ-934 | V3-EXQ-935 | change |
|---|---|---|---|
| 42 | 0.3373 | 0.8139 | **x2.41** |
| 43 | 0.7681 | 0.3217 | **x0.42** |
| 44 | 0.7850 | 0.7851 | identical to 4 dp |

Seeds 42 and 43 essentially **exchanged** values while seed 44 reproduced bit-stably. That is not
noise -- noise perturbs all three. The margin distribution is **bimodal in both runs** (a ~0.32-0.36
cluster and a ~0.78-0.81 cluster), and it is the *seed -> basin assignment* that failed to
reproduce across the substrate move.

**Scope of the damage, stated precisely.** 935 measures each seed's `baseline_margin`
**in-run** (`ARM_CALIB`), so the normalisation itself is internally self-consistent and the sweep
is valid. What the non-reproduction invalidates is narrower but decisive: **the imported value of
R_STAR**. 934's three banked r values are just its two graded caps divided by margins that
happened to cluster -- 0.75/0.3373 = 2.224, 1.75/0.7681 = 2.278, 1.75/0.7850 = 2.229. The
apparently "narrow r band 2.22-2.28" is largely an artefact of a coarse 5-point absolute cap grid
(0.75...1.75) intersected with a bimodal margin distribution, in which graded cells were only ever
found at the two **ends** of the grid. 935's own five-seed sweep puts the graded window's lower
edge at r ~ 2.45 -- above the entire banked band.

### 5c. Failure-location summary (GOV-FAILLOC-1)

| Bucket | Reads from | Verdict |
|---|---|---|
| MECHANISM FAILED | Implementation completeness | **not established** -- `partial` (MECH-266's asymmetry unimplemented; clip not normalisation) |
| MEASURES FAILED | Measurement adequacy | **ESTABLISHED** -- four defects, 5a |
| ENVIRONMENT FAILED | Environment adequacy | **not established** -- `adequate`, 5/5 anchors |
| REE FAILED | all three | **false** |

**Net classification: MEASURES -- single bucket. Not chargeable to REE, and not to the mechanism.**
The observation classified is "no common normalised cap rule exists". That observation is itself
refuted by the run's own sweep, so the bucket assignment is doubly conservative.

## 6. Re-derive brake (MOVE-3)

Counted under R1-R3 (unit = run; latest adjudication supersedes; `substrate_ceiling` only):

- **MECH-266: 6** ceiling hits -- 464b, 467b (2026-06-04), 464c, 467c (2026-06-12),
  464d, 467d (grandfathered batch, 2026-08-08).
- **SD-032a: 6** -- identical set (co-tagged throughout).

Not counted: `v3_exq_797` (`substrate_conditional`), 464e / 467e (`standard`, 2026-08-13),
934 (`standard`, 2026-08-16).

**The brake does NOT fire on this autopsy.** Its trigger is "when *this* autopsy makes that the
Nth **`substrate_ceiling`** reading". This autopsy's reading is a **measurement / test-design
defect**, not a ceiling, so under R3 it adds **0** and the historical count of 6 is unchanged. The
last three adjudications in this lineage (464e, 467e, 934) likewise read `standard` -- the
2026-08-13 autopsy states plainly that "the substrate ADVANCED, it did not ceiling."

**This matters and is not bookkeeping.** The brake, when it fires, *refuses a same-claim
re-queue*. The correct routing here **is** a same-question re-queue with a corrected constant, and
the run's own data already shows the target clearing. Firing the brake on a count that this
reading does not contribute to would block the cheapest available step in favour of speculative
substrate work.

**V3-EXQ-935 did not violate the brake that fired at 934.** 935 was queued at 2026-08-16T12:59Z
(`ree-v3 cbe407e`) and started ~13:01Z; the 934 autopsy was generated at **18:26:35Z**, 5.5 hours
later. 935 was already running when the refusal landed. Recorded so no later reader mistakes the
sequence for a discipline failure. (Independently, the 935 driver reached the same critique of
934's `winning_cap_band` on its own, before that autopsy existed.)

## 7. Granularity-debt recurrence trigger: **DOES NOT FIRE**

`granularity_debt_cluster.py MECH-266` -> **10 targets across 6 files** (same for SD-032a; the two
are co-tagged on every one).

`claim_alignment` distribution: **intact 3, weakened 2, unclear 2, unstamped 1** (+2 rows the
reader truncates). The two `weakened` targets are 464d and 467d, both annotated *"weakened (6th
consecutive non-engagement)"*.

The trigger requires **at least one `weakened` AND structurally differing signatures**. The first
holds; **the second does not**. Every target in this cluster carries the *same* signature -- the
MECH-266 mechanism is never exercised because the arbitration is mis-calibrated (unreachable in
464b-d/467b-d, saturated in 464e/467e, and now mis-centred in 934/935). Six repetitions of one
signature is **measurement and calibration debt, not granularity debt**; the claim is not several
claims, it is one claim that has never yet been reached. Routing to `/claim-synthesis` would
decompose a claim whose decomposition is not the problem.

## 8. Learning extracted

1. **An aliasing control that is not wired into the routing does not control aliasing.** The
   driver identified the H-IDIO/H-KNIFE aliasing hazard, built the exact instrument to resolve it,
   recorded the readout -- and then routed through an `else` that never reads it. Recording an
   instrument is not consulting it. Any pre-registered aliasing control should have a *named
   branch* in the routing, not an INFO_ONLY field.
2. **A hardcoded `route_reason` on a fall-through branch will eventually be false.** This is the
   second false `route_reason` in this lineage in five days (2026-08-13:
   `external_task_mode_not_occupied` emitted while the mode was 100% occupied). Reasons should be
   derived from which criterion actually failed.
3. **A constant imported from a prior run inherits that run's reproducibility, not just its
   arithmetic.** R_STAR's derivation was sound arithmetic on a seed->margin mapping that did not
   survive a 3-commit substrate move. A pre-registered constant carried across a substrate change
   needs its basis re-verified against `substrate_hash`, not asserted.
4. **A "narrow band" observed on a coarse grid may be an artefact of the grid.** 934's r band
   2.22-2.28 came from two cap values at the *ends* of a 5-point grid; 935's finer sweep put the
   real window entirely above it.
5. **Scale-normalisation retrofitted onto a hard clip is fighting the gain stage.** The biological
   mechanism (divisive normalisation) is scale-free by construction and needs no per-agent
   constant. Every calibration difficulty in this lineage is downstream of substituting a clip for
   a division.
6. **The mixed regime is two-mode, not four.** `internal_replay` and `offline_consolidation` were
   0 in all 35 cells. "Graded occupancy regime" in this lineage means external_task vs
   internal_planning only -- a scope limit any successor's claim language must respect.

## 9. Routing (confirmed at the Step 8 gate)

**Primary: `/queue-experiment` -- same-question re-queue, new letter `V3-EXQ-935a`.**

The scientific question is unchanged ("is the recalibration a shippable rule"), so it takes an
alphabetic suffix, not a new number. Required changes:

1. **Pre-register `R_STAR = 2.45`** -- the lower edge of the graded window observed in 935's own
   five-seed sweep. State the derivation openly: it is drawn from 935 and is therefore *in-sample*
   for seeds 42-46, which is precisely why (3) is mandatory.
2. **Extend the sweep upward** -- e.g. {2.25, 2.45, 2.65, 2.85, 3.05} -- so the graded window's
   **upper** edge is measured, and so a seed-42-class agent (which needs r > 2.65) gets a tested r
   rather than falling off the end.
3. **Fresh out-of-sample seeds (e.g. 47-51).** r = 2.45 is in-sample on 42-46; the common-rule
   claim must be re-earned on seeds that did not choose it.
4. **Wire H-KNIFE into the routing.** Add an explicit branch -- fires when C1 fails at R_STAR *and*
   some single common r in the sweep clears `MIN_FRACTION` -- routing
   `rule_right_r_wrong_requeue`. **Never fall through to H-IDIO while the sweep contains a
   clearing r.** H-IDIO should require that *no* swept r clears.
5. **Derive `route_reason` from the failing criterion** instead of hardcoding it per branch.
6. **Re-verify or drop the "this exact substrate" claim** in `ANCHOR_REACHABILITY_EXEMPT`; gate it
   on `substrate_hash` equality rather than prose.
7. **Report the two-mode scope** (`internal_replay` / `offline_consolidation` occupancy) so the
   regime claim is bounded by what was measured.

Note (2) and (3) are also what keeps this re-queue outside the re-derive brake's spirit: it is not
another letter circling the same operating point, it is the first test of a *measured* window on
*unseen* seeds.

**Secondary: `/lit-pull` commission -- `targeted_review_salience_gain_normalisation`.**
Divisive normalisation as the biological gain-control mechanism in cortico-BG salience
arbitration (Carandini & Heeger canonical normalisation; BG lateral-inhibition / FSI pooling),
against the substrate's hard clip. The question to answer: does the biology support replacing
`max(-cap, min(cap, v))` with a normalising stage, which would eliminate the free per-agent
parameter this entire lineage has been trying to calibrate? A substrate proposal should follow the
lit, not precede it -- this is `complex (probe-gated) / puzzle (known rules)`, not
`complicated (buildable)`.

**No substrate_queue write from this autopsy** (`action: none`). The substrate state is unchanged
by this diagnosis; the V3-EXQ-934 autopsy's `implement-substrate` routing already covers the
substrate side, and the defects found here are in an **experiment driver**, not in `ree_core`.

## 10. Draft `evidence_quality_note` text for governance

**MECH-266:**

> [2026-08-18 | V3-EXQ-935 | failure_autopsy_V3-EXQ-935_2026-08-18] PERIPHERAL / not exercised.
> V3-EXQ-935 sweeps a single symmetric `affinity_input_cap` and contains no asymmetric-threshold
> arm, so MECH-266's Schmitt trigger (`exit_threshold` < `enter_threshold`) was never instantiated
> and the claim could not express itself. The run is a calibration step upstream of any MECH-266
> test. `non_contributory` UPHELD; no `substrate_ceiling` attribution accrues and the brake count
> stays at 6. Keep `pending_retest_after_substrate`. -> standard

**SD-032a:**

> [2026-08-18 | V3-EXQ-935 | failure_autopsy_V3-EXQ-935_2026-08-18] Direction CORRECTED
> `weakens` -> `supports` (narrow, diagnostic; excluded from confidence scoring). The driver
> stamped `weakens` from the same `else` branch that emitted a factually false `route_reason`
> ("no common normalised rule outperformed the best absolute cap") while `c3_beats_best_absolute_cap`
> was true. On the data the SD-032a mode register produced graded, non-degenerate occupancy
> (0.124-0.925) with 15-26 genuine switches per cell on 4/5 seeds across a monotone dose-response
> -- its best performance in this lineage -- and alternates at R_STAR = 2.25 as well, so the
> correction does not rest on the post-hoc r. Re-scoring the run's own pre-registered gate at
> r = 2.45 and r = 2.65 (both inside its own sweep) returns PASS on C1, C2 and C3; only the
> imported R_STAR = 2.25 fails. -> standard

## 11. Hypothesis-space ledger (Step 9b)

Question `mech266_mode_arbitration_saturation` (claims MECH-266, SD-032a;
`initial_frozen_count` 3; `growth_restriction`: **none**, so no STOP applies).

- **H2-structural-bang-bang -> `eliminated`** (Mode B resolve). 935 refutes it decisively:
  occupancy takes 12 distinct interior values spanning 0.124-0.925 with 15-26 switches per cell.
  That is not a discrete argmax bang-bang register. Bar: `control_passed` true (ARM_ABS ran and
  gave a clean interpretable 0/5 bimodal result; all five readiness anchors cleared 5/5),
  `non_degenerate` true (`manipulation_landed`, `occupancy_varies_across_r`,
  `margin_varies_across_r` all true), `met_elimination_bar` true, direction = discriminating.
- **H1-cap-miscalibration -> stays `alive`**, basis updated. 935 supports it strongly, but
  confirming it on a post-hoc r drawn from the same sweep would be exactly the best-point
  selection this lineage exists to avoid. Confirmation belongs to V3-EXQ-935a, which
  pre-registers r = 2.45 and tests fresh seeds. Recorded with 935 in `resolving_runs` and
  935a as the adjudicating run.
- **H3-instrument-illposed -> stays `alive`**, basis updated. 935 replaced the corrupting
  min-across-arms gate and still found real graded structure, so instrument ill-posedness is not
  the whole story -- but 935 exhibits a *new* instrument defect of the same family (the aliasing
  control excluded from routing), so the family is not eliminated.
- **H4-clip-not-normalisation -> NEW leg, pre-registered `alive`** (Mode A + labelled
  FANOUT-GROWTH, invariant 3a). "The arbitration's scale-sensitivity is a consequence of hard
  clipping rather than divisive normalisation; a normalising gain stage removes the free parameter
  entirely." Axis: `constitution`. Its adjudicating run does not exist yet, so 3a(a) is satisfied
  trivially; `pre_registration_source` and a `fanout_growth_events[]` entry are recorded, and
  `initial_frozen_count_at_registration` is preserved at 3 while `initial_frozen_count` moves
  3 -> 4.

  **This is NOT a Mode C discovery**: it cannot be born resolved (it needs a lit-pull and a
  substrate change before anything can adjudicate it), so per the Mode C rule it is pre-registered
  via Mode A for a future run rather than forced through discovery growth with a same-day
  resolution that has not been earned.

**Fan-out growth is a non-convergence signal and is recorded as such.** This question now carries
its third growth event across three autopsies (08-13, 08-16, 08-18). The campaign has not
converged; the denominator is growing while the surviving set is only now taking its first
elimination.

### 11a. Convergence class: **`circling`** -- flag kept, not engineered away

`build_hypothesis_space.py` classifies the H4 growth event as **`circling`**:
*"a growth event added ONLY legs re-entering already-eliminated families"* --
`families_touched: [constitution]`, `families_already_dead: [constitution]`,
`families_fresh: [instrumentation, representation]`. H4's axis `substrate` maps to the same
`constitution` family as the H2 leg this autopsy just eliminated (`intrinsic-architecture`).

**This was foreseen and the flag is deliberately left standing.** `representation` was considered
as an alternative axis and is genuinely arguable -- divisive normalisation is canonically a
*representational* gain-control computation, and it would have placed H4 alongside the still-alive
H1 and produced no flag. It was **not** taken, for three reasons:

1. Re-labelling an axis *after seeing the classifier's verdict, in order to clear it*, is the one
   move that destroys the classifier's value. The discriminator exists to catch campaigns
   re-entering dead territory; a leg that relabels itself out of the warning teaches the next
   reader nothing.
2. The skill offers two responses to a `circling` verdict -- *"prefer a different family, or state
   explicitly why this leg is not the dead one wearing a new name."* The second is taken, in full,
   in H4's `basis`: **H4 presupposes H2's refutation.** H2 claimed graded occupancy is unproducible
   by the discrete register; 935 showed it is producible. H4 concerns the gain stage *upstream* of
   the register and asks why producing it requires a per-agent constant. Refuting H2 is a
   precondition of H4 being interesting at all.
3. At the **campaign** level the flag is arguably just correct. This lineage has spent eight
   experiments across three months (464b/c/d/e, 467b/c/d/e, 797, 934, 935) without once reaching a
   MECH-266 test, and the denominator has now grown three times. A warning on that pattern is
   information, not noise -- and suppressing it here to make one leg look tidy is the leg-level
   version of exactly the re-derive loop MOVE-3 exists to stop.

Read `circling` here as: *the leg is defensible, the campaign is not converging.* The two are
separate readings and both belong in the record.
