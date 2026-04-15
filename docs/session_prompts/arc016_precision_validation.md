# ARC-016: Dynamic Precision Validation

> Paste this into a new Claude Code session as your opening message.
> Created: 2026-04-14

## Prompt

Task: ARC-016 dynamic precision — review staged fix and queue validation experiment

ARC-016 (precision-to-commitment circuit) works in a single environment (EXQ-018b PASS: precision drops 40% when perturbed, commitment rate drops proportionally). But it fails to generalize across environment parameterizations (EXQ-038 FAIL: running_variance locks at initialization value across 5 hazard_harm levels — no sensitivity to environment danger).

**What exists:**
- EXQ-018b PASS: relative threshold works within one env
- EXQ-060 PASS: committed sequences form (5980 steps, hold_rate 0.936)
- EXQ-038 FAIL: variance invariant to hazard_harm sweep (0.40257 across all levels)
- EXQ-088/094 FAIL: harm-variance reframe also failed (harm_eval outputs collapse)
- EXP-0094 proposed: auto-calibrate threshold = k * warmup_baseline_variance
- EXQ-038b staged: precision sweep retest on current substrate

**Session goal:** (1) Read the EXQ-038 manifest and script to understand the generalization failure. (2) Check if EXQ-038b is already written as a script in ree-v3/experiments/. If so, review it and queue it. If not, write it. (3) Consider whether EXP-0094 (auto-calibration) should be implemented as a code change before the experiment, or whether the experiment should first confirm the raw mechanism works on current substrate. (4) Queue the experiment.

Key code: ree-v3/ree_core/predictors/e3_selector.py (lines 170-236 for precision computation).
