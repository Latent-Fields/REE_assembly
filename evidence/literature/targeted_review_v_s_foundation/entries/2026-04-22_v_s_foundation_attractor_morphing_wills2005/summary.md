# Wills, Lever, Cacucci, Burgess & O'Keefe 2005 -- Attractor dynamics in the hippocampal representation of the local environment

DOI: [10.1126/science.1108905](https://doi.org/10.1126/science.1108905) -- Science (PubMed 15879220)

## What the paper did

Rats were familiarised over six days with two distinct enclosures (square and circular, different materials). CA1 place-cell ensembles were recorded as the environment was systematically morphed through intermediate (octagonal) shapes on day 7. The question: do hippocampal representations transition smoothly across the morph series (continuous coding) or do they snap between discrete states (attractor coding)?

## Findings relevant to V_s foundation

When pre-exposure created two distinct context-bound representations, place-cell ensembles abruptly and simultaneously switched between square-mode and circle-mode firing as shape changed incrementally. The transition was sharp, near-step-function, not graded. Critically, the same physical location was represented by two different attractor states depending on which side of the transition the morph sequence was on. This is the cleanest published demonstration of bistability between coexisting hippocampal representations of the same place.

## Translation to REE / MECH-269 / MECH-272

This is the strongest single piece of biological support for hard active/inactive dual-trace anchors. Wills shows two attractor states for the same physical place can coexist, and the system switches between them in near-step fashion under input morphing. MECH-269 dual-trace preservation maps onto this directly: the inactive anchor is the attractor state not currently dominating, and routing flips it to active when input crosses the basin boundary.

The architectural commitment (anchors marked active vs inactive, with hard switching) gets direct empirical support from this paper. It also provides a scaling argument: pre-exposure was required for the bistability to emerge -- familiarity created the two attractors. This implies that in the substrate, an anchor set seeded only from current experience will not yet have the bistable structure; dual-trace coexistence requires repeated exposure under conditions that establish each anchor as a stable attractor.

The paper is also evidence that what determines which anchor fires is the current input pattern hitting one basin or the other -- consistent with MECH-272 routing being driven by input rather than by V_s alone. V_s on the active anchor would only be informative once the input has already moved into the alternate basin (so the active anchor is now mismatched). The trigger therefore looks like a downstream consequence of the routing decision, not its cause.

## Limitations and caveats

CA1 only -- the underlying substrate (CA3 attractor or upstream input-distance gating) is inferred. Geometric morphing only. Bistability required pre-exposure; whether all anchors in the substrate eventually settle into bistable basins, or whether some remain graded indefinitely, is open. N=4/6 rats showed the bistability cleanly. Rodent only.

## Confidence reasoning

Source quality very high (Science, O'Keefe lab). Mapping fidelity is high for the qualitative claim (two attractor states for same place; near-step switching). Transfer risk low for the substrate claim, moderate for assuming V_s drives the switching (the paper instead implicates input-distance crossing the basin boundary).