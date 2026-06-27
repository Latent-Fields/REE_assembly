# Single-neuron cost-benefit analysis in frontal cortex (Hosokawa, Kennerley, Sloan & Wallis, 2013)

**Claim under test:** MECH-451 — the intermediate channel-granularity falsifier. Does exposing the compressed single modulatory channel as several separately-learnable finer channels (OFC-devaluation, dACC-conflict, lateral-PFC rule-evidence, vigour, liking) localise the F-dominance conversion ceiling to *representational compression* rather than to a need for full anatomically-segregated loops?

## What the paper did

Hosokawa and colleagues recorded single neurons across four frontal regions — orbitofrontal cortex (OFC), anterior cingulate cortex (ACC), dorsolateral prefrontal cortex (DLPFC), and cingulate motor area (CMA) — while macaques made cost-benefit choices that traded reward against either *delay* or *physical effort*. The design lets one ask whether frontal cortex computes a single integrated subjective-value signal that pools across cost types, or whether it carries something more fragmented.

## Key finding relevant to the claim

The integrated subjective-value signal — the clean scalar that a "compressed value channel" picture would predict — was carried by only a *minority* of neurons, concentrated in ACC. The *majority* across all four areas instead encoded the **decision type** (delay-based vs effort-based), with partial regional specialisation: OFC and DLPFC showed the largest firing-rate changes for delay- but not effort-based decisions, while the reverse held for CMA; only ACC was modulated by both. The authors explicitly conclude this "challenge[s] the idea that OFC calculates an abstract value signal" and that frontal neurons instead categorise stimuli by their predicted consequences.

This is the most load-bearing single datum in the MECH-451 pull because it cuts both ways. It *supports* the premise that control is not one compressed scalar — different cost dimensions live in partially segregated populations, which is the biological permission slip for finer separately-learnable channels. But it also complicates the clean five-channel story: the dominant code is *categorical* (which kind of decision is this?), not a set of graded value channels feeding a comparator. And the integrated-value population, where it exists, looks like exactly the shared bottleneck MECH-451 worries about.

## Mapping to REE

The honest translation is that this paper evidences the *segregation/separability* half of MECH-451 strongly and the *separately-learnable-improves-conversion* half not at all. Neural representation of decision variables is necessary-but-not-sufficient for the claim that a gating learner, given finer channels, converts more non-motor influence into committed action. The biology says the substrate for finer channels exists; it is silent on whether a learner exposed to them escapes the conversion ceiling — appropriately, since that is a claim about learner architecture, not about brains.

## Caveats and confidence

Primate single-unit recording transfers to an artificial gating layer only loosely (mapping_fidelity 0.55), but the source quality is high (0.92). I have logged this as **mixed** rather than supports precisely because the dominant categorical code and the minority integrated-value population are themselves a concrete prediction of how the MECH-451 falsifier could *fail*: a learner exposed to finer channels might discover category gating, or might re-funnel everything through a shared value node — reproducing the ceiling rather than relieving it. Confidence 0.6.
