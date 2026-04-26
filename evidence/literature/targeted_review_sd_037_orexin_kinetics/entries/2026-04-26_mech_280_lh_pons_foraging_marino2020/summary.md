# Marino et al. 2020 — LH GABAergic projection to dorsal pons gates food approach

## What the paper did

Marino and colleagues asked whether the lateral hypothalamus carries a projection-specific signal for food approach and consummation, distinct from the broader pool of LH glutamatergic and orexinergic outputs. They used a combination of viral cell-type tracing, optogenetic and chemogenetic manipulation, and in vitro slice electrophysiology in mouse to isolate an LH GABAergic projection to the peri-locus-coeruleus / dorsal pons region. They then tested behavioural consequences of activating and silencing this projection while mice were engaged in food-approach paradigms.

## Key findings relevant to MECH-280

The projection is genuinely projection-specific (LH-GABA cells targeting peri-LC are anatomically and physiologically distinguishable from broader LH outputs), and its activation drives food approach and bouts of consummation. Silencing the projection reduces approach and consummation under hunger. The behavioural effect is route-specific — the same LH cells projecting elsewhere do not produce the same approach effect — and the synapse is functional GABAergic (i.e., the engagement signal is carried by inhibition of downstream targets).

For MECH-280 the relevance is the existence proof: there is an LH-originating, projection-specific, active-coping engagement signal that gates approach behaviour at the brainstem level. MECH-280 names the LH-to-PAG branch of an active-coping override system; this paper documents the LH-to-peri-LC / dorsal-pons branch of the same broader system. The biology is consistent with MECH-280's claim that LH carries an override signal recruited under metabolic demand and that the signal acts at brainstem rather than cortical level.

## How this translates to REE

MECH-280's prediction is that an LH-driven scalar override raises theta_freeze_effective and biases the agent toward active foraging. This paper supports the existence and behavioural sign of the LH override (active engagement over passive avoidance) but localises a sister branch of the system rather than the named PAG branch. In REE terms: the broad architectural claim — there is an LH-originating override channel that biases toward engagement — is well supported. The narrow mechanistic claim — the operative substrate is LH→PAG specifically with a multiplicative gain on freeze threshold — is one circuit inference within this broader system, not directly evidenced by this paper.

## Limitations and caveats

Two caveats matter. First, the projection studied is LH-to-pons, not LH-to-PAG. PAG and peri-LC are anatomically adjacent and the literature treats them as part of the same brainstem defensive-behaviour cluster, but the precise synaptic target differs. MECH-280 inherits its specific PAG-targeted prediction from the SD-037 spec, not from this paper. Second, the projection is GABAergic — the engagement signal is carried by disinhibition. If MECH-280 in REE is implemented as a multiplicative gain on freeze threshold, the sign of the underlying biology is opposite (disinhibition of escape rather than direct elevation of a freeze parameter). This is a parameterisation question that does not invalidate the mechanism but should be flagged for the V4 PAG-subcolumn substrate work where the disinhibitory route may need explicit modelling.

## Confidence reasoning

I am giving this 0.78. Source quality is high (PNAS, projection-specific manipulation, internal anatomical and physiological controls) at 0.88. Mapping fidelity is moderate (0.70) because the named pathway here is LH-to-pons rather than LH-to-PAG — this paper supports the broader LH active-coping system but not the specific PAG channel. Transfer risk is standard for mouse-to-REE (0.32). The aggregate sits below the de Araujo Salgado anchor because the behavioural toggling story in that paper maps more directly onto MECH-280's drive-modulated freeze-to-forage transition than the projection-specific approach-engagement story here. Together the two papers establish the existence and behavioural shape of the LH override system; neither pins down the alpha_override scalar.
