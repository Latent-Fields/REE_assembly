# Provenance probe P0 — result: the genealogy endogeneity gate

**Date:** 2026-09-10
**Probe:** [`scripts/provenance_genealogy_probe_p0.py`](../../scripts/provenance_genealogy_probe_p0.py)
**Gates:** provenance **P1** generated-ancestry harness, per [`provenance_harness_generated_ancestry_design.md`](provenance_harness_generated_ancestry_design.md) §9.3 (REE_assembly `f2869ac00e`)
**Designs against:** [`provenance_false_evidence_multiplication_campaign_supplement_20260910.md`](provenance_false_evidence_multiplication_campaign_supplement_20260910.md) §§4, 7
**Chip:** `chip-20260910-provenance-probe-p0`
**Status:** synthetic probe run only. No claim registered or promoted, no queue entry, no edit to the design note, the ladder or the supplement. Recommendations below are recommendations, not changes.

---

## 1. Verdict, up front

**The decisive gate passed. Build P1 — with two specified fixes that are cheaper than the probe was.**

| Sweep | Preregistered verdict | What it means |
|---|---|---|
| **(b) ENDOGENEITY** | **PASS** (all three processes, all three discriminative controls) | Ancestry loss in a harness of this class **can be generated, not merely stipulated**. Design-note falsifier 1 and supplement falsifier 2 **do not fire**. This is the whole reason the probe exists. |
| **(a) NON-DEGENERACY** | **FAIL**, on one clause of one criterion (A1) | The decay axis did not produce `SOFT` and `ABSENT` as simultaneously-populated **episode-level** regimes on the preregistered `tau` grid. A2, A3 and A4 all passed. |
| Preregistered conjunction `verdict_build_P1` | **False** | Reported faithfully; it is `(a) AND (b)`. The reasoned verdict below is not a substitute for it. |

The A1 failure is **not** a failure of the decay process family. Post-hoc work reported in §5, and fully disclosed as post-hoc, locates it precisely: episode-level `SOFT` is the min over ~10 edges and therefore an extremely steep function of the per-edge `ABSENT` rate, so the whole episode-level transition is compressed into `tau ∈ [10, 8.5]` — a window the preregistered grid stepped straight over (12 → 8). On a finer grid the decay axis reaches `SOFT` 0.627 / `ABSENT` 0.372 at `tau = 9.5`, i.e. it clears the 0.10 coexistence threshold by more than 3x.

Design note §9.3 already prescribes the disposition for exactly this pattern — "if (a) fails but (b) passes, the process families need reworking before P1, not abandonment" — and the diagnosis narrows it further: **the processes need no rework at all; the classifier's aggregation rule and the knob-grid selection method do.**

Stated in the work-graph debt vocabulary: the question the design note classed `complex (probe-gated)` has been probed and resolves to `complicated (buildable)`. What remains at the P1 boundary is execution, not discovery.

---

## 2. What was built, and what was deliberately not

Built (design note §5.1–5.3): the genealogy representation — traces carrying content, a timestamp and a source-family identifier; directed ancestry edges with binding strength in `[0,1]`; a derived source-family partition by thresholding and taking connected components. The three degradation processes (decay, interference, misbinding). The four-way regime classifier.

**Not built, on purpose,** because building any of it would defeat the point of gating: no descendant content generators (§4.2's four kinds), no confidence computation, no posterior over `H`, no `N_eff` readout, no calibration against world truth, no replay loop, none of §6's eight contract operations. Trace content exists only as a unit vector supporting a cosine metric, because interference and misbinding need something to act on.

**The endogeneity criterion is enforced structurally rather than by discipline.** `GroundTruth` (true ancestor, true family) is a separate object passed **only** to the scorer. `GenealogyStore` carries content, timestamps, the current edge set and explicit family assignments, and nothing else; every process function's signature is `(store, knob, rng, ...)`. §3's criteria 1 and 3 are therefore properties of the type signatures, not promises. The store's edges are *initialised* to the true ancestry — the architecture starts veridical — and diverge under the dynamics, which is what makes reading them a measurement rather than a copy.

**Size:** 876 lines against the §9.4 estimate of 150–250. The overrun is almost entirely the three discriminative-validity comparators of §4 below, which §9.3 did not specify and which turned out to carry the result.

---

## 3. Preregistered criteria

Declared in the script's module docstring **before any execution**, and unchanged thereafter. Knob grids and every threshold (0.15 / 0.10 / 0.30 / 0.80 / 0.01) were fixed in the same commit as the criteria. Two implementation defects were fixed after smoke runs; §6 records both, with pre-adjustment numbers.

**Sweep (a), non-degeneracy.** A1: the decay axis populates `SOFT` ≥ 0.15 at some `tau`, `ABSENT` ≥ 0.15 at some `tau`, and `SOFT` ≥ 0.10 **and** `ABSENT` ≥ 0.10 simultaneously at some `tau`. A2: the same three clauses for interference. A3: misbinding produces `FALSE_SPLIT` ≥ 0.15 at some rate. A4: `VERIDICAL` ≥ 0.80 at the null end of all three grids. Passes iff all four hold.

**Sweep (b), endogeneity.** Knob selection rule, declared in advance: the grid value whose mean degraded-edge fraction is closest to 0.50. B1: with the store **held fixed** and only the dynamics seed varying, mean pairwise Jaccard **distance** between degraded-edge sets ≥ 0.10. B2: mean per-store Spearman rho between each edge's degradation **propensity** and that process's content/timing statistic ≥ 0.30, with ≥ 0.80 of stores rho > 0 and a within-store permutation p < 0.01. B3, discriminative validity: `stipulation_index` must fail B1 **and** B2; `decay_deterministic` must fail B1; `pure_noise` must fail B2. Passes iff B1 and B2 hold for all three endogenous processes **and** all three B3 clauses hold.

Run: seed 11 authoritative, seeds 23 and 47 as confirmation. 200 episodes per knob value; 40 stores x 30 dynamics seeds; 1000 permutations. 13 s per seed on the Mac.

---

## 4. Sweep (b) — the decisive result

Three seeds, `11 / 23 / 47`:

| Process | Jaccard distance (B1) | mean rho (B2) | stores rho>0 | perm p | B1 | B2 |
|---|---|---|---|---|---|---|
| **decay** | 0.360 0.352 0.343 | +0.927 +0.927 +0.911 | 1.00 1.00 1.00 | 0.001 | PASS | PASS |
| **interference** | 0.168 0.145 0.147 | +0.684 +0.724 +0.664 | 1.00 1.00 1.00 | 0.001 | PASS | PASS |
| **misbinding** | 0.561 0.554 0.571 | +0.686 +0.746 +0.678 | 0.97 1.00 0.95 | 0.001 | PASS | PASS |
| `decay_deterministic` | **0.000 0.000 0.000** | +0.792 +0.788 +0.791 | 1.00 1.00 1.00 | 0.001 | **FAIL** (required) | pass |
| `pure_noise` | 0.780 0.776 0.777 | **+0.006 −0.063 −0.032** | 0.53 0.47 0.40 | 0.472 0.878 0.710 | pass | **FAIL** (required) |
| `stipulation_index` | **0.000 0.000 0.000** | −0.090 −0.070 +0.064 | 0.42 0.50 0.55 | 0.946 0.880 0.119 | **FAIL** (required) | **FAIL** (required) |

**All three endogenous processes pass both clauses; all three comparators fail exactly the clauses they were predeclared to fail.** Seed-to-seed spread is small enough that nothing here is a coin flip.

**The two comparator rows are what make this a result rather than a demonstration.** The criterion is a conjunction, and each comparator shows one conjunct is individually satisfiable by something that is not endogeneity:

- `decay_deterministic` is the same process family with reinstatement noise set to zero. Its degraded set is **strongly** content/timing-determined (rho = +0.79) and **perfectly** seed-invariant (Jaccard distance exactly 0.000). It is stipulation in the sense that matters — you can compute the degraded set from the knob and the store without simulating — and B2 alone would have scored it as endogenous.
- `pure_noise` is exposure-matched noise with no pressure term. It varies richly across seeds (Jaccard 0.78) and carries no structure whatever (rho ≈ 0, p ≈ 0.5–0.9). B1 alone would have scored it as endogenous.
- `stipulation_index` degrades edges chosen by trace index and fails both, as the floor case must.

So the design note's decision to require both conjunctively is load-bearing, and the probe confirms it empirically rather than by argument.

**Answering §3's operational question directly:** at a fixed knob, which edges degrade is *not* predictable from the knob alone. For decay it is predicted by edge age (rho +0.93), for interference by the descendant's similarity to other traces (+0.68), for misbinding by similarity to the nearest competitor (+0.69) — every one of them a property of the realised store, none of them an ancestry-indexed argument. **Break A's route is open.**

---

## 5. Sweep (a) — what failed, and why it is not what it looks like

Seed 11, 200 episodes per knob. Episode-level as §5.3 specifies; edge-level reported as a diagnostic.

**decay** (knob = `tau`, large = slow):

| tau | ep V | ep S | ep A | ep F | edge S | edge A |
|---|---|---|---|---|---|---|
| 1e6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 20 | 0.025 | 0.975 | 0.000 | 0.000 | 0.359 | 0.000 |
| 12 | 0.000 | 1.000 | 0.000 | 0.000 | 0.807 | 0.000 |
| **8** | 0.000 | **0.060** | **0.940** | 0.000 | **0.738** | **0.247** |
| 5 | 0.000 | 0.000 | 1.000 | 0.000 | 0.278 | 0.722 |
| 1.5 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 | 1.000 |

**interference** passes the same clauses: at gain 0.45, episode `SOFT` 0.540 / `ABSENT` 0.450. **misbinding** reaches `FALSE_SPLIT` 0.995. **A4** holds exactly: `VERIDICAL` = 1.000 at all three null ends.

A1's third clause fails at 0.060 / 0.065 / 0.070 across the three seeds against a 0.10 threshold — consistently, narrowly, and reproducibly.

**A rejected explanation, reported because it was tested and was wrong.** The obvious diagnosis is that decay pressure is more uniform *within* an episode than interference pressure, so all of an episode's edges move together. The within-episode coefficient of variation does differ in that direction (age 0.303 vs similarity 0.405, a 1.34x ratio), but the prediction it makes is false: widening the within-episode age spread (`t_max` 8 → 20, `steps` 12 → 24) made episode-level coexistence **worse**, 0.015 versus 0.060. The explanation is discarded.

**The actual cause, and it is arithmetic.** An episode is `SOFT` only if *every* one of its ~10 edges stays above `theta_low`, so episode `SOFT` ≈ `(1 − p_absent_edge)^n_edges`. Measured against a finer post-hoc `tau` grid, that identity is near-exact — predicted 1.000 / 0.866 / 0.623 / 0.369 / 0.168 / 0.061 against observed 1.000 / 0.865 / 0.627 / 0.360 / 0.155 / 0.062. A tenth power compresses the entire episode-level transition into a narrow knob window:

| tau | 12 | 11 | 10.5 | **10** | **9.5** | **9** | 8.5 | 8 |
|---|---|---|---|---|---|---|---|---|
| ep `SOFT` | 1.000 | 0.993 | 0.978 | 0.865 | **0.627** | **0.360** | 0.155 | 0.062 |
| ep `ABSENT` | 0.000 | 0.007 | 0.022 | 0.135 | **0.372** | **0.640** | 0.845 | 0.938 |

At `tau = 9.5` coexistence is **0.372**, more than 3x the threshold. The preregistered grid's adjacent points were 12 and 8; there was no sample inside the window. **A1 failed on grid resolution, not on process behaviour** — and the same arithmetic explains why interference passed: its grid happened to place a point where the per-edge `ABSENT` rate was ~7.6%, landing mid-transition by luck rather than design.

**A structural finding that is not empirical and should not be recorded as one.** Decay and interference produce `FALSE_SPLIT` in **0.000** of episodes at every knob value on every seed — but this is true *by construction of the representation*, not as a contingent result. The architecture's confident edges initially point only at true ancestors; a loss process can lower a strength but can neither raise a strength on an edge to a foreign trace nor assert a fresh family identifier. So §5.4's "losing a link cannot manufacture a positive belief in independence" is definitional given §5.1, whereas its other half — that the decay axis yields `SOFT` and `ABSENT` as distinct populated regimes — is a genuine empirical question, and one this probe answers affirmatively. The design note presents both halves as a single prediction; they are of different kinds. Misbinding, conversely, produces a little `ABSENT` (0.01–0.10) via re-points *within* the true family, which delete a true edge without creating a wrong confident component, and essentially no `SOFT` (0.000), because it never touches binding strengths.

---

## 6. Adjustments made after seeing numbers — disclosed in full

Two implementation defects were found and fixed after smoke runs, both **before** the authoritative run and neither touching a criterion, threshold or knob grid.

**(i) Reinstatement noise was acting as a second degradation process.** Originally applied as `w *= exp(−pressure + eta·z)`. Because `w` has a reflecting ceiling at 1.0, that walk drifts downward regardless of pressure, so the null ends of the grids were already degraded: at `tau = 1e6` — decay entirely off — the first smoke run gave `VERIDICAL` 0.05, `SOFT` 0.35, `ABSENT` 0.60, and criterion A4 could not have been met by any parameterisation. Changed to scale the pressure, `pressure ← max(pressure·(1 + eta·z), 0)`, so the noise perturbs how much a retrieval costs a binding and vanishes when there is no pressure. Null ends went to `VERIDICAL` 1.000.

**(ii) The `pure_noise` comparator was not exposure-matched, and therefore was not a negative control.** The endogenous processes act on an edge only once its descendant exists, so an older edge accumulates more applications. A noise comparator gated the same way inherits an age correlation for that reason alone: it passed B2 with rho = **+0.830**, which would have failed the required B3c clause and, worse, would have made B2 look satisfiable by structureless noise. Fixed by applying the noise to every edge on every step. Post-fix rho = +0.006.

**Neither adjustment moved the decisive result, and the direction was already visible pre-adjustment.** Decay, interference and misbinding passed B1 in the very first smoke run. What the fixes changed was whether the *comparators* discriminated — that is, whether sweep (b) was a test at all. This is worth stating plainly because it is the disclosure that matters: the fixes made the criterion **harder** to pass, not easier.

The authoritative configuration was run once, at the preregistered criteria, and is reported above whichever way it came out.

---

## 7. Recommendations to P1 — recorded here, not applied

The design note, the ladder and the supplement were not edited. These are recommendations.

1. **Select knob grids by per-edge degradation rate, not a priori.** A grid chosen on the knob scale can step over the entire episode-level transition, as the `tau` grid did here. Calibrate each axis so that sample points span per-edge `ABSENT` rates of roughly 1–30%; that is where the episode-level regimes live.
2. **Make edge-level stratification the primary readout, with episode-level secondary.** §5.3 defines the four conditions per episode, and the `min`-over-edges rule turns a graded edge-level population into a near-binary episode-level one. P1's stratified table is meant to be comparable to Yousif 2019's stipulated contrast; an aggregation that suppresses `SOFT`/`ABSENT` coexistence at episode level will make that comparison misleading. Report both, and say which is which.
3. **Carry exposure-matching as an explicit design requirement.** Defect (ii) is the general trap, not a quirk of this probe: any statistic that correlates with how long a trace has been in the store will correlate with degradation for reasons that have nothing to do with content. This is the same discipline as supplement P3-R3's "match retrieval quality before attributing an interaction to ancestry", and it should be stated once in P1's design rather than rediscovered per readout.
4. **Split §5.4 into its two kinds.** "Decay produces `SOFT`/`ABSENT`" is empirical and now supported. "Decay does not produce `FALSE_SPLIT`" is definitional given the §5.1 representation. Recording the second as an empirical finding would over-credit the design; recording it as an entailment makes visible that a `FALSE_SPLIT` under a loss process would indicate a representation bug, not a discovery.
5. **Keep the three discriminative comparators in P1.** They cost little, they are already written, and `decay_deterministic` in particular is the cheapest available continuous check that P1 has not quietly drifted back into stipulation as it grows. `decay_deterministic` passing B2 while failing B1 is exactly the failure mode a maturing harness would slide into.
6. **The probe's store is a usable base for the §6 contract.** The state layer here — store, edges, partition, three processes, classifier — is what §6's operations 1–3 need, and it was written against §5.1 rather than against P1's convenience. Growing it is cheaper than rebuilding it; adding a descendant generator to it is the boundary that turns P0 into P1 and should be a deliberate step.

---

## 8. Epistemic boundary

- Nothing here is evidence about psychosis, and nothing here is claim evidence. This is a synthetic probe of whether a harness can be built, not a measurement of anything the harness would measure. It is not banked as an evidence run-pack.
- The probe measures **no** confidence, **no** effective source count and **no** calibration, by design. It therefore says nothing whatever about whether corrupted ancestry inflates confidence — that is P1's question, and P0's only contribution is that the question is askable by construction rather than by stipulation.
- Trace content is a placeholder geometry. It is not one of §4.2's four descendant kinds and carries no claim about how descendants are actually produced. §4.3's judgement that the ambiguous-perception kind carries the design is untouched by anything here.
- The human results (Yousif 2019 PMID 31291546, Connor Desai 2022 PMID 35149359, Weaver 2007 PMID 17484607) remain what P1 must not merely reproduce. This probe shows the route past them is open; it does not walk it.
