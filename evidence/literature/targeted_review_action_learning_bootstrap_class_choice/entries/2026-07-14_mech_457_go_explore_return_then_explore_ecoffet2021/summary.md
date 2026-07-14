# First return, then explore

**Class surveyed:** MEMORY / GO-EXPLORE | **Evidence direction:** supports | **Confidence:** 0.82

**Source:** Adrien Ecoffet, Joost Huizinga, Joel Lehman et al. (2021). *First return, then explore.* Nature 590:580-586 DOI: 10.1038/s41586-020-03157-9

Ecoffet et al. diagnose the two failure modes that make intrinsic-motivation exploration plateau: *detachment* (the agent forgets how to reach a promising frontier once the local novelty bonus is consumed) and *derailment* (stochastic actions prevent reliable return to a known-good state). Their fix is not a better bonus but a memory: an archive of discovered states plus a deterministic return-then-explore loop -- first return to a promising archived state, then explore onward from it.

The load-bearing datapoint for REE is the head-to-head on the same benchmark: Go-Explore scored >43,000 mean on Montezuma's Revenge versus RND's ~11,000, solved all previously-unsolved Atari games, and exceeded human performance on Pitfall where prior intrinsic-motivation methods scored ~0. The gap between RND and Go-Explore on identical hard-exploration tasks is direct evidence that the missing ingredient is memory + reliable return -- a credit/archival mechanism -- not a stronger novelty signal.

This maps directly onto REE's floor->competent gap. RND stalled at 5.22 exactly as a detached novelty bonus is expected to. In a small gridworld the mechanism is cheap: the archive is a hash over discretised z_world/position, and 'return' is a trajectory replay or reset-to-state. It is more than reward shaping (needs an archive + a return controller), but a gridworld is the easiest possible place to build it.

Crucially for the duplication question, Go-Explore does NOT compute a per-step novelty reward -- it is orthogonal to RND/ICM and to REE's curiosity substrate; if novelty is used at all it becomes an archive-selection heuristic, not a reward term. It is also complementary to REE's existing hippocampal backward_credit_sweep (Go-Explore selects where to start exploring; reverse-replay propagates credit once reward is found). Confidence 0.82 -- the strongest single 'different class' candidate.
