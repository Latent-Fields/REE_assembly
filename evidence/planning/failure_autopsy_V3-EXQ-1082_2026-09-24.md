# Failure autopsy: V3-EXQ-1082 (SD-PP-B5 re-validation at alpha_world 0.9 on a live battery)

- **run_id**: `v3_exq_1082_sdppb5_alpha09_live_battery_revalidation_20260924T045004Z_v3`
- **queue_id**: V3-EXQ-1082 · **outcome**: FAIL · **purpose**: diagnostic · **claim_ids**: `[]`
- **self-route**: `margin_lowers_action_read` (FAIL-a), `off_arm_premise: off_reads_action`
- **bears_on**: `SD-PP-B5-z-world-per-step-displacement-range`, `SD-PP-B10-zworld-encoder-action-displacement`, MECH-573, MECH-574, SD-008
- **Status**: `awaiting_human_confirmation`. This is a STAGING draft, written by a subagent of the /governance session `governance-20260924-workset`. No claim was opened, nothing was committed, the hypothesis registry was not written, and no regeneration was run.
- **Generated**: 2026-09-24T06:19:09Z · **Red-team (Step 7c)**: CONTESTED (narrow), cross-model (fable; session model Opus 5.5). Four findings were adopted.

## Bottom line

The self-routed label holds, but it answers the smaller question. The larger finding comes from the **OFF arm**. At SD-008's operating point (alpha_world 0.9), on a live battery, the world_forward head with no lever applied already reads its action:

- d_act is 0.341/0.216/0.227, with CI lower > 0 on 3/3 seeds. That is 64-81% of the action-aware ridge ceiling.
- It beats copy-the-input: skill_vs_identity is +0.35/+0.22/+0.21.

SD-PP-B5's margin remedy targets an action-blind head, and no such head exists at this operating point. The margin never raises the read, and it destroys reconstruction at margin >= 0.05.

**Verdict.** The FAIL is a **genuine negative for the margin lever**. It is also **a premise failure for the lever's purpose**: it cures a defect that does not reproduce at alpha 0.9 on a live agent. It is **not an instrument artefact**:

- All 7 preconditions are met.
- The positive control is live on 3/3 seeds.
- The null is analytic.
- The battery is stationary.

Two caveats narrow the "lowers" sub-label. The drop at M001 is not attributed to the margin, and the drop at M005 is confounded with reconstruction loss.

## 0. Premise audit (re-measured before any diagnosis)

- **Brief premise: "predecessor V3-EXQ-1073".** Corrected. The manifest names V3-EXQ-1079 as its predecessor and cites `failure_autopsy_V3-EXQ-1079_2026-09-23` as its autopsy. The lineage runs as follows:

  | Run | Role | alpha_world | Battery |
  |---|---|---|---|
  | 1073 | originating (MECH-572) | 0.3 | LIVE |
  | 1075 | margin ladder | 0.3 | post-death |
  | 1079 | alpha probe, OFF arm only | 0.3 and 0.9 | post-death |
  | 1082 | this run | 0.9 | live (done-handling ported from 1073) |

- **Label reproduced.** All 15 d_act values and all 12 lifts were recomputed from `per_row_se_true` / `per_row_se_swap_mean` and match to 4 dp. The red-team reproduced them independently.
- **Stale record found.** SD-PP-B5's `validation_outcome` (governance, 2026-09-23) and section 6 of the 1079 autopsy both say 1073 collected its battery after the agent died, without reading `done`. That is **false for 1073**. Both `_sample_probe_battery` and the P0 loop unpack `done` and reset. The post-death defect applies to 1075 and 1079 only. A `governance_flag.py raise --flag-type stale_note` is owed.

## 1. Facts

**Dry-run gate.** `check_dry_run_citations.py` was run over the 1082 run_id plus V3-EXQ-1082 and V3-EXQ-1073: 0 dry, exit 0. The smoke run went to scratch and is not in evidence. Excluded ids: none.

**Recording.** All the always-core fields are present:
- `recording_schema` rec/v1
- `substrate_hash`, with `substrate_commit` 5f3b27a (clean, stable across the run)
- machine ree-cloud-2, `machine_class`
- `elapsed_seconds` 142.8
- full `config`
- `seeds` [42, 123, 456]
- per-row errors for every cell

**Design.** 5 arms x 3 seeds:
- Arms: OFF, plus interventional margin 0.01, 0.05, 0.10 and 0.50.
- Training: 3600 P0 steps. Only `agent.e2` is optimised, so the encoder stays untrained and is equal across arms.
- Battery: 512 rows, collected by a fresh OFF-config agent with its own rng, so it is bit-identical across the arms of a seed.
- DV: `d_act = (SSE_swap - SSE_true)/(SSE_swap + SSE_true)`, with an analytic null of 0. Lift is `d_act(ON) - d_act(OFF)`, CI'd by a paired row bootstrap.
- Training path: torch-RNG-free (the env uses numpy `default_rng`; sense and world_forward are deterministic), so the margin gradient is the only difference between arms.

**Per-seed lifts vs OFF** (all 12 CIs are wholly < 0):

| seed | OFF d_act [CI] | M001 | M005 | M010 | M050 |
|---|---|---|---|---|---|
| 42 | 0.341 [0.323, 0.360] | -0.177 | -0.173 | -0.246 | -0.326 |
| 123 | 0.216 [0.203, 0.229] | -0.055 | -0.094 | -0.131 | -0.211 |
| 456 | 0.227 [0.216, 0.238] | -0.046 | -0.054 | -0.135 | -0.217 |

**Reconstruction and head health:**

| rung | A4 MSE(ON)/MSE(OFF) | model_r2 (range over seeds) | head action separation (L2) |
|---|---|---|---|
| OFF | 1 | 0.48 to 0.56 | 0.017 to 0.024 |
| M001 | 1.07 to 1.25 (guard ok) | 0.37 to 0.45 | 0.016 to 0.024 |
| M005 | 3.1 to 4.2 | -1.13 to -0.57 | 0.064 to 0.079 |
| M010 | 9.3 to 11.8 | -5.1 to -3.8 | 0.115 to 0.131 |
| M050 | 187 to 202 | -104 to -82 | 0.53 to 0.54 |

Transition L2 on the battery is 0.021-0.024, and rms_dz_per_dim is 0.0068-0.0078. Mean margin loss is 6-8e-7 at M001 and 1.5-1.8e-5 at M005. The hinge still gets satisfied quickly, but its gradient is scale-free, so the size of the loss value says nothing about how much it steered training.

**The OFF arm is the key result:**
- It reads its action: d_act CI > 0 on 3/3, against an untrained-head floor of |d_act| < 0.003.
- The true action beats the four alternatives on 94.5/91.4/97.5% of rows.
- It is stationary: per-64-row-block d_act is 0.28-0.44, 0.195-0.238 and 0.188-0.274 for the three seeds.
- skill_vs_identity is +0.349/+0.219/+0.215.
- model_r2 is 0.557/0.479/0.486, against persistence_r2 of 0.320/0.332/0.346. The persistence status reads `ready` on 3/3.

**Criteria:**
- C1 (load-bearing), "margin raises the action read": 0/3 at every rung.
- C2, "bought by reconstruction": 0.
- C3, "excluded on every rung": 3.

With all preconditions met, the verdict is FAIL-a, and the label is `lowers` because every rung shrinks on at least 2 seeds.

## 2. Claim layer

There are no claim_ids, by design. This run bears on MECH-573, MECH-574 and SD-008 through the SD-PP-B5 entry. No claims.yaml write is recommended (`per_claim_recommendation: {}`).

Two things this run does to neighbouring work:

- **MECH-573 (readability).** Its readability premise, as characterised at alpha 0.3, is not reproduced at 0.9 on a live battery. That is recorded here, not adjudicated.
- **SD-PP-B10.** Its own hint ("do not build before rank 1 runs; may dissolve the premise") is now largely borne out for the head-read question.

## 3. Biological-reference triage

The closest mechanism is the cerebellar / efference-copy forward model (Wolpert, Miall & Kawato; the Frith/Shergill comparator behind SD-031). It learns the consequence of the specific command from action-specific prediction error.

The SD-013/SD-PP-B5 hinge, `max(0, m - ||f(z,a) - f(z,a_cf)||)`, is a formal import from contrastive metric learning, and it differs in two ways:

- It is **scale-unaware**. At alpha 0.9 the head's own separation is 0.017-0.024 L2, so any m >= 0.05 imposes 2-25x the separation that physically exists.
- It is **direction-agnostic**. It rewards separating any pair of actions, including wall-bump pairs whose true outcomes are identical.

A biological forward model separates commands only as far as the world does.

The biology also supports SD-008: a representation smeared below the action timescale hides action consequences. That is the 0.3-vs-0.9 contrast, though here it rests on cross-run evidence.

Literature status is partial:
- `targeted_review_e2_forward_model_action_divergence` (ML-heavy)
- `targeted_review_efference_copy_small_signal_gain`
- `targeted_review_sd_008`
- `targeted_review_sd_031`

No /lit-pull is owed for routing; this run moved the premise, not the form.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim-free |
| Biological reference | partial | the margin is a formal import; separating by forward-model PE is the biological route |
| Prerequisites | present | 7/7 preconditions; PC live 3/3 |
| Implementation | complete | margin live on about 30% of steps; separation tracks the margin |
| Environment | adequate | live, stationary; rows come from the first ~20 steps of a random-policy life, on an untrained encoder |
| Measurement | adequate / partial | verdict secure (12/12 negative); M001 lowering unattributed (the row bootstrap carries no training variance); M005 lowering confounded with MSE blow-up; d_act `reads_action` is not head-health guarded (M050 "reads" at model_r2 -104) |
| Integration | coupled | dose moves the DV on 3/3 seeds, secure at M010/M050 |
| Scale | adequate | 3 seeds; no within-arm perturbation replicate |

**Failure location (GOV-FAILLOC-1): MIXED.** Two buckets apply:
- **MECHANISM**: the margin remedy is ineffective and harmful.
- **MEASURES-partial**: the "lowers" sub-label.

It is not chargeable to REE, because the untouched head reads its action at the SD-008 operating point.

## 5. Epistemic category

`standard`, with `non_contributory` evidence (claim-free diagnostic). The free-text failure mode is `remedy_premise_not_reproduced_at_operating_point + margin_mis_scaled`.

## 7. Learning and routing

The node class is `complex (probe-gated)` narrowing to `puzzle (known rules)`: one fact is missing, the inverted-action-map ratio on the OFF head at 0.9.

**Learning extracted:**
1. **A dependency is strengthened.** SD-008's alpha >= 0.9 floor is load-bearing for the head's action read. The attribution rests on cross-run evidence (1073 at 0.3 vs 1082 at 0.9, plus 1079).
2. **The margin form's negative is now clean at the operating point.**
3. **There are measurement gaps.** The `reads_action` status has no head-health guard, and there is no training-variance control.
4. **There is a stale record** (the 1073 post-death text).

**Routing (recommended; reported, not spawned):**
1. **/queue-experiment**: an OFF-only probe on a live battery, 3 seeds, with alpha **0.3 and 0.9 as two arms in one run**.
   - Readouts: the inverted-action-map battery ratio, with a bar that excludes the degenerate ~1.0, next to d_act and skill_vs_identity.
   - Optional: a null-perturbation OFF replicate, to size the training variance of d_act.
   - Reuse: 1079's `_make_env(invert_action_map=True)` and `action_sensitivity_gate.readiness_verdict`.
   - Declared null: the ratio stays <= ~1.0 at 0.9 even though d_act > 0.
   - Consequence of a pass: the V3-EXQ-1073 MECH-572 contradiction design, re-posed at alpha 0.9, becomes posable.
2. **/governance**: amend SD-PP-B5 (below), and raise the stale_note flag for the 1073 post-death text.
3. **Refused on this evidence:**
   - the (0.01, 0.05) margin re-rung
   - the InfoNCE leg (SD-056 form)
   - the encoder-displacement build

   All three presuppose an action-blind head, and no such head exists at the operating point on the axes measured.

**Draft evidence_quality_note (exact):** see `recommended_evidence_quality_note` in the JSON.

### Recommended SD-PP-B5 substrate_queue change (`action: amend`)

- `status` STAYS `implemented_validated_negative`, and `ready` STAYS false.
- SET `status_phase: probe_gated`; the field is currently absent on the entry.
- `node_class` STAYS `complex (probe-gated)`.
- `severity` STAYS `corrupting`. This run re-confirms it: every ON rung, M050 included, returns `reads_action` on a destroyed head.
- ADD `ree_core/predictors/e2_fast.py::compute_world_interventional_loss` to `substrate_paths`.
- APPEND the `implementation_hint_append`, `title_correction_2026_09_24` and `validation_outcome_append` texts from the JSON. The validation_outcome text includes the correction that 1073 read `done`.
- APPEND the 1082 `failure_record` item (`resolved: open`).

Dispositions on the prior failure records:
- **1079 → `resolved`.** All three conjuncts of its target are met.
- **1075 → `superseded`.** The same manipulation was re-measured cleanly.
- **1073 → left `open`,** with a note. Only clause (3) of its target (skill > 0) is met. Clauses (1)-(2), the inverted-rule readouts, are still owed at 0.9.

### Brake and recurrence

- **Re-derive brake:** n/a (claim-free).
- **GOV-DIAG-1:** the full-token chain `SD-PP-B5-z-world-per-step-displacement-range` counts 1 without this artifact and 2 with it. Reconciling 1075's short token `SD-PP-B5` would make it 3. The chain is converging on an answer, not circling one floor. Reconciling the token is governance's decision.
- **Granularity-debt recurrence trigger: does NOT fire.** `claim_ids` is empty, and `granularity_debt_cluster.py MECH-573` finds 0 tagging targets.

## 7b. Mechanical checks

- **C7 fired** on `persistence_r2`, which is identical across arms. **Dismissed**: it is copy-the-input on an arm-invariant battery, so it cannot vary by construction. It is cited only as the baseline next to model_r2, never as a discriminator.
- **C1/C2/C3/C5** were inapplicable (the artifact is claim-free, and the .md did not exist when the checks ran).
- **C1 was checked by hand:** no queued item or driver covers the probe. The queue holds only V3-EXQ-1067. V3-EXQ-1081 runs at 0.9 but has no inverted-map readout.

## 7c. Red-team (fable, cross-model): CONTESTED, narrow

The FAIL-a verdict, the category, the substrate status and the routing all stood. Four findings were adopted:

1. **M001 attribution.** The draft said the margin "lowers at every rung" and used M001 to call the untested interval unpromising, while its own measurement row called M001 unattributed. Both claims are hedged now. The confirmer is a null-perturbation OFF replicate.
2. **Alpha attribution.** The draft called the defect an "operating-point artefact", but that inference is cross-run. It has been reworded, and an alpha 0.3 arm has been added to the probe.
3. **1073 → superseded was over-reach.** The record is now left `open`.
4. **Stale 1073 post-death text.** This was verified against the 1073 driver.

The red-team also verified the following:
- All d_act values recompute from the per-row arrays.
- d_act > 0 cannot come from a shared bias, EMA dynamics or identical-outcome action pairs; each of those pushes d_act toward 0.
- `reads_action` can fail.
- The probe is not already covered by any driver or queued item.

## 9b. Hypothesis ledger: drafted only (`hypothesis_space_ledger_pending` in the JSON)

These edits apply to qid `zworld_action_readability_lever`. Its `growth_restriction` is empty, so there is no STOP.

- **Mode B.** `H-margin-form` gains resolving run V3-EXQ-1082 and stays `alive`: the interval is still unsampled, and the bar is not met.
- **Mode A / 3a labelled growth.** `H-operating-point` is added, on axis `representation-update-rate`, and resolved `confirmed` on the d_act/skill axes.
  - Pre-registration source: `failure_autopsy_V3-EXQ-1079_2026-09-23.json`.
  - Git witness: REE_assembly 18a3306a5bf, committed 2026-09-23T18:26Z. The 1082 driver 5f3b27a carries the off_arm_premise split and was committed at 04:43Z. The run resolved at 04:50Z.
  - `initial_frozen_count` goes from 3 to 4; `initial_frozen_count_at_registration` stays 3.
- **Mode D.** An `h_other_event` is recorded: the lever-only partition omitted the operating point. Response: `partition_expansion`.
- **`decision.decidable` stays false.** The live_gate readout, the inverted-map ratio, is unmeasured at 0.9.
- **Step 8 alternative.** The new leg could instead be registered under a new qid, because the question asks about a *training-time lever* and this leg is an operating point.

## 8. Owed at the interactive gate

Confirm or revise each of these:
- the verdict and the SD-PP-B5 amend;
- the 1073 record left `open`;
- the stale_note flag;
- ledger growth vs a new qid;
- whether to reconcile the GOV-DIAG-1 token.
