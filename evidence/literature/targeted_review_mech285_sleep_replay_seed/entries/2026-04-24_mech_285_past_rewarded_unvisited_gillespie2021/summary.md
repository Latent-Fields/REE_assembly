# Gillespie et al. 2021 -- replay is enriched for past-rewarded and not-recently-visited places

## What the paper did

Rats performed a dynamic spatial memory task in which the rewarded goal could change across blocks, requiring the animal to update its map of where reward was available. CA1 activity was recorded, and state-space methods were used to decode replay events with fine spatial resolution. The experimenters asked a very pointed question: is awake replay content a preview of the animal's imminent choice (a planning sampler), or something else?

## Key findings relevant to MECH-285

Replay content was decoupled from subsequent choice. The animals did not appear to replay their upcoming trajectory; replay was selectively *enriched* for two other things: previously rewarded locations (including locations that were no longer the current goal) and places the animal had not recently visited. The upshot is that the seed pool is broad (spans locations beyond the active trajectory), and the weighting over that pool does not track current decision need. Instead, it tracks a composite of past-reward-history and something that looks very much like a time-since-visited signal.

## Translation to REE

MECH-285 is a bet that the sleep-replay seed distribution is biased by accumulated epistemic staleness (MECH-284 residuals) and that this bias is dissociable from dopaminergic salience-only accounts. Gillespie et al. provide the cleanest available behavioural-neural match to that bet. The two enrichments they find map directly onto two of MECH-285's central architectural features: past-reward enrichment corresponds to the salience/dopaminergic arm (MECH-074b lineage), and *not-recently-visited* enrichment corresponds to the staleness arm. That both are present simultaneously, and that the staleness-like enrichment is specifically inverted from recency (places not-recently-visited, not places most-recently-visited), is a near-direct validation of the broad-coverage-with-staleness-priority reading.

The decoupling from imminent choice is also load-bearing. MECH-285 posits that during the sleep regime the computational task changes from "make a decision" to "revise the schema" -- full-Bayesian schema-revision work. An awake-replay pattern that does not preview upcoming choice but instead sweeps past-relevant-and-stale content is exactly what the sleep-regime architecture predicts should happen when the decision-sampling role is suppressed.

The one caveat worth taking seriously: this is awake replay, not sleep replay. The extension rests on the content-overlap argument (Joo & Frank 2018, Karlsson & Frank 2009) -- awake and sleep SWR content share substantial structure, and the findings here are best read as consistent with but not identical to a direct sleep-replay test.

## Limitations and caveats

Visit-recency is a proxy for staleness; they are related but not identical variables. A place the animal has not visited recently may be stale because it has not been tested against reality lately, but recency and staleness can dissociate (a place visited recently in a stable environment carries low staleness; a place not visited in a highly volatile environment carries extreme staleness). The task does not manipulate these independently. The study also cannot directly test MECH-285's salience-dissociation claim -- past reward is confounded with salience-tagging.

## Confidence reasoning

Source quality is high -- state-space decoding, large N, top lab. Mapping fidelity is high because the paper's central findings come very close to direct test of the MECH-285 architecture. Transfer risk is moderate but not large -- the main risk is the awake-to-sleep extension. Aggregate confidence 0.82.
