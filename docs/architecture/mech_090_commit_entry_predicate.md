---
title: MECH-090 Commit-Entry Predicate (R-c single-gate conjunction)
parent: "Executive & PFC Control"
grandparent: Architecture
nav_order: 9
status: active
status_asof: 2026-07-10
status_claim: MECH-090
---

# MECH-090 Commit-Entry Predicate (R-c single-gate conjunction)

**Claim ID:** MECH-090 (commit-entry predicate amendment, 2026-05-28)
**Subject:** `control_plane.beta_gate.commit_entry_readiness_conjunction`
**Status:** IMPLEMENTED 2026-05-28 (substrate); VALIDATION PENDING V3-EXQ-592b
**Registered:** 2026-05-28
**Plan-of-record:** [commitment_closure_plan.md](../../evidence/planning/commitment_closure_plan.md) GAP-4
**Predecessor synthesis:** [targeted_review_connectome_mech_090/synthesis.md](../../evidence/literature/targeted_review_connectome_mech_090/synthesis.md) (commit `9e68c5ca8a`)
**Depends on:** MECH-090 base BetaGate (IMPLEMENTED 2026-04-10), E3SelectionResult `scores` + `committed` fields (existing)
**Blocks:** SD-034 / MECH-266 / MECH-267 / MECH-268 behavioural arms (transitively, via GAP-4)

## Problem

The current REE-V3 BetaGate elevates into committed mode when

    running_variance < commitment_threshold

is satisfied at [e3_selector.py:829](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/predictors/e3_selector.py).
`running_variance` is an EMA over E2 world-forward prediction error -- a precision-of-prediction proxy.
Nothing else gates entry.

[V3-EXQ-592](../../evidence/experiments/v3_exq_592_gap11_pilot_committed_mode_curriculum/) seed 42
showed this predicate is satisfiable in two architecturally distinct ways:

- **Honest path.** E2 learns environment dynamics; predictions tighten; rv falls; commitment is earned.
- **Degenerate path.** The policy collapses to a near-fixed-point trajectory; the dynamics it samples
  are trivially self-consistent; rv falls to 2.7e-5; commitment is "earned" with `nav_competence = 0.0`.

The substrate cannot distinguish the two. The agent enters committed mode without being competent
to execute anything -- a structural pathology that licenses degenerate fixed-points.

## Solution

Single-gate conjunction at BetaGate entry:

    BetaGate.elevate() admitted iff
        E3SelectionResult.committed (rv-low)
        AND
        per-candidate first-action margin (top1 - top2) >= floor

The readiness signal is the per-candidate E3 score margin: the gap between the chosen
trajectory's score and the next-best alternative's score, computed off `result.scores`
after the dACC / lateral_pfc / OFC / MECH-295 / MECH-314 / MECH-320 / MECH-341
score_bias chain. REE convention is lower-is-better (winner = `argmin`), so

    margin = scores.sort().values[1] - scores.min()

A positive margin means there is a clear winner; a near-zero margin means the candidate
pool collapsed to a near-tie (the V3-EXQ-592 seed-42 signature).

**Reading.** R-c (single-gate conjunction). The pass-1 synthesis disposes:

- **R-a** (rv-only is correct; V3-EXQ-592 is a curriculum problem) -- NOT defensible
  against the post-pass corpus.
- **R-b** (rv-only entry + separate downstream propagation gate) -- conservative;
  consistent with Tandetnik 2021 frontal-lesion finding; preserves rv-only commit
  semantics for downstream consumers at the cost of a "stuck-elevated, blocked-from-
  propagating" intermediate state.
- **R-c** (single-gate conjunction) -- strongest reading; anchored on Cisek & Kalaska 2010
  affordance-competition, Hanes & Schall 1996 accumulator-to-threshold, and
  Roesch / Calu / Schoenbaum 2007 dopaminergic readiness signal. Hanes-Schall in
  particular shows the biological commit gate fires on a readiness accumulator crossing
  a criterion, not on a precision threshold.

## Architecture Context

The gate sits at the boundary between E3 (the rv-low decision) and BetaGate (the actual
elevation event). The cleanest implementation site is `agent.py`, NOT `e3_selector.py`:
`E3SelectionResult.committed` continues to mean "rv crossed", as it always has; what we
change is what `agent.py` does with that signal. Downstream consumers that read
`result.committed` (E3-internal trajectory commit tracking, the bistable / legacy
elevate branches, etc.) see unchanged semantics. The R-c gate is a conjunction layered
on top.

This is the same architectural shape as the MECH-094 categorical write gate (which gates
content writes at simulation/replay paths) and MECH-261 (which gates EMA update strength
on operating mode). MECH-090 R-c is the third member of a category: it gates the
beta-elevation event itself.

The gate logic lives in `BetaGate.should_admit_elevation(score_margin, n_candidates)`
([ree-v3/ree_core/heartbeat/beta_gate.py](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/heartbeat/beta_gate.py)):
when `use_commit_readiness_gate=False`, the predicate is unconditionally `True` (bit-identical
to pre-R-c). When `True`, the predicate returns `margin >= commit_readiness_floor`.

## Config and defaults

| Param | Type | Default | Purpose |
|---|---|---|---|
| `HeartbeatConfig.use_commit_readiness_gate` | bool | `False` | master switch |
| `HeartbeatConfig.commit_readiness_floor` | float | `0.05` | minimum admissible margin |
| `HeartbeatConfig.commit_readiness_strict_single_candidate` | bool | `False` | how to treat n_candidates < 2 |

All knobs default to no-op. Master OFF means `should_admit_elevation` returns `True`
unconditionally; the BetaGate diagnostic counters do not increment. Single-candidate
permissive default admits when the pool collapsed to one trajectory (no margin to
compute against); strict-mode blocks (diagnostic only; production substrate stays
permissive).

The floor of `0.05` is small relative to the EXQ-608 `mean_top2_class_gap` range of
0.27-1.96 seen in unaugmented baselines, so the gate fires only on genuinely degenerate
near-tie scoring. Q-053-style calibration is a follow-on substrate task, not a
precondition for the substrate landing.

## Data flow

```
e3.select(...) -> E3SelectionResult.scores [K], .selected_index, .committed
       |
       +-- agent.py: if result.committed and use_commit_readiness_gate:
       |       _readiness_margin = sorted(scores)[1] - sorted(scores)[0]
       |       _n_candidates = K
       |
       +-- bistable branch (heartbeat.beta_gate_bistable=True):
       |       if result.committed
       |          and not beta_gate.is_elevated
       |          and beta_gate.should_admit_elevation(margin, K):
       |              beta_gate.elevate()
       |              snapshot anchor keys (MECH-269 / MECH-090)
       |              record_committed_trajectory (MECH-290)
       |
       +-- legacy branch (heartbeat.beta_gate_bistable=False):
               admit = should_admit_elevation(margin, K) if result.committed else True
               if result.committed and admit:
                   reset _committed_step_idx
                   if not beta_gate.is_elevated: [entry snapshots]
                   beta_gate.elevate()
               else:
                   if beta_gate.is_elevated: reset _committed_step_idx
                   beta_gate.release()
```

The legacy branch's `release()` semantic when gate blocks is deliberate: an rv-low /
readiness-low tick is treated as effectively uncommitted, so any prior elevation
is released. This avoids a "stuck-elevated, no propagation" state that R-b would
have produced; R-c is single-stage by design.

## Backward compatibility

With `use_commit_readiness_gate=False` (default):
- `BetaGate.__init__` accepts the new kwargs but `should_admit_elevation` returns
  `True` unconditionally without incrementing counters.
- `agent.py` enters the `_readiness_margin` computation block only when both
  `result.committed=True` AND `use_commit_readiness_gate=True`, so the margin
  computation is gated entirely off.
- `beta_gate.elevate()` fires exactly when it would have pre-R-c.

Verified: 506/506 contracts PASS with defaults unchanged. `BetaGate.get_state()`
exposes the new keys (`mech090_n_elevation_admitted` / `_blocked` /
`_single_candidate` / `_last_readiness_score_margin`) so experiments can
write the diagnostics into manifests without conditional handling.

## Phased training

N/A -- pure arithmetic regulator. No learned parameters, no gradient flow,
no encoder head, no MECH-094 simulation-write surface (the gate decides whether
to admit a control-state transition, it does not write content).

## MECH-094

N/A. The gate decision is at waking action-selection; the substrate is read-only
over E3 scores and writes only a control-state transition (beta elevation), not
memory content.

## What this enables

1. The V3-EXQ-592 seed-42 degenerate basin is no longer satisfiable -- the gate
   blocks elevation when score margin collapses, regardless of how low rv goes.
2. SD-034 / MECH-266 / MECH-267 / MECH-268 behavioural arms can be re-queued under
   the conjunction substrate; their PASSes are no longer contaminated by the
   "rv-only entry into degenerate committed mode" failure mode.
3. The Hanes-Schall accumulator-to-threshold motif is now the architectural shape
   of the commit gate, with the per-candidate margin readout as the readiness signal.
   This positions REE for the Phase-2 accumulator EMA upgrade (sub-flag dispatch
   pattern, MECH-313 / MECH-314 / MECH-320 precedent) if Q-053 surfaces the need.

## Validation experiment

V3-EXQ-592b (2-arm diagnostic):

- **ARM_0 GATED.** `use_commit_readiness_gate=True`, `commit_readiness_floor=0.05`.
  Same env + seed (42) as V3-EXQ-592. **Acceptance:** total committed steps == 0
  AND `mech090_n_elevation_blocked >= 1` AND `running_variance < commitment_threshold`
  at some point during the run (confirming the gate is the load-bearing block,
  not an upstream rv failure).
- **ARM_1 GATED_FORCED_READY.** Same gate config; experiment script artificially
  injects `score_bias` to ensure a non-collapsed candidate distribution
  (margin >= 0.10 by construction). **Acceptance:** total committed steps > 0
  AND `mech090_n_elevation_admitted >= 1` (confirming the gate does not
  permanently lock out commitment when readiness clears).

Joint PASS = MECH-090 R-c substrate landing validated; commitment_closure:GAP-4
status `partial` -> `done`. Joint FAIL on ARM_0 (degenerate basin re-enters
committed mode despite gate ON) = substrate retest under diagnostic
counters / re-tune the floor. ARM_0 PASS + ARM_1 FAIL = gate is over-restrictive
(permanently locks out commitment); re-tune floor downward. ARM_0 FAIL +
ARM_1 PASS = unexpected; root-cause via `/diagnose-errors`.

## Related claims

- **MECH-090** (this claim) -- BetaGate; the substrate the predicate amendment modifies.
- **ARC-028, MECH-105** -- hippocampal-BetaGate completion coupling (the release-side counterpart;
  this amendment touches only the entry side).
- **MECH-091** -- urgency interrupt (the orthogonal release-side override; unaffected).
- **SD-034** -- governance closure operator (downstream beneficiary; behavioural arms unblock once
  the validation EXQ confirms degenerate-basin entries are blocked).
- **Cisek & Kalaska 2010** -- affordance-competition framework (literature anchor R1).
- **Hanes & Schall 1996** -- FEF accumulator-to-threshold (literature anchor R2).
- **Roesch, Calu & Schoenbaum 2007** -- dopaminergic readiness signal / premature-commit pathology
  (literature anchor R3).
- **Tandetnik 2021** -- frontal-lesion dissociation of commitment from belief-lock (R-b's anchor;
  this implementation retains R-b's empirical content as a fallback if validation fails).
- **commitment_closure:GAP-4** -- the closure-plan gap this amendment resolves.

---

## R-c amendment continued (nav_competence axis, 2026-05-29)

**Status:** IMPLEMENTED 2026-05-29 (substrate); VALIDATION PENDING V3-EXQ-592b
**Subject:** `control_plane.beta_gate.commit_entry_readiness_conjunction.nav_competence`

The 2026-05-28 substrate landed the **within-tick decisiveness** axis of R-c (per-candidate
score margin -- the Hanes & Schall 1996 accumulator-to-threshold reading). This continuation
adds the **across-tick motor-program readiness** axis (the Cisek & Kalaska 2010 affordance-
preparation + Roesch / Calu / Schoenbaum 2007 dopaminergic-readiness reading). Both axes are
R-c readings of the same literature; they detect different aspects of the V3-EXQ-592 seed-42
degeneracy and compose via AND.

### Why a second axis

The score_margin gate detects degeneracy at the candidate-distribution level: when the policy
collapsed to a near-fixed-point trajectory, the E3 candidate pool's first-action margin
collapses with it. But score_margin is silent about whether the agent has demonstrably
succeeded recently. A trivially-predictable policy can produce a marginally-clear E3 winner
on a useless trajectory; the within-tick gate would admit, even though the across-tick
competence record says the agent has reached `nav_competence = 0.0`.

V3-EXQ-592 seed 42's manifest carries `nav_competence = 0.0` at every P0 probe tick while
`running_variance = 2.7e-5`. The prior session's score_margin gate plausibly catches the
within-tick signature of the same degeneracy, but does not consult the across-tick
competence record. The two axes compose: elevation is admitted iff *both* (a) the current
candidate pool is decisive enough AND (b) the recent-success EMA clears a floor.

### Module

`ree-v3/ree_core/policy/commit_readiness.py` introduces `CommitReadiness` -- a pure-arithmetic
regulator, sibling pattern to `MECH-313 NoiseFloor` / `MECH-320 TonicVigor`. Maintains a
`[0, 1]` readiness EMA over per-tick outcome signals plus an explicit `notify_outcome(value)`
harness-push seam:

```python
class CommitReadiness:
    def update(outcome_signal: Optional[float] = None, simulation_mode: bool = False) -> float
    def notify_outcome(value: float, simulation_mode: bool = False) -> float
    def is_above_floor(floor: float) -> bool
    def notify_block() -> None
    def reset() -> None
    def get_state() -> dict
```

The EMA is windowless; `commit_readiness_window` is informational (the rough effective half-
life the alpha targets). Initial readiness is `1.0` (fail-open: an agent with no outcome
history defaults to "ready" so the conjunction reduces to the score_margin-only path until
real outcome data has been collected). The MECH-094 simulation gate is the standard
`SD-035 / MECH-279 / gated_policy / MECH-313 / MECH-320` pattern: `simulation_mode=True`
returns without advancing the EMA and only increments the simulation-skip counter.

`outcome_signal=None` is the no-signal sentinel: substrates that do not emit an outcome key
let the EMA sit at its initial value, preserving the fail-open default.

### Phase-1 wiring (this pass)

- **Module:** `ree-v3/ree_core/policy/commit_readiness.py` (NEW)
- **Config:** `REEConfig.use_mech090_readiness_conjunction` (default `False`, bit-identical
  OFF), `mech090_readiness_floor` (default `0.3`, calibratable), `use_commit_readiness`
  (default `False`, auto-armed `True` by `__post_init__` / `from_dims` OR-only resolver when
  the conjunction flag is on), `commit_readiness_window` (default `20`),
  `commit_readiness_ema_alpha` (default `0.1`), `commit_readiness_initial` (default `1.0`)
- **REEAgent.__init__:** instantiates `self.commit_readiness` when `use_commit_readiness=True`
- **REEAgent.select_action:** computes `_readiness_admits` once at the top of the
  beta-gate block; AND-composes with `BetaGate.should_admit_elevation(score_margin, K)`
  at *both* call sites (bistable + legacy). Block diagnostics advance via
  `commit_readiness.notify_block()` at the source.
- **REEAgent.reset:** calls `commit_readiness.reset()` per-episode (readiness returns to
  `commit_readiness_initial`).
- **Per-tick outcome-signal source:** Phase-1 seam is `notify_outcome(value)`. The
  experiment harness is responsible for pushing outcomes (e.g.
  `committed_mode_curriculum.run_p0_warmup` feeding its probe-derived `nav_competence`).
  Phase-2 follow-on (separate `/implement-substrate` pass): wire an env-emitted
  `mech090_readiness_outcome` key reading in `agent.sense()` so the substrate advances
  readiness automatically without harness involvement.

  **Phase-2 env-source follow-on -- DONE 2026-06-02.** The Phase-2 follow-on above
  is implemented. Crucially the Phase-1 `notify_outcome` seam was never actually
  exercised by any caller (`committed_mode_curriculum` computes `nav_competence`
  but does not push it; grep-verified zero callers repo-wide), so the across-tick
  axis sat fail-open (readiness pinned at the initial `1.0`) in every ecological
  run -- which is why `V3-EXQ-063a` deliberately left it OFF. The follow-on adds
  the automatic source:
  - **Env source:** `CausalGridWorldV2.mech090_readiness_outcome_enabled` (env-only
    kwarg, default `False`, NOT in `from_dims`). When `True`, `step()` emits
    `info["mech090_readiness_outcome"] = clip(1 - mean(limb_damage), 0, 1)` -- a
    `[0,1]` motor-program-readiness scalar that degrades with SD-022 limb damage
    (Cisek-Kalaska affordance-preparation: can the prepared motor program be
    executed) and recovers as damage heals. Absent-when-disabled (bit-identical OFF).
  - **Agent sink:** `REEAgent.sense(mech090_readiness_outcome: Optional[float] = None)`
    forwards the env value into `commit_readiness.update(outcome_signal=...,
    simulation_mode=hypothesis_tag)`. No-op when `commit_readiness is None` or the
    value is `None`. The `CommitReadiness` module is unchanged (its `update()`
    None-sentinel + simulation_mode gate already supported this).
  The across-tick axis is now exercisable ecologically for the first time. The
  Phase-1 `notify_outcome` seam remains for controlled-probe pushes (592b ARM_4).
  Validation: V3-EXQ-630 (ecological ARC-029 successor to 063a). Contract:
  `ree-v3/tests/contracts/test_mech090_readiness_outcome_wiring.py`. Substrate
  implementation log: `ree-v3/CLAUDE.md` "MECH-090 R-c continuation Phase-2
  follow-on" section.

### Composition with the score_margin gate

```
e3.select(...) -> E3SelectionResult.scores [K], .selected_index, .committed
       |
       +-- agent.py (both bistable + legacy branches):
       |       _readiness_margin    = sorted(scores)[1] - sorted(scores)[0]   (existing)
       |       _readiness_admits    = commit_readiness.is_above_floor(floor)  (NEW, AND-ed)
       |                              when use_mech090_readiness_conjunction
       |                              else True (legacy bit-identical)
       |
       +-- elevation admitted iff:
               result.committed
               AND BetaGate.should_admit_elevation(_readiness_margin, K)   (existing)
               AND _readiness_admits                                       (NEW)
```

The two gates are independently togglable: `use_commit_readiness_gate` controls the
within-tick score_margin gate; `use_mech090_readiness_conjunction` controls the
across-tick nav_competence gate. Both gates default OFF for bit-identical baseline.
Either flag alone reduces the conjunction to that single axis; both ON gives the full
R-c reading.

### Falsifiability

The two-axis composition admits independent falsification:

- score_margin-only PASS + nav_competence-only PASS + COMPOSED PASS on V3-EXQ-592b ->
  Either axis is sufficient; the literature corpus does not constrain which one.
  Open question deferred to a future Q-claim.
- score_margin-only PASS but nav_competence-only FAIL -> within-tick decisiveness
  is the load-bearing signal; nav_competence is not the right across-tick proxy
  (escalate to a Hanes-Schall-internal across-tick accumulator EMA).
- score_margin-only FAIL but nav_competence-only PASS -> across-tick competence is
  the load-bearing signal; within-tick margin does not actually catch the V3-EXQ-592
  degenerate basin (escalate to a Cisek-Kalaska affordance-preparation reading).
- Both axes FAIL on V3-EXQ-592b -> the substrate amendment is mis-targeted; the
  degenerate basin is admitted under both readings. Escalate to R-b conservative
  reading (rv-only entry + downstream propagation gate).

### Phase-1 scope limits

The Phase 1 instantiation is the simplest tractable instantiation of the across-tick
readiness signal: EMA over outcome signals plus a harness override seam. Three
candidate alternative readiness signals named in the user's invocation are deferred
unless the EMA-over-outcome-signals generalisation fails the V3-EXQ-592b acceptance:

1. **CEM accumulator-to-threshold readiness (Hanes-Schall direct analog).** Would
   require threading a per-candidate accumulator value through
   `HippocampalModule.propose_trajectories`; out-of-scope this pass. The
   notify_outcome seam can already plumb a harness-side accumulator if needed.
2. **Affordance-preparation readiness (Cisek-Kalaska direct analog).** Would require
   an affordance-competition layer that REE does not yet have; out-of-scope.
3. **Phasic dopaminergic burst on the leading candidate.** Would require wiring
   through `HippocampalModule.compute_completion_signal` which already maps to a
   different dopamine analog (`subiculum -> NAc -> VP -> VTA` loop per MECH-105).
   Collapsing the two dopamine analogs into one substrate is a separate governance
   question.

### Validation experiment (continued)

The V3-EXQ-592b arms documented above measure the score_margin axis. Additional arms
for the nav_competence axis to be queued in the same EXQ via `/queue-experiment`:

- **ARM_2 GATED_NAV_COMP_ON.** `use_mech090_readiness_conjunction=True`,
  `mech090_readiness_floor=0.3`, score_margin gate OFF. Harness pushes
  probe-derived `nav_competence` via `notify_outcome` each P0 probe tick.
  Same env + seed (42) as V3-EXQ-592. **Acceptance:** total committed steps == 0
  AND `commit_readiness.get_state()["n_blocks_emitted"] >= 1` AND
  `running_variance < commitment_threshold` at some point during the run
  (confirming the across-tick readiness gate is the load-bearing block, not an
  upstream rv failure).
- **ARM_3 GATED_BOTH_ON.** Both gates active. Same env + seed. **Acceptance:**
  total committed steps == 0 AND at least one gate's block counter >= 1
  (confirming the composed conjunction is at least as strict as either single
  axis).
- **ARM_4 BOTH_GATES_OFF + HARNESS_FORCES_READY.** Both gate flags off; harness
  pushes `notify_outcome(1.0)` each tick. **Acceptance:** total committed steps
  > 0 (legacy rv-only baseline preserved when both gates are off).

### MECH-094

Both `update` and `notify_outcome` honour the `simulation_mode` argument; the conjunction
itself is read-only at the elevate sites and is gated by `result.committed` (which is
already a waking signal). Replay / DMN consumers cannot inherit waking-only readiness.

### Backward compatibility

Verified: 523/523 contracts PASS (506 prior + 17 new MECH-090 R-c-nav-competence
contracts) with defaults unchanged. Master-OFF construction produces
`agent.commit_readiness = None` and the agent runs bit-identical to pre-amendment.
Master-ON with default `commit_readiness_initial = 1.0` produces readiness == 1.0
on first tick, so the conjunction admits while the EMA has no real outcome data
(fail-open). The conjunction begins blocking only once `notify_outcome` (harness)
pushes a low value or `update` drives the EMA below the floor via real outcome signals.

