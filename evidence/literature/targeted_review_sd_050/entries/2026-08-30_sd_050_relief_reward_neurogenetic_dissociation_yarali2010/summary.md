# Yarali & Gerber 2010 -- relief learning is neurogenetically dissociable from reward learning

## What the paper did

Drosophila olfactory conditioning, with the valence of the learned odour set by whether it precedes
or follows an electric shock. Onto that the authors layer targeted genetic interference. Blocking
output from TH-Gal4 dopaminergic neurons with UAS-shibire(ts1) partially impaired punishment
learning but left relief learning intact. The tbh(M18) mutation, which compromises octopamine
biosynthesis, partially impaired sugar-reward learning but left relief learning intact. Blocking the
DDC-Gal4 and TDC2-Gal4 populations affected neither. The conclusion, stated carefully and with
respect to the specific tools used: relief learning is neurogenetically dissociated from both
punishment and reward learning.

## Why this is the entry that matters for SD-050

SD-050 has two halves, and they are not equally well defended. The first -- that a relief-completion
event exists and should be detected -- is supported by Gerber 2014 and by the Navratilova grounding
already in the claim. The second is a reuse assertion: relief-completion should fire *the same
downstream tag-and-release pipeline as goal-achievement*, meaning MECH-057a's beta-gate release and
MECH-094's VALENCE_LIKING write. That half has been carried mostly by architectural economy. It is
cheap, the pipeline already exists, and relief feels like a reward.

This paper is the best available reason to be suspicious of that feeling. In the one preparation
where relief and reward have been separated with genetic precision, they came apart: the octopamine
manipulation that degraded sugar-reward learning did nothing to relief learning. If relief were
simply a call into the reward machinery, that result should not be obtainable.

## The reading under which SD-050 survives -- and why I am not taking it as a free pass

The honest counter is that this is a dissociation of *teaching signals*, not of *effectors*. What
Yarali and Gerber separated is which neuromodulatory populations are required to establish the
memory. What SD-050 asserts is shared is what the event then writes to -- the beta gate, the valence
field. Two distinct upstream paths converging on a common downstream write is a perfectly ordinary
architecture, and nothing here excludes it.

So the paper does not refute SD-050 as literally stated. What it does is remove the presumption. The
burden shifts: REE now has to show that routing relief-completion through the goal-achievement write
is behaviourally correct rather than merely convenient, and that it can ablate relief-completion
independently of goal-achievement tagging. That is a real design constraint the claim does not
currently carry. Given the claim's own falsifier branch (b) -- fires occur but one or both reuse
sites do not execute -- this entry is best read as saying the reuse half deserves its own measurement
rather than inheriting the detector's.

## Limitations

This is the longest transfer hop in the pull and I want it named rather than softened. Drosophila
has no mesolimbic homologue; the octopamine/dopamine division of labour in flies has no counterpart
in REE's single valence channel; several of the reported impairments are partial, which the authors
do not over-read and neither should this entry. Mapping fidelity is scored at 0.58 and transfer risk
at 0.62 for exactly these reasons. The entry is filed as `weakens` because it weakens a presumption
that is doing real architectural work, not because it falsifies a measured prediction.

## Confidence

0.62. Low enough to reflect the invertebrate preparation and the teaching-signal-versus-effector
mismatch; high enough to register that this is the only direct evidence anyone has on the question,
and it points away from the convenient answer.
