# Convergence Signal Synthetic Assay 002 — Bayes Ceiling and Dependency Topology

**Date:** 2026-09-09  
**Status:** preregistered synthetic assay design; no REE claim registration, no creature code change, no experiment-queue mutation  
**Parent result:** `evidence/planning/convergence_signal_synthetic_assay_001_result_2026-09-09.md`  
**Programme:** `evidence/planning/convergence_signal_experiment_ladder.md`

## 1. Purpose

Assay 001 established the narrow measurement fact that matched marginal reliability and matched vote count do **not** imply matched evidential confidence when dependency differs. It also showed that collapsing dependency into one mean-correlation-derived `N_eff` scalar miscalibrates intermediate topologies.

Assay 002 asks the next question:

> **Can a cheap topology/provenance-aware approximation recover materially more of the exact Bayesian answer than reliability-only or one-scalar `N_eff` aggregation, without being given the full joint generative model?**

The topology-aware method is not expected to beat exact Bayes. Exact Bayes is the ceiling.

## 2. Frozen regimes

Binary truth `y ∈ {-1,+1}`. Priors are balanced.

### A — INDEPENDENT_5

Five independent evaluators, each accuracy `p=0.70`.

### B — COPIES_5

One `p=0.70` latent evaluator copied to five observed channels.

### C — SHARED_CLUSTER_5

Five observed evaluators. On each trial, with probability `alpha=0.70`, all five inherit one shared `p=0.70` latent judgement; otherwise all five sample independently at `p=0.70`.

### D — TWO_CLUSTERS_3_2

Two independent latent clusters, sizes 3 and 2. Within each cluster, with probability `alpha=0.70`, members inherit the cluster latent judgement; otherwise they sample independently at `p=0.70`.

The two cluster latent judgements are independent conditional on `y`.

### E — MIXED_3_PLUS_2

One size-3 shared cluster generated as above, plus two fully independent `p=0.70` evaluators.

### F — MINORITY_EXPERT

Four independent generalists at `p=0.65` and one independent specialist at `p=0.90`.

This regime is included to prevent any topology-aware approximation from collapsing into majority rule.

## 3. Distribution-shift leg

Calibration occurs at `alpha_cal=0.70` for correlated regimes.

Held-out shift condition changes the within-cluster sharing probability to:

```text
alpha_test ∈ {0.30, 0.70, 0.90}
```

Marginal individual accuracy remains approximately unchanged. Only dependency changes.

This tests whether a cheap dependency representation degrades gracefully when historical correlation estimates become stale.

## 4. Compared methods

### M0 — RAW / RELIABILITY-ONLY

Treat observed channels as independent and combine their calibrated marginal reliabilities.

This is the baseline that Assay 001 showed is blind to duplicated evidence.

### M1 — MEAN-CORRELATION `N_eff`

The Assay-001 heuristic:

```text
N_eff = N / (1 + (N-1) * rho_bar)
```

and shrink aggregate log-odds by `N_eff/N`.

This is deliberately retained as the one-scalar baseline expected to lose topology.

### M2 — COARSE TOPOLOGY / PROVENANCE

The method receives only:

- evaluator membership in declared provenance clusters;
- calibrated marginal reliability per evaluator;
- one calibrated within-cluster residual-correlation estimate per cluster;
- no trial truth at test time;
- no hidden mixture variable;
- no exact `alpha_test`;
- no full joint likelihood.

For each declared cluster, M2 computes a cluster-level effective-source count from its own within-cluster correlation, then combines cluster contributions plus independent evaluators in log-odds space.

Unlike M1, dependence is retained **per cluster** rather than averaged over the whole ensemble.

### M3 — EXACT JOINT BAYES

Uses the true frozen generative model, including the actual test dependency parameter and evaluator reliabilities, to compute:

```text
P(y | observed vote pattern, regime)
```

This is the normative ceiling, not a competitor the REE heuristic is expected to beat.

## 5. Data splits

Frozen defaults:

```text
seed = 11
calibration trials per regime = 200,000
in-distribution test trials per regime = 200,000
shift test trials per regime per alpha = 200,000
```

Calibration labels may be used to estimate marginal reliability and residual-correlation summaries for M0–M2.

Test labels may only be used for scoring.

## 6. Primary readouts

For each regime/method:

- Brier score;
- log loss;
- expected calibration error (10 equal-width bins, reported descriptively);
- majority/decision accuracy;
- confidence on unanimous patterns;
- confidence on 4:1 patterns;
- absolute confidence gap to exact Bayes.

For distribution shift:

- degradation in Brier/log loss from `alpha_test=0.70` to 0.30 and 0.90;
- whether the ranking M3 <= M2 <= M1/M0 generally survives.

## 7. Preregistered criteria

### C1 — topology adds information beyond one-scalar dependence

Across `TWO_CLUSTERS_3_2` and `MIXED_3_PLUS_2`, M2 must improve mean Brier score over M1 by at least:

```text
0.005 absolute
```

and must not worsen either regime by more than `0.002`.

### C2 — exact Bayes remains ceiling

M3 must have Brier score <= M2 in every in-distribution regime, tolerance `0.001` for Monte Carlo noise.

If M2 appears materially better than exact Bayes, treat that as a bug or scoring mismatch until disproven.

### C3 — duplicate-evidence trap remains solved

In `COPIES_5`, M2 unanimous confidence must be within `0.03` of empirical unanimous accuracy and at least `0.15` lower than M0 unanimous confidence.

### C4 — minority expert protection

In `MINORITY_EXPERT`, for vote patterns where the 0.90 specialist dissents from four 0.65 generalists, M2 must move posterior confidence toward the specialist relative to unweighted majority and must not become *more* majority-dominated than M0.

This is a qualitative-direction criterion plus reported numerical posterior.

### C5 — graceful dependency-shift degradation

When `alpha_test` changes from 0.70 to 0.30 or 0.90, M2 may become miscalibrated because its calibration dependency estimate is stale. However:

- its mean Brier degradation across correlated regimes must be no worse than M1 by more than `0.005`;
- catastrophic reversal where copies/shared clusters become treated as five independent sources is a FAIL.

### Measurement verdict

```text
PASS = C1 && C2 && C3 && C4 && C5
```

A PASS validates only the utility of retaining coarse dependency topology in a bounded synthetic aggregator.

## 8. Mandatory negative interpretation

Even a clean PASS does **not** establish that REE should add a convergence module.

It would establish only:

> when exact joint inference is unavailable, a compact representation of evidence provenance/dependency can preserve second-order information that is destroyed by marginal-reliability weighting or one global correlation scalar.

The following remain open:

- whether REE's heterogeneous channels have estimable dependency graphs;
- whether those graphs are stable enough to matter;
- whether explicit provenance is cheaper than learning the same relation in existing arbitration machinery;
- whether convergence topology improves stopping or information allocation;
- whether biological systems represent such topology explicitly.

## 9. Stop / weaken conditions

Weaken the convergence programme if:

1. M2 does not beat M1 on the multi-cluster regimes;
2. M2 requires almost as much regime knowledge as exact Bayes;
3. M2 collapses under modest dependency shift;
4. the minority expert is swamped by topology-aware majority confidence;
5. all useful gains can be reproduced by ordinary reliability weighting plus one cheap covariance estimate.

## 10. Next branch only if this survives

If Assay 002 passes, the next assay should switch sign from convergence to divergence:

> **Can coarse structured disagreement choose useful information-seeking actions above raw uncertainty, raw committee disagreement, and expected information gain baselines under bounded compute?**

No REE action authority should be granted before that opposite-sign test.
