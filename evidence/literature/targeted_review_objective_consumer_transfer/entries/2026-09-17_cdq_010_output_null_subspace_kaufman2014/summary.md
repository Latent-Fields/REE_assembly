# Output-null subspace (Kaufman et al., 2014)

## The finding

Motor cortex carries large preparatory population activity that generates **no movement**, because it lies in an
**output-null** subspace of the downstream readout. Movement arises only from the **output-potent** subspace.

## Why it matters for CDQ-010

It is the cleanest biological demonstration that **variance magnitude upstream is not the quantity the consumer
responds to -- alignment with the readout is**. That is MECH-566's mechanism stated in neural terms.

SD-106 raised held-out preservation R^2 by +0.1184 and moved the consumer by +0.0081. Read through this paper,
the budget bought variance that was largely output-null with respect to the policy consumer.

## The disanalogy, stated

Kaufman's null space is **hard**: it is fixed by the muscle plant. REE's consumer is a *trained* MLP, so its
null space is **soft** -- directions it could read in principle but cannot reach with finite capacity, finite
data and standard initialisation. This is why MECH-566's falsifier is a **whitening test** (which changes the
code's conditioning while preserving its information exactly) rather than a subspace-alignment measurement.
