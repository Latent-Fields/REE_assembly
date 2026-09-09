# Convergence Signal Synthetic Assay 001 — Result

**Date:** 2026-09-09  
**Status:** synthetic measurement result; no claim promotion, no creature code change, no queue mutation  
**Preregistration:** `evidence/planning/convergence_signal_synthetic_assay_001.md`  
**Driver:** `scripts/convergence_signal_synthetic_assay_001.py`  
**Banked run:** `evidence/experiments/convergence_signal_synthetic_assay_001/runs/20260909_seed7/manifest.json`

## Executive result

The first falsifier **passes all four preregistered measurement criteria**.

The assay was designed to distinguish two observationally identical unanimous vote patterns:

- five genuinely independent 70%-reliable evaluators;
- five copies of one 70%-reliable evaluator.

The independence-aware observable assigns:

- independent unanimity: **0.98588** confidence;
- copied unanimity: **0.70168** confidence;

for a preregistered confidence gap of **0.28420** (criterion required >= 0.15).

By contrast, the reliability-only baseline assigns essentially the same confidence to both:

- independent unanimity: **0.98588**;
- copied unanimity: **0.98625**;

endpoint delta **0.00037**.

Thus the assay demonstrates the narrow point it was built to test:

> **marginal evaluator reliability plus vote count is insufficient when evidence routes differ in dependence, and a cheap dependence-aware correction can recover useful second-order information.**

This is a measurement result, not yet a REE architecture result.

---

## Registered criteria

### C1 — duplicated evidence discrimination: PASS

Required: independent-vs-copy unanimity confidence gap >= 0.15.

Observed: **0.28420**.

### C2 — dependency ordering: PASS

Predicted independence-aware unanimity confidence:

```text
independent  0.98588
mixed        0.90979
shared_bias  0.75493
copies       0.70168
```

This preserves the preregistered ordering:

```text
independent > mixed > shared_bias > copies
```

### C3 — endpoint calibration: PASS

Independent endpoint:

- predicted confidence: 0.98588
- observed unanimity accuracy: 0.98684
- absolute error: **0.00096**

Copies endpoint:

- predicted confidence: 0.70168
- observed unanimity accuracy: 0.70029
- absolute error: **0.00139**

Both are well inside the preregistered <= 0.03 bound.

### C4 — reliability-only insufficiency visible: PASS

The reliability-only model gives the independent and copied unanimous states nearly identical confidence despite radically different observed accuracy.

Observed endpoint confidence delta: **0.00037**, inside the <= 0.02 criterion.

---

## Important intermediate-regime imperfection

The simple effective-source correction is not perfectly calibrated away from the endpoints.

### Shared-bias regime

- predicted independence-aware unanimity confidence: **0.75493**
- observed unanimity accuracy: **0.71647**
- error: about **+0.03846** (over-confident)

### Mixed regime

- predicted independence-aware unanimity confidence: **0.90979**
- observed unanimity accuracy: **0.93717**
- error: about **-0.02737** (under-confident)

This matters.

The result supports the **existence and measurability of dependency-sensitive evidential structure**, but it does not validate the current `N_eff` heuristic as a generally calibrated confidence model.

A richer dependency model may need to preserve cluster topology rather than compress all dependence into one mean pairwise-correlation scalar.

That is precisely the kind of result the synthetic stage is meant to expose before anything reaches REE action authority.

---

## What this result does establish

It establishes, in the frozen synthetic setup:

1. five reasons and one reason repeated five times are not epistemically equivalent;
2. a reliability-only combiner is blind to that distinction when marginal reliabilities are matched;
3. a cheap calibration-split dependency estimate can recover the distinction without test-label access;
4. the intended ordering across independent, mixed, shared-bias and copied regimes is measurable;
5. the first candidate heuristic is good at the clean endpoints but imperfect in intermediate topologies.

## What it does not establish

It does **not** establish that:

- REE needs a new convergence module;
- the proposed observable beats exact Bayesian inference;
- pairwise residual correlation is the right biological or architectural representation of dependence;
- heterogeneous REE evaluators will have dependencies that can be estimated this cleanly;
- convergence should directly affect action selection;
- structured divergence improves information-hunger allocation;
- the Aha hypothesis is correct.

No claim should be promoted from this run alone.

---

## Immediate next discriminator

The next assay should be the **Bayes-ceiling / rich-topology extension**.

It should compare:

1. exact Bayesian aggregation with the true joint dependency model;
2. reliability-only aggregation;
3. the current mean-correlation `N_eff` heuristic;
4. a cluster/provenance-aware but still cheap approximation.

Required environments should include:

- exact copies;
- one shared latent-error cluster;
- two independent clusters;
- mixed cluster + independent specialists;
- one high-reliability minority expert;
- distribution shift where historical error correlations change.

The convergence heuristic is **not expected to beat exact Bayes**. It earns a REE role only if a cheap topology-aware representation approaches the useful decisions/confidence of exact inference while requiring materially less model structure or compute and degrading gracefully when dependence estimates are imperfect.

Only after that should the programme proceed to the opposite-sign test: whether **structured divergence** is a useful cheap selector for information-seeking beyond raw uncertainty and ordinary expected information gain.

---

## Bottom line

The first measurement question survives.

> **The architecture should not count agreement without asking how many genuinely different routes produced it.**

But the run also gives an early warning against reducing this to a single `effective number of voters` scalar. The topology of dependence may itself be part of the information.
