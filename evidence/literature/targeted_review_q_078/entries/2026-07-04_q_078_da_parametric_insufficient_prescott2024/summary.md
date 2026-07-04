# Prescott et al. 2024 — parametric dopamine sweeps don't buy clean selection

According to PubMed. Source: Prescott TJ, Montes Gonzalez FM, Gurney K, Humphries MD, Redgrave P. "Simulated Dopamine Modulation of a Neurorobotic Model of the Basal Ganglia." *Biomimetics* 9(3):139, 2024. [DOI](https://doi.org/10.3390/biomimetics9030139) · PMID 38534824.

## What the paper did

This is the embodied descendant of the Gurney/Redgrave selection model — the same selection architecture, now driving a robot on an animal-inspired foraging task. The manipulation is deliberately narrow and parametric: sweep the tonic level of *simulated dopamine* up and down while leaving the selection circuit itself untouched, and watch what happens to behaviour. The findings form a clean inverted-U with two failure modes at the edges. Reducing DA slowed behaviour and, at low levels, produced outright **inability to initiate movement**; these low-DA deficits were only **partially** relieved by increasing salience (stronger sensory/motivational input). Raising DA above baseline did not sharpen selection — it **distorted** motor acts, with partially-expressed *losing* actions leaking through and an elevated rate of behaviour-switching. At both extremes the agent could lose behavioural integration entirely, sometimes stuck in a "behavioural trap." The authors frame the parallels to dopamine-dysregulation syndromes in animals and humans.

## Why it speaks to Q-078

Q-078 sets constitution against a specific parametric alternative: maybe the conversion ceiling is just "upstream signals too weak / modulatory channels too quiet." Tonic dopamine is the canonical parametric/modulatory lever, and the closest biological analogue of REE's "modulatory channels too quiet" pole (and of the SD-037-style tone signals in the channel list). This paper is, in effect, an experiment on that pole *with the selection constitution held fixed and working* — and the answer is that turning the parametric knob does not deliver graceful conversion. Too little and nothing commits; too much and the wrong things commit; and stacking a second parametric lever (salience) on top of a low-DA deficit only **partially** rescues it. That is exactly the shape Q-078 reports: formed, measurable signals across five channels that fail to convert *reliably*, with strengthening producing partial or non-monotone effects rather than clean conversion.

The useful discriminating signatures for the paired experiment: (1) if REE conversion responds only *partially* — or non-monotonically — to strengthening an upstream channel, that argues against a purely parametric ceiling; (2) a monotone "more signal is always better" assumption is simply false for a real selection architecture, since excess drive degrades selection by letting losing actions leak.

## The mapping and its limits

I am reading this against the grain of the paper's own thesis, which is about modelling dopamine dysregulation and Parkinsonism, not about adjudicating constitutional-vs-parametric — so the parametric-insufficiency inference is mine, drawn from its results, and I weight it accordingly. There is also a structural asymmetry: the study varies parameters *given* a working selection constitution, so it shows parametric levers are insufficient when the constitution is intact. It does *not* run the converse experiment REE actually needs — take a constitution-poor system and show that *adding* the selection constitution fixes conversion. And it is a robot-embodied simulation, so transfer to REE's E3 is analogical. This is corroborating context for the parametric-insufficiency half of Q-078, not a primary anchor.

## Confidence

0.62, `supports` (weakly weighted). Source quality is good but below the two anchor papers — a specialist neurorobotics demonstration rather than a validated-prediction study. Mapping fidelity is moderate because the parametric-insufficiency reading is inferred rather than the paper's claim. Transfer risk is elevated for the embodied-simulation and architecture-held-fixed reasons above.
