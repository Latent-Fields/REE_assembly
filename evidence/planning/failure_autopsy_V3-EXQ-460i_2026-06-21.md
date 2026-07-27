# Failure Autopsy -- V3-EXQ-460i (rung-6 natural-commit-occupancy-release lever)

- **Run:** `v3_exq_460i_natural_commit_occupancy_release_decommit_falsifier_20260621T023222Z_v3`
- **Queue:** V3-EXQ-460i  | **Claims:** MECH-446 (scored DV), MECH-445 (commit-intent precondition)
- **Machine:** ree-cloud-2  | **Generated:** 2026-06-21T05:39:13Z  | **Status:** confirmed (user-adjudicated 2026-06-21, Option B + lever/gate amend)
- **Outcome:** FAIL / `non_contributory`; self-routed `substrate_not_ready_requeue` at readiness gate 3 (`route_reason=lever_did_not_shorten_occupancy`).

This adjudicates the gate-3 self-route the 2026-06-21 governance cycle left un-applied. It does **not** edit claims.yaml / the manifest / substrate_queue (governance applies the recommendation).

---

## 1. Facts (no interpretation)

The experiment trains one curriculum per seed (lever OFF during training) then evaluates **four arms**, each a clone of the same trained weights with the rung-6 lever toggled at eval (the lever carries no trainable parameters, so the clone is exact):

- `ARM_LEVER_OFF` (460h baseline / occupancy reference), `ARM_GAP_SCALED` (PRIMARY, graded urgency, gap_entry_sensitivity=1.0), `ARM_FLAT_RATE` (fixed-refractory control, sensitivity=0), `ARM_ACTION_EXTENT` (Jin rendering).

Six readiness gates must all clear before the load-bearing CO_OCCURRENCE DV is scored. The self-route stops at the **first** failed gate.

**Readiness gate states (manifest `acceptance`):**

| Gate | Met | Fraction |
|---|---|---|
| 1 foraging_contact_guard | yes | 1.0 |
| 2 rule_bias_head_trained | yes | 1.0 |
| **3 natural_commit_lever_shortened_occupancy** | **NO** | **0.0** |
| 4 closure_coupling_nonvacuous (MECH-445) | no | 0.0 |
| 5 closure_trigger_available | yes | 1.0 |
| 6 within_arm_window_nonvacuous | no | 0.0 |

`criteria_non_degenerate` = false for both criteria; the CO_OCCURRENCE DV never ran. `per_seed_guard_pass = [true, true, true]`.

**The lever fired zero releases on every armed arm and seed** (`ncur_n_releases_total=0`, `ncur_n_urgency_releases=0`, `ncur_n_action_extent_releases=0`, `ncur_mean_*=0.0`).

**Per-seed beta dynamics (ARM_GAP_SCALED, the primary):**

| seed | total_committed_steps | total_beta_elevated | beta_release_events | mean_beta_elevated_steps | avg single-hold (elev/rel) | n_closures | sd034_n_closure_commit_intent | sd034_n_closure_coupled_elevations | ncur_n_releases_total |
|---|---|---|---|---|---|---|---|---|---|
| 42 | 0 | 0 | 0 | 0.0 | -- | 8 | 0 | 0 | 0 |
| 43 | 2610 | 536 | 523 | 35.7 | ~1.02 | 10 | 0 | 0 | 0 |
| 44 | 1432 | 104 | 103 | 6.9 | ~1.01 | 3 | 0 | 0 | 0 |

ARM_LEVER_OFF mirrors the fragmentation (seed 43: 415 elevated / 405 releases ~= 1.02 tick/hold; seed 44: 143/143 = 1.0). Seed 42 formed no commits at all (`hazard_stage_survival_pass=false`).

---

## 2. The decisive disambiguation (V3-EXQ-642 fresh-substrate-mislabel check)

The manifest self-routed `lever_did_not_shorten_occupancy`. The autopsy adjudicates **why** the lever did nothing -- the two readings the user posed:

### (A) Config / wiring gap (lever not armed) -> re-queue with the lever armed. **RULED OUT.**
- `_make_config` leaves the lever OFF on the trained base; [`_clone_arm`](https://github.com/Latent-Fields/ree-v3/blob/main/experiments/v3_exq_460i_natural_commit_occupancy_release_decommit_falsifier.py) explicitly sets `use_natural_commit_urgency_release = lv["on"]` + `urgency`/`action_extent`/`gap_sensitivity` per arm. Manifest confirms `lever_present: true` on all three armed arms (`false` only on ARM_LEVER_OFF).
- The eval runs the full `agent.select_action` path, so the lever's arm-site (`note_commit_entry`) and release-site (`tick`) were reachable.

### (B) Armed but ineffective -> substrate finding routing to a lever amend. **CONFIRMED (refined).**

**The arm-site WAS reached at runtime, and the commits were NATURAL.** Per the MECH-445 beta-engagement wiring, `note_commit_entry` is called on `result.committed` (the natural arm); `note_closure_commit_intent` / `note_closure_coupled_elevation` fire on the closure-coupled path. Both closure certifiers are **0** on every seed, while `total_beta_elevated > 0` on seeds 43/44 -- so the beta elevations were natural `result.committed` commits (not closure-coupled), and `note_commit_entry` fired on each one. The lever armed every commit.

**The lever fired zero because the natural-commit latch is fragmented, not sustained.** Average single-hold length `= total_beta_elevated / beta_release_events ~= 1.0 tick` (seed 43: 536/523; seed 44: 104/103) -- ~35 re-commits/episode, each a ~1-tick blip. The urgency accumulator (`urgency += 0.01 * decisiveness_scale`, **reset to 0 on each fresh `note_commit_entry`**) needs ~50-100 *consecutive* held ticks to reach `release_bound=1.0`; over ~1 tick it accrues ~0.01-0.02 then resets. Action-extent mode likewise never completes a committed trajectory in ~1 tick.

So: the seeds *did* form natural commits, but they are **transient/fragmented, not the sustained monolithic holds the lever shortens** -- "nothing (sustained) to shorten." This is Option B.

### Root cause
The 460h **sustained monolithic natural-commit-hold regime (~2400-2600 steps)** -- the premise of the disjoint-certifier problem AND the operating premise of the rung-6 lever -- **did not reproduce** in the 460i eval. **ARM_LEVER_OFF also cycles ~1-tick**, so the fragmentation is the full active de-commit control-plane (Leg-B committed-run-scaled refractory + MECH-342 maintenance-release + closure releases) dropping the latch -- **not** the lever. There was no sustained occupancy for the lever to act on.

### Measurement gap
Readiness gate 3's occupancy proxy is `mean_beta_elevated_steps` (per-episode average), which is **blind to sustained-vs-fragmented**: it cleared its `>0.5` floor (27.7 / 9.5) on ~35 fragmented 1-tick commits, mis-certifying "occupancy present to shorten." Gate 3 short-circuited on the missing `ncur_n_releases_total > 0` clause anyway, so the route reason is correct; but had the lever fired once, the drop comparison would still have been computed against a sustained-blind proxy.

---

## 3. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | intact | no fair test reached; self-route correctly prevented scoring |
| Biological reference | clear | BG-3 D1 graded-urgency release (Thura/Cisek 2022; Jin 2014) is a faithful translation; failure is not in the mechanism |
| Prerequisites | **missing** | the 460h sustained natural-commit-hold regime is absent in eval |
| Implementation completeness | complete | lever wired + armed (config + runtime) + arm-site reached on natural commits |
| Environment / regime adequacy | **wrong pressures** | active de-commit plane fragments the latch to ~1 tick even with the lever OFF |
| Measurement adequacy | **misleading** | gate-3 `mean_beta_elevated_steps` proxy blind to sustained-vs-fragmented occupancy |
| Integration | isolated | urgency resets per fresh entry; rapid re-committing structurally caps urgency below `release_bound` |
| Scale / capacity | adequate | not a budget issue |

---

## 4. Repair pathway -- `implement-substrate` (amend)

Recommended `substrate_queue` action **amend** on `f_dominance_conversion_ceiling` (rung 6: NaturalCommitUrgencyRelease). Two coupled parts:

1. **Readiness-gate redesign.** Replace gate 3's sustained-blind `mean_beta_elevated_steps` proxy with a **sustained-hold proxy** -- longest consecutive beta-elevated run on the OFF arm, or mean per-commit hold length `total_beta_elevated / max(1, beta_release_events)` -- above a floor, so the gate certifies the 460h monolithic-hold regime IS present before the co-occurrence DV is allowed.
2. **Establish the sustained-hold regime in eval.** Diagnose which release mechanism fragments the OFF-baseline latch to ~1 tick (Leg-B committed-run-scaled de-commit refractory vs MECH-342 maintenance-release vs closure releases vs marginal `running_variance` flicker around the natural commit threshold) and either re-establish the F-decisive strong-commit regime the 460h finding described, or make the OFF baseline actually sustain. Until a sustained natural-commit hold exists in the OFF arm, the rung-6 urgency lever (and the disjoint-certifier problem it dissolves) cannot be exercised.

Independent side-finding: **seed 42 nav-competence under-train** (`total_committed_steps=0`, `hazard_stage_survival_pass=false`) -- a separate `scaffolded_sd054_onboarding` Stage-H matter, not the lever question.

**Granularity-debt check:** the 460e/f/g/h/i lineage is a **coherent substrate-build campaign** on one mechanism (each autopsy finds the next prerequisite link; each prior fix advanced the build), NOT multi-signature granularity debt circling a coarse claim. No `/claim-synthesis` recommendation.

---

## 5. Governance hand-off (not applied here)

- **evidence_direction:** `non_contributory` (both MECH-446 and MECH-445); **no weakens** -- no fair test was reached.
- **Claims:** MECH-446 and MECH-445 stay `candidate / v3_pending / pending_retest_after_substrate` (commitment-closure-control-plane). Unchanged.
- **evidence_quality_note** (draft, for governance to write): see the JSON `recommended_evidence_quality_note`.
- **Retest gate:** a working amend must (a) certify a sustained natural-commit hold in `ARM_LEVER_OFF` (sustained-hold proxy above floor on >= 2/3 guard seeds) and (b) produce `ncur_n_releases_total > 0` with a >= `LEVER_OCC_DROP_FRAC` occupancy drop vs OFF on the gap-scaled arm, before the CO_OCCURRENCE DV is scored.
