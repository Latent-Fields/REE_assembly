# Summary: Diversity is All You Need: Learning Skills without a Reward Function

**Entry ID:** 2026-05-16_devrobotics_diayn_diversity_eysenbach2019
**Claim IDs:** MECH-194, MECH-195, ARC-050, INV-058

## What the paper does

Eysenbach, Gupta, Ibarz, and Levine (ICLR 2019) present DIAYN (Diversity Is All You Need), which learns diverse skills without a reward function by maximizing the mutual information I(S;Z) between states S and skill latent identifiers Z. A discriminator q(z|s) is trained to identify which skill generated a given state sequence. Skills are diverse to the extent that they visit distinguishable state distributions. Pretrained skills provide good policy initialization for downstream tasks.

## Key findings

The discriminability metric -- the discriminator's ability to identify skills from states -- operationalizes rollout diversity in a principled, information-theoretic way. Skills are diverse if and only if different z values produce distinguishable state trajectories. This is non-Goodharted: maximizing I(S;Z) rewards genuine behavioral separation, not just surface variability. The pretrained skills as initialization finding is the key developmental connection: skill structure learned in an unsupervised phase transfers to downstream tasks even though no task reward was present during pretraining.

## REE mapping

DIAYN provides an implementable diversity metric for the DEV-NEED play stage gates. For DEV-NEED-010 (sensorimotor play) and DEV-NEED-011 (constructive play), the exit criterion includes: are rollout trajectories within play episodes discriminably different from each other? If I(S;Z) measured over play-episode state sequences is near zero, the play type has not produced a genuine behavioral repertoire -- sensorimotor play has collapsed to monostrategy in the synthetic domain.

The pretrained-skills-as-initialization finding maps to ARC-050 and MECH-195. MECH-195 claims that strategy transfers from play while magnitude calibration re-anchors. DIAYN demonstrates exactly this in computational form: the policy structure (which states the agent visits, what trajectory shapes it generates) is learned without reward and transfers; the reward magnitude is entirely absent from the pretraining phase. This is the strongest available computational evidence for strategy-calibration dissociation as a viable mechanism -- though in DIAYN the dissociation is total (no reward at all in pretraining) rather than partial (synthetic reward in play).

## Limitations and caveats

The analogy is structural, not mechanistic. DIAYN has no play frame, no synthetic harm or goal signals, and no bilateral tag architecture. The mutual information metric measures discriminability of state distributions, not the REE-specific distinction between E3 trajectory structure and harm/goal magnitude calibration. Using DIAYN metrics as DEV-NEED gates requires implementing a discriminator over play-episode trajectory distributions, which is an additional architectural commitment not present in current ree-v3.

## Confidence reasoning

Confidence 0.68: high source quality (ICLR), directly implementable metric, strong analogy for strategy-calibration dissociation. Mapping fidelity moderate-low because the play frame architecture is entirely absent. The metric is applicable by adaptation but requires significant REE-specific engineering.
