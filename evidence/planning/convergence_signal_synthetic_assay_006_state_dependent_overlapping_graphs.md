# Convergence Signal Synthetic Assay 006 — State-Dependent and Overlapping Relation Graphs

**Date:** 2026-09-09  
**Status:** preregistered synthetic assay; no REE claim registration, no creature code change, no experiment-queue mutation  
**Parent programme:** `evidence/planning/convergence_signal_experiment_ladder.md`  
**Predecessor:** Assay 005  
**Authoritative run seed:** `37`

## 1. Purpose

Assay 005 allowed evidence provenance, learned leverage and evaluator competence to be uncertain, but it still assumed that the relevant relation graphs were stationary within a problem and that downstream leverage could be represented as a linear scalar.

Assay 006 removes that convenience while simplifying everything else.

Evaluator competence is held constant. Provenance labels are not corrupted. Downstream leverage is not learned. The only target is:

> **Do source-dependency and downstream-overlap need to be conditioned on the current state/context rather than represented by one static graph?**

The assay is deliberately factorial. It asks separately whether context-sensitive evidence dependency helps, whether context-sensitive downstream overlap helps, and whether the two together outperform either axis alone.

---

## 2. Fixed evidence generator

Five visible evaluators have identical marginal machinery.

Each latent source judgement is correct with probability:

```text
p_source = 0.78
```

Each visible evaluator reads its source with reliability:

```text
p_readout = 0.90
```

Thus marginal evaluator competence is deliberately constant across evaluators and contexts. This assay is not another test of domain-specific reliability.

There are three contexts. The same evaluator identities have different true source ancestry in each context:

```text
C0: [[0,1,2], [3], [4]]
C1: [[0], [1], [2,3,4]]
C2: [[0,3], [1,4], [2]]
```

So a pair of evaluators can be redundant in one state and independent in another.

---

## 3. Evidence-dependency representations

### STATIC evidence graph

For every evaluator pair, use its mean probability of sharing a source across the three contexts.

This graph is correct on average but wrong for individual contexts.

### DYNAMIC evidence graph

Use the current context's source-dependency relation.

For an approximate posterior, evaluator `i` is weighted as:

```text
w_i = 1 / (1 + Σ_j shared_source_ij)
```

and visible-vote log odds are summed with those weights.

### EXACT evidence oracle

The exact oracle marginalises the latent source judgement for every true context-specific source group.

---

## 4. Context-dependent downstream overlap

There are eight named downstream consumers. Their effective consequence groups also change with context:

```text
C0: [[0,1,2], [3], [4,5], [6], [7]]
C1: [[0], [1,2], [3,4,5], [6,7]]
C2: [[0,7], [1], [2,3], [4], [5,6]]
```

A candidate query affects a random subset of between one and six named consumers.

### Raw count leverage

```text
L_count = number of named consumers affected
```

This double-counts consumers that are functionally redundant in the current context.

### Static-overlap leverage

Use the mean consumer-overlap graph across all contexts and discount affected consumers by the same effective-source rule.

### Dynamic-overlap leverage

Use the current context's consumer grouping. For an affected set, each equivalence group contributes one unit in total irrespective of how many members of that same group appear.

This is the true downstream leverage used by the oracle.

---

## 5. Query quality

As before:

```text
q ∈ {0.50, 0.65, 0.80, 0.95}
P(q) = {0.15, 0.25, 0.30, 0.30}
```

Information value is expected binary entropy reduction `EIG(p,q)`.

---

## 6. Compared selectors

```text
M0 STATIC + COUNT
   L_count × EIG(p_static_evidence, q)

M0b STATIC + STATIC-OVERLAP
   L_static_overlap × EIG(p_static_evidence, q)

M1 DYNAMIC-EVIDENCE ONLY
   L_count × EIG(p_dynamic_evidence, q)

M2 DYNAMIC-LEVERAGE ONLY
   L_dynamic_overlap × EIG(p_static_evidence, q)

M3 DYNAMIC BOTH
   L_dynamic_overlap × EIG(p_dynamic_evidence, q)

M4 EXACT ORACLE
   L_dynamic_overlap × EIG(p_exact_joint, q)
```

M3 is the bounded candidate. M4 remains the ceiling.

---

## 7. Main assay

Authoritative run:

- `10,000` episodes;
- six candidate queries per episode;
- context sampled uniformly;
- truth sampled uniformly;
- query quality sampled from the frozen distribution;
- affected downstream consumer subset size sampled uniformly from 1–6, then consumers sampled without replacement.

Every method selects one candidate. Chosen utility is scored by M4.

Readouts:

- mean regret;
- exact-optimum hit rate;
- fraction of oracle utility captured.

---

## 8. Preregistered criteria

### C1 — dynamic relation graph is useful overall

PASS if:

```text
M3 mean regret <= 0.020
and
M3 oracle utility fraction >= 0.98
```

### C2 — state-dependent evidence dependency matters

Compare M3 with M2, which has correct downstream overlap but a static evidence graph.

PASS if:

```text
regret_M3 <= 0.60 × regret_M2
```

### C3 — state-dependent downstream overlap matters

Compare M3 with M1, which has dynamic evidence but raw downstream count.

PASS if:

```text
regret_M3 <= 0.60 × regret_M1
```

### C4 — both axes together improve exact-optimum selection

PASS if:

```text
hit_rate_M3 >= max(hit_rate_M1, hit_rate_M2) + 0.04
```

### C5 — static-average relations are not sufficient

PASS if both:

```text
oracle_utility_fraction_M0b <= 0.97
M3 oracle utility fraction - M0b oracle utility fraction >= 0.02
```

M0b is the important rival here because it already knows that overlap exists, but only as a context-averaged graph.

### C6 — exact oracle remains the ceiling

PASS only if M4 has zero regret within numerical tolerance and there are zero episode-wise oracle-ordering violations.

**Measurement PASS requires C1–C6.**

---

## 9. Threshold provenance

Thresholds were set after non-authoritative local design pilots at seeds `201–203` using 3,000 episodes each.

Those pilots are threshold-design material only and are not banked evidence or independent replication.

The authoritative seed `37` had not been inspected when this preregistration was written.

---

## 10. Interpretation gates

### If C2 fails

A static dependency graph may be adequate even when the true source graph changes by context. Do not add state-conditioned source topology merely because it is biologically appealing.

### If C3 fails

Raw downstream count may be adequate; overlap-aware consequence topology has not earned its complexity.

### If C4 fails

The two relation graphs may not need joint state conditioning. Preserve the independently useful axis only.

### If all pass

The permitted conclusion is:

> **In this bounded synthetic world, both evidence dependency and downstream consequence overlap are state-dependent relational variables. A context-conditioned representation of both improves information allocation relative to static-average graphs or one-axis corrections.**

This still does not establish how live REE should infer context, source ancestry or downstream consumer equivalence.

---

## 11. Next gate if successful

A PASS would remove the main synthetic objection to a **shadow-only REE diagnostic**.

The shadow diagnostic should not yet change behaviour. It should ask whether, in existing REE traces, context-conditioned estimates of:

- source dependency;
- evaluator competence;
- downstream consumer overlap/leverage;
- structured dissent;

predict the marginal value of another rollout/query, later action reversal, harmful error, or post-hoc correction better than existing uncertainty/confidence signals.

No action authority should be granted until the shadow signal demonstrates incremental predictive value in the actual organism.