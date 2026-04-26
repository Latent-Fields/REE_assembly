# Berridge & Robinson 1998 -- wanting persists as incentive salience, not mere pleasure

## What the paper did

Berridge and Robinson reviewed lesion, pharmacological, and behavioral evidence
to separate three reward functions that had often been conflated: liking,
wanting, and reward learning. Their central argument is that dopamine is not the
substrate of pleasure itself. Instead, dopamine primarily mediates incentive
salience: the motivational pull toward a goal.

## Key findings relevant to ghost-goal search

The load-bearing result is the wanting/liking dissociation. Animals can lose
approach motivation while retaining hedonic reactions at contact, and can show
elevated approach drive without increased pleasure. This means a goal can remain
motivationally live in a form that is not reducible to local consummatory reward.

For ghost-goal search, that matters because the architecture needs to preserve a
trace of "what is still wanted" even when the goal is not currently reachable.
If wanting is a real and separable signal, then preserving a goal-linked payload
on an inactive anchor is biologically and computationally sensible.

## Translation to REE

REE already separates wanting-related machinery from contact-level benefit. This
paper strengthens the case for SD-039 and ARC-060: unresolved-goal traces should
preserve motivational identity, not just `z_world` geometry or a stale-region
flag. A stale region with no preserved wanting content is not a ghost goal; it
is just unresolved terrain.

## Limitations and caveats

This paper does not discuss hippocampal anchors, replay, or blocked-goal memory.
Its role here is foundational rather than specific: it establishes that wanting
is the kind of signal worth preserving independently of contact pleasure.

## Confidence reasoning

Confidence 0.87. The paper is canonical and directly supports the distinction
between preserved wanting and local hedonic contact. The gap is specificity: the
translation from mesolimbic incentive salience to REE's ghost-goal substrate
requires additional hippocampal and replay literature.
