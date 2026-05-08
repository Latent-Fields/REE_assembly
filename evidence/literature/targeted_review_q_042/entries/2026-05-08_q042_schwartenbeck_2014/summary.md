# Schwartenbeck, FitzGerald, Mathys, Dolan & Friston 2014 — The Dopaminergic Midbrain Encodes the Expected Certainty about Desired Outcomes

**Source:** Schwartenbeck P, FitzGerald THB, Mathys C, Dolan R, Friston K. *Cerebral Cortex* 25(10):3434-3445 (2014). [DOI](https://doi.org/10.1093/cercor/bhu159). PMID 25056572, PMCID PMC4585497. According to PubMed.

## What the paper did

Working within the active-inference framework, the authors tested whether dopamine's role in choice could be reframed as encoding the *precision* of beliefs about optimal policies -- the agent's confidence that the chosen policy will deliver desired outcomes -- rather than as encoding reward prediction error. They designed a "limited offer" decision-making task where subjects had to decide how long to wait for a high offer before accepting a low one, with the risk of timing out. They fit two competing models to choice behaviour: classical utility maximisation and active-inference surprise minimisation. Active inference fit better. They then tested whether trial-by-trial active-inference estimates of policy precision predicted midbrain BOLD activity. The fit was strong: dopaminergic midbrain BOLD tracked policy precision, and the signal was time-locked to the choice / commit moment rather than to outcome arrival.

## Why it matters for Q-042

This paper provides the strongest active-inference-framed argument for Option B in Q-042. REE's running-variance precision is, conceptually, a confidence-in-the-current-policy quantity: it scales how much weight to give the current best estimate when committing to action. Schwartenbeck et al. show the brain has a quantity at exactly that role -- policy precision in the active-inference sense -- and that quantity is broadcast at choice time by midbrain dopamine, before outcome integration.

The active-inference framing also sharpens what the timing answer should mean. Precision in this framework is a forward-looking quantity: it is the agent's confidence that the current chosen action will work out. It must, structurally, be available BEFORE commit -- otherwise it cannot gate the choice it is supposed to inform. A precision signal that fires only post-outcome is not the same quantity; it is a backward-looking estimate of whether the just-completed action worked out, which has a separate computational role (updating the model). Q-042's tension between Option A and Option B is partly a confusion about which quantity is being updated where; this paper helps clarify that the pre-commit precision (gating the choice) and the post-outcome learning rate (updating the model) are computationally distinct, and biology runs both.

## Mapping to REE

The structural mapping is at the architectural level. The active-inference policy precision is the closest available theoretical match to REE's running-variance precision -- both are scalars that scale how confidently the agent commits to its current best policy. Schwartenbeck et al. give a direct biological substrate (midbrain dopamine projection neurons) and a direct timing answer (broadcast at choice time, before outcome).

For REE: the recommendation that follows from this paper is to ensure ARC-016's precision-related broadcast is live at action selection time, even if the underlying running-variance statistic continues to be updated at outcome time. That is the dual-update variant Q-042's notes section already identifies as the most biologically plausible default. The Schwartenbeck reading argues specifically that the broadcast cannot be skipped at action selection without breaking the role of precision in the choice itself.

## Caveats

Active inference is a specific theoretical framework; alternative interpretations (reward prediction error, value coding, novelty signal) attribute midbrain DA activity to different quantities. The paper does not definitively rule out those alternatives -- it shows that policy precision fits the data well, not that it is the only quantity that fits. The 'limited offer' task is narrow and may emphasise the policy-precision component disproportionately. BOLD is an indirect dopamine proxy. None of these caveats undermine the relevance to Q-042's timing question, but they do mean the substrate identification (DA = policy precision) should be carried as one available reading, not as settled fact.

## Confidence reasoning

0.72 supports for Q-042. Source quality high (0.78, Cerebral Cortex, careful Friston-lab work). Mapping fidelity high (0.75) -- the active-inference policy-precision framing is the closest available theoretical match to REE's running-variance precision. Transfer risk moderate (0.32) -- the active-inference reading of DA is one of several available, and the substrate identification depends on accepting the framework. Direction is supports for Option B (with the active-inference caveat).
