# V3-EXQ-148 -- Q-003: R-Field Dimensionality Discriminative Pair

**Status:** FAIL
**Claim:** Q-003
**Decision:** retire_ree_claim
**Q-003 guidance:** inconclusive_collapsed
**Seeds:** [42, 123]
**Conditions:** SCALAR vs VECTOR (residue_dim=3)
**Warmup:** 300 eps x 200 steps  **Eval:** 100 eps x 200 steps
**Env:** CausalGridWorldV2 size=10, 2 hazards, 3 resources

## Design

Q-003 asks whether R(x,t) should be scalar or vector. SCALAR condition uses the standard ResidueField.evaluate() (1-D output). VECTOR condition uses VectorResidueWrapper.evaluate_vector() producing 3 dims: harm_intensity (standard RBF), harm_recency (EMA-decayed weights), and benefit_proximity (benefit terrain from ARC-030). E3 receives the vector fused into z_world via a small projection head (Linear(world_dim+3, world_dim)) trained jointly.

Key discriminator: harm_ratio = mean_harm_vector / mean_harm_scalar. If vector reduces harm by >= 8% (ratio < 0.92) AND dims are non-degenerate AND benefit dim is non-zero --> vector preferred.

## Pre-Registered Thresholds

C1: harm_ratio < 0.92 (both seeds -- vector reduces harm >= 8%)
C2: dim_var > 0.01 for dims 0+1 (non-degenerate vector)
C3: benefit_dim2_mean > 0.01 (benefit dim non-zero)
C4: harm_ratio < 1.1 (vector does not regress harm)
C5: C1 results consistent across seeds

## Results

| Condition | mean_harm | mean_benefit |
|-----------|-----------|-------------|
| SCALAR | 1.19401 | 0.14369 |
| VECTOR | 1.19401 | 0.14369 |

**harm_ratio (vector/scalar) per seed: [1.0, 1.0]**
**mean_harm_ratio: 1.0000**

### Vector Dimensionality Check

| Metric | Value |
|--------|-------|
| dim_var_0 (harm intensity) | 0.0046 |
| dim_var_1 (harm recency)   | 0.0001 |
| dim_var_2 (benefit prox.)  | 0.0027 |
| benefit_dim2_mean          | 0.0005 |

### Per-Seed SCALAR
  seed=42 cond=SCALAR: harm=1.18236 benefit=0.14198
  seed=123 cond=SCALAR: harm=1.20566 benefit=0.14541

### Per-Seed VECTOR
  seed=42 cond=VECTOR: harm=1.18236 benefit=0.14198 dim_var=(0.0046,0.0000,0.0020) benefit_dim2=0.0004
  seed=123 cond=VECTOR: harm=1.20566 benefit=0.14541 dim_var=(0.0045,0.0001,0.0035) benefit_dim2=0.0005

## PASS Criteria

| Criterion | Result |
|-----------|--------|
| C1: harm_ratio < 0.92 (both seeds) | FAIL |
| C2: dim_var > 0.01 dims 0+1 (both seeds) | FAIL |
| C3: benefit_dim2 > 0.01 (both seeds) | FAIL |
| C4: harm_ratio < 1.1 (no regression) | PASS |
| C5: C1 seed-consistent | PASS |

Criteria met: 2/5 -> **FAIL**

## Interpretation

Q-003 INCONCLUSIVE: vector dims collapsed. harm_ratio=1.0000. dim_var=(0.0046,0.0001,0.0027). All dims track the same pattern -- benefit terrain not populated or recency RBF collapses to intensity. Q-003 not answerable with current data density.

## Failure Notes

- C1 FAIL: harm_ratio [1.0, 1.0] not < 0.92. Vector residue field does not reduce harm avoidance by >= 8%. Possible causes: (1) E3 cannot learn a useful linear combination of 3 residue dims with the current training budget; (2) benefit terrain is not rich enough to differentiate from harm dims; (3) random actions reduce the signal from residue field geometry.
- C2 FAIL: dim_var (0.0046,0.0001,0.0027) -- one or more dims < 0.01. Vector dims have collapsed: all three dimensions track the same scalar pattern. The vector residue field adds no new information. Q-003 is not answerable at current scale with this implementation.
- C3 FAIL: mean_benefit_dim2=0.0005 < 0.01. Benefit terrain (dim 2 of vector) is near-zero -- insufficient benefit events accumulated during training to populate the benefit RBF field. Benefit terrain is not contributing to the vector's informational content.
