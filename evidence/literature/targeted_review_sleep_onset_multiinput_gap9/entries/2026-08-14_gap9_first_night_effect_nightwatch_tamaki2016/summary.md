# Tamaki, Bang, Watanabe & Sasaki 2016 -- Night watch in one brain hemisphere during sleep

According to PubMed: Tamaki M, Bang JW, Watanabe T, Sasaki Y. *Current Biology* 2016;26(9):1190-1194. [DOI 10.1016/j.cub.2016.02.063](https://doi.org/10.1016/j.cub.2016.02.063) (PMID 27112296).

## What the paper did

Measured sleep in 35 human participants across two nights a week apart, combining polysomnography with magnetoencephalography and structural MRI, and probed with deviant auditory stimuli delivered to one ear or the other. The target was the long-known but unexplained **first-night effect**: people sleep poorly on their first night in an unfamiliar environment.

## Core finding

On night one, a network (default-mode) in **one hemisphere remained less deeply asleep** than the other during slow-wave sleep. Deviant stimuli presented to the less-sleeping hemisphere produced **more arousals and faster behavioural responses** than the same stimuli to the other side. The degree of asymmetry correlated with sleep-onset latency on night one. All of these asymmetries were **absent by night two**. The authors read this as a survival mechanism -- one hemisphere kept on watch in an unvetted environment.

## Why this matters for GAP-9

Two contributions, both supporting rather than primary.

**1. Partial sleep is not a bird-specific curiosity.** This is the human counterpart of Rattenborg 1999 (sibling entry), and it matters that it appears in a species with no unihemispheric sleep capability -- the asymmetry is graded depth, not a hemisphere staying awake. That strengthens the synthesis's claim that the risk response is *partial with a retained vigilance channel* rather than a permit/refuse decision, by showing the pattern survives in a brain organised like a mammal's.

**2. The operative variable is predictive, and it habituates.** Nothing threatening happened on night one; the environment was a sleep laboratory. What drove the vigilance state was **unfamiliarity** -- an expectation about unobserved risk -- and it **extinguished with experience** by night two. That is the signature of a predictive state being updated by evidence, not of a current-harm reading. Together with Loftus 2022 (whose baboons responded to location unfamiliarity in the wild), this is the second independent line of evidence that "safe enough to sleep" should key on predicted rather than current harm -- the organism-review Section 8 question.

The habituation is the detail worth carrying into any REE implementation: a novelty-sourced threat term that does not decay with repeated exposure to a region would reproduce the first night and get every subsequent night wrong.

## Where the paper's coverage ends

Laboratory novelty is a weak proxy for ecological threat -- no participant was in danger, and the generalisation to predation risk is the authors' interpretation rather than a measurement. The dependent variable is also sleep **depth asymmetry**, not sleep **onset**: the paper is mostly about how one sleeps in a novel place rather than whether one sleeps, though the correlation with sleep-onset latency gives it some purchase on the onset question. Its use here is therefore supporting; Loftus 2022 carries the primary weight for the predicted-harm argument. REE additionally has no hemispheric decomposition, so as with Rattenborg the mechanism does not transfer -- only the shape and the habituation dynamics.

## Confidence reasoning

Source quality 0.90 -- *Current Biology*, well-powered within-subject two-night design, and the behavioural readout (arousal latency to deviant stimuli on the vigilant side) makes the asymmetry functional rather than merely correlational. Mapping fidelity 0.82, reduced because the manipulation is novelty-in-a-lab rather than risk and the DV is depth rather than onset. Transfer risk 0.25. Confidence 0.87.

## Failure signatures for the cluster

1. **Non-habituating novelty term.** If REE adds a novelty or unfamiliarity term to sleep onset that does not decay with repeated visits to a region, Tamaki predicts the wrong dynamics -- the biological state extinguishes by the second exposure. Diagnostic: track the threat/novelty term's value in a fixed region across repeated visits; a flat trace is the signature.

2. **All-or-nothing response to novelty.** If the response to an unfamiliar region is a full sleep refusal rather than a reduction in depth or duration, that is the same boolean-shape error flagged by Rattenborg 1999, appearing on the novelty axis rather than the hazard axis.
