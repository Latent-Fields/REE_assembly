# V3-EXQ-1043b -- PRE-REGISTRATION (option E: rank co-primary alongside the declared absolute-difference primary)

Written 2026-09-22T19:49:59Z by session `pensive-feistel-471e3c`, BEFORE the driver was written
and BEFORE anything was queued. Chip `chip-20260922-exq1043b-prereg-rank-coprimary`.

**Authority.** User decision OPTION E on `chip-20260920-exq1043b-readiness-gate-formula`, answered
2026-09-22 in orchestrator session `orchestrate-20260922-0722`. Upstream: the CONFIRMED autopsy
`failure_autopsy_V3-EXQ-1043a_2026-09-20.json` (`routing_detail.successor`), ratified by
`/governance` cycle governance-20260920.

**Why this document exists, stated plainly.** The 1043 lineage has been autopsied twice, and the
second autopsy's own red-team record shows the failure mode is *re-anchoring a threshold after
seeing the numbers that fail it*. Option E adds a statistic that was computed during a probe
before it was adopted as a readout. The ONLY thing distinguishing that from option C -- the
re-anchoring move the lineage was refused for -- is that every choice below is fixed in advance,
in writing, on origin, before the run is queued. If any of it slips, option E is option C wearing
a better argument. That sentence is the user's, from the decision chip, and it is reproduced here
because it is the standard this document is to be held to.

---

## 0. The one-line design

Keep option A's non-degeneracy **GATE**; add a pre-registered **RANK CO-PRIMARY**; retain the
original absolute-difference CI as the **DECLARED PRIMARY**, reported whatever it says.

---

## 1. The pre-registration defence (read this before section 2)

The charge option E must answer is that the rank statistic was chosen after seeing that the
absolute-difference statistic would disappoint. Three facts, in descending order of strength:

**(a) The rank statistic is the falsifier the hypothesis registry ALREADY registered, on
2026-09-17, three days before the smoke ran.** `hypothesis_space_registry.v1.json`, qid
`mech537_communication_subspace_orientation`, hypothesis **H2-no-orientation**:

> *label*: "the fitted communication subspace is not meaningfully different from **a random
> subspace of the same rank** at this interface; C2's positivity is noise and will not survive a
> permutation null."
> *Declared null*: "**the observed C2 sits inside the** [reference] **null**."

The per-seed percentile of `D_comm` within a B-draw random-rank-r reference distribution IS
"where the observed value sits inside the distribution of random same-rank subspaces". It is not
a new statistic. What 1043a built instead -- a refit permutation null on shuffled sender/receiver
pairing -- answers a *different* question (is the fitted map real? yes, p = 1.0 on 6/6), and the
1043a autopsy says so in those words. So the rank co-primary is the registered falsifier for H2
being instrumented correctly for the first time, not a statistic introduced to rescue a result.

**(b) The mechanism argument is stated in advance and is independent of the direction of the
answer.** The declared primary is a cross-seed t-CI on an ABSOLUTE difference, and what binds it
is the cross-seed sd (0.0377), i.e. between-seed heterogeneity -- not draw noise. Draw-averaging
cannot touch that, which is why the CI's upper bound first clears 0.05 near n ~ 75 seeds. The
heterogeneity is measurable and large: `rr_mean` ranges 0.5318-0.6205 across seeds, a spread of
0.0887, ~2.4x the C2 cross-seed sd. A percentile is scale-free and calibrated inside each seed,
so that baseline-level variation divides out **by construction**. This argument predicts that the
rank statistic is better *whatever it returns*, including a null.

**(c) The known hazard is named, not hidden.** The competence inclusion criterion in section 5
excludes a seed (45) that was already seen to fail it. That is acknowledged as the weakest point
of the design, and it is why section 5 requires the result to be reported BOTH ways, with neither
form permitted to stand alone.

---

## 2. (i) THE DECLARED PRIMARY -- unchanged, and reported whatever it says

**This is not demoted, not conditional, and not omitted if it disappoints.**

- **Statistic.** `C2_denoised[s] = mean_B(D_randrank[s]) - mean_K(D_comm[s])` per seed `s`, read at
  that seed's parsimonious rank `r_pars` (the smallest rank whose grouped-CV held-out R2 is within
  `PARSIMONIOUS_R2_TOL = 1e-3` of the ladder maximum -- a within-run, cross-validated rule,
  unchanged from 1043a).
- **Test.** 95% two-sided t-CI (df = n_seeds - 1) on the cross-seed mean of `C2_denoised`.
- **Declared null, verbatim from the registry (H1-small-but-real).** "the CI **excludes 0.05**
  (H1 falsified, not rescued)."
- **Also recorded, for direct lineage comparability with 1043a's landed [0.0051, 0.0948]:**
  `C2_single[s] = D_randrank[s][draw 0] - D_comm[s][refit 0]`, i.e. 1043a's exact single-draw,
  single-fit protocol, with the same CI. Draw 0 and refit 0 are fixed by index in advance; their
  RNG seeds are recorded.

**Pre-registered EXPECTATION, written down now so that its occurrence cannot later be used as an
argument for switching statistics.** Substituting the B=24 draw-mean comparator into this exact
statistic gave `[+0.0013, +0.0804]` (smoke, Result 4), against 1043a's landed `[+0.0051, +0.0948]`.
Both exclude 0 and include 0.05. **We therefore EXPECT the declared primary to return "positive,
small, below the floor, H1 still alive" -- i.e. undecided -- at n = 6.** That expected outcome is
a property of the cross-seed variance, is stated here in advance, and **does not license
demoting, re-anchoring, or omitting this statistic.** It is reported first in the manifest and
first in every summary.

---

## 3. (ii) THE RANK CO-PRIMARY -- statistic and DIRECTION

**Statistic, per seed `s`:**

```
p[s] = ( #{ b in 1..B : D_randrank[s][b] <= D_comm[s][refit 0] } + 1 ) / (B + 1)
```

i.e. the percentile of `D_comm` within that seed's own B-draw random-rank-r reference
distribution, with the standard +1 correction.

**DIRECTION -- stated explicitly, because it is easy to invert and the sign is not obvious from
the field names.**

> **LOW `p[s]` = EFFECT PRESENT.**

Read it through: MECH-537's routing phenotype is *decision content encoded in the sender but NOT
exposed through the communication subspace*. So the phenotype predicts `D_comm` is **LOW** --
the communication subspace decodes the oracle's action *worse* than a random same-rank subspace
does. A low `D_comm` sits near the BOTTOM of the reference distribution, so few draws fall at or
below it, so `p[s]` is SMALL. Small `p[s]` = the communication subspace is specially bad at
carrying the action = the routing phenotype is present. This is the same sign as C2 =
`D_randrank - D_comm` being positive.

Cross-check against the recorded field name: the smoke JSON's
`frac_draws_at_or_below_recorded_comm` is this quantity without the +1 correction, and its values
(0.583 / 0.042 / 0.042 / 0.500 / 0.000 / 0.000 on seeds 42-47) pair with C2 values of 0.0015 /
0.0329 / 0.0407 / 0.0006 / 0.0871 / 0.0825. Low fraction goes with high C2. Confirmed.

**`D_comm` enters as a SINGLE decoder fit (refit 0), matched to the randrank draws' single
fits.** This is deliberate and is a correctness requirement, not an economy: the null being
tested is *`D_comm` is exchangeable with a random rank-r subspace*, and exchangeability holds
only between quantities produced by the SAME fit protocol. Averaging `D_comm` over K refits while
comparing it to single-fit draws would shrink the numerator's noise but not the reference's, and
would inflate apparent extremity. Under the stated null, `p[s]` is exactly uniform on
`{1/(B+1), ..., (B+1)/(B+1)}`.

**Recorded, NOT scored:** `percentile_refit_spread[s]` -- the percentile recomputed from each of
the K `D_comm` refits, so a reader can see how much of the rank verdict is decoder jitter. The
declared statistic remains refit 0.

---

## 4. (iii) THE COMBINING RULE ACROSS SEEDS, AND ITS ALPHA -- fixed before the run

**n = 6 seeds (42-47), the same set as 1043a, for direct lineage comparability. Six seeds is
coarse for any combining rule; the rule is therefore fixed here, in advance, and reported with a
mandatory per-seed table that cannot be collapsed.**

Across seeds the `p[s]` are independent: each seed trains its own encoder on its own data, so
under the null they are independent uniforms.

- **PRIMARY combining rule: FISHER.** `X2 = -2 * sum_s ln p[s]`, compared to chi-square with
  `df = 2 * n_contributing`. **ALPHA = 0.05, one-sided** (low percentiles = effect). Discreteness
  at B = 1000 is 1e-3-grained, so the chi-square approximation is effectively exact and, where it
  errs, errs conservative.
- **ROBUSTNESS combining rule, reported alongside and pre-registered as such: SIMES.** Reject if
  `min_k ( n * p_(k) / k ) <= 0.05` over the order statistics. Simes is far less driven by a
  single extreme seed than Fisher is.
- **Pre-registered reading of a disagreement between them.** If Fisher fires and Simes does not,
  the combined result rests on one or two seeds, and it is reported in those words -- not as a
  clean positive.

**Why Fisher and not a cross-seed average.** Fisher aggregates evidence; it does not average
effect sizes. Averaging is precisely what the declared primary's t-CI does, and averaging a split
is how this lineage reached two autopsies. Fisher plus the mandatory split declaration (section 7)
reports the heterogeneity instead of dissolving it.

**No disjunctive success rule, and therefore no multiplicity correction between the two
primaries.** We do NOT declare success if *either* primary fires. The declared primary is reported
on its own terms against its own declared null; the rank co-primary is reported on its own terms
against alpha = 0.05. A disagreement between them is a RESULT (section 7), not a tie broken in
favour of whichever is friendlier.

---

## 5. (iv) THE COMPETENCE INCLUSION CRITERION -- and the mandatory both-ways reporting

**Criterion, per seed, evaluated from that seed's OWN measured quantities:**

```
COMPETENT[s]  <=>  rr_mean[s] > strongest_trivial_agreement[s]      (strict, threshold 0.0)
```

`rr_mean[s] = mean_B(D_randrank[s])`; `strongest_trivial_agreement[s]` is the previous-executed-
action predictor, recorded per seed by the existing 1002 machinery.

**Rationale.** If a random rank-r subspace decodes the oracle's action no better than the
previous-action predictor, then that seed's reference distribution is not a distribution of
*competent* decoders. `D_comm` sitting low inside it does not mean the communication subspace is
specially bad -- it means everything at that rank is bad. Such a seed is **NON-CONTRIBUTORY**,
which is NOT the same as evidence of no effect. This is the elevation bar 1043a applied as a
global readiness GATE (at 0.05), re-scoped to a per-seed INCLUSION criterion (at 0.0). Two
differences matter: it asks "competent at all", not "competent by a margin"; and it scopes a SEED
out, never the whole run. That is the substantive change from 1043a, which refused at readiness
and adjudicated nothing.

**Expected failures, named in advance so that a deviation is visible.** On the smoke's B = 24
means, exactly one of six fails: **seed 45, margin -0.0219**. Seeds 42/43/44/46/47 pass with
margins +0.0364 / +0.0402 / +0.0122 / +0.0117 / +0.0230. At B = 24 the SE of `rr_mean` is
0.0309/sqrt(24) = 0.0063, so seed 45's margin is ~3.5 SE below zero; at B = 1000 the SE falls to
~0.00098 and the determination will be sharp. **If a different seed fails, or if seed 45 passes,
that is new information and is reported as such.**

**MANDATORY BOTH-WAYS REPORTING -- this is the clause the design most depends on.**

Two analysis sets, **both declared, both always reported, neither permitted to stand alone**:

- **SET-ALL** -- all 6 seeds, no exclusion. Fisher on 6 p-values, df = 12.
- **SET-COMPETENT** -- only seeds with `COMPETENT[s] == True`. Fisher on `n_c` p-values,
  df = 2 * `n_c`.

**Reporting only SET-COMPETENT is the failure mode this document exists to prevent.** The
manifest carries both under fixed keys; any summary, abstract, or governance note that states one
without the other is non-compliant with this pre-registration.

- If SET-ALL and SET-COMPETENT **agree** at alpha: the conclusion is robust to the inclusion
  question, and is reported that way.
- If they **disagree**: the conclusion is conditional on competence, and the run is labelled
  `rank_coprimary_conditional_on_competence`.
- If `n_c < 3`: SET-COMPETENT is still reported but is flagged underpowered, and the run's
  conclusion rests on SET-ALL.

---

## 6. (v) B, ITS JUSTIFICATION, AND WHY THE SMOKE'S B=50 DOES NOT CARRY OVER

### B = 1000.

**RESOLUTION IS CAPPED AT 1/B.** With the +1 correction the floor is `1/(B+1)`. At B = 24 the
floor is 0.04, so the two seeds recorded as 0.000 (46 and 47 -- both with `D_comm` below even the
randrank MINIMUM: 0.5037 < 0.5444 and 0.5102 < 0.5371) **cannot be distinguished from 0.042**, the
value of the two moderate seeds. They must be reported as **"< 1/B"**, never as zero. At B = 1000
they resolve to 0.001-grained values and the four-way structure becomes a measurement.

**The re-derivation the decision chip asked for: B trades against RANK RESOLUTION, not against
de-noising, and the smoke's B = 50 was derived for the de-noising use.** For de-noising, the
relevant quantity is `SE = sd_draw / sqrt(B)`, which at B = 50 is 0.0035 -- adequate, and that is
what the smoke recommended. For the rank co-primary the relevant quantity is the **floor
`1/(B+1)`**, which enters the Fisher statistic as `-ln(1/(B+1)) = ln(B+1)` per resolution-capped
seed. A capped seed contributes evidence bounded by the censoring, not by the data.

Projecting the smoke's observed fractions to larger B (these justify the B CHOICE by showing where
resolution censoring dominates; they are **not** predictions of 1043b's result, which re-measures
`D_comm`):

| B | floor 1/(B+1) | Fisher X2 | Fisher p | **Simes p** | cost, 6 seeds |
|---|---|---|---|---|---|
| 24 (smoke) | 0.0400 | 25.31 | 0.013 | **0.12** | 0.04 h |
| 50 (smoke's de-noising rec.) | 0.0196 | 29.35 | 0.0035 | **0.059** | 0.14 h |
| 200 | 0.0050 | 35.94 | 3.3e-4 | **0.0149** | 0.55 h |
| 500 | 0.0020 | 39.86 | 7.6e-5 | **0.0060** | 1.38 h |
| **1000** | **0.0010** | **42.72** | **2.5e-5** | **0.0030** | **2.77 h** |
| 2000 | 0.0005 | 45.53 | 8.3e-6 | 0.0015 | 5.53 h |

**The decisive row is B = 50: the pre-registered Simes robustness check returns p = 0.059 and
does NOT clear alpha -- purely from resolution censoring, not from the data.** A design at B = 50
would therefore be unable to report the split as robust even if the split is exactly as the smoke
measured it. That is the concrete re-derivation: **B = 50 does not carry over to this use.**

B = 1000 puts Simes ~17x below alpha and Fisher ~3 orders below, with the floor three orders below
alpha so no seed is evidence-capped. B = 2000 doubles the cost for a further ~2x, which is
diminishing. B = 500 is the honest cheaper alternative (Simes 0.0060, ~8x below alpha) and is
rejected only because the margin is thin enough that a modestly weaker true effect would land
non-significant for censoring reasons again -- the exact failure this run exists to stop
repeating.

**Cost.** At the measured ~1.66 s/replicate (one decoder fit, the dominant term; an RRR refit is
~0.06 s and is not in this loop), B = 1000 is ~28 min/seed, **~2.8 h over six seeds**, against a
warmup-dominated base of ~1.8 h/seed. Total ~13 h, versus 1043a's 11.13 h. The permutation loop
1043a spent ~332 s/seed on is REMOVED (it answered the wrong question), partly offsetting.

**Also fixed in advance:** `K = 8` refits, matching the smoke's `K_FIXED = 8`, used for (a) the
decoder-noise decomposition in section 7's gate and (b) `mean_K(D_comm)` in the declared primary
and `percentile_refit_spread`. Cost ~26 s/seed, negligible.

---

## 7. THE READINESS GATE (option A's non-degeneracy gate), PER SEED

The gate certifies that the reference distribution can RESOLVE `D_comm` -- which is what the
gate's own shipped purpose text says ("a low `D_comm` must carry information about ORIENTATION").
It does **not** certify elevation over the trivial predictor; that quantity is retained as a
recorded readout and as section 5's per-seed competence criterion.

**Per seed, both must hold:**

1. **Orientation dominance.** `sd_orientation[s] >= 2.0 * sd_decoder[s]`, where
   `sd_orientation[s] = sqrt(max(0, sd_total[s]^2 - sd_decoder[s]^2))` and `sd_decoder[s]` is the
   sd over K = 8 refits of ONE fixed draw.
   *Justification (mechanistic, not calibrated to pass):* below 2x, the reference distribution's
   spread is not dominated by subspace orientation, so a percentile measures decoder refit jitter
   rather than orientation, and the statistic does not mean what it is read as.
   *Disclosed:* the smoke clears this 6/6 with ratios 3.69 / 3.05 / 3.40 / 8.33 / 3.62 / 5.82,
   minimum **3.05**.
2. **Absolute spread floor.** `sd_total[s] >= 0.005`.
   *Justification:* held-out steps are ~2000, so one classification flip moves the agreement
   statistic by ~1/2000 = 0.0005. A floor of 0.005 = ~10 flips asserts the distribution's spread
   exceeds the granularity of the statistic itself.
   *Disclosed:* the smoke's minimum `sd_total` is 0.0191, ~3.8x above the floor.

**Per-seed scoping, NOT a whole-run AND.** A seed failing the gate is scoped out and recorded;
the run proceeds on the rest. This follows the V3-EXQ-785 rule (one arm's impossible precondition
must not vacate another arm's valid result). **Only if ZERO of six seeds pass does the run
self-route `substrate_not_ready_requeue`.**

**SPLIT DECLARATION -- mandatory, mechanical, fixed now.** The design must be able to report the
split as the finding rather than average it away. Declared rule:

> **SPLIT is declared when at least one contributing seed has `p[s] <= 0.05` AND at least one
> contributing seed has `p[s] >= 0.25`.**

When SPLIT fires, the run's label carries a `_split` suffix and the per-seed percentile vector is
reported in the summary line, not only in the manifest body. On the smoke's numbers SPLIT fires
(0.583 / 0.042 / 0.042 / 0.500 / <1/B / <1/B).

---

## 8. INTERPRETATION GRID -- including the DISAGREEMENT outcomes

**Pre-registered, and binding: if the declared primary and the rank co-primary disagree, that
disagreement IS the result and is reported as such.** The run's criteria do not quietly become
"whatever the rank statistic says".

| declared primary (95% CI on cross-seed mean C2) | rank co-primary (Fisher, alpha 0.05) | label |
|---|---|---|
| CI excludes 0 and excludes 0.05 from BELOW (entirely above 0.05) | significant | `orientation_effect_confirmed_both_primaries` |
| CI includes 0.05 (undecided) -- **the expected case** | significant | `orientation_effect_rank_only_magnitude_undecided` |
| CI includes 0.05 | not significant | `orientation_effect_not_established` |
| CI excludes 0.05 from ABOVE (entirely below 0.05), excludes 0 | significant | `orientation_effect_present_but_below_floor` |
| CI excludes 0.05 from above, excludes 0 | not significant | `orientation_effect_sub_floor_rank_null` |
| CI includes 0 | any | `orientation_contrast_not_positive` |

Suffixes, appended mechanically: `_split` (section 7), `_conditional_on_competence` (section 5).

**Hypothesis-ledger consequences, declared in advance:**

- **H1-small-but-real.** Declared null = "the CI excludes 0.05". Adjudicated by the DECLARED
  PRIMARY only. The rank co-primary does not speak to H1's magnitude claim and must not be used
  to close it.
- **H2-no-orientation.** Declared null = "the observed C2 sits inside the reference null".
  Adjudicated by the RANK CO-PRIMARY, which is the reference distribution H2 actually names.
  A significant Fisher result falsifies H2's declared null.
- **H3-no-low-rank-bottleneck.** Declared null = "C2 is flat in rank". Adjudicated by the recorded
  rank ladder (C2 at `r_pars` vs at rank 32), unchanged from 1043a.

---

## 9. WHAT THIS RUN IS EXPECTED TO REPORT -- do not expect a clean YES

The six smoke percentiles are **not a uniform shift, they are a SPLIT**: two seeds typical of
random (0.583, 0.500 -- and 0.500 is seed 45, which also fails the competence criterion), two
moderate (0.042, 0.042), and two extreme (< 1/B, < 1/B, with `D_comm` below even the randrank
MINIMUM on both). The design above reports that split as the finding. The current
absolute-difference framing averages it into "positive, small, undecided", which is how this
lineage arrived at an autopsy twice.

Stated bluntly so it cannot be claimed as a surprise later: **the most likely single outcome is
`orientation_effect_rank_only_magnitude_undecided_split`** -- declared primary undecided, rank
co-primary significant, split declared, and one seed non-contributory on competence. That is a
real adjudication of H2 and a non-adjudication of H1's magnitude claim, and it should be reported
as exactly that, with no upgrade.

---

## 10. WHAT IS SETTLED AND MUST NOT BE RE-MEASURED

From `REE_assembly` `dc39f672a0`,
`evidence/planning/v3_exq_1043b_randrank_reference_smoke_20260920.{md,json,py}`:

- One decoder fit ~1.6 s; one RRR refit at a single rank ~0.06 s (25x cheaper). 1043a's
  200-replicate permutation loop (~332 s/seed) was almost entirely DECODER fits.
- Within-seed draw sd 0.0244, of which ~94% is genuine subspace-ORIENTATION variance
  (0.0237) and only 0.0055 is decoder-training noise. `x1002._train_adapter` **never seeds
  anything** -- its `seed` / `arm_id` arguments are print labels; `_make_adapter` and
  `torch.randperm` draw from the ambient global RNG.
- Pipeline fidelity vs the landed 1043a manifest: OK on 6/6 seeds (`n_sender_dims_live` = 146,
  `heldout_steps` 2148/2061/1965/2001/2162/2050, `strongest_trivial_agreement` all matching).
  Recomputing the C2 CI from 1043a's recorded single draws reproduces `[0.0051, 0.0948]` to four
  decimals.
- `r_pars` per seed: 11 / 11 / 10 / 8 / 10 / 10 on seeds 42-47.

**The smoke is a PROBE: no manifest, no `claim_ids`, no `substrate_hash`. Its percentiles use
1043a's RECORDED `D_comm` as an indicative reference point and are NOT a measurement of 1043b's
statistic** (`D_comm` needs the fitted receiver, which the probe did not build). They are used in
this document only to (a) justify the B choice by resolution adequacy and (b) name expected
failures in advance. 1043b re-measures `D_comm`.

---

## 11. PRE-FLIGHT GATES (recorded for audit)

- **Step 2.4 existing-evidence / GOV-REUSE-1.** Decisive readout = the per-seed percentile of
  `D_comm` in a many-draw random-rank-r reference distribution. Checked: `V3-EXQ-1043`
  (`...20260916T111630Z_v3`) and `V3-EXQ-1043a` (`...20260919T030056Z_v3`) -- both record ONE
  randrank draw per seed, so no reference distribution exists; the 2026-09-20 smoke has a
  distribution but at B=24 (resolution-censored, section 6) and no measured `D_comm`.
  **PARTIALLY recoverable -> run, scoped to the missing piece**: the B=1000 reference distribution
  paired with a same-run measured `D_comm`. The permutation-null loop is dropped.
- **Step 2.5 / 2.5a substrate readiness.** Read-only over a frozen encoder; no `ree_core` change,
  no new substrate. Identical footprint to 1043a, which ran to completion with six of seven
  readiness gates green.
- **Step 2.5b re-derive brake.** MECH-537 count = **0**. Both prior autopsies are
  instrument/measurement defects owing no substrate build, which the brake predicate correctly
  does not count. Not braked.
- **Step 2.5c substrate-path overlap.** No open `corrupting` entry overlaps the data-generating
  path: `x1002._collect_episodes` drives episodes with the ORACLE or a RANDOM policy and labels
  are ALWAYS the oracle's action, so the agent's own E3 selection is not in the label path, and
  the four open corrupting entries (`MECH-320` tonic_vigor, `contextmemory-write-path-addressing-
  degeneracy`, `sd_blocked_agency_mismatch_floor_calibration`, `sd105_frozen_shared_entropy_floor_
  multiplier`) are all selection/affect-side. **Declared DEGRADING overlaps**, carried as stated
  limitations exactly as 1043a carried SD-106: `SD-018` and `SD-106`
  (`ree_core/latent/stack.py`, `ree_core/latent/zworld_p0.py` -- the receiver encoder),
  `SD-ZWORLD-SENSE-PATH-PARITY` (`REEAgent.sense`, `ZWorldP0Trainer._z_world_path` -- the receiver
  read path), and `sd_zharm_a_warmup_optimizer_group` / `sd061-resume-progress-ecology`
  (`allon_training.py::_train_all_on_agent`, the warmup).
- **Step 2.5d falsifier-runnability (GOV-UNWRITTEN-1).** EVENT: none required -- the falsifier is
  read at the end of the P2 measurement phase, emitted by the driver. DV: the per-seed percentile
  and the cross-seed C2 CI. INSTRUMENT: `_project` + `x1002._train_adapter` + `x1002._agreement`
  (randrank arm) and `interface_probe.communication_subspace` (comm arm). **CAN IT MOVE -- MEASURED,
  not asserted:** the smoke built the reference distribution at the real sample size on all six
  seeds (`sd_total` 0.019-0.031, orientation component 3.05-8.33x decoder noise) and located
  1043a's recorded `D_comm` inside it at 0.000-0.583 -- **neither degenerate nor saturated at
  either end**. Not ABSENT, not INERT.
- **Step 2.6 ethics preflight.** All involvement flags `false`, `decision: allow`. Read-only probe
  over a frozen encoder; no harm drive, no sleep loop, no self-model.
- **DV-symmetry invariance.** The DV (held-out top-1 agreement of a decoder refit on the projected
  sender) is invariant under (a) orthogonal change of basis WITHIN the r-dim subspace, since the
  decoder is refit, and (b) permutation of episodes within a fold group. The manipulation changes
  the SUBSPACE (its span), not the basis within it, and not the fold structure -- so **the
  manipulation is NOT invariant under the DV's symmetry group**. Confirmed empirically by the
  measured orientation-variance component (0.0237 mean), which would be ~0 under invariance. Arms
  are rank-matched (`r_pars` per seed), so the contrast is not a rank artefact.

---

## 12. WHAT WOULD MAKE THIS PRE-REGISTRATION VIOLATED

Recorded so a later autopsy has a checklist rather than a judgement call:

1. Reporting the rank co-primary without the declared primary, or demoting the declared primary
   because it came back undecided.
2. Reporting SET-COMPETENT without SET-ALL.
3. Changing B, the combining rule, alpha, the direction convention, or the competence threshold
   after any 1043b cell has run.
4. Reading a resolution-floored percentile as zero rather than as `< 1/B`.
5. Averaging a declared SPLIT into a single summary number without reporting the per-seed vector.
6. Upgrading `orientation_effect_rank_only_magnitude_undecided` to a claim that H1's magnitude
   question is settled.
7. Treating the 2026-09-20 smoke's percentiles as evidence for MECH-537. They are a probe.

---

## 13. PROVENANCE

- Decision: OPTION E, user, 2026-09-22, chip `chip-20260920-exq1043b-readiness-gate-formula`
  (amended by `orchestrate-20260922-0722`).
- This document: chip `chip-20260922-exq1043b-prereg-rank-coprimary`, session
  `pensive-feistel-471e3c`.
- Upstream autopsies: `failure_autopsy_V3-EXQ-1043_2026-09-17.json`,
  `failure_autopsy_V3-EXQ-1043a_2026-09-20.json` (both CONFIRMED).
- Instrument probe: `v3_exq_1043b_randrank_reference_smoke_20260920.{md,json,py}`,
  `REE_assembly` `dc39f672a0`.
- Hypothesis ledger: `hypothesis_space_registry.v1.json`, qid
  `mech537_communication_subspace_orientation`.
