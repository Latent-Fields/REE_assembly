# Ambrosi & Lerner 2022 — Striatonigrostriatal closed-loop architecture

## What the paper did

Ambrosi & Lerner used transsynaptic viral tracing combined with intersectional genetic
tools in mice to ask a precise question: when the dorsomedial striatum (DMS, associative
loop) and dorsolateral striatum (DLS, sensorimotor loop) project through the substantia
nigra and back, are those projections forming closed loops (DMS -> SN_DMS -> DMS) or
open loops (DMS -> SN -> DLS)? The "ascending spiral hypothesis" (Haber 2003, Haber et al.
2000) had proposed that open loops are the mechanism by which information transfers
between striatal subregions during habit formation -- so this is a direct test of the
strongest version of the integrative crosstalk story.

The team additionally recorded whether functional synapses in open-loop configurations
could actually modulate tonic dopamine neuron firing, which is what would matter for
the spiral hypothesis to do real work.

## Key findings relevant to Q-019

Two main findings, both relevant to the three-gate vs single-gate architecture question.

First, closed loops dominate. Striatal subregions project through the substantia nigra
in a way that returns to the same subregion -- meaning DMS and DLS each substantially
regulate their own dopamine release. This is exactly what Q-019's three-gate model
needs: anatomically distinct loops with internal control of their own learning signals.

Second, the open-loop component is real but functionally weak. Synapses do exist in
the cross-loop configuration, but they fail to modulate tonic dopamine firing. So the
"DMS hands off to DLS via dopamine spiral" story is, at minimum, more constrained than
the integrative network view suggests.

## How this maps to REE

Q-019 is the open question of whether REE's three-gate model (sensorium loop, thought
loop, action commitment loop) is anatomically and functionally segregated, or whether
a single-gate model with three convergent criteria better describes the biology.
Ambrosi & Lerner come down on the side of segregation -- at least for the DMS/DLS
boundary. The closed-loop result is the strongest modern causal evidence for parallel
segregated processing in the BG, complementing the older Alexander 1986/1990 anatomical
work that already lives in this targeted_review.

For REE-V3 specifically, this evidence supports keeping E1/E2/E3 update channels
distinct rather than merging them into a single critic. It also supports MECH-069
(incommensurable error signals across the three loops) -- if the loops were truly
integrative at the dopamine level, MECH-069 would be harder to defend, because the
same dopamine signal would be available across loops.

## Limitations and caveats

The paper studies dorsal striatum only (DMS and DLS). The ventral striatum and the
classical "limbic-to-associative-to-motor" spiral that Haber 2008 emphasises is not
directly tested. So while Ambrosi & Lerner are decisive against open loops in the
dorsal striatum, the limbic-to-cognitive ascending spiral could still be operative.
For Q-019, this means the segregation premise holds well between sensorium and action
commitment loops, but the thought loop's relationship to either remains an open question
that needs separate evidence -- specifically primate or human work, since the limbic
spiral is most commonly invoked in the context of cognitive-emotional integration.

Mouse-to-human transfer is also a real risk, though basal ganglia architecture is
broadly conserved across mammals and the parallel-loop model was originally derived
from primate work.

## Confidence reasoning

I rate this 0.82. Source quality is high (Cell Reports, modern causal methods,
peer-reviewed). Mapping fidelity is good for the segregation question -- the paper
asks essentially the same question Q-019 asks, with better tools than were available
to Alexander or Haber. Transfer risk is moderate; mouse BG architecture is broadly
conserved. The main reason it isn't higher is that the paper doesn't directly test
the three-loop model -- it tests two of the three. A V3 experiment that asks whether
distinct error signals must flow through distinct learning channels (MECH-069) would
benefit from this evidence as anatomical grounding.

According to PubMed: [10.1016/j.celrep.2022.111228](https://doi.org/10.1016/j.celrep.2022.111228)
