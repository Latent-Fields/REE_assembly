# Smoothened on cholinergic interneurons modulates ACh-DA dynamics, learning and effort (Uribe-Cano & Kottmann, 2026)

## Provenance

This is the paper behind the raw thought at
`REE_assembly/docs/thoughts/2026-05-04_smoothened_modulation_ACh_Dopamine_learning.md`, and the
2026-09-16 hygiene pass recorded that it "is not banked under any `targeted_review_*`". It is now.
Banking the source a thought was built from is not a formality -- it is what lets a later reader
check whether the thought's reading of the paper was right.

## What the paper does

Uribe-Cano and Kottmann had previously found that the GPCR Smoothened on cholinergic interneurons
suppresses L-DOPA-induced dyskinesias in the Parkinsonian brain. Here they ask what it does in the
healthy one. Using cholinergic-neuron-specific manipulation, they show Smo activity *bidirectionally*
modulates acetylcholine inhibition following either dopaminergic or cholinergic neuron activity, and
that this alters the temporal organisation of ACh and its coupling to DA in dorsolateral striatum.
Behaviourally, Smo ablation from cholinergic neurons promotes motor learning and alters how the
animal adjusts the effort or time it will spend to obtain reward.

## Why it matters for the gate

The 2026-05-04 intake stages `e3.da_ach_coordination_layer`: a layer whose job is to coordinate the
*timing* of two modulatory signals rather than to carry content. That is an unusual architectural
proposal -- most modulatory-system claims make the modulator a content carrier -- and the intake's
own guardrail was that the biology should be checked before it is registered.

This paper is the check, and it passes. A single receptor, expressed on one interneuron class, can be
manipulated to change how ACh and DA are organised in time, *without being the source of either
signal*. Separability of the coordination layer from the signals it coordinates is exactly what the
candidate asserts, and here it is demonstrated causally rather than argued.

It also does something the other two ACh-DA entries cannot. Cragg 2006 is a review and is
correlational at the level of reward-related activity; Kim 2019 is a simulation. This is a causal
manipulation with a behavioural readout: change the coordination, and learning changes.

## The result that complicates the claim, and should be carried into it

Smo ablation *promotes* motor learning.

Disrupting the modulator that organises ACh-DA timing makes the animal learn the motor task better.
Whatever the wild-type coordination is for, it is not maximising learning rate. The same manipulation
also alters effort management, which suggests the coordination is trading learning against something
in the effort/persistence domain -- plausibly the thing that keeps an animal from over-committing to
whatever it most recently rehearsed.

For REE the implication is direct and slightly uncomfortable: a design that treats the plasticity
window as a learning-rate knob, to be tuned until learning is fastest, is optimising a quantity the
biology visibly declines to optimise. If the staged candidates are registered with the window framed
as a learning-efficiency mechanism, they will have imported the opposite of what this paper shows.

## A scope limit I want recorded

The locus is dorsolateral striatum and the assays are motor learning and effort -- a procedural,
habit-learning territory. INV-056's selective neoteny claim explicitly predicts that procedural and
motor substrates *can* fully harden, while social, goal-representation and epistemic-ethical
substrates retain elevated plasticity. The cluster these candidates belong to is mostly about the
latter. So this paper grounds the mechanism's existence and its causal reality, but generalising its
behavioural findings to the substrates the intake actually cares about is a step it does not support.

## Confidence

0.70, direction mixed. Good causal design and the right provenance, discounted for being a single
2026 laboratory result with no replication, for evidencing a coordination *layer* cleanly and a
discrete *window* only by inference, and for the procedural-locus mismatch.
