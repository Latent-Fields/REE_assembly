# Failure Autopsy -- V3-EXQ-603d (scaffolded SD-054 onboarding; Q-045 / MECH-313 / MECH-260)

**Generated:** 2026-06-01T17:33:42Z
**Session:** failure-autopsy-v3-exq-603d-20260601T173342Z
**Scope:** single (sits in the 603-chain seed-fragility cluster; see Section 6)
**Status:** confirmed (interactive Step 8 gate passed)
**Target:** V3-EXQ-603d (run_id `v3_exq_603d_q045_mech313_mech260_scaffolded_sd054_20260601T095345Z_v3`)
**Claim IDs:** Q-045, MECH-313, MECH-260
**Routing (user-confirmed):** implement-substrate AMEND on `scaffolded_sd054_onboarding` (wire `update_z_goal` into the scheduler training loop + positive-control gate)

---

## 0. Context and supersession state

V3-EXQ-603d is the 5th iteration of the 603 chain (603 -> 603a -> 603b -> 603c -> 603d)
and the **first behavioural retest on the implemented `scaffolded_sd054_onboarding`
substrate** (landed 2026-05-31, ree-v3 commit 28ebd3d; substrate-readiness V3-EXQ-621a
PASS 2026-06-01T05:55Z). It supersedes V3-EXQ-603c. The /governance cycle of
2026-06-01T1658Z marked the run reviewed but intentionally LEFT it pending and routed it
here ("603d -> /failure-autopsy, P1 survival gate 2/3 seeds").

The 591-triage memo (`z_goal_collapse_triage_2026-05-31.md`) Section 8 explicitly
anticipated this autopsy: *"If `scaffolded_sd054_onboarding` lands and V3-EXQ-603d / 591b
STILL FAIL, a re-triage is needed to find prereq (4)+."* This artifact is that re-triage.
**Prereq (4) is not a new scientific prerequisite -- it is a missing `update_z_goal` call
in the implemented scheduler (Section 1, load-bearing finding).**

The manifest already carries `evidence_direction: non_contributory` (per-claim
non_contributory on all three claims) and `interpretation_label: SUBSTRATE_FAILURE`.
**No claim disposition is recommended; no manifest field is changed.** The artifact records
the diagnosis and hands a structured implement-substrate AMEND to /governance.

---

## 1. Facts reconstruction (manifest + script + scheduler verbatim)

### 1a. The two observables

3 seeds (42, 43, 44) x 5 arms (ARM_0 both-off / ARM_1 mech313-only / ARM_2 mech260-only /
ARM_3 both-on / ARM_4 matched-noise). Per-cell pipeline = scheduler P0 (30 ep) ->
scheduler P1 (30 ep) -> bespoke P2 measurement (30 ep x 500 step, FIFO warmup 75).

**Observable 1 -- P1 survival gate.** In every arm, seeds 42 and 44 abort at
`scaffold_p1` with `survival_gate_passed: false` (`abort_reason: p1_survival_gate_failed`);
only **seed 43** clears the gate and runs P2. The gate is `median episode length over the
last stability window >= scaffold_p1_survival_gate_steps (75)`.

| Arm | seed 42 P1 median_len | seed 43 P1 median_len | seed 44 P1 median_len |
|---|---|---|---|
| ARM_0 | 13.5 (fail) | 200.0 (pass) | 8.5 (fail) |
| ARM_1 | 13.5 (fail) | 200.0 (pass) | 12.5 (fail) |
| ARM_2 | 10.5 (fail) | 200.0 (pass) | 9.5 (fail) |
| ARM_3 | 12.0 (fail) | 108.0 (pass) | 9.0 (fail) |
| ARM_4 | 9.0 (fail) | 200.0 (pass) | 9.0 (fail) |

Result: `p2_cell_count = 5` (the five seed-43 cells), `aborted_cells = 10`. Effective N=1.
The divergence is visible already in **P0**: seeds 42/44 reach P0 mean episode length
~21-41, while seed 43 reaches ~175-200. Seeds 42/44 never develop a survival-competent
policy even on the easy (goal-pipeline-frozen) P0 env.

**Observable 2 -- z_goal is zero everywhere.** `z_goal_norm_peak_ARM_3_max = 0.0`; every
arm_result row has `z_goal_norm_peak = 0.0`, including the surviving seed-43 cells that ran
the full 500-step P2. Therefore C4 (`z_goal_norm_peak_max(ARM_3) > Z_GOAL_FLOOR=0.4`) =
false, and C5 (`rolling_h_pos_mean(ARM_3) > 3.23`) = false (h_pos rolling logs are all
0.0). `_interpretation_label` returns `SUBSTRATE_FAILURE` because `not c4 or not c5`.

### 1b. Load-bearing finding -- the scheduler never feeds z_goal

`z_goal` is mutated only by `GoalState.update()`, reachable only via
`REEAgent.update_z_goal()` (`ree_core/agent.py`). I searched the implemented scheduler
`ree-v3/experiments/scaffolded_sd054_onboarding.py` for
`update_z_goal | update_liking | update_schema_wanting`: **zero matches.**

- The scheduler's training loop `_train_episode` (lines 551-632) runs
  `sense -> clock.advance -> _e1_tick -> generate_trajectories -> select_action ->
  E1/E2 training -> env.step`. It **never calls `update_z_goal`**. `run_p1` un-freezes the
  goal-pipeline *gates* (`_set_goal_pipeline_frozen(agent, frozen=False)`) and anneals
  `mech295_min_drive_to_fire` / `mech307_conjunction_z_beta_threshold`, but with no
  `update_z_goal` call the goal pipeline is never driven -- the gates open onto a stream
  that is never fed.
- 603d's own bespoke P2 loop (`_run_p2_measurement` / `_select_action_with_harm`, script
  lines 363-389, 429-589) also never calls `update_z_goal`. It threads `obs_harm_a` for
  the dACC path but not the goal feed.

So `z_goal` sits at its `torch.zeros(1, goal_dim)` init for every step of every arm in both
training and measurement. **This is the same Class-1 hook-omission the V3-EXQ-626 autopsy
diagnosed today** (`failure_autopsy_V3-EXQ-626_2026-06-01.md`: "bespoke episode loops drop
the seeding hook") -- except here it is in the **implemented substrate module (the
scheduler)**, not just an experiment script. It exactly explains V3-EXQ-621a's
substrate-readiness note ("C2 z_goal floor unmet; z_goal feeding under scaffolded
onboarding is not yet wired correctly").

**Consequence:** C4 (z_goal) was structurally guaranteed to fail independent of substrate
quality. The `SUBSTRATE_FAILURE` label is therefore a **wiring/harness artifact, not a
substrate ceiling.** It is non_contributory and must NOT be read as evidence the substrate
cannot form goals.

### 1c. Which criterion failed

The manifest gate `PASS = C2 AND C4 AND C5 AND FP2 AND (p2_cell_count == 15)`. Three
independent reasons it cannot pass: (i) C4/C5 false via the z_goal/h_pos wiring artifact
(1b); (ii) `p2_cell_count = 5 != 15` (the survival aborts); (iii) Q-045 discrimination
(C2 / FP2) is untestable at N=1. **Failed criterion class:** `absolute` (the C4 substrate-
engagement gate), but the failure is upstream of the substrate -- a harness omission.

---

## 2. Claim-layer mapping

| Claim | Type | Status | Did the test let it express? |
|---|---|---|---|
| Q-045 | open_question | open, v3_pending, pending_retest_after_substrate, substrate_ceiling | NO -- coupling/independence untestable at effective N=1; z_goal never fed |
| MECH-313 | mechanism_hypothesis | candidate_substrate_landed, v3_pending, pending_retest_after_redesign | NO -- ARM_1 vs ARM_0 only readable at N=1 (seed 43); z_goal=0 means the goal-rich regime the noise floor is supposed to diversify never existed |
| MECH-260 | mechanism_hypothesis | candidate, v3_pending, pending_retest_after_substrate | NO -- dACC operative in seed-43 ARM_2/ARM_3 cells (dacc_forward_calls 728/870, max_suppression 1.0) but behavioural effect unmeasurable at N=1 |

All three already carry `pending_retest_after_substrate` / `epistemic_category:
substrate_ceiling`. **This autopsy adds a failure_record, not a re-classification.**
`claim_ids` accuracy: tags are correct and inherited consistently from the 603 chain; the
FAIL does not weigh against any of the three (it never tested them).

EXQ-445h remains the sole valid MECH-260 support; nothing in 603d touches that record.

---

## 3. Biological-reference triage

- **MECH-313 (LC-NE tonic noise floor)** -- clear (Aston-Jones & Cohen 2005; Haarnoja 2018
  SAC). Untestable here: with z_goal=0 there is no goal-directed behaviour for a noise floor
  to diversify away from.
- **MECH-260 (dACC anti-recency)** -- clear (Scholl & Kolling 2015; Kennerley 2006). FIFO +
  suppression both fire in surviving cells. Biology intact.
- **Q-045 (LC-NE / dACC independence)** -- biology says coupled-not-collapsed (Tervo 2014);
  needs a non-degenerate, goal-engaged substrate to test.
- **Goal maintenance (the wiring gap)** -- vmPFC/dlPFC sustain goal representations
  (the 622 autopsy's reference frame). But 603d never seeded a goal at all, so this is not
  even the 622 persistence-under-anneal question yet -- it is upstream of it.
- **Biology divergence: none.** This is a substrate-wiring failure, not claim falsification.
  No formal-definition import is implicated; no `/lit-pull` commission warranted.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | none of the three claims under fair test; FAIL weighs against none |
| Biological reference | clear | all three mechanisms well-anchored; no divergence |
| Developmental / dependency prerequisites | **missing (wiring)** | the implemented scheduler never calls `update_z_goal`; goal-pipeline gates open onto an unfed stream |
| Implementation completeness | **partial / wiring gap** | symbol-of-mechanism (gates annealed, pipeline un-frozen) present; functional role (z_goal actually formed) absent -- the single most important line is missing, exactly the 626 fault class |
| Environment adequacy | confounded | P0 frozen-goal env still kills seeds 42/44; but with no goal drive the policy has no reason to forage, so survival is not a clean env read |
| Measurement adequacy | partial | bespoke P2 also omits the goal feed; C4/C5 cannot measure substrate engagement on an unfed pipeline |
| Integration adequacy | isolated | goal-stream never integrated into the trained policy because it was never driven |
| Scale / capacity | confounded | P0=30/P1=30 is below 603c's 100/50; survival fragility cannot be cleanly attributed without restored budget |

**Dominant diagnosis:** named `substrate_ceiling` (the category the claims already carry),
but the proximal mechanism is an **implementation/wiring gap in the implemented scheduler**
(`update_z_goal` never called) -- recoverable, not a ceiling.
**Recommended `epistemic_category`:** `substrate_ceiling` (unchanged; the wiring gap lives
under the same substrate entry).

---

## 5. The z_goal=0 reading (user-confirmed)

The z_goal=0 / C4 `SUBSTRATE_FAILURE` is a **harness/wiring artifact (626-class),
non_contributory; NOT substrate-ceiling evidence.** Two distinct z_goal-zero mechanisms
must be kept separate:

1. **Triage-memo mechanism** (`z_goal_collapse_triage_2026-05-31.md` Section 3): even when
   `update_z_goal` IS called, at default config the `benefit_threshold` gate rarely fires
   (drive_floor=0.0). The scaffolded onboarding was designed to anneal those gates so the
   gate fires. This is what 621a/622 probe.
2. **Harness mechanism (626-class, dominant in 603d):** `update_z_goal` is never called at
   all, so `GoalState.update()` is never even reached. Mechanism (1) is moot because the
   function that mechanism (1) gates is never invoked.

603d is dominated by mechanism (2). Until the scheduler calls `update_z_goal`, neither the
603d behavioural result nor the 622 anneal-rate amend can be evaluated -- the hook wiring is
strictly upstream of the persistence/anneal-rate question.

---

## 6. Cluster pattern

The seed-fragility (only seed 43 survives) is structurally identical across the entire 603
chain (603a/b/c all 1/3 surviving seeds; 604/605 seed 42 dies). 603d reproduces it on the
implemented substrate. But the **load-bearing new signal is single**: the scheduler's
`update_z_goal` omission. The survival fragility is a continuation of the known cluster
shape, now confounded (Section 4) by reduced budget + an inert goal pipeline; it is recorded
as a failure_record but is NOT a clean survival-ceiling signal.

This is the "negative-control / absolute criterion passes; discrimination fails" substrate-
ceiling fingerprint (P0 builds episode length for seed 43; discrimination across arms is
untestable) -- but here the absolute criterion (C4) itself fails for a wiring reason, which
is the additional diagnostic content beyond the 2026-05-29 cluster autopsy.

---

## 7. Learning extracted

1. **The implemented `scaffolded_sd054_onboarding` scheduler does not feed the goal
   pipeline.** `_train_episode` (and 603d's bespoke P2) never call `update_z_goal`. This is
   the 626 fault class surfacing in a *substrate module*. It is the true content of 621a's
   "z_goal feeding not yet wired correctly" note and of the 591-triage's anticipated
   "prereq (4)".
2. **The hook omission is strictly upstream of the 622 anneal-rate amend.** The 622 autopsy
   recommended slowing the drive_floor anneal to fix z_goal persistence -- but that
   recommendation assumed `update_z_goal` was being called (it traced `GoalState.update()`
   persistence in the *shared* `goal_stream_stages_sd054` runner). The scheduler is a
   different module that never calls it. Wire the hook first; re-evaluate anneal-rate after.
3. **603d's `SUBSTRATE_FAILURE` label is a wiring artifact, not a ceiling.** C4 could not
   have passed regardless of substrate quality. Reading it as substrate-ceiling evidence
   would understate the substrate and mis-route the fix.
4. **The P1 survival fragility persists but is confounded** (reduced budget 30/30 vs 603c
   100/50; inert goal pipeline => no foraging drive => worse survival policy). Recorded as a
   failure_record, flagged confounded, to be re-tested on 603e at restored budget on the
   hook-fixed scheduler.
5. **A positive-control assertion is mandatory.** A dry-run that does not assert a non-zero
   z_goal cannot catch this omission (626 lesson). The scheduler amend must ship with a
   Stage-0-style guard (forced inputs to the goal feed produce non-zero z_goal) so a
   z_goal=0 scheduler is structurally unshippable.

---

## 8. Repair pathway and routing (user-confirmed Step 8 gate)

**Routing:** `implement-substrate` **AMEND** on `scaffolded_sd054_onboarding`
(`action: amend`, `target_sd_id: scaffolded_sd054_onboarding`).

**Amend content:**
- Wire `agent.update_z_goal(benefit_exposure=..., drive_level=...)` into the scheduler's
  `_train_episode` every step in P1 (and P0 if goal-pipeline-frozen design permits), mirroring
  the shared `experiments/goal_stream_stages_sd054.py` runner that the 622 autopsy confirmed
  calls `update_z_goal` (training line ~537, eval line ~590).
- Add a Stage-0-style positive-control assertion / contract test: forced benefit+drive inputs
  to the goal feed must produce non-zero, direction-stable z_goal under the scheduler, so the
  hook can never be silently dropped again.
- The 622 autopsy's anneal-rate amend (slower drive_floor anneal; decoupled risk_floor;
  drive_ema recalibration at low drive) is **downstream** of this hook fix -- re-evaluate its
  priority after the hook lands and z_goal forms.

**Then** re-issue 603d -> **603e** via `/queue-experiment` on the hook-fixed scheduler with
restored budget (P0/P1 back toward 603c's 100/50 or scheduler defaults) and a z_goal-driven
positive-control gate, so the survival-fragility read is no longer confounded by an inert
goal pipeline.

**Draft `evidence_quality_note` for /governance (exact text; not applied here)** -- append
to the `scaffolded_sd054_onboarding` substrate_queue implementation_log AND as a dated note
on Q-045 / MECH-313 / MECH-260:

> "[2026-06-01 autopsy V3-EXQ-603d] First behavioural retest on the implemented
> scaffolded_sd054_onboarding substrate. FAIL non_contributory on Q-045 / MECH-313 /
> MECH-260. Two findings: (1) LOAD-BEARING -- the scheduler's `_train_episode` (and 603d's
> bespoke P2) never call `agent.update_z_goal`, so z_goal stays at zero-init for every step
> of every arm; the `SUBSTRATE_FAILURE`/C4 z_goal=0 label is a Class-1 harness/wiring
> artifact (same class as V3-EXQ-626), NOT substrate-ceiling evidence. This is the true
> content of 621a's 'z_goal feeding not yet wired correctly' and the 591-triage's
> anticipated prereq (4). Routing: implement-substrate AMEND -- wire update_z_goal into the
> scheduler + Stage-0 positive-control gate; this is upstream of the 622 anneal-rate amend.
> (2) P1 survival gate failed 2/3 seeds (42, 44; only 43 to P2; p2_cell_count 5/15),
> reproducing the 603-chain seed-fragility -- but confounded by reduced budget (P0/P1=30/30
> vs 603c 100/50) and the inert goal pipeline; recorded as a failure_record, to be re-tested
> on 603e at restored budget on the hook-fixed scheduler. EXQ-445h remains the sole valid
> MECH-260 support; the cumulative sub-threshold MECH-313 directional signal from the 603
> chain is unchanged (603d adds no new MECH-313 read -- N=1, z_goal=0)."

---

## 9. Provenance

- Manifest: `REE_assembly/evidence/experiments/v3_exq_603d_q045_mech313_mech260_scaffolded_sd054_20260601T095345Z_v3.json` (outcome=FAIL, evidence_direction=non_contributory, interpretation_label=SUBSTRATE_FAILURE, supersedes V3-EXQ-603c).
- Script: `ree-v3/experiments/v3_exq_603d_q045_mech313_mech260_scaffolded_sd054.py` (1062 lines; interpretation grid lines 99-130; bespoke P2 lines 429-589).
- Substrate module: `ree-v3/experiments/scaffolded_sd054_onboarding.py` (`_train_episode` lines 551-632; `run_p1` lines 403-485; zero `update_z_goal` matches).
- Substrate entry: `REE_assembly/evidence/planning/substrate_queue.json` (`sd_id: scaffolded_sd054_onboarding`, status=implemented, priority 1, unblocks Q-045/MECH-313/MECH-260/...).
- Predecessor autopsies: `failure_autopsy_V3-EXQ-603a-b-c-604-605_2026-05-29.md`, `failure_autopsy_V3-EXQ-603_2026-05-23.md`, `failure_autopsy_V3-EXQ-591_2026-05-27.md`, `failure_autopsy_V3-EXQ-622_2026-06-01.md`, `failure_autopsy_V3-EXQ-626_2026-06-01.md`.
- Triage memo: `z_goal_collapse_triage_2026-05-31.md` (Section 8 anticipated this re-triage).
- Substrate-readiness prior: V3-EXQ-621a PASS 2026-06-01T05:55Z (C2 z_goal floor unmet).
- Companion JSON: `failure_autopsy_V3-EXQ-603d_2026-06-01.json`.
