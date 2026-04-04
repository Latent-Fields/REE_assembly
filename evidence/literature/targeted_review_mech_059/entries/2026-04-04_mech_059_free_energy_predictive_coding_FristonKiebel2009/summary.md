# Friston & Kiebel (2009) — Predictive coding under the free-energy principle

**Citation:** Friston K, Kiebel S. Predictive coding under the free-energy principle. *Phil Trans R Soc B*. 2009;364(1521):1211-1221. DOI: 10.1098/rstb.2008.0300. PMID: 19528002.

**Relevance to MECH-059:** Foundational. Establishes the mathematical architecture in which precision and prediction error are structurally distinct quantities.

---

This is the paper that lays out, in formal terms, exactly why precision and prediction error cannot be the same thing. Friston and Kiebel derive the predictive coding update rules from a single variational free-energy objective, and the result is a quantity called the precision-weighted prediction error: xi = Pi * epsilon. The key observation is that this product has two separable factors. Epsilon is the residual mismatch between what was predicted and what arrived — it belongs to the error unit. Pi is the estimated inverse variance of that error — it belongs to the generative model's beliefs about signal reliability. They are optimised with respect to different degrees of freedom in the model.

The neurobiological implementation the paper proposes makes this separation concrete. Prediction errors are carried by superficial pyramidal cells ascending the cortical hierarchy, while predictions descend from deep pyramidal cells. Precision is not a property of the error unit's firing rate — it is encoded by the post-synaptic gain applied to those error units. The synaptic gain is a separate computational parameter, modulated by top-down and lateral connections, that scales how much the prediction error influences higher levels. If precision and prediction error were conflated into a single signal, this gain-modulation mechanism would have nothing to operate on: you cannot scale a signal by itself without destroying its information content.

The paper is not primarily about the necessity of this separation — it takes the Bayesian formulation as given and works out its biological consequences. But the separation is an inescapable structural feature of the framework. A system that encodes precision as a function of prediction error magnitude has made a category error: it has confused the noise estimate with the signal being estimated. This is precisely the failure mode MECH-059 is designed to prevent in REE. The confidence channel (z_beta or equivalent) must track uncertainty in the generative model's parameters, not the instantaneous residual from the last prediction step.

One important nuance: Friston and Kiebel describe a unified computational operation (precision-weighted prediction error), not two separate output streams. The separation is in the optimisation variables, not necessarily in the anatomical wiring. REE MECH-059 goes slightly further in requiring architectural separation — but this paper provides the theoretical warrant for that requirement.
