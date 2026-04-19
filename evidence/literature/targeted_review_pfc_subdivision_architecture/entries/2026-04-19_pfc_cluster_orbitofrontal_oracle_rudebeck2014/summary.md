# Rudebeck & Murray 2014 — The Orbitofrontal Oracle

## What the paper does

This Neuron review is the clearest published argument for dissociating OFC from vmPFC on functional grounds. The Murray lab has spent years refining the fiber-sparing excitotoxic lesion method in macaques precisely to resolve the long-standing confusion between OFC and vmPFC contributions to value-based behaviour. Older aspiration-lesion work that appeared to implicate "ventral PFC" in reward processing was actually cutting fibres of passage to amygdala and other structures. Once the fibres are spared, a clean dissociation emerges: OFC lesions impair prediction of specific expected outcomes (reward devaluation, outcome-specific Pavlovian-instrumental transfer, stimulus-outcome learning), while vmPFC lesions impair value integration and subjective choice but leave specific-outcome prediction intact.

## Key findings relevant to the PFC cluster

The review's central claim — that OFC is the "oracle" for specific-outcome prediction — has two direct consequences for REE:

1. **REE has been lumping OFC under vmPFC.** The audit I did before this lit pull confirmed that existing claims reference vmPFC for "value" functions without distinguishing the specific-outcome-prediction function from the subjective-valuation function. This is the same kind of premature lumping that produced SD-010 → SD-011 splits on the nociceptive side, and the same kind of lumping that produced SD-003 before the SD-010/011 split. The fix is to register an OFC-analog claim distinct from the vmPFC-analog (ARC-035, MECH-151/152).

2. **The OFC-analog is the natural home for E2 harm predictions in REE.** E2 is already a specific-outcome prediction model. Mapping E2's output onto an OFC-analog substrate (rather than onto the generic vmPFC-analog) aligns REE's architecture with the primate neurobiology. This also gives MECH-261 a natural target: during internal_planning, writes into the OFC-analog are speculative (counterfactual outcome predictions); during internal_replay, writes are suppressed; during offline_consolidation, slow updates from accumulated real-outcome experience consolidate the predictive model.

## How this translates into REE

Concrete proposals:

- Register an OFC-analog SD (or cluster member) distinct from the vmPFC value substrate.
- Map E2 harm predictions onto the OFC-analog substrate (not the vmPFC substrate).
- Distinguish "value integration" (vmPFC-analog, already covered) from "specific-outcome prediction" (OFC-analog, currently missing).
- Add MECH-261 write-gating rules for the OFC-analog: permit updates during internal_planning and offline_consolidation; suppress during internal_replay.

## Limitations and caveats

The strongest evidence comes from primate selective-lesion studies. Rodent OFC and primate OFC do not cleanly align: rodent medial OFC is often functionally closer to primate vmPFC, and rodent lateral OFC may be closer to primate OFC. REE should treat the primate and human data as primary and be cautious about importing rodent-specific findings without considering the cross-species mapping. The review also acknowledges that the OFC / vmPFC boundary is gradient-like rather than a sharp border, so REE's implementation should probably treat them as adjacent substrates with overlapping but distinguishable functions, not as two hermetically sealed modules.

## Confidence reasoning

Source quality high (Neuron, Murray lab, careful methodology). Mapping fidelity strong — the dissociation fills an identified gap in REE's claim graph. Transfer risk moderate, mostly around the rodent/primate mapping. Net confidence: 0.83.
