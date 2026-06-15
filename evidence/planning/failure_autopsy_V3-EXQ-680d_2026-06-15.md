# Failure Autopsy — V3-EXQ-680d (MECH-423 cross-model super-additivity ablation)

- **Generated (UTC):** 2026-06-15T16:00:47Z
- **Scope:** single
- **Status:** confirmed (interactive, user-directed 2026-06-15: "Re-queue 680e, fix gate")
- **Run:** `v3_exq_680d_mech423_superadditivity_ablation_20260615T044447Z_v3`
- **Queue ID:** V3-EXQ-680d · **supersedes** V3-EXQ-680c
- **Claim tested:** MECH-423 (cross-model super-additivity; `mechanism_hypothesis`, `candidate`, `epistemic_category: standard`, `v3_pending`)
- **Self-route under adjudication:** `interpretation.label = substrate_not_ready_requeue`, `fork=3`, `route=r1_grad_cosine_net_negative`; `non_degenerate=false`; `evidence_direction=inconclusive`
- **Adjudication trigger:** `precondition_unmet` — readiness precondition `r1_grad_cosine_not_net_negative` measured `min_cos=-0.0371 < 0.0`

This is the implementation fix the [680c autopsy](failure_autopsy_V3-EXQ-680c_2026-06-15.md) ordered (stabilise the integrated co-training so PAIR seeds do not diverge to the world_R2 floor; inf/NaN-guard the readiness cosine over usable seeds). It ran to completion and self-routed FORK 3. This autopsy adjudicates that self-route.

---

## 1. Facts (no interpretation)

n=5 seeds (42, 123, 456, 789, 1011); `min_seeds_pass=3`; arms ISOLATED / INTEGRATED_PAIR / INTEGRATED_TRIPLE. The 680c-ordered fixes are present and **worked**:

- **Co-training is stable.** `co_training.n_diverged_seeds=0`, `n_usable_pair_seeds=5`. All 5 PAIR seeds finite and **off the −1 clamp floor**: `pair_world_r2_raw` = {42: 0.346, 123: 0.252, 456: 0.167, 789: 0.207, 1011: 0.147}. No `pair_finite_off_floor` is false; no nonfinite skips. (Contrast 680c: 4/5 PAIR seeds diverged to the floor with inf grads / NaN cosine.)
- **Readiness cosine is now clean** (no NaN). `pair_r1_cosine` = {42: **+0.0506**, 123: **−0.0371**, 456: **−0.0149**, 789: **−0.0286**, 1011: **+0.0266**}. Range −0.037 … +0.051; **2/5 positive**; every |cos| < 0.051. `min_grad_norm` per seed ~4.2e-4 … 1.0e-3 (coupling genuinely present).

**PAIR vs ISOLATED integration_score (= world_R2 + affordance_R2, held-out):**

| seed | ISOLATED | PAIR | delta_pair |
|------|----------|------|-----------|
| 42   | 0.2072 | 0.8022 | **+0.5950** |
| 123  | 0.2618 | 0.5990 | **+0.3373** |
| 456  | 0.1367 | 0.5347 | **+0.3980** |
| 789  | 0.1574 | 0.3654 | **+0.2080** |
| 1011 | 0.2328 | 0.4431 | **+0.2103** |

PAIR > ISOLATED on **5/5 seeds**; mean delta **+0.3497 > 0**; all deltas positive.

**Failed criterion:** a **readiness precondition** (not an absolute or discrimination criterion). The super-additivity verdict (FORK 2) never ran — the run self-excluded at the readiness gate before scoring.

**The readiness gate logic (script lines 814–835):** `min_cos = min(cosine over usable seeds)` = −0.0371; check `r1_grad_cosine_not_net_negative` has `threshold=0.0, direction=lower` → requires `min_cos >= 0`; −0.0371 < 0 ⇒ `met=false` ⇒ `p0_readiness_gate` raises `P0NotReady` ⇒ FORK 3 ⇒ `substrate_not_ready_requeue`, `non_degenerate=false`, note = "GENUINE finite net-negative shared-encoder cosine … negative-transfer regime … super-additivity is NOT expected … Route: /implement-substrate or narrow MECH-423, NOT another re-queue."

---

## 2. The self-route is mis-designed, not informative — adjudication

**The gate suppressed a passing result.** Recomputing the FORK-2 verdict from the manifest's own `integration_score` values (exactly the script's scoring block, lines 882–895):

```
delta_pair      = [0.595, 0.337, 0.398, 0.208, 0.210]   (mean +0.3497)
delta_sd        = pstdev(delta_pair) = 0.1430
margin          = max(2.0 * 0.1430, 0.02) = 0.2859
n_seeds_pass    = #{delta > 0.2859} = 3   (seeds 42, 123, 456)
super_additive  = (3 >= MIN_SEEDS_PASS=3) = TRUE   ->  PASS / supports
```

Had the readiness cosine gate not short-circuited scoring, **680d would have PASSED** the pre-registered super-additivity criterion (3/5 seeds clear the hardened SD-of-delta+floor margin; mean delta +0.35 > 0; PAIR>ISO 5/5).

**The −0.0371 is gradient orthogonality noise, not negative transfer.** Three reasons the manifest's "negative-transfer regime, super-additivity NOT expected" reading is wrong:

1. **Magnitude.** The cosines cluster at ≈0 (±0.05), 2/5 positive. This is the near-**orthogonal** regime, not anti-alignment. The 680c "−0.399 negative-transfer" datum was an order of magnitude larger **and** measured on a *diverged* seed; on the stabilised substrate the cosine collapsed toward zero. Near-orthogonal task gradients predict *additive/independent* contributions (Caruana 1997), and the empirics show **super-additivity** — the opposite of what the self-route claims.
2. **The aggregator + threshold are mis-calibrated.** The gate takes `min(cosine)` over 5 seeds against a hard `0.0` threshold. For a quantity noise-distributed around zero, the minimum of 5 samples is essentially always slightly negative — the gate is structurally near-impossible to clear (FORK 2 requires *all five* seeds ≥ 0) and fires on noise. It conflates "coupling exists" (already verified by `min_grad_norm` ≥ floor, genuinely met) with "coupling is non-conflicting."
3. **Claim spec.** MECH-423's `what_would_answer` readiness precondition (i) requires the shared latent carry **NON-ZERO cross-module gradient (measured)** — i.e. that coupling *exists*. That is the `min_grad_norm` check (met). The `cosine ≥ 0` sub-check is an experiment-design addition beyond the claim's readiness spec; as a binary readiness gate at threshold 0.0 it is mis-calibrated, and as a negative-transfer detector it should be an *outcome interpretation*, not a run-excluding gate.

This is the V3-EXQ-642 pattern named in the skill: the precondition's branch assumption was not genuinely unmet — the **precondition test itself is wrong**. MECH-423 is **neither weakened nor falsified**; if anything the suppressed data *supports* it. 680b's 2/3 strong super-additive seeds stand, and 680d (gate-corrected) would add a 3/5-seed PASS on a stable substrate.

---

## 3. Biological-reference triage

Closest mechanism: multisensory super-additivity / inverse effectiveness (cortical + superior-colliculus multisensory neurons exceeding the unimodal sum); shared-representation MTL (Caruana 1997). Lit-pull present: `targeted_review_mech_423_integration_prerequisites` (2026-06-12). **Not** a formal-definition import — a working biological existence proof for the *class*. The failure is **not** a missing-dependency biology signature; it is a readiness-gate measurement-design defect on a substrate that demonstrably exhibits the mechanism (PAIR>ISO 5/5). No new `/lit-pull` arises.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | strengthened / intact | self-route is mis-designed, not a weakens; suppressed verdict would PASS; MECH-423 supported by its own data |
| Biological reference | clear | multisensory super-additivity; lit present; failure not a missing-dependency biology signature |
| Prerequisites / readiness | **met** (coupling) but **mis-gated** | `min_grad_norm` met (~4e-4–1e-3); cosine sub-check fires on orthogonality noise via `min(cos)≥0` |
| Implementation completeness | complete (co-training **fixed**); readiness readout **defective** | 680c-ordered stabilisation worked (0/5 diverged); the cosine gate is the remaining defect |
| Environment adequacy | adequate | grid 6 / 4 hazards / 3 resources |
| Measurement adequacy | **misleading** | `min(cosine)≥0` on a ≈0-noise quantity self-excludes a passing run; conflates orthogonal with anti-aligned |
| Integration adequacy | coupled and **stable** | shared-encoder co-training stable on all 5 PAIR seeds |
| Scale / capacity | adequate | n=5; 5/5 usable |

**Recommended `epistemic_category`:** `standard` (unchanged). **Dominant diagnosis layer:** measurement / test-design (mis-calibrated readiness cosine gate), on a now-stable substrate.

---

## 5. Learning extracted

1. **The 680c-ordered co-training stabilisation worked.** 0/5 diverged, all PAIR world_R2 finite & off-floor. The instability that poisoned 680b (one diverged seed) and 680c (4/5 diverged → NaN cosine) is resolved.
2. **The readiness cosine gate is the remaining defect.** `min(cosine over seeds) ≥ 0` is the wrong test for a quantity noise-distributed around zero: it requires all 5 seeds ≥ 0 (≈1/32 likely), fires `net_negative` on −0.037 orthogonality noise, and self-excludes the run before the verdict. It also conflates the near-orthogonal regime (super-additivity present) with the anti-aligned regime (super-additivity not expected).
3. **First clean readiness measurement shows the near-orthogonal regime, and super-additivity is empirically present.** Cosines cluster at ≈0 (2/5 positive); PAIR>ISO on 5/5 seeds; the gate-corrected verdict is a 3/5-seed PASS (margin 0.286, mean delta +0.35). The "negative-transfer, super-additivity not expected" self-route reading is contradicted by the run's own data.
4. **Recurrence is convergence, not granularity-debt.** 680b/680c shared one root cause (numerical instability); 680d peels to the next layer (gate design) on a fixed substrate. Not a `/claim-synthesis` trigger — same-question re-queue.

---

## 6. Routing (user-confirmed 2026-06-15)

**`/queue-experiment` → V3-EXQ-680e** (supersedes 680d; same scientific question + same hardened margin + same readiness intent — alphabetic suffix = measurement/test-design fix). Redesign spec:

- **Fix the readiness cosine gate.** Replace `min(cosine) ≥ 0` with a magnitude-floored / tolerance-band test so a net-negative route fires only on *meaningful* anti-alignment, not orthogonality noise. Concretely (pick one, pre-register):
  - route `r1_grad_cosine_net_negative` only if `min_cos < -COS_FLOOR` (e.g. COS_FLOOR ≈ 0.1), OR a majority (≥ ⌈n/2⌉) of seeds have `cos < -COS_FLOOR`; AND
  - treat the **near-orthogonal band** (`|cos| ≤ COS_FLOOR`) as **readiness-MET** so the super-additivity verdict runs (orthogonal gradients do not preclude super-additivity).
  - Consider testing the **mean** cosine against a negative magnitude floor rather than the bare per-seed minimum, to stop one near-zero seed self-excluding the run.
- **Keep everything else 680d-identical:** the gentled co-training (works), the inf/NaN guard, the hardened SD-of-delta + abs-floor margin, n≥5.

**Pre-register the fork** so the next self-route is unambiguous:
- co-training diverges again → instability regressed (diagnose, do not iterate blindly).
- stable + corrected gate, cosine in the orthogonal/positive band → readiness MET → super-additivity verdict runs (expected on this substrate; likely **PASS** — 680d's suppressed verdict was 3/5 over margin).
- stable + **genuine** finite net-negative cosine (`min_cos < -COS_FLOOR` on a majority) → genuine negative-transfer readiness fail → THEN `/implement-substrate` (shared-latent objective reconciliation) or narrow MECH-423.

**Recommended governance writes (do NOT apply here):**
- `evidence_direction: non_contributory` on the 680d manifest (it is `inconclusive` + `non_degenerate=false`/`scoring_excluded=degenerate`; either is correct — the run carries no MECH-423 evidence because the verdict never ran). Pair with `pending_retest_after V3-EXQ-680e`.
- Draft `evidence_quality_note` (governance to write on the 680d manifest / MECH-423 ledger):
  > "V3-EXQ-680d substrate_not_ready_requeue (FORK 3, min_cos=-0.0371, non_degenerate=false). Autopsy 2026-06-15: the 680c-ordered co-training stabilisation WORKED (0/5 PAIR seeds diverged; all world_R2 finite off-floor). On the stable substrate the shared-encoder cosines collapsed to ~0 (range -0.037..+0.051, 2/5 positive) — the near-ORTHOGONAL regime, not negative transfer. The readiness gate's `min(cos)>=0` test fires on orthogonality noise and self-excluded a run whose suppressed FORK-2 verdict would PASS (3/5 seeds clear margin 0.286; mean delta +0.35; PAIR>ISO 5/5). MECH-423 NOT weakened — the self-route is a mis-calibrated precondition, not a negative-transfer finding (the manifest's `/implement-substrate or narrow` note is contradicted by its own PAIR>ISO data). pending_retest_after V3-EXQ-680e (magnitude-floored / tolerance-band readiness cosine gate; near-orthogonal = readiness-MET so the verdict runs)."

No `recommended_substrate_queue_entry` (`action: none`) — the defect is the experiment's readiness readout, fixable in the harness via the 680e gate redesign. A shared-latent objective-reconciliation substrate gap only becomes live if 680e, with a *corrected* gate on a stable substrate, confirms a *genuine* finite net-negative cosine (below a meaningful magnitude floor) across a majority of seeds.

---

## 7. Recurrence (granularity-debt check)

Prior planning autopsies on this target: `failure_autopsy_V3-EXQ-679_2026-06-14` (clean diagnostic gate-clear, tags nothing), `failure_autopsy_V3-EXQ-680b_2026-06-14`, `failure_autopsy_V3-EXQ-680c_2026-06-15`. 680b/680c shared one root cause (numerical instability of the integrated co-training); 680d is the *converging* next peel (instability fixed → readiness-gate design defect exposed) on a now-stable substrate, not a claim circling in structurally-different ways. This is iteration convergence, **not** granularity-debt — no `/claim-synthesis` recommendation. Re-evaluate only if 680e (corrected gate) returns a *third structurally-distinct* failure shape.
