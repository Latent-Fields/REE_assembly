# Convergence Signal Synthetic Assay 004 — Result

**Date:** 2026-09-09  
**Status:** synthetic measurement result; no claim promotion, no creature code change, no queue mutation  
**Preregistration:** `evidence/planning/convergence_signal_synthetic_assay_004_evidence_vs_downstream_leverage.md`  
**Pre-run amendment:** `evidence/planning/convergence_signal_synthetic_assay_004_prerun_amendment.md`  
**Reference driver:** `scripts/convergence_signal_synthetic_assay_004.py`  
**Banked run:** `evidence/experiments/convergence_signal_synthetic_assay_004/runs/20260909_seed23/manifest.json`

## Executive result

Assay 004 **passes all five preregistered criteria**.

The narrow result is:

> **Evidence independence and downstream research leverage are separable computational variables. A policy that treats “how many independent reasons I currently have” as a proxy for “how much of the system would benefit from learning more” allocates queries badly.**

The candidate factorised policy represents:

```text
current epistemic confidence <- evidence-source dependency topology
future information value     <- downstream leverage
```

and combines them only at the value-of-information calculation.

### Main random-choice assay

```text
selector                  mean regret   optimal hit   oracle utility captured
M0 conflated               0.61343       44.92%        65.89%
M1 leverage-only           0.42390       56.11%        76.43%
M2 global factorised       0.01929       94.33%        98.93%
M3 topology factorised     0.01526       95.22%        99.15%
M4 exact oracle            0.00000      100.00%       100.00%
```

The key architectural lesson is not that topology magically creates value. It is that two different graphs must not be collapsed:

```text
who supplied the current evidence?
             !=
who would benefit if this uncertainty were resolved?
```

---

## C1 — factorisation defeats conflation: PASS

Preregistered requirement:

```text
regret_M3 <= 0.10 × regret_M0
oracle_utility_fraction_M3 >= 0.98
```

Observed:

```text
M3/M0 regret ratio = 0.02487
M3 oracle utility  = 0.99152
```

Thus the factorised policy has only about 2.5% of the regret of the deliberately conflated policy.

---

## C2 — both axes are necessary: PASS

M1 knows the true downstream leverage but treats the five current evaluators as independent.

Observed:

```text
M1 mean regret = 0.42390
M3 mean regret = 0.01526
M3/M1 ratio    = 0.03599
```

So getting downstream leverage right is not enough if duplicated/correlated current evidence is counted repeatedly.

---

## C3 — detailed topology still adds value beyond a single global dependence scalar: PASS

Observed:

```text
M2 global-N_eff regret      = 0.01929
M3 topology-aware regret    = 0.01526
M3/M2 regret ratio          = 0.79083

M2 optimal-hit rate         = 94.33%
M3 optimal-hit rate         = 95.22%
absolute hit-rate gain      = 0.89 percentage points
```

This is a smaller effect than C1/C2, as expected. The main conceptual win in Assay 004 is **separating evidence topology from downstream leverage**. Preserving internal evidence-cluster topology is a secondary refinement.

---

## C4 — forced anti-conflation pair: PASS

The forced pair deliberately opposes the two axes:

```text
A: five independent current reasons, downstream leverage = 1
B: five copies of one current reason, downstream leverage = 8
```

Oracle-following rate:

```text
M0 conflated               16.82%
M1 leverage-only           55.94%
M2 global factorised      100.00%
M3 topology factorised    100.00%
M4 oracle                 100.00%
```

This is the cleanest result in the assay.

A method that equates evidence diversity with research leverage strongly prefers the wrong query in this anti-aligned world. Once current-evidence dependence and downstream usefulness are represented separately, the bounded policies recover the oracle choice in every sampled forced-pair episode.

This does **not** imply that `COPIES_5, L=8` is always more valuable in general. It means that the correct value can only be calculated after both quantities are represented separately.

---

## C5 — exact Bayes remains the ceiling: PASS

Exact oracle mean regret is zero and there are zero oracle-ordering violations.

The programme therefore remains a bounded-computation project, not a claim that a convergence heuristic surpasses correct joint inference.

---

## What Assay 004 changes conceptually

The convergence/divergence programme should now keep at least three quantities distinct:

1. **current evidence competence/reliability**;
2. **current evidence dependency/provenance topology**;
3. **downstream consequence or model leverage of resolving the uncertainty**.

A fourth quantity remains query reducibility / information quality.

A schematic information-hunger term therefore looks less like:

```text
many systems disagree -> investigate
```

and more like:

```text
value(query)
  ~= reducible uncertainty
     × consequence/leverage
     × correction for what current evidence is genuinely independent
```

with the exact form still open.

The result also explains why the subjective/research intuition of “several lines are pulling me toward the same question” can be useful without being sufficient. Several lines may indicate that an unknown is well connected, but **connectivity of evidence generation and connectivity of downstream consequences are different relations**.

---

## Important limits

The assay still supplies several conveniences that REE will not receive for free:

- provenance clusters are correct and known;
- downstream leverage `L` is given rather than learned;
- all evaluators have stationary 70% competence;
- competence is not domain-specific;
- downstream consumers contribute linearly and independently;
- evidence topology is static;
- the query's information quality is known.

Therefore this remains measurement evidence, not an architecture result.

---

## Next falsifier

The highest-value next step is to corrupt one of those conveniences rather than add more idealised topology.

Recommended Assay 005:

> **Imperfect provenance and learned leverage.**

At minimum, independently perturb:

- missing/incorrect evidence-source ancestry labels;
- estimated rather than supplied downstream leverage;
- domain-specific evaluator competence.

The key question becomes:

> **Does the benefit of factorising evidence topology from downstream leverage survive when the organism only has fallible estimates of both?**

A useful architecture must degrade gracefully. If its advantage disappears as soon as provenance or leverage is imperfect, it is unlikely to deserve a first-class REE representation.

---

## Governance interpretation

No new REE scientific claim is minted from this result.

Assays 001–004 together now justify continuing the synthetic programme and sharpen the candidate representation, but they still do not show that the live creature's E1/E2, hippocampal, harm, goal, residue, curiosity or selector channels expose these quantities or benefit from them.

The next gate remains synthetic robustness before any shadow diagnostic in live REE.