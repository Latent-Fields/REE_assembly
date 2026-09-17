# Spatial representations of self and other in the hippocampus (Danjo et al., 2018)

## What the paper did

Danjo, Toyoizumi and Fujisawa recorded CA1 pyramidal cells in rats running an observational T-maze
task, and asked whether hippocampal spatial coding extends to the position of another animal. It
does. They report that information about the spatial location of both the self and the other was
jointly and discretely encoded. A subset of cells had spatial receptive fields that were identical
for self and for other.

This appeared back-to-back with Omer et al. in the same issue of *Science*, from an independent
laboratory, in a different species, using a different paradigm. That convergence is the main reason
to take the phenomenon seriously rather than as an artefact of one lab's task design.

## Why this bears on ARC-083

The phrase that matters for REE is "jointly and discretely encoded". Jointly, because self and other
are simultaneously present in one population -- there is no separate other-module. Discretely,
because the two are recoverable as distinct. That combination is roughly what ARC-083 needs: the
other agent lives inside the general object/place machinery (the ARC-080 inheritance) while
remaining individuated (the token-keying).

But "discretely encoded within a shared population" and "has its own slot" are not the same
architectural statement, and the difference is not cosmetic. The first is multiplexing; the second is
allocation. ARC-083 asserts allocation. And the same paper reports the finding that most strains
that reading: a subset of cells fired for the same place whether the rat itself or the other animal
occupied it. Those cells are not keyed to an agent token at all. They are keyed to a location, with
the occupant's identity discarded.

## The limitation that matters most

A single-other paradigm cannot test what makes ARC-083 an architectural claim. ARC-083 says each
other agent j gets its own slot -- the interesting content is in the plural. Distinguishing me from
one other animal is a much weaker capacity than maintaining separate persistent files for several
agents and keeping them from cross-contaminating. Nothing here tests allocation across multiple
others, and nothing tests whether a file for the other animal persists once that animal leaves.

That second gap connects to a hole I should flag explicitly rather than paper over. ARC-083 inherits
from DEV-NEED-021 the strong prerequisite that otherness inference REQUIRES object permanence plus
self-stability. I went looking for evidence on that prerequisite in this pull and found none -- it
remains an assertion carried forward from the developmental needs register, not a literature-grounded
finding. It should be pulled separately rather than treated as covered by these hippocampal entries,
which speak only to the representation and not to its developmental preconditions.

## Confidence

0.60, matching the Omer entry, for the same reasons: excellent source quality, moderate mapping
fidelity, moderate transfer risk. The convergence between the two papers raises my confidence in the
*phenomenon* considerably while leaving my confidence in the *architectural translation* where it
was -- these are separate things, and it would be a mistake to let the first inflate the second.
