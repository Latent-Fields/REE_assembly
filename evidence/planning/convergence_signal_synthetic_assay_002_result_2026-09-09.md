# Convergence Signal Synthetic Assay 002 — Result

**Date:** 2026-09-09  
**Status:** synthetic measurement result; no claim promotion, no creature code change, no queue mutation  
**Preregistration:** `evidence/planning/convergence_signal_synthetic_assay_002_bayes_ceiling.md`  
**Driver:** `scripts/convergence_signal_synthetic_assay_002.py`  
**Banked run:** `evidence/experiments/convergence_signal_synthetic_assay_002/runs/20260909_seed11/manifest.json`

## Executive result

Assay 002 **passes all five preregistered criteria**.

The key finding is narrower than “convergence helps”. It is:

> **When evidence dependence has internal topology, preserving coarse cluster/provenance structure retains useful information that is destroyed by one global dependence scalar.**

The strongest cell is the `MIXED_3_PLUS_2` regime: one correlated three-member cluster plus two independent routes.

Brier score:

```text
M0 reliability-only          0.18594
M1 global N_eff              0.16697
M2 cluster/provenance-aware  0.15227
M3 exact Bayes               0.15073
```

Thus M2 recovers most of the improvement available from the exact joint model while using only coarse cluster membership, marginal reliabilities and calibrated within-cluster correlation.

Exact Bayes remains the best method, as required.

---

## C1 — topology adds information beyond global `N_eff`: PASS

The preregistration required M2 to beat M1 by at least 0.005 mean Brier across the two explicitly multi-topology regimes.

Observed improvements (`M1 - M2`):

```text
TWO_CLUSTERS_3_2  0.00222
MIXED_3_PLUS_2    0.01469
mean              0.00846
```

The first regime shows only a small gain. The second shows a substantial gain.

This asymmetry is informative: **topology matters most when globally averaging correlation confuses a correlated coalition with genuinely independent routes.**

---

## C2 — exact Bayes remains the ceiling: PASS

Across every in-distribution regime, exact joint Bayes is at least as good as M2 within the registered Monte Carlo tolerance.

This is important epistemically. The result is not evidence that a bespoke convergence score discovers information unavailable to probability theory. The useful claim is bounded-resource compression:

```text
full joint dependency model
        ↓ expensive / structurally rich
coarse provenance topology
        ↓ retains much of the useful distinction
one global covariance scalar
        ↓ loses topology
marginal reliability only
        ↓ can count duplicated evidence repeatedly
```

---

## C3 — copied evidence remains correctly discounted: PASS

In `COPIES_5`:

- empirical accuracy: **0.69952**;
- M0 reliability-only confidence: **0.98579**;
- M2 topology-aware confidence: **0.70028**.

So M2 remains calibrated to the fact that five copied observations are effectively one reason, while M0 remains grossly over-confident.

---

## C4 — minority expert protection: PASS, with a useful nuance

The minority-expert regime contains four independent 0.65 generalists and one independent 0.90 specialist.

When the four generalists unanimously oppose the specialist, the pattern occurred on about **3.16%** of trials.

Posterior confidence in the generalist-majority direction:

```text
raw vote fraction  0.80000
M0                 0.56509
M2                 0.56509
exact Bayes        0.56928
```

Thus reliability weighting correctly makes the specialist matter a great deal even though it does not quite overturn four independent generalists in this frozen parameterisation.

M2 does not become more majority-dominated than the reliability baseline.

This is a useful reminder that **independence-aware convergence is not majority rule and should not replace reliability/relevance weighting**.

---

## C5 — dependency shift degrades gracefully: PASS

Calibration occurs at within-cluster sharing `alpha=0.70`; test dependence then shifts to 0.30 or 0.90 without changing marginal competence.

Mean Brier change across correlated regimes, M2 relative to M1:

```text
alpha_test = 0.30:  M2 is worse by 0.00405
alpha_test = 0.90:  M2 is better by 0.00227
```

The preregistered tolerance was 0.005, so both pass.

This is not invariance to dependency drift. M2 uses stale calibration and does become imperfect. It merely avoids catastrophic collapse under the tested shifts.

---

## What Assays 001 and 002 now jointly support

The two synthetic assays establish a compact measurement hierarchy:

1. **vote count is not evidence count**;
2. matched marginal reliability does not resolve duplicated evidence;
3. one global dependence scalar can recover clean endpoints but loses internal dependency structure;
4. coarse provenance/cluster topology can recover materially more of the exact joint answer;
5. exact Bayes remains the normative ceiling;
6. topology-aware aggregation must still coexist with evaluator-specific reliability and protected specialist/veto logic.

The surviving computational object is therefore no longer simply `consensus strength`.

It is closer to:

```text
who supports what
× how reliable each route is here
× which routes share ancestry/error
× which credible routes remain independent
× what structured dissent remains
```

This is the **convergence–divergence geometry** proposed by the child thought.

## What remains unproven

Nothing here yet shows that REE's actual harm, benefit, goal, memory, residue, uncertainty or predictive channels should expose this representation.

The assays do not show that:

- a provenance graph is biologically realistic;
- REE channel dependencies are stable or measurable;
- topology-aware confidence improves organism behaviour;
- convergence should alter commitment;
- divergence identifies useful information-seeking better than existing uncertainty/value-of-information machinery;
- the Aha formulation is correct.

No scientific claim should be promoted from these two synthetic runs alone.

---

## The programme should now flip sign

Continuing to refine consensus estimators would risk overfitting the easy half of the idea.

The next decisive question is the one that motivated the discussion in the first place:

> **When several competent but differently grounded systems disagree about the same unresolved structure, does the topology of that disagreement tell a bounded organism where another observation, experiment or computation is most worth spending?**

The next synthetic assay should therefore compare query allocation by:

1. raw uncertainty;
2. raw committee disagreement;
3. exact expected information gain where calculable;
4. decision-relevant value of information;
5. independence-aware structured disagreement.

It must include an **irreducible-noise trap** so that permanent disagreement is not automatically interpreted as information hunger.

## Bottom line

Assay 002 strengthens the narrow measurement programme while narrowing the architecture claim:

> **Do not merely count independent sources; preserve enough of their dependency topology to know whether apparent consensus contains several reasons, one repeated reason, or a coalition plus genuinely separate support.**

The next test is whether the same representation earns its keep on the opposite side: **where to look when good reasons disagree.**
