# V3-EXQ-1043b -- PRE-REGISTRATION (option E: rank co-primary alongside the declared absolute-difference primary)

Written 2026-09-22T19:49:59Z by session `pensive-feistel-471e3c`, BEFORE the driver was written
and BEFORE anything was queued. Chip `chip-20260922-exq1043b-prereg-rank-coprimary`.

**Authority.** User decision OPTION E on `chip-20260920-exq1043b-readiness-gate-formula`, answered
2026-09-22 in orchestrator session `orchestrate-20260922-0722`. Upstream: the CONFIRMED autopsy
`failure_autopsy_V3-EXQ-1043a_2026-09-20.json` (`routing_detail.successor`), ratified by
`/governance` cycle governance-20260920.

> **AMENDED 2026-09-22T20:40Z, BEFORE ANY CELL RAN -- see Amendment 1 at the end.** The
> Step 4.5 adversarial red-team (cross-model, fable) returned CONTESTED and demonstrated by
> execution that TWO claims in this document as first written were WRONG: the characterisation
> of Simes in section 4, and the quotation of H2's declared null in section 1(a). Both are
> corrected in place below and the corrections are itemised in Amendment 1. This is permitted
> by this document's own section 12, whose violation 3 is scoped to changes made *after any
> 1043b cell has run* -- nothing had run, and no result had been seen. **Correcting a
> demonstrated error before the run is the opposite of the move section 12 forbids.**

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

**(a) The HYPOTHESIS the rank statistic tests was registered on 2026-09-17, three days before
the smoke ran -- though its registered METHOD was not this one, and the distinction matters.**
`hypothesis_space_registry.v1.json`, qid `mech537_communication_subspace_orientation`,
hypothesis **H2-no-orientation**, both fields quoted in full and verbatim:

> *label*: "the fitted communication subspace is not meaningfully different from **a random
> subspace of the same rank** at this interface; C2's positivity is noise and will not survive a
> permutation null."
>
> *desc*: "Permutation null on the RRR fit itself (refit on shuffled sender-receiver pairing) to
> give C2 a within-run reference distribution instead of a hand-set floor. **Declared null: the
> observed C2 sits inside the permutation null.**"

**CORRECTED (red-team finding 6).** This document as first written quoted the declared null as
"the observed C2 sits inside the [reference] null", substituting a bracketed word for
"permutation". That substitution overstated the case and is withdrawn. The honest statement is
a three-step one, and it is still a good defence -- just not the one-line one:

1. H2's **hypothesis**, in its `label`, is about *a random subspace of the same rank*. That is
   the thing the percentile measures, and it was registered on 2026-09-17.
2. H2's **registered method**, in its `desc`, was a permutation null on shuffled pairing. 1043a
   built exactly that method and ran it.
3. The CONFIRMED 1043a autopsy then established that **the registered method does not test the
   registered hypothesis**: the permutation null answers "is the fitted map real?" (p = 1.0 on
   6/6 -- all 200 shuffled refits decoded WORSE than the real subspace) and never constructs a
   random same-rank subspace at all. Its own words: "A refit-based permutation null answers 'is
   the fitted structure real?'. 'Is its ORIENTATION special?' needs a reference over random
   subspaces of the same rank."

So the claim this document is entitled to make is: **the rank co-primary is the instrument H2's
registered HYPOTHESIS requires, substituted for a registered METHOD that a confirmed autopsy had
already ruled unable to test it.** That is a method change ratified by an autopsy, not a
statistic introduced after seeing a disappointing number. The weaker, accurate version of the
claim is the one that governs.

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
- **SECONDARY, reported alongside: SIMES.** Reject if `min_k ( n * p_(k) / k ) <= 0.05` over
  the order statistics. A valid FWER-controlling test, reported as a per-seed-strength readout.
- **ROBUSTNESS-AGAINST-ONE-SEED check: LEAVE-ONE-OUT FISHER.** Drop the smallest per-seed p (the
  most influential seed under Fisher), re-run Fisher on the remaining `n-1`, and report whether
  it still clears alpha. If the full-set Fisher fires and the leave-one-out does NOT, the
  combined result rests on a single seed and is reported in those words -- **never as a clean
  positive.** Recorded, not scored: it qualifies how the verdict reads, it does not gate it.

> **CORRECTED (red-team finding 1), and this correction is load-bearing.** This document as
> first written described Simes as "far less driven by a single extreme seed than Fisher", and
> used a *Fisher-fires-Simes-does-not* disagreement as the test for "rests on one or two seeds".
> **That is backwards at B = 1000, and the reversal is caused by the very resolution floor that
> B = 1000 was chosen to lower.** Simes's `k = 1` order term is the BONFERRONI term `n * p_min`;
> at B = 1000 the floor is `1/1001`, so a single seed at the floor gives `6/1001 = 0.006 <=
> 0.05` and **Simes fires on that one seed alone**. Measured against the driver's own functions:
>
> | per-seed p | Fisher | Simes |
> |---|---|---|
> | `[0.001, 1.0 x5]` | 0.313 -- NOT significant | **0.006 -- SIGNIFICANT** |
> | `[0.008, 0.5 x5]` | 0.166 -- not significant | **0.048 -- SIGNIFICANT** |
> | `[0.009, 0.5 x5]` | 0.176 -- not significant | 0.054 -- not significant |
>
> So at this B, Simes is MORE single-seed-driven than Fisher, not less, and the original
> predicate could never have fired on the case it was written for. Simes is retained and
> reported (it is what this document named, and it is a valid test); its ROLE is corrected, and
> the robustness job moves to the leave-one-out check, which tests the property directly.
> Pinned by four self-test assertions in the driver so the claim cannot silently drift back.

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

> **IMPLEMENTATION NOTE (red-team finding 3), because the obvious encoding of that sentence is
> wrong.** "Zero seeds pass" must be counted CONJUNCTIVELY, per seed: a seed passes only if it
> meets clause 1 AND clause 2 *on that same seed*. The driver's first implementation reported
> the BEST seed on each clause SEPARATELY, so a seed passing only the ratio plus a different
> seed passing only the sd floor would turn both checks green while **no single seed was
> non-degenerate** -- and the analysis would then silently fall back to all six. The operative
> gate is now an explicit count of seeds meeting both clauses together
> (`randrank_reference_nondegenerate_seed_count >= 1`); the two per-clause checks are retained
> only because they name WHICH clause failed, which a bare count cannot.

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
| CI includes 0 | **not significant** | `orientation_contrast_not_positive` |
| CI includes 0 | **significant** | `orientation_contrast_not_positive_rank_significant_DISAGREEMENT` |

Suffixes, appended mechanically: `_split` (section 7), `_conditional_on_competence` (section 5).

> **CORRECTED (red-team finding 2), and this was the most consequential of the seven.** The last
> row of this table originally read "CI includes 0 | **any** | `orientation_contrast_not_positive`"
> -- i.e. a non-positive CI VETOED the rank co-primary and erased it from the label. That
> contradicts this document's own governing principle, stated two paragraphs above it, that a
> disagreement between the primaries IS the result. And it is not a theoretical concern: on the
> smoke's own numbers the CI is `[+0.00172, +0.08061]`, so the veto is a **coin flip decided by
> the one seed this document already calls NON-CONTRIBUTORY.** `ci_positive` is computed over
> non-degenerate seeds with no competence scoping, so seed 45 enters it unconditionally;
> shifting seed 45's C2 by **-0.005** moves the lower bound to `-0.00028` and flips the label
> from the expected outcome to "contrast not positive", **silencing a Fisher p of ~2e-5**.
> The competence exclusion is fully defused for the rank statistic (SET-ALL is the scored
> basis), and was NOT defused here -- the incompetent seed could reach the headline through the
> one door section 5's both-ways clause does not cover.
>
> **The fix removes the VETO, not the statistic.** The CI is NOT re-scoped to competent seeds --
> that would be re-anchoring a pre-registered statistic, which is the move this whole document
> exists to refuse. A non-positive CI with a significant rank co-primary now reports as an
> explicit DISAGREEMENT, which is what it is.

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

---

## AMENDMENT 1 -- 2026-09-22T20:40Z, before any cell ran

**Trigger.** `/queue-experiment` Step 4.5 adversarial design red-team, run cross-model (drafting
session Opus 5; reviewer **fable**), on the driver plus this document, before the queue entry
existed. **VERDICT: CONTESTED** -- no pre-registered criterion was non-discriminating under every
outcome, so not BLOCKING, but seven findings, of which five changed the design or this document.

**Standing of this amendment.** Section 12's violation 3 forbids changing B, the combining rule,
alpha, the direction convention or the competence threshold **after any 1043b cell has run**. No
cell had run, no result had been seen, and the queue entry did not yet exist. Two of the seven
findings showed that statements in this document were *demonstrably false as written* -- verified
by executing the driver's own functions, not by argument. Leaving them standing to preserve the
letter of a pre-registration would have shipped a document that misdescribes its own instrument.
Every correction below is recorded rather than silently applied, and each is a CORRECTION or a
TIGHTENING; **none relaxes a threshold, and none was made in response to a result.**

| # | Family | Status | Disposition |
|---|---|---|---|
| 1 | criterion cannot discriminate | **CONFIRMED** | Simes's role corrected (section 4); robustness job moved to a new leave-one-out Fisher. Pinned by 4 self-test assertions. |
| 2 | verdict grid | **CONFIRMED** | The non-positive-CI veto removed; a disagreement now reports as `..._rank_significant_DISAGREEMENT` (section 8). |
| 3 | gate certifies its own subject | **CONFIRMED** | Operative gate is now a CONJUNCTIVE per-seed count (section 7). |
| 4 | verdict grid | **CONFIRMED** | `_c2_falsified` rescoped to the same seed set the confirming conjunct reads. |
| 5 | verdict grid | **CONFIRMED, NOT FIXED** | Recorded as a stated limitation below. |
| 6 | pre-registration provenance | **CONFIRMED** | Section 1(a) quotation corrected and the defence weakened to the accurate version. |
| 7 | cosmetic | **CONFIRMED** | `primaries_agree` now compares existence against existence. |

**Finding 5, CONFIRMED and deliberately NOT fixed -- recorded because it is the one a later
autopsy should read first.** Neither primary can move `evidence_direction`. `_adjudicate`'s
confirming branch requires C4 (C4b at or below the per-seed measured ceiling on >= 4 seeds), and
on 1043a's landed numbers at the same scored rank that is **2 of 6**:

| seed | 42 | 43 | 44 | 45 | 46 | 47 |
|---|---|---|---|---|---|---|
| measured | 1.1992 | 1.1633 | 1.1770 | 0.9451 | 0.9709 | 1.1523 |
| ceiling | 1.1174 | 1.1008 | 1.0807 | 1.0907 | 1.1218 | 1.0285 |
| | fail | fail | fail | **PASS** | **PASS** | fail |

So this document's own most-likely outcome -- H2 decisively falsified by the rank co-primary --
**coexists with `outcome: FAIL`, `evidence_direction: mixed`,
`routing_signature_incomplete_undetermined`**, byte-identical to what V3-EXQ-1043 landed. A
consumer reading only `evidence_direction` therefore sees **no movement across three runs of this
lineage**, while `interpretation.primary_agreement` carries a decisive result.

This is NOT repaired here, and the reason is the reason this whole document exists: C4 is part of
MECH-537's registered CONFIRMING conjunction, and loosening it so that the rank co-primary could
drive `evidence_direction` would be re-anchoring a pre-registered criterion to make a favoured
statistic count. **It is recorded as a limitation instead, and the limitation is owed to
governance:** the C4b ceiling rule carries its own unresolved weakness (1043a's red-team M2, the
effective per-unit bar rising toward 1.0 as F approaches I, "OWED to governance / a successor
autopsy"), and this is the second consequence of the same unresolved thing. **A reader adjudicating
this run must read `interpretation.primary_agreement`, not `evidence_direction` alone.**

**What did NOT change**, so the record is unambiguous: B = 1000; Fisher as the primary combining
rule; alpha = 0.05; the direction convention (LOW percentile = effect present); the competence
threshold (0.0) and its both-ways reporting requirement; the non-degeneracy thresholds (2.0 and
0.005); the declared primary, its statistic and its declared null; and the requirement that the
declared primary is reported whatever it says. The expected outcome in section 9 is unchanged.

**Cleared by the red-team**, recorded because a clean finding is evidence too: `_project` uses an
independent basis per draw with no shared fitted object across arms; `x1002._train_adapter` never
reseeds on this path (the only `torch.manual_seed` in x1002 is in its own `run_experiment`, off
this path); the percentile's direction and its `+1` floor; Fisher's `df = 2n` and its
discreteness being conservative; `_c2_falsified` as a positive predicate rather than `not c2`;
and the equivalence branch being unreachable (full 0.92-0.95 against comm 0.50-0.60).

**One item the red-team did NOT raise, recorded by the drafting session rather than left
implicit.** Draw 0 of the reference distribution reuses the `ws250_randrank_parsrank` arm's
agreement, which was fitted inside `arm_cell` (a complete RNG reset), while draws 1..B-1 are
fitted from the ambient RNG. This is deliberate -- it is what makes the comparability form of the
declared primary 1043a's *literal* number rather than a re-drawn approximation -- and it is
benign in the direction that matters: `D_comm` (refit 0) is ALSO a reset-RNG fit, so the two
sides of the percentile comparison are matched on that axis, and 999 of the 1000 reference
members are ambient. Since `_train_adapter` draws only its initialisation and shuffling from the
RNG, a reset-RNG fit is a valid draw from the same decoder-noise distribution, not a
systematically different one. Recorded so a later reader does not have to rediscover it.
