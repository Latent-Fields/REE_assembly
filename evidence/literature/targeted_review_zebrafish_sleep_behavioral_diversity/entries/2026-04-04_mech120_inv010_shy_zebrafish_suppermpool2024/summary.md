# Suppermpool et al. 2024 — SHY at Single-Neuron Resolution in Zebrafish

**Source:** Suppermpool A, Lyons DG, Broom E, Rihel J. "Sleep pressure modulates single-neuron synapse number in zebrafish." *Nature* 629(8012):639-645, 2024. DOI: [10.1038/s41586-024-07367-3](https://doi.org/10.1038/s41586-024-07367-3)

**Claims evidenced:** MECH-120, INV-010

---

## What the paper did

The Rihel group at UCL performed longitudinal in vivo two-photon imaging of all excitatory synapses on individually identified neurons in larval zebrafish, tracking synapse number continuously across sleep-wake states. This is technically demanding: they tracked the same neurons (identified by their morphology and axonal projections) through repeated imaging sessions spanning natural wake, sleep, forced waking, and pharmacologically-induced sleep.

The key manipulation was sleep pressure: they separated conditions by whether the fish had accumulated high sleep pressure (after prolonged enforced waking) or low sleep pressure (early in an undisturbed night). They also pharmacologically induced sleep using hypnotic agents under both high and low pressure conditions, and manipulated adenosine levels and noradrenergic tone independently.

## Key findings relevant to REE

Synapses were gained during waking and lost during sleep -- consistent with the Synaptic Homeostasis Hypothesis (SHY). But the critical new finding is the sleep-pressure dependence: synapse loss was greatest during high-pressure sleep (after prolonged waking), not during routine sleep. Low-pressure pharmacological sleep failed to trigger synapse loss unless adenosine was simultaneously boosted while noradrenergic tone was suppressed. This establishes that sleep-dependent synaptic downscaling is an active, pressure-gated process -- not a passive default of any quiescent state.

Neuron-subtype specificity was also demonstrated: not all neurons participated equally in SHY. Some subtypes showed greater synapse dynamics than others. This suggests that the downscaling is not a uniform global event but a circuit-structured process.

## Translation to REE

MECH-120 posits that the SWS sub-phase performs global attractor flattening and residue field denoising -- a synaptic homeostasis analog. The Suppermpool paper provides the zebrafish-level confirmation: in precisely the model organism at the REE minimal mind calibration level, sleep actively downscales synaptic contacts in a pressure-dependent manner. Several implications follow.

First, this vindicates the framing of MECH-120 as requiring a genuine offline phase rather than intermittent micro-quiescence: MECH-092's quiescent replay is the V3 prerequisite, but MECH-120 requires sustained sleep-pressure discharge. The adenosine signal is the molecular marker of accumulated waking load -- precisely the integrative burden that ARC-011 posits must be resolved offline.

Second, the neuron-subtype specificity complicates the 'global attractor flattening' language in MECH-120. A more accurate framing may be circuit-structured selective downscaling: different cell populations within the viability map architecture participate in SHY to different degrees. For REE, this might mean that z_world encoder synapses and z_harm pathway synapses participate in SHY differently -- and the MECH-094 hypothesis tag may be one mechanism protecting harm traces from downscaling.

Third, INV-010 is strongly supported: the sleep-pressure accumulation during enforced waking directly demonstrates that waking imposes a representational debt that accumulates and must be repaid offline.

## Limitations and caveats

The paper measures synapse number, not synaptic weight or attractor basin width. MECH-120 is framed in terms of attractor flattening and SNR -- these are functionally adjacent but not identical to synapse count. A neuron losing synapses is presumably weakening its Hebbian monopoly on downstream targets, which would flatten the attractor, but this chain of inference is not closed in the paper. Additionally, larval zebrafish may not have fully developed the E1/E3 architecture complexity that V4 sleep regulation is intended to serve; these results come from young larvae whose pallial circuits are still maturing.

## Confidence reasoning

Confidence 0.90 -- exceptional for a zebrafish-specific mechanistic claim. Nature 2024, single-neuron resolution, longitudinal design, causal pharmacological manipulations. The small dock reflects the synapse-number vs attractor-flattening conceptual gap and the larval developmental stage uncertainty.
