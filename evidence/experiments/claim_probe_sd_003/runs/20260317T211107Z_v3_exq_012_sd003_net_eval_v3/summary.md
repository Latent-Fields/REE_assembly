# V3-EXQ-012 — SD-003 Signed Net Eval (Benefit + Harm Signal)

**Status:** FAIL
**Warmup:** 300 eps, RANDOM policy + recon loss + 5-step E2 + net_eval regression
**Probe eval:** 10 grid resets × (near-hazard + safe positions)
**Seed:** 0

## Key Change vs EXQ-002 through EXQ-010

Binary BCE `harm_eval` (harm=1, no-harm=0) replaced with signed REGRESSION
`net_eval` trained on actual `harm_signal` values (normalised to [-1, 1]).

- `agent_caused_hazard` → target ≈ -0.8  (`-0.4 / 0.5`)
- `env_caused_hazard`   → target ≈ -1.0  (`-0.5 / 0.5`)
- `resource`            → target ≈ +0.6  (`+0.3 / 0.5`)
- `none`                → target ≈  0.0

E3 now has full ±0.3–0.5 value boundaries. Benefit/harm contrast amplifies
the SD-003 causal signature.

Mean E2 world loss: 0.000318  |  Mean reconstruction loss: 0.03481
Warmup harm events: 819   |  Warmup benefit events: 244

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: TRAINED calibration_gap > 0.05 | FAIL | 0.0007 |
| C2: RANDOM abs(calibration_gap) < 0.10 | PASS | 0.0004 |
| C3: Warmup harm events > 100 | PASS | 819 |
| C4: No fatal errors | PASS | 0 |
| C5: net_eval non-degenerate | PASS | std=0.0158 |
| C6: Probe coverage >= 10 each | PASS | near=231 safe=66 |
| C7: Warmup benefit events > 20 | PASS | 244 |

## Calibration Results

| Condition | mean_causal_sig(near_hazard) | mean_causal_sig(safe) | calibration_gap |
|---|---|---|---|
| TRAINED | 0.0019 | 0.0012 | 0.0007 |
| RANDOM  | -0.0002 | -0.0006 | 0.0004 |

## Attribution Pipeline

```
z_world = encoder(obs_world)                    [reconstruction-loss trained]
z_world_actual = E2.world_forward(z_world, a_actual)
z_world_cf     = E2.world_forward(z_world, a_cf)
v_actual = net_eval(z_world_actual)             [SIGNED regression, not binary]
v_cf     = net_eval(z_world_cf)
causal_sig = v_actual - v_cf
```

Criteria met: 6/7 → **FAIL**

## Failure Notes

- C1 FAIL: TRAINED gap 0.0007 <= 0.05
