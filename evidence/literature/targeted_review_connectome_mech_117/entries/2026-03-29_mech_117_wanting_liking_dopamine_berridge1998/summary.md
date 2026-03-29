# Berridge and Robinson (1998) -- What is the role of dopamine in reward: hedonic impact, reward learning, or incentive salience?

**Claim tested:** MECH-117 (wanting and liking signals are functionally dissociable in trajectory scoring)

## What the paper did

This is one of the most consequential papers in reward neuroscience. Berridge and Robinson asked a precise question that had been implicit but unresolved since the discovery of dopamine's role in reward: does dopamine mediate pleasure, or something else? Their approach was systematic. They nearly completely depleted dopamine in rats via bilateral 6-OHDA lesions, then measured three things separately: (1) hedonic reactions to sweet and bitter tastes via the taste reactivity paradigm (facial expressions that are species-conserved across mammals), (2) the capacity to learn new hedonic values via taste aversion conditioning, and (3) pharmacological enhancement of palatability via benzodiazepine administration. Each of these tests a different component of reward that prior theories had conflated with dopamine. All three tests showed normal function in dopamine-depleted rats. What these rats could not do was approach food or water voluntarily.

## Key findings relevant to MECH-117

The dissociation is triple-confirmed. Dopamine is not required for liking (normal hedonic reactions). Dopamine is not required for reward learning (normal taste aversion conditioning). Dopamine is not required for pharmacological hedonic enhancement (normal benzodiazepine palatability amplification). But dopamine is required for wanting -- for the prospective, anticipatory motivation that drives approach to food before contact. The paper concludes that dopamine mediates incentive salience: the transformation of a neutral stimulus or anticipated outcome into a motivationally attractive target. This is a gradient signal that rises as the agent approaches the goal, driven by dopaminergic activity triggered by predictive cues.

MECH-117 predicts exactly this profile in the REE architecture: benefit_eval_head (liking) produces a sharp proximity spike near the resource cell -- high near contact, zero elsewhere. z_goal_latent (wanting) produces a smooth gradient rising from distance -- goal_proximity = 1/(1 + MSE(z_world, z_goal)), positive from many steps away. The resource relocation test (moving resource from L1 to L2 at step 1500) tests whether the signals dissociate temporally: liking should redirect within approximately 10 steps (benefit_eval_head updates quickly because it trains on current benefit_exposure), while wanting should maintain approach toward L1 for at least 25% of the next 200 steps (z_goal decays slowly, incentive salience outlasts the location change).

## REE translation

Berridge and Robinson 1998 provide the primary biological grounding for MECH-117. The wanting/liking dissociation in the dopamine depletion paradigm is a direct empirical analog of the spatial and temporal profile differences MECH-117 predicts for z_goal_latent versus benefit_eval_head in REE trajectory scoring. The wanting signal is prospective, graded, and spatially extended (the gradient rises from distance); the liking signal is consummatory, sharp, and spatially local (spikes at contact). This is not a quantitative difference but a qualitative functional distinction arising from different neural substrates -- precisely what MECH-117 requires to be true of the two REE signals.

## Limitations and caveats

The dopamine depletion model is a global intervention -- all mesolimbic dopamine is removed, which is more drastic than any operation possible in REE. The biological wanting system's persistence properties may depend on the specific dynamics of dopamine receptor sensitisation and cue conditioning over a lifetime, which would not emerge from REE's training regime without deliberate architectural specification (the slow z_goal decay parameter in MECH-117's formulation). The paper also does not directly measure the spatial gradient profile of incentive salience -- the conclusion that wanting is graded from distance is inferred from approach dynamics and blocking experiments rather than from direct measurement.

## Confidence reasoning

Confidence is 0.85. This is primary experimental data, rigorous pharmacological dissection, from the originator of the framework. The dissociation is clean and has been replicated across many subsequent studies. The mapping to MECH-117 is structurally direct: wanting maps to z_goal_latent spatial gradient, liking maps to benefit_eval_head proximity spike. This is the strongest single piece of literature support for MECH-117.
