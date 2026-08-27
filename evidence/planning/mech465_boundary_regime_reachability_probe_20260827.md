# MECH-465 boundary-regime reachability: EXP-0590 DECLINED at the /queue-experiment guardrail

- **Generated:** 2026-08-27T06:02:49Z
- **Session:** `igw-234-proposal-for-mech-465` (IGW-20260827-234, headless `/queue-experiment`)
- **Proposal:** EXP-0590 (`claim_id: MECH-465`), status `proposed` -> `blocked_substrate`
- **Claims touched:** MECH-465 (primary). MECH-463 / SD-011 referenced, not tagged.
- **ree-v3 substrate at probe time:** `8bfcf19` (post-`2023589`, the ascending-gate fix)
- **Outcome:** NOT queued. The design's own pre-registered non-degeneracy gate (P1 HEADROOM,
  P2 DISPERSION FLOOR) is **empirically unreachable** on the current commit gate, measured on
  3/3 seeds in the very boundary regime the proposal was minted to create.

---

## 1. What EXP-0590 asked for

Re-run the V3-EXQ-785a exogenous-urgency design in a **boundary regime** -- set
`agent.e3.config.commitment_threshold ~ 0.0057` post-construction so the commit gate sits
inside the gated quantity's own dispersion -- and score a **residual DV**: observed commit
rate minus the counterfactual built from the OFF-arm empirical running-variance (rv) CDF
evaluated at each level's shifted threshold. Three conjuncts, all required:

- **P1 HEADROOM** -- median gate margin in [0.5, 2.0] on >=50% of scored FRESH-SELECT ticks;
  **commit rate at EVERY urgency level in [0.05, 0.95]**; baseline commit rate in [0.2, 0.8].
- **P2 DISPERSION FLOOR** -- `IQR(rv)/median(rv) >= 0.51` (the pre-registered 785a value).
- **P3 RESIDUAL DV** -- mandatory; the run "is not worth doing without it".

The claim's own `what_would_answer` declares reachability **settled**: *"REACHABILITY
(settled on recorded data, no longer open)"*.

## 2. The reachability analysis is wrong, and the error is a specific one

MECH-465's `what_would_answer` cites this rv distribution:

> p5 0.00259, p25 0.00330, median 0.00562, p75 0.00618, p95 0.00720

Recomputing from 785a's own `*_per_tick.jsonl` (1765 fresh selections, 5 seeds) reproduces
those figures **exactly** -- **as the POOLED-ACROSS-SEEDS distribution**:

| | p5 | p25 | median | p75 | p95 | IQR/median |
|---|---|---|---|---|---|---|
| pooled, 5 seeds | 0.002592 | 0.003299 | 0.005621 | 0.006184 | 0.007209 | **0.5133** |

So the pre-registered P2 floor of 0.51 **is** the pooled figure. But post-warmup
(`tick >= 90`, as the design pre-registers) the **within-seed** distribution is a near
point mass:

| seed | n | median | p5 | p95 | **IQR/median** |
|---|---|---|---|---|---|
| 0 | 324 | 0.006155 | 0.006077 | 0.006263 | **0.0116** |
| 1 | 416 | 0.005614 | 0.005550 | 0.005697 | **0.0104** |
| 2 | 324 | 0.006700 | 0.006101 | 0.007286 | **0.0729** |
| 3 | 323 | 0.003366 | 0.003108 | 0.003792 | **0.0848** |
| 4 | 323 | 0.002608 | 0.002556 | 0.002893 | **0.0193** |

**The pooled 0.51 dispersion is almost entirely BETWEEN-seed.** Within a seed the rv varies
by 1-8% of its median. Pooling five near-degenerate distributions with different locations
produces a smooth-looking CDF whose "dispersion" encodes *seed identity*, not any
within-run quantity.

This matters because urgency sweeps the threshold by a factor of `1.34/1.04 = 1.288` (+29%)
across the pre-registered grid, which is **larger than the entire within-seed rv spread**.
Per seed, the gate is therefore a **step function** of urgency, not a graded one -- and the
residual DV's counterfactual (the empirical CDF at the shifted threshold) predicts exactly
that step. Scored pooled, P1/P2 would appear to pass while measuring between-seed rv
relocation; scored per-seed, they fail.

**This is the same class of defect the 2026-08-26 thought-digestion pass corrected one level
up.** That pass caught the DV being arithmetically determined by *the threshold sliding
against a fixed distribution*, and added P3 to strip it. P3 does strip that. It does not
strip *the distribution being five point masses*.

Feasibility sweep over the recorded post-warmup rv, 4000-point geometric threshold grid,
asking P1's "commit rate in [0.05,0.95] at EVERY level":

| target | feasible thresholds | best achievable |
|---|---|---|
| POOLED (5 seeds) | 1281 / 4000 | 6/6 levels -- **the artefact** |
| seed 0 | **0 / 4000** | 1/6 |
| seed 1 | **0 / 4000** | 1/6 |
| seed 2 | **0 / 4000** | 4/6 |
| seed 3 | **0 / 4000** | 5/6 |
| seed 4 | **0 / 4000** | 3/6 |

Two rescues were tested on the recorded data and both fail as general designs:
**(A) per-seed threshold centred on that seed's own median** -- best is seed 3 at 5/6; level
`u=0.04` reads 0.0 on all five seeds. **(B) narrowing the urgency grid to match the rv
spread** -- the required span differs ~8x across seeds (0.029 for seed 1 vs 0.223 for seed
3), so one pre-registered grid cannot serve them.

## 3. Live probe: the boundary regime does not create the missing dispersion

The recorded-data argument has one honest gap: commit state feeds the latch, so a
boundary-threshold run realises a *different* rv trajectory than the ceiling-regime run the
analysis is built from. The proposal names this itself as the reason to calibrate first.
So it was measured directly.

Scratch probe replicating the 785a harness exactly (`alpha_world=0.9`,
`modulatory_authority_gain=0.5`, exogenous urgency via
`e3.config.urgency_weight = assigned / ||z_harm_a||`, diagnostics cleared before every
`select_action`), 600 ticks/seed, post-warmup `tick >= 90`:

| seed | thr | 785a rv median | **boundary rv median** | shift | **IQR/med** (floor 0.51) | commit rate by level (0.04 .. 0.34) | P1 levels in band |
|---|---|---|---|---|---|---|---|
| 1 | 0.00570 | 0.005614 | 0.005544 | -1.2% | **0.0266** | .904 .937 .944 .964 .965 .982 | 3/6 |
| 3 | 0.00283 | 0.003366 | 0.008918 | **+165%** | **0.0450** | 0 0 0 0 0 0 | **0/6** |
| 0 | 0.00517 | 0.006155 | 0.004002 | **-35%** | **0.0279** | .976 .987 1.0 1.0 1.0 1.0 | **0/6** |

**P2 fails 3/3, by 11-19x.** The boundary regime shifts the rv **location** substantially
(exactly as the proposal predicted) but leaves the **dispersion** a point mass -- and
dispersion is what P2 and P3 need.

**P1 fails 3/3.** No seed puts all six levels in [0.05, 0.95]: one floor-pinned at exactly
0, one ceiling-pinned at 1.0 on four levels, one (seed 1) breaching the 0.95 ceiling on
three levels.

**A third failure the recorded data could not have shown: the calibration target moves
further than the band is wide.** Seed 3 was calibrated at 0.00283 against a recorded median
of 0.003366; under that threshold the realised median became 0.008918 -- 3.15x the
threshold, so commitment never fires at any urgency level. Seed 0 moved -35% the other way.
The induced perturbation (35-165%) is **7-50x the width of the graded band** (2.7-4.5%), so
the proposal's "cheap 3-threshold x 1-seed x 500-tick sweep" is not a calibration procedure
that converges -- there is no demonstrated stable per-seed operating point inside the band.

## 4. Root cause, precisely

`E3TrajectorySelector` gates on `commit_variance = self._running_variance`
(`e3_selector.py:3545-3547`), an EMA at `E3Config.precision_ema_alpha = 0.05`
(~20-tick time constant) over world-model prediction error. In a stationary environment
with a converged world model it settles to a per-seed fixed point. **A converged EMA is
structurally the wrong quantity to place a threshold inside**: it has a location but
effectively no dispersion.

The substrate has two gated quantities that *would* carry genuine within-run dispersion,
and **neither is reachable from the live agent path**:

| alternative | where | why unreachable |
|---|---|---|
| SD-063 `conditional_predictive_variance` (per-input predictive variance from `E2WorldUncertaintyHead`) | `e3_selector.py:2711, 3545-3546` | `select()` kwarg only. **0 occurrences in `agent.py`** -- `_e3_select_kwargs` never sets it, so `use_conditional_precision_gate` silently falls back to the EMA ("byte-identical OFF") |
| `use_harm_variance_commit` + `harm_bridge` (cross-candidate harm-score variance) | `e3_selector.py:2696, 3528` | both `select()` kwargs only. **0 occurrences in `agent.py`** |

The SD-063 gap is the sharp one and is a **doc-vs-runtime discrepancy of exactly the kind
`/queue-experiment` Step 2.5a exists to catch**: `substrate_queue.json` carries SD-063 at
`implementation_status: implemented_validated`, titled *"E2 conditional predictive-uncertainty
head ... **feeding E3 commitment gating**"*. The **head** is built, instantiated
(`agent.py:573-612`) and trained online (`_train_e2_world_uncertainty`, `agent.py:4131`),
and it does feed MECH-314b curiosity. Its **E3-commitment-gating consumer half is not
wired.** That is the half MECH-465 needs.

## 5. Confirmed positives (recorded so they need not be re-derived)

Measured live on all three probes, post-`2023589`:

1. **`commitment_threshold` does NOT land through `REEConfig.from_dims`** -- passed
   explicitly, `agent.e3.config.commitment_threshold` still read **0.40** (the default) in
   3/3 probes. The proposal's post-construction attribute-assignment idiom
   (`v3_exq_018b` / `v3_exq_050b`) is required, and it works. (Instance of
   [memory] `reference-reeconfig-from-dims-silent-kwargs`.)
2. **The ascending gate is live and exact.** `effective_threshold = commitment_threshold *
   (1 + urgency_applied)` reproduces to full precision at all six levels
   (e.g. thr 0.0057 -> 0.005928 .. 0.007638). The proposal is correct that the design must be
   written against the post-fix ascending direction, not 785a's descending table.
3. **The exogenous urgency instrument still lands exactly** post-fix:
   `max |realized - assigned| <= 5.6e-17` across all three probes.

These three are what a successor experiment would otherwise have to re-establish.

## 6. Disposition

- **EXP-0590 -> `blocked_substrate`.** Queuing it would spend cloud compute on a run whose
  most likely outcome is, by its own pre-registration, `substrate_not_ready_requeue` --
  "NOT A VERDICT". The worse outcome is that it is scored **pooled**, passes P1/P2 on
  between-seed variance, and returns a spurious signed verdict on MECH-465.
- **Do NOT resolve this by lowering the P2 floor.** Per `/queue-experiment` Step 3: *"A
  pre-registered value that provably fails a gate is a design-time proof, not a substrate
  fact. NEVER lower the threshold to resolve it -- that converts a detected artifact into a
  citable result."*
- **Release condition:** wire a state-dependent gated quantity into `agent.select_action`'s
  `e3.select()` call -- SD-063's `conditional_predictive_variance` is the natural one and
  its producer is already built, trained and validated. Route: `/implement-substrate` on the
  SD-063 consumer half. Once the gate reads a per-input quantity with real within-run
  dispersion, P1/P2 become reachable and EXP-0590's residual DV becomes meaningful as written.
- **MECH-465 is SHARPENED, not refuted, by this.** The claim says arousal's commit-gate
  effect "is expressible only near the commit-gate boundary". This probe adds: on the
  current EMA gate that boundary is not merely un-visited but **un-occupiable in graded
  form** -- the gated quantity has no dispersion for a threshold to sit inside. That is a
  substantive finding about the gate, and it is why the route is a substrate build rather
  than another lettered experiment.

## 7. Work-graph classification

`complicated (buildable)` -- the SD-063 consumer-half wiring is a named build with no open
question, so the route is `/implement-substrate`, not an experiment. MECH-465's own falsifier
remains `complex (probe-gated)` **behind** that build.

## 8. Reproduction

Probe source is committed alongside this note as
`evidence/planning/mech465_boundary_regime_probe_20260827.py`. It is a **scratch harness, not
an experiment** -- no manifest, no queue entry, not evidence, deliberately not under
`ree-v3/experiments/`. Invocation: `python3 mech465_boundary_regime_probe_20260827.py <threshold>
<seed> <n_ticks>`; the three rows in section 3 are `(0.00570, 1, 600)`, `(0.00283, 3, 600)`,
`(0.00517, 0, 600)`. Recorded-data analysis reads
`evidence/experiments/v3_exq_785a_mech463_arousal_exogenous_urgency_decomp_20260719T133431Z_v3_per_tick.jsonl`.
