---
status: candidate
status_asof: 2026-07-19
status_claim: SD-074
---

# SD-074: probe.trained_enough_agent_warmup

**Claim ID:** SD-074
**Subject:** probe.trained_enough_agent_warmup
**Registered:** 2026-07-18
**Status:** IMPLEMENTED 2026-07-18
**Depends on:** none unresolved (composes landed harness modules only -- see Solution)
**Blocks:** MECH-063 sub-claim (i); the 2x2 read-only control-plane telemetry-probe family
(V3-EXQ-777 / 777a lineage)
**Routed by:** `evidence/planning/failure_autopsy_MECH-063-777a-779a-cluster_2026-07-18.json`
(`targets[0]`), which fired the re-derive brake on the 777 lineage

## Problem

The 2x2 read-only telemetry-probe family measures gain/bias regulators -- MECH-320
`tonic_vigor` score-bias and MECH-313 `noise_floor` temperature -- on the E3 pre-commit
softmax while running an **untrained** agent.

A regulator that *modulates* a distribution is unobservable when that distribution has no
dynamic range. V3-EXQ-777a quantified this precisely:

| quantity | V3-EXQ-777a |
|---|---|
| seeds with `D_action_mass_mean` at ceiling (>= 0.95) | 7 of 14 |
| seeds at floor (<= 0.05) | 2 of 14 |
| **informative-seed yield** | **4 of 14 (28.6%)** |
| `corr(distance of D from saturation, norm_v_score)` | **0.884** |
| median magnitude asymmetry `v_temp / v_score` | 8.1x |

The 0.884 correlation is the quantitative statement of the dependency: the score axis's
*measurable authority* is very largely determined by how far the action-value mass sits
from its 0/1 bounds. Where `D` is pinned, the score-bias lever has nothing to act on, its
effect vector collapses toward zero, and the angle between a large temperature vector and
a near-zero score vector becomes numerically ill-conditioned.

The consequence is a power ceiling, not a bad reading. At the observed effect size and
dispersion the design needs **~51 informative seeds**; at a 28.6% yield that is ~177 raw
seeds and ~31 h. Infeasible.

**This is a substrate gap, not a sampling defect.** V3-EXQ-777a's sample-driven stopping
(the F1 fix) worked perfectly -- all 56 cells reached 250 fresh E3 selections, every cell
stopped on `floors_met`, `starved_cells` empty -- and the saturation rate barely moved from
its starved predecessor V3-EXQ-777 (80% of 5). Saturation is a property of an untrained
agent's degenerate action-value distribution: either one candidate dominates (`D -> 1`) or
the scores are flat (`D -> 0`). It is invariant to how long the cell is sampled.

Note also what did NOT fail. C1 did not fail on collinearity: `mean_sin_angle` 0.5454
**exceeds** the 0.500 margin and `c1_seed_count` PASSED. The best-conditioned seed (17;
`D` 0.497, the single genuinely mid-range seed) gave `sin_angle` **0.9883** -- near-perfect
orthogonality. Where the instrument can see, it sees the claim. MECH-063 sub-claim (i) is
**untested**, not weakened.

## Solution

A warmup/checkpoint stage that brings the agent to a non-degenerate action-value landscape
**before** telemetry collection begins, and records the realised per-seed saturation
distribution so informative yield is **auditable rather than inferred**.

Implemented as `ree-v3/experiments/_lib/probe_warmup.py`. This is **training-regime
substrate enrichment for the probe harness** -- the same class as the V3-EXQ-603c precedent
-- and explicitly **not** a `ree_core` mechanism change. Nothing under `ree_core/` is
touched, no config default moves, and no existing script imports the module, so backward
compatibility is total by construction.

It **composes landed modules** rather than writing a fourth training loop:

| reused | role |
|---|---|
| `experiments/_lib/goal_pipeline_tier1.warmup_train` | the canonical StepHarness-coupled warmup (Adam over `e1`, `e2.world_transition` + `e2.world_action_encoder`, `e3.harm_eval_head`, `latent_stack`) |
| `experiments/_lib/baselines/maturation_curriculum` | the atomic checkpoint-cache discipline (`os.replace`; key re-verified on load; agent rebuilt on both paths so RNG consumption is identical hit-vs-miss) |
| `experiments/_lib/sample_driven_rollout` | sample-driven stopping for the de-saturation read (the F1 fix), so a short-lived agent in a hazard-terminating env cannot return a handful of samples and a misleading mean |

### Public API

```python
WarmupRecipe(num_episodes, steps_per_episode=300, regime="target_env",
             probe_selections=120, probe_max_env_steps=4000, probe_max_episodes=40)

warm_agent(agent, env, *, seed, recipe, env_kwargs, label="",
           cache_dir=None, logger=print, measure=True) -> WarmupOutcome

measure_action_mass(...) -> dict        # read-only D_action_mass probe
saturation_summary(outcomes) -> dict    # the auditable yield record
assert_state_dict_shareable(agents, labels)   # cross-arm sharing guard
assert_any_informative(outcomes)              # raises only if NOTHING de-saturated
reapply_candidate_capture(agent) -> dict      # re-install the candidate capture
```

`D_SAT_LOW = 0.05` / `D_SAT_HIGH = 0.95` are deliberately **identical** to V3-EXQ-777a's
constants (script:246-247) so this substrate's success criterion is denominated in the same
units as the failure record that motivated it. They must not be retuned to make a warmup
look better -- that would silently move the goalposts the autopsy set.

### Design decisions (user-confirmed 2026-07-18)

1. **Record, do not abort.** A seed that stays saturated is reported (`saturated=True`) with
   its realised mean; the *consumer* decides whether to drop it. The autopsy explicitly asks
   for the realised saturation distribution to be recorded, and aborting would discard
   exactly that. `assert_any_informative()` covers the one case worth failing loudly on --
   zero seeds de-saturated, i.e. the warmup provably did nothing.
2. **Target env only, budget-swept.** Warmup runs on the same env the probe measures in,
   with `num_episodes` an explicit swept parameter. No 603c-style easy-env curriculum by
   default: it would add a second env as a confound before the de-saturation question is
   even answered. `regime="curriculum"` raises rather than silently doing something else.

### Three hazards defended against

**H1 -- `e3._running_variance` is not in `state_dict`.** It is a plain Python float
(`ree_core/predictors/e3_selector.py:291`), not a `register_buffer`, and it feeds
`commit_variance` (`e3_selector.py:2703`) -- directly upstream of the very probs
distribution `D_action_mass` measures. A naive `state_dict`-only cache would make cache-HIT
and cache-MISS agents differ in commit behaviour, silently. The blob therefore carries the
declared non-buffer E3 scalars explicitly and asserts the round trip.

*Measured 2026-07-18:* fresh agent 0.500 vs warmed 0.0092 -- a ~54x drift that `state_dict`
alone would have discarded.

**H2 -- per-seed checkpoint sharing across arms.** The 2x2's arms differ only in
`use_tonic_vigor` / `use_noise_floor`, and both regulators are documented "no learned
parameters, no nn.Module inheritance" (`policy/tonic_vigor.py:225`,
`policy/noise_floor.py:129`), so they contribute zero `state_dict` keys. One warmed
checkpoint per seed therefore loads into all four arms -- which is what makes the 2x2 clean:
arms differ *only* in regulator scalars at the `e3.select()` call site.
`assert_state_dict_shareable()` **asserts** this rather than assuming it, so a future arm
that flips a flag which *does* construct a module fails loudly instead of silently leaving a
module at random init.

*Measured 2026-07-18:* all four arms share an identical 194-key `state_dict` with both
regulators live.

**H3 -- the consumer's `generate_trajectories` monkeypatch is instance-level.** It is not
part of `state_dict`, so a probe that captures candidates that way (777a:484-491) must
re-apply it *after* `load_state_dict`. If it is lost, every `observe()` returns `None`, the
cell yields zero samples, and the run self-routes to `sample_starvation_requeue` -- i.e. a
lost patch **masquerades as a sampling bug**, the exact misdiagnosis this lineage has
already made twice. `reapply_candidate_capture()` exists so the consumer cannot forget.

### Non-destructive measurement

`measure_action_mass` snapshots and restores both the full `state_dict` and the declared
non-buffer scalars. `torch.no_grad()` + `agent.eval()` stop *gradient* updates but not the
two ways this agent carries state forward while merely being stepped: plain-Python
accumulators (`_running_variance` drifted 0.001839 -> 0.001855 over a 25-selection read) and
**registered buffers** (the three-factor plasticity / eligibility traces at
`e3_selector.py:373-462`, updated in place under `no_grad`; two agents identical at load
diverged by `max |dw| = 2.5e-01` after reads of different lengths). Without the restore, the
"read-only" probe would perturb the distribution it measures and `measure=True` would hand
back a different agent than `measure=False`. With it, the round trip is exact
(`max |dw| = 0.000e+00`, verified).

## What This SD Enables

- **MECH-063 sub-claim (i)** -- the orthogonal-control-axes question (MECH-320 score-bias vs
  MECH-313 temperature on the E3 softmax) becomes *askable* at feasible compute. The
  re-derive brake refuses any further iteration of the 777 probe against an untrained agent
  until this substrate exists.
- Any future read-only control-plane telemetry probe measuring a **gain or bias regulator**,
  which faces the same dynamic-range prerequisite by construction.

## Not repaired here (consumer-side, deliberately)

V3-EXQ-777a's `c1_robust` bar is `(mean_sin - pstdev_sin) > MARGIN` (script:697; `pstdev` at
:541). A **population** dispersion does not shrink with `n`, so that bar is unreachable at
any sample size, and it conflates seed-to-seed dispersion with measurement noise (the line
comment reads "effect exceeds its own noise", which is a standard-error intent). Whoever
authors the successor experiment must re-express it against a standard error.

This SD cannot fix a criterion it does not own -- and the autopsy is explicit that repairing
the bar is **necessary but not sufficient**: even at `n=51` informative seeds the binding
constraint was always the *yield*, which is what this SD moves.

## Biological grounding

LC-NE tonic vs phasic modes (Aston-Jones & Cohen adaptive gain theory); DA tonic/phasic
(Grace) as a second instance of the class. The autopsy's four-layer diagnosis records the
biological reference as **clear** and the prerequisites as **present** -- the failure does
not match a missing-dependency signature.

The dependency this SD supplies is itself biological: *a gain/bias regulator is only
observable when the distribution it modulates has dynamic range.* In brains that range is
supplied by a trained, non-degenerate action-value landscape; in the probe it was absent
because the agent was untrained. Per the autopsy this is "a genuine prerequisite discovered
by the FAIL, not a falsification".

## Phased training

**Required.** The consumer probe becomes P0 (warmup) -> P2 (frozen read-only telemetry).
There is no P1 head-training stage, so the EXQ-166b/c/d joint-training head-collapse mode
does not arise -- but the frozen-measurement boundary is mandatory: telemetry must be
collected on a non-training agent, which is why `measure_action_mass` runs under
`no_grad` + `eval` and restores all mutated state.

## MECH-094

**N/A.** Warmup is waking-only gradient training. It runs no simulation, no replay, and
writes nothing to memory, so the `hypothesis_tag=True` requirement does not arise.

## Related Claims

- **MECH-063** -- tonic/phasic control-axis dissociation (the blocked claim; sub-claim (i))
- **MECH-320** -- `tonic_vigor` capacity-to-action-bias (the score axis under test)
- **MECH-313** -- stochastic noise-floor regulator (the temperature axis under test)
- **ARC-066** -- `tonic_vigor_coupling` (MECH-320's parent)
- **SD-070** -- `latent.zworld_p0_anticollapse_recipe`; a sibling training-recipe SD, and a
  reminder that a P0 which trains the wrong thing can *collapse* a representation rather
  than enrich it. Any budget sweep here should watch for the same signature.
