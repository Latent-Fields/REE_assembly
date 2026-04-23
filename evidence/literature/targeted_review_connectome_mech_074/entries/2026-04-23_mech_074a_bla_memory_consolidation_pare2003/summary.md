# Summary: Pare (2003) — Role of the basolateral amygdala in memory consolidation

**Source:** Pare D (2003). *Progress in Neurobiology*, 70(5):409–420. [DOI: 10.1016/s0301-0082(03)00104-7](https://doi.org/10.1016/s0301-0082(03)00104-7)

**Claim tested:** MECH-074a — BLA analogue applies an arousal-dependent multiplicative gain to hippocampal write strength.

---

## What the paper does

This is Denis Paré's 2003 synthesis review integrating the prior 20 years of evidence on how the BLA modulates memory consolidation. It brings together pharmacological, lesion, and microdialysis data to argue that emotional arousal triggers a transient (~2h) surge of noradrenaline (NA) and acetylcholine (ACh) in the BLA, and that this surge — by increasing the excitability of BLA projection neurons — facilitates synaptic plasticity in distributed target structures, principally the hippocampus and rhinal cortex. BLA lesions block the memory-enhancing effects of systemic or local adrenal stress hormones. Post-learning intra-BLA infusions of beta-adrenergic or muscarinic antagonists reduce long-term retention on emotionally charged tasks.

## Key findings relevant to MECH-074a

The paper establishes several mechanistic components that map onto MECH-074a:

1. **Arousal triggers NE/ACh release in BLA**: Microdialysis shows BLA NA and ACh transiently elevated after emotionally arousing learning episodes, returning to baseline over ~2h. This provides the biological substrate for the post-event decay window in MECH-074a's encoding_gain scalar.

2. **BLA is necessary for stress hormone memory effects**: BLA lesions eliminate the memory-enhancing effects of posttraining glucocorticoid or adrenaline administration. The BLA is not a storage site but a neuromodulatory *gateway* — encoding_gain > 1 requires BLA intactness.

3. **Theta-frequency BLA activity**: During arousal, BLA neurons rhythmically discharge at theta (~4–8 Hz) and, via uniform axon conduction times to rhinal sites, can synchronise plastic changes across co-active temporal lobe structures. This is a circuit-level prediction for how BLA amplifies hippocampal write strength: not a direct synapse but coordinated timing.

## REE translation and mapping

MECH-074a frames this as an encoding_gain scalar that multiplies HippocampalModule write strength as a function of z_harm_a magnitude. Paré's review is the theoretical backbone: arousal (z_harm_a = BLA activation) → NE/ACh surge in BLA → excitability boost → facilitated plasticity at hippocampal synapses. The REE implementation collapses the NE/ACh biochemistry into a scalar gain, which is a faithful simplification.

The mapping caveat is the inverted-U shape. Paré's paper does not demonstrate high-arousal memory impairment — the reviewed literature predominantly samples the moderate-arousal facilitatory range. The ceiling and reversal of the inverted-U are inferred from Yerkes-Dodson-type principles and are documented elsewhere (Diamond, Joels). MECH-074a's encoding_gain_max at ‖z_harm_a‖ ~ 0.7, with floor below 0.4 threshold, is a reasonable but not directly evidenced parameterisation from this paper alone.

## Limitations and caveats

The review focuses on consolidation-phase NE/ACh effects rather than online encoding during the experience. REE's encoding_gain operates at the encoding step. Whether NE/ACh effects on hippocampal plasticity are mediated online (during the event) versus post-event is not resolved here. Additionally, Paré proposes that BLA influences hippocampal regions via the rhinal cortex, not necessarily by direct BLA-CA1 synaptic contacts — this is consistent with the REE design but adds a layer of indirection to the write-strength framing.

## Confidence reasoning

Confidence 0.80. High-quality synthesis from a leading group, well-replicated mechanism across rodent and human. Mapping fidelity is good but the gain arithmetic (specifically the inverted-U shape and 2.5x maximum) is inferred not directly evidenced here. Transfer risk is low — NE/ACh modulation of hippocampal plasticity is conserved.
