# Neural responses to monetary incentives in bipolar disorder (Johnson et al. 2019)

## What the paper did

Johnson, Mehta, Ketter, Gotlib and Knutson (NeuroImage Clinical 2019) ran fMRI MID in 24 remitted bipolar I participants and 24 age- and gender-matched controls. The contrast of interest was NAcc activity during gain anticipation, with Positive Urgency (a trait measure of impulsive responses to positive emotions) as a candidate mediator of bipolar-related differences.

## Key findings relevant to the SD-014 question

Remitted bipolar participants showed blunted NAcc activity during anticipation of monetary gains, relative to controls. Critically, this blunting did not directly correlate with bipolar diagnosis once Positive Urgency was entered into the model — Positive Urgency statistically accounted for the bipolar-vs-control difference. Individuals with high Positive Urgency, regardless of bipolar diagnosis, showed blunted NAcc anticipation. The interpretation is that the trait dimension of impulsivity-in-response-to-positive-emotion is the locus of variation, and bipolar I diagnosis is one population that loads heavily on this trait.

For SD-014 this is the clinical-anchor evidence for VALENCE_EXCITEMENT. Bipolar mania is, phenomenologically, hyperexcitement: individuals in mania experience amplified anticipatory positive arousal, racing thoughts, goal-directed activity scaling out of regulatory bounds. The blunting in remission is consistent with a homeostatic over-correction following manic episodes — a representation of "anticipatory positive arousal" that is hyper-active during mania and dampened during recovery.

REE adopting VALENCE_EXCITEMENT as a channel would acquire the representational machinery to model bipolar-like trait variation. Specifically: an agent with elevated VALENCE_EXCITEMENT amplitude (perhaps via amplified MECH-216 schema-readout writes to the channel) would exhibit mania-like over-amplification of anticipatory arousal at cues; an agent with blunted writes would model the remitted phenotype. This is forward-looking — REE is not currently modeling bipolar — but having the representational expressiveness is the architectural payoff.

## How this maps to REE

The bipolar Positive Urgency mediation is the load-bearing piece for thinking about VALENCE_EXCITEMENT as a *trait-modulated* channel rather than just a state-coded write. In REE, this would mean the gain (write strength) on VALENCE_EXCITEMENT updates could be a per-agent parameter, varying across what we might think of as REE temperament types. That is a substantial architectural commitment but it is consistent with the clinical literature.

## Limitations and caveats

Sample size moderate (n=24 / n=24); remitted not active mania (so the pathological-amplification phenotype is not directly observed); Positive Urgency is a self-report trait scale with the usual psychometric caveats. The translation to REE assumes future interest in clinical phenotype modeling, which is V4-or-later scope.

## Confidence reasoning

0.74. Recent clinical fMRI source, novel mediation finding, but indirect support for the SD-014 architectural decision. Strongest contribution: anchors VALENCE_EXCITEMENT to a clinical phenotype (mania) whose phenomenology demands a "high-arousal positive anticipation" representation that the existing 4 channels cannot capture.

Source: PubMed via PMID 31670069. [DOI](https://doi.org/10.1016/j.nicl.2019.102018).
