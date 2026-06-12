# Failure Autopsy -- SD-034 ClosureOperator behavioural cluster (V3-EXQ-468c + V3-EXQ-460c)

- generated_utc: 2026-06-12T11:25:25Z
- scope: cluster (2 FAILs)
- status: confirmed (2026-06-12T22:16Z governance cycle; user AskUserQuestion "Apply as recommended"; 460c/468c manifests reclassified non_contributory + substrate_ceiling + pending_retest, SD-034 substrate_queue amended). COHORT EXTENSION PENDING: 461c/464c/466c/467c/629b landed and were flagged this cycle for a /failure-autopsy cluster extension (governance left them pending, no inline evidence_direction applied).
- targets:
  - V3-EXQ-468c -- run `v3_exq_468c_sd034_mech268_commitment_vs_contradiction_behavioural_20260612T080105Z_v3` -- claim_ids [SD-034, MECH-268, MECH-090]
  - V3-EXQ-460c -- run `v3_exq_460c_sd034_verified_but_not_released_behavioural_20260612T090021Z_v3` -- claim_ids [SD-034, MECH-260, MECH-261]
- substrate (both): `scaffolded_sd054_onboarding` full curriculum (Stage-0 -> 0b -> P0 -> Stage-H -> P1 -> P2; 603n config; ready=true 2026-06-11) + commitment control-plane (bistable BetaGate MECH-090 + SD-034 ClosureOperator + SD-033a LateralPFC + SD-032 dACC/salience; 468c also MECH-268 dACC PE saturation + GAP-3 contradiction env primitives; 460c also subgoal_mode waypoint tolerance-band completion).
- cohort context: these are the first two landed results of the commitment_closure:GAP-4 `*c` cohort (468c/460c/461c/464c/466c/467c + 629b). 461c/464c/466c/467c/629b had not landed at autopsy time -- they share substrate + likely failure shape and should be folded into this cluster as they arrive.

---

## 1. Why these two cluster

Both circle the **SD-034 ClosureOperator** on the **same 603n foraging-competent substrate**, both **passed their pre-registered non-vacuity gates** (`route_reason: criteria_unmet_genuine_weakens`), and both show the **same shape**: the closure control-plane's *proximal* signal partially fires or is reachable, but the *distal* behavioural consequence -- de-commitment of the MECH-090 latch / closure done-token / No-Go install -- does not occur. A convergent failure across two structurally-different SD-034 behavioural probes is the load-bearing signal; per-FAIL each would read as tuning noise.

This is NOT the third-or-later autopsy circling SD-034 with a *different* signature each time (the granularity-debt tell). The only prior SD-034 autopsy is `failure_autopsy_V3-EXQ-460b-461b-464b-466b_2026-06-04` -- the `*b` cohort, which self-scored `n_closures=0` because `committed_mode_curriculum` trained commitment but NOT foraging competence (the substrate was never engaged). The `*c` cohort is the **corrective successor**: it rebuilt on the 603n scaffolded curriculum specifically to supply that foraging competence. So this is convergent iterative substrate engineering on one mechanism (no-foraging -> foraging-competent-but-closure-inert), **not** granularity debt. No `/claim-synthesis`.

---

## 2. Facts -- V3-EXQ-460c (SD-034 verified-but-not-released; MECH-260 No-Go; MECH-261)

Criteria (all guard-passing seeds 42/43/44; contact + commitment/completion non-vacuity gates BOTH met, fraction 1.0):

| Criterion | load-bearing | passed | per-seed |
|---|---|---|---|
| C1 `n_closures >= 1` (ON arm) | yes | **FAIL** | n_closures = 0 / 0 / 0 in ARM_CLOSURE_ON despite n_sequence_completions = 2 / 5 / 6 |
| C2 `beta_release_events >= 1` | yes | PASS | 483 / 166 / 200 |
| C3 `nogo_installed_total >= 1` | yes | **FAIL** | 0 / 0 / 0 (downstream of closure; closure never fired) |
| C4 OFF holds latch / never closes | yes | mixed | seed 42 true, 43/44 false |

`criteria_non_degenerate`: all true. ARM_CLOSURE_OFF reached MORE sequence completions (7 / 6 / 8) than ARM_CLOSURE_ON (2 / 5 / 6), and n_closures=0 in BOTH arms. So **with closure ON, the ClosureOperator never emitted a done-token even though the env reported real task completions and the agent was committed with beta elevated** (total_committed_steps ~2400, total_beta_elevated 167-535).

Failed criterion type: **discrimination** (C1/C3 are the SD-034 signature; C2 absolute control passes).

## 3. Facts -- V3-EXQ-468c (SD-034 closure + MECH-268 dACC PE saturation + MECH-090 release)

| Criterion | load-bearing | passed | per-seed |
|---|---|---|---|
| C1 `beta_release_near_contradiction >= 1` (ON) | yes | PASS | 14 / 14 / 69 (vs OFF 6 / 8 / 20 -- ON releases MORE near contradiction) |
| C2 ON `committed_frac_post_vs_pre < 0.85` | yes | **FAIL** | 39 / 34 / 35 (vs OFF 39 / 31 / 29) |
| C3 OFF perseverates | yes | PASS | -- |

`criteria_non_degenerate`: all true. `mean_committed_pre = 5`, `mean_committed_post = 195` in BOTH arms (so `committed_frac_post_vs_pre = post/pre ~= 39` -- structurally >= 1 whenever the agent commits at all in the 195-step post-window). C1 PASS means the closure/saturation ON arm DOES fire more beta releases near contradictions; C2 FAIL means those releases do not translate into a net drop in committed-step occupancy -- the agent immediately re-commits and `committed_post` pins at the window cap in both arms.

Failed criterion type: **discrimination** (C1 absolute fires; C2 the behavioural-effect discrimination fails on a cap-pinned metric).

---

## 4. Code-grounded root cause (the load-bearing finding)

`ree-v3/ree_core/governance/closure_operator.py` -- the done-token fires by exactly two paths:

1. **Automatic detector** (`tick`): `||rule_state_t - rule_state_{t-1}|| < completion_rule_delta_threshold (0.001)` for `completion_stable_ticks (3)` consecutive ticks **AND** rule_state has meaningful magnitude (a near-zero rule_state is "trivially stable" and is filtered out) **AND** beta elevated **AND** `operating_mode in allowed_closure_modes` **AND** `write_gate("sd_033a") >= min_sd033a_write_gate (0.5)`.
2. **Explicit** (`emit_closure(action_class, z_world)`): "used by **environment completion hooks**."

The 460c env emits `transition_type == "sequence_complete"` (subgoal_mode waypoint tolerance), but the experiment **never routes that signal into `emit_closure()`** -- it relies solely on the automatic detector. On the scaffolded foraging agent that automatic conjunction is not co-satisfied at completion moments:

- the SD-033a `rule_bias_head` is zeroed-init unless `train_rule_bias_head=True` (GAP-D); on these arms the lateral-PFC `rule_state` is plausibly near-zero or continuously perturbed by SP-CEM diversity, so it never holds `delta<0.001` for 3 ticks **with meaningful magnitude** (the "trivially stable zero" filter);
- and/or the `sd_033a` write-gate / `allowed_closure_modes` conjunction is not cleared at those ticks.

Net: **the env's actual task-completion events and the ClosureOperator's trigger condition are decoupled, and the explicit env->`emit_closure` hook the docstring describes is not wired.** The closure mechanism was never given the chance to fire on a real completion. `n_closures=0` is a *trigger-availability* failure, not a closure-that-fired-and-did-nothing.

For 468c, the closure-coupled bistable releases DO fire (C1), but a single release does not hold -- the latch re-elevates and `committed_post` pins at the cap, so the **release lacks behavioural authority over net latch occupancy**, and C2 (`committed_frac < 0.85*pre`) is a near-cap-pinned statistic that demands near-total commitment cessation rather than a measurable de-commitment delta.

This is the same family of finding as the dominant cluster theme (modulatory-bias-selection-authority: 569f/661/654a/643/667/485e) -- a substrate computes a proximal signal that has no *authority* over the committed action -- but here at the **commitment-latch occupancy** layer rather than the E3-argmin layer.

### The non-vacuity gates checked the WRONG precondition (V3-EXQ-642 pattern)

460c's gate asserted "ON arm committed AND reached env completions, so closure HAD an opportunity to fire". But the ClosureOperator's *actual* trigger is rule_state-stability + sd_033a-gate + mode + meaningful-magnitude, NOT env completion. Reaching an env completion does not establish that the closure detector's trigger was satisfiable. The gate verified env-completion-availability when it needed to verify **closure-detector-trigger-availability** (`n_closures>0` reachable) -- exactly the V3-EXQ-642 lesson (a self-route precondition test that checks the wrong branch assumption).

---

## 5. Claim-layer map -- did the test let the claims express?

| Claim | type / status | tested fairly? | reading |
|---|---|---|---|
| SD-034 (closure operator) | design_decision / provisional / v3_pending=false | **NO** -- the done-token never fired (460c) because its trigger was unmet + env->emit_closure unwired; in 468c the release fired but had no de-commitment authority + C2 cap-pinned | intact; not falsified |
| MECH-260 (dACC No-Go) | mechanism_hypothesis / candidate / v3_pending / pending_retest_after_redesign | **NO** -- No-Go install is strictly downstream of a closure event; with n_closures=0 it could never fire | intact |
| MECH-261 (mode-conditioned write-gate) | mechanism_hypothesis / **stable** | **NO** -- not the subject under test here; carried as a tag, not exercised | do not weaken a stable claim on this |
| MECH-268 (dACC PE saturation) | mechanism_hypothesis / provisional | partial -- coupled into the closure release; C1 (more release near contradiction) is a weak positive | intact; C2 inconclusive |
| MECH-090 (beta latch) | mechanism_hypothesis / active | partial -- the latch elevates/releases; the gap is release-hold authority, not the latch itself | intact |

`claim_ids` accuracy: the tags are inherited correctly from the mechanism set, but **none of these claims could express its behavioural prediction** because the closure done-token's trigger was unreachable (460c) or the release lacked latch authority + the metric was cap-pinned (468c). An implementation/integration gap must not demote a provisional design_decision or weaken a stable claim.

---

## 6. Biological-reference triage

- **SD-034 closure operator** closest mechanism: OFC sequence-completion cells (Rich & Shapiro 2009) + frontal task-set disengagement (Collins & Frank 2014) + mPFC task-stage encoding (Schuck 2016). Faithful biological translation (not a formal-definition import). Completion-triggered disengagement is a real, working mechanism -- a clear existence proof for the *class*.
- **Missing-dependency signature?** Yes. Biologically, the disengagement signal is driven by the *actual* completion of the task sequence (the animal reaching the goal), not by an internal rule-vector happening to stabilise. The REE failure -- env completion occurs but the internal completion detector does not recognise it -- is precisely what you would see if the dependency "completion-event -> closure trigger" were absent. The FAIL is a **discovered missing coupling**, not a falsification.
- **468c release-authority**: BG-thalamo-cortical de-commitment (Cisek & Kalaska 2010; STN conflict-graded release, Cavanagh & Frank 2011) is a *held* state change, not a one-tick blip. A release that immediately re-commits is the signature of a missing hold/refractory term -- a missing dependency, not evidence the closure mechanism is wrong.
- lit status: `present` for the closure mechanism class (Rich/Collins/Schuck already anchor SD-034). No new `/lit-pull` required.

---

## 7. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | the test did not let SD-034/MECH-260 express; MECH-261 not exercised |
| Biological reference | clear | OFC completion cells; failure matches a missing completion->closure coupling |
| Developmental / dependency prerequisites | missing | env `sequence_complete` -> `emit_closure` hook unwired; rule_state-stability trigger unmet (zeroed/untrained rule_bias_head; SP-CEM perturbation) |
| Implementation completeness | partial (symbol-without-functional-role) | ClosureOperator present and wired; its trigger is decoupled from real completions and its release lacks hold authority |
| Environment adequacy | adequate | 603n foraging competence achieved; env emits completions + contradictions |
| Measurement adequacy | under-instrumented / misleading | 460c gate checked env-completion not closure-trigger-availability; 468c C2 is a cap-pinned ratio (post/pre ~39) demanding near-total commitment cessation |
| Integration adequacy | isolated | the closure done-token does not propagate to committed-latch occupancy / No-Go install on this agent |
| Scale / capacity | adequate | not a budget problem |

Recommended `epistemic_category`: **substrate_ceiling** (the substrate has the closure wiring the claims assert but does not carry the completion->closure->de-commitment information at the granularity the claims assert).

---

## 8. Cluster pattern table

| Experiment | Claim(s) | Absolute / control criterion | Discrimination criterion | Read |
|---|---|---|---|---|
| V3-EXQ-460c | SD-034 / MECH-260 | C2 beta_release >= 1 PASS | C1 n_closures>=1 + C3 nogo_install FAIL (closure done-token never fired despite env completions) | closure trigger unreachable -- env completion not routed to emit_closure; rule_state-stability conjunction unmet |
| V3-EXQ-468c | SD-034 / MECH-268 / MECH-090 | C1 beta_release_near_contradiction>=1 PASS (ON > OFF) | C2 committed_frac drop FAIL (cap-pinned 39x both arms) | release fires but lacks hold authority over latch occupancy; metric near-cap-pinned |

**One structural property, not two independent bugs:** *the SD-034 closure control-plane is wired and its proximal events partially fire/are reachable, but on the 603n foraging-competent agent it has no behavioural authority over MECH-090 latch occupancy -- because (a) the env completion signal is not routed into the closure trigger, and (b) the closure/release has no de-commitment hold.* Both readings below are live:

- **Reading 1 (substrate-integration + measurement defect -> non_contributory):** the closure detector never fired / the release lacked authority + C2 cap-pinned -> the FAILs do not license a weakens. **Decisive evidence: n_closures=0 on ALL seeds despite high beta-elevation and real env completions = the claim was not tested under conditions where it could express.** Forces: amend the closure substrate + re-queue.
- **Reading 2 (genuine weakens of SD-034 behavioural prediction):** substrate is foraging-competent, closure ON, completions/contradictions occurred, still no behavioural effect -> SD-034 demotion candidate. Forces: governance demotion.

**Reading 1 dominates.** 468c C1 PASS (closure-coupled release fires MORE under ON) is a partial positive that the mechanism is doing something; 460c proves the done-token's trigger was simply never satisfiable. Demotion needs tested-fairly + biology-supports + still-fails; the first condition is not met. Route to substrate amend, NOT demotion.

---

## 9. Learning extracted

- New dependency discovered: SD-034 closure requires the **env task-completion event routed into `emit_closure()`** (the explicit hook the docstring describes but the `*c` experiments do not wire), and/or a **trained, magnitude-bearing rule_state** (GAP-D `train_rule_bias_head`) so the automatic rule-stability detector can fire with meaningful magnitude.
- Existing dependency strengthened: MECH-260 No-Go is strictly downstream of a closure event -- its zero is a positive-negative confirming the closure->No-Go ordering, not a No-Go failure.
- Implementation gap: the closure release (468c) needs a **de-commitment hold / refractory term** so a release survives >1 tick and produces a measurable latch-occupancy delta.
- Measurement gap: the readiness precondition must gate on **closure-detector-trigger-availability** (`n_closures>0` reachable on the positive control), not env-completion-availability (V3-EXQ-642 lesson); and 468c's de-commitment DV must be a **non-cap-pinned statistic** (e.g. fraction of post-contradiction ticks uncommitted, or committed-run-length delta), not `post/pre` against a 5-step pre-baseline.

---

## 10. Routing

- **Primary: `/implement-substrate` (action=amend)** on the SD-034 ClosureOperator + commitment control-plane (existing commitment_closure substrate track). Amend: (a) route env `sequence_complete` into `emit_closure()`; (b) add a de-commitment hold/refractory term to the closure-coupled release; (c) ensure the rule_bias_head is trained (GAP-D) in the behavioural arm so the automatic detector has a magnitude-bearing rule_state.
- **Then `/queue-experiment`** the `*d` successors (468d/460d) that (i) wire env->emit_closure, (ii) gate readiness on `n_closures>0` reachable on the positive control, (iii) re-state the de-commitment DV on a non-cap-pinned statistic.
- **`/governance`**: reclassify both manifests `non_contributory` + `epistemic_category: substrate_ceiling` + `pending_retest_after_substrate=true` + `narrow_supports_flag=true` (SD-034's only supports are the 460/466/468 landing-diagnostic smoke sub-tests -- narrow / substrate-readiness, not behavioural). NO demotion of SD-034 (provisional holds). NO weaken of MECH-261 (stable). MECH-260 stays candidate. Mark both runs reviewed. Amend the commitment_closure substrate_queue entry with both failure records (ready stays false).
- NO `/claim-synthesis` (convergent iterative substrate engineering on one mechanism, not granularity debt).

### Draft evidence_quality_note (governance writes; do not write here)

SD-034 / MECH-260 (460c) + SD-034 / MECH-268 / MECH-090 (468c): non_contributory, substrate_ceiling, pending_retest_after_substrate. First behavioural arms of SD-034 on the 603n foraging-competent substrate. The ClosureOperator done-token never fired (460c n_closures=0 on 3/3 seeds despite env sequence_completions=2/5/6 and beta elevated) because the env completion signal is not routed into emit_closure() and the automatic rule_state-stability trigger (delta<0.001 x3 ticks + meaningful magnitude + sd_033a gate>=0.5 + allowed mode) is unmet on this agent (untrained/zeroed rule_bias_head + SP-CEM perturbation). 468c closure-coupled beta releases fire more under ON (C1 PASS) but lack hold authority over latch occupancy and C2 is a cap-pinned post/pre ratio. The non-vacuity gates checked env-completion-availability, not closure-trigger-availability (V3-EXQ-642 pattern). Not a falsification: the claims were not tested under conditions where they could express. Retest after amend (env->emit_closure + de-commit hold + trained rule_bias_head + n_closures>0 readiness gate + non-cap-pinned de-commitment DV).
