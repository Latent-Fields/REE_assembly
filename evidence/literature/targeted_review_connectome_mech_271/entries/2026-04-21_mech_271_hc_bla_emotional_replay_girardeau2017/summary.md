# Girardeau, Inema & Buzsáki (2017) — "Reactivations of emotional memory in the hippocampus-amygdala system during sleep"

**Nature Neuroscience** 20:1634–1642. [DOI](https://doi.org/10.1038/nn.4637). PMID 28892057.

*(According to PubMed.)*

## What the paper does

Girardeau and colleagues ask a specific mechanistic question: consolidation of context-dependent emotional memory is known to require communication between hippocampus and basolateral amygdala, but how does that communication actually happen? They recorded simultaneously from CA1 and BLA ensembles in rats learning an aversive air-puff task on a linear track, and looked at how the two regions behaved during the non-REM sleep that followed learning.

They found three things. First, hippocampal and BLA ensembles showed coordinated reactivation during sleep, and this coordination peaked at the moment of hippocampal sharp-wave ripples. Second, a subgroup of BLA cells was positively modulated during hippocampal SWRs specifically — so the BLA is a genuine downstream recipient of SWR-gated signalling, not an independent co-active structure. Third, and most important for the present purpose, the reactivation was not indifferent to content. Hippocampus–BLA correlation patterns for the aversive-air-puff direction reactivated more strongly than patterns for the safe direction. Emotional content — the portion of the trajectory that carried affective load — drove the HC–BLA communication selectively.

## Findings relevant to MECH-271

MECH-271 predicts that the hypothesis tag in MECH-094 is realised not as an undifferentiated source-side flag on simulated content, but as a routing difference on the downstream fan-out of hippocampal replay. Anchored replay should preferentially reach consolidation consumers (subiculum → EC → neocortex; lateral PFC viability map); probe replay should preferentially reach affective-tagging consumers (BLA) and curiosity channels (NAc).

Girardeau et al. give the strongest direct evidence for the BLA side of that prediction. They establish two things that MECH-271 needs: (a) HC replay reaches the BLA specifically — it is a downstream target, not a coincidentally co-active region — and (b) the routing is content-selective, not a broadcast. The BLA is engaged by the affectively-loaded subset of replay content, not by everything the hippocampus rehearses. That is exactly the architectural shape MECH-271 predicts: a differential routing signature, not a flag riding on all content equally.

The selectivity result matters more than the raw routing result. A non-selective HC→BLA broadcast would be consistent with MECH-271 being wrong (tag as undifferentiated flag just delivered through one more channel). The fact that aversive content reactivates more than safe content says that the channel is gated, and that the gating is on content — which is structurally isomorphic to MECH-271's routing-based tag realisation.

## How it translates to REE

The translation is fairly direct. REE's amygdala analog (SD-035, under active implementation as of 2026-04-21) is the predicted probe-destination consumer for MECH-271. Girardeau et al.'s finding that HC SWRs route content-selectively to BLA is the biological counterpart of MECH-271's architectural prediction. When the BLA analog experiment (V3-EXQ-474) runs, the expected signature is: BLA engagement correlates with emotionally-loaded or probe-tagged replay content, not with anchored/consolidation-routed content.

This paper also sharpens the failure mode MECH-271 predicts for tag loss. If the content-gating breaks — if HC→BLA replay starts routing with equal strength for both aversive and safe content, or if conversely HC→EC consolidation routing becomes equally strong for probe and anchored content — that would be the observable signature of the tag erosion MECH-094 predicts for confabulatory planning.

## Limitations and caveats

The paradigm contrasts aversive and safe spatial content. That maps cleanly onto REE's z_harm_s stream, but not as cleanly onto the full anchor/probe distinction. Probe rollouts in MECH-269's sense are epistemically-driven (low per-stream verisimilitude, high prediction error) rather than emotionally-driven. Mapping "emotional content" to "probe content" requires granting that affective load and epistemic uncertainty both route through BLA — a plausible REE-side claim, but one this paper does not establish.

The study is rodent-only, and the aversive content is a simple spatial air-puff association. Scaling to the richer structure REE assumes — multiple latent streams, anchor/probe decomposition across z_world / z_self / z_harm_s / z_goal — requires interpretive work the source does not do.

The paper examines sleep-state reactivation. Awake SWR routing may differ, as Tang et al. 2017 show for the HC–PFC axis. MECH-271's routing prediction is phrased without a state qualifier; future work should establish whether the anchored/probe routing split holds during awake SWRs too, or whether the state itself is a gating variable.

## Confidence reasoning

Source quality is very high — Nature Neuroscience, Girardeau and Buzsáki as senior authors, rigorous simultaneous dual-site electrophysiology with appropriate controls. Mapping fidelity is the best of the MECH-271 papers I pulled because this is direct evidence for the BLA side of the routing prediction with content selectivity, which is the architectural feature MECH-271 hinges on. Transfer risk is moderate: aversive spatial content is narrower than REE's latent-stack and the sleep-state specificity is a further caveat. Net confidence 0.78.
