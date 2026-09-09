# Convergence as a General Computational Signal — Literature Review Seed

**Date:** 2026-09-09  
**Status:** initial targeted literature pass; incomplete review; no claim registration  
**Parent thought:** `docs/thoughts/2026-09-09_convergence_as_general_computational_signal.md`

## 1. Review question

The target is narrower than “how does the brain make decisions?” and broader than “how do ensembles vote?”

> **Is there established theory or evidence that agreement among partially independent cognitive/evaluative systems is itself represented or exploited as a distinct computational signal?**

The review must distinguish four neighbouring ideas:

1. multiple systems contribute to one action;
2. their outputs are converted into a common currency;
3. an arbitrator weights systems by reliability/context;
4. the **degree and structure of cross-system agreement itself** changes what the organism does next.

Only (4) is the proposed new centre of gravity.

---

## 2. Initial evidence matrix

### A. Biological degeneracy — strong foundation, not convergence signal

**Edelman GM, Gally JA (2001). _Degeneracy and complexity in biological systems._ PNAS 98:13763–13768. DOI: 10.1073/pnas.231499798.**

Degeneracy is the capacity of structurally different elements to yield the same output. It supports robustness, adaptability and evolvability.

**Relevance:** establishes that many-to-one functional mappings are normal in biology and therefore that multiple routes may legitimately bear on the same behavioural problem.

**Boundary:** the paper does not propose that an organism computes “how many independent routes agree” and uses that agreement as a meta-signal.

**Noppeney, Friston & Price (2004). _Degenerate neuronal systems sustaining cognitive functions._ J Anat / related review literature.**

Multiple neuronal systems can sustain the same cognitive function, either simultaneously or as latent compensatory routes.

**Relevance:** supports within-organism plurality of mechanisms.

**Boundary:** degeneracy can exist without online arbitration or convergence detection.

### B. Basal ganglia action selection — strong foundation for plural inputs and constitutional arbitration

**Mink JW (1996). _The basal ganglia: focused selection and inhibition of competing motor programs._ Progress in Neurobiology 50:381–425. DOI: 10.1016/S0301-0082(96)00042-1.**

The basal ganglia are framed as selecting desired actions while suppressing competing actions.

**Relevance:** supports the REE intuition that action selection is not simply one value channel issuing a command.

**Boundary:** focused selection is not the same as measuring independent evidential convergence.

**Costa RM (2019). _What, If, and When to Move: Basal Ganglia Circuits and Self-Paced Action Initiation._ Annual Review of Neuroscience 42:459–483. DOI: 10.1146/annurev-neuro-072116-031033.**

The striatum receives information about goals, context and actions from several cortical/thalamic sources, alongside dopaminergic modulation.

**Relevance:** supports state-dependent weighting of heterogeneous information at a selector.

**Boundary:** evidence does not imply a dedicated consensus signal.

**2026 policy-controller review:** current work arguing for basal ganglia as a policy-based controller further weakens overly simple discrete-action lookup interpretations and emphasizes rich context-dependent control.

**Relevance:** compatible with dynamic state-dependent voting power.

**Boundary:** still not direct evidence for convergence as a meta-variable.

### C. Arbitration between controllers — nearest established neighbour

**Daw ND, Niv Y, Dayan P (2005). _Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control._ Nature Neuroscience 8:1704–1711.**

Normative account of arbitration between competing choice systems based on uncertainty/reliability.

**Relevance:** very close prior art. It establishes that the brain may need a second-order computation over the quality of distinct controllers.

**Difference:** arbitration chooses or weights controllers based on estimated reliability. It does not necessarily assign extra value because several independent controllers converge on the same candidate.

**Lee SW, Shimojo S, O'Doherty JP (2014). _Neural computations underlying arbitration between model-based and model-free learning._ Neuron 81:687–699. DOI: 10.1016/j.neuron.2013.11.028.**

Behavioural control shifts as a function of the reliability of model-based and model-free predictions; inferior lateral prefrontal/frontopolar cortex carries reliability and comparison signals.

**Relevance:** strong evidence that reliability comparison across controllers can be an explicit meta-computation.

**Difference:** the critical variable is relative reliability, not cross-controller agreement per se. A convergence-signal theory should reduce to ordinary arbitration where only reliability matters and should demonstrate added value in cases where several competent routes independently agree.

### D. Common-currency accounts — important rival

**Levy DJ, Glimcher PW (2012). _The root of all value: a neural common currency for choice._ Current Opinion in Neurobiology 22:1027–1038.**

Meta-analysis/review literature supports common value coding in vmPFC/OFC across heterogeneous rewards.

**Relevance:** a scalar common currency is the cleanest rival to a plural-convergence architecture.

**Challenge to the present thought:** if all action-relevant variables can be lawfully converted into one value representation and confidence adequately attached to that value, a separate convergence signal may be unnecessary.

**Sripada C (2026). _The case for value as a common currency in decision-making and intersystem competition._ Frontiers in Cognition. DOI: 10.3389/fcogn.2026.1767189.**

Recent defence/refinement of common-currency approaches, distinguishing decision/learning phases and option/meta levels.

**Relevance:** especially important because it explicitly addresses competition between dissimilar psychological systems.

**Negative-evidence role:** convergence must outperform or explain phenomena not captured by a well-formed meta-level common currency, rather than merely rename common valuation.

### E. Exploration and information value — foundation for epistemic allocation

**Daw ND et al. (2006). _Cortical substrates for exploratory decisions in humans._ Nature 441:876–879. DOI: 10.1038/nature04766.**

Separates exploratory information gathering from exploitative value-guided behaviour in a computationally defined task.

**Relevance:** supports information seeking as a real competing behavioural mode rather than free preprocessing.

**Friston K et al. (2015). _Active inference and epistemic value._ Cognitive Neuroscience 6:187–214. DOI: 10.1080/17588928.2015.1020053.**

Expected free energy decomposes into pragmatic/extrinsic and epistemic/information-seeking value.

**Relevance:** gives a formal rival in which information hunger and goal value already coexist in one policy objective.

**Difference:** epistemic value concerns expected information gain. The proposed convergence signal adds the possibility that one unknown has unusually high value because resolving it simultaneously updates several partially independent models.

**_Curiosity and the dynamics of optimal exploration_ (Trends in Cognitive Sciences, 2024; DOI 10.1016/j.tics.2024.02.001).**

Review integrates uncertainty/information gain with learning progress, explicitly discussing curiosity as a common currency for exploration balanced against drives such as safety and hunger.

**Relevance:** very close to the information-hunger portion of the thought.

**Open discriminator:** does “cross-model impact” improve exploration beyond uncertainty, information gain and learning progress?

### F. Homeostatic multi-drive models — foundation for competing needs

**Neurocomputational theories of homeostatic control (2019 review; PMID 31395433).**

Homeostatic reinforcement-learning models can capture interactions among competing physiological needs, satiety and risk.

**Relevance:** supports the idea that action value is state-dependent because internal needs change the weighting of outcomes.

**Boundary:** competing drives can be integrated without any convergence-sensitive meta-signal.

### G. Insight / representational change — foundation for the “aha” branch

**Kounios J, Beeman M (2014). _The Cognitive Neuroscience of Insight._ Annual Review of Psychology 65:71–93. DOI: 10.1146/annurev-psych-010213-115154.**

Insight has distinct phenomenology and neural correlates, including internally focused attention and coarse semantic processing.

**Wiley J, Danek AH (2024). _Restructuring processes and Aha! experiences in insight problem solving._ Nature Reviews Psychology 3:42–55.**

Modern review distinguishes cognitive restructuring from the phenomenological Aha experience and emphasizes that the two should not be collapsed.

**Danek AH, Williams J, Wiley J (2020). _Closing the gap: connecting sudden representational change to the subjective Aha! experience in insightful problem solving._ Psychological Research 84:111–119. DOI: 10.1007/s00426-018-0977-8.**

Sudden change toward a correct representation was associated with stronger Aha reports than incremental change.

**Becker M, Sommer T, Cabeza R (2025). _Insight predicts subsequent memory via cortical representational change and hippocampal activity._ Nature Communications 16:4341.**

Links insight with representational change and later memory.

**Relevance:** supports representational change as a real measurable component of insight.

**Boundary:** none of these sources, on this first pass, establish the specific proposal that insight is a **cross-model convergence event** in which one abstraction simultaneously simplifies multiple partially independent representations.

That proposed metric therefore remains hypothesis-generating.

### H. Statistical analogues — useful mathematics, not biology

**Bayesian model averaging** provides a principled way to combine predictions across uncertain models while accounting for their posterior support.

**Relevance:** shows that prediction across multiple models can be superior to premature model selection.

**Boundary:** standard BMA does not automatically treat independent agreement as an extra signal; agreement influences the posterior/predictive distribution through the models and data.

**Mixture-of-experts / gating models** provide a machine-learning analogue in which specialist systems are selectively weighted by a gate.

**Relevance:** useful baseline for REE experiments.

**Boundary:** a gate trained to route among experts is not the same as detecting meaningful cross-expert convergence; naive gating can also collapse expert diversity.

---

## 3. Preliminary novelty judgement

The first pass finds abundant support for all of the ingredients:

```text
multiple controllers
+ state-sensitive drive weighting
+ reliability-based arbitration
+ common-currency integration
+ epistemic value
+ biological degeneracy
+ representational restructuring in insight
```

What is not yet obvious in the literature is one unified principle saying:

> **the unexpected agreement of relatively independent evaluators is itself represented as a general-purpose meta-signal used across action selection, epistemic allocation and representational revision.**

That absence should not be interpreted as novelty proof. It sets the target for a deeper prior-art search.

---

## 4. Negative-evidence programme

The investigation should actively search for evidence that makes the convergence proposal unnecessary or unsafe.

### Rival R1 — common currency is sufficient

If a confidence-weighted common value signal predicts action, stopping and exploration as well as a convergence-sensitive system, then convergence may be an explanatory re-description rather than an additional computation.

### Rival R2 — reliability arbitration is sufficient

If optimal behaviour depends only on controller reliability/relevance and not on how many independent controllers agree, then Lee/Daw-style arbitration may already contain the required computation.

### Rival R3 — convergence is merely correlated confidence

Agreement may simply increase confidence in an ordinary Bayesian model. A distinct convergence variable is justified only if it adds explanatory or control value beyond posterior confidence.

### Rival R4 — diversity is more valuable than agreement

Selection for convergence could homogenise models, induce groupthink and reduce robustness or exploratory reach.

### Rival R5 — independence cannot be estimated online

If shared causal ancestry among evaluators cannot be identified cheaply enough, convergence estimates may systematically overcount duplicated evidence.

### Rival R6 — insight does not require sudden restructuring

Insight literature already shows that restructuring is not exclusive to Aha solutions and impasse is not mandatory. Any computational Aha theory must allow gradual representational convergence and distinguish the subjective appraisal from the underlying restructuring.

---

## 5. Literature debts for the next pass

Before claim intake, targeted searches are still owed on:

1. **multi-attribute / multi-motive action integration** in striatum, OFC, vmPFC and hypothalamic–striatal interactions;
2. **basal-ganglia parallel loops / convergence zones** for limbic, associative and motor information;
3. **metacontrol beyond two-controller arbitration**, including reliability and uncertainty arbitration among more than two systems;
4. **conflict monitoring and consensus**, especially anterior cingulate / prefrontal signals that distinguish agreement from conflict;
5. **ensemble diversity and correlated-error correction** in statistics/machine learning;
6. **collective intelligence / wisdom-of-crowds conditions** as an explicit independence analogue, with special attention to correlated errors;
7. **curiosity and cross-domain learning progress** — whether exploration is preferentially allocated to queries that improve several models/tasks at once;
8. **compression / minimum-description-length accounts of insight**, if any, versus restructuring-only accounts;
9. **subjective Aha and prediction-error / confidence dynamics**;
10. **pathological premature convergence** analogues: habits, delusions, groupthink, compulsive certainty, attractor dominance.

---

## 6. Intake posture

**No claim should be minted from this initial literature pass.**

The correct next sequence is:

```text
REE archaeology
→ deeper nearest-neighbour literature pull
→ formal metrics
→ synthetic discriminators
→ only then claim overlap / minting decision
```

The strongest current statement is that the thought sits at a plausible intersection of several established literatures while the proposed **cross-view convergence meta-signal** itself remains insufficiently established.
