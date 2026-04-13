# Popa et al. (2017) -- The Cerebellum: Adaptive Prediction for Movement and Cognition

## What the paper did

This review examines the cerebellum's role in adaptive prediction across both motor and cognitive domains. Working from a foundation of direct electrophysiological and neuroimaging evidence, the authors characterise the cerebellum's predictive mechanism and its temporal properties. They address both the classical sensorimotor forward model account and more recent proposals that the cerebellum performs prediction in cognitive and language domains -- which has been contentious, since those domains apparently require longer timescales than the millisecond-range corrections classically attributed to the cerebellum.

## Key findings relevant to MECH-070

The review provides a rare quantitative timescale claim: cerebellar predictive capabilities span "relatively short time intervals relevant for skilled movement (up to a second or so)." This is not just a qualitative characterisation -- the upper bound of roughly one second is stated explicitly. The paper further argues that temporal precision is a key characteristic distinguishing cerebellar from cortical processing. This is important: the cerebellum is described as particularly suited to short-horizon continuous prediction under tight temporal constraints, with the implication that longer-horizon planning is handled by structures outside the cerebellum. The paper notes that even cerebellar involvement in sequencing (e.g., language sequencing, cognitive tasks) may be decomposed into chains of short predictions rather than single long-horizon rollouts -- which is a different computational strategy from extended planning.

## How findings translate to REE

The evidence_quality_note for MECH-070 already documents the problem: EXQ-132 and EXQ-212 showed E2 degrading faster across horizons than E1, which is opposite to the claim. Popa et al. provide the biological grounding for why this experimental result is not a surprise. A cerebellar-analogue system operating under tight temporal constraints -- optimised for up-to-a-second prediction -- would be expected to degrade rapidly when asked to roll out 20-30 discrete steps. The original MECH-070 claim appears to have confused the rollout_horizon design parameter (E2=30 > E1=20) with a genuine claim about the natural operation of the biological system. The neuroscience, read carefully, places E2 as the short-horizon component and E1 as the longer-horizon one, not the reverse. This is consistent with the updated evidence_quality_note: E2's training horizon is 1-step (efference-copy forward prediction), separate from the rollout_horizon. The claim needs reformulating rather than defending.

## Limitations

The paper's upper bound of "a second or so" is for biological motor prediction in continuous time. It is not obvious how to translate this to discrete grid-world steps. If a step corresponds to 100 ms of real time, then the cerebellar analogue might span 10 steps -- which is non-trivial. The paper also notes cerebellar contributions to cognitive tasks, which complicates a clean short-horizon characterisation. And the "up to a second" bound may not apply to cerebellar computations embedded in cerebro-cerebellar loops involving cortex, which might effectively extend the horizon. These caveats prevent the evidence from being treated as definitive.

## Confidence reasoning

Confidence is 0.65 weakening. The source is high quality (Trends in Cognitive Sciences, direct electrophysiological backing). The quantitative timescale claim directly contradicts the direction of MECH-070 as originally formulated, and the experimental evidence already in the record (EXQ-132, EXQ-212) is convergent with this. The confidence is held below 0.70 because the timescale mapping from biological milliseconds to REE discrete steps is genuinely uncertain, and because the paper acknowledges cognitive extensions of cerebellar prediction that are not fully characterised. The direction of weakening is clear; the magnitude is uncertain.
