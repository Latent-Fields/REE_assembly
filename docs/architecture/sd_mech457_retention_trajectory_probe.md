---
title: "SD-MECH457-RETENTION-TRAJECTORY-PROBE: experiments._lib.mech457_explorer_classes.train_a2c.probe"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 24
---

# SD-MECH457-RETENTION-TRAJECTORY-PROBE: experiments._lib.mech457_explorer_classes.train_a2c.probe

**Claim ID:** mech457_retention_trajectory_probe
**Subject:** action_learning.mid_training_competence_probe
**Status:** IMPLEMENTED
**Registered:** 2026-07-19
**Implemented:** 2026-07-19
**Depends on:** none (instrumentation only)
**Blocks:** H-retention-critic, H-retention-auxiliary-decay, H-retention-consolidation,
H-consummation-binding (all four retention legs of the `competence_floor` question)

## Problem

The `competence_floor` retention portfolio requires every leg to record the **post-installation
competence TRAJECTORY** rather than terminal competence
(`evidence/planning/mech457_retention_portfolio_2026-07-18.md` §53). Terminal-only measurement is
precisely what kept the retention deficit invisible for ten legs. V3-EXQ-780 is the worked
failure: `raw_view` reached **20.933** immediately post-BC, RL refinement eroded it to **11.667**,
and because only the terminal value was scored the run read as a null.

Before this build the substrate could not express that measurement at all:

- `train_a2c` (`experiments/_lib/mech457_explorer_classes.py`) had **no observation hook** — all
  16 optional parameters are reward/loss-shaping hooks. Its guard dict returned rolling-window
  means only, with no per-episode series and no resumable state.
- All 18 mech457 experiment scripts call `capability_eval.evaluate_seed` 1–3 times, always
  terminal.

The obvious driver-side workaround — chunk the RL budget and evaluate between segments — is
**unfaithful on two independent grounds**:

1. **Schedules restart.** `coef_schedule` / `entropy_schedule` / `bc_aux_schedule` are invoked as
   `fn(ep, n_episodes)` with `ep` the LOCAL loop index, and `warm_then_anneal` / `linear_anneal`
   compute their cutoffs from that same local `n_episodes`. N segments restart the warm-start and
   anneal N times. (`denom` does not help — it is print-progress only.) For
   `H-retention-auxiliary-decay` this is fatal in a specific way: the `bc_aux` anneal **is** the
   independent variable, so chunking would destroy the manipulation itself.
2. **Optimiser state resets.** The Adam optimiser, the `_RunningStd` reward normaliser, the
   `novelty_counter` and the rolling deques are all constructed inside the call. At a ~250-episode
   cadence over a 3000-episode run that is ~12 resets of exactly the learning dynamics whose
   erosion is the dependent variable.

## Solution

An **observation hook** on `train_a2c`, plus a config-declared cadence on
`BootstrapExplorerConfig` and a passthrough on `train_bootstrap_explorer`.

| Where | Param | Default |
|---|---|---|
| `train_a2c` | `probe_every: Optional[int]` | `None` |
| `train_a2c` | `probe_fn: Optional[Callable[[int], Dict[str, Any]]]` | `None` |
| `BootstrapExplorerConfig` | `retention_probe_every: Optional[int]` (declared in `as_slice()`) | `None` |
| `train_bootstrap_explorer` | `probe_fn` | `None` |

**Data flow.** driver builds `probe_fn` (fresh env + `rep.eval_policy()` + `evaluate_seed`) →
`train_bootstrap_explorer` → `train_a2c` → fires at the episode boundary **after** the optimiser
step, credit-replay sweep, RND update and deque appends → appends
`{"episode", "foraging_competence", ...}` → `guard["competence_trajectory"]`.

The cadence lives on the **config** (so it is fingerprint-declared) while the probe **closure** is
passed by the driver, which needs a fresh env and the eval policy — neither owned by the `_lib`
modules.

### RNG isolation (load-bearing, not defensive)

`train_a2c` snapshots and restores the torch, global-numpy and python-`random` streams around each
probe call. This was initially assessed as belt-and-braces on the reasoning that the env owns a
per-instance generator (`causal_grid_world.py:1123`) and `ActorCriticEvalPolicy` is deterministic
argmax. **That assessment was wrong and was corrected by mutation testing:** the training rollout
itself draws from the global torch stream, so an unrestored probe genuinely desynchronises
training from the same run measured without a probe. With the restore removed, trained weights
diverge; with it in place they are bit-identical.

### Half-wired is an error

Supplying `probe_every` without `probe_fn` (or vice versa) **raises**, as does a non-positive
cadence. A half-wired probe would silently return an empty `competence_trajectory` that is
indistinguishable from a genuinely flat one — the degenerate-arm-read-as-a-verdict failure the
distributional critic's raise-on-scalar-path guards against.

## Backward compatibility

Both hook params default to `None` → no call site, empty trajectory, byte-identical OFF path.
`competence_trajectory` is emitted **unconditionally** (empty when unprobed), matching the
`bc_aux_coef_first`/`_last` precedent so consumers read one stable key rather than branching on
presence.

**Fingerprint:** edits `experiments/_lib/**`, which is bound into `substrate_hash`, so pre-change
baseline arm fingerprints are correctly refused for reuse — expected, not a regression.
`as_slice()` gains one declared key for the same reason the bc_aux fields did: a probed and an
unprobed cell are not interchangeable **artifacts** (only one carries the trajectory), even though
the probe cannot change the learned result.

## Anti-alias constraint

**Instrumentation only.** This build changes no update rule, loss term, schedule or value
estimator, so it cannot contaminate the three-way retention anti-alias:

| Locus | Owner |
|---|---|
| value estimator only | `mech457_distributional_critic` (H-retention-critic) |
| update constraint only | `mech457_policy_kl_anchor` (H-retention-consolidation) |
| auxiliary persistence only | `mech457_bc_aux_schedule` (H-retention-auxiliary-decay) |

The measurement-neutrality contract (T2) is what enforces this mechanically rather than by
assertion.

## Same-statistic requirement

Consumers must report the SAME statistic the verdict routes on: unshaped `foraging_competence` via
`capability_eval.evaluate_seed`, which is what `post_bc_foraging_competence` uses and what every
reference band is denominated in (floor 1.0 / RND plateau 5.22 / lift target 13.05 / the 20.933
install positive control / BC-expert 32.72 / `local_view_greedy` 48.05 / `greedy_oracle` 57.2).

Do **not** substitute the cheaper `mean_train_forage_recent`: it is SHAPED on-policy training
forage measured under the intrinsic drive, is not comparable to those bands, and would put the
half-life on a different statistic from the criterion — the V3-EXQ-643 magnitude-vs-range mismatch
class.

## Implementation shape: hook, not mirrored loop

`experiments/_lib/mech459_probe_r.py:1-24` mirrored the training loop into a separate module
rather than adding a hook, because a default-`None` hook still changes the bytes of
`mech457_explorer_classes.py` and therefore the `arm_fingerprint` substrate hash of the then-live
780/781.

**That constraint has lapsed** — 780 and 781 are complete and autopsied
(`failure_autopsy_MECH-457-gov-fanout-1-cluster-780-781-782_2026-07-18`), and the sibling
`mech457_bc_aux_schedule` build edited `experiments/_lib/**` and recorded the resulting fingerprint
refusal as expected. The hook is preferred because a mirrored loop duplicates the update rule, and
any drift between mirror and live loop would mean the trajectory is measured on different dynamics
than the manipulation acts on — an unacceptable hazard for a retention DV specifically.

## Validation

Contracts T1–T7 in `ree-v3/tests/contracts/test_mech457_retention_trajectory_probe.py` (11 tests).
Lives in its own file rather than extending `test_mech457_bootstrap_explorer.py` because that
file's C18–C18f belong to the concurrently-developed untrained-encoder guard; matches the
`test_mech457_distributional_critic.py` precedent.

**T2 is load-bearing** and was **mutation-checked in both directions**. The first draft compared
the guard's aggregate means and passed even with the RNG restore removed — a vacuous pass, since
8 episodes of rolling-window means can coincide across two divergent runs. It now asserts on
trained policy **weights**, which fail under the same mutation, plus a non-degeneracy assertion
that training actually moved the weights.

Phased training: not applicable (no head trained). MECH-094: not applicable (no simulation or
replay memory writes).

## What This Enables

Queueing `H-retention-critic` and `H-retention-auxiliary-decay` as a pair under new EXQ numbers,
per `evidence/planning/competence_floor_reposing_2026-07-19.md` §6 — both manipulations were
already built (`8e88ffc`, `9a8dbae`) and were blocked only on this measurement.

MECH-457 stays `candidate` / `v3_pending`; INV-088 unchanged. This build promotes and demotes
nothing.

## Related Claims

MECH-457, INV-088. Question `competence_floor` in
`evidence/planning/hypothesis_space_registry.v1.json`.
