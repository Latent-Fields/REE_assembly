# V3-EXQ-884c (MECH-428 content-DV, pre-arrival credit) -- DESIGN REFUSED at `/queue-experiment` Step 4.5 (red-team BLOCKING)

**Status: NOT QUEUED. No queue entry, no coordinator row, no manifest.** The driver is parked at
`ree-v3/experiments/_scratch/v3_exq_884c_mech428_subgoal_bootstrapped_goal_seeding.py` with the
refusal in its own module docstring, following the 884a/884b convention. Four scratch probes are
kept alongside it because the measurements they carry are the durable output of this session.

- **Written:** 2026-09-16
- **Session:** `science-batch5c-20260916` (supervised Opus subagent of Metaworker Orchestrator
  `orchestrate-20260916-1305`, per-launch user decision 2026-09-16T13:36Z, continued on the
  16:13Z decision).
- **Chip:** `chip-20260914-mech428-c1-redesign-v2-attained-signature`, unclaimed (not resolved) --
  the residual it tracks is still live and is now better characterised, not discharged.
- **Red-team model:** `fable`, one pass, foreground. Verdict **BLOCKING**, four findings.
  **All four were independently re-confirmed against the driver's own source before being
  accepted**; none was taken on the reviewer's word.

---

## 1. The refusal, in one sentence

The criterion adopted to replace 884b's unpassable one is **biased positive with zero content
signal** -- the parent is an EMA built *from* the attained group, so the parent-to-attained-mean
cosine carries a self-overlap term the parent-to-non-attained-mean cosine does not, and the
label-permutation null holds the parent fixed and so never re-runs the step that makes the
observed labelling special -- and the negative control built specifically to catch that failure
was scored against the wrong partition and is silent by construction.

## 2. What this session measured (the durable output -- all of it survives the refusal)

The chip made an achievable-ceiling measurement a precondition of any redesign. Four probes, all
kept at `ree-v3/experiments/_scratch/`:

| Probe | Question | Result |
|---|---|---|
| `_probe_884c_credited_repr_ceiling.py` (batch 5b) | RAW observation space | post-arrival 0.0132/0.0182/0.0140, pre-arrival 0.0261/0.0242/0.0222, both 100th pct of own null on 3/3; waypoint-field 0.0018/0.0036/0.0023, AT-CHANCE on seed 42 |
| `_probe_884c_encoded_ceiling.py` (new) | ENCODED z_world, the 2x2 of credited tick x `alpha_world` | see table below |
| `_probe_884c_parent_level.py` (new) | PARENT-level ceiling + C0 fidelity | statistic S AT-CHANCE on 3/3; C0 = 1.000000000 / 0.999999881 / 1.000000119 |
| `_probe_884c_f1_self_overlap_check.py` (new) | is statistic T biased with NO signal? | YES -- see section 4 |

### 2a. The one finding that SURVIVES the refusal and should be carried forward

```
alpha_world  credited tick   seed 42     seed 43     seed 44
0.3 (884b)   post-arrival    AT-CHANCE   AT-CHANCE   AT-CHANCE
0.3          pre-arrival     AT-CHANCE   AT-CHANCE   AT-CHANCE
0.9          post-arrival    AT-CHANCE   SEPARATES   AT-CHANCE
0.9          pre-arrival     SEPARATES   SEPARATES   SEPARATES
                             0.002160    0.002288    0.001145
                             (p95        (p95        (p95
                              0.000799)   0.000989)   0.000558)
```

**Two levers, jointly necessary, individually insufficient.** This is a group-mean result that
never touches the parent EMA, so F1-F4 do not bear on it at all.

1. **Pre-arrival crediting** -- the chip's direction 1. Note this is available *through the real
   substrate call*: `REEAgent.notify_subgoal_attainment(ttype, child_representation=...)`
   (`ree_core/agent.py:10334`), and `GoalState.credit_subgoal_attainment`'s own docstring
   (`ree_core/goal.py:937`) states that which representation counts as the attained subgoal is
   "an experiment-design decision ... left to the call site, not baked into the substrate". So a
   successor does **not** need a substrate change for this.
2. **`alpha_world = 0.9`** -- NOT in the chip's candidate list, found by reading the substrate.
   `ree_core/latent/stack.py:1584` blends `z_world = alpha_world * z_world + (1 - alpha_world) *
   prev_state.z_world`. 884b never set it, so it ran at the `REEConfig` default **0.3**: every
   sensed z_world was 70 percent inherited from the previous tick, a temporal EMA that smears an
   attainment tick into its transit neighbours before any crediting happens.
   `stack.py:1537` calls 0.3 backward-compat only ("set alpha_world >= 0.9 to fix event
   suppression"); `config.py:80-84` says the same.

**This also corrects red-team 884b finding F4's STRONG form.** F4 held that the credited
observation carries no waypoint signature. It does: the raw post-arrival observation separates at
the 100th percentile of its own null on 3/3 seeds. The dominant loss was the **sense path**, not
the marker overwrite.

### 2b. Rejected on measurement, so no successor re-derives them

- **Chip direction 2 (credit the SD-WAYPOINT-FIELD observable).** Weakest of the three raw
  candidates and not robust across seeds (AT-CHANCE on seed 42). Not implemented.
- **Parent-level statistic S** = `1 - cos(parent_true, parent_control)`, both built by the same
  decay+credit replay at the same credit-tick positions. **AT-CHANCE on 3/3 seeds** (percentile
  78.0 / 63.0 / 86.5 of its own null). Mechanism: a resampled control parent inherits the EMA's
  effective sample size, ~`1/parent_goal_alpha` = 20, so the null's spread exceeds the achievable
  signal. **S is the statistic whose null is SOUND** -- it re-runs the parent-building step inside
  the null -- which is exactly why it reads at chance while the biased T does not.

## 3. What was built and how far it got

The driver implements: pre-arrival crediting through the real substrate call; `alpha_world=0.9`
with a `from_dims`-swallowed-kwarg assert; a null-referenced G3 (replacing the absolute floor that
884b red-team F3 showed 96 percent of random partitions cleared); a C0 fidelity control comparing
the replay to the real `agent.goal_state.z_goal_parent`; and a fourth arm `CREDIT_RANDOM_TICKS`.
It passes `validate_experiments.py --strict` and its `--dry-run` smoke cleanly.

Two genuine reproducibility bugs were caught by the smoke and are worth recording because **one
of them is inherited from 884b and is still live in the parked 884b driver**:

- `random.Random(("shuffle884b", seed))` -- a TUPLE seed, which `random.Random` rejects outright
  (`TypeError`). Present in the parked 884b file at its `parent_shuffled` construction; any
  session that resurrects 884b will hit it.
- A `hash((tag, seed))`-derived `torch.Generator` seed. `str.__hash__` is salted per process by
  `PYTHONHASHSEED`, so the permutation nulls -- and therefore the PASS/FAIL verdict -- would
  differ between two runs of the same script on identical data. Fixed here with `zlib.crc32`.

## 4. The red-team findings, all four re-confirmed against source

**F1 -- BLOCKING -- C1's statistic is biased positive with zero content signal.**
`T = cos(parent, mean(attained)) - cos(parent, mean(non_attained))`. Writing each representation
as `mu + eps_i`, the observed `parent . mean(attained)` contains a self-overlap term
`sum_{i in A} w_i ||eps_i||^2 / n_a`, because every constituent of the parent is also a member of
`mean(attained)`; `parent . mean(non_attained)` contains none. Under a label permutation that
holds the parent FIXED, those constituents spread across both permuted groups in proportion and
the term **cancels**. So `T_obs - E[T_perm] ~ S / n_a > 0` with no content signal at all.

**Independently confirmed** (`_probe_884c_f1_self_overlap_check.py`, written from scratch, no
encoder and no environment -- representations are one shared unit direction plus iid gaussian
noise, so the labels carry zero information by construction):

```
 sigma | T_obs      null_p95    pct   | C1 verdict
 0.02  | 0.000160   0.000049   100.0 | SEPARATES on  4/12 trials
 0.05  | 0.001000   0.000139   100.0 | SEPARATES on 12/12 trials
 0.10  | 0.003187   0.000881   100.0 | SEPARATES on 12/12 trials
 0.20  | 0.012278   0.004178   100.0 | SEPARATES on 12/12 trials
```

Every "SEPARATES" is a false positive. The magnitudes at sigma = 0.10 (~0.003) are the SAME ORDER
as the real parent-level measurement (0.003431 / 0.000662 / 0.001100), so **the real measurement
is fully consistent with pure self-overlap artifact and cannot be read as evidence of anything
else.** The reviewer reached the same conclusion on its own independently-written sweep.

**F2 -- BLOCKING -- the negative control cannot fire.** `_score(rand, "c2_rand")` scores the
`CREDIT_RANDOM_TICKS` arm against `row["_content_attained_reprs"]`, i.e. the ATTAINMENT partition,
rather than against that arm's own credited/uncredited partition. That arm's parent is an EMA of
non-attained representations, so by the same self-overlap term its T is **negative by
construction** (smoke: -0.000612 / -0.000110 / -0.000645). C2 therefore passes for a bookkeeping
reason, the `elif not c2_pass` branch is dead, and the one control designed to catch F1 is blind
to it.

**F3 -- CONTESTED, confirmed -- G3 gates on a representation the DV never uses.** The readiness
probe stores `z_now`, the POST-arrival latent; C1 credits and scores `prev_z`, the PRE-arrival one,
at five times the sample size. Worse, this session's own measurement (2a) says the post-arrival
statistic is AT-CHANCE on 2/3 seeds at `alpha_world=0.9`, and G3 requires every seed -- so at real
scale the run is expected, by its own numbers, to self-route `substrate_not_ready_requeue` before
any C criterion is read.

**F4 -- CONTESTED, confirmed -- the "random" control arm is not random.**
`random_tick_set = set(random_tick_order)` where `random_tick_order` is a shuffled
`range(1, n_steps+1)`: taking the set discards the shuffle, so membership is always true and the
arm credits the EARLIEST non-attainment ticks until its budget is spent. Verified:
`len(set) == 400` and every tick is a member.

## 5. Disposition, and what a successor should and should not do

**Do NOT search for a fourth parent-level statistic.** Three have now been measured. The one with
a sound null (S) reads at chance; the one that separates (T) separates on noise. The pattern is
structural, not a run of bad luck: any statistic that compares the parent to a group the parent was
built from inherits F1, and any statistic that re-runs parent-building inside its null inherits
S's variance problem.

**The live lever is the substrate's own event-integration parameters, as an INDEPENDENT VARIABLE.**
The parent EMA's effective sample size is ~`1/parent_goal_alpha` = 20 at the `GoalConfig` default,
against 60 credit events in a 400-step walk. That ratio -- not the observation, not the encoder --
is what bounds every parent-level content measurement here. A successor that sweeps
`parent_goal_alpha` / `parent_goal_decay` / event rate and asks *where the content signal becomes
measurable at all* is asking a question that can be answered; the 884 lineage's current framing is
not.

**Carry forward unconditionally:** pre-arrival crediting via `child_representation=`, and
`alpha_world = 0.9`. Both are cheap, both are established on 3/3 seeds, and neither depends on any
refuted statistic.

**Registry state.** This session was launched with `ree-v3/experiment_queue.json` and
`ree-v3/experiments` as its resources and did not hold a claim on
`REE_assembly/evidence/planning/experiment_proposals.v1.json`, so the refusal is routed to
governance by `governance_flag.py raise` (Step 2.5 STOP-GATE route 2b) rather than by a direct
registry status write. EXP-0390 is left at `status: proposed`.

## 6. Artifacts

- Parked driver: `ree-v3/experiments/_scratch/v3_exq_884c_mech428_subgoal_bootstrapped_goal_seeding.py`
- Probes: `ree-v3/experiments/_scratch/_probe_884c_encoded_ceiling.py`,
  `_probe_884c_parent_level.py`, `_probe_884c_f1_self_overlap_check.py`,
  `_probe_884c_reachcheck2.py`, and batch 5b's `_probe_884c_credited_repr_ceiling.py` /
  `_probe_884c_reachcheck.py`
- Predecessor refusal: `evidence/planning/exq884b_mech428_c1_content_dv_redteam_blocking_20260914.md`
- This document.
