# Reality filtering versus context source monitoring (Bouzerda-Wahlen et al. 2015)

## What the paper does

The authors put two memory-control processes inside one continuous recognition task, so that the
comparison could not be an artefact of different paradigms. One was context source monitoring:
remembering the precise past context in which a piece of information was acquired. The other was
orbitofrontal reality filtering: sensing whether an upcoming thought, assembled from memory
fragments, refers to present reality and may be acted upon. Both have been blamed for false
memories, including confabulation, and whether they share a mechanism was unknown. High-resolution
evoked potentials were recorded while healthy participants performed the task.

They dissociated on both channels. Reality filtering produced a frontal positivity, a specific
electrocortical configuration, and estimated posterior medial orbitofrontal activity at 200-300 ms.
Context source monitoring produced nothing at all in that early window; it was slower and less
accurate, and produced a prolonged frontal positivity beginning at 400 ms. The authors describe
this as a hitherto unrecognised separation, and are careful to add that while deficient reality
filtering has an established correlate in reality confusion, the behavioural correlate of deficient
source monitoring still needs controlled exploration.

## Why it bears on MECH-037 in two opposite directions

The supportive direction is architectural, and I think it is the more durable of the two. REE's
`papez_circuit.md` draws a boundary that is easy to state and hard to honour: the loop "can amplify
or suppress candidate trajectories", but "does not mint authority writes" and "does not bypass
E3/verifier commit checks". What this paper shows is that the brain really does implement that
boundary -- a fast, cheap, pre-commitment bias at 200-300 ms that is not the same thing as, and
runs well ahead of, the deliberate attribution machinery that decides where a memory came from. If
REE built the provenance gate as a second verifier, it would have built the 400 ms process. The
dissociation is evidence that the two-stage design is the right one.

The weakening direction is about what the gate reads. MECH-037 says the gate consults provenance --
trace presence, temporal ordering, recency. But provenance read-out, as operationalised here, *is*
the 400 ms process. Put this beside Liverani et al. 2015 in this same directory and a consistent
pattern emerges: every signal REE nominates as an input to the fast gate turns out, on measurement,
to be a slow process sitting downstream of it. That is a strong enough regularity that I would treat
it as the central finding of this pull rather than as two separate caveats.

## How I would translate it

The claim's architecture survives; its causal story needs rewriting. The honest reformulation is
something like: there is a fast pre-commitment gate whose output *correlates with* provenance but
whose input is not a provenance read-out -- it is something cheaper that provenance happens to
track. In Schnider's account that cheaper thing is extinction, a relevance suppressor. Whether REE
wants to implement that, or wants to argue that its trace signal is available at gate latency in a
way the human ordering/source read-outs are not, is a substrate question and a real one. Either way
the experiment MECH-037 needs has to instrument the gate's latency, not only its accuracy: a REE
gate that gets the right answer by consulting an expensive downstream signal would pass a pure
accuracy criterion while implementing the wrong mechanism.

## Limitations and confidence

Healthy participants only, and the abstract does not state the sample size, which is a real
limitation for a single-lab ERP dissociation. Source localisation from scalp potentials is coarse,
so "posterior medial orbitofrontal" is an inference. And the authors' own caution matters: the
asymmetry in clinical consequence between the two deficits is asserted from the existing literature
on one side and explicitly left open on the other. Mapping any of this onto REE's E1/E3 commitment
architecture is a substantial abstraction. Confidence 0.70, direction `mixed` -- it genuinely
supports one half of the claim and genuinely weakens the other, and collapsing that to a single
direction would lose the information governance needs.
