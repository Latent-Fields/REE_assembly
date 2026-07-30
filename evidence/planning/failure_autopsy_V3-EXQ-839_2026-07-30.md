# Failure Autopsy: V3-EXQ-839 (SD-084 mid-execution reachability)

**Generated:** 2026-07-30T06:31:32Z
**Scope:** single
**Status:** confirmed (interactive gate cleared with user, 2026-07-30)
**Trigger:** chip `chip-20260730-autopsy-839`, spawned by the 2026-07-29/30 `/governance` cycle -- this diagnostic PASS routes SD-084's readiness decision but had no confirmed or in-flight autopsy.

## Why this needed an autopsy despite being a clean PASS

The manifest self-reports `evidence_direction: non_contributory` with `claim_ids: []` -- per this skill's Step 1 scoping rule, a non-standard `evidence_direction` value is itself a diagnosis-pending signal, independent of whether the pipeline's `precondition_unmet`/`vacuous_pass` indexer flag fired (it did not; the run appears in `pending_review.md`'s "Unclaimed manifests" table, not the "Diagnostic adjudication required" table). SD-084 is a `candidate_substrate_landed` design-decision claim whose own `implementation_note` states explicitly: *"Result NOT YET IN: nothing here may be read as validated until V3-EXQ-839 lands a manifest."* This is exactly the decide-to-build-routing shape CLAUDE.md's governance protocol requires a confirmed autopsy for before the downstream decision (here: trusting that MECH-321's R4 mid-execution mechanism is genuinely reachable, unblocking a successor evidence experiment) is acted on.

## 1. Facts reconstruction

**Target:** `v3_exq_839_sd084_midexec_reachability_20260729T220727Z_v3` (queue_id V3-EXQ-839), outcome PASS, self-routed label `midexec_reachable_handle_validated`.

**Dry-run check (Step 2a):** `check_dry_run_citations.py` -- 1 clean, 0 dry. Not a smoke; `elapsed_seconds: 1580.234` (~26 min, full budget). `validate_recording.py` -- OK, 0 always-core gaps (recording standard fully satisfied: `substrate_hash`, `machine_class`, `config`, `seeds` all present).

**The question (from the driver's own docstring, `experiments/v3_exq_839_sd084_midexec_reachability.py`):** MECH-321's R4 mid-execution decomposition hook had NEVER executed in any experiment -- not rarely, structurally: the hook requires `e3._committed_trajectory is not None` on entry to `select_action`, but `E3Selector.post_action_update`'s LAST statement unconditionally sets it to `None` every tick. V3-EXQ-830 confirmed this empirically (`decomp_n_evaluated_midexec = 0` in all 10 cells against `decomp_n_evaluated_precommit` 1862-2618). SD-084 adds a persistent handle (`_persistent_committed_trajectory`) that survives the teardown, gating the hook on the UNION of the two handles when `use_persistent_committed_program_handle=True`.

**Acceptance criterion**, taken verbatim from `failure_autopsy_V3-EXQ-830_2026-07-29.md`'s `failure_record_entry.target`: *"decomp_n_evaluated_midexec > 0 on a standard select_action -> update_residue driver loop, without hand-injected preconditions."* This is C1 below, the sole load-bearing criterion.

**Design (the load-bearing feature of this run):** natural reachability is seed-dependent -- the hook only fires on a tick following a committed MULTI-ACTION program (gate 6: `len(remaining) > 1`), and E3 commits a multi-action ARC-071 chunk only when it beats CEM-optimised candidates on raw score, with no chunk-selection-bias knob in the substrate to force it. So a zero DV has two possible causes that route to opposite conclusions: (a) SD-084 doesn't work, or (b) this seed never committed a multi-action program (no test occurred). The script separates these via **two pre-registered seed tiers**: ATTRIBUTABLE (3, 47, 71, 89 -- measured to commit multi-action programs) and NEGATIVE CONTROL (23, 53 -- measured to commit none, with pre-commit decomposition nonetheless live), plus an existential per-arm readiness precondition (`multi_action_commits_present`) so a partially-attributable arm is never swallowed into a false red.

**Measured result:**
- `total_midexec_on = 415`, `total_midexec_off = 0` -- C1 PASSES cleanly, C2 (negative control: OFF reproduces the structural zero) holds exactly.
- Attributability: 4/6 seeds per arm carried a multi-action commit (`n_on_cells_with_midexec = 4`, matching the pre-registered attributable tier exactly); the 2 non-attributable seeds (23, 53) show `midexec_off=midexec_on=0` and `action_divergence_frac=0.0` in `behavioural_delta` -- bit-identical between arms, exactly the negative-control expectation. `negative_control.expectation_held = true`, `tier_still_valid = true`.
- Readiness preconditions: both arms cleared `multi_action_commits_present` (measured 139 both arms, best cell) and `decomposition_precommit_live` (measured 1724 both arms) -- `non_degenerate: true`, `per_arm_gate.all_green: true`. No vacuous-pass pattern.
- C4 (non-load-bearing behavioural divergence): mean_divergence = 0.159375 on the attributable tier, PASSES -- the arms take different action sequences once the handle can act, as the SD-084 design doc's "not a pure diagnostic" section predicts.
- One informative internal detail, not a defect: seed 47 shows `midexec_on=134` but `decomposed_midexec_on=0` and `action_divergence_frac=0.0` -- the hook evaluated 134 times but never decided to decompose (no boundary fired on those evaluations), so no commit-latch release occurred and the action sequence stayed identical to OFF. This is consistent with the mechanism (`evaluate()` can be reached and still decide "no" every time) and is exactly why the manifest records `decomp_n_evaluated_midexec` (reachability) separately from `decomp_n_decomposed_midexec` (actual re-segmentation) -- not a design flaw.

**Self-route logic** (script `_analyse`): `substrate_not_ready_requeue` if `non_degenerate` false -> `off_path_not_structurally_zero` if C2 false -> `midexec_reachable_handle_validated` (PASS) if C1 true -> `midexec_still_unreachable_with_handle` (FAIL) otherwise. All branches correctly ordered (readiness gate first, negative control second, load-bearing criterion third); the label actually taken (`midexec_reachable_handle_validated`) is the correct one for the measured values.

## 2. Claim-layer mapping

`claim_ids: []` by design (diagnostic; weights no claim confidence). `bears_on: [SD-084, MECH-321, ARC-070, ARC-071, MECH-288]`.

- **SD-084** (design_decision, `candidate_substrate_landed`): this run is the explicit validation this claim's own `implementation_note` was waiting on. Confirmed reachable -- the claim's implementation is functioning as designed. No status/confidence field changes (this claim type doesn't carry the promotion machinery a MECH/ARC claim does), but the readiness question is now closed.
- **MECH-321** (mechanism_hypothesis, `candidate`/`v3_pending`): R4 (mid-execution phase) previously had zero experimental access at all (V3-EXQ-830). This run does not move MECH-321's confidence (`claim_ids=[]`, deliberately, per the driver's own comment: "MECH-457 deliberately not tagged" analog for R1's sibling runs) -- but it removes the substrate blocker that made R4 untestable. R1 (pre-commit phase) already has an active discrimination portfolio (V3-EXQ-816/816b/816c/820/822). R4 has none yet.
- **ARC-070 / ARC-071 / MECH-288**: infrastructure dependencies, unaffected by this run's outcome (not exercised as claims, only as substrate this experiment runs on top of).

## 3. Biological-reference triage

This is a mid-execution-reachability engineering question (does a cross-tick handle survive a per-tick teardown), not itself a test of a biological mechanism -- the biological content lives in MECH-321's own claim (Zacks 2007 event-segmentation boundary triggers; Badre & D'Esposito 2009 hierarchical control). SD-084 is enabling infrastructure for testing that mechanism's second phase; the biological triage question ("does the failure resemble a missing biological dependency") does not apply to an infrastructure-reachability run. No divergence to flag.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (N/A -- claim_ids=[]) | Run correctly weights nothing; it validates infrastructure readiness, not MECH-321's mechanism claim itself |
| Biological reference | N/A | Infrastructure-reachability question, not a mechanism test |
| Developmental / dependency prerequisites | present | MECH-321, ARC-070, ARC-071, MECH-288 all substrate-built; SD-084 built directly on top per its implementation_note |
| Implementation completeness | complete | `_persistent_committed_trajectory` set at commit entry, survives teardown, gated by `use_persistent_committed_program_handle` (default False, bit-identical OFF); contract `test_mech321_midexec_natural_reachability.py` 4/4 |
| Environment adequacy | adequate | CausalGridWorldV2 standard driver loop, no hand-injected preconditions -- exactly the acceptance criterion's requirement |
| Measurement adequacy | adequate, exemplary | Two pre-registered seed tiers with a genuine negative control that held bit-identically; existential per-arm readiness gate avoiding the V3-EXQ-785 "one red seed vacates a green arm" failure; hold-weighting explicitly triaged (C1/C4 both shown threshold-invariant to it); DV-symmetry invariance declared per the 604c rubric |
| Integration adequacy | coupled, verified | Gate (4) reads the union of both handles as designed; behavioural effect (C4) confirms the union actually changes agent behaviour, not just an inert counter |
| Scale / capacity | adequate | Small toy env sufficient for a reachability question; not a capacity-limited claim |

**Recommended `epistemic_category`: standard** (not `substrate_ceiling` -- nothing ceilinged; the mechanism reached exactly what it was built to reach). Not a recording gap (validate_recording OK). Not a measurement gap. Not a dry-run artifact.

## 5. Learning extracted

- SD-084's cross-tick handle makes MECH-321's R4 mechanism reachable exactly as designed: 415 mid-execution evaluations across the attributable tier, zero in the OFF arm and zero in both arms on the negative-control tier.
- The attributability design (existential per-arm gate + declared negative-control tier) is doing real work here, not decorative: 2 of 6 seeds per arm never tested the hook at all (no multi-action commit), and without the tiering those seeds' zeros would be indistinguishable from a genuine substrate failure.
- Reachability (C1) and actual re-decomposition (`decomp_n_decomposed_midexec`) are measurably different things -- seed 47 fires the hook 134 times without ever deciding to decompose, which is a legitimate outcome of the mechanism's own logic, not a defect in this run.
- MECH-321's R4 has a reachability floor cleared but **zero evidence on whether the behavioural effect it produces (commit-latch release, aborting a multi-action macro) is beneficial or harmful** -- C4 is explicitly non-load-bearing and the driver's own docstring is explicit that "this run adjudicates REACHABILITY only."

## 6. Repair pathway / routing

**Work-graph classification:** `complicated (buildable)` for the successor -- the discrimination-pair design pattern for R4 already has a direct precedent (R1's ARM_0/ARM_1/ARM_2 lineage, V3-EXQ-816 et al.), so this is a named build with no open scientific-design question, not a probe-gated spike.

**Routing: `queue-experiment`.** Per user confirmation (interactive gate, both questions), recommend a successor EVIDENCE experiment (new EXQ number, `claim_ids=[MECH-321]`) testing MECH-321 R4's actual behavioural/scientific claim -- whether mid-execution decomposition (aborting a stale committed macro when the region's V_s drops or a rollout boundary fires) improves task performance versus letting the macro run to completion. Design guidance for `/queue-experiment`:
- Use this run's `behavioural_delta` block (per-seed action-sequence divergence, first-divergence tick, committed-run-length delta, harm delta) as the design template, per the driver's own note: "A successor evidence experiment consumes this block instead of re-deriving it (Experimental Recording Standard sec 3c)."
- The attributable seed tier (3, 47, 71, 89) is pre-verified to produce multi-action commits at this config on this machine class; seed 47 specifically shows the hook fires but never decomposes (a useful "reachable but inert" cell to include for contrast against seeds 3/71/89 where it does decompose).
- Follow the R1 precedent's discriminative-pair shape rather than inventing a new one: an OFF arm (handle disabled, reproduces V3-EXQ-830/839's structural zero), an ON-fires-but-inert arm if separable, and an ON-decomposes arm, scored on task/harm outcome rather than on reachability counters.

**No re-derive brake applies** (claim_ids=[], no substrate_ceiling reading, first autopsy touching SD-084). **No granularity-debt trigger** (no `weakened` target). **No fanout_recommendation** (single unambiguous confirmatory result, not a discrimination between rival hypotheses). **No hypothesis-space-registry action (Step 9b)**: checked `hypothesis_space_registry.v1.json` for existing SD-084/V3-EXQ-830/839 entries -- none found; this run does not resolve a previously pre-registered fan-out leg and does not itself open a rival-hypothesis discrimination (it is a single reachability confirmation), so there is nothing to pre-register or resolve. Skipped cleanly per the skill's own instruction.

**Draft `evidence_quality_note` for governance** (informational only -- SD-084 has no confidence/status field this note would attach to beyond its `implementation_note`, which already documents V3-EXQ-839 by name pending this confirmation):

> V3-EXQ-839 confirmed (failure_autopsy_V3-EXQ-839_2026-07-30): mid-execution reachability validated cleanly (415 evaluations ON, 0 OFF, negative-control tier held bit-identically). No defect found; routing recommends a successor MECH-321 R4 evidence experiment (new EXQ, claim_ids=[MECH-321]) testing the behavioural/task effect of the now-reachable hook, using this run's behavioural_delta block as the design template.
