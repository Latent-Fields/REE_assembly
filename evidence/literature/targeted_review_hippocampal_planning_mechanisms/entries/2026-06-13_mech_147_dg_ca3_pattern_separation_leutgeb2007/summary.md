# DG/CA3 pattern separation (Leutgeb et al. 2007) — MECH-147

**Claim:** MECH-147 — DG-mediated pattern separation gates trajectory disambiguation: a dentate-gyrus-equivalent sparse layer must produce non-redundant encodings of similar z_world states before rollout proposals are generated.

## What the paper did

Leutgeb and colleagues recorded place-modulated granule cells in the dentate gyrus, and principal cells in CA3, while rats explored environments whose *shape* was gradually morphed between two familiar configurations. The question was where, along the entorhinal → DG → CA3 path, similar inputs become decorrelated. They found that even small changes in environment shape substantially altered the *correlation structure* of dentate granule-cell activity — the DG rapidly drove similar inputs apart by changing which cells were co-active. CA3, by contrast, decorrelated by a different route: when environments were made more different, CA3 *recruited new, non-overlapping cell populations* that the DG did not. The conclusion is a **dual mechanism** for pattern separation — coincidence-pattern change in the DG, and assembly recruitment in CA3.

## Why it matters for REE

This is the canonical primary evidence that a dedicated DG stage decorrelates similar inputs *before* the downstream associative network operates — exactly the ordering MECH-147 asserts (separate the seed before proposing rollouts). It directly supports the existence and placement of a separation layer upstream of trajectory generation.

The more interesting payload for the assembly plan is the **completion-set harvest**. The paper's dual mechanism makes explicit that DG separation does not act alone: CA3's recurrent recruitment is its structural counterpart, and the two together produce the usable decorrelation. CA3 is also the site of pattern *completion* (recurrent collaterals reconstructing a whole pattern from a partial cue). So a REE substrate that builds a DG-style sparse expander without an accompanying CA3-style recruitment/completion stage would implement only half of the circuit the biology describes — and would likely fail to deliver the property MECH-147 wants, because separation and completion are jointly tuned (over-separate and you lose generalisation; over-complete and you lose disambiguation). HPL-3 (the MECH-147 node) should therefore carry CA3 recurrent completion as a co-required partner, not an optional later addition.

## Caveats and confidence

The honest limit is the transfer. What is measured is decorrelation of a *spatial place code* under environment morphing; what MECH-147 ultimately wants is that decorrelating a *planning seed* reduces near-duplicate trajectory proposals. That downstream consequence — separation improving rollout diversity — is REE's forward inference, not a result in this paper. With that caveat, the evidence is strong and direct for the separation stage itself: a definitive Science result from the Moser lab, high methodological quality, with the mapping to REE's z_world seed clear at the representational level. Confidence 0.81 (supports), held just under the top band by the spatial-code → planning-seed transfer.

*According to PubMed.* Source: Leutgeb JK, Leutgeb S, Moser MB, Moser EI (2007), *Science* 315(5814):961–6. [DOI](https://doi.org/10.1126/science.1135801)
