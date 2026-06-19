# Failure Autopsy -- V3-EXQ-460g (SD-034 commitment-closure-control-plane, de-commit-AUTHORITY-MAGNITUDE retest)

- **Generated / confirmed:** 2026-06-19T20:22:03Z
- **Status:** confirmed (interactive gate; user AskUserQuestion 2026-06-19)
- **Scope:** single (one target; SD-034 closure-control-plane lineage -- 7th autopsy)
- **Predecessor:** `failure_autopsy_V3-EXQ-460f_2026-06-18` (+ `..._460e_2026-06-17`, `..._SD-034-closure-control-plane-d_2026-06-13`, `..._SD-034-closure-cluster_2026-06-12`, `..._SD-034-closure-cluster-ext_2026-06-12`, `..._V3-EXQ-460b-461b-464b-466b_2026-06-04`)
- **Substrate under test:** `commitment-closure-control-plane` (status `amend_implemented_pending_validation`) -- Legs A (env-completion hook) + B (de-commit refractory) + Leg C (scaffold_train_rule_bias_head) + BETA-ENGAGEMENT coupling (`use_closure_commit_beta_coupling`, 2026-06-17) + the **DE-COMMIT-AUTHORITY MAGNITUDE lever** (committed-run-scaled Leg-B refractory, ree-v3 main 2cd0aa2, 2026-06-19) live this run.
- **Run:** `v3_exq_460g_sd034_closure_control_plane_decommit_magnitude_20260619T185744Z_v3` (machine ree-cloud-1, supersedes 460f). FAIL, self-route `substrate_not_ready_requeue`, route_reason `closure_coupling_not_engaged`.

---

## One-line verdict

460g armed BOTH amends the 460f autopsy prescribed -- (a) the committed-run-scaled refractory MAGNITUDE lever and (b) the tightened `sd034_n_closure_coupled_elevations > 0` non-vacuity gate -- and they are **self-defeating in direct tension**: scaling the post-closure refractory to overcome the swamping natural-commit latch occupancy installs a hold that pins at the 60-tick cap (~530-560-step runs x 0.1), and while the refractory is active `BetaGate.elevate()` is a no-op, so the closure-coupled re-elevations the non-vacuity gate counts can never fire. The coupling counter collapsed **36 -> 0 on seed 42** (vs 460f) and stayed 0 on 43/44, so `closure_coupling_nonvacuous` (0/3) and `within_arm_window_nonvacuous` (1/3) both fail and the run self-routes `substrate_not_ready_requeue`. **The self-route is correct and conservative** (the tightened gate refuses to weaken SD-034 because the closure->beta coupling never engaged -- protected, NOT a false weakens), but the *implied* next step ("requeue with more magnitude") is WRONG: more magnitude deepens the suppression. This is the **structurally-different signature the 460f WATCH ITEM pre-registered as the granularity-debt trigger** (460f = "coupling fires, refractory too weak"; 460g = "the strong refractory suppresses the coupling we must measure" -- the bottleneck moved and the two levers now conflict). 7th autopsy in the SD-034 closure lineage. ROUTE (user-confirmed): `/claim-synthesis` for the SD-034 closure cluster as the load-bearing output, PLUS a 460h re-queue spec with a refractory-INDEPENDENT coupling counter. SD-034 / MECH-261 -> `non_contributory` + `pending_retest_after_substrate`; MECH-260 -> `supports` (No-Go C3 3/3, narrow positive). Seed-42 within-arm de-commit (pre 0.333 -> post 0.0) recorded as a narrow non-scoring positive existence proof.

---

## Facts reconstruction

### Readiness gates (2 of 5 fail -- the load-bearing pair)

| Gate | measured | threshold | met |
|---|---|---|---|
| foraging_contact_guard | 1.0 | 0.667 | yes |
| rule_bias_head_trained | 1.0 | 0.667 | yes (Leg C) |
| **closure_coupling_nonvacuous** (the 460f-prescribed gate: ON `sd034_n_closure_coupled_elevations > 0` AND `n_sequence_completions > 0`) | **0.0** | 0.667 | **NO** |
| closure_trigger_available_count (n_closures > 0) | 1.0 | 0.667 | yes |
| **within_arm_window_nonvacuous** (>= C2_MIN_WINDOW_EVENTS scored windows with mean_pre_occ > floor) | **0.333** | 0.667 | **NO** |

`criteria_non_degenerate` = {C1 false, C2 false, C3 false}; `overall_pass` false; per-seed criteria pass `[true, false, false]`; route_reason `closure_coupling_not_engaged`.

### Per-seed ARM_CLOSURE_ON (the coupling regression)

| seed | n_closures (hook/auto) | `sd034_n_closure_coupled_elevations` | n_window_events | mean_pre_occ | mean_post_occ | C2 (within) |
|---|---|---|---|---|---|---|
| 42 | 9 (9/0) | **0** (460f: 36) | 2 | 0.333 | **0.0** | PASS |
| 43 | 6 (6/0) | **0** | 0 | 0.0 | 0.0 | FAIL |
| 44 | 5 (5/0) | **0** | 0 | 0.0 | 0.0 | FAIL |

Closures + No-Go + sequence completions all fire (No-Go installed 27/18/15; n_sequence_completions 9/6/5). The coupling counter -- the metric the de-commit DV needs to be scorable -- is zero on every seed, including seed 42 where it was 36 in 460f.

### The self-defeating interaction (code-confirmed)

- `BetaGate.apply_refractory(n)` sets `_refractory_remaining = max(_refractory_remaining, n)` (beta_gate.py:116).
- `BetaGate.elevate()` is a **no-op while `_refractory_remaining > 0`** (beta_gate.py:138) and otherwise resets `_committed_run_length = 0`.
- `note_closure_coupled_elevation()` (the counter source) is called ONLY after a successful `elevate()` in the bistable coupling block (agent.py:6082-6083, guarded by `_closure_commit_active and not result.committed`).
- The 460g magnitude lever: `ClosureOperator._fire()` captures `run_length_at_fire = beta_gate.committed_run_length` BEFORE `release()`, then installs `apply_refractory(closure_decommit_hold_ticks + round(0.1 * run_length), cap 60)`.

Net: each closure (sequence completion) calls `release()` + installs a refractory that, at ~530-560-step committed runs, **pins at the 60-tick cap**. For the rest of the post-closure episode the gate is refractory-blocked, so subsequent closure-plane commitments cannot drive an `elevate()` -> `note_closure_coupled_elevation()` is never reached -> the counter stays 0. In 460f the fixed 5-tick refractory left gaps where seed-42's 36 coupled elevations could fire; the magnitude lever closed those gaps. **The fix for "refractory too weak" (460f) created "refractory suppresses the coupling metric" (460g).**

### claim_ids accuracy: MECH-261 not exercised (unchanged from 460f)

`n_hook_fires == n_closures` and `n_automatic_fires = 0` on all three seeds. Every closure came from the Leg-A `notify_env_completion -> emit_closure` hook, NOT the automatic rule_state-stability detector MECH-261's mode-conditioning predicate gates. The hook bypasses mode-conditioning, so the run does not exercise MECH-261; it must not weaken a stable claim (the EXQ-048/MECH-057b inherited-tag class). The manifest's `mech261_note` already protects this (`non_contributory unless n_automatic_fires > 0`).

---

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | SD-034 partial (seed-42 positive) / MECH-261 NOT exercised / MECH-260 exercised+passed | SD-034 de-commit authority shows on seed 42 (pre 0.333 -> post 0.0) but cannot be certified closure-coupled (counter 0). MECH-261 mode-conditioning bypassed (n_automatic_fires=0). MECH-260 No-Go 3/3. |
| Biological reference | clear | Rich & Shapiro 2009 OFC completion cells; Collins & Frank 2014 task-set disengagement. Release magnitude must scale with re-commitment pressure -- but a fixed-or-scaled refractory that BLOCKS re-elevation also blocks the coupling-driven re-elevations being measured. The metric, not the mechanism, is the new fault. |
| Prerequisites | present (Legs A/B/C + coupling + magnitude) | Every leg built and firing; no missing leg. |
| Implementation | partial -- self-defeating lever/metric coupling | The magnitude lever (apply_refractory cap 60) and the coupling non-vacuity counter (counts refractory-surviving elevations) are coupled through the SAME refractory window. Scaling one zeroes the other. |
| Environment | adequate | guard 3/3; closures + completions + No-Go on all seeds. |
| Measurement | **mis-instrumented (the binding fault)** | `sd034_n_closure_coupled_elevations` counts elevations that BOTH are closure-driven AND survive the refractory. It should count closure-plane commit INTENTS (e3._committed_trajectory forming while not result.committed) independent of whether the refractory then blocks the elevate. As built, the metric is confounded by the very lever under test. |
| Integration | partially coupled but the de-commit and coupling-readout are entangled | The de-commit refractory works (seed-42 occupancy 0.333 -> 0.0) but it suppresses its own coupling certifier. |
| Scale / capacity | adequate | not the binding gap. |

**Recommended epistemic_category:** keep SD-034 `non_contributory` + `pending_retest_after_substrate` (no status/confidence change). The dominant reading is a **measurement/test-design entanglement on top of a granularity-debt recurrence** -- not `substrate_ceiling` (the substrate carries and expresses the de-commit on seed 42), not a falsification (the coupling was never fairly measured).

---

## Recurrence / granularity-debt (the 460f WATCH ITEM fired)

This is the **7th autopsy** circling SD-034 closure: 460b-cluster (06-04) -> SD-034-cluster + ext (06-12) -> control-plane-d (06-13) -> 460e (06-17) -> 460f (06-18) -> **460g (06-19)**. The 460f autopsy pre-registered the exact trigger:

> WATCH ITEM: ... If the 460g retest (post de-commit-magnitude amend) ALSO fails on a structurally-different signature, that recurrence tips into granularity-debt territory and the SD-034 closure cluster should be handed to `/claim-synthesis`.

460g's signature IS structurally different from 460f. The claim "the SD-034 ClosureOperator has behavioural de-commit authority over the MECH-090 latch" keeps fragmenting into distinct finer mechanisms each iteration: closure-fires? (460c/d) -> head-trained? (460d/e) -> beta-engages? (460e/f) -> refractory-strong-enough? (460f) -> **does a strong-enough refractory suppress the very coupling we measure de-commit by?** (460g). Each is a separate testable sub-mechanism the coarse claim does not name. That is granularity debt, not one clean falsification.

---

## Learning extracted

- The committed-run-scaled de-commit refractory has **de-commit authority** (seed-42 within-arm occupancy 0.333 -> 0.0) but **suppresses the closure-coupled-elevation counter** it is measured by, because both ride the same `_refractory_remaining` window and `elevate()` is a no-op during it.
- A coupling non-vacuity gate keyed on `sd034_n_closure_coupled_elevations` is **confounded by any de-commit lever that blocks re-elevation**. The fair non-vacuity readout is the closure-plane commit INTENT (e3._committed_trajectory forming while not result.committed), counted BEFORE the elevate/refractory gate -- not the refractory-surviving elevation.
- The 460f-prescribed (a) magnitude + (b) tightened-gate pair are in **mutual tension**; iterating magnitude alone (a 460h with even larger holds) makes the coupling readout worse, not better.
- **claim_ids hygiene (unchanged):** a Leg-A-hook-only run (n_automatic_fires=0) does not exercise MECH-261 mode-conditioning; do not weaken the stable claim.

---

## Repair pathway (user-confirmed routing)

**PRIMARY: `/claim-synthesis` on the SD-034 closure cluster.** The 7-autopsy recurrence with structurally-different signatures and now mutually-tensioned levers is the load-bearing output -- the pre-registered granularity-debt trigger. Hand the cluster for proposal-first, lit-grounded decomposition into testable children (e.g. closure-firing vs closure->beta-coupling-engagement vs de-commit-authority-magnitude vs coupling-measurability-under-refractory as named sub-claims). NOT demotion -- SD-034 is coarse here, not wrong.

**SECONDARY (concrete substrate next-step, recorded as the 460h spec): `/queue-experiment` 460h** with a refractory-INDEPENDENT coupling readout: count closure-plane commit INTENTS (e3._committed_trajectory forming while `not result.committed`) regardless of whether the refractory then blocks the `elevate()`, and score the within-arm around-closure occupancy drop that already works on seed 42 against that intent-based non-vacuity gate. This decouples the de-commit-authority lever from its own certifier so the magnitude amend can be scored without zeroing the metric. Re-issue as 460h (new letter; do NOT re-author 460d/e/f/g).

---

## Draft evidence_quality_note (governance applies; this skill does not write it)

> V3-EXQ-460g (supersedes 460f): the committed-run-scaled de-commit-magnitude lever + the 460f-prescribed tightened coupling non-vacuity gate are SELF-DEFEATING -- the scaled refractory pins at the 60-tick cap on ~530-560-step runs, and BetaGate.elevate() is a no-op while the refractory is active, so the closure-coupled re-elevations the gate counts can never fire (sd034_n_closure_coupled_elevations collapsed 36 -> 0 on seed 42, 0/3 overall). Autopsy (failure_autopsy_V3-EXQ-460g_2026-06-19, confirmed): the de-commit refractory HAS authority (seed-42 within-arm occupancy 0.333 -> 0.0, C2 PASS) but suppresses its own coupling certifier; the self-route substrate_not_ready_requeue is correct and conservative (no false weakens) but a larger-magnitude 460h would deepen the suppression. SD-034 -> non_contributory + keep pending_retest_after_substrate (measurement/test-design entanglement + granularity-debt recurrence; de-commit-authority not fairly certifiable on the current coupling metric). MECH-261 -> non_contributory: all closures hook-driven (n_automatic_fires=0), mode-conditioning bypassed -- do not weaken the stable claim. MECH-260 -> supports (No-Go nogo_installed >= 1 on 3/3, narrow positive). 7th autopsy in the SD-034 closure lineage; the 460f WATCH ITEM granularity-debt trigger fired -> route /claim-synthesis (primary) + 460h re-queue with a refractory-independent commit-intent coupling counter (secondary).

---

## Routing decision (user-confirmed 2026-06-19)

1. **`/claim-synthesis`** on the SD-034 closure cluster -- PRIMARY, the load-bearing output (pre-registered 460f WATCH ITEM trigger fired; 7-autopsy recurrence; structurally-different signature; mutually-tensioned levers).
2. **`/queue-experiment` 460h** (secondary, recorded) -- refractory-INDEPENDENT coupling counter (closure-plane commit INTENT, counted before the elevate/refractory gate) + score the seed-42-style within-arm de-commit against it. New letter; do NOT re-author 460d/e/f/g.
3. **Evidence disposition (mirror 460f):** SD-034 -> `non_contributory` + keep `pending_retest_after_substrate`. MECH-261 -> `non_contributory` (not exercised; protect stable claim). MECH-260 -> `supports` (No-Go C3 3/3, narrow non-promoting positive). Seed-42 ON within-arm drop (0.333 -> 0.0) recorded as a narrow non-scoring positive existence proof of de-commit authority.
4. **pending_retest_after_substrate:** TRUE for SD-034 + MECH-261 (+ MECH-260) until a contributory PASS on a refractory-independent coupling metric OR the cluster is re-grained by /claim-synthesis.
5. **Plan-node:** `commitment_closure:GAP-4` owner_exq is to be repointed 460f -> 460g and its resume_condition refreshed to the /claim-synthesis hand-off + 460h spec by the session that holds `commitment_closure_plan.md` or a later governance walk (NOT reconciled here; a concurrent /governance session holds the governance collision set).
6. **Owed successor:** 460h (post refractory-independent-metric design) -- separate /queue-experiment session, gated on the /claim-synthesis decomposition (so 460h targets the re-grained child, not the coarse SD-034 closure umbrella). The 468e MECH-090 commit-entry conjunction leg remains separately owed.

commitment_closure:GAP-4 stays in-progress; closes when a contributory PASS shows the closure-coupled de-commit lowers within-arm post-closure occupancy on a refractory-independent coupling metric on >= 2/3 seeds.
