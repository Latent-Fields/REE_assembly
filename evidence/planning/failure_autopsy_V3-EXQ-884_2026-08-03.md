# Failure Autopsy: V3-EXQ-884 (MECH-428 subgoal-bootstrapped goal seeding)

Generated: `2026-08-03T09:40:32Z`
Status: confirmed (user-confirmed routing 2026-08-03)
Scope: single

## 0. Pending-review flags and dry-run gate

- `v3_exq_884_mech428_subgoal_bootstrapped_goal_seeding_20260803T022131Z_v3` — `pending_review.md` "FAIL (action required)", claim MECH-428.
- **Dry-run gate:** `scripts/check_dry_run_citations.py` on this run_id and its sibling `v3_exq_883_mech427_cross_level_subgoal_credit_20260803T022051Z_v3` (cited below as context) — 0 dry cited, 2 clean. Manifest `dry_run` is absent/falsy on both. Neither is a smoke.
- **Recording provenance:** `ree-v3/validate_recording.py` reports OK — `recording_schema: rec/v1`, `substrate_hash`, `machine`/`machine_class`, `elapsed_seconds`, full `config`, explicit `seeds` all present. No always-core gap. (A narrower recording gap — the `n_steps` field — is itself part of this autopsy's finding; see Section 2b.)

## 1. Facts

**Run:** `v3_exq_884_mech428_subgoal_bootstrapped_goal_seeding_20260803T022131Z_v3`
**Queue ID:** V3-EXQ-884
**Claims:** MECH-428
**Outcome:** FAIL. Self-route: gates G0 (readiness, attainment fired) and G1 (readiness, forced-seed clears structured floor) both PASS; the load-bearing C1 (lift-fraction-of-ceiling >= 30%) passes on only 1/3 seeds. Self-declared `evidence_direction: weakens`.

**Design (as intended).** 3 seeds x 3 arms (`NO_SUBGOAL`, `SUBGOAL_BOOTSTRAP`, `FORCED_SEED`), each cell a single scripted-trajectory episode through `CausalGridWorld(subgoal_mode=True, num_waypoints=3)`, budgeted for `N_STEPS=400` so that (per the driver's own docstring) "MANY discrete credit events occur" and the EMA accumulation-vs-decay arithmetic of `GoalState.credit_subgoal_attainment` (SD-092) can be measured under a realistic intermittent event rate, benchmarked against a `FORCED_SEED` positive control that forces the parent every tick.

**Sibling context (not itself an autopsy target — a clean PASS):** V3-EXQ-883 (MECH-427, same day, same SD-092 primitive) tests the *maintenance* direction with a short (`N_STEPS=40`), single-waypoint, single-attainment-event design and PASSED cleanly. This matters directly to Section 4/5 below: 883's short, single-target design happens to structurally avoid the defect this autopsy found in 884's multi-waypoint design.

## 2. Reconstruction — what actually happened (facts, no interpretation yet)

**2a. The manifest's own `n_steps` field is misleading.** It records the CONFIGURED step budget (400), verbatim, regardless of how long the episode actually ran. Reading `parent_goal_norm_trace` length (the one field that reflects real per-tick history) shows every cell terminated far short of 400:

| Seed | Recorded trace length (real steps) | `n_waypoint_events` | `n_sequence_complete_events` | `n_subgoal_credits` (BOOTSTRAP arm) |
|---|---|---|---|---|
| 42 | 32 | 2 | **0** | 2 |
| 43 | 19 | 2 | **0** | 2 |
| 44 | 90 | 8 | 3 | 11 |

All three cells within a seed (NO_SUBGOAL / SUBGOAL_BOOTSTRAP / FORCED_SEED) share the identical trace length, confirming the *episode*, not any per-arm logic, ended early — and `FORCED_SEED`'s `n_subgoal_credits` exactly equals the trace length in every case (32/19/90), confirming `credit_subgoal_attainment` really is called (and increments) every tick with no dedup, as the driver intends — so the short episode, not a crediting defect, is what starved event counts.

**2b. Why the episode ends early: `done = agent_health <= 0.0 or self.steps >= 500`** (`ree_core/environment/causal_grid_world.py:2936`). The step cap (500) never binds (all cells end under 90). So every cell dies via `agent_health` reaching 0. `_build_env` passes `num_hazards=0, num_resources=0` and nothing else — but health loss is **not gated by `num_hazards`**: `CausalGridWorld`'s ambient self-contamination mechanic (`contamination_spread=0.5`, `contamination_threshold=2.0`, `contaminated_harm=0.4`, all constructor defaults, none overridden here) is always active. A cell's `contamination_grid` value increments every time the agent occupies it; once it crosses `contamination_threshold`, the cell's grid-rendered type becomes `"contaminated"`, and the *next* time the agent steps onto it, `agent_health -= contaminated_harm` (0.4) fires — 3 hits from `health=1.0` is fatal. **There is an established precedent for disabling exactly this** for a hazard-free probe: `experiments/v3_exq_513_sd049_multi_resource_heterogeneity_substrate_readiness.py` explicitly sets `contamination_spread=0.0  # isolate SD-049 from contamination dynamics`. Neither 884 nor its sibling 883 does this.

**2c. Why the agent sits still long enough to self-contaminate — the deeper bug.** Live reproduction (seed 42, identical scripted-walk logic) traces the mechanism exactly:

```
waypoints: [[8, 9], [3, 3], [8, 7]]
step 4  pos=(8,7)  <- passes THROUGH waypoint[2]'s cell early, target_type==WAYPOINT fires,
                       but wp_idx(2) != next_waypoint_idx(0) so no credit; grid[8,7] is
                       nonetheless overwritten to ENTITY_TYPES["agent"] this tick (step() line
                       ~2490: `self.grid[new_x, new_y] = self.ENTITY_TYPES["agent"]`,
                       unconditional on subgoal_mode)
step 5  pos=(8,8)  <- leaving (8,7): "old-cell clearing" logic sets grid[8,7] -> EMPTY
                       (never restored to WAYPOINT -- no re-stamping pass exists)
...
step 26 pos=(8,7)  <- agent legitimately arrives at waypoint[2] as the NOW-current target
                       (next_waypoint_idx==2). grid[8,7] reads EMPTY (destroyed at step 4-5),
                       so `elif target_type == ENTITY_TYPES["waypoint"]` NEVER fires.
                       transition_type stays "none". next_waypoint_idx never advances.
step 27-28         <- scripted walker sees ax==wx, ay==wy already -> emits STAY_ACTION
step 29-31         <- stationary; contamination_grid[8,7] (already primed by the step-4
                       visit + dwelling) crosses threshold; agent_caused_hazard fires 3x
                       (-0.4 each); health 1.0 -> 0.6 -> 0.2 -> 0.0; done=True at step 31
```

**This is a substrate bug in `causal_grid_world.py`, independent of MECH-428.** Waypoint-arrival detection (`ree_core/environment/causal_grid_world.py:2270-2313`) is keyed on the grid cell's *rendered entity type* still reading `ENTITY_TYPES["waypoint"]` at the moment of arrival — but the same grid array doubles as the agent's own position marker (`grid[new_x,new_y] = ENTITY_TYPES["agent"]`, line ~2490), and the "leaving a cell" logic reverts a vacated cell to `EMPTY`, never back to whatever it was before the agent arrived. **Any waypoint cell the trajectory merely transits before it becomes the current target has its marker permanently and silently destroyed**, with no error, no warning, and no re-stamping pass anywhere in the module. On a small grid with only 3 waypoints, an earlier waypoint's greedy path crossing a later waypoint's cell is a routine geometric coincidence, not a contrived edge case.

**Confirmed independently for all three seeds:**
- **Seed 42** — waypoints `[[8,9],[3,3],[8,7]]`. Path to waypoint[0]=(8,9) crosses (8,7)=waypoint[2] at step 4 (pre-target transit). Waypoint[2] never fires on legitimate arrival (step 26). `n_sequence_complete_events=0`. Dies step 31 (32 real steps — matches manifest).
- **Seed 43** — waypoints `[[9,1],[8,4],[6,2]]`. Path to waypoint[0]=(9,1) crosses (6,2)=waypoint[2] at step 1. Identical failure shape. `n_sequence_complete_events=0`. Dies step 18 (19 real steps — matches manifest).
- **Seed 44** — waypoints `[[9,1],[1,9],[8,10]]`. First 3-waypoint cycle completes cleanly (no crossing collision this time — a full `sequence_complete` fires at step 63 after respawn). But `_respawn_waypoints()` reused/relocated a waypoint onto a cell the agent had already occupied earlier (step 85, entering `(7,10)`, `transition="none"` — the identical defect recurring on a later respawned cycle). Dies step 89 (90 real steps — matches manifest).

**2d. Recording gap.** The manifest records neither the actual episode length (only the misleading configured `n_steps`) nor `done`'s cause (`agent_health<=0` vs step-cap) nor the discarded `harm_signal`. Nothing in the manifest itself would have surfaced this without live re-execution — the driver captures `_harm_signal` and discards it (`obs_flat, _harm_signal, done, info, _obs_dict = env.step(...)`), so even the experimenter reading the manifest had no visibility into what happened.

**2e. Preflight declaration is factually contradicted.** The script's own `ethics_preflight` block declares `involves_negative_valence: false` ("no hazards/resources in this config; harm stream unused"). Every seed's episode ends in agent death from self-inflicted harm — the declaration is incorrect for what the harness actually does, not merely for what the author intended.

## 3. Claim-layer mapping

**MECH-428** (`subgoal_bootstrapped_goal_seeding`, candidate, `implementation_phase: v3`, registered 2026-06-12, `depends_on`: INV-086, MECH-427, ARC-051, MECH-112, MECH-230). `what_would_answer`: "In a regime where DIRECT superordinate-goal seeding is sparse... enabling subgoal-attainment + cross-level credit (MECH-427) BOOTSTRAPS a structured z_goal attractor... NON-DEGENERACY: subgoals must be ATTAINED at a non-zero rate AND the forced-seed positive control must itself show a structured z_goal in the SAME harness [else... self-routes substrate_not_ready, NOT a FAIL]."

**Did the experiment test the claim under conditions where it could express itself? No.** The claim's own non-degeneracy clause anticipates exactly one failure mode ("subgoals never attained" / "forced control doesn't work") and the script's G0/G1 gates check exactly that — but neither gate checks whether the episode ran its *intended length*, so a harness defect that silently truncates the episode to 5-23% of its design budget sails through both gates undetected. G0 passed because *some* non-zero credits occurred (2, 2, 11) — the gate's own bar ("`n_subgoal_credits > 0` for EVERY seed") is trivially satisfied by 2 credits, which is nowhere near the "MANY discrete credit events" the design's own accumulation-vs-decay logic requires to be a fair test. G1 passed because `FORCED_SEED`'s continuous, event-rate-independent forcing reaches a structured parent even in a truncated 19-90-step window — it says nothing about whether the harness ran long enough for a *sparse*-event arm to do the same.

**MECH-427** (sibling, same day, same primitive) is directly informative here: its clean PASS under a short, single-event, non-colliding design demonstrates the SD-092 primitive itself works exactly as intended when the harness runs cleanly. The FAIL is not evidence the primitive or the cross-level credit mechanism is broken — G1 (forced-seed) *in this same run* independently proves that too (steady-state parent_goal_norm ~0.5-0.6, far above the 0.05 floor).

## 4. Biological-reference triage

**Closest mammalian reference:** Bandura & Schunk (1981) — proximal-subgoal decomposition sustains motivation/mastery in initially-uninterested learners; a formation-direction result. Existing REE literature entry: `evidence/literature/targeted_review_proxy_progress_goal_maintenance` — present, not absent. This is not a formal-definition import with no biology grounding; the claim already has a lit anchor (though the claim's own notes flag a Vygotsky zone-of-proximal-development anchor as a still-open strengthening opportunity, unrelated to this FAIL).

**Does the failure resemble a missing biological dependency?** No — the failure mode here is a software/environment bookkeeping bug (grid-cell type used as a proxy for "has this location been visited/claimed", clobbered by an unrelated rendering convention), not anything with a biological analog. This is squarely an implementation/environment-layer artifact, not a discovered prerequisite or evidence for/against the claim's biological plausibility.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | Precondition (episode running its intended length, arrival detection working) silently unmet; G0/G1 passed vacuously. Not evidence for or against MECH-428. |
| Biological reference | clear | Bandura & Schunk (1981); existing lit entry present. |
| Developmental / dependency prerequisites | present | MECH-427 (sibling, same day) confirms the SD-092 primitive functions; INV-086/ARC-051/MECH-112/MECH-230 dependencies not implicated by this FAIL. |
| Implementation completeness | complete | `GoalState.credit_subgoal_attainment` / `REEAgent.notify_subgoal_attainment` fully implemented, contract-tested (19/19, `test_sd092_cross_level_subgoal_credit.py`), and demonstrably functioning (G1, and sibling 883/427 PASS). Not the source of the FAIL. |
| Environment adequacy | **defective** | `causal_grid_world.py`'s subgoal_mode waypoint-arrival detection is coupled to a mutable grid-cell type the agent's own position marker destructively overwrites on premature transit — a general substrate bug, not MECH-428-specific. Compounded by an always-on ambient self-contamination mechanic this experiment (unlike the V3-EXQ-513 precedent) did not disable. |
| Measurement adequacy | **under-instrumented** | `n_steps` field records the configured budget, not the real episode length; `done`'s cause and `harm_signal` are discarded; nothing in the manifest signals the defect without live re-execution. |
| Integration adequacy | isolated but coupled to an unrelated substrate bug | SD-092's goal.py primitive is sound in isolation (proven by G1 and by 883); the FAIL arises entirely from `causal_grid_world.py`'s waypoint/entity-grid/contamination coupling, an interaction this experiment's author did not anticipate (its `ethics_preflight` block incorrectly declares `involves_negative_valence: false`). |
| Scale / capacity | not implicated | — |

## 6. Learning extracted

- **New dependency discovered (substrate bug, not MECH-428-specific):** `causal_grid_world.py`'s subgoal_mode waypoint-arrival detection must not depend on the mutable grid-cell entity type, which the agent's own position marker permanently overwrites on any premature transit through a not-yet-current waypoint's cell. A position-based check (agent position vs. `self.waypoints[self._next_waypoint_idx]` directly — the substrate's own `completion_tolerance_enabled` feature already does exactly this, gated off by default) would sidestep the defect entirely.
- **Existing mitigation precedent not applied:** `contamination_spread=0.0` is an established, precedented fix (V3-EXQ-513/SD-049) for isolating a hazard-free probe from the ambient self-contamination mechanic. Neither 884 nor its sibling 883 applied it (883 escaped the consequence only because its short, single-event design never dwells long enough to matter).
- **Recording gap:** the manifest's `n_steps` field should record the actual realized episode length distinct from the configured budget, and `done`'s cause (health-death vs step-cap) should be recorded as a standard field for any `CausalGridWorld`-based experiment — this would have made the defect visible from the manifest alone, without live re-execution.
- **Scope risk flagged, not investigated here (user-confirmed to route as a separate chip):** ~24 other experiment scripts (the SD-034/MECH-268/ARC-071 commitment/closure family — `v3_exq_460*`, `v3_exq_468*`, `v3_exq_715/717/721`, etc.) use `subgoal_mode=True` with `num_waypoints=2` or `4`. Whether any of their confirmed results are compromised by the same waypoint-grid-clobbering defect has **not** been checked by this autopsy — their designs/DVs may not depend on full-sequence completion, or their waypoint geometry may not happen to collide. This is a distinct, unverified risk, not a finding.

## 7. Routing (user-confirmed 2026-08-03)

**Evidence direction: overridden from self-declared `weakens` to `non_contributory`** (precondition_unmet). The FAIL is not evidence against MECH-428's bottom-up bootstrapping mechanism — canonical parallel to this skill's own reference incident (V3-EXQ-642: a self-route that looked like a substrate reading was actually an unmet precondition).

**Routing: `implement-substrate`.** File a substrate_queue entry to fix `causal_grid_world.py`'s waypoint-arrival detection (position-based check against `self.waypoints[self._next_waypoint_idx]`, not the mutable grid-cell entity type) and to disable/gate the ambient contamination mechanic by default for hazard-free (`num_hazards=0`) configurations, or at minimum document the `contamination_spread=0.0` precedent prominently. `pending_retest_after_substrate: true` — re-queue V3-EXQ-884 (new letter, e.g. `884a`) once the fix lands, with the additional fix of recording real episode length + `done` cause in the manifest.

**Draft `evidence_quality_note` for governance:**
> V3-EXQ-884 FAIL is non-contributory to MECH-428: the episode terminated 77-95% short of its designed budget in all 3 seeds due to a `causal_grid_world.py` substrate bug (waypoint-arrival detection clobbered by the agent's own grid-position marker on premature transit) compounded by an undisabled ambient self-contamination mechanic, starving the accumulation-vs-decay dynamics the claim's own non-degeneracy clause requires. G0/G1 passed vacuously; the sibling MECH-427 run (883) confirms the underlying SD-092 primitive functions correctly. Re-test pending substrate fix (see SD-XXX).

**Follow-on (chipped, not spawned by this session per CLAUDE.md Session Land Protocol Step 6 — this substrate fix IS this autopsy's own routing recommendation, so `/governance` chips it once ratified):** the `recommended_substrate_queue_entry` below.

**Follow-on (chipped by this session, user-confirmed — a distinct, collateral risk this autopsy did not itself diagnose):** audit the SD-034/MECH-268/ARC-071 commitment/closure family (`subgoal_mode=True`, `num_waypoints>=2`) for the same latent defect.

**Re-derive brake:** MECH-428 has 0 prior confirmed autopsies (`granularity_debt_cluster.py MECH-428`: 0 targets/0 files; re-derive brake count: 0 `substrate_ceiling` hits). Does not fire — this is the claim's first FAIL, and this reading is not `substrate_ceiling` in any case.

**Granularity-debt trigger:** does not fire (0 prior tagging targets).
