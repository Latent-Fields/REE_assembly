# MECH-091 integration observability probe -- 2026-08-22

**Status:** read-only probe result, informational. No `claims.yaml` edit, no
experiment queued, no `substrate_queue.json` entry made by this document --
per the chip brief and per the source autopsy's own note that `/governance`
ratifies an autopsy's routing before anything is spawned.

**Source of scope:** `targets[0].successor_spec.separate_probe_gated_followon`
in the V3-EXQ-944 failure autopsy (`nooarche` commit `6ee88c7a97`, ratified by
governance cycle `bold-chaum-7e245c` / `REE_assembly` `ba43c47ab9`). That note
poses two preconditions for the INTEGRATION half of MECH-091's
`what_would_answer` ("harm/goal estimates are FULLY INTEGRATED within the
following cycle") to become buildable:

> (a) a training protocol that GROUNDS E3 harm_eval with a positive-control
> grounding assertion per `agent.py:9690-9693`, or an integration readout
> built on a head this protocol does train, and (b) if goal estimates are in
> scope, the goal subsystem enabled (`goal_state_present` is false today).

This document answers (a) and (b) from source, plus a third check the chip
brief added: whether the candidate DV would be absorbed by the EXQ-131
E3-output-freeze staleness artifact.

*(Line numbers below are `ree-v3` `main` as read on 2026-08-22, `HEAD` at
probe time. The autopsy's own citation of `agent.py:9690-9693` is off by
~100 lines against this checkout -- the grounding-assertion docstring is at
`agent.py:9580-9591` here, verified by exact string match on
`"only meaningful once those heads are grounded (ARC-030 phased protocol)"`.
Treat the autopsy's line numbers as approximate; the ones below were read
directly.)*

---

## (a) Is there a training protocol that grounds E3's harm_eval?

**Yes -- twice over, and both are already-run, production-shape patterns, not
proposals.**

The grounding requirement itself is stated at `ree_core/agent.py:9580-9591`
(`actor_critic_reward`'s docstring):

> `benefit_eval` / `harm_eval` start random-init behind the ARC-030 warmup
> gate, so this signal is only meaningful once those heads are grounded
> (ARC-030 phased protocol) -- a validation using it MUST first assert
> grounding on a positive control.

Two concrete implementations of that grounding exist in `ree-v3` today:

1. **`ree_core/agent.py:10153-10180`, `compute_benefit_eval_loss`** (ARC-030 /
   MECH-112). Trains `E3.benefit_eval_head` by MSE regression against
   `benefit_exposure` (`body_state[11]`, a resource-proximity proxy field on
   `CausalGridWorldV2`). This is benefit, not harm, and it is a proxy target
   rather than the harm signal itself -- named for completeness, not as the
   grounding path for harm_eval.

2. **`experiments/v3_exq_085m_arc030_benefit_eval_e3.py:247-359,520-537`**
   (already run, not hypothetical). Maintains a running positive/negative
   buffer of `z_world` keyed on `harm_signal < 0` (`harm_buf_pos` /
   `harm_buf_neg`), trains `agent.e3.harm_eval_head` with a dedicated Adam
   optimizer via `F.mse_loss(pred_harm, target)` against a 1/0 pos/neg label
   (lines 330-359), and at eval time computes **exactly the positive-control
   grounding assertion the docstring calls for**: `harm_calibration_gap =
   harm_pos - harm_neg` (lines 528-537), i.e. does `harm_eval` separate known
   harmful `z_world` states from known non-harmful ones. This is a drop-in
   template for "assert grounding on a positive control before using the
   signal."

3. **`experiments/_lib/goal_pipeline_tier1.py:513-580`, `warmup_train`**. A
   second, independent implementation of the same idea inside the
   already-landed goal-pipeline lineage: a `harm_eval_optimizer =
   optim.Adam(agent.e3.harm_eval_head.parameters(), lr=LR_E3_HARM)` (line
   535) trained each step against `harm_target = abs(harm_signal) if
   harm_signal < 0 else 0.0` (line ~535+, harm buffer accumulation follows).
   This is the pattern MECH-091's own baseline would need to add.

**Contrast with what MECH-091's own baseline actually trains.** The lineage's
warmup, `experiments/_lib/baselines/mech091_phase_reset.py:336-362`, backs
the autopsy's characterisation exactly:

```python
loss = agent.compute_prediction_loss() + agent.compute_e2_loss()
```

No `E3` optimizer at all -- `compute_e2_loss` trains E2's `z_self` forward
model (`predict_next_self`), not `E2_harm_s`, and nothing touches
`harm_eval_head` or `benefit_eval_head`. The docstring is candid about this:
*"No downstream head is trained on a latent in this lineage, so the
phased-training protocol reduces to P0 -> P2 (frozen)."* So on THIS driver,
today, `harm_eval` is random-init, exactly as `harm_stream_validity` in the
autopsy states. The finding is that grounding it is a known, reusable
addition (pattern 2 or 3 above), not new substrate work.

**Verdict on (a): the grounding protocol exists and is buildable by reuse.**
Nothing needs to be invented; an integration probe needs to import one of the
two existing patterns (085m's pos/neg calibration-gap pattern is the closer
fit, since it already produces the positive-control assertion as a first-class
metric rather than a training-loop side effect).

---

## (b) Is the goal subsystem enabled at all?

**Not in MECH-091's own baseline -- but this is a default, not an absence.**

`experiments/_lib/baselines/mech091_phase_reset.py:241-259` (`build_agent`)
constructs the agent via:

```python
cfg = REEConfig.from_dims(
    body_obs_dim=env.body_obs_dim, world_obs_dim=env.world_obs_dim,
    action_dim=env.action_dim, **shared_config_kwargs(),
)
cfg.heartbeat.beta_gate_bistable = BETA_GATE_BISTABLE
```

`shared_config_kwargs()` (lines 131-139) passes only `alpha_world`,
`alpha_self`, `self_dim`, `world_dim` -- no `z_goal_enabled` or any
`goal.*` kwarg. `REEConfig.from_dims`'s own signature
(`ree_core/utils/config.py:6369`) defaults `z_goal_enabled: bool = False`.
So `GoalState` is never constructed on this config, which is exactly what
V3-EXQ-944's manifest measured: `goal_state_present: false`,
`writer_defect: null`. Per `experiments/_lib/z_goal_stream.py:1-90`
(the module the autopsy's `harm_stream_validity` note is quoting),
`writer_defect: null` specifically means *"configuration rather than
defect"* -- distinguished from `writer_defect: true`, which would mean a
driver that should have called `update_z_goal` and silently didn't
(V3-EXQ-626 / V3-EXQ-830's confirmed bug). `ticks_total: 0` follows
mechanically from `goal_state_present: false`: there is no `GoalState` object
for any tick to be counted against.

**The subsystem itself is not missing from the substrate.** A canonical,
already-used enablement path exists at `ree_core/utils/config.py:9002-9040`,
`REEConfig.goal_stream(...)`, which sets `z_goal_enabled=True` plus the
companion bundle (`goal_weight`, `drive_weight`, `wanting_weight`,
`schema_wanting_enabled`, `use_mech307`, `use_mech295_liking_bridge`, etc.)
in one call, and is exercised by the whole ARC-030 / goal-pipeline
experiment family (`v3_exq_085*`, `v3_exq_899_arc030_mech307_g0_readiness.py`,
and others). `StepHarness` (used by `mech091_phase_reset.py:343,386`) is
independently documented (`z_goal_stream.py`'s own module docstring) as
pinning the `update_z_goal` call as an invariant -- i.e. once `z_goal_enabled`
is turned on, the harness this lineage already uses cannot reproduce the
V3-EXQ-626/830 writer-defect bug; `writer_calls` would be nonzero by
construction.

**Verdict on (b): buildable by configuration, not blocked on substrate.**
Turning the goal subsystem on for a probe is a `REEConfig.goal_stream(...)`
call (or a narrower hand-set `z_goal_enabled=True` plus the specific
companion flags a probe actually needs) -- not new code. The honest caveat is
scope, not feasibility: `goal_stream()` is a *bundle* (MECH-307 conjunction,
schema-wanting, MECH-295 liking bridge all default True inside it), so
"enable the goal subsystem" is not a one-flag change if the probe wants to
avoid also silently pulling in three other mechanisms' worth of confound.

---

## (c) Is the candidate DV absorbed by the EXQ-131 E3-output-freeze staleness artifact?

**Not for what V3-EXQ-944 measured; yes as a hazard for what a successor's
INTEGRATION DV would measure -- and it is a guardable hazard, not a blocker.**

The artifact: `E3TrajectorySelector` populates `last_score_diagnostics` /
`last_channel_terms` / `last_scores` / `last_raw_scores` / `last_selected_idx`
etc. **only inside `select()`**, which itself only runs on an E3 tick
(`heartbeat.e3_steps_per_tick`, default 10 -- `ree_core/utils/config.py:2776`).
Between ticks these attributes latch at their previous value. This is
documented and enforced by a static lint,
`validate_experiments.e3_diagnostics_staleness_lint`
(`ree-v3/validate_experiments.py:2033-2130`), which exists precisely because a
driver that reads these fields once per env step without a
clear-before-select / `e3_tick`-guard / identity-freshness guard
pseudo-replicates one selection as many independent rows (measured 9.0x
inflation on a real prior run).

MECH-091's own C3 criterion (`straddle_frac`, computed at
`mech091_phase_reset.py:378-473`) is **not exposed to this**: it is built
purely from salient-event step indices vs. tick-boundary step indices
(`ticks[ep]` bookkeeping around lines 403-413), never from
`E3TrajectorySelector`'s latched `last_*` attributes. So the TIMING half of
`what_would_answer`, as measured by V3-EXQ-944, is clean of this artifact --
consistent with the autopsy treating C1-C4 as valid measurements that simply
didn't gate on a broken precondition.

A future **INTEGRATION** DV is a different story by construction: "harm/goal
estimates are fully integrated within the following cycle" is a claim about
`E3.harm_eval` / `E3.benefit_eval` (or their `last_score_diagnostics`
composites) becoming current *after* a salient event, which is exactly the
latched-attribute shape the lint exists to catch. Reading those values on
every env step (the natural first draft of such a probe) would either report
a frozen pre-event value as "not yet integrated" for up to
`e3_steps_per_tick - 1` steps regardless of any real integration dynamic, or
silently pseudo-replicate one tick's value across many rows. The fix is
already characterised by the lint's own documented obligations (any of:
clear-before-select, an `e3_tick` guard, a direct `e3.select()` call site, or
an identity-freshness guard via `id(...)`) -- this is implementation
discipline, not an open question.

---

## Recommendation: **BUILD** (as a small, staged probe -- not the full
compound in one shot)

All three checks resolve to "known and buildable," which is what makes this a
`puzzle (known rules)` rather than a `mystery` or an `aleatoric` unknown: the
missing facts were sitting in already-committed, already-run code
(V3-EXQ-085m, `goal_pipeline_tier1.py`, `REEConfig.goal_stream`,
`e3_diagnostics_staleness_lint`), not behind an experiment that needed to be
run first. Concretely, a successor probe is:

1. Ground `harm_eval` by importing the V3-EXQ-085m pos/neg buffer +
   `harm_calibration_gap` pattern (the closer fit of the two grounding
   implementations, since it *is* the positive-control assertion rather than
   an implicit side effect of training).
2. Sample the integration readout only on a fresh E3 tick (any of the four
   `e3_diagnostics_staleness_lint`-sanctioned guards), never per env step.
3. Treat goal-subsystem enablement as a **separate**, later step behind its
   own decision, not bundled into step 1 -- see the counter-argument below.

**Honest counter-argument, stated plainly.** "Buildable" is not the same as
"cheap" or "well-isolated," and the autopsy's own framing --
*"complex (probe-gated) ... needs a cheap observability probe first"* --
is in tension with what a fully-scoped version of this actually requires:

- The 085m grounding pattern was built and run inside a **different**
  experiment lineage (the full ARC-030 goal-pipeline harness), not the
  minimal `mech091_phase_reset.py` P0-only baseline. Porting it is not
  copy-paste: it needs a second optimizer, a pos/neg buffer, and a
  per-step training call added to a baseline whose whole design point
  (per its own docstring) is to keep the substrate-operating config
  identical across arms so the reset-policy manipulation stays the only
  difference. Adding a harm-grounding side-loop is a second manipulation
  living in the same run, and the autopsy's own `must_not` clause for the
  *timing* successor (944a) --*"Bolt an INTEGRATION DV onto this run"* --
  reads as a general caution against exactly this kind of compounding, not
  a restriction specific to 944a.
- `REEConfig.goal_stream()` is a bundle, not a flag (MECH-307 conjunction +
  schema-wanting + MECH-295 liking bridge, all default True). Turning it on
  for an integration probe pulls in three more mechanisms' worth of
  confound unless each is deliberately re-disabled, which is itself a
  design decision the successor_spec does not currently make.
- The INTEGRATION claim this would produce evidence for is a diagnostic
  half of MECH-091's `what_would_answer`, not itself gating a specific
  registered claim the way the TIMING half does -- so the probe's payoff is
  real but modest, and the honest framing is "worth doing cheaply," not
  "urgent."

**Net:** BUILD, but as two separable steps -- (1) harm-only grounding +
staleness-guarded integration readout, no goal subsystem, is the actual
"cheap observability probe"; (2) goal-subsystem inclusion is a second,
independently-scoped decision to make only if step 1's result makes it
worth the added confound surface. Recommend `/governance` ratify step 1
alone as the next `/queue-experiment` follow-on; defer step 2 pending
step 1's result, rather than routing both at once.

---

## Files read (primary sources, this probe)

- `ree-v3/ree_core/agent.py:9580-9591` (grounding-assertion docstring),
  `:9850` (`harm_signal` doc), `:10153-10180` (`compute_benefit_eval_loss`)
- `ree-v3/ree_core/predictors/e3_selector.py:277-360,529-533` (`harm_eval`/
  `benefit_eval` heads, ARC-030 warmup gate)
- `ree-v3/ree_core/utils/config.py:6369` (`from_dims` `z_goal_enabled`
  default), `:9002-9040` (`REEConfig.goal_stream`), `:2776`
  (`e3_steps_per_tick` default)
- `ree-v3/experiments/_lib/baselines/mech091_phase_reset.py:131-270,336-362,
  378-473` (build_agent, shared_config_kwargs, warmup, straddle_frac)
- `ree-v3/experiments/_lib/z_goal_stream.py:1-90` (goal-stream liveness
  counters, `writer_defect` semantics)
- `ree-v3/experiments/_lib/goal_pipeline_tier1.py:513-580` (`warmup_train`,
  independent harm_eval-grounding implementation)
- `ree-v3/experiments/v3_exq_085m_arc030_benefit_eval_e3.py:247-359,520-537`
  (already-run harm_eval grounding + positive-control calibration gap)
- `ree-v3/validate_experiments.py:2033-2130`
  (`e3_diagnostics_staleness_lint`)
- `REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-944_2026-08-22.json`
  (`targets[0]`, read via `git show 6ee88c7a97:...` -- not present in the
  live worktree; committed only as part of `ba43c47ab9`'s referenced source,
  the standalone autopsy artifact itself was not retained as a tracked file)
- `REE_assembly/evidence/decisions/decision_log.v1.jsonl:449` (governance
  disposition of V3-EXQ-944, session `bold-chaum-7e245c`)
