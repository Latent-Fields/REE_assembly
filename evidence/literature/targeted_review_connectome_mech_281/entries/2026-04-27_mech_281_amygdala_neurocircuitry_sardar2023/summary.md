# Sardar et al. 2023 -- Amygdala neurocircuitry at the interface between emotional regulation and narcolepsy with cataplexy

**Source:** *Frontiers in Neuroscience* 17:1152594. DOI: [10.3389/fnins.2023.1152594](https://doi.org/10.3389/fnins.2023.1152594) (PMID 37266541, PMC10230954).
**Cited via PubMed.**

## What the paper did

Sardar, Goldstein-Piekarski, and Giardino (Stanford Sleep and Circadian Sciences) wrote a synthetic review of the amygdala's contribution to narcolepsy with cataplexy. They draw together the rodent lesion and circuit-tracing literature (the Burgess line, the Hasegawa serotonin work, the BNST literature) with the small but growing human functional neuroimaging literature in narcolepsy. The framing is explicit: cataplexy is an emotional-regulation -> motor-coupling failure, and the amygdala is the most plausible interface where this conversion can break.

## Key findings

The review's contribution is to dissociate the amygdala into three structurally distinct contributions to the cataplexy circuit. The CeA carries the GABAergic projection to brainstem motor-tone nuclei (the Burgess pathway). The BLA encodes emotional-stimulus value and projects forward to CeA, supplying the trigger signal. The BNST (extended amygdala) contributes the slower context-and-state-modulated component, including the role of stress and arousal context. Across all three, orexin loss removes a key gain term that normally prevents emotional arousal from collapsing motor output. The review also flags that human functional imaging in narcolepsy with cataplexy is sparse but consistent with elevated amygdala activation around cataplexy episodes.

## How this maps to MECH-281

MECH-281 names BLA/CeA arbitration as a canonical downstream target of the orexin-analog gain. Sardar's framing extends this in a useful way: the relevant target is a small distributed subset of amygdala-family nuclei (CeA + BLA + BNST), not a single nucleus, and they each contribute a different functional component (motor-tone projection, value computation, state context). For the REE architecture, this suggests the override_signal does not modulate "amygdala" as a unit -- it modulates a specific arbitration computation that runs across these subnuclei. The qualitative prediction MECH-281 makes (loss of orexin-analog gain produces cataplexy-analog motor failure even when z_harm and drive_level compute normally) is consistent with the integrated picture Sardar lays out.

## Limitations and caveats

This is a review, so I treat it as supportive context, not confirmatory evidence. The specific quantitative claim MECH-281 commits to -- that override_signal scales the amygdala arbitration term in commit-gate threshold computations -- is not tested anywhere in the review. The human imaging evidence is sparse enough that the rodent-to-primate transfer remains an inference, not a demonstration. The review's value is structural: it confirms that the amygdala-circuit framing MECH-281 uses is consistent with current consensus, and it usefully widens the scope from CeA-only to the broader amygdala family.

## Confidence reasoning

I assign 0.7. Source quality is moderate (Frontiers, recent, Stanford group); mapping fidelity is high because the review's explicit thesis is the same emotional-regulation -> motor-coupling framing MECH-281 uses. Transfer risk is moderate (still mostly rodent). I rank this lower than Burgess because reviews aggregate rather than generate evidence, but it is more than 0.6 because the framework match is unusually clean.
