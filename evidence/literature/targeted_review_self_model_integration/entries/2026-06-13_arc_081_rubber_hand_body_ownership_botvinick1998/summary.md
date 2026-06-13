# Rubber hands 'feel' touch that eyes see (Botvinick & Cohen, 1998)

*According to PubMed (PMID 9486643).* Botvinick & Cohen, *Nature* 391(6669):756, 1998. [DOI](https://doi.org/10.1038/35784).

**Claims:** ARC-081 (self-as-object), SD-030 (E2 self-forward-model comparator) -- L1 body-ownership strand of the self_model_v4:SELF-8 grounding node.

## What the paper did

The original rubber-hand illusion demonstration. A subject's real hand is hidden; a visible rubber hand is stroked in synchrony with the hidden real hand. After a short period of congruent visuo-tactile stimulation, subjects report feeling the touch as arising from the rubber hand and experience it as their own, and their proprioceptive estimate of where their real hand is drifts toward the rubber hand. Asynchronous stroking abolishes the effect. It is a minimal, controlled instance of the bodily self being captured by an external object purely on the strength of multisensory congruence.

## Why it grounds the claim

The reason this paper sits at the foundation of the self-model literature is that it shows the felt boundary of the self is *inferred*, not given. The self does not come with a fixed, unrevisable register of "what is me"; it is continually re-computed from the current multisensory evidence, and that computation can be hijacked by a well-timed fake. For REE this is exactly the licence ARC-081 needs: if z_self were a hard-wired body-state primitive, there would be no mechanism by which a rubber hand could be incorporated. The fact that it *can* be incorporated is what makes "the self is an object-file slot, subject to the same inference machinery as any other object" a biologically grounded stance rather than a philosophical preference.

The temporal-congruence requirement is the second, quieter point, and it is the one that speaks to SD-030. Ownership only transfers when seen touch and felt touch match in time. Break the match (asynchronous stroking) and the illusion collapses. That is the signature of a comparator: ownership is referred to whatever source best predicts the incoming signal. SD-030's proposed self-stream residual (`z_self_observed - E2_self(z_self_{t-1}, a_actual)`) is the REE-side restatement of the same idea -- self-attribution tracks prediction/observation match.

## Limitations and caveats

This is a perceptual ownership illusion in healthy adults measured by questionnaire and proprioceptive drift, not a recording of any forward-model residual. It supports the *general* claim that the bodily self is inferred and recalibratable; it does not, on its own, establish that REE's particular E2 self-forward-model is the right mechanism, nor does it touch the stateful temporal self-model that SELF-1 must build before SD-030 can attach (the illusion is about body-PART ownership, not a persistent self over time). I have therefore tagged only ARC-081 and SD-030, not MECH-215 (which is about agentive prediction) or MECH-214 (interoceptive goal content).

## Confidence

0.61. Source quality is near-ceiling -- this is one of the most robustly replicated findings in cognitive neuroscience. I have held the aggregate below 0.7 because mapping fidelity is moderate: the illusion grounds the *inferred-self* premise cleanly but reaches SD-030's specific comparator architecture only by analogy, and the transfer from a healthy-adult perceptual illusion to a latent self-model in a reinforcement agent is a representational-level transfer rather than a same-mechanism one. Honest support, not proof of mechanism.
