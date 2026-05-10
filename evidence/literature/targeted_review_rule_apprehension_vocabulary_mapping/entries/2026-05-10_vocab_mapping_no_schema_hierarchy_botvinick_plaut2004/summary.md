# Botvinick & Plaut 2004 -- The deliberate counter-current: doing without schema hierarchies

## What the paper did

Botvinick and Plaut deliberately built the strongest counter-argument to schema-hierarchy accounts of routine action. They trained a *single recurrent connectionist network* mapping environmental inputs to actions on the same coffee-preparation and lunch-packing tasks the Cooper-Shallice schema model handled. The single recurrent network learned to encode task context in distributed recurrent state and reproduced behaviour qualitatively equivalent to the schema-hierarchy model -- *including* the characteristic action-disorganisation-syndrome lesion patterns when the representational substrate was degraded. Their conclusion: explicit schema hierarchies are not required to explain the data; recurrent processing over distributed state representations is sufficient.

## Key findings relevant to the rule-apprehension vocabulary question

This is the deliberate counter-current paper for Pull 4, and it bears on the user's reframing of the original Pull 4 scope. The original framing -- "falsify the rule-apprehension framing entirely by showing option-policies suffice" -- was rejected, but Botvinick-Plaut 2004 is the closest existing-literature *partial* version of that argument. Their claim is not "options suffice" (they pre-date much of the options-discovery literature); their claim is "recurrent connectionist dynamics over distributed state representations suffice -- you do not need an explicit schema hierarchy at all".

For REE's ARC-062 + ARC-064 + MECH-318 cluster, this is a meaningful weakener:

- *Counter-claim 1*: ARC-062's gated_policy + discriminator may be unnecessary; a recurrent policy over distributed latent state may produce equivalent behaviour. The "rule application" appearance is emergent from recurrent dynamics rather than a property of an explicit gating substrate.
- *Counter-claim 2*: MECH-318's rule-state-abstraction substrate may be unnecessary; distributed recurrent state already encodes context. There is no need for a separate OFC-cognitive-map-analog.
- *Counter-claim 3*: ARC-064's explicit bottom-up rule discovery may be unnecessary; learning the recurrent policy *is* learning the rules, with no separate extraction step.

## How the findings translate to REE

The 2004 result limits to the *routine-sequential-action* regime, where schema-hierarchy and recurrent-connectionist accounts are observationally equivalent. For the regimes REE actually cares about -- cross-task generalisation, novel-context rule application, long-horizon planning, sleep-mediated consolidation -- the equivalence has not been demonstrated. Subsequent options/HRL literature has continued to assume explicit hierarchical decomposition, with empirical support from Solway 2014 (humans spontaneously discover near-optimal hierarchies, hard to explain on a pure-recurrent account) and the OFC-cognitive-map literature (Wilson 2014, Schuck 2016, Niv 2019; explicit task-state representations are decoded from OFC).

The constructive use of this paper for REE: it is the canonical *minimum-architecture baseline* against which the explicit-cluster claim should be defended. If REE's V3 substrate produces equivalent rule-apprehension behaviour using only recurrent latent-stack dynamics (no MECH-318 substrate), then MECH-318 is a redundant claim and Pull 2's R2 verdict is wrong. This is a falsifiable empirical comparison REE could run -- and the V3-EXQ-543 / 543b experiments are partway there.

## Limitations and caveats

The Botvinick-Plaut 2004 model is empirically demonstrated on relatively short routine-action tasks. The recurrent-distributed-state account is known to be harder to scale to long horizons and to cases where rules must transfer to genuinely novel contexts -- which is exactly where the explicit-hierarchy account predicts payoff (Solway 2014's bottleneck-state result, Bacon 2017's option-discovery transfer experiments).

The paper is also 22 years old; both the connectionist and HRL traditions have moved on. Adopting the 2004 result as the baseline-to-beat is reasonable but should be paired with newer comparisons (e.g. transformer-based recurrent policies vs option-critic, which is a live debate in the ML literature).

## Confidence reasoning

Scored 0.74, weakens-direction. Source quality high (Psych Review, well-cited). Mapping_fidelity moderate-high (0.72) because the architectural challenge is real but limited to the routine-action regime. Transfer_risk moderate-high (0.45) because the model has not been replicated for the long-horizon / cross-task regimes REE cares about. The weakens-direction is calibrated -- this paper does *not* refute the explicit-cluster account, but it does establish that the cluster needs to defend its load-bearing claims against the recurrent-distributed-state baseline. The paper feeds Pull 4 R3 (genuine REE divergences) by sharpening the question: which parts of REE's rule-apprehension cluster are load-bearing beyond what recurrent dynamics on the existing latent stack can produce? Those are the parts to KEEP-AS-IS; the parts that *aren't* load-bearing beyond the recurrent baseline are candidates for absorption.
