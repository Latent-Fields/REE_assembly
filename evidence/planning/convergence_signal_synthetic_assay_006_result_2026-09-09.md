# Convergence Signal Synthetic Assay 006 — Result

**Date:** 2026-09-09  
**Status:** synthetic measurement result; no claim promotion, no creature code change, no queue mutation  
**Preregistration:** `evidence/planning/convergence_signal_synthetic_assay_006_state_dependent_overlapping_graphs.md`  
**Driver:** `scripts/convergence_signal_synthetic_assay_006.py`  
**Banked run:** `evidence/experiments/convergence_signal_synthetic_assay_006/runs/20260909_seed37/manifest.json`

## Executive result

Assay 006 **passes all six preregistered criteria**.

The narrow result is:

> **When evidence dependency and downstream consequence overlap change with context, a static average relation graph leaves useful information on the table. Conditioning both graphs on the current state improves bounded information allocation beyond conditioning either axis alone.**

Evaluator competence was held constant, provenance labels were clean, and leverage was not learned in this assay. The gain therefore isolates the state-dependence / overlap question rather than re-testing Assay 005.

---

## Main comparison

```text
selector                    mean regret   optimal hit   oracle utility captured
M0 static + raw count        0.04969       77.17%        94.87%
M0b static + static overlap  0.03841       80.17%        96.04%
M1 dynamic evidence only     0.02583       84.34%        97.33%
M2 dynamic leverage only     0.03222       81.52%        96.67%
M3 dynamic both              0.01107       89.82%        98.86%
M4 exact oracle              0.00000      100.00%       100.00%
```

The factorial structure matters. Both one-axis repairs improve substantially over the static baseline, but the joint dynamic representation improves again.

---

## C1 — dynamic relation graph useful overall: PASS

Registered requirement:

```text
M3 regret <= 0.020
M3 oracle utility fraction >= 0.98
```

Observed:

```text
regret = 0.01107
oracle utility fraction = 0.98857
```

---

## C2 — state-dependent evidence dependency matters: PASS

Compare M3 with M2, where downstream overlap is correct but evidence dependency is frozen to its context average.

```text
M3 / M2 regret = 0.34358
```

The registered ceiling was `0.60`.

Thus a pair of evaluators being redundant in one context and independent in another is computationally consequential in this synthetic world.

---

## C3 — state-dependent downstream overlap matters: PASS

Compare M3 with M1, where evidence dependency is context-correct but downstream leverage is just a raw count of named consumers.

```text
M3 / M1 regret = 0.42857
```

The registered ceiling was `0.60`.

So the number of named downstream consumers is not equivalent to the number of distinct consequences when consumers can become functionally redundant by context.

---

## C4 — both axes together improve optimum selection: PASS

```text
M1 hit rate = 84.34%
M2 hit rate = 81.52%
M3 hit rate = 89.82%
```

M3 exceeds the better one-axis policy by **5.48 percentage points**, above the preregistered four-point requirement.

---

## C5 — static-average relations are insufficient: PASS

The strongest static rival already knows that downstream overlap exists, but uses only its average relation across contexts.

```text
M0b oracle utility fraction = 96.04%
M3  oracle utility fraction = 98.86%
absolute gain               = 2.82 percentage points
```

Thus the result is not merely `overlap matters`. **Which things overlap depends on state.**

---

## C6 — exact oracle remains the ceiling: PASS

M4 has zero regret and there are zero episode-wise oracle-ordering violations.

Again, this is a bounded approximation result, not a claim to outperform exact joint inference.

---

## Architectural consequence

After Assays 001–006, the useful object is no longer well described by a scalar convergence score.

A more faithful abstraction is a context-conditioned relation structure containing at least:

```text
current evaluator outputs
        |
        +-- source-dependency relations
        |      P(route i and j are redundant | current state)
        |
        +-- competence relations
        |      P(route i is reliable | current domain/state)
        |
        +-- downstream-impact relations
               which consumers would change if this uncertainty were resolved?
               which of those consumers are effectively redundant in this state?
```

The value of another query/rollout is then a function of the current belief plus this relation structure, not of disagreement magnitude alone.

That is strikingly compatible with the original constitutional / basal-ganglia intuition: the arbitration machinery does not need one universal scalar ruler. It needs an **umpire with context-sensitive knowledge about which votes are independent, which judges are competent here, and which consequences are genuinely distinct**.

---

## Important limit

Assay 006 gives the candidate dynamic graph the current context identity directly.

It therefore does not solve:

- how REE discovers the relevant context partition;
- how fast dependency relations can change;
- whether the same representation that defines context also biases the dependency estimator;
- how developmental changes alter the relation graph;
- whether query/rollout costs themselves vary by subsystem;
- or whether the graph can be estimated from live REE observables without hidden oracle labels.

Those now become empirical questions for shadow instrumentation rather than reasons to keep adding synthetic mechanics indefinitely.

---

## Governance conclusion

No scientific claim is promoted and no action-selection authority is added.

However, Assays 001–006 have now closed the main synthetic objections in sequence:

1. copied agreement is not independent agreement;
2. one global dependence scalar can lose topology;
3. disagreement needs reducibility/consequence structure to guide information hunger;
4. evidence independence and downstream leverage are different axes;
5. provenance/leverage/competence can be uncertain and still useful;
6. the relevant relation graphs can be state-dependent and overlapping.

The next clean step is therefore no longer another elaborate synthetic toy.

It is a **shadow-only REE diagnostic**.

The shadow system should observe existing decisions without changing them and test whether context-conditioned relational features add held-out predictive value above existing confidence/uncertainty measures for:

- value of another E1/E2 rollout;
- later action reversal;
- harmful or low-value choice;
- post-hoc correction;
- sensitivity to evaluator/channel ablation;
- and perhaps whether a disagreement resolves after sleep/replay.

Only if those shadow features earn incremental predictive value should the convergence/divergence structure receive any causal control role.

## Compact result

> **Static maps are not enough when the meaning of independence and consequence changes with state. In the registered synthetic world, representing both source dependency and downstream overlap as context-conditioned relations captures 98.86% of oracle information-allocation value and outperforms static or one-axis alternatives. The synthetic programme is now mature enough to justify shadow measurement in the actual REE organism, but not action authority.**
