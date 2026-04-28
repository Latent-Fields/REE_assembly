# Pfeiffer & Foster 2013 -- Hippocampal place-cell sequences depict future paths to remembered goals

According to PubMed: [10.1038/nature12112](https://doi.org/10.1038/nature12112) (PMID 23594744).

## What the paper did

Pfeiffer and Foster recorded large CA1 ensembles in rats freely navigating an open arena to multiple known goal locations. Before the rat began each goal-directed traversal, they extracted brief hippocampal sequence events from the pause-and-plan epochs and decoded the spatial trajectory those sequences represented. They then asked whether the decoded trajectories were biased toward the rat's current location at one end and the remembered goal location at the other -- and whether the bias predicted the path the rat actually took. The control that matters most here is the novel start/goal pair manipulation: even when a particular start-goal combination had never been performed before, sequences still tended to bridge from current location to that goal.

## Key findings relevant to MECH-057b

The hippocampus does not emit a random sample of remembered trajectories. It emits trajectories that can be completed: that start at the animal's current state and reach a stored goal. This is exactly the structure MECH-057b posits -- a candidacy gate that promotes only those trajectories that survive an internal completion check, before any downstream evaluator (E3, BG, prefrontal cortex) sees them. The novel start/goal control matters because it shows the bias is not merely cached behaviour: the hippocampus can stitch a goal-reaching sequence that has never been executed, provided both endpoints are individually known.

## Mapping to REE

In REE the candidacy gate sits inside the hippocampal substrate (HippocampalModule in V3), and its job is to suppress trajectory proposals that do not complete -- that fail to reach a goal, fail to terminate cleanly, or break midstream. Pfeiffer and Foster's data fit the output signature of such a gate: what we observe reaching the recording electrodes is heavily skewed toward complete, goal-reaching sequences. The REE prediction the paper does not directly test is that incomplete or non-goal-reaching sequences exist in the substrate but are blocked from propagation. That requires direct trajectory-emission instrumentation of the kind only V3 will support.

## Limitations and caveats

The paper measures what reaches the recording electrodes. It does not measure what was generated and discarded. The candidacy-gate framing is therefore inferred rather than directly demonstrated. The goal locations were rewarded and remembered, not internally generated -- so this paper speaks to externally-anchored goal pursuit, not to the harder case of an agent inventing a novel goal during planning. The mapping from rat open-field navigation to REE's general candidacy machinery has a transfer cost that should be acknowledged when this entry is cited.

## Confidence reasoning

I score this 0.82. Source quality is very high (Nature, careful electrophysiology, well-controlled novel pair manipulation). Mapping fidelity is good but not perfect because the gate itself is inferred from output statistics. Transfer risk is moderate. This is the canonical reference for hippocampal trajectory candidacy and is already cited in MECH-057b's literature_evidence in claims.yaml; I am formalizing it as a record entry because no record.json previously existed in this directory.
