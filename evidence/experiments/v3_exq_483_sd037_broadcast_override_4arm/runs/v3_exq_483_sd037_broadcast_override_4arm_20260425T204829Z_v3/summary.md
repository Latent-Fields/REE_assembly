# V3-EXQ-483 -- SD-037 Broadcast Override Regulator (orexin-analog) 4-arm validation

**Status:** FAIL
**Purpose:** Validate SD-037 broadcast_override regulator. 2x2 factorial
{use_gabaergic_decay, use_broadcast_override} x {OFF, ON} with PAG freeze-gate
always on. SD-036 baseline arm = ON_OFF. SD-037 effect arms = OFF_ON, ON_ON.

**Acceptance criteria** (from orexin kinetics lit-pull synthesis):
- PWS-hyperphagia analog: saturated arm (ON_ON) >=2x approach-commit vs ON_OFF.
  Observed: ratio=0.000 -> FAIL
- Narcolepsy/cataplexy analog: lost arm (OFF_OFF) <30% approach-commit vs ON_OFF.
  Observed: ratio=0.000 -> PASS

**Warmup:** 60 eps | **Eval:** 5 eps | **Steps/ep:** 200 | **Seeds:** [0, 1, 2]

## Arm Means

| Arm | reward | harm | approach | freeze_commit | freeze_active | pag_releases | override_mean | override_max |
|-----|--------|------|----------|---------------|---------------|--------------|---------------|--------------|
| OFF_OFF | -0.3719 | 0.3993 | 0.0 | 20.0 | 1000.0 | 5.3 | 0.0000 | 0.0000 |
| ON_OFF | -0.2667 | 0.3748 | 0.0 | 20.0 | 1000.0 | 5.3 | 0.0000 | 0.0000 |
| OFF_ON | -0.3719 | 0.3993 | 0.0 | 21.0 | 1000.0 | 9.3 | 0.5633 | 0.6224 |
| ON_ON | -0.2667 | 0.3748 | 0.0 | 20.0 | 1000.0 | 9.0 | 0.5633 | 0.6224 |

