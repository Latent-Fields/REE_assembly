# Context selection is dynamical, not gated (Mante, Sussillo, Shenoy & Newsome 2013)

Monkeys watched a patch of moving coloured dots and, depending on a contextual cue, had to judge
either the direction of motion or the dominant colour -- ignoring the other feature entirely. Mante
and colleagues recorded prefrontal populations while the animals did this, and then trained a
recurrent network to reproduce the population dynamics so they could interrogate the mechanism.

The headline finding is the one that gets cited: selection and integration are not two stages but
one dynamical process. The finding underneath it is the one that matters for SD-082. The
*irrelevant* feature was not gated out at the input. Both motion and colour evidence remained
robustly represented in the prefrontal population regardless of which one the animal was supposed
to use. What context did was reorient the population's integration axis, so that only the relevant
evidence accumulated toward the choice. The contextual signal itself was a comparatively modest
displacement of the population state -- small in the raw response, decisive in behaviour.

The first half of that is straightforwardly good news for SD-082's diagnosis, and it is the same
lesson as the dPCA entry arriving from a different direction. A rule signal can be small, can sit
inside a much larger shared representation, and can still be the thing that determines the action --
provided something downstream is capable of isolating it. If the read-out cannot, the signal is
functionally absent, which is precisely the 0.0 propagation V3-EXQ-822 measured while the rule pool
itself was differentiated at 0.644.

The second half is the awkward part, and I would rather write it down than leave it implicit.
SD-082's remedy is a feedforward head: subtract the per-tick mean across candidates, then bound the
output with a scaled tanh so the gradient survives. Mante et al. found that cortex, facing a
structurally similar problem, does not solve it that way -- it solves it with recurrence unfolding
over the timecourse of the decision. That is not a measurement against SD-082 and I want to be
careful not to inflate it into one. The task is a two-modality perceptual discrimination in a
macaque; SD-078's rule_state is a learned pool of up to sixteen live rules biasing action
candidates. Those are different objects. Nothing here shows a demixed feedforward read-out fails at
REE's problem; it shows that the one biological system we can look at chose a richer mechanism.

What I take from it operationally is a caution about what a PASS on V3-EXQ-822a would license.
Acceptance is `on_prop_delta_mean >= 0.001` with an ON>OFF contrast, which establishes that the
propagation path is non-vacuous. It does not establish that a static head can express whatever
rule-conditional structure the pool actually contains. Worth instrumenting the head for saturation
and for whether its bias depends on anything beyond the instantaneous demixed summary.

Direction mixed, confidence 0.66 -- high source quality discounted hard by mapping fidelity, since
the supporting half maps cleanly and the weakening half maps only by analogy.
