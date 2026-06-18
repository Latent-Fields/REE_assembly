# Failure Autopsy -- V3-EXQ-460f (SD-034 commitment-closure-control-plane, de-commit DV on the beta-engagement amend)

- **Generated / confirmed:** 2026-06-18T06:03:54Z
- **Status:** confirmed (interactive gate; user AskUserQuestion 2026-06-18)
- **Scope:** single (one target; SD-034 closure-control-plane lineage)
- **Predecessor:** `failure_autopsy_V3-EXQ-460e_2026-06-17` (+ `..._SD-034-closure-control-plane-d_2026-06-13`, `..._SD-034-closure-cluster_2026-06-12`)
- **Substrate under test:** `commitment-closure-control-plane` (status `amend_implemented_pending_validation`) -- Legs A (env-completion hook) + B (de-commit refractory, hold=5) landed 2026-06-12; Leg C (scaffold_train_rule_bias_head) landed 2026-06-16; **BETA-ENGAGEMENT amend (`use_closure_commit_beta_coupling`, ree-v3 main f4ceea4, 2026-06-17) live this run.**
- **Run:** `v3_exq_460f_sd034_closure_control_plane_decommit_behavioural_20260617T222759Z_v3` (machine ree-cloud-4, supersedes 460e). FAIL, self-route `residual_decommit_authority_open`, route_reason `decommit_dv_unmet_genuine_weakens`.

---

## One-line verdict

The beta-engagement amend **worked** -- all four non-vacuity preconditions cleared this run (foraging contact 1.0, rule_bias_trained 1.0, beta_engagement_both_arms 1.0, closure_trigger_available 1.0), so for the first time in this lineage the load-bearing **C2 de-commit occupancy-drop DV actually ran**. C2 **PASSED on 1/3 seeds (seed 42)** and FAILED on 43/44, so the run self-routed a genuine weakens. But the autopsy reading is **NOT a falsification and NOT a fair-test genuine weakens**: (i) the amend's own coupling diagnostic (`sd034_n_closure_coupled_elevations`) fired **36/52 on seed 42 but 0/0 on seeds 43/44** -- the coupling only did work on the one weak-natural-commit seed it was built for; on 43/44 strong natural commit-entry made the coupling inert and the comparison reduced to the bare Leg-B refractory, whose **magnitude (5 ticks x 4-7 closures ~ 20-35 tick-blocks vs ~530-560 natural-commit elevated steps) is swamped**; and (ii) the C2 DV is a **between-arm, unpaired, stochastic-eval-episode occupancy comparison** -- underpowered for a few-tick-per-closure effect. Seed 42 (this run) + seed 44 (460e, ON 11.73 < OFF 14.87) are **existence proofs that the de-commit mechanism has the right sign**; the gap is de-commit **authority magnitude** + DV **power**, a substrate/measurement gap. Separately, the self-stamped **MECH-261 weakens is mis-attributed** -- every closure was hook-driven (`n_automatic_fires = 0`), so the Leg-A env-completion hook **bypassed the MECH-261 mode-conditioning predicate**, which the run never exercises. Route to `/implement-substrate` **amend** of `commitment-closure-control-plane` (de-commit-magnitude lever + within-arm around-closure C2 DV); SD-034 / MECH-261 -> `non_contributory` + `pending_retest_after_substrate`; MECH-260 -> `supports` (No-Go C3 3/3, narrow positive).

---

## Facts reconstruction

### Readiness gates (all four cleared -- the C2 DV ran for the first time)

| Gate | measured | threshold | met |
|---|---|---|---|
| foraging_contact_guard | 1.0 | 0.667 | yes |
| rule_bias_head_trained | 1.0 | 0.667 | yes (Leg C) |
| **beta_engagement_both_arms** | **1.0** | 0.667 | **yes (the 460e blocker; beta-coupling amend fix)** |
| closure_trigger_available_count | 1.0 | 0.667 | yes (n_closures 4-9) |

`criteria_non_degenerate` = {C1: true, C2: true, C3: true}; `overall_pass` false; per-seed criteria pass `[true, false, false]`.

### Per-seed C2 de-commit DV (load-bearing): ON mean_beta_elevated_steps < OFF, >= 10% relative drop, OFF > 0.5

| seed | ON occ | OFF occ | C2 | drop | `sd034_n_closure_coupled_elevations` ON/OFF | ON n_closures (hook/auto) | ON committed_steps | ON total_beta_elevated |
|---|---|---|---|---|---|---|---|---|
| 42 | **23.73** | 35.67 | **PASS** | -33.5% | **36 / 52** | 9 (9/0) | 1826 | 356 |
| 43 | 37.33 | 35.73 | FAIL | ON > OFF | **0 / 0** | 4 (4/0) | 2804 | 560 |
| 44 | 10.53 | 9.4 | FAIL | ON > OFF | **0 / 0** | 7 (7/0) | 2412 | 158 |

C2 passes 1/3 (need 2/3). C1 (n_closures >= 1) 3/3; C3 (nogo_installed >= 1) 3/3.

### Two load-bearing observations

**(1) The coupling fired only on the seed it was built for.** `sd034_n_closure_coupled_elevations` counts beta elevations driven by `_closure_commit_active AND NOT result.committed` (agent.py:5877-5894) -- i.e. coupling-driven elevations that the natural `running_variance < commit_threshold` path would not have produced. 36/52 on seed 42 (the lowest-committed-steps ON arm, 1826 -- the weak-natural-commit seed the 460e autopsy predicted) vs **0/0 on seeds 43/44** (committed_steps 2804/2412). On 43/44 `result.committed` always co-occurred with `e3._committed_trajectory`, so the coupling added nothing and beta occupancy was dominated by identical natural commit-entry on both arms. The `beta_engagement_both_arms` gate (which only asserts `total_beta_elevated > 0`) passed **vacuously w.r.t. the coupling** -- it confirmed beta elevates, not that the coupling made the DV sensitive to the closure de-commit.

**(2) With the coupling inert on 43/44, ON-vs-OFF isolates exactly the Leg-B refractory -- and it is swamped.** Both arms share trained weights + running_variance; the only ON/OFF difference is the ClosureOperator (Leg-A hook firing closures -> Leg-B `apply_refractory(5)` + MECH-260 No-Go + residue discharge). The refractory blocks re-elevation for 5 ticks x 4-7 closures = ~20-35 tick-blocks, against ON `total_beta_elevated` ~530-560. The net effect on occupancy is ~0 (ON even runs slightly higher: closure-plane drives more commitment / cross-arm stochastic variance on unpaired episodes). The refractory has the **correct sign** but **sub-threshold magnitude**; it is visible on seed 42 only because there latch occupancy is coupling-dominated and lower overall, so the refractory is proportionally large.

### claim_ids accuracy: MECH-261 not exercised

`n_hook_fires == n_closures` and `n_automatic_fires = 0` on all three seeds. Every closure came from the Leg-A `notify_env_completion -> emit_closure` hook, **not** from the automatic rule_state-stability detector that MECH-261's mode-conditioning predicate (`allowed_closure_modes` + `sd_033a` write-gate floor) actually gates. The hook bypasses mode-conditioning. So the manifest's `evidence_direction_per_claim["MECH-261"] = "weakens"` -- which the script ties mechanically to the C2 outcome (`supports if overall_criteria_pass else weakens`) -- is mis-attributed: the run does not test MECH-261's mechanism. MECH-261 is `stable` (exp_conf 0.724); a non-exercising run must not weaken it (the EXQ-048/MECH-057b inherited-tag failure-mode class).

---

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | SD-034 partial / MECH-261 NOT exercised / MECH-260 exercised+passed | SD-034 DV ran, non-vacuous, expressed on seed 42 -- partially fair. MECH-261 mode-conditioning bypassed by the Leg-A hook (n_automatic_fires=0) -- do not weaken. MECH-260 No-Go installed 3/3. |
| Biological reference | clear | Sequence-completion -> beta-latch release (Rich & Shapiro 2009 OFC completion cells; Collins & Frank 2014 task-set disengagement). Release magnitude must scale with how strongly the agent would otherwise re-commit; a fixed 5-tick block is sub-threshold against strong natural re-commitment. |
| Prerequisites | present (Legs A/B/C) | env hook + refractory + trained head all built and firing. The residual prerequisite is de-commit-authority MAGNITUDE, not another missing leg. |
| Implementation | partial | Leg-B refractory is a fixed 5-tick re-elevation block; insufficient authority over the latch when natural commit dominates. Coupling makes the DV readable only when natural commit is weak. |
| Environment | adequate | guard 3/3; closures + sequence completions + No-Go fire on all seeds. |
| Measurement | **under-instrumented** | C2 is a between-arm, unpaired, stochastic-eval-episode occupancy comparison -- cross-arm variance + natural-commit baseline dwarf a few-tick-per-closure refractory. A within-arm around-closure (pre-vs-post-closure window) occupancy delta would isolate the refractory. |
| Integration | partially coupled | Coupling -> beta engaged on every seed (the 460e fix) BUT only adds non-natural elevations on the weak-commit seed; on strong-commit seeds the de-commit refractory is decoupled (by magnitude) from a measurable occupancy drop. |
| Scale / capacity | adequate | not the binding gap (eval=15, closures fire). |

**Recommended epistemic_category:** `substrate_ceiling` -- the substrate carries the wiring SD-034 asserts (closure -> refractory -> latch) and expresses it (seed 42 / 460e seed 44), but not at the de-commit-authority magnitude or DV sensitivity needed to clear >= 2/3 on the between-arm occupancy DV. The response is substrate/DV enrichment, not more runs on the current parameterization, and not demotion.

---

## Recurrence check (granularity-debt / `/claim-synthesis` trigger)

Fourth autopsy in the SD-034 closure lineage (cluster 2026-06-12 -> -d 2026-06-13 -> 460e 2026-06-17 -> 460f). The signatures continue to **advance one structural property link-by-link** -- Leg-A hook (n_closures=0) -> Leg-C trained head (de-commit authority absent) -> beta-engagement fragility (460e) -> now **de-commit MAGNITUDE / DV power** (460f, the first run where the C2 DV actually ran). Each closes one prerequisite and surfaces the next predicted one; this is the pre-registered escalation chain, NOT structurally-different signatures circling one coarse claim. Consistent with the 460e autopsy's reading: **NOT granularity debt; `/claim-synthesis` is not the route.** WATCH ITEM: this is the second consecutive "next prerequisite surfaces" link past 460e. If the 460g retest (post de-commit-magnitude amend) ALSO fails on a structurally-different signature, that recurrence tips into granularity-debt territory and the SD-034 closure cluster should be handed to `/claim-synthesis`.

---

## Learning extracted

- The beta-engagement coupling (460e fix) is **necessary but seed-conditional**: it engages the latch on the closure-plane commit only when the natural `running_variance < commit_threshold` crossing does NOT also fire (the weak-commit seed); on strong-natural-commit seeds it is inert and the de-commit DV reduces to the bare Leg-B refractory.
- The Leg-B de-commit refractory has the **correct sign** (de-commit lowers occupancy: seed 42 -33.5%, 460e seed 44) but **insufficient authority magnitude** to move a between-arm occupancy statistic against ~530-560 natural-commit elevated steps. A fixed 5-tick block is not enough.
- The C2 between-arm unpaired DV is **underpowered** for a few-tick-per-closure effect; a within-arm around-closure (pre-vs-post) occupancy delta would isolate the refractory from cross-arm stochastic variance and the natural-commit baseline.
- The `beta_engagement_both_arms` readiness gate is **necessary but not sufficient** as a non-vacuity gate for the de-commit DV: it asserts beta elevates, not that the coupling makes the per-seed DV sensitive to the closure de-commit. A stronger gate would require `sd034_n_closure_coupled_elevations > 0` on the scored seeds (so the closure -- not a natural commit -- is the elevation source the de-commit acts on).
- **claim_ids hygiene:** a Leg-A-hook-only run does not exercise MECH-261 mode-conditioning (`n_automatic_fires = 0`); do not let it weaken a stable claim.

## Repair pathway (user-confirmed routing)

`/implement-substrate` **amend** on the existing `commitment-closure-control-plane` substrate_queue entry (do NOT duplicate). Deliverable: de-commit **authority magnitude** + DV **sensitivity** (user-confirmed BOTH):

- **(a) de-commit authority magnitude** -- make the Leg-B de-commit hold scale with the committed-run length (e.g. refractory proportional to `committed_steps`-since-entry), or convert the de-commit from a fixed re-elevation block into an active maintenance-release-pressure event (MECH-342 `CommitMaintenanceRelease`-style) so a closure fire actually drives the latch DOWN rather than merely blocking re-entry for 5 ticks;
- **(b) within-arm C2 DV** -- redesign C2 to a within-arm around-closure occupancy delta (pre-closure vs post-closure window on the ON arm), isolating the refractory effect from cross-arm stochastic variance + the natural-commit baseline; tighten the non-vacuity gate so scored seeds require `sd034_n_closure_coupled_elevations > 0` (the closure, not a natural commit, is the elevation source the de-commit acts on).

Retest gate (after amend): on >= 2/3 guard seeds with the coupling engaged, the within-arm around-closure occupancy drops post-closure AND ON < OFF on the (now-sensitized) cross-arm statistic. Re-issue as **460g**.

## Draft evidence_quality_note (governance applies; this skill does not write it)

> V3-EXQ-460f (supersedes 460e): the beta-engagement amend (use_closure_commit_beta_coupling) cleared all four readiness gates so the C2 de-commit occupancy-drop DV ran for the first time; it PASSED on seed 42 (ON 23.73 < OFF 35.67, -33.5%) but FAILED 2/3. Autopsy (failure_autopsy_V3-EXQ-460f_2026-06-18, confirmed): NOT a fair-test weakens. The coupling diagnostic sd034_n_closure_coupled_elevations fired 36/52 on seed 42 but 0/0 on seeds 43/44 -- on strong-natural-commit seeds result.committed always co-occurred with the closure-plane commit, so the coupling was inert and the DV reduced to the bare Leg-B 5-tick refractory, whose magnitude (~20-35 tick-blocks vs ~530-560 natural-commit elevated steps) is swamped; the between-arm unpaired occupancy DV is also underpowered for a few-tick-per-closure effect. Seed 42 (this run) + seed 44 (460e, ON 11.73 < OFF 14.87) are existence proofs that the de-commit mechanism has the correct sign. SD-034 -> non_contributory + pending_retest_after_substrate (substrate-limited: de-commit-authority magnitude + between-arm-DV power). MECH-261 -> non_contributory: all closures were hook-driven (n_automatic_fires=0), so the Leg-A env-completion hook bypassed the MECH-261 mode-conditioning predicate -- the run does not exercise it; do not weaken the stable claim. MECH-260 -> supports (No-Go nogo_installed >= 1 on 3/3, narrow positive). Substrate amend: commitment-closure-control-plane de-commit-authority-magnitude lever + within-arm around-closure C2 DV; re-issue 460g.

---

## Routing decision (user-confirmed)

1. **substrate_queue `action=amend`** on `commitment-closure-control-plane`: append the 460f failure record + the de-commit-authority deliverable (mechanism (a) magnitude lever + (b) within-arm around-closure C2 DV; tighten the non-vacuity gate to require `sd034_n_closure_coupled_elevations > 0` on scored seeds). Status stays `amend_implemented_pending_validation`; `ready` stays false.
2. **Evidence disposition:** SD-034 -> `non_contributory` + keep `pending_retest_after_substrate` (no status/confidence change). MECH-261 -> `non_contributory` (not exercised; correct the mis-attributed weakens) + keep `pending_retest_after_substrate`; protect the stable claim. MECH-260 -> `supports` (No-Go C3 3/3, recorded as a narrow non-promoting positive observation). Seed-42 ON<OFF recorded as a narrow non-scoring positive observation for the de-commit DV.
3. **pending_retest_after_substrate:** TRUE for SD-034 + MECH-261 (and MECH-260) until the post-amend 460g re-queue returns a contributory PASS.
4. **Plan-node:** `commitment_closure:GAP-4` owner_exq still pins 460e; **NOT reconciled by this session** -- `commitment_closure_plan.md` is held by an active (now ~15h stale) claim `gap8-sd033b-485g`. Flagged to the user; reconcile (repoint owner_exq -> 460g, refresh resume_condition) in the session that holds the file or a later governance walk.
5. **Owed successor:** 460g (post de-commit-magnitude + within-arm-DV amend) -- separate `/queue-experiment` session, gated on the amend landing. The 468e MECH-090 commit-entry conjunction successor is separately owed (queued alongside 460f).

commitment_closure:GAP-4 stays in-progress; closes when 460g returns a contributory PASS (closure-coupled de-commit lowers within-arm post-closure occupancy AND ON < OFF on >= 2/3 seeds).
