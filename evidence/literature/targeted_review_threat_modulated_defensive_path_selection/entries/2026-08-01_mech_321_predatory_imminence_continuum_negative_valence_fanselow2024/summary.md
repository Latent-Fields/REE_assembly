# Fanselow & Hoffman 2024 -- Fear, defense, and emotion: a neuroethological understanding of the negative valence RDoC

**Source**: Fanselow MS, Hoffman AN (2024). *American Psychologist* 79(5):725-734. [DOI 10.1037/amp0001354](https://doi.org/10.1037/amp0001354). PMID 38695781, PMC11829742.

## What the paper did

This is a 2024 synthesis, from the lab that originated the Predatory Imminence Continuum (PIC), restating the theory against the current NIMH Research Domain Criteria (RDoC) framework for negative valence. It is not new primary data; it is the most current authoritative statement of PIC available, and the natural entry point for this lit-pull because it explicitly cross-walks PIC's defensive modes onto RDoC's Potential-Threat / Acute-Threat constructs, and reviews recent causal (not just correlational) evidence tying human subjective fear states to amygdala activity.

## Key findings relevant to the claim

The PIC's central claim, restated here: antipredator defense is not a single graded response but is organized into a small number of qualitatively distinct behavioral MODES, keyed to the perceived psychological/spatiotemporal closeness of the threat -- pre-encounter (diffuse, anticipatory, corresponds to anxiety/RDoC Potential Threat), post-encounter (a specific, present-but-not-yet-contacting threat, corresponds to fear/RDoC Acute Threat, freezing-dominant), and circa-strike (contact is imminent or occurring, panic, flight/fight-dominant). Mode identity -- not a single continuous intensity dial -- governs which behavioral repertoire is available. The paper also reviews causal (optogenetic/lesion, plus new human intracranial) evidence that amygdala activity is not merely correlated with but drives both the felt emotional state and the corresponding defensive behavior across this continuum.

## How this translates to REE

This is the conceptual scaffold for the harm-valence-weighted selection step MECH-321/SD-hazard-aware-policy-decomposition needs. It argues that the redecomposition step's selection rule should not be built as a single linear/continuous bias term alone -- the biology it is meant to approximate organizes behavior into qualitatively distinct regimes as a function of imminence, and REE's `z_harm_a`/BLA `threat_scale` signal is the natural REE-side analog of the variable that would need to determine which regime is "in force" at selection time. This motivates the two-part functional-form recommendation in this pull's SYNTHESIS.md (a graded bias term plus a threshold-gated regime change), rather than either a single fixed threshold or a pure linear weight alone.

## Limitations and caveats

This is a review of whole-organism, whole-behavior mode selection (which overt defensive action the animal performs), not of a redecomposition/replanning subsystem choosing among internally-generated candidate sub-plans. REE has no existing architectural analog of "defensive mode" -- this paper motivates building one, it does not describe one that already exists in the substrate. The mapping is conceptual/structural, not a quantitative calibration.

## Confidence reasoning

High source quality (current, authoritative, senior-author synthesis of a decades-long research program with converging causal evidence). Moderate-high mapping fidelity: the mode-organized-by-imminence claim is exactly on point for the design question, but transfer risk is real because the REE-side construct it would map onto does not yet exist. Confidence 0.85, weighted toward source quality given the review's role here is to establish the theoretical frame the rest of this pull's more mechanistic/empirical entries fill in.
