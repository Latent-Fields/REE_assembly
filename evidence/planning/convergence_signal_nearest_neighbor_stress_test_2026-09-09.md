# Convergence as a General Computational Signal — Nearest-Neighbour Stress Test

**Date:** 2026-09-09  
**Status:** completed first stress-test tranche; literature-informed; no claim registration, promotion, or experiment queue mutation  
**Parent thought:** `docs/thoughts/2026-09-09_convergence_as_general_computational_signal.md`  
**Related:** `evidence/planning/convergence_signal_literature_review.md`, `docs/thoughts/2026-09-09_convergence_signal_formal_notes.md`, `docs/thoughts/2026-09-09_diversity_vs_convergence.md`, `docs/thoughts/2026-09-09_aha_as_cross_model_restructuring.md`

---

## 1. Executive result

The original intuition survives, but its novelty boundary has moved.

The strongest defensible formulation is **not**:

> agreement among several systems is a wholly new kind of computational signal.

There is already direct prior art for parts of that statement.

Instead, the interesting REE hypothesis is now:

> **A bounded cognitive architecture may use the independence-aware topology of agreement and disagreement among heterogeneous evaluators as a meta-control signal: convergence can support confidence/closure, structured divergence can support information allocation, and a restructuring that converts several previously discordant views into one lower-complexity predictive structure can be treated as an insight candidate.**

The phrase **independence-aware** is load-bearing. Agreement between duplicated or strongly coupled evaluators is not equivalent to convergence between routes with genuinely different evidence histories, assumptions, representations, or failure modes.

This stress test therefore converts the original single notion of “convergence signal” into a more discriminating **convergence–divergence geometry**.

---

## 2. Direct nearest neighbour: confidence through consensus

### Paz et al. 2016 — the closest computational prior art found so far

Luciano Paz et al., *Confidence through consensus: a neural mechanism for uncertainty monitoring*, Scientific Reports 6:21830 (2016), DOI `10.1038/srep21830`.

The model proposes many loosely coupled modules, each integrating a stochastic sample of the same sensory evidence. Modules vote on the decision; the **dispersion across modules** is used as a confidence signal. Critically, as inter-module coupling grows, dispersion ceases to track task reliability well even when mean task accuracy and response time remain broadly similar.

This is extremely close to one branch of the REE thought:

```text
parallel partially independent evaluations
             ↓
pattern of agreement / dispersion
             ↓
confidence about the resulting decision
```

It also independently supplies the exact warning REE had already reached from first principles:

> **If the modules are too coupled, apparent consensus loses epistemic value.**

### What this prior art does and does not pre-empt

It substantially pre-empts any novelty claim that REE invented “confidence from consensus among parallel modules.”

It does **not** cover the full proposed REE scope:

- its modules are redundant samplers of one sensory-evidence process, not heterogeneous systems with different representational objects or objectives;
- it does not use disagreement to allocate information-seeking across problems;
- it does not address structural convergence among alternative models/representations;
- it does not connect consensus geometry to developmental preservation of evaluator diversity;
- it does not treat an `aha` as cross-view restructuring.

**Verdict:** direct prior art for the confidence branch; strong constraint on novelty language; strong support for keeping independence/coupling explicitly measurable.

---

## 3. Reliability arbitration is a serious simpler explanation

### Lee, Shimojo & O'Doherty 2014

*Neural computations underlying arbitration between model-based and model-free learning*, Neuron 81:687–699, DOI `10.1016/j.neuron.2013.11.028`.

Human behaviour and fMRI were consistent with arbitration of model-based versus model-free control using the **relative reliability of their predictions**. Inferior lateral prefrontal/frontopolar signals represented reliability and comparison of reliabilities.

For REE this is an important rival:

```text
system A reliability
system B reliability
      ↓
weighted arbitration
```

may be sufficient without an extra “agreement signal.”

### Multisensory reliability weighting

Ernst & Banks 2002 showed visual and haptic cues being combined approximately according to their reliabilities, close to maximum-likelihood integration (`10.1038/415429a`). A large multisensory literature generalizes reliability-dependent weighting.

### Consequence for novelty

If the architecture already knows:

- each evaluator's likelihood model;
- each evaluator's reliability;
- all pairwise/shared-source covariance;
- and the correct generative structure;

then a normatively correct Bayesian integrator already contains the informational value of agreement. A separate “convergence bonus” would be redundant or potentially double-count evidence.

Therefore REE should **not** claim that an independence-aware convergence signal outperforms a fully specified Bayesian aggregator.

The more defensible role is:

> **a bounded metacognitive heuristic / control observable that approximates useful second-order information when the organism cannot perform exact joint inference over every evaluator and dependency.**

This is a substantial sharpening of the original thought.

---

## 4. Divergence is already an information-seeking signal

The most important complementary prior art comes from machine learning.

### Query by Committee

Freund, Seung, Shamir & Tishby, *Information, Prediction, and Query by Committee* (NIPS 1992) formalizes active learning in which **disagreement among plausible committee members identifies informative queries**.

That gives the other sign of the REE signal:

```text
credible model agreement   → confidence / closure candidate
credible model disagreement → information-seeking candidate
```

This immediately prevents the convergence project from becoming “maximize agreement.”

### Epistemic value / active inference

Friston et al. 2015 formalize epistemic value as expected information gain; curiosity/information seeking continues while actions are expected to reduce uncertainty. Reviews of information seeking similarly distinguish uncertainty, information gain, learning progress, novelty and value-of-information criteria.

The new REE contribution, if it survives, would therefore be narrower:

> **use the structure of disagreement among heterogeneous internal views as one cheap estimate of where information gain is likely to be available.**

Disagreement is not automatically useful. Irreducible noise, a broken evaluator, or an out-of-domain subsystem can disagree forever without offering learnable information.

---

## 5. Independent convergence really can carry epistemic information

### Pfänder, De Courson & Mercier 2025

*How wise is the crowd: Can we infer people are accurate and competent merely because they agree with each other?*, Cognition 255:106005, DOI `10.1016/j.cognition.2024.106005`.

Analytical/simulation results show that, under broad conditions with **independent and unbiased estimates**, informants whose answers converge tend to be more accurate and competent. Human participants also infer greater competence from convergence; the inference weakens when informants are systematically biased.

This is unusually close to the proposed epistemic interpretation:

> convergence is informative conditional on assumptions about independence and bias.

It is not evidence for the REE mechanism, but it helps establish that the intuition has normative content.

### 2026 probability-aggregation evidence

A 2026 Cognitive Science analysis of 451,200 probability judgments reports that lower inter-judge correlation/diversity contributes to group accuracy and compares majority, unanimity, probability averaging and log-odds aggregation.

Again, the important quantity is not head-count consensus alone. **Correlation structure matters.**

---

## 6. Diversity is not merely tolerated; it is part of the computation

The wisdom-of-crowds/collective-intelligence literature repeatedly shows that correlated errors can destroy the benefit of aggregation. Social influence can make opinions converge without increasing truth contact. Recent work even shows that inducing divergent estimates can sometimes improve aggregate accuracy because errors cancel more effectively.

This directly supports the companion thought `2026-09-09_diversity_vs_convergence.md`:

> **Rewarding agreement can destroy the independence that made agreement informative.**

A convergence-aware architecture therefore needs active protection against:

- shared upstream representations making nominally separate evaluators duplicate one another;
- evaluator training causing co-adaptation/herding;
- the dominant evaluator teaching the others to agree;
- one common error source being counted many times;
- minority reports being suppressed merely because the majority is confident.

A useful implementation cannot simply count modules. It must estimate **effective independent evidence**.

Candidate proxies include:

- provenance / ancestry overlap;
- shared training data or replay episodes;
- empirical residual/error correlation;
- common input dependence;
- shared parameters or latent sources;
- response covariance under controlled perturbations;
- lesion/dropout redundancy.

---

## 7. Insight: strong nearby theory, but a possible narrower REE discriminator remains

### Representational change theory and insight neuroscience

Insight research already treats restructuring/re-representation as central. Kounios & Beeman's 2014 review defines insight around sudden reinterpretation producing a non-obvious solution; representational-change work emphasizes constraint relaxation and re-encoding.

### Active inference account of curiosity and insight

Friston et al. 2017, *Active Inference, Curiosity and Insight*, DOI `10.1162/neco_a_00999`, goes further. In simulations, curiosity samples contingencies to close explanatory gaps, while **Bayesian model reduction / structure learning** over candidate invariances produces events with the hallmarks of `aha` moments.

Laukkonen and colleagues' later “insight as precision” work similarly treats implicit restructuring/Bayesian reduction plus a precision-weighted prediction error as a possible basis for the confidence, pleasure and attentional capture of insight.

### Consequence for the REE `aha` thought

REE should not claim novelty for:

```text
aha = model reduction / restructuring + confidence
```

That territory is already occupied.

The potentially distinctive operationalization is narrower:

> **A candidate insight is especially interesting when one new representation simultaneously reduces predictive/description complexity across several previously useful but partly independent views, and survives held-out reality checks.**

This makes “cross-model convergence” a proposed **measurement signature** of some restructuring events, not a universal definition of subjective insight.

---

## 8. Revised computational object: convergence–divergence geometry

Let evaluators `E_i` produce candidate-relative outputs `v_i(a)`, reliabilities `r_i`, and dependency structure `D_ij`.

The useful object is not merely:

```text
S(a) = Σ_i r_i v_i(a)
```

because this is ordinary weighted integration.

Instead expose second-order quantities such as:

```text
agreement topology
error/dependency covariance
which independent routes agree
which credible routes dissent
whether dissent is structured and resolvable
whether a new representation collapses several disagreements at once
```

A schematic family is:

```text
C(a) = convergence among competent approximately independent routes
D(a) = structured disagreement among competent approximately independent routes
```

with neither quantity granted authority by itself.

Possible control readings:

```text
high C + low consequential D  → confidence / closure pressure
high structured D             → information-hunger / diagnostic pressure
high D + no reducible query    → tolerate uncertainty or disengage
new representation lowers D across several views while improving held-out prediction
                              → restructuring / insight candidate
```

This is not yet a claim or implementation.

---

## 9. The decisive experiments have changed

### Test 1 — duplicated-vote trap

Construct evaluator ensembles with the same nominal vote count and similar individual accuracy but different dependency structures.

- A: five genuinely independent evaluators;
- B: one evaluator copied five times;
- C: five evaluators sharing one hidden bias;
- D: mixed independent + correlated cluster.

A raw vote/sum should be fooled. An independence-aware estimator should not.

### Test 2 — exact Bayes ceiling

In a synthetic world where the full joint generative model and covariance are known, compare:

1. exact Bayesian aggregation;
2. reliability-weighted sum;
3. naïve consensus count;
4. independence-aware convergence heuristic.

The convergence heuristic **must not be expected to beat exact Bayes**. Its question is whether it approaches the Bayes decision/confidence at substantially lower representational/computational cost and degrades gracefully when dependency estimates are approximate.

If it adds no bounded-resource benefit, the general signal is unnecessary.

### Test 3 — disagreement as query selector

Create several competent models whose predictions diverge only in specific environmental regions.

Compare information-seeking driven by:

- global uncertainty;
- expected information gain (oracle/gold standard where calculable);
- raw disagreement;
- independence-aware structured disagreement.

The candidate signal earns its keep only if it identifies useful queries above cheap baselines and avoids irreducible-noise traps.

### Test 4 — preserve diversity

Reward agreement and observe whether evaluator error correlation increases over development. Then introduce protected independent training/provenance or decorrelation pressures.

Success requires:

- maintaining individual competence;
- retaining useful dissent;
- preventing apparent confidence from rising merely because evaluators became copies.

### Test 5 — synthetic `aha`

Construct a world where several separately useful models encode different projections of one hidden invariant.

At some point introduce/learn a shared abstraction.

Measure before/after:

- held-out prediction error per view;
- joint minimum description length / model complexity;
- number of separate parameters/rules required;
- cross-view disagreement;
- ability to derive previously separate predictions from one structure.

A compelling computational `aha` signature would be:

```text
joint complexity ↓
held-out predictive reach ↑ or preserved
cross-view disagreement ↓
without simply deleting a dissenting model
```

This distinguishes genuine restructuring from confidence inflation or forced consensus.

---

## 10. What would falsify or dissolve the REE-specific proposal

The proposal should be abandoned or reduced to ordinary arbitration if:

1. correct reliability/covariance weighting explains every benefit with no need for a separate meta-control observable;
2. independence cannot be estimated cheaply enough to make convergence useful;
3. disagreement fails to predict information value above ordinary uncertainty/information-gain measures;
4. preserving evaluator diversity costs more competence than it saves;
5. apparent cross-view `aha` compression does not predict held-out generalization or future problem solving;
6. the same behaviours emerge more simply from confidence, uncertainty and value-of-information signals already present in REE.

---

## 11. Novelty decision

**Do not mint a broad “convergence is a general computational signal” claim yet.**

The literature has now shown that important pieces are already established:

- consensus/dispersion can encode confidence;
- reliability can arbitrate between controllers;
- disagreement can drive active learning;
- independent convergence can rationally imply accuracy/competence;
- diversity/correlation structure determines whether aggregation helps;
- model reduction/restructuring already provides a computational account of insight.

The remaining candidate novelty is a **REE-level synthesis and control architecture** linking these pieces through provenance-aware convergence/divergence across heterogeneous systems.

That is a narrower and better hypothesis than the starting formulation.

---

## 12. Operational line after stress test

> **Do not reward agreement. Measure the structure that produced it. Independent convergence can support closure; credible divergence can identify where to learn; restructuring earns an `aha` interpretation only when it makes several views simpler and more predictively coherent without erasing reality-facing dissent.**
