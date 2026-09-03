# Failure autopsy — V3-EXQ-978 (SD-018 directional-field fishtank)

**Generated:** 2026-09-03T20:04:14Z · **Scope:** single · **Status:** confirmed at the /failure-autopsy Step 8 interactive gate, 2026-09-03
**Claims tagged:** INV-088, MECH-457 (both **peripheral co-tags** — see §3) · **Machine-readable:** `failure_autopsy_V3-EXQ-978_2026-09-03.json`

---

## 1. Why this run matters

`docs/CURRENT_FRONT.md` names SD-018 as *the* gate on the v3 critical path — "buildable now… still un-owned". V3-EXQ-978 is the owed validation of the SD-018 amend (`ree-v3 028a625e09`, 2026-09-02). It nulled, on a **fully green 8/8 precondition gate**. This is a scored scientific result, not a readiness failure.

## 2. Facts

- **All 8 preconditions PASSED.** No red arms, no vacuous arms. `field_loss_off::zworld_encoder_trained_in_p0` measured 0.28158509731292725 against a 1e-06 threshold.
- **The loss was applied and demonstrably trained.** `used_resource_field_head` true 3/3 at weight 0.5; P0a held-out field r² 0.678 / 0.627 / 0.653; `n_latent_stack_changed` 7 (OFF) → 9 (ON), the +2 being the head's own parameters.
- **z_world did not move.** Δ sense-path decode r² −0.00063, Δ encoder-path r² +0.00038, Δ participation-ratio +0.0029 — all two to three orders below the within-arm seed spread (~0.099 r², ~1.61 PR) and sign-inconsistent across seeds.
- **Criteria.** `C_on_clears_floor` (load-bearing) **FAILED**, 0/3 seeds (0.30 / 0.30 / 0.25 vs a 1.0 floor). `C_off_subfloor_replication` PASSED. `C_decode_lift` failed on margin only (−0.00063 vs +0.05) while its absolute conjunct `r_on > 0` passed at 0.7093.
- **The bed is weak.** Both trained arms score at or below the random-walk anchor on every seed: OFF 0.0 / 0.25 / 0.55, ON 0.3 / 0.3 / 0.25, against an anchor of 0.85–1.05. ON-arm `survival_horizon` is 25.35 / 200.0 / 97.15 with `death_rate` 0.95 / 0.0 / 0.55.
- **The behavioural DV is quantised** at 0.05 per resource event; cells produced 0–11 events; the entire arm-mean difference (+0.0167) is one third of a single event.

## 3. Claim layer — both tags are peripheral

This run validates SD-018's encoder supervision. It does not exercise MECH-457's actor-critic substrate, nor INV-088's evaluator-bounded-by-z_world relation. MECH-457 and ARC-065 appear in SD-018's `unblocks_claims`, so the tags are **downstream-beneficiary tags**. INV-088's own stated re-check condition is gated on a *different* substrate route (SD-e1-rollout-consistency-training ITEM 2).

Both are recorded `non_contributory` with `epistemic_category: standard`, and both carry `recommended_epistemic_category_per_claim` so the re-derive-brake counter does not increment either claim's hit count from this run.

## 4. The routing finding

The driver's **own pre-registered null table** says: read the OFF arm's ABSOLUTE r² first — if OFF already decodes well, the null points at the consumer (shape b); only if BOTH arms decode poorly is the result a statement about the P0a training recipe.

**Measured OFF r²: 0.70991 sense-path, 0.85838 encoder-path.** Both arms decode the resource field well.

The emitted label nonetheless reads *"Re-run at another weight before concluding"*, because the code's label ladder never consults `r_off`. **The label contradicts the driver's own pre-registration and must not drive the routing.** The manipulation was also a ~1.5x *reweighting*, not supervision-vs-none: `reconstruction_weight = 10.0` already supervises the field at 10/250 per element and the ON leg adds only 0.5/25 — which is exactly why the absolute OFF-arm r² is the load-bearing read.

Corroborating, and not in the manifest: in the fishtank log the ON-arm head's argmax **varies across 17 of 25 cells on the encoder path** (9.28% match to truth vs 4.0% uniform / 23.71% majority-cell) but is **constant at cell 6 across all 97 sense-time steps**, with the OFF arm constant on both paths — the red-team F7 signature the author said would route a null to shape (b) rather than back to the P0a recipe. (Seed 42 only, unequal samples.)

## 5. But "not the encoder" is not "the consumer"

A linear probe recovering the field at r² 0.71–0.86 shows the information is **present**. It does not show it is in a geometry a policy can **use** under the actual learning dynamics.

The user's own thought document, written against this run (`docs/thoughts/2026-09-03_temporary_coordinated_representational_transformations.md`, §8), enumerates three readings and states verbatim: **"V3-EXQ-978 does not distinguish B from C."**

- **A. Information loss** — *weakened* by the OFF-arm decode.
- **B. Consumer/readout/learning failure** — the information is usable; the consumer failed to learn the mapping. Recorded there as "the most important simple alternative", which "should be tested before introducing richer architecture."
- **C. Representational mismatch** — the information is recoverable but the geometry does not make the required relationships accessible under the actual learning dynamics.

SD-018's pre-declared fallback — shape (b), side-channelling the raw field past z_world — **presupposes B.** If C holds it may well raise the score while telling us nothing about the actual constraint, banking a confident-but-wrong localisation. That is the failure GOV-FANOUT-1 exists to prevent.

## 6. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | untested (both tags) | SD-018 validation, not a test of either claim's mechanism |
| Biological reference | clear | auxiliary supervision of a shared sensory representation; not the failure locus |
| Prerequisites | present | all 8 preconditions passed |
| Implementation | complete | head trained; P0a field r² 0.63–0.68 |
| Environment | too sparse | both arms at/below the random-walk anchor |
| Measurement | under-instrumented | arm difference = ⅓ of one 0.05 DV quantum |
| Integration | coupled but unstable, **locus not yet identified** | decodable ≠ usable |
| Scale | likely insufficient on 2 of 3 seeds | ON death_rate 0.95 / 0.0 / 0.55 |

**Failure location (GOV-FAILLOC-1): MIXED — explicitly NOT chargeable to REE.** The head is complete and trained, but the DV was sub-quantum for the observed effect and both arms foraged below a random walk, so neither measurement nor environment independently reads adequate.

## 7. Routing — discriminate before building

**`/queue-experiment`**, carrying a GOV-FANOUT-1 `fanout_recommendation`:

1. **The discriminator (readout axis).** Freeze z_world exactly as this run left it and behaviour-clone the `local_view_greedy` oracle (which scores 45.75 on this same field) from the frozen latent. Declared null: the adapter cannot reproduce oracle actions above a pre-registered floor. **Cannot reproduce → H-C. Can reproduce → H-B.**
2. **H-C corroborator (representation axis), queue only if the adapter fails.** Apply a transformation preserving approximately the same recoverable information while rotating/reweighting the geometry; test whether competence tracks decision-relevant separability rather than global decode score.

**Why supervised and not another PPO run.** The frozen-latent reader has already been run twice with a PPO reader — V3-EXQ-948 `ppo_ree_latent` 0.5, V3-EXQ-978 OFF 0.267, both 0/3 against floor. Both failures are confounded with RL credit-assignment difficulty. A behaviour-clone removes exactly that confound, which is what makes this a discriminator rather than a third repetition. It is also strictly cheaper than shape (b): no `ree_core` change at all, hence no contract-gate exposure.

**Re-derive brake: FIRED.** MECH-457 carries 13 prior ceiling readings, INV-088 carries 2 — both at or past the threshold of 2. A same-claim lettered re-run (exactly what the emitted label proposes) is **refused**, independently corroborated by the driver's own null table. The brake normally routes to `/implement-substrate`; here the bottleneck is a *discrimination* rather than one unambiguous build, so per GOV-FANOUT-1 the probe precedes any build. A redesign under a new EXQ number testing a different question is explicitly permitted by the brake.

**Substrate:** `amend` SD-018 — record the failure_record item and move `amend_status` off "AWAITING VALIDATION" to validated-negative-for-shape-(a). **Do not promote shape (b) to the next build on this result alone.**

## 8. Ledger (Step 9b)

Registered a **new question**, `zworld_actor_adequacy_locus`, with H-B and H-C pre-registered alive (Mode A). `competence_floor` matches this run's claims exactly but is **CLOSED TO FURTHER FAN-OUT**; its restriction directs precisely this case to open its own qid, no exception applies, and the restriction was surfaced verbatim at the Step 8 gate. Integrity audit after the append: **a=0 b=0 c=0 d=0**, `competence_floor` reads ACKNOWLEDGED (not grown).

Related: `conversion_ceiling_root`'s `H-observation-interface` is already **confirmed** — "the REE latent is not a foraging-adequate representation for an external actor" — on V3-EXQ-813 + V3-EXQ-948. This new qid refines that confirmed leg by asking *why*, and exists because the confirmation was obtained with a PPO actor that cannot separate B from C.

## 9. Claim-rotation observation (for GOV-ROTATE-1)

`docs/thoughts/2026-09-03_claim_rotation_dual_view_claim_matrix.md` §9 asks: *"Does rotating a stalled claim produce a clearer, smaller or more discriminating next experiment?"* This autopsy is its first held-out trial.

- **Architectural framing's next step:** SD-018 shape (b) — a substrate build; presupposes H-B; does not discriminate.
- **Transformation framing's next step:** freeze z_world, behaviour-clone the oracle — a probe; no substrate change; discriminates on its declared null.

**Verdict: yes on all three counts for this case.** Smaller, cheaper, and more discriminating; it also converted the node from `complicated (buildable)` to `complex (probe-gated)`, the direction CLAUDE.md's debt vocabulary prefers.

**Caveat, stated because it matters:** N=1 and not blind — the same document supplied both the rotation and the probe, so this trial cannot separate "rotation helps" from "this author's next idea was good." Recorded as one data point, not as support for the general rule. This autopsy does not register GOV-ROTATE-1 and touched no claim.

## 10. Read-across, not adjudicated

**Governance discrepancy.** `claims.yaml` records SD-e1-rollout-consistency-training ITEM 2 as *pending* — it is INV-088's stated re-check gate — while V3-EXQ-978's queue note reports `ree-v3/CLAUDE.md` recording that same item as *IMPLEMENTED 2026-09-01*. One is stale, and it matters because INV-088's re-check is keyed to it. Recommend a `governance_flag`, not an autopsy verdict.

## 11. Red-team pass

Cross-model adversarial review (Fable). Verdict on this artifact: **CONFIRMED** — the docstring null table, the label ladder's failure to consult `r_off`, the recomputed OFF r² (0.70991 / 0.85838) and the brake counts all verified. Four hygiene items were corrected: the trained-arm competence range (0.0–0.55, not 0.25–0.55), the ON-arm survival figures, an incomplete `prior_substrate_ceiling_autopsies` list now marked as a partial sample, and a non-schema `route_to` string.
