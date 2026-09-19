# Cavanagh et al. (2011) -- Subthalamic nucleus stimulation reverses mediofrontal influence over decision threshold

**Claim tested:** MECH-065 -- *Reality-coherence conflict lane modulates loop precision and commitment thresholds before execution lock-in.*
**Direction:** supports (mechanism-shape) | **Confidence:** 0.82

## What the paper did

Cavanagh and colleagues recorded scalp EEG from Parkinson's disease patients performing a probabilistic
reinforcement-learning choice task, both with subthalamic nucleus deep brain stimulation ON and with it
OFF, and separately recorded intracranially from the STN area. Rather than reading the result off
accuracy or reaction time, they fitted a hierarchical Bayesian drift-diffusion model to the choice and
RT distributions, which decomposes behaviour into a rate of evidence accumulation (drift) and a
*threshold* of accumulated evidence required before a choice is emitted. The question was then
specific: does trial-to-trial mediofrontal activity predict the threshold, and does it do so as a
function of conflict?

The answer was yes on both counts. Trial-to-trial increases in mediofrontal theta power (4-8 Hz)
tracked an increased decision threshold, and the relationship scaled with decision conflict --
operationalised as similarity in learned value between the presented options. Intracranial recordings
showed elevated 2.5-5 Hz STN activity on those same high-conflict trials. Critically, STN deep brain
stimulation *reversed* the mediofrontal-threshold relationship and produced impulsive choice: with the
brake disabled, the cortical conflict signal no longer bought time.

## Why this is the closest empirical analogue MECH-065 has

MECH-065 asserts a specific control topology: a conflict signal that acts on the *commitment threshold*
and on lock-in pressure, and that acts *before* execution lock-in rather than showing up as a
downstream behavioural correlate. Almost every part of that shape is demonstrated here. The mediofrontal
theta signal is an independently-measured channel, not inferred from the choice. The decision threshold
is a separately estimated parameter of the pre-commitment accumulation process, not the outcome. The
STN-DBS manipulation converts what would otherwise be a correlation into a causal claim about the
pathway. And the direction is the one MECH-065 predicts: more conflict, higher threshold, slower and
more deliberate commitment.

The design lesson for REE is the one the claim's own non-degeneracy precondition already asks for, now
with a worked example. A REE experiment on MECH-065 should (a) instrument RC_conflict as a readable
channel with demonstrated non-zero variance across the manipulation, (b) estimate the commitment
threshold as a separable pre-commit parameter rather than reading it off final behaviour, and (c)
include a knock-out arm in which the RC_conflict-to-lock-in-pressure coupling is severed. It is (c)
that does the real work here: without the DBS-OFF/ON contrast this would be one more correlational
theta finding.

## Where the mapping strains, and I want to be honest about it

The conflict in this experiment is *value conflict* between two similarly-rewarding options. It is not
reality-coherence conflict, not provenance mismatch, and not authority spoofing. So the paper is
evidence that a cortical conflict signal can gate a subcortical threshold brake; it is not evidence
that reality-coherence conflict is a *distinct lane* from value conflict, which is exactly the part of
MECH-065 that remains open. If anything, a sceptic could read Cavanagh et al. as showing that one
generic conflict-to-threshold pathway suffices, with no need to carve a separate reality-coherence
channel at all -- which is the reading Alexander & Brown (2011), also in this pull, would press.

Two further caveats. The population is Parkinson's disease patients undergoing DBS, who carry
dopaminergic pathology and surgical selection effects; the parameters are not healthy-baseline
parameters. And the threshold is a fitted latent, recoverable only because the DDM separates it from
drift rate -- a REE run that reads "commitment threshold" off final behaviour alone would not be able to
distinguish a threshold shift from a drift-rate shift, and the two make overlapping behavioural
predictions. REE has an advantage the paper does not: it can instrument the threshold directly rather
than inferring it.

## Confidence reasoning

Source quality 0.90 -- Nature Neuroscience, multimodal, causal manipulation, and by now a canonical
result. Mapping fidelity 0.70 -- the control topology is right and the measurement design transfers
cleanly, but the conflict *content* is wrong for MECH-065's specific reality-coherence framing.
Transfer risk 0.35 -- clinical population, fitted latent rather than read channel. Aggregate 0.82,
weighted toward source quality because the load-bearing contribution here is an empirical demonstration
that this control shape exists at all, which until now MECH-065 had only assumed.
