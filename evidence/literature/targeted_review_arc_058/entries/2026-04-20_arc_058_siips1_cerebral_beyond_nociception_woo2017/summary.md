# Woo et al 2017 -- SIIPS1 (Stimulus Intensity Independent Pain Signature-1)

## What the paper did

Woo and colleagues developed a second multivariate pain-prediction signature, SIIPS1, explicitly orthogonalised against nociceptive input and the earlier NPS. Using fMRI from 137 participants across four training studies and 46 in two independent test samples, the authors identified a distributed pattern that predicts trial-by-trial pain ratings NOT captured by nociception-driven variance. SIIPS1 loads on nucleus accumbens, lateral prefrontal and parahippocampal cortices, with partial overlap with NPS in anterior insula. The signature mediates the pain-modulating effects of three distinct psychological manipulations -- expectation, perceived control, and cue valuation.

## Key findings relevant to ARC-058

For ARC-058 this paper provides the complementary half of the picture that NPS alone does not: pain decomposes into at least two separable multivariate patterns, one tracking nociceptive input (NPS) and one tracking the affective/contextual modulation beyond nociception (SIIPS1). Under a pure shared-trunk model with no per-stream heads, SIIPS1 should collapse to near-zero variance after orthogonalisation -- because a single unsigned magnitude code cannot produce reliable signed structure unique to the affective stream. Instead, SIIPS1 explains substantial residual variance and mediates top-down psychological effects.

Equally important: NPS and SIIPS1 show PARTIAL overlap in anterior insula, while being dissociable in posterior insula (NPS-dominant) and in NAcc/lateral PFC (SIIPS1-dominant). This is exactly the spatial structure ARC-058 predicts: a shared upstream unsigned magnitude computation (anterior insula, common to both signatures) plus stream-specific signed readouts (dpIns for sensory-discriminative; NAcc/lateral PFC/parahippocampal for affective/contextual).

## How this translates to REE

SIIPS1 is the closest available human-fMRI analogue to z_harm_a in the REE dual-stream model. The existence of a cross-validated, generalising pattern for the affective-contextual component of pain argues against ARC-033 as "fully independent substrates with no shared computation" and in favour of ARC-058's trunk-plus-heads architecture -- or at minimum in favour of whichever architecture produces the observed partial AIC overlap.

Specifically, ARC-058 says E2HarmSForward and E2HarmAForward can share a trunk (shared_trunk constructor arg) while owning separate HarmForwardHeads. Woo 2017 provides a parsimony argument for this: the brain already decomposes pain into orthogonalised components with partial shared substrate, and the shared substrate lives in the region (AIC) that the signed unsigned-PE literature (Horing & Buchel 2022) also identifies as the modality-general aversive-PE hub.

## Limitations and caveats

SIIPS1 is trained on residual pain variance after orthogonalising against NPS, which makes the boundary between "affective pain" and "everything else that modulates pain reports" fuzzier than the clean z_harm_a spec. Perceived-control and expectation manipulations drive SIIPS1, but these are not the same as a pure C-fibre-driven affective-pain stream. There is also an ongoing debate in the pain-decoding literature about whether NPS + SIIPS1 fully separate nociception from affect or whether both contain mixed signals (see the Zunhammer/Bingel 2018 meta-analysis of NPS specificity, not pulled here).

The paper images realised pain, not a forward-model PE. The inference "a forward-model trunk is shared because these signatures partially overlap in AIC" is structural, not mechanistic -- Horing & Buchel 2022 closes this gap by directly computing signed vs unsigned PE within the insula.

## Confidence reasoning

I have this at 0.80. Source quality is very high (Nat Comm, N=183 total across independent samples, psychological-manipulation mediation as a convergent test). Mapping fidelity is good (0.75) because SIIPS1 is the strongest existing fMRI decoder that isolates the component ARC-058 partitions as z_harm_a. Transfer risk is moderate (0.35) -- SIIPS1's coverage is broader than z_harm_a, and the architectural inference is structural rather than mechanistic. The evidence direction is supports for ARC-058's two-layer architecture and weakens for a pure ARC-033 no-shared-trunk interpretation.

According to PubMed, [DOI: 10.1038/ncomms14211](https://doi.org/10.1038/ncomms14211).
