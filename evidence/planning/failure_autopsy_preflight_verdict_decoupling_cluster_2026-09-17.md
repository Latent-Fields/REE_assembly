# Failure autopsy (CLUSTER) -- pre-flight / readiness verdict decoupling

**Targets:** V3-EXQ-849, V3-EXQ-852, V3-EXQ-864a, V3-EXQ-865, V3-EXQ-899
**Generated:** 2026-09-17T10:07:04Z | **Status:** confirmed (user-gated) | **Scope:** cluster
**Machine-readable:** `failure_autopsy_preflight_verdict_decoupling_cluster_2026-09-17.json`

> **These five runs were cleared as reviewed before they were ever adjudicated.** All five appear in
> `review_tracker.json` under BOTH `reviewed_run_ids` and `discussed_experiment_dirs`. Because
> `pending_review.md` lists only results *not yet* marked reviewed, they were invisible to it -- a
> diagnostic cleared as reviewed without an autopsy cannot be surfaced by the normal discovery net.
> Governance has moved on. **The review markings have deliberately NOT been reverted.**

---

## 1. The cluster shape

All five emit a verdict that is **decoupled from the scientific question**, and in all five a
readiness/precondition control **fires unconditionally by construction**.

| Run | Outcome | The criterion carrying the question |
|---|---|---|
| V3-EXQ-849 | **PASS** | sole load-bearing `C1_any_lever_shows_precursor_reach` -- `passed: false`, 0.0 vs 1.0 |
| V3-EXQ-865 | **PASS** | sole load-bearing `C1_any_target_shows_precursor_reach` -- `passed: false`, 0.0 vs 1.0 |
| V3-EXQ-864a | **PASS** | `C1_crossover_bracketed_in_swept_range` -- `load_bearing: false` *and* `passed: false`; both branches set PASS |
| V3-EXQ-852 | **PASS** | three criteria, none with `measured`/`threshold`; `C2` is an IEEE-754 identity |
| V3-EXQ-899 | **FAIL** | failing criterion **arithmetically unreachable** -- perfect play still fails |

The self-certifying readiness controls:

- **849 / 865** -- `has_behavioural_reach=true` in all 30 cells is guaranteed: the probe hardcodes
  `use_anchor_sets=True` / `use_per_region_vs=True` two statements before calling
  `assert_behavioural_reach`, which reads only those flags. The parent module's own docstring calls this
  "a BLANKET FLAG CHECK ... necessary but NOT sufficient" -- **it is the defect the probe was built to replace.**
- **852** -- the lone precondition is declared unfailable *by the driver itself*
  (`ANCHOR_REACHABILITY_EXEMPT`, driver:74-81, "reachable by construction"). Two of three
  `criteria_non_degenerate` flags are that same boolean; the third is the literal `True`.
- **864a** -- `real_exposure_achieved` is 1.0 by construction; the driver's own comment (driver:344-345)
  says "trivially 1.0 by construction (the inner loop never breaks)".
- **899** -- `curriculum_reached_p2` tests only `total_steps > 0`, firing once the measurement loop runs.

### Is this five bugs or one property?

**One property.** The convergence runs across structurally different claims -- Q-081 (open_question),
SD-076 and SD-085 (design decisions), ARC-030/MECH-307 (not even tagged) -- which is what makes it a
family property rather than a per-experiment defect. The family's verdict machinery certifies that the
**harness ran**, not that the substrate has the property under test; and because the certification is
built from values the driver has just set, it cannot report otherwise.

**The `test_design_ceiling` reading is NOT live.** A substrate-enrichment reading would require that
these experiments interrogated the substrate and found it wanting. In four of five the substrate was
never interrogated at all (unwired signals, an absent gate object, a tautological identity, an
unreachable threshold); in the fifth the data was collected and never analysed.

---

## 2. Per-target findings

### V3-EXQ-849 -- the checked signals are unwired from the lever
The repository's own contract test states it (`test_q081_pair_reach_check.py:436-443`): the probe's
checked signal set "structurally does not" have a live wired path from boundary events, "for any of the
8 populated signals". The maximal lesion (`suppress`) also returns `has_pair_specific_reach=False`.
That audit landed in `02c155c` (2026-08-01 19:51) -- **after** 849 ran (00:59Z), **before** 865 ran (22:13Z).

Compounding it: 849's substrate predates the seed-determinism fix (`02c155c` is not an ancestor of its
`substrate_commit` `1bca42e7`). The INTACT arm is `mode="off"` in every cell, so per-seed boundary counts
should match across levers -- in 849 they never do (seed 0: 27/544 vs 23/405; seed 3: 88/1034 vs 1/62;
seed 4: 0/28 vs 116/1200). In 865, on the post-fix substrate, they are identical at all 20 cells.
**849's `seed` label does not identify the agent initialisation.**

### V3-EXQ-865 -- the mechanism under test is absent from the run's own config
`agent.vs_rollout_gate` is `None` under the exact config the probe builds: `use_vs_rollout_gating` is
never set, and `ree_core/agent.py:2739-2745` gates construction on it. So the two `gate_stream` call
sites the design names as *the* reach paths (`agent.py:5886-5887`, `:10124-10125`) never execute,
`per_stream_vs` stays `{}` (`config.py:2836`), and the probe takes its `else: gated_value = raw_value`
branch. **The `*_gated_*` half of every snapshot is a verbatim copy of the `*_raw_*` half -- 60/60
snapshots.** The probe compared a value with itself. Its queue note asserts these paths were
"already-config-reachable"; that is false for this run.

### V3-EXQ-852 -- a tautological criterion, and a real substrate defect underneath
`C2_default_arm_bit_identical_to_raw_f` cannot fail for any input. The driver sets `f_weight = 1.0` on
`ARM_DEFAULT` (driver:127) -- already the substrate default (`config.py:991`) -- then checks
`abs(tick0_f_weighted - tick0_f_raw) <= 0.0 + 1e-9`, where both come from the same dict, same
`score_trajectory` call, same tensor (`e3_selector.py:1505, :1604, :1609`). `1.0 * f` is bit-identical in
IEEE-754. The one branch that could break it (`use_e3_channel_commensurability`) defaults `False` and is
never enabled here.

**The real finding is underneath:** `score_trajectory` is called **per-candidate in a loop**
(`e3_selector.py:3062-3092`) and `_last_traj_components` is overwritten each iteration, so `tick0_f_raw`
records the **last candidate's** value, not the 32-candidate pool statistic its name implies. The
arithmetic gives it away -- seed 22's recorded diff `5.460163116455078` is not
`0.5 * 11.305198669433594 = 5.652599334716797`. Filed as a `create` at **severity `corrupting`**
(user-confirmed): the field looks like a population statistic and is one arbitrary sample.

### V3-EXQ-864a -- the data contains the effect its statistics miss
Verdict machinery first: both branches of the crossover test set `outcome = "PASS"` (driver:813-818), and
the sole load-bearing criterion `C0_trajectory_data_usable` is literally `bool(gate["all_green"])`
(driver:775) -- the same expression as `readiness_ok` (driver:809), a restatement of the precondition gate.

**Then the substance.** In **12/12 cells**, exactly half the sign flips sit at episode boundaries and half
**mid-episode**. After every reset `rv` falls below `wci_symmetric_rv_ref` and recovers mid-episode, and
**the recovery latency shortens as training proceeds** -- a recalibration-speed learning curve:

| arm | seed | steps/ep | recovery latency (ticks after reset) |
|---|---|---|---|
| ARM_INFL_LO | 0 | 200 | 75, 75, 60, 50, 50, 40, 50 |
| ARM_INFL_LO | 1 | 200 | 70, 60, 60, 65, 60, 45, 35 |
| ARM_INFL_HI | 0 | 200 | 65, 70, 50, 45, 45, 40, 45 |
| ARM_INFL_HI | 1 | 200 | 60, 55, 55, 60, 50, 40, 30 |
| ARM_INFL_LO | 0 | 500 | 72, 60, 72, 60, 72, 48, 12 |
| ARM_INFL_LO | 1 | 500 | 72, 72, 60, 60, 48, 36, 24 |
| ARM_INFL_HI | 0 | 500 | 60, 48, 72, 60, 60, 36, 12 |
| ARM_INFL_HI | 1 | 500 | 60, 60, 60, 48, 48, 36, 12 |
| ARM_INFL_LO | 0 | 1000 | 75, 75, 75, 75, 50 |
| ARM_INFL_LO | 1 | 1000 | 75, 75, 50, 50, 25, 50, 50 |
| ARM_INFL_HI | 0 | 1000 | 75, 75, 50, 50, 50 |
| ARM_INFL_HI | 1 | 1000 | 75, 50, 25, 50, 25, 25, 25 |

Why the statistics miss it: `sign_flip_seen` compares only the **first and last** sample
(driver:653-654), both positive; `crossover_global_tick` equals **exactly `steps_per_ep`** in all 12 cells
(the reset transient); and C1 reads only six seed-mean `diff_final` scalars (driver:744-768) -- no
variance, no statistical test, and **it never touches the trajectory arrays the experiment was built to
collect.**

**Stated precisely so it is not over-read:** the run does not report a false result. Its statistics are
correct about what they measure. The defect is that all three are blind to an effect present in 12/12
cells of its own banked data. **The remedy is re-analysis at zero compute cost** -- the trajectories are
already in the run pack. (User also asked for a re-queue alongside; recorded in the routing.)

**Recurrence:** predecessor V3-EXQ-864 was already autopsied as `measurement_test_design_defect` /
`non_contributory` (user-gated 2026-08-01). Its sweep was bit-identical across all three swept values and
it *also* reported PASS under the identical criteria architecture with the identical
`interpretation.label`. 864a inherited that architecture unchanged.

### V3-EXQ-899 -- a criterion perfect play could not satisfy, on a DV that rewards dying
Resources spawn 5 per episode, never respawn, over 30 episodes -- a hard ceiling of **150 events per
cell**. `resource_visit_rate = n_resource_events / total_steps`:

| condition | seed | steps | events | rate | ceiling @150 | required | reachable? |
|---|---|---|---|---|---|---|---|
| FULL_M307_ON | 42 | 5413 | 15 | 0.00277 | 0.02771 | ~0.0625 | **no** |
| FULL_M307_OFF | 42 | 4433 | 14 | 0.00316 | 0.03384 | ~0.0568 | **no** |
| FULL_M307_ON | 43 | 3649 | 10 | 0.00274 | 0.04111 | ~0.0568 | **no** |
| FULL_M307_OFF | 43 | 4233 | 12 | 0.00283 | 0.03544 | ~0.0568 | **no** |
| FULL_M307_ON | 44 | 4035 | 10 | 0.00248 | 0.03717 | ~0.0658 | **no** |
| FULL_M307_OFF | 44 | 3849 | 9 | 0.00234 | 0.03897 | ~0.0658 | **no** |

**A perfect forager fails G0 in all six trained cells.** The FAIL is not a measurement of the substrate.

And the DV is **anti-correlated with competence**. RANDOM scores ~4.4x the trained arms while having
`survival_rate` **exactly 0.0** in all three seeds (320/296/317 steps, 4/2/5 events) -- it "wins" only
because dying at ~300 steps instead of surviving ~4000 shrinks the denominator by an order of magnitude.

**The self-route label is a mislabel.** `readiness_fail_curriculum_gate_blocks_retest` asserts a curriculum
gate blocked the retest; but both readiness preconditions measured 1.0, and the run completed 9/9 cells
over 5h13m. Nothing about a curriculum gate was measured as blocking. The label is emitted by elimination
from a three-way `if/elif/else` -- no code inspects any curriculum outcome. Meanwhile
`hazard_survival_gate_passed` *varies* (false on 5 of 6 trained cells) and is read by no criterion. The
pre-queue smoke had already returned `G0_ON=0` and was recorded as the gate "correctly" routing
readiness_fail -- the same observation, the opposite conclusion.

`claim_ids` is `[]` (tags neither ARC-030 nor MECH-307) and `queue_id` is absent -- a hand-recovered run
that bypassed the spool (`7141d4c9190`).

---

## 3. Mechanical pre-routing checks (Step 7b) -- 5 fires, all disposed

The checks caught something the draft had missed, and it is the sharpest finding in the cluster.

- **C2 on 849 and 865 -- ACTED ON.** Substrate entry `Q081-REACH-CHECK-PAIR-SPECIFIC` (status
  `implemented`) already covers this gap, and its `implementation_hint` instructs verbatim:
  *"Do NOT flip another blanket flag: build a cheap low-episode pre-flight reach probe that asserts at
  least one arm moves."* **849 and 865 ARE that probe** -- and they omit precisely that assertion (the
  manipulated arm's preservation report is computed and discarded, `q081_pair_reach_check.py:538`;
  `dropped_ticks` is zero in every cell) while hardcoding the blanket flag the entry warns against, which
  the readiness control then reads. Routing corrected from `none` to **`amend`** on that entry.
  **This is a second dropped handoff in this batch**, structurally identical to the 983a -> 1036 one
  recorded in the sibling V3-EXQ-1036 artifact.
- **C2 on 864a -- DISMISSED WITH REASON.** `sd_waking_confidence_inflation_headroom` is an rv-*floor
  mechanism* repair; 864a's defect is analysis-layer blindness over correctly-collected data. Different
  gap. One connection flagged for governance: the unexamined post-reset rv dip-and-recovery *is* dynamics
  of the rv floor, so the owed re-analysis may produce evidence bearing on that entry.
- **C7 on 852 and 864a -- ACCEPTED AS EXPECTED-BY-DESIGN, RECORDED.** `tick0_f_raw` (852) and
  `wci_symmetric_rv_ref_after_training` (864a) are bit-identical across arms. Both are the *unmanipulated*
  half of their comparison, so this is expected -- recorded rather than left silent because for 852 it
  corroborates the tautology: the arm manipulation provably never moved the channel C2 compares against.

C1/C3 applied and did not fire. C5 was inapplicable (no sibling `.md` at check time).

---

## 4. Re-derive brake -- Q-081 is already at threshold

Q-081 stands at **2 counting ceiling autopsies** (`v3_exq_824a` via `failure_autopsy_2026-07-28-sweep.json`;
`v3_exq_838` via `failure_autopsy_v3-exq-838_2026-07-29.json`), which **meets** the default
`RE_DERIVE_BRAKE_THRESHOLD` of 2. **Both 849 and 865 ran after those autopsies were filed**
(2026-07-28/29 vs 2026-08-01).

Neither of this artifact's Q-081 targets adds to that count: both are stamped `standard` with
instrument-defect notes and owe no substrate *build*, so R3 clause 2 excludes them. Flagged for
governance: a further Q-081 probe at the same granularity is already brake-gated, and the correct next
step is **instrument repair** -- making the probe capable of detecting a lever at all -- which is a
different question from re-testing the claim.

SD-076 stands at 0 ceiling hits across 6 autopsy targets.

---

## 5. Learning extracted

1. **Before queuing, demonstrate that each load-bearing criterion can produce BOTH outcomes.** Four of
   five here could not, and in three cases the driver's own source says so (an exemption list, a
   "trivially 1.0 by construction" comment, a contract test).
2. **A readiness control must not be computed from values the driver itself just set.** 849/865 read back
   their own hardcoded flags; 852 reports its own declared-unfailable exemption as a non-degeneracy flag.
3. **Compute a criterion's value at perfect play before running it.** 899's ceiling was fixed by the
   environment (5 resources x 30 episodes) and knowable in advance.
4. **A rate DV with an environment-capped numerator and a survival-driven denominator rewards early
   death.** Check the ordering against a random control that dies: if RANDOM wins, the metric is inverted.
5. **An experiment that collects trajectories and decides from endpoint scalars has not tested the
   trajectory.** Require at least one load-bearing criterion to READ the array the run was built to collect.
6. **A probe must assert that the mechanism it probes is live before reporting a negative.** A null from a
   probe whose gate object is `None` is a statement about the config, not the substrate. Where a driver
   compares gated against raw, equality across 100% of snapshots is a free positive control.
7. **A self-route label emitted by elimination from an `if/elif/else`, with no code inspecting the
   condition it names, will confidently misattribute the cause.**
8. **Where a predecessor was already autopsied for a test-design defect, diff the successor's criteria
   architecture against that finding before queuing.** 864a inherited 864's unchanged.
9. **Dropped handoffs are a recurring failure mode in this corpus, not a one-off.** This batch contains
   two independent instances (Q081-REACH-CHECK-PAIR-SPECIFIC -> 849/865; 983a -> 1036). In both, a prior
   confirmed artifact specified the exact guard, and the successor omitted it.

---

## 6. Routing (user-confirmed at the Step 8 gate, 2026-09-17)

| Run | Routing | Substrate action |
|---|---|---|
| V3-EXQ-849 | `implement-substrate` | **amend** `Q081-REACH-CHECK-PAIR-SPECIFIC` |
| V3-EXQ-865 | `implement-substrate` | **amend** `Q081-REACH-CHECK-PAIR-SPECIFIC` |
| V3-EXQ-852 | `implement-substrate` | **create** `e3-traj-components-per-candidate-overwrite`, severity `corrupting` |
| V3-EXQ-864a | `queue-experiment` | none -- **re-analysis of the banked pack first**, plus a re-queue |
| V3-EXQ-899 | `implement-substrate` | **create** `g0-readiness-gate-competence-inverted-dv`, severity `corrupting` |

All five stamped `recommended_evidence_direction: non_contributory` and
`recommended_epistemic_category: standard` (the enum-compliant spelling of "no category applies"); the
failure modes live in the note fields. `recommended_diagnostic_evidence_adjudicated: true` is set for
Q-081 and SD-076, the two tagged claims.

**Open question surfaced for `/governance`, not decided here:** whether the readiness/pre-flight family
needs a standing structural check -- that at least one load-bearing criterion be demonstrated capable of
both outcomes before a run is queued, and that a readiness control not be computed from values the driver
itself set. Five instances in one eight-day window is the argument for it; one authoring window is the
argument against generalising too fast.

**Not chipped from here.** Per CLAUDE.md, an autopsy does not `spawn_task` its own routing's follow-on --
the routing is a proposal until `/governance` Step 2b ratifies it, and governance chips it.
