# Failure Autopsy — V3-EXQ-603p (base harm-landscape discriminativeness diagnostic)

- **Generated (UTC):** 2026-06-15T15:59:15Z
- **Scope:** single
- **Status:** confirmed
- **run_id:** `v3_exq_603p_base_harm_landscape_discriminativeness_diagnostic_20260615T101732Z_v3`
- **queue_id:** V3-EXQ-603p
- **machine:** ree-cloud-2
- **claim_ids:** `[]` (claim-free diagnostic)
- **outcome:** FAIL · **evidence_direction:** non_contributory · **self-route label:** `substrate_not_ready_requeue`
- **owning closure node:** `behavioral_diversity_isolation:GAP-C` (tonic noise floor / escape-affordance bridge; SD-059/MECH-358/MECH-313/MECH-260/Q-045)

---

## 1. Facts (no interpretation)

603p is the **diagnose-first locator** for the single readiness gate that 603o
(`escape_affordance_bridge_behavioural_redesign`) failed:
`harm_landscape_discriminative_on_base` cleared `harm_eval_range >= 0.02` on only 1/3 seeds
at proximity_harm=0.15. 603p isolates whether that failure is **regime-difficulty** (find the
hardest trainable proximity_harm) or **harm-training-strength** (3x-LR rescue at 0.15).

Design: BASE arm only (escape bridge OFF), run through **Stage-H only** (P1/P2 skipped),
on the 603k harm-pathway-trained + 603j trained-safety-signal substrate. 4 cells x 3 seeds.
Primary metric `harm_disc_frac` = fraction of seeds with `harm_eval_range >= HARM_DISC_RANGE_FLOOR`
(0.02). Gate: PASS if `>= 2/3`. **Positive control** = ARM_REGIME_0p10 (the *easiest* regime,
where 603k is asserted to have trained a discriminative harm landscape) must clear `>= 2/3`,
else the run self-routes `substrate_not_ready_requeue` — "harm-pathway training or the
readiness metric is broken even at the easy regime; diagnose the optimizer/loss before any
regime tuning (do NOT read this as a regime-difficulty result)."

| Cell | proximity_harm | harm_lr | harm_disc_frac | per-seed `harm_eval_range` [42,43,44] | mean prox_corr (where formed) |
|---|---|---|---|---|---|
| ARM_REGIME_0p10 (**positive control**) | 0.10 | 1e-3 | **0.333 (1/3)** | [0.1665 ✓, 0.0057, 0.0] | 0.831 (seed 42) |
| ARM_REGIME_0p12 | 0.12 | 1e-3 | 0.333 (1/3) | [0.1455 ✓, 0.0, 0.0] | 0.759 (seed 42) |
| ARM_REGIME_0p15 | 0.15 | 1e-3 | 0.333 (1/3) | [0.0, 0.1100 ✓, 0.0] | 0.441 (seed 43) |
| ARM_HARMTRAIN_3X_0p15 (LR rescue) | 0.15 | 3e-3 | **0.0 (0/3)** | [~3.7e-23, 0.0, 0.0] | — (collapsed) |

**Failed criterion:** the **positive-control readiness precondition** (an absolute/negative-control
criterion, not a discrimination criterion). `positive_control_clears = false` (1/3 < 2/3).

Three load-bearing observations:
1. **The positive control failed.** Even the easiest regime, where 603k allegedly trained the
   landscape, clears only 1/3 seeds.
2. **A different seed succeeds in each cell, and seed 44 never forms a landscape.** seed 42 forms
   at 0.10 and 0.12 but not 0.15; seed 43 forms at 0.15 but not 0.10/0.12; seed 44 is flat in
   every cell. The success is unsystematic across the regime axis.
3. **Tripling the harm-pathway LR collapses the landscape to numerically zero** on all three seeds
   (~1e-23). The training-strength axis, in the up direction, *destroys* the harm landscape rather
   than strengthening it.

When the landscape *does* form, it is strongly proximity-correlated (prox_corr 0.44–0.83) — i.e.
`harm_eval_head` learns the correct hazard-proximity mapping when it converges at all.

## 2. Claim layer

`claim_ids: []`. **No claim moves.** This is a substrate-readiness locator. SD-059 / MECH-358
(escape-affordance bridge) are **untouched** — 603p adjudicates *whether the substrate is ready to
test them*, not their truth. There is nothing to weaken, narrow, split, or demote.

## 3. Biological-reference triage

- **Closest reference mechanism:** amygdala (BLA→CeA) / periaqueductal-grey threat-value system +
  insular interoceptive aversion — a learned mapping from threat-proximity cues onto an aversive
  value that biases action selection. In REE this is `E3.harm_eval_head(z_world)`, which scores
  every candidate trajectory in `E3.select`.
- **Faithful translation vs formal import:** **faithful translation** (`is_formal_import: false`).
  This is a biologically-motivated value head trained on hazard-proximity, not a Pearl/Shannon/optimal-control
  formal definition. The SD-003 failure mode (formal-import divergence) does not apply here.
- **Lit status:** **present** — `evidence/literature/targeted_review_hazard_avoidance_learning/SYNTHESIS.md`
  (already referenced by the `scaffolded_sd054_onboarding` current_pending_amend). **No lit-pull
  commission needed.**
- **Does the failure match a missing-dependency / under-training signature?** Yes. A value head that
  forms a discriminative landscape on only a *minority* of seeds, and that a *stronger* learning rate
  *destroys*, is the fingerprint of an **under-trained / optimization-unstable** value head — exactly
  what you would expect if the aversive teaching signal is too sparse/noisy to reliably shape the head
  within the current training budget. It is **not** the mechanism being wrong: the amygdala/PAG
  threat-value mechanism is a solid existence proof, and the high prox_corr where it converges
  confirms the head learns the right mapping when it converges at all.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **N/A (claim-free)** | no claim tested; nothing to weaken/strengthen |
| Biological reference | **clear** | amygdala/PAG threat-value + insular aversion; failure = unstable/under-trained value head, not a wrong mechanism; `is_formal_import: false`; lit present |
| Prerequisites / dependencies | **present-but-immature** | `scaffold_train_harm_pathway` (603k, 2026-06-09 amend) IS in the optimizer, but converges on only 1/3 seeds under direct base measurement |
| Implementation completeness | **partial** | symbol present (head trains; prox_corr correct where it forms) but functional role unreliable across seeds; 3x-LR collapses it |
| Environment adequacy | **adequate** | all cells reached the hazard stage 3/3; proximity_harm 0.10–0.15 spans the needed difficulty; positive control is the *easiest* regime |
| Measurement adequacy | **adequate / non-vacuous** | cross-arm dynamic range MET (0.057 > 0.02 floor); prox_corr 0.44–0.83 when formed; NaN prox_corr only when range=0 (constant → undefined correlation, expected, not a metric bug) |
| Integration adequacy | **isolated** | Stage-H-only probe; no cross-module integration confound |
| Scale / capacity | **likely insufficient** | training budget/stability too low to converge reliably across seeds; raising LR 3x destabilizes (collapse) → the lever is steps/stability, not gain |

**Recommended `epistemic_category`:** `substrate_ceiling` — V3-tractable in principle; the correct
response is **substrate enrichment** (make harm-pathway training seed-robust), NOT more experiments
on the existing substrate and NOT a demotion. (Diagnostic is claim-free, so this is advisory; the
manifest's `evidence_direction: non_contributory` stands.)

## 5. The load-bearing correction (status over-statement)

The `scaffolded_sd054_onboarding` substrate-queue entry records the harm-pathway-survival leg as
**"VALIDATED 2026-06-09 (V3-EXQ-603k PASS)"**. That validation rested on a **narrow probe** — a
single `harm_eval(z_world)` range readout (~0.133) plus load-bearing G_H 2/3. Measured directly as
`harm_eval_range >= 0.02` under the BASE arm at the *easiest* regime, the leg clears only **1/3
seeds**. The "VALIDATED" status is **over-stated**: seed-robustness is an open residual. Governance
should record this and bake a **`>= 2/3`-seed gate on the direct `harm_eval_range` statistic** into
the harm-pathway readiness criterion so the leg stops flapping between "validated/cleared" and
re-failing on a broader measurement.

## 6. Recurrence note (granularity-debt hook)

603p is the **Nth** substrate-readiness autopsy in the 603 lineage
(603 / 603b / 603d / 603e / 603f / 603g-624c-651a / 603h / 603i / 603l / 603m → 603p). These circle a
**substrate** (Stage-H / harm-pathway / scaffolded_sd054 readiness), **not** a `bears_on` claim with
divergent failure signatures, so **`/claim-synthesis` does NOT apply** — there is no claim to
decompose. The recurrence is nonetheless a genuine signal: the harm-pathway / Stage-H survival leg
keeps being declared "validated/cleared" and then re-failing on a broader or more direct
measurement. The structural fix is the `>= 2/3`-seed robustness gate (Section 5), so the readiness
criterion converges instead of re-flapping.

## 7. Learning extracted

- The Stage-H harm-valuation pathway (`harm_eval_head(z_world)`, `scaffold_train_harm_pathway`) is
  **seed-fragile**: it forms a discriminative, proximity-correlated harm landscape on only 1/3 seeds
  at the easiest regime, and the success seed varies unsystematically with regime.
- **Raising the harm-pathway LR is the wrong lever** — 3x LR collapses the landscape to ~0 on all
  seeds. The fix is in training stability / steps / init, not gain.
- **The mechanism is right; convergence is the gap.** Where it forms, prox_corr is 0.44–0.83 — the
  head learns the correct hazard-proximity mapping. This tells the substrate fix what success looks
  like (more seeds reaching the seed-42-quality landscape).
- The "harm-pathway-survival leg VALIDATED 2026-06-09" status was a narrow probe; a direct
  `harm_eval_range >= 0.02` on `>= 2/3` seeds is the criterion that should gate it.

## 8. Routing decision (user-confirmed 2026-06-15)

- **Route:** `/implement-substrate` — **amend** `scaffolded_sd054_onboarding` (harm-pathway leg).
  Stabilize/strengthen harm-pathway training so `harm_eval_range >= 0.02` clears `>= 2/3` seeds at
  proximity_harm=0.10. Candidates: more training steps; **lower** LR with more steps; gradient
  stabilization; seed-robust init. NOT raising LR (collapses it).
- **Do NOT queue V3-EXQ-603q.** Its premise — that a regime exists where the base harm landscape
  clears `>= 2/3` seeds — is **false** (no cell clears 2/3, including the positive control). The
  GAP-C node's durable 603q spec is therefore **blocked** on this substrate fix landing, not on a
  located parameter.
- **Status correction (user-confirmed):** recommend governance flag the harm-pathway leg's
  "VALIDATED 2026-06-09" status as over-stated and add the `>= 2/3`-seed direct-`harm_eval_range`
  gate.
- **No `/claim-synthesis`** (claim-free substrate lineage, Section 6). **No `/lit-pull`** (biology lit
  present, Section 3). **No `/diagnose-errors`** (ran to completion, no crash). **No demotion**
  (claim-free; biology supports the mechanism class).
- SD-059 / MECH-358 / MECH-313 / MECH-260 / Q-045 statuses **unchanged**. The 603l/603o manifests
  are **not** re-touched.

## 9. Draft `evidence_quality_note` (for /governance to write; NOT written here)

> V3-EXQ-603p (claim-free Stage-H base-harm-landscape diagnostic; non_contributory; non-degenerate
> — cross-arm dynamic range 0.057 > 0.02, stage-0 z_goal lit 2/3). Positive control
> proximity_harm=0.10/harm_lr=1e-3 cleared harm_eval_range>=0.02 on only 1/3 seeds; all three
> standard cells clear 1/3 (a different seed each cell; seed 44 never); the 3x-LR rescue collapsed
> the landscape to ~0 on all seeds. Confirms the Stage-H harm-valuation pathway training (603k) is
> seed-fragile — NOT a regime-difficulty result (per the script's own positive-control interpretation
> rule). The "harm-pathway-survival leg VALIDATED 2026-06-09" status on scaffolded_sd054_onboarding
> rested on a narrow probe; seed-robustness is an open residual. Route: /implement-substrate
> (stabilize harm-pathway training to >=2/3 seeds at the easy regime; do NOT raise LR). Do NOT queue
> the V3-EXQ-603q bridge re-run until harm_eval_range>=0.02 clears >=2/3 seeds. SD-059/MECH-358
> unchanged.
