# Durrant et al. 2011 -- Sleep-dependent consolidation of statistical learning

## What the paper did

Durrant and colleagues exposed adult participants to a continuous sequence of tones whose transitions followed a hidden Markov structure -- some tone-to-tone transitions were probable, others were rare, and the pattern was not signalled to the participants. After exposure, one group took a 90-minute afternoon nap (with EEG), one stayed awake, and a no-exposure control was included for baseline. At re-test, participants had to discriminate genuinely structured tone sequences from random ones. The nap group showed a clear post-sleep gain in discrimination; the wake group did not. The size of the post-sleep gain correlated positively with the duration of slow-wave sleep (SWS) the participant had during the nap.

The paper is small (n around 16 per condition) but tightly designed and the SWS correlation gives a direct neurophysiological hook for the behavioural effect.

## Key findings relevant to MECH-275

This paper supplies the empirical regularity-extraction arm of MECH-275: regularities present in the waking exposure are only partially registered at the time, and NREM sleep -- specifically the SWS phase -- stabilises and amplifies those regularities until they support discrimination behaviour at re-test. The mechanism is not generic post-rest improvement; the wake control did not show it. And the SWS-correlation localises it to the same NREM sleep phase that Lewis & Durrant's overlapping-replay theory names as the mechanism for cognitive schema construction.

For MECH-275, this is direct evidence that sleep does aggregate-and-extract regularities across waking traces in humans, with the right phase-of-sleep signature. It is the behavioural-and-EEG complement to the Lewis & Durrant theoretical paper and to the Tse et al. animal demonstration.

## How the findings translate to REE

The translation is at the level of mechanism existence: NREM sleep extracts regularities from prior waking exposure, in humans, with the SWS phase specifically responsible. MECH-275 inherits this and specifies the input type and the consumer architecture (E1 consolidation and SD-033a viability-map revision via the anchored channel).

## Limitations and caveats

There is one important tension. The regularities Durrant et al. test are correlational -- transitional probabilities between adjacent tones in a sequence. MECH-275 explicitly says that aggregation over correlational input alone should produce noise-fit, not schema revision; the input has to be counterfactual-backed (MECH-276's deliberate intervention loop) for the aggregation to be coherent. Durrant et al. demonstrate that the aggregation mechanism evidently does operate on correlational input -- which is in tension with MECH-275's stronger claim. The way MECH-275 has to read this paper is: yes, the mechanism operates on correlational input, but the output of doing so is shallow regularity-detection (which is what Durrant et al. measure -- structured-vs-random discrimination), not deep schema revision (which is what MECH-273 requires for self-model formation).

Other limitations: sample size is small, the task is narrow, and the integration arm of MECH-275 (whether the extracted regularities are then folded into prior knowledge structures) is not tested.

## Confidence reasoning

Confidence 0.69 -- supports MECH-275 on the regularity-extraction mechanism, with a load-bearing caveat about input type. Source quality solid (peer-reviewed Neuropsychologia paper with EEG-correlated behavioural effect). Mapping fidelity moderate because the input-type mismatch is real -- the paper supports the existence of the mechanism but is silent on the counterfactual-vs-correlational distinction MECH-275 makes the centrepiece. Transfer risk elevated because tone-sequence statistical learning is a long way from cross-domain Bayesian aggregation of attributions.
