# CausalGridWorldV2 Env Extensions -- Spec (primitives 1-3)

- Status: **DRAFT for review** (no implementation yet)
- Owner gap: `commitment_closure:GAP-3` (Phase 3, env infrastructure, no claim-validation EXQ)
- Registered: 2026-05-16
- Decision basis: user decision 2026-05-16 -- Q2 tolerance-band = **adaptive
  (scaled to env size)**; spec primitives 1-3 now; deliverable 4 (phased
  rule_state training curriculum) split to a separate design pass.
- Unblocks: `commitment_closure:GAP-8` (SD-033b behavioural validation,
  `depends_on: GAP-3`) and the full behavioural arms of GAP-2 / GAP-4
  (SD-034 / MECH-266 / MECH-268 provisional -> stable).

## 0. Naming note

There is no separate `CausalGridWorldV2` class. The active env is the
single `CausalGridWorld` class in
`ree-v3/ree_core/environment/causal_grid_world.py`. "V2 extensions" =
the additional env-only config surface specified here, layered on the
existing class via the established kwarg->`self.attr` threading pattern
(same as `harm_gradient_enabled`, `microhabitat_max_seed_redraws`,
`transient_benefit_enabled`). The plan-of-record term "CausalGridWorldV2"
is retained as the logical label for this extension set.

## 1. Cross-cutting conventions (all three primitives)

These follow the project's env-only-kwarg precedent (NOT routed through
`REEConfig.from_dims`):

1. **Master switch, default-False, bit-identical OFF.** Each primitive
   gets a `<name>_enabled: bool = False` constructor kwarg, threaded
   `self.<name>_enabled = bool(<name>_enabled)`. When False: zero extra
   RNG draws, zero behavioural change, sentinel/inert info keys. A C1
   contract per primitive asserts 300-step bit-identical parity vs
   pre-extension env.
2. **Per-episode counters reset in `reset()`**, updated in `step()`,
   surfaced in the info-dict construction block (lines ~1659-1789).
   Always-present keys (inert values when disabled), matching the
   `microhabitat_*` / `transient_benefit_*` precedent.
3. **Determinism via `self._rng`** (the per-episode seeded RNG), so
   scripted-eval `reset_to(...)` contract tests are reproducible.
4. **Causal tagging via `transition_type`** for any env-injected event,
   so agent-caused vs env-caused stays cleanly separable (same
   discipline as SD-029 `env_caused_hazard`).
5. No `REEConfig` change; no `claims.yaml` change (env infra unblocks but
   does not itself promote SD-034 / MECH-266 / MECH-268).

## 2. Primitive 1 -- Adaptive tolerance-band completion

**Goal.** `rule_state` / goal completion fires when the agent reaches a
state *within tolerance T of* the target, not exact-match. Required by
EXP-0156 / EXP-0157 / EXP-0162.

**Current exact-match sites (to be wrapped, not replaced):**
- Waypoint completion: `grid[new_x,new_y] == ENTITY_TYPES["waypoint"]`
  AND `wp_idx == self._next_waypoint_idx` (~line 1324); sequence done at
  `self._next_waypoint_idx >= len(self.waypoints)` (~line 1331);
  `transition_type = "sequence_complete"` (~line 1335).
- Resource contact: agent steps onto `target_type ==
  ENTITY_TYPES["resource"]` (~line 1199).

For the OCD / SD-034 behavioural arms the relevant "rule_state target"
is the **next waypoint** in subgoal mode (the persistent committed
target). Tolerance applies there first; resource-contact tolerance is an
optional secondary toggle (see open question Q-1a).

**Adaptive T (the resolved Q2 choice).**

```
T_cells = max(0, round(completion_tolerance_frac * self.size))
# completion_tolerance_frac default 0.0 -> exact-match (bit-identical)
# per-experiment override: completion_tolerance_cells (absolute, wins if >=0)
```

`self.size` is the grid side length (the env-size scaling variable).
Distance metric: **Chebyshev** (`max(|dx|,|dy|)`) -- matches 8-cell
grid-step semantics; configurable to Manhattan via
`completion_tolerance_metric` if a behavioural arm needs it (default
`"chebyshev"`).

Completion predicate (waypoint i at `self.waypoints[i]`):
```
dist = chebyshev((agent_x, agent_y), waypoints[_next_waypoint_idx])
within = self.completion_tolerance_enabled and dist <= T_cells
fire if (exact-cell hit)  OR  within
```
Exact-cell behaviour is preserved as a strict subset (frac 0.0 -> T=0 ->
`dist <= 0` == exact), so OFF and frac=0 are both bit-identical to today.

**New env-only kwargs:**

| kwarg | type | default | meaning |
|---|---|---|---|
| `completion_tolerance_enabled` | bool | `False` | master switch |
| `completion_tolerance_frac` | float | `0.0` | T = round(frac * size); adaptive |
| `completion_tolerance_cells` | int | `-1` | absolute override; >=0 wins over frac |
| `completion_tolerance_metric` | str | `"chebyshev"` | `"chebyshev"` or `"manhattan"` |
| `completion_tolerance_targets` | str | `"waypoint"` | `"waypoint"` or `"waypoint+resource"` |

**Info keys (always present):**
`completion_tolerance_enabled`, `completion_tolerance_T` (int; -1 when
disabled), `completion_within_tolerance_this_tick` (bool),
`completion_dist_to_target` (int; -1 when no active target).

## 3. Primitive 2 -- Counter-evidence injection hook

**Goal.** Env can introduce a contradicting outcome stream against a
*persistent* rule_state. Required by EXP-0164 (SD-034 + MECH-268
commitment vs contradiction full-loop).

**Build on the SD-029 `scheduled_external_hazard` pattern** (master
switch + interval + prob gate ~lines 1568-1579, `_inject_*()` method
~lines 3020-3089, `transition_type` tag, info diagnostics). No existing
reward-flip / persistent-state-contradiction mechanism exists; this is
new but structurally identical to the hazard injector.

**Mechanism.** While a rule_state is persistent (subgoal sequence
in-progress: `self._sequence_in_progress` True with
`_next_waypoint_idx` pointing at a committed target), the hook injects a
*contradicting outcome* at the committed target on a scheduled cadence:
the env presents the next-waypoint cell as yielding the opposite of the
expected committed outcome (a negative/contradiction event) without
clearing the rule_state. This is the env-side substrate for "sustained
counter-evidence" against which MECH-268 PE-saturation and the SD-034
closure operator are tested (closure must NOT fire on weak contradicted
local outcomes; must fire on genuine completion).

`_inject_counter_evidence()`: tag `transition_type =
"counter_evidence"`; apply a configurable contradiction signal
(`counter_evidence_magnitude`, signed, applied to the step
harm/benefit term at the committed target); do **not** advance
`_next_waypoint_idx` or clear `_sequence_in_progress`.

**New env-only kwargs:**

| kwarg | type | default | meaning |
|---|---|---|---|
| `counter_evidence_enabled` | bool | `False` | master switch |
| `counter_evidence_interval` | int | `50` | steps between injection attempts |
| `counter_evidence_prob` | float | `0.5` | prob of injection when scheduled |
| `counter_evidence_magnitude` | float | `0.3` | signed contradiction applied at committed target |
| `counter_evidence_requires_persistent_rule` | bool | `True` | only inject while a rule_state is persistent |

**Info keys (always present):**
`counter_evidence_enabled`, `counter_evidence_event_count` (int),
`counter_evidence_injected_this_tick` (bool),
`counter_evidence_last_step` (int; -1 if none).

## 4. Primitive 3 -- Dual simultaneously-active resource cue

**Goal.** Two competing goal cues active in the same episode. Required
by EXP-0160 (MECH-266 competing goals) and EXP-0163 (MECH-266 mode
stickiness).

**Build on existing multi-resource support.** `self.resources` already
holds multiple `[x,y]`; SD-049 heterogeneity already provides per-type
lists `self._resources_by_type[type_idx]` and tags
`self._resource_type_grid[x,y]`. The primitive designates exactly two
*distinct, simultaneously-active, type-tagged* resource cues and
guarantees both remain active (uncontacted, on-grid) for at least
`dual_cue_min_active_ticks` ticks (Phase 3 acceptance: dual cues active
for >= 10 ticks).

**Mechanism.** At `reset()` (and on respawn) place exactly two cues with
distinct type tags (`cue_A`, `cue_B`); suppress respawn collapse so both
persist; track per-step both-active tick count. If one is consumed
before `dual_cue_min_active_ticks`, optionally re-place it to honour the
"both active >=N ticks" acceptance criterion
(`dual_cue_replace_on_early_consume`, default True).

**New env-only kwargs:**

| kwarg | type | default | meaning |
|---|---|---|---|
| `dual_cue_enabled` | bool | `False` | master switch |
| `dual_cue_min_active_ticks` | int | `10` | acceptance floor for "both active" |
| `dual_cue_replace_on_early_consume` | bool | `True` | re-place a cue consumed before the floor |
| `dual_cue_type_tags` | tuple | `(1, 2)` | the two distinct SD-049 type tags used |

**Info keys (always present):**
`dual_cue_enabled`, `dual_cue_n_active` (int 0/1/2),
`dual_cue_ticks_both_active` (int),
`dual_cue_consumed_tag_this_tick` (int; -1 if none).

Interaction note: `dual_cue_enabled` should imply / require the SD-049
multi-resource heterogeneity path (it relies on `_resources_by_type` /
`_resource_type_grid`). Spec sets `dual_cue_enabled=True` to auto-enable
the SD-049 type machinery if not already on, logged via an ASCII
diagnostic; alternative is a hard precondition error (open question
Q-3a).

## 5. Acceptance / integration smoke

Per the plan-of-record Phase 3 acceptance: a single integration smoke
run with **all four** primitives exercised in one episode produces
non-zero `committed_steps`, non-zero counter-evidence injection events,
and dual cues active for >= 10 ticks. For this spec (primitives 1-3, no
curriculum) the smoke target is:

- `completion_within_tolerance_this_tick` True at least once with
  `completion_tolerance_frac > 0` and a near-miss (dist in `1..T`);
- `counter_evidence_event_count > 0` while a rule_state is persistent;
- `dual_cue_ticks_both_active >= dual_cue_min_active_ticks`;
- OFF-path 300-step bit-identical parity (per-primitive C1).

Contract-test home: `ree-v3/tests/contracts/` alongside
`test_microhabitat_gap2.py` / `test_harm_gradient_gap1.py`. Proposed
file: `test_env_extensions_gap3.py` with C1 (bit-identical OFF, all
three) + C2-C4 per primitive (tolerance fires within band / not outside;
counter-evidence injects only while rule persistent + tags correctly;
dual-cue both-active floor honoured). Implementation + tests go via
`/implement-substrate` (env is substrate); any validating EXQ via
`/queue-experiment` -- but note Phase 3 itself has no claim-validation
EXQ (env infrastructure).

## 6. Out of scope (deliverable 4 -- separate design pass)

**Phased rule_state training curriculum** is explicitly NOT in this
spec. It is the committed-mode-elicitation blocker that stalled
V3-EXQ-321 / V3-EXQ-261 (substrate_queue SD-021 / SD-022), the
highest-risk piece, and is kept off the GAP-3 critical path per the
2026-05-16 user decision. It needs its own design doc + risk analysis
before the SD-034 behavioural arms can run end-to-end even with
primitives 1-3 landed.

## 7. Open sub-questions (for review)

- **Q-1a**: tolerance on resource-contact as well as waypoint? Spec
  default `completion_tolerance_targets="waypoint"` (waypoint only).
  Confirm or widen.
- **Q-1b**: Chebyshev vs Manhattan default. Spec default Chebyshev
  (8-neighbour grid-step semantics). Confirm.
- **Q-2a**: counter-evidence as a signed reward/harm perturbation at the
  committed target (spec default) vs a richer "contradicting outcome
  stream" (e.g. flipping the resource/hazard identity at the target).
  Spec takes the simpler perturbation; flag if EXP-0164 needs identity
  flip.
- **Q-2b**: should counter-evidence injection respect the SD-029
  `scheduled_external_hazard` cadence knobs (shared scheduler) or own
  independent interval/prob? Spec uses independent knobs.
- **Q-3a**: `dual_cue_enabled` auto-enabling SD-049 type machinery
  (spec default) vs hard precondition error. Confirm.
- **Q-3b**: re-placement on early consume (spec default True) can
  perturb the MECH-266 competing-goals measurement -- confirm this is
  acceptable for EXP-0160 / EXP-0163 or prefer "episode invalid if
  consumed before floor".

## 8. References

- Plan-of-record: `commitment_closure_plan.md` (GAP-3, Phase 3,
  decision-log 2026-05-16 Q2 resolution).
- Env source: `ree-v3/ree_core/environment/causal_grid_world.py`
  (exact-match completion ~1199/1324-1335; SD-029 injector pattern
  ~1568-1579 / 3020-3089; info-dict block ~1659-1789; env-only kwarg
  precedent: `harm_gradient_enabled` / `microhabitat_max_seed_redraws` /
  `transient_benefit_enabled`).
- Behavioural arms: EXP-0156 / EXP-0157 / EXP-0160 / EXP-0162 /
  EXP-0163 / EXP-0164 (commitment_closure Test cohort).
