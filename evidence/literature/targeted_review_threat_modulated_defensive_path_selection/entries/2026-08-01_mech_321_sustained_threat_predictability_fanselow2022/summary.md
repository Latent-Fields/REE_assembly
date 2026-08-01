# Fanselow 2022 -- Negative valence systems: sustained threat and the predatory imminence continuum

**Source**: Fanselow MS (2022). *Emerging Topics in Life Sciences* 6(5):467-477. [DOI 10.1042/ETLS20220003](https://doi.org/10.1042/ETLS20220003). PMID 36286244, PMC9788377.

## What the paper did

This review tackles a gap in the RDoC-to-PIC mapping: RDoC's Negative Valence System includes a "Sustained Threat" construct alongside Potential Threat and Acute Threat, but nothing in the PIC's pre-encounter/post-encounter/circa-strike structure corresponds to it directly. Fanselow traces the research history of the bed nucleus of the stria terminalis (BST), initially thought to be the brain region responsible for SUSTAINING fear responses over long durations, and shows how follow-up work overturned that reading.

## Key findings relevant to the claim

The BST turns out not to be about duration of fear per se — it becomes functionally critical specifically when the stimuli predicting an aversive outcome are hard to learn about, i.e. when the aversive outcome is difficult to accurately PREDICT. The BST (together with the hippocampus) functions to widen the range of conditions that can trigger post-encounter (Acute Threat/fear) defense when predictive cues are poor or ambiguous. "Sustained threat" is then reframed not as a fourth PIC mode in its own right, but as a state where the normal imminence-to-mode mapping becomes DISTORTED by chronic stress — defensive behavior starts intruding into contexts and time-windows where the organism should instead be doing other adaptive things.

## How this translates to REE

This is the clearest grounding this pull found for the "which threat features (beyond magnitude/proximity) should modulate the selection rule" half of the design question. Predictability of the harm-predicting cue is not incidental context here — it recruits a functionally distinct mechanism (BST/hippocampus, widening the trigger conditions) rather than simply scaling the existing one. For REE, this argues that `z_harm_a`/BLA `threat_scale` as a bare scalar magnitude may eventually be an incomplete input on its own; a companion signal capturing how reliably a harm-predicting pattern has actually preceded harm could plausibly need to modulate the PERSISTENCE or scope of a threshold-gated regime, separate from what triggers it. The paper also hands implementers a concrete negative control to test for once a selection step is built: a version that never disengages once triggered — keeps biasing every subsequent redecomposition toward maximally-defensive tiles regardless of whether the harm-predicting condition has resolved — is architecturally the same failure mode as this paper's "sustained threat" pathology, and should be checked for explicitly.

## Limitations and caveats

The evidence base here is BST/hippocampal lesion, pharmacology, and stress-and-anxiety-disorder literature — one architectural layer removed from MECH-321's specific junction (BST/hippocampus here govern whether post-encounter defense triggers at all, not which re-tiling gets chosen once triggered). REE has no direct analog of BST-mediated predictability learning to calibrate against quantitatively; the transfer is conceptual.

## Confidence reasoning

Strong, authoritative single-author synthesis from the field's leading voice on PIC. Mapping fidelity moderate: highly relevant to the predictability-as-a-modulating-feature question and to a useful failure-mode caution, but one step removed from the precise selection junction. Confidence 0.72, included primarily to ground the predictability dimension the pure imminence/proximity entries in this pull do not cover.
