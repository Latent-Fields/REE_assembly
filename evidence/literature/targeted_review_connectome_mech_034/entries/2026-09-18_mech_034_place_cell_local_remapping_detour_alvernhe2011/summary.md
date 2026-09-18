# The rat that found the detour, and the map that only changed near the barrier

Alvernhe, Save and Poucet ran a Tolman detour: a familiar three-way maze, two rewarded end locations,
and then -- in specific sessions -- a transparent barrier dropped across the shortest central path.
The rats did what Tolman's rats did, choosing the shortest alternative detour rapidly and
consistently. The interesting part is what the hippocampus did while they did it.

CA1 and CA3 place cells with fields *near the barrier* remapped locally. Cells with fields away from
the barrier did not change. The representation updated precisely where the world's navigability had
changed, and nowhere else.

## Why I chose this paper for MECH-034

Of everything in this pull, this is the entry whose dependent variable most literally *is* the thing
MECH-034 calls a viability map. No harm was delivered. Reward locations were unchanged. What changed
was whether a path could be traversed, and the representation that moved was a representation of
where the animal can go. That is navigability, updated from experience, in isolation from value --
which is the half of MECH-034 that the reward-learning literature simply cannot speak to.

The spatial confinement matters more than it might first appear. MECH-034's registered falsifier asks
that manipulation M raise staleness *at the perturbed region* and not elsewhere, with off-diagonal
effects held under a fifth of the on-diagonal effect. Alvernhe et al. is the biological existence
proof that a feasibility representation can in fact update with that kind of locality, which is not a
foregone conclusion -- a global remap would have been an entirely plausible result and would have made
the region-keyed design of the StalenessAccumulator look like an architectural convenience rather than
a principled choice.

## Two honest complications

First, and the authors raise it themselves: this finding sits awkwardly with their own earlier
shortcut-task result, where CA3 discharge was altered for *distant* fields. Their reading is that
opening a novel path and blocking a familiar one are not equivalent manipulations, and that CA3 has a
specific role in representing spatial connectivity and sequences. I think that is the right reading,
but it carries a consequence for REE: the locality MECH-034 leans on is condition-dependent, not a
law. A V3 manipulation-M arm needs to say which of the two it implements -- closing an affordance or
opening one -- before its locality prediction is even well posed. That is a design note worth carrying
into the experiment, and it is why I logged it as a failure signature rather than burying it here.

Second, the barrier confounds two things MECH-034 keeps separate in its wording. The claim defines
viability mapping as updating from predicted-observed *self-sensory mismatch*. A transparent barrier
delivers mismatch (the rat expected to pass, and did not) but it also changes the affordance structure
directly. The paper cannot tell us which drove the remapping. For REE's purposes the two are meant to
be the same mechanism, so this may not be a problem -- but it is an assumption, not a finding.

## Confidence

0.72, direction `supports`. The mapping fidelity here (0.75) is the best in the pull. The discount is
transfer: rodent place fields code physical space, REE's navigability surface is over action-object
space, and a physical barrier is a blunter instrument than a region-scoped dynamics perturbation.
