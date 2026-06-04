# Development of the ability to use recall to guide action: infants' AB performance (Diamond 1985)

## What the paper did

Diamond tested 25 infants fortnightly, from the age each first reached for a hidden object until
12 months, on Piaget's A-not-B (AB) task: an object is hidden at location A, the infant retrieves
it (repeated until reliable), then the object is hidden at B in full view — and the young infant
reaches back to A. Her central manipulation was *delay*: the interval between hiding and the
infant being allowed to reach. She found the delay an infant could tolerate before committing the
A-not-B error rose steadily — roughly two seconds per month, from under two seconds at 7.5 months
to over ten seconds by twelve. She paired this with the cross-species fact that rhesus monkeys
with bilateral dorsolateral-prefrontal lesions reproduce the error at comparable delays, while
intact monkeys do not.

Her interpretation reframed the error. It is not that the infant has lost the object, or believes
it is back at A. It is that succeeding requires two maturing abilities — holding the new (B)
location in working memory across the delay, and *inhibiting* the prepotent, previously-rewarded
reach toward A. When either fails, the hand goes to A even though, on looking-time measures, the
infant may well represent the object at B. The A-not-B error is a limit on *using recall to guide
action*, not on whether the hidden object is represented.

## Why it grounds MECH-045 / ARC-006

This is the entry that supplies the **store-versus-readout** distinction — and that distinction is
the precise shape of REE's *partial* permanence. The SD-039/MECH-292/293 ghost-goal bank does two
separable things: it *stores* a value snapshot that persists when its spatial anchor is out of view
(the store), and it *queries* that store by wanting-rank to influence behaviour (the readout).
Diamond shows that in biology these are genuinely separate stages, with distinct maturational
timelines and distinct substrates: the persistent representation can be in place while the action
that should use it perseverates. The hidden-object representation is the competence; using it to
reach correctly is the performance; and the A-not-B error is a performance failure sitting on top
of an intact-or-near-intact competence.

For the permanence pillar this carries a design lesson. A permanence mechanism is not finished when
it has a buffer that holds an object out of view. It also needs a *retrieval/selection* stage that
can read that buffer without being captured by a prepotent prior response — and that stage is
delay-sensitive and fallible in its own right. REE's analog of the A-not-B failure would not live in
a damaged store; it would live in the query layer (the wanting-rank readout, or whatever action-
selection consumes it) perseverating on a previously-rewarded option. That is a useful failure mode
to be able to name, because it predicts that a *correct* permanence store can still produce wrong,
perseverative behaviour — exactly the kind of dissociation that makes a substrate interesting to
test.

## Limitations and caveats

The substrate does not transfer. Diamond localises the readout limit to prefrontal working memory
and response inhibition; REE's ghost bank is a hippocampal-anchored value store queried by
wanting-rank. So what transfers is the *functional architecture* — store and readout as separable
stages — not the neural locus. I have kept the mapping explicitly functional-analogical. There is
also a deeper live controversy I should not paper over: whether the A-not-B (search) literature and
the Baillargeon (looking-time) literature are even measuring the same construct. The reach-based and
look-based tasks dissociate, and which one indexes "real" permanence is unsettled. Diamond's account
is in fact one of the better resolutions of that tension — the looking-time competence is real and
early, the search performance is later and prefrontally gated — but I have flagged the controversy
rather than assume it away.

## Confidence reasoning

Confidence 0.71. Source quality is high (0.80): a landmark longitudinal study corroborated by a
clean lesion comparison, foundational to the entire executive-function reading of infant cognition.
Mapping fidelity is moderate (0.68) — the store/readout dissociation transfers cleanly and is exactly
what REE's ghost bank instantiates, but the prefrontal substrate does not match REE's hippocampal
store, so the bridge is architectural rather than mechanistic. Transfer risk is moderate (0.40). The
entry's contribution is conceptual precision: it tells the permanence pillar to separate the buffer
from the (fallible, delay-sensitive) act of reading it.
