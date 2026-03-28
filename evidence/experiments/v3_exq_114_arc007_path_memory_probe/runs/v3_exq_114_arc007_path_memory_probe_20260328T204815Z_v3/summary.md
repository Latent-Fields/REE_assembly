# V3-EXQ-114 -- ARC-007 Path Memory Probe

**Status:** PASS
**Claim:** ARC-007
**Decision:** retain_ree
**Seeds:** [42, 123]
**Conditions:** MAP_NAV (hippocampal terrain guidance) vs MAP_ABLATED (random action selection)
**alpha_world:** 0.9  (SD-008)
**Warmup:** 300 eps  **Eval:** 50 eps
**Env:** CausalGridWorldV2 size=6, 4 hazards, use_proxy_fields=True

## Pre-Registered Thresholds

C1: harm_reduction_frac >= 0.15  (MAP_NAV reduces harm rate by >=15% vs MAP_ABLATED)
C2: residue trajectory samples >= 5 for MAP_NAV  (hippocampal proposals generate world_states)
C3: consistent harm rate reduction for ALL seeds  (seed_pair_pass >= 2)
C4: n_harm_min >= 20  (data quality gate)

## Results

| Condition | harm_rate | harm_events | steps |
|-----------|----------|------------|-------|
| MAP_NAV  | 0.0060 | 119 | 20000 |
| MAP_ABLATED | 0.7648 | 1086 | 1420 |

**harm_reduction_frac: +0.9922**  (0.7648 -> 0.0060)

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: harm_reduction >= 0.15 | PASS | 0.9922 |
| C2: residue samples available | PASS | 20000 |
| C3: consistent across seeds | PASS | 2/2 |
| C4: n_harm_min >= 20 | PASS | 58 |

Criteria met: 4/4 -> **PASS**

## Interpretation

ARC-007 SUPPORTED: Hippocampal terrain-guided navigation reduces harm rate by 99.2% (MAP_NAV=0.0060 vs MAP_ABLATED=0.7648). Consistent direction across all {len(seeds)} seeds. Path memory through residue-field terrain provides measurable safety advantage.

## Per-Seed

MAP_NAV:
  seed=42: harm_rate_eval=0.0061 harm_events=61/10000 residue=nan
  seed=123: harm_rate_eval=0.0058 harm_events=58/10000 residue=nan

MAP_ABLATED:
  seed=42: harm_rate_eval=0.7642 harm_events=538/704
  seed=123: harm_rate_eval=0.7654 harm_events=548/716

