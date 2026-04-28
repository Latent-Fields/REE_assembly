# Stalnaker, Raheja & Schoenbaum (2021) -- OFC State Representations and Choice Adaptation

## What the paper did

Six rats were trained on an odour-guided choice task structured as five trial blocks. Each block defined a distinct set of action-outcome contingencies -- a "state" in the formal sense -- and transitions between blocks were unsignaled, so the animal had to infer the current state from the pattern of recent outcomes. Single-unit ensembles in rat OFC were recorded across many sessions and analysed with population decoding algorithms to ask three questions in sequence: (i) do OFC neurons represent which state the animal is in, independent of the immediate odour cue and reward delivery; (ii) does the rate at which OFC integrates evidence for a new state predict how quickly the animal's choices adapt; and (iii) does the quality of OFC's outcome predictions depend on the accuracy of its underlying state representation?

## Key findings relevant to MECH-263

The vast majority of OFC neurons contributed to state representation, and this was true even at the single-unit level -- not just as a population code. State coding was robust to local sensory and reward variation, suggesting it indexes the abstract task position rather than the current observation. At state transitions, OFC ensembles gradually integrated evidence for the new state, and the rate of this integration in the prechoice period predicted how rapidly the rat's behaviour adapted to the new contingencies. Crucially, OFC outcome predictions -- the canonical "value/reward expectation" signal that the OFC literature has historically emphasised -- were dependent on the accuracy of the underlying state representation. When the state representation was wrong, the outcome prediction was wrong.

## How this maps to REE

MECH-263 asserts that SD-033b carries two co-present representations: (i) a structured cognitive map of task state space, and (ii) specific-outcome predictions that are resolved against that map. The Stalnaker 2021 finding is exactly the layered architecture this claim specifies -- state-coding is primary, outcome-coding is conditioned on it. The result rules out the alternative reading in which OFC simply caches outcome expectations independent of any structured task model. For ree-v3, this gives the E2 module a clean architectural story: the latent representation that supports specific-outcome queries (E2's harm-prediction behaviour, rule-conditioned generalisation) needs to encode task-state structure first; outcome predictions ride on that structure rather than replacing it.

## Limitations and caveats

The result is from rat OFC, n=6, in a single odour-block task with five discrete states. REE's task-state space is potentially much larger and more abstract than five blocks of action-outcome contingencies, so the transfer from this paper's quantitative findings (rate-of-integration, decoding accuracy) to REE's substrate is not direct. The species transfer is the usual rodent-to-primate-to-REE chain. The behavioural-adaptation correlation is a between-subject finding over 6 animals and would benefit from cross-lab replication.

## Confidence reasoning

I have set this at 0.85. Source quality is high (J Neurosci, Schoenbaum lab is the canonical proponent of the cognitive-map view, methods are clean), mapping fidelity is high (the paper tests exactly the layered relationship MECH-263 asserts), and transfer risk is moderate (rat substrate to REE). The reason it is not higher is the small n and the narrow task range; the reason it is not lower is that this is a directly mechanistic test of the claim's core architecture rather than a correlational finding.

## Citation

According to PubMed, DOI: [10.1523/JNEUROSCI.0753-20.2020](https://doi.org/10.1523/JNEUROSCI.0753-20.2020). PMID 33446521.
