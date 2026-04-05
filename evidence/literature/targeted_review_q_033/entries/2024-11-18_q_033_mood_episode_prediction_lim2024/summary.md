# Summary: Lim et al. 2024 — Wearable Sleep and Circadian Features Predict Mood Episodes

## Study Overview

Lim and colleagues followed 168 patients with mood disorders (bipolar I/II and major depression) in South Korea for a mean of 587 days, with wearable sleep-wake monitoring over approximately 267 of those days. From this data, they derived 36 features capturing aspects of sleep timing, duration, regularity, and circadian rhythm, then built machine learning models to predict whether a patient would experience a mood episode on the following day. The resulting performance figures were striking: AUCs of 0.98 for manic episodes, 0.95 for hypomanic episodes, and 0.80 for depressive episodes.

## The Key Predictive Feature

The most important predictive signal was not total sleep time but daily circadian phase shifts. Phase delays — the body clock drifting later — preceded depressive episodes; phase advances — drifting earlier — preceded manic episodes. This directional specificity is the finding most relevant to Q-033: the sleep-phase signal does not merely distinguish sick from well, but carries information about the type of decompensation that is approaching. Total sleep time lacks this polarity; a patient sleeping too little could be heading into mania or depression depending on the circadian context.

## Relevance to Q-033's Specificity Hypothesis

Q-033 asks whether a sleep-phase sufficiency index, combined with waking error burden estimates, can predict decompensation type and timing with better specificity than total sleep time alone. This study provides a partial existence proof: wearable circadian features already outperform total sleep time in episode-type discrimination, without any additional error burden signal. The implication is that Q-033's more complex mismatch index — adding a waking-load component to the sleep-phase component — has a reasonable prior for providing additive information, particularly for timing precision (days or weeks ahead rather than next-day).

## What the Study Does Not Show

The prediction horizon is one day, not the multi-week clinical decompensation window Q-033 envisions. The model does not include any estimate of waking prediction error load or homeostatic demand — the component that makes Q-033's mismatch index conceptually distinct. And while mood disorder broadly maps onto psychiatric decompensation, Q-033 extends to cognitive decline, making the generalisability question open. There is also a question of whether AUCs this high will survive replication in Western, more heterogeneous clinical cohorts.

## Honest Assessment

This paper is the strongest single piece of existing evidence that the core intuition behind Q-033 is tractable: sleep-phase signals from wearables carry episode-type information that cruder duration metrics do not. The gap between this paper and Q-033 is the mismatch architecture — the question of whether adding an explicit waking error burden estimate to the phase index genuinely improves on what phase alone can achieve. That gap is exactly where Q-033 sits as an open question.
