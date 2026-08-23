# The hippocampus as a predictive map (Stachenfeld, Botvinick & Gershman, 2017)

**Claim tested:** Q-095 — does explicit coordinated episodic organisation add capability
beyond REE's existing trajectory-generation account, or is it a re-description?
**Direction: weakens** (i.e. supports the REINTERPRETATION horn), confidence 0.68.

## What the paper did

The authors ask a normative question rather than a descriptive one: given that an agent is
trying to maximise future reward, what spatial representation is most *useful*? Their answer
is the successor representation — encode each state by its expected discounted future
occupancy under the current policy. They then show that this representation, derived purely
from the predictive/RL objective, reproduces a long list of place-cell findings that the
classical "cognitive map" metaphor struggles with: place fields skew backwards along
travelled trajectories, they are sensitive to reward, they depend on the policy rather than
on geometry alone, and they change with barriers and environment structure. Grid cells then
fall out as the low-dimensional eigenbasis of that same predictive representation, useful
for noise suppression and for multiscale hierarchical planning.

Nothing in the model stipulates episodes, binding, segmentation, separation, or completion.
The organising structure is a *consequence* of predicting where the trajectory goes next.

## Why this is the paper Q-095 has to survive

Q-095 is deliberately posed against itself: the raw thought's own falsification condition is
that if the existing architecture already produces appropriate episodic discrimination,
completion and context-sensitive retrieval without an additional organising principle, then
the thought is a re-description and should not be promoted. This paper is the published form
of exactly that worry, and it is not a weak form. It shows that a substantial part of what
looks like hippocampal "organisation" is what you get for free from an objective REE already
runs. If REE's memory store were to develop place-like or grid-like structure and this were
reported as evidence for a coordinated episodic principle, that inference would be wrong
under this paper — such structure is the expected eigenstructure of a predictive
representation.

That is the sharpened bar it sets for Q-095's ADDS-CAPABILITY verdict. It is not enough to
show the coordinated version produces a nicer topology. The 2x2 in MECH-495's
`what_would_answer` already scores on downstream generalisation and discrimination rather
than internal representational statistics, and this paper is the reason that choice is right
rather than merely fashionable: internal statistics cannot separate the two hypotheses,
because the null hypothesis produces them too.

## Where it stops, and why the confidence is 0.68 rather than 0.85

Honesty about scope matters more here than usual, because the temptation is to read this as
settling Q-095 in the negative. It does not. The successor representation is a claim about
*state* representation in a broadly spatial setting. It speaks to the geometric members of
the thought's six capabilities — indexing/addressing, and remapping — and is silent on the
compositional ones. It does not bind objects, locations, actions, internal states, goals and
outcomes into a single event representation; it does not segment a continuous stream into
events; it does not perform holistic retrieval of an event's incidental elements. Q-095's own
notes identify BINDING as the capability with no clean existing owner and the most likely
source of a future claim, and that is precisely the capability this paper leaves untouched.

So the correct reading is a partition, not a verdict: for the geometric half of the bundle,
the reinterpretation horn now has real published weight and REE should not claim novelty
there. For the compositional half, this paper is simply not evidence either way, and the
question stays genuinely open.

## Mapping caveat

The transfer here is at the level of objectives, not anatomy — the argument is "a predictive
objective suffices to produce X", which is substrate-agnostic and travels to REE reasonably
well. The risk is in the other direction: over-reading a spatial-representation result as
covering episodic composition. `mapping_fidelity` is set at 0.62 to record that the paper
addresses roughly two of the six capabilities Q-095 bundles together, and any use of this
entry that treats it as covering all six is a misuse of it.

Note also the non-degeneracy precondition already recorded in Q-095: as of 2026-08-20 the
existing mechanisms are not all armed (MECH-147 unbuilt at phase v4, MECH-074d demoted, the
ContextMemory write path repaired only on 2026-08-19 with no scored validation). This entry
does not change that. A null result obtained before the substrate is ready still measures
readiness rather than the question, and this paper — which makes the null result *more*
plausible a priori — makes that confound more dangerous, not less.
