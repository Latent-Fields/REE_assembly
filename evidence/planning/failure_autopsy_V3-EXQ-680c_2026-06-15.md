# Failure Autopsy — V3-EXQ-680c (MECH-423 super-additivity ablation)

- **Generated (UTC):** 2026-06-15T03:56:56Z
- **Scope:** single
- **Status:** confirmed (interactive, user-directed: "Autopsy 680c → route 680d")
- **Run:** `v3_exq_680c_mech423_superadditivity_ablation_20260614T233657Z_v3`
- **Queue ID:** V3-EXQ-680c · **supersedes** V3-EXQ-680b
- **Claim tested:** MECH-423 (cross-model super-additivity; `mechanism_hypothesis`, `candidate`, `epistemic_category: standard`)
- **Self-route under adjudication:** `interpretation.label = substrate_not_ready_requeue`; `non_degenerate = false`; `evidence_direction = inconclusive`
- **Adjudication trigger:** `precondition_unmet` — readiness precondition `r1_grad_cosine_not_net_negative = NaN`

This is the redesign the [680b autopsy](failure_autopsy_V3-EXQ-680b_2026-06-14.md) ordered (grad-clip + bounded score + real cosine probe + n≥5). It ran to completion and self-routed. This autopsy adjudicates that self-route.

---

## 1. Facts (no interpretation)

n=5 seeds (42, 123, 456, 789, 1011); `min_seeds_pass=3`. Arms ISOLATED / INTEGRATED_PAIR / INTEGRATED_TRIPLE. Fixes applied vs 680b: `GRAD_CLIP_NORM=1.0` (heads + shared encoder in P0, heads in P1), `R2_SCORE_FLOOR=-1.0` (bounded world/affordance R2), real shared-encoder gradient cosine probe, n raised 3→5.

**INTEGRATED_PAIR per-seed:**

| Seed | world_R2 | affordance_R2 | R1 min_grad_norm | R1 shared-encoder cosine |
|------|----------|---------------|------------------|--------------------------|
| 42   | −1.0 (floor) | −1.0 | **inf** | **NaN** |
| 123  | −1.0 (floor) | 0.194 | 1.46e19 | **NaN** |
| 456  | −1.0 (floor) | −1.0 | **inf** | **NaN** |
| 789  | **0.817** | 0.461 | 0.0032 | **−0.399** |
| 1011 | −1.0 (floor) | −0.174 | **inf** | **NaN** |

`R2_SCORE_FLOOR=-1.0` ⇒ world_R2 = −1 is the **clamp floor**: the integrated-PAIR world head diverged on **4 of 5 seeds**. On those seeds the R1 shared-encoder gradient probe overflows (`min_grad = inf`) and its cosine is NaN. `min_cos = min(per-seed cosine)` is therefore NaN ⇒ readiness gate `r1_grad_cosine_not_net_negative` (threshold ≥ 0.0) reports `measured=NaN, met=false` ⇒ `substrate_not_ready_requeue`, `non_degenerate=false`, `degeneracy_reason="substrate_not_ready: P0 readiness unmet: r1_grad_cosine_not_net_negative"`.

INTEGRATED_TRIPLE also diverged on seed 456 (world_R2 −1.0); seeds 123/789/1011 finite (0.78 / 0.44 / 0.62).

**Failed criterion:** readiness precondition (not an absolute or a discrimination criterion). The super-additivity verdict never ran — the run self-excluded before scoring.

---

## 2. Claim-layer mapping — the self-route is claim-DESIGNED, not a failure

MECH-423's `what_would_answer` field defines the readiness gate verbatim:

> READINESS PRECONDITION … the integration machinery must demonstrably be doing cross-module work before the test means anything — (i) the shared latent must carry NON-ZERO cross-module gradient (measured), (ii) the inference loop must be running to convergence, (iii) offline/consolidation transfer must be active. **Below any of these the integrated and isolated arms are indistinguishable by construction and the run self-routes substrate_not_ready (non_degenerate=false), NOT a FAIL.**

So `non_degenerate=false` + `substrate_not_ready_requeue` is **exactly the behaviour the claim prescribes** for an unmet readiness gate. The R1 cosine sub-check is precondition (i). **MECH-423 is neither weakened nor falsified** — the run is non-contributory by the claim's own construction. 680b's 2/3 clean super-additive seeds (+1.57, +1.24) stand as the live evidence; this run adds nothing for or against.

What IS under adjudication: was precondition (i) genuinely unmet, or is the precondition *test* broken? **Both, in different ways:**

- The `min_cos` aggregate is **broken/poisoned** — unguarded against the inf/NaN gradients produced by the diverged seeds. A NaN here is the V3-EXQ-642 precondition-unmet pattern: the readout cannot evaluate the precondition, so the route is vacuous rather than informative.
- On the **one numerically-stable seed (789)**, the precondition is genuinely informative and **fails for a real reason**: shared-encoder cosine = **−0.399, net negative**. By the script's own design (`e3`/probe comments l534-537) a net-negative cosine is "the negative-transfer regime where sub-additivity is the EXPECTED consequence of gradient conflict." This is the first real R1 measurement and it points at genuine E1-world ↔ E2-self gradient conflict on the shared latent.

---

## 3. Biological-reference triage

Closest mechanism: multisensory super-additivity / inverse effectiveness (cortical + superior-colliculus multisensory neurons exceeding the unimodal sum); shared-representation MTL. Lit-pull present: `targeted_review_mech_423_integration_prerequisites` (2026-06-12). **Not** a formal-definition import — the mechanism has a working biological existence proof for the *class*.

Does the failure resemble a missing biological dependency? Partly — but the dominant signature is **numerical-instability (the 4/5 inf-gradient seeds)**, not a biology divergence. The one informative datum (seed 789 net-negative transfer) *is* a biologically-meaningful signal: shared-representation MTL helps only when the integrated objectives are related (Caruana 1997); anti-aligned task gradients (PCGrad / Yu 2020) produce negative transfer. Whether REE's E1-world and E2-self objectives are in that regime is the substantive open question 680d must answer on a *stable* substrate — it cannot be read off a run where 4/5 seeds diverged.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | self-route is claim-prescribed; MECH-423 not weakened; 680b 2/3 super-additive stands |
| Biological reference | clear | multisensory super-additivity existence proof; lit present; failure is numerical, not a missing-dependency biology signature |
| Prerequisites / readiness | unmet (and untestable) | precondition (i) cosine NaN on 4/5 seeds; genuinely net-negative (−0.40) on the 1 stable seed |
| Implementation completeness | partial | `GRAD_CLIP_NORM=1.0` + bounded score did **not** cure PAIR co-training divergence — clamp bounded the symptom (no 1e16 delta poisoning), divergence persists (world head pins at −1, encoder grads → inf) |
| Environment adequacy | adequate | grid 6 / 4 hazards / 3 resources |
| Measurement adequacy | under-instrumented / misleading | `min(cosine)` unguarded against inf/NaN gradients ⇒ the diverged seeds poison the aggregate to NaN; conflates "diverged" with "net-negative transfer" |
| Integration adequacy | coupled but unstable | shared-encoder co-training numerically unstable on 4/5 PAIR seeds despite grad clipping |
| Scale / capacity | n=5 adequate as designed, but 4/5 diverged ⇒ only 1 usable readiness datum |

**Recommended `epistemic_category`:** `standard` (unchanged). **Dominant diagnosis layer:** implementation/measurement (co-training numerical instability + unguarded readiness aggregate), with a genuine secondary readiness signal (negative transfer on the stable seed) that 680d must isolate.

---

## 5. Learning extracted

1. **Grad-clip-norm 1.0 + bounded score did NOT stabilise the integrated co-training.** The −1 clamp removed the 680b margin-poisoning (good) but the PAIR world head still diverges on 4/5 seeds — the clamp bounds the *reported* R2, not the *training* dynamics. The encoder gradients overflow to `inf`. A stronger stabilizer is required (LR reduction / warmup, detached-target discipline on the shared latent, or per-objective gradient-norm balancing à la PCGrad).
2. **The readiness cosine aggregate is poisoned by diverged seeds.** `min(per-seed cosine)` with any inf-gradient seed → NaN. Diverged seeds must be detected and bucketed as a *distinct* "diverged / non-finite" readiness category — NOT folded into the net-negative-transfer test, which they make uninterpretable.
3. **First genuine R1 readiness datum is net-negative (−0.40).** On the one stable seed the shared-encoder objectives are anti-aligned. This is a real, biologically-meaningful negative-transfer signal — but n=1 of 5. It is the load-bearing scientific question for 680d: if a stabilised substrate shows persistent net-negative shared-encoder cosine across seeds, that is a substrate-readiness finding (super-additivity is *not expected*; the shared-latent integration is in the negative-transfer regime), routing toward `/implement-substrate` or claim-narrowing — **not** a re-queue. If stabilisation lifts the cosine to ≥0, the super-additivity test can finally run.

---

## 6. Routing

**`/queue-experiment` → V3-EXQ-680d** (supersedes 680c). Same scientific question (implementation fix), so a lettered iteration. Two coupled fixes:

- **(a) Stabilise the integrated co-training** so the PAIR arm does not diverge to the world_R2 floor: reduce the encoder/head co-training LR and/or add warmup; consider detaching the shared-latent target on the off-objective; optionally a per-objective gradient-norm balance so neither stream's gradient dominates. Acceptance precondition: ≥4/5 PAIR seeds finite world_R2 (off the −1 floor) before any cosine is read.
- **(b) Guard the readiness cosine** against inf/NaN: compute `min_cos` only over finite-gradient seeds; emit a separate `n_diverged_seeds` readout and route `substrate_not_ready` with reason `co_training_diverged` when diverged seeds dominate — distinct from `r1_grad_cosine_net_negative`, which should fire only on a *finite* net-negative cosine (the genuine negative-transfer readiness fail).

**Pre-register the fork** in 680d so the next self-route is unambiguous:
- diverged-seeds dominate again → instability unfixed → diagnose / stronger stabiliser (do not iterate blindly).
- stable substrate, cosine ≥ 0 on ≥3/5 → readiness met → super-additivity verdict runs (the actual MECH-423 test).
- stable substrate, cosine net-negative on ≥3/5 → **genuine readiness fail / substrate finding**: shared-latent integration is in the negative-transfer regime; super-additivity not expected; route to `/implement-substrate` (shared-latent objective reconciliation) or narrow MECH-423, **not** another re-queue.

**Recommended governance writes (do NOT apply here):**
- `evidence_direction: non_contributory` on the 680c manifest (it is already `inconclusive` + `non_degenerate=false`/`scoring_excluded=degenerate`; either is correct — the run carries no MECH-423 evidence). Pairs with `pending_retest_after V3-EXQ-680d`.
- Draft `evidence_quality_note`: *"V3-EXQ-680c substrate_not_ready_requeue (non_degenerate=false). Autopsy 2026-06-15: the readiness cosine NaN is poisoned by 4/5 PAIR seeds diverging to the world_R2 −1 clamp floor (encoder grads → inf) despite GRAD_CLIP_NORM=1.0 — the 680b-ordered grad-clip + bounded score did NOT cure the co-training instability. The one stable seed (789) shows a genuine net-negative shared-encoder cosine (−0.40) = negative-transfer readiness signal. MECH-423 NOT weakened (the self-route is the claim-designed non_degenerate response; 680b's 2/3 super-additive seeds stand). pending_retest_after V3-EXQ-680d (co-training stabilisation + inf/NaN-guarded cosine separating diverged seeds from genuine net-negative transfer)."*

No `recommended_substrate_queue_entry` (`action: none`) — the defect is in the experiment training regime + readiness readout, fixable in the harness via the 680d redesign. The negative-transfer question only becomes a substrate gap if 680d, on a stable substrate, confirms persistent net-negative shared-encoder cosine across seeds.

Also owed to `/governance` (out of scope here): mark 680b `reviewed` (the prior autopsy landed; review-mark was never written).
