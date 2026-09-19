# HuD, Bdnf mRNA, and activity-induced dendritic synthesis (Vanevski & Xu, 2015)

## What the paper shows

Vanevski and Xu trace a chain that is worth stating in order, because the order is the finding.
Neuronal ELAV-family RNA-binding proteins associate with Bdnf mRNA isoforms in the adult brain, and
the association is activity-dependent. HuD binds directly to sequences in the long Bdnf 3'UTR and
co-localises with the transcript in hippocampal dendrites. Activating protein kinase C increases
dendritic translation of long-3'UTR Bdnf mRNAs, and that increase requires HuD and requires its
phosphorylation at threonine 149 and/or 165.

The sentence that matters for us is their framing of the baseline: activity-dependent signalling
*relieves basal repression* of Bdnf mRNA translation in dendrites.

## Why this is the mechanism shape the intake was asking for

The 2026-05-21 intake stages `plasticity.signal_as_proposal_not_update` -- the idea that a plasticity
signal should propose a write rather than perform one, with a separate decision about whether the
proposal commits. That is an architectural assertion, and the intake's own guardrail was that no MECH
gets registered until the biology has been looked at.

Here is the biology doing it. The transcript is already in the dendrite. It is already bound. It is
already repressed. The write, in other words, is staged and waiting, and it carries its own content.
What the activity signal supplies is not the content but the *release*. Proposal and commit are
separate objects in the molecular implementation, and the separation is not incidental -- it is what
makes local, synapse-specific plasticity possible at all, since a signal that carried its own content
could not be localised the way a release signal can.

That, combined with the previous entry, gives the (a) half of the gate both limbs it needed: the
operator is present and functional in the adult brain (Vanevski & Xu, and the addiction-related adult
plasticity work from the same HuD literature), and running it without restriction is harmful
(Bolognani et al.).

## Two places where the mapping should not be waved through

The gate's *direction* is de-repression. The default is blocked; the signal unblocks. Several of the
staged candidates -- `typed_gated_event_controller`, `depth_ladder_eight_rungs` -- are phrased as
admission: a controller opens a window and writes come through it. These are not interchangeable. A
de-repression gate that fails leaves the write blocked, which is safe. An admission gate that fails
can leave the window open, which is not. If the candidates are registered without stating which
polarity they mean, REE acquires an ambiguity that the biology it is citing does not actually have.

The gate's *specificity* is per-target, not per-event. What makes this write gateable is a feature of
this mRNA's 3'UTR. The staged controller candidates assume something types the *event* and then
permits a class of writes. Both are coherent designs; they are not the same design, and this paper
supports the first.

## Confidence

0.69. PLoS ONE rather than a top-tier venue, and the assays are dendritic translation rather than
behaviour, so source quality is moderate. The mapping is the strong part: I have rarely seen a piece
of molecular biology sit this close to an architectural claim's own wording. The discount is for the
polarity and specificity gaps above, which are real and which I would rather see resolved at
registration than after.
