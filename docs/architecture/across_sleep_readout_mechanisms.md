---
status: candidate/v3_pending
status_asof: 2026-09-22
status_claim: MECH-572
---

# Across-Sleep Readout Mechanisms (INV-063 leg B)

**Status:** architecture stub. Registered by the CDQ-011 Mine+Register pass of the Convergence
Demand Pipeline, 2026-09-22, session `pensive-feistel-471e3c`.
**Claims:** MECH-572 (lead), MECH-573, MECH-574 -- all `candidate`, `implementation_phase: v3`,
`v3_pending: true`, wired into `INV-063.depends_on`.
**Row:** CDQ-011, `evidence/planning/convergence_demand_queue.v1.json`.
**Registration is not build authorisation.** INV-063 is `epistemic_category:
substrate_conditional`; no experiment is queued and V3-EXQ-1071 stays reserved and unused.

---

## 1. The question, and why it is not a question about objectives

INV-063 leg B needs a readout on `agent.e2.world_forward` that is simultaneously

- **(i) READABLE** on a converged base -- not sitting at its chance or degenerate value; and
- **(ii) CORRECT-SIGNED** -- the across-sleep delta positive at that same setting.

Two objectives have been measured and each fails one:

| Candidate | (i) readable | (ii) positive across sleep |
|---|---|---|
| 701b/701c per-element MSE reconstruction | yes | **no** -- worse 9/9 cells on a converged base (V3-EXQ-1063) |
| SD-056 InfoNCE frozen battery | needs `tau <= 0.01` | needs `tau >= 0.03` -- **no overlapping window** (GFLAG-0382) |

Governance de-pinned leg B on 2026-09-22 and restated it as a requirement rather than an
objective. CDQ-011 then forbade a third objective, on the grounds that two failures on the same
framing indict the framing.

**This stub's answer: the readout was never the free variable.** The bind is produced by the
consolidation pass's OPTIMISER and by the REFERENCE the readability gate uses -- neither of which
changes when the objective changes. That is why substituting InfoNCE for MSE reproduced the bind
instead of dissolving it.

## 2. MECH-572 (lead) -- the step-to-residual ratio governs the sign

`CrossModuleConsolidator.consolidate()` builds a **fresh** `torch.optim.Adam` on every call, by
design ("built fresh each call so the pass owns no persistent optimiser state",
`ree-v3 ree_core/sleep/cross_module_consolidation.py`). A fresh Adam's bias-corrected first step is
`~ lr * sign(g)` **regardless of `|g|`**, so the displacement is bounded by
`n_steps * lr = 8 * 1e-3 = 0.008` whatever the gradient is.

Measured, from the landed V3-EXQ-1063 manifest:

| arm | seed | conv_rel_drop | residual (battery MSE) | `world_head_max_abs_delta` | % of 0.008 bound | across-sleep delta |
|---|---|---|---|---|---|---|
| CONV_ON | 42 | 0.99802 | 1.49e-05 | 0.008053 | 100.7% | **negative** |
| CONV_ON | 123 | 0.99670 | 9.28e-06 | 0.008070 | 100.9% | **negative** |
| CONV_ON | 456 | 0.99917 | 9.63e-06 | 0.008034 | 100.4% | **negative** |
| FRESH_ON | 42 | 0.0 | 7.51e-03 | 0.008009 | 100.1% | **positive** |
| FRESH_ON | 123 | 0.0 | 2.81e-03 | 0.008067 | 100.8% | negative |
| FRESH_ON | 456 | 0.0 | 1.16e-02 | 0.007978 | 99.7% | **positive** |

The displacement is **identical to three significant figures across a ~1000x range of residual**.
It is set by the optimiser, not by the loss and not by how converged the head is.

On the converged base the first-cycle MSE rise is **18.2x, 41.3x and 19.7x** the residual it was
supposed to be reducing. The pass overwrites the residual; the measured "sleep degrades the
readout" is that overwrite.

**Why this makes (i) and (ii) structurally opposed.** (ii) needs the residual large relative to the
displacement. (i) drives the residual toward zero. With a displacement that does not scale with
convergence, satisfying one defeats the other -- **for any objective**.

The external anchor is DreamerV3's free bits: "clipping the dynamics and representation losses
below the value of 1 nat", a floor on **optimiser effort**, so an already-sufficient term stops
producing gradient. REE's consolidator has no such floor and takes its fixed 8 steps regardless.
(`REE_convergence/sources/dreamer-v3/consolidation_readout_alignment.md`, DREAMER-V3-OBJ-007.)

## 3. MECH-573 -- readability must be referenced to the TRIVIAL predictor

`conv_rel_drop` is normalised by the **random-init** battery MSE. Random init on a forward model is
vastly worse than simply copying the input, so `conv_rel_drop >= 0.99` is satisfiable while the head
sits at its degenerate value.

Measured, from the same landed manifest (`identity_predictor_mse = mean((z1-z0)^2)`, already
recorded per cell):

| seed | conv_rel_drop | model MSE | identity MSE | ratio | skill `1 - model/identity` |
|---|---|---|---|---|---|
| 42 | 0.99802 | 1.487e-05 | 1.388e-05 | 1.071 | **-0.071** |
| 123 | 0.99670 | 9.282e-06 | 1.201e-05 | 0.773 | +0.227 |
| 456 | 0.99917 | 9.628e-06 | 9.565e-06 | 1.007 | **-0.007** |

The "converged" head is **at or below copy-the-input on 2 of 3 seeds**. A pass cannot improve what
is not there, which is the most economical account of deltas as small as -7.14e-05.

This is the REE form of Ellenbogen et al. 2007: trained premise-pair retention was above 85% in
every group with no differences -- at ceiling, a degenerate value -- while the held-out inference
probe carried the whole effect. Reporting only the trained measure would have licensed
"sleep does nothing", which the held-out probe falsifies.

**Offered to governance, not applied here:** requirement (i) should additionally require skill > 0
against `identity_predictor_mse`. That is a falsifier edit and belongs to a governance cycle.

## 4. MECH-574 -- replay must REGENERATE a target, not re-present one

MuZero Reanalyze "revisits its past time-steps and re-executes its search using the latest model
parameters, potentially resulting in a better quality policy than the original search"; that
re-derived target drives 80% of updates. Replay is productive because it regenerates a **better**
target, not because it re-shows stored data.

`compute_e2_world_loss` draws `(world[i], action[i+1], world[i+1])` from the replay buffers and
descends against the **originally observed** next state, unchanged every cycle. Against a target
the head already matches, the gradient carries no information and only the optimiser's displacement
remains.

MuZero's operator (MCTS over a reward-bearing action space) does not port -- REE has no planning
operator over world states. The REE-available regenerators are **k-step consistency**
(`world_forward_contrastive_loss_multistep` already exists) and harder in-batch negatives.

## 5. How the three separate, and the cheapest next measurement

MECH-572 and MECH-574 are the same observation with different operators -- optimiser vs replay
content -- and they are **separable on one two-by-two**: MECH-572 predicts the delta tracks the
displacement-to-residual ratio regardless of target novelty; MECH-574 predicts it tracks target
novelty regardless of step size.

**Cheapest first, and it needs no run at all:** MECH-573 is already decided by the landed manifest
(section 3). If the converged base is at or below the trivial predictor, leg B is blocked *upstream*
of the readout question, and neither MECH-572 nor MECH-574 is worth a run until a base with
positive skill exists. That ordering should be respected.

## 6. CORRECTION OF RECORD -- what these claims are NOT

A landed artifact asserted that "InfoNCE is insensitive to a global scale/shift of the prediction,
so it can improve while frozen-battery MSE does not move". **That is false for this
implementation**, and V3-EXQ-1063's own header already refuses it: the logits are
`-||pred_j - target_i||^2 / tau`, squared L2 distances rather than dot products or cosines, so a
global scale changes every distance and a global shift leaves a cross term
`2c.(pred_j - target_i)` that varies with j and does not cancel in the softmax.

Nothing registered here revives that argument. What is true, and different, is a statement about
the loss's **level sets**: the objective is satisfied once each `pred_i` is nearer `target_i` than
any competitor, so its tolerance for absolute error is set by the in-batch target spacing rather
than by zero. That is a margin argument, not an invariance argument, and the distinction is
load-bearing.

## 7. Recorded but NOT registered

The biology's **selection** mechanism -- Wilhelm et al. 2011 (sleep gave no benefit over wake for
uninformed, unselected material) and Born & Wilhelm 2012 ("does not enhance every memory") --
predicts that a held-out battery drawn from a different env instance than the replay buffer is
diluted toward zero. It was **not** registered as a claim because it predicts a **null** while leg B
measured a consistent **negative**, so on its own it under-determines the observation. Carried as
`SLEEPRC-Q-002` in `REE_convergence/sources/sleep-replay-consolidation/`.

## 8. Scope

These claims address **leg B only**. **Leg A is independently blocked**: all three registered C1
leg-A DVs are transforms of `e3_prediction_error`, the scalar P1's own manipulation check gates on
(GFLAG-0389), so leg A needs re-registration with an independent DV before the four-arm ladder is
worth running *even if* leg B gets a readout.

**Limits carried, not buried.** GFLAG-0382 is n=1 seed, 1800-step P0, one sleep cycle -- enough to
decline the InfoNCE pin, **not** enough to assert leg B is permanently unreadable, and nothing here
asserts that. V3-EXQ-1063 is n=3 seeds, one configuration, and is `non_contributory` for INV-063 by
design; the quantitative support above is a re-reading of what it recorded, not a new result.
