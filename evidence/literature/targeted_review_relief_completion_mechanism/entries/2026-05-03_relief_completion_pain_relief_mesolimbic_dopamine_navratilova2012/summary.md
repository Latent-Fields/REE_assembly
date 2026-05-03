# Navratilova, Xie, Okun et al. 2012 — Pain relief produces negative reinforcement through activation of mesolimbic reward-valuation circuitry

## What the paper did

The Porreca lab took rats with experimental postsurgical pain (hindpaw incision) and asked, mechanistically, what circuitry the *relief* of that ongoing pain engages. They combined three methods in the same animals and the same paradigm: conditioned place preference for the context paired with pain relief, single-unit recording from VTA dopaminergic neurons during pain relief, and microdialysis of dopamine in the nucleus accumbens. They also tested whether dopamine antagonism in the NAc was sufficient to block the place preference.

## Key finding

Peripheral nerve block — which removes the painful afferent input — produced robust conditioned place preference (the rats learned to seek the context where the relief had occurred), activated VTA dopaminergic neurons, and elevated dopamine release in the nucleus accumbens. The behavioural preference was abolished by injecting dopamine antagonists into the NAc. So pain relief is not merely *correlated* with reward-circuit activity — the dopamine signal in the NAc is *necessary* for the reinforcing effect of relief to be expressed.

This is the cellular complement to the Andreatta 2012 structural dissociation. Where Andreatta showed that conditioned relief required the ventral striatum (and not the amygdala), Navratilova shows that the relevant ventral-striatal signal is dopaminergic, originates in the VTA, and is sufficient to support negative-reinforcement learning when activated.

## How it translates to REE

For the REE architectural decision, this entry pins down the *same machinery* claim of Model 1 at the cellular level. The relief-completion event, in biological systems, does fire the canonical mesolimbic dopamine pathway — the same VTA-to-NAc-shell circuit that handles reward-based reinforcement. This means that an REE implementation can model relief and goal-achievement as feeding a shared release/tag pipeline (MECH-057a beta-gate-drop, MECH-091 phase-reset, MECH-094 categorical write gate) without violating the biology. The polarity is set at the input — what counts as "good" is the suffering-drop event, not a reward-onset event — but the downstream consolidation is shared.

Combined with the Andreatta 2012 result, this is strong evidence that "things that reduce suffering" should be tagged in the same approach-attractor structure as "things liked", with the proviso that the *predictive* encoding of relief-cues may have a parallel substrate (per the Kreutzmann and Meyer entries in this slate).

## Limitations and caveats

The paradigm is acute postsurgical pain. The relief signal here is the offset of an ongoing physical nociceptive input, not the resolution of a long-horizon goal-shaped suffering state of the kind REE's SD-011 dual-stream architecture models. The transfer assumes that the mesolimbic relief-DA signal is general across kinds-of-suffering rather than specific to acute physical pain. Subsequent Porreca-lab work (Xie 2014, Navratilova-Atcherley-Porreca 2015 review) and convergent ACC-opioid findings make that assumption more defensible, but it is still a transfer step.

The paper does not directly compare the temporal profile of relief-DA to that of reward-DA, so the strong claim "same machinery" rather than "overlapping machinery" is not fully tested. For REE this matters less than it might — the architectural decision is whether to build a parallel pipeline or reuse the existing one, and the empirical answer is that the existing one is engaged.

## Confidence

Source quality is high (PNAS, three converging methods, well-replicated by the same lab and others since). Mapping fidelity is high because this is the precise mechanism the architectural question turns on. Transfer risk is moderate, mainly because the suffering modelled in REE is wider than postsurgical pain. Net confidence 0.84, supports.
