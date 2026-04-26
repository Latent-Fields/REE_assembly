# Wikenheiser & Redish 2015 -- Hippocampal theta sequences reflect current goals

## What the paper did

Wikenheiser and Redish recorded CA1 place cells from rats performing a value-guided decision-making task and analysed the structure of theta-cycle place-cell sequences as a function of the rat's current goal. The headline finding: theta sequences project ahead of the rat's current location, and the *distance* projected (look-ahead) scales with the distance to the goal. Look-ahead extends farther on journeys to distant goals than to proximal goals, is predictive of the animal's destination, and equalises across journeys at the moment of goal arrival.

## Key findings relevant to MECH-294

This paper supplies direct rodent unit-level evidence that one of MECH-294's four content streams -- goal_latent -- is theta-locked and theta-cycle-resolved. The look-ahead-scales-with-goal-distance result is particularly important: it shows that theta sequences are not just clock signals, they carry task-relevant content shaped by the agent's current intentions. That is exactly the substrate property MECH-294 needs.

## How the findings translate to REE

MECH-294 takes Wikenheiser & Redish as direct evidence for the goal-latent stream of its four-stream packet. By analogy, the theta-cycle-resolved goal content is what MECH-294 expects E3 (or its biology analogue, the BG-PFC-hippocampus loop) to read on each cycle. The next architectural question -- whether the goal stream can be co-read with action_proposal, risk_estimate, and state_summary in the same phase-aligned window -- is not addressed by this paper.

## Limitations and caveats

Three caveats. First, single-stream theta-locking is necessary but not sufficient for MECH-294's joint-binding claim. Second, the streams in MECH-294 include action and risk content sourced from BG and amygdala/ACC, not place-cell content from CA1; whether those streams are theta-locked at all is an open question. Third, the look-ahead-modulation result is a content-modulation effect on a single stream type, not a binding-window effect across stream types.

## Confidence reasoning

Confidence 0.74. Source quality high (Nature Neuroscience, direct rodent recording, established analysis). Mapping fidelity moderate-high because goal_latent theta-locking is directly demonstrated for one of MECH-294's four streams. Transfer risk modest -- the result is single-stream and the joint-binding extension is not tested. Tag: (b) individual content theta-locked but joint binding not shown.
