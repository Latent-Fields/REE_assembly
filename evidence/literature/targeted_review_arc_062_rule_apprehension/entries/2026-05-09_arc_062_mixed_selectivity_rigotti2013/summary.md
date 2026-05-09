# Rigotti et al. 2013 — The importance of mixed selectivity in complex cognitive tasks

According to PubMed: Rigotti, Barak, Warden, Wang, Daw, Miller & Fusi 2013, *Nature* 497(7451):585–90. [DOI 10.1038/nature12160](https://doi.org/10.1038/nature12160) (PMID 23685452, PMC4412347).

## What the paper shows

Single-unit recordings in macaque PFC during an object-sequence memory task. Most PFC neurons are tuned to *mixtures* of task-related variables rather than to a single clean variable. Mixed-selectivity neurons encode distributed information about all task-relevant aspects in a high-dimensional representational space; each task variable can be decoded from the population *even when the neurons that show single-cell tuning to that variable are excluded*. The dimensionality of the representation is behaviour-predictive — it collapses on error trials. The authors argue that this high-dimensional, mixed-selectivity coding offers a computational advantage over specialised responses by enlarging the repertoire of input-output functions a downstream readout can implement.

## What this means for R1 (input streams)

Direct, unambiguous support for the maximal-input default. PFC neurons do not channelise into "exteroceptive cell" / "interoceptive cell" / "affective cell" categories at the single-unit level — each neuron carries a mixture. ARC-062's discriminator should read all three streams (`z_world + z_self + z_harm_a`) rather than gating on `z_world` alone. The paper does not arbitrate among the three; it predicts that integration happens at the single-unit level rather than via stream-specific routing.

## What this means for R2 (discrete heads vs continuous gating) — the caveat

This is where Rigotti's biology pulls *against* ARC-062's weak-reading architecture. The mechanism Rigotti identifies is *continuous high-dimensional mixed selectivity*, not discrete head selection. ARC-062 proposes two policy heads with a learned context discriminator producing a soft gating weight in [0, 1] — that is an explicit dimensionality reduction on what the biology achieves with high-dim mixtures. The honest reading is: the SD-054 substrate is a 2-mode partition by *experimental construction*, so 2 heads is the right Phase 1 commitment, but the caveat is load-bearing at Phase 4 / GAP-E in the cluster plan, where multi-strategy scaling tests ARC-062's ceiling. If multi-strategy scaling fails, Rigotti's biology says the missing capacity is *dimensionality at the gating substrate*, and ARC-063's distributed `CandidateRule` field with continuous tolerance gates is the natural successor architecture.

## What this means for R3 (gating site)

Indirect. Rigotti is a representational finding, not a site-selection finding. The mixed selectivity is observed in PFC; the paper does not compare against BG single-unit recordings or hippocampal preplay sequences. It strengthens R3-(iii) (PFC-side score_bias) as the substrate for the *integrative* function but does not exclude (i) and (ii) as parallel implementing sites. For ARC-062 architectural decisions, R3 is better arbitrated by Gurney/Humphries/Redgrave 2015 (BG-side), Pfeiffer & Foster 2013 (hippocampal preplay), and the Mansouri/Capkova 2025 lesion dissociation.

## Confidence reasoning

Source quality high — Nature paper, primate single-unit, theoretically rigorous, behaviour-predictive. Mapping fidelity is the binding factor: the paper supports R1 strongly and provides an R2 caveat, but it does not directly test ARC-062's specific architectural commitments. Transfer risk is moderate — the dimensionality argument generalises, but the specific behaviour-prediction signature (dimensionality collapses on errors) is task-dependent and not yet replicated in the SD-054 reef/forage discriminative-cut setting. Confidence 0.74 reflects: strong R1 support + meaningful R2 caveat - mapping_fidelity gap.

## Mixed-direction reasoning

This entry is `mixed`, not `supports` or `weakens`, because:
- It *supports* R1 (multi-stream integration is biologically primary).
- It *weakens* (mildly) the architectural commitment in R2 to discrete heads — the biology is continuous and high-dim.
- It is *neutral* on R3 site selection.

The cluster's pre-registered Phase 2 falsifier on SD-054 is unaffected (2 heads is the right Phase 1 commitment for the 2-mode substrate). The caveat is a Phase 4 / V4 flag, not a Phase 1 blocker. Captured in `failure_signatures` so a future GAP-E session has the diagnostic in hand.
