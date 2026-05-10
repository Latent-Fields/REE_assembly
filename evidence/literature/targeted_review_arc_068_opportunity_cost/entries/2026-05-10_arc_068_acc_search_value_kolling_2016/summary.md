# Kolling, Behrens, Wittmann & Rushworth 2016 -- Multiple signals in anterior cingulate cortex

**Citation:** Kolling N, Behrens T, Wittmann MK, Rushworth MFS. Multiple signals in anterior cingulate cortex. *Curr Opin Neurobiol*. 2016;37:36-43. PMID: 26774693. [DOI](https://doi.org/10.1016/j.conb.2015.12.007).

## What the paper does

Kolling et al. write a synthesis review arguing that the apparent paradox of anterior cingulate cortex tracking BOTH commitment-to-action AND exploration-of-alternatives dissolves once one recognises that dACC carries multiple computationally distinct signals at once: a commitment / value signal, an explore / search signal, a belief-and-model-updating signal, and an environmental-average-value ('search value') signal. The review is in part a defence of the original Kolling et al. 2012 Science paper (PMID 22517861) against Shenhav et al.'s 2014 reinterpretation that the apparent foraging-value signal is actually choice-difficulty tracking. Critically for ARC-068, the review explicitly argues for the search-value scalar -- an average-value-of-current-environment metric that biases switching from the current option when its value falls below the environmental average. This is the architectural ancestor of SD-032b's existing foraging_value bundle component, and a close cousin of the long-run-avg-reward-rate scalar Niv 2007 derives for opportunity cost on rest.

## Why this matters for ARC-068

The R1 verdict (ARC-068 vs SD-032b boundary) rests on whether ARC-068's always-on cost-of-passivity computation is architecturally distinct from SD-032b's task-conditioned switch-when-current-option-bad computation. Kolling 2016 is the load-bearing literature anchor for the SD-032b side of this question. The paper's central claim -- multiple computationally distinct signals coexist in dACC -- LICENCES a clean architectural separation: even within the same neural substrate, the foraging-value computation is separable from the choice-difficulty computation AND from the model-updating computation. By extension, an always-on opportunity-cost-on-rest computation could plausibly be a separable signal that coexists with the current-environment foraging-value signal.

But the paper does not COMMIT to that separation. The 'search value' scalar Kolling formalises is current-environmental-average, not long-run-reward-history. ARC-068 (as registered) is closer to Niv's long-run kernel; SD-032b is closer to Kolling's current-environmental kernel. R2 (reward-rate kernel) verdict: PRIMARY recommendation is the long-run EMA (Niv 2007) for ARC-068; SECONDARY fallback is the current-environmental average (Kolling 2016) which is what SD-032b already uses. The two kernels predict different behaviour in changing environments: a Niv-kernel agent retains opportunity-cost pressure even after a sharp drop in environmental reward, whereas a Kolling-kernel agent's pressure adjusts faster.

For the R1 verdict, the recommendation is: separate ARC-068 from SD-032b at the architectural level, but acknowledge that the biology probably implements them on overlapping substrate (Kolling's multi-signal view). The clean architectural separation IS a design choice rather than a strict biological commitment, and the synthesis must say so.

## Caveats

The paper is a REVIEW, not a primary mechanistic study. Its central claim (multiple signals in dACC) is itself contested. Shenhav et al. 2014 (Nature Neuroscience) and Shenhav et al. 2016 ([DOI](https://doi.org/10.3758/s13415-016-0458-8), PMID 27580609 -- separate entry) argue that what Kolling reads as foraging-value tracking is better described as choice-difficulty tracking, with appropriate methodological corrections. The R1 verdict cannot lean on Kolling alone; the synthesis must explicitly engage the Shenhav counter-position.

A second caveat: the original empirical evidence is Kolling et al. 2012 Science (PMID 22517861), which I have not retrieved as a separate entry in this pull because the 2016 review is the load-bearing synthesis statement. A future pull on the dACC foraging-value substrate (likely commissioned by SD-032b directly) would benefit from the 2012 primary paper as a separate entry.

A third caveat: the 'search value' scalar is silent on the WHEN-WANTING-IS-ABSENT regime that ARC-068 most cares about. Kolling's task is foraging between alternatives; ARC-068 fires when no specific alternative is wanted. The scalar architecture transfers (an environmental-average computation can be done with no specific target in scope), but the empirical evidence does not directly address that regime.

## Confidence reasoning

Source quality high for a review (Curr Opin Neurobiol; principal authors are the Kolling lab). Mapping fidelity moderate-to-strong: the search-value scalar maps onto the ARC-068 commitment but at a different point on the kernel spectrum than the registered ARC-068 functional_restatement implies. Transfer risk moderate-to-high: human fMRI data, contested interpretation, the architectural separation between ARC-068 and SD-032b is partly a design choice. Direction `mixed` rather than `supports` because the multi-signal framing simultaneously LICENCES separation (different signals can coexist) AND undermines clean separation (they coexist on the same substrate). Aggregate 0.71.

According to PubMed, this paper appears under the cited PMID with the DOI as listed.
