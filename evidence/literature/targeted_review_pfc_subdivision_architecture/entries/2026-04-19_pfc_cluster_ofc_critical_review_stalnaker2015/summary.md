# Stalnaker, Cooch & Schoenbaum 2015 — What the Orbitofrontal Cortex Does Not Do

## What the paper does

This Nature Neuroscience review is a deliberate counterweight to the simpler "OFC encodes value" framing that dominated the preceding two decades. Schoenbaum's lab has accumulated rodent and primate data showing that OFC neurons discriminate between states that differ only in their latent task-structural role — same sensory inputs, same rewards, different position in the overall task structure — and argue from this that OFC represents a "cognitive map" of task structure rather than value per se. Value signals do appear in OFC, but the authors argue that these ride on top of a more fundamental structural representation. The paper explicitly lists functions that OFC does *not* do (direct value computation, action selection, reward learning per se) to sharpen the positive claim.

## Key findings relevant to the PFC cluster

The cognitive-map framing is important for REE because it aligns OFC-analog function with REE's model-based architecture. If OFC represents task structure — what state the agent is in, what transitions are available, what outcomes each state predicts — then the OFC-analog is where REE's learned world-model lives at the decision-relevant level. This is not the same as E2 (which is the fast-predictive forward model on z_gamma) or E1 (which is the slow LSTM-backed deep predictor). It is the abstracted, decision-relevant state-space representation that E2 and E3 consult when choosing actions.

Two specific implications:

1. **OFC-analog is model-based, not model-free.** Value-tracking happens elsewhere (vmPFC-analog). The OFC-analog carries the structure of "where am I in the task" such that value tracking *can* be computed downstream.

2. **This framing makes OFC-analog updates a natural consolidation target.** If the OFC-analog is the task-structure representation, then Frankland & Bontempi-style systems consolidation is the process that slowly builds that representation from repeated hippocampal-cortical dialogue during offline phases. This ties directly into the systems-consolidation lit-pull I ran yesterday and into MECH-261's offline_consolidation mode.

## How this translates into REE

The Stalnaker framing and the Rudebeck & Murray framing agree on the core claim — OFC is not just scalar value — but diverge on the precise content. Stalnaker says "cognitive map of task structure." Rudebeck & Murray say "oracle for specific expected outcomes." REE can take these as complementary: the OFC-analog holds a structured representation of the state space and the outcomes associated with each state, such that queries of the form "if I were in state s and took action a, what outcome would I expect?" can be answered. This matches what E2 is doing computationally in REE but gives it a proper neural-substrate address.

## Limitations and caveats

The cognitive-map framing is compatible with but not identical to the reinforcement-learning "model-based state representation" framing used in computational neuroscience. Different authors in the OFC literature use "state" and "outcome" differently; REE should not import one framing wholesale. Also, the dissociation between OFC's role and adjacent structures (lateral PFC, agranular insular cortex, perirhinal cortex) is not fully settled — some findings attributed to OFC may belong to adjacent structures once finer-grained lesion methods are used. REE should treat the OFC-analog claim as "there is a substrate here that represents structured task-model information, biologically in or adjacent to OFC" rather than "OFC exactly."

## Confidence reasoning

Source quality high (Nature Neuroscience, careful synthesis). Mapping fidelity moderate-strong because the cognitive-map framing aligns well with REE's architecture but the theoretical framing is contested. Transfer risk moderate: the claim that OFC represents structured task-model information is robust; the exact computational interpretation varies. Net confidence: 0.80.
