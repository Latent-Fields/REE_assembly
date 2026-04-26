# Sakurai 2014 — orexin in motivated behaviour, recruitment and downstream gain

## What the paper did

Sakurai — the discoverer of orexin — wrote this Nature Reviews piece as a comprehensive synthesis of orexin's role across motivated behaviours: feeding, arousal, reward, stress, and the panic and addiction states orexin pharmacology now treats. The review integrates rodent physiology, optogenetics, pharmacology, and human narcolepsy data. Two strands of the synthesis are directly relevant to MECH-280: (a) the recruitment kinetics of orexin neurons across behavioural states, and (b) the downstream gain orexin exerts on its target populations (PAG, locus coeruleus, VTA, dorsal raphe).

## Key findings relevant to MECH-280

The recruitment side establishes the biological referent for MECH-280's recruitment_threshold parameter. Orexin neurons are intrinsically depolarised — they sit close to firing threshold and are pushed across it by relatively modest excitatory drive — and they show roughly a five-fold ratio between quiet-waking and active-waking firing rates, with maximal firing during exploration and high-effort behavioural episodes. The recruitment is therefore graded with a sigmoid-like inflection that sits well above baseline; the recruitment_threshold ≈ 0.5 default in SD-037 is a defensible midpoint for that recruitment curve.

The gain side gives MECH-280 its alpha_override anchor. Sakurai reports that saturating orexin doses produce 1.3x to 3x firing-rate increases at downstream targets. Mapped onto MECH-280's multiplicative formulation theta_freeze_effective = theta_freeze_base × (1 + alpha_override × override_signal), with override_signal saturating at 1.0, alpha_override = 0.5 produces a 1.5x maximum threshold elevation, which sits at the lower end of the biologically reported gain band. alpha_override up to 1.0 (giving 2x maximum elevation) is equally defensible; alpha_override above ~1.5 (giving 2.5x elevation) is at or beyond the biological band's upper edge.

## How this translates to REE

The review supports two MECH-280 design choices: the multiplicative formulation (gain rather than hard switch), and the recruitment_threshold midpoint sitting above quiet-waking baseline. It places alpha_override = 0.5 at the conservative lower edge of the biological band — defensible as a starting default, but the SD-037 validation factorial should sweep up to 1.0 if the conservative default produces only marginal active-coping shift (the REVIEW.md synthesis already flags this).

The review also reinforces MECH-280's framing as a broadcast-override scalar rather than a target-specific channel: orexin's gain is reported across PAG, LC, VTA, and dorsal raphe simultaneously. This is consistent with SD-037's parent-claim formulation in which override_signal is a global regulator and MECH-280 / MECH-281 are its target-specific child claims.

## Limitations and caveats

This is a review by a single author (a senior figure in the field, but with a known stake in promoting the orexin literature's centrality). The 1.3x-3x downstream-gain band is a cross-target average rather than a PAG-specific measurement; the underlying primary sources differ in methodology, species, and saturation regime. The 0.5 alpha_override anchor is therefore an order-of-magnitude claim, not a precision constraint. For MECH-280 this is sufficient — the parameter is anchored, not pinned.

## Confidence reasoning

I am giving this 0.74. Source quality is high (0.85, Nature Reviews, authoritative author) but discounted from the absolute ceiling because it is a review rather than a primary paper. Mapping fidelity is 0.72 — the gain band is a cross-target average and the recruitment characterisation is qualitative rather than quantitative on the threshold. Transfer risk is standard at 0.30. The aggregate sits in the supports band, slightly below the de Araujo Salgado direct behavioural anchor but reinforcing the parameter-anchoring story the SD-037 REVIEW.md synthesis already records.
