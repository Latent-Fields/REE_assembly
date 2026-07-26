# Failure Autopsy — batch: V3-EXQ-822a, V3-EXQ-826, V3-EXQ-817a, V3-EXQ-827

**Generated:** 2026-07-26T17:06:06Z
**Scope:** batch (4 independent targets from the same pending-review cycle; no shared claim, substrate, or failure shape across all four — each diagnosed separately, per the `failure_autopsy_batch-793a-817-819_2026-07-26` precedent for unrelated same-cycle FAILs)
**Status:** confirmed (user-adjudicated via AskUserQuestion, 2026-07-26)

This batch covers all 4 pending FAILs surfaced by a fresh `pending_review.md` regeneration (0 diagnostic self-routes were pre-flagged, but 3 of the 4 carry the self-route label `substrate_not_ready_requeue` — investigated individually since the underlying mechanisms differ).

---

## 1. V3-EXQ-826 — MECH-244 (psychosis as precision-weighting failure)

**Self-route:** `substrate_not_ready_requeue` — **MISNAMED.**

### Facts
First experimental test of MECH-244 (2 lit entries, 0 prior experimental entries, `exp_conf=0.0`). Manipulates `pe_precision` (a scalar gain on E1's own prediction-error gradient, via a dedicated optimizer scoped to `agent.e1.parameters()`) across ARM_CONTROL/LOW/VERYLOW, then measures adaptation to a deterministic regime change (hazard relocation) via `adaptation_ratio`.

All three P0 readiness preconditions measured **exactly 0.0** against thresholds 0.25 / 1.15 / 1.5:
- `world_model_converged_phaseA_control`: 0.0
- `regime_change_disconfirms_control`: 0.0
- `pe_precision_manipulation_took`: 0.0

`delta_verylow_per_seed` and `delta_low_per_seed` are `[0.0, 0.0, 0.0, 0.0, 0.0]` — not near-zero, bit-exact zero, for every seed, both arms. `arm_results.phaseA_episode_means` / `phaseB_episode_means` confirm E1's per-episode mean loss is literally `0.0` from episode 1 through episode 400.

### Root cause (traced in source)
`REEAgent.compute_prediction_loss()` ([ree_core/agent.py:8549-8567](../../../ree-v3/ree_core/agent.py)) hard-returns a zero-gradient stub (`next(self.e1.parameters()).sum() * 0.0`) whenever `len(self._world_experience_buffer) < 2`. That buffer is appended to **only** inside `_e1_tick()` ([agent.py:4641-4676](../../../ree-v3/ree_core/agent.py)), which is itself called **only** from `act()` / `act_with_split_obs()` / `act_with_log_prob()` ([agent.py:8208/8238/8260](../../../ree-v3/ree_core/agent.py)) — never from `sense()`.

V3-EXQ-826 deliberately uses pure random-action rollout (`action_idx = random.randint(...)`) rather than calling any `act*()` method, explicitly to "match the established V3-EXQ-818 convention, removing any policy confound." That design choice means `_world_experience_buffer` never reaches length 2, so `compute_prediction_loss()` is structurally pinned to its zero-gradient stub for the entire run, on every arm and seed. This is not a substrate-readiness or convergence problem — E1 itself is functional; the experiment script's driving loop never engages it.

The script's own degeneracy guard (`criteria_non_degenerate.C1 = false`) correctly caught the pinned-zero signature and self-routed to FAIL rather than reporting a false PASS or a false negative — the instrumentation did its job; only the self-route *label* mischaracterizes the cause.

**Precedent check:** the docstring cites `v3_exq_032`/`032b`/`032c` and `v3_exq_396a` as establishing the `sense()` + `compute_prediction_loss()` pattern. Reading those scripts shows the **identical** pattern — `agent.sense(...)` in a loop, random-action selection, `agent.compute_prediction_loss()` — with no intervening `act*()`/`_e1_tick()` call. Whether those historical runs share this defect is **not verified here** (out of scope for this autopsy) but is flagged as a follow-on audit.

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | MECH-244 untested — E1 never received a gradient |
| Biological reference | clear | precision-weighted PE gating on a generative model is a faithful, well-grounded operationalisation |
| Prerequisites | present | E1 module and its dependencies (MECH-094, INV-011) are fine |
| Implementation | absent (this run) | script never ticks E1 under random-action rollout; `compute_prediction_loss()` behaves exactly per its documented contract |
| Environment | adequate | regime-A/B hazard relocation is a clean disconfirming-evidence manipulation, untested only because E1 never trained |
| Measurement | adequate, self-diagnosing | P0/C1 degeneracy guard worked correctly |
| Integration | isolated | break is in the script's tick-driving loop, not cross-module coupling |
| Scale | not reached | no training occurred |

### Biological reference
Closest mechanism: precision-weighted PE gating on a generative world model (predictive-processing account of psychosis — dopaminergic/cholinergic PE-gain modulation). No biology divergence — the manipulation design is sound; the failure is purely at the script-wiring layer.

### Routing — **queue-experiment** (redesign, same question)
Route to `/queue-experiment` for **V3-EXQ-826a**: keep the random-action design (no policy confound) but explicitly tick E1 after `sense()` — e.g. `agent._e1_tick(latent)`, mirroring the pattern V3-EXQ-822a already uses correctly (see below). Separately, flag the `v3_exq_032` family and `v3_exq_396a` for a dedicated defect audit (not performed here).

---

## 2. V3-EXQ-822a — SD-078 (rule-selection consumer, SD-082 re-run)

**Self-route:** `substrate_not_ready_requeue` — correctly labelled as a precondition failure, but this is now the **second consecutive** identical failure of the same readiness gate.

### Facts
Same-question re-run of V3-EXQ-822 (autopsied in `failure_autopsy_816c-822_2026-07-26`, REE_assembly `afb2df901e`), which failed readiness gate (d) `propagation_non_vacuity` at exactly 0.0 while its other three gates passed. That autopsy routed to `/implement-substrate`, landing **SD-082** (`lateral_pfc_rule_readout_consumer`): (i) center the candidate-summary input across candidates (fixing the SD-008 ~0.98-cosine cone saturating every candidate to the same clamp rail), (ii) a scaled-tanh soft bound in place of a hard clamp (so the head stays gradient-trainable under REINFORCE).

V3-EXQ-822a enables SD-082 correctly: `lateral_pfc_rule_readout_consumer=True`, `lateral_pfc_train_rule_bias_head=True` are both set in config. The upstream chain is now strong and non-degenerate:
- `zworld_common_mode_cone_present`: 0.963 > 0.9 floor ✓
- `on_pool_differentiated`: 3.0 > 2.0 floor ✓
- `on_rule_active_p2`: 0.882 > 0.1 floor ✓
- `on_rule_state_diff_mean`: 0.644 (C1 `on_rule_state_differentiates` PASSES, non-degenerate) ✓

But **`on_prop_delta_mean` = `off_prop_delta_mean` = exactly 0.0 again** (`readiness_prop_nonvac: false`) — the exact same bit-pattern as 822's pre-fix failure.

### Root cause (traced in source, unverified — recording gap blocks confirmation)
`compute_bias()` ([ree_core/pfc/lateral_pfc_analog.py:359-416](../../../ree-v3/ree_core/pfc/lateral_pfc_analog.py)): SD-082's fix touches (i) centering `candidate_world_summaries` and (ii) the scaled-tanh output bound plus a `readout_init_scale=0.25` rescale of the **last** Linear layer's weights at init. `rule_bias_head` itself ([lateral_pfc_analog.py:227-244](../../../ree-v3/ree_core/pfc/lateral_pfc_analog.py)) is `Linear(rule_dim + world_dim, hidden_dim) → ReLU → Linear(hidden_dim, 1)` — the **first** Linear+ReLU layer is untouched by SD-082 and always uses standard random init, regardless of `train_rule_bias_head`/`rule_readout_consumer`.

**Working hypothesis (unverified):** dead or magnitude-insensitive ReLU units in the first hidden layer make the head's scalar output insensitive to the `rule_state` slice of its concatenated input — plausible if `rule_state`'s raw magnitude is small relative to the (now-centered) world-summary component, but the manifest carries **no head-internals diagnostics** (weight norms per phase, hidden-activation statistics, or the raw magnitude ratio between `rule_state` and the world-summary) to confirm or rule this out. This is a **recording gap**, not a measurement gap: the diagnostic data exists inside the live `nn.Module` at run time and simply was not persisted.

The `_prop_delta_and_flip` counterfactual itself (`lpfc.rule_state.zero_()` → `compute_bias()` → restore) is mechanically sound — it correctly isolates the rule_state contribution; the zero result is a genuine reading, not an instrumentation bug in the delta computation.

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | SD-078's downstream consumer behaviour still cannot be tested |
| Biological reference | clear | corticostriatal rule-to-action mapping requires a trained, *sensitive* read-out |
| Prerequisites | present | SD-082 landed and engaged; upstream chain fully healthy |
| Implementation | partial | SD-082 fixed the diagnosed saturation mechanism but propagation is still zero; a second, unaddressed insensitivity point (likely the untouched first layer) remains |
| Environment | adequate | |
| Measurement | under-instrumented for root-causing | no head-internals diagnostics recorded — a recording gap |
| Integration | isolated | upstream substrate healthy; break is inside the trained head |
| Scale | 5 seeds; per-seed prop_delta not reported (another instrumentation gap) |

### Biological reference
Closest mechanism: corticostriatal rule-to-action mapping. A differentiated rule representation with a read-out that is technically trainable but not actually coupled to the rule signal produces no behavioural propagation — a discovered second-order prerequisite (input-stage coupling), narrowing 822's "consumer absent" finding to 822a's "consumer present but its input-stage coupling appears broken." Not a claim falsification.

### Routing — **implement-substrate**, amend SD-082
Amend the SD-082 substrate_queue entry: add head-internals instrumentation (weight-norm tracking per phase, hidden-activation statistics, `rule_state`-vs-world-summary input magnitude ratio) and chase the dead-ReLU/insensitivity hypothesis as the lead, before queuing a third consumer-validation run. **Re-derive brake did not formally fire** (R3 counts only `substrate_ceiling` readings; this is `competence_implementation_gap`), but two consecutive identical-gate failures argue for a substrate amend over a third blind re-queue letter regardless.

---

## 3. V3-EXQ-817a — SD-004 / SD-080 (world-effect grounding falsifier)

**Self-route:** `grounding_real_but_not_load_bearing` — correctly labelled; this is already a clean, well-instrumented, self-consistent finding.

### Facts
Redesigned successor to V3-EXQ-817 (autopsied as `competence_implementation_gap` in `failure_autopsy_batch-793a-817-819_2026-07-26`; that autopsy's routing was exactly this redesign). 817 used a delta-prediction grounding objective that moved the head's parameters without inducing state-dependence. 817a replaces it with a state-dependence-targeted objective.

All four grounding-took preconditions PASS cleanly, with clean controls:
- `worldeffect_groundable_from_zworld`: MSE 0.773 ≤ 0.85 ceiling (ARM_2 shuffled control ~1.0, the no-structure baseline)
- `arm1_state_dependence_acquired`: r² 0.725 ≤ 0.90 ceiling (dropped from ARM_0/ARM_2's frozen baseline of ~0.99)
- `arm1_state_dependence_paired_drop`: 0.271 ≥ 0.10 floor (paired within-seed)
- `content_not_traffic_discriminated`: margin 0.275 ≥ 0.10 floor (ARM_2's shuffled target stays unfittable — confirms the effect is CONTENT, not gradient traffic)

`grounding_took = true`. The **load-bearing behavioural criterion** was then evaluated (not vacuously skipped) and FAILED: `ARM_1 harm_rate = 0.5144` vs `ARM_0 (frozen) = 0.4426` vs `ARM_2 (shuffled) = 0.4209` — grounding produced no behavioural benefit; nominally worse than the frozen baseline.

### Interpretation
The manifest's own summary is accurate and well-scoped: *"Grounding O in the world-effect took ... but did NOT change behaviour ... SD-004's semantic-grounding efficiency rationale is demoted; SD-080 stays candidate as a correctness-not-capability finding."* User-endorsed read (2026-07-26): score SD-004 and SD-080 on **different directions** rather than a blanket weakens on both —
- **SD-004** (`weakens`): the claim's behavioural/efficiency rationale — that a compressed, consequence-structured O drives measurably better long-horizon planning/harm-avoidance — is directly undercut: even when the representation is technically correct, no behavioural benefit manifests.
- **SD-080** (`non_contributory`, stays candidate): SD-080's core assertion is about the **unmodified** substrate ("O ... zero gradient from every REE training path"). V3-EXQ-817a's grounding objective is itself a bespoke, newly-added training path built specifically for this diagnostic — demonstrating grounding is *achievable in principle* does not establish that any *existing* REE path already grounds O. Not falsified; the claim's language may eventually need updating to acknowledge achievability, but that is a wording note, not a status change.

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | SD-080 intact/reframed; SD-004 weakened | see interpretation above |
| Biological reference | partial | SD-004's efference-copy/consequence-coding grounding is biologically motivated; this run's bespoke objective is a reasonable induction attempt that succeeded representationally |
| Prerequisites | present | the training objective SD-080 said was missing has now been built and shown to work |
| Implementation | complete (representational half) | representational grounding achieved; behavioural coupling from geometry to CEM planner choice is the remaining open link |
| Environment | adequate | |
| Measurement | adequate, thorough | 5-seed paired + shuffled controls, explicit non-gating of an unstable secondary readout (M6) rather than silently thresholding it — a model instance of self-aware instrumentation |
| Integration | isolated | frozen encoder, head-only grounding; a fully integrated grounding path is untested |
| Scale | adequate | low per-seed variance on the grounding metrics (unlike 817's unstable M6) |

### Biological reference
Closest mechanism: learned action-consequence (efference-copy/forward-model) compression. No divergence in the grounding mechanism itself; the gap is in SD-004's implicit assumption that achieving consequence-structured geometry is *sufficient* for behavioural benefit — the CEM planner's sensitivity to that geometry, or the training budget needed for a planner-side benefit to manifest, is a separate, still-open question.

### Routing — **governance demotion** (partial)
Recommend governance apply the split `evidence_direction_per_claim` above: SD-004 weakens (behavioural/efficiency rationale specifically), SD-080 non_contributory (stays candidate, wording note only).

---

## 4. V3-EXQ-827 — INV-091 (cross-stream similarity band)

**Self-route:** `substrate_not_ready_requeue` — honest and correctly scoped ("Not a verdict on INV-091"), but the label undersells a specific, traceable design confound.

### Facts
Three arms — `decouple` (landmark/IEI scramble, predicted LOWEST cross-stream similarity), `intact` (baseline), `lockstep` (forced synchronous tick cadence across all streams, predicted HIGHEST similarity — the collapse direction). Pre-registered non-degeneracy guard: `similarity(decouple) < similarity(intact) < similarity(lockstep)`, each gap above a floor.

Measured: `decouple = 0.2262`, `intact = 0.2715`, `lockstep = 0.1679`. First inequality holds (`decouple < intact`). Second inequality **reverses**: lockstep is the **lowest** of all three arms, not the highest — a directional reversal on the lockstep leg specifically, not a generic null.

### Root cause (traced in source)
`_force_lockstep()` ([experiments/v3_exq_827_inv091_cross_stream_similarity_band.py:261-265](../../../ree-v3/experiments/v3_exq_827_inv091_cross_stream_similarity_band.py)) sets `e1_steps_per_tick = e2_steps_per_tick = e3_base_steps = e3_current_steps = 1` — collapsing **all** stream tick rates to fire every environment step. Under `intact`, E3 by default ticks once per ~10 env-steps. This changes not only phase-alignment (the intended manipulation) but also the **tick sampling density/resolution** of every stream relative to `intact`. `_cross_stream_xcorr` operates in tick-unit lags (`max_lag_ticks=8`), so "8 ticks of lag" represents very different amounts of real elapsed time under `lockstep` vs `intact` — a plausible confound bundling synchrony together with a change in effective sampling resolution, which could pull the correlation statistic in an unintended direction.

The `decouple` leg (landmark/IEI scramble) behaved exactly as predicted — the design's problem is isolated to the `lockstep` leg's clock-rate lever, not the whole apparatus.

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | non-degeneracy guard failed; INV-091 itself untested |
| Biological reference | clear | synchronous cross-stream coupling as a substrate for temporal binding is a reasonable operationalisation intent |
| Prerequisites | present | decouple leg validates the apparatus works |
| Implementation | traced | `_force_lockstep()` conflates phase-alignment with tick-rate/sampling-density — a design-level confound, not a code bug |
| Environment | adequate for decouple/intact; lockstep's clock-rate collapse is the suspect leg | |
| Measurement | DV design gap | `_cross_stream_xcorr`'s tick-unit lag window isn't invariant to a per-stream tick-rate change |
| Integration | n/a | |
| Scale | 1 seed reported in this row (full per-seed detail not required for this autopsy's routing) |

### Biological reference
Closest mechanism: cross-stream temporal binding/phase-coupling (e.g. thalamocortical synchrony) as a substrate for integrated self-world representation — INV-091's emergent-invariant framing (emergent from ARC-025, MECH-063, MECH-069, SD-010, SD-011, MECH-035). No biology divergence identified; the gap is in the experimental operationalisation of "lockstep."

### Routing — **queue-experiment** (redesign, same question)
Route to `/queue-experiment` for **V3-EXQ-827a**: force phase-synchrony without altering per-stream tick rate/sampling density (e.g. align tick *boundaries* across streams while preserving each stream's own native rate), and/or normalize the cross-correlation window to real elapsed time rather than raw tick count so cross-arm comparisons sit on a common temporal scale.

---

## Cross-target notes

- No cluster shape ties these four together — different claims, different substrates, different failure mechanisms (script-side E1-tick omission; a second-order head-insensitivity gap surviving a first-round fix; a genuine well-instrumented negative behavioural result; a manipulation-design confound). Treated as an unrelated batch, per the `failure_autopsy_batch-793a-817-819_2026-07-26` precedent.
- Three of the four share the self-route label `substrate_not_ready_requeue`, but that label maps to three *different* actual causes here (script bug / second-order implementation gap / DV design confound) — reinforcing the skill's "self-route is a hypothesis, not a verdict" rule (canonical V3-EXQ-642).
- Re-derive brake did not fire for any target (none reached `substrate_ceiling` under the R1-R3 convention).
- No granularity-debt recurrence trigger fires: SD-078 has 2 autopsies now (822, 822a) but both are `precondition_unmet`/`competence_implementation_gap` reads, not `weakened` claim_alignment, and the signatures are related (same gate) rather than structurally different.
- Follow-on (not performed here, flagged for chipping): audit `v3_exq_032`/`032b`/`032c`/`v3_exq_396a` for the same E1-tick-omission defect found in V3-EXQ-826.

## Foreign TASK_CLAIMS entry swept into this session's claim-open commit

Per CLAUDE.md remedy (a): opening this session's TASK_CLAIMS claim (commit `71888e12ac`) carried a foreign, complete, uncommitted claim entry `igw-auto-igw-209-proposal-for-arc-112-20260726T170308Z` (new, complete) along with it. Preserved, not reverted — surfaced here per the standing remedy.
