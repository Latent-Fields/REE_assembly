# Friston et al. 2015 — Active inference and epistemic value

**Citation.** Friston K, Rigoli F, Ognibene D, Mathys C, Fitzgerald T, Pezzulo G. (2015). Active inference and epistemic value. *Cognitive Neuroscience* 6(4):187-214. [DOI](https://doi.org/10.1080/17588928.2015.1020053). PMID 25689102.

## What the paper does

This is a foundational treatment of the active-inference framework with explicit focus on the exploration-exploitation problem. Friston and colleagues show that minimising expected free energy is mathematically equivalent to maximising the sum of (a) extrinsic value — utility or pragmatic reward — and (b) epistemic value — information gain about the causes of outcomes. The decomposition is exact under the framework's assumptions, and the implication is that a single quantity (expected free energy) generates both the exploratory and exploitative behaviour an agent should display, with the exploratory weight scaling with how much information remains to be gained.

A key consequence is that softmax temperature parameters in standard choice models become reinterpretable as the precision of beliefs about policies, not as a free behavioural-noise knob. Phasic dopamine discharges, the paper argues, may correspond to precision updates rather than to raw prediction error — a framework-level reinterpretation of the canonical RPE literature.

## Relevance to Q-044

If the brain implements active inference, then MECH-314a (novelty bonus), MECH-314b (uncertainty bonus), and MECH-314c (learning-progress bonus) are all readings of the same epistemic-value computation with different priors over which features the agent treats as informative. Novelty is information gain about the structure of the state space; uncertainty is information gain about an outcome distribution; learning progress is the time-derivative of information gain. All three are mathematically related quantities derived from the agent's belief state.

This makes Friston 2015 the LOAD-BEARING anchor for one specific Q-044 resolution outcome: the COLLAPSE-ALL option in the claim's notes — "All three collapse (one signature): collapse to a single MECH-314 with notes documenting the collapse." Under active inference, the three-arm ablation might not produce three distinct failure signatures — it might produce one general "epistemic-blind" signature when the unified mechanism is disabled, and three specialised forms only if the unified computation happens to map onto three anatomically separable substrates.

## Caveats

I have to push back on my own reasoning here. Active inference is a normative-mathematical framework — it says what an OPTIMAL agent SHOULD compute, not what brains DO compute. Wittmann 2007 and Daw 2006 supply empirical evidence for at least partial substrate-level separation between novelty (SN/VTA) and uncertainty (frontopolar cortex). That separation is compatible with the brain implementing the unified normative quantity via multiple anatomical substrates — like having three calculators that each compute one term of a known sum.

So the empirical question Q-044 asks is not exactly the same as the normative question active inference addresses. A "three substrates" outcome would not refute active inference (the brain could be approximating the normative quantity with three specialised paths). A "one substrate" outcome would be consistent with active inference but also with simpler accounts. The Q-044 falsifier needs to distinguish substrate architecture, not normative correctness.

I am also aware that the active-inference formalism for epistemic value is information gain over a posterior (KL divergence between prior and posterior beliefs), not learning progress as a time-derivative of prediction error. The Schmidhuber/Kaplan-Oudeyer learning-progress quantity sits adjacent to but is not identical with active-inference epistemic value. So Friston 2015's collapse-all argument applies more cleanly to novelty-vs-uncertainty than to all three sub-flavours together.

## Why the "mixed" direction

I tagged this as mixed rather than supports because Friston 2015 supports ONE Q-044 outcome (collapse) and weakens the substrate-level evidence for any of the three retain-three or retire-one outcomes. It is informative for Q-044 in either direction depending on which outcome holds — and as a theoretical paper, its weight is in the framing rather than in providing evidence one way or the other.

## Confidence reasoning

I assign 0.60. Source quality (0.70) is modest (theoretical paper in Cognitive Neuroscience). Mapping fidelity (0.65) is moderate — the unification thesis maps onto the COLLAPSE-ALL outcome but only loosely covers learning-progress alongside novelty and uncertainty. Transfer risk (0.40) is moderate-high because normative-correctness does not automatically translate into substrate architecture. The 0.60 reflects load-bearing role for one Q-044 resolution outcome while preserving skepticism about over-claiming.
