# V3-EXQ-061 — MECH-104: Volatility Interrupt (Jitter Approximation)

**Status:** PASS
**Claims:** MECH-104, MECH-090
**Design:** Two-condition — baseline (no spike) vs surprise spike on harm contact
**spike_magnitude:** 0.05  |  **alpha_world:** 0.9  |  **Warmup:** 400 eps  |  **Seed:** 0

## Design Rationale

Without a volatility interrupt mechanism, world_forward training drives running_variance
to near-zero, permanently locking the agent in committed state (MECH-090 permanently
elevated). MECH-104 proposes that unexpected harm contact should spike running_variance
upward, enabling de-commitment. This experiment tests the V3 jitter approximation:
add spike_magnitude to _running_variance when actual_harm < -0.01.

## Condition A — Baseline (no spike)

| Metric | Value |
|--------|-------|
| Final running_variance (post-train) | 0.000003 |
| Uncommitted steps (eval) | 0 |
| Committed steps (eval) | 10000 |
| calibration_gap_approach | 0.9657 |

## Condition B — Surprise Spike (ε=0.05)

| Metric | Value |
|--------|-------|
| Final running_variance (post-train) | 0.950002 |
| Uncommitted steps (eval) | 317 |
| Committed steps (eval) | 0 |
| calibration_gap_approach | 0.4908 |
| Harm contacts during eval | 317 |
| Mean variance before harm contact | 8.850002 |
| Mean variance after harm contact | 8.900002 |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: baseline n_uncommitted == 0 (confirms collapse) | PASS | 0 |
| C2: spike n_uncommitted > 100 (de-commitment enabled) | PASS | 317 |
| C3: variance rises after harm contact | PASS | 8.8500 → 8.9000 |
| C4: spike calibration_gap > 0 (harm signal preserved) | PASS | 0.4908 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 5/5 → **PASS**

