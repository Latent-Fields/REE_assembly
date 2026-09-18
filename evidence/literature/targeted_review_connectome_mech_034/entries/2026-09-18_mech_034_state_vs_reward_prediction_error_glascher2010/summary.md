# States versus rewards -- the canonical two-currencies dissociation

Glascher, Daw, Dayan and O'Doherty put eighteen people in a scanner on a probabilistic Markov
decision task built in two phases: first a transition-learning phase with no rewards at all, so that
participants could only be learning the structure of the world, and then a reward phase layered on
top. That design is the whole point. By decoupling *learning where the world goes* from *learning
what the world is worth*, they could regress two different model-derived error terms against BOLD
and ask whether the brain treats them as one quantity or two.

It treats them as two. The state prediction error -- the discrepancy between the learner's current
transition model and the state it actually landed in -- loaded on intraparietal sulcus and lateral
prefrontal cortex. The reward prediction error loaded, as a decade of prior work would predict, on
ventral striatum. The regions did not overlap. The authors read this as evidence for two distinct
forms of learning signal in humans, underwriting two computational strategies.

## What this does and does not give MECH-034

MECH-034 asserts that viability mapping updates and residue curvature updates are different things:
one surface encodes path stability, the other ethical cost, and both are post-action. Glascher et al.
is the closest biological precedent I can find for the *structure* of that assertion. Two error
signals, computed from the same stream of experience, carried separately. If the brain had one
generalised post-action error currency, this experiment is where that would have shown up, and it
did not.

But I should be honest about the join. The paper dissociates model error from *reward* value. REE's
residue is harm-keyed, not reward-keyed, and the architecture treats that asymmetry as load-bearing
rather than cosmetic -- residue is meant to persist and to raise trajectory cost, not to decay toward
a running average the way an appetitive value estimate does. So this entry supports the claim's
skeleton (two currencies, separable substrates) without touching the flesh (that one of them is
specifically ethical curvature). That is a real limit, and it is why the confidence sits at 0.78
rather than higher despite a Neuron paper with a replication record.

There is a second, sharper limit that matters for how MECH-034's own falsifier is written. The
dissociation here is *anatomical*: two regressors, two regions. The falsifier registered against
MECH-034 asks for something stronger -- a double dissociation on the *manipulation* side, where
harm is delivered at well-predicted states and mismatch is induced without harm, and each surface is
required to move on its own diagonal and stay put off it. Glascher et al. never manipulate the two
independently; both errors arise from the same transitions. So the paper tells us the two signals can
be separately *read out*; it does not tell us they can be separately *driven*. That is precisely the
gap the V3 experiment would close, which is a useful thing for a literature entry to establish.

## Confidence

0.78. Source quality is near the ceiling. Mapping fidelity is the binding constraint, and for an
architectural claim the skill's calibration guide says mapping fidelity should dominate. Transfer
risk I have put at 0.35 -- the risky transfer is not human-to-machine here, which is routine for this
corpus, but appetitive-value-to-ethical-curvature, which is a genuine conceptual substitution and one
REE elsewhere insists on not making.
