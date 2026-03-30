# V3-EXQ-085k -- SD-015 RFM+Encoder Hybrid Action Selection

**Status:** FAIL
**Claims:** SD-015, SD-012, MECH-112
**Decision:** hybridize
**Seeds:** [42, 7, 13]
**Supersedes:** V3-EXQ-085j

## Architecture

Hybrid action selection: `cosine_sim(enc.encode(RFM(rf, a)), z_goal)`

- **RFM** (25->25, raw rf space): reliable dynamics (085h/i loss=0.0078)
- **ResourceEncoder** (25->16, BCE contact prediction): spatial invariance (085j: acc=0.927, r=0.819)
- **z_goal**: EMA of enc.encode(rf) at contacts (not raw rf)

**Rationale:** 085j E2Resource (dynamics in 16-dim latent space) had e2r_loss=0.0414 and degenerated to a constant action policy (benefit_present=0.020). RFM dynamics in raw 25-dim space are reliable (fine-grained position info). Encoder handles goal comparison with spatial invariance. Hybrid gets both.

**alpha_world:** 0.9  (SD-008)
**SD-012:** drive_weight=2.0, resource_respawn_on_consume=True
**lr_enc:** 0.001  **lr_rfm:** 0.0005
**enc_final_loss (avg):** 0.2258
**rfm_final_loss (avg):** 0.0069
**enc_contact_acc (avg):** 0.927
**Warmup:** 800 eps (curriculum=100 eps)
**Eval:** 100 eps (GOAL_PRESENT: RFM+enc hybrid; GOAL_ABSENT: random)

## Diagnostic Series Summary

| Variant | goal_resource_r | benefit_ratio | Note |
|---|---|---|---|
| 085g (z_world) | 0.066 | 0.37x | baseline |
| 085i (raw rf, contact-only) | 0.218 | 1.03x | spatial position issue |
| 085j (enc z_goal, E2Resource) | 0.819 | 0.034x | E2Resource degenerate |
| 085k (enc z_goal, RFM+enc hybrid) | 0.582 | 0.98x | this run |

## Navigation Results

| Condition | benefit/ep | z_goal_norm_enc | cal_gap | r_enc |
|---|---|---|---|---|
| GOAL_PRESENT | 0.573 | 1.173 | 0.2987 | 0.582 |
| GOAL_ABSENT  | 0.587 | -- | -- | -- |

**Benefit ratio (goal/no-goal): 0.98x**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: z_goal_norm_enc > 0.1 | PASS | 1.173 |
| C2: benefit ratio >= 1.3x | FAIL | 0.98x |
| C3: goal_resource_r_enc > 0.2 | PASS | 0.582 |
| C4: enc_contact_acc > 0.7 | PASS | 0.927 |

Criteria met: 3/4 -> **FAIL**

## MECH-124 Diagnostics

goal_vs_harm_ratio: 0.451 (< 0.3 = V4 risk)

## Per-Seed

GOAL_PRESENT:
  seed=42: benefit/ep=0.540 z_goal_norm_enc=0.976 r_enc=0.703 enc_acc=0.898 rfm_loss=0.0082
  seed=7: benefit/ep=0.560 z_goal_norm_enc=1.366 r_enc=0.525 enc_acc=0.953 rfm_loss=0.0060
  seed=13: benefit/ep=0.620 z_goal_norm_enc=1.176 r_enc=0.516 enc_acc=0.930 rfm_loss=0.0064

GOAL_ABSENT:
  seed=42: benefit/ep=0.500
  seed=7: benefit/ep=0.650
  seed=13: benefit/ep=0.610

## Failure Notes

- C2 FAIL: benefit_ratio=0.98x < 1.3x BUT C3 PASS (goal_resource_r_enc=0.582 > 0.2). RFM+enc goal representation works; navigation policy gap. Check: RFM quality (rfm_loss should be < 0.01); consider nav_bias multiplier or stronger eval action selection.
