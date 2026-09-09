# Failure autopsy -- V3-EXQ-1015 (MECH-465 z_world warmup-budget dispersion sweep, GFLAG-0136 decision probe)

- **Status:** `confirmed` (user gate 2026-09-09T00:55:13Z) -- drafted interactively by session `fa-20260909-batch`
  (DLAPTOP main checkout, `/failure-autopsy` batch with V3-EXQ-822f and V3-EXQ-1014), red-teamed
  cross-model at Step 7c (**CONTESTED**, ten findings, all applied -- Section 9), Step 8 gate held (Section 9).
- **Generated (UTC):** 2026-09-09T00:26:26Z
- **Scope:** single
- **Run:** `v3_exq_1015_mech465_zworld_warmup_budget_dispersion_sweep_20260908T202858Z_v3`
- **Queue id:** V3-EXQ-1015 -- `experiment_purpose: diagnostic`, priority 70, campaign W5-S1 item 3,
  chip `chip-20260905-mech465-warmup-budget-sweep`, GFLAG-0136 user decision 2026-09-05.
  **An OPEN governance flag, GFLAG-0238 (2026-09-08T20:58Z), already asks governance to decide on
  this run's result, and an existing proposal EXP-0590 (blocked_substrate) is the conjunct-3
  experiment this autopsy routes to. Both are addressed below.**
- **Claims:** MECH-465 (candidate, `epistemic_category: substrate_ceiling`,
  `pending_retest_after_substrate: true`, depends_on SD-011 + MECH-463).
- **Outcome:** FAIL, `evidence_direction: non_contributory`, self-route
  `p2_below_bar_trend_indeterminate`, `non_degenerate: true`, all 15 cells gate-green (57/57
  readiness preconditions met).
- **Ran:** 2003 s on `ree-cloud-2`, `linux-x86_64-py3.10-torch2.12.0+cpu`, substrate hash
  `f6fc776b61a1...` stable across the run.
- **Dry-run gate:** clean (`check_dry_run_citations.py`: 0 dry / 1 real in family; the driver's
  `--dry-run` relaxations never touch a real run; `dry_run_unreachable_criterion` lint silent).
- **Recording:** flat JSON carries the always-core (`recording_schema` rec/v1, `config`, `seeds`
  [0,1,3], `elapsed_seconds`) and the every-tick rv traces; the run-pack `manifest.json` is thin
  (`metrics.json` is `{values: {}}`; `validate_recording.py` flags the pack).

**Headline.** The run answers the question governance asked -- can a commit-gate boundary regime
be reached by warming z_world? -- with a **narrow yes its own label does not report.** Its
load-bearing bar (`P2_BAR = 0.51`, within-seed IQR(rv)/median) is the 785a **pooled-across-seeds**
figure that MECH-465's `what_would_answer` (revised 2026-09-01) says *must not be used as a per-seed
bar* (the driver's own comment calls it the "785a pooled figure"). Scored against the claim's
registered headroom precondition instead, the commit-rate band clause -- every urgency level in
[0.05, 0.95] -- holds in six of fifteen cells, on seeds 0 and 3, with commit rate rising
monotonically with urgency in five of them. Two things the red team established narrow that
reading: the precondition's urgency-off baseline clause is **not measured** by this design, and no
per-seed dispersion floor derivable from these cells separates seed 1 (5/6 levels at every budget)
from seeds 0 and 3. The substrate-gating premise of the `substrate_ceiling` stamp is gone; the
category itself is **held** this cycle and sequenced behind the amend of EXP-0590.

---

## 1. Facts (no interpretation)

### 1a. Design

Five arms x seeds {0, 1, 3}: `COLD` (no warmup), `WARM200/400/800` (SD-070 `run_zworld_p0`
encoder warmup, P0a episodes), `PHASED400` (P0a 400 then P0b 100 episodes of SD-056 e2
forward-model contrastive warmup). Per cell: a 360-tick never-commit calibration pass sets
`thr = cal_median / (1 + U_MID)` with `U_MID = 0.19`, so the six urgency levels
`[0.04 .. 0.34]` place effective thresholds at 0.874x .. 1.126x of the free-running rv median
(post-`2023589` sign: threshold *ascends* with urgency; grid span 1.288x). Then a 1200-tick scored
pass with exogenous urgency drawn i.i.d. per tick from the grid; **no urgency-off arm**. DV =
IQR/median of the every-tick rv trace over the fixed 1110-tick window, moving-block bootstrap CI.

Criteria (`combination_rule`: outcome = PASS iff C1):

| Criterion | Load-bearing | Result | Number |
|---|---|---|---|
| C1 P2 clears at some budget: max sweep DV >= 0.51 on >= 2/3 seeds | yes | **FAIL** | 0/3; max 0.2662 (WARM200/s3) |
| C2 plateau below bar: pooled ln-gain/doubling CI95 upper < ln 1.15 | label only | false | 0.1168, CI [0.0375, 0.1828] vs 0.1398 |
| C2b climbing: CI lower > 0 AND point >= ln 1.15 | label only | false (pooled) | per seed: s0 0.207 [0.084, 0.299], s1 0.211 [0.060, 0.384] CLIMB; s3 -0.068 [-0.188, 0.044] |
| C3 PHASED lever: |ln(PHASED400/WARM400)| >= ln 1.25 with CI excluding 0 | recorded | pass | 2/3 (s0 x2.52 [0.565, 1.167]; s1 x1.43 [0.007, 0.880]; s3 x0.81) |
| C4 P1 readable: all six levels' commit rate in [0.05, 0.95] | recorded | pass | 6/15 cells |

### 1b. Per-cell results (DV = within-seed IQR(rv)/median; commit rate by urgency level u = .04/.10/.16/.22/.28/.34; n per level 25-65)

| arm | seed | DV | CI95 | commit rate by level | levels in band | monotone | gate-margin median |
|---|---|---|---|---|---|---|---|
| COLD | 0 | 0.0099 | [0.0079, 0.0127] | 0.00/0.00/0.00/0.89/1.00/0.88 | 2 | no | 1.012 |
| COLD | 1 | 0.0185 | [0.0139, 0.0238] | 0.00/0.00/0.03/0.88/0.94/0.88 | 3 | no | 1.011 |
| COLD | 3 | 0.0425 | [0.0316, 0.0616] | 0.00/0.00/0.21/0.74/0.90/0.83 | 4 | no | 1.015 |
| WARM200 | 0 | 0.0668 | [0.0583, 0.0787] | 0.00/0.00/0.15/0.50/0.76/0.89 | 4 | yes | 1.049 |
| WARM200 | 1 | 0.0995 | [0.0713, 0.1231] | 0.00/0.03/0.27/0.53/0.75/0.86 | 4 | yes | 1.032 |
| WARM200 | 3 | **0.2662** | [0.2235, 0.3229] | 0.19/0.28/0.50/0.47/0.45/0.71 | **6** | **no** | 1.031 |
| WARM400 | 0 | 0.0783 | [0.0653, 0.0975] | 0.00/0.10/0.37/0.57/0.76/0.92 | 5 | yes | 1.004 |
| WARM400 | 1 | 0.1250 | [0.0879, 0.1604] | 0.03/0.18/0.29/0.40/0.58/0.81 | 5 | yes | 1.033 |
| WARM400 | 3 | 0.1890 | [0.1542, 0.2392] | 0.39/0.65/0.79/0.84/0.89/0.95 | **6** | yes | 0.876 |
| WARM800 | 0 | 0.1011 | [0.0856, 0.1162] | 0.13/0.38/0.59/0.77/0.86/0.93 | **6** | yes | 0.973 |
| WARM800 | 1 | 0.1518 | [0.1170, 0.1811] | 0.03/0.23/0.31/0.50/0.71/0.68 | 5 | no | 1.045 |
| WARM800 | 3 | 0.2326 | [0.1936, 0.2777] | 0.16/0.38/0.52/0.56/0.67/0.76 | **6** | yes | 0.992 |
| PHASED400 | 0 | 0.1976 | [0.1459, 0.2407] | 0.40/0.62/0.70/0.81/0.87/0.91 | **6** | yes | 0.892 |
| PHASED400 | 1 | 0.1790 | [0.1349, 0.2442] | 0.03/0.18/0.30/0.70/0.72/0.73 | 5 | yes | 1.014 |
| PHASED400 | 3 | 0.1524 | [0.1207, 0.1919] | 0.23/0.39/0.58/0.69/0.76/0.84 | **6** | yes | 0.948 |

`gate_margin_frac_in_band` is 1.000 in 14/15 cells and 0.995 in the fifteenth -- **including the
three COLD point-mass cells** -- because the margin is measured against a threshold calibrated
from the cell's own median (red team F2). Arm means: COLD 0.024, WARM200 0.144, WARM400 0.131,
WARM800 0.162, PHASED400 0.176. `projected_doublings_to_bar` (from WARM800 to 0.51): 10.3, CI95
[6.6, 32.2] = ~77,000 P0a episodes at the optimistic end. Seed 1 misses the band only at
u = 0.04 (~0.03) in every sweep cell; the lower-tail mass P(rv < 0.874 x median) is 0.032 at
WARM800/s0 (passes) vs 0.121 at WARM800/s1 (fails). The one recorded (non-gating) precondition
miss is `cold_reproduces_spike_dispersion_band` on COLD/s0 (machine-class-bound).

### 1c. What the driver itself says

`what_a_null_does_not_mean`: "A plateau below the bar says the gate-rescale ROUTE is exhausted
... it is not evidence against MECH-465's assertion." `routing`: "NEITHER 'route exhausted' NOR
'extend budget' is data-supported ... More power is a fourth seed or a WARM1600 rung." Docstring
lines 88-90: "commit rate is graded across levels only once IQR/median is comparable to the
+/-13% bracket, i.e. as P2 approaches its bar."

---

## 2. Claim layer

MECH-465 (mechanism_hypothesis, candidate): *arousal's effect on WHETHER commitment fires is
expressible only near the commit-gate boundary; in every run to date the gated quantity sits
25-48x below the threshold and commit rate is pinned at 0.99-1.00, so MECH-463's commit-gate
prediction is UNTESTED rather than falsified.*

Its `what_would_answer` (revised 2026-08-26, corrected 2026-09-01) sets a three-conjunct
non-degeneracy precondition, all required:

1. **HEADROOM** -- median gate margin within [0.5, 2.0] on >= 50% of scored fresh-select ticks;
   commit rate at EVERY urgency level within [0.05, 0.95]; **baseline (urgency-off) commit rate
   within [0.2, 0.8]**.
2. **DISPERSION FLOOR** -- IQR(rv)/median(rv) >= a pre-registered floor. Verbatim: "785a's 0.51 is
   the POOLED figure and MUST NOT be used as a per-seed bar ... SCORE IT PER SEED, and set the floor
   from within-seed data. Do NOT simply lower the floor to make it passable -- a regime that
   collapses rv dispersion is exactly what this conjunct exists to catch."
3. the residual-DV experiment (the assertion itself) -- already proposed as **EXP-0590**
   (2026-08-26; `blocked_substrate`; release condition "confirming within-seed IQR/median clears
   MECH-465's pre-registered 0.51 floor").

**Did the run test the claim?** No, and it never claims to. **Did it test the claim's
precondition?** Partly, against the wrong bar: C1 scores conjunct (2) at 0.51 per seed, which the
claim forbids, and the driver, the 2026-09-04 spike, the substrate entry, GFLAG-0136 and EXP-0590's
release condition all inherit it. Conjunct (1): the commit-rate band clause is met in 6/15 cells
(seeds 0 and 3); the gate-margin clause is met in 15/15 by construction; the urgency-off baseline
clause is unmeasured. `claim_ids` accuracy: correct, single tag.

Stored-category check: `substrate_ceiling` was stamped 2026-09-01 on the stated basis
"reachability OPEN and measured NEGATIVE ... blocker `sd_zworld_warmup_optimizer_group` SHARED with
MECH-457 / INV-088 / Q-002". That blocker has been validated since 2026-07-22 and this run used it.

---

## 3. Biological-reference triage

Closest mechanism: LC-NE adaptive gain on a decision threshold (Aston-Jones & Cohen 2005;
jepma2010 -- both in `targeted_review_connectome_mech_463`; no `/lit-pull` owed). The commit gate
is a formal import of a precision threshold. The load-bearing divergence is on the **threshold's
reference frame**: biological gain control sets a threshold relative to the running statistics of
its input; REE's is a fixed absolute constant (`from_dims` default 0.4 against a free-running rv
median of 0.003-0.038, 10-120x apart). Every "25-68x below the gate" figure in the MECH-463/465
lineage is a measurement of that constant. The driver's per-cell recalibration is the biological
move, and the post-construction override reaches the same gate the organism uses
(`e3_selector.py:822` returns `config.commitment_threshold` unchanged). It is *necessary but not
sufficient*: recalibrated COLD gives 2/6, 3/6, 4/6 levels in band (seeds 0, 1, 3), never 6/6,
because an untrained z_world gives a point-mass rv. Warm the encoder and the same gate is graded.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | Assertion untested by design; two of three conjunct-(1) clauses reached in 6/15 cells (2/3 seeds); third clause unmeasured. |
| Biological reference | **clear** | LC-NE adaptive gain; divergence = fixed absolute threshold; load-bearing for substrate design. |
| Prerequisites | **present** | SD-070 warmup engaged in every WARM/PHASED cell; SD-056 P0b >= 200 steps in PHASED400. |
| Implementation | **complete** | Gate, urgency modulation (post-2023589 sign), warmup recipes all ran; urgency fidelity <= 1e-6. |
| Environment | **adequate** | The manipulation moved the DV 3-6x on 3/3 seeds. |
| Measurement | **misleading** | (i) Load-bearing bar is the forbidden pooled 0.51 scored per seed. (ii) The driver's arithmetic premise (graded once IQR/median ~ the +/-13% bracket) holds; only its "i.e. 0.51" gloss is wrong. (iii) No per-seed IQR/median floor separates seed 1 from seeds 0/3; lowest-level gradedness tracks the rv lower-tail mass. (iv) Gate-margin clause is uninformative under per-cell recalibration. |
| Integration | **coupled** | Warmup -> e2 prediction error -> rv -> gate move together; P0b is an independent lever (C3 2/3; seed 1's CI lower bound 0.007). |
| Scale | adequate for what the cells answer | Pooled slope 0.117/doubling = seeds 0/1 climbing with confidence + seed 3 declining. |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Verdict |
|---|---|
| MECHANISM FAILED | not established -- Implementation reads complete; the cells reach the band clause |
| MEASURES FAILED | **established** -- the load-bearing bar is the one the claim forbids |
| ENVIRONMENT FAILED | not established |
| REE FAILED | **false** |

**Net: MEASURES, single bucket, not chargeable to REE.**

### Recommended `epistemic_category`

**HOLD `substrate_ceiling` this cycle; flip to `standard` when EXP-0590 is amended and the
conjunct-3 experiment is queued** (same disposition, sequenced). `pending_retest_after_substrate:
true -> false` now, because no substrate build gates the experiment. The direction of the eventual
move is defensible on the repo's own discriminator (the substrate is not too coarse; the shared
blocker is validated; the band clause is reachable per seed), but the premise is narrower than
"headroom regime reached" -- two of three clauses, on two of three seeds, with the per-seed floor
unregistered -- and the 2026-08-26 move to `standard` was reversed on 2026-09-01 for exactly the
shape "reachability CLOSED on over-read data" (red team F10). **Alternative for the gate:** move to
`standard` now on the discriminator alone (the original draft recommendation).

---

## 5. Learning extracted

1. **A rule registered in one claim field does not propagate.** The 2026-09-01 correction (0.51 is
   pooled; score per seed from within-seed data; do not lower the floor either) was followed by
   the 2026-09-04 spike, GFLAG-0136 and this driver all scoring 0.51 per seed (the 2026-08-27
   probe pre-dates it). The "2.7-5.8x shortfall" (0.51/0.190, 0.51/0.088) is distance to a bar the
   claim forbids.
2. **The driver's arithmetic premise is right and its gloss is wrong**: graded commit response
   appears once within-seed IQR/median is comparable to the +/-13% bracket (0.10-0.27 in the six
   band cells), not "as P2 approaches 0.51". But no IQR/median floor from these cells separates
   seeds (seed 1: 5/6 at 0.125-0.179; seed 0: 6/6 at 0.101); the lowest level tracks the lower-tail
   mass (0.032 vs 0.121). The per-seed floor must be REGISTERED, not chosen from passing cells,
   and may need to be a tail statistic.
3. **Only the commit-rate band clause carries information in this design**: the gate-margin clause
   passes 15/15 by construction under per-cell recalibration; the urgency-off baseline is unmeasured.
4. **The budget lever is climbing with confidence on seeds 0 and 1 and declining on seed 3**; the
   pooled indeterminate label averages two climbs and a decline. Against 0.51 the climb is
   impractical (5.7-7.8 doublings on the climbing seeds; ~77,000 P0a episodes at the pooled CI's
   optimistic end); against any defensible per-seed floor the question is moot.
5. **P0b e2-contrastive warmup is an independent lever** (C3 2/3 with CI; seed 1 fragile at a CI
   lower bound of 0.007). Read with the disclosed residue asymmetry of PHASED400.
6. **Recalibration is necessary but not sufficient**: recalibrated COLD reaches 2/6, 3/6, 4/6.
7. **Biology divergence, load-bearing for substrate**: fixed absolute commit threshold vs adaptive
   gain; the substrate entry's "1.455x urgency bar" is on the pre-2023589 sign (span now 1.288x).
8. **Coordination**: OPEN GFLAG-0238 and existing EXP-0590 already own this decision and this
   experiment; a "new EXQ" routed without naming them would create a second owner and leave a
   proposal whose release condition can never be met.
9. **Recording hygiene**: pack thin; the index reads the pack.

### Granularity-debt recurrence trigger: DOES NOT FIRE

`granularity_debt_cluster.py MECH-465`: 0 tagging targets across 0 files.

### Re-derive brake (R1-R3 recount)

MECH-465 prior counted hits: **0**. This target retains `substrate_ceiling` (held for sequencing,
not a new ceiling reading) and therefore **counts under clause 1 of the recipe: hits become 1**,
below the threshold of 2. The eventual flip to `standard` is a claims.yaml write, not a
re-adjudication, so governance should note the count will not self-decrement.
**Refused:** a WARM1600 rung / fourth seed (GFLAG-0238 option 1). **Licensed:** conjunct 3 via an
amended EXP-0590.

---

## 6. Repair pathway and routing (confirmed at the gate)

**Node classification:** `complex (probe-gated) / mystery (known data)` for the label -- the data
to decide GFLAG-0238 are in this manifest; the frame (0.51 per seed) is wrong; no further rungs.
`complex (probe-gated) / puzzle (known rules)` for one missing fact before conjunct 3 can be
pre-registered honestly: a per-seed conjunct-(2) floor statistic that separates the six band cells
from the nine non-band cells across all three seeds -- settleable OFFLINE from this run's recorded
rv traces, no new compute.

**Routing: `queue-experiment`, through EXP-0590.**

1. `/governance` -- **resolve GFLAG-0238 with a third option**: neither "extend the sweep" nor
   "accept indeterminate and gate EXP-0590 on 0.51"; the bar is invalid per seed, the band clause
   is reachable on 2/3 seeds, re-frame and run conjunct 3.
2. `/governance` -- **amend EXP-0590** (do not mint a new proposal): replace the release
   condition's 0.51 clause with per-seed conjunct-(1) readiness INCLUDING an urgency-off baseline
   arm, plus a per-seed conjunct-(2) floor registered from an offline re-analysis of V3-EXQ-1015's
   rv traces (if no IQR/median value separates the seeds, register a lower-tail statistic and say
   why); keep P3 (the residual DV) mandatory; `blocked_by: []`, status gated on that re-analysis;
   design against WARM800 / PHASED400 warmup with per-cell recalibration as here.
3. `/queue-experiment` against the amended EXP-0590 -- NEW EXQ number, `claim_ids: [MECH-465]`,
   seeds 0 and 3 plus new seeds screened per seed by conjunct (1).
4. `/governance` -- substrate amend: append the 1015 failure record to
   `MECH465-COMMIT-GATE-HEADROOM`; **annotate, do not supersede**, the `route_retired_2026-09-04`
   item (its outcome -- no static gate-rescale build -- stands; its basis is partly stale:
   untrained z_world, pre-2023589 1.455x); rewrite the status string; leave `ready: false`; correct
   "2.7-5.8x" wherever cited; update the WWA's stale "max 0.085" sentence. Category held; flip
   when step 3 lands; `pending_retest_after_substrate -> false` now.
5. Optional substrate decision (not owed): an adaptive, running-median-relative commit threshold
   in `ree_core`; `complicated (buildable)` if elected.

**Explicitly not recommended:** WARM1600 / fourth seed; accepting the indeterminate label and
gating EXP-0590 on 0.51; closing the route as exhausted on 0.51; minting the retired static
gate-rescale build; choosing the per-seed floor from the cells that pass; `/implement-substrate`;
`/lit-pull`; governance demotion.

### Draft `evidence_quality_note` for MECH-465

Verbatim in the JSON artifact (`recommended_evidence_quality_note`).

### Per-claim recommendation

MECH-465: `non_contributory`; `epistemic_category` held at `substrate_ceiling` (flip sequenced);
`pending_retest_after_substrate: true -> false` (the `change` tail); `diagnostic_evidence_adjudicated:
true`; status stays candidate.

---

## 7. Hypothesis-space ledger (Step 9b, applied after the gate)

Mode B on a **new question** `mech465_commit_gate_headroom_reachability` (claims [MECH-465]),
`pre_registered_utc` = the run's own date, three legs: H-warmup-plus-recalibration-reaches-band
(**confirmed**, scoped to the band clause; negative control = recalibrated COLD, never 6/6;
non_degenerate true), H-budget-alone-reaches-0.51 (**alive**; per-seed climbs on 0/1, decline on
3; ill-posed on a forbidden bar, kept alive for want of an adjudicated direction),
H-p0b-recipe-independent-lever (**confirmed**; C3 2/3 with CI). No existing question lists
MECH-465.

## 8. Mechanical checks

- Dry-run gate: clean. `validate_recording.py`: pack thin. Lint: silent.
- Step 7b `autopsy_pre_routing_checks.py`: **0 fires** on the draft and on the revised pair.
- Step 7c: Section 9.

## 9. Step 7c red team and Step 8 gate

**Step 7c -- cross-model, read-only. Model Fable 5.1 (`claude-fable-5-1`). Verdict: CONTESTED.**
Findings file `redteam_1015.md` (session scratchpad). It reproduced the DV in all 15 cells, the
projection and the per-seed slopes exactly, and confirmed the 0.51-is-pooled reading verbatim
(H1-H7 held). Ten findings moved assertions or recommendations; all applied:

| # | Finding | Disposition |
|---|---|---|
| F1 | conjunct (1) has a third clause (urgency-off baseline) that no cell measures | **APPLIED** -- "2 of 3 clauses met"; OFF arm required in the successor |
| F2 | gate-margin clause is pinned by the per-cell recalibration (15/15 incl. COLD) | **APPLIED** -- dropped as evidence; only the band clause carries information |
| F3 | "monotone in all six cells" false for WARM200/s3 | **APPLIED** -- 5 of 6 |
| F4 | recommended 0.10 floor refuted by three seed-1 cells and is the "lower the floor" move the WWA forbids | **APPLIED** -- floor withdrawn; register from an offline re-analysis; tail-mass observation recorded |
| F5 | "exhausted" rests on the invalid bar; seeds 0/1 climb with confidence; 12,800 -> ~77,000 | **APPLIED** -- reworded; arithmetic corrected |
| F6 | "COLD bang-bang on every seed" -- COLD/s3 is 4/6 | **APPLIED** |
| F7 | the driver's arithmetic premise holds; only the "i.e. 0.51" gloss is wrong | **APPLIED** |
| F8 | OPEN GFLAG-0238 and EXP-0590 own this decision/experiment and were unreferenced | **APPLIED** -- routing now resolves 0238 (third option) and amends EXP-0590 |
| F9 | superseding the route_retired item contradicts explicitly_not_recommended and re-arms IGW | **APPLIED** -- annotate, do not supersede; 1.455x sign note added |
| F10 | category move argued from F1's over-read premise; repeats the reversed 2026-08-26 shape | **APPLIED** -- category HELD this cycle, flip sequenced; move-now retained as the gate alternative |

Hygiene M1-M7 applied (margin range 0.876-1.031; min n 27; 77,000; WWA "max 0.085" stale; ledger
leg wording).

**Step 8 gate -- user decision, binding (2026-09-09T00:55:13Z):**

> Hold substrate_ceiling, flip when conjunct 3 is queued (Recommended) -- pending_retest_after_substrate -> false now; resolve GFLAG-0238 with the third option; amend EXP-0590; flip to standard when the conjunct-3 EXQ lands.

The routing above is confirmed as drafted; the hypothesis-space ledger moves in Section 7 are applied in this session.
