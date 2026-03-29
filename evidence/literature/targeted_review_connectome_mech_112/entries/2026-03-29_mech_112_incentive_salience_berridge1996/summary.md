# Berridge (1996) -- Food reward: brain substrates of wanting and liking

**Claim tested:** MECH-112 (E3 requires a structured latent goal representation distinct from harm avoidance)

## What the paper did

Berridge (1996) set out to ask a deceptively simple question: what does the brain actually do when it rewards an animal? The prevailing assumption in the 1980s and early 1990s was that mesolimbic dopamine was the brain's pleasure or reward system, full stop. Dopamine meant reward; more dopamine meant more pleasure; lesion the system and reward disappears. Berridge challenged this by systematically depleting dopamine in rats via 6-OHDA lesion and measuring what actually happened to both hedonic responses (affective facial reactions to sweet and bitter tastes) and motivational behavior (approach to and consumption of food). The dissociation he found was striking: dopamine-depleted rats showed completely normal hedonic reactions -- the same positive orofacial responses to sucrose, the same aversive gapes to quinine -- but failed entirely to approach or consume food. They would starve unless fed by the experimenter, yet if food was placed in their mouths, they showed normal pleasure reactions.

## Key findings relevant to MECH-112

The central finding is the functional and neural dissociation between wanting (incentive salience, mesolimbic dopamine, nucleus accumbens core and shell, amygdala) and liking (hedonic impact, opioid/GABA/benzodiazepine systems, NAc shell hedonic hotspots, ventral pallidum, brainstem gustatory relays). These are not two names for the same process. You can have one without the other. The wanting system generates prospective, anticipatory motivation -- the approach gradient that pulls an animal toward a goal state before contact. The liking system generates hedonic evaluation at the moment of contact -- the consummatory pleasure signal. Both systems are anatomically distributed, but their substrates are separable.

Crucially for MECH-112, wanting is inherently prospective and persistent. It must be active before contact to generate approach. Liking is consummatory -- it spikes at contact and then dissipates. This temporal profile difference is architecturally significant: a system that only has liking cannot generate the sustained approach gradient needed to navigate toward a goal state across a multi-step trajectory.

## REE translation

MECH-112 claims that E3 requires a structured latent goal representation (z_goal, a positive attractor in z_world or z_goal sub-space) distinct from harm avoidance. Berridge 1996 provides the empirical existence proof that such a distinction is not just architecturally convenient but biologically necessary. The brain maintains a wanting system (z_goal analog, dopaminergic, prospective, persistent) separate from the hedonic evaluation system (benefit_eval_head analog, opioid, consummatory, reactive). REE currently has a benefit_eval_head that trains on benefit_exposure at receipt -- this is the liking system. What it lacks, and what MECH-112 says it needs, is a z_goal latent that generates the smooth approach gradient from distance -- the wanting system. The Berridge 1996 dopamine depletion experiment shows exactly what happens when wanting fails with liking intact: the animal cannot approach or consume even though it will enjoy food if delivered. This is the degenerate policy MECH-112 is designed to prevent.

## Limitations and caveats

The experimental model is food-seeking in rats under pharmacological dopamine depletion -- a more radical intervention than any manipulation possible in a neural network. REE's z_goal is a learned latent representation, not a biological dopamine circuit, so the specific implementation differs. The paper also predates the full characterisation of NAc shell hotspot anatomy and the distinction between absolute wanting and relative incentive salience (amplified by drive states, stress, and cue conditioning), which are relevant to SD-012 but not directly addressed here. The temporal persistence property of wanting across multi-step trajectories is inferred from the behavioral dynamics rather than directly measured.

## Confidence reasoning

Confidence is 0.82. The paper is rigorous primary experimental data from the originator of the wanting/liking framework, with a clean dissociation. The mapping to MECH-112 is structurally direct: wanting maps to z_goal, liking maps to benefit_eval_head. The main source of uncertainty is the implementation gap -- biological dopamine versus learned latent -- which is real but does not undermine the architectural principle.
