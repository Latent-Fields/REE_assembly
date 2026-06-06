# Cai et al. 2016 -- A shared neural ensemble links distinct contextual memories encoded close in time

**Claim under review:** CANDIDATE-contextual-memory-allocation-gate (V4/V5 intake, 2026-06-06)
**Direction:** supports (temporal distance as a first-class gating variable) | **Confidence:** 0.76

## What the paper did

Cai, Silva and colleagues tested the *memory allocation hypothesis*: that learning triggers a transient rise in neuronal excitability which biases the representation of a *subsequent* memory toward the ensemble that encoded the first, so that the two memories become linked. Using head-mounted miniature-microscope calcium imaging to track the same CA1 neurons across days, they showed in mice that the overlap between the ensembles activated by two distinct contexts encoded within a single day is markedly higher than when the two contexts are separated by a week. The overlap was behaviourally consequential -- recall of one memory increased recall of the other -- and was causally tied to the excitability mechanism: manipulating excitability moved the linking window, and aged animals, which lack the learning-induced excitability increase, failed to link and failed to show the elevated overlap.

## Why it matters for the intake

This is the most direct empirical grounding I found for the intake's `temporal_distance` (days-vs-hours) variable. The time gap between two encoding episodes is, by itself, a measurable determinant of whether traces are allocated to overlapping or separate representations -- short gap pushes toward integration, long gap toward separation. It pairs tightly with the de Sousa 2026 result: de Sousa supplies the *top-down* controller (vmPFC deciding linking-vs-separation for days-apart memories), while Cai supplies the *bottom-up* allocation rule (intrinsic excitability time-window) that the top-down signal modulates. Together they make a strong case that temporal distance belongs as a genuine first-class input to a REE allocation gate, not a derived afterthought. In REE terms this grounds the `temporal_gap_weight(estimate_temporal_distance(...))` term in the intake's `allocate_memory_trace` sketch, and points at an excitability/allocation-bias substrate (conceptually adjacent to MECH-261 awake-reactivation bias) as what such a weight would actuate.

## Limitations and caveats

The mechanism here is bottom-up -- an intrinsic excitability time-window -- not a top-down control decision. So the paper licenses temporal distance as a *variable* but says nothing about a control plane *setting its weight*; reading it as evidence for the allocation policy itself would be a category error. The effect is also state-conditional: it disappears in aged animals, meaning a REE temporal-gap term modelled on it would inherit that conditionality rather than behaving as a fixed law. And the readout is memory linking / co-recall, a benign bias toward integration -- it is not a demonstration that inappropriate linking is *harmful*. The reality-coherence / false-linking-risk cost has to come from elsewhere (the over-generalization literature, e.g. Sahay 2011 in this same review).

## Confidence reasoning

Source quality is high: Nature, longitudinal single-cell ensemble imaging combined with causal excitability manipulation, foundational and heavily replicated. Mapping fidelity is high for the temporal-distance variable specifically -- close to a one-to-one grounding of the temporal-gap term. Transfer risk is moderate (rodent ensemble allocation to artificial-agent trace allocation, plus the state-conditional caveat). Net 0.76.
