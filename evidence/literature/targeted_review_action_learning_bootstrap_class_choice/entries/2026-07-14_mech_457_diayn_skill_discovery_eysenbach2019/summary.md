# Diversity is All You Need: Learning Skills without a Reward Function

**Class surveyed:** OPTIONS / SKILLS | **Evidence direction:** mixed | **Confidence:** 0.6

**Source:** Benjamin Eysenbach, Abhishek Gupta, Julian Ibarz et al. (2019). *Diversity is All You Need: Learning Skills without a Reward Function.* ICLR 2019 (arXiv:1802.06070)

DIAYN learns a set of distinguishable skills with no environment reward by maximizing the mutual information between a latent skill code z and the states visited: a discriminator that predicts z from state provides the intrinsic reward, pushing skills to be diverse and distinguishable, while each skill's policy is kept maximum-entropy. The learned skills can then be composed or fine-tuned for downstream tasks.

It is directly on-point for 'convert exploration into reusable competence' -- DIAYN turns unsupervised exploration into a library of reusable behaviours that measurably accelerate downstream learning, a capability the flat-policy + RND arm lacks (RND is transient, per-episode, nothing carried forward). This is the genuinely distinct thing the options/skills class adds.

The catch for REE's substrate is decisive on cost/benefit: DIAYN's diversity payoff shines in high-dim continuous control where the state space is huge; in a tiny discrete forage-world the number of usefully-distinct skills is small and a novelty bonus may already reach most of them, so the marginal floor->competent gain may be modest. And DIAYN is the heaviest build of the candidate classes -- a skill-conditioned policy, a separately-trained discriminator, a max-entropy objective, and a two-level control loop.

Confidence 0.60, evidence_direction mixed: the class adds a real capability but the strongest instantiation is the worst-fitting to a small substrate. The lightweight middle path (hand-specified options + termination bracketing, per Sutton 1999 and the striatal-chunking biology) is the cheap probe; full DIAYN-class discovery should be skipped unless cross-task skill reuse becomes the actual target.
