# Cavanagh et al. 2011 -- Mediofrontal cortex sets a conflict-scaled decision threshold the STN implements

**Claim touched:** ARC-063 design element (ii), tolerance-gated rule availability. Cross-ref MECH-309 (the non-Bayesian rule-creator), ARC-062.

## What the paper did
Cavanagh and colleagues combined human EEG, the drift-diffusion model of decision making, intracranial subthalamic-nucleus (STN) recordings, and STN deep-brain stimulation (DBS) in Parkinson's disease. The drift-diffusion decomposition let them read off a *decision threshold* -- how much evidence must accumulate before a choice is committed -- trial by trial. They found that on high-conflict trials, increased medial-prefrontal (mPFC) theta power (4-8 Hz) predicted a *higher* threshold: the cortex, sensing conflict, raised the bar and bought time. STN DBS reversed this coupling, producing impulsive choice, and STN-area slow-frequency activity (2.5-5 Hz) rose specifically during high-conflict decisions.

## Why it matters for ARC-063
This is the cleanest empirical, *causal* grounding I have found for the kind of gate ARC-063 posits. The tolerance principle says a candidate rule should not become available for use until its accumulated support clears a bar -- and that the bar should *rise* when there is competition or accumulated exception. Cavanagh shows exactly that shape in the brain: a frontally-set, dynamically-adjusted threshold, implemented through a cortico-subthalamic pathway, that scales with conflict and whose removal (DBS) yields premature, under-gated commitment. The "hold your horses" architecture is the biological skeleton of a tolerance gate.

## The honest caveat
What the paper measures is a *response* threshold -- a drift-diffusion boundary on a motor choice -- not a gate on which abstract *rule* becomes available. ARC-063 borrows the mechanism (frontal set-point, conflict scaling, STN implementation) and re-points it at a different target. That re-pointing is biologically motivated but is an architectural extension, not a demonstrated identity; I have logged it as the mapping caveat and held mapping_fidelity at 0.55 accordingly. There is also a clinical-to-healthy and motor-to-cognitive transfer to discount.

## Confidence
0.66 -- supports. The source quality is high (Nature Neuroscience, with a causal DBS manipulation that is rare for this kind of claim), and the mechanism maps onto the tolerance gate with unusual precision. I withhold the top band only because the target of the threshold (response vs rule availability) is not the same, so this grounds the *mechanism* of ARC-063's gate, not its *scope*.