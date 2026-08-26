---
title: "SD-034: Governance Closure Operator"
parent: "Executive & PFC Control"
grandparent: Architecture
nav_order: 24
status: provisional
status_asof: 2026-07-10
status_claim: SD-034
---

# SD-034: Governance Closure Operator

**Claim ID:** SD-034
**Subject:** governance.closure_operator
**Status:** IMPLEMENTED 2026-04-20 (validated 2026-04-21; design doc backfilled 2026-04-27; behavioural-authority amend `commitment-closure-control-plane` 2026-06-12; Leg C rule_bias_head training amend 2026-06-16; de-commit-authority MAGNITUDE amend 2026-06-19; refractory-independent commit-intent coupling certifier 2026-06-19 -- see amend sections below)
**Registered:** 2026-04-20
**Depends on:** SD-033 (governance cluster), SD-033a (lateral PFC analog rule_state), MECH-090 (BetaGate commitment latch), MECH-260 (dACC action-class No-Go), MECH-094 (hypothesis tag write gate), SD-032a (SalienceCoordinator), SD-032b (dACC analog)
**Blocks:** EXP-0156 / V3-EXQ-460 (verified-but-not-released), EXP-0157 / V3-EXQ-461 (delayed-reward persistence), EXP-0162 / V3-EXQ-466 (satisficing / residue discharge), EXP-0164 / V3-EXQ-468 (commitment vs contradiction). All landing-diagnostic variants PASSed 2026-04-21.

## Problem

REE-V3 has the substrate for Go (basal-ganglia-like gate, SD-032a operating-mode register), Hold (MECH-090 BetaGate bistable commitment latch), and No-Go (MECH-260 dACC action-class suppression). What is missing is the operator that turns evaluation **off** on successful completion. Without it, a committed rule_state that has been satisfied keeps being evaluated, keeps consuming mode budget, keeps generating residue, and the agent cannot disengage. The 2026-04-20 GAP MEMO and the OCD thought set identify this as the load-bearing missing piece in the governance layer — verified-but-not-released, delayed-reward-persistence, and satisficing failures all trace back to the absence of a closure operator.

## Solution

Implemented as `ree_core/governance/closure_operator.py` (`ClosureOperator`, `ClosureOperatorConfig`, `ClosureEvent`). On detection of rule-completion, the operator emits a five-part coordinated "done" token:

1. **Beta release** — calls `MECH-090 beta_gate.release()` to drop the commitment latch.
2. **No-Go injection** — calls `MECH-260 dacc.inject_nogo(action_class, count)` to bias the just-completed action class toward suppression on the next cycle. Uses the same FIFO mechanism as execution-recorded suppression but is semantically distinct (closure-driven rather than execution-recorded).
3. **Residue discharge** — calls `ResidueField.discharge_domain(z_world, factor, radius)` for rule-domain multiplicative decay on RBF weights. A hard 1e-6 floor preserves the "residue cannot be erased" invariant; valence_vecs are not modified so 4-component valence is preserved (replay prioritisation remains faithful).
4. **Salience signal** — calls `SalienceCoordinator.update_signal("closure_event", value)`, which re-biases mode affinity toward `internal_planning` via registered affinity_weights (default `internal_planning=0.5`).
5. **dACC PE reset** — calls `dacc.reset_episode_pe()` and optionally installs a `dacc_pe_cap` (MECH-268 saturation/reset coupling).

### Completion detection

Two paths.

**Tick path** (default): the operator checks at every `select_action()` whether
- `||rule_state(t) - rule_state(t-1)|| < closure_rule_delta_threshold` for `closure_stable_ticks` consecutive ticks
- AND `beta_gate_elevated == True`
- AND `current_mode in allowed_closure_modes`
- AND `sd_033a write_gate >= closure_min_sd033a_gate`
- AND `||rule_state|| > 0` (guard against firing on an unset rule_state).

**Explicit path**: `emit_closure(action_class, z_world, bypass_mode_conditioning=False)`. The experiment hook for controlled ablations.

### Mode conditioning as falsifiability predicate

Mode conditioning generalises MECH-094's hypothesis-tag write gate to the closure operation. Closure firing is blocked in `internal_replay` and `offline_consolidation` modes via `allowed_closure_modes` and via the `sd_033a` gate floor (`write_gate("sd_033a") = 0.05` in internal_replay). The architectural commitment is testable: if MECH-090 + MECH-260 + MECH-094 tuning *without* closure produces the same behavioural signature as closure-with-MECH-094-restriction in follow-up behavioural variants, SD-034 is over-specification. The mode-conditioning predicate is the falsification handle.

### ResidueField.discharge_domain API (added in same pass)

Multiplicative decay + sign-aware 1e-6 floor + radius-scoped in-domain selection via squared-distance comparison against `(radius * bandwidth)^2`. `valence_vecs` are NOT modified — the 4-component valence is preserved so replay prioritisation remains faithful.

### DACCAdaptiveControl extensions

- `dacc_pe_cap` config field (absolute cap on precision-weighted PE after closure).
- `inject_nogo(action_class, count)` method.
- `reset_episode_pe()` method (distinct from full `reset()` — preserves `_action_history` where the just-injected No-Go lives).

### Agent wiring

`REEAgent.__init__` instantiates `closure_operator` when `use_closure_operator=True` (requires `use_lateral_pfc_analog=True` and `use_dacc=True`; salience coordinator optional). `select_action()` calls `closure_operator.tick()` after action emission with current `z_world`, `argmax(action_class)`, `operating_mode`, and `sd_033a` gate. `reset()` calls `closure_operator.reset()`. `register_on_coordinator()` wires `closure_event` into `salience.config.affinity_weights` at init.

### Config surface

- `REEConfig.use_closure_operator` (bool, default False) — master switch
- `closure_rule_delta_threshold` (default 0.001)
- `closure_stable_ticks` (default 3)
- `closure_require_beta_elevated` (default True)
- `closure_min_sd033a_gate` (default 0.5)
- `closure_nogo_injection_count` (default 3)
- `closure_residue_discharge_factor` (default 0.5)
- `closure_residue_discharge_radius` (default 1.5)
- `closure_signal_value` (default 1.0)
- `closure_reset_pe_ema` (default True)
- `closure_pe_cap_after` (default None)
- `closure_signal_affinity_internal_planning` (default 0.5)

### Backward compatibility

`use_closure_operator=False` by default → `agent.closure_operator is None`; every integration site is a no-op. Existing experiments unaffected. Bit-identical with `closure_signal_affinity_internal_planning=0.0` and the master switch off.

## Architecture Context

SD-034 is the first substrate landed in the SD-033 governance cluster (see `evidence/planning/sd033_governance_plan.md`). It is also the first consumer of the MECH-261 write-gate registry's mode-conditioning predicate. Subsequent substrates in the cluster — MECH-266 (asymmetric mode hysteresis), MECH-267 (mode-conditioned hippocampal proposals), MECH-268 (dACC conflict saturation) — are independent extensions of existing modules; SD-034 is the only one that is a new module / new operator.

The five-part signal collocates several biologically-observed end-of-sequence signatures: OFC sequence-completion cells (Rich & Shapiro 2009; Schuck 2016), task-set disengagement (Collins & Frank 2014), and the post-completion No-Go refractory period (Mayr & Keele 2000). The collocation hypothesis is the architectural commitment: V3 treats them as one operator, EXP-0156 and EXP-0162 probe whether they should remain co-located or split.

## Biological Grounding

- **Rich & Shapiro 2009** — rat PFC strategy-switch neurons; transient activity at strategy completion ([DOI 10.1523/JNEUROSCI.4732-08.2009](https://doi.org/10.1523/JNEUROSCI.4732-08.2009)).
- **Schuck 2016** — human OFC encodes task-stage / state-space position; supports a "where in the sequence am I?" detector that closure can read from ([DOI 10.1016/j.neuron.2016.08.019](https://doi.org/10.1016/j.neuron.2016.08.019)).
- **Collins & Frank 2014 (OPAL)** — D1/D2 striatal opponent dynamics produce task-set disengagement under DA modulation ([DOI 10.1037/a0037015](https://doi.org/10.1037/a0037015)).
- **Mayr & Keele 2000** — backward inhibition: post-completion refractory period on re-entry to the just-abandoned task set, six replicating experiments ([DOI 10.1037/0096-3445.129.1.4](https://doi.org/10.1037/0096-3445.129.1.4)).
- **Smith & Graybiel 2013** — dual-operator action-bracketing in striatum + infralimbic cortex; flags closure substrate may be multi-region rather than OFC/ACC-only ([DOI 10.1016/j.neuron.2013.05.038](https://doi.org/10.1016/j.neuron.2013.05.038)).

The 2026-04-27 SD-034 lit-pull (`evidence/literature/targeted_review_sd_034/`) recommends:
1. Implement No-Go as graded score_bias decay rather than hard refractory gate. **The V3 implementation matches**: MECH-260's FIFO action-class history produces a graded recency-bias suppression rather than a binary block.
2. Closure-detection signal can fire from multiple substrates (not OFC/ACC only). **The V3 implementation is consistent**: the substrate commitment is the rule-state-delta-stability detector, not anatomical localisation. The architectural choice is substrate-agnostic.
3. Post a transient negative bias to the just-completed rule via SD-033a's per-candidate projection. **The V3 implementation differs slightly**: closure does not modify SD-033a's bias weights directly; the negative bias is delivered through MECH-260 action-class suppression. The downstream effect is similar (next-cycle bias against the just-completed action class) but the substrate is different (action-class FIFO rather than rule-bias projection). For V4 reconsideration: routing the post-completion bias through SD-033a's existing per-candidate bias projection would unify the bias channels.

## What This SD Enables

Validation experiments queued + run + PASSed 2026-04-21:
- **V3-EXQ-460** (EXP-0156 verified-but-not-released): substrate-landing diagnostic, 6 sub-tests covering backward compat, wiring, beta release, No-Go, pe reset, mode conditioning. **PASS** on smoke.
- **V3-EXQ-466** (EXP-0162 satisficing / residue discharge): residue-discharge landing diagnostic, 5 sub-tests covering near attenuation, far spared, invariant preserved, closure→discharge end-to-end, distant-z spares. **PASS** on smoke.
- **V3-EXQ-468** (EXP-0164 commitment vs contradiction): coupled SD-034 + MECH-268 PE-saturation diagnostic. **PASS** on smoke.

Behavioural variants with full E3 task loop + tolerance-band completion env are deferred. Both variants depend on phased rule_state training (not yet on the V3 roadmap) and on a CausalGridWorldV2 task-loop env extension that has not been authored.

## Related Claims

- **MECH-260** — dACC action-class suppression. Closure inject_nogo extends the existing FIFO mechanism with a closure-driven entry point.
- **MECH-261** — write-gate registry. Closure consumes the mode-conditioning predicate to gate firing in internal_replay / offline_consolidation modes.
- **MECH-262** — rule-bias projection from SD-033a. Closure reads SD-033a write_gate as a precondition.
- **MECH-094** — hypothesis tag / categorical write gate. Closure mode-conditioning generalises this to the closure operation.
- **MECH-268** — dACC PE saturation. Closure couples to MECH-268 via `closure_reset_pe_ema` and the optional `dacc_pe_cap` install.

## StepHarness write-path audit (commitment_closure:GAP-10)

**Completed:** 2026-05-17. All four governance write sites named in the GAP-10 spec were walked
and classified. The audit question (per `commitment_closure_plan.md` Phase 8): does any
commitment/closure write site need to be re-routed through `StepHarness`, or does each site have
a documented architectural exception?

**Note on StepHarness location.** `StepHarness` lives in `experiments/_harness.py`, NOT in
`ree_core/`. It enforces the canonical waking per-tick sequence
(`sense → record_transition → clock/E1/generate → update_z_goal → update_schema_wanting →
select_action → env.step → update_residue`). Governance writes that run inside `select_action()`
are within-step-7 architectural exceptions by design — they fire after the canonical sense/
update_z_goal inputs are in place and before `env.step` consumes the action.

### Write sites and exception classifications

| Site | Code location | Exception class | Notes |
|------|--------------|----------------|-------|
| **SD-034 closure pulse** (`closure_operator.tick()`) | `agent.py:3525-3550`, called at end of `select_action()`, after action tensor is formed | Within-select_action governance write | `_current_latent` (sense step 1) and mode/gate (update_z_goal step 4) are already in place. Closure fires after, not before, the canonical update steps. Hypothesis-tag guard (`hypothesis_tag=False`) enforced at call site — replay paths cannot trigger closure. |
| **MECH-260 `dacc.record_action()`** | `agent.py:3511-3518`, end of `select_action()` | Within-select_action governance write | Execution-path recency recording — appends chosen action class to `_action_history` FIFO. Fires after action is chosen; consumed by next `select_action()` call. |
| **MECH-260 `dacc.inject_nogo()`** | `closure_operator._fire()` → triggered by `tick()` at `agent.py:3541` | Within-select_action governance write | Closure-driven No-Go injection (multiple `record_action`-equivalent pushes for the just-completed action class). Mechanistically identical to `record_action()` but semantically distinct; both are within step 7. |
| **MECH-268 `dacc.reset_outcome_history()`** | `closure_operator._fire()` → `agent.py:3541` | Within-select_action governance write | SD-034 closure hook: clears the MECH-268 saturation FIFO so the next rule-state starts fresh. Fires inside step 7 alongside the other closure sub-signals. |
| **MECH-268 `dacc.reset_episode_pe()`** | `closure_operator._fire()` → `agent.py:3541` | Within-select_action governance write | Rebaselines the precision-weighted PE EMA on closure. Distinct from `reset()` (which also clears action history — too destructive for a per-closure event). Within step 7. |
| **MECH-268 `dacc.record_outcome()`** | EXQ-463 / EXQ-468 experiment scripts only; NOT in `agent.py` | Experiment-only unit test; canonical wiring deferred | Outcome class labeling after `env.step()` would naturally sit at StepHarness step 10 (after `update_residue()`). This call site is absent from the agent canonical path intentionally: env-level outcome tagging requires the GAP-3 env extension (counter-evidence/dual-cue hooks). EXQ-463 and EXQ-468 test the MECH-268 mechanism in isolation directly on a standalone `DACCAdaptiveControl` object, bypassing REEAgent. No routing gap; intentional deferral. |
| **SD-033a `lateral_pfc.update()`** | `agent.py:2835`, inside `select_action()` after MECH-319 sim-mode gate check | Within-select_action governance write | `z_delta`/`z_world` from `_current_latent` (sense step 1); `lpfc_gate` from `salience.write_gate("sd_033a")` (update_z_goal step 4). Both prerequisites established by canonical harness steps before step 7. MECH-319 sim-mode gate (`simulation_mode_rule_gate`) guards against replay-path rule-state writes at this site. |

**Audit result:** ALL six write sub-sites are documented exceptions. Zero require re-routing
through `StepHarness`. The one pending item (`dacc.record_outcome()` in canonical agent path) is
a deferred wiring task gated on GAP-3 env extension, not a routing error. The GAP-10 acceptance
criterion is satisfied.

### Sequence alignment note

The four major sites all run inside `select_action()` (StepHarness step 7). By the time step 7
runs, the canonical prerequisites are in place:
- `_current_latent` (z_world, z_self, z_delta) set by `sense()` at step 1.
- `update_z_goal(benefit_exposure, drive_level)` has run at step 4, setting salience gate state
  including `write_gate("sd_033a")`.
- No subsequent harness step modifies these values until `env.step()` at step 9.

There is therefore no ordering hazard between the governance writes and the canonical sequence.

---

## Amend: commitment-closure-control-plane (env-completion hook + de-commit hold) -- 2026-06-12

**Routed by:** `evidence/planning/failure_autopsy_SD-034-closure-cluster_2026-06-12.{md,json}`
(confirmed 2026-06-12 governance cycle). The 2026-04-20 landing is unit-level; the
2026-06-12 `*c`-cohort behavioural arms on the 603n foraging-competent substrate
showed the operator had **no behavioural authority**:

- **V3-EXQ-460c** -- `n_closures=0` on 3/3 seeds despite env `sequence_completions=2/5/6`
  and beta elevated; `nogo_installed_total=0` (strictly downstream of a closure fire).
  Root cause: the env emits `transition_type == "sequence_complete"` but the experiment
  **never routes it into `emit_closure()`** -- it relied solely on the automatic
  rule-state-stability detector, whose conjunction (rule_state delta < 0.001 x3 ticks +
  meaningful magnitude + sd_033a gate >= 0.5 + allowed mode) was unmet on the
  untrained/zeroed `rule_bias_head` + SP-CEM-perturbed agent.
- **V3-EXQ-468c** -- closure-coupled beta releases fire MORE under ON (C1 PASS) but the
  latch re-elevates immediately, so `committed_frac_post_vs_pre` cap-pins (~39 both arms,
  post pinned at the 195-step window); the release lacks de-commit hold authority.

Both reclassified `non_contributory` / `substrate_ceiling` / `pending_retest_after_substrate`
(NO demotion of SD-034; NO weaken of MECH-261). This amend supplies the two missing
substrate links; the `*d` retests + non-cap-pinned DV are experiment-side.

### Two no-op-default legs (bit-identical OFF)

**Leg A -- explicit env-completion hook seam** (closes 460c `n_closures=0`).
`REEAgent.notify_env_completion(action_class, z_world=None, bypass_mode_conditioning=False,
simulation_mode=False) -> Optional[ClosureEvent]` (ree-v3/ree_core/agent.py). When
`use_closure_env_completion_hook=True` AND `closure_operator is not None` AND not
simulation, it routes the env completion into `closure_operator.emit_closure(action_class,
z_world or self._current_latent.z_world, ...)` and returns the `ClosureEvent` (so the
harness counts fires / No-Go installs); returns `None` (no-op) otherwise. The experiment
harness calls it post-`env.step()` on a `sequence_complete` tick. This is the explicit
hook the operator docstring already described but the `*c` cohort left unwired.

**Leg B -- de-commitment hold / refractory** (closes 468c `committed_frac` cap-pin).
`BetaGate` (ree-v3/ree_core/heartbeat/beta_gate.py) gains `_refractory_remaining` +
`apply_refractory(n)` + a `refractory_remaining` property; `elevate()` is a no-op while
the window is active (records `_n_elevation_refractory_blocked`); `propagate()` decrements
the window once per tick (it runs every `select_action`). `ClosureOperatorConfig.decommit_hold_ticks`
(default 0) makes `_fire()` install `beta_gate.apply_refractory(decommit_hold_ticks)` on
any closure fire (recorded as `ClosureEvent.decommit_refractory_applied`). The release
now survives >1 tick -> measurable post-completion uncommitted fraction.

**Leg C (experiment-side, NOT substrate).** The `*d` retests set the landed GAP-D
`lateral_pfc_train_rule_bias_head` so the automatic detector has a magnitude-bearing
rule_state, gate readiness on `n_closures>0` reachable on the positive control, and read
de-commitment on a non-cap-pinned statistic (post-completion uncommitted fraction /
committed-run-length delta), not a post/pre ratio against a 5-step pre-baseline.

### Config (REEConfig + from_dims; both no-op default)

- `use_closure_env_completion_hook` (bool, default False) -- Leg A master.
- `closure_decommit_hold_ticks` (int, default 0) -- Leg B hold length; wired into the
  `ClosureOperatorConfig` build in `REEAgent.__init__` via getattr fallback.

### Validation

1014 contracts (1008 prior + 6 new in `tests/contracts/test_sd034_decommit_hold_and_env_hook.py`)
+ 7/7 preflight PASS; `v3_exq_460c --dry-run` unchanged (hook OFF -> prior FAIL signature);
agent smoke confirms hook ON routes a completion (`n_closures 0->1`, `nogo_pushed=3`) +
refractory blocks re-commit. **Validation experiments:** V3-EXQ-460d (supersedes 460c) +
V3-EXQ-468d (supersedes 468c) via `/queue-experiment`. **Retest gate:** `n_closures>=1`
reachable on the positive control AND `nogo_installed>=1` on >=2/3 seeds after the
env->emit_closure wiring; and a non-cap-pinned de-commitment DV showing ON<OFF on >=2/3
seeds. Phased training: N/A. MECH-094: env hook is waking-only + simulation-gated; the
refractory is a control-state transition. Step-8.5 staleness: not triggered (no-op-default).

## Amend: Leg C rule_bias_head training (commitment_closure:GAP-4) -- 2026-06-16

The 2026-06-12 amend flagged Leg C as "experiment-side, NOT substrate" -- the `*d`
retests were supposed to add the GAP-D `rule_bias_head` to a P1 optimizer and train it.
The confirmed `failure_autopsy_SD-034-closure-control-plane-d_2026-06-13` found they did
not: both `v3_exq_460d_*.py` and `v3_exq_468d_*.py` set
`lateral_pfc_train_rule_bias_head=True` (un-zeroing the head's last Linear) but a grep for
`optim|Adam|.backward(|bias_head_parameters` returned ZERO matches in either script. So
the head stayed at random init -- the rule_state handed to the ClosureOperator's automatic
rule-stability detector carried no task-shaped magnitude, the detector stayed inert (Leg A's
explicit hook rescued C1 regardless), and the closure-coupled de-commit had **no net
authority** over the MECH-090 latch: 460d C2_beta_release / C4 FAIL (ON latch occupancy
>= OFF on seeds 43/44, 12.27 vs 10.07; 31.73 vs 27.67), and the agent committed-without-beta
on 468d seeds 43/44 (`total_beta_elevated=0`). **Not a falsification of SD-034/MECH-261** --
the literal "Leg C not built".

This amend builds Leg C as a **scaffold-harness training leg** (the more durable place than
a per-experiment loop -- it makes the onboarded agent's rule_state magnitude-bearing for any
downstream commitment experiment), mirroring the existing `scaffold_train_harm_pathway` leg.
ree_core is UNTOUCHED -- it calls the existing SD-033a/ARC-062 GAP-D
`lateral_pfc.compute_bias` / `bias_head_parameters` substrate (landed 2026-05-17).

**Module:** `ree-v3/experiments/scaffolded_sd054_onboarding.py`. A
`scaffold_train_rule_bias_head` leg trains `agent.lateral_pfc.bias_head_parameters()` during
**P1** (goal-unfrozen, ecological contact, commitment forms) via the V3-EXQ-598b
outcome-coupled E3-gradient REINFORCE pattern. Episode-level (not per-step like the harm
pathway): `run_p1` builds the optimizer + a persistent runtime (outcome buffer + EMA return
baseline) via `Scheduler._make_rule_bias_pathway`; each `_train_episode` records a
`(candidate_features = world_states[1] of the leading n_probe candidates, selected-candidate
index)` snapshot every N steps and accumulates the episode return (`-harm`); at episode end
`_rule_bias_episode_update` takes one Adam step -- advantage = `ep_return - EMA baseline`;
`bias = lateral_pfc.compute_bias(candidate_features)` recomputed (gradient flows into the
head); `loss = mean(-adv * log_softmax(-bias / T)[sel])`; grad-clip 1.0; step.

**Trainable-head guard.** Requires the agent built with `use_lateral_pfc_analog=True` AND
`lateral_pfc_train_rule_bias_head=True` (the GAP-D un-zero flag). With the head
zeroed-and-frozen OR no lateral_pfc, `_rule_bias_params` returns `[]` -> optimizer None ->
the leg is a clean inert no-op (surfaced as `rule_bias_pathway_enabled=False` on the P1
manifest; never silently trains the baseline-OFF head).

### Config (ScaffoldedSD054OnboardingConfig; all no-op default, bit-identical OFF)

NOT surfaced through `REEConfig.from_dims` (matches the `scaffold_train_harm_pathway` /
SD-054 env-only scheduler-config precedent -- the 460e experiment sets them on the scheduler
config directly):

- `scaffold_train_rule_bias_head` (bool, default False) -- master.
- `scaffold_rule_bias_lr` (5e-4), `_batch_size` (32), `_record_every_n_steps` (4),
  `_outcome_buf_max` (512), `_n_probe_candidates` (8), `_policy_temperature` (1.0),
  `_adv_min_threshold` (0.005), `_ema_decay` (0.9) -- the 598b constants.

`P1OnboardingResult` gains `rule_bias_pathway_enabled` + `rule_bias_diag` (REINFORCE
counters + live per-candidate `|bias|` samples for the validation's non-vacuity gate).

### Validation

109/109 scaffolded contracts (102 prior + 7 new C17) + 7/7 preflight PASS; `v3_exq_460d
--dry-run` unchanged (leg off). Activation smoke (run_p1, tiny scale, leg ON): rule_bias_head
last-Linear `max|dW|=0.0015 > 0` (head TRAINS -- the 460d bug inverted), 3 REINFORCE steps
over 57 snaps, mean per-candidate `|bias|=0.039` (non-trivial, vs ~0 for the untrained 460d
head); leg OFF -> `max|dW|=0.0` exactly (bit-identical). Phased training: correctly phased by
construction (P0 warms the encoder goal-frozen; the head trains in P1 after warmup -- the 598b
P0->P1 discipline; no new encoder head). MECH-094: N/A (waking P1 training loop; no
simulation/replay write surface; lateral_pfc.update keeps its MECH-319 simulation gate).
Step-8.5 staleness: NOT triggered (no-op-default flag; no dependent claim's measured mechanism
changed).

**Validation experiment:** V3-EXQ-460e (supersedes 460d) via `/queue-experiment` -- the
closure-control-plane re-run with `scaffold_train_rule_bias_head=True` +
`lateral_pfc_train_rule_bias_head=True` + a **non-cap-pinned ON<OFF latch-occupancy-drop DV**
for C2_beta_release + a beta-engagement non-vacuity gate + a rule_bias-magnitude readiness
gate (`rule_bias_diag` mean `|bias|` > floor, else `substrate_not_ready_requeue`). Acceptance
per the autopsy failure record: ON<OFF de-commit on a non-cap-pinned statistic on >=2/3 seeds
with beta-engagement met. The `commitment-closure-control-plane` substrate_queue `ready` STAYS
false until 460e scores a contributory PASS.

## Amend: de-commit-authority MAGNITUDE (committed-run-scaled Leg-B refractory) -- 2026-06-19

Routed by the confirmed `failure_autopsy_V3-EXQ-460f_2026-06-18` (user-adjudicated
2026-06-18T08:04Z governance cycle). The 2026-06-17 beta-engagement amend WORKED -- all 4
readiness gates cleared and the C2 de-commit occupancy-drop DV ran for the first time (PASS
seed 42: ON 23.73 < OFF 35.67, -33.5%; FAIL 2/3). But on strong-natural-commit seeds the
closure->beta coupling was INERT (`sd034_n_closure_coupled_elevations` 36/52 seed 42 vs 0/0
seeds 43/44), so the DV reduced to the bare Leg-B 5-tick refractory whose magnitude (~20-35
tick-blocks) is **swamped** by the ~530-560 natural-commit elevated steps. NOT a falsification
(seed 42 + 460e seed 44 are existence proofs of the correct de-commit SIGN); the residual gap is
de-commit-authority **MAGNITUDE** + **DV POWER** (the latter is experiment-side, see Validation).

**The fix (part a; no-op-default, bit-identical OFF):** scale the Leg-B refractory installed at
a closure fire by the **committed-run length** captured from the BetaGate *before* the closure's
own `release()`, so a long committed run -- the exact source of the swamping latch occupancy --
triggers a proportionally long post-closure hold:

```
n = closure_decommit_hold_ticks
    + round(closure_decommit_hold_scale_with_run * committed_run_length)   # clamped to
                                                                            # closure_decommit_hold_max_ticks (0=uncapped)
```

- `ree_core/heartbeat/beta_gate.py`: `BetaGate` gains a per-run `_committed_run_length` counter +
  `committed_run_length` property + `sd034_committed_run_length` get_state key. Incremented once
  per `propagate()` tick while elevated; reset on a FRESH `elevate()` (not-elevated -> elevated;
  a re-elevate while already elevated leaves it unchanged) and on `release()`; cleared in
  `reset()`. Pure bookkeeping -- never read unless the lever is armed, so bit-identical when off.
- `ree_core/governance/closure_operator.py`: `ClosureOperatorConfig` gains
  `decommit_hold_scale_with_run` (0.0) + `decommit_hold_max_ticks` (0). `_fire()` captures
  `run_length_at_fire` from `beta_gate.committed_run_length` BEFORE step (a) `release()` (which
  resets it), then step (a.2) installs the scaled hold. With scale 0.0 (default), `hold_ticks ==
  decommit_hold_ticks` unchanged -> bit-identical to the fixed-hold path.
- `ree_core/utils/config.py`: `REEConfig.closure_decommit_hold_scale_with_run` (0.0) +
  `closure_decommit_hold_max_ticks` (0) + `from_dims` passthrough; `ree_core/agent.py` forwards
  both into the `ClosureOperatorConfig` build via getattr fallback (absent flat attr ->
  bit-identical), mirroring the `closure_decommit_hold_ticks` precedent.

**On the autopsy's "EITHER...OR"** (committed-run-scaled refractory OR active MECH-342-style
release-pressure): the closure `_fire()` ALREADY calls `beta_gate.release()` (drops the latch at
the fire), so option B's "drive the latch DOWN rather than block re-entry" distinction is moot
here -- the latch is already down at fire; the only lever is HOW LONG to keep it down, which is
exactly the refractory. So the committed-run-scaled refractory is the faithful magnitude lever;
an active release-pressure event would duplicate MECH-342 with no distinct mechanism (user-confirmed
A-only, 2026-06-19).

**Backward compatible:** `closure_decommit_hold_scale_with_run=0.0` by default -> the refractory
uses `closure_decommit_hold_ticks` exactly as the 2026-06-12 Leg-B landing -> bit-identical; the
run-length counter increments but is never read. 6 new contracts in
`tests/contracts/test_sd034_decommit_magnitude.py` (C1 counter lifecycle + get_state; C2 scale 0.0
bit-identical independent of a 40-tick run; C3 scale>0 -> `n = base + round(scale*run)` captured
before release + longer-run->longer-hold; C4 max_ticks clamp; C5 from_dims + agent wiring; C6
agent action stream bit-identical default vs explicit scale=0.0) + 7/7 preflight + full contract
suite 1101 passed (the 3 failures -- `control_vector` C4 + 2 `runner_fail_branch` -- are the
documented pre-existing flakes, CONFIRMED failing identically on a clean stash). Activation smoke
(the 460f scenario, 530-step committed run then a closure fire): FIXED base5/scale0 -> 5 ticks
suppressed (swamped); SCALED base5/scale0.1 -> 58 ticks (capped 60 -> 58) -- the de-commit
authority now scales with the latch occupancy it must overcome.

**Phased training:** N/A (control-state counter + scalar arithmetic; no learned parameters).
**MECH-094:** N/A -- waking `select_action` control-state transition; no replay/memory write
surface (the run-length counter only advances on the waking `propagate()` path). **Step-8.5
staleness:** NOT triggered (no-op-default lever; no dependent claim's measured mechanism changed --
KEEP all evidence). **Governance:** PROMOTES NOTHING; SD-034 provisional / MECH-260 candidate /
MECH-261 stable, all non_contributory + pending_retest_after_substrate; `claims.yaml` NOT modified.

**Validation experiment:** V3-EXQ-460g (supersedes V3-EXQ-460f) via `/queue-experiment` -- the
de-commit retest arming the magnitude lever (`closure_decommit_hold_scale_with_run` + max_ticks)
ON TOP of the beta-engagement-amended substrate, with **part (b)** the C2 DV redesigned to a
WITHIN-ARM around-closure occupancy delta (pre-vs-post-closure window on the ON arm) and the
non-vacuity gate tightened to `sd034_n_closure_coupled_elevations > 0` on scored seeds.
Acceptance: ON<OFF de-commit on the within-arm non-cap-pinned statistic on >=2/3 seeds with the
coupling non-vacuity gate met. Do NOT re-author 460d/460e/460f; the parallel V3-EXQ-468e
(MECH-090 commit-entry conjunction) leg is separately owed. The
`commitment-closure-control-plane` substrate_queue `ready` STAYS false until 460g scores a
contributory PASS. Autopsy: `evidence/planning/failure_autopsy_V3-EXQ-460f_2026-06-18.md`.

## Children (de-commit pipeline decomposition 2026-06-19)

Routed by confirmed `failure_autopsy_V3-EXQ-460g_2026-06-19` (the 7th autopsy of this
cluster; the 460f WATCH ITEM fired). User-approved 2026-06-19T20:38Z. Full spec:
`evidence/planning/claim_synthesis_SD-034-closure_2026-06-19.md`.

The 7-autopsy chain (460b..460g, 2026-06-04..06-19) showed the single SD-034 "behavioural
de-commit authority over the MECH-090 beta latch" sub-property bundles a **multi-stage
de-commit pipeline**: closure-firing (S1, closed via the Leg-A env-completion hook, 460d
C1 PASS), detector magnitude / trained head (S2, a built substrate leg), closure->beta
**coupling engagement** (S3), de-commit **magnitude** (S4), and coupling-measurability-
under-refractory (S5). The decisive evidence is the **double dissociation** across 460f/460g:
coupling ENGAGES yet magnitude is INSUFFICIENT (460f seed 42: 36 coupled elevations but
swamped by ~530-560 natural-commit elevated steps) vs magnitude HAS AUTHORITY yet coupling
is UNMEASURABLE (460g seed 42: within-arm occupancy 0.333 -> 0.0 but coupling counter 0).
A single property cannot express that; two named children can.

SD-034 stays the **umbrella `design_decision`** (closure-operator existence + five-part
"done" token firing + No-Go install retained; provisional; NOT demoted, NOT superseded).
The de-commit-authority sub-clause is decomposed into:

- **MECH-445 -- closure->beta coupling engagement (S3).** A closure-plane commit elevates/binds
  the MECH-090 latch via the `use_closure_commit_beta_coupling` path *independent of* a natural
  `running_variance < commit_threshold` commit-entry. `depends_on: SD-034, MECH-090, SD-033a`.
  Lit: Collins & Frank 2014 (OPAL task-set disengagement); Smith & Graybiel 2013 (stop-bracket).
  Falsifier: a refractory-independent commit-intent counter `> 0` on >= 2/3 seeds incl. a
  strong-natural-commit seed; falsified if the closure-plane commit only co-occurs with a natural
  `result.committed` (coupling inert).
- **MECH-446 -- de-commit-authority magnitude (S4).** The closure-coupled de-commit lowers
  post-closure latch occupancy with authority sufficient to overcome the natural-commit occupancy
  it competes against; the committed-run-scaled refractory drives a within-arm around-closure
  occupancy drop scaling with committed-run length. `depends_on: SD-034, MECH-090, MECH-445,
  MECH-342`. Lit: Mayr & Keele 2000 (post-completion refractory strength); Cavanagh & Frank 2011
  (STN graded release -- targeted lit addition recommended, non-blocking). Falsifier: ON-arm
  within-arm post-closure occupancy below pre-closure by >= `DECOMMIT_MIN_DROP_FRAC` on >= 2/3
  seeds, measured on a refractory-independent coupling gate.

**Refused (anti-proliferation rail) -- NOT a claim:** *coupling-measurability-under-refractory*
(S5, the 460g signature where a strong-enough refractory suppresses the very coupling metric the
de-commit is scored by) is a **measurement / test-design property** with no biological mechanism
to ground. It is handled by the **460h experiment fix** -- a refractory-independent commit-intent
counter (increments on the closure-plane commit INTENT, `e3._committed_trajectory` forming while
`not result.committed`, BEFORE the elevate/refractory gate) -- which is why both children carry
"refractory-independent coupling gate" in their falsifiers. The gated 460h re-queue targets the
re-grained children **MECH-445 / MECH-446**, NOT the coarse SD-034 umbrella; new letter, do NOT
re-author 460d/460e/460f/460g.

## Amend: refractory-independent commit-intent coupling certifier (460h fix) -- 2026-06-19

**Status:** IMPLEMENTED 2026-06-19 (substrate; MECH-445/446 stay candidate / v3_pending /
pending_retest_after_substrate -- PROMOTES NOTHING). Routed by the confirmed
`failure_autopsy_V3-EXQ-460g_2026-06-19` `recommended_substrate_queue_entry` (SECONDARY
action; the Children decomposition above is the PRIMARY action and this amend's precondition).

This lands the measurement fix the Refused item (S5, *coupling-measurability-under-refractory*)
is routed to -- it is the 460h experiment fix, NOT a claim. The S5 self-defeating entanglement
(code-confirmed): the 460f coupling non-vacuity gate keyed on `sd034_n_closure_coupled_elevations`,
counted by `note_closure_coupled_elevation()` INSIDE the bistable elevate if-block guarded by
`not beta_gate.is_elevated` (`agent.py`). Once the closure-coupled commit latches beta elevated
for the long committed run (~530-560 steps) the per-ENTRY counter freezes, and the 460g
committed-run-scaled de-commit-MAGNITUDE refractory (`apply_refractory` cap 60) blocks
re-elevation so it cannot re-fire as a transition -- so scaling the de-commit authority UP
suppresses its own certifier (counter 36 -> 0 on seed 42) even though the de-commit acted
(within-arm occupancy 0.333 -> 0.0).

**The fix (no-op-default; bit-identical OFF; rides `use_closure_commit_beta_coupling`):**
`BetaGate` gains `_n_closure_commit_intent` + `note_closure_commit_intent()` +
`sd034_n_closure_commit_intent` (get_state) + per-episode reset. `REEAgent.select_action`
calls `note_closure_commit_intent()` when `_closure_commit_active and not result.committed`
**BEFORE** the elevate/refractory gate, so the closure-plane commit INTENT is certified every
E3 tick a closure-coupled commitment forms without a natural `running_variance` crossing --
regardless of whether the latch is held elevated OR the de-commit-magnitude refractory then
blocks the elevate. `sd034_n_closure_coupled_elevations` is retained (now measures
refractory-/latch-surviving elevations only); the new counter is the refractory-INDEPENDENT
**MECH-445** coupling-engagement certifier that **MECH-446**'s magnitude lever cannot zero.

Pure control-state readout (no gate-state effect): the action stream is bit-identical with the
coupling flag OFF (every existing experiment) AND ON. MECH-094 N/A (waking select_action
readout; no replay/memory write surface). 3 new contracts (C6 primitive advances under an
active refractory + get_state/reset; C7 the load-bearing property -- a blocked elevate gate
freezes the coupled counter at 0 while the intent counter keeps certifying; C8 coupling-OFF
intent stays 0).

**Validation:** `V3-EXQ-460h` (supersedes the de-commit lineage; do NOT re-author 460d/e/f/g)
arms the full amended substrate (`beta_gate_bistable` + `use_closure_commit_beta_coupling` +
Leg-A env-completion hook + Leg-B committed-run-scaled refractory magnitude lever + Leg-C
`scaffold_train_rule_bias_head`), keeps the 460g within-arm around-closure occupancy-delta C2 DV,
and gates non-vacuity on `sd034_n_closure_commit_intent > 0` (NOT the coupled counter). Acceptance:
closure-coupled commit-intent `> 0` on >= 2/3 seeds (MECH-445 precondition) AND ON within-arm
post-closure occupancy `<` pre-closure by >= `DECOMMIT_MIN_DROP_FRAC` on >= 2/3 seeds (MECH-446
scored). `claim_ids=[MECH-446]` (scored) + MECH-445 (coupling-engagement non-vacuity precondition).

## Anchor Documents

- Anchor doc: `REE_assembly/evidence/planning/sd033_governance_plan.md`
- Source thought file: `docs/thoughts/2026-04-20_ocd4.md`
- Lit-pull review: `evidence/literature/targeted_review_sd_034/` (6 entries, 2026-04-21 + 2026-04-27)
- Implementation notes (full): `ree-v3/CLAUDE.md` lines 1476-1555
