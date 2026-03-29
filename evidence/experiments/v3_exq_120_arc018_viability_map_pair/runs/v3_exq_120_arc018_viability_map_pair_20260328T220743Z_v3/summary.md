# V3-EXQ-120 -- ARC-018 Viability Map Discriminative Pair

**Status:** PASS
**Claim:** ARC-018
**Decision:** retain_ree
**Seeds:** [42, 123]
**Conditions:** VIABILITY_MAP_ON (residue+hippo+precision) vs VIABILITY_MAP_ABLATED (no terrain, no precision update)
**alpha_world:** 0.9  (SD-008)
**Warmup:** 400 eps  **Eval:** 50 eps  **Steps/ep:** 200
**Env:** CausalGridWorldV2 size=6, 4 hazards, use_proxy_fields=True, nav_bias=0.4

## Pre-Registered Thresholds

C1: harm_reduction_frac >= 0.15  (MAP_ON reduces harm by >=15%)
C2: residue_events_min_on >= 20  (viability map actually populated)
C3: consistent harm reduction for ALL seeds  (seed_pair_pass >= 2)
C4: n_harm_min >= 20  (data quality gate)
C5: active_centers_min_on >= 5  (viability map covers enough latent space)

## Results

| Condition | harm_rate | harm_events | steps |
|-----------|----------|------------|-------|
| MAP_ON  | 0.0058 | 116 | 20000 |
| MAP_ABLATED | 0.7471 | 1055 | 1412 |

**harm_reduction_frac: +0.9922**  (0.7471 -> 0.0058)
**residue_events_min_on: 3556**  **active_centers_min_on: 32**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: harm_reduction >= 0.15 | PASS | 0.9922 |
| C2: residue_events_min >= 20 | PASS | 3556 |
| C3: consistent across seeds | PASS | 2/2 |
| C4: n_harm_min >= 20 | PASS | 54 |
| C5: active_centers_min >= 5 | PASS | 32 |

Criteria met: 5/5 -> **PASS**

## Interpretation

ARC-018 SUPPORTED: Hippocampal viability map provides measurable harm reduction: MAP_ON=0.0058 vs MAP_ABLATED=0.7471 (99.2% reduction). Residue field populated (min events=3556, active centers=32). Consistent across all 2 seeds. E2 rollout scoring (terrain prior) enables the viability map navigation advantage.

## Per-Seed

VIABILITY_MAP_ON:
  seed=42: harm_rate=0.0062 harm_events=62/10000 residue_events=3556 active_centers=32
  seed=123: harm_rate=0.0054 harm_events=54/10000 residue_events=3638 active_centers=32

VIABILITY_MAP_ABLATED:
  seed=42: harm_rate=0.7449 harm_events=511/686
  seed=123: harm_rate=0.7493 harm_events=544/726

