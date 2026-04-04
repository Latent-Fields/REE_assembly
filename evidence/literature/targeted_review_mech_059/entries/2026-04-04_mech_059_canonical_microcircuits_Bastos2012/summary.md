# Bastos et al. (2012) — Canonical microcircuits for predictive coding

**Citation:** Bastos AM, Usrey WM, Adams RA, Mangun GR, Fries P, Friston KJ. Canonical microcircuits for predictive coding. *Neuron*. 2012;76(4):695-711. DOI: 10.1016/j.neuron.2012.10.038. PMID: 23177956.

**Relevance to MECH-059:** Strong empirical support. Maps precision weighting and prediction error encoding onto distinct cortical layers, cell types, and temporal dynamics — anatomical evidence for the separation MECH-059 requires.

---

This paper does something valuable: it takes the abstract mathematics of predictive coding and asks where in the cortical microcircuit each quantity actually lives. The result is a detailed mapping that reveals precision weighting and prediction error as not just conceptually distinct but physically separated across layers, cell types, and frequency bands.

Prediction errors are carried by superficial pyramidal cells in layers 2 and 3, ascending the hierarchy via feedforward connections that operate characteristically at high (gamma-range) frequencies. Predictions descend from deep pyramidal cells in layers 5 and 6, carried by feedback connections operating at lower frequencies. This asymmetry has been confirmed in multiple primate electrophysiology studies. The error signal is fast, bottom-up, and specific to the current mismatch between expectation and observation.

Precision weighting operates through an entirely different mechanism. Specific subtypes of GABAergic inhibitory interneurons, particularly those targeting distal dendrites of pyramidal cells, gate the influence of incoming signals selectively. These interneurons receive input from attentional and neuromodulatory systems — acetylcholine, dopamine — not from the prediction error signal itself. This means the gain applied to error signals is set by a circuit that reads out the reliability context of the environment, not the magnitude of recent errors. Bastos and colleagues explicitly place precision 'against the superficial pyramidal cells' as a gain parameter for post-synaptic sensitivity — a multiplier on the error unit output, computed independently of it.

There is a temporal dynamics argument here that maps onto REE in an interesting way. Prediction errors are updated at the timescale of the perceptual stimulus — within hundreds of milliseconds. Precision estimates are updated more slowly, reflecting accumulated evidence about environmental volatility or task context. In REE terms, this corresponds to the observation that z_beta (or an equivalent confidence channel) should track model uncertainty over episodes, not flip with every prediction step. A system whose confidence channel is derived from instantaneous residual error has no mechanism for this slower timescale of reliability assessment — it is, in effect, running without an uncertainty representation at all, just a relabelled error signal.

The broader message from Bastos et al. is that the cortex has gone to considerable architectural expense to maintain this separation. Different cell types, different layers, different oscillatory regimes. That expense is not incidental — it is necessary for the inference to work correctly. MECH-059 encodes the same engineering rationale.
