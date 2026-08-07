# Pupillo et al. 2023 -- the magnitude-to-retention rule changes sign, so one cut cannot express it

**Claim tested:** Q-090 -- is the retained-alternative admission criterion the interrupt's scale at a lower cut, or an independent relevance criterion?

**Direction:** weakens the same-cut-scale horn. **Confidence: 0.58.** This is the pull's primary disconfirming source.

## What the paper does

Participants learn associations between contexts and object categories, with the associations deliberately built at different strengths, and make predictions whose outcomes they see. A reinforcement-learning model then supplies subject-specific, trial-by-trial prediction-error estimates at encoding, which are related to performance on a later recognition test. The move that makes the paper useful is that they do not treat prediction error as a single lever. They split by whether the participant's prediction was actually correct.

The result is a crossover. When predictions were correct, a stronger prediction error -- arising from weak prior expectations -- *enhanced* memory. When predictions were incorrect, a stronger prediction error -- arising this time from strong prior expectations -- *impaired* it. Same magnitude construct, opposite consequences, with the direction set by a second variable.

## Why it bears on Q-090

The same-scale horn is a specific architectural proposal, and this result contradicts it structurally rather than empirically. The horn says: one predicted-harm magnitude, two thresholds, interrupt high and retain low. Any such rule is monotone in magnitude -- larger magnitude, weakly more likely to be retained. That is simply what a threshold on a scalar does.

A sign flip cannot be produced by any threshold on any single scale, at any cut-point. If the biological retention rule really changes direction as a function of a second term, then no choice of low cut-point on the leg-1 magnitude reproduces it. The criterion takes at least two arguments.

I find this the most informative finding in the pull, because it does something better than picking a side: it suggests Q-090's disjunction may be false as posed. The question offers "same scale, lower cut" or "independent goal-match criterion", and this paper says the answer is likely neither -- it is a magnitude term *gated by* something else. The productive next question is not which horn wins but what the second argument is.

## Caveats and where the mapping strains

The most important caveat is one that cuts against over-reading this entry in the other direction. The second argument Pupillo et al. identify is whether the agent's own prediction proved correct. That is not goal-match. If anything it is a cousin of MECH-485's own `epistemic_deficit` confidence term -- which is interesting, since MECH-485 already posits confidence as the variable that routes between interrupt and orient/survey. There is a tidy reading in which confidence gates all three legs rather than only the first two, and this paper is a hint toward it. But a hint is what it is. Nobody should record this as support for the goal-match horn; it eliminates one candidate and nominates a third.

The retained items are, once again, experienced object images rather than computed-and-discarded alternatives. The gap flagged in the Kalbe entry applies here unchanged: MECH-485 leg 3 retains a branch of a forward rollout, which has no perceptual existence at all, and no source in this pull bridges that gap.

And the load-bearing finding is an interaction, in a single study, with a modest sample. Interactions are the effect class least likely to replicate. The entire disconfirming force of this entry rests on the crossover being real, and I would want it replicated before treating the same-scale horn as closed rather than as doubtful. One housekeeping oddity worth passing to a governance reader: PubMed tags this record as "Journal Article, Review" while the abstract plainly describes a primary experiment. I have classed it as `behavioral_human` on the reported design, but the tag should be checked before anyone leans on it hard.

## Confidence reasoning

Source quality 0.7 -- computationally explicit, model-derived trial-wise prediction errors rather than a crude proxy, published in a reasonable venue, but single-study, modest-sample, interaction-dependent, with an ambiguous article-type tag. Mapping fidelity 0.6, the highest in this pull, because the paper is directly about what governs admission to retention as a function of a magnitude signal -- Q-090's actual subject matter -- and because the claim being transferred is structural (a scalar threshold cannot express a sign flip) rather than a parameter that would need to survive the species and domain jump. Transfer risk 0.45, moderated by that same structural character. The aggregate of 0.58 reflects a result that is architecturally decisive if true and empirically fragile as yet.
