---
title: "SD-092: Cross-Level Subgoal Credit"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 20
status: candidate
status_asof: 2026-08-03
status_claim: SD-092
---

# SD-092: Cross-Level Subgoal Credit

**Claim ID:** SD-092 (substrate). Mechanism claims served: MECH-427 (`cross_level_subgoal_credit`,
maintenance-direction), MECH-428 (`subgoal_bootstrapped_goal_seeding`, formation-direction).
**Subject:** `goal.cross_level_subgoal_credit`
**Status:** PRIMITIVE + AGENT-LOOP CALL SITE IMPLEMENTED; environment-driven harness wiring
(deciding which representation to credit, and calling the hook from an actual
`experiments/` driver) still needed before EXP-0385/EXP-0390 can run — see "What this pass
delivers" and the 2026-08-02 call-site-wiring update below.
**Registered:** 2026-08-02
**Depends on:** none unresolved (MECH-217 exists as a within-level precedent, not a hard
dependency; ARC-051 already exists as the "flat" three-level VALENCE_WANTING scheme this SD adds
a distinct up-level channel alongside).
**Blocks (until steps beyond this pass land):** EXP-0385 (MECH-427), EXP-0390 (MECH-428) —
unblocked by this primitive existing and passing its own unit tests, but the experiments still
need the harness-side subgoal-attainment -> credit call site wired (see "What remains").

---

## Problem

`GoalState` (`ree_core/goal.py`) holds exactly one persistent attractor, `self._z_goal`. There is
no representation anywhere in `ree_core` of a *parent* (superordinate) goal distinct from a
*child* (subgoal), and no code path that propagates credit from one to the other.

Confirmed by direct grep (`ree_core/`, 2026-08-02): zero hits for `MECH-427`, `parent_goal`, or
any credit-propagation-to-parent logic. ARC-051's "three levels" (see its own claims.yaml notes)
all write into the **same** `VALENCE_WANTING` field on the residue field — they are three
contributors to one flat scalar, not three distinct goal-representation nodes with a channel
between them. MECH-217 (`HippocampalModule.backward_credit_sweep` /
`spread_reverse_replay_wanting`) is the nearest built precedent, but it propagates credit
**within** one representation, backward along a single trajectory's `VALENCE_WANTING` field — not
**across** a parent/child hierarchy of distinct goal nodes.

`causal_grid_world.py`'s `subgoal_mode` already emits discrete subgoal-attainment events
(`get_subgoal_state()`: `sequence_step`, `next_waypoint_idx`, `sequences_completed`), but these
feed only scalar reward-shaping (`harm_signal`/`total_benefit`) — never `GoalState`, and the
harness has no separate superordinate-goal object for an attained subgoal to credit.

**Experimental/proposal evidence:** EXP-0385 and EXP-0390 (`experiment_proposals.v1.json`) were
both marked `blocked_substrate` on exactly this gap on 2026-08-02, with the `blocked_note` on each
naming "a parent/subgoal z_goal split + an up-level credit-propagation channel" as the missing
prerequisite.

**Biological grounding:** Bandura & Schunk (1981) — decomposing a distal goal into attainable
proximal subgoals sustained motivation and mastery; the bare distal goal alone behaved
indistinguishably from no goal. The superordinate goal is maintained (MECH-427) and can even be
formed (MECH-428) through subgoal attainment, not by direct top-down seeding alone. Goal-gradient
literature (Hull 1932; Kivetz et al. 2006) supports a discrete, event-triggered credit pulse
(rather than a continuous derivative — that is MECH-426's role) at the moment of attainment.

---

## Solution

**Minimum-viable two-level representation, added to the existing `GoalState`/`GoalConfig`
pair rather than a new class hierarchy** — the two levels are: the existing `_z_goal` attractor
(read as the **subgoal/child** level, unchanged in every respect) and a new, optional
`_z_goal_parent` attractor (the **superordinate/parent** level). This mirrors the functional form
already used for the single-level attractor (`alpha_goal`/`decay_goal` EMA-pull-and-decay) rather
than importing a new mechanism, applied one level up and triggered by a discrete event instead of
a continuous benefit signal — the same "discrete-event, cross-representation, decay-scaled write"
shape MECH-217's `spread_reverse_replay_wanting` uses for its (within-level) case.

**(a) `GoalConfig` — new fields, all no-op by default:**

```python
use_hierarchical_goal_credit: bool = False   # master switch (MECH-427/428)
parent_goal_alpha: float = 0.05              # EMA pull rate per credit event (mirrors alpha_goal)
parent_goal_decay: float = 0.005             # per-update() decay of the parent attractor (mirrors decay_goal)
subgoal_credit_min: float = 0.0              # minimum credit magnitude that applies a pull
```

**(b) `GoalState.__init__` — lazily-allocated parent attractor:**

```python
self._z_goal_parent: Optional[torch.Tensor] = (
    torch.zeros(1, config.goal_dim, device=device)
    if getattr(config, "use_hierarchical_goal_credit", False) else None
)
self._parent_goal_norm_peak: float = 0.0
self._n_subgoal_credits: int = 0
```

Mirrors `IncentiveTokenBank`'s `None`-unless-enabled pattern (SD-057) — with the flag off, no
extra tensor exists and no extra branch in any hot path is taken (the branch itself is guarded on
the flag, not merely the tensor).

**(c) `GoalState.credit_subgoal_attainment(child_representation, credit=1.0)` — the up-level
credit channel (MECH-427/428's shared primitive):**

```python
def credit_subgoal_attainment(self, child_representation, credit=1.0):
    if not self.config.use_hierarchical_goal_credit:
        return {}
    if self._z_goal_parent is None:  # flag flipped after construction — lazily allocate
        self._z_goal_parent = torch.zeros_like(self._z_goal)
    if credit < self.config.subgoal_credit_min:
        return {"n_subgoal_credits": self._n_subgoal_credits, "parent_goal_norm": self.parent_goal_norm(), "credit_applied": 0.0}
    z = child_representation.detach()
    ...  # coerce to [1, goal_dim]
    a = min(1.0, self.config.parent_goal_alpha * float(credit))
    self._z_goal_parent = (1.0 - a) * self._z_goal_parent + a * z
    self._n_subgoal_credits += 1
    norm = self._z_goal_parent.norm().item()
    self._parent_goal_norm_peak = max(self._parent_goal_norm_peak, norm)
    return {"n_subgoal_credits": self._n_subgoal_credits, "parent_goal_norm": norm, "credit_applied": a}
```

`child_representation` is caller-supplied rather than implicitly `self.z_goal`, so the same
primitive serves both directions without hardcoding which representation counts as "the attained
subgoal": MECH-427 (maintenance) credits the parent from the subgoal's own settled `z_goal`/child
`z_world` once attained; MECH-428 (formation/bootstrap) is the *identical* call — the claim's own
text states the same cross-level credit does the seeding when the parent starts low. No separate
formation-mode code path is needed; MECH-428 is what happens when `credit_subgoal_attainment` is
called repeatedly against a `_z_goal_parent` starting at (or decayed back to) ~0.

**(d) `GoalState.update()` — parent decay tick**, gated identically to the rest of the flag: when
`use_hierarchical_goal_credit` and `_z_goal_parent is not None`, decay it by `parent_goal_decay`
each call, exactly mirroring the unconditional `decay_goal` decay already applied to `_z_goal`.
With the flag off this branch is never entered — `update()`'s existing behavior is untouched by
construction, not merely by an additional `if` that happens to evaluate False on every historical
call site.

**(e) Readouts:** `parent_goal_norm() -> float` (0.0 when disabled/unallocated — the `what_would_answer`
metric both EXP-0385 and EXP-0390 name), `z_goal_parent` property, `reset()` clears the parent
attractor + counters when active (per-episode state, matching the base `_z_goal` reset — the
claim text scopes this within a single onboarding/bootstrap run, not as a cross-episode store like
MECH-189's `SuperOrdinalGoalMemory`, which already exists for the cross-episode case and is
explicitly a different mechanism).

**Numerical/engineering notes (Layer 7):** the EMA-pull-and-decay form is the same one already
validated for the base single-level attractor (SD-012/GoalConfig defaults) — no new numerical
technique is introduced, only its reapplication one hierarchy level up. The one departure worth
flagging: `credit` is caller-supplied and unbounded above; `parent_goal_alpha * credit` is clamped
to `1.0` (a full-replacement pull, never an overshoot) rather than being asserted in-range, since a
future caller may want a single very-high-salience attainment event to seed the parent in one
shot (the MECH-428 "bootstrap" framing explicitly wants a fast initial rise from ~0).

---

## What this pass delivers vs. what remains

**Delivered (this pass):** the primitive above, entirely inside `ree_core/goal.py` +
`ree_core/utils/config.py`, contract-tested standalone (no `REEAgent`, no environment) exactly in
the style of `test_goalstate_forced_seed_positive_control.py`. Flag-off path is asserted
bit-identical to current `GoalState` behavior (the critical regression to prevent, since
`goal.py` is read by many consumers). Flag-on path is asserted to (i) leave the parent at zero
without any credit call, (ii) raise `parent_goal_norm()` measurably above zero on a credit call
from a zero start (the MECH-428 bootstrap/seeding shape), (iii) raise it further on repeated
credit calls toward the child representation (the MECH-427 maintenance shape), (iv) decay between
credit events, and (v) leave the base `_z_goal`/`goal_norm()` numerically untouched by any
parent-level activity (the two attractors are independent state).

**NOT done this pass, deliberately** (mirrors the SD-091 precedent — build the self-contained
primitive first, defer live-agent-loop wiring):

1. ~~**No call site.**~~ **DONE 2026-08-02** (call-site-wiring follow-up chip). Added
   `REEAgent.notify_subgoal_attainment(transition_type, child_representation=None, credit=1.0)`,
   mirroring the `notify_env_completion` (SD-034) convention exactly: an explicit hook the
   *experiment harness* calls right after `env.step()`, passing `info["transition_type"]`. No-op
   (`{}`) when `self.goal_state is None`, when `transition_type` is not `"waypoint"` /
   `"sequence_complete"`, or when `use_hierarchical_goal_credit` is `False` (that gate lives
   solely in `credit_subgoal_attainment` itself, one source of truth). `child_representation`
   defaults to the current latent's `z_world` when not supplied, but the caller may override it
   — this keeps the representation choice an experiment-design decision, not a substrate one, per
   item 2 below. See `ree_core/agent.py` (`notify_subgoal_attainment`, next to
   `notify_env_completion`) and `tests/contracts/test_sd092_notify_subgoal_attainment.py`
   (contracts C1-C6: no-goal-state no-op, flag-off no-op, non-attainment-transition no-op,
   flag-on credits the parent, default-vs-explicit `child_representation`).
2. **No environment wiring yet, and no experiment driver calls the new hook yet.**
   `causal_grid_world.py`'s `subgoal_mode` waypoint/sequence-complete events are not
   *automatically* connected to `credit_subgoal_attainment()` — by design, matching the
   `notify_env_completion` precedent: the environment stays agnostic of `GoalState`, and it is
   the harness driver (an `experiments/` script) that reads `info["transition_type"]` off
   `env.step()`'s return and calls `agent.notify_subgoal_attainment(info["transition_type"])`.
   EXP-0385/EXP-0390's own designs (a matched ATTAINED vs NO-ATTAINMENT trajectory contrast, and
   a 3-arm NO-SUBGOAL / SUBGOAL-BOOTSTRAP / FORCED-SEED harness respectively) still need that
   driver-side call added, and deciding *which* attained-subgoal representation to pass as
   `child_representation` (the env's raw waypoint `z_world`? the agent's own settled
   child-level `z_goal` at the moment of attainment? — the hook's default is the current
   latent's `z_world`, but this is a convenience, not a commitment) remains an experiment-design
   decision for `/queue-experiment`'s Step-2.5, not a substrate decision.
3. **No `REEConfig.from_dims` kwargs.** The new `GoalConfig` fields are set directly
   (`cfg.goal.use_hierarchical_goal_credit = True`, matching how `test_goalstate_forced_seed_positive_control.py`
   constructs `GoalConfig` directly and how MECH-217's flags are exercised in its own contracts) —
   no `from_dims`/`goal_stream()` passthrough was added, since there is no consumer yet to receive
   the value through that path (the `from_dims`-swallows-unknown-kwargs hazard applies to adding a
   *partial* passthrough; adding none is the conservative option until step 1/2 above land and
   define what an experiment driver actually needs to set).

---

## Architecture Context

Distinct from, and does not modify:
- **MECH-217** (`HippocampalModule.backward_credit_sweep`/`spread_reverse_replay_wanting`):
  within-level, writes into `ResidueField.VALENCE_WANTING`. SD-092 is cross-level, writes into a
  second `GoalState`-owned attractor. No shared code path; SD-092 does not touch
  `hippocampal/module.py`.
- **MECH-189** (`SuperOrdinalGoalMemory`): a cross-EPISODE persistent cue-indexed store keyed on
  context. SD-092's parent attractor is per-episode state (reset with `_z_goal`), analogous to how
  the base `_z_goal` itself is per-episode while MECH-189 sits above it as a separate persistent
  layer. The two are not coupled by this pass.
- **ARC-051**: its three levels remain a flat contributor scheme into one `VALENCE_WANTING`
  field; SD-092 does not change that scheme, it adds an orthogonal parent/child pair of
  `GoalState`-owned attractors alongside it.
- **SD-057** (`IncentiveTokenBank`): the `None`-unless-enabled allocation pattern is reused
  directly; no other coupling.

---

## What This SD Enables

The primitive (this pass) and the agent-loop call site (2026-08-02 follow-up, item 1 above) both
now exist. EXP-0385 and EXP-0390 are queueable once `/queue-experiment`'s own Step-2.5 adds the
remaining harness-side piece (item 2 above: a driver script that reads `info["transition_type"]`
off `env.step()` and calls `agent.notify_subgoal_attainment(...)`, plus decides which
representation to credit):
- **EXP-0385 (MECH-427)**: matched ATTAINED vs NO-ATTAINMENT contrast measuring
  `parent_goal_norm()` post-event.
- **EXP-0390 (MECH-428)**: 3-arm NO-SUBGOAL / SUBGOAL-BOOTSTRAP / FORCED-SEED harness measuring
  whether repeated subgoal-attainment credit alone raises `parent_goal_norm()` from near-zero
  toward the FORCED-SEED reference.

Both experiment_proposals.v1.json entries are flipped from `blocked_substrate` to `proposed`
(as of this pass) — `/queue-experiment` still needs to do its own Step-2.5 readiness check
(driver-side call + representation choice + a non-degenerate subgoal-attainment rate check,
guarding the goal_pipeline:GAP-2 foraging-ceiling trap) before either can actually run.

---

## Related Claims

MECH-427 (`cross_level_subgoal_credit`), MECH-428 (`subgoal_bootstrapped_goal_seeding`),
INV-086 (`goal_maintenance_feedback_necessity`, umbrella), ARC-051 (existing flat multi-level
VALENCE_WANTING scheme), MECH-217 (within-level credit precedent, template for this SD's
call/gate/return-dict style), MECH-112/MECH-230 (the `z_goal` attractor structure MECH-428 claims
gets bootstrapped), INV-034 (goal-seeding reliability, held pending exactly this class of fix).
