# Convergence Signal Synthetic Assay 005 — Imperfect Provenance, Learned Leverage, and Domain-Specific Competence

**Date:** 2026-09-09  
**Status:** preregistered synthetic assay; no REE claim registration, no creature code change, no experiment-queue mutation  
**Parent programme:** `evidence/planning/convergence_signal_experiment_ladder.md`  
**Predecessors:** Assays 001–004  
**Authoritative run seed:** `29`

## 1. Purpose

Assay 004 showed that evidence-source dependency and downstream leverage should not be collapsed into one quantity. It still gave the candidate architecture two conveniences that a real organism will not have:

1. provenance/source ancestry was effectively correct;
2. downstream leverage was supplied rather than learned.

A third convenience also remained partly hidden: evaluator competence was treated as if it were broadly stable across contexts.

Assay 005 removes all three conveniences at once.

The central question is:

> **Does a factorised convergence/divergence policy degrade gracefully when provenance is incomplete or wrong, downstream leverage must be estimated from experience, and evaluator competence is domain-specific?**

The aim is not to preserve near-oracle performance under arbitrary corruption. The aim is to determine whether the architectural distinctions discovered in Assays 001–004 remain useful when their inputs are themselves uncertain.

---

## 2. Fixed synthetic world

Each candidate query concerns a binary latent state `theta ∈ {-1,+1}`.

### 2.1 Evidence-source topology

Five visible evaluators are generated from one of four true source topologies:

```text
INDEPENDENT_5       [[0],[1],[2],[3],[4]]
COPIES_5            [[0,1,2,3,4]]
TWO_CLUSTERS_3_2    [[0,1,2],[3,4]]
MIXED_3_PLUS_2      [[0,1,2],[3],[4]]
```

Topology prior:

```text
0.30, 0.20, 0.20, 0.30
```

Each true source first generates a latent source judgement with accuracy:

```text
p_source = 0.78
```

Each visible evaluator then reads that source judgement through a domain-dependent noisy readout.

### 2.2 Domain-specific competence

There are three domains `D0,D1,D2`.

Readout reliabilities are fixed as:

```text
          D0    D1    D2
E0       .98   .80   .80
E1       .80   .98   .80
E2       .80   .80   .98
E3       .92   .86   .86
E4       .86   .92   .86
```

Thus different evaluators are genuinely more or less informative depending on the current domain.

The candidate system is not handed these marginal accuracies directly. Before the main run it receives a separate fixed calibration corpus of `20,000` labelled examples per domain and estimates evaluator accuracy by domain. A domain-blind baseline uses the same corpus but pools across domains.

### 2.3 Query quality

```text
q ∈ {0.50, 0.65, 0.80, 0.95}
P(q) = {0.15, 0.25, 0.30, 0.30}
```

`q=0.50` is an irreducible/no-information query.

### 2.4 True downstream leverage

```text
L ∈ {1,2,4,8}
```

sampled uniformly and independently of evidence topology and domain.

The exact oracle uses `L` directly. Candidate bounded policies must estimate it.

---

## 3. Learned leverage

For each candidate, the policy receives a finite history of analogous downstream outcomes rather than the true `L`.

If true leverage is `L`, each historical sample produces a downstream-success event with probability:

```text
L / 8
```

With `h` successes in `n_hist` observations, the bounded estimate is:

```text
L_hat = 8 × (h + 1) / (n_hist + 2)
```

This is a deliberately simple Beta(1,1)-smoothed estimator. It is not tuned to the current episode.

---

## 4. Imperfect provenance

Each evaluator has a true source label induced by the sampled topology.

The observed provenance label can be:

- missing;
- correct;
- or replaced by a wrong source label.

Three preregistered corruption regimes are run separately:

```text
CLEAN:
  missing = 0.00
  wrong   = 0.00
  n_hist  = 64

MODERATE:
  missing = 0.25
  wrong   = 0.10
  n_hist  = 32

HARSH:
  missing = 0.50
  wrong   = 0.20
  n_hist  = 8
```

The candidate `soft provenance` policy does not pretend those labels are certain. It uses frozen pairwise probabilities that two evaluators share a source, conditional on their observed provenance relation.

```text
CLEAN:
  same observed label        1.000
  different observed label   0.000
  one/both missing           0.370

MODERATE:
  same observed label        0.911
  different observed label   0.104
  one/both missing           0.370

HARSH:
  same observed label        0.812
  different observed label   0.184
  one/both missing           0.370
```

These values were fixed from the known corruption process and topology prior before the authoritative seed was inspected. They are not inferred from the current candidate's ground truth.

---

## 5. Approximate posteriors

### Domain-blind independence

Treat all five visible evaluators as independent and use marginal reliability pooled across domains.

### Domain-aware independence

Treat all five as independent, but use marginal reliability estimated separately within the current domain.

### Hard provenance

Use domain-aware marginal reliability. Evaluators with the same non-missing observed provenance label are treated as one effective source by averaging their log-odds contributions. Missing labels become singleton groups.

### Soft provenance

Use domain-aware marginal reliability and assign evaluator `i` weight:

```text
w_i = 1 / (1 + Σ_j P(shared_source_ij | observed provenance))
```

The approximate log odds are:

```text
log_odds = Σ_i w_i × vote_i × logit(p_i,domain)
```

This does not reconstruct the full latent source model. It is intentionally a cheap bounded approximation.

### Exact oracle

The oracle knows the true topology, source reliability, readout reliabilities, current domain, and true `L`, and evaluates the full joint likelihood by marginalising each latent source judgement.

---

## 6. Compared query-allocation policies

For every candidate, information value is expected binary entropy reduction `EIG(p,q)`.

```text
M0 CONFLATED:
   observed hard provenance cluster count × EIG(domain-blind posterior, q)

M1 GLOBAL-FACTORISED:
   L_hat × EIG(domain-blind independence posterior, q)

M2 DOMAIN-FACTORISED:
   L_hat × EIG(domain-aware independence posterior, q)

M3 HARD-PROVENANCE:
   L_hat × EIG(domain-aware hard-provenance posterior, q)

M4 SOFT-PROVENANCE:
   L_hat × EIG(domain-aware soft-provenance posterior, q)

A_TRUEPROV:
   L_hat × EIG(domain-aware posterior with true source grouping, q)

A_TRUEL:
   L × EIG(domain-aware soft-provenance posterior, q)

M5 EXACT-ORACLE:
   L × EIG(exact joint posterior, q)
```

`A_TRUEPROV` and `A_TRUEL` are decomposition controls, not candidate policies.

---

## 7. Main assay

For each corruption regime independently:

- `10,000` episodes;
- six candidate queries per episode;
- topology, domain, truth, query quality and leverage sampled independently according to the frozen distributions;
- every method selects one candidate;
- chosen utility is scored using the exact oracle value of that candidate.

Readouts:

- mean regret;
- exact-optimum hit rate;
- fraction of oracle utility captured;
- mean absolute error of `L_hat`.

---

## 8. Preregistered criteria

### C1 — moderate corruption remains useful

PASS if under `MODERATE` corruption:

```text
regret_M4 <= 0.45 × regret_M2
and
oracle_utility_fraction_M4 >= 0.95
```

This asks whether uncertain provenance still adds value beyond domain-aware reliability plus learned leverage.

### C2 — harsh corruption degrades gracefully rather than collapsing

PASS if under `HARSH` corruption:

```text
regret_M4 <= 0.65 × regret_M2
and
oracle_utility_fraction_M4 >= 0.92
```

### C3 — soft provenance beats brittle hard labels

PASS if:

```text
MODERATE: regret_M4 <= 0.95 × regret_M3
HARSH:    regret_M4 <= 0.80 × regret_M3
```

The clean condition is expected to tie because provenance labels are correct.

### C4 — learned leverage remains adequate

PASS if all of the following hold:

```text
MODERATE L_hat mean absolute error <= 0.45
HARSH    L_hat mean absolute error <= 0.90

MODERATE oracle_utility_fraction_A_TRUEPROV >= 0.975
HARSH    oracle_utility_fraction_A_TRUEPROV >= 0.955
```

This does not require learned leverage to equal supplied leverage. It requires that finite history does not by itself destroy useful allocation when provenance is otherwise correct.

### C5 — domain-specific competence earns its representation

Across the three corruption regimes, let `R_domain` be mean regret of M2 and `R_global` mean regret of M1.

PASS if:

```text
R_domain <= 0.95 × R_global
```

Thus domain-specific reliability must improve allocation rather than merely add parameters.

### C6 — oracle ceiling

PASS only if M5 has zero regret within numerical tolerance and no method is scored as exceeding the exact oracle utility for an episode.

**Measurement PASS requires C1–C6.**

---

## 9. Threshold provenance

Thresholds were set from non-authoritative local design pilots using seeds `101–103` at smaller episode counts.

Those pilot values:

- are not banked evidence;
- must not be treated as replication;
- must not be used for claim promotion;
- existed only to prevent vacuous thresholds.

The authoritative seed `29` had not been inspected when this preregistration was written.

---

## 10. Interpretation gates

### If C1/C2 fail

The architecture is too dependent on clean provenance or supplied leverage to justify live REE shadow instrumentation.

### If C3 fails

Representing provenance uncertainty explicitly has not earned its complexity; hard labels or a simpler global dependence correction may be sufficient.

### If C4 fails

Downstream leverage cannot yet be treated as a learnable control quantity with this estimator. Improve leverage learning before any organism-level use.

### If C5 fails

Domain-specific competence does not justify a separate reliability representation in this setting.

### If all criteria pass

The permitted conclusion remains narrow:

> **In a bounded synthetic query-allocation world, the factorisation into evidence dependency, downstream leverage and domain-specific competence remains useful under substantial uncertainty in all three quantities, and a soft provenance representation degrades more gracefully than hard ancestry labels.**

This still does not establish that REE's live channels expose these variables in a useful form.

---

## 11. Next gate if successful

If Assay 005 passes, the next move should not be direct action authority.

Two reasonable gates remain:

1. **Assay 006 — state-dependent/overlapping dependency graphs:** source relationships and downstream consumers change with context, and consumers overlap rather than adding linearly.
2. **REE shadow diagnostic:** instrument existing channels without changing decisions and ask whether measured source-dependency / leverage / domain-competence structure predicts value of additional rollout, action reversal, harmful error or later correction.

The choice between those should depend on how much headroom remains after Assay 005.