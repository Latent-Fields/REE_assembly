# V3-EXQ-483a -- SD-037 Broadcast Override Regulator (orexin-analog) 4-arm validation

**Status:** PASS (accepted path: substrate_readiness_fallback)
**Supersedes:** V3-EXQ-483 (60-warmup baseline-zero confound)
**Purpose:** Validate SD-037 broadcast_override regulator. 2x2 factorial
{use_gabaergic_decay, use_broadcast_override} x {OFF, ON} with PAG freeze-gate
always on. SD-036 baseline arm = ON_OFF. SD-037 effect arms = OFF_ON, ON_ON.

**Behavioural acceptance** (used when baseline approach_commit > 0):
- PWS-hyperphagia analog: ON_ON >=2x ON_OFF approach-commit.
  Observed: ratio=0.000 -> FAIL
- Narcolepsy/cataplexy analog: OFF_OFF <30% ON_OFF approach-commit.
  Observed: ratio=0.000 -> PASS
- Path available: NO (baseline approach_commit=0)

**Substrate-readiness fallback** (used only when baseline approach_commit=0):
- Override climbs in ON arms: mean(OFF_ON, ON_ON)=0.563
  threshold > 0.3 -> PASS
- PAG release ratio ON_ON/ON_OFF: 1.688
  threshold > 1.3 -> PASS

**Warmup:** 200 eps | **Eval:** 5 eps | **Steps/ep:** 200 | **Seeds:** [0, 1, 2]

## Arm Means

| Arm | reward | harm | approach | freeze_commit | freeze_active | pag_releases | override_mean | override_max |
|-----|--------|------|----------|---------------|---------------|--------------|---------------|--------------|
| OFF_OFF | -0.0705 | 0.2666 | 0.0 | 28.3 | 1000.0 | 5.3 | 0.0000 | 0.0000 |
| ON_OFF | -0.0705 | 0.2666 | 0.0 | 22.0 | 1000.0 | 5.3 | 0.0000 | 0.0000 |
| OFF_ON | -0.0705 | 0.2666 | 0.0 | 28.7 | 1000.0 | 9.3 | 0.5633 | 0.6224 |
| ON_ON | -0.0705 | 0.2666 | 0.0 | 28.7 | 1000.0 | 9.0 | 0.5633 | 0.6224 |

