# SD-084: e3.persistent_committed_program_handle

**Claim ID:** SD-084
**Subject:** e3.persistent_committed_program_handle
**Status:** IMPLEMENTED
**Registered:** 2026-07-29
**Depends on:** MECH-321, ARC-070, ARC-071, MECH-288
**Blocks:** any measurement of MECH-321's R4 mid-execution phase

## Problem

MECH-321's R4 second phase -- the **mid-execution** re-evaluation of the
REMAINING, unexecuted content of an already-committed chunk trajectory -- has
**never executed in any experiment**, and could not, under the standard driver
loop. It is not rare; it is structurally unreachable.

The hook lives in `REEAgent.select_action` (`ree_core/agent.py`) behind a
seven-way gate conjunction. Gate (4) requires
`e3._committed_trajectory is not None`. But:

- The **last statement** of `E3Selector.post_action_update`
  (`ree_core/predictors/e3_selector.py`) is an unconditional
  `self._committed_trajectory = None`.
- `REEAgent.update_residue` calls `post_action_update`, and every standard
  driver calls `agent.update_residue(...)` on **every** step, immediately after
  `agent.select_action(...)`.
- The hook needs a trajectory committed on a **previous** tick, since it
  re-evaluates unexecuted remainder. Every previous tick ends by destroying it.
- It cannot be set earlier within the same call either: the sole setter is
  `E3Selector.select` under `if committed:`, and both in-`select_action`
  `e3.select()` call sites are **after** the hook, while the other selection
  path `_e3_tick` is invoked outside `select_action` entirely.

**Empirical confirmation.** V3-EXQ-830 recorded
`decomp_n_evaluated_midexec = 0` in **all 10 cells** (5 seeds x 2 arms) against
`decomp_n_evaluated_precommit` of 1862-2618 per cell. Decomposition demonstrably
fired pre-commit; the mid-execution phase never occurred once.

Full diagnosis:
`evidence/planning/failure_autopsy_V3-EXQ-830_2026-07-29.md` section 3.

**Why it is a missing-dependency signature, not evidence against MECH-321.** In
brains, a committed motor program has a *persistent representation* that outlives
the moment of commitment -- and that persistence is what mid-flight monitoring
acts upon (supplementary/pre-SMA and dorsomedial frontal ongoing-action
monitoring, with the basal-ganglia stop pathway providing the abort).
REE has the **monitor** (the hook, correctly written and contract-covered) but
not the **persistent program representation** the monitor requires. The mechanism
has never had the substrate it needs in order to express itself.

## Solution

A persistent committed-program handle on `E3Selector`, mirroring the existing
`_closure_committed_trajectory` precedent -- which was built for exactly this
reason, and whose docstring already states the property: *"Unlike
`_committed_trajectory` it is NOT torn down by post_action_update -- it persists
across ticks."*

```python
# e3_selector.py -- declaration
self._persistent_committed_trajectory: Optional[Trajectory] = None

# e3_selector.py -- SET at commit entry, alongside the F-driven handle
if committed:
    self._committed_trajectory = selected_trajectory
    self._persistent_committed_trajectory = selected_trajectory   # SD-084

# agent.py -- gate (4) reads the UNION
_mid_traj = self.e3._committed_trajectory
if _mid_traj is None and getattr(
    self.config, "use_persistent_committed_program_handle", False
):
    _mid_traj = self.e3._persistent_committed_trajectory
```

**Config:** `REEConfig.use_persistent_committed_program_handle` (default
`False`). **Three** wiring sites -- the field, the `from_dims` signature, and the
`from_dims` assignment. No sub-config mirror: the consumer is `REEAgent`, which
reads the top-level `REEConfig` off `self.config`. (Adding a mirror by analogy
with `use_decomposition_scale_resolved_probe` would create a field nothing
reads; the neighbouring `..._midexec` flag documents the same decision.)

**The setter is deliberately UNGATED.** `E3Selector` holds an `E3Config`, not the
top-level `REEConfig` where the flag lives, so gating the setter would require a
fourth wiring site. Storing a reference that nothing reads is output-neutral --
the established in-file precedent is `_fp_chosen_world_endpoint` /
`last_raw_scores`, *"stored unconditionally ... output-neutral (bit-identical)"*.
Only the **consumer** is flag-gated.

### Liveness: an invariant, not a list of clear sites

The handle is reaped in `REEAgent.select_action`, immediately before the hook:

```python
if not self.beta_gate.is_elevated:
    self.e3._persistent_committed_trajectory = None
```

**This is the part that is easy to get wrong, and the reason a site list is not
enough.** `agent.py` has **ten** `beta_gate.release()` sites and only **five**
clear `_committed_trajectory`. The other five do not need to -- because
`post_action_update` tears it down every tick regardless. This handle removes
exactly that backstop. Clearing only at the five documented de-commit sites would
therefore strand a stale trajectory on, among others, the MECH-091 safety release
and the E3-tick non-commit release; gate (2) (`beta_gate.is_elevated`) would then
re-open on a **later, unrelated** commit with a dead program still installed, and
the hook would fire against a program that is no longer running.

A handle outliving beta elevation is by definition dead, so the invariant covers
all ten paths by construction. The six explicit clears (the five de-commit sites
plus `reset()`) are **kept alongside** it for same-tick observability and
idiom-match with the neighbouring `_closure_committed_trajectory` teardown; they
are redundant with the reap, not load-bearing.

**Known interaction.** The natural-commit latch hold re-asserts beta *after* the
hook, so a handle reaped on a beta-down tick is not resurrected by that
re-assert. This is correct: the F-driven program has genuinely ended,
`_committed_trajectory` is `None` there too, and the stepping path already falls
back. `use_natural_commit_latch_hold` is default-off in any case.

### Backward compatibility

With the flag off, gate (4) reads `self.e3._committed_trajectory` exactly as
before and remains structurally unsatisfiable -- the V3-EXQ-830 null is
reproduced exactly. The only OFF-path deltas are two attribute writes that
nothing reads. **Bit-identical.**

### NOT a pure diagnostic -- behaviour changes when ON

A reachable mid-execution hook can newly reach `boundary.fired`, which feeds
MECH-321's R1 OR trigger, and a mid-execution fire **releases the commit latch**,
**aborting the remaining macro**. Agents running with this flag on will take
different action sequences from agents running with it off. It must not be
enabled in an arm intended to be behaviourally identical to a default-path
control. This is stated in the config field docstring.

### MECH-094

**Not applicable.** `select_action` is the waking path (`simulation_mode=False`
at every neighbouring site), and the handle is a reference to an already-committed
waking trajectory. There is no replay, simulation, or memory-write surface, so
no `hypothesis_tag` obligation arises.

### Cost

The handle retains one `Trajectory` (and any autograd graph on it) across ticks
rather than freeing it each tick. Bounded at one trajectory, and
`_closure_committed_trajectory` already ships with exactly this property.

## Architecture Context

Two subsystems, each internally correct, contradicting each other in the seam:
E3's per-tick commitment teardown, and a hook requiring cross-tick persistence.
The autopsy classifies this `competence_implementation_gap` -- deliberately **not**
`substrate_ceiling`, since nothing was tested and found wanting; the mechanism was
never reachable.

## What This SD Enables

- MECH-321's R4 mid-execution phase becomes **measurable for the first time**.
- `use_decomposition_scale_resolved_probe_midexec` (ree-v3 `aaf5caac26`) becomes
  **reachable** rather than merely unexercised. It is correct and
  contract-covered but modifies a signature dict inside a block that never runs;
  it must not be read as validated by V3-EXQ-830.
- A mid-execution experiment becomes possible at all.

## Validation

Contract `ree-v3/tests/contracts/test_mech321_midexec_natural_reachability.py`
asserts the hook fires in a **real** `sense -> select_action -> env.step ->
update_residue` rollout with **no hand-injected preconditions**, and that the same
loop with the flag off yields `decomp_n_evaluated_midexec == 0`.

This is the assertion the pre-existing
`tests/contracts/test_mech321_scale_resolved_boundary.py` could not make: it
reaches the hook only by setting `fake_traj.metadata`, `agent._committed_step_idx
= 1` and calling `agent.beta_gate.elevate()` directly. That proves
reachability-in-principle behind a correct anti-vacuity guard -- and is exactly
why this defect survived. Reachability-in-practice is a different assertion.

## Related Claims

MECH-321 (R4 mid-execution phase), ARC-070 (policy decomposition), ARC-071
(policy chunking), MECH-288 (rollout-boundary detection).

**No claim status, confidence, `live_status` or `v3_pending` value is changed by
this SD.** MECH-321 remains `candidate` / `v3_pending`: this build makes its R4
half *measurable*, and measurement is what governance acts on.
