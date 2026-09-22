# Substrate necessities surfaced by the precision-provenance experiment design (2026-09-22)

**Session:** `compassionate-pike-fe9174` (user-commissioned: design, implement, run and govern the
minimal behavioural-precision-provenance consolidation-gain experiment from
`thought_intake_2026-09-22_behavioral_precision_provenance_and_sleep_plasticity_gain.md`).
**User decision 2026-09-22 (recommendation ledger entry 520):** "Build full producers first, then
experiment", followed by: "This whole exercise likely identifies a number of substrate necessities
and we should pay heed to them." This register is that heed. Every item below was found by reading
live code (ree-v3 `a38a834`, REE_assembly `b425fccdb40`) while tracing the intake's information-loss
boundary; none is inferred from documentation alone.
**Spec for the items being built now:** `docs/architecture/precision_provenance_substrate_spec.md`.
**Preregistration:** `evidence/planning/precision_provenance_consolidation_gain_design_20260922.md`.

Classification uses CLAUDE.md's work-graph debt vocabulary (bracket is part of the token).

---

## A. Being BUILT this session (user-authorised, SD-PP-1..4)

| id | subject | what was missing | node class | unblocks |
|---|---|---|---|---|
| SD-PP-1 | `precision.observation_reliability` | NO evidence/sensory precision producer exists anywhere in `ree_core` (grep for sensory/obs/observation/evidence/outcome_precision returns nothing). The intake's "evidence precision" had no organism-side source. | complicated (buildable) | MECH-572, MECH-016, ARC-055, MECH-043 |
| SD-PP-2 | `precision.world_forward_epistemic_precision` | No producer of the precision of `e2.world_forward`'s own prediction. The only live precision EMA (E3 `running_variance`) is fed by the PROPOSER's predicted z_world, not the world head; SD-063's head is default-off and emits TOTAL spread (absorbs observation noise). Historical and current model precision therefore had no shared producer. | complicated (buildable) | MECH-572, MECH-573, MECH-016, ARC-055, MECH-059 |
| SD-PP-3 | `hippocampal.replay_provenance_packet` | The replay buffers the weight-consolidation pass draws from hold only `(z_world, action_one_hot)`; no prediction-at-test, PE, precision or outcome is bound to an entry; under V3-EXQ-1063's configuration nothing even computes the executed-action world-forward prediction at test time. | complicated (buildable) | MECH-572, MECH-269, MECH-284/285, MECH-368/431 |
| SD-PP-4 | `sleep.provenance_conditioned_consolidation_gain` | `CrossModuleConsolidator` has no gain input; fresh Adam pins displacement at `n_steps*lr` regardless of gradient (MECH-572), so a loss-weight alone cannot act on magnitude -- the consumer needs a per-step lr hook AND per-row weighting, plus per-step displacement/gradient instrumentation that does not exist. | complicated (buildable) | MECH-572, MECH-574, MECH-016, ARC-055, MECH-368/431, ARC-137 |

---

## B. Surfaced, NOT built -- registered in `substrate_queue.json` as REGISTRATION ONLY

Each row below is minted `proposed_REGISTRATION_ONLY_not_a_build_authorisation`, `ready: false`,
owner route `/governance`, because this session is a science session, not governance, and the
user's build authorisation covered the producers only.

### B1. No default-on behavioural consumer of `e2.world_forward` (organism-level readout path absent)
- **Found:** `e3_selector.py`'s only reference to `world_forward` is a docstring (line 1286). The
  consumers that exist -- MECH-314a `curiosity_candidate_source="e2_world_forward"`, MECH-353
  blocked-agency comparator, SD-063 deficit path, the escape-affordance linker -- are all
  default-off levers. The planning world model E3 actually acts through is E1 (proposer rollouts).
- **Consequence:** ANY claim about consolidating the world-forward head (MECH-572/573/574, INV-063
  leg B) is capped at a mechanistic/local evidence level: a changed head has no native route to
  E3 behaviour. The preregistration for V3-EXQ-1073 states this cap explicitly (Result 4 route).
- **Node class:** complex (probe-gated) -> puzzle (known rules): which default-off consumer, if any,
  gives the head causal reach to committed action must be measured before a behavioural endpoint
  is designed. A build that simply switches one on would change the waking regime of every
  experiment that inherits it.
- **Cheapest next action:** a diagnostic that enables MECH-314a's e2_world_forward candidate source
  in all arms and measures whether a post-sleep head change alters E3's candidate ranking on a
  fixed probe set (organism-level follow-up chip named in the preregistration).

### B2. Hippocampal selection is disconnected from weight consolidation
- **Found:** `SleepReplaySampler` (MECH-285 Phase B) draws anchors from the AnchorSet broad pool
  for the SWS aggregation cluster and is documented as a NO-OP CONSUMER; the weight-consolidation
  pass (`compute_e2_world_loss`, `compute_prediction_loss`, `compute_e2_loss`) draws
  `torch.randperm` batches from the raw experience buffers. The intake assumed the anchor payload
  (`AnchorGoalPayload`, which already carries state-at-write metadata) was the storage locus for
  provenance; it is not on the path.
- **Consequence:** replay PRIORITY (MECH-284/285) and plasticity GAIN (SD-PP-4) cannot yet be
  dissociated in the intake's F5 sense, because priority never reaches the pass that applies
  gain. SD-PP-3 rides the raw buffer index for that reason.
- **Node class:** complicated (buildable) -- a routed consumer (anchor-selected replay draw feeding
  the module loss closures) is a design question with known rules, but it is architecture-level
  (ARC-137 typed transformations) and must not be built inside an experiment.

### B3. Evidence-precision manipulation is a driver-level hack, not an env lever
- **Found:** additive observation noise is applied by `_apply_obs_noise` inside drivers
  (V3-EXQ-798a :565-577, V3-EXQ-1071 :387-400) on the `world_state` tensor before `sense()`.
  `CausalGridWorldV2` has no `obs_noise_sigma` kwarg.
- **Consequence:** every experiment manipulating sensory reliability re-implements the hook;
  the manipulation is invisible to `enabled_default_off_flags` and to the env fingerprint.
- **Node class:** complicated (buildable), small.

### B4. One-shot world-rule shift needs a driver poke of `env._action_map`
- **Found:** `world_rule_shift_enabled/interval/depth` fires on a modulo schedule
  (`_maybe_shift_world_rule`); there is no "shift once at step S" or "apply this permutation"
  kwarg, so the confidently-wrong condition (converged on rule R0, then reliable contradiction
  under R1) must permute `env._action_map` from the driver and mirror it onto the held-out battery
  env.
- **Node class:** complicated (buildable), small. Shares the MECH-318 / UEP-034 shape (a
  rule-context event the falsifiers cite but no env registers a provider for).

### B5. The world-forward head sits near copy-the-input because z_world barely moves per step
- **Found:** V3-EXQ-1063's `identity_predictor_mse` is ~1e-5 (mean((z1-z0)^2) on the frozen
  battery), i.e. the encoder maps a one-cell move to a z displacement of RMS ~3e-3 per dim, and the
  "converged" head has skill 1 - MSE_model/MSE_identity of -0.071 / +0.227 / -0.007 (MECH-573).
  A rule inversion therefore produces a PE of only ~4x the converged residual, and observation
  noise at sigma 0.12 ~1.6x -- the epistemic signal any gain rule must read is compressed into the
  encoder's dynamic range.
- **Consequence:** this bounds the effect size of EVERY consolidation experiment on this head,
  including V3-EXQ-1073; the preregistration carries a non-degeneracy gate on the measured PE
  separation for exactly this reason. It is the v3 binding constraint (observation -> z_world ->
  E1/E2) showing up again.
- **Node class:** complex (probe-gated) -> mystery (known data): the data exist (1063 manifest); the
  reframing is whether the world head should be trained on a z_world with more per-step
  displacement (SD-018 amend / resource-field supervision) rather than fixed downstream.

### B6. Per-state model precision that separates epistemic from aleatoric natively
- **Found:** SD-063's `E2WorldUncertaintyHead` estimates TOTAL predictive spread by quantile
  regression; it will learn the observation-noise spread as readily as model uncertainty.
  SD-PP-2 separates them by SUBTRACTION of the SD-PP-1 evidence variance with a pre-registered
  `noise_gain = 2.0`, which is a proxy.
- **Cheapest upgrade:** an ensemble-disagreement or error-predictor head over (z, a) giving
  epistemic variance directly (MECH-441's `ModelDisagreementEnsemble` already exists for curiosity
  and is the obvious candidate to re-point).
- **Node class:** complicated (buildable).

### B7. A learned sensory-precision estimator
- **Found:** SD-PP-1 is a frame-difference MAD statistic that relies on the exteroceptive field
  being mostly static between frames (true of CausalGridWorldV2: clean frac_changed 0.127). A
  moving-camera or high-flux env would need a motion-compensated innovation estimate.
- **Node class:** complicated (buildable), deferred until an env needs it.

### B8. Optimiser-state persistence across consolidation cycles (MECH-572's own alternative lever)
- **Found:** `consolidate()` builds a fresh Adam per call by design ("owns no persistent optimiser
  state"). MECH-572's falsifier names reusing optimiser state as one of three levers. SD-PP-4
  deliberately keeps the fresh Adam in all arms so ARM A reproduces the phenotype; persistence is
  a separate rival that V3-EXQ-1073 does NOT test.
- **Node class:** complicated (buildable); a follow-on arm, not this run.

---

## C. Governance-owed (not substrate)

- MECH-573's readability gate (skill > 0 against `identity_predictor_mse`) is a falsifier edit
  owed to `/governance`; V3-EXQ-1073's preregistration adopts it as a readiness precondition
  locally rather than waiting.
- MECH-572's `what_would_answer` names lr / n_steps / optimiser-state as the levers; V3-EXQ-1073's
  ARM D-global is exactly the lr lever at matched budget, so the run's A-vs-D contrast is also a
  direct MECH-572 CONFIRMING/FALSIFYING measurement and should be tagged as such at governance.

---

## D. Falsifier-runnability trace for V3-EXQ-1073 after SD-PP-1..4 land (queue-experiment Step 2.5d)

- **EVENT** -- a waking behavioural test of a world-forward prediction followed by a consolidation
  pass: emitted by `_e1_tick` + `SleepLoopManager.force_cycle` (present).
- **DV** -- across-sleep frozen-battery MSE (retention battery, shifted-rule correction battery),
  per-step displacement and gain: V3-EXQ-1063 instrument (present) + SD-PP-4 trace (built).
- **INSTRUMENT able to move** -- displacement: pinned at the Adam bound today (MECH-572, 6/6
  cells), freed by the step-scale hook (SD-PP-4 test 10 is the liveness pin). Evidence precision:
  0.000 vs 0.127 (probe). Model precision: ~1000x residual range between converged and fresh
  (1063). Historical-vs-current precision: differ only if the estimator updates between test and
  sleep entry -- the preregistration gates on measured within-run variance of `pi_hist`.
- **Verdict:** runnable after the build, subject to the preregistration's non-degeneracy gates
  (which can still STOP the run at smoke).
