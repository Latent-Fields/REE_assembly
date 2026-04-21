# Tang, Shin, Frank & Jadhav (2017) — "Hippocampal-Prefrontal Reactivation during Learning Is Stronger in Awake Compared with Sleep States"

**Journal of Neuroscience** 37:11789–11805. [DOI](https://doi.org/10.1523/JNEUROSCI.2291-17.2017). PMID 29089440.

*(According to PubMed.)*

## What the paper does

The authors recorded simultaneously from hippocampal CA1 and medial prefrontal cortex in rats learning a spatial alternation task, and compared how replay-during-SWRs differed between the awake and sleep states. Their central question: do awake SWRs and sleep SWRs play the same role in memory, or are they suited to different functions?

What they found is a striking asymmetry. Awake SWRs produced higher-fidelity reactivation of behavioural experience. CA1–PFC synchronisation was stronger during awake SWRs. Spatial reactivation — measured both pairwise and by ensemble decoding — was more structured in awake than in post-task sleep SWRs. And crucially, this enhancement was most prominent during initial learning in a novel environment, not during well-practised behaviour. Sleep SWRs, by contrast, showed lower-fidelity reactivation but coupled more tightly with cortical delta and spindle oscillations — a signature the authors interpret as integration across experiences rather than high-fidelity rehearsal of a specific one.

## Findings relevant to MECH-269

MECH-269 predicts that the hippocampal proposer's anchor eligibility — whether a given starting state is trustworthy enough to roll forward from — is context-dependent. Anchored-mode proposals should dominate when the currently observed latent is well-aligned with recent realised experience; probe-mode proposals should dominate when the agent is exploring poorly-modelled territory.

Tang et al. do not test per-stream verisimilitude directly, but they do demonstrate that reactivation quality is state-modulated in exactly the shape MECH-269 requires. High-fidelity, content-specific, CA1-PFC-synchronised replay appears preferentially under conditions where one would expect the hippocampal representation to be a trustworthy anchor — during awake active behaviour, during early learning when the representation of the environment has just been stabilised. Lower-fidelity, more integrative replay appears during sleep when the relevant content is being reorganised rather than rehearsed.

This is consistent with the architectural shape MECH-269 predicts, without being a direct test of it.

## How it translates to REE

Two translations are worth noting. First, the paper supports the specific MECH-269 prediction that anchored replay should dominate during high-fidelity, active moments — awake behaviour is one operationalisation of "I currently have a well-aligned latent state." The mapping onto REE is: anchored-mode proposals reaching the SD-033a lateral-PFC-analog consumer correspond to what Tang et al. observe as awake, high-synchrony CA1–PFC SWR reactivation.

Second, this paper is usefully dual-coded. The awake-vs-sleep asymmetry also bears on MECH-271, because the different states engage different downstream consumers. Awake SWRs with their tight CA1–PFC synchronisation are the anchored-destination (consolidation, viability map) mode; sleep SWRs with their different coupling are closer to what MECH-271 would predict for the reorganisation side of the routing distinction.

## Limitations and caveats

The awake–sleep axis is not the anchor–probe axis. MECH-269's within-context anchor/probe split says that at any given moment, some of the hippocampal output is trustworthy-anchored and some is deliberately-seeded probe — it is a decomposition within a single window, not across major brain states. Tang et al. report an across-state difference in replay quality, which is compatible with the within-state prediction but does not test it.

The rodent spatial-alternation paradigm is a narrow task slice. REE's per-stream decomposition — z_world vs z_self vs z_harm_s — does not have a clean rodent analogue in this study. The translation from "reactivation of a spatial trajectory in a W-maze" to "per-stream verisimilitude-gated anchor selection" is an interpretive step that the source does not take.

Awake SWRs may be higher-fidelity simply because the CA1 representation of the just-experienced trajectory is still in spiking memory — a retrieval-window effect that need not imply per-stream verisimilitude gating.

## Confidence reasoning

Source quality is strong — J Neurosci, Frank lab, rigorous simultaneous multi-site recordings, thoughtful analytical controls. Mapping fidelity is moderate: the paper demonstrates state-modulated replay quality in a shape consistent with MECH-269, but does not test the specific per-stream verisimilitude claim. Transfer risk is the main discount. Net confidence 0.68.
