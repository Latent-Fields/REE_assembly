# V3-EXQ-030c — SD-003 Full Attribution (Large Scale)

**Status:** FAIL
**Claims:** SD-003, ARC-024, MECH-071
**World:** CausalGridWorldV2 (n_hazards=8, size=12, proximity_scale=0.05)
**Warmup:** 2000 eps | **Eval:** 200 eps × 300 steps
**alpha_world:** 0.9  (SD-008)
**Seed:** 0

## Motivation: Resolving EXQ-030b Sign Switch

EXQ-030b seed-0 PASS (agent_caused=+0.017), seed-1 FAIL (agent_caused=-0.008).
Root cause: n_agent_caused_eval ≈ 32 → SE ≈ 0.009. Both means within 2 SE of zero.
EXQ-030c scales up to N ≥ 100 contact events per type:
- n_hazards: 4 → 8 (doubles contact frequency)
- warmup: 500 → 2000 (better-calibrated E2 and E3 on contact states)
- eval: 50 → 200 episodes (more data)
- steps: 200 → 300 (more exposure per episode)

## Attribution Results

| Transition | mean causal_sig | median | std | n |
|---|---|---|---|---|
| none (locomotion)    | -0.096339 | -0.094441 | 0.038301 | 175 |
| hazard_approach      | 0.007953 | 0.000939 | 0.090433 | 1780 |
| env_caused_hazard    | 0.009678 | -0.006982 | 0.098431 | 80 |
| agent_caused_hazard  | 0.005444 | 0.014887 | 0.060771 | 37 |

- **world_forward R²**: 0.9512
- **attribution_gap** (approach − env_caused): -0.001726
- **sign_structure_correct** (agent > env): False  *(diagnostic — not a pass criterion)*

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: attribution_gap > 0 | FAIL | -0.001726 |
| C2: causal_sig_approach > causal_sig_none | PASS | 0.007953 vs -0.096339 |
| C3: causal_sig_approach > 0.005 | PASS | 0.007953 |
| C4: world_forward_r2 > 0.05 | PASS | 0.9512 |
| C5: n_agent_hazard_eval >= 100 (reliable contact stats) | FAIL | 37 |

Criteria met: 3/5 → **FAIL**

## Failure Notes

- C1 FAIL: attribution_gap=-0.001726 <= 0
- C5 FAIL: n_agent_hazard_eval=37 < 100 (insufficient data for sign test)
