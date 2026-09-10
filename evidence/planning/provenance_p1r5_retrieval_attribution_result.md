# Provenance P1-R5 — result: the retrieval-attribution arm, and the stored-tag/attribution discriminator

**Date:** 2026-09-10T20:23:37Z
**Arm:** [`scripts/provenance_p1r5_retrieval_attribution_arm.py`](../../scripts/provenance_p1r5_retrieval_attribution_arm.py)
**Harness:** [`scripts/provenance_genealogy_harness.py`](../../scripts/provenance_genealogy_harness.py) — imported **unmodified**
**Compares against:** [`provenance_p1_result.md`](provenance_p1_result.md) (REE_assembly `062d774289`)
**Specified by:** [`provenance_branch_hippocampal_audit_verification_20260910.md`](provenance_branch_hippocampal_audit_verification_20260910.md) §6–§7 (`P1-R5`)
**Status:** synthetic arm run only. No claim registered or promoted, no queue entry, no edit to the harness, the P1 driver, the design note, the ladder or the supplement.

Reproduce: `/opt/local/bin/python3 scripts/provenance_p1r5_retrieval_attribution_arm.py --out-json <path>` (~3 min, three seed pairs).

---

## 1. Verdict, up front

**Both routes inflate. §6's discriminator table is realised exactly. And the most consequential result is neither of those — it is that the `dependent` fix P1 recommended does not eliminate the inflation on *either* route.**

| | Result |
|---|---|
| A1 stored-tag invariant to the criterion | **PASS** (structural) |
| A2 attribution moves with the criterion | **PASS** — range 3.943 |
| A3 attribution invariant to storage | **PASS** (structural) |
| A4 stored-tag reproduces P1 | **PASS** — 1.117 → 4.869, exact to P1's landed digits |
| A5 attribution reaches P1's magnitude | **PASS** — +3.850 vs P1's +3.753 |
| A6 absent-policy crossing | **FAIL, on BOTH routes** — see §4 |
| A7 read-time similarity sensitivity | **PASS** — rho = 1.000 |
| A7b similarity dial does not move the vote | **PASS** — accuracy range 0.006 |
| A8 where similarity acts | branch **`ATTRIBUTION_ONLY`** — §6's supposition **not realised** |
| A9a fluency reaches cardinality (readout 3) | **FAIL** on the attribution route — −0.025 |
| A9b fluency reaches source attribution (readout 2) | **PASS** on the attribution route — −33.5% relative |

Every one of these holds identically on all three seed pairs (primary 17/23, held-out 41/53 and 67/71).

**The three findings, in descending order of consequence:**

1. **`absent_policy = dependent` does not eliminate the inflation on the stored-tag route either.** P1 reported the P2 knob at its two endpoints (`N_eff` 1.117 → 1.000, "the effect vanishes"). Read across the whole decay axis it does not vanish: it peaks at **+0.760** at `tau = 20` and only then falls to zero. The same holds on the attribution route (+0.637). P1's own recommendation 3 — *report calibration as a curve, not two endpoints* — turns out to apply to P1's own P2 sub-measurement, and applying it changes the conclusion from *elimination* to *≈80% attenuation with the residue displaced into the partial-degradation regime*. **P1's numbers are reproduced exactly; it is the two-point summary of them that was the wrong summary.** §4.

2. **§6's claim that the stored-tag route has a similarity sensitivity via misbinding is not realised in this harness.** Across the whole candidate-similarity dial, **2834 misbinding re-points fired and exactly one crossed a source family** (0.035%). Misbinding re-points to the trace of highest content similarity, and a descendant's *siblings* — which share its ancestor's content — dominate any cross-family candidate; raising the similarity dial raises within-family similarity too, because siblings inherit the shared context from their common ancestor. So similarity-driven cross-family source confusion is available on the **attribution route only**. The discriminator is sharper than §6 supposed, in §6's own favour. §5.

3. **Fluency is live on the attribution route, on readout 2 and not on readout 3.** Sixteen in-place retrieval events at fixed cardinality and fixed storage move the source-attribution readout by **−33.5% relative** (`p_external` 0.0824 → 0.0547) while moving the cardinality readout by only −0.025. On the stored-tag route both are **exactly** zero. P1-R7's own criterion — confidence does not track retrieval events at fixed cardinality — passes on *both* routes (attribution confidence moves 0.5909 → 0.5890). What P1-R7 does not test, and what the attribution route does not clear, is the source-attribution readout. §6.

**What this does to P1's scope.** A5 passing is the outcome §6 called "a genuinely strong result": the effect is architecture-independent, so the branch's engineering rule applies more widely than to systems that store genealogy. But finding 1 relocates where the strength is. The cardinality inflation is architecture-independent **because the readout rule, not the representation, is the locus** — which is what P1 already said, and this arm confirms it by changing the entire route by which the pairwise structure is computed and getting the same behaviour. The narrowing is elsewhere and it is finding 2 and 3: similarity and fluency reach the two routes differently, so **P1's clearance of the fluency rival (P1-R7 "fluency is not live") is route-specific and readout-specific and must not be carried over to an attribution architecture.**

---

## 2. What was built, and what deliberately was not

The arm implements a **read-time attribution route** and runs it against the harness's stored-tag route. The harness is imported unmodified.

**The harness was not edited, on purpose.** Its module docstring predeclares it as the stored-tag route and states that "a read-time-attribution variant is a different architecture, not a parameter of this one." Adding a read-time path to that file would falsify its own predeclaration and would touch a file both P1's landed result and P3's design depend on. So the attribution route lives in the arm.

The cost of that choice is that the `N_eff` **aggregation** — the `absent_policy` fill plus `sum_i 1/(1 + dep_i)` — had to be reimplemented in the arm so that it could be applied to a pairwise matrix built from features rather than from a store. The entire validity of the comparison rests on the two routes differing in *exactly one place* and sharing everything downstream, so a reimplementation that drifted would silently invalidate every number here. That is closed by a hard gate, not by care: `assert_aggregation_equivalence()` builds 240 randomised stores spanning intact / decayed / interfered / misbound structures, computes `P` from `H.shared_ancestry_prob`, and asserts equality with `H.effective_source_count` for all three policies. It runs first and aborts the run on mismatch. **Measured worst |delta| = 0.0, exactly.**

**The one difference between the routes:**

```text
STORED-TAG    P[i][j] = H.shared_ancestry_prob(store, i, j)
              -- product of STORED binding strengths along the ancestry paths to the lowest
                 common ancestor. Degradation acts on those strengths. No read-time
                 parameter enters at all.

ATTRIBUTION   P[i][j] = sigmoid(BETA * (score(i,j) - C))
              -- a judgement made at read time from QUALITATIVE TRACE FEATURES against a
                 shiftable criterion C. The stored edge set is held constant, and
                 `attribution_score` cannot read it: it touches only content, timestamps
                 and recorded retrieval events.
```

`score` is Johnson, Hashtroudi & Lindsay 1993's three feature families mapped onto what a harness trace carries — perceptual/content detail as rectified cosine similarity (weight 0.60), contextual and semantic accompaniment as temporal proximity (0.25), and recorded cognitive operations as `store.retrieval_events` (0.15). Weights and `BETA = 12` are fixed constants, declared, not fitted.

**The association edge set is deliberately not a feature.** Feeding it into the count is exactly the "collapses distinct sources" failure the harness's two-edge-set separation exists to prevent, and it would make this route fail P1-R2 for a structural reason rather than an empirical one.

**The one fitted quantity is the reference criterion `C_STAR`**, fitted by bisection on a **calibration split with a different content seed (101)** from every reported number, so that the attribution route's intact `N_eff` matches the stored-tag route's undegraded `N_eff`. Fitted value **0.4896**, against target 1.1159. Without this, A5 would be measuring where the criterion grid happens to start rather than what the route can do.

**C1, extended across routes rather than across ancestry conditions.** Content hashes and per-episode votes are asserted bit-identical between the two routes, so any confidence difference between them is attributable to `N_eff` alone. Hard assertion, passed. Accuracy is **exactly 0.6990** in every cell of both routes' criterion and storage sweeps — the same construction-enforced flatness P1 reports, now holding across architectures too.

---

## 3. The discriminator (§6's table), measured

§6 supplies the test. It is realised exactly, and both halves are reported for what they are.

```text
                            criterion shift            elapsed interval (decay)
                            at fixed storage           at fixed criterion
  stored-tag route          0.000  (A1, structural)    +3.753  (A4)
  attribution route        +3.943  (A2)                 0.000  (A3, structural)
```

Two of those four cells are **structural**, and saying so is the point rather than a hedge. The stored-tag route takes no criterion argument, and `attribution_score` cannot reach `edge_w`; each zero therefore *had to* happen, in the same way the design note's P0 correction records that "decay never yields `FALSE_SPLIT`" is definitional. They are implementation checks. A non-zero in either cell would be a bug in the arm, not a discovery. **The empirical content is the off-diagonal**: each route moves a long way on its own axis, and the two axes are cleanly orthogonal.

### Stored-tag route — a reproduction of P1, on P1's own seeds

| decay `tau` | N_eff | confidence | accuracy | signed err | P(external) |
|---|---|---|---|---|---|
| 1e6 | 1.117 | 0.591 | 0.699 | −0.108 | 0.084 |
| 20 | 1.966 | 0.653 | 0.699 | −0.046 | 0.457 |
| 12 | 2.589 | 0.693 | 0.699 | **−0.006** | 0.615 |
| 9.5 | 2.975 | 0.715 | 0.699 | +0.016 | 0.693 |
| 8 | 3.288 | 0.731 | 0.699 | +0.033 | 0.749 |
| 6 | 3.825 | 0.757 | 0.699 | +0.058 | 0.835 |
| 4 | 4.463 | 0.783 | 0.699 | +0.084 | 0.928 |
| 2.5 | 4.869 | 0.798 | 0.699 | +0.099 | 0.983 |

Every digit matches P1's landed §3 table. A4 is therefore a real reproduction check and it passes: this module's episode builder is the same architecture P1 measured.

### Attribution route — the criterion sweep at fixed storage

`frac above` is the share of pairwise judgements scoring above the criterion — the share of the store the reader is currently willing to call one source. It is what keeps the magnitude interpretable.

| criterion | frac above | N_eff | confidence | accuracy | signed err | P(external) |
|---|---|---|---|---|---|---|
| 0.35 | 1.000 | 1.023 | 0.584 | 0.699 | −0.115 | 0.017 |
| 0.45 | 1.000 | 1.073 | 0.588 | 0.699 | −0.111 | 0.053 |
| **0.4896 = C\*** | 1.000 | **1.116** | 0.591 | 0.699 | −0.108 | 0.082 |
| 0.55 | 0.998 | 1.226 | 0.599 | 0.699 | −0.100 | 0.155 |
| 0.60 | 0.914 | 1.385 | 0.611 | 0.699 | −0.088 | 0.247 |
| 0.65 | 0.511 | 1.631 | 0.630 | 0.699 | −0.069 | 0.369 |
| 0.70 | 0.186 | 1.990 | 0.655 | 0.699 | −0.044 | 0.510 |
| 0.75 | 0.008 | 2.466 | 0.685 | 0.699 | **−0.014** | 0.649 |
| 0.85 | 0.000 | 3.578 | 0.746 | 0.699 | +0.047 | 0.856 |
| 0.95 | 0.000 | 4.415 | 0.781 | 0.699 | +0.082 | 0.951 |
| 1.05 | 0.000 | 4.802 | 0.795 | 0.699 | +0.096 | 0.985 |
| 1.20 | 0.000 | 4.966 | 0.801 | 0.699 | +0.102 | 0.997 |

**Calibration is U-shaped on this route too**, with the minimum at `C = 0.75` (−0.014) — the same shape P1 found on the decay axis with its minimum at `tau = 12` (−0.006). Under-confident when the criterion is lax, best calibrated at a moderate criterion, over-confident when strict. An endpoint-only report of either route would miss the same thing.

**A5 passes and must be reported as near-definitional.** The attribution route reaches +3.850 from `C*`, exceeding P1's landed +3.753 — so *both routes inflate*. But both routes feed the identical aggregation, and that aggregation returns `N_eff = n` whenever the pairwise matrix is driven to zero. **Any** route with a parameter that can drive its matrix to zero will inflate. That is the same shape as P1's own "the count inflation is near-definitional given an independence default", and the `frac above` column shows the price: P1's magnitude is only reached at `C >= 1.05`, where **no pair at all** is judged to share a source. The stored-tag route's matching endpoint is equally extreme — ancestry binding driven from 0.861 to 0.000. Both routes need their axis pushed to its far end; the comparison is symmetric, and neither should be read as showing the effect arrives easily.

---

## 4. Finding 1 — `dependent` does not eliminate the inflation, on either route

This is the result that changes something already landed.

P1's §1 reported the P2 knob as three numbers per policy, taken at the decay axis's two endpoints:

```text
absent_policy = independent   N_eff 1.117 -> 4.869   inflation +3.753
absent_policy = dependent     N_eff 1.117 -> 1.000   inflation -0.117
absent_policy = soft          N_eff 1.117 -> 5.000   inflation +3.883
```

and concluded, in recommendation 2, that "`dependent` eliminates the inflation." Reading the same policy across the *whole* axis instead of at its ends:

| decay `tau` | stored-tag N_eff, `dependent` | | attribution criterion | attribution N_eff, `dependent` |
|---|---|---|---|---|
| 1e6 | 1.117 | | 0.4896 = C\* | 1.116 |
| 20 | **1.877** | | 0.65 | 1.622 |
| 12 | 1.307 | | 0.70 | **1.753** |
| 9.5 | 1.298 | | 0.75 | 1.359 |
| 8 | 1.139 | | 0.85 | 1.001 |
| 6 | 1.011 | | 0.95 | 1.000 |
| 4 | 1.000 | | 1.05 | 1.000 |
| 2.5 | 1.000 | | 1.20 | 1.000 |

Both curves are **non-monotone**, with a peak in the partial-degradation / moderate-criterion middle:

```text
                     inflation at axis ENDPOINT     inflation at axis MAXIMUM
  stored-tag           -0.117                         +0.760   (tau = 20)
  attribution          -0.116                         +0.637   (C = 0.70)
```

The mechanism is the same on both routes and it is the `unknown_below = 0.25` threshold. The policy fills only pairs it holds *no usable evidence* about. At the axis endpoint every pair has fallen below that threshold, the fill is total, and `N_eff` collapses to exactly 1. In the middle of the axis a substantial band of pairs sits *above* the threshold and keeps its real value, so the fill is partial and a genuine intermediate count survives. On the stored-tag route decay drives all bindings toward zero together; on the attribution route the criterion sweeps a distribution of judgements across the threshold gradually. Different mechanisms, same consequence.

**How this should be stated.** `dependent` attenuates the peak inflation by about 80% (3.753 → 0.760 stored-tag; 3.850 → 0.637 attribution) and moves what remains from the axis's far end into its middle. That is a real and useful reduction. It is not elimination, and a fix adopted on the strength of the endpoint reading would be adopted for a property it does not have — precisely in the partial-ancestry-loss regime that the supplement (§5.4) and Connor Desai 2022 identify as the *empirically loaded* one.

`soft` degenerates to `independent` on both routes (5.000 and 5.000 against 4.869 and 4.966), for the structural reason P1 already gave: once every pairwise entry is below the usable threshold there is nothing left to interpolate a prior from. P1's recommendation 2 — do not adopt `soft` — is unaffected and now holds on a second architecture.

---

## 5. Finding 2 — similarity reaches only one route, and §6's supposition about the other is not realised

§6 states that "P1's *interference* process is content-similarity-driven and therefore partially attribution-like, and its *misbinding* process is similarity-gated", and treats the difference between the routes as one of *when* similarity acts — storage-time versus read-time. A8 measured that, on two-family episodes with two genuinely independent world events sharing a context vector of weight `kappa` drawn orthogonal to the vote direction.

The scorer-side measure is **cross-family confusion** `X`: the mean judged shared-source probability between traces of genuinely different true families. Ground truth enters only to select which pairs to average over, never into the judgement.

| `kappa` | attribution `X` | attribution N_eff | stored-tag `X`, no degradation | stored-tag `X`, misbinding | misbinding re-points | of which cross-family |
|---|---|---|---|---|---|---|
| 0.0 | 0.0813 | 2.064 | 0.000000 | 0.000000 | 400 | 0 |
| 0.5 | 0.0840 | 2.059 | 0.000000 | 0.000000 | 402 | 0 |
| 1.0 | 0.0905 | 2.048 | 0.000000 | 0.000000 | 402 | 0 |
| 1.5 | 0.1012 | 2.029 | 0.000000 | 0.000000 | 412 | 0 |
| 2.0 | 0.1163 | 2.002 | 0.000000 | 0.000000 | 407 | 0 |
| 3.0 | 0.1614 | 1.927 | 0.000000 | 0.000000 | 408 | 0 |
| 4.5 | 0.2627 | 1.770 | 0.000000 | 0.000036 | 403 | 1 |

A7 passes with **rho = 1.000**: the attribution route's cross-family confusion rises monotonically with candidate-source similarity, with storage entirely pristine — Johnson's signature, "misattributions increase as candidate sources resemble each other", reproduced at read time. The count falls correspondingly (2.064 → 1.770 against a true count of 2), i.e. the route *merges* genuinely independent sources as they become confusable. A7b confirms the dial is not smuggling in a vote effect: accuracy range across the whole dial is **0.006**.

**The stored-tag route's cell is 0.000000 everywhere, and the mechanism is measured rather than inferred from the null.** Misbinding fired **2834 re-points across the grid; exactly one crossed a source family** (0.035%). Misbinding re-points an edge to the trace of highest rectified content similarity, and a descendant's siblings — all derived from the same ancestor's content — dominate every cross-family candidate. Raising `kappa` does not help, because siblings inherit the shared context from their common ancestor, so within-family similarity rises alongside cross-family similarity.

**So §6's supposition is not realised here, and the correction runs in §6's own favour.** The two routes do not merely differ in *when* similarity acts; in this harness similarity-driven cross-family source confusion is reachable on the attribution route **only**. Which makes A8 the sharpest discriminator available: it is the one manipulation on which the two routes are not merely differently sensitive but qualitatively different, and unlike A1/A3 neither half of it is structural.

One boundary, so this is not over-read: the stored-tag route's edge set is still *similarity-gated* in the sense §6 means — misbinding fires more often on similar traces, and it demonstrably fires often. What it does not do is produce cross-family confusion. Interference likewise weakens bindings in proportion to similarity, which raises `N_eff` (P1's misbinding axis reaches 4.611) without ever merging two families.

---

## 6. Finding 3 — fluency reaches readout 2 but not readout 3, on the attribution route only

P1-R7 asked whether confidence tracks retrieval events at fixed cardinality and answered no, licensing P1 to attribute its inflation to cardinality. Crossing that axis with route:

| retrieval events | stored-tag N_eff | stored-tag P(ext) | attribution N_eff | attribution conf | attribution P(ext) |
|---|---|---|---|---|---|
| 0 | 1.1166 | 0.0835 | 1.1156 | 0.5909 | 0.0824 |
| 1 | 1.1166 | 0.0835 | 1.1003 | 0.5897 | 0.0707 |
| 2 | 1.1166 | 0.0835 | 1.0964 | 0.5894 | 0.0651 |
| 4 | 1.1166 | 0.0835 | 1.0937 | 0.5892 | 0.0602 |
| 8 | 1.1166 | 0.0835 | 1.0920 | 0.5890 | 0.0568 |
| 16 | 1.1166 | 0.0835 | 1.0910 | 0.5890 | 0.0547 |

The stored-tag column is **exactly** constant — structural, since `retrieval_events` is not an input to `shared_ancestry_prob`. On the attribution route:

- **A9a FAILS**: cardinality moves by −0.025 across sixteen retrieval events, under the predeclared 0.050 threshold and far under P1's 0.2215 count-instrument floor. Fluency does not reach readout 3.
- **A9b PASSES**: source attribution moves by **−33.5% relative** (0.0824 → 0.0547). Fluency does reach readout 2, substantially.
- **P1-R7's own criterion still passes on both routes**: confidence moves 0.5909 → 0.5890, a change of −0.0019, because confidence here is driven by `N_eff` and `N_eff` barely moves.

The direction is as predeclared and is the *protective* one: recorded cognitive operations are diagnostic of internal generation, so a repeatedly-retrieved trace reads as *less* likely to be an external observation and *more* likely to share a lineage. Repeated retrieval makes this architecture more conservative, not less.

**Consequence for the branch.** P1's clearance of the fluency rival is route-specific and readout-specific. On an attribution architecture, an occurrence/source-attribution result that moved with replay count would be **uninterpretable without an in-place control**, because the route makes fluency live on exactly that readout — which is exactly the interpretive problem §5 records the human literature having (Goff & Roediger 1998's monotonic source-attribution dose-response against Sharman 2004's flat-beyond-one-exposure confidence result with a fluency explanation). This arm reproduces that *readout dissociation* inside one architecture: on the attribution route, retrieval count moves source attribution by a third and cardinality by essentially nothing.

---

## 7. Disclosures

**Five defects were found in smoke runs and fixed before the authoritative run**; all five are recorded in full in the arm's `PRE-RUN AMENDMENTS` docstring. Two of them deserve restating here, because they cut in directions that deserve scrutiny.

1. **The criterion grid was truncating the route, so A5 was measuring the grid.** It ended at `C = 0.95`, where the route reached 4.42 and was still rising toward its asymptote of 5. Extended to 1.20. **This makes A5 easier to pass** — same class of fix as P1's own amendment 3 (`READ_NOISE` raised because the arm "had no resolvable range"). The mitigation is that A5's near-definitional character is now stated in the preregistration itself and the `frac above` column is reported alongside, so a reader can see the criterion had to be pushed past the entire judgement distribution.

2. **A6 summarised the two routes asymmetrically** — axis endpoints on the stored-tag route, max-over-grid on the attribution route. Made symmetric (max over each route's own axis). **This makes A6 strictly harder to pass, on both routes**, and it is what produced §4: under the symmetric reading the stored-tag route fails a criterion its own landed result appeared to pass.

3. **A8's premise was wrong and the smoke run reversed it** (§5). It was written from §6 as a prediction that stored-tag cross-family confusion would be positive under misbinding; measured, it is 0.000000. Restated as a two-branch measurement with the re-point fraction reported as the mechanism, rather than left as a prediction that failed.

4. **A9 conflated two readouts** and would have recorded "fluency is not live" when what is true is §6's dissociation. Split into A9a and A9b. A9a's threshold was left unchanged and still fails, as the amendment note predicted.

5. **A claimed orthogonality was false.** The docstring asserted the similarity dial leaves every vote bit-identical. That holds for the two world-event seeds but not their descendants: the `prediction` generator's forward model couples dim 15 into dim 0 — the vote direction — and `retrieved_memory` rescales by `norm(base)`, which `kappa` changes. A7b was added as an explicit control on the realised accuracy range (measured 0.006) rather than leaving a false invariance claim standing.

**Threshold-setting and held-out seeds.** Several thresholds were set with smoke runs on the primary seed pair (17/23) in view. That pair could not be changed — A4's reproduction check requires P1's own seeds. Two further pairs (41/53, 67/71) were therefore run as genuine confirmation, held out from all threshold-setting. **Every criterion returns the same verdict on all three**, and the quantities are stable to three digits (stored-tag `dependent` peak +0.7604 / +0.7675 / +0.7635; attribution A9b −0.3354 / −0.3387 / −0.3374; A5 reach 3.8500 / 3.8502 / 3.8497).

**The aggregation-equivalence gate passed with worst |delta| exactly 0.0** over 240 randomised stores across all three policies.

**P1-R6 is not outstanding and was not done here.** It is already discharged: P1's result note §5 makes the `MECH-544` boundary declaration, records that readouts 1, 2 and 4 all moved, and states that the run must not feed both claim lineages. Nothing in this arm changes that — though §6 above adds one item to it, since readout 2 is a shared readout and this arm shows it is fluency-sensitive on the attribution route.

---

## 8. Recommendations

1. **Restate P1 recommendation 2.** "`dependent` eliminates the inflation" holds only at the decay axis's endpoint. Across the axis it attenuates the peak by ~80% and displaces the residue (+0.760) into the partial-loss regime that the supplement identifies as the empirically loaded one. Recommend the same wording P1 itself used for calibration: report the policy as a curve, not two endpoints.
2. **Report P1's positive result as architecture-independent, with the locus named.** A5 passing means the cardinality inflation is not a property of storing genealogy. It is a property of the readout rule's default for unknown ancestry — which is what P1 found by swapping the default, and what this arm confirms by swapping the entire route that computes the pairwise structure. The branch's engineering rule applies to any architecture with that default.
3. **Do not carry P1-R7's fluency clearance to an attribution architecture.** It is route- and readout-specific (§6). Any assay on an attribution route that reads out source attribution needs its own in-place control; P3-R5's exposure-without-internal-generation arm is the right shape and should be required rather than recommended if P3 is ever run on this route.
4. **A8 is the discriminator worth building on, not A1/A3.** The criterion/storage orthogonality is structural once the two routes are defined. Cross-family confusion under a candidate-similarity dial is not: it separates the routes qualitatively, with storage untouched, and it is the direct synthetic analogue of the Johnson prediction the §6 argument rests on. If one measurement is carried into P3, this is it.
5. **The similarity dial is reusable and cheap.** `build_two_family_episode` gives two genuinely independent sources with a tunable confusability and a verified-invariant vote axis (accuracy range 0.006). P3's psychosis extension is about *elevated baseline source-attribution error* (Mammarella 2010, per verification doc §5) — which is what this dial moves, at fixed storage and fixed evidence.
6. **This arm licenses no clinical or human inference.** It measures two synthetic architectures. Nothing here bears on which route the human effect runs on; Johnson 1993 motivated the design and is untouched by the result.

---

## 9. Epistemic boundary

- Nothing here is evidence about psychosis, and nothing here is claim evidence. Synthetic architectures only; the literature constrains the assay, the assay licenses no clinical claim.
- **Two of the four discriminator cells are structural.** A1 and A3 had to come out as they did; they are implementation checks. A5's pass is near-definitional given the shared aggregation, and is reported as such rather than as a discovery. The empirical content is A4, A6, A7, A8 and A9.
- **A8's negative is a negative about this harness, not about stored-tag architectures in general.** A representation whose degradation could re-point across source families would behave differently; this one, measured, does not (1 cross-family re-point in 2834).
- Accuracy being exactly 0.6990 in every cell of both routes is enforced by construction, not discovered — as in P1.
- The attribution route is *an* implementation of Johnson's account, not *the* one. Its feature weights, its criterion form and its restriction of candidate sources to temporally preceding traces are all choices; other choices would give other numbers. What is robust across the three seed pairs is the *pattern*, not the constants.
- P1's landed results are unchanged and were reproduced here to their published digits. Finding 1 is a correction to the two-point **summary** of P1's P2 sub-measurement, not to any number P1 reported.
