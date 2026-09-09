# Convergence Signal Synthetic Assay 004 — Evidence Independence vs Downstream Leverage

**Date:** 2026-09-09  
**Status:** preregistered synthetic assay; no REE claim registration, no creature code change, no experiment-queue mutation  
**Parent programme:** `evidence/planning/convergence_signal_experiment_ladder.md`  
**Predecessors:** Assays 001–003  
**Authoritative run seed:** `23`  

## 1. Purpose

Assay 003 used evidence-source topology both to estimate how independent the current evidence was and, indirectly, as a proxy for how broadly resolving the uncertainty would matter downstream.

That convenience is not safe for a real architecture.

This assay separates two quantities that can vary independently:

1. **Evidence independence** — how many genuinely distinct routes produced the current belief/evaluation.
2. **Downstream leverage** — how many distinct consequential models/decisions would benefit from resolving the queried uncertainty.

The central falsifier is:

> **A useful convergence/divergence architecture must not infer downstream research leverage merely from the number of independent current evidence routes.**

The two graphs may overlap in real systems, but they are not the same graph.

---

## 2. Fixed synthetic world

Each candidate query concerns a binary latent state `theta ∈ {-1,+1}`.

Current evidence consists of five 70%-reliable evaluators generated under one of five evidence-dependency topologies inherited from Assay 002:

- `INDEPENDENT_5`
- `COPIES_5`
- `SHARED_CLUSTER_5`
- `TWO_CLUSTERS_3_2`
- `MIXED_3_PLUS_2`

Query quality is independently sampled from:

```text
q ∈ {0.50, 0.65, 0.80, 0.95}
```

where `q=0.50` is irreducible/no-information.

Downstream leverage is sampled **independently of evidence topology**:

```text
L ∈ {1, 2, 4, 8}
```

Interpretation: if the query resolves useful uncertainty, `L` is the predeclared aggregate number/weight of distinct downstream consequential consumers that benefit.

`L` is intentionally an external synthetic variable in this assay. Learning or estimating leverage is deferred.

---

## 3. Ground-truth query utility

For each candidate, exact Bayes under the known evidence generative model provides the current posterior `p_exact`.

The exact query value is:

```text
U_true = L × EIG(p_exact, q)
```

where `EIG` is expected binary entropy reduction from the prospective query.

This deliberately factorises:

```text
current epistemic state  <- evidence-source dependency topology
future usefulness        <- downstream leverage graph
```

Exact Bayes remains the ceiling.

---

## 4. Compared selectors

### M0 — CONFLATED TOPOLOGY/LEVERAGE

Use the number of evidence-provenance clusters as both:

- a correction for current evidence dependence; and
- a proxy for downstream leverage.

```text
score_M0 = evidence_cluster_count × EIG(p_topology, q)
```

This is the deliberately wrong hypothesis under test.

### M1 — LEVERAGE-ONLY WITH INDEPENDENCE ASSUMPTION

Use the true downstream `L`, but infer the current posterior from marginal evaluator reliability while treating all five votes as independent.

```text
score_M1 = L × EIG(p_reliability_only, q)
```

This gets downstream leverage right but can count duplicated evidence repeatedly.

### M2 — GLOBAL-DEPENDENCE FACTORISED

Represent downstream leverage separately, but compress current evidence dependence to one global `N_eff` scalar.

```text
score_M2 = L × EIG(p_global_Neff, q)
```

### M3 — TOPOLOGY-FACTORISED

Represent the two axes separately:

```text
score_M3 = L × EIG(p_cluster/provenance_topology, q)
```

This is the candidate bounded architecture.

### M4 — EXACT ORACLE

```text
score_M4 = L × EIG(p_exact_joint_Bayes, q)
```

M4 is the ceiling. M3 must not be claimed superior to it.

---

## 5. Main random-choice assay

For each of `20,000` episodes:

1. generate six candidate queries;
2. sample evidence topology independently for each candidate;
3. generate current evaluator votes;
4. sample `q` independently;
5. sample downstream leverage `L` independently;
6. compute M0–M4 scores;
7. select the highest-scoring candidate under each method;
8. score chosen **true** utility using M4.

Primary readouts:

- mean regret relative to M4;
- exact-optimum hit rate;
- fraction of oracle utility captured.

---

## 6. Forced anti-conflation diagnostic

A second diagnostic uses paired candidates with the **same query quality**:

```text
A: INDEPENDENT_5 evidence, L = 1
B: COPIES_5 evidence,      L = 8
```

The axes deliberately point in opposite directions:

- A has many independent current reasons but little downstream leverage;
- B has one effective current reason but much greater downstream leverage.

The latent state and realised votes are independently generated for each candidate.

This is not constructed so that B must always win. The oracle decides episode by episode from exact expected information value.

The diagnostic asks whether M3 follows the oracle rather than treating evidence diversity as a stand-in for usefulness.

---

## 7. Preregistered criteria

### C1 — factorisation defeats conflation

PASS if, on the main assay:

```text
regret_M3 <= 0.10 × regret_M0
and
oracle_utility_fraction_M3 >= 0.98
```

### C2 — both axes are necessary

PASS if:

```text
regret_M3 <= 0.15 × regret_M1
```

M1 has the correct downstream leverage but the wrong current-evidence independence model. If it matches M3, evidence topology is not earning its keep here.

### C3 — topology retains value beyond one global dependence scalar

PASS if:

```text
regret_M3 <= 0.90 × regret_M2
and
optimal_hit_rate_M3 >= optimal_hit_rate_M2 + 0.005
```

This is intentionally a smaller effect than C1/C2.

### C4 — forced anti-conflation pair

PASS if:

```text
oracle_hit_rate_M3 >= 0.95
and
oracle_hit_rate_M0 <= 0.40
```

This criterion directly tests whether the architecture separates **how many reasons support the current belief** from **how much would benefit from learning more**.

### C5 — oracle ceiling

PASS only if:

```text
mean_regret_M4 == 0 within numerical tolerance
oracle ordering violations == 0
```

M3 may approach but must not outrank exact Bayes by construction.

**Measurement PASS requires C1–C5.**

---

## 8. Threshold provenance

Thresholds were set after a non-authoritative local design pilot using different random seeds (`101–103` for the main assay and `201–203` for the forced-pair diagnostic).

Those pilot values are **not banked evidence, must not be used in claim support, and must not be reported as independent replication**. Their only purpose was to avoid choosing vacuous thresholds before freezing the fresh authoritative seed `23`.

No authoritative seed-23 result was inspected before this preregistration was written.

---

## 9. Interpretation gates

### If C1/C2 fail

The proposed two-axis factorisation has not earned a distinct representation. Ordinary leverage weighting or a simpler policy is sufficient in this world.

### If C3 fails while C1/C2 pass

Separating evidence dependence from leverage matters, but one global dependence scalar may be enough. Do not retain detailed provenance topology merely because Assay 002 found it useful elsewhere.

### If C4 fails

The candidate architecture still implicitly conflates evidence diversity with information value and is not ready for REE shadow use.

### If all pass

The permitted conclusion is narrow:

> **In a bounded synthetic query-allocation problem, evidence-source dependency and downstream leverage are separable computational variables, and representing both separately improves allocation relative to policies that conflate either axis.**

It does **not** establish that REE currently exposes either variable correctly.

---

## 10. Next gate if successful

Do not move directly to causal creature control.

The next assay should remove one convenience, for example:

- provenance labels are incomplete or wrong;
- downstream leverage must be learned rather than supplied;
- evaluator competence is domain-specific;
- the evidence-dependency graph changes with state;
- downstream consumers overlap/correlate rather than contributing linearly.

Only after robustness to imperfect topology/leverage information should a shadow diagnostic be considered in live REE.