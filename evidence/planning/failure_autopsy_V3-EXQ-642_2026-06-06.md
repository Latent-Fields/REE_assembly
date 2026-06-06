# Failure Autopsy -- V3-EXQ-642 (MECH-353 blocked-agency / z_block discriminative diagnostic)

- **Generated (UTC):** 2026-06-06T08:06:25Z
- **Run:** `v3_exq_642_blocked_agency_zblock_discriminative_20260606T055351Z_v3`
- **Queue ID:** V3-EXQ-642
- **Outcome:** FAIL (`experiment_purpose: diagnostic`, `claim_ids: []` -- does not weight governance confidence)
- **Scope:** single
- **Status:** confirmed (interactive gate answered 2026-06-06 -- Reading A)
- **Bears on (cited, not tagged):** MECH-353, SD-029, MECH-112, MECH-320, MECH-342, ARC-016, SD-011, SD-019b

---

## 1. Verdict (one line)

The C0 comparator-non-discriminative result is an **untrained-substrate test-design
artifact**, NOT a trained-substrate ceiling and NOT a falsification of MECH-353. The
experiment's P0 trained `world_forward` on a **frozen random encoder** with **SD-056
contrastive OFF**, so the SD-029 action-outcome comparator was floored to exactly 0 on
every step by construction. MECH-353 was never actually tested. **Route: re-queue
V3-EXQ-642a** at an adequate P0 (train the encoder so `z_world` tracks position + enable
SD-056). MECH-353 stays `v3_pending`.

This corrects the manifest's own self-route (`substrate_ceiling_comparator_nondiscriminative`),
which is premature because the substrate was never trained to the level the MECH-353 design
doc requires before the comparator can be read.

---

## 2. Facts reconstruction (no interpretation)

### Manifest (per-seed, both arms)

| seed | wf_mse_final | blocked_step_mismatch_mean | free_step_mismatch_mean | z_block_peak (BLOCK / CONTROL) | z_harm_a_mean | C0 | C1 | C2 | C3 |
|------|-------------|----------------------------|-------------------------|--------------------------------|---------------|----|----|----|----|
| 42 | 2.34e-05 | 0.0 | 0.0 | 0.0 / 0.0 | 0.0 | F | F | F | **T** |
| 43 | 8.13e-05 | 0.0 | 0.0 | 0.0 / 0.0 | 0.0 | F | F | F | **T** |
| 44 | 2.04e-05 | 0.0 | 0.0 | 0.0 / 0.0 | 0.0 | F | F | F | F |

- `interpretation.label = substrate_ceiling_comparator_nondiscriminative`;
  `c0/c1/c2_seeds_pass = 0`, `c3_seeds_pass = 2`, `seeds_needed = 2`.
- Env fired the block: ARM_BLOCK `n_blocked_steps` ~1179-1183/seed, ARM_CONTROL 0.
  `action_rate` ~0.92-1.0 in both arms; `z_harm_a_mean = 0.0` everywhere (num_hazards=0,
  harm held constant as designed).
- `n_runs_completed = 6 / 6` (ran to completion -- a FAIL, not an ERROR).

### Which criterion failed, and the fingerprint

- **Discrimination criteria C0, C1, C2: 0/3 seeds.**
- **Negative-control / absolute criterion C3 (assert-not-withdraw): 2/3 seeds** -- and it
  passes **vacuously**. With `z_block` identically 0 the ASSERT consumer never fires, so
  both arms are bit-identical; `action_rate(BLOCK) ~= action_rate(CONTROL)` and `z_harm_a`
  flat trivially satisfy "no withdrawal / no suffering rise." Seed 44 fails C3 only because
  `action_rate` saturated at 1.0 in both arms and `alt_switch_rate(BLOCK)=0.0238 <
  alt_switch_rate(CONTROL)=0.0279`, so the `assert_sig` OR-clause is False.
- Shape = "negative control passes, every discrimination criterion fails" -- the canonical
  substrate-ceiling tell. The autopsy's job is to adjudicate the **cause** of that shape.

### Script (what P0 actually trained)

`experiments/v3_exq_642_blocked_agency_zblock_discriminative.py`:

- `_train_world_forward` (P0) optimises **only**
  `e2.world_transition.parameters()` + `e2.world_action_encoder.parameters()`.
  Docstring, verbatim: *"Encoder is left fixed (random); world_forward is the trainable
  target."*
- `CFG_KWARGS = dict(use_blocked_agency=True, z_goal_enabled=True, drive_weight=2.0,
  alpha_world=1.0)` -- **does NOT** set `e2_action_contrastive_enabled` (SD-056 OFF) or
  `use_resource_proximity_head` (SD-018 OFF). No encoder-side supervision of any kind.
- Detector floor: `blocked_agency_predicted_effect_floor` default `0.05` (config.py:2090);
  `outcome_mismatch_floor` default `0.1`. The agent's `_update_blocked_agency` zeroes
  `outcome_mismatch` whenever `pred_mag = ||world_forward(z_world_prev, a) - z_world_prev||
  < predicted_effect_floor`.

---

## 3. Claim-layer mapping

- `claim_ids: []` (diagnostic substrate-readiness; correctly untagged -- carries no
  governance weight). `bears_on` lists MECH-353 + dependencies; none are weighted by this
  run.
- MECH-353 (`affect.blocked_agency_control_failure_stream`): status IMPLEMENTED 2026-06-06,
  `v3_pending` TRUE until this discriminative experiment PASSes. The substrate implementation
  is complete and contract-clean (9/9 MECH-353 contracts; 803/803 ree-v3). **The experiment
  did not let the claim express itself** -- z_block never left 0, so MECH-353 is *untested*,
  not weakened.
- **`claim_ids` accuracy:** correct. This is a substrate-readiness gate, not a claim test;
  no inherited-tag contamination risk (claimless by design).

---

## 4. Biological-reference triage

- Closest mechanism: frustrative-non-reward / RAGE assert-pole comparator -- expected-minus-
  obtained on the action-effect channel (Papini 2024 FNR; Carruthers 2012 comparator;
  Davis & Montag 2019 RAGE; Bertsch 2020 prefrontal-gated assert). The 2026-06-05 lit-pull
  (`targeted_review_blocked_agency_anger_stream`) grounds the claim as a distinct stream.
- Is the REE detector a faithful translation or a formal import? **Faithful** -- the SD-029
  comparator is a single-pass forward-model mismatch (MECH-256 family), already the
  biology-correct shape (contrast SD-003's two-pass error). No formal-import divergence here;
  **no lit-pull commission is warranted.**
- Does the failure resemble a missing biological dependency? **Yes, exactly.** The comparator
  cannot read a block if the perceptual substrate (`z_world`) does not represent agent
  position at single-cell granularity -- the biological analogue of "a comparator with no
  trained world model to compare against." The dependency (a trained encoder + action-
  conditional forward model, SD-056) was absent. This is a **discovered/confirmed
  prerequisite**, not a falsification.

---

## 5. Root-cause mechanics (why the comparator floored to 0)

`outcome_mismatch = ||world_forward(z_world_prev, a) - z_world_now|| / (pred_mag + eps)`,
zeroed when `pred_mag < predicted_effect_floor (0.05)`.

- With a **frozen random encoder**, `z_world` is a fixed random projection of the obs. The
  agent-position-dependent component of a single-cell move is a small fraction of the
  (largely static, per-episode) landmark-field obs, so `||z_world_now - z_world_prev||` for a
  move is tiny.
- `world_forward` trained on this low-variance target trivially fits **near-identity**
  (`predict z_world_now ~= z_world_prev`). Hence `wf_mse_final ~ 2e-5` -- **misleadingly
  low**: it is a low-variance-target fit, *not* evidence of a discriminative comparator.
- Consequence: `pred_mag = ||zw_pred - z_world_prev|| ~ 0 < 0.05` on **every** step ->
  `outcome_mismatch` identically 0 on both blocked and free steps -> z_block never
  accumulates -> C0/C1/C2 fail by construction; C3 passes vacuously.
- The MECH-353 design doc (`mech_353_blocked_agency_zblock.md`, "Backward compatibility /
  training notes" + ree-v3/CLAUDE.md MECH-353 "DETECTOR DISCRIMINATION DEPENDS ON A TRAINED
  SUBSTRATE") **predicts exactly this** for an untrained encoder and prescribes the fix:
  "The validation experiment trains the encoder (representing scene/position in z_world) and
  the action-conditional world_forward (SD-056) in P0." The script trained neither.

**Why the self-route is premature:** `substrate_ceiling` (per REE_assembly Phase-3 epistemic
schema) means "V3-tractable in principle but the substrate is too coarse to deliver the
distinction *even when trained*." That claim cannot be made from this run because the
substrate was never trained. The correct category is a measurement / test-design gap.

---

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **untested** | z_block never rose; MECH-353's affective claim never had a chance to express. Not weakened, not strengthened. |
| Biological reference | clear | RAGE / FNR assert-pole comparator (Carruthers 2012, Papini 2024); claim grounded by the 2026-06-05 lit-pull. No formal-import divergence; no lit-pull needed. |
| Developmental / dependency prerequisites | **missing** | SD-056 (`e2_action_contrastive_enabled`) OFF; encoder untrained (no SD-018 / event-contrastive supervision) -> SD-029 comparator inert. Confirmed prerequisite, not falsification. |
| Implementation completeness | complete | BlockedAgency regulator + detector wired correctly (9/9 contracts, 803/803 ree-v3). The defect is in the *experiment's P0*, not the substrate. |
| Environment adequacy | adequate | scheduled_action_block fired (~1180 blocked steps/seed in ARM_BLOCK, 0 in CONTROL); harm + goal held constant as designed. |
| Measurement adequacy | adequate-but-floored | The metric is correct; `pred_mag < floor` on every tick forced `outcome_mismatch` to 0. The floor is doing its fail-safe job on an untrained substrate. |
| Integration adequacy | n/a (untested) | consumers (assert bias / decommit) never fired because z_block stayed 0. |
| Scale / capacity | **insufficient** | random encoder + no SD-056 -> z_world does not track single-cell moves at supra-floor magnitude. P0 budget irrelevant until the *right things* are trained. |

**Recommended epistemic_category:** none for MECH-353 status change (claimless diagnostic).
The run is best characterised as a **measurement / test-design gap** -> `/queue-experiment`.
Do **not** record `substrate_ceiling` on any claim from this run.

---

## 7. Learning extracted

1. **Confirmed prerequisite:** the SD-029 z_world action-outcome comparator (MECH-353
   detector) requires a *trained* encoder + action-conditional `world_forward` (SD-056)
   before it can discriminate a blocked move from a successful one -- exactly as the design
   doc predicted. This run is positive evidence for that dependency, not against MECH-353.
2. **`wf_mse` is not a substrate-readiness signal on its own.** A low `wf_mse` over a
   low-variance (position-insensitive) `z_world` target is fully compatible with a degenerate
   `pred_mag ~ 0`. The right readiness metric is `pred_mag` / `cand_world_pairwise_dist`
   (SD-056's `cand_world_pairwise_dist` diagnostic), not the reconstruction/forward MSE.
3. **A self-routing diagnostic still needs an autopsy.** The manifest's
   `substrate_ceiling_comparator_nondiscriminative` label is correct about the *symptom*
   (C0 non-discriminative) but wrong about the *cause* (untrained, not coarse). The
   interpretation grid's "C0 fail -> substrate_ceiling" branch assumed a trained substrate;
   this run did not meet that precondition.

---

## 8. Routing decision (user-confirmed: Reading A)

**Primary route: `/queue-experiment` -> V3-EXQ-642a** (alphabetic suffix; same scientific
question -- MECH-353 blocked-agency discrimination -- with a corrected P0). Required changes:

1. **Train the encoder so z_world tracks position.** Add encoder-side supervision in P0:
   `use_resource_proximity_head=True` (SD-018) and/or event-contrastive supervision (SD-009),
   or a dedicated position-supervised encoder warmup. The acceptance precondition is a
   supra-floor `pred_mag` (i.e. `cand_world_pairwise_dist` / single-step `pred_mag` >=
   `predicted_effect_floor=0.05` by a clear margin) on a successful move BEFORE measuring C0.
2. **Enable SD-056:** `e2_action_contrastive_enabled=True` (action-conditional `world_forward`
   divergence preservation) so the forward model is action-discriminative, per the design doc.
3. **Add a P0 readiness gate:** measure `pred_mag` on a known successful move and assert it
   clears the floor with margin; if it does not, self-route to a *genuine* substrate-readiness
   finding (then -- and only then -- a substrate-enrichment task is warranted).
4. Keep the rest of the design (static landmark env, harm held constant, pinned z_goal,
   scripted + policy measurement, C0-C3 grid, 3 seeds) unchanged.

**MECH-353 stays `v3_pending`.** Not falsified, not `substrate_ceiling`, no enrichment claim
minted. No claims.yaml / manifest / substrate_queue edit from this autopsy (analysis +
handoff only; `/queue-experiment` builds 642a; governance owns any later status change).

**Draft `evidence_quality_note` for governance (do NOT write here):**
> V3-EXQ-642 (2026-06-06) FAILed C0/C1/C2 with the comparator floored to outcome_mismatch=0
> on every step. Failure autopsy (failure_autopsy_V3-EXQ-642_2026-06-06): untrained-substrate
> test-design artifact, NOT a falsification or substrate ceiling -- P0 trained world_forward
> on a frozen random encoder with SD-056 OFF, so pred_mag stayed below the 0.05 predicted-effect
> floor by construction (wf_mse~2e-5 is a low-variance-target fit, not a discriminative
> comparator). MECH-353 remains v3_pending pending V3-EXQ-642a (encoder trained to track
> position + e2_action_contrastive_enabled). pending_retest_after_substrate: true.

---

## 9. Cross-references

- Substrate: ree-v3/CLAUDE.md "MECH-353" section; `docs/architecture/mech_353_blocked_agency_zblock.md`.
- SD-056 (action-conditional world_forward + `cand_world_pairwise_dist` readiness diagnostic):
  ree-v3/CLAUDE.md "SD-056" sections.
- SD-018 (resource-proximity supervision), SD-009 (event-contrastive) -- candidate encoder-side
  supervision for the 642a P0.
- Manifest: `REE_assembly/evidence/experiments/v3_exq_642_blocked_agency_zblock_discriminative_20260606T055351Z_v3.json`.
- Script: `ree-v3/experiments/v3_exq_642_blocked_agency_zblock_discriminative.py`.
