# Convergence Signal Synthetic Assay 005 — Result

**Date:** 2026-09-09  
**Status:** synthetic measurement result; no claim promotion, no creature code change, no queue mutation  
**Preregistration:** `evidence/planning/convergence_signal_synthetic_assay_005_imperfect_provenance_learned_leverage.md`  
**Driver:** `scripts/convergence_signal_synthetic_assay_005.py`  
**Banked run:** `evidence/experiments/convergence_signal_synthetic_assay_005/runs/20260909_seed29/manifest.json`

## Executive result

Assay 005 **passes all six preregistered criteria**.

The narrow result is:

> **The factorisation discovered in Assays 001–004 remains useful even when all three inputs are uncertain: evidence provenance can be missing/wrong, downstream leverage can be learned from finite history, and evaluator reliability can vary by domain. Soft uncertainty over provenance degrades more gracefully than hard ancestry labels.**

This is still a synthetic measurement result, not evidence that the live REE organism already exposes these variables in a usable form.

---

## Main result

### Oracle utility captured

```text
                         CLEAN      MODERATE     HARSH
M0 conflated             68.16%      69.44%      70.81%
M1 global factorised     89.08%      88.25%      86.48%
M2 domain factorised     89.88%      89.09%      87.14%
M3 hard provenance       98.49%      94.92%      90.03%
M4 soft provenance       98.49%      95.83%      93.24%
A true prov + learned L  98.49%      98.12%      96.68%
A soft prov + true L     98.88%      96.57%      95.37%
M5 exact oracle         100.00%     100.00%     100.00%
```

The pattern is useful because it is not an all-or-none PASS. Performance falls as metadata quality falls, but the factorised architecture retains substantial value.

---

## C1 — moderate corruption remains useful: PASS

Registered requirement:

```text
regret_M4 <= 0.45 × regret_M2
oracle utility fraction_M4 >= 0.95
```

Observed:

```text
M2 regret = 0.16875
M4 regret = 0.06458
ratio     = 0.38266
M4 oracle utility fraction = 0.95827
```

Thus uncertain provenance still contributes substantial value beyond domain-aware reliability plus learned leverage.

---

## C2 — harsh corruption degrades gracefully: PASS

Registered requirement:

```text
regret_M4 <= 0.65 × regret_M2
oracle utility fraction_M4 >= 0.92
```

Observed:

```text
M2 regret = 0.19563
M4 regret = 0.10284
ratio     = 0.52568
M4 oracle utility fraction = 0.93240
```

At 50% missing provenance, 20% wrong provenance, and only eight leverage-history observations, the candidate policy still captures 93.24% of oracle query utility.

This should not be described as robust to arbitrary provenance failure. It is evidence of graceful degradation under the registered corruption regime.

---

## C3 — soft provenance beats brittle hard labels: PASS

Observed regret ratios:

```text
MODERATE: M4/M3 = 0.82092
HARSH:    M4/M3 = 0.67812
```

Under clean labels the two methods tie exactly, as expected.

Under corruption, treating provenance as uncertain is clearly better than turning noisy labels into categorical ancestry claims.

An interesting detail is that under MODERATE corruption, hard provenance has a slightly higher exact-optimum hit rate (`79.58%` vs `78.86%`) despite worse regret. Soft provenance therefore wins not by choosing the exact optimum more often, but by making **less costly mistakes** when it does miss the optimum.

That distinction may matter in REE, where the severity of an allocation error can matter more than raw hit count.

---

## C4 — learned leverage remains adequate: PASS

Mean absolute leverage-estimation error:

```text
CLEAN     0.27641
MODERATE  0.40240
HARSH     0.81519
```

With true provenance but the same learned leverage:

```text
MODERATE oracle utility captured = 98.12%
HARSH    oracle utility captured = 96.68%
```

So the simple finite-history leverage estimator is not the dominant failure source in this assay.

Conversely, with true leverage but corrupted soft provenance:

```text
MODERATE = 96.57%
HARSH    = 95.37%
```

This decomposition suggests both estimation problems contribute, but provenance uncertainty is the larger source of headroom under the registered harsh regime.

---

## C5 — domain-specific competence earns its representation: PASS

Mean regret across corruption regimes:

```text
M1 global/domain-blind reliability  = 0.18498
M2 domain-specific reliability      = 0.17315
ratio                               = 0.93603
```

The gain is modest but consistent enough to clear the preregistered 0.95 ratio.

This supports an important architectural caution:

> **An evaluator should not carry one global trust weight if its competence depends on the current representational or behavioural domain.**

This remains a bounded synthetic result; it does not establish the appropriate domain partition for REE.

---

## C6 — exact oracle remains the ceiling: PASS

The exact oracle has zero regret in all three regimes and no method exceeded episode-wise oracle utility.

The programme therefore remains an approximation/compression programme rather than a purported alternative to exact joint inference.

---

## What Assay 005 changes conceptually

The current picture is now at least three-dimensional.

```text
1. evidence dependency
   Who are genuinely independent sources of the current belief?

2. downstream leverage
   Which distinct consequential consumers would benefit if this uncertainty were resolved?

3. domain competence
   How trustworthy is each evaluator for this particular kind of problem?
```

And each of those has its own uncertainty:

```text
P(source dependency | provenance evidence)
P(downstream leverage | prior experience)
P(evaluator competence | domain, calibration history)
```

The architectural object is therefore moving away from a scalar `convergence score` and toward a small **uncertainty-bearing relation graph**.

That is a stronger fit with the original basal-ganglia / constitutional intuition: multiple systems need not collapse into one universal currency before arbitration. The umpire can care about where signals came from, what they are competent to judge, and what would change if a disputed relation were resolved.

---

## Important negative result / remaining weakness

Assay 005 still assumes several conveniences:

- source relationships are stationary within a candidate;
- downstream consumers contribute linearly through scalar `L`;
- downstream consumers do not overlap or share failure modes;
- the corruption process is known well enough to assign fixed soft-provenance probabilities;
- domain identity is supplied cleanly;
- leverage history is generated from a stationary process.

The assay therefore does **not** yet establish that a single persistent topology graph is adequate.

The strongest remaining synthetic rival is:

> **dependency and leverage may themselves be state-dependent relational objects, changing as the system enters different contexts, modes, developmental stages or representational frames.**

---

## Governance conclusion

No scientific claim is promoted from this run.

Assays 001–005 now justify continuing the programme, but the strongest broad claim still has not earned live action authority.

A reasonable next gate is either:

1. **Assay 006 — state-dependent and overlapping relation graphs**, testing whether static provenance/leverage representations become misleading when dependencies change with context; or
2. a **shadow-only REE diagnostic**, measuring these quantities without allowing them to influence action.

Given the remaining synthetic convenience is specifically *stationarity and non-overlap*, Assay 006 is the cleaner next falsifier before live shadow instrumentation.

## Compact result

> **When provenance is uncertain, treat provenance as uncertain. When competence is domain-specific, calibrate it by domain. When research leverage must be learned, keep that estimate separate from the evidence graph. Under the registered corruption regimes, this factorised representation degrades gracefully and remains substantially closer to exact information allocation than policies that collapse those distinctions.**
