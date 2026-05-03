# Colosio et al. 2017 - Neural Mechanisms of Cognitive Dissonance: An EEG Study

[DOI](https://doi.org/10.1523/JNEUROSCI.3209-16.2017) | PMID 28438968 | J Neurosci, 2017 | According to PubMed.

## What the paper did

Colosio's group recorded EEG during a free-choice paradigm in healthy adults, with the addition of a resting-state baseline. They isolated a frontocentral negative deflection that emerged ~60 ms after the choice response — spatially and temporally similar to the error-related negativity (ERN) seen in performance-monitoring tasks. The amplitude of this evoked response correlated with the magnitude of the subsequent reevaluation of the chosen and rejected items (the spreading-of-alternatives effect).

A second result is more unusual: individual differences in resting-state long-range temporal correlations of frontocentral activity predicted both the size of the dissonance-related evoked response and the size of the behavioural preference shift. People whose resting prefrontal dynamics had stronger long-range correlations showed both stronger evoked dissonance signals at the moment of choice and larger downstream representational shifts.

## Why this matters for the commit-boundary belief lock proposal

The brief proposes that the architecture treats the typed commit boundary as a performance event whose register-time activity sets up the downstream representational rearrangement. Colosio's paper provides a tidy electrophysiological correlate of exactly that: the moment of commit triggers an ERN-like signal whose amplitude predicts how much the agent's value representations will subsequently shift. The frontocentral midline source maps onto the dACC / SMA region that the existing REE control-plane signal map already places at the commit-monitoring locus.

The individual-difference finding is also interesting for the proposal's two-parameter framing. The brief sketched an "attribution-rigidity setpoint" as the dial that distinguishes confabulation territory (too low) from delusion territory (too high). Colosio's resting-state predictor — long-range temporal correlations in frontocentral cortex — is at least a candidate biological marker of where on that dial a given individual sits. This is speculative, but it is the kind of thing that the proposed mechanism predicts should exist if it exists at all.

## Limits and caveats

The signal is locked to the commit, not to a subsequent attempt to revise the just-committed belief under counter-evidence. So the paper does not directly observe the revision-cost asymmetry the brief targets — it observes the upstream commit-monitoring signature whose downstream consequence is the representational shift. The full mechanism the brief proposes (revision is expensive because the belief is now load-bearing for the action record) is one inferential step beyond what Colosio measured.

The ERN attribution is also somewhat by analogy — the canonical ERN is a response-monitoring signal triggered by errors. Whether the dissonance-related deflection here is the same neural process under a different label, or a related-but-distinct signal in the same anatomy, is unsettled. The authors are appropriately cautious.

## Confidence reasoning

Confidence at 0.78. Source quality is good; mapping fidelity is moderate (one inferential step from the measured signal to the brief's hypothesis); transfer risk is modest. This entry supplements Izuma 2010 by adding electrophysiological resolution and an individual-difference predictor that the proposed two-parameter mechanism would expect to exist.

It does not stand on its own as evidence for the brief — it stands as confirmation that the value-update circuitry the brief implicates is (a) engaged at the moment of commit and (b) variable across individuals in a way that predicts behavioural outcome. Both of those properties are necessary if the proposed mechanism is to do real explanatory work.
