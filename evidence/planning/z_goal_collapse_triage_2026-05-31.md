# z_goal collapse triage (GAP-C prereq 2)

**Date:** 2026-05-31T17:15Z
**Session:** `triage-z-goal-collapse-20260531T170500Z`
**Trigger:** behavioral_diversity_isolation:GAP-C resume_condition + goal_pipeline:GAP-4 closure-distance bookkeeping list prereq (2) (`goal-pipeline training regime produces non-trivial z_goal in default config`) as `OPEN, load-bearing blocker ... owned today by IGW-20260528-016 / goal_pipeline:GAP-4 / V3-EXQ-490g cohort`. This triage tests that attribution and classifies the failure mode.
**Scope:** triage only -- no substrate code, no new experiment scripts queued, no claims.yaml edits. Updates to GAP-C / GAP-4 plan-doc resume_condition + ownership pointers only.

---

## TL;DR

**Classification: (b) substrate-structural.**

The substrate at REE-v3 default config cannot produce non-trivial z_goal under random-policy training in the target env. The 490 cohort is the wrong owner for this prereq -- it tests a different problem (MECH-295 bridge necessity under the gap4 substrate where z_goal is already active). The correct owner has existed since 2026-05-29: the substrate-design memo at [evidence/planning/sd_054_scaffolded_onboarding_substrate_design.md](sd_054_scaffolded_onboarding_substrate_design.md) and the substrate_queue.json entry `scaffolded_sd054_onboarding` (status=`pending_implementation`), surfaced as IGW-20260531-029.

**Action:** the substrate fix is already designed and queued; no further substrate-design work is owed by this triage. The fix's `/implement-substrate` session is the next forward-progress action. This triage's deliverable is the documentation update that re-attaches prereq (2) ownership to the correct owner so the bookkeeping stops misdirecting future sessions to the 490 cohort.

---

## 1. What I read

| Source | Relevant content |
|---|---|
| [failure_autopsy_V3-EXQ-591_2026-05-27.md](failure_autopsy_V3-EXQ-591_2026-05-27.md) | Canonical autopsy for the substrate-uniform z_goal-zero family (591 / 540-series / 590a / 603-series). Defines the three substrate prerequisites in section 7. Prereq (2) text verbatim: "Goal-pipeline training regime produces non-trivial z_goal in default config -- V3-EXQ-603c routed 2026-05-27 (P0 / P1 phased training per the 603b autopsy)". The owner-of-record at the time of writing was V3-EXQ-603c, NOT the 490g cohort. |
| [failure_autopsy_V3-EXQ-490g-cohort_2026-05-29.md](failure_autopsy_V3-EXQ-490g-cohort_2026-05-29.md) | Explicitly splits the five-experiment cohort (471a / 475a / 483c / 490g / 524a + 603c) into TWO STRUCTURALLY DISTINCT CLUSTERS. Cluster A (483c / 524a + cohort siblings) = GAP-4 Tier-1 library measurement-gap; goal_norm 0.09-0.36 firing across all runs; NOT z_goal-zero. Cluster B (603c) = absorbed into the 591 family; routed to `/implement-substrate` for scaffolded SD-054 onboarding. The autopsy's section 6 quote: "Forcing 483c/524a into the 591-cluster substrate-uniform-zero framing would (a) waste the SD-054-onboarding substrate-design effort on a measurement gap it doesn't fix, and (b) understate the substrate's actual capability in the fishtank slice. The two clusters need different fixes; collapsing them is misleading." |
| [failure_autopsy_V3-EXQ-490h-V3-EXQ-592b_2026-05-30.md](failure_autopsy_V3-EXQ-490h-V3-EXQ-592b_2026-05-30.md) | 490h was a silent-drop runner bug (ree-v3 commit 41c3411 fix), not a substrate result. Irrelevant to the z_goal-zero question. |
| [failure_autopsy_V3-EXQ-490i_2026-05-30.md](failure_autopsy_V3-EXQ-490i_2026-05-30.md) | 490i was a continued MECH-295 cohort iteration; ARM_1 ran with `drive_floor=0.9, drive_ema_alpha=1.0, goal_stream=True`. Bridge fires cleanly across seeds 42 / 7 / 19. Confirms goal pipeline is active in the cohort's standard config. |
| [failure_autopsy_V3-EXQ-490j_2026-05-31.md](failure_autopsy_V3-EXQ-490j_2026-05-31.md) | 490j ARM_1: `goal_active_fraction = 1.0` in all 3 seeds; `mech295_anticipatory_liking_write_peak 0.287 / 0.0066 / 0.069`; `mech295_approach_cue_bias_peak 0.396 / 0.054 / 0.427`. Substrate-side C6/C7/C9 PASS. The 490j autopsy revises to `weakens` at the behavioural-necessity layer + `supports` at the substrate-firing layer, recommending MECH-295 narrowing from necessity to modulation. This work is downstream of prereq (2); it does NOT test prereq (2). |
| [sd_054_scaffolded_onboarding_substrate_design.md](sd_054_scaffolded_onboarding_substrate_design.md) | Substrate-design memo (2026-05-29). Plan-of-record for the goal-pipeline training-regime fix. Three-phase scheduler (P0 scaffolded SD-054 + goal pipeline frozen / P1 annealed `mech295_min_drive_to_fire` 1.0->0.01 + `mech307_conjunction_z_beta_threshold` 0.6->0.3 + spawn returning to midline / P2 measurement). Master switch `use_scaffolded_sd054_onboarding_scheduler` default OFF; all new flags. Implementation surface: new `ree-v3/experiments/scaffolded_sd054_onboarding.py` + one new env kwarg `reef_bipartite_agent_spawn_in_reef_half`. `ree_core/` untouched. |
| substrate_queue.json entry 89 | `sd_id: scaffolded_sd054_onboarding`, `status: pending_implementation`, `priority: 1`, `ready: false`, `design_doc: evidence/planning/sd_054_scaffolded_onboarding_substrate_design.md`, `unblocks_claims: [Q-045, MECH-313, MECH-260, MECH-295, MECH-307, MECH-117, SD-049 Phase 2 behavioural, ARC-030, Q-040]`. autopsy_refs include both V3-EXQ-490g-cohort and V3-EXQ-603a-b-c-604-605. |
| [inter_governance_workset.md](inter_governance_workset.md) IGW-20260531-029 | `Implement substrate: scaffolded_sd054_onboarding (unblocks MECH-260)`. Lane=substrate, Skill=/implement-substrate. Currently blocked behind SD-054 candidate_v3_pending (transitive, non-load-bearing). |
| [ree-v3 ree_core/goal.py](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/goal.py) lines 100-228 | Authoritative source for z_goal update logic. See section 3 for the code trace. |

---

## 2. What the user-supplied premise gets wrong

The user's task prompt (reconstructing from `behavioral_diversity_isolation_plan.md` GAP-C `resume_condition`) said:

> "(2) goal-pipeline training regime produces non-trivial z_goal in default config -- STILL OPEN, owned by goal_pipeline:GAP-4 / IGW-20260531-013 / V3-EXQ-490g cohort"

That ownership attribution is wrong. The 490g cohort autopsy was written on 2026-05-29 and explicitly migrated ownership of prereq (2) to a different substrate target. The GAP-C resume_condition was not updated to reflect that migration; today's IGW-20260531-013 (which the user's prompt also names) is in fact a sibling work item, not the prereq-(2) owner.

The correction in this triage is a documentation fix, not a scientific finding. The scientific finding (z_goal-zero in default config is substrate-structural and needs scaffolded onboarding) was already made in the 591 autopsy and crystallised in the 2026-05-29 substrate-design memo. This triage simply re-states it cleanly + corrects the broken pointer.

---

## 3. Code trace -- why z_goal collapses in default config

z_goal is updated in [ree-v3/ree_core/goal.py](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/goal.py) `GoalState.update()` (lines 148-225). The update gate:

```python
# line 173: always decay
self._z_goal = self._z_goal * (1.0 - self.config.decay_goal)   # decay_goal = 0.005 default

# lines 195-202: SD-012 drive amendment (GAP-3, Option 2 floor + Option 1 EMA)
drive_level_floored = max(drive_level, self.config.drive_floor)   # drive_floor = 0.0 default
alpha = self.config.drive_ema_alpha                                # drive_ema_alpha = 1.0 default
self._drive_trace = (1.0 - alpha) * self._drive_trace + alpha * drive_level_floored

# lines 207-216: MECH-187 seeding gain + benefit threshold gate
effective_benefit = benefit_exposure * self.config.z_goal_seeding_gain * (
    1.0 + self.config.drive_weight * self._drive_trace
)   # drive_weight = 2.0 default; z_goal_seeding_gain = 1.0 default

if effective_benefit > self.config.benefit_threshold:   # benefit_threshold = 0.1 default
    # pull z_goal toward z_world_current via alpha_goal EMA
    ...
```

The pull only fires when `benefit_exposure * (1 + 2 * drive_trace) > 0.1`.

**At default config in the target env** (`drive_floor=0.0`, drive starts at 0 and rises only via consummatory exposure; agent dies before drive develops; benefit_exposure is sparse and small at random-init):

- `drive_trace` stays near 0.
- `effective_benefit ~= benefit_exposure * 1.0 ~= benefit_exposure`.
- benefit_exposure clears 0.1 only on actual food contact, which a dying random-init policy makes in ~0-2 ticks total per episode.
- z_goal therefore decays toward zero (decay every tick) while pull-events are rare to nonexistent.
- Floating-point residual lives at ~1e-7 (consistent with the 591 manifest's `final_z_goal_norm` values across all 15 runs).

**At the 490 cohort's gap4 substrate config** (`drive_floor=0.9, drive_ema_alpha=1.0, goal_stream=True`):

- `drive_level_floored = max(drive_level, 0.9) >= 0.9` every step.
- `drive_trace = 0.9+` from step 1 onward.
- `effective_benefit = benefit_exposure * 1.0 * (1 + 2*0.9) = benefit_exposure * 2.8`.
- benefit_exposure of just `0.0357` clears the 0.1 threshold.
- z_goal pull fires routinely; `goal_active_fraction = 1.0` (consistent with 490j ARM_1 across all 3 seeds).

This is exactly what V3-EXQ-540g PASS validated 2026-05-15 (MECH-307 default-value recalibration prereq (1)) and what GAP-3 V3-EXQ-582a PASS validated 2026-05-19 (drive_floor=0.9 + drive_ema_alpha=1.0).

**The gap is in the *default* config, not in the substrate's capability.** The substrate has the knobs to produce non-trivial z_goal; the gate is that no default training regime exists that traverses the configuration space from "agent dies at random-init in target env" to "agent inhabits goal-rich states with drive elevated enough for the goal-pipeline gate to fire".

---

## 4. What the 490 cohort tests vs what prereq (2) asks

| | Prereq (2) | 490 cohort |
|---|---|---|
| Config | REE-v3 default (`drive_floor=0.0`) | gap4 substrate (`drive_floor=0.9, drive_ema_alpha=1.0, goal_stream=True, use_dacc=True`) |
| Env | 591-family CausalGridWorldV2 size=12, infant_curriculum or target reef | Tier-1 fishtank `ENV_FISHTANK_KWARGS` |
| Training | Random-policy 2000 episodes | Single eval window, no training |
| z_goal behaviour | Collapses to ~1e-7 (591 manifest) | Active across all 3 seeds (`goal_active_fraction = 1.0`, 490j) |
| What the experiment measures | Whether substrate produces z_goal in default config | Whether MECH-295 bridge is necessary for approach commit, given an active z_goal |
| Can it close prereq (2)? | -- | **No.** The cohort already operates above the threshold; it cannot demonstrate that the substrate produces z_goal when the substrate is forced into the regime where z_goal is known to fire. |

The bookkeeping conflation was tractable because both prereq (2) and the 490 cohort live under `goal_pipeline:GAP-4`. But within GAP-4, the cohort owns the **MECH-295 cascade behavioural validation** sub-goal (Phase 4 of `goal_pipeline_plan.md`); prereq (2) is upstream of the cascade and owned at a different layer. The 490 cohort can close `goal_pipeline:GAP-4` Phase 4 (MECH-295 narrowing per 490j + a follow-on V3-EXQ-490k) without ever providing evidence for prereq (2).

---

## 5. Classification

Under the four-way scheme from the triage chip:

- **(a) cohort-tuning-issue** -- NO. The 490 cohort cannot tune its way into testing prereq (2); the cohort tests a different scientific question with a different config. The cohort's residual hyperparameter space (which V3-EXQ-490j or successor V3-EXQ-490k explores) is in the MECH-295 narrowing direction (modulation vs necessity), not in the z_goal-production direction.
- **(b) substrate-structural-issue** -- **YES, with a load-bearing caveat.** The substrate at default config cannot produce non-trivial z_goal under random-policy training in the target env. The training-regime gap is structural in the sense that no parameter tuning of the existing scheduler closes it; what is needed is a new training scheduler that scaffolds the agent's start-state distribution through SD-054 spatial structure while the goal-pipeline gates anneal in. The caveat: the substrate fix has already been designed (`sd_054_scaffolded_onboarding_substrate_design.md`, 2026-05-29), staged in `substrate_queue.json` as `scaffolded_sd054_onboarding` status=`pending_implementation`, and surfaced as IGW-20260531-029. This triage does NOT need to design a new substrate; it needs to correct the ownership pointers and confirm the existing design is still the right one.
- **(c) environment-precondition issue** -- NO at the top level. The target env (SD-054 reef + bipartite + hazard_food_attraction=0.7 + proximity_harm_scale=0.1) is the env the system is supposed to learn in; the gap is in the *training trajectory through state space*, not in the env's parameters. The scaffolded onboarding substrate does include a P0 env relaxation (`hazard_food_attraction=0.0, proximity_harm_scale=0.05`) but this is implemented as a phased scheduler change, not a permanent env change. Classifying as (c) would mis-name the substrate-level fix as env-level and obscure the spatial-scaffolding insight (agent spawning inside the reef refuge band during P0).
- **(d) ambiguous** -- NO. The 591 autopsy + 490g-cohort autopsy + substrate-design memo together produce an unambiguous reading.

**Final classification: (b) substrate-structural.** The triage chip's action for (b) says "propose + queue a substrate-side fix ... that's a follow-on /implement-substrate session". The substrate-side fix is already proposed + queued; the follow-on `/implement-substrate` is IGW-20260531-029.

---

## 6. Why the existing substrate-design memo is still the right fix

Re-checking the 2026-05-29 design against the as-of-2026-05-31 substrate state (after today's landings: SD-049 Phase 3 commit `3d276e5`, MECH-090 wiring, InfantCurriculumScheduler H_POS_FRAC recalibration `da4a1bc`):

- **SD-049 Phase 3 cascade landing (today)**: per-axis homeostatic drive substrate change in `ree-v3`. Does NOT change the `drive_floor`, `drive_ema_alpha`, `drive_weight`, or `benefit_threshold` defaults in `GoalConfig`. The phased-anneal of `mech295_min_drive_to_fire` 1.0->0.01 in the onboarding memo is orthogonal to per-axis drive substrate and remains correct.
- **MECH-090 wiring landing (today)**: beta-gate -> action selection. Does not interact with goal-pipeline training; if anything, it tightens commitment-mode discipline which the P0 frozen-goal-pipeline phase preserves.
- **InfantCurriculumScheduler H_POS_FRAC recalibration 0.70 -> 0.20 (today, prereq (3))**: the onboarding memo's choice of a NEW scheduler rather than extending `InfantCurriculumScheduler` (memo section "Implementation surface choice") explicitly de-couples the two. Today's H_POS_FRAC change does not affect the onboarding design.

The substrate-design memo's specification is unchanged by today's landings. The IGW-20260531-029 `/implement-substrate` work is still well-scoped exactly as written.

---

## 7. Action items (this triage)

| # | Action | Surface | Owner | Status |
|---|---|---|---|---|
| 1 | Write this triage memo | `evidence/planning/z_goal_collapse_triage_2026-05-31.md` | this session | done |
| 2 | Correct `behavioral_diversity_isolation_plan.md` GAP-C `resume_condition` prereq (2) ownership pointer (490g cohort -> `scaffolded_sd054_onboarding` substrate-design memo + IGW-20260531-029) | `evidence/planning/behavioral_diversity_isolation_plan.md` | this session | pending |
| 3 | Add note to `goal_pipeline_plan.md` GAP-4 making explicit that prereq (2) of GAP-C is OWNED by the scaffolded_sd054_onboarding substrate work, NOT the 490 cohort. The 490 cohort owns MECH-295 cascade behavioural validation (Phase 4) only. | `evidence/planning/goal_pipeline_plan.md` | this session | pending |
| 4 | Append a decision-log entry in `goal_pipeline_plan.md` recording today's bookkeeping correction with the triage memo cross-link. | `evidence/planning/goal_pipeline_plan.md` | this session | pending |

NO other action items. In particular, this triage does NOT:

- Edit `claims.yaml` or `substrate_queue.json`.
- Queue new experiments. The 490 cohort's V3-EXQ-490j -> V3-EXQ-490k MECH-295 narrowing path stays as the 490j autopsy already routed (separate `/queue-experiment` session).
- Trigger `/implement-substrate` for `scaffolded_sd054_onboarding`. That session has its own scheduling logic (IGW-20260531-029) and the substrate-design memo is its plan-of-record. This triage does not pre-empt it.
- Edit any 490g/490h/490i/490j autopsy. They are unchanged by this triage.

---

## 8. What this triage does NOT settle

- **Whether `scaffolded_sd054_onboarding` will actually produce non-trivial z_goal once implemented**. The memo's "Why this should work" section sets up a falsifiable bet (C2 acceptance `goal_norm_peak >= 0.1` per cell in P2). The implementation + validation experiment will decide. Today's triage only confirms the substrate-design route is correctly chartered.
- **Whether GAP-C's three-prereq decomposition is exhaustive**. The 591 autopsy listed three prereqs (`MECH-307 default-value recalibration`, `goal-pipeline training regime produces non-trivial z_goal`, `InfantCurriculumScheduler exit signal`). Prereqs (1) and (3) are cleared. If `scaffolded_sd054_onboarding` lands and V3-EXQ-603d / 591b STILL FAIL, a re-triage is needed to find prereq (4)+; today's evidence does not anticipate this.
- **MECH-295 necessity vs modulation**. The 490j autopsy's revision recommendation is in the governance lane and not relevant to GAP-C closure-distance.

---

## 9. Cross-links

- [behavioral_diversity_isolation_plan.md](behavioral_diversity_isolation_plan.md) GAP-C (resume_condition pointer fix below)
- [goal_pipeline_plan.md](goal_pipeline_plan.md) GAP-4 (decision-log entry below)
- [failure_autopsy_V3-EXQ-591_2026-05-27.md](failure_autopsy_V3-EXQ-591_2026-05-27.md) section 7 prereqs
- [failure_autopsy_V3-EXQ-490g-cohort_2026-05-29.md](failure_autopsy_V3-EXQ-490g-cohort_2026-05-29.md) section 6 cluster split
- [failure_autopsy_V3-EXQ-490j_2026-05-31.md](failure_autopsy_V3-EXQ-490j_2026-05-31.md) section 9 routing (downstream of prereq (2), not the owner)
- [sd_054_scaffolded_onboarding_substrate_design.md](sd_054_scaffolded_onboarding_substrate_design.md) plan-of-record
- substrate_queue.json entry `scaffolded_sd054_onboarding` (priority 1, pending_implementation)
- IGW-20260531-029 (`/implement-substrate` lane)
