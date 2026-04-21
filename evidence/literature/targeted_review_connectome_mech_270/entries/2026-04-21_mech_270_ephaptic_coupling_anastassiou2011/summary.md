# Anastassiou, Perin, Markram & Koch (2011) — "Ephaptic coupling of cortical neurons"

**Nature Neuroscience** 14:217–223. [DOI](https://doi.org/10.1038/nn.2727). PMID 21240273.

*(According to PubMed.)*

## What the paper does

Anastassiou and colleagues address a long-standing open question in cortical physiology: does the endogenous extracellular field actually matter for neuronal function, or is it just a bystander to synaptic communication? They built a rat cortical slice preparation with a twelve-electrode field-stimulation array and simultaneous patch-clamp recordings from up to four pyramidal neurons in close proximity, so they could apply calibrated extracellular fields and measure the membrane-potential response directly.

What they found is that physiologically plausible field amplitudes produce somatic membrane-potential changes below 0.5 mV — small, in raw terms. But these small perturbations strongly entrained action-potential timing, particularly for slow (<8 Hz) field fluctuations. The authors argue that this is the first clean demonstration that endogenous brain activity can causally influence neural function through field effects under physiological conditions, independent of synaptic transmission.

## Findings relevant to MECH-270

MECH-270 is the claim that ephaptic field coherence in CA1/CA3 pyramidal layers is the biological substrate for the per-stream verisimilitude signal that MECH-269 anchor selection operates over. For that claim to be defensible at all, ephaptic coupling has to be real at physiological field amplitudes in mammalian cortical tissue. Anastassiou et al. 2011 is the foundational empirical result that establishes this. Without it, MECH-270 is a theoretical wish.

The specific features of the result also constrain MECH-270. The entrainment is strongest for slow fluctuations, which fits the theta-band framing in MECH-089 (theta-gamma nesting feeds the proposer's per-cycle summary). The fact that sub-threshold membrane perturbations can entrain spiking is what makes "field coherence as readout" feasible at all — otherwise the signal-to-noise of ephaptic communication would be too poor to carry anything informative.

## How it translates to REE

The translation is an existence-proof rather than a mechanism-for-mechanism map. MECH-270 needs three things to be true: (a) extracellular fields influence firing non-synaptically, (b) the effect is detectable at physiological amplitudes, and (c) it is strong enough to carry signal across populations, not just one-neuron-at-a-time. Anastassiou et al. establish (a) and (b) directly. They speak to (c) through their multi-neuron recordings — proximal pyramidal cells showed correlated effects — but only at a small spatial scale.

For REE specifically, the result is relevant because the CA1 and CA3 pyramidal layers are far more tightly packed than neocortex, and the fields generated during sharp-wave ripples are much larger than the physiological fields Anastassiou et al. studied. The forward inference is: if ephaptic coupling is measurable in cortex at sub-mV amplitudes, it should be considerably stronger in hippocampus during SWRs. The paper does not test this directly.

## Limitations and caveats

The experimental system is cortex, not hippocampus. The pyramidal cells studied are homologous but not identical in their field-generation and field-reception properties. Hippocampal CA1 has particularly dense and laminated cell bodies that likely amplify ephaptic effects, but the quantitative extrapolation is not made in this paper and would need separate work to establish.

The fields studied are sub-threshold. MECH-270's claim about verisimilitude readout involves much larger fields during ripple events. "If it matters at 0.5 mV, it matters more at ripple amplitudes" is the natural inference but it is not tested here, and the dose-response curve of ephaptic effects is not characterised.

The paper also does not address the specific claim MECH-270 makes — that field coherence encodes stream-local prediction alignment. That is a functional interpretation that Anastassiou et al. cannot speak to; their contribution is establishing that the channel exists and can carry signal.

## Confidence reasoning

Source quality is essentially maximal for a primary mechanistic paper — Nature Neuroscience, senior authors include Markram and Koch, rigorous multi-electrode patch-clamp methodology, clean controls. The result has also been extended by later work (which should be pulled separately if MECH-270 needs further grounding). Mapping fidelity is discounted to 0.60 because the experimental system is cortex rather than hippocampus, and the claim about functional interpretation (field coherence as verisimilitude readout) is not addressed. Transfer risk is the main reason overall confidence is 0.72 rather than higher: translating from 0.5 mV cortical fields to ripple-scale hippocampal fields and then to a per-stream functional readout is a two-step extrapolation. Still, this is the best possible foundational evidence for MECH-270, and without it the claim would be unsupported.
