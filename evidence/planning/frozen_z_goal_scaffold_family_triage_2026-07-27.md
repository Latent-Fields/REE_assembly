# Frozen (not dead) z_goal in the scaffold-warmed family -- triage

**Date:** 2026-07-27T20:25:50Z
**Session:** `charming-dijkstra-9ef48e`
**Surfaced by:** the 2026-07-27 dead-z_goal-stream audit (ree-v3 `fd7bd5d68c`), which
deliberately did NOT fold this in -- `dead_z_goal_stream_lint` discharges this family via
`_uses_a_z_goal_driving_helper` because "pinned at zero-init for the whole run" is simply
false for them.
**Verdict:** **No retro-fix. No manifest edit. No claim change.** One `supports` manifest
exists in the family and it survives. Findings close with documentation + a contract pin.

---

## 1. The condition, restated precisely

28 scripts under `ree-v3/experiments/` drive warmup through
`ScaffoldedSD054OnboardingScheduler` (`experiments/scaffolded_sd054_onboarding.py`), which
calls `agent.update_z_goal(...)` on Stage-0 / P1 / P2 steps, then hand the warmed agent to a
**hand-rolled measurement loop that never calls it again**. Two substrate facts, both
re-verified this session:

| Fact | Verification |
|---|---|
| `REEAgent.reset()` resets 47 subsystems but **not** `goal_state` | `agent.py` lines 2816-3180; AST scan shows zero occurrences of `goal_state` in the 364-line body. Its only documented exception is residue. |
| `GoalState`'s decay lives **inside** `GoalState.update()` | `goal.py:754` -- `self._z_goal = self._z_goal * (1.0 - decay_goal)` is the first statement of `update()`, reachable only through `update_z_goal`. |

So z_goal **freezes** at its post-warmup value across the whole measurement phase.
`is_active()` (`abs().sum() > 1e-6`) stays True and every consumer keeps firing against a
goal that no longer tracks the episode.

**Family re-derived, not transcribed.** The supplied list of ~27 reproduces **exactly**, at
28 members, under the discriminator *scaffold importer + z_goal knob truthy + no own
`update_z_goal` + hand-rolls its own `select_action` **and** env `step`*:

> 460c 460d 460e 460f 460g 460h 460i 460j 460k 460l 460m 460n 461c 464c 464d 466c 466d 466e
> 467c 467d 468c 468d 468e 468f 629b 629c 797 799

50 scaffold importers enable a z_goal knob without writing z_goal themselves; the other 22
(603f-603q, 634/634b/634c, 638/638a, 640/640a/640b, 652, 733a, 812) **delegate every step to
the scheduler**, so the scheduler keeps calling `update_z_goal` and they never freeze. The
`select_action`+`step` test is what separates the two groups, and it is now pinned.

---

## 2. Is the freeze the INTENDED design? -- **Half of it is. The half that reached the
measurement phase is not.**

This is the load-bearing finding, and it is sharper than "intended vs not".

The scheduler has a **purpose-built primitive** for holding the goal still:

```python
def _set_goal_pipeline_frozen(agent, frozen: bool) -> None:
    if frozen:
        agent.config.use_mech295_liking_bridge = False
        agent.config.use_mech307_conjunction  = False
    else:
        ...
```

Its own definition of "goal pipeline FROZEN" is a **pair**: skip `update_z_goal`
(`seed_goal=False`) **and** short-circuit the MECH-295 liking bridge + MECH-307 conjunction,
so the held goal cannot drive behaviour. The scaffold uses it deliberately and documents it
richly -- Stage-0b consolidation ("a short PROTECTED window ... where `update_z_goal` is NOT
called, so the just-formed z_goal cannot decay", with a pre-registered `retention_gate` of
0.75), P0, and Stage-H ("Goal pipeline FROZEN (the isolation: no goal-unfreeze competing)").
Freezing a goal is unambiguously an intended primitive in this family.

**But the call sites tell the rest of the story:**

| Stage | freeze state set |
|---|---|
| `run_stage0_nursery` | `frozen=False` |
| `run_stage0b_consolidation` | `frozen=True` |
| `run_p0` | `frozen=True` |
| `run_hazard_avoidance` | `frozen=True` |
| `run_p1` | **`frozen=False`** |
| `run_p2` | *(does not touch it)* |

`run_p1` unfreezes and nothing sets it back. So the agent reaches the measurement phase with
**z_goal held still but the consumers LIVE** -- a combination the scaffold itself never
constructs anywhere. The measurement phase inherits **exactly half** of the primitive, by
omission. None of the 28 calls `_set_goal_pipeline_frozen` (0 call sites across all 28), and
**none of them documents its measurement-phase goal state at all** -- zero mentions of the
freeze in any of the 28 docstrings.

**Conclusion on Q1:** the plausible reading ("the scaffold is developmental, the measurement
phase deliberately probes the resulting agent with a fixed goal") is *defensible as a
design*, and two facts support it -- `run_p2` is itself documented as "frozen-policy
measurement", and all 28 set `scaffold_contact_gated_goal_updates=True`, so `update_z_goal`
is already skipped on non-contact steps inside P1/P2 and the measurement phase is a
*continuation* of an already-mostly-frozen regime rather than a discontinuity. But it is not
what was *written down*, and it is not the state the family's own freeze primitive produces.
The honest classification is **inherited by omission, benign in outcome, undocumented**.

### 2b. The frozen goal is NOT inert -- the trap that makes this worth pinning

None of the 28 sets `goal_weight`, and `E3Config.goal_weight`'s dataclass default is `0.0`
(`utils/config.py:603`), which reads as "the goal term is off, so a stale z_goal is
harmless". **That reading is wrong.** `REEConfig.from_dims` carries its own default of
`1.0` and assigns `config.e3.goal_weight` (`config.py:5258`, `:6329`). Verified at runtime
on the 460c config: `e3.goal_weight = 1.0`, `goal.e1_goal_conditioned = True`. So on every
E3 tick of the measurement phase, `score_trajectory` executes
`score = score - goal_weight * goal_proximity(...)` (gated on `goal_weight > 0` **and**
`goal_state.is_active()`, both true), and E1 stays goal-conditioned. The stale goal actively
biases action selection throughout. Note the direction: freezing makes the goal term
**maximally and permanently strong**, the opposite of the dead-stream defect.

---

## 3. Which scripts read downstream of z_goal? -- **all 28**, but arm-symmetrically

Because `goal_weight=1.0` and `e1_goal_conditioned=True` resolve live for every member, the
E3 goal term and E1 goal-conditioning are live in all 28. The prompt's expectation that
"most may read none of them" does not hold. Additionally: the MECH-295 liking->approach
bridge is explicitly enabled (`use_mech295_liking_bridge=True`) across the 460/46x/629
cohort, and `use_external_task_drive=True` in 464d / 467d / 797. MECH-189 super-ordinal
anchors, MECH-293 ghost probes and MECH-288's slow BOCPD scale are **off** in all 28.

**The structural mitigation, uniform across the family.** Every one of the 28 constructs
**exactly one** `ScaffoldedSD054OnboardingScheduler` per seed and evaluates every arm from a
**copy of that single build** (`ARM_CLOSURE_OFF` clones the same trained weights; 799
onboards once in `_onboard_seed` and runs all four DiD cells "from a copy of the onboarded
agent"; 797 is single-arm). The frozen z_goal is therefore **bit-identical across arms** and
cannot produce a between-arm difference. This is the same argument the dead-stream lint's own
carrier table makes for V3-EXQ-615.

---

## 4. Landed manifests -- does any recorded conclusion rest on it?

All 28 landed exactly one flat manifest each (no `runs/<run_id>/` packs).

| evidence_direction | n | members |
|---|---|---|
| `non_contributory` | 22 | 460c/e/h/i/j/k/l, 461c, 464c, 464d, 466c, 467c, 467d, 468c/d/e/f, 629b, 629c, 797 |
| `superseded` | 3 | 460f, 460g, 466d |
| `mixed` (diagnostic) | 1 | 460d |
| *(none; diagnostic)* | 3 | 460m, 460n, 799 |
| **`supports`** | **1** | **466e** |

**15** of the 28 self-routed `substrate_not_ready_requeue` -- a readiness gate failed and the
run refused to score, so there is no conclusion to rest on anything (460e/g/h/i/j/k/l/m/n,
464d, 467d, 468d, 468f, 629b, 629c). **10** more route `residual_*_open`, i.e. "the question
stays open" (460c, 460d, 460f, 461c, 464c, 466c, 466d, 467c, 468c, 468e). That leaves
**exactly three** carrying a substantive conclusion -- and all three survive:

### 466e -- the only governance-weighting manifest. **Conclusion stands.**
`PASS` / `supports` / SD-034, label `sd034_satisficing_discharge_confirmed`. Its criteria are
**existence thresholds on the ON arm** (C1 `n_closures >= 1`, C2 `discharge_events >= 1`) plus
C3, a **structural negative control** on an OFF clone that has no closure operator at all and
therefore cannot discharge by construction. None of the three reads z_goal. Both arms share
the one curriculum build (`arm_note`: "Both arms share the trained curriculum build (one build
per seed)"), so the frozen goal is bit-identical between them. The frozen goal biases the
*absolute* level of foraging/completion identically in both arms, and it points at a
scaffold-env latent attractor that is not aligned with the eval env's waypoints -- a nuisance
bias, not something that could manufacture the positive. **No action.**

### 797 -- the one script whose DV *is* goal-derived. **Route stands; report the caveat.**
`PASS` / `diagnostic` / `non_contributory`, label `commitment_layer_starved`, route
`route_upstream_bg_commitment`. It measures the external-task engagement injection
`engagement = goal_active ? clip(commit_w*[beta_elevated] + prox_w*goal_proximity(z_world), 0, 1) : 0`,
and reports `goal_proximity` per coordinator tick -- computed against the **frozen** z_goal.
Two honest caveats worth recording, neither of which flips the route:
- The route survives *a fortiori*. With a live decaying goal, `is_active()` would eventually
  go False and -- since `external_task_drive_require_goal_active=True` -- engagement would be
  identically 0. The D1 conclusion ("the latch is the only term that can carry engagement over
  the flip point") would be *reinforced*, not overturned.
- But its precondition `forager_z_goal_norm_at_contact_supra_floor` ("the agent holds a goal
  representation, so `goal_proximity` is meaningful", measured 0.4138 vs a 0.4 gate) is
  measured **during P2**, where z_goal is live; the proximity magnitudes it then reports are
  read in the eval phase against a **stale** target. The precondition is satisfied partly *by
  the freeze itself*. (797 separately already records that its
  `genuine_e3_tick_sample_floor` was **not** met -- 66 vs 100 -- so its numbers were already
  flagged as under-powered.)

### 799 -- **structurally immune.** `diagnostic`, no direction, label
`mu_overlay_entropy_only_no_behavioural_authority`. It is a genuine difference-in-differences
whose estimand is the (regime x coupling) **interaction**, with all four cells run from copies
of one onboarded agent. A constant background bias differences out of an interaction exactly.

**Nothing to re-open.** No manifest was edited; no claim status, confidence, `live_status` or
`v3_pending` was touched.

---

## 5. Recommendation

1. **Do not retrofit the 28.** They ran, they are arm-symmetric, and 25 of the 28 carry no
   substantive conclusion at all (15 refused to score, 10 leave the question open). Adding
   `update_z_goal` to a landed script is **not a free
   wiring fix** in general: the call is also the SD-024 benefit-attractor producer -- it
   invokes `ResidueField.accumulate_benefit` *ahead of* the `goal_state` guard (verified:
   `agent.py`, the `accumulate_benefit` block sits above `if self.goal_state is None ...:
   return`), so it populates `benefit_rbf_field` and un-zeroes the SD-025 curiosity bonus in
   `HippocampalModule._curiosity_bonus` (previously exactly 0.0, because
   `RBFLayer.compute_local_density` early-returns on an empty active mask).

   **Precision worth having for THIS family:** that block is gated on
   `residue.benefit_terrain_live_producer`, whose default is `False`
   (`utils/config.py:2147`), and **neither the scheduler nor any of the 28 sets it**
   (verified by grep across all 28 plus `scaffolded_sd054_onboarding.py`). So a retrofit
   here would *not* fire the SD-024 path. The behaviour change it *would* introduce is the
   goal dynamics themselves -- 0.5%/step decay plus contact reseeding, replacing a constant
   -- which changes the E3 goal term on every tick and still makes a patched script
   non-comparable to the runs before it. State the SD-024 caveat when recommending the
   retrofit anywhere else in the corpus, where the producer flag may well be on.
2. **New members must choose and state their measurement-phase goal state.** Three coherent
   options: (a) drive the goal (`update_z_goal` per step, accepting the SD-024 consequence);
   (b) re-freeze the pipeline properly by calling `_set_goal_pipeline_frozen(agent,
   frozen=True)` before the measurement loop, restoring the pair the scaffold intends; or
   (c) declare in the docstring that a fixed post-development goal is the intended probe
   condition. Silence is what produced this finding.
3. **Cross-reference (in flight at time of writing, not yet landed):** a concurrent session
   is adding a runtime `z_goal_active_frac` counter to `REEAgent` plus an
   `experiments/_lib/z_goal_stream.py` manifest block. That counter is a direct **detector
   for this condition**: a frozen member reports `z_goal_active_frac ~= 1.0` for its whole
   measurement phase (always active, never re-seeded), which is distinguishable from both a
   dead stream (0.0) and a live one (intermediate, tracking contact). If it lands, reading
   it against the run's design is the cheapest way to spot a new half-freeze.
4. **Pinned** in `ree-v3/tests/contracts/test_frozen_z_goal_scaffold_family.py`: the runtime
   behavioural fact (reset leaves a seeded z_goal bit-identical; no decay without
   `update_z_goal`), the fact that the frozen goal is **not** inert (`e3.goal_weight > 0`),
   the freeze primitive's consumer-silencing pair, the `run_p1`-unfreezes /
   `run_p2`-untouched hand-off, and the family size of 28.

---

## 6. Adjacent finding, NOT triaged here (needs its own pass)

`_set_goal_pipeline_frozen` silences MECH-295 and MECH-307 but **not** the E3 goal term or
E1 goal-conditioning, which are gated independently on `E3Config.goal_weight > 0` and
`goal_state.is_active()`. Entering `run_p0` / `run_hazard_avoidance`, z_goal has already been
seeded by Stage-0 (gate: `z_goal_norm_peak > 0.4`) and protected by Stage-0b, so
`score_trajectory` **is** subtracting `goal_weight * goal_proximity` during the stages the
scheduler calls "goal pipeline FROZEN". `run_hazard_avoidance`'s docstring -- "the agent's E3
harm evaluation drives survival without the goal pipeline" -- is therefore not strictly
accurate. This affects the isolation claim of the scaffold's own curriculum stages and so
touches all **78** scaffold importers, not just these 28. Scope-separated deliberately;
chipped for its own triage.
