# Provenance P1 — result: generated-ancestry false-independence assay

**Date:** 2026-09-10
**Harness:** [`scripts/provenance_genealogy_harness.py`](../../scripts/provenance_genealogy_harness.py) (the design note §6 contract)
**Driver:** [`scripts/provenance_p1_false_independence_assay.py`](../../scripts/provenance_p1_false_independence_assay.py)
**Designs against:** [`provenance_harness_generated_ancestry_design.md`](provenance_harness_generated_ancestry_design.md), plus §7 of [`provenance_branch_hippocampal_audit_verification_20260910.md`](provenance_branch_hippocampal_audit_verification_20260910.md)
**Gated by:** [`provenance_genealogy_probe_p0_result.md`](provenance_genealogy_probe_p0_result.md) (REE_assembly `b81f9764bc`)
**Status:** synthetic assay run only. No claim registered or promoted, no queue entry, no edit to the design note, the ladder or the supplement.

---

## 1. Verdict, up front

**Every preregistered criterion passes, on all three seed-pairs. But the headline is not the one the ladder was expecting, and the useful result is the sub-measurement.**

| | Result |
|---|---|
| MAIN dose-response (M1–M4) | **PASS** — count inflates, calibration crosses into overconfidence, accuracy is *exactly* flat |
| P1-R2 adaptive linking | **PASS** |
| P1-R3 legitimate computation | **PASS** — the decomposition is realisable; supplement falsifier 5 does **not** fire |
| P1-R4 independent new observation | **PASS** |
| P1-R7 fluency vs cardinality | **PASS** — fluency is **not** live; the inflation *is* attributable to cardinality |
| C1 content-fixed | **PASS** (hard assertion) |
| Instrument-calibration floor (§8.2) | cleared by **15.8x** |

**The finding that matters is P2, not H1.** "Ancestry loss inflates the effective-source count" is close to definitional once the readout treats unbound traces as separate sources — and this run shows exactly that, by changing the readout and watching the effect disappear:

```text
absent_policy = independent   N_eff 1.117 -> 4.869   inflation +3.753   signed error -0.108 -> +0.099
absent_policy = dependent     N_eff 1.117 -> 1.000   inflation -0.117   signed error -0.108 -> -0.117
absent_policy = soft          N_eff 1.117 -> 5.000   inflation +3.883   signed error -0.108 -> +0.103
```

So the confidence inflation is **not forced by ancestry loss**. It is forced by the readout rule's *default for unknown ancestry*, and swapping that default eliminates it completely. The locus of the phenomenon is the default, not the corruption — which is precisely why the supplement (§9) promoted P2, and it is the one result here that is not near-definitional.

The `soft` default is worth its own line, because it is the obvious fix and it **does not work**: once every binding has fallen below the usable threshold there is nothing left to interpolate a prior from, so it degenerates to `independent` exactly in the regime where it was supposed to help. That is structural, not a tuning failure.

---

## 2. What was built

`provenance_genealogy_harness.py` (726 lines) implements the §6 eight-operation contract; `provenance_p1_false_independence_assay.py` (764 lines) is the driver. Endogeneity is enforced by type signature, not discipline: `GroundTruth` (true ancestry, true family, per-descendant `alpha`, `H`) is passed only to scorer operations, `GenealogyStore` carries no ground truth, and `degrade()` has no argument that could name an ancestry edge.

Three design decisions are load-bearing enough to state:

**Ancestry and association are separate edge sets.** Only ancestry feeds the count. With one edge set, P1-R2 could not pass by construction: linking two descendants of different world events would raise the pairwise dependency term and drive the count *down* — the "collapses distinct sources" failure the control exists to detect. Keeping them apart is what makes the control's correct outcome reachable at all.

**Initial binding strength is derived from content, not set to 1.0.** How tightly a descendant binds to its ancestor is how well the ancestor's stored content explains it (rectified cosine). This is inference-path legal, and without it the count readout has no dynamic range across the `alpha` dial — an `alpha = 0` descendant (a genuinely independent observation) would bind as tightly as a pure replay, `N_eff` would sit at 1 across the whole dial, and P1-R4 would be unpassable.

**P1-R5 route, predeclared before running:** this is the **stored-tag** architecture. Source structure lives in persistent ancestry edges that the dynamics degrade, and `source_attribution` reads that stored structure at retrieval. It does not reconstruct source structure at retrieval from a shiftable criterion. Every result here is a result about the stored-tag route only.

---

## 3. MAIN dose-response

2000 episodes per knob, `p_est = 0.6459`, content seed 17 / dynamics seed 23.

| decay `tau` | N_eff | confidence | accuracy | signed err | P(external) | assoc | edge V/S/A/F |
|---|---|---|---|---|---|---|---|
| 1e6 | 1.117 | 0.591 | 0.699 | −0.108 | 0.084 | 0.861 | 1.00/0/0/0 |
| 20 | 1.966 | 0.653 | 0.699 | −0.046 | 0.457 | 0.273 | .13/.87/0/0 |
| 12 | 2.589 | 0.693 | 0.699 | **−0.006** | 0.615 | 0.127 | 0/1.00/0/0 |
| 9.5 | 2.975 | 0.715 | 0.699 | +0.016 | 0.693 | 0.077 | 0/.87/.13/0 |
| 8 | 3.288 | 0.731 | 0.699 | +0.033 | 0.749 | 0.049 | 0/.46/.54/0 |
| 6 | 3.825 | 0.757 | 0.699 | +0.058 | 0.835 | 0.019 | 0/.04/.96/0 |
| 4 | 4.463 | 0.783 | 0.699 | +0.084 | 0.928 | 0.003 | 0/0/1.00/0 |
| 2.5 | 4.869 | 0.798 | 0.699 | +0.099 | 0.983 | 0.000 | 0/0/1.00/0 |

The misbinding axis is the same story through a different regime: `N_eff` 1.117 → 4.611, confidence 0.591 → 0.787, signed error −0.108 → +0.088, with the edge population moving into `FALSE_SPLIT` (0 → 0.94) rather than `ABSENT`.

**Accuracy is exactly 0.699 at every knob on both axes** — one distinct value across sixteen conditions. That is the content-fixed enforcement (§4.4) working as specified: identical content means identical votes means identical beliefs, so only the genealogy differs. It is a design property, not a finding, but it is the property that makes the confidence movement interpretable.

**Calibration is monotone in sign and U-shaped in magnitude, and the second half is easy to miss.** Signed error rises monotonically, which is what M3 tests. But the architecture is *under*-confident when ancestry is intact (−0.108), best calibrated at **moderate** ancestry loss (−0.006 at `tau = 12`, deep in the `SOFT` regime), and only over-confident once loss is heavy. Mild ancestry corruption **improves** calibration here. An endpoint-only report would say "ancestry loss degrades calibration" and miss that the path runs through a minimum.

### Stratified by dominant edge regime

Edge-level stratification is primary here, per P0's recommendation 2 — the episode-level classifier scores an episode by its worst surviving edge, which compresses the transition into a narrow knob window.

| regime | n | N_eff | confidence | accuracy | signed err |
|---|---|---|---|---|---|
| VERIDICAL | 12226 | 1.520 | 0.619 | 0.700 | −0.081 |
| SOFT | 7245 | 2.650 | 0.695 | 0.698 | −0.003 |
| ABSENT | 6827 | 4.234 | 0.772 | 0.699 | **+0.073** |
| FALSE_SPLIT | 5702 | 4.072 | 0.764 | 0.697 | **+0.066** |

**No divergence from the human pattern.** Design note §5.4 consequence 2 required that inflation appearing *only* under `FALSE_SPLIT` be reported as divergence. It does not: `ABSENT` and `FALSE_SPLIT` are nearly identical in both count (4.23 vs 4.07) and calibration (+0.073 vs +0.066), and `SOFT` already carries most of the movement. The empirically loaded regimes — the ambiguity Connor Desai 2022 locates the human effect under — are where the effect lives here too.

### Instrument-calibration floor (§8.2)

The count instrument's own signed error, measured against known topology in the same run, on the undegraded `alpha` dial: worst |error| = **0.2215** (at `alpha = 0.4`). The measured inflation is **3.494** on the weaker of the two axes — clearing the floor by **15.8x**. The result is interpretable; had it been the other way, §8.2 requires reporting it as uninterpretable rather than as a null or a positive.

---

## 4. The controls

**P1-R3 — legitimate computation (the one that decides whether the hypothesis is testable).** The §7.2 decomposition is realisable under one unmodified rule:

```text
legitimate arm   confidence +0.0845   N_eff exactly 1.000   signed-error delta -0.0010
corrupted arm    confidence +0.1922   N_eff       +3.346    signed-error delta +0.1922
```

Both arms' confidence rises — which is the requirement that makes the contrast non-trivial — and only one of them is entitled to. Legitimate computation raised `p` by averaging read noise over a fixed observation set and its accuracy rose with it; false independence raised `N_eff` while `p`, the votes and the accuracy were untouched. **Supplement falsifier 5 does not fire.**

**P1-R7 — fluency versus cardinality (mandatory).** Three arms:

```text
in_place        retrieval events 0 -> 16, cardinality FIXED 5 -> 5, VERIDICAL rate 1.00
                delta confidence  -0.0013                                 <- fluency NOT live
spawn_bound     cardinality 5 -> 21 with ancestry INTACT, N_eff 1.117 -> 1.145
                delta confidence  -0.0103                                 <- correct discounting
spawn_degraded  cardinality rises AND ancestry degraded, N_eff 2.974 -> 7.630
                delta confidence  +0.1280                                 <- dynamic-range control
```

Confidence does not track retrieval events at fixed cardinality, and the positive control confirms the measurement has range. **The main inflation is therefore attributable to cardinality**, which is the condition §7.5 sets on reporting it as a P1 result at all.

`spawn_bound` is a secondary result worth its own sentence: sixteen replays with ancestry intact move the count by 0.028 and confidence by −0.010. The architecture correctly refuses to treat replays of one event as sixteen sources — the E43 behaviour, arrived at without being asked for.

**P1-R2 — adaptive linking.** Association rises by 1.000 over baseline while `N_eff` after linking is 2.071 (target 2, tolerance 0.30). The collapse failure direction (`N_eff < 1.70`) does not fire. Readout 1 moves with readout 3 flat, which §8.1 names as the E43 signature.

**P1-R4 — independent new observation.** `N_eff` tracks the derived ground-truth count across the `alpha` dial with rho = 1.000, confidence rises by 0.041, and calibration is preserved (signed error −0.117 at `alpha = 1` to −0.085 at `alpha = 0`). The count readout has dynamic range in the correct direction, without which a null under corruption would be uninterpretable.

**C1 — content fixed.** Hard assertion: content hashes bit-identical across ancestry conditions, and `degrade()` verified not to mutate content.

---

## 5. P1-R6 boundary declaration

Readouts 1, 2 and 4 all move here: association 0.861 → 0.000, P(external) 0.084 → 0.983, calibration −0.108 → +0.099. Per P1-R6 those three alone are **`MECH-544`'s territory**; P1's distinctive product is readout 3, the cardinality variable. Readout 3 does move (1.117 → 4.869), so this is a P1 result — but the other three moving means **the same run is also consistent with `MECH-544`, and the two claims must not both be fed from it.** Recording the boundary here is the whole point of R6.

---

## 6. Disclosures

**Four defects found in smoke runs and fixed before the authoritative run** (full detail in the driver's `PRE-RUN AMENDMENTS` docstring). None changed a threshold or a knob grid, and two were making criteria *fail* — the direction that deserves most scrutiny:

1. `spearman` did not average tied ranks, so a **constant** series scored rho = 1.00 against any monotone x. The perfectly flat accuracy curve was being read as perfectly rising, and M2 failed on it.
2. M2's accuracy clause was preregistered as a rank correlation, which is undefined on a constant series; with (1) fixed it returns `nan` and `nan <= 0.30` is False, so the clause would fail on the *ideal* outcome. Now evaluated on a flatness test; the literal preregistered `rho_accuracy` is still computed and reported.
3. P1-R3 estimated `p` over the wrong population, so the arm measured the estimator rather than the architecture; and `READ_NOISE` was raised 0.9 → 2.0 because at 0.9 the legitimate effect (p 0.718 → 0.747) was **smaller than the standard error of `p_est` itself** and the arm had no resolvable range (measured rise: exactly 0.000).
4. P1-R7's positive control required confidence to rise as replay cardinality rose — but a *correct* architecture must discount bound replays, so the control was unpassable by construction. Replaced with the three-arm design above.

**One defect found after the authoritative run:** `absent_policy` fired only on *exactly* zero shared-ancestry probability, but decay approaches zero asymptotically without reaching it, so the knob was **inert** — all three policies returned identical inflation (+3.753). Now thresholded at the classifier's own uncertain-band floor. This affected only the P2 sub-measurement of §1; every preregistered criterion uses the `independent` policy, whose code path is untouched, and all headline numbers were re-run after the fix.

**Built against a concurrent amendment that was uncommitted at build time — since reconciled.** When P1-R7 was implemented, it existed only in another session's (`jolly-neumann-a8857e`) working-tree edit of the design note: not in `HEAD`, not on `origin`. I built the mandatory arm from that in-flight text anyway, on the grounds that omitting a mandatory rival-hypothesis control is worse than building against wording that might still change. That amendment has since landed as `b2f569f84f`, and the committed §7.5 is **byte-identical** to the text this assay was built against — verified by diff, not assumed. The debt is discharged; no reconciliation is outstanding.

**The design-note amendment I was asked to make was not made.** `jolly-neumann-a8857e` holds the claim on that file (opened 19:22:45Z, "provenance tranche fold-in") and `task_claim.py` arbitration named me not-owner. P0's §7 recommendations 1–4 are already durable on origin at `b81f9764bc` for that session to fold in.

---

## 7. Recommendations

1. **Report P2 as the primary result of this branch, not H1.** The count inflation is near-definitional given an independence default; the finding with content is that the default is the locus and is changeable. §1's three-policy table is the result.
2. **Do not adopt the `soft` default as the fix.** It degenerates to `independent` exactly where it is needed, for a structural reason. If a fix is wanted, `dependent` eliminates the inflation — at the cost of leaving the architecture under-confident everywhere (signed error −0.117 at both ends), which is its own miscalibration.
3. **Report calibration as a curve, not two endpoints.** |signed error| is U-shaped with a minimum inside the `SOFT` regime; mild ancestry loss improves calibration here.
4. **Carry the P1-R6 boundary into whatever consumes this.** Readouts 1, 2 and 4 all moved, so this run is also consistent with `MECH-544` and must not be counted twice.
5. **P3 can be designed against this harness now.** All eight contract operations are implemented, `degrade` and `replay` are orthogonal as §6 requires, and `replay(mode='in_place')` — which P3's healthy-replay gate needs — is exercised by P1-R7 here.

---

## 8. Epistemic boundary

- Nothing here is evidence about psychosis, and nothing here is claim evidence. This is a synthetic architecture; the clinical literature constrains the assay, the assay licenses no clinical claim.
- Nothing here bears on which mechanism the **human** effect runs on. P1-R7 shows this architecture's confidence does not track retrieval fluency; it says nothing about whether people's does. Weaver 2007 and O'Donnell 2023 are untouched by it.
- The result is about the **stored-tag** route only (P1-R5, predeclared). A read-time-attribution architecture is a different system, not a parameter of this one.
- Accuracy being exactly flat is enforced by construction, not discovered.
- Yousif 2019 (PMID 31291546), Connor Desai 2022 (PMID 35149359) and Weaver 2007 (PMID 17484607) remain what P1 must not merely reproduce. The route past them is the *generated* corruption that P0 gated and this assay exercises — not the inflation number itself.
