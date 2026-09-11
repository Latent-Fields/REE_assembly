# The same ordering, arrived at independently (Jacquey et al., 2019)

## What the paper did

This is a review rather than an experiment, and it is the one paper in today's ARC-059 pull that
sits on the supporting side. Jacquey, Baldassarre, Santucci and O'Regan take sensitivity to
sensorimotor contingencies -- the detectable relation between what an agent does and what it then
senses -- and follow it across two literatures that do not usually get read together: infant
developmental psychology and developmental robotics. Their synthesis is that this single sensitivity
drives the acquisition of body knowledge first, and then memory, generalisation and goal-directedness
downstream of it. They close by proposing a blueprint architecture: an agent that exploits
contingency sensitivity, combines it with goal-setting, and acquires skills in that order.

## How this bears on ARC-059

The value here is the convergence, and it is worth being precise about what kind of value that is.
ARC-059 asserts a three-stage construction order with stage 1 -- action-space discovery through
motor experimentation -- producing the substrate the later stages consume. Jacquey et al. arrive at
a structurally identical commitment from a different starting point, and crucially they arrive at it
*for artificial agents*, not only as a description of infants. That matters for mapping fidelity,
which I have set at 0.8: most developmental evidence has to be translated across a species and an
embodiment gap before it says anything about REE, and this review has already done that work in its
own terms. The blueprint is close enough to a curriculum specification that the translation is
almost a restatement.

## The reason I have capped confidence at 0.65

A review that argues for an architecture is not evidence that the architecture is necessary. Nothing
in this paper withholds the contingency-learning stage and measures what degrades downstream; the
ordering is defended on grounds of coherence and convergent plausibility, which is the same footing
ARC-059 currently stands on. Counting it as confirmation would be double-counting a commitment
rather than testing it -- the confirmer failure mode, arriving in the politest possible form. The
honest description is that this raises ARC-059's *literature grounding* (the backlog reason that sent
me here) without moving it any closer to promotion, and I would resist any later reading of the
evidence matrix that treats it as doing the latter.

## Read alongside today's other two entries

The picture this pull leaves is not flattering to a naive version of the claim, and I think that is
the useful outcome. Jacquey et al. support the stage-1-first ordering on architectural grounds.
Klein-Radukic and Zmyj find no longitudinal trace of the corresponding developmental route in human
infants. Surian and Caldi find the stage-2 → stage-3 dependency running the wrong way at 10 months.
Three papers, three different footings, and the one that supports the claim is the one that is not
an empirical test.

For ARC-059 specifically that convergence-without-confirmation pattern is a live warning rather than
an abstraction. The claim's own `what_would_answer` already records that the skip-ordering ablation
is not currently constructible on V3 -- the action space is hand-wired, and the MECH-276
counterfactual-attribution feedstock is not substrate-ready. What this pull adds is that even once
those gates clear, two of the three studies here describe ways the ablation could return an
uninformative null for reasons unrelated to whether the ordering is real.
