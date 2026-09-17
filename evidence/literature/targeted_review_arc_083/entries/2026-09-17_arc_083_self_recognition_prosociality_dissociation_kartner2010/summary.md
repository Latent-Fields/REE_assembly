# Cognitive and social influences on early prosocial behavior in two sociocultural contexts (Kärtner, Keller & Chaudhary, 2010)

## What the paper did

Thirty-eight Berlin toddlers and thirty-nine Delhi toddlers, all around 19 months, were given a
mirror self-recognition test and observed for prosocial behaviour; their mothers were interviewed
about socialisation goals. The design exists to test whether the self-recognition-to-prosociality
link — the Bischof-Köhler prediction that anchors the previous entry in this directory — is a
developmental universal or a feature of the populations it was discovered in.

It is not a universal. Self-recognition correlated with prosociality in Berlin and did not in Delhi.
What predicted prosocial conduct in *both* samples was the mother's emphasis on relational
socialisation goals.

## Why this is the strongest counter-evidence in the pull, and why the control condition matters

The result that does the work is not the Delhi null on its own. A null in a small sample is cheap.
The result that does the work is that **the two groups did not differ in how much prosocial
behaviour the toddlers actually produced.** That closes off the reading that would otherwise defuse
this entirely — that Delhi toddlers simply had not got there yet, and the correlation was absent
because the behaviour was absent. It was not absent. Equivalent other-directed behaviour, present in
both groups, predicted by self-recognition in one and not the other.

A necessity claim cannot survive that pattern. If a stable self-representation were *required*
before a system can act on another agent's state, there is no way to get a population that mounts
the behaviour at full rate while the proposed prerequisite carries no predictive weight. DEV-NEED-021
does not say "self-stability is one common route to otherness inference". It says otherness inference
REQUIRES self-stability, and ARC-083 restates that as a gate on PILLAR 4. This paper is a
counterexample to the gate.

## What it does not establish, which is more than I would like

Prosocial helping is not otherness inference, and I do not want to slide between them. A toddler who
hands back a dropped clothespeg has done something other-directed, but has not necessarily
individuated the adult as a persisting agent with her own goal state — which is what ARC-083's
per-agent slot is for. The dissociation could be occurring one level below the capacity actually at
issue, with both samples' helping driven by a cue-response route that never touches agent
individuation at all. That possibility is genuinely open and this study cannot close it. It is the
reason mapping fidelity here sits at 0.6 rather than higher, the same figure I gave the supporting
Bischof-Köhler entry — the two papers share the same proxy weakness, and it would be
self-serving to credit the proxy when it supports the claim and discount it when it does not.

The other honest limitation: a socialisation-goals moderator explains variance without supplying a
mechanism. Knowing that Delhi mothers weight relational goals more heavily tells us the developmental
input differs; it does not tell us what the Delhi toddlers were representing in place of a
self-recognition-gated other-model. For an architectural claim that is the question, and this paper
does not answer it.

## What REE should take from this

Not a demotion. ARC-083 is an architectural commitment with promote/demote suppressed, so the
question is never "does this refute the claim" but "does it change what should be built". Here it
does, in a specific way.

The DEV-NEED-021 prerequisite should be treated as **one developmental route** to per-agent
other-object slots, not as a gating condition on them. Concretely, an implementation that hard-blocks
other-object allocation behind a self-stability audit — which is what the current dependency
structure invites, ARC-083 `depends_on` ARC-081 with the `readiness_gate` language in
`mirror_modelling_other_self_v5` making it explicit — would be encoding a culturally contingent human
developmental pathway as an architectural invariant. That is the kind of mistake that is invisible
until the agent needs to do social inference and the gate will not open.

The cheaper and better-supported move is to keep the *ordering* as a default build sequence (build
the self first because it is convenient and because ARC-081 is independently motivated) while
dropping the *necessity* language from the claim text. Those are different commitments, and
DEV-NEED-021 currently conflates them. I have not made that edit — it is a governance disposition,
not a lit-pull's call — but it is what this entry and the Sodian entry jointly point at.

## Confidence

0.62. Above both the hippocampal entries and the Bischof-Köhler anchor, because this is the only
paper in the directory whose design directly targets the proposition under test rather than bearing
on it incidentally, and because the matched-behaviour control makes the dissociation interpretable
rather than merely null. Capped there by the small cells, the proxy problem, and the fact that a
cultural moderator names a difference without explaining it.
