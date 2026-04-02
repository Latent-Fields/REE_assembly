# SD-015 HippocampalModule Goal Navigation — Design Session Prompt

**Created:** 2026-04-02
**Purpose:** Structured starting point for the session that will design and write the first experiment using the HippocampalModule for genuine goal-directed navigation.

---

## Session Goal

Design and write `v3_exq_2xx_sd015_hippocampal_goal_nav.py` — one experiment that uses the already-implemented `HippocampalModule` to achieve `benefit_ratio >= 1.3x` for goal-directed navigation on CausalGridWorldV2.

This is the **first-paper gate** experiment for goal-directed behavior.

---

## What Has Been Established (Do Not Revisit)

### Representation is validated
- `prox_r² = 0.91`, `goal_resource_r = 0.87` (EXQ-085l)
- z_goal seeding works with SD-012 (`drive_weight=2.0`, implemented 2026-04-02)
- The encoder correctly captures resource proximity in z_goal latent

### 1-step greedy is the failure mode — not representation
- EXQ-085a through EXQ-085o: all FAIL on C2 (`benefit_ratio < 1.3x`; best = 0.42x)
- EXQ-085n (depth=5 multi-step greedy): FAIL — compound RFM error washes out gradient
- Root cause: 1-step or shallow greedy cannot navigate 10×10 grid efficiently
- The `ResourceFeatureMap` (RFM) approach is exhausted — no further RFM variants needed

### HippocampalModule is fully implemented
- CEM trajectory generation wired
- Action-object space navigation (SD-004)
- Terrain prior (SD-002) and sd015 prerequisite (`benefit_eval_head`) available in `e3_selector.py`
- **The SD-015 experiments never used the HippocampalModule** — they used experiment-local RFM only

### MECH-163 confirms the correct mechanism
- SNc/habit system (model-free): sufficient for familiar, well-practiced contexts — but the grid world provides insufficient practice during training
- VTA/HippocampalModule system (model-based): generates multi-step trajectory proposals; evaluates them in latent space; appropriate for novel contexts
- First-paper gate requires the VTA/hippocampal system, not habit alone

---

## Files to Read at Session Start

Before designing the experiment, read these in order:

1. **`ree-v3/ree_core/predictors/e3_selector.py`**
   Focus: `E3TrajectorySelector.select()` method — how CEM candidate trajectories are scored. Where is `benefit_eval_head` currently used? What does the cost function `J(ζ)` look like? Where would a z_goal-proximity term be added?

2. **`ree-v3/ree_core/latent/stack.py`** (GoalState section)
   Focus: How is `z_goal` currently seeded? What is `GoalState.update()`? What signal does `z_goal_latent` hold when seeded? How does it decay?

3. **`ree-v3/ree_core/hippocampus/` or equivalent**
   Focus: How does the HippocampalModule generate trajectory candidates? What inputs does it take? Does it currently receive any goal signal?

4. **`ree-v3/experiments/v3_exq_085l_sd015_proximity_regression_enc.py`**
   Focus: How was z_goal seeding used for action selection in the best-performing RFM experiment? What can be reused vs. what needs to change?

5. **`ree-v3/ree_core/utils/config.py`** (`E3Config`, `HippocampalConfig`)
   Focus: What config fields exist for the hippocampal trajectory evaluator? Is there a `goal_weight` in the trajectory scoring cost?

---

## Design Questions to Resolve in the Session

### Q1: What cost term adds z_goal to trajectory scoring?
Current `J(ζ) = F(ζ) + λ·M(ζ) + ρ·Φ_R(ζ) - β·B(ζ) - η·novelty`

Options:
- **A**: `- γ·cosine_sim(z_goal_trajectory_end, z_goal_current)` — penalise distance between z_goal at trajectory end vs. current z_goal latent
- **B**: `- γ·benefit_eval_head(z_world_trajectory_end)` — use existing trained benefit head on final trajectory state
- **C**: `- γ·goal_proximity_score(resource_field_trajectory_end)` — direct resource proximity at trajectory end (simpler, bypasses latent)

Which is biologically correct? Which is most likely to produce a clean test of the MECH-163 claim?

### Q2: Training curriculum
z_goal must be seeded before CEM evaluation contributes usefully. Options:
- **Phased**: P0 = E1/E2 encoder warmup (no goal signal, N episodes); P1 = goal-seeded evaluation enabled (SD-012 drive kicks in)
- **Always-on**: SD-012 drive_weight=2.0 means goal seeding happens naturally — no phasing needed
- **Warmup gate**: E3 only applies goal term in trajectory scoring once `goal_seeded=True` flag is set

### Q3: Acceptance criteria
What constitutes a clean first-paper gate PASS?
- C1: `benefit_ratio >= 1.3x` (primary — matches all prior EXQ-085 criteria)
- C2: `prox_r² >= 0.7` (representation still intact)
- C3: Ablation check — goal scoring disabled → benefit_ratio drops below 1.1x (confirms goal term is causal, not confounded)
- C4: `>= 4/7 seeds pass` (replication)

### Q4: Ablation vs. direct test
Two experimental designs:
- **Direct test**: HippocampalModule + z_goal term; measure benefit_ratio. Simple but doesn't isolate the contribution.
- **Ablation pair**: Condition A = HippocampalModule + no z_goal term; Condition B = HippocampalModule + z_goal term. Compares ratios across conditions within experiment. Cleaner scientifically.

Which design is more appropriate for the first-paper claim?

### Q5: Claim IDs
What claims does this experiment directly test?
- **SD-015** (goal representation seeding) — primary
- **MECH-163** (VTA/hippocampal system for goal-directed nav) — directly tested
- **ARC-030** (D1/D2 approach-avoidance balance) — tangentially tested if harm avoidance coexists with goal approach

Should this be a single-claim test (SD-015 only) or multi-claim? Per `claim_ids` accuracy rules: only tag what the experiment *directly* tests.

---

## Constraints

- Use `CausalGridWorldV2` (standard V3 env: `use_proxy_fields=True`, 10×10 grid)
- SD-012 `drive_weight=2.0` — already in default config, no change needed
- SD-011 dual harm streams — already wired, use as-is
- Phased training protocol is **MANDATORY** for any downstream head trained on encoder outputs (per 2026-04-01 protocol): P0 encoder warmup → P1 frozen-encoder head training → P2 collection
- Must run a smoke test (`--dry-run`) before queuing
- Machine affinity: `DLAPTOP-4.local` (primary)
- EXQ number: check `experiment_queue.json` and `runner_status.json` before assigning

---

## Expected Outcome

If **PASS**: SD-015 validated, MECH-163 VTA system confirmed, first-paper gate for goal-directed behavior cleared.
If **FAIL**: Diagnose whether failure is in (a) z_goal seeding (SD-012 insufficient), (b) cost term design (wrong proxy for goal), or (c) CEM horizon too short. Each failure mode has a targeted next experiment.

---

## Related Claims

- `SD-015` — goal representation seeding via benefit exposure
- `MECH-163` — dual goal-directed systems (SNc habit vs. VTA/hippocampal)
- `ARC-030` — D1/D2 approach-avoidance balance
- `ARC-018` — hippocampal rollout viability mapping
- `SD-012` — homeostatic drive modulation (prerequisite, implemented)
- `SD-011` — dual nociceptive streams (prerequisite, implemented)
