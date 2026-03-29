# V3-EXQ-143 -- MECH-118 Hopfield Familiarity Discriminative Pair

**Status:** FAIL
**Claims:** MECH-118
**Decision:** hybridize
**Seeds:** [42, 123]
**Conditions:** HOPFIELD_ON vs HOPFIELD_ABLATED
**Warmup:** 300 eps x 200 steps  **Memory collection:** 30 eps  **Post-perturb eval:** 50 eps
**Env:** CausalGridWorldV2 size=10, 3 hazards, 4 resources nav_bias=0.35
**Perturbation:** R3 coherent-unfamiliar vector (orthogonal to mean stored pattern, same norm as baseline z_self)
**hopfield_weight:** 0.05  **hopfield_capacity:** 64  **maint_weight:** 0.1  **d_eff_target:** 1.5

## Design

MECH-118 asserts Hopfield-style pattern familiarity is a distinct self-maintenance signal from D_eff coherence. HOPFIELD_ON adds a familiarity pull loss (toward nearest stored z_self pattern) on top of the D_eff homeostatic loss. HOPFIELD_ABLATED uses D_eff homeostasis only. A Regime 3 (coherent-unfamiliar) perturbation is injected at eval start: R3 vector has low D_eff (coherent, D_eff~1) but near-zero Hopfield stability (unfamiliar direction). D_eff homeostasis cannot detect this state. HOPFIELD_ON should recover stability; HOPFIELD_ABLATED should not.

## R3 Perturbation Quality

| Metric | Value | Expectation |
|--------|-------|-------------|
| R3 stability (analytic) | 0.0237 | ~0 (unfamiliar) |
| R3 D_eff (analytic) | 22.194 | ~1 (coherent) |

## Pre-Registered Thresholds

C1: HOPFIELD_ON stab_post >= 0.3 both seeds (familiarity recovery)
C2: HOPFIELD_ABLATED stab_post <= 0.2 both seeds (no spontaneous recovery without Hopfield)
C3: per-seed stab_gap (ON_post - ABL_post) >= 0.08 both seeds (discriminative separation)
C4: D_eff difference |ON - ABL| <= 0.8 both seeds (Hopfield adds familiarity signal, does NOT replace D_eff control)
C5: n_stab_samples >= 50 per condition per seed (data quality)

## Results

| Condition | stab_baseline | stab_post | d_eff_baseline | d_eff_post |
|-----------|---------------|-----------|----------------|------------|
| HOPFIELD_ON      | 1.0000 | 0.9991 | -- | 21.4357 |
| HOPFIELD_ABLATED | 1.0000 | 0.9978 | -- | 21.6266 |

**Per-seed stability gap (ON - ABL): [0.0012, 0.0012]**
**Per-seed D_eff difference: [0.343, 0.0386]**

### HOPFIELD_ON per seed
  seed=42: stab_base=1.0000 stab_post=0.9991 d_eff_base=20.5823 d_eff_post=20.2951 n_stab=1080
  seed=123: stab_base=1.0000 stab_post=0.9990 d_eff_base=22.6341 d_eff_post=22.5764 n_stab=1100

### HOPFIELD_ABLATED per seed
  seed=42: stab_base=1.0000 stab_post=0.9978 d_eff_base=20.5823 d_eff_post=20.6381 n_stab=1080
  seed=123: stab_base=1.0000 stab_post=0.9979 d_eff_base=22.6341 d_eff_post=22.6150 n_stab=1100

## PASS Criteria

| Criterion | Result |
|-----------|--------|
| C1: ON stab_post >= 0.3 (both seeds) | PASS |
| C2: ABL stab_post <= 0.2 (both seeds) | FAIL |
| C3: stab_gap >= 0.08 (both seeds) | FAIL |
| C4: d_eff_diff <= 0.8 (both seeds) | PASS |
| C5: n_stab >= 50 (both conditions both seeds) | PASS |

Criteria met: 3/5 -> **FAIL**

## Interpretation

MECH-118 NOT SUPPORTED: Hopfield familiarity loss does not produce discriminative stability recovery after R3 perturbation. ON stab_post=0.9991; ABL stab_post=0.9978. Possible causes: R3 perturbation not sufficiently unfamiliar (r3_stab_analytic=0.0237 should be near 0); hopfield_weight too small to drive recovery; or D_eff homeostasis incidentally restores familiarity (no dissociation). Re-evaluate after Q-022 dissociation result (EXQ-084d).

## Failure Notes

- C2 FAIL: HOPFIELD_ABLATED stab_post [0.9978, 0.9979] > 0.2 -- ablated condition spontaneously recovers familiarity without Hopfield; R3 perturbation may not be sufficiently orthogonal to familiar subspace or D_eff homeostasis indirectly restores familiarity
- C3 FAIL: per-seed stab gap [0.0012, 0.0012] < 0.08 in some seeds; conditions do not discriminate -- increase hopfield_weight or eval episodes
