# The metastable brain (Tognoli & Kelso, 2014) -- Q-081, INV-091, ARC-112

## What the paper did

A Neuron review by the two researchers most associated with Coordination Dynamics, setting out
metastability as the answer to a question REE's cluster restates almost word for word: how do
parts of a system engage and disengage over time while remaining one system? Their answer is
that the brain occupies a regime where two tendencies coexist -- for regions to express
individual autonomy and specialised function, and for them to couple and coordinate globally.
Neither wins. The review illustrates this in continuous neural and behavioural recordings and
argues the regime underlies real-time cognitive, behavioural and social coordination.

The formal core is symmetry breaking. In the elementary coordination law, metastability appears
when the tendency of components to couple is set against their tendency to express intrinsic,
different behaviour -- and the coupling is not strong enough to win. What results is neither
locking nor independence but a succession of dwells (relative phase moves slowly, integration
dominates) and escapes (the system releases and moves on).

## Key findings relevant to the cluster

Three things are worth carrying, and only three.

The first is the architectural proposition itself, which is the closest external statement of
ARC-112 I have found: a system can be integrated without being synchronised, and without a
central controller imposing the integration. The raw thought's framing -- "a federation of
asynchronous, partially independent cognitive streams coordinated by shared organisational
constraints" -- is the same proposition arrived at independently.

The second is the anti-collapse qualification, which this literature states as a *requirement*
rather than a caveat. Integration must not be confused with homogenisation: the value of the
metastable regime is precisely that segregation survives it. INV-091 asserts that integration
and protected non-equivalence are jointly necessary. This review says the same thing from the
other end -- that a system which achieved integration by making its parts alike would have lost
the thing integration was for.

The third is dwell/escape as vocabulary for the band. If both the locked limit and the
independent limit are failures, the relationship between cross-stream similarity and function
cannot be monotonic. That is exactly the shape INV-091 predicts and the shape its falsifier
(an ablation series producing a non-monotonic curve) is built to detect.

## How this translates to REE

Carefully, and less far than it first appears.

The framing transfers: REE-as-federation has an external precedent, and the requirement that
integration preserve difference is not something the programme invented to protect its own
design choices. That matters for ARC-112, which is a framing claim and was registered on the
understanding that it must earn its keep as the parent node for the other three.

The mechanism does not transfer, and the reason is worth stating because it is close to being
the whole of Q-081. In this literature the rate structure *emerges*: components have intrinsic
frequencies, coupling competes with detuning, and the metastable regime is what that competition
produces. In REE the rate structure is *configured* -- E1 every step, E2 every three, E3 every
ten, written in a config file. Q-081 asks whether a system with imposed rate separation gets
anything resembling what a system with emergent rate separation gets. This paper describes the
target state in detail and is silent on whether an imposed-rate system can reach it. Reading it
as support for REE having done so would be the exact error the raw thought's self-correction
already warns against.

## Limitations and caveats

The operational content is relative phase between oscillators, and REE has neither oscillators
nor phase. Any REE analogue of a "dwell" would be a redefinition -- a period of stable
cross-stream configuration, say -- and redefinitions do not inherit the original's validation.
The 2024 Nature Reviews Neuroscience review (also in this pull, and with Kelso as an author)
supersedes this one on measurement specifically, and its Box 2 warns that dwelling-then-switching
is necessary but not sufficient for the inference this framework wants to make.

This is also a review rather than a test. It argues for a regime and illustrates it; it does not
adjudicate between metastability and its alternatives in any dataset, and the later review says
the field still largely cannot.

GOV-ANALOGY-1: analogy, not evidence. Nothing about REE is established by the brain being
organised this way.

## Confidence

0.52 -- deliberately modest for a paper this influential. Source quality 0.85 (Neuron, the
originating authors, and the reference point for everything downstream). Mapping fidelity 0.55:
the architectural claim maps onto ARC-112 and INV-091 about as directly as external literature
can, while the mechanism maps onto nothing in REE. Transfer risk 0.55, the highest in this pull,
because the concept cannot be operationalised in REE without being redefined first.

Its value is that it names the target state and insists both extremes are failures. It has no
bearing on whether REE reaches it. Literature confidence 0.52; experimental confidence 0.0.
