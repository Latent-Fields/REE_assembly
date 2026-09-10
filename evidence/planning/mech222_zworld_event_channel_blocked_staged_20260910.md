**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry).**

# EXP-0893 / MECH-222 -- why no experiment was queued, and what is owed first

- **Date (UTC):** 2026-09-10T21:00:59Z
- **Chip:** `chip-proposal-exp-0893`
- **Proposal:** EXP-0893 (`backlog_id` EVB-1462, `proposal_type` experimental)
- **Claims:** MECH-222 (primary, per the proposal file), MECH-221 (co-tagged mechanism)
- **Disposition:** `blocked_substrate`. **No queue entry was created.** EXQ ID
  V3-EXQ-1018 was reserved and has been released.
- **Driver written and left on trunk (NOT queued):**
  `ree-v3/experiments/v3_exq_1018_mech222_self_attribution_contamination.py`

> **Brief correction.** The dispatch brief named MECH-221. The proposal entry's own
> `claim_id` is **MECH-222**; MECH-221 is EXP-0891. The proposal file was treated as
> authoritative and both claims were co-tagged, since the design ablates MECH-221's
> mechanism to test MECH-222's consequent.

## 1. What was built

A 3-arm x 5-seed diagnostic ablating the substrate's continuous z_world
residualization:

- `ARM_RESID_ON` -- `reafference_action_dim = action_dim`; the trained
  `ReafferencePredictor` (SD-007 / MECH-098 / MECH-101) subtracts
  `dz_world_loco = f(z_world_raw_prev, a_prev)` on every encode tick
  (`ree_core/latent/stack.py:1462-1483`), which is MECH-221's "continuous" in the
  literal sense: `REEAgent.sense` passes `prev_action` every tick
  (`ree_core/agent.py:4777`).
- `ARM_RESID_OFF` -- predictor set to `None` after P0 (the MECH-221 failure condition).
- `ARM_SHAM_RESID` -- matched-noise control subtracting the same module's output with
  the action mis-paired.

The mechanism is present, wired, and trainable. **The substrate is not missing the
manipulation.** What it is missing is a measurable dependent variable.

## 2. The blocking finding

MECH-222's testable content is that contamination of `z_world` has a *downstream
consequence*: a consumer reading `z_world` can no longer tell an exogenous world event
from the agent's own doing. Every such DV requires that `z_world` carry
exogenous-world-event information at all. **It does not.**

This is already recorded in the substrate, and was reproduced here independently.
`ree_core/latent/zworld_p0.py` (SD-070 recipe docstring, measured 2026-07-18 on this
substrate) states that transition-type information is **at or below chance** in the
`world_obs` channel that `z_world` encodes:

```
world_obs  (what z_world sees)   -0.014  (3-class)   -0.060  (6-class)
body delta (routed to z_self)    +0.240               +0.427
```

with the stated cause: `z_world` is a **static single-frame** encoding, and SD-005's
split encoder deliberately routes the body delta -- where the transition information
actually lives -- to `z_self`, so "z_world structurally cannot see it."

## 3. Independent measurements taken here (all on this substrate, seed 42 unless noted)

| # | Measurement | Result | Reading |
|---|---|---|---|
| 1 | `ReafferencePredictor` held-out R2 on pure self-motion transitions, 4000 grad steps | **0.34 - 0.40** (3 seeds) | mechanism trains fine |
| 2 | R2 with mis-paired action (what SHAM subtracts) | **-2.94**; cos(real, sham) = **0.59** | SHAM is a genuine control |
| 3 | Drift-detection probe AUC from `dz_world`, clock-locked hazard drift | 0.53 - 0.63 | near chance |
| 4 | Same, after training the encoder on E1+E2 losses | 0.58; **training loss collapsed to 0.00000** | representation collapse, matching `zworld_p0.py`'s recorded PR 9.21 -> 1.06 |
| 5 | Stationary positive control AUC at the shipped budget (3 seeds) | **0.488 / 0.550 / 0.570** | 2 of 3 below the 0.55 readiness floor |
| 6 | Graded DV: held-out Spearman(`dz_world` -> exogenous move COUNT), clock-independent channel | **0.03, -0.03, -0.02, 0.01, 0.20, 0.07** | chance |

Rounds 3-6 span frozen and trained encoders, binary and graded DVs, and clock-locked
and clock-independent exogenous channels. All land at chance.

## 4. Two design defects found and fixed en route (recorded so they are not re-derived)

- **Off-by-one delta/label alignment.** `z_{t+1} - z_t` is produced by the transition
  at `t` and must carry `t`'s labels. Labelling it with `t+1`'s pushes every AUC to
  chance. Fixed in the driver; called out in its docstring.
- **`z_world_raw` is PRE-EMA as well as pre-correction** (`stack.py:1462`). With the
  predictor disabled entirely, `z_world != z_world_raw` on 38/38 probed steps -- the
  difference is the `alpha_world` EMA, not the correction. A within-run
  `z_world - z_world_raw` contrast measures smoothing and would be misread as
  residualization. The arms are the only valid contrast.

## 5. Red-team (Step 4.5)

Ran on the session model; the `fable` override returned HTTP 429 (monthly spend limit),
and the skill's documented fallback was used. **Verdict: BLOCKING.**

| Finding | Disposition |
|---|---|
| F-B: exogenous label is collinear with step phase (`causal_grid_world.py:3148`, `steps % env_drift_interval == 0`; at 8 hazards x p=0.8, P(event\|tick) = 0.99999744, i.e. exactly step parity) | **CONFIRMED.** Verified from source and by arithmetic. Fatal to the original DV. |
| F-C / F-F: `moved` AUC exceeds the `stationary` control, inverting the design premise; worst-cell control straddles its floor | **CONFIRMED** by measurement 5 above -- worse than the reviewer estimated. |
| F-D: verdict grid's `elif not c1` fires before C3, so a failed attribution control records `weakens` | **CONFIRMED** by code read. Real defect; would have been fixed had the run proceeded. |
| F-H: episodes terminate on health depletion well before `STEPS_PER_EPISODE`; calibration figures predated an eval-episode change | **CONFIRMED.** Mean episode length 21-47 vs a nominal 60. |
| F-A: "SHAM is ~98.5% identical to the real correction, so C3 can never pass" | **DISMISSED** by measurement 2. The reviewer's closed-form *linear* ridge underestimated the shipped *nonlinear* MLP's action sensitivity. |
| F-E: R1 certifies a fit with no self-content | **DISMISSED**, same evidence. |

F-B was solved: `_step_background_drift` (`causal_grid_world.py:4785`) runs **every
step** with a per-source Bernoulli, not on a clock tick, and measured clock-parity AUC
on that channel is 0.46-0.54 (clean). It did not rescue the experiment -- the DV is at
chance there too (measurement 6).

## 6. What is owed before MECH-221 / MECH-222 are testable

A `z_world` that demonstrably encodes world content, and specifically enough of it that
an exogenous world event is decodable from the downstream stream.

- SD-070 (`ree_core/latent/zworld_p0.py`) is the existing repair recipe, but it targets
  **static, single-frame properties of `world_obs`** by construction. A correctly
  SD-070-trained `z_world` would therefore still not make a *transition* decodable, so
  SD-070 alone does not clear this gate. This should be confirmed rather than assumed.
- The deeper question is architectural and is MECH-221's own: if the body delta is
  routed to `z_self` by SD-005, what is the intended pathway by which a downstream
  consumer of `z_world` ever perceives an exogenous event? MECH-222 presupposes such a
  pathway. Until it is named and built, the claim's consequent has no observable.

**Route:** `/implement-substrate`, not another `/queue-experiment` iteration. A chip has
been raised.

## 7. Recommended registry edits (NOT applied beyond the proposal-status field)

Applied: `experiment_proposals.v1.json`, item `(EVB-1462, experimental)` ->
`status: "blocked_substrate"` with `blocked_by` / `blocked_note`.

Not applied, for a human to decide:
- whether MECH-222 / MECH-221 should carry an explicit "no observable DV in V3"
  annotation in `claims.yaml`;
- whether the sibling proposals EXP-0891 (MECH-221), LIT-0892, LIT-0894 are blocked by
  the same gate -- EXP-0891 very likely is, but it was not audited here.
