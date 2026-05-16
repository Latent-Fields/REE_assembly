# DIAYN: Diversity is All You Need (Eysenbach et al., ICLR 2019)

## What the paper did

Eysenbach, Gupta, Ibarz, and Levine asked whether an agent could learn a rich repertoire of useful behaviours without ever receiving a task reward. Their answer is DIAYN: train a maximum-entropy policy conditioned on a discrete skill variable Z by maximising the mutual information I(S;Z) between visited states and the active skill. A discriminator that estimates I(S;Z) produces a pseudo-reward driving each skill to visit distinguishable state regions. No human reward, no curriculum -- just information-theoretic pressure to make each skill look different from the others.

## Key findings

The theory is unusually clean. On gridworlds, the unique optimum of the DIAYN objective is to partition the state space evenly across skills, each skill maintaining a uniform distribution over its own partition. This is the formalisation of what "no monostrategy" should mean: not just "some diversity exists" but "each skill mode occupies a structurally distinct region, and none collapses onto another." In practice, across MuJoCo benchmarks (HalfCheetah, Hopper, Ant), DIAYN discovers interpretable locomotion primitives -- forward and backward running at various speeds, flips, jumping, turning -- without task reward. The skills are reusable: they provide parameter initialisation that accelerates downstream fine-tuning, sometimes solving sparse-reward tasks without additional task-reward training.

## Translation to REE

REE's V_s monostrategy bottleneck is precisely the phenomenon DIAYN is designed to prevent: gradient-based training on a single policy parameterisation finds the dominant attractor (the route that satisfies the forward model F most efficiently) and ignores other behavioural modes. DIAYN's structural fix: introduce a context variable indexing which mode should be active, and add a discriminability term rewarding the policy for visiting mode-distinguishable states under that context. This maps onto ARC-065 (behavioral diversity generation requires a structured diversity channel, not noise) and MECH-314 (curiosity/novelty bias). The implication is that MECH-314 as currently implemented -- novelty on individual steps -- is the wrong level of analysis. What is needed is discriminability across trajectory-level state distributions, conditioned on context. This is a qualitatively different signal from step-level novelty.

## Limitations and caveats

DIAYN operates in pure pre-training with no task reward. REE trains with concurrent task reward, and EXQ-571 showed that forward model F dominates E3 score variance (~0.89 fraction). A diversity term added to E3 scoring will be swamped by F unless bias scale is raised 5-10x (calibration WP-B). DIAYN's solution -- temporal separation of diversity learning from task learning -- may be more directly applicable than adding diversity bias to a live task-reward pipeline. The navigation domain (vs locomotion) also means some skill types discovered by DIAYN are not directly analogous to REE's route-mode diversity problem.

## Confidence

0.80. Strong theory, top venue, clean mechanism. Transfer risk is the main moderator: REE's concurrent task reward and navigation domain differ from DIAYN's pre-training locomotion setting.
