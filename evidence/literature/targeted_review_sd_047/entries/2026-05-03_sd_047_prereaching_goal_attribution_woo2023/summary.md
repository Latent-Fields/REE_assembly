# Woo, Liu, Spelke (2023): Prereaching Infants Attribute Goals

This is the falsifying entry in the SD-047 lit-pull, and it deserves
to be read carefully because it is the cleanest available challenge
to the strong reading of the substrate-ceiling diagnosis. Woo, Liu,
and Spelke ran five experiments (N=117 total) with 3-month-old
infants who cannot yet reach for objects themselves. The question they
were testing is the classical Piagetian one: do infants need first-
person reaching experience before they can perceive others' reaches
as goal-directed? The classical answer was yes. The Woo et al.
answer is no — prereaching 3-month-olds rapidly learn whether a
specific agent's reaches are aimed at objects or at places, after
seeing the agent reach for the same object across varying locations
(or to the same place across varying objects). Passive movements do
not produce the same inferences, so the effect is specific to
goal-directed action perception.

Why this matters for SD-047: it is a direct challenge to the
inference chain "MECH-095 fails C1-C3 in V3-EXQ-506 → V3 env is too
clean → SD-047 multi-source dynamics fixes this." If 3-month-olds
can attribute agency from sparse, clean visual stimuli of reaching
movements, the substrate-ceiling diagnosis may be misreading what
features the comparator is sensitive to. Spelke's research programme
has consistently argued that motion-contingency, goal-directedness,
and biological-motion signatures are the load-bearing features for
agency perception, not multi-source noise statistics. SD-047's three
sources (smooth perturbation field, transient Poisson events, drift
sources) may not deliver any of those features in their relevant
forms, even when calibrated to the 1:1-2:1 env:agent change ratio.

Where the challenge has limits: the paper is about goal attribution
TO OTHERS — infants observing an agent and inferring its goals. This
is one architectural level above MECH-095's job, which is detecting
whether the agent's OWN action caused state change. The two
operations share machinery (both depend on a forward model and a
comparator) but they are not identical, and the substrate-ceiling
diagnosis on MECH-095 is specifically about the self-vs-not-self
discrimination, not the inference-of-others' goals. So Woo et al.
weakens the strong reading without invalidating the diagnosis
outright.

The right response to this paper is to treat it as a falsifiability
hook for the SD-047 implementation. If the pre-registered ON-vs-OFF
discriminative pair shows that multi-source dynamics do not flip
C1-C3, this paper is part of why: the relevant features may be
motion-contingency or goal-directedness signatures that V3 substrate
cannot deliver without genuine other-agents (V4-1 multi-agent
ecology). That would route MECH-095 from substrate_ceiling under V3
to V4-bound, and SD-047 would be retired as the wrong substrate
intervention. Better to know this before committing implementation
effort.

Confidence reasoning: source quality is high (Spelke lab, multi-
experiment design, N=117, online and lab methods). Mapping fidelity
is moderate because the paper addresses inference-about-others rather
than self-vs-not-self comparator function. Transfer risk is elevated
because infant looking-time paradigms have their own well-known
caveats (familiarity vs novelty looking, surprise vs interest
disambiguation). Net confidence ~0.65 — useful as the falsifying
voice in the set rather than load-bearing.

According to PubMed, [DOI: 10.1111/desc.13453](https://doi.org/10.1111/desc.13453).
