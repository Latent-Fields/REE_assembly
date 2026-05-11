# Meder et al. 2017 — Simultaneous representation of a spectrum of dynamically changing value estimates

According to PubMed, [DOI 10.1038/s41467-017-02169-w](https://doi.org/10.1038/s41467-017-02169-w), PMID 29208968.

## What the paper did

Humans performed a probabilistic reversal-learning task in the fMRI scanner. The model-based analysis decomposed BOLD signal in four regions (dorsal anterior cingulate cortex, ventromedial prefrontal cortex, posterior cingulate, parietal cortex) into value estimates based on different timescales of recent experience — short-term, medium-term, longer-term. Each region held the full spectrum, but with different sub-regions weighted toward different timescales, organised as a systematic cortical gradient. Across the task, the relative weight of different timescales shifted as environmental statistics changed.

## Key findings relevant to Q-045

The dACC substrate is doing something computationally elaborate: it holds value at multiple recency timescales simultaneously, organised as a gradient, and dynamically rebalances which timescale drives current choice as the environment changes. The shorter-timescale estimates are exactly the ones that would need to be down-weighted when recency-bias is detected — Scholl 2015's anti-recency machinery would operate on this short-timescale representation. The Meder paper does not directly demonstrate the anti-recency gating, but it shows the substrate is COMPUTATIONALLY ELABORATE in a way that is incompatible with a uniform-noise-floor primitive.

## How this translates to REE

For Q-045 this paper supports the SUBSTRATE-DISTINCT verdict from a different angle than Scholl 2015. Scholl shows that dACC's anti-recency suppression is content-selective (the trial label gates it). Meder shows that dACC's value computation is multi-timescale-elaborate. Both arguments point at the same conclusion: dACC is not a uniform noise generator. Whatever MECH-260 (anti-recency penalty) is doing in REE, it is doing it inside a substrate that holds multi-timescale recency-weighted value, and the primitive is incompatible with collapse into MECH-313's noise-floor primitive.

For REE's implementation, Meder also raises a Phase-2 refinement question: should MECH-260 instantiate a single anti-recency timescale (current default) or a multi-timescale spectrum like Meder observes? A single timescale is more parsimonious and probably adequate for the 4-arm ablation question Q-045 asks. A multi-timescale spectrum would be a future architectural commitment if the 4-arm experiment shows partial-but-incomplete dissociation in patterns that suggest different timescale-specific failure modes. The current substrate-readiness diagnostic (V3-EXQ-544 already PASSed for MECH-313; equivalent for MECH-260 pending) does not test for multi-timescale structure. This lit-pull does not require that test to be added before the Q-045 4-arm runs — it surfaces the question as a Phase-2 refinement.

## Limitations and caveats

The paper does not directly demonstrate anti-recency suppression — that is Scholl 2015's contribution in this same pull. Meder shows multi-timescale value REPRESENTATION; the suppression of biased influence on choice is inferred. The fMRI BOLD analysis is correlational; the multi-timescale interpretation depends on the specific model-fit. The cortical-gradient finding is robust across the four regions but is finer-grained than REE currently models — REE's MECH-260 has no notion of sub-regional gradient organisation, only a single anti-recency mechanism in the dACC slot.

## Confidence reasoning

Confidence 0.79. Source quality high (Nature Communications, well-powered human fMRI, model-based with explicit timescale decomposition). Mapping fidelity moderate-strong on the substrate-distinctness argument that Q-045 actually needs. Transfer risk low (cingulate computational architecture is conserved across primate species). The direct relevance to MECH-260 specifically is by inference rather than direct demonstration, hence mapping_fidelity not higher than 0.74.
