# Kim & Lim (2022) — Dynamical origin for winner-take-all competition in the dentate gyrus

**Source:** Physical Review E 105(1-1):014418. DOI [10.1103/PhysRevE.105.014418](https://doi.org/10.1103/PhysRevE.105.014418). PMID 35193268. Retrieved via PubMed.

**Claim:** SD-016 (selection mechanism leg — GOV-FANOUT-1 H3).
**Direction:** supports. **Confidence:** 0.66.

## What the paper did

Where Espinoza et al. (2018) measured the wiring that makes winner-take-all *possible*, Kim & Lim
build a conductance-based spiking model and ask what actually *decides* the winners. The model
groups granule cells into lamellar clusters, each with one inhibitory basket cell. Granule cells
receive three external drives — direct excitation from entorhinal cortex, feedforward inhibition via
HIPP cells, and excitation from hilar mossy cells — and the authors summarise the balance with a
single scalar per cell: the time-averaged ratio of external excitatory to inhibitory conductance,
R\*<sub>E-I</sub>.

The result is a clean threshold rule. Granule cells become active when their R\*<sub>E-I</sub> exceeds
a threshold R\*<sub>th</sub>; among those that do, firing rate correlates strongly with
R\*<sub>E-I</sub>. Feedback inhibition from the cluster's basket cell does the selecting: cells above
threshold survive and become winners, everything else falls silent. That is what produces the ~5%
granule-cell activation degree that the pattern-separation literature treats as the DG's signature.
The paper closes by perturbing the competing population — mossy-cell death, and the addition of
adult-born immature granule cells — and showing the WTA competition shifts in both cases.

## Why this matters for SD-016

I included this paper for one reason, and it is worth being explicit about it: it is the only entry
in this pull that states the selection rule as something you could sit down and implement. The
electrophysiology papers establish *that* the dentate gyrus is built for competition and *what*
connectivity it uses; this one gives the update equation.

Reduced to its skeleton, and stripped of the biophysics, the mechanism is:

1. compute each unit's drive;
2. compute a shared inhibitory quantity pooled over the competing set;
3. let each unit survive according to its drive **relative to that pool**, against a threshold;
4. renormalise over the survivors only.

That is a k-winner-take-all / thresholded lateral-inhibition layer, and it is directly droppable into
`extract_cue_context` as the "minimal selection-mode knob" the SD-016 portfolio scope recommends for
H3. Set against what SD-016 does today — produce 16 slot logits and softmax them, with no mechanism
by which one slot's drive suppresses another's — the contrast is exactly the diagnosis the V3-EXQ-898
autopsy reached. A plain softmax has no step 2 and no step 3. There is nothing in it that makes
non-uniform selection preferable to uniform mixing, which is presumably why uniform mixing turns out
to be a stable attractor of the loss landscape (C2 reproduces ln(16) = 2.772589 to five decimal
places on every OFF cell, on every seed, across two architecturally distinct selection paths).

There is also a useful diagnostic prediction here, which I think is the paper's second contribution
to the H3 design. If a competitive operator is working, the *number* of surviving slots should be
small and reasonably **stable**, while *which* slots survive should vary with context. That maps onto
the C1/C1b instrument pair SD-016 already has — and it predicts they should move **together**. That
is worth stating in the H3 acceptance criteria, because it discriminates against the specific
degenerate outcome 418m produced: a static non-uniform-but-fixed selector, which passes a low-entropy
test while context-divergence stays flat at ~0.002 against a 0.1 target. Under the Kim & Lim
mechanism that combination should not occur, because the thresholding is applied to *relative* drive,
which is context-dependent by construction. A build that produces low entropy with flat divergence has
probably implemented step 3 against an absolute threshold rather than a pooled one.

## Limitations — and why I held confidence at 0.66

This is the weakest entry in the pull on source quality, and I want to be straight about why it is
still here. Physical Review E is a respectable venue, but this is a single-group modelling paper with
no empirical component and modest impact. More importantly, **it assumes the framing it explains**. It
tells us how sparse selection arises *given* a DG-like circuit; it is not independent evidence that
the dentate gyrus performs pattern separation. That evidence lives in the Espinoza and Neunuebel
entries, and this paper must not be double-counted as if it corroborated them.

The mapping caveats are substantial and I have priced them in at transfer_risk 0.45 — the highest in
this directory:

- **The spiking time axis has no counterpart.** A conductance ratio time-averaged over a spiking
  simulation is meaningless in a single-tick feedforward tagger. Only the relative-drive comparison
  survives the abstraction.
- **The lamellar-cluster topology is real structure that I am proposing to discard.** Competition in
  the model is *local* to a cluster with its own basket cell, not global across the population.
  Collapsing that to a single global inhibition term over all 16 SD-016 slots is a substantive
  architectural change, not a faithful reduction, and the paper gives no grounds for expecting the two
  to behave equivalently.
- **The sparsity regime does not instantiate.** ~5% of a granule-cell population is a large absolute
  number of winners; ~5% of 16 slots is less than one. So the model cannot tell us what *k* should be
  for SD-016 — that will have to be swept, and the sweep is a design cost the H3 leg should budget for
  rather than assume away.
- **The WTA regime is fragile to population composition.** The mossy-cell-death and immature-granule-cell
  manipulations both perturb the competition. Read across, that says a slot array with heterogeneous or
  drifting effective gain may simply not sit in the competitive regime — which is a live risk for
  SD-016, whose 16 slots are not guaranteed to be gain-matched.

Taken together with Espinoza (2018), the pair does the H3 job jointly and neither does it alone:
Espinoza says the competitive machinery is structural rather than loss-induced and constrains its
*shape* (lateral not recurrent, broad suppression, relative decision); Kim & Lim turns that shape into
an operator with a threshold in it. The honest summary is that H3 now has a biologically-grounded
specification, and one genuinely open parameter (*k*, and the choice of differentiable relaxation)
that the literature does not settle.
