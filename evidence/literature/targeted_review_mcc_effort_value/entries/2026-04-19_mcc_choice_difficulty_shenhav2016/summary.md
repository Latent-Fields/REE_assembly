# Shenhav, Straccia, Botvinick & Cohen 2016 — dACC and vmPFC have inverse roles in both foraging and economic choice

**Source:** *Cognitive, Affective & Behavioral Neuroscience* 16(6):1127-1139, [10.3758/s13415-016-0458-8](https://doi.org/10.3758/s13415-016-0458-8). Via PubMed (PMID 27580609).

## What the paper does

Shenhav et al. re-analyse the Kolling, Behrens, Mars & Rushworth (2012) foraging paradigm with (a) a larger sample, (b) methodological fixes for choice biases, and (c) an extended range of foraging values. They find that dACC activity in the original Kolling paradigm is better accounted for by *choice difficulty* (how closely valued the alternatives are) than by *foraging value per se*. Critically, they also show that the same inverse dACC-vmPFC pattern appears in *both* foraging and economic choice regimes, arguing against the Kolling hypothesis that these are distinct choice circuits. The paper positions this against the Expected Value of Control framework (Shenhav/Botvinick/Cohen 2013, separate entry) as evidence that dACC does one thing — evaluate the control needed for this choice, regardless of whether the choice is framed as "search vs engage" or "compare two options".

## Key findings relevant to the claim

- **dACC activity correlates with choice difficulty across both foraging and economic regimes.** The same regressor (value difference between alternatives, inverted) explains activity in both paradigms.
- **Kolling 2012's foraging-value signal is partly an artefact of how the value range was distributed.** With a broader value range and bias corrections, the foraging-specific signal collapses.
- **Foraging and economic choice are NOT supported by distinct circuits.** The original Kolling dissociation does not replicate with more careful methodology.
- **vmPFC tracks value of the chosen option invariantly.** This part of the Kolling finding survives the re-analysis.

## How this maps onto REE (the translation)

This paper is the disciplinary counter-weight to Kolling 2012. It forces SD-032b's output specification to include a choice-difficulty / decision-entropy signal alongside the mode-value signal. Concretely: the dACC-analog should emit at least

- `mode_values[M]` — expected net value of each candidate mode M (EVC-style or Kolling-style)
- `mode_choice_difficulty` — a function of how tightly clustered the mode values are (e.g., entropy of softmax(mode_values) or variance of the top-k)

The salience-network coordinator (SD-032a) should then use both: it switches mode when one mode clearly dominates (low difficulty + large EV gap) and holds the current mode when alternatives are closely tied (high difficulty). This is the biological solution to a genuine computational problem: you do not want a trigger-happy switch that abandons the current commitment on every momentary z_harm_a spike when the alternatives are only marginally better.

For MECH-259 (mode-switch threshold), this suggests the threshold should be *adaptive* — higher when difficulty is high (stick with the current mode when alternatives are ambiguously better), lower when difficulty is low (switch readily when a mode is obviously better). Implementing MECH-259 as a fixed numeric threshold would fail to capture this.

For MECH-260 (bias suppression against monostrategy), this paper actually provides support: a monostrategy agent would show chronically low *mode_choice_difficulty* (because only one mode ever gets serious evaluation), which in a biological system would mean dACC activity drops over time as the agent commits harder. The therapeutic signature of breaking monostrategy is specifically an *increase* in dACC-analog activity as alternative modes re-enter the evaluation.

## Limitations and caveats

The Shenhav vs Kolling debate is genuinely unresolved. The Kolling lab has published responses defending the foraging-value interpretation (see Kolling et al. 2016 Nature Neurosci and follow-ups), and the two labs have run parallel experiments with different conclusions. The methodologies differ enough that it is not obvious which interpretation wins. The fair reading is that dACC probably reflects both foraging-value and choice-difficulty, and these are correlated in most experimental paradigms to the point where dissociating them requires specifically designed experiments that neither lab has yet definitively run.

For ree-v3 the practical implication is pluralistic: SD-032b should emit multiple signals and the substrate should not be committed to a single interpretation. This is architecturally more conservative but also more expensive; we should flag this as a design-choice-to-be-validated rather than a settled specification.

The paper is human fMRI. Whether the same dACC computation runs in a closed-loop embodied agent remains a transfer risk.

## Confidence reasoning

0.76. Solid methodology directly engaging a canonical Kolling result. Lower than the Kolling 2012 paper not because the work is weaker but because its claim is essentially negative ("the original interpretation does not hold up") and the affirmative interpretation (choice-difficulty) is itself one of several competing accounts. Critical value for SD-032b design because it forces the dACC-analog to output multiple signals rather than one. Transfer risk moderate; debate is unresolved.
