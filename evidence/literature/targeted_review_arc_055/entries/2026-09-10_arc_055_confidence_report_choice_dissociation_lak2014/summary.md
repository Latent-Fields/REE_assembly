# Confidence-guided waiting is abolished while choice survives (Lak et al., 2014)

**Claim tested:** ARC-055 -- verisimilitude signal availability: V(t) and D_V must be explicitly available to E3 selection and influence E1/E2 learning updates.
**Direction:** mixed | **Confidence:** 0.60

## What the paper did

Rats performed a perceptual decision and then expressed how confident they were in it by how long they were willing to wait for a delayed reward -- a temporal wagering readout that turns a private metacognitive quantity into a behavioural one. Orbitofrontal cortex was then inactivated, and both the confidence report and decision accuracy were measured under the same manipulation in the same animals.

The result is a clean internal dissociation: inactivation disrupted waiting-based confidence reports without affecting decision accuracy.

## Why this entry is filed as mixed

ARC-055 joins two assertions with an "and": V(t) and D_V are explicit signals, *and* they are available to E3 selection as well as to E1/E2 learning. This experiment takes those apart and returns a different verdict on each, which is why a single direction token would misrepresent it.

On explicitness, the evidence is supportive and unusually strong. A quantity that can be removed by inactivating one region, with a selective and specific behavioural consequence, is by construction an addressable representation. This is not a diffuse property of the computation that happens to be describable as confidence; it is something with an address. That is the distinction ARC-055 is built on, and here it is drawn causally rather than argued.

On availability-to-selection, the same result is awkward for the claim. The choice was unimpaired by the very manipulation that abolished confidence-guided behaviour. If REE's E3 selection is the analogue of the choice, then in this preparation selection ran perfectly well without the explicit signal ARC-055 says it must have. The pattern is what one expects if an implicit graded evidence quantity drives the choice while the explicit confidence signal serves the report and the across-trial update -- which is a coherent architecture, and *not* the one ARC-055 commits to.

## The reading that would rescue the claim, and why it does not settle things

One can save ARC-055 by saying that choice here uses an implicit quantity while only the report needs the explicit one, so the claim's E3 leg is simply untested rather than contradicted. That is fair. But notice that implicit-versus-explicit is precisely the distinction the claim turns on, so invoking it as a defence concedes that this experiment leaves the architectural commitment undetermined. The honest summary is that ARC-055's E3 leg now has to be argued from something other than the assumption that a signal that exists must be read.

There is a second and better defence, which I think carries more weight: a two-alternative perceptual choice has essentially no trajectory structure. ARC-055 lives inside a claim family (ARC-053, ARC-054) about selection among *extended* trajectories evaluated over a planning horizon. A depth-like signal would have nothing to contribute to accuracy in a task with a degenerate trajectory space, whether or not it is mandatory in a richer one. That makes this a weak test of the E3 leg rather than a strong disconfirmation -- but it also means the claim's E3 leg is currently unsupported by anything in this directory, which governance should see plainly.

## Limitations and confidence reasoning

Inactivation removes a region, not a signal. Orbitofrontal cortex carries a great deal besides confidence, and preserved accuracy shows that the choice circuit was intact under the manipulation, not that it never reads a confidence-like quantity. Species and task scope (rat, sensory two-alternative, wagering readout) are a substantial extrapolation to REE's E3.

Source quality is 0.85 -- Neuron, a causal manipulation rather than a correlation, with the critical control measured in the same animals so that the dissociation is internal rather than assembled across studies. Mapping fidelity is 0.65: the explicitness leg maps well, the selection leg maps onto a degenerate trajectory space. Transfer risk is 0.40. The aggregate 0.60 is set by the two-directional bearing rather than by any weakness in the experiment. It is filed `mixed` deliberately, so that governance sees the tension rather than a net-of-signs number that would hide it.
