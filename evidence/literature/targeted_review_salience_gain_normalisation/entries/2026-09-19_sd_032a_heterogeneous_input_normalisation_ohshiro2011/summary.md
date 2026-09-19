# A normalization model of multisensory integration (Ohshiro, Angelaki & DeAngelis, 2011)

## Why this paper is in this review

The standing objection to importing divisive normalization into the SalienceCoordinator is
structural rather than empirical. Normalization, as Carandini and Heeger present it, operates over a
pool of like-coded units -- orientation channels, odour channels, value-coded targets. SD-032a's
`affinity_weights` pool is nothing like that. It holds a prediction error, a foraging value, and a
bounded engagement drive: different provenance, different units, wildly different dynamic ranges.
The 2026-08-12 comment in `salience_coordinator.py` records the consequence precisely -- diagnostic
replay measured `dacc_pe` around 16-17 through eval, two orders of magnitude above the
`[0,1]`-bounded engagement signal, so `internal_planning`'s argmax never yielded and the operating
mode collapsed to one-hot.

Ohshiro and colleagues address exactly that structure. Their normalization operates at the stage
where inputs of *different modalities* converge, and they show it reproduces the empirical
signatures of multisensory integration: inverse effectiveness, the spatial principle, and -- the
striking one -- the fact that the mathematical rule by which neurons combine their inputs *changes
with cue reliability*. The paper's diagnostic prediction, cross-modal suppression, was confirmed six
years later in macaque MSTd.

## What it settles for REE, and what it opens

It settles the structural objection. Normalization is not restricted to homogeneous pools; the
brain uses it precisely where incommensurable inputs must be combined without one swamping the
others. That is the SalienceCoordinator's problem statement almost word for word.

But reading the model carefully makes the substrate question *harder*, not easier, and this is the
part I would not want a governance session to miss. Two properties the model depends on are not
innocuous when ported.

The first is inverse effectiveness. Normalization does not merely bound large inputs; it makes weak
inputs combine super-additively. A normalizing operator in `tick()` would therefore change mode
occupancy in the low-signal regime as well as the high-signal one. The `mode-governance-engagement`
entry is titled as if the change were a safer bound on an existing behaviour. It is not: it is a
change to the shape of the whole response function, and no current REE experiment measures the
low-signal end.

The second is cross-modal suppression. In the model, a non-preferred input that activates the unit
on its own *suppresses* the response to a preferred input from another modality, because the
normalization pool includes both. Ported to SD-032a, a large `dacc_pe` would suppress
`external_task_drive`'s affinity contribution even when the two argue for different modes. Today's
clamp is strictly per-signal and independent; no such coupling exists. Adopting the pooled form is
therefore introducing a new mechanism into the coordinator, not bounding the old one more gently.

There is also a plain gap: the model's explanatory power comes from reliability-weighted pooling,
and REE has no reliability or precision estimate attached to these signals at the affinity-input
stage. Fix the weights and you keep the coupling while losing the property that made the model work.

## Confidence

0.71. It is a modelling paper, which caps source quality below the electrophysiology entries, but
its central prediction has since been confirmed and it is the only entry in this review that speaks
directly to heterogeneous convergence. The discount reflects that its faithful import would be a
larger substrate change than the one currently on the queue -- which is useful information, but not
the same as endorsement.
