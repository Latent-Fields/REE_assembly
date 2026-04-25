# Sosa et al. 2025 — BLA State Gates HPC Reconsolidation Plasticity (MECH-074d)

**Source:** Sosa MC, Comas Mutis R, Riva Gargiulo M, Martijena ID, Bender CL, Calfa GD. "A hyperexcited basolateral amygdala complex state determines the hippocampal structural plasticity associated with the reconsolidation of a fear memory." *Neuroscience* 592:111–119. DOI: 10.1016/j.neuroscience.2025.11.023

## What the paper did

Sosa et al. used local infusion of bicuculline (GABA-A antagonist) into the BLA of rats to induce a pharmacologically-controlled hyperexcited state analogous to the GABAergic disinhibition that occurs during acute stress. Animals then underwent contextual fear conditioning and memory reactivation, and dorsal hippocampal dendritic spine density was measured as an index of structural plasticity during reconsolidation. A separate group received D-cycloserine (partial NMDA agonist) prior to memory reactivation to test whether NMDA receptor modulation could rescue BLA-disrupted hippocampal reconsolidation.

## Key findings relevant to MECH-074d

BLA hyperexcitation produced dendritic spine changes in dorsal hippocampus that mimicked acute stress exposure: the normal reconsolidation-related spine remodelling was disrupted. D-cycloserine reversed this effect, restoring hippocampal structural plasticity. The findings establish a causal pathway: BLA excitability state → dorsal hippocampus structural plasticity during fear memory reconsolidation. This provides the biological mechanistic precedent for MECH-074d's core claim that BLAAnalog state (PE spike amplitude) determines whether HippocampalModule undergoes representational update (remap_signal).

## Translation to MECH-074d

MECH-074d proposes that BLAAnalog emits a remap_signal to HippocampalModule when ||z_harm_a - E2_harm_a_pred|| exceeds ~1 SD of the running PE distribution AND predictor-attribution flags target latent codes. Sosa et al. operationalise the BLA-state → hippocampal-plasticity pathway at the structural level: elevated BLA activity is sufficient to alter whether dorsal hippocampus rewrites memory traces during reactivation. The NMDA-rescue finding is also relevant — it shows the reconsolidation gate is plastic and pharmacologically modifiable, consistent with the MECH-074d prediction that attribution-head training (learnable gate, second pass) could improve remap specificity.

## Limitations and caveats

The study measures global dendritic spine density, not attribution-specific partial remapping of particular representations. MECH-074d's most distinctive claim — that remap fires on only ~30-40% of predictor-candidate codes (partial, not wholesale remap) — cannot be evaluated from global spine counts. BLA hyperexcitation via bicuculline is not equivalent to a discrete harm-PE spike; it is a sustained pharmacological manipulation. Whether a brief, naturally occurring PE spike produces the same effect is not tested.

## Confidence

0.72. Good causal evidence for BLA-state gating of hippocampal reconsolidation plasticity. Mapping fidelity limited by global structural measure (no attribution specificity) and pharmacological vs physiological BLA manipulation.
