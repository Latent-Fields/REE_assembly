# Social place-cells in the bat hippocampus (Omer et al., 2018)

## What the paper did

Omer and colleagues recorded from dorsal CA1 in bats while an observer bat watched a demonstrator
bat fly to a goal location. The question was whether the hippocampal spatial machinery -- the
place-cell system we normally think of as a map of where *I* am -- also carries where *someone else*
is. It does. A subpopulation of neurons represented the position of the other bat in allocentric
coordinates. The authors named these social place-cells. About half of them also represented the
observer's own position.

## Why this bears on ARC-083

ARC-083 commits REE to carrying each other agent j as its own token-keyed object-file slot -- a
specialisation of the ARC-080 object-file rather than a separate social subsystem. The claim has two
separable parts, and this paper speaks to them very differently.

The first part is about *format*, and the paper supports it well. The other bat is not encoded in
some dedicated social coordinate system; it is encoded in the same allocentric frame the animal uses
for places. That is precisely what licenses the architectural move ARC-083 makes: if the brain
formats another agent the way it formats the world, then treating other-as-object is not a
convenience, it is what the substrate already does.

The second part is about *separability*, and here the paper pushes back. Roughly half of the social
place-cells also carried the observer's own position. A clean token-keyed slot predicts a disjoint
code for agent j; what was measured is a substantially shared one. This does not refute ARC-083 --
an architecture can perfectly well maintain separate slots and still let them share representational
substrate -- but it means the slot is an idealisation, and the idealisation is doing work that the
biology does not obviously license.

## The question this does not answer, and it is the important one

ARC-083 asserts an *others*-specific specialisation. What would make that specialisation real is
evidence that these cells track agents as such, rather than tracking any behaviourally relevant
moving thing. If a moving inanimate object recruited the same population equally, the finding would
support the ARC-080 object-file umbrella and give ARC-083 nothing of its own -- the pillar would
collapse into its parent. The abstract does not settle this, and I have not resolved it here. Until
it is resolved, ARC-083's marginal contribution over ARC-080 remains formally open, which is worth
saying plainly given that the claim's own functional_restatement already concedes it is a thin
coherence-map child.

## Limitations and confidence

Bat dorsal CA1, observational spatial task, transferred to a V4 agent architecture that does not yet
exist. The paper evidences one field of the proposed slot -- the spatial state of agent j -- and is
silent on z_harm_a_j, drive, and the commitment chain, which are the fields that would make the slot
*social* rather than merely *spatial*. Source quality is near ceiling (Science, Ulanovsky lab,
careful design); confidence sits at 0.60 because for an architectural commitment the binding
constraint is mapping fidelity, not method quality, and the mapping here covers one field of four
and gets the separability wrong.
