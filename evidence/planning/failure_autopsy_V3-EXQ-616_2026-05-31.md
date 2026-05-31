# Failure Autopsy -- V3-EXQ-616 (Q-054 entropy_bias_scale sweep on MECH-341 B_only isolation)

Generated UTC: 2026-05-31T18:01:45Z
Scope: cluster member (V3-EXQ-616 primary; V3-EXQ-614a ARM_0_B_only + V3-EXQ-569e Pathway A vs B as cluster siblings)
Status: confirmed (interactive AskUserQuestion gate 2026-05-31T18:08Z)

---

## 1. Facts (no interpretation)

- **Run:** `v3_exq_616_q054_mech341_entropy_bias_scale_sweep_20260531T141508Z_v3`
- **Outcome:** FAIL. Manifest `evidence_direction: weakens`, per-claim `Q-054: mixed`, `MECH-341: mixed`. `interpretation_label: FAIL_no_floor_under_max_swept_scale`. `load_bearing_floor_scale: null`.
- **Design:** 4 arms x 3 seeds (12 total); single-axis sweep of `e3_diversity_entropy_bias_scale in {1.0, 2.0, 4.0, 8.0}`; all other substrate IDENTICAL to V3-EXQ-614a ARM_0_B_only (SP-CEM OFF, MECH-313 OFF, V_s OFF, MECH-341 ON both sub-flavours).
- **Pre-registered Rung-1 PASS rule:** per-arm majority of seeds (>=2/3) with `n_unique_selected_classes >= 2`, `selected_class_entropy_nats > 0.3`, `frac_pre_ge2 >= 0.5`.
- **Per-arm result:** ALL 4 arms `majority_rung1_pass = false`. Every arm: `mean_selected_class_entropy_nats = 0.000`, `mean_n_unique_selected_classes = 1.00`.
- **Per-seed result (load-bearing):** seed 42 -> class 0, seed 43 -> class 2, seed 44 -> class 4. **Bit-identical across all 4 scale arms**: `n_p1_ticks` matches per-seed across scales (seed 42 = 11806 ticks every arm; seed 43 = 11423; seed 44 = 358); committed_classes counts identical; selected_classes counts identical. `frac_pre_ge2 = 0.0` on every seed.
- **Seed 44 truncation:** 358 ticks across all 4 arms (vs ~11k for seeds 42/43). Same truncation point bit-identically; not scale-dependent.
- **Machine:** ree-cloud-4.

## 2. Claim-layer map

- **Q-054 (open question, registered 2026-05-25):** "What is the minimum trajectory-class diversity floor (Rung 1 first_action_entropy threshold) required for the ARC-062 context discriminator to learn a reliable discriminative cut?" Status: `open`, conf=0.0 by construction, `implementation_phase: v3`, depends_on [ARC-065, ARC-062, MECH-313, MECH-314]. Operationalised here as the scale-axis sub-question: "At what entropy_bias_scale does B_only produce Rung-1 diversity?" -- a strictly narrower instantiation of Q-054, not Q-054 itself.
- **MECH-341 (e3 score-diversity preservation):** Status: `candidate`, `v3_pending: true`, depends_on [ARC-065, ARC-033, SD-003, INV-076]. V3-EXQ-614a (2026-05-30 PASS) stamped `evidence_direction_per_claim[MECH-341] = supports` for load-bearing-in-stack via C2+C3 (ablate_B necessity + ALL_ON Rung-1). C1 R2.c (B_only Rung-1) was already false on 614a; Q-054 sweep here was the script-grid's PASS-via-C2+C3 follow-up.

**Did the experiment test the claims under conditions where they could express themselves?** NO at both levels. (a) The candidate pool entering MECH-341 was monostrategic on every tick (`frac_pre_ge2 = 0.0`): scoring-layer rescue is structurally impossible when the candidate pool contains one class. (b) The scale axis cannot be evaluated when the substrate it operates on never presents inputs the knob could re-rank.

## 3. Biological-reference triage

- **Closest mechanism:** striatal/cortico-striatal action evaluation -- scoring/winner-take-all over a candidate pool *proposed by* cortex/hippocampus. The biological substrate distinguishes proposal (Layer A in the plan doc) from selection (Layer B), with explicit upstream-cortical contribution to option diversity.
- **Is formal-definition import?** Partial. `entropy_bonus` is a Shannon-information scoring penalty (formal import); `stratified_select` is a class-balanced sampling primitive (engineering construct). Lit anchor exists for the upstream MECH-341 cluster (`targeted_review_arc_065_behavioral_diversity_generation` + `targeted_review_rl_diversity_monostrategy_curriculum` + `targeted_review_zebrafish_sleep_behavioral_diversity` under `REE_assembly/evidence/literature/`). No dedicated Q-054 / MECH-341 biology pull -- but the plan doc's R2 / R_X.b decision rules already commit to the layered reading.
- **Dependency-absence signature?** YES. Biological scoring-layer dysfunction in the presence of impoverished cortical proposal produces exactly this phenotype: deterministic single-class selection regardless of selection-side gain. This matches what would happen biologically if Layer A / Layer D (proposal / representation diversity) were absent. The FAIL therefore **strengthens** the prerequisite reading rather than falsifying MECH-341.
- **Divergence reading:** non-load-bearing. The mechanism is biologically licit; the test-bed substrate is missing an upstream dependency the biology would require.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear -> intact | Neither claim was tested under conditions where it could express itself. Q-054 question unanswered; MECH-341 not weakened. |
| Biological reference | partial | Closest mechanism (striatal scoring) requires upstream proposal diversity; biology supports a layered model where Layer B cannot rescue Layer A collapse. Lit-pull anchors exist for the broader cluster. |
| Developmental / dependency prerequisites | missing | Pre-MECH-341 candidate pool monostrategic (`frac_pre_ge2 = 0.0`); the SD-056 amend (E2-world-forward per-candidate signal preservation; multistep contrastive h=5 + per-step norm clamp ratio=2.0) is the named prerequisite that V3-EXQ-614b will measure. |
| Implementation completeness | complete | `e3_diversity_entropy_bias_scale -> clamp(min=-scale, max=scale)` plumbing verified in `ree-v3/ree_core/predictors/e3_score_diversity.py:198` and `e3_selector.py:840`. Bit-identical-across-scales is NOT a plumbing bug -- it reflects identical inputs producing identical outputs. |
| Environment adequacy | adequate | SD-054 bipartite reef env unchanged from 614a; same seeds; not a test-design flaw at the env layer. |
| Measurement adequacy | adequate | Pre-bias `frac_pre_ge2` instrumented; the metric correctly surfaces that the candidate pool is monostrategic. The metric is what makes the diagnosis legible. |
| Integration adequacy | isolated -> collapses | Layer B in isolation cannot rescue upstream Layer A / Layer D collapse; this is the integration property the layered plan-doc model predicts. |
| Scale / capacity | adequate | 30 P0 + 60 P1 episodes per seed; seed 44 truncation (358 ticks) is a substrate-survival artifact bit-identical across the swept axis, not a budget shortfall. |

**Recommended epistemic_category:** `substrate_ceiling` (test-bed substrate cannot present diversity to the selection layer being tested; the substrate gap is upstream at Layer A / Layer D, not at Layer B).

## 5. Cluster pattern -- B_only / single-pathway isolation -> monostrategy on pre-SD-056-amend substrate

| Experiment | Claim | Failed criterion | Discrimination criteria | Read |
|---|---|---|---|---|
| V3-EXQ-616 (this) | MECH-341, Q-054 | Rung-1 (all 4 arms) | `frac_pre_ge2 = 0.0`; bit-identical per-seed outputs across scale=1/2/4/8 | Scoring-layer cannot rescue empty candidate pool |
| V3-EXQ-614a ARM_0_B_only | MECH-341 | C1 R2.c isolation | C2 (ablate_B necessity) + C3 (ALL_ON Rung-1) both true | MECH-341 load-bearing in stack, not in isolation |
| V3-EXQ-569e Pathway A vs B | ARC-065, MECH-341 | Pathway dissociation | Routed to /failure-autopsy 2026-05-31 (verdict INSTRUMENTATION_FAILURE; SD-056 multistep amend authored) | Same root cause: per-candidate z_world bit-identical after one E2 step |

**Convergent shape (load-bearing reading):** these are NOT three independent bugs. They are one structural property of the pre-SD-056-amend substrate -- the E2-world-forward step collapses per-candidate z_world to bit-identity, so any single-pathway isolation arm (B_only, Pathway A vs B) receives a monostrategic candidate pool and cannot demonstrate the layer it isolates. The full-stack ALL_ON arm masks this because Layer C (noise) + Layer D (V_s) inject diversity outside the collapsed per-candidate signal.

**Planning decision the cluster forces:** V3-EXQ-614b (queued 2026-05-31T12:32Z; SD-056-amended re-run of 614a 3-arm falsifier) is the single load-bearing retest for the whole cluster. If 614b PASSes C1 on the SD-056-amended substrate, the cluster's substrate-ceiling reading is *confirmed and resolved*: Q-054 sweep can be re-issued as V3-EXQ-616a on amended substrate; MECH-341 v3_pending clears. If 614b also FAILs C1, the cluster's substrate-ceiling reading escalates to a substrate-redesign decision (script-grid's "stratified_temperature default + A-vs-B partial-redundancy probe"; amend the existing MECH-341 substrate_queue entry).

## 6. Learning extracted

1. **The bit-identical-across-scales observation is the load-bearing diagnostic signal.** Per-seed `n_p1_ticks` identical across an 8x scale range -- this is only possible if the swept knob produces zero argmax-flipping effect, which is only possible if either (a) the bonus magnitude is dwarfed by the score gap and saturated at every scale (the V3-EXQ-611c C2 finding amplified), or (b) the candidate pool is monostrategic so no bonus could flip anything. The `frac_pre_ge2 = 0.0` evidence settles it as (b).
2. **Layer-B isolation arms presume multi-class candidate pools that the pre-SD-056-amend substrate doesn't deliver.** Any scoring-layer ablation arm is uninformative until the upstream proposal pathway provides diversity.
3. **MECH-341 is not falsified.** 614a C2+C3 PASS is preserved as load-bearing-in-stack supports. The 616 FAIL is structurally consistent with that reading -- scoring-layer mechanism, no candidate pool to score over -> no behavioural effect.
4. **The script's interpretation grid was correct as authored** but underspecified the substrate-ceiling reading: the FAIL_no_floor row routes to "substrate revisit (stratified_temperature default + A-vs-B redundancy probe)", which is the right *if 614b also fails C1* recovery path. On the SD-056-amended substrate (614b PASS C1) the same row is the wrong routing; the right routing is "re-issue Q-054 sweep on amended substrate".
5. **Seed 44 truncation at bit-identically 358 ticks across all 4 scale arms** is an orthogonal substrate-survival artifact independent of the swept axis; not addressed by this autopsy.

## 7. Repair pathway -- HOLD routing on V3-EXQ-614b outcome

**Primary (recommended).** Hold Q-054 follow-up until V3-EXQ-614b lands. Two contingent branches:

- **V3-EXQ-614b PASSes C1** on SD-056-amended substrate -> `/queue-experiment` V3-EXQ-616a (re-issue this Q-054 sweep on amended substrate; same 4-arm scale sweep, same acceptance grid, same interpretation grid; supersedes V3-EXQ-616).
- **V3-EXQ-614b FAILs C1** -> `/failure-autopsy` on 614b (cluster successor) + amend MECH-341 substrate_queue entry to add stratified_temperature default + A-vs-B partial-redundancy probe (the script-grid's substrate-revisit row). This autopsy pre-fills the substrate_queue amend recommendation in `recommended_substrate_queue_entry.action = amend` so /governance can apply it directly if 614b FAILs.

**Not now.** No substrate_queue write today (the user explicitly chose "hold Q-054 follow-up; re-issue as 616a only if 614b passes C1"). No /lit-pull (existing cluster anchors cover the layered model). No /diagnose-errors (no crash; ran to completion).

## 8. Recommended evidence_quality_note (governance applies; do not write here)

> V3-EXQ-616 (2026-05-31T14:15Z) FAIL_no_floor_under_max_swept_scale on entropy_bias_scale in {1,2,4,8} for MECH-341 B_only isolation. Per-seed n_p1_ticks AND selected-class outputs bit-identical across all 4 scale arms (seed 42 -> class 0, 43 -> class 2, 44 -> class 4; 11806 / 11423 / 358 ticks identical across scales), confirming the swept knob has zero downstream effect when the upstream candidate pool is already monostrategic. frac_pre_ge2 = 0.0 on every seed-arm: the pre-MECH-341 pool never contains >=2 classes, so the Layer-B scoring substrate has nothing to stratify over. Same root cause as V3-EXQ-569e Pathway A vs B FAIL and the SD-056 amend (E2-world-forward per-candidate signal collapse). Does NOT weaken MECH-341 (614a C2+C3 PASS stamped supports / load-bearing-in-stack; that reading preserved). Q-054 scale-axis sub-question is uninformative on pre-SD-056-amend substrate; broader Q-054 question (minimum class-diversity floor for ARC-062) unanswered because the test-bed couldn't surface diversity at all. Recommended `evidence_direction_per_claim: {Q-054: non_contributory, MECH-341: non_contributory}` + `pending_retest_after_substrate: true` keyed to V3-EXQ-614b (SD-056-amended re-run, queued 2026-05-31T12:32Z). On V3-EXQ-614b PASS_C1 -> re-issue Q-054 sweep as V3-EXQ-616a on amended substrate. On V3-EXQ-614b FAIL_C1 -> amend MECH-341 substrate_queue entry for stratified_temperature default + A-vs-B redundancy probe. Cluster siblings: V3-EXQ-614a ARM_0_B_only, V3-EXQ-569e Pathway A vs B. Recommended epistemic_category: substrate_ceiling.

## 9. Narrow-supports check (paired with non_contributory recommendation per skill rule)

- **MECH-341 supports** carrying weight as of 2026-05-31 morning: V3-EXQ-614a C2+C3 only. Single-pathway "load-bearing-in-stack" reading. **`narrow_supports_flag: true`** -- the supports tag is one ALL_ON arm on the pre-SD-056-amend substrate; no replication. Governance must preserve `MECH-341.v3_pending=true` until V3-EXQ-614b reproduces 614a's C2+C3 PASS on the amended substrate (per the 2026-05-31 midday governance note this is already the policy). If 614b PASSes C1, MECH-341 v3_pending clears with a non-narrow supports profile.
- **Q-054 supports:** none (open question, conf=0.0). No narrow-supports concern.

This pairing satisfies the skill rule that any non_contributory + substrate-ceiling recommendation must include an explicit narrow-supports check.

## 10. Routing decision (confirmed)

- per-claim direction: `non_contributory / non_contributory` + `pending_retest_after_substrate: true`
- primary routing: HOLD on V3-EXQ-614b; re-issue as V3-EXQ-616a only on 614b PASS_C1
- cluster framing: YES (cluster member with V3-EXQ-614a ARM_0_B_only + V3-EXQ-569e Pathway A vs B)
- substrate_queue write today: NO (`recommended_substrate_queue_entry.action: none` pending 614b)
- contingent substrate_queue write on 614b FAIL_C1: amend MECH-341 (`stratified_temperature default + A-vs-B redundancy probe`)
