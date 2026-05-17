# Phased rule_state Training Curriculum -- Design + Risk Analysis

**Owner:** `commitment_closure` deliverable 4 (the GAP-3 carve-out)
**Status:** DESIGN COMPLETE -- PENDING IMPLEMENTATION. Design questions
  O-1..O-5 RESOLVED 2026-05-17 (Section 8 is the frozen implementation
  contract). Implementation concurrency-blocked on the active
  goal_pipeline:GAP-3 session (holds `experiments/` + queue).
**Registered:** 2026-05-17
**Depends on:** GAP-3 env primitives 1-3 (IMPLEMENTED 2026-05-17,
  causalgridworldv2_env_extensions_spec.md); MECH-090 BetaGate bistable
  latch (implemented); SD-033a LateralPFCAnalog (implemented); SD-034
  closure operator (implemented)
**Blocks:** every behavioural arm in the OCD battery --
  V3-EXQ-460b/461/463b/464b/466b/467b/468b (EXP-0156/0157/0159/0160/
  0162/0163/0164) -- and therefore the SD-034, MECH-266, MECH-268,
  SD-021 behavioural promotions
**Non-substrate:** this is an experiment-harness training protocol, NOT
  a new `ree_core` substrate feature (see Section 4 / Open Question O-1)

---

## 1. Problem

A family of experiments cannot be run because the agent never enters --
let alone *holds* -- a committed rule_state during evaluation, so the
target metric is never even computable. The failure signature is
identical across three independent lineages:

| Experiment | Claim | Failure metric (all seeds, all arms) |
|---|---|---|
| V3-EXQ-321 (MECH-090 bistable latch) | MECH-090 | `total_committed_steps = 0`; `hold_rate = 0.0` |
| V3-EXQ-261 (SD-021 descending modulation) | SD-021 | `committed_traversals = 0` (50 eval eps) |
| V3-EXQ-325 (SD-021, post beta-fix) | SD-021 | `n_committed_steps = 0` all 5 seeds |

The governed verdict on every one is `non_contributory`: the experiment
does not weaken its claim, it simply never exercised the mechanism.
EXQ-321's own manifest states it plainly:

> "The wiring exists but the training curriculum does not elicit
> committed mode."

The only "PASS" in the lineage, V3-EXQ-321b, reached its result by
*scripting* the committed state (force `_running_variance = 0.001`,
inject E3-tick-aligned synthetic variance spikes, deepcopy a single
trained agent into condition clones). That is a harness workaround, not
emergent commitment -- MECH-090's supporting evidence is currently
scripted-only.

substrate_queue.json (SD-021 `metric_trajectory`) states the prerequisite
and the acceptance bar precisely:

> "Training curriculum change that reliably elicits committed-mode
> sequences (total_committed_steps > 100 per eval episode); MECH-090
> bistable latch confirmed working on same curriculum."

GAP-3 primitives 1-3 (adaptive tolerance-band completion, counter-evidence
degradation, dual-cue) are now landed -- but they are the *env* half.
They lower the competence bar for sequence entry; they do not make an
undertrained agent converge into committed mode. Deliverable 4 is the
missing training-side half.

---

## 2. Root-cause analysis

### 2.1 The commitment gate is a single trained-variance threshold

`ree-v3/ree_core/predictors/e3_selector.py:806`:

```
committed = self._running_variance < effective_threshold
```

`effective_threshold` starts at `commit_threshold` and is only ever
*reduced* by the MECH-108 breath sweep and SD-011 z_harm_a urgency
(e3_selector.py:781-796). Defaults (`utils/config.py:309-311`):

- `precision_init = 0.5`   (initial `running_variance`)
- `commitment_threshold = 0.40` (variance-space)
- `precision_ema_alpha = 0.05`

`running_variance` is an EMA of E2/E3 world-forward prediction-error MSE.
At init it is 0.5 > 0.40, so `committed` is False and
`beta_gate.elevate()` is never called. The **only** way it crosses below
0.40 is sustained training that drives world-forward prediction error
down. The code documents the failure mode directly (e3_selector.py:190-191):

> "deadlock: rv starts above commit_threshold -> agent never commits ->
> rv never updates -> agent can never commit."

A partial ARC-016 fix (always store the last selected trajectory so rv
keeps updating even when uncommitted, e3_selector.py:841) removes the
hard deadlock but **not** the requirement: rv only falls below 0.40
under a world model that has actually learned to predict. Short generic
E1+E2 loops on the OCD-battery agents never converge -> `committed`
stays False all episode -> the all-zero signature.

### 2.2 Two distinct "committed" constructs, both required

SD-034 closure (and therefore every behavioural arm) fires only when
**all** of the following hold (sd_034_governance_closure_operator.md):

1. `||rule_state(t) - rule_state(t-1)|| < closure_rule_delta_threshold`
   (0.001) for `closure_stable_ticks` (3) consecutive ticks,
2. `beta_gate_elevated == True` (MECH-090 committed -- the 2.1 gate),
3. `current_mode in allowed_closure_modes`,
4. SD-033a `write_gate >= closure_min_sd033a_gate` (0.5),
5. `||rule_state|| > 0`.

So an agent must (a) drive `running_variance` below threshold so the
beta latch elevates, **and** (b) accumulate a stable, non-zero SD-033a
`rule_state` (a gate-modulated EMA, ~20-step rise time, reset per
episode). (a) is a trained-world-model property; (b) needs enough
in-task ticks under a non-trivial write gate. Neither emerges from a
random or undertrained policy. The curriculum must produce both.

### 2.3 Env-side competence floor

`_sequence_in_progress` (causal_grid_world.py:1483-1525) flips True only
on correct in-order waypoint contact. GAP-3 primitive 1 (adaptive
tolerance-band) relaxes exact-cell to within-T contact, but the policy
must still reach the *correct next* waypoint in order. An undertrained
navigator almost never does -- the EXQ-261 `committed_traversals = 0`.
The curriculum must also raise navigation competence, not just
world-model convergence.

---

## 3. Non-goals (explicit guardrails)

- **NOT an oracle rule-cue curriculum.** The original "phased
  pre-training on a rule-cue curriculum" idea (retired Open Question Q1,
  commitment_closure_plan.md) presupposed an oracle `rule_cue_id` label.
  MECH-309's reframe forbids this: trainers weight rules they do not
  invent. This curriculum must elicit commitment from task structure +
  world-model convergence, **never** from a supervised rule-identity
  label.
- **NOT the SD-033a bias-head training problem.** That is the separate
  ARC-062/MECH-309 line (V3-EXQ-542/543*). This curriculum makes the
  agent *enter committed mode*; it does not train the rule-bias head.
- **NOT the SD-021 condition-dispatch bug.** EXQ-325a surfaced a
  *separate* downstream bug (DESCENDING == CONTROL bit-identical after
  commit fired). The curriculum only has to clear the
  commitment-elicitation blocker; the dispatch bug is tracked
  independently.
- **NOT a substrate change to the commit gate semantics.** Tuning the
  existing variance-EMA knobs is in scope (Section 4.4); redefining what
  "committed" means is not.

---

## 4. Design

The evidence (Section 6 of the research basis: EXQ-321b `run_training`,
SD-049 `_global_step` schedule, ARC-062 P0/P1/P2 + behavioural-divergence
probe, EXQ-261/325 `p0_episodes`/`p1_episodes` config idiom) converges
on one architecture: a **three-phase training protocol implemented as a
shared experiment-harness helper**, not a `ree_core` substrate feature.
Committed mode is an emergent property of a converged world model under
task pressure -- it is produced by a *training loop*, exactly as
EXQ-321b's `run_training` already demonstrates. Baking a scheduler into
the substrate would add risk for no benefit and risks the oracle trap.

### 4.1 Phase structure

**P0 -- world-model + navigation warmup (target: cross the variance gate).**
Train E1 + E2 world-forward (Adam, replay buffer, the EXQ-321b
`run_training` recipe generalised) on an *easy* env configuration until
`running_variance < commitment_threshold` is reached and stable, AND a
navigation-competence proxy (in-order waypoint contact rate, or GAP-3
`completion_within_tolerance` rate) exceeds a floor. Easy config: few
waypoints, short inter-waypoint distance, low hazard density, GAP-3
primitive 1 tolerance ON with a generous band, counter-evidence and
dual-cue OFF. Exit criterion is a *measured state*, not a fixed episode
count.

**P1 -- staged-difficulty commitment consolidation.** Ramp env
difficulty across episodes keyed on cross-episode `_global_step` (reuse
the SD-049 `resource_introduction_schedule` pattern, already validated):
increase `num_waypoints`, inter-waypoint distance, hazard density;
tighten the GAP-3 tolerance band toward the experiment's target;
introduce GAP-3 counter-evidence / dual-cue only at the end of P1 and
only for the arms that need them. Hold the beta latch in bistable mode
(`beta_gate_bistable=True`) so commitment, once entered, latches rather
than flickering. P1 ends when `total_committed_steps` per episode is
sustained above the acceptance floor on the *target* (not the easy) env
config.

**P2 -- frozen-policy evaluation.** Standard eval. The behavioural-arm
metric (SD-034 closure timing, MECH-268 PE plateau, MECH-266 switch
cost, SD-021 attenuation) is measured here, on an agent that entered
committed mode *emergently* during P0->P1.

### 4.2 Mid-curriculum probe gate (cost control)

Direct analogue of the ARC-062 rough-and-ready behavioural-divergence
probe. Every N episodes during P0/P1, sample
`running_variance`, `total_committed_steps`, `hold_rate`. If commitment
has not begun to emerge by a pre-registered checkpoint (e.g.
`running_variance` still > `commit_threshold` at 60% of the P0 budget),
**abort early** with `commitment_not_elicited` rather than burning the
full multi-hour run to read an all-zero metric (the concrete EXQ-321
waste this is designed to prevent). The probe is also the curriculum's
own success readout.

### 4.3 Emergent vs forced-control contrast arm

The curriculum's scientific purpose is *emergent* commitment. But each
behavioural EXQ should additionally run a **forced-commitment control
arm** (the EXQ-125a / EXQ-321b primitive: force `_running_variance`
either side of threshold). The contrast emergent-vs-forced isolates
whether a target metric requires *emergent* commitment or merely the
*committed state*. This converts the existing scripted-only evidence
(MECH-090 via EXQ-321b) into a properly controlled comparison rather
than discarding it.

### 4.4 Variance-gate knob tuning (in scope, bounded)

`precision_init`, `commitment_threshold`, `precision_ema_alpha` (and
`beta_gate_bistable`) directly set whether/how fast convergence crosses
the gate. The curriculum may tune these (per-experiment config, no
substrate change) but must account for the MECH-108 breath sweep and
SD-011 urgency, which already perturb `effective_threshold` downward
(e3_selector.py:781-796) -- the curriculum target must be the *stable*
crossing, not a transient one induced by an urgency spike. Recommended
default: `beta_gate_bistable=True` for all curriculum runs (its False
default was itself a contributing blocker in the SD-021 trajectory).

### 4.5 Integration with GAP-3 primitives 1-3

- Primitive 1 (adaptive tolerance) is the **competence ramp lever**:
  generous band in P0, tightened across P1 toward the arm's target.
  `frac=0.0` recovers exact-match for the final P2 if an arm needs it.
- Primitive 2 (counter-evidence degradation) is introduced **only at
  end of P1 / in P2** for EXP-0164-class arms -- never during P0/P1
  convergence (it would fight the world model learning the contingency).
- Primitive 3 (dual-cue) likewise enters only for EXP-0160/0163 arms at
  end of P1, on the SD-049 path the precondition already enforces.

---

## 5. Acceptance criteria

Pre-registered, from substrate_queue SD-021 `metric_trajectory`:

1. On the *target* (not easy) eval env, **`total_committed_steps > 100`
   per eval episode**, median over >= 3 seeds, with NO scripted variance
   injection and NO forced `_running_variance`.
2. MECH-090 bistable latch holds (no premature release) on the **same**
   curriculum that produced (1) -- i.e. EXQ-321's question becomes
   answerable without the EXQ-321b scaffold.
3. A stable SD-033a `||rule_state|| > 0` accumulates and satisfies the
   SD-034 closure stability predicate (delta < 0.001 for >= 3 ticks)
   during committed segments.
4. The mid-curriculum probe (4.2) correctly fires `commitment_not_
   elicited` on a deliberately starved control (sanity: the abort gate
   works).
5. At least one downstream behavioural arm (recommend EXP-0157 /
   V3-EXQ-461, the simplest -- delayed-reward persistence) produces a
   non-degenerate, computable target metric on the curriculum.

(1)-(3) are the curriculum's own validation; (5) is the proof it
unblocks the battery. Per spec section 5 precedent these are contract /
integration validations; whether a governance EXQ is queued is Open
Question O-4.

---

## 6. Risk analysis

This is flagged the **highest-risk piece** of commitment_closure. The
risks, with mitigations:

**R1 -- Convergence is not reliably reachable at all.** It is possible
that the E2 world-forward model on CausalGridWorldV2 simply cannot drive
`running_variance` below 0.40 within any feasible training budget (the
env may be too stochastic: env drift, hazards, counter-evidence). If so,
the blocker is not "curriculum tuning" but a substrate mismatch between
the commit-gate threshold and the achievable world-model accuracy.
*Mitigation:* P0 runs on the *easiest possible* env (minimal stochastic
sources, drift off) to establish that convergence is reachable in
principle before any ramp; the mid-curriculum probe (4.2) detects
non-convergence in ~60% of P0 rather than at the end; 4.4 permits
bounded `commitment_threshold` relaxation as an explicit, logged knob
(not a silent redefinition). If even the easiest config cannot converge,
the design pass output is "escalate: the commit gate is mis-calibrated
vs achievable world-model error" -- a substrate finding, not a curriculum
failure.

**R2 -- Curriculum overfits to the easy config; commitment collapses on
the target env.** The agent commits in P0 then loses it as difficulty
ramps. *Mitigation:* acceptance criterion (1) is explicitly measured on
the *target* env, not the easy one; P1 ramp is gated on *sustained*
commitment at each difficulty step before advancing (a within-P1
ratchet, not a fixed schedule).

**R3 -- "Emergent" is indistinguishable from "scripted".** If the only
way to hit the acceptance bar is heavy knob tuning + a near-scripted
schedule, the evidence is no better than EXQ-321b. *Mitigation:* the
emergent-vs-forced contrast arm (4.3) makes this measurable rather than
arguable; criterion (1) forbids scripted variance / forced rv; the doc
states the honest fallback -- if only forced commitment is achievable,
say so and treat MECH-090/SD-021/SD-034 behavioural evidence as
permanently scripted-tier (a governance-confidence ceiling, not a hidden
failure).

**R4 -- Compute / time cost.** EXQ-321 wasted ~50 min to read an
all-zero metric; a full curriculum is longer and there are >= 7
behavioural arms. *Mitigation:* the mid-curriculum abort gate (4.2);
P0 is shared across arms (train once, deepcopy into arm-specific P1/P2,
the EXQ-321b deepcopy precedent); arms batched by shared P0 config.

**R5 -- effective_threshold flicker (MECH-108 / SD-011).** Commitment
that only appears during an urgency/breath trough is not stable and will
not satisfy the SD-034 stability predicate. *Mitigation:* 4.4 -- target
the stable crossing; measure committed-segment length, not instantaneous
commit; bistable latch ON.

**R6 -- Scope creep into the SD-033a bias head / oracle rule cue.** The
tempting "just supervise the rule signal" shortcut is forbidden
(Section 3). *Mitigation:* explicit non-goal; any design iteration that
introduces a rule-identity label is out of bounds by construction.

**R7 -- The curriculum unblocks commitment but the SD-021
condition-dispatch bug still blocks SD-021.** *Mitigation:* out of
scope by Section 3; flagged so SD-021 reviewers do not mistake a
curriculum success for an SD-021 result.

Net risk posture: R1 is the genuine existential risk (it could turn out
the gate is mis-calibrated, not the curriculum). The design deliberately
front-loads the cheap test of R1 (easiest-env P0 + early probe) so the
expensive arms are never launched until R1 is retired.

---

## 7. What this unblocks

On acceptance: the Phase 4/5 behavioural arms become runnable --
V3-EXQ-460b/461/463b/464b/466b/467b/468b -> the SD-034 closure operator,
MECH-268 dACC PE saturation, MECH-266 competing-goals / mode-stickiness,
and SD-021 descending-modulation behavioural promotions
(provisional -> stable). It also retires the "scripted-only" caveat on
MECH-090. It is the last structural blocker between the landed GAP-3 env
primitives and an end-to-end OCD battery.

---

## 8. Design questions -- RESOLVED 2026-05-17 (user)

All five resolved; this section is now the implementation contract.

- **O-1 (architecture home) -- RESOLVED: experiment-harness helper.**
  The curriculum is a shared helper (e.g.
  `experiments/_lib/committed_mode_curriculum.py`) that behavioural EXQs
  import -- NOT a `ree_core` substrate scheduler. No substrate change;
  generalises the EXQ-321b `run_training` precedent.
- **O-2 (emergent vs forced) -- RESOLVED: emergent + forced control.**
  Every behavioural arm runs BOTH the curriculum (emergent) arm and a
  forced-`_running_variance` control arm (4.3). The contrast is
  mandatory -- it is what converts the EXQ-321b scripted-only MECH-090
  evidence into a controlled comparison. Accept the ~2x per-arm compute.
- **O-3 (R1 escalation trigger) -- RESOLVED: one step, then escalate.**
  At most ONE documented `commitment_threshold` step (0.40 -> 0.45) on
  the easiest env. If commitment still does not emerge, STOP and
  escalate as "the commit gate is mis-calibrated vs achievable
  world-model error" -- a substrate finding, not a curriculum knob. NO
  hyperparameter sweep of the variance-gate params (the R3 hazard).
  Section 4.4 is bound by this: the only in-scope gate tuning is the
  single 0.40->0.45 step plus `beta_gate_bistable=True`.
- **O-4 (validation route) -- RESOLVED: contract/integration, queue
  deferred.** Validate via the contract/integration harness per the
  GAP-3 spec-section-5 precedent. A queued governance EXQ is deferred
  regardless until the concurrent goal_pipeline:GAP-3 session releases
  its hold on `experiments/` + `experiment_queue.json`.
- **O-5 (pilot arm) -- RESOLVED: EXP-0157 / V3-EXQ-461.** The pilot is
  delayed-reward persistence (the simplest committed-hold test). Prove
  the curriculum elicits + holds commitment there before scaling to the
  harder SD-034 / MECH-268 / MECH-266 arms.

**Implementation gating:** the next step (harness-helper build + the
EXP-0157 pilot) is **concurrency-blocked** -- it needs `experiments/`
(and the queue for the pilot run), currently held by the active
goal_pipeline:GAP-3 session. The implementation pass waits for that
claim to clear (or explicit coordination). Until then GAP-11 stays
`design_complete` with this section as the frozen contract.

---

## 9. References

- Failure record: V3-EXQ-321 / 321a / 321b, V3-EXQ-261, V3-EXQ-325 /
  325a manifests (`REE_assembly/evidence/experiments/`).
- substrate_queue.json SD-021 `metric_trajectory` (acceptance bar);
  SD-022 (separate body-damage substrate, not this blocker).
- commitment_closure_plan.md (Phase 3 deliverable 4; Phase 4/5; Test
  cohort; decision-log 2026-05-16 split; retired Q1 oracle-cue caveat).
- causalgridworldv2_env_extensions_spec.md Section 6 (the carve-out).
- Substrate: `ree-v3/ree_core/predictors/e3_selector.py` (commit gate
  806, deadlock 190-191, effective_threshold 781-796), `agent.py`
  (beta latch 3300-3391), `heartbeat/beta_gate.py`,
  `pfc/lateral_pfc_analog.py`, `utils/config.py` (309-311, 988),
  `environment/causal_grid_world.py` (1483-1525 + GAP-3 primitives).
- Design docs: sd_034_governance_closure_operator.md,
  sd_033a_lateral_pfc_analog.md, sd_021_descending_pain_modulation.md.
- Precedent: arc_062_rule_apprehension_plan.md (P0/P1/P2 +
  behavioural-divergence probe); ree-v3 experiments
  v3_exq_321b_mech090_bistable_holdrate.py (`run_training` + deepcopy),
  v3_exq_125a_arc029_committed_mode_redesign.py (forced-rv control),
  v3_exq_543b_arc062_phase3_optimized_falsifier.py (P0/P1 scaffolding).
