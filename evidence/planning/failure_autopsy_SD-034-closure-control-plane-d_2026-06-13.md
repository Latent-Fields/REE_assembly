# Failure Autopsy -- SD-034 commitment-closure-control-plane `*d` validation cohort (460d + 468d)

- **Generated / confirmed:** 2026-06-13T09:47:14Z
- **Status:** confirmed (interactive gate; user AskUserQuestion 2026-06-13)
- **Scope:** cluster (2 targets, one tightly-coupled cohort, same just-landed substrate)
- **Parent:** `failure_autopsy_SD-034-closure-cluster_2026-06-12` (+ sibling `..._ext_2026-06-12`)
- **Substrate under test:** `commitment-closure-control-plane` (ree-v3 `6fdb111`, 2026-06-12) -- Leg A env-completion hook + Leg B de-commit refractory landed; **Leg C (trained `rule_bias_head` + non-cap-pinned de-commit DV) explicitly experiment-side and NOT built.**

---

## One-line cohort verdict

The substrate's Legs A+B **closed the `*c` `n_closures=0` gap** -- closure now fires on the actual completion event (460d **C1 PASS**, MECH-260 supports) -- but the **de-commit behavioural authority** over the MECH-090 latch is still absent, because **Leg C is code-confirmed unbuilt**: both scripts *set* `lateral_pfc_train_rule_bias_head=True` but **never train the head** (no optimizer inclusion, no `.backward()`/REINFORCE). Neither `*d` run is a falsification. Route a `460e/468e` `/queue-experiment` redesign that actually trains the head + reads a non-cap-pinned DV + gates beta-engagement; amend the substrate_queue entry with both failure records.

---

## Facts reconstruction

### 460d (`residual_closure_open`; claims SD-034, MECH-260, MECH-261)

| Criterion | Result | Why |
|---|---|---|
| C1 `n_closures` (load-bearing) | **PASS** | Leg-A env hook fires closure: `n_closures` 6/3/7, all `n_hook_fires`; `nogo_installed` 18/9/21. The `*c` `n_closures=0` gap is **closed**. |
| C3 `nogo_installed` | **PASS** | No-Go installs strictly downstream of fired closures. |
| C2 `beta_release` | **FAIL** | All-seeds aggregation artifact: releases fire on 2/3 seeds (184, 463); fails **only** on seed-42 where `total_beta_elevated=0` (beta never engaged that seed). |
| C4 `off_holds_latch_never_closes` | **FAIL** | `C4 = arm_off.n_closures==0 AND arm_off.mean_beta_elevated >= arm_on.mean_beta_elevated`. On seeds 43/44 **ON occupancy was higher than OFF** (12.27 vs 10.07; 31.73 vs 27.67) -> the closure-coupled de-commit has **no net authority** over latch occupancy vs the OFF control. |

Per-seed `total_beta_elevated`: seed42 ON=0 / OFF=0; seed43 ON=184 / OFF=151; seed44 ON=476 / OFF=415. Guard passed 3/3; commitment+completion non-vacuity 0.667 (met); closure-trigger-availability 1.0 (met).

### 468d (`substrate_not_ready_requeue`; claims SD-034, MECH-268, MECH-090)

- Precondition `commitment_and_contradiction_engaged` = **0.333 < 0.667** -> indexer flagged `precondition_unmet`; criteria degenerate (`C1=False, C2=False`, `criteria_non_degenerate {C1:false, C2:false}`).
- Per-seed ON arm: seed42 `total_beta_elevated=123`, contradiction=5 -> non-vacuity True; seed43 `total_beta_elevated=0`, contradiction=5 -> False; seed44 `total_beta_elevated=0`, contradiction=3 -> False.
- **The binding failure is commitment, not contradiction.** Contradiction injection fired on all 3 seeds (`episodes_with_contradiction` 5/5/3 ON; 4/6/8 OFF). On seeds 43/44 the ON arm committed an E3 trajectory (`total_committed_steps` 2608/2216) but the bistable BetaGate **never registered elevated** (`total_beta_elevated=0`) -- the same commit-without-beta dissociation seen on 460d-seed42.

---

## The load-bearing finding (code-confirmed)

Both `v3_exq_460d_*.py` and `v3_exq_468d_*.py` set `lateral_pfc_train_rule_bias_head=True` (the GAP-D flag that un-zeroes the head's last `Linear`). **Grep for `optim|Adam|reinforce|.backward(|loss|bias_head_parameters` returns ZERO matches in either script** beyond the docstring/config mentions of "Leg C". The head is therefore at **random init, never task-trained**:

- The trainable-head **substrate already exists** (SD-033a GAP-D, landed 2026-05-17). Building Leg C means the *experiment* must (1) add `agent.lateral_pfc.bias_head_parameters()` to a P1 optimizer and train via the V3-EXQ-598b E3-gradient REINFORCE pattern, and (2) read de-commitment on a **non-cap-pinned ON<OFF occupancy-drop** statistic. Neither was done.
- Without a task-shaped magnitude in the rule_state, the automatic rule-stability detector is inert (Leg A's explicit hook rescued C1 regardless), and the closure-coupled de-commit has no net authority (C4: ON occupancy >= OFF). The same untrained rule_state produces the commit-without-beta fragility that gates 468d.

This is the literal "Leg C not built" the substrate doc named -- **not** a falsification of SD-034/MECH-261.

---

## Four-layer diagnosis (cohort)

| Layer | 460d | 468d |
|---|---|---|
| Claim alignment | SD-034/MECH-261 intact (closure fires, de-commit authority cannot express); MECH-260 strengthened | intact (DV never ran; no beta latch on 2/3 seeds) |
| Biological reference | clear -- OFC completion + task-set disengagement; completion->closure now coupled (Leg A) | clear -- dACC PE saturation + BG de-commit; mechanism never engaged |
| Prerequisites | **missing -- trained Leg-C `rule_bias_head` (code-confirmed flag-set-but-untrained)** | **missing -- commit-with-beta engagement (untrained rule_state -> fragile)** |
| Implementation | partial -- Leg A works, Leg B refractory installed, Leg C unbuilt | partial -- contradiction injection works; commitment/beta does not engage |
| Environment | adequate (guard 3/3, completions emitted) | adequate (subgoal_mode + counter_evidence engaged) |
| Measurement | misleading -- C2 all-seeds aggregation; C4 cap-pinned (no non-cap-pinned occupancy-drop DV) | non-vacuity gate correctly self-routed at 0.333 (caught no-commit seeds) |
| Integration | isolated -- closure fires but release has no net occupancy effect | n/a -- no beta latch to act on |
| Scale | adequate | adequate |

---

## Cluster pattern

- **Shape:** Legs A+B advanced the `*c` cohort one link (closure now fires; 460d C1 PASS, MECH-260 supports), but de-commit authority over latch occupancy is still absent (460d C4: ON >= OFF) and the agent commits-without-beta on a seed subset (`total_beta_elevated=0`: 460d-seed42, 468d-seeds43/44), gating 468d's contradiction arm.
- **Independent bugs?** No.
- **Structural property:** the wired closure control-plane fires its proximal events but carries **no net authority** over the commitment latch at the granularity the de-commit claims assert, because Leg C (trained magnitude-bearing `rule_bias_head` + non-cap-pinned DV) is experiment-side and was not built; the same untrained rule_state produces the commit-without-beta fragility. One structural property, advanced from the `*c` cohort.
- **Readings:** `experiment_side_leg_c_unbuilt`, `beta_engagement_fragility`.

---

## Recommended governance writes (governance applies; this skill does not)

| Claim | Run | Recommended direction | Notes |
|---|---|---|---|
| SD-034 | 460d | **non_contributory** + pending_retest_after_substrate | OVERRIDE self-stamped `weakens`. Closure fires (C1); de-commit authority needs trained Leg C. Provisional holds. |
| MECH-261 | 460d | **non_contributory** + pending_retest_after_substrate | OVERRIDE self-stamped `weakens`. Mode-conditioning NOT exercised (closure fired via the Leg-A bypass hook). Stays `stable`. |
| MECH-260 | 460d | **supports (narrow)** | Closure->No-Go ordering confirmed (`nogo_installed` 18/9/21 downstream of fired closures). `narrow_supports_flag`. Stays candidate / v3_pending. |
| SD-034 / MECH-268 / MECH-090 | 468d | **non_contributory** + pending_retest_after_substrate | Self-route `substrate_not_ready_requeue` CONFIRMED. Binding gap = commit-with-beta (not contradiction). No status change. |

No `epistemic_category` flip recommended: the residual is the **unbuilt experiment-side Leg C**, not a substrate ceiling. Pair every non_contributory with `pending_retest_after_substrate`; the lone surviving support (MECH-260) is **narrow** (single pathway: hook-driven closure + No-Go install; the automatic detector and de-commit authority remain unproven).

---

## Routing (user-confirmed: "Both")

1. **substrate_queue `action=amend`** on `commitment-closure-control-plane`: append the 460d + 468d failure records and the Leg C deliverable (train the existing GAP-D head via the 598b REINFORCE pattern + non-cap-pinned ON<OFF occupancy-drop DV + beta-engagement non-vacuity gate). Flag the commit-without-beta fragility as a watch item.
2. **Next actionable step: `/queue-experiment` 460e/468e** (alphabetic suffix -- same scientific question, experiment-side implementation fix). The trainable-head substrate already exists; no new `ree_core` code is required.
3. **Beta-elevation fragility:** folded into the Leg-C re-queue (beta-engagement non-vacuity gate, already partial in 468d). **Escalate** to a MECH-090 R-c-gate / scaffolded-curriculum substrate amend **only if** beta still fails to elevate on >=2/3 seeds *after* the head is trained.

GAP-4 stays in-progress; closes when the 460e/468e re-queue returns a contributory PASS (ON<OFF de-commit on a non-cap-pinned DV with beta-engagement met).
