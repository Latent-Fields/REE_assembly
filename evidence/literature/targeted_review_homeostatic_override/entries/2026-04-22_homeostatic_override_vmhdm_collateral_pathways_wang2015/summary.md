# Wang, Chen, Lin 2015 -- VMHdm Collateral Pathways

## Source
Wang L, Chen I-J, Lin D. "Collateral pathways from the ventromedial hypothalamus mediate defensive behaviors." Neuron 2015. DOI: 10.1016/j.neuron.2014.12.025

## Key claim
VMHdm SF1+ neurons send collateral projections to AHN, dlPAG, and other downstream targets. Optogenetic terminal stimulation reveals: VMHdm -> dlPAG drives freezing/immobility; VMHdm -> AHN drives avoidance. Distinct sub-behaviours are produced from the SAME upstream population by selecting DIFFERENT downstream nodes.

## Why this matters for REE V3
This is the canonical broadcast-with-downstream-arbitration architecture. One source, multiple outputs, behaviour determined by which downstream target wins. Direct evidence that V3's z_harm should be modeled as a broadcast signal arriving at multiple arbitration nodes rather than a switchboard with pre-routed channels.

## Failure signatures supporting REE
- **Broadcast topology, single source**: Same VMHdm cell projects to multiple downstream nodes. Architectural pattern matches SD-032a SalienceCoordinator's job: arbitration at the receiver, not at the source.
- **Behaviour selection happens downstream**: Different terminal stimulation produces different behaviour. The arbitration nodes (PAG, AHN) are where competition happens.
- **MECH-279's locus is one such node**: The dlPAG GABAergic gate is exactly where the broadcast meets a threshold-converter to commit freezing. V3-EXQ-471's lock-in maps onto a stuck freeze-gate.

## Caveats
- VMHdm is predator-specific (innate threat). Pain, malaise, social threat may use parallel architectures.
- Override question (what suppresses VMHdm or its downstream gates under metabolic demand) not addressed here.
