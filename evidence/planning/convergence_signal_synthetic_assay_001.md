# Convergence Signal Synthetic Assay 001 — Five Reasons vs One Reason Repeated

**Date:** 2026-09-09  
**Status:** preregistered synthetic assay design; no REE claim registration, no creature code change, no experiment-queue mutation  
**Parent programme:** `evidence/planning/convergence_signal_experiment_ladder.md`  
**Stress test:** `evidence/planning/convergence_signal_nearest_neighbor_stress_test_2026-09-09.md`

## 1. Purpose

Test the narrowest non-tautological claim in the convergence programme:

> **Two ensembles with the same number of agreeing evaluators and the same marginal evaluator reliabilities can warrant very different confidence if the evidence routes have different dependency structure.**

The assay must distinguish:

- five genuinely independent reasons;
- one reason copied five times;
- a cluster sharing a hidden common error source;
- a mixed ensemble containing both correlated and independent routes.

This is not a test of the full REE architecture. It is a measurement test for whether an inexpensive independence-aware confidence observable can recover information lost by raw voting / reliability-only aggregation.

## 2. Fixed synthetic world

Binary ground truth `y ∈ {-1,+1}`.

Five evaluators each have the same marginal accuracy:

```text
P(v_i = y) = p = 0.70
```

No evaluator has higher nominal vote weight than another.

Four dependency regimes:

### A — INDEPENDENT

All five errors are conditionally independent given `y`.

### B — COPIES

One 70%-accurate evaluator is sampled and its output is copied into all five channels.

Marginal evaluator accuracy remains 0.70. Vote count is five. Effective evidence source count is one.

### C — SHARED_BIAS

With probability `rho = 0.70`, all five evaluators use one shared 70%-accurate latent judgement. Otherwise they sample independently at 0.70 accuracy.

Marginal individual accuracy remains approximately matched to the other regimes, but residual errors are strongly correlated.

### D — MIXED

Three evaluators form the `SHARED_BIAS` cluster and two evaluators remain independent 70%-accurate routes.

This creates a partially redundant coalition rather than the trivial all-independent/all-copy endpoints.

## 3. Why unanimity is the clean first discriminator

With five independent 70%-accurate evaluators, conditional on unanimous agreement the correct direction is:

```text
P(correct | 5/5 agree, independent)
  = p^5 / (p^5 + (1-p)^5)
  ≈ 0.98575
```

With five exact copies of one 70%-accurate evaluator:

```text
P(correct | 5/5 agree, copies) = 0.70
```

Thus the **observable vote pattern is identical** (`5/5`), while its evidential meaning is radically different.

A metric that cannot distinguish these two cases cannot serve the proposed REE role.

## 4. Compared methods

### M0 — raw unanimity / vote strength

Use `|Σ v_i| / 5` as confidence.

Expected failure: assigns maximal confidence to every 5/5 agreement regardless of dependency.

### M1 — reliability-only independent-evidence combiner

Assume all five 70%-accurate sources are independent and combine using reliability/log-odds.

Expected failure: copied or correlated channels are double-counted because marginal reliability does not encode ancestry/covariance.

### M2 — independence-aware effective-source approximation

Estimate pairwise **error/correctness correlation** from a labelled calibration set.

For mean off-diagonal correlation `rho_bar`, define a deliberately simple effective sample size:

```text
N_eff = N / (1 + (N-1) * max(0, rho_bar))
```

Then scale reliability evidence by `N_eff/N` before converting to confidence.

For equal evaluator reliability `p` and signed vote sum `s = |Σ v_i|`:

```text
log_odds_correct ≈ s * (N_eff/N) * log(p/(1-p))
confidence = sigmoid(log_odds_correct)
```

This is a **cheap heuristic**, not a claim of optimal inference.

### M3 — rich joint-pattern / covariance-aware ceiling

Use a high-information baseline that learns or knows the full vote-pattern/dependency distribution on calibration data.

M2 is not expected to beat M3. The programme survives only if M2 captures a substantial fraction of the dependency correction while remaining much simpler.

## 5. Data split

Default reference run:

- calibration: 100,000 trials per regime;
- held-out evaluation: 100,000 trials per regime;
- fixed reproducibility seed: 7;
- evaluator accuracy `p = 0.70`;
- shared-bias mixture `rho = 0.70`.

The held-out labels are not used to estimate evaluator dependence.

A later replication should sweep seeds, `p`, `rho`, evaluator count, class balance and heterogeneous reliabilities.

## 6. Primary readouts

For each regime report:

1. majority-vote accuracy;
2. unanimity frequency;
3. true accuracy conditional on unanimity;
4. confidence assigned to unanimous decisions by M0/M1/M2/M3;
5. Brier score / log loss of confidence if calibrated outputs are compared;
6. estimated pairwise residual correlation;
7. estimated `N_eff`.

## 7. Pre-registered qualitative ordering

For unanimous decisions, the independence-aware method should produce:

```text
confidence(INDEPENDENT)
  > confidence(MIXED)
  > confidence(SHARED_BIAS)
  > confidence(COPIES)
```

The exact MIXED/SHARED_BIAS spacing may vary with the dependency estimator, but the endpoint distinction is mandatory.

M0 and M1 are expected to substantially overstate confidence in COPIES and SHARED_BIAS.

## 8. PASS criteria for the measurement primitive

This is a measurement PASS, not a REE claim confirmation.

All must hold:

### C1 — duplicate-evidence discrimination

Under 5/5 agreement, M2 assigns materially lower confidence to COPIES than INDEPENDENT, with a target separation of at least `0.15` absolute confidence.

### C2 — correct ordering

Across the four regimes, M2 confidence follows the dependency ordering above on held-out trials.

### C3 — endpoint calibration sanity

For INDEPENDENT unanimity, M2 predicted confidence is within `±0.03` of empirical conditional accuracy.

For COPIES unanimity, M2 predicted confidence is within `±0.03` of empirical conditional accuracy.

These endpoint criteria ensure the method is not merely ranking regimes while remaining badly calibrated.

### C4 — reliability-only insufficiency is visible

M1 must fail to distinguish INDEPENDENT from COPIES when marginal reliabilities and observed unanimous vote strength are matched. If M1 somehow already solves the task under the implemented definition, the purported convergence-specific gain dissolves.

### C5 — rich baseline ceiling respected

M2 is not required to beat M3. If M2 materially outperforms a correctly implemented full-joint baseline, treat that first as a likely baseline bug.

## 9. Stronger programme criteria for later replication

After the reference design clears measurement range, test whether M2:

- recovers at least 70% of the calibration improvement from M1 toward M3 across a dependency sweep;
- remains useful when dependence is estimated approximately rather than known;
- degrades gracefully under dependency shift;
- is robust to evaluator dropout;
- is not fooled by one powerful hidden common ancestor;
- handles heterogeneous reliabilities without collapsing to head-count consensus.

These are **not** required for Synthetic Assay 001's first pass.

## 10. Negative controls / ways to kill the idea early

1. **Wrong dependency estimate:** deliberately permute/corrupt the correlation matrix. The claimed benefit should diminish. If it does not, the metric is not actually using dependency information.
2. **Zero-information evaluators:** p=0.5 channels should not gain epistemic weight merely through independent agreement.
3. **Shared systematic bias:** independence of stochastic residuals is insufficient if all sources share a directional bias. This is a known limitation and must not be hidden.
4. **One excellent specialist vs weak majority:** belongs to the next assay; raw convergence must never be allowed to override reliability/relevance.
5. **Protected veto:** explicitly out of scope for this assay; no convergence score can buy off a protected harm veto.

## 11. Interpretation table

| Result | Interpretation |
|---|---|
| M2 separates independent vs copies and calibrates endpoints | independence-aware convergence is a viable measurement primitive worth deeper testing |
| M2 ranks regimes but is badly calibrated | dependency topology is useful, current metric inadequate |
| M1 matches M2 | no separate convergence primitive needed at this grain; reliability model already captures it |
| M2 fails independent vs copies | stop/reframe before touching REE |
| M3 succeeds but M2 fails | dependency matters, but the proposed cheap observable may be too crude |
| all methods fail | simulation or problem definition is wrong; no architecture inference |

## 12. Non-evidentiary parameter sanity check

Before preregistration, a local design-only simulation with the fixed parameters produced the expected qualitative range:

- independent unanimous decisions: ~0.986 empirical accuracy;
- exact copies: ~0.700;
- shared-bias: ~0.72;
- mixed: ~0.94.

A simple `N_eff` correction produced endpoint confidence close to the independent/copy values and intermediate confidence in the correlated regimes.

**This was a design sanity check only. It is not registered evidence, does not count as an experiment result, and must not be used to promote any claim.**

## 13. Implementation

Reference implementation:

`scripts/convergence_signal_synthetic_assay_001.py`

It should emit a machine-readable JSON/CSV summary and print the preregistered diagnostics. The first authoritative run should be executed after code review against this document, with outputs banked separately rather than editing this preregistration post hoc.

## 14. Next experiment if this passes

The next high-value test is not more confidence aggregation. It is the opposite sign of the proposed meta-signal:

> **Can independence-aware structured disagreement choose informative queries better than raw uncertainty or raw disagreement?**

That becomes Synthetic Assay 002 / experiment-ladder Stage 4, connecting directly to the information-hunger observation that started this branch.
