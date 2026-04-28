# Spellman et al. 2015 — Hippocampal-prefrontal input supports spatial encoding in working memory

According to PubMed: Spellman, Rigotti, Ahmari, Fusi, Gogos & Gordon. *Nature* 522:309-314 (2015). [DOI 10.1038/nature14445](https://doi.org/10.1038/nature14445). PMID 26053122.

## What the paper did

Mice ran a delayed non-match-to-sample T-maze task. The authors used phase-specific optogenetic silencing to dissociate the cue-encoding, maintenance, and retrieval phases of spatial working memory, while recording mPFC single units and dual-site LFP. The intervention silenced direct ventral CA1 → mPFC afferents during one phase at a time.

The key finding is a clean temporal dissociation: silencing the vCA1 → mPFC pathway during the encoding phase abolished accurate cue representation in mPFC and impaired behavioural performance. Silencing during the delay (maintenance) or choice (retrieval) phases did neither. The cue-related signal in mPFC was carried by individual PFC units whose tuning depended on HPC input only during encoding. Gamma-frequency synchrony between the two structures was the candidate temporal coordination signal.

## Why this matters for REE's question

The REE question is whether frontal subdivisions consume rich associative goal content from a posterior store via top-down query (the user's "z_goal as a key into E1" intuition), or whether they hold a compact goal handle directly. Spellman 2015 says the answer is **phase-dependent**: at the moment of encoding, mPFC reads rich content out of vHPC; once cached, it maintains and retrieves locally without further HPC traffic.

That maps onto REE V3 cleanly. The right architectural interface is not a continuous z_goal-keyed query into a rich associative store. It is an **event-gated write** that takes the LatentStack contents at goal-instantiation time, transfers them through a high-bandwidth gamma-coherent window into a frontal-resident representation (SD-033a rule_state, SD-033b state_code, the existing ARC-035 vmPFC content interface), and from then on the frontal substrate carries the representation under its own dynamics. The boundary-event machinery in MECH-288 and the SD-039 anchor goal-payload population layer are already shaped roughly correctly for this — both fire at goal-creation moments.

## What it does NOT settle

The paper studies spatial cues, not abstract task-relevant goals. REE's z_goal in SD-015 is location-invariant; whether the encoding-only-dependence generalises from grid coordinates to the resource-encoder latent is not directly established. The "hippocampus" in this paper is dorsal CA1; REE's ResidueField + AnchorSet machinery is closer to ventral HPC + EC functional territory, where the connectivity to mPFC is heavier and more reciprocal (Hallock 2016 covers that route). And the paper does not subdivide PFC — it speaks of mPFC monolithically — so it cannot directly say whether SD-033a (lateral-PFC analogue, rule-holding) and SD-033b (OFC analogue, outcome-prediction) consume HPC input on the same schedule or with different gating.

## Confidence reasoning

I sit this at 0.82. The encoding-vs-maintenance dissociation is the architecturally informative finding and it is empirically clean — Nature-grade methodology with phase-specific optogenetics, single-unit decoding, and gamma-coherence corroboration. Source quality 0.90. Mapping fidelity 0.70 because the spatial-cue-to-abstract-goal generalisation is implicit. Transfer risk 0.30 because Ito 2015 (in the same review) shows the same circuit operating at trajectory-level abstraction, which mitigates the species/task-specific worry.
