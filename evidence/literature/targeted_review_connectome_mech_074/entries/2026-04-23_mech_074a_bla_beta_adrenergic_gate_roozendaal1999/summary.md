# Summary: Roozendaal et al. (1999) — BLA noradrenergic influence enables hippocampal glucocorticoid memory enhancement

**Source:** Roozendaal B, Nguyen BT, Power AE, McGaugh JL (1999). *Proceedings of the National Academy of Sciences*, 96(20):11642–11647. [DOI: 10.1073/pnas.96.20.11642](https://doi.org/10.1073/pnas.96.20.11642)

**Claim tested:** MECH-074a — BLA analogue applies an arousal-dependent multiplicative gain to hippocampal write strength.

---

## What the paper does

Roozendaal, Nguyen, Power, and McGaugh (1999) ask a precise mechanistic question: when glucocorticoid receptors in the hippocampus are activated by stress hormones, does BLA noradrenergic activity enable this effect? They infuse a glucocorticoid receptor (GR) agonist (RU 28362) directly into the dorsal hippocampus after inhibitory avoidance training, producing dose-dependent enhancement of 48h retention. Then they ask whether blocking BLA beta-adrenergic receptors ipsilaterally (atenolol) abolishes this hippocampal GR effect. The answer is clear: ipsilateral, but not contralateral, BLA beta-adrenergic blockade completely eliminates the hippocampal memory enhancement.

## Key findings relevant to MECH-074a

1. **BLA NE is permissive, not redundant**: The hippocampal GR agonist has no memory effect when ipsilateral BLA NE signalling is blocked. This establishes BLA as a gate — without BLA NE activity, hippocampal arousal signalling cannot translate into enhanced consolidation.

2. **Ipsilateral specificity**: Contralateral BLA blockade is ineffective, ruling out peripheral (systemic) explanations. The effect travels via ipsilateral BLA-to-hippocampus neural pathways.

3. **Beta-adrenergic (not muscarinic) receptor**: Atropine in BLA does not block the hippocampal GR effect, isolating the mechanism to the NE beta-adrenergic channel.

## REE translation and mapping

In REE, z_harm_a magnitude drives the BLAAnalog, which emits encoding_gain. This paper provides the canonical empirical evidence for the gating operation: when z_harm_a is below threshold (NE below threshold in REE terms), encoding_gain = 1.0; when z_harm_a is elevated, encoding_gain > 1.0. The beta-adrenergic specificity supports framing encoding_gain as driven by the NA-pathway analogue of z_harm_a.

The caveat is that this paper demonstrates gate/permissive control rather than graded gain. It shows presence/absence: NE blocked → no enhancement. Whether the gain scales continuously with NE level, and especially whether it reverses at very high levels (the inverted-U), requires the Roozendaal & McGaugh 2011 review and pharmacological dose-response data. The REE parameters (encoding_gain_max = 2.5x at ‖z_harm_a‖ ~ 0.7) are extrapolated from this gate structure combined with dose-response curves from other sources.

## Limitations and caveats

The GR agonist model of arousal is pharmacological, not naturalistic — it does not confirm that the same gate operates under spontaneous emotional events. The inhibitory avoidance paradigm involves single-trial learning under strong foot-shock, which saturates arousal and may not probe the full gain curve. The ~18000 sim-step post-event window in MECH-074a corresponds to the ~2h biological consolidation window in this paradigm, which is a reasonable mapping.

## Confidence reasoning

Confidence 0.82. PNAS, McGaugh lab, well-replicated; beta-adrenergic gating is conserved across mammalian species and is one of the most robust findings in the emotional memory literature. The main limitation for MECH-074a is that gating (binary) is shown, not graded gain. This paper is load-bearing for the gate premise of MECH-074a; the gain-curve shape is inferred from other sources.
