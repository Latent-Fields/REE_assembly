# Learning Representations for Pixel-based Control: What Matters and Why? (Tomar, Mishra, Zhang & Taylor, 2021)

## What the paper did, and why it is here

This entry is the deliberate counterweight. The other four in this pull all push in one direction -- that a task-agnostic objective will not select decision-relevant structure -- and a pull that only assembles agreement is not evidence, it is advocacy. Tomar and colleagues re-evaluate the representation-learning methods for pixel-based control under background distractors and report a set of mostly *negative* findings about the field, including about the two methods this pull otherwise leans on.

Their baseline is deliberately austere: reward prediction plus latent transition prediction, with "no metric-based learning, no data augmentations, no world-model learning, and no contrastive learning". It matches or beats the more elaborate methods. Around it they report that adding DBC's bisimulation metric *degrades* performance relative to omitting it; that contrastive losses add nothing when a supervised loss is available; and that most of the benefit of crop augmentation "is an artifact of how the benchmark environments save data".

## The moderator, stated almost in SD-106's terms

The sentence that earns this entry its place:

> "Pixel reconstruction is a sound technique in the absence of clutter in the pixels, but suffer massively when distractors are added."

That is the conditional the whole pull actually turns on, and it reframes SD-106's open question. The live issue is not "generic or task-conditioned?" in the abstract -- it is **how much of REE's observation-stream variance is task-irrelevant?** Where clutter is absent, reconstruction is a sound technique and SD-106's design is not condemned by any general principle. Zhang et al. supply the same moderator from the other side (a reconstruction method wins in their default, distractor-free setting), and Fu et al. supply its dose-response (the gap widens monotonically as distractors accumulate). Three independent sources, one moderator.

The paper also generalises the point into a methodological warning that applies to REE reading it as much as to the methods it evaluates:

> "finer categorization of benchmarks on the basis of characteristics like density of reward, planning horizon of the problem, presence of task-irrelevant components, etc., is crucial in evaluating algorithms."

SD-106's rung has not been characterised on any of those three axes.

## What follows for REE

This is the entry that converts the pull from an opinion into a test. If the moderator is what decides whether a generic objective is adequate, then the next thing to do is *measure the moderator*, not swap the objective. That is available cheaply and at the encoder plane: the subspace-overlap probe already offered as V3-EXQ-1041's second fan-out axis -- principal angles between the SD-106 code and PCA-32 on the same P0a buffer, reported beside the existing post-hoc R^2 -- is a direct read on whether the retained directions are the decision-relevant ones, and it needs no consumer-rung run at all.

It also warns against the obvious successors. Both task-conditioned methods in this pull are reported here to underperform a much simpler reward-plus-transition-prediction target. Choosing a DBC- or TIA-shaped objective for SD-106 by copying either paper would be selecting against this evidence.

## Caveats

Preprint-first and critical-re-evaluation in genre. Negative results about other groups' methods are exactly the kind that get contested, and nothing in this corpus independently verifies them; this entry establishes that the advantages of DBC and TIA are *not robust across benchmark characteristics*, not that those methods are wrong. Its own positive baseline again presupposes a reward signal at representation-training time, which SD-106's P0 warmup under a RandomPolicy may not provide. And the distractors studied are literal image backgrounds on pixel benchmarks -- REE's observation stream is not pixels, so "clutter" has to be re-operationalised (as, for instance, the fraction of observation variance lying outside the oracle-action-relevant subspace) before the moderator can be read off for REE at all.

## Confidence

0.6, the lowest in the pull, and source quality at 0.6 is the reason -- preprint-first, critical genre, unverified negative claims. Mapping fidelity is nonetheless good at 0.7: the moderator it names is directly the quantity SD-106's open (a)/(b) discrimination turns on, and it is offered as a design axis rather than as a single benchmark result. Transfer risk 0.45 -- a finding about *when* a class of objectives wins travels better than a performance number, but "clutter" still needs redefining for a non-pixel stream.
