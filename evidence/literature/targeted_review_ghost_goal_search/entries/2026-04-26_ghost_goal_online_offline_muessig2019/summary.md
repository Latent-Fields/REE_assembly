# Muessig et al. 2019 -- one sequence generator can support waking and offline unresolved-goal work

## What the paper did

Muessig and colleagues studied the developmental emergence of hippocampal theta
sequences and SWR replay. Their key finding was that these two forms of sequence
generation emerge together rather than as independent, unrelated capacities.

## Key findings relevant to ghost-goal search

The main implication is architectural unity: online and offline sequence
generation are two modes of the same underlying mechanism. For ghost goals, this
means the unresolved-goal substrate should not be sleep-only. If an unresolved
goal trace is important enough to bias offline replay, it is reasonable for the
same trace to bias waking probe allocation as well.

## Translation to REE

This anchors the shared-substrate part of ARC-060 and MECH-293. The waking
proposal branch and the offline replay branch can differ in timing and weight, but
they should not require totally separate representations of unresolved goals.

## Limitations and caveats

The evidence is developmental and indirect. It supports a shared sequence
generator, not an explicit ghost-goal bank. The translation here is architectural
inference rather than direct empirical demonstration.

## Confidence reasoning

Confidence 0.66. Good support for shared waking/offline substrate, moderate gap on
the unresolved-goal-specific mapping.
