# In search of the neural circuits of intrinsic motivation
**Kaplan & Oudeyer (2007) -- Frontiers in Neuroscience**

## What the paper did

Kaplan and Oudeyer, in the inaugural issue of Frontiers in Neuroscience, presented a computational model and series of robotic experiments investigating intrinsic motivation as a mechanism for generating organized developmental sequences. The central hypothesis is that intrinsically motivating activities correspond to expected decrease in prediction error. The system avoids both predictable (already mastered) and unpredictable (too hard to learn) situations, focusing on the intermediate region of maximum expected learning progress.

## Key findings

Robotic experiments showed that this principle generates organized sequences of behavior of increasing complexity, matching several developmental patterns observed in human children. The paper then proposes two neural hypotheses: (1) tonic dopamine acts as a learning progress signal (the rate of improvement in prediction); (2) this progress signal is computed through a hierarchy of cortical microcircuits acting as both prediction and meta-prediction systems. These hypotheses make the computational framework neurobiologically grounded.

## REE translation

Two REE-relevant contributions emerge here. First, the meta-prediction hierarchy is a concrete neural hypothesis for how REE's E1 system could be extended to generate intrinsic exploration motivation: E1 already produces prediction error; adding a running average of E1 loss rate-of-change (its derivative) would implement the learning progress signal. Actions should be prioritized during the infant phase by expected learning progress, not by reward.

Second, the tonic dopamine / learning progress hypothesis maps onto REE's neuromodulation architecture. If tonic dopamine encodes learning progress (and phasic dopamine encodes reward prediction error, per standard Schultz models), then REE's infant stage requires a different neuromodulatory gate than its adult stage: the infant stage uses tonic dopamine to drive exploration, while the adult stage uses phasic dopamine to consolidate successful outcomes.

This is the mechanistic grounding for the two-phase model seen in Griffin et al. (2026) above, and provides a neural implementation target.

## Limitations and caveats

The neural hypotheses (tonic dopamine as learning progress signal) remain speculative -- this has not been directly demonstrated in developing infants. The microcortical prediction hierarchy is highly abstracted. The robotic experiments use simple platforms without safety constraints. The paper is from 2007 and predates much of the modern developmental neuroscience literature on dopamine and intrinsic motivation.

## Confidence reasoning

Foundational paper in the field of intrinsic motivation and developmental robotics; inaugural Frontiers in Neuroscience. Source quality moderate by current standards (Frontiers, 2007). High conceptual value. Confidence 0.73.
