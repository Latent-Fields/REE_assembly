# Achiam, Held, Tamar & Abbeel (2017) -- the case FOR an explicit term, taken seriously

## Why this entry exists

Two of the three ARC-012 entries in this directory point the same way, and a literature pull that
only collects agreement is not evidence, it is decoration. This paper is here because it states the
opposing architectural position clearly, from a strong source, and because the failure mode it
identifies is one ARC-012 should be able to say something about.

## What the paper did

CPO is a general-purpose policy search algorithm for constrained reinforcement learning. Its
contribution is a method that trains neural network policies for high-dimensional control while
guaranteeing near-satisfaction of explicit constraints at *each iteration* of training, not merely
at convergence -- underwritten by a new bound relating the expected returns of two policies to an
average divergence between them. It is demonstrated on simulated locomotion with safety-motivated
constraints.

The sentence that matters for us is the opening premise rather than the algorithm: for many
applications it is more convenient to specify both a reward function and constraints than to try to
design the behaviour through the reward function alone. Systems that physically interact with or
around humans, the authors note, should satisfy safety constraints -- and the field's accumulated
experience is that folding those constraints into a single scalar objective is brittle.

## How this bears on ARC-012

ARC-012 says E3 does not require an explicit ethical cost term. CPO's whole design rationale is
that where behaviour must reliably respect a normative boundary, that boundary gets its own signal
and its own machinery, because the alternative does not hold up. If REE's ethical desiderata are
constraint-shaped, ARC-012 is betting against the prevailing engineering result, and the specific
prediction that follows is uncomfortable: an architecture with no explicit term has no analogue of
CPO's per-iteration guarantee, so ethical behaviour would be a property of the converged system
only, with nothing underwriting it *during* learning or at the tails of the distribution. That is
worth stating as a live failure signature rather than arguing away.

## Where the analogy loosens, and why this is 'weakens' not 'refutes'

Three things stop this from being decisive. First, CPO's constraints are externally specified,
scalar, and known in advance -- "do not enter this region". REE's ethical content, on the ARC-012
reading and via INV-001's care-marker route, is neither pre-specified nor obviously expressible as
a scalar constraint set, so the two architectures may simply not be competing for the same job.
Second, CPO argues from convenience and from what its guarantees require; it does not show that no
unconstrained architecture can reach the behaviour, and an existence proof on the other side is
exactly what Hutcherson et al. (2015) supply for one class of choice. Third, the constraint-based
framing presupposes that the ethically relevant quantity has already been identified and measured,
which is the part I suspect is actually hard.

So I read this as genuine pressure on ARC-012's *generality* -- it should not be asserted as a
universal architectural truth -- rather than as a refutation of it.

## Confidence

0.62. High source quality, moderate mapping fidelity. The number is held where it is by the
safety-constraint versus ethical-content gap; the entry earns its place less by adjudicating the
claim than by naming, concretely, the failure mode ARC-012 has to be willing to look for.
