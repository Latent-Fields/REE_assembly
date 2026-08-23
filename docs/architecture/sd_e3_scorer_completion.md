---
title: "SD-E3-SCORER-COMPLETION: predictors.e3_selector.untrained_fallback_scorers"
parent: "Core Engines & Forward Models"
grandparent: Architecture
nav_order: 12
---

# SD-E3-SCORER-COMPLETION: predictors.e3_selector.untrained_fallback_scorers

**Claim ID:** SD-E3-SCORER-COMPLETION
**Subject:** predictors.e3_selector.score_trajectory (reality_scorer, harm_cost_fallback_scorer)
**Status:** IMPLEMENTED
**Registered:** 2026-08-09
**Depends on:** (none unresolved)
**Blocks:** MECH-022 fair retest; ARC-007 (same E3-routed-selection seam)

## Problem

`E3TrajectorySelector.score_trajectory()` composes the trajectory score
`J = f_weight*F + lambda_eff*M + rho_residue*Phi_R (- benefit - goal)`. Two of
its cost sub-components read `nn.Sequential` heads that are **never touched by
any loss anywhere in `ree_core`** -- confirmed by exhaustive grep in
`failure_autopsy_V3-EXQ-190a_2026-08-09`:

- `reality_scorer` -- the `- viability` term in `compute_reality_cost` (F).
  Present on **every** scoring path.
- `harm_cost_fallback_scorer` -- the subtracted term in
  `compute_harm_cost_fallback` (M), present only on the **default fallback M
  path** used when neither `harm_forward_model` nor `harm_bridge` is supplied.

Both heads therefore contribute random-initialisation noise to every trajectory
score, in both conditions, for the whole run. Because `select() ->
score_trajectory` is on the **live agent action path** (`REEAgent.select_action`
-> `e3.select`), this perturbs the policy itself, not merely a diagnostic
readout. It contaminated MECH-022's V3-EXQ-190a well-powered test: C1/C2/C3 all
FAILed where predecessor V3-EXQ-190 had cleanly PASSed C1/C2, including a **sign
flip on a repeated seed** (123: +0.0168 -> -0.00706). The autopsy rejected the
manifest's self-declared `retire_ree_claim` on the grounds that the claim was
not tested fairly.

This is the textbook shape of "an implementation that has the symbol of the
mechanism but not its functional role": the architecture correctly assigns
value-computation to E3, but two of E3's scoring sub-components were never wired
to a training signal.

## Solution

Gate both untrained heads' **contribution** to the score behind a single
`E3Config` flag, `e3_include_untrained_fallback_scorers` (default **False = the
fix**).

- **Default (False):** `compute_reality_cost` returns the parameter-free
  coherence (transition-smoothness) proxy alone; `compute_harm_cost_fallback`
  returns the **trained** `harm_eval_head` sum alone. Neither untrained head
  influences the score.
- **Legacy (True):** restores the pre-2026-08-09 behaviour bit-identically, for
  exact reproduction of an old run only.

The `nn.Sequential` heads remain **instantiated** so `state_dict` / checkpoint
keys are unchanged; only their contribution is gated. This mirrors the
`benefit_eval_head` warmup-gate idiom already in `e3_selector.py`, which gates an
untrained head out of selection "to prevent random-init noise from corrupting
trajectory selection early in training."

**Wire vs remove decision:** removal (gating out), not wiring. Wiring would
require inventing training labels for "final-state viability" and a "fallback
harm" signal distinct from the already-trained `harm_eval_head` -- unspecified
architecture beyond this SD's scope. If such a signal is later designed, the
heads are still present and their contribution can be re-enabled behind that
training, not behind this flag.

**Default-is-the-fix inversion:** the default deliberately departs from the
usual E3Config "False = bit-identical legacy" convention, because here the legacy
behaviour *is* the defect. Making the fix opt-in would leave every experiment
silently contaminated by default -- exactly the trap the autopsy diagnosed.

### Data flow

```
score_trajectory
  F: compute_reality_cost(traj)
       default -> coherence_cost                       (parameter-free)
       legacy  -> coherence_cost - reality_scorer(final)   (UNTRAINED head)
  M (fallback path only):
     compute_harm_cost_fallback(traj)
       default -> sum(harm_eval_head(states))          (TRAINED head)
       legacy  -> sum(harm_eval_head(states)) - harm_cost_fallback_scorer(final)
```

Config: `E3Config.e3_include_untrained_fallback_scorers` (default `False`;
set `cfg.e3.e3_include_untrained_fallback_scorers = True` per-arm for legacy --
not wired through `REEConfig.from_dims()`, following `f_weight`'s precedent).

## Architecture Context

Touches only the E3 trajectory-scoring path. No new latent field, encoder, or
obs channel. No phased-training requirement (nothing new is trained). MECH-094
does not apply (no simulation/replay content written to memory). ML/AI parallel:
this is the standard "do not let a randomly-initialised auxiliary head into the
selection objective before it has a training signal" hazard -- the same reason
target networks and warmup gates exist; the REE substrate already applies it to
`benefit_eval_head`, and this SD extends the same discipline to the two heads
that were missed.

## What This SD Enables

- A **fair** retest of MECH-022 (hypothesis injection) whose C1/C2/C3 are no
  longer read through random-init noise.
- Cleaner evidence on ARC-007, which was demoted 2026-07-25 on the same
  E3-routed-selection seam.

## Validation

`ree-v3/tests/contracts/test_e3_scorer_completion.py` (5 tests): asserts the
default gates both heads off (re-randomising their weights leaves the default
score bit-identical), with a legacy-flag negative control proving the test is
not vacuous, plus direct checks that `compute_reality_cost` == coherence-only
and `compute_harm_cost_fallback` == the trained-head sum by default. The defect
is a deterministic property (does the score depend on these heads' parameters?),
so a contract test validates it directly and permanently -- no stochastic
experiment is required for the substrate-readiness check.

## Retest follow-on (governance-gated, NOT queued by this SD)

The MECH-022 full retest is `pending_retest_after_substrate: true` in
`substrate_queue.json` and is for governance to ratify and queue. When it is
queued, per the autopsy's Section 6 it MUST preserve full condition-dependence
in eval: **raise `eval_episodes`, do NOT apply the `nav_bias` forced-random
override inside the eval loop.** V3-EXQ-190a's eval loop added that override
(self-labelled "the deliberate C4 fix"; predecessor V3-EXQ-190's eval loop was
pure `select_action`), which fixed C4's harm-contact floor but diluted exactly
the condition-dependent behavioural signal C1/C2/C3 measure -- a plausible
co-cause of C1's PASS->FAIL collapse independent of the untrained-head
contamination this SD fixes. Both issues must be addressed before MECH-022 is
adjudicated on this seam.

## Related Claims

MECH-022 (hypothesis injection gated by control plane), ARC-007 (E3 value
computation), ARC-016 (dynamic precision -- same selector). Motivating record:
`REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-190a_2026-08-09.md`.
