# MECH-090: Bistable Beta Gate — Diagnose and Fix

> Paste this into a new Claude Code session as your opening message.
> Created: 2026-04-14

## Prompt

Task: MECH-090 bistable beta gate — diagnose and fix

The bistable commitment gate (MECH-090) is implemented in ree-v3 but failing validation. This is the single biggest blocker in the deliberative layer — it cascades to SD-021 (descending pain modulation), MECH-057b (completion gate), and all commitment-gated mechanisms.

**What MECH-090 is supposed to do:** E3 maintains a running_variance of prediction error. When variance drops below a relative threshold (2x warmup baseline), the BetaGate latches into committed state — action selection switches from stochastic sampling to argmin(scores), and the agent follows its chosen trajectory. When the hippocampal completion signal fires (trajectory quality exceeds threshold), the gate releases and the agent returns to uncommitted exploration.

**What's working:** EXQ-018b PASS shows the precision-to-commitment circuit functions end-to-end in a single environment. EXQ-060 PASS shows committed-step formation (5980 steps, hold_rate 0.936). The code is in ree-v3/ree_core/predictors/e3_selector.py (precision/commitment) and ree-v3/ree_core/control/beta_gate.py (bistable latch).

**What's failing:** EXQ-049 FAIL — committed sequences not forming under the specific test conditions. The exact failure mode needs diagnosis. Also EXQ-038 shows variance locks at initialization across different hazard_harm levels (generalization failure).

**Session goal:** (1) Read the MECH-090 code, the EXQ-049 manifest and script, and understand the specific failure mode. (2) Check whether the failure is a wiring issue (gate never receives the right signal), a threshold issue (thresholds miscalibrated for the test conditions), or a training issue (E3 variance doesn't converge during warmup). (3) Propose a fix or parameter adjustment. (4) If the fix is clear, write an EXQ-049a experiment script and queue it.

Start by reading: ree-v3/ree_core/control/beta_gate.py, ree-v3/ree_core/predictors/e3_selector.py (lines 170-236), and the EXQ-049 manifest in REE_assembly/evidence/experiments/. Then check ree-v3/CLAUDE.md for the SD implementation table.
