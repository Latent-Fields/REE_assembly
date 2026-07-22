# Ni, Sun & Li (2023) -- The shadowing effect of initial expectation on learning asymmetry

## What the paper did

The authors asked whether the widely reported asymmetry between learning rates for positive and negative prediction errors is a real property of the learner or partly an artefact of model specification. Across two reinforcement-learning experiments spanning stable and volatile reinforcement probabilities, and gain, loss and mixed environments, they compared models that fit an asymmetry alone against models that also fit the value expectation the participant brought into the task. They backed this with parameter recovery simulations.

## Key findings relevant to SD-076

Models including both the asymmetric rates and an initial value expectation consistently won, and -- this is the part that matters for us -- the apparent *direction* of the asymmetry can flip depending on what the initial expectation is assumed to be. Because prediction errors are computed relative to a running value, where that value starts biases which errors are positive and which are negative for a long stretch of learning, and an asymmetry parameter fitted without accounting for it absorbs the difference. The authors are explicit that no consensus exists on the direction of learning asymmetry in elementary reinforcement learning, in contrast to the high-level belief-updating literature where the optimistic direction is better established.

## How this translates to REE

I have filed this as *weakens*, and I want to be careful about what exactly it weakens. It does not show that SD-076's posited asymmetry is absent. It shows that the parameter is harder to measure than it looks, and it removes a support SD-076 might otherwise have leaned on -- one cannot cite the reinforcement-learning literature as settled evidence for a downward drift, because that literature is not settled.

The concrete consequence is for validation design. SD-076 is implemented as an EMA over the agent's own prediction error, and every EMA has an initialisation. This paper says initialisation and asymmetry are partially non-identifiable, which means the MECH-204 Phase 7 retest has a confound available to it: an arm that inadvertently changes where the running-variance estimate starts will produce a drift signature that looks like a precision-inflation effect. The retest must hold the rv initialisation fixed and identical across arms and say so in the manifest, or fit it explicitly as a nuisance parameter.

There is a mitigating asymmetry in REE's favour that I should state plainly rather than let the caveat run further than it should. The identifiability problem is severe when fitting human choice data because the initial expectation is unobserved and must be inferred. In REE the initialisation is a line of code. We can hold it fixed, vary it deliberately, and measure the interaction. So this is a design warning we can fully discharge, not a standing threat to the claim.

## Limitations and confidence

The experiments are first-order reward learning, not second-order precision estimation, so the confound's magnitude in REE's setting is unmeasured. Confidence 0.7 -- the methodological point is well made and well supported by recovery analysis, and it is directly actionable for SD-076's validation, but its force is procedural rather than evidential.

*Retrieved via PubMed. [DOI](https://doi.org/10.1371/journal.pcbi.1010751)*
