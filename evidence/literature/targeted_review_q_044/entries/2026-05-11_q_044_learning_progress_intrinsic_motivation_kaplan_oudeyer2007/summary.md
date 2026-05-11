# Kaplan & Oudeyer 2007 — In search of the neural circuits of intrinsic motivation

**Citation.** Kaplan F, Oudeyer PY. (2007). In search of the neural circuits of intrinsic motivation. *Frontiers in Neuroscience* 1(1):225-36. [DOI](https://doi.org/10.3389/neuro.01.1.1.017.2007). PMID 18982131.

## What the paper did

Kaplan and Oudeyer propose a specific computational definition of intrinsic motivation that distinguishes it from older curiosity formulations. Intrinsic motivation, they argue, is not a raw novelty bonus and not a raw uncertainty bonus; it is a bonus on **expected decrease in prediction error** — the rate at which the agent is currently learning about a state, situation, or skill. An agent driven by this signal avoids two failure modes: situations so predictable that no learning happens, and situations so chaotic that learning is impossible. The signal pushes the agent toward what they call the "learnable middle band": situations whose dynamics are tractable enough to model but not yet fully modelled.

The paper supports this thesis with robotic-simulation experiments showing that a learning-progress-driven agent organises its exploration into developmental phases of increasing complexity, broadly mirroring observations from infant developmental psychology. They also propose a neural substrate hypothesis: tonic dopamine carries the learning-progress signal, and a hierarchy of microcortical predictive circuits computes it. The neural hypothesis is explicitly framed as a prediction rather than as established empirical finding.

## Relevance to Q-044

This is the foundational anchor for MECH-314c (learning-progress curiosity). Q-044 asks whether MECH-314a (novelty), MECH-314b (uncertainty-driven curiosity), and MECH-314c (learning progress) are three distinct mechanisms or three readings of one underlying quantity. Kaplan & Oudeyer 2007 supplies the algorithmic argument for treating learning progress as DERIVATIVE in a way the other two are not: it is not the prediction-error signal, but its rate of change. Two states with the same novelty score and the same uncertainty score can have very different learning-progress scores — one might be in a phase of rapid model improvement, the other in plateau.

For REE's three-arm ablation, this gives MECH-314c a distinctive prediction. With MECH-314c disabled, the agent should fail to abandon two kinds of regions: irreducibly noisy ones (which still register as novel and uncertain, so MECH-314a and MECH-314b would keep the agent there), and mastered ones (where novelty and uncertainty are both low but learning has plateaued, so the agent should move on but doesn't have the signal). The 314c-OFF failure signature is "stuck in plateaus" — qualitatively distinct from 314a-OFF "won't visit new states" and 314b-OFF "won't choose uncertain options".

## Caveats — the weakest-anchored of the three sub-flavours

I have to be honest: of the three MECH-314 sub-flavours, learning-progress is the most theoretically motivated and the least empirically anchored. Kaplan & Oudeyer 2007 is a computational paper with robotic simulations, not an empirical demonstration in humans or animals that a specific neural signal tracks learning progress. The tonic-dopamine hypothesis is in tension with Wittmann 2007's evidence that the phasic SN/VTA signal tracks novelty — both papers cite the dopamine system, but in different roles, and the empirical literature has not cleanly arbitrated.

The Schmidhuber/Pathak intrinsic-motivation tradition the ARC-065 family doc cites runs in parallel to Kaplan & Oudeyer and supplies the formal ML-side anchor. But that tradition has no neural anchoring at all — it is purely algorithmic. So MECH-314c sits on a combination of strong algorithmic motivation and weak empirical neural evidence.

For Q-044, this means a "MECH-314c-OFF produces no distinct signature" outcome — i.e., 314c collapses into 314a or 314b — would not be surprising; the existing evidence makes the dissociation more theoretical than well-tested.

I am also conscious that learning progress and uncertainty are operationally correlated: uncertainty decreases as learning progresses, and the rate of decrease IS learning progress. Dissociating them experimentally requires tasks where some regions have plateaued uncertainty (irreducible noise) and others have rapidly-decreasing uncertainty (active learning). This is not standard practice in human curiosity experiments, so the empirical literature does not yet support a clean three-way ablation prediction.

## Confidence reasoning

I assign 0.62, the lowest in the Q-044 set. Source quality (0.65) is modest (Frontiers in Neuroscience, theoretical with robotic support). Mapping fidelity (0.80) is high because the algorithmic distinction Kaplan & Oudeyer propose is exactly what MECH-314c instantiates. Transfer risk (0.50) is the highest in this lit-pull because the tonic-dopamine ↔ learning-progress mapping is a theoretical prediction rather than an empirical finding. The 0.62 aggregate weights the algorithmic anchoring more than the neural anchoring, with appropriate skepticism reflected in the failure_signatures.

For Q-044's three-arm ablation, this entry is the load-bearing reason to KEEP MECH-314c as a candidate substrate rather than collapse it into 314a or 314b prematurely; it is NOT load-bearing for the prediction that the ablation will show three independent failure modes.
