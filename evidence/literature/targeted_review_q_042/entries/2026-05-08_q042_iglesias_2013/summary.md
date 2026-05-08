# Iglesias, Mathys, Brodersen, Kasper, Piccirelli, den Ouden & Stephan 2013 — Hierarchical prediction errors in midbrain and basal forebrain during sensory learning

**Source:** Iglesias S, Mathys C, Brodersen KH, Kasper L, Piccirelli M, den Ouden HEM, Stephan KE. *Neuron* 80(2):519-530 (2013). [DOI](https://doi.org/10.1016/j.neuron.2013.09.009). PMID 24139048. According to PubMed.

## What the paper did

Iglesias and colleagues tested a specific theoretical claim: that prediction errors at different levels of a Bayesian hierarchy may be encoded by different neuromodulators. Healthy adults performed an audio-visual associative learning task while BOLD was recorded with fMRI. A hierarchical Gaussian filter (HGF) model decomposed each trial into a low-level prediction error (about whether the visual stimulus was the predicted one or not -- effectively an outcome PE) and a high-level prediction error (about whether the stimulus probability itself had changed -- effectively a volatility PE). They then asked which brain regions tracked each signal trial-by-trial. Low-level PEs were reflected in widespread visual / supramodal cortex but specifically also in midbrain BOLD. High-level PEs were reflected specifically in basal forebrain. Both signals were time-locked to outcome arrival -- the moment the cue revealed what actually happened. Replicated in two independent cohorts.

## Why it matters for Q-042

This paper is the cleanest empirical argument for Option A in Q-042 -- the precision-related update fires AT outcome time, downstream of action arrival. The high-level PE in basal forebrain is the most direct biological analogue of ARC-016's precision update: it tracks how surprising the just-arrived outcome was relative to the prior, and it modulates the agent's downstream learning rate / threshold-related variables. That signal is computed at outcome arrival, not at action selection. So if REE's running-variance update lives inside agent.update_residue() (post-outcome), it is biologically faithful to where the analogous neuromodulator signal actually fires.

The Iglesias result is critical context for Q-042 because it stops the question from collapsing entirely toward Option B. The combined picture from this lit-pull is: biology has both an action-selection-time gain broadcast (Aston-Jones LC phasic, Frank STN-preSMA threshold modulation, Schwartenbeck DA policy precision) AND a post-outcome PE update (Iglesias midbrain low-level + basal forebrain high-level). The two arms are computationally distinct: the early arm gates the choice itself, the late arm calibrates the model. ARC-016's running variance is closest to the LATE arm in the sense that it is a statistic accumulated over observed prediction errors -- it tracks how surprising the just-arrived outcomes have been. The action-selection-time signal that biology also runs is closer to a separate quantity (immediate confidence in the current policy) that REE may or may not need to model separately.

## Mapping to REE

The architectural recommendation that falls out of combining Iglesias with the other Q-042 entries: keep the running-variance update at outcome time, where it currently lives, AS the post-outcome arm; but consider whether REE separately needs a pre-commit confidence broadcast that consumes the *current* (pre-update) precision and gates the choice. The dual-update variant in Q-042's notes is what biology runs, and Iglesias is the empirical case for the late arm.

For the immediate Q-042 implementation question -- "should the running-variance update fire at action-selection time, at outcome-integration time, or both?" -- the Iglesias reading favours retaining the outcome-time update unconditionally. The action-selection-time work in the rest of this lit-pull argues for an *additional* pre-commit broadcast of the current value, not for moving the underlying statistical update earlier. That distinction (broadcasting vs updating) maps onto Option A retained, plus a structurally separate read-site at action selection that consumes the current value.

## Caveats

The neuromodulator assignments (DA = low-level PE, ACh = high-level PE) rely on indirect BOLD inference combined with the Yu-Dayan framework's pharmacological mapping; later work (Marshall 2016 [DOI](https://doi.org/10.1371/journal.pbio.1002575)) complicates the clean assignments. The audio-visual learning task is narrow -- the strong claim about hierarchical PE timing may not generalise to all decision domains. The paper does not address what fires AT action selection at all, so it does not directly speak to Option B; the take-away is specifically about the *late* timing arm.

## Confidence reasoning

0.74 supports for Q-042. Source quality high (0.85, Neuron, replicated across two cohorts, methodologically careful Stephan-lab work). Mapping fidelity high (0.74) -- the high-level PE in basal forebrain is the closest available biological analogue of ARC-016's precision update. Transfer risk low-moderate (0.27) -- the post-outcome timing claim transfers cleanly even though the specific neuromodulator assignments are contested. Direction is supports for *retaining* Option A; combined with the action-selection-time entries, the overall lit pattern is the dual-update reading.
