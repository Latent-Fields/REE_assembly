# Scholl et al. 2015 — The Good, the Bad, and the Irrelevant

According to PubMed, [DOI 10.1523/JNEUROSCI.0396-15.2015](https://doi.org/10.1523/JNEUROSCI.0396-15.2015), PMID 26269633.

## What the paper did

Human participants performed a reward + effort learning task on two options over many trials. On each trial the reward outcome was randomly labelled REAL or HYPOTHETICAL. The labelling was informationally irrelevant for the longer-term value of each option (which depended on the magnitude, not the label) but participants showed an irrational bias to repeat choices that had just produced a real reward. The model-based fMRI design decomposed the BOLD signal into a bias term (the influence of the irrelevant real/hypothetical label on next-trial choice) and an anti-bias term (the degree to which the participant resisted that influence).

## Key findings relevant to Q-045

Amygdala and ventromedial prefrontal cortex activity tracked the irrational bias — these substrates represented the influence of recent real-reward labels on subsequent choice. In striking contrast, dorsal anterior cingulate cortex, frontal operculum / anterior insula, and especially lateral anterior prefrontal cortex activity tracked the SUPPRESSION of that bias — the degree to which participants resisted the irrelevant signal and chose based on aspects of outcomes that had sustained relationships with the underlying option values. The authors describe this as "suppressing irrelevant reward information for more optimal learning and decision making." That sentence is the substrate-level statement of MECH-260's architectural commitment in REE: a dACC layer that can SELECTIVELY suppress the influence of recently-rewarded-but-informationally-irrelevant trials on future value updates.

This recovers the MECH-260 anchor citation that was flagged as missing in the arc_065 Pull 1 synthesis on 2026-05-10 ("Citation lookup was ambiguous and the specific dACC-anti-recency-suppression Scholl paper was not retrieved in this pull"). The Scholl 2015 J Neurosci paper is now retrievable and matches both the Scholl-as-first-author and the dACC-anti-recency-on-vmPFC-bias content that MECH-260 was registered against.

## How this translates to REE

For Q-045 this paper anchors the SUBSTRATE-DISTINCT side of the question. Q-045 asks whether MECH-313 (LC-NE tonic noise floor) and MECH-260 (dACC anti-recency penalty) are independent parallel substrates or whether they collapse. Scholl supplies content-specific evidence that dACC's contribution is NOT noise-like: it is selective for which reward signals propagate to choice, content-conditional on the trial-feature labelling. A noise floor (MECH-313's primitive) is content-uniform by construction — it perturbs all features equally. A content-selective anti-recency gate (MECH-260's primitive) is a computationally distinct primitive that adds information the system did not previously have, namely a discrimination between informative and uninformative reward signals. The two cannot collapse into one substrate because they instantiate different computational primitives.

Combined with the Tervo 2014 Cell finding (LC → ACC directional coupling), the architectural reading for Q-045 is COUPLED-NOT-COLLAPSED: MECH-313 and MECH-260 are substrate-distinct (Scholl) and circuit-coupled (Tervo). The 4-arm ablation registered against Q-045 should test this dissociation by predicting different behavioural signatures from 313-only and 260-only, not just different magnitudes of the same effect.

## Limitations and caveats

Scholl's anti-recency is GATED by an explicit task label (real vs hypothetical); REE's MECH-260 is currently conceived as gated by an internal recency-detection signal without a content label. The mapping is to the COMPUTATIONAL PRIMITIVE that dACC can suppress reward-signal influence on choice in a content-selective way, not to the specific gating condition. Whether REE's recency-detection signal can play the gating role Scholl's task-label plays is an architectural follow-on this lit-pull surfaces as a refinement to MECH-260's implementation notes — not a current substrate gap. The fMRI BOLD inference is correlational; the companion Kennerley 2006 lesion paper (in this same pull) supplies the causal link for the ACC → choice direction.

## Confidence reasoning

Confidence 0.82. Source quality high: J Neurosci, well-powered human fMRI, model-based design with an explicit anti-bias contrast that maps directly onto MECH-260's primitive. Mapping fidelity strong on the primitive (content-selective anti-recency suppression by dACC). Transfer risk low because cingulate computational architecture is conserved across primate species. This is the load-bearing dACC anchor for both MECH-260 (substrate-level identification) and the SUBSTRATE-DISTINCTNESS side of Q-045 (content-selectivity argument against collapse with MECH-313).
