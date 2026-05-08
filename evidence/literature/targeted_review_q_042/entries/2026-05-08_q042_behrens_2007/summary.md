# Behrens et al. 2007 — Learning the value of information in an uncertain world (Q-042 cross-reference)

**Source:** Behrens TEJ, Woolrich MW, Walton ME, Rushworth MFS. *Nature Neuroscience* 10(9):1214-1221 (2007). [DOI](https://doi.org/10.1038/nn1954). PMID 17676057. According to PubMed.

## Cross-reference note

This entry duplicates the Q-041 entry of the same paper (`../../targeted_review_q_041/entries/2026-05-08_q041_behrens_2007/`) but addresses Q-042 specifically. The Q-041 entry covers the supervisor-existence question; this entry covers the supervisor-timing question. Both readings arise naturally from the same empirical result.

## What the paper did

Recapped briefly: human subjects performed a probabilistic reward-learning task with periodic volatility shifts. A Bayesian observer model with explicit volatility tracking fit behaviour well. ACC BOLD signal at trial outcome tracked the trial-by-trial volatility estimate, and cross-subject variability in the ACC signal predicted cross-subject variability in learning rate.

## Why it matters for Q-042

The relevant detail for Q-042 is the BOLD timing. The ACC volatility signal is locked to OUTCOME response, not to cue or action onset. The trial-by-trial Bayesian update of the volatility estimate happens when the just-observed outcome is integrated, and the BOLD response in ACC tracks the magnitude of that update. This is direct evidence for Option A in Q-042: the precision-related (here: volatility-related) statistic is updated at outcome arrival, in the cortical region whose signal is downstream of and predictive of subsequent learning rate.

In the broader pattern of this Q-042 lit-pull, Behrens 2007 functions as cortical-level corroboration of Iglesias 2013's neuromodulator-level evidence. The high-level PE in basal forebrain (Iglesias) and the volatility-tracking signal in ACC (Behrens) are likely two sides of the same outcome-time update -- the basal forebrain ACh broadcast carries the high-level PE, ACC integrates it into the volatility estimate. Both fire at outcome time. Both supply downstream learning rate.

## Mapping to REE

The structural recommendation is the same one that fell out of Iglesias: the running-variance statistic in ARC-016 should continue to be updated at outcome time. That is when the underlying error-magnitude data becomes available, and that is where biology computes the analogous quantity. The case for an additional pre-commit broadcast of the current rv value (Option B retained on top of A) is what the action-selection-time entries (Aston-Jones, Frank, Schwartenbeck) argue for, but Behrens specifically supports keeping the *update* at outcome time.

The signal-variability point is also worth noting for REE. Cross-subject variability in ACC volatility signal predicts cross-subject variability in learning rate. Mapped to REE: cross-experiment variability in rv evolution should predict cross-experiment variability in BG commit-gate behaviour. That's a testable prediction REE could evaluate by comparing rv trajectories across the EXQ-475a / 483c / 490g / 471a / 524a retest cohort once it lands.

## Caveats

The 2007 paper's localisation of the volatility signal to ACC has been refined; later work places parts of the signal in basal forebrain (Iglesias 2013) and parts in dACC vs sgACC subregions (later HGF work). The 2007 paper does not directly compare outcome-time vs action-selection-time as alternative locations for the update; the inference that "the update happens at outcome" follows from the BOLD timing being outcome-locked, but the paper does not test the negative claim (no signal at action selection). So this entry is corroborating rather than dispositive for Q-042's timing question.

## Confidence reasoning

0.72 supports for Q-042. Source quality very high (0.88). Mapping fidelity moderate-to-high (0.70) -- the timing claim transfers cleanly, but for Q-042 specifically this paper is supplementary to Iglesias 2013 rather than the primary anchor. Transfer risk low-moderate (0.28). Direction is supports for *retaining* Option A. This entry exists to keep the lit-pull's evidence trail complete and to make explicit that the same empirical result anchors both Q-041 and Q-042 readings.
