# Mattar & Daw (2018) — Prioritized memory access explains planning and hippocampal replay

**Source:** Nature Neuroscience, 21(11):1609-1617. DOI: [10.1038/s41593-018-0232-z](https://doi.org/10.1038/s41593-018-0232-z)
**PubMed:** PMID 30349103

## What the paper did

Mattar and Daw developed a normative computational theory of hippocampal replay: which memories should be accessed at each moment to optimise future decisions? They formalise this as prioritisation by utility -- the expected gain in future reward from accessing and updating each memory. This balances two competing pressures: the need to evaluate imminent choices (replay of states near the current decision point) against the gain from backward propagation of newly encountered value information (replay of states leading to recently updated states). The theory is tested against a large body of empirical replay findings -- forward vs reverse replay, replay at reward sites, sleep replay -- and accounts for a striking range of phenomena within a single framework.

## Key findings

The central prediction is that replay order is not random but reflects a gradient of utility across state space. States with high utility (those where better choices would most improve expected future reward) are replayed preferentially. The paper shows that this explains why replay is often observed at reward sites (high new-information gain), why forward replay precedes decisions (evaluating imminent choice) and reverse replay follows them (backward propagation), and why sleep replay tends to emphasise recently important states. The authors also propose that dysfunction of this prioritisation mechanism -- pathological replay of aversive or craving-relevant states -- is a candidate mechanism for rumination and craving.

## REE translation -- ARC-018

This paper provides the most compelling computational argument for why the hippocampal viability map in ARC-018 should be error-driven. ARC-018 claims that the viability map is updated by E3 harm/goal error. Mattar & Daw's utility metric is the normative answer to what that error signal should optimise: replay a state when updating its value estimate will most improve future decisions. In REE terms, this is precisely what E3 harm/goal error computes -- the discrepancy between expected and observed harm/goal outcomes, propagated back to the states that led there. The agreement is not coincidental; it reflects that both frameworks are asking the same normative question (what should guide value-map updates?) and arriving at the same answer (utility gradient / error-driven prioritisation).

The paper's rumination/craving note is also relevant for ARC-018. If the prioritisation mechanism preferentially replays harm-adjacent states (because those have high unsigned error), the viability map will develop concentrated harm representations around dangerous action sequences -- which is exactly the threat-field structure ARC-018 predicts the hippocampal map should acquire.

Where the corrected V3 framing finds support: the error-driven update logic is well-grounded here, and the forward/backward asymmetry in replay (pre-decision vs post-outcome) is consistent with ARC-018's dual-mode viability map (consultation before action, update after outcome). Where it is agnostic: the model uses spatial location as the state representation. Whether action-object coordinates would function as an equivalent state space is not addressed. The model also treats harm as negative reward, which is a simplification -- ARC-018 gives harm a separate signal pathway (E3).

## Limitations and caveats

This is a computational model, not a direct recording study. Its predictions are tested against existing datasets but not with new experiments designed to dissociate the utility prioritisation account from alternatives. The utility metric is defined only for reward, not harm; whether aversive signals generate the same kind of prioritised replay is assumed but not demonstrated. The claim about rumination and craving is speculative and not empirically tested in this paper.

## Confidence reasoning

Strong theoretical alignment with ARC-018's error-driven update mechanism. The normative framework is compelling and the empirical validation against known replay phenomena is broad. Confidence is held at 0.80 because this is a model paper (not electrophysiology), and because the harm-as-negative-reward simplification is a genuine gap for the ARC-018 mapping.
