# van Tilburg & Igou 2017 — Boredom Begs to Differ: Differentiation From Other Negative Emotions

[DOI](https://doi.org/10.1037/emo0000233) · PMID 27709976 · *Emotion*

## What the paper argues

A multi-study empirical paper that asks whether boredom is a distinguishable emotion or just a flat label for low-engagement states. Across appraisal, action-tendency, and feeling dimensions, the authors compare boredom against sadness, anger, frustration, disappointment, and regret. Boredom emerges as empirically separable on a specific signature: mild negative valence, low arousal, low perceived challenge, low perceived meaningfulness. The action-tendency profile is the load-bearing distinctive: boredom motivates the re-establishment of *meaningfulness*, not generic stimulation. The combination of low-arousal-but-action-motivating is unusual and is the paper's main contribution.

## Why this matters for ARC-067

This is the load-bearing R1 paper for the *boredom-as-functional-emotion* reading and a key R5 anchor for the differentiation against anhedonia / abulia. ARC-067's pre-registered architectural shape needs three properties this paper directly constrains:

1. **Low-arousal aversive.** Boredom is empirically low-arousal, which means the ARC-067 output must NOT couple to the SD-037 broadcast-override / orexin-analog substrate (which is the high-arousal recruiter). Routing through z_harm_a is consistent with this — the affective harm stream can carry low-arousal aversive content without recruiting high-arousal escape.

2. **Action-recruiting despite low arousal.** This is the architecturally distinctive feature. Most low-arousal aversives (sadness, mild anhedonia) reduce action; boredom motivates action. ARC-067 must therefore couple low-arousal aversive *to* the E3 score-bias path that competes with positive valence, not to the broadcast-override path.

3. **Meaning-seeking, not stimulation-seeking.** This is the cleanest disambiguation against MECH-314a striatal novelty. Novel territory without engagement opportunity (passive watching of novel content, or being placed in novel surroundings without interaction) does not discharge boredom on van Tilburg's account. ARC-067's discharge condition therefore requires action that *re-engages meaningful pursuit*, not just action that produces novel input. This converges with Westgate & Wilson 2018 MAC and supports a two-channel implementation: engagement-rate channel + meaning-misfit channel feeding the same valence accumulator.

For the R5 anhedonia / abulia anchor: van Tilburg & Igou's distinguishing signature gives the diagnostic for what an ARC-067 ablation should look like. Ablation removes the meaning-seeking action-pressure, which is precisely what abulia / anhedonia produce clinically — the patient registers the absence of engagement but does not generate action-pressure to re-establish it.

## Limitations and confidence

The empirical methodology is self-report on hypothetical and recalled emotional episodes. The action-tendency claim is based on reported behavioural intentions, not measured behaviour. Transfer to embodied open-ended REE foraging carries the usual self-report-to-mechanism caveat — the construct differentiation establishes that boredom is empirically distinct in human concept-space, but the underlying substrate need not be cleanly partitioned in the same way. Confidence aggregate 0.74 — Emotion venue is APA flagship for emotion research; multi-study with appropriate appraisal-and-tendency methodology; modest transfer risk for the self-report-to-mechanism mapping.

## Failure signature it would falsify

An ARC-067 substrate that produces a high-arousal aversive will fail the differentiation against frustration and anger — both are engagement-failure signals but high-arousal. The boredom aversive must be specifically low-arousal-but-action-recruiting, an unusual combination. If the substrate's discharge condition is satisfied by any-stimulation rather than meaningful-stimulation, it will reproduce stimulation-seeking but not the meaning-seeking signature, which on van Tilburg's account is the diagnostic feature.
