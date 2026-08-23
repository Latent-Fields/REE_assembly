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
