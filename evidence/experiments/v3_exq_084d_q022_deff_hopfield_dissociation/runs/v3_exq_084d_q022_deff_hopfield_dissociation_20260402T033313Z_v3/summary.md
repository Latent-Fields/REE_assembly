# V3-EXQ-084d -- Q-022 D_eff / Hopfield Stability Dissociation

**Status:** FAIL
**Claims:** Q-022, MECH-118, MECH-119
**Seed:** 42  **Warmup:** 300  **Memory eps:** 50  **Analysis eps:** 100
**noise_sigma:** 2.0  **hopfield_capacity:** 64
**alpha_world:** 0.9  (SD-008)

## Three Regimes

| Regime | D_eff (mean) | Stability (mean) | Description |
|--------|-------------|-----------------|-------------|
| R1 Normal   | 20.640 | 0.9996 | raw z_self |
| R2 Noise    | 20.757 | 0.0625 | z_self + N(0,2.0^2) |
| R3 Novelty  | 22.643 | 0.0257 | orthogonal unit vec * norm |

R3 analytic: d_eff=22.643  stability=0.0257  (measured before analysis phase)

## PASS Criteria

| Criterion | Result | Value vs Threshold |
|-----------|--------|--------------------|
| C1: d_eff_R3 < d_eff_R2 - 1.0 | FAIL | 22.643 < 19.757 |
| C2: stab_R3 < stab_R1 - 0.05  | PASS | 0.0257 < 0.9496 |
| C3: d_eff_R2 > d_eff_R1 + 1.0 | FAIL | 20.757 > 21.640 |
| C4: stab_R2 < stab_R1 - 0.05  | PASS | 0.0625 < 0.9496 |

Criteria met: 2/4 -> **FAIL**

## Interpretation

PARTIAL DISSOCIATION: Some metric independence present but below threshold. Either z_self dynamics are too uniform (agent undertrained), or the orthogonal direction chosen for R3 is still within the familiar subspace. Consider longer warmup or stronger env_drift to create richer z_self variety.

## Failure Notes

- C1 FAIL: R3 d_eff=22.643 not < R2 d_eff-1.0=19.757 -- R3 vector may not be coherent (check r3_d_eff_analytic in metrics)
- C3 FAIL: R2 d_eff=20.757 not > R1 d_eff+1.0=21.640 -- noise_sigma=2.0 may be too small to disperse z_self
