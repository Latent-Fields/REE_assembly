# Cholinergic and dopaminergic effects on prediction error and uncertainty responses during sensory associative learning

Iglesias, Kasper, Harrison, Manka, Mathys & Stephan (2021), *NeuroImage* 226:117590. DOI [10.1016/j.neuroimage.2020.117590](https://doi.org/10.1016/j.neuroimage.2020.117590) · PMID 33285332

**Claim tested:** MECH-043 — *Dopamine-like modulation of precision-weighting for unsigned prediction errors.*
**Direction:** weakens (confidence 0.72)

## What the paper did

This is a replication attempt the authors ran against their own hypothesis, which is what makes it worth reading carefully. Their 2013 *Neuron* study had found that low-level precision-weighted prediction errors about visual outcomes activated the midbrain, while high-level precision-weighted PEs about cue-outcome associations activated the basal forebrain — a tidy suggestion of selective dopaminergic and cholinergic influence at different levels of a hierarchical Bayesian model. Here they tested that directly, with two between-subject double-blind placebo-controlled pharmacological fMRI studies: study 1 with antagonists (biperiden, muscarinic; amisulpride, dopaminergic), study 2 with agonists (levodopa; galantamine).

The anatomical pattern replicated when pooled across drug conditions. The pharmacology did not cooperate. Drug effects on brain activity emerged only after splitting the precision-weighted PE back into its separate PE and precision components, and the resulting pattern crossed the systems rather than respecting them: galantamine, a cholinergic drug, enhanced low-level PE responses in the putative *dopaminergic* midbrain; amisulpride, a dopaminergic drug, affected a putatively *cholinergic* brainstem region and separately enhanced high-level precision activity in the midbrain. Task behaviour was unaffected by any of the four drugs. The authors conclude that their results do not support a clear-cut dichotomy between hierarchical inference levels and neurotransmitter systems, and propose a more complex interaction instead.

## How this translates to REE

It is worth being precise about which half of MECH-043 this bears on. The claim has two parts. The first — that REE's precision term is computed from unsigned error magnitude with no valence reaching it, is live-invoked, and influences commitment — is essentially settled by code audit; INV-008 confirmed it, and `current_precision = 1/(running_variance + 1e-6)` over an EMA of squared PE is unsigned by construction. This paper says nothing about that half.

The second part is the attribution: that this channel is *dopamine-like specifically*. MECH-043's falsifier (iv) states the claim is violated if the effect is fully explained by a shared, general precision-scale parameter that also governs MECH-054's signed channels identically, with no functional dissociation demonstrable. Iglesias et al. is the most direct human test of that specificity available, run by the group with the strongest prior stake in a positive result, and it comes back negative: no clean dopaminergic locus for precision-weighted PE, cross-system effects that invert the predicted assignment, and no behavioural consequence at all.

The implication for REE is concrete rather than merely cautionary. If the biology does not cleanly separate a dopaminergic precision channel from a cholinergic one, then routing precision through a single dopamine-like term is a *simplification* the literature does not underwrite. MECH-043 is better read as a claim about REE's own architecture whose biological warrant is thinner than Haarsma et al. (2021) would suggest if taken alone.

There is also a sobering practical signal. No drug affected behaviour. If REE expects that misallocating its dopamine-like precision channel will shift a behavioural DV, the closest human pharmacological analogue produced nothing behaviourally — which should lower the expected effect size for MECH-043's CONFIRMING sweep, and argues for powering it accordingly rather than reading a small null as a falsification.

## Limitations and caveats

A null is not an absence, and this one comes with confounds the authors name themselves. Pharmacological fMRI is vulnerable to vascular effects on BOLD that are independent of neural activity, to dose-response non-monotonicity, and to between-subject designs being underpowered for exactly the interaction effects at issue. They discuss all three and outline improved future tests rather than declaring the hypothesis dead. That is why this sits at 0.72 and as *weakens* rather than as a refutation.

Nor does it undercut Haarsma et al. Those authors used a different paradigm, targeted cortical rather than subcortical loci, and did obtain both behavioural and clinical effects. The two are compatible. The honest summary of the human pharmacology is that it supports "dopamine modulates precision-weighting somewhere" considerably better than it supports "precision-weighting is *the* dopaminergic channel, dissociable from others."

Read constructively, that is an argument for running MECH-043's isolation experiment rather than against it. A REE sweep that isolates the precision channel from MECH-054's signed channels and from ARC-108/109 would be testing something the biology has not settled — which makes it more informative, not less.
