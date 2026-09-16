# Hierarchical prediction errors in midbrain and basal forebrain (Iglesias et al., 2013)

**Claim under test:** MECH-003 -- *Precision must be tau-scoped with lossy projections.*
**Direction:** supports

## What the paper did

This is the empirical companion to the Mathys entry in this directory, from the same Zurich group
and using the same class of model. Iglesias and colleagues put healthy volunteers through an
audio-visual associative learning task while scanning them, fitted a hierarchical Bayesian model to
each subject's behaviour, and then used the model's *level-specific* prediction-error terms as
trial-wise regressors against the BOLD signal. The question was blunt and good: if the brain really
does run a hierarchy of prediction errors, do the levels live in different places?

They do. Low-level prediction errors -- about what the visual stimulus actually turned out to be --
showed up in visual and supramodal cortex and in the **midbrain**. High-level prediction errors --
about the *probabilities* governing those stimuli -- showed up in the **basal forebrain**. Both
findings replicated in a second, independent group of volunteers. The authors draw the obvious
inference from the anatomy: dopamine for the low-level, concrete errors; acetylcholine for the more
abstract ones.

## Why this bears on MECH-003

MECH-003 ends with a short non-normative note claiming that its mandated tau-separation "mirrors ...
anatomical separation enforcing tau isolation," and lists among its hard prohibitions "collapsing
πγ…πδ into a single attention scalar." Those are two statements of very different epistemic
standing: the first is an empirical bet, the second an architectural rule justified by it.

Iglesias et al. are the closest thing we have to a direct test of the bet. Fit a hierarchy to
behaviour, ask where its levels appear in the brain, and the levels come apart *anatomically* --
different structures, different neuromodulatory identities, replicated. A fast concrete error and a
slow abstract one are not two readings of a single graded quantity smeared across one substrate.
This is the licence REE needs for treating depth-indexed registers as physically separate stores
rather than as a convenience of notation, and it is a real difficulty for any implementation that
would quietly route all depths through one shared precision variable.

## Where the mapping strains

Two gaps, and one of them is more interesting than a mere caveat.

The ordinary gap: this paper measures *prediction errors* at different levels, not *precisions* at
different levels, and MECH-003 is a claim about precision. Under the model the two are entangled --
what is actually regressed against BOLD is a precision-weighted error term -- so separate registers
for one is suggestive of separate registers for the other. But it is suggestive, not direct.

The interesting gap: the paper's transmitter dichotomy **cuts across** the one MECH-003 proposes.
MECH-003's biological note splits *dopamine* by timescale -- phasic dopamine to πγ/πβ, tonic
dopamine to πθ/πδ -- so one transmitter carries the whole tau-axis, fast and slow. Iglesias et al.
find the low/high split falling between dopamine and *acetylcholine* instead. If they are right,
MECH-003's non-normative note is at best incomplete: the cholinergic axis needs a place in it, and
the "tonic dopamine does the long timescales" gloss is doing work the data do not support. This does
not touch the normative core of the claim -- separation is separation, whatever implements it -- but
it is a correction owed to the architecture doc.

## Limitations

The authors themselves flag the main one: fMRI in midbrain and basal forebrain "does not reveal the
exact neuron types activated." The transmitter attribution is an inference from which regions lit
up, not a measurement of anything being released. These are also small structures sitting near
sources of physiological noise, where BOLD is harder to trust than in cortex -- the two-group
replication is what makes this tolerable, and it is the single best feature of the study. Finally,
"hierarchical level" here means statistical abstraction (outcome versus probability), not temporal
depth. That the two covary is plausible and is exactly what REE assumes, but this study does not
check it.

## Confidence

0.72. Source quality is high (0.85) and the replication is what earns it. Mapping fidelity is held
to 0.70 by the epsilon-versus-pi gap and by the transmitter mismatch. The result is an entry that
supports MECH-003's separation requirement well while simultaneously flagging that the claim's own
biological footnote needs revising.
