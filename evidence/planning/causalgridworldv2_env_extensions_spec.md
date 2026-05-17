# CausalGridWorldV2 Env Extensions -- Spec (primitives 1-3)

- Status: **IMPLEMENTED 2026-05-17** (primitives 1-3; validated by
  contract test, no claim-validation EXQ per spec section 5)
- Owner gap: `commitment_closure:GAP-3` (Phase 3, env infrastructure, no claim-validation EXQ)
- Registered: 2026-05-16

## Implementation record (2026-05-17)

Primitives 1-3 implemented in
`ree-v3/ree_core/environment/causal_grid_world.py` as env-only
constructor kwargs (NO REEConfig / config.py / queue change -- the
concurrency-safe path; concurrent goal_pipeline:GAP-3 session held those
files). Contract test:
`ree-v3/tests/contracts/test_env_extensions_gap3.py` (14 tests, C1-C5
incl. the section-5 integration smoke) -- 14/14 PASS; full ree-v3
contract regression 434/434 PASS (bit-identical OFF confirmed
suite-wide).

- **Primitive 1** -- `completion_tolerance_*` (7 kwargs). Tolerance
  block wraps the waypoint exact-match; Chebyshev/Manhattan; `hard` /
  `graded_exp` (credit `exp(-d/lambda)`). OFF and `frac=0.0` both
  dynamics bit-identical (verified by lockstep rollout). Per-tick
  diagnostics reset every step.
  **Scope deviation:** `completion_tolerance_targets="waypoint+resource"`
  is **reserved and raises ValueError** -- primitive 1 ships
  waypoint-only (Q-1a default). The resource-target extension
  (tolerance-driven consume-at-distance) is a documented future option;
  failing fast was preferred over silently honouring only the waypoint
  half. None of EXP-0156/0157/0162 need the resource half.
- **Primitive 2** -- `counter_evidence_*` (6 kwargs) +
  `_inject_counter_evidence()` (cloned structurally from the SD-029
  injector). Graded contingency degradation: validity decremented toward
  floor while the rule_state is persistent; committed-target reward
  scaled by validity; context (hazards/resources/drift) provably
  untouched (method-level invariant test). `transition_type` is set by
  the existing waypoint path; the hook degrades the realised outcome,
  not the transition label. Bit-identical when disabled.
- **Primitive 3** -- `dual_cue_*` (4 kwargs). Rides SD-049
  `_resources_by_type`; **hard ValueError if SD-049 not enabled**
  (Q-3a fail-fast); `dual_cue_replace_on_early_consume` defaults
  **False** (invalidate-episode, Q-3b); both-active tick accounting via
  SD-049 per-type lists + the existing `_consumed_type_tag_this_tick`
  (no edit to the consume block).

Validation deviates from the implement-substrate skill Step 8 (queue a
validation EXQ) **by spec design**: spec section 5 states Phase 3 has no
claim-validation EXQ (env infrastructure), and the concurrency
constraint forbade touching the queue/experiments. Validation is the
14-test contract file incl. the section-5 integration smoke. Deliverable
4 (phased rule_state training curriculum) remains a separate design pass
(section 6) -- the SD-034/MECH-266/MECH-268 *behavioural* arms still
need it before they run end-to-end.
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
| `completion_tolerance_kernel` | str | `"hard"` | `"hard"` (band) or `"graded_exp"` (Shepard) |
| `completion_tolerance_lambda` | float | `1.0` | exp-decay length for `graded_exp` kernel |

**Resolved 2026-05-16 (Q-1b, lit-grounded -- see
[literature_synthesis_2026-05-16_counter_evidence_generalization_competing_goals.md](./literature_synthesis_2026-05-16_counter_evidence_generalization_competing_goals.md)).**
Shepard's universal law of generalization ([DOI](https://doi.org/10.1126/science.3629243);
naturalistic confirmation [DOI](https://doi.org/10.1037/xge0001533)):
generalization decays *concave-exponentially* with distance under a
metric set by whether the stimulus dimensions are integral (Euclidean /
isotropic) or separable (city-block). Grid (x, y) location is a single
*integral* percept -> **isotropic metric; Chebyshev is the discrete
isotropic approximation on an 8-neighbour grid; Manhattan rejected.**
Second, generalization is graded not hard -> a `graded_exp` kernel is
added (completion credit `~ exp(-d / lambda)` inside the band). Default
stays `hard` (deterministic, contract-testable); `graded_exp` exists for
EXP-0156/0162-class arms that probe generalization *shape*.

**Info keys (always present):**
`completion_tolerance_enabled`, `completion_tolerance_T` (int; -1 when
disabled), `completion_within_tolerance_this_tick` (bool),
`completion_dist_to_target` (int; -1 when no active target),
`completion_tolerance_credit` (float; 1.0 for `hard` in-band, decayed
for `graded_exp`, 0.0 out-of-band/disabled).

## 3. Primitive 2 -- Counter-evidence injection hook

**Goal.** Env can introduce a contradicting outcome stream against a
*persistent* rule_state. Required by EXP-0164 (SD-034 + MECH-268
commitment vs contradiction full-loop).

**Build on the SD-029 `scheduled_external_hazard` pattern** (master
switch + interval + prob gate ~lines 1568-1579, `_inject_*()` method
~lines 3020-3089, `transition_type` tag, info diagnostics). No existing
reward-flip / persistent-state-contradiction mechanism exists; this is
new but structurally identical to the hazard injector.

**Resolved 2026-05-16 (Q-2a, lit-grounded -- the load-bearing one).**
The earlier "signed perturbation at the target" default is **rejected on
biological grounds**. Per Piquet, Faugère & Parkes 2023
([DOI](https://doi.org/10.1016/j.cub.2023.11.036)) and Dutech, Coutureau
& Marchand 2011 ([DOI](https://doi.org/10.1016/j.jphysparis.2011.07.017))
-- MECH-268 literature entries + synthesis doc -- "counter-evidence
against a committed action" is, mechanistically, **graded contingency
degradation**: the committed action progressively loses validity as a
predictor of the committed outcome while the surrounding context is held
constant. It is NOT a one-shot signed perturbation (i) and NOT a
contingency reversal / identity flip (ii); these are dissociable and
recruit different circuitry. Dutech 2011 further shows the discriminating
regime is *sustained* contradiction (a pe-saturation cap and a low-gain
integrator make opposite predictions only over a long horizon), so dose
and duration must be first-class sweepable parameters.

**Mechanism.** While a rule_state is persistent (`_sequence_in_progress`
True, `_next_waypoint_idx` at a committed target), the hook *degrades the
action->outcome contingency* for that committed target: each scheduled
injection lowers the probability that reaching the committed target
yields its expected committed outcome (by `counter_evidence_degrade_step`,
accumulating toward `counter_evidence_degrade_floor`), while the
background context (hazards, other resources, drift) is held unchanged.
The rule_state is NOT cleared and `_next_waypoint_idx` is NOT advanced.
Cumulative degradation (dose) and the number of steps it has been
sustained (duration) are tracked and surfaced so EXP-0164 can sweep the
weak/strong boundary -- the measured quantity is *where* MECH-268
pe-saturation lets SD-034 correctly withhold closure, not the response
to a single contradicting event.

`_inject_counter_evidence()`: tag `transition_type =
"counter_evidence"`; decrement the committed target's outcome-validity
toward the floor; never co-vary the context; do **not** advance
`_next_waypoint_idx` or clear `_sequence_in_progress`.

**New env-only kwargs:**

| kwarg | type | default | meaning |
|---|---|---|---|
| `counter_evidence_enabled` | bool | `False` | master switch |
| `counter_evidence_interval` | int | `50` | steps between degradation steps |
| `counter_evidence_prob` | float | `0.5` | prob of a degradation step when scheduled |
| `counter_evidence_degrade_step` | float | `0.2` | validity decrement per injection (dose rate) |
| `counter_evidence_degrade_floor` | float | `0.0` | minimum outcome-validity (1.0=intact, 0.0=fully degraded) |
| `counter_evidence_requires_persistent_rule` | bool | `True` | only degrade while a rule_state is persistent |

**Info keys (always present):**
`counter_evidence_enabled`, `counter_evidence_event_count` (int),
`counter_evidence_injected_this_tick` (bool),
`counter_evidence_target_validity` (float; 1.0 when intact/disabled),
`counter_evidence_sustained_steps` (int; duration the rule has been
under degradation), `counter_evidence_last_step` (int; -1 if none).

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
before `dual_cue_min_active_ticks`, the episode is **marked
precondition-not-met and excluded from the EXP-0160/0163 analysis
cohort** (`dual_cue_invalid_this_episode=True`); the cue is NOT
re-placed by default.

**Resolved 2026-05-16 (Q-3b measurement-validity; Q-3a fail-fast).**
Q-3b: re-placing a consumed cue mid-episode makes the choice set
non-stationary *and contingent on the agent's own prior choice* -- a
reactive-measurement confound that contaminates the MECH-266
mode-stickiness readout. Default is therefore **invalidate-episode**
(`dual_cue_replace_on_early_consume` default flipped True -> **False**);
the True path is a diagnostic/relaxation mode only, never for the
MECH-266 measurement. If invalidation discards too many episodes, the
fix is to make the cues harder to reach within
`dual_cue_min_active_ticks`, not to re-place them. Q-3a: `dual_cue` will
**raise a hard precondition error** if the SD-049 multi-resource path is
not enabled, rather than silently auto-enabling it -- explicit-config /
fail-loud discipline (matches the bit-identical-OFF + contract-test
culture); silent cross-subsystem coupling can mask misconfiguration.

**New env-only kwargs:**

| kwarg | type | default | meaning |
|---|---|---|---|
| `dual_cue_enabled` | bool | `False` | master switch |
| `dual_cue_min_active_ticks` | int | `10` | acceptance floor for "both active" |
| `dual_cue_replace_on_early_consume` | bool | `False` | diagnostic only; re-place a cue consumed before the floor (confounds MECH-266) |
| `dual_cue_type_tags` | tuple | `(1, 2)` | the two distinct SD-049 type tags used |

**Info keys (always present):**
`dual_cue_enabled`, `dual_cue_n_active` (int 0/1/2),
`dual_cue_ticks_both_active` (int),
`dual_cue_consumed_tag_this_tick` (int; -1 if none),
`dual_cue_invalid_this_episode` (bool; True if a cue was consumed before
the floor and replacement is off).

Interaction note: `dual_cue_enabled` requires the SD-049 multi-resource
heterogeneity path (it relies on `_resources_by_type` /
`_resource_type_grid`). Per Q-3a it raises a hard precondition error if
SD-049 is not enabled (fail-fast, no silent auto-enable).

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

**Design pass complete 2026-05-17:**
[../../docs/architecture/phased_rule_state_training_curriculum.md](../../docs/architecture/phased_rule_state_training_curriculum.md)
(Status: DESIGN -- PENDING IMPLEMENTATION). Root cause: the commit gate
is a single trained-variance threshold (`running_variance <
commitment_threshold`, 0.5 init vs 0.40) that short generic training
loops never cross -> the EXQ-321/261/325 all-zero signature. Design:
a 3-phase experiment-harness training protocol (P0 world-model+nav
warmup to cross the gate; P1 staged-difficulty consolidation with a
mid-curriculum abort probe; P2 frozen eval), emergent + forced-control
contrast arms, GAP-3 primitive 1 as the competence-ramp lever. R1 (the
gate may be mis-calibrated vs achievable world-model error, not a
curriculum-tuning problem) is the existential risk and is front-loaded
for cheap early falsification. 5 open design questions (O-1..O-5) await
review before implementation.

## 7. Sub-questions -- RESOLVED 2026-05-16

All six resolved. Biology-grounded ones (Q-1b, Q-2a, Q-3b) via the
literature pull
([synthesis](./literature_synthesis_2026-05-16_counter_evidence_generalization_competing_goals.md);
MECH-268 lit entries for Q-2a). Engineering ones (Q-1a, Q-2b, Q-3a) by
reasoned recommendation.

- **Q-1a** -- RESOLVED: `completion_tolerance_targets="waypoint"`
  (waypoint only). Basis (engineering): EXP-0156/0157/0162 are
  rule_state/waypoint arms; resource contact is a homeostatic
  *consumption* event (consuming removes the resource) with different
  semantics -- tolerance there would let the agent "consume at a
  distance", perturbing foraging dynamics and confounding the SD-012
  homeostatic-drive measurement. `"waypoint+resource"` retained as a
  non-default option for arms that explicitly need it.
- **Q-1b** -- RESOLVED: **Chebyshev confirmed** (grid x/y is an integral
  percept -> Shepard isotropic metric; Manhattan rejected); **add an
  optional `graded_exp` kernel** (generalization is concave-graded, not
  hard). Default stays `hard`. Basis (lit): Shepard 1987
  ([DOI](https://doi.org/10.1126/science.3629243)); Marjieh 2024
  ([DOI](https://doi.org/10.1037/xge0001533)).
- **Q-2a** -- RESOLVED: **graded contingency degradation**, context held
  constant, dose+duration sweepable. Signed perturbation and identity
  flip/reversal both rejected on biological grounds. Basis (lit):
  Piquet 2023 ([DOI](https://doi.org/10.1016/j.cub.2023.11.036)),
  Dutech 2011 ([DOI](https://doi.org/10.1016/j.jphysparis.2011.07.017)) --
  MECH-268 entries. (Section 3 rewritten.)
- **Q-2b** -- RESOLVED: **independent interval/prob knobs**, NOT a shared
  scheduler with SD-029 `scheduled_external_hazard`. Basis (engineering):
  counter-evidence and SD-029 hazard test different things; shared
  cadence entangles two manipulations and blocks factorial designs. Minor
  code duplication is the acceptable cost of analyzability.
- **Q-3a** -- RESOLVED: **hard precondition error** if SD-049 path not
  enabled (no silent auto-enable). Basis (engineering): explicit-config /
  fail-loud discipline; silent cross-subsystem coupling masks
  misconfiguration. (Section 4 updated.)
- **Q-3b** -- RESOLVED: **invalidate-episode**
  (`dual_cue_replace_on_early_consume` default flipped True -> False).
  Basis (measurement-validity reasoning; no canonical lit -- PubMed empty,
  WebSearch thin): mid-episode replacement is contingent on the agent's
  own prior choice = reactive-measurement confound for MECH-266 mode
  stickiness. (Section 4 updated.)

Net-effect table and per-sub-question rationale: see the
[synthesis doc](./literature_synthesis_2026-05-16_counter_evidence_generalization_competing_goals.md).
The spec is now decision-complete for primitives 1-3; next step is
`/implement-substrate` review (deliverable 4 / phased curriculum remains
a separate design pass per section 6).

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
