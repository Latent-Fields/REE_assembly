# Habits as hierarchically organised action sequences (Dezfouli & Balleine 2013)

**Claim tested:** MECH-323 (policy_composition_chunk_accumulator)
**Direction:** supports · **Confidence:** 0.78

## What the paper does

The standard story about instrumental behaviour has two controllers: a model-based, goal-directed system that is sensitive to outcome value and contingency, and a model-free habit system that caches action values and is not. On that *flat* account, some external arbitrator decides which controller drives behaviour on a given trial.

Dezfouli and Balleine put a rival *hierarchical* account to test. On the hierarchical account there is no second controller. Habits are **chunked action sequences**, and a single goal-directed process selects between individual actions and habitual sequences to reach the goal. The two accounts make a clean, discriminating prediction on a two-stage decision task: if a first-stage action and a second-stage action are bound into a sequence, then selecting the habitual action at stage one should be followed by the habitual action at stage two. On the flat account the two stages are independent.

Using human subjects' choices and reaction times, they found the coupling the hierarchical account predicts: subjects combined single actions into sequences, and sequence formation was **sufficient** to explain habitual action. A Bayesian model comparison across families of models favoured the hierarchical family over the flat family.

## Why this matters for MECH-323

MECH-323's output contract is that the accumulator takes planned-system trajectories as input and emits chunked primitives, after which the planner selects over a mixed inventory of primitives and chunks. That is the ARC-071 R3 planned-to-habitual transition, and until now it has been a design commitment resting on the striatal chunking literature (Graybiel, Smith & Graybiel, Jin & Costa) — which establishes that chunks form, but not that the resulting chunks are *selected by the planner alongside primitives*, which is the part MECH-323 actually needs.

This paper supplies that part, and supplies it as a discriminating test rather than an assumption. It is the strongest single piece of evidence for MECH-323's architecture that I have found, and its mapping fidelity is unusually high because what transfers is a *relation* — who selects over what inventory — rather than a parameter. Relations port across domains in a way that rates and thresholds do not.

## The tension worth flagging to governance

The paper's central negative claim is that **model-free RL is unnecessary**. If chunked sequences alone suffice to produce every signature of habitual behaviour, then a dual-system architecture is one system too many.

MECH-323 cross-links to MECH-163 (dual_goal_directed_systems), and positions itself as "the formation machinery on the habit-system side" of that dual system. Dezfouli and Balleine's result puts pressure on the framing rather than on MECH-323 itself: on their account MECH-323 would not be the formation half of a habit *system*, it would be very nearly the *whole* of what "habit" names, with the habit system reducing to the chunk inventory plus the grain at which the planner can intervene. I have deliberately not tagged this entry against MECH-163, because the direction differs by claim — it supports MECH-323 while complicating MECH-163's framing, and a single `evidence_direction` field cannot carry both honestly. But it should be picked up when MECH-163 is next visited, and I have recorded it as the lead failure signature so it is discoverable from there.

There is a second, more practical consequence in the same vein. If apparent outcome-insensitivity is a consequence of sequence *grain* — the controller simply cannot intervene mid-chunk — rather than of a separate insensitive controller, then MECH-323's chunk-size budget is quietly a controllability parameter. Set the budget too high and the agent looks habit-bound, not because anything in the accumulator misfired but because there are fewer decision points at which the planner can act. That failure would present as outcome-insensitivity and would report nothing at the accumulator. Worth instrumenting.

## Where the mapping breaks

This is evidence for the architecture, not the accumulator. The paper says chunked sequences exist and are hierarchically selected. It says nothing about MECH-323's actual commitments: the formation trigger (repetition plus outcome consistency), the hysteresis relation F_low < F_high, or the 2–5 element chunk-size budget per level. Those come from the R1/R4/R5 verdicts and remain ungrounded by this entry — the Desrochers et al. companion entry speaks to the trigger; the hysteresis and size parameters are still literature-thin.

It is also a single two-stage decision paradigm with abstract choices, a long way from either motor grain or REE's policy-primitive grain, and the authors are careful to say the finding does not rule out all possible model-free accounts. I have taken that caution seriously in the confidence.

## Confidence reasoning

0.78. Source quality 0.82 — a solid computational-neuroscience venue, formal Bayesian model comparison over model *families* rather than single models, and two converging behavioural measures, discounted for single-paradigm evidence. Mapping fidelity 0.80, high for the reason given above. Transfer risk low at 0.25, since architectural relations are the safest thing to borrow across domains. I would be comfortable treating this as load-bearing for MECH-323's output contract, and not at all comfortable treating it as evidence for any of MECH-323's numeric parameters.
