# Convergence Signal Synthetic Assay 003 — Structured Divergence and Query Allocation

**Date:** 2026-09-09  
**Status:** preregistered synthetic assay design; no REE claim registration, no creature code change, no experiment-queue mutation  
**Parent result:** `evidence/planning/convergence_signal_synthetic_assay_002_result_2026-09-09.md`  
**Child thought:** `docs/thoughts/2026-09-09_convergence_divergence_as_dual_meta_signal.md`

## 1. Purpose

Assays 001–002 tested the convergence/closure side of the proposed dual meta-signal.

Assay 003 flips sign.

It asks:

> **When several competent but differently grounded views disagree, can a bounded topology-aware signal allocate one scarce query toward the unresolved structure with greatest expected value, while avoiding permanent disagreement caused by irreducible noise?**

The important comparison is not against raw uncertainty alone. The hard baseline already knows query reliability, consequence weight and one global dependence estimate.

## 2. Pilot firewall

A non-authoritative pilot was used only to ensure the assay has measurement range and to choose thresholds.

The pilot result must not be counted as evidence.

The authoritative run uses a fresh seed and the criteria below frozen in advance.

## 3. Episode structure

Each episode contains **6 candidate unknowns**. The agent may query exactly one.

Each candidate has:

- a hidden binary truth `theta ∈ {-1,+1}`;
- five observed evaluator votes;
- a provenance topology;
- a historically calibrated query channel with reliability `q`;
- a visible consequence weight `w`;
- a number of distinct downstream views equal, in this first synthetic world, to the number of provenance clusters.

The candidate topologies are sampled from:

```text
INDEPENDENT_5      five distinct views
COPIES_5           one view reported five times
SHARED_CLUSTER_5   one provenance cluster with correlated reporters
TWO_CLUSTERS_3_2   two distinct view clusters
MIXED_3_PLUS_2     one 3-reporter cluster plus two independent views
```

Within correlated clusters, the same `alpha=0.70` shared-latent mixture used in Assay 002 generates reporter dependence.

Evaluator marginal accuracy is `p=0.70`.

## 4. Query channels

Each candidate independently draws historically calibrated query reliability:

```text
q ∈ {0.50, 0.65, 0.80, 0.95}
probability = {0.20, 0.25, 0.30, 0.25}
```

`q=0.50` is the mandatory **irreducible-noise trap**: querying yields no information about `theta`.

The selector may use the calibrated `q`; this assay does not yet test learning query-channel reliability.

## 5. Consequence weights

Each candidate independently draws visible decision relevance:

```text
w ∈ {1, 1, 1, 2, 4}
```

This prevents the task from collapsing to epistemic uncertainty alone. A lower-uncertainty question may rationally be queried if resolving it matters much more for action.

## 6. Ground-truth query utility

The exact current posterior under the true joint generative model is:

```text
pi_exact = P(theta=+1 | observed votes, true topology)
```

For a binary query channel of reliability `q`, exact expected information gain is the expected reduction in binary entropy after one query.

Ground-truth utility is:

```text
U_true = distinct_view_count * w * EIG(pi_exact, q)
```

This is deliberately a synthetic operationalisation of the discussion's “several information-hunger drives pull toward the same unknown”.

In this first assay, a provenance cluster defines one distinct downstream view. Later assays must relax that simplifying assumption.

## 7. Compared selectors

### M0 — RAW UNCERTAINTY

Uses only closeness of the five observed hard votes to a 50:50 split.

Ignores provenance, query reducibility and consequence.

### M1 — RAW COMMITTEE DISAGREEMENT

Uses pairwise/hard-vote disagreement only.

For binary equal-weight votes this is intentionally close to M0; it represents the simple Query-by-Committee intuition without value/reducibility controls.

### M2 — RELIABILITY-ONLY VALUE OF INFORMATION

- treats all five observed reporters as independent;
- uses their calibrated marginal reliability;
- uses calibrated `q` and consequence weight `w`;
- assumes nominal leverage of five views.

This is a strong baseline: it knows reducibility and decision relevance but not duplicated evidence or provenance topology.

### M3 — GLOBAL `N_eff` VALUE OF INFORMATION

Uses Assay-001 global mean-correlation correction, calibrated per topology class, plus `q` and `w`.

It knows that some reporter sets are redundant but collapses the whole dependency structure to one scalar.

### M4 — TOPOLOGY-AWARE STRUCTURED DIVERGENCE

Uses:

- calibrated marginal reliability;
- declared provenance clusters;
- calibrated within-cluster residual correlation;
- calibrated query reliability `q`;
- visible consequence `w`;
- number of distinct provenance clusters as the first synthetic proxy for cross-view leverage.

It does **not** receive the hidden truth or trial query outcome.

### M5 — EXACT VALUE-OF-INFORMATION ORACLE

Computes `U_true` from the exact joint posterior and selects the maximum-utility candidate.

This is the ceiling. M4 is not expected to beat it.

## 8. Frozen authoritative run

```text
seed = 17
episodes = 20,000
candidates per episode = 6
```

Ties are broken deterministically by lowest candidate index for all methods.

## 9. Primary readouts

For each selector:

- mean regret relative to M5;
- optimal-query hit rate;
- rate of selecting `q=0.50` irreducible-noise candidates;
- mean true utility captured / oracle utility;
- topology distribution of selected candidates;
- consequence-weight distribution of selected candidates.

## 10. Preregistered criteria

### C1 — topology improves bounded value-of-information allocation

M4 mean regret must be at least **30% lower** than M3:

```text
regret_M4 <= 0.70 * regret_M3
```

and absolute M4 mean regret must be <= `0.020`.

### C2 — optimal-query hit rate improves over global `N_eff`

```text
hit_M4 >= hit_M3 + 0.03
```

### C3 — irreducible disagreement is not mistaken for information hunger

M4 must select `q=0.50` candidates on <= `1%` of episodes, and its irreducible-noise selection rate must be at least **10 percentage points lower** than M1 raw disagreement.

### C4 — exact oracle remains ceiling

M5 must have zero regret by construction. If any implementation reports M4 true utility above M5 for an episode, treat the assay as invalid until the scoring bug is found.

### C5 — topology gain is not merely consequence weighting

M2 and M3 already receive `q` and `w`.

Therefore M4 must also beat M2 mean regret and must not have a lower optimal-query hit rate than M2.

### Measurement verdict

```text
PASS = C1 && C2 && C3 && C4 && C5
```

## 11. Mandatory negative interpretation

A PASS would establish only that, in this constructed bounded world, coarse provenance topology improves allocation of a scarce information-gathering action after query reducibility and decision relevance are already represented.

It would **not** establish that:

- REE should create a new information-hunger module;
- disagreement is always useful;
- provenance clusters equal biological independence;
- one query really updates multiple REE subsystems in proportion to cluster count;
- exact expected information gain is biologically computed;
- the same signal should influence action selection.

## 12. Strong failure interpretations

- If M4 does not beat M3: per-cluster topology may add little for information allocation even though it helped confidence calibration.
- If M4 chases `q=0.50`: structured disagreement has failed the irreducible-noise requirement.
- If M2 matches M4: ordinary reliability + reducibility + consequence may already be enough; convergence/divergence topology is unnecessary.
- If M4 works only because `distinct_view_count` is handed to it: the next assay must estimate leverage rather than declaring it from provenance.

## 13. Next step only if PASS

Do **not** move directly into REE action authority.

The next assay should remove one convenience at a time:

1. learn query reducibility rather than provide `q`;
2. make provenance imperfect/latent;
3. separate evidence-source independence from downstream consequence leverage;
4. introduce evaluator domain specificity;
5. only then consider a REE shadow diagnostic for where additional rollout or observation is valuable.
