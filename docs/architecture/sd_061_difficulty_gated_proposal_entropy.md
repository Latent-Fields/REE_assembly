---
title: "SD-061: difficulty_gated_proposal_entropy"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 18
status: candidate/v3_pending
status_asof: 2026-07-10
status_claim: SD-061
---

# SD-061: difficulty_gated_proposal_entropy

**Claim ID:** SD-061
**Subject:** control_plane.difficulty_gated_proposal_entropy
**Status:** IMPLEMENTED (2026-06-19; v3_pending until the validation experiment PASSes)
**Registered:** 2026-06-19
**Depends on:** ARC-018 (hippocampal/CEM proposal layer), modulatory-bias-selection-authority (E3.select authority — IMPLEMENTED), MECH-090 / MECH-342 (commitment predicates), MECH-341 (E3 score-diversity preservation), SD-032b (dACC choice_difficulty)
**Blocks:** MECH-343 (difficulty_gated_proposal_entropy mechanism — its `substrate_conditional` blocker part 2), Q-056 (the 3-arm stuck-gated-vs-constant-entropy falsifier)

## Problem

MECH-343 (the difficulty_gated_proposal_entropy mechanism) is `substrate_conditional`
/ `v3_pending`. Its own `evidence_quality_note` names the two upstream pieces it is
blocked on: **(1)** the modulatory-bias-selection-authority gap — *now IMPLEMENTED*
(the 569i top-k shortlist conversion gives modulatory/diversity signals genuine
authority at E3.select); and **(2)** *"a difficulty-gated proposal-entropy regulator
(stuck-state detector + transient CEM temperature/candidate-count gain + decay) not
yet designed."* SD-061 is piece (2).

What V3 had: `noise_floor.py` (MECH-313) — a **state-independent** uniform temperature
lift on the **action-selection** softmax; `dacc.py` — a `choice_difficulty` **signal**
(std of per-candidate EVs); `salience_coordinator.py` — routes `dacc_difficulty` to an
`internal_planning` bias. None of these is a closed loop that (a) detects a
stuck-with-a-goal state and (b) transiently widens the **proposal-generation** entropy
in response, decaying after the impasse clears. Q-056's 3-arm falsifier (entropy-off /
stuck-gated / always-high) would be vacuous against a non-existent mechanism.

## Solution

Two coupled no-op-default modules; OFF = bit-identical to the current substrate.

### Component 1 — `StuckStateDetector` (`ree_core/cingulate/stuck_state_detector.py`)

Integrates four signals REE already computes into a graded `stuck_score ∈ [0,1]` plus
binary `is_stuck`, GUARDED by goal salience:

| axis | source | deficit (higher = more stuck) |
|------|--------|-------------------------------|
| goal-progress stall | `GoalState.goal_proximity` over a window | improvement ≤ `progress_stall_eps` → full deficit |
| decision impasse | E3 first-action margin (`sorted(scores)[1]-[0]`) | `clip((margin_floor − margin)/margin_floor)` |
| committed lock-in | unique-class fraction over a recent committed-action window | `clip((div_floor − frac)/div_floor)` |
| choice ambiguity | dACC `choice_difficulty` (std of EVs; small spread = hard) | `clip((diff_ref − choice_difficulty)/diff_ref)` (inverted) |

Present-axis deficits combine by `mean` (default) or `max`. The combined evidence is
gated by goal salience — when no goal is pursued (`goal_salience < goal_salience_floor`)
the tick contributes **0** (absence of progress without a goal is rest, not impasse —
the *stuck-with-goal* distinction MECH-343 insists on). The gated evidence drives an
**asymmetric EMA** (`ema_alpha_rise ≫ ema_alpha_fall`) so `stuck_score` rises quickly
and decays slowly — the hysteretic "entropy narrows once a workable candidate is found"
behaviour. `is_stuck = stuck_score ≥ stuck_threshold`.

### Component 2 — `DifficultyGatedProposalEntropy` (`ree_core/policy/difficulty_gated_proposal_entropy.py`)

Maps `stuck_score` to a transient gain on the **proposal layer**:

```
extra_candidates = round(candidate_widen_max * stuck_score)     # ARC-018 CEM candidate-set widening
temperature_gain = 1.0 + temperature_gain_max * stuck_score     # within-class CEM sampling temperature
```

At `stuck_score = 0` the gain is identity → bit-identical proposal. Scoring,
commitment thresholds (MECH-090/342), and selection authority (569i top-k / MECH-341)
are **untouched** — a hard problem triggers *wider internal proposals*, not random
behaviour. The decay is carried by the detector's asymmetric EMA (entropy narrows as
the impasse clears).

### Data flow

```
[detector inputs at select_action end]
  goal_proximity, score_margin, committed_action_class, dacc.choice_difficulty, goal_salience
    -> StuckStateDetector.update() -> agent._last_stuck_score        (one-tick lag seam)
[_e3_tick, next tick]
  DifficultyGatedProposalEntropy.compute_proposal_gain(_last_stuck_score)
    -> (extra_candidates, temperature_gain)
    -> HippocampalModule.propose_trajectories(num_candidates += extra,
         differentiable_cem_temperature *= gain  [transient, restored in finally])
    -> E3 scores + 569i top-k authority + MECH-341 preserver  [UNCHANGED]
```

### Config (all no-op default; `REEConfig` + `from_dims`)

`use_difficulty_gated_proposal_entropy` (master, False); detector:
`stuck_progress_window` (8), `stuck_progress_stall_eps` (0.01), `stuck_score_margin_floor`
(0.05), `stuck_committed_diversity_window` (8), `stuck_committed_diversity_floor` (0.34),
`stuck_choice_difficulty_ref` (0.05), `stuck_goal_salience_floor` (0.05),
`stuck_ema_alpha_rise` (0.3), `stuck_ema_alpha_fall` (0.05), `stuck_threshold` (0.5),
`stuck_combine_mode` ("mean"); regulator: `dgpe_candidate_widen_max` (8),
`dgpe_temperature_gain_max` (1.0).

### Backward compatibility

`use_difficulty_gated_proposal_entropy=False` by default → both modules are `None`; the
`_e3_tick` proposal-gain block and the `select_action` detector-update block are skipped
→ bit-identical (verified: default == explicit-False action stream). 8/8 contracts
(`tests/contracts/test_sd_061_difficulty_gated_proposal_entropy.py`) + preflight + full
contract suite green with the master flag OFF.

### MECH-094

Both modules' state-advancing methods take `simulation_mode` and no-op when True (a
replay/DMN tick must not accumulate waking impasse or widen an imagined proposal).
Matches the SD-035 / MECH-279 / MECH-313 / MECH-320 / MECH-342 pattern.

### Phased training

N/A — both are pure-arithmetic regulators with no learned parameters; the only
"learning" is the detector's eligibility-style EMA. No encoder head, no gradient flow.

## What This SD Enables

- MECH-343 blocker part 2 → built. With part 1 (modulatory authority) already
  implemented, MECH-343's `substrate_conditional` block is cleared at the substrate
  level (promotion still requires the Q-056 evidence experiment).
- Q-056 (the 3-arm stuck-gated-vs-off-vs-always-high falsifier) becomes buildable
  against a real mechanism.

## Architecture Context

Distinct from MECH-313 (state-independent action-selection noise floor), from MECH-342
(release-pressure on an *already-committed* latch — opposite end of the commitment
loop), and from a raw dACC `choice_difficulty` readout (integrated + goal-gated, acting
on the proposal layer). It is the proposal-generation-side complement to the
selection-side diversity stack (569i top-k, MECH-341).

## Related Claims

MECH-343 (parent mechanism), ARC-018 (proposal locus), modulatory-bias-selection-authority
(blocker part 1, implemented), MECH-341 / ARC-062 (downstream selection-side diversity),
MECH-090 / MECH-342 (commitment predicates, untouched), SD-032b (dACC choice_difficulty),
MECH-313 (state-independent sibling; distinct), Q-056 (the falsifier), MECH-094
(simulation gate).

---

## 2026-09-18 amendment (GFLAG-0352): the temperature half had no live consumer

**Two statements above were wrong in a way that misled the evidence record.** Both are
corrected here rather than edited out, because the shape of the error is the reason for the
diagnostics added alongside the fix. Measurement record:
`REE_assembly/evidence/planning/exq1056_mech343_q056_upstream_leg_design_refusal_20260918.md`.
Substrate change: ree-v3 `6ba3eb96a1`. **PROMOTES NOTHING** -- MECH-343 stays
`candidate` / `substrate_conditional` / `v3_pending`.

### (a) `differentiable_cem_temperature *= gain` reached nothing

The data-flow block above ends with

```
    -> HippocampalModule.propose_trajectories(num_candidates += extra,
         differentiable_cem_temperature *= gain  [transient, restored in finally])
```

The mutation happens. The **read** does not. `differentiable_cem_temperature` has exactly
one consumer in `ree_core` -- `HippocampalModule`'s CEM refit -- and it sits inside SD-055's
`if getattr(self.config, "use_differentiable_cem", False):`, default **False**.
`use_differentiable_cem` appears in **none** of: the **Config** section above (which
enumerates all 13 SD-061 knobs), the ree-v3 substrate record, SD-061's or MECH-343's
`what_would_answer`, or V3-EXQ-694's driver.

So at every configuration this document names, SD-061's effective manipulation was
**candidate-COUNT widening alone**. V3-EXQ-694's C2 "regulator load-bearing" PASS therefore
certified the count half only -- while SD-061's `what_would_answer` criterion (2) reads as
certifying that the regulator "lifts `differentiable_cem_temperature` transiently".

**Fix.** New knob `dgpe_enable_differentiable_cem` (default `False`; `REEConfig` +
`from_dims`). True alongside the master flag -> `REEAgent.__init__` sets
`hippocampal.use_differentiable_cem = True`. Default-off is bit-identical, so V3-EXQ-694
still reproduces exactly.

**Fix that matters more.** `DifficultyGatedProposalEntropy.get_state()` now reports
`sd061_temperature_lever_consumer_live` and `sd061_temperature_half_inert`. A manifest
carrying the regulator state now says whether the half acted, so the 694-class error cannot
recur silently.

**Measured scope of the coupled lever -- do not over-read the fix.** Isolating the
temperature (count lever off, `dgpe_candidate_widen_max=0`): *uncoupled*, the proposed
candidate set is **bit-identical** at `stuck_score` 1.0 vs 0.0 (max abs diff exactly 0.0);
*coupled*, action-OBJECT content moves by ~1.2e-5 while the candidate **first-action-CLASS**
distribution is **unchanged**. The class is a coarse argmax and a perturbation that small
essentially never flips it. So the coupling makes the lever live; it does **not** make it
able to move `candidate_first_action_entropy` -- the DV criterion (3) and MECH-343's
upstream leg (a) both name. In the same measurement, the only thing that moved that DV was
the COUNT lever, in **both** directions across successive proposals -- consistent with
V3-EXQ-694's "count-widening is silent-to-adverse on entropy". Pinned by contract `C13b`.

### (b) Two of the five declared detector inputs never arrive

The data-flow block lists the detector inputs as
`goal_proximity, score_margin, committed_action_class, dacc.choice_difficulty, goal_salience`.
Measured over an ecological loop (`REEConfig.goal_stream` + `CausalGridWorldV2`, agent
selecting its own actions): 100/100, 99/100, **0/100**, **0/100**, 100/100.

`choice_difficulty` (the SD-032b axis) needs **four** conditions, not one --
`REEAgent.select_action` writes `_dacc_last_bundle` only inside
`if self.dacc is not None and z_harm_a is not None:`

1. `use_dacc=True` -- constructs `agent.dacc`;
2. `use_affective_harm_stream=True` -- constructs the `AffectiveHarmEncoder` producing `z_harm_a`;
3. the environment must emit `harm_obs_a` (`CausalGridWorldV2` does);
4. **the driver must forward it**: `agent.sense(..., obs_harm_a=...)`. `act_with_split_obs`
   calls `sense(obs_body, obs_world)` with no harm channel, so a driver on that convenience
   interface can **never** populate the axis, at any config. `experiments/_harness.py`,
   `experiments/_lib/allon_training.py` and `_lib/baselines/*` forward it correctly.

`use_dacc=True` was deliberately **not** made sufficient: forcing `use_affective_harm_stream`
on would instantiate an `nn.Module` encoder, changing the parameter set and the RNG stream,
which is not bit-identical. The requirement is recorded instead (user decision, 2026-09-18).

`committed_action_class` needs a commitment to have occurred (a beta elevation), which runs
into MECH-342's registered open failure (V3-EXQ-629, "no natural commit when score margins
are flat") -- a connected failure MECH-343's own notes already cite.

**Why it bites arithmetically.** The combine is a mean over **PRESENT** axes, so which axes
arrive sets the *attainable maximum* of `stuck_score`. With the progress axis saturated at
1.0 and the margin axis at 0.0, evidence is exactly `mean(1.0, 0.0) = 0.5` -- identical to
the default `stuck_threshold`, approached from below by the EMA, so `is_stuck` **never
fires** (measured duty cycle 0.000 in every arm). And `last_deficit_*` was 0.0 for both an
absent axis and a present-but-zero one, so a null was unattributable between "not stuck" and
"the axes that would have said so never arrived".

**Fix (diagnostics only; `update()` arithmetic untouched).** `StuckStateDetector.get_state()`
now reports `sd061_last_present_{progress,margin,diversity,difficulty}`, `sd061_n_present_*`
and `sd061_n_axes_present_last`.

### (c) Deliberately NOT decided here

What the detector should do when axes are absent -- an axis mask, a minimum-present-axes
requirement, or a threshold recalibration -- and which axes ought to carry the firing,
determine what "stuck" **means**, and are therefore a scientific decision rather than a
build one. Raised as a decision chip. **Do not queue Q-056 until (c) is answered.**

---

## 2026-09-19 amendment (c): the declared axis mask

**User decision, 2026-09-19 (option 1 of the (c) chip).** ree-v3 `f372ce4207`.
**PROMOTES NOTHING**; Q-056 is still not queued.

### What was decided, and what was rejected

A run **declares** which detector axes are in scope. The combination is taken over
exactly the declared set -- an undeclared axis is ignored even when its input
arrives, so the denominator is fixed by the declaration and cannot drift with
instrumentation. A declared axis that is not wired **refuses** the run
(`StuckStateAxisUnavailable`) rather than silently rescaling.

**Threshold recalibration was considered and REJECTED.** Scaling the threshold by
the present-axis count would let `is_stuck` fire again without making the trigger
attributable, and would redefine "stuck" as a function of instrumentation rather
than of the agent's state.

`declared_axes=None` (the default) is the legacy mean-over-present behaviour,
bit-identical, so nothing already recorded changes meaning.

### The grace window

`declared_axis_grace_ticks` (8) exists because "absent" has two causes. The first
implementation refused on any tick with a `None` input, and the ecological probe
caught the flaw immediately: `score_margin` is `None` on the **first tick only**
(until `e3.last_scores` exists), which made `margin` undeclarable by any driver.
So an axis unseen *inside* the window is UNDETERMINED -- no advance, and **no
partial combination is formed**, so the anti-rescale guarantee holds absolutely;
still unseen *after* it is NOT WIRED and refuses; and an axis seen earlier that
goes missing refuses at once. The knob can only change *when* a mis-wired run is
told, never a measured quantity (contract `C26`).

### Measured, on the loop the 2026-09-18 baseline used

| `declared_axes` | stuck_score range | duty(`is_stuck`) | note |
|---|---|---|---|
| `None` (legacy) | 0.0000 - 0.5000 | 0.000 | baseline reproduced exactly |
| `("progress",)` | 0.0000 - 1.0000 | 0.980 | peak at the LAST tick; no decay |
| `("progress","margin")` | 0.0000 - 0.5000 | 0.000 | = the axes that arrive |
| `("progress","difficulty")` | -- | -- | REFUSED after 9 ticks |

**Neither declarable axis set gives a usable trigger, and for opposite reasons.**
`("progress","margin")` never fires (G9 pole A). `("progress",)` fires on 98% of
ticks, peaks on the last tick and never decays (G9 pole B). MECH-343 requires a
peak that exceeds threshold **and then decays**, and a pinned-high score turns
every arm contrast into a DOSE contrast rather than a TIMING one.

So the mask delivers what the decision asked for -- a declared, attributable
trigger with no silent rescale -- but it does **not** by itself make Q-056
non-vacuous. **Which axes Q-056 declares is a live scientific choice, deliberately
not taken here**, and is raised as a decision chip together with the separate
finding that the now-coupled temperature lever does not move the registered
first-action-class DV.
