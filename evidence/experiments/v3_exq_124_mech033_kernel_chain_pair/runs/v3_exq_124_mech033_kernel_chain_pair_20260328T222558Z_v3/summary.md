# V3-EXQ-124 -- MECH-033 Kernel Chaining Interface Discriminative Pair

**Status:** FAIL
**Claim:** MECH-033
**Proposal:** EXP-0023 / EVB-0018
**Seeds:** [42, 123]
**alpha_world:** 0.9  (SD-008)
**Warmup:** 400 eps  **Eval:** 50 eps
**n_candidates:** 8  **horizon:** 5  **n_cem_iterations:** 3

## Design

KERNEL_CHAIN_ON: HippocampalModule CEM in action-object space O. Terrain prior seeds distribution; E2 action_object kernels chain across horizon; residue field scores trajectories; elite refit.
KERNEL_CHAIN_ABLATED: Random candidate actions; E3 selects best via one-step E2 world_forward lookahead. No kernel chaining.
Both conditions train E1, E2, E3 harm_eval, and hippocampus identically.

## Pre-Registered Thresholds

C1: harm_rate_ABLATED - harm_rate_CHAIN >= 0.03  (absolute harm reduction)
C2: relative_reduction >= 0.15  (15pct relative reduction)
C3: harm_rate_CHAIN < harm_rate_ABLATED for ALL seeds  (consistency)
C4: min_contacts_ablated >= 20  (data quality)
C5 (diagnostic): mean_residue_CHAIN <= mean_residue_ABLATED

## Aggregate Results

| Metric | KERNEL_CHAIN_ON | KERNEL_CHAIN_ABLATED | Delta | Pass |
|--------|----------------|---------------------|-------|------|
| harm_rate (C1 delta) | 0.6211 | 0.0568 | -0.5643 | NO |
| relative_reduction (C2) | -9.9342 | -- | -- | NO |
| seed consistency (C3) | [False, False] | -- | -- | NO |
| min_contacts_ablated (C4) | -- | 369 | -- | YES |
| mean_residue (C5 diag) | 0.0750 | 0.0750 | -- | n/a |

## Interpretation

MECH-033 NOT SUPPORTED: Kernel chaining provides no meaningful planning advantage. harm_rate_CHAIN=0.6211, harm_rate_ABLATED=0.0568, delta=-0.5643. Random candidate generation with E3 selection performs comparably to hippocampal CEM in action-object space. The kernel chaining interface does not preserve causal continuity in a way that reduces harm at this scale.

## Per-Seed (KERNEL_CHAIN_ON)

  seed=42: harm_rate=0.7462 n_contacts=585 n_total=784 mean_residue=0.0779 train_harm_steps=54363 train_e2_world_steps=79600
  seed=123: harm_rate=0.4961 n_contacts=694 n_total=1399 mean_residue=0.0721 train_harm_steps=54328 train_e2_world_steps=79600

## Per-Seed (KERNEL_CHAIN_ABLATED)

  seed=42: harm_rate=0.0754 n_contacts=516 n_total=6841 mean_residue=0.0779
  seed=123: harm_rate=0.0382 n_contacts=369 n_total=9664 mean_residue=0.0721

## Failure Notes

- C1 FAIL: harm_rate delta=-0.5643 (needs >=0.03). Kernel chaining does not produce a meaningful absolute harm reduction. Possible causes: (1) E2 world_forward model not well trained (check train_e2_world_steps); (2) terrain prior does not learn hazard structure; (3) 400 warmup insufficient for hippocampal CEM to calibrate.
- C2 FAIL: relative_reduction=-9.9342 (needs >=0.15). Chaining eliminates less than 15pct of ablated-condition harm. Chaining may add planning signal but it is weak relative to baseline.
- C3 FAIL: per_seed direction inconsistent ([False, False]). Chaining did not consistently reduce harm across both seeds.
