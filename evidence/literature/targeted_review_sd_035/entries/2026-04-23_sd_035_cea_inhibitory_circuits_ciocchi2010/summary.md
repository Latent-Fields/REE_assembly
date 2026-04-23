# Summary: Ciocchi et al. 2010 — Central Amygdala Inhibitory Microcircuits for Fear

**Source:** Ciocchi, Herry, Grenier, Wolff, Letzkus, Vlachos, Ehrlich, Sprengel, Deisseroth, Stadler, Muller & Luthi (2010). *Encoding of conditioned fear in central amygdala inhibitory circuits.* Nature 468(7321): 277–282. [DOI: 10.1038/nature09559](https://doi.org/10.1038/nature09559)

## What the paper did

Ciocchi and Luthi's group used in vivo single-unit electrophysiology combined with optogenetics (channelrhodopsin) in mice to characterise the inhibitory microcircuitry within the central amygdala (CeA) during auditory fear conditioning. They recorded from neurons in the lateral (CEl) and medial (CEm) subdivisions and mapped the functional architecture: CEl neurons receive CS-US pairing and gate acquisition; CEm neurons drive fear responses as output. The key innovation was identifying cell-type-specific plasticity: a subpopulation of CEl neurons increases firing to the CS during conditioning (fear-ON cells) while another decreases firing (fear-OFF cells), with fear-ON neurons projecting to and inhibiting fear-OFF neurons. CEm neurons receive disinhibited drive from CEl fear-ON cells and drive conditioned behaviour output.

## Key findings

CEl neural activity is required for fear acquisition: optogenetic stimulation of CEl during extinction could reinstate fear; inactivation during acquisition impaired learning. CEm drives conditioned fear expression: CEm neurons show correlated responses to CS during fear expression, and their activity predicts fear behaviour. The inhibitory gating mechanism within CeA — CEl fear-ON cells disinhibiting CEm — is the functional basis for the phasic/tonic dissociation: phasic CS-elicited responses in CEl gate tonic CEm output. This dissociation explains fear generalisation: when the CEl phasic gate is imprecise (low specificity), generalised CEm output produces generalised fear.

## REE mapping

SD-035's CeAAnalog emits two signals: mode_prior (a sustained motivational bias pre-softmax into SalienceCoordinator) and fast_prime (a phasic conditioned-cue priming signal). The Ciocchi microcircuit provides the biological justification for this two-output architecture:

- fast_prime maps to CEl fear-ON phasic output: rapid, cue-triggered, CS-specific priming with 1–2 step latency
- mode_prior maps to CEm sustained output: the downstream behavioural mode bias driven by CEl-mediated disinhibition

The phasic/tonic dissociation documented by Ciocchi supports the SD-035 design choice to set fast_prime with a decay tau (3–5 steps) while mode_prior is more sustained (updated by the cortical integration of z_harm_a magnitude). The tonic guardrail on fast_prime (from the synthesis.md defaults: suppress next phasic when tonic elevated) echoes the CEl fear-ON/fear-OFF balance mechanism Ciocchi describes.

The GABAergic nature of CeA output (inhibitory on its downstream targets) is consistent with mode_prior as an additive log-odds bias rather than a direct activating signal: CeA's action on behaviour is disinhibitory (releases behaviour from inhibition) rather than directly excitatory, which maps to mode_prior as a pre-softmax log-odds adjustment shifting the probability mass toward the harm-engaged operating mode.

## Limitations and caveats

This paper characterises mouse fear conditioning, a single valence and paradigm. SD-035's CeAAnalog is intended to operate across harm-context modes more generally (freeze, flee, approach-cautiously). The CEl/CEm internal distinction is not explicitly implemented in SD-035's initial non-trainable pass — the single-output CeAAnalog module conflates the CEl phasic gate and CEm sustained drive into a single z_harm_a-threshold computation. This is a deliberate simplification for the initial pass; the Ciocchi finding is the biological target for a future pass that splits fast_prime and mode_prior generation into internal CEl-like and CEm-like computations.

## Confidence

0.75. High-quality paper (Nature, optogenetics) providing the internal CeA microcircuit architecture that SD-035's CeAAnalog is abstracting. Mapping fidelity moderate because the initial non-trainable pass does not implement the CEl/CEm subdivision.
