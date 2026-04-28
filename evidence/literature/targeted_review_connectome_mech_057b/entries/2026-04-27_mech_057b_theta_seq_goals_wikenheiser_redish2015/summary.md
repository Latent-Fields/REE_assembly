# Wikenheiser & Redish 2015 -- Hippocampal theta sequences reflect current goals

According to PubMed: [10.1038/nn.3909](https://doi.org/10.1038/nn.3909) (PMID 25559082).

## What the paper did

Wikenheiser and Redish recorded CA1 ensembles in rats performing a value-guided decision task and decoded theta-cycle-bounded sequences trial by trial. The key analysis was whether the distance the sequence projected ahead of the animal's current location -- the "look-ahead" -- varied with the rat's active goal. They examined journeys to distant versus proximal goals and the moment of goal arrival.

## Key findings relevant to MECH-057b

Look-ahead extent was not fixed. On journeys to distant goals it extended further; on journeys to proximal goals it stayed shorter; and on arrival at the goal it contracted. The on-arrival contraction is the piece that matters most for MECH-057b: when the goal is reached, the candidate-generation machinery stops extending forward, consistent with a completion-detection event short-circuiting further candidacy. Combined with Pfeiffer and Foster's finding that pre-run sequences are biased toward goal-reaching trajectories, this gives a coherent picture: trajectory candidates are sized to the gap between current state and goal, and the candidacy machinery itself responds to completion of the goal as a state change.

## Mapping to REE

In REE this maps onto the candidacy-gate framing of MECH-057b: trajectories that complete the current task (reach the goal) are the ones promoted; once completion is detected, the gate stops emitting forward-extending candidates. The observed look-ahead modulation is the behavioural signature of this gating logic operating in real time, on a theta-cycle timescale.

## Limitations and caveats

The paper measures the distribution of look-ahead extents, not the candidacy gate directly. Look-ahead modulation is consistent with several plausible architectures: a candidacy gate, a value-modulated trajectory generator without candidacy, or a downstream pruning mechanism. Distinguishing these requires the kind of internal-suppression instrumentation V3's HippocampalModule will eventually support. The on-arrival contraction is the strongest single observation, but it has alternative explanations (e.g. resource depletion at goal sites).

## Confidence reasoning

I score this 0.74. Strong source quality (Nature Neuroscience, well-designed task). Mapping fidelity is moderate because look-ahead modulation is consistent with several gating architectures, not uniquely with the MECH-057b completion-verification framing. Together with Pfeiffer & Foster (2013) it provides convergent but still indirect support.
