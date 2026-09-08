# V3-EXQ-884a (MECH-428 subgoal-bootstrapped goal seeding) -- DESIGN REFUSED at `/queue-experiment` Step 4.5 (red-team BLOCKING, independently confirmed)

**Status: NOT QUEUED. No queue entry, no coordinator row, no manifest.** The SD-094-fixed driver is landed under `ree-v3/experiments/_scratch/` so the (genuinely useful) environment fix is recoverable for whoever redesigns the criterion; nothing here has been written to `claims.yaml`, `substrate_queue.json`, or `experiment_queue.json`. A governance flag (`evidence_discrepancy`, MECH-428) carries the follow-on.

- **Written:** 2026-09-08T16:19:13Z
- **Session:** `w5-s2a-queue-fill-20260908` (Mac `DLAPTOP`, main checkout), campaign W5-S2a item 1 (`chip-20260908-w5-s2a-queue-fill`, member chip `chip-20260905-exq884a-mech428-two-kwarg-retest`).
- **Red-team model:** `fable` (Fable 5.1), one pass, foreground, 2026-09-08. Verdict **BLOCKING**. Findings preserved in section 5.
- **Verification:** the arithmetic and every source citation re-checked by this session against `ree_core` (sections 2-3); the numbers reproduced by an independent 400-step probe written by this session (section 3), matching the red-team's to 4 dp.

---

## 1. The refusal, in one sentence

**V3-EXQ-884a's load-bearing criterion C1 cannot fail.** `lift_fraction` is, at steady state, the closed form `alpha / (1 - (1 - alpha) * decay^T)` in the mean inter-event interval `T` alone -- `alpha = 0.05` and `decay = 0.995` are fixed `GoalConfig` defaults, so C1's floor of 0.30 is cleared for every `T <= 26.1` steps, while the scripted greedy walk's longest possible waypoint leg on a 12x12 grid is 22 steps (Manhattan bound). The realized `T` is ~6.5, giving `lift_fraction` 0.60-0.63 -- a 2x margin over a bar that is geometrically unreachable from above. The run would therefore record `PASS / supports` for MECH-428 no matter what the substrate, the encoder, or the environment did, and the `weakens` branch its own docstring describes ("bottom-up bootstrapping is too weak to net out against decay") is unreachable by construction.

**This is a defect in the design V3-EXQ-884 pre-registered, not in the SD-094 fix.** The fix works and is confirmed (section 4). Re-queuing 884 verbatim-plus-fix -- which is exactly what the confirmed autopsy `failure_autopsy_V3-EXQ-884_2026-08-03` instructed, and what this session was chipped to do -- would have converted an honest `precondition_unmet` into a citable `supports` that certifies arithmetic rather than a mechanism. That is the specific laundering `/queue-experiment` Step 4.5 exists to catch, so the entry was refused rather than queued.

## 2. Source verification (all in `ree-v3` at the shared checkout, 2026-09-08)

| claim | where | verified |
|---|---|---|
| The parent EMA pull is `parent := (1-a)*parent + a*z` with `a = min(1, parent_goal_alpha * credit)` | `ree_core/goal.py` `credit_subgoal_attainment`, `a = min(1.0, float(self.config.parent_goal_alpha) * float(credit))`; `self._z_goal_parent = (1.0 - a) * self._z_goal_parent + a * z` | yes |
| `parent_goal_alpha` default 0.05, `parent_goal_decay` default 0.005 | `ree_core/goal.py:346` `parent_goal_decay: float = 0.005`; `GoalConfig` `parent_goal_alpha` 0.05 (driver re-declares both in `full_config`) | yes; the driver overrides neither |
| The parent decays by `(1 - parent_goal_decay)` on EVERY `GoalState.update()` tick, in every arm | `ree_core/goal.py:929-935`, gated only on `use_hierarchical_goal_credit` and parent-allocated | yes; the driver calls `update_z_goal` every step in all three arms by design |
| FORCED_SEED's `a` saturates: `min(1, 0.05*20.0) = 1.0` -> full replacement every step, so its steady state is just the current `z_world` norm | same `credit_subgoal_attainment` line, `FORCED_CREDIT = 20.0` | yes |
| NO_SUBGOAL's parent is never allocated, so its DV is exactly 0.0 | `_z_goal_parent` allocated only inside `credit_subgoal_attainment`; `parent_goal_norm()` returns 0.0 when `None` | yes; measured 0.000000 on all three seeds |
| The scripted walk is a greedy Manhattan walk (x first, then y), one cell per step | driver `_scripted_action` | yes |
| Waypoints are placed inside the `size=12` grid | `CausalGridWorld` waypoint placement / `_respawn_waypoints` | yes -> longest possible leg = 11 + 11 = 22 steps |

## 3. Numerical confirmation (independent probe, this session, 400 steps = the pre-registered budget)

Run through the driver's own `_build_env` / `_build_agent` / `_scripted_action` under `arm_fingerprint.reset_all_rng(seed)`; writes nothing.

| seed | NO_SUBGOAL | SUBGOAL_BOOTSTRAP | FORCED_SEED | `lift_fraction` | credits | `T` | closed form | z_world coherence |
|---|---|---|---|---|---|---|---|---|
| 42 | 0.000000 | 0.3651 | 0.5927 | **0.6161** | 60 | 6.67 | 0.6156 | 0.9985 |
| 43 | 0.000000 | 0.2882 | 0.4790 | **0.6016** | 58 | 6.90 | 0.6077 | 0.9982 |
| 44 | 0.000000 | 0.2985 | 0.4748 | **0.6286** | 65 | 6.15 | 0.6341 | 0.9981 |

Bar: `C1_FRACTION_FLOOR = 0.30`. Passes 3/3 at ~2x. The closed form `0.05 / (1 - 0.95 * 0.995^T)` predicts the measured value to within 1.5% on every seed.

Sensitivity of the criterion to the only free quantity, `T`:

| `T` (steps between credit events) | closed-form `lift_fraction` |
|---|---|
| 6.5 (realized) | 0.6215 |
| 15 | 0.4208 |
| 22 (geometric max leg, 12x12 grid) | 0.3351 |
| **26.14 (the value at which C1 would first fail)** | **0.3000** |
| 40 | 0.2246 |

`T > 26.1` is unreachable: the greedy walk reaches the pending waypoint in exactly its Manhattan distance, at most 22 on this grid. **C1 has no failing region.**

The high `z_world` coherence (0.998, an untrained encoder on a low-variety hazard-free grid) is what makes the vector EMA behave as the scalar identity above -- and is a second, independent vacuity: the "structured parent attractor" the DV certifies is 0.61 x one nearly-constant direction, which a constant vector fed to `credit_subgoal_attainment` every ~7 ticks would reproduce with no environment at all.

## 4. What DOES stand: the SD-094 fix is confirmed and worth keeping

The chip's premise -- that a verbatim re-queue reproduces the 884 failure because both SD-094 flags default OFF -- was correct and is now measured on this substrate (seeds 42/43/44, this session):

| SD-094 flags | steps run (of 400) | `done_cause` | final health | `sequence_complete` events |
|---|---|---|---|---|
| OFF (the 884 configuration) | 32 / 19 / 90 | `health_depleted` | 0.000 | 0 / 0 / 3 |
| ON | 400 / 400 / 400 | (none) | 1.000 | 20 / 19 / 21 |

The OFF row reproduces the autopsy's recorded 32/19/90 exactly. `subgoal_arrival_position_check=True` + `hazard_free_contamination_gate=True` close the defect completely. The driver carrying that fix -- plus the autopsy's requested episode-length / `done_cause` recording, a G2 readiness gate over it, and a `dv_headroom` block -- is landed at `ree-v3/experiments/_scratch/v3_exq_884a_mech428_subgoal_bootstrapped_goal_seeding.py` so a redesign starts from it rather than re-deriving it. It passes `validate_experiments.py --strict` and its dry-run smoke.

## 5. Red-team findings (model: fable, one foreground pass)

Verbatim reviewer output at `/private/tmp/.../scratchpad/redteam_884a.md` (session-local). Summary, with this session's dispositions:

- **Finding 1 (BLOCKING) -- C1 cannot fail; it is an arithmetic identity fixed before the run.** Derivation, measurements and the `T <= 22` geometric bound as in sections 2-3. **Disposition: ACCEPTED, independently reproduced. This is the refusal.**
- **Finding 2 (CONTESTED) -- the driver's `dv_headroom` block is mis-stated.** It records `achievable = 1.0` "by construction", which is FORCED_SEED's own lift, not what a bootstrap arm can reach (~0.61-0.63 at this cadence, 0.335 at the worst-case `T = 22`); and the docstring's "close to the boundary" evidence (0.243/0.297/0.259) is a pre-asymptotic 80-step transient -- at ~10 events against a ~12-event time constant, with the 60-step median window reaching back to step 20. **Disposition: ACCEPTED. Confirmed by section 3 (the 400-step values are 0.60-0.63, not 0.24-0.30). The dry-run reading was mine and it was wrong; it is the reason the defect nearly shipped.** Correcting `dv_headroom` alone would not save the design -- finding 1 stands regardless -- so the block is left as-is in the scratch driver with this record as its correction.
- **Finding 3 (note) -- G1 and C2 are foregone at 10x / 30x slack** (FORCED 0.47-0.59 vs a 0.05 floor; BOOTSTRAP 0.29-0.37 vs a 0.01 floor), and both are calibrated against the same untrained-encoder norm scale the DV is measured in. With C1 unfailable too, the only reachable FAILs in the whole grid are the harness gates G2/G0. **Disposition: ACCEPTED as corroboration of finding 1.**
- **Finding 4 (note) -- the DV is a norm, and does not reach MECH-428's `what_would_answer`,** which asks for a structured attractor AND goal-directed behaviour the no-subgoal control does not produce. The behavioural half is explicitly declared out of scope in the driver docstring (a deliberate, documented choice, for the F-dominance/commitment-substrate reason), but a `supports` would enter `claim_evidence` for the whole claim. **Disposition: NOTED, not part of the refusal; it is a scope question for governance, and is recorded here so the redesign can decide it deliberately.**
- **Checked clean by the reviewer and not disputed:** decay ticks every step in every arm (measured inter-event ratio 0.9950); `notify_subgoal_attainment` filters to `{"waypoint", "sequence_complete"}` and nothing in `act()` resets the parent mid-episode; the encoder is seeded per cell identically across the arms of a seed, so numerator and denominator share an encoder; no sampling bias between FORCED (all steps) and BOOTSTRAP (event steps) in mean `||z||` (0.588 vs 0.589); the SD-094 flags genuinely take effect.

## 6. What is owed, and to whom

The gap is `complex (probe-gated)` -- not `complicated (buildable)`. What is missing is not a build but a **criterion that can distinguish the MECH-428 mechanism from the EMA arithmetic that any credit schedule at this alpha/decay would produce**. Candidate reframings, none of them this session's to choose:

1. **Score the parent's CONTENT, not its norm.** At coherence 0.998 the norm is uninformative. A DV such as the parent's alignment with the *attained subgoal* representations specifically (versus a shuffled / non-attained control, or versus the episode-mean `z_world`) would fail if the parent were merely a running average of whatever the encoder emitted.
2. **Train the encoder (P0), so `z_world` carries content the parent can be structured BY.** The current run's parent is a constant-direction vector; there is nothing for a "structured attractor" claim to bite on.
3. **Make `T` an independent variable rather than a fixed property of the grid geometry.** The closed form is the prediction; testing it against a manipulated event cadence would turn the identity from a confound into the measurement (and would be a genuine test of the accumulation-vs-decay framing).
4. **Withdraw C1's 0.30 floor as pre-registered and re-derive a bar from the closed form** -- i.e. score the *residual* above what alpha/decay/`T` alone predict.

Governance owns that choice (`/governance` Step 2b, then `/queue-experiment` on the ratified design). This session raised an `evidence_discrepancy` governance flag on MECH-428 rather than acting on any of the four.

**Also owed, and unrelated to the refusal:** MECH-428's `implementation_note` still reads `STILL NEEDED: EXP-0390's 3-arm design ... needs an experiments/ driver`. That driver has existed since 2026-08-03 (`experiments/v3_exq_884_mech428_subgoal_bootstrapped_goal_seeding.py`, run as V3-EXQ-884). Governance appended a correction to `evidence_quality_note` on 2026-09-05 but left `implementation_note` untouched. The same governance flag names this.

## 7. Provenance

- Autopsy that requested the re-queue: `failure_autopsy_V3-EXQ-884_2026-08-03` (confirmed) -- its `recommended_substrate_queue_entry` minted SD-094, now `implemented_validated`.
- Re-derive brake count for MECH-428 at refusal time: **1** (below the threshold of 2), so the brake was not the reason for the refusal.
- Substrate-path overlap gate (`/queue-experiment` Step 2.5c): two open `corrupting` entries name `ree_core/agent.py` (`mode-governance-engagement`, `SD-082`), both `implemented_pending_validation`. Neither is live in this configuration -- `use_salience_coordinator` is `False` and `use_lateral_pfc_analog` / `lateral_pfc_rule_readout_consumer` are both `False` at the driver's `REEConfig.from_dims(...)`, verified by probe -- and the driver never reaches the E3 selection path at all (the walk is scripted from env state). Recorded so the disposition is auditable rather than silent.
- Existing-evidence check (GOV-REUSE-1): the decisive readout is `lift_fraction` on an SD-094-fixed substrate. V3-EXQ-884 is the only prior run and it ran on the unfixed substrate (different `substrate_hash`, and starved). Not recoverable from the record -- which is why the run was designed rather than reanalysed. The refusal is on the criterion, not on redundancy.
