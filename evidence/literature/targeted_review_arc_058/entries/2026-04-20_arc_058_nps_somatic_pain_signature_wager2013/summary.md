# Wager et al 2013 -- NPS (Neurologic Pain Signature)

## What the paper did

Wager and colleagues used machine-learning multivariate pattern analysis on fMRI data from 114 participants across four training studies and two independent test samples to derive a distributed brain pattern -- the Neurologic Pain Signature (NPS) -- that predicts the intensity of somatic thermal pain at the single-trial level. The NPS loads positively on thalamus, dorsal posterior insula, anterior insula, S2, ACC, and PAG, among other regions. They then asked whether this pattern is specific to physical pain by testing it against nonpainful warmth, pain anticipation, pain recall, social rejection pain, and opioid (remifentanil) analgesia.

## Key findings relevant to ARC-058

The NPS discriminates physical pain from warmth at 93-95% accuracy, from pain anticipation and recall at >89%, and -- the finding most relevant to ARC-058 -- from social pain at 85% sensitivity and 73% specificity (and 95%/95% in forced-choice). Remifentanil substantially reduces the NPS response, confirming that it indexes the nociceptive-affective cascade rather than task-general processes.

The reason this matters for ARC-058: if a single shared forward-model trunk encoded a modality-independent aversive-PE signal that dominated the per-stream variance, then physical pain and social pain should produce highly overlapping distributed patterns at the realised-pain level. Instead, the NPS and a subsequent social-pain pattern are substantially separable, and a joint pattern achieves near-perfect forced-choice discrimination. This is consistent with stream-specific readouts downstream of whatever shared computation may exist upstream.

## How this translates to REE

ARC-058's architecture is a shared HarmForwardTrunk plus stream-specific HarmForwardHeads. ARC-033 is independent per-stream forward models. The NPS is a readout of realised physical pain, not a readout of the forward model itself, so it does not directly adjudicate the trunk question. What it does adjudicate is whether the downstream per-stream signal is strong enough to carry modality-specific structure: it is. A strong version of ARC-058 that predicted trunk-dominant variance at the representation level is weakened by this paper. A weak version of ARC-058 in which the trunk carries a single unsigned surprise scalar while the heads carry all the per-stream structure is fully compatible.

Combined with Horing & Buchel 2022 (already in the pain_predictive_coding directory), this points toward a two-layer architecture: shared anterior-insula unsigned magnitude + stream-specific distributed readouts. That is, in fact, exactly what ARC-058's specification says: a single trunk producing an unsigned surprise signal, with signed per-stream heads carrying the discriminating information.

## Limitations and caveats

The NPS indexes realised pain, not the precision-weighted PE that ARC-058 specifies. Social pain is a much larger modality gap than the z_harm_s vs z_harm_a distinction REE makes; the Wager paradigm does not test within-pain sub-modality separability. Opioid modulation is strong evidence that the NPS indexes the nociceptive cascade rather than generic salience, but it does not fix the forward-model question.

The classification accuracies are excellent for binary out-of-sample discrimination but were derived on thermal pain only; Krishnan et al 2016 subsequently showed the NPS generalises to mechanical and electrical pain, which supports the "somatic pain" label rather than "thermal pain only."

## Confidence reasoning

I have this at 0.78. Source quality is very high: NEJM, multiple independent samples, cross-validation, opioid control. Mapping fidelity is moderate (0.60) because the paper does not directly image the forward-model trunk -- it images realised pain and infers about upstream architecture by exclusion. Transfer risk is low within the human thermal pain domain but moderate when the finding is asked to arbitrate a claim about within-pain sub-modality forward-model structure. The paper weakens the strong form of ARC-058 but does not kill it; the weak form (unsigned trunk + signed heads, as the spec actually says) is compatible.

According to PubMed, [DOI: 10.1056/NEJMoa1204471](https://doi.org/10.1056/NEJMoa1204471).
