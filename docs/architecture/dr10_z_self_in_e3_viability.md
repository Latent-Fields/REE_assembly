---
title: "DR-10: z_self enters E3 trajectory viability scoring"
parent: "Executive & PFC Control"
grandparent: Architecture
nav_order: 5
---

# DR-10: z_self enters E3 trajectory viability scoring

**Claim ID:** (DR-10 audit item; v4_spec.md V4-2) -- owner node `self_model_v4:SELF-3`
**Unblocks:** MECH-215 (self-model prerequisite for agentive prediction -- the z_self
viability half; DR-10 + DR-12 together) and ARC-081 (the E3-scoring half of the
self-as-object cutover).
**Subject:** ethics_engine_3.self_viability_weighting
**Status:** IMPLEMENTED 2026-07-01
**Generation:** v4 (off the V3 critical path; promotes nothing in V3; excluded from the V3 closure %)
**Depends on:** SD-005 (z_self/z_world split, implemented), **DR-13 / SELF-1 (stateful
z_self, implemented + validated 2026-07-01)** -- the stateful z_self is the SUBJECT of the
viability estimate; this is why SELF-3 was blocked on the SELF-1 substrate build until
today. ARC-016 (E3 dynamic precision) is the sibling per-candidate-cost precedent.
**Blocks:** SELF-5 (DR-11 z_self-domain goals) and SELF-7 (INV-064 gate) list SELF-3 as a
prerequisite.

---

## Problem

DR-10 from `docs/architecture/v4_spec.md` V4-2: *"z_self in E3 trajectory scoring.
score_trajectory() currently evaluates entirely in z_world space; bodily state must
modulate viability."*

V3 today: `E3.score_trajectory()` scores `J(zeta) = F + lambda*M + rho*Phi - beta*B - goal`
purely over the z_world trajectory (`compute_reality_cost` / `harm_eval` / `compute_goal_score`
all read z_world; `stack.py` line comments confirm "All scoring operates over z_world
(SD-005)"). There is **no z_self term in viability** -- the same trajectory scores identically
whether the agent is fresh or depleted/damaged. DR-10 makes the agent's own bodily
capacity/affect/damage state (read from the DR-13 stateful z_self) gate which trajectories
are viable **for this agent**.

This is the E3-scoring half of the MECH-215 unblock (DR-12/SELF-4 supplied the
E2-self-transition-accuracy half). It requires a **stable** z_self as the subject of the
viability estimate -- hence the dependency on DR-13/SELF-1, which landed + validated
(V4-EXQ-002 PASS) on 2026-07-01.

## Solution

A **no-op-default monotone viability-by-self-cost lever** in `E3TrajectorySelector`, a
sibling to the DR-12 PE lever on the **same machinery** (`score_trajectory` cost
composition + `select()` per-candidate threading). Because REE scoring is lower-is-better,
a higher self-viability COST raises the trajectory's cost -> the trajectory is discounted
(its viability is down-weighted). The lever adds **no learned parameters**.

**Where the penalty is applied (`score_trajectory`):**

```
score = F + lambda*M + rho*Phi - beta*B - goal_term   (+ DR-12 PE penalty)
if config.use_self_viability_weighting and self_viability is not None and self_viability_weight != 0:
    score = score + config.self_viability_weight * penalty(self_viability)
```

`penalty(sv)` is monotone non-decreasing in the cost (clamped >= 0):
- `mode = "linear"` (default): `penalty = sv`
- `mode = "saturating"`: `penalty = 1 - exp(-sv / self_viability_scale)` in `[0, 1)` -- a
  bounded viability-deficit reading.

**Per-candidate threading (so it can change selection):** `select()` accepts an optional
`self_viability_per_candidate` `[K]` tensor and passes element `i` into candidate `i`'s
`score_trajectory`. A per-candidate cost that varies across candidates can change the
committed argmin; a uniform scalar is argmin-invariant (the V3-EXQ-571 deleted-broadcast
lesson), which is why the signal is per-candidate.

**Diagnostics** (`last_score_diagnostics`): `self_viability_active` (bool),
`self_viability_weight`, `self_viability_range` (cross-candidate range of the supplied cost
-- the pilot's non-vacuity gate), `self_viability_penalty_range` (cross-candidate range of
the applied penalty).

### Config (all no-op default; bit-identical OFF)

| Param | Type | Default | Purpose | Class |
|-------|------|---------|---------|-------|
| `use_self_viability_weighting` | bool | `False` | master switch | E3Config (+ REEConfig.from_dims) |
| `self_viability_weight` | float | `0.0` | monotone penalty gain | E3Config |
| `self_viability_mode` | str | `"linear"` | `linear` \| `saturating` | E3Config |
| `self_viability_scale` | float | `1.0` | saturating-mode scale | E3Config |

With `use_self_viability_weighting=False` (or no `self_viability` supplied), the lever is
skipped entirely -> bit-identical to the pre-DR-10 selector.

### Per-candidate self-viability source (v1 scope decision)

v1 is **caller/agent-supplied** (user-confirmed AskUserQuestion 2026-07-01): the lever
consumes a per-candidate self-viability cost passed into `select()` (the DR-12
`e2_forward_pe` threading precedent). `REEAgent.set_injected_self_viability()` /
`_injected_self_viability` plumbs it through `select_action` (default `None` ->
bit-identical; version-layering guarded so the default V3 path never sends the kwarg). The
DR-10 pilot (V4-EXQ) is a **controlled substrate-readiness probe** that assigns a known
per-candidate self-viability (high on some candidates) and tests whether the ON arm selects
differently from the OFF baseline.

The signal is **derived from the DR-13 stateful z_self** -- that is what makes this "z_self
enters E3 viability". **Documented ecological follow-on (NOT v1):** an agent-side auto-source
that computes the per-candidate cost from z_self without a supplied signal -- e.g. an
allostatic z_self-deviation (distance of the stateful z_self from its running homeostatic
setpoint) times a per-candidate demand proxy, or a learned z_self->viability head (which
would need phased training + arguably SELF-2's E2_self per-candidate self-transition). That
is the piece that adds new state/params and is deferred to keep v1 a "lever on existing
machinery."

## What this enables / the falsifier

**FALSIFIER:** *if the z_self-derived self-viability weighting does NOT change trajectory
selection vs the OFF baseline when a decisive per-candidate cost is supplied, DR-10 buys
nothing and the wiring is inert.* The pilot pre-registers a **non-vacuity precondition**
(cross-candidate `self_viability_range` >= floor AND the applied penalty exceeds the
best-vs-second primary gap; else `substrate_not_ready_requeue`) and an **inert-wiring
off-ramp** (range clears but ON==OFF selection). PASS = the ON arm avoids the low-viability
candidate the OFF arm selects, i.e. bodily state now gates viability. This is the DR-10 half
of the (DR-10 + DR-12) pair that unblocks MECH-215.

## Architecture context

- **DR-13 (SELF-1)** supplies the stateful z_self this lever reads as the viability subject.
- **DR-12 (SELF-4)** is the sibling lever (E2-forward-PE -> E3 confidence) on the identical
  `score_trajectory` + per-candidate `select()` machinery; DR-10 and DR-12 are the two
  halves of the MECH-215 unblock.
- **ARC-016** (E3 dynamic precision) is the precedent for a per-candidate cost modulation on
  E3 scoring.
- **SELF-2 (SD-030, V4-deferred)** would give per-candidate z_self self-transition, enabling
  the richer ecological self-viability source noted above.

## ML/AI engineering parallel (Layer 7)

State-dependent / risk-sensitive action valuation: the same engineering move as a
capacity/constraint-aware cost in constrained RL (penalize actions whose demand exceeds the
agent's current budget), but here (a) the "budget" is the interoceptive/proprioceptive
z_self state, not a hand-specified constraint, and (b) the locus + grounding are
neuroscientific (interoceptive/allostatic modulation of action selection -- Craig/Seth
interoceptive-inference; the self as the subject of viability), not an RL constraint solver.
No learned parameters in v1 (pure monotone arithmetic on a supplied per-candidate cost).
Hazard imported from the modulatory-authority cluster: a penalty whose scale is mismatched
to the primary score range either vanishes or dominates -> the pilot pre-registers the
range non-vacuity + decisiveness gates and calibrates `self_viability_weight`.

## Related claims

MECH-215 (unblocked half; stays candidate/v4), ARC-081 (self-as-object pillar; E3-scoring
half; stays candidate/v4), DR-13/SELF-1 (the stateful z_self subject), DR-12/SELF-4 (sibling
lever), ARC-016 (E3 dynamic precision -- precedent), SD-005 (z_self/z_world split),
MECH-094 (N/A -- waking action-selection scoring, no replay write surface).
