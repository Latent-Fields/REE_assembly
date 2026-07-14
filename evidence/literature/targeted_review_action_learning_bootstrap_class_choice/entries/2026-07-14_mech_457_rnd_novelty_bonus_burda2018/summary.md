# Exploration by Random Network Distillation

**Class surveyed:** NOVELTY-DRIVE | **Evidence direction:** mixed | **Confidence:** 0.72

**Source:** Yuri Burda, Harrison Edwards, Amos Storkey et al. (2018). *Exploration by Random Network Distillation.* ICLR 2019 (arXiv:1810.12894)

Burda et al. introduce Random Network Distillation (RND): a fixed randomly-initialised target network maps each observation to features, and a predictor network is trained to match it. Prediction error is high on novel states and decays as they are revisited, giving a smooth differentiable pseudo-count used as an exploration bonus added to extrinsic reward. This is precisely the mechanism REE's V3-EXQ-751 `ac_zworld_rnd` arm instantiated over z_world.

The result that matters for the class-choice: RND was the first method to reach above-average-human performance on Montezuma's Revenge without demonstrations -- but the authors are explicit that the bonus rewards *coverage*, not task success, that the intrinsic signal is non-stationary, and that it vanishes as states become familiar. RND's Montezuma win is contingent on the game's structure making novelty (new rooms) coincide with progress.

This maps onto REE's data almost exactly. RND cleared the 1.0 forage floor (5.22, 3/3 seeds) but plateaued at ~16% of the BC expert (32.72) and ~11% of the local-view ceiling (48.05). In a sparse-pellet forager, 'unvisited cell' and 'pellet reward' are only weakly aligned, so a coverage bonus is expected to get off the floor and then stall -- the textbook shape, not an under-tuned bonus.

Buildability is high (two small MLPs, MSE bonus) -- but that is the problem: RND is the same *class* as REE's existing count-based / EFE novelty substrate (ARC-065, MECH-314). It changes the shape of the novelty estimate (smooth pseudo-count, works in continuous z_world) but adds no mechanism that converts coverage into competence. Swapping count-based -> RND is an intra-class refinement, not a class change. Confidence 0.72: strong evidence, but it argues *against* treating the floor->competent gap as a novelty problem.
