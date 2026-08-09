# Failure Autopsy — V3-EXQ-190a (MECH-022 Hypothesis Injection Probe, well-powered)

**Generated:** 2026-08-09T05:43:28Z
**Scope:** single
**Status:** confirmed (interactive gate run 2026-08-09 — user confirmed REJECTING the manifest's own self-declared `Decision: retire_ree_claim`)

## 0. Bottom line

The manifest's own `Decision: retire_ree_claim` is **not accepted**. The demotion bar ("tested fairly + biology supports the mechanism + still fails") is not met on the "tested fairly" leg, on two independent, code-verified grounds: (1) two of E3Selector's four trajectory-scoring cost components are never trained anywhere in the codebase, contaminating both conditions with random-init noise; (2) this run newly extends a forced-random-action override into the eval loop (absent in the predecessor), diluting exactly the signal C1/C2 need. **Recommended reading: `non_contributory`/`competence_implementation_gap`, routed to `/implement-substrate`, not demotion.**

## 1. Facts

Manifest `v3_exq_190a_mech022_hypothesis_injection_probe_wellpowered_20260809T002451Z_v3`, `claim_ids: ['MECH-022']`, `supersedes: v3_exq_190_mech022_hypothesis_injection_probe`. Design changes vs V3-EXQ-190: `nav_bias` 0.25->0.40, `eval_episodes` 50->100, `warmup_episodes` 150->220, seeds 2->3.

| Criterion | Threshold | 190 (predecessor) | 190a (this run) |
|---|---|---|---|
| C1 harm_gap, all seeds >=0.005 | 0.005 | PASS: [0.0062, 0.0168] | **FAIL**: [0.00252, -0.00706, -0.00007] |
| C2 residue_gap, all seeds >=0 | 0.0 | PASS: [0.559, 0.019] | **FAIL**: [-0.709, 0.246, 0.244] |
| C3 traj_gap, all seeds <0 | 0.0 | FAIL: [-716.4, +3.8] | **FAIL**: [-6.65, -35.23, +141.17] |
| C4 n_harm_min >=10 | 10 | FAIL: 0 | PASS: 148 |
| C5 score_var >1e-6 (ON) | 1e-6 | PASS | PASS |

2/5 criteria met -> FAIL, not degenerate.

**A design change the docstring does NOT flag as a design axis but the code confirms is qualitatively new**: in V3-EXQ-190, the `nav_bias` random-action override appears only in the training loop; the eval loop is pure `agent.select_action(...)`. In 190a, the identical override is **also applied inside the eval loop** ("the deliberate C4 fix"). `n_harm_min` genuinely rose 0->148 (real C4 fix), but the mechanism (forcing 40% of eval actions to be random regardless of condition) is not power-neutral for C1/C2, which need condition-dependence to resolve — a plausible cause of C1's collapse from clean PASS (190) to near-zero/negative (190a), including a **sign flip** on repeated seed 123 (+0.0168 -> -0.00706).

**Code-verified implementation gap** (`ree_core/predictors/e3_selector.py`, `score_trajectory()`, fallback path, no `harm_forward_model` kwargs passed by this driver):
```
score = f_weight*F(zeta) + lambda_eff*M(zeta) + rho_residue*Phi_R(zeta)
```
- F(zeta) = `compute_reality_cost`: uses `self.reality_scorer` (an `nn.Sequential`, instantiated at `__init__`, line 243).
- M(zeta) (fallback) = `compute_harm_cost_fallback`: uses `self.harm_cost_fallback_scorer` (a second `nn.Sequential`, line 253) *on top of* the trained `harm_eval_head`.

Exhaustive grep across `ree_core/` and the driver: **`reality_scorer` and `harm_cost_fallback_scorer` appear only at instantiation and inside these two cost functions — never inside any loss computation anywhere.** The driver's only E3-side training signal is `harm_loss = F.mse_loss(agent.e3.harm_eval(z_world), harm_target)`, which trains only `harm_eval_head`. Both scorer heads therefore contribute random-initialization noise to every trajectory score, in both conditions, for the whole run — and `agent.select_action()` routes through this same E3 selection machinery for the action actually taken at every tick, so this plausibly corrupts the policy itself, not merely the C3 diagnostic readout.

This is the textbook shape of the skill's core principle: "an implementation that has the symbol of the mechanism but not its functional role." The architecture correctly assigns value-computation to E3 (biologically appropriate, per ARC-007's own resolution — hippocampus should not compute value), but two of E3's four scoring subcomponents were never wired into this experiment's training loop.

Dry-run check: clean.

## 2. Claim-layer mapping

MECH-022 (`docs/claims/claims.yaml`): "Hippocampal systems inject hypotheses gated by control plane." `status: provisional`, no `epistemic_category` or `evidence_quality_note` ever applied — this is the first confirmed adjudication opportunity for MECH-022. `depends_on: [ARC-007, ARC-005]`.

**ARC-007 (direct dependency) was independently demoted active->provisional on 2026-07-25** on the *identical* E3-routed-selection seam: V3-EXQ-114a found the harm-reduction advantage collapses to 11.4% (< 15% required) once E3-routed selection with a matched episode budget and a static no-op control is used — the earlier 99.2% headline was "a denominator artefact of a constant action stream." **This is a load-bearing structural signal, not coincidence**: both claims cleanly passed a first, less-rigorous test and both weakened once the E3-routing/selection stage was exercised more carefully. Not a formal cluster (different claim IDs, different drivers), but the same "convergent failure across structurally different claims sharing a substrate seam" pattern the skill treats as load-bearing, pointing at E3-selection specifically — independently confirmed by the code trace above.

## 3. Biological-reference triage

Closest reference: hippocampal SWR-mediated replay (offline and awake-quiescent), propagating to prefrontal/decision circuits for prospective planning. Existing lit review: `evidence/literature/targeted_review_connectome_mech_022/`, 4 entries, all `supports`, 0.72-0.78 confidence:

- Carr, Jadhav & Frank 2011 (0.72): awake replay is episodic, quiescence-gated, retrieves remote trajectories — matches "internally gated, retrieval-based injection." Explicitly notes the biology does *not* specify how content is selected once retrieved.
- Shin, Tang & Jadhav 2019 (0.76): strongest direct evidence — PFC reads and uses HPC replay content, correct upcoming paths preferentially represented. **Its own caveat is the crux**: "the internal E3 mechanism by which injected hypotheses are evaluated and selected is not illuminated by this paper."
- Joo & Frank 2018 (0.78): SWR content/timing modulated by behavioral state — biological substrate for control-plane gating; caveat that biology is a continuous modulator, REE implements a discrete gate.

The architecture correctly delegates value-computation to E3 rather than the hippocampal module, per ARC-007's own resolution (hippocampus doesn't compute value — Bittner 2017). **Verdict**: biology is partial, not absent — genuinely load-bearing lit exists, but it does not cover the specific mechanism (downstream valuation of injected candidates) that the decisive criterion (C3) tests. The failure targets exactly the part biology hasn't resolved, which is weak evidence against the whole claim.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened, but with a competing implementation-gap explanation | test targets the right claim, but two evaluator subcomponents are unwired |
| Biological reference | partial | strong lit for phenomenology; explicitly silent on the downstream-valuation mechanism C3 tests |
| Dependency prerequisites | immature | ARC-007 demoted 2026-07-25 on the same E3-routed-selection seam |
| Implementation completeness | partial (code-verified) | reality_scorer, harm_cost_fallback_scorer never trained anywhere in ree_core |
| Environment adequacy | adequate | hazard-density calibration correctly ruled out as the C4 bottleneck |
| Measurement adequacy | under-instrumented / confounded | nav_bias override newly extended into eval — dilutes exactly the condition-dependent signal C1/C2/C3 need |
| Integration adequacy | partially coupled, by design tension | hippocampal CEM elite-selects on residue-terrain only (architecturally intentional); E3's downstream scoring is unfinished |
| Scale/capacity | unknown | not clearly implicated |

## 5. Learning extracted

1. `score_trajectory`'s fallback path carries two nn.Sequential heads never touched by any loss anywhere in `ree_core` — code-verified by exhaustive grep.
2. `nav_bias` forced-random override was newly extended into the eval loop in 190a — a measurement-design change, not a pure power increase, and a plausible driver of C1's PASS->FAIL collapse including a sign flip on repeated seed 123.
3. ARC-007 (a direct MECH-022 dependency) was independently demoted 2026-07-25 on the same E3-routed-selection substrate seam — convergent signal across two claims.
4. Existing targeted lit review grounds the general phenomenology but explicitly disclaims coverage of the downstream-valuation mechanism C3 tests.

## 6. Routing (confirmed)

**Reclassified per user confirmation**: `epistemic_category: competence_implementation_gap` (rejecting the manifest's own `retire_ree_claim`), `evidence_direction: non_contributory`. Routing: `/implement-substrate` — `action: create` (no existing `substrate_queue.json` entry covers this gap). Train (or route out) `reality_scorer`/`harm_cost_fallback_scorer` before further MECH-022/ARC-007 evidence through this scoring path is treated as decisive. Secondary note for whenever a retest is queued: `/queue-experiment` should preserve full condition-dependence in eval (increase `eval_episodes` rather than applying `nav_bias` in eval, exactly as V3-EXQ-190's own manifest originally recommended: "increase nav_bias **or** eval episodes" — 190a did both, when only the latter is signal-preserving).

`pending_retest_after_substrate: true`. `severity: corrupting` (contaminates every score, both conditions, whole run), `substrate_paths: ["ree_core/predictors/e3_selector.py::compute_reality_cost", "ree_core/predictors/e3_selector.py::compute_harm_cost_fallback"]`.

**Step 9b**: no existing hypothesis-space qid names MECH-022; no `fanout_recommendation` emitted. Registration deferred.

## 7. Evidence quality note (for governance to apply)

> V3-EXQ-190a (2026-08-09): well-powered successor to V3-EXQ-190, criteria met 2/5 (C1/C2/C3 FAIL, C4/C5 PASS). NOT accepted as a demotion-grade FAIL despite the manifest's own self-declared Decision: retire_ree_claim. Two implementation/measurement issues undermine a fair test: (1) E3Selector.score_trajectory()'s fallback path carries two untrained scoring subnetworks (reality_scorer, harm_cost_fallback_scorer -- verified never touched by any loss in ree_core), contaminating both the C3 metric and, very likely, action selection itself in both conditions; (2) 190a newly extends the nav_bias forced-random-action override into the eval loop (absent in V3-EXQ-190), diluting the condition-dependent behavioral signal -- plausible cause of C1's collapse from clean PASS (190) to near-zero/negative including a sign flip on repeated seed 123. Existing targeted lit review (targeted_review_connectome_mech_022, 3 entries, 0.72-0.78 confidence, all supports) grounds the general hippocampal-replay-injection phenomenology but explicitly does not cover the downstream-valuation mechanism C3 tests. Convergent with ARC-007's 2026-07-25 leg-scoped demotion on the same E3-routed-selection seam -- treat as a shared substrate signal, not two independent falsifications. Reclassified competence_implementation_gap/non_contributory, pending_retest_after_substrate: true. Routed to /implement-substrate to complete E3's scoring heads before further evidence on this seam is adjudicated.
