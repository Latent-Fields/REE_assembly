# Failure Autopsy: V3-EXQ-490k (MECH-295 modulatory-sufficiency)

- **Generated:** 2026-06-04T15:28:54Z
- **Status:** confirmed (user-confirmed disposition + routing via AskUserQuestion 2026-06-04)
- **Scope:** single (convergent with the goal-pipeline substrate-ceiling family)
- **Run:** `v3_exq_490k_mech295_modulatory_sufficiency_20260604T091944Z_v3`
- **Outcome:** PASS (probe ran), `experiment_purpose=diagnostic`, author-stamped `evidence_direction=weakens` on MECH-295
- **Predecessor:** V3-EXQ-490j (necessity test; FAILed via `approach_commit_rate` ceiling-saturation; `failure_autopsy_V3-EXQ-490j_2026-05-31`)

## 1. Facts (no interpretation)

490k is the modulatory-sufficiency successor to 490j. It uses the 490j-autopsy's **option-(c) argmin-flip probe**: at each tick where the MECH-295 cue bias `m` fires, it checks whether removing the MECH-295 contribution changes the committed argmin (`argmin(scores)` vs `argmin(scores - m)`). This metric is structurally immune to the `approach_commit_rate` ceiling that contaminated 490j.

3 arms x 3 seeds (42/7/19), 900 eval-step budget. Config = gap4_operating (drive_floor=0.9, drive_ema_alpha=1.0, goal_stream=True, use_dacc=True).

Recorded (per `acceptance` + `per_run`):

| Metric | Value |
|---|---|
| `grid_row` | `ROW_2_fires_but_never_flips` |
| `full_arm_fired_seeds` (ARM_1) | 3/3 |
| `only_arm_fired_seeds` (ARM_2 mech295-only) | 3/3 |
| `full_arm_argmin_flip_seeds` | **0/3** |
| `only_arm_argmin_flip_seeds` | **0/3** |
| per-seed `action_tv_distance` (ARM_1 vs ARM_0 severed) | 0.0 / 0.0 / 0.0 |
| `first_commit_action_differs` | false / false / false |
| **`mech295_bias_range_mean`** (seed 42) | **0.0** |
| `mech295_fired_ticks` / `bridge_cue_fires` (seed 42) | 145 / 145 |
| `goal_norm_peak` (seed 42) | **0.193** |
| `action_entropy` (seed 42) | 0.71 (action_counts dominated by actions 1 + 3) |

## 2. The decisive metric

The probe (script lines 358-382) counts a **fire** when `torch.any(m != 0)` — the MECH-295 bias vector is non-zero — and accumulates `mech295_bias_range_sum += (m.max() - m.min())`. That sum is **0.0** across all 145 fired ticks. Therefore on every fired tick **`m.max() == m.min()`: the per-candidate MECH-295 bias is a uniform constant across candidates.**

The argmin check `argmin(s) != argmin(s - m)` **cannot** register a flip when `m` is a constant — subtracting the same scalar from every candidate's score leaves the argmin unchanged. So `argmin_flip_ticks=0` is **range-zero by construction**, NOT a small-but-real bias being outcompeted by the primary harm/goal scores.

## 3. Why the bias has zero range

`compute_approach_cue_score_bias(effective_drive, proximities)` returns a genuine per-candidate `[K]` vector (CLAUDE.md MECH-295 entry), so the constancy comes from its **input**: the per-candidate `goal_proximity` values are uniform. Two upstream substrate collapses produce that, both unfixed in this run:

1. **E2 action-conditional collapse (SD-056).** Candidates differ only in first action, but `E2.world_forward` compresses them to near-identical `z_world` (the V3-EXQ-571 `cand_world_pairwise_dist≈0` finding). 490k did not set `use_e2_action_contrastive` (default OFF). Identical candidate z_world → identical `goal_proximity` → uniform bias.
2. **Weak z_goal (goal-pipeline GAP-2 foraging ceiling).** `goal_norm_peak=0.193` — the attractor barely forms, so it cannot differentiate candidates spatially.

And the **`modulatory-bias-selection-authority`** substrate (landed 2026-06-03, the day before, precisely to give modulatory biases argmin-competitive authority via gap-relative scaling) was **OFF** (default). 490k ran on the un-enriched substrate.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | a range-zero bias can never flip an argmin regardless of MECH-295's true modulatory strength; `weakens` misattributes the layer |
| Biological reference | clear | NAcc/VP hedonic, Berridge wanting; not a formal import; lit covered, no pull |
| Prerequisites | missing | per-candidate z_world differentiation (SD-056), structured z_goal (GAP-2), modulatory-bias-selection-authority |
| Implementation | complete at MECH-295 | bridge fires (cue_fires=145); gap is upstream |
| Environment | inadequate for this measurement | gap4 env does not deliver differentiated per-candidate goal_proximity |
| Measurement | under-controlled | saturation-immune (490j fix worked) but defeated by a different upstream collapse (range-zero bias); needs a `bias_range>0` precondition guard |
| Integration | partially coupled | bridge computes per-candidate bias but receives uniform proximities |
| Scale | adequate | 900 steps x 3 seeds, cue fired all seeds |

**Recommended epistemic_category: `substrate_ceiling`.**

## 5. Disposition (user-confirmed)

- `evidence_direction` → **non_contributory** (override author-stamped `weakens`).
- `epistemic_category` → **substrate_ceiling**.
- `pending_retest_after_substrate` → **true**.
- **narrow_supports_flag = true:** MECH-295 carries substrate-firing support only (493 UC1-UC6; 490j C6/C7/C9) and STILL has zero behavioural-sufficiency support across the entire 490g/h/i/j/k lineage. non_contributory does not resolve that gap — MECH-295 stays candidate + v3_pending.
- The draft `evidence_quality_note` for governance is in the JSON artifact (`recommended_evidence_quality_note`).

## 6. Routing (user-confirmed): /queue-experiment + substrate amend

- **`/queue-experiment` V3-EXQ-490L** on the **enriched substrate**: `modulatory-bias-selection-authority` ON + SD-056 E2-contrastive ON, with a **pre-registered `mech295_bias_range_mean > 0` precondition guard** — argmin-flip results are interpretable only once the per-candidate bias is shown to be non-uniform. (This is the same lesson as the headroom guard 490j's autopsy added: guard the input-non-degeneracy before reading the discriminative metric.) Acceptance on the guarded substrate: `mech295_argmin_flip_fraction > 0` on ≥ 2/3 seeds = modulatory contribution behaviourally consequential.
- **substrate_queue: amend `scaffolded_sd054_onboarding`** — add `MECH-295` to `unblocks_claims` and append the 490k `failure_record`. The retest is gated on the same foraging-competence readiness (V3-EXQ-634c) that the rest of the cluster waits on, plus the modulatory-bias-selection-authority validation (both in flight).

## 7. Cluster context

Convergent with the goal-pipeline substrate-ceiling family (514l / 632 / 634 / 603e and the 460b-468b *b-cohort): one structural property — **the substrate does not deliver differentiated per-candidate goal structure** — surfacing here at the MECH-295 behavioural-sufficiency layer. Not N independent bugs.

## Lineage (substrate-firing sound, behavioural-sufficiency never shown)

- **490j** (2026-05-31): necessity test; `approach_commit_rate` ceiling-saturation; substrate-firing supports / behavioural-necessity weakens.
- **490k** (2026-06-04): modulatory-sufficiency probe; argmin-flip range-zero; non_contributory / substrate_ceiling (this artifact).
- **490L** (to be queued): modulatory-sufficiency on enriched substrate with bias-range guard.
