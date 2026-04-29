# Staresina, Duncan, Davachi (2011): Perirhinal and parahippocampal cortices differentially contribute to object- vs scene-related event details

## What the paper did

The team designed a source-memory paradigm in which participants imagined objects or scenes while undergoing fMRI, with perceptual input held constant across the two domains. They then asked which medial temporal lobe (MTL) subregions' encoding activation predicted which kind of source memory at later test. The methodological strength is that perceptual input was equated across conditions, so any dissociation cannot be reduced to differences in stimulus complexity or visual richness -- it must be referable to the representational domain (object identity vs spatial context).

## Key findings

The paper reports a clean fMRI double dissociation: perirhinal cortex (PrC) encoding activation predicted later object source memory but not scene source memory, while parahippocampal cortex (PhC) encoding activation predicted later scene source memory but not object source memory. The hippocampus contributed to both, consistent with its canonical role as the associative locus. Importantly, the transitional zone between PrC and posterior PhC contributed to both object and scene source encoding, suggesting that the representational separation is a gradient rather than a sharp anatomical boundary.

## How the findings translate to REE

Q-030 asks how z_resource (object-identity, SD-015) and z_world (spatial-contextual) should be configured across REE's processing stages: separate encoders or joint? E2 sees one or both? Hippocampus fuses or processes in parallel? E3 evaluates jointly or via separate harm/benefit channels? The Staresina paper provides the canonical mammalian architecture answer for the *encoding* stage: separate encoders (PrC for object, PhC for scene) feeding a shared associative locus (hippocampus). This directly supports two REE commitments: SD-015 (z_resource encoded separately from z_world) and MECH-162 (z_resource and z_world re-converge at the hippocampal planning stage). It also weakens the design option of a single joint encoder at input: if the mammalian substrate, which has had hundreds of millions of years to optimise this split, uses separate encoders, that is non-trivial evidence about which permutation works. The transitional-zone finding is also informative: the separation is graded, not strict, which gives REE design freedom to allow some shared representation in a "buffer zone" without committing to a strict orthogonalisation constraint.

## Limitations and caveats

Mammalian MTL anatomy is not the only viable architecture for object-vs-scene representation, and the REE substrate is not mammalian. Generalising from PrC/PhC to z_resource/z_world is an analogy of function, not identity of mechanism. The transitional-zone evidence pushes against any strict-separation reading: if REE enforces hard orthogonalisation between z_resource and z_world at the encoder, that is a stronger constraint than the mammalian solution actually uses. The paper also measures source memory (a behavioural downstream readout) rather than testing the latent representations directly, so the inference from "encoding activation predicts source memory" to "these regions encode the relevant latent" is the standard fMRI inferential step but is not a direct latent-representation measurement.

## Confidence reasoning

Source_quality is 0.85 -- well-controlled fMRI paradigm in J Neurosci with a clean double dissociation. Mapping_fidelity is 0.82 because the paper directly addresses the encoding-stage permutation Q-030 cares about and the source-memory read-out maps onto downstream goal-directed use of the encoded representations. Transfer_risk 0.32 reflects that mammalian MTL anatomy is one viable solution among many, but the convergent evolution of object/scene separation across mammals is itself non-trivial evidence. Aggregate confidence 0.78 marks this as a strong anchor for the SD-015 and MECH-162 commitments at the encoding and convergence stages, with the transitional-zone finding flagged as a refinement signal: REE should permit graded rather than strict separation.
