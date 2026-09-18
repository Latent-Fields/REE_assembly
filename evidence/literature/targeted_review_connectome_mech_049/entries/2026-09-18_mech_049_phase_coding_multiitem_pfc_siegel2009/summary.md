# Siegel, Warden & Miller (2009) -- phase separation of concurrent content in primate PFC

## What the paper did

Monkeys held two visual objects in short-term memory across a brief delay while neuronal activity was
recorded from prefrontal cortex. During the delay, the prefrontal population was rhythmically synchronised
at roughly 32 Hz and again near 3 Hz. The analysis asked a specific question: does the information a spike
carries about *which* object is being remembered depend on *when in the oscillatory cycle* the spike occurs?

It does. Spikes carried the most information about the memorised objects at specific phases, and -- this is
the part that makes the result hard to explain away -- the optimal phase differed systematically by
presentation order, with the first-presented object peaking significantly earlier in the 32 Hz cycle than
the second.

## Why this entry is here

The other two neuroscience entries in this directory both descend from the Hasselmo SPEAR lineage. That is a
real independence problem for an evidence base: the foundational model, its empirical test and its
retrospective review share an author, and a claim supported only by one lab's programme is less well
supported than the entry count suggests. This paper is from a different lab, a different structure
(prefrontal rather than hippocampal), a different species (macaque rather than rat), and a different
theoretical starting point.

It also sits closer to REE's architecture in a way that matters. MECH-049 is about proposal, evaluation and
veto -- deliberative operations, which in a primate live in prefrontal cortex, not in the hippocampal
formation. Whatever the hippocampus does with theta, the question for REE is whether the cortical substrate
that would host its stages can use phase this way. Siegel et al. say it can.

## What it establishes, precisely

The weakest and most portable version of MECH-049's premise: temporal phase is a usable resource for keeping
concurrently-active things from contaminating one another. Two objects held at once are not smeared into a
single superposed representation. They are assigned distinct phases, and the assignment is systematic rather
than arbitrary.

That is an existence proof for the substrate MECH-049 presupposes. It is not the claim.

## Where it stops, and why the gap is wide

The distance between this result and MECH-049 is the distance between *multiplexing* and *protection*, and I
do not think it should be glossed.

Two remembered objects are symmetric, mutually indifferent, and equally passive. Neither is trying to
influence the other; there is no incentive gradient running between them. An optimiser and a constraint on
that optimiser are none of those things. They are asymmetric, in tension, and -- this is the entire content
of MECH-049 -- the tension tends to resolve the wrong way, with the constraint absorbed into the objective,
unless something prevents it. Showing that phase keeps two indifferent representations distinguishable does
not show that phase keeps a constraint safe from a process that has a standing incentive to erode it.

There is also a timescale problem worth flagging for anyone designing against this claim. The operative
rhythm here is ~32 Hz, about 31 ms per cycle. The thought behind MECH-049 reasons at 100-300 ms. A 31 ms
window is too short to contain a deliberative harm evaluation, so if REE cites this result as evidence for
its phase architecture it is importing from a timescale two orders of magnitude away from the one the claim
needs. The ordering effect compounds this: if phase is already carrying serial position, it is not
simultaneously free to carry functional-stage identity without a multiplexing scheme nobody has specified.

Finally, this is correlational. Phase was measured, not manipulated. The authors are appropriately careful
-- encoding at distinct phases "may play a role" in disambiguation. Nothing here shows that collapsing the
phase difference degrades memory, which is the perturbation that would make the separation causal.

## Confidence

0.62, direction supports. High source quality, genuinely independent of the other neuroscience entries here,
and in the right structure and species. Marked down on mapping because it separates content rather than
function, and content separation is multiplexing rather than the independence-preservation MECH-049 asserts.
