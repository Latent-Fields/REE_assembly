# Moran et al. (2013) -- Free energy, precision and learning: the role of cholinergic neuromodulation

**Claim tested:** MECH-002 (Precision control analogues shape cognitive regimes)
**Direction:** supports | **Confidence:** 0.75

## What the paper did

Of the five entries in this directory, this is the one that comes closest to a real experiment on a
real neuromodulator. Moran and colleagues first simulated a mismatch-negativity paradigm under the
free energy principle, deriving a specific prediction: evoked sensory prediction-error responses
should be suppressed trial by trial as a stimulus becomes predictable, and cholinergic
neuromodulation should *attenuate* that suppression. They then tested it -- 13 healthy volunteers,
within-subject, placebo-controlled, 8 mg galantamine (a cholinesterase inhibitor), 128-channel EEG.
The prediction held. Dynamic causal modelling of the evoked responses then attributed the
drug-induced difference to gain modulation of supragranular pyramidal cells in primary auditory
cortex, decisively over the alternatives in the compared model space.

That last step is what makes the paper valuable here, and it is also the step that carries the most
weight on assumptions. Worth holding both facts together.

## Findings relevant to MECH-002

MECH-002's cholinergic regime says acetylcholine "increases precision at sensory depths
(`alpha_gamma`) under expected noise" and thereby "forces perceptual updating against top-down
prediction". Moran et al. supply the implementation: precision *is* gain on the units carrying
ascending prediction error, and raising it makes bottom-up evidence win against the descending
prediction. That is not a paraphrase of the claim, it is the mechanism the claim presupposes,
measured under a causal manipulation.

The localisation matters more than it might first appear. Supragranular pyramidal cells are the
canonical error-carrying population in predictive-coding microcircuit models. An arousal effect
would not respect that anatomy; a precision effect should. So the DCM result is what distinguishes
"the drug made the subject more alert" from "the drug moved a specific precision term at a specific
level of the hierarchy" -- and it is the latter that MECH-002 needs, because the whole architecture
of depth-indexed `alpha_k` depends on precision being settable *per depth* rather than globally.

This also gives the design constraint an empirical foothold from the cholinergic side. The
manipulation moved sensory-depth gain specifically. It did not move one global scalar.

## How this translates to REE, and where it strains

The gap I would flag hardest is between direction and control law. This study manipulates the drug
and observes the gain change. It does not manipulate uncertainty. Stimulus predictability is a fixed
feature of the MMN paradigm rather than a parametrically varied quantity, so nothing here shows that
*endogenous* acetylcholine sets `alpha_gamma` as a function of expected uncertainty -- which is the
normative half of the Yu and Dayan account that MECH-002 inherits. What is evidenced is: push ACh
up, sensory gain goes up. What is asserted: sensory gain tracks expected noise. The second does not
follow from the first, and the two entries in this directory that address it (Yu and Dayan for the
normative argument, this one for the mechanism) do not overlap in the way one might assume from
reading them together.

Two further limits, both real. N=13 is small, even within-subject, and the headline mechanistic
result is reported as a log Bayes factor over a model comparison rather than an effect size on a
directly observed quantity -- a model space that omits the true generator can still return decisive
evidence for the best of a bad set. And "sensory depth" in REE is a position in an abstract
hierarchy, while the measured effect is in primary auditory cortex under a particular microcircuit
model. Identifying those two is an architectural assumption we are making, not something the paper
licenses.

## Confidence reasoning

Source quality 0.80: J Neurosci, causal placebo-controlled pharmacology with a simulate-then-test
structure that is genuinely stronger than post-hoc modelling, discounted for N=13 and for the key
parameter being model-derived. Mapping fidelity 0.85: gain on ascending prediction-error units at
sensory depth is close to a definition of what `alpha_gamma` is meant to be. Transfer risk 0.30 --
the lowest in this directory, since this is human data with an actual drug, but the
depth-to-cortical-layer identification and the fixed-predictability paradigm both leave room.

Aggregate 0.75, weighted toward source quality as the skill directs for empirical claims. This is
the entry I would put most weight on if only one of MECH-002's four regimes could be defended.
