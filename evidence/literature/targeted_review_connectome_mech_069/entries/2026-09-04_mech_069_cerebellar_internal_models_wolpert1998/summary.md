# Wolpert, Miall & Kawato (1998) -- "Internal models in the cerebellum"

## What the paper did

This is the canonical Trends in Cognitive Sciences review that established, and made broadly accessible, the forward-model account of cerebellar motor control: the cerebellum learns to predict the sensory consequences of a motor command by using a copy of the command itself (an "efference copy") as an input, generating a prediction that can be compared against actual sensory feedback once it arrives. The mismatch -- the forward-model prediction error -- is taught into the cerebellum via climbing-fiber signals.

## Key findings relevant to MECH-069

The paper's central architectural claim is that this motor-conditioned prediction error is a computationally distinct kind of signal from generic sensory prediction. Predicting "what will I sense next" from passive context requires no knowledge of one's own efferent commands; predicting "what will I sense as a RESULT of this specific action" does require that knowledge (the efference copy) as an input. The cerebellum's architecture -- and its dedicated climbing-fiber teaching pathway -- exists specifically to compute the latter, action-conditioned quantity, and the review treats this as anatomically and functionally separable from generic sensory forecasting.

## Translation to REE

MECH-069 splits E1 (sensory prediction error -- carries no information about which action caused a mismatch) from E2 (motor-sensory error on z_gamma -- explicitly action-conditioned, requires knowing what action was taken). This is close to a textbook restatement of the forward-model/efference-copy distinction that Wolpert, Miall and Kawato lay out: E1 is analogous to passive sensory forecasting, E2 is analogous to the cerebellum's forward-model prediction error, and the paper's core argument is precisely that these require structurally different computations and, in the brain, different dedicated circuitry.

## Limitations and caveats

Two things temper this. First, it is a 1998 theoretical review, not a fresh empirical measurement of REE's specific architecture -- it establishes the computational argument for why E1 and E2 should be separable in principle, not a direct test of REE's implementation. Second, and worth flagging explicitly: the paper itself notes that cerebellar climbing fibers carry information not only about motor performance errors but also about errors in the PREDICTION of aversive events -- a complication for any assumption that the motor-error channel (E2) is cleanly separable from a harm-related channel (E3). This nuance should be read alongside the Schultz (1998) counterweight entry in this same directory, which raises a related point about dopamine's own generality.

## Confidence reasoning

High source quality within its domain -- this is one of the most cited papers in computational motor neuroscience and remains the standard reference for the forward-model account. Mapping fidelity is moderate: it grounds the E1-vs-E2 conceptual distinction well, but says nothing about REE's specific object-level z_gamma representation and nothing at all about the E3/harm arm of MECH-069's three-way partition.
