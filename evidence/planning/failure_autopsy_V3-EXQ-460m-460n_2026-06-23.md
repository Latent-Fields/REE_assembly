# Failure Autopsy — V3-EXQ-460m + V3-EXQ-460n (closure-commit-ENTRY readiness cluster)

- **run_ids:**
  - `v3_exq_460m_closure_commit_entry_readiness_20260623T100603Z_v3` (bool latch, `use_closure_commit_entry`, ree-v3 84c1e7c)
  - `v3_exq_460n_closure_commit_entry_trajectory_readiness_20260623T104846Z_v3` (C-STEP trajectory, `use_closure_commit_entry_trajectory`, ree-v3 96ee30c)
- **queue_ids:** V3-EXQ-460m, V3-EXQ-460n
- **claims:** `[]` (claim-free substrate-readiness diagnostics for the commitment_closure:GAP-4 / f_dominance_conversion_ceiling rung-6 closure-commit-entry primitive lineage)
- **outcome:** FAIL — self-route `substrate_not_ready_requeue`, adjudication `precondition_unmet`
- **scope:** cluster (2 runs, one shared root)
- **generated_utc:** 2026-06-23T22:55:41Z
- **status:** confirmed (user interactive gate, 2026-06-23 — "Confirm re-queue (harness fix)")
- **routing:** queue-experiment (re-issue both readiness diagnostics with goal seeding in the eval-arm loop). **re-derive brake NOT fired.** `recommended_substrate_queue_entry.action = none` — **no create/amend on `f_dominance_conversion_ceiling`.**

---

## 1. Facts (no interpretation)

Both runs report `outcome: "FAIL"`, `interpretation.label: "substrate_not_ready_requeue"`, `route_reason: "closure_rule_directed_commit_not_formed"`.

The two preconditions:

| precondition | 460m measured / threshold | 460n measured / threshold | met |
|---|---|---|---|
| `foraging_contact_guard` (603n G2+G3: P2 contact_rate>0 AND z_goal_norm_at_contact_peak>0.4 on ≥2/3) | 0.667 / 0.667 | 1.0 / 0.667 | **PASS** |
| `closure_rule_directed_commit_formed` (ARM_ON forms goal-active rule-directed commit: `goal_state.is_active()` AND `lateral_pfc.rule_state` norm ≥ `closure_commit_entry_rule_norm_floor`=0.01 on ≥2/3) | **0 / 1** | **0 / 1** | **FAIL** |

Per-seed/arm in BOTH runs: `n_rule_directed_commit_ticks = 0` on **every** arm, **every** seed (460m: ARM_ENTRY_OFF/ON; 460n: ARM_ENTRY_OFF/ARM_BOOL/ARM_TRAJECTORY). Consequently `ncl_hold_closure_armed_total = 0`, `ncl_hold_reassert_total = 0`, `max_consecutive_beta_run` 4–7, `n_f_commits` = `total_committed_steps` (the legacy F-driven commit path; the closure-exclusive eval is meant to suppress it, but the F-commit *read point* still counts). 460n also reports `closure_program_steps_total = 0` on all arms (gate-b C-STEP unscorable).

**The decisive number:** `rule_state_norm_peak` is **0.394 / 0.310 / 7.586** (460m seeds 42/43/44) and **0.286 / 0.322 / 0.398–0.497** (460n) — every value is **≫ the 0.01 floor**. So the rule-norm half of the SET precondition is satisfied; the *goal-active* half is what is missing.

**Which criterion failed:** a **precondition / non-vacuity gate** (`closure_rule_directed_commit_formed`). No discrimination criterion ran (gate-a `armed_and_sustained`; 460n gate-b `cstep`). Both are `criteria_non_degenerate: false` because their inputs never formed. Clean readiness self-route, not a claim test.

## 2. Claim-layer mapping

`claim_ids = []` on both. These are claim-free readiness probes that certify the substrate is ready before any de-commit falsifier (a 460-lineage successor) is scored. No claim is exercised, supported, or weakened. MECH-445 / MECH-446 (the downstream de-commit claims) stay candidate / v3_pending / pending_retest_after_substrate, untouched by this cluster.

## 3. The root — code-confirmed, and DISTINCT from 460k

### 3.1 What 460k was

`failure_autopsy_V3-EXQ-460k_2026-06-22` found the closure-exclusive de-commit eval armed the latch-hold via `_closure_commit_active`, which was gated two hops down on `e3._committed_trajectory is not None` — and the **only** non-None writer of `_committed_trajectory` in `ree_core/` was `e3_selector.py:1926` under `if committed:` (pure running-variance/F). So a closure-directed commit forming **while not** F-committed was a contradiction in the code: the commit-intent counter was **pinned at 0 by construction**. Routing: `/implement-substrate` to **build** an F-independent commit-entry primitive. That build landed (84c1e7c bool latch + 96ee30c C-STEP trajectory).

### 3.2 What 460m/460n are — the F-independent writer EXISTS, but its SET precondition is starved by the eval harness

The 84c1e7c primitive added a genuinely F-independent writer at `agent.py:6519–6532`:

```python
if (getattr(self.config, "use_closure_commit_entry", False)
    and self.goal_state is not None
    and self.goal_state.is_active()
    and result is not None
    and result.selected_action is not None
    and self.lateral_pfc is not None):
    _rule_norm = float(self.lateral_pfc.rule_state.norm().item())
    if _rule_norm >= _rule_floor:
        self.e3._closure_committed_active = True   # F-INDEPENDENT, sticky
```

The 460k structural wedge is therefore **resolved in code** — there now is a path that sets the latch without `result.committed`. The SET predicate's precondition is `goal_state.is_active() AND rule_state.norm() >= floor`.

The readiness eval-arm loop (`_eval_arm_behaviour`, lines 480–544 in 460m; mirrored in 460n) drives `_sense_with_optional_harm` → `generate_trajectories` → `select_action` → `env.step` → `update_residue`, and at line 530–536 counts the non-vacuity readout:

```python
gs = getattr(agent, "goal_state", None)
goal_active = bool(gs is not None and gs.is_active())
rs_norm = _rule_state_norm(agent)
if goal_active and rs_norm >= rule_floor:
    n_rule_directed_commit_ticks += 1
```

**`agent.update_z_goal(...)` is never called anywhere in this loop** (grep-confirmed: `update_z_goal` appears in neither script outside `_make_config`'s `z_goal_enabled=True`). The agent is built with a GoalState (`z_goal_enabled=True`, `drive_weight=DRIVE_WEIGHT`), but `GoalState.is_active()` only returns True when z_goal has been seeded above threshold by `update_z_goal`, and `agent.reset()` (line 482, per episode) clears it. With no seeding call in the eval loop, **`goal_active` is False at every tick** → `n_rule_directed_commit_ticks` is pinned at 0 → the SET predicate never fires → `_closure_committed_active` is never set → the latch never arms (gate-a) and the program never steps (460n gate-b).

The rule half clears the floor on its own (`rule_state_norm_peak` 0.31–7.59 ≫ 0.01), so **the sole missing ingredient is goal activation**, and it is missing because the *eval harness* does not seed the goal — not because the substrate cannot form one.

### 3.3 Why this is NOT a substrate property (the existence proof)

The `foraging_contact_guard` precondition **PASSED** (z_goal_norm_at_contact_peak > 0.4 on 2/3 and 3/3 seeds). That metric comes from the scaffold's `run_p2`, which seeds z_goal via consumption-gated `update_z_goal`. So z_goal seeding **demonstrably works on this exact trained substrate** — it is simply absent from the hand-rolled closure-eval arm loop. The eval loop was cloned from 460l, which predated the goal-dependent SET predicate (460k/460l armed off `_committed_trajectory`, which needed no goal seeding). The test design did not keep up with the substrate change — the canonical copy-and-modify propagation gap.

This is the **V3-EXQ-642 pattern** (`failure_autopsy_V3-EXQ-642_2026-06-06`): a `precondition_unmet` self-route where the branch's assumption was unmet because the eval never drove the precondition's input (642: P0 never trained the substrate → untrained-substrate artifact; here: the eval never seeds z_goal → goal-inactive artifact). Correct route = **re-queue with a corrected eval**, NOT substrate enrichment.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | claim-free; nothing tested. No weakens anywhere. |
| Biological reference | not the failing layer | The closure-coupled commit-entry (rule-stability precursor → committed program, SD-034 ClosureOperator / Rich & Shapiro 2009) is the design intent; the failure is upstream of it, in the eval harness. |
| Prerequisites | present (in code) | The F-independent SET writer exists (84c1e7c/96ee30c). The 460k missing-dependency is built. |
| Implementation | complete (substrate); **incomplete (experiment)** | The substrate primitive is correct. The readiness eval-arm loop is missing the `update_z_goal` call its own SET precondition requires — a test-harness gap, the symbol of the readiness test without its function. |
| Environment | adequate | Foraging substrate forages + seeds in P2 (contact guard passed). |
| Measurement | adequate (caught it) | The `closure_rule_directed_commit_formed` non-vacuity gate correctly refused to score the downstream gates and self-routed `substrate_not_ready_requeue` — instrument working as designed. |
| Integration | not reached | The closure plane and the latch-hold never couple because the SET precondition never fired. |
| Scale | not the issue | 15 eval episodes/arm; the gate is a per-tick conjunction, not a budget. |

Recommended epistemic_category: **n/a** (claim-free; this is an eval-harness re-queue, not a claim adjudication). The reading is `substrate_not_ready_requeue` taken at face value, with the cause localised to the experiment's eval loop.

## 5. Cluster pattern

| Experiment | Latch under test | Precondition gate | Discrimination gates | Read |
|---|---|---|---|---|
| V3-EXQ-460m | bool `_closure_committed_active` | `closure_rule_directed_commit_formed` = 0 | gate-a `armed_and_sustained` unscorable | starved by missing goal seeding |
| V3-EXQ-460n | bool + C-STEP `_closure_committed_trajectory` | `closure_rule_directed_commit_formed` = 0 | gate-a + gate-b `cstep` unscorable | starved by missing goal seeding |

**One structural property, not two bugs:** both runs share the identical eval-arm loop (the trajectory run is a sibling of the bool run, not a supersede), and that loop omits `update_z_goal`. The two readiness gates of 460n (occupancy + C-STEP) and the single gate of 460m are all downstream of the one starved precondition. Fixing the eval loop (seed z_goal each step) makes both runs scorable in the same re-issue.

## 6. Learning extracted

1. The 460k structural wedge (no F-independent writer) is **resolved** by the 84c1e7c/96ee30c primitives — there now is a code path that sets `_closure_committed_active` without an F-driven `committed` trajectory. 460m/460n do **not** re-hit that root.
2. The new SET predicate added a `goal_state.is_active()` dependency the predecessor (460l) eval-arm loop never had. The loop was cloned without adding the `update_z_goal` seeding the new predicate requires → the goal-active half of the precondition is starved → `n_rule_directed_commit_ticks = 0` on every seed.
3. The rule-norm half is fine (`rule_state_norm_peak` 0.31–7.59 ≫ 0.01); only goal activation is missing, and it is missing in the *experiment*, not the substrate (proven by the P2 contact guard passing on the same trained agent).
4. The fix is a **re-queue** with the eval-arm loop calling `agent.update_z_goal(...)` each step (mirror `run_p2`'s consumption-gated seeding, or a forced-feed seed so the SET precondition has a goal-active tick to latch on). The substrate primitives are built and correct — **no substrate enrichment, no `f_dominance_conversion_ceiling` amend, no re-derive brake.**

## 7. Routing decision (user-confirmed)

- `evidence_direction: non_contributory` for both runs (claim-free; nothing exercised). Neither weakens any claim.
- **Routing: queue-experiment** — re-issue both readiness diagnostics (new letters; supersede 460m/460n) with the eval-arm loop seeding z_goal each step so `goal_state.is_active()` can be True, restoring the `closure_rule_directed_commit_formed` non-vacuity input. Keep the same gates (a `armed_and_sustained`; b C-STEP), the same `closure_exclusive_decommit_eval` substrate, and the same self-route guards.
- **`recommended_substrate_queue_entry.action = none`** — the rung-6 closure-commit-entry primitives (84c1e7c bool, 96ee30c trajectory) are built and correct. **No create/amend on `f_dominance_conversion_ceiling`** for the next `/governance` pass.
- **Re-derive brake NOT fired** — claim-free; not a `substrate_ceiling`/`non_contributory` substrate reading; this is a harness re-queue (V3-EXQ-642 class), exactly the loop the brake does *not* govern.

### Note for the next `/governance` pass

No substrate_queue write is owed by this autopsy. The f_dominance_conversion_ceiling rung-6 implementation_log already records the 84c1e7c/96ee30c builds; the readiness gate for them stays open until the **re-queued** 460m/460n successors (with goal seeding) score a contributory PASS. Do not interpret this FAIL as a substrate-ceiling signal against the closure-commit-entry primitives.
