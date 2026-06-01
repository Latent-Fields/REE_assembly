# Failure autopsy: V3-EXQ-626 goal-pipeline developmental-window diagnostic

**Date:** 2026-06-01
**Author session:** goal/wanting/liking stream repair intake
**Primary subject:** V3-EXQ-626 (`v3_exq_626_goal_pipeline_developmental_window_diagnostic_20260601T152729Z_v3`, FAIL)
**Context cohort:** V3-EXQ-514k, V3-EXQ-625, V3-EXQ-623, V3-EXQ-622 (S0 positive control)
**Verdict:** **626 is a Class-1 harness/measurement failure, NOT a substrate formation
regression.** Its axis-dissociation criteria (C2/C3/C4) are vacuous. Do not use 626 to
explain z_goal collapse via drive / hazard / writer-freeze.

---

## 1. Root cause (load-bearing finding)

The 626 script defines its own episode loop `_run_episode` (lines 416-524 of
`ree-v3/experiments/v3_exq_626_goal_pipeline_developmental_window_diagnostic.py`). That loop
does, per step:

```
sense -> clock.advance -> _e1_tick -> generate_trajectories -> select_action
      -> _measure_step_metrics -> _train_step_e1_e2 -> env.step
```

It **never calls `agent.update_z_goal(...)`** (nor `update_liking`, nor
`update_schema_wanting`). Confirmed: a content search for `update_z_goal|update_liking|
update_schema_wanting` over the 626 script returns **no matches**.

`GoalState.update()` -- the only function that mutates `z_goal` toward a benefit-seeded
target -- is reachable **only** through `REEAgent.update_z_goal()`
(`ree_core/agent.py:4827`). It is not called inside `sense()`, `generate_trajectories()`, or
`select_action()`. Therefore in 626 `z_goal` remained at its `torch.zeros(1, goal_dim)`
initialisation for **every step of every episode of every arm**.

This fully and exactly explains the manifest:

| 626 observable | Value | Explanation |
|---|---|---|
| ARM_A `z_goal_norm_median` (all phases) | 0.0 | `update()` never called -> z_goal never left zero-init |
| `arm_a_window_medians` | [0.0, 0.0, 0.0] | same, all 3 seeds |
| `bridge_cue_fires_per_episode_mean` | 0.0 | MECH-295 cue bias = f(drive * goal_proximity); goal_proximity uses z_goal=0 attractor -> candidate proximities degenerate -> `_n_cue_fires` never increments |
| `dacc_bias_nonzero_steps_per_episode_mean` | 0.0 | see Section 5 -- partly metric-keying, partly no goal signal |
| C1 (formation guard) | FAIL 0/3 | correct: ARM_A did not form z_goal -- because it was never fed |
| C2 (drive-axis isolation) | "true" | **vacuous**: 0 < ceiling trivially |
| C3 (hazard-axis isolation) | "true" | **vacuous**: 0 < ceiling trivially |
| C4 (writer-freeze rescue) | FAIL | both A and D at 0 -> ratio undefined/fails |
| C5 (consumer readout) | FAIL 0/3 | no z_goal -> no goal-driven dACC contribution |

## 2. Positive control proves the substrate is NOT regressed

V3-EXQ-622 used the shared runner `experiments/goal_stream_stages_sd054.py`, which **does**
call `agent.update_z_goal(benefit_exposure=benefit, drive_level=drive)` every step
(training stage line 537; eval stage line 590). 622 **S0 PASSed on all 3 seeds** with
`z_goal_norm_peak` 0.281 / 0.439 / 0.342 (>= 0.1 threshold). V3-EXQ-582a (GAP-3) independently
confirmed mean effective benefit at contact = 0.115 > benefit_threshold 0.1 at drive_floor=0.9.

Both 622 and 626 build agents with the same `z_goal_enabled=True`, `drive_floor=0.9`,
`drive_weight=2.0`. The ONLY material difference for formation is that 622 drives the pipeline
and 626 does not. **Conclusion: protected formation works; 626 did not test it.**

This is the same failure class as the EXQ-475 / 483 / 524 "update_z_goal omitted / TypeError"
superseded family documented in `goal_pipeline_plan.md` (Phase 4 cohort table) and the
EXQ-550 "1200/1200 update_z_goal calls but z_goal_norm_peak=0.0" incident (a different
manifestation -- there the calls fired but benefit feed was inert; here the calls are absent).
The recurring lesson: **bespoke episode loops drop the seeding hook.** The fix pattern is to
reuse the shared runner, not to re-implement the loop.

## 3. Answering the autopsy's mandatory questions

**Q: Did 626 fail because of drive anneal, hazard introduction, writer-freeze failure, or
earlier formation failure?**
None of those. It failed *upstream of all of them*: the experiment never fed the goal
pipeline, so z_goal never formed in any arm. The drive/hazard/writer-freeze axes were never
actually exercised because there was no z_goal for them to act on.

**Q: Why are C2/C3 in 626 potentially vacuous if ARM_A never forms z_goal?**
C2 ("ARM_B drive-anneal collapses z_goal below ceiling") and C3 ("ARM_C hazard collapses
z_goal below ceiling") are *differential* criteria: they assume there is a non-zero z_goal in
the control that the manipulated arm reduces. With every arm pinned at z_goal=0 by the missing
hook, "B is below the ceiling" and "C is below the ceiling" are trivially true (0 < 0.05) and
carry **no information** about whether drive-anneal or hazard actually collapse a formed goal.
The acceptance code even reports them as `pass=true`, which is misleading -- the overall gate
correctly fails because C1 and C5 fail.

**Q: What does `bridge_cue_fires_per_episode_mean = 0.0` imply?**
With z_goal=0, the MECH-295 bridge's `candidate_proximities` (derived from goal_proximity to a
zero attractor) do not produce a non-zero `liking_signal`, so `_n_cue_fires` never increments.
It implies the cue-bias path is *downstream-starved*, not broken: no wanted signal exists for
it to convert into an approach cue. It is NOT evidence the bridge is faulty (493 isolation
6/6 PASS).

**Q: What does high `approach_commit_rate` with z_goal = 0.0 imply?**
(Observed in sibling runs 622 S3 and 483c/524a, not 626 specifically.) It implies
`approach_commit` is being satisfied by something *other than* a formed goal -- e.g. the beta
gate elevating plus a residue VALENCE_WANTING write that does not require z_goal, or a metric
that saturates trivially. It is a **measurement-validity red flag**: a commit metric that is
high while z_goal is zero is not measuring goal-driven approach. (626's design tried to fix
this with `approach_commit_at_high_z_goal_rate` gated on z_goal>0.05 -- a good instinct -- but
the gate is moot when z_goal is uniformly 0.)

**Q: What does 514k's `wanting_liking_dissoc_fraction = 0.0` imply?**
Here the pipeline WAS driven (Class-2). It implies that even with SD-049 multi-resource
identity + SD-015 z_resource available, the trajectory that maximises wanting is the same as
the trajectory that maximises liking on every arm and seed -- i.e. **wanting carries no
object-identity information distinct from liking.** This is the direct symptom of the missing
L2-L3 (object binding + incentive token). It is confounded by the GAP-2 SP-CEM monostrategy
issue (a monomodal policy cannot generate the behavioural variety needed to *measure*
dissociation), so 514k is `weakens`/`non_contributory`, not a clean falsification -- but it is
the strongest current evidence for the object-binding gap.

**Q: What does 625's event-without-consumer-input pattern imply for the goal stream?**
625 is the harm/threat axis (SD-037), but it exhibits the *same structural fault shape* the
goal stream suffers: a scheduled environment event (hazard) fired in 2/3 seeds, yet every
consumer-input channel (`z_harm_a_norm`, `cea_low_freq_magnitude`, `bla_pe_magnitude`,
`dacc_pe`, ...) is identically 0.0. "Event happened in the env but did not enter the consumer
stream." For the goal stream this raises a concrete hypothesis to check during the L7 wiring
audit: **is there a systematic gap where producer events do not reach consumer channels?**
625 must be flagged for governance separately -- its manifest headline says PASS (the six
measurement distributions had n>0) while `acceptance_pass=false` (the substrate-readiness gate
C1/C2/C3 failed). **The headline/acceptance conflict must not be normalised.**

**Q: What does 623 PASS teach us as a positive control?**
623 (MECH-104 volatility interrupt) produced a discriminative signal (`delta_var_unexpected`
~0.031 ON vs 0.0 ablated) AND behavioural de-commitment (24-31 decommits ON, 0 ablated), 8/8
criteria. It proves the REE signal->behaviour machinery is intact: **when a signal path is
correctly wired and actually driven, REE turns the signal into a behavioural consequence.**
Therefore the goal stream's problem is not "REE cannot act on signals"; it is either "the
wanted signal is never produced/fed" (Class-1, 626) or "the wanted signal is not object-bound"
(Class-2, 514k). 623 is the contrast that localises the fault to production/binding, not to
the consumer's ability to act.

## 4. Why this was not caught earlier

- The 626 script passed its `--dry-run` (the dry-run only checks the loop executes and emits
  an outcome; with no `update_z_goal` it still "runs", just at z_goal=0). A dry-run that does
  not assert a *non-zero positive-control metric* cannot catch a missing seeding hook.
- 626 was authored as a fresh bespoke loop (to add per-phase drive_floor / HFA / writer-freeze
  mutation and dACC measurement) rather than extending the 622 `GoalStreamStagesRunner`. The
  re-implementation silently dropped the single most important line.

## 5. dACC metric note (secondary)

Even had z_goal formed, the C5 dACC metric reads `bundle["mode_ev"]` (fallback
`harm_interaction`) norm > 1e-6 (`_measure_step_metrics`, lines 393-405). The wiring map
confirms dACC does **not** read z_goal/goal_proximity directly -- its bundle is harm-PE +
payoff/effort + drive. So C5 partly measures whether the dACC bundle is *non-zero at all*, not
whether it reflects the goal signal. The PROP-CONSUME claim and the Stage-3 diagnostic make
"does z_goal reach dACC?" an explicit, separate test rather than an incidental byproduct.

## 6. Routing

- **626 -> /diagnose-errors (harness fix), re-issue as V3-EXQ-626a** (lettered iteration;
  scientific question unchanged, implementation was wrong -> append letter per EXQ versioning
  policy). 626a must reuse the shared `update_z_goal`-driven runner (or add the call to the
  bespoke loop) AND add a Stage-0-style positive-control assertion. `supersedes: V3-EXQ-626`.
- **Stage 0 unit test** (no substrate change) should exist as a contract so this class of bug
  is structurally impossible to ship again: assert forced inputs to `GoalState.update` produce
  non-zero, direction-stable z_goal.
- **514k -> object-binding ladder** (Stage 1-2), gated on GAP-2 SP-CEM; do not re-run the
  ecological dissociation test until the object-bound substrate exists and the harness is
  positive-control-guarded.
- **625 -> separate governance flag** (headline/acceptance conflict + harm-consumer-zero);
  cross-ref this autopsy for the shared "event does not enter consumer stream" hypothesis.
- **No claims.yaml change from this autopsy.** 626/625 are `claim_ids=[]` diagnostics; their
  evidence_direction is `non_contributory` and they must NOT weight any claim.

## 7. What must not be concluded

- NOT "protected goal formation is broken" (622 S0 + 582a refute it).
- NOT "drive anneal / hazard / writer-freeze explains z_goal collapse" (never tested in 626).
- NOT "the goal stream is closed" or "wanting/liking dissociation demonstrated."
- NOT "625 passed."
