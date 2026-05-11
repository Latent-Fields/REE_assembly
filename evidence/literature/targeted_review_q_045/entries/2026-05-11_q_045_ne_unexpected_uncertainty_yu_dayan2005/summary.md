# Yu & Dayan 2005 — Uncertainty, neuromodulation, and attention

According to PubMed, [DOI 10.1016/j.neuron.2005.04.026](https://doi.org/10.1016/j.neuron.2005.04.026), PMID 15944135.

## What the paper did

This is a theoretical / computational synthesis. Yu and Dayan formalise two qualitatively different forms of uncertainty in Bayesian inference: EXPECTED uncertainty (the known unreliability of a cue within a stable context — e.g. an 80%-valid cue, where uncertainty is signalled by the cue itself) and UNEXPECTED uncertainty (an unsignaled context-switch that makes previously-reliable predictions inconsistent — e.g. cue validity changes from 80% to 20% without warning). They propose acetylcholine signals expected uncertainty and norepinephrine signals unexpected uncertainty, and the two neuromodulators interact both antagonistically and synergistically to enable optimal inference and learning. The model is then validated against a wide span of physiological, pharmacological, attentional, and behavioural data.

## Key findings relevant to Q-045

For Q-045 the relevant claim is the COMPUTATIONAL DISTINCTNESS of NE-based and ACC-based signalling. NE's role in the Yu-Dayan framework is unexpected-uncertainty signalling: detect a context-switch, broadcast that prior predictions cannot be trusted, drive exploration / belief-revision. dACC's role (not directly modelled in this paper but well-established elsewhere) is recency-weighted history-tracking + selective anti-recency suppression. These are different computational primitives, with different temporal kernels and different update rules. The architectural argument for Q-045 is that they cannot collapse into one substrate without losing one of the two computational roles. The Yu-Dayan framework supplies the theoretical statement of this distinctness.

## How this translates to REE

For Q-045 this paper supports the SUBSTRATE-DISTINCT verdict from the computational-theory side. MECH-313 (LC-NE tonic noise floor) is the REE analogue of the NE substrate; MECH-260 (dACC anti-recency penalty) is the REE analogue of the dACC substrate. The Yu-Dayan framework predicts these will respond differently under pharmacological manipulation: NE-blockers should impair context-switch detection (mode-switching as in Tervo 2014) without impairing within-context value learning, while ACC-lesions should impair value learning without impairing context-switch detection. The 4-arm ablation in REE's Q-045 design is the in-silico version of this manipulation — Yu-Dayan predicts dissociable behavioural signatures, not just dissociable magnitudes.

There is also a refinement that this paper surfaces. Yu-Dayan's NE role is UNEXPECTED-UNCERTAINTY signalling — a triggered response to context-switch — not a continuous always-on noise floor as MECH-313 is currently conceived. These two NE roles are related (the tonic-vs-phasic axis Aston-Jones & Cohen 2005 describes is the most plausible bridge: tonic is always-on baseline, phasic is the unexpected-uncertainty trigger) but they are not identical primitives. The arc_065 Pull 1 synthesis already noted this — MECH-104 covers the phasic role; MECH-313 is intended to cover the tonic role. The Yu-Dayan framework adds that the tonic role MAY need an unexpected-uncertainty modulation on its amplitude (a state-switch on top of the always-on baseline) to fully match the LC-NE biology. This is a Phase-2 architectural refinement, not a current substrate gap.

## Limitations and caveats

The paper is theoretical, not empirical. The Yu-Dayan framework synthesises and predicts; it does not independently test. The mapping to MECH-313 specifically is loose because MECH-313 is currently a noise-floor primitive rather than an unexpected-uncertainty primitive — these are related but not identical. The architectural argument for Q-045 (NE-based and dACC-based substrates are computationally distinct) is robust to this looseness; the implementation refinement (should MECH-313 add an unexpected-uncertainty trigger?) is the open question this mapping surfaces.

## Confidence reasoning

Confidence 0.74. Source quality high (Neuron 2005, canonical Bayesian theory of neuromodulation, heavily cited and broadly accepted). Mapping fidelity moderate-strong on the substrate-distinctness argument that Q-045 actually needs, but weaker on the direct MECH-313 anchor — Yu-Dayan's NE role does not perfectly match MECH-313's noise-floor primitive. Transfer risk moderate (theoretical synthesis to substrate-level commitment is a two-hop transfer, but the architectural commitment is at the computational-primitive level where the mapping is cleanest).
