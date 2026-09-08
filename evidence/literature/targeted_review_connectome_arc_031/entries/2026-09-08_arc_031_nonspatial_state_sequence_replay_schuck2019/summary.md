# Sequences, not just positions -- the half of ARC-031 the map literature misses

**Schuck & Niv (2019), _Science_ 364(6447):eaaw5181.**
Claim assessed: **ARC-031** -- HippocampalModule navigates z_self trajectory space in addition to
z_world action-object space O.

## What the paper did

Participants performed a decision task with sequential structure, then rested in the scanner.
Hippocampal fMRI patterns during that rest reflected the sequentiality of the task states they had
just been through -- consecutive patterns corresponding to nearby states. That is replay, detected
non-invasively, of a trajectory through a state space with no spatial content whatsoever.

The finding I think matters more architecturally is the second one: hippocampal sequentiality
correlated with the fidelity of task representations in orbitofrontal cortex during
decision-making, and OFC fidelity was itself related to better performance. So the replayed abstract
sequences are not epiphenomenal; they track how well the task is represented elsewhere.

## Why it is in this pull

Because the rest of the abstract-cognitive-map literature answers the wrong question for ARC-031.
Constantinescu et al. and Tavares et al. establish that non-physical spaces are mapped and that the
self can have a position in one. But ARC-031's object is a **trajectory** -- "planned sequences of
internal self-state transitions constituting deliberation" -- and a map is not a route.

This is the paper that shows hippocampus producing ordered sequences through an abstract state
space. Together with the OFC correlation, it also gestures at the functional role ARC-031 assigns:
sequence generation that builds and refines representations used elsewhere, which is recognisably
the shape of what deliberation-planning would need to be for.

## Retrospective, not prospective

The gap is that replay reconstructs sequences of states the participant *actually visited*. ARC-031
needs candidate future sequences generated and scored -- by self-coherence cost, hypothesis-tag
integrity cost, self-maintenance cost, per the claim's own specification.

These are architecturally adjacent. Offline replay of experience is a standard route to building the
model that prospective planning then searches, and the REE architecture makes the same connection:
ARC-031 lists MECH-092 (offline replay extended to z_self trajectories) among its dependencies. But
adjacency is not identity, and I would flag for governance that this entry may speak more directly
to MECH-092 than to ARC-031's own distinguishing content. I have tagged it to ARC-031 because
trajectory-in-abstract-space is what it evidences and that is ARC-031's object, but the weighting is
arguable.

## The other gap, briefly

Task states are experimenter-defined and learned from feedback. They are states of the environment
and the agent's relation to it, not states of the agent's own epistemic condition. z_self -- D_eff,
hypothesis-tag integrity -- has no counterpart here.

## Confidence

0.5. Method caveats are real: fMRI replay detection sits near the edge of what the technique
supports, and the authors present establishing feasibility as part of their contribution. But the
sequence result is the piece ARC-031 most needs and least had, and it is worth having on file at
that weight. Standing caveat as elsewhere in this pull: ARC-031 is phase-locked v4 with zero
distinguishing substrate in ree-v3.
