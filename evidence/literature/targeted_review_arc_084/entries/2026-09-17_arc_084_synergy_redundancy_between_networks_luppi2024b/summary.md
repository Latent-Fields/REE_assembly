# Quantifying synergy and redundancy between networks (Luppi et al., 2024)

## What the paper did

This is a formal contribution rather than an empirical one. Luppi, Olbrich, Finn, Suarez, Rosas,
Mediano and Jost present an analytical framework that decomposes the shortest paths between nodes
according to which of two source networks contributes them: uniquely by one network, redundantly by
either, or synergistically by both together. They apply it across 125 species' connectomes and report
that long-range white-matter connections make substantial unique contributions to structural
organisation, and that communication efficiency shows significantly greater synergy between
long-range and short-range fibres than chance would predict.

## Why this is the entry a governance decision should read first

The other three ARC-084 entries lean supportive with caveats. This one is genuinely two-directional,
and the two directions bear on different halves of the claim.

It supports the typed half about as well as anything could. ARC-084 asserts that inter-field coupling
should be represented as a typed edge rather than a scalar weight. Here is a rigorous, quantitative,
comparatively validated instance of doing exactly that between two networks. If anyone doubted that
"typed coupling between networks" is a coherent formal object rather than a gesture, this settles it.

And it weakens the signed half, quietly but persistently. The type space is `{unique, redundant,
synergistic}`. It is non-negative throughout. There is no competitive mode, no negative sign, and
across 125 species the framework nevertheless does real explanatory work. The best-developed formal
typology of inter-network coupling available simply does not need the thing ARC-084 declares to be
first-class.

## What that actually licenses one to conclude

Less than it first appears, and I want to be careful here because the temptation to over-read is
strong in both directions.

This is a *structural* decomposition defined over shortest paths in a graph. Its types are properties
of routing topology. ARC-084's edge is a *dynamic* object carrying gain, precision, gate, timescale
and write authority as independently manipulable parameters. A topological typology having no
competitive mode is genuinely weaker evidence against a dynamic signed mode than the surface parallel
suggests -- you would not expect a shortest-path decomposition to represent suppression even if
suppression were everywhere in the dynamics.

So the honest conclusion is narrower and more useful than "this weakens ARC-084". It is that the
typed-edge literature has already conceded ARC-084's first point and does not speak to its second.
That isolates the real burden precisely: ARC-084 does not need to argue that edges can be typed, which
is now settled, but that *adding a sign* buys causal power an unsigned typology cannot reproduce. That
is exactly the dissociation the claim's own CONFIRMING criterion demands -- manipulating edge sign or
gain producing effects that adjusting local softmax temperature or top-k cannot -- and it is a
sharper target than the claim's current framing conveys.

## Confidence

0.55. Transfer risk is the lowest of anything in this pull (0.40), because a mathematical
decomposition carries over to an artificial substrate far more cleanly than a species-specific
physiological finding does; if REE ever builds a cognifold edge layer, this framework could be applied
to it more or less directly. Mapping fidelity is middling (0.52) for the axis-mismatch reason set out
in the companion eLife entry. The direction is recorded as mixed rather than split because both
effects fall on the same claim and neither dominates.
