# Cisek 2007 -- the affordance competition hypothesis

## What the paper does

Cisek sets out to dislodge the serial picture of behaviour -- perceive, then decide, then act -- on
the grounds that the neurophysiology simply does not look like that. His alternative is that sensory
information is used to specify, in parallel, *several* actions that are currently available, and that
these candidate actions then compete against one another within fronto-parietal cortex while biasing
signals accumulate until one wins. The dorsal visual stream does the specifying. Prefrontal cortex and
the basal ganglia do the biasing. A computational model accompanies the argument and reproduces
qualitative features of premotor and parietal recordings along with a set of behavioural phenomena.

The paper is a framework paper, not a measurement. That matters for how much weight it can carry, and
I have priced it accordingly below.

## Why it bears on MECH-151

MECH-151 is, stripped to its skeleton, an assertion about *where in the pipeline top-down context is
allowed to act*. It says the E1 cue-indexed context vector projects to an action_bias which is added to
E2.action_object() outputs, so that the affordance manifold is already shaped by context before
HippocampalModule searches it and before E3 selects from it. The alternative architectures -- bias the
percept (MECH-082), or let search run unbiased and veto the winner afterwards -- are genuinely different
designs with different failure modes.

Cisek's hypothesis makes the same structural commitment. Candidate actions are specified first; biasing
influences from prefrontal cortex arrive into that already-specified set; selection happens last. The
sequence is the claim. So this is about as direct an architectural endorsement as the primate literature
offers for MECH-151's insertion point, and it is worth noting that the endorsement was arrived at
independently and two decades earlier, from electrophysiological constraints rather than from
engineering convenience.

## Where the translation strains

Two places, and I want to be honest that the second one is the more serious.

First, Cisek's action space is parameterised movement -- reach directions in a spatially organised
sensorimotor map. REE's action-object space is a learned compressed representation of what an action
does to the world. An additive bias vector is a natural operation on a topographic map of directions;
it is not obviously the natural operation on an arbitrary learned latent. MECH-151 assumes it is, and
Cisek does not license that assumption.

Second, "prefrontal regions and the basal ganglia" is a conjunction. MECH-151 routes the entire biasing
signal through one cortical projection (E1 -> action_bias) with nothing playing the role of a striatal
gate. If the biological arrangement is cortical-bias-then-subcortical-gating, then a purely additive
cortical projection may be a partial implementation rather than a faithful one -- which would show up
in REE as a bias that is present in the tensors but weak in its behavioural consequence. That is worth
holding in mind given that the V3-EXQ-640a autopsy found mean_cue_action_bias_norm NULL in all six cells
under default settings: a bias that is architecturally correct but functionally inert is exactly the
shape of failure this caveat predicts.

## Confidence

0.75. High mapping fidelity -- the architectures line up unusually well -- against the standing discount
for a framework paper carrying no new data. I would not use this entry to argue that MECH-151's *additive*
form is correct; only that biasing a pre-specified affordance manifold, before search, is a shape of
architecture the primate motor system appears to use.
