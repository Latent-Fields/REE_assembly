---
nav_exclude: true
---

# Convergence Signal — Formal Notes

**Date:** 2026-09-09  
**Status:** exploratory mathematics / measurement notes; no architectural commitment  
**Parent:** `2026-09-09_convergence_as_general_computational_signal.md`

## 1. Why formalise before implementation

“Several things agree” is too vague to implement safely.

A usable quantity must separate at least:

- **preference strength** — how strongly evaluators favour a candidate;
- **reliability** — how trustworthy each evaluator currently is;
- **relevance** — whether that evaluator is competent for this state / question;
- **dependence** — whether apparent votes share the same evidence or failure mode;
- **alignment** — whether evaluators actually point toward the same candidate / relation;
- **diversity** — whether the evaluator family remains meaningfully heterogeneous.

The purpose of these notes is to define candidate measurements, not choose one prematurely.

---

## 2. Evaluator representation

Let evaluator `i` emit a vector over `K` candidate actions / hypotheses / interventions:

\[
v_i \in \mathbb{R}^K.
\]

Its current reliability and task relevance are represented by non-negative weights:

\[
r_i,\; q_i \in [0,1].
\]

A simple effective weight is:

\[
w_i = r_i q_i.
\]

This is only a placeholder. In REE, reliability and relevance may be multi-dimensional and state-dependent rather than one scalar.

Before comparing directions, vectors should usually be centred or converted to relative preference so that a globally optimistic evaluator does not look aligned merely because all entries are positive.

---

## 3. Ordinary aggregate pull

The ordinary weighted preference is:

\[
P = \sum_i w_i v_i.
\]

For action `a`, `P_a` is the aggregate weighted pull toward that candidate.

This is **not** the convergence signal.

A single high-weight evaluator can make `P_a` large even when every other evaluator disagrees.

Thus `P` answers:

> what does the weighted coalition currently favour?

whereas convergence should answer something like:

> how independently and robustly is that direction supported?

---

## 4. Directional alignment candidate

One scale-free first-pass convergence measure is:

\[
C_{dir} = 
\frac{\left\|\sum_i w_i \hat{v}_i\right\|}
     {\sum_i w_i + \epsilon},
\]

where `\hat{v}_i` is the unit-normalised centred evaluator vector.

Interpretation:

- near `1`: weighted evaluators point in similar directions;
- near `0`: vectors cancel or point orthogonally;
- intermediate: partial coalition structure.

### Limitation

This counts correlated clones as independent supporters. It is therefore not sufficient.

---

## 5. Pairwise alignment view

A complementary quantity is weighted pairwise agreement:

\[
C_{pair} =
\frac{\sum_{i<j} w_iw_j\cos(\hat v_i,\hat v_j)}
     {\sum_{i<j}w_iw_j + \epsilon}.
\]

This makes disagreement topology inspectable rather than hiding it in one resultant vector.

It also permits a coalition graph:

```text
node = evaluator
edge weight = task-relative agreement
node weight = reliability / relevance
```

Clusters can then reveal:

- broad convergence;
- two competing coalitions;
- one dominant specialist against a weak majority;
- isolated dissent;
- fragmentation.

This may be more useful diagnostically than a single scalar.

---

## 6. Independence correction

### 6.1 Error covariance

Suppose evaluator residual errors can be estimated over an appropriate history or held-out calibration set. Let:

\[
\Sigma_{ij} = \operatorname{Cov}(e_i,e_j).
\]

Highly correlated residual errors imply duplicated evidence.

A statistical analogue is to weight sources by something related to inverse covariance:

\[
w^* \propto \Sigma^{-1} w.
\]

This is not automatically the correct biological implementation. It is a useful upper-bound / analysis tool.

### 6.2 Effective number of evaluators

A simpler diagnostic quantity is an effective source count. If normalised source weights are `p_i`, an entropy-style effective number is:

\[
N_{eff}=\exp\left(-\sum_i p_i\log p_i\right).
\]

But this only corrects unequal weights, not correlated errors.

A dependence-adjusted `N_eff` should fall when sources have shared upstream ancestry or correlated failure.

### 6.3 Causal ancestry correction

REE has an advantage over a biological observer: its computation graph is partly known.

For evaluators A and B we can annotate:

- shared input fraction;
- shared latent bottleneck;
- shared training objective;
- direct parent/child relation;
- evidence copied through replay / memory;
- shared model checkpoint or teacher.

This may allow a **causal redundancy penalty** even before robust empirical covariance estimates exist.

---

## 7. Candidate independence-aware convergence

A general form is:

\[
C = \mathcal{A}(\{v_i\},\{w_i\},D),
\]

where `D` is a dependency / covariance structure.

One analysis-only candidate is:

\[
C_{ind} =
\frac{\left\|\sum_i \tilde w_i \hat v_i\right\|}
     {\sum_i \tilde w_i + \epsilon}
\cdot g(N_{eff}^{dep}),
\]

where `\tilde w_i` are dependence-corrected weights and `g` increases sublinearly with effective independent support.

The sublinear term matters: ten weak independent votes should not necessarily overwhelm one protected veto simply because ten is larger than one.

---

## 8. Convergence versus confidence

A major rival is that convergence adds nothing beyond ordinary posterior confidence.

Therefore experiments must compare:

```text
confidence-only model
vs
reliability-aware confidence model
vs
independence-aware convergence model.
```

A valid convergence metric should add value in regimes where two candidate states have equal aggregate confidence but different **support topology**.

Example:

```text
State A:
  one highly confident model supplies almost all support.

State B:
  four moderately reliable, independent models converge.

Aggregate confidence is matched.
```

If B is more robust to perturbation / distribution shift and convergence predicts that robustness, the quantity earns explanatory value.

---

## 9. Convergence and value of computation

Let unknown or question `q` affect models `M_1...M_n`.

Standard epistemic value might be approximated by expected information gain:

\[
IG(q)=\mathbb E[H(M)-H(M\mid o_q)].
\]

The new proposal is not simply to multiply by number of models.

A candidate **cross-model epistemic leverage** is:

\[
L(q)=\sum_i \alpha_i\,\mathbb E[\Delta U_i\mid q],
\]

where `\Delta U_i` is expected useful uncertainty reduction in model `i` and `\alpha_i` discounts redundant models / low decision relevance.

A stronger quantity could include interaction:

\[
X(q)=L(q)+\lambda\,\mathbb E[\Delta C_{models}\mid q],
\]

where `\Delta C_{models}` asks whether the observation is expected to resolve disagreement or establish a reusable common structure.

This would distinguish:

```text
interesting because uncertain
```

from:

```text
interesting because resolving it may reorganise several models at once.
```

---

## 10. Aha / insight candidate metrics

Suppose before insight the system has several representations / predictive models `M_i`, and a new abstraction `Z` becomes available.

A computational Aha candidate should not be triggered by compression alone. A degenerate constant representation is maximally simple and useless.

Require some combination of:

### 10.1 Complexity reduction

\[
\Delta K = K_{before} - K_{after} > 0
\]

where `K` may be Minimum Description Length, model size, number of independent rules, or another task-appropriate complexity proxy.

### 10.2 Predictive improvement or preservation

\[
\Delta E = E_{before} - E_{after} \ge 0
\]

on held-out data / future trajectories.

### 10.3 Cross-view integration

A new abstraction should explain multiple previously separate relations:

\[
I = \#\{M_i : Z \text{ yields held-out gain or lawful simplification}\}.
\]

Again this should use effective independence rather than raw count.

### 10.4 Suddenness

Subjective Aha is associated with suddenness, but the cognitive change may sometimes be gradual.

Define change-point magnitude over time:

\[
S_t = \left\|R_t - R_{t-1}\right\|
\]

or a more meaningful task-relative restructuring quantity.

The **computational insight event** and **phenomenological Aha signal** should remain separable:

```text
restructuring may occur without strong Aha;
strong confidence/reward may feel Aha-like without deep restructuring.
```

---

## 11. Diversity metric

Convergence is only meaningful if diversity remains.

Possible evaluator-diversity diagnostics include:

- residual-error covariance;
- representational similarity / dissimilarity;
- intervention response diversity;
- distinct dependency ancestry;
- distinct failure sets;
- policy disagreement in diagnostic environments;
- parameter / architecture diversity only as weak proxies.

A simple target should **not** be `maximize diversity`.

Useful diversity is diversity of *routes/failure modes* while preserving competence.

One can imagine a Pareto surface:

```text
competence
robustness
useful diversity
convergence when warranted
```

rather than a scalar objective.

---

## 12. Vetoes and asymmetric evidence

A majority-style convergence signal must not erase asymmetric consequences.

For protected harm or irreversible catastrophe, one reliable negative evaluator may deserve nonlinear authority.

Possible structure:

```text
eligible only if protected constraints clear;
within eligible set, convergence informs confidence / compute allocation;
```

or:

\[
Authority(a)=VetoGate(a)\times F(P_a,C_a,uncertainty,...)
\]

where `VetoGate` cannot be bought off by many weak positive votes.

This fits REE better than treating every channel as commensurable evidence.

---

## 13. Dropout robustness as a practical proxy

One very useful operational measure may be **support robustness under evaluator ablation**.

For candidate `a`, repeatedly remove one evaluator or one dependency cluster and recompute the selected direction.

Define:

\[
R_{drop}(a)=P(\text{same decision under lawful evaluator dropout}).
\]

This directly tests whether “agreement” reflects distributed support or one hidden monarch.

It may also be easier to interpret than a sophisticated independence scalar.

Potentially:

```text
high convergence + high dropout robustness = broad support
high convergence + low dropout robustness = apparent consensus hiding a dominant source
```

---

## 14. First experimental mathematics target

Before any REE-native use, create a synthetic environment with known evaluator dependencies.

Manipulate independently:

- evaluator accuracy;
- pairwise error correlation;
- number of evaluators;
- one protected veto;
- context relevance;
- one high-reliability minority expert;
- distribution shift.

Compare:

```text
max
simple sum
majority vote
confidence-weighted sum
Bayesian / oracle combiner
independence-aware convergence
```

Readouts:

- action accuracy;
- calibration;
- distribution-shift robustness;
- evaluator-dropout robustness;
- value-of-computation decisions;
- preservation of expert diversity.

Only a metric that earns something beyond standard weighting should proceed.

---

## 15. Current mathematical posture

The attractive idea is not one magic formula.

The likely useful object is a small **diagnostic bundle**:

```text
aggregate pull P
+ reliability / precision
+ convergence topology C
+ dependency / redundancy D
+ structured dissent
+ dropout robustness
```

The control system can then ask different questions of the same bundle.

Action selection may care about `P` plus vetoes.
Information hunger may care about disagreement and cross-model leverage.
Closure may care about convergence plus expected value of more computation.
Insight detection may care about sudden cross-model restructuring.

That is more consistent with REE's “umpire, not ruler” philosophy than introducing another universal scalar.
