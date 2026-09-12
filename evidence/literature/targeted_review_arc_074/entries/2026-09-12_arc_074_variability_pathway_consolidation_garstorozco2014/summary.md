# Garst-Orozco, Babadi & Olveczky 2014 -- how does an exploratory epoch actually end?

Garst-Orozco and colleagues made intracellular recordings in RA, the songbird motor cortex analogue,
and tracked how its two functionally distinct inputs changed across song development. The
song-patterning pathway from HVC was strengthened and pruned as the skill consolidated. The
variability-inducing pathway from LMAN was *unchanged*. A network model then showed why this
suffices: strengthening and pruning of action-specific connections reduces the circuit's sensitivity
to variable input and to neural noise. Skill rises and variability falls, without anything having
turned the variability source down.

I have marked this `mixed` rather than `supports`, and the reason is the interesting part. It
corroborates Aronov et al. on the point that matters most -- there really is an architecturally
separate exploration channel, and it persists into adulthood rather than being a scaffold that is
dismantled. But it undercuts a different commitment ARC-074 makes, one that has attracted less
scrutiny than the reward-free premise: the *exit mechanism*. ARC-074 proposes that Phase 0 ends when
explicit gate criteria are met -- `residue_entropy_min` and `z_self_loss_max` crossed, at which point
E3 scoring activates and Phase 1 begins -- and that failure to meet them within `epoch_steps` raises
a training error. That is a thresholded switch. What this circuit appears to do instead is never
switch at all. The exploratory drive is constant; the downstream system's susceptibility to it
attenuates as task-specific structure consolidates. The transition is graded and emergent from the
learning itself, not gated on a measured criterion.

If that shape is right for REE too, then two things in the current ARC-074 design are modelling a
transition that does not exist. The gate criteria would be measuring a boundary that biology treats
as a gradient, and the error path -- raise a training error if the criteria are unmet in time -- would
be enforcing a deadline on a process that has no natural deadline. There is a more attractive
alternative available: an exploration channel that is never suppressed, whose influence simply
declines as `z_world` and the residue field differentiate. That version has the pleasant property of
degrading gracefully rather than throwing, and it removes the need to calibrate two thresholds nobody
currently knows how to set. I would want this weighed before `Phase0Config` is built, since it is
cheaper to choose the shape now than to retrofit it.

The caveats are real and I do not want to over-sell a circuit result as an architectural law. The
mechanism here is synaptic -- strengthening and pruning of specific afferents -- and REE's residue
field plus E3 scoring is not a synaptic-weight substrate, so the principle could hold while the
implementation has no counterpart at all. This is also a single species and a single developmental
time course being read as a general claim about exploration-to-exploitation transitions, which is a
stretch; the songbird transfer risk that applies to Aronov et al. applies here with at least equal
force, and I have set it slightly higher at 0.50.

Confidence 0.62. Source quality 0.85 -- eLife, intracellular recordings across development with a
complementary model. Mapping fidelity 0.60, reduced because the entry's most valuable content is a
*challenge to an implementation detail* rather than a test of ARC-074's central assertion, and
because the substrate analogy carrying that challenge is loose.
