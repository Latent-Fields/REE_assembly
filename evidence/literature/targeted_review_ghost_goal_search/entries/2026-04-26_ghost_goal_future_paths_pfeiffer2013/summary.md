# Pfeiffer & Foster 2013 -- hippocampus sweeps future paths to remembered goals

## What the paper did

Pfeiffer and Foster recorded CA1 ensembles in rats navigating an open field with
remembered goal locations and decoded brief hippocampal trajectory events before
goal-directed navigation. They asked whether these events were generic sweeps or
goal-biased path computations.

## Key findings relevant to ghost-goal search

The decoded events were biased to progress from the animal's current location
toward the remembered goal. This is strong evidence that hippocampal sequence
generation can be future-directed and goal-specific rather than just a generic
sampler.

For ghost-goal search, that matters because it means a goal-preserving probe
policy is not biologically exotic. The sequence generator already supports
goal-directed future sweeps; the missing question is what latent goal traces get
fed into it.

## Translation to REE

MECH-293 proposes that waking search should spend some budget on unresolved but
still-wanted anchors. Pfeiffer & Foster do not prove that exact algorithm, but
they strongly support the more general step from "hippocampal search over current
terrain" to "hippocampal search guided by remembered goal structure".

## Limitations and caveats

The sequences were SWR-associated rather than straightforward theta-bound planning
events, so the precise timing channel in REE is still an implementation choice.
The important part for this review is goal-biased future-path generation, not the
carrier rhythm.

## Confidence reasoning

Confidence 0.73. Strong support for goal-directed hippocampal search, with a real
caveat about the biological timing channel.
