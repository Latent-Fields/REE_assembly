# Learning, memory and consolidation in hierarchically organised cortico-basal ganglia systems

**Rusu & Pennartz (2019), Hippocampus, DOI: 10.1002/hipo.23167**

## What the paper did

Rusu and Pennartz offer a synthesis of how the brain coordinates hierarchically organised behavior -- low-level habitual routines nested inside larger sequences of planned, goal-directed action. They review evidence from the prefrontal cortex, hippocampus, striatum, and dopaminergic mesencephalon to propose a three-level cortico-BG loop architecture: (1) a limbic-affective loop (orbitomedial PFC + ventral striatum) that codes the goal landscape and sets action context; (2) a dorsomedial PFC-striatal loop that selects actions within that context; and (3) a sensorimotor-dorsolateral striatal loop that executes sequences. The hippocampus and its SWR-associated replay are given a central role in consolidating world-state representations and goal context into this frontal hierarchy.

## Key findings relevant to the claim

The central claim that bears on MECH-112 is the proposal that the orbitomedial PFC encodes a goal landscape -- a representation of the task space of behaviorally relevant variables -- rather than merely outcome values. This is a persistent, context-setting representation that is distinct from moment-to-moment reward prediction error. The limbic-affective loop is not just a valuation system that fires at outcomes; it maintains a structural model of what the agent is oriented toward. Second, the paper proposes that hippocampal SWR replay consolidates goal-context representations into the frontal corticothalamic circuit -- replay is not purely spatial but also goal-shaped, transferring information about valued states into the system that coordinates multi-step action.

## Translation to REE (the mapping)

MECH-112 requires that E3 maintain a structured latent goal representation (z_goal positive attractor) separate from harm avoidance. Rusu and Pennartz provide precisely the biological architecture that MECH-112 is abstracting: the limbic-affective loop is the seat of z_goal, encoding what the agent is trying to achieve and within what context. This is why REE needs z_goal to be a persistent, landscape-level representation rather than a scalar reward signal -- the biological original is a goal-landscape coder, not a reward counter. The three-loop hierarchy also directly supports the ARC-030 architecture: the limbic-affective loop (goal attractor, z_goal) must co-exist and jointly act with the nociceptive stream (SD-010, harm avoidance) as dual inputs to the action-selection loop. The SWR replay mechanism maps to the hippocampal terrain consolidation in REE -- goal attractors in the residue field are not just specified online but consolidated during quiescent replay into stable terrain that persists across training episodes.

## Limitations and caveats

This is a review paper, and not all of its claims have equally strong primary evidence. The goal-landscape coding attributed to orbitomedial PFC is proposed based on multiple indirect lines of evidence rather than a single definitive experiment. The case for goal-shaped (as opposed to purely spatial) SWR replay remains contested in the broader literature. The paper conflates some distinctions that matter for REE -- for example, model-based learning and goal-directed behavior are treated as overlapping but not identical, and the hippocampus is described as supporting model-based learning without being required for all goal-directed behavior. REE's V3 design does not yet fully implement the three-loop hierarchy; the current substrate approximates elements of loops 2 and 3 but lacks the full limbic-affective loop as a distinct circuit.

## Confidence reasoning

This is an authoritative synthesis from the Pennartz lab, which has contributed primary electrophysiology data on OFC reward coding and striatal function. The mapping fidelity to MECH-112 is very strong: the three-loop architecture is precisely the biological substrate that MECH-112 is designed to implement. Transfer risk is low because the claim is at the architectural level rather than the mechanistic implementation level. Overall confidence: 0.83.
