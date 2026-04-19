# Croxson, Walton, O'Reilly, Behrens & Rushworth 2009 — Effort-based cost-benefit valuation and the human brain

**Source:** *The Journal of Neuroscience* 29(14):4531-4541, [10.1523/JNEUROSCI.4515-08.2009](https://doi.org/10.1523/JNEUROSCI.4515-08.2009). Via PubMed (PMID 19357278).

## What the paper does

Croxson et al. scanned humans performing a factorial effort-reward task in which cues indicated both the effort required (levels 1-2) and the reward available (levels 1-4) for a secondary reinforcer. They then dissociated activity that reflects reward alone, effort alone, net value (reward discounted by effort), and the interaction of reward × effort. The finding that drives the paper is a clean division of labour: ventral striatum and midbrain carry the net-value signal, posterior orbitofrontal and insular activity reflect reward magnitude alone, and dorsal ACC specifically reflects the *interaction* — it is maximal when both reward and effort are high, signalling a costly but potentially worthwhile course of action. This establishes dACC as an integration site for cost-benefit arithmetic, distinct from the downstream value-computation regions.

## Key findings relevant to the claim

- **Ventral striatum + midbrain encode net value.** The "expected reward minus effort" scalar lives in the dopaminergic value system, not in dACC.
- **dACC encodes the reward × effort interaction.** Activity is not just reward or just effort or their sum — it is specifically elevated when both are high, consistent with dACC being the node that *integrates* them rather than the node that outputs the final choice.
- **OFC/insula encode reward alone, unmodulated by effort.** Value-of-outcome is preserved in OFC regardless of whether the path to that outcome is costly.
- **Effort is processed as a first-class variable, not derived from reward.** The factorial design dissociates cost from benefit, showing they enter the dACC computation as independent terms.

## How this maps onto REE (the translation)

Croxson 2009 sharpens the architectural specification of SD-032b relative to the rest of the cingulate cluster. The paper cleanly dissociates two computations that ree-v3 currently conflates: *integration* (combining benefit and cost into a meaningful interaction term) and *selection* (emitting the final "continue or switch" decision). Ventral striatum / midbrain does the selection; dACC does the integration. The ree-v3 analogue should have:

- SD-032b (dACC/aMCC-analog) emits an *integration signal*: reward-of-continuing-current-mode combined with effort-of-switching-mode, with the interaction term preserved (not collapsed to a subtraction).
- A downstream substrate — closer to E3 trajectory scoring combined with SD-012 homeostatic drive — emits the *net-value* signal that actually drives mode selection.
- SD-032a (salience-network coordinator) reads both and gates the mode-switch.

This is a cleaner decomposition than "dACC just computes a net value"; it gives SD-032b a specific computational job that does not duplicate E3/striatal-analog function. The MINIMUM VIABLE form of SD-032b is therefore narrower than it might appear: it only needs to emit an integration signal, not a final decision.

The paper also grounds MECH-258 (precision-weighted pain PE) in the broader cost-benefit circuit. Affective pain (z_harm_a) is a cost term that enters the dACC integration in the same way effort does in Croxson's paradigm. The biological prediction: z_harm_a should modulate dACC-analog activity specifically when paired with a reward signal (a trajectory with both high reward AND high projected affective cost), not when either is isolated. This is directly testable in ree-v3.

## Limitations and caveats

The study uses secondary reinforcers (visual cues for cued-effort bulb-squeeze producing fluid reward). Effort is conceptual/cued rather than physiological. Whether the same dACC integration runs for physiological effort (fatigue, pain) is a reasonable inference but not directly shown; the transfer from cued effort to embodied ree-v3 effort-cost will not be one-to-one. The sample is modest (N=16).

Croxson 2009 pre-dates both the Kolling foraging-value and Shenhav EVC frameworks. The dACC integration result is compatible with both interpretations — EVC would call this "expected value of controlled effort", Kolling would call this "relevance to foraging-mode decision". The paper does not disambiguate them, which is why we need the other entries in this pull. Its value is architectural: it establishes the integration-vs-selection dissociation that both later frameworks assume.

## Confidence reasoning

0.80. Highly cited J Neurosci paper from Rushworth lab. Clean factorial design. Strong architectural contribution to ree-v3 because it separates integration (SD-032b) from selection (downstream substrate), which was implicit and ambiguous in the initial cingulate-substrate lit-pull. Transfer risk is moderate because effort in the paradigm is cued/abstract rather than physiological — ree-v3's effort cost will be more directly embodied via SD-012 homeostatic drive, and whether the integration architecture survives the domain shift is a testable open question.
