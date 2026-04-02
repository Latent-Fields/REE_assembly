# V3-EXQ-075d -- MECH-113 Self-Maintenance (z_self D_eff)

**Status:** FAIL
**Claims:** MECH-113
**Seed:** 42  **Warmup:** 200  **Eval:** 30
**maintenance_weight:** 0.1  **d_eff_target:** 1.5
**noise_sigma:** 2.0

## Results

| Metric | NoMaintenance | Maintenance |
|---|---|---|
| D_eff baseline (pre-perturb) | 23.8477 | 23.8477 |
| D_eff post-perturbation | 23.8409 | 23.8409 |
| D_eff ratio (post/baseline) | 1.00x | 1.00x |
| E2 loss post-perturb | 0.00000 | 0.00000 |

**D_eff gap (nomaint - maint) post-perturb: 0.0000**

## PASS Criteria

| Criterion | Result |
|---|---|
| C1: maint D_eff ratio <= 1.5x | PASS |
| C2: nomaint D_eff ratio >= 2.0x | FAIL |
| C3: gap >= 0.5 * nomaint_post | FAIL |
| C4: e2_loss not degraded | PASS |

Criteria met: 2/4 -> **FAIL**

## Interpretation

MECH-113 PARTIAL: Some homeostatic signal present but below threshold. Perturbation may be too weak, or maintenance weight needs adjustment.

## Failure Notes

- C2 FAIL: nomaint D_eff post/baseline=1.00x < 2.0x
- C3 FAIL: gap=0.0000 < 0.5 * nomaint_post=11.9205
