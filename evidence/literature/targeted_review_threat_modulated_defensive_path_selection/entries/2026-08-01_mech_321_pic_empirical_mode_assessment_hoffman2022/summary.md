# Hoffman, Trott, Makridis & Fanselow 2022 -- Anxiety, fear, panic: assessing the defensive behavior system across the predatory imminence continuum

**Source**: Hoffman AN, Trott JM, Makridis A, Fanselow MS (2022). *Learning & Behavior* 50(3):339-348. [DOI 10.3758/s13420-021-00509-x](https://doi.org/10.3758/s13420-021-00509-x). PMID 35112315, PMC9343476.

## What the paper did

This is a direct empirical test, in mice, of whether the Predatory Imminence Continuum's three defense modes (pre-encounter/anxiety-like, post-encounter/fear-like, circa-strike/panic-like) are genuinely dissociable rather than a single graded response wearing three theoretical labels. The authors built a dedicated behavioral battery for each mode -- open-field locomotor velocity for anxiety-like behavior, freezing to a discrete footshock-paired cue for fear-like behavior, and acoustic-startle/activity-burst reactivity for panic-like behavior -- and asked whether a single acute stressor (a series of unsignaled footshocks) would move all three, and whether the three measures track together or independently.

## Key findings relevant to the claim

Stressed mice showed increases in all three measures relative to controls: reduced open-field velocity (more anxiety-like), more freezing to a subsequent footshock-paired cue (more fear-like), and a more robust startle/activity-burst response to white noise (more panic-like, i.e. more circa-strike-like). The three measures are independently operationalized and were separately assessed rather than collapsed into one score, and the paper explicitly frames this as evidence that the PIC's three modes are separable behavioral constructs that can each be probed and modulated.

## How this translates to REE

This paper supplies the empirical backbone for the theoretical claim in the companion Fanselow & Hoffman 2024 entry: the PIC's modes are not just a narrative convenience, they are measurably dissociable in behavior. For the SD-hazard-aware-policy-decomposition design question, this argues that a harm-valence-weighted selection step should be evaluated (and probably built) to reproduce qualitatively distinguishable selection PATTERNS at different `z_harm_a` regimes, not merely a single continuously-scaled output. It also flags a real subtlety: an acute stress/elevated-threat-baseline condition raised ALL THREE modes together here, rather than sharpening the distinction between them -- a caution that if REE ever adds something like a running or baseline harm-exposure signal alongside the instantaneous per-tick `z_harm_a`, it should be checked that this raises response magnitude without collapsing mode/regime SELECTIVITY.

## Limitations and caveats

The manipulation is acute stress (a footshock series), not a direct trial-by-trial manipulation of predator proximity or imminence -- so this paper demonstrates the modes are dissociable and jointly stress-modulated, but the imminence-to-mode gradient itself is evidenced elsewhere in this pull (the PIC theoretical entries, and Mobbs et al. 2007's human fMRI imminence manipulation). It is rodent-only, and the mapping from a mouse behavioral battery to REE's abstract `z_harm_a` scalar and its downstream tile-selection step is structural analogy, not quantitative calibration.

## Confidence reasoning

Solid, well-controlled behavioral study from the lab that originated the PIC framework, giving high source quality. Mapping fidelity is good for the "the modes are behaviorally real and separable" sub-claim this pull needed, somewhat weaker for the imminence-gradient question specifically. Confidence 0.78, reflecting strong support for the categorical-mode half of the design question with an acknowledged gap on direct imminence manipulation.
