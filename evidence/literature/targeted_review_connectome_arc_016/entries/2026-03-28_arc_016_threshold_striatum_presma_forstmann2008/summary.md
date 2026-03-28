# Forstmann et al. 2008 — Striatum and pre-SMA Facilitate Decision-Making Under Time Pressure

**Source:** Forstmann BU, Dutilh G, Brown S, Neumann J, von Cramon DY, Ridderinkhof KR, Wagenmakers EJ (2008). *PNAS* 105(45):17538–42. [DOI: 10.1073/pnas.0805903105](https://doi.org/10.1073/pnas.0805903105)

---

## What the paper did

Nineteen healthy human participants performed a two-alternative forced-choice perceptual decision task while undergoing fMRI. Before each trial, they received either a speed-emphasis cue (prioritise fast responses) or an accuracy-emphasis cue (prioritise correct responses). The authors fit a drift-diffusion model to the response data, extracting the response threshold parameter for each emphasis condition for each participant. They then correlated individual variation in neural activation (speed vs. accuracy conditions) with individual variation in threshold adjustment, asking: which brain regions implement the instruction-to-threshold mapping?

## Key findings relevant to ARC-016

The primary result was a double dissociation: striatum and pre-SMA were significantly more active under speed emphasis than accuracy emphasis, and the magnitude of this activation predicted the magnitude of each participant's threshold reduction. Participants who showed larger striatum/pre-SMA responses to speed cues also showed larger threshold drops — confirming that this circuit is not merely correlating with behaviour but is the mechanism through which the task-level demand (speed or accuracy) is converted into a decision threshold parameter.

This is the empirical evidence that the basal ganglia-frontal circuit implements what ARC-016 calls the commitment threshold: a variable parameter that gates when accumulated evidence or prediction confidence permits action release. The result is not merely that BG/frontal circuits are active during decisions, but that *individual variation in threshold* (a specific quantitative parameter extracted from a computational model) tracks *individual variation in neural activation* — a quantitative, mechanistic link.

## Translation to REE / ARC-016

ARC-016 proposes a circuit: E3-derived prediction variance → relative threshold (2x training baseline variance, EXQ-018b) → BetaGate → action_selection. The Forstmann et al. result provides the neural instantiation of the threshold → gate step: the striatum-pre-SMA circuit is the anatomical locus where a threshold parameter translates into an action-selection gate (or release from inhibition). In REE terms, once E3's variance drops below the relative threshold, the BetaGate should engage — this corresponds to the striatum releasing the motor system from global inhibition when the threshold is crossed under speed pressure. The commit_rate vs. precision relationship in EXQ-018b directly parallels the threshold-activation correlation this study documents.

## Limitations and caveats

The critical limitation is that the threshold manipulation in Forstmann et al. is externally imposed via instructions (speed/accuracy cue), whereas ARC-016 requires the threshold to be dynamically derived from E3's internal prediction uncertainty. The neural circuit might be identical, but the driving input differs: external instruction vs. internal variance estimate. The inference is that the same striatum-pre-SMA mechanism that adjusts threshold based on instruction also adjusts threshold based on internal uncertainty — a reasonable inference given that both ultimately need to modulate the same circuit parameter, but not directly tested. The paper also addresses perceptual thresholds (evidence accumulation for stimulus identity) rather than cognitive commitment thresholds (commitment to a plan or mode), which is a further level of abstraction.

## Confidence reasoning

Confidence 0.74. Source quality is strong (PNAS, human fMRI with rigorous computational modelling, n=19). Mapping fidelity is good for the threshold → gate relationship, penalised for the external-vs-internal threshold distinction and perceptual-vs-cognitive level difference. Transfer risk is moderate for these reasons. This paper and Friston 2012 together provide complementary grounding: Friston grounds the variance-to-precision computation (the E3 side), Forstmann grounds the threshold-to-action-gate conversion (the BetaGate side).

*According to PubMed, this article is available at PMID 18981414. [DOI: 10.1073/pnas.0805903105](https://doi.org/10.1073/pnas.0805903105)*
