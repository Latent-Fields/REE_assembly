# Contingency detection does not predict later self-recognition (Klein-Radukic & Zmyj, 2020)

## What the paper did

Klein-Radukic and Zmyj ran a longitudinal study on 113 infants, asking a question that
developmental theory had largely assumed the answer to. At 6 and 9 months they measured two things
in contingency tasks: whether infants *preferred* a noncontingent over a perfectly contingent view
of themselves, and whether they *differentiated* the two at all (indexed by looking longer at
either). Then they waited. At 18 months they ran a mirror-face-recognition task and a
mirror-leg-recognition task; at 26 months, a video-face-recognition task and again the mirror-leg
task. The design is the right shape for an ordering question: an early measure of sensitivity to
self-produced sensory change, a later measure of self-representation, and enough time between them
for the causal story to play out if there is one.

There was no predictive relationship. Neither contingency preference nor contingency detection in
the first year forecast self-recognition in the second or third. The authors read this as support
for Bischof-Köhler's position that self-recognition emerges independently of contingency
experience, and conclude that a representation of the self "relies on more than a specific
developmental pathway" running from contingency to recognition.

## How this bears on ARC-059

ARC-059 is an ordering claim, and it is explicit that the ordering is load-bearing rather than
merely convenient: without a self-model the agent cannot separate self-produced from world-produced
sensory change, so stage 1 has to come first. The developmental literature is the obvious place to
look for an existence proof, and the obvious existence proof is exactly the one this study fails to
find. That is worth recording honestly rather than filing the paper away because the result is
inconvenient.

But I want to be careful about what has actually been weakened, because the temptation is to take
this as more damaging than it is. The outcome measure here is mirror and video self-recognition --
an explicit, conceptual, arguably socially-scaffolded achievement that REE does not implement and
ARC-059 does not claim to produce. Stage 1's content is narrower and more mechanical: a
counterfactual-backed attribution of sensory change to self or world, closer to what the same
literature calls an online egocentric body schema than to the mirror mark test. Those two are not
the same construct, and the failure of one to predict the other is not the failure of stage 1 to
support stage 2. The predictor side has its own slack, too: a looking-time preference score is a
measure of *sensitivity to* contingency, not a measure of whether the infant has built an
action-space model out of it.

## What I take from it

The honest reading is that this weakens a strong version of the claim -- "contingency-based
self-discovery is the developmental route to a self-model" -- while leaving the narrow comparator
precondition largely untouched, because nobody measured the narrow thing. That is still a live
result for us, for a reason that has nothing to do with infants: it is a warning about
operationalisation. If a REE skip-ordering ablation reads stage-1 competence off a coarse
behavioural proxy and then reads the downstream effect off a coarse self-model proxy, this study is
a demonstration that the two can fail to correlate even in a system where the mechanism is
arguably present. A null in that arm would then be uninformative rather than falsifying, which is
precisely the non-degeneracy trap ARC-059's own `what_would_answer` is already circling.

There is also a transfer question running the other way, and it cuts against reading the null too
broadly. Infants are not blank agents. Whatever action-space priors they are born with, REE's
stage 1 has to *construct*. A developmental null showing that human self-recognition survives
without a contingency route says relatively little about whether an artificial agent with no innate
body model can skip the equivalent stage. I have set transfer risk at 0.55 for that reason, and
confidence at 0.5: the method is good, the mapping is the weak joint.
