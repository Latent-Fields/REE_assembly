# Large-Scale Study of Curiosity-Driven Learning

**Class surveyed:** NOVELTY-DRIVE | **Evidence direction:** weakens | **Confidence:** 0.7

**Source:** Yuri Burda, Harrison Edwards, Deepak Pathak et al. (2018). *Large-Scale Study of Curiosity-Driven Learning.* ICLR 2019 (arXiv:1808.04355)

This large-scale study runs *purely* curiosity-driven agents (ICM-style forward-model prediction error, no extrinsic reward) across 54 environments to characterise what a novelty drive optimises on its own. It is the canonical documentation of both the strength and the fatal limitation of the class.

Two findings pull opposite ways. Pure curiosity produced competent Atari play on many games -- but *because* game designers set up curricula where extrinsic reward aligns with novelty. Where that alignment breaks, curiosity fails: the paper is the reference for the noisy-TV problem, where an agent that finds a stochastic source parks in front of it forever because prediction error never decays.

For REE this is diagnostic gold. It explains why the ICM arm (V3-EXQ-751 `ac_zworld_icm`) did not clear the floor (0.22) despite higher intrinsic reward than RND: forward-model curiosity is the most noisy-TV-vulnerable member of the class. More importantly it tells us the RND plateau REE observed is the *theoretically-expected* behaviour of the whole novelty class on a task where novelty and reward are only partly aligned -- not a tuning failure that a bigger bonus would fix.

The entry weakens the 'build another/better curiosity mechanism' route and reinforces that REE already owns this class. Its value is as a bound on the class, not as new substrate; re-testing forward-model curiosity is explicitly low-value. Confidence 0.70.
