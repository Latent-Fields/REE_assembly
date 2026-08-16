# Gourley et al. 2013 -- oPFC regulates outcome-based decision-making via lateral striatum

## What the paper does

Disconnection surgery, which is the part that makes it worth having. Unilateral lesions of orbitofrontal
cortex on one side and ventrolateral striatum on the other leave each structure partly intact but sever
the functional pathway between them; symmetric lesions, which spare one complete oPFC-striatal network,
serve as controls. Mice so disconnected lost sensitivity to outcome-predictive relationships -- in
food-reinforced responding and in cocaine-associated responding alike. Knocking down Bdnf bilaterally in
oPFC reproduced the deficit and changed BDNF expression in the downstream striatum, and striatal c-Fos
predicted whether an animal remained sensitive to action-outcome contingencies.

The authors read the whole as evidence for compartmentalisation: a dorsolateral striatal compartment for
stimulus-response habit, a ventral compartment doing outcome-based decision-making in concert with oPFC.

## Why it bears on MECH-151

MECH-151's notes carry an anatomical justification -- vmPFC projects directly to striatum and premotor
cortex, and the claim asserts these projections are "not just evaluation input but action gate
modulation". That is an assertion about what the pathway *does*, and until now it has been supported by
citation to descriptive anatomy (Haber & Behrens frontostriatal loops), which establishes that the wire
exists but not what runs down it.

This study is the causal complement. Cut the wire and the animal stops tracking what its actions produce.
Note the specific quantity that is lost: not preference, not value, but sensitivity to the *action-outcome
relationship*. REE's E2.action_object(z_world, action) -> o_t is precisely a compressed prediction of an
action's world-effect. So the frontal-to-striatal traffic is in the currency MECH-151 says it is in.

## What it cannot settle, which is a lot

A disconnection abolishes; MECH-151 posits a graded additive nudge. Both an additive bias and an
all-or-none gate predict that removing the pathway removes outcome sensitivity, so this design does not
favour MECH-151 over the gating alternative that the Cisek entry already flagged as live. That is the
central limitation and it is not a small one.

There is also a compartment question worth flagging rather than burying. The effect runs through
*ventro*lateral striatum, explicitly contrasted against a dorsolateral compartment doing stimulus-response
habit. If REE's action_bias ends up behaving as a fast stimulus-response shortcut -- cue fires, certain
action-objects get elevated, no dependence on the outcome model -- then it is the dorsolateral analogue,
and this paper's warrant does not transfer to it. That is testable in REE: does the bias survive
devaluation of the outcome it points at? I do not think anyone has asked.

Standard rodent-lesion caveats apply and I will not belabour them: permanent lesions permit compensation,
the Bdnf arm shows trophic dependence rather than moment-to-moment signalling, and contingency degradation
is a many-trial aggregate.

## Confidence

0.52. Causal evidence in the right pathway for the right quantity, discounted hard for a coarse readout,
mouse-to-REE transfer, and an inability to discriminate the two architectures actually in contention.
