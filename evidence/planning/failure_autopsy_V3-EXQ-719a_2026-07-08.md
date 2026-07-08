# Failure Autopsy — V3-EXQ-719a (conversion-ceiling dissociation diagnostic)

- **Generated (UTC):** 2026-07-08T22:58:03Z
- **Run:** `v3_exq_719a_conversion_ceiling_dissociation_diagnostic_20260708T215846Z_v3`
- **Queue id:** V3-EXQ-719a (supersedes V3-EXQ-719; tick-budget P2 re-queue)
- **Claims:** ARC-062, MECH-309 (both `candidate / v3_pending / substrate_ceiling / ceiling_decision: deferred / pending_retest_after_substrate`)
- **Outcome:** FAIL, `evidence_direction: non_contributory` (experiment_purpose = diagnostic; excluded from governance scoring)
- **Self-routed label:** `substrate_not_ready_requeue` — **adjudicated a MISLABEL** (see below)
- **Scope:** single (but reframes the ARC-062/MECH-309 downstream-behavioural-retest cluster)
- **Status:** confirmed (user-gated 2026-07-08)

---

## 1. Facts (no interpretation)

719a is the tick-budget re-queue of 719. 719 self-aborted on its own MI-estimability readiness gate (951 P2 ticks/seed vs a 3000 floor; agent died early on seeds 42/44; 1/3 seeds estimable). 719a's one substantive change: P2 is tick-budget-driven (target 6000 committed P2 ticks OR 400-episode cap) so every seed clears the floor. Everything else identical to 714's all-ON config (sleep OFF).

**Phase structure:** P0 = 200-ep encoder/E2 warmup (SD-056 online contrastive, CRF matures); P1 = 90-ep frozen-encoder outcome-coupled REINFORCE on the lateral_pfc bias head (reward = harm_signal); P2 = **all-frozen** tick-budgeted eval/logging (OFC devaluation injected into the Go/No-Go gate exactly as 714).

**Readiness (all MET this time — the 719→719a fix worked):**

| Precondition | Measured | Threshold | Met |
|---|---|---|---|
| mi_estimable_sufficient_ticks | 6005 (min over seeds) | 3000 | ✅ |
| mi_estimable_enough_occupied_state_bins | 6 (min) | 4 | ✅ |
| readiness_majority_seeds_mi_estimable | 3/3 | 2/3 | ✅ |

**Per-seed (all 3 seeds):**

| seed | P2 ticks | occupied bins | marginal H (nats) | raw MI > shuffle p95 | debiased MI | resources/ep | competence≥floor |
|---|---|---|---|---|---|---|---|
| 42 | 6008 | 10 | 1.406 | ✅ | 0.0098 | 0.065 | ❌ |
| 43 | 6076 | 6 | 0.693 | ✅ | 0.0036 | 0.000 | ❌ |
| 44 | 6005 | 10 | 1.055 | ✅ | 0.0511 | 0.455 | ❌ |

Thresholds: `MI_DEBIASED_FLOOR=0.05`, `COMPETENCE_RESOURCE_FLOOR=1.0` resources/ep, majority = 2/3.

**Gate roll-up:** `raw_mi_above_shuffle_p95_majority = TRUE` (3/3); `mi_debiased_supra_floor_majority = FALSE` (1/3); `competence_supra_random_majority = FALSE` (0/3); `genuine_collapse_majority = FALSE` (0/3, because "genuine collapse" requires raw MI *not* above null and every seed *is* above null). Load-bearing criterion `state_drives_commitment_mi_debiased_and_above_null = FALSE`.

**Which criterion failed:** the load-bearing *discrimination* criterion. Neither the `decisive_state_appropriate_commitment` gate (needs debiased-MI + real-coupling + competence, all majority) nor the `genuine_monomodal_collapse` gate (needs debiased-MI≈0 AND raw MI *not* above null) is satisfied → the code falls to its `else` branch (line 1203) and emits `substrate_not_ready_requeue`.

---

## 2. The self-route is a mislabel

The pre-registered grid (`interpretation.preconditions` + script docstring lines 79–104) defines `substrate_not_ready_requeue` as the **under-sampled** case — "total P2 ticks below floor or occupied bins below floor → MI under-sampled → re-queue at a larger P2 budget." That is the 719 case.

Here sampling is fully adequate (all three readiness gates met). The label fires from the code's `else` branch — the grid's separately-documented **"EVIDENCE AGAINST either conclusion"** outcome — which reuses the *same string*. The two situations are semantically opposite: one says "collect more data," the other says "data is adequate and supports neither branch." A larger P2 budget will not change this result.

This is the structural mirror of the V3-EXQ-642 incident (a `substrate_ceiling` *verdict* self-routed on an *untrained* substrate): the self-routed label names the wrong cause. Here it points at sampling when the real blocker is behavioural competence. **The label is a hypothesis; adjudication overrides it.** (Instrumentation follow-up noted in §7: the `else` branch should carry its own label, e.g. `dissociation_undefined_low_competence`, and competence should be a *readiness precondition*, not a parallel discrimination criterion.)

---

## 3. Claim-layer mapping

Both ARC-062 (architectural_commitment) and MECH-309 (mechanism_hypothesis) are `candidate`, `v3_pending`, `implementation_phase: v3`, `epistemic_category: substrate_ceiling`, `ceiling_decision: deferred`, carrying `pending_retest_after_substrate`. The conversion ceiling is owned by the `f_dominance_conversion_ceiling` substrate entry (unblocks MECH-309/ARC-062/ARC-063 + the MECH-448/449 levers).

**Did the experiment test the claim under conditions where it could express itself? No.** The dissociation question ("is committed action state-appropriate, or genuinely collapsed?") is only *meaningful* when the agent competently commits to *something*. With competence below floor on 0/3 seeds, the committed-action stream is diffuse flailing and neither branch is licensed. A diagnostic that cannot license either branch **falsifies nothing**. Both claims stay UNWEAKENED.

---

## 4. Biological-reference triage

- **Closest reference mechanism:** basal-ganglia committed action-selection — the conversion of graded candidate value into a decisive, *state-appropriate* committed action (cortico-striatal Go/No-Go arbitration; the ARC-062/MECH-309 target).
- **Dependencies in real brains:** competent action-selection presupposes a *trained* sensorimotor/striatal policy. You cannot dissociate "decisive vs collapsed commitment" in an animal that has not yet learned the task — the readout is undefined before behavioural competence exists.
- **Faithful translation vs formal import:** the *mechanism* (BG arbitration) is a faithful biological target, not a formal-definition import — so this is not an SD-003-style lit gap. The failure is at the **prerequisite/training** layer, not the mechanism layer.
- **Missing-dependency signature:** competence ≈ 0 after a thin P1 regime (90-ep bias-head-only REINFORCE on a frozen encoder) resembles exactly what you'd see if the cortico-BG policy were **under-trained** — a developmental/training prerequisite absent, not the arbitration mechanism being wrong. The FAIL is a **discovered prerequisite**, not a falsification.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | test could not let either branch express; claim untouched |
| Biological reference | clear | BG committed action-selection; faithful target, not a formal import |
| Developmental / dependency prerequisites | **missing** | competent committed foraging is an unstated prerequisite of the dissociation; absent here |
| Implementation completeness | partial | all-ON mechanisms wired, but the **training regime** (frozen encoder + 90-ep bias-head-only REINFORCE) is the symbol of training, not enough to produce competent behaviour |
| Environment adequacy | partial/unknown | short P2 episodes (~15 ticks: 6005 ticks / ~400 eps) give little room to forage; reef-enabled CausalGridWorldV2 config may differ from the GAP-A substrate where MECH-448/449 was validated |
| Measurement adequacy | under-instrumented | no **competence readiness gate**; the `else` branch overloads the under-sampled label onto a competence-blocked case |
| Integration adequacy | coupled-but-possibly-unstable | all-ON composite does not convert into competent committed behaviour — live alternative to the training-budget reading |
| Scale / capacity | likely insufficient | 90-ep bias-head-only REINFORCE is a thin budget for competent foraging |

**Dominant diagnosis (recommended `epistemic_category`):** `substrate_ceiling` — specifically a **behavioural-competence / training-regime** ceiling in the integrated all-ON agent. Consistent with the 20 prior ARC-062 autopsies, but 719a adds a **first-time-measured mechanism**: the DV the campaign reads as "collapse" is, in the integrated diagnostic, actually **diffuse, state-blind, incompetent commitment** (moderate-to-high marginal entropy, MI≈0, competence≈0) — *not* literal monomodal collapse.

---

## 6. What 719a rules in / out (hand-off content)

- **RULED OUT — branch B (metric-artifact reframe / `decisive_state_appropriate_commitment`).** There is no working state-conditioned policy being misread as collapsed: debiased MI clears the floor on only 1/3 seeds; competence on 0/3. The "it's just a marginal-entropy artifact" escape hatch is **closed**.
- **NOT CLEANLY branch A (`genuine_monomodal_collapse`).** Raw MI is above the shuffle null on 3/3 seeds (committed action is *not* statistically independent of state) and marginal entropy is not low. The pathology, if real, does **not** present as textbook monomodal collapse in this integrated setup.
- **Reframes the downstream-retest wall.** 654h / 485i / 625e / 460h / 460i all self-routing `substrate_not_ready` is at least partly because the all-ON agent is not competent enough to *produce* meaningful committed behaviour to measure. The missing substrate is **not** another selection lever (MECH-448/449 are built and lifted the selection face on GAP-A) — it is whatever makes the fully-integrated agent competently commit.

---

## 7. Learning extracted + repair pathway

**Learning:**
1. The integrated all-ON agent forages at 0.065 / 0.0 / 0.455 resources/ep in P2 — genuinely below the competence floor (instrumentation confirmed: the resource counter fires nonzero on 2/3 seeds, so this is real behaviour, not a mis-wire).
2. The conversion-ceiling behavioural DV is undefined until competence exists; the recurring `substrate_not_ready` self-routes across the retest cluster share this root.
3. The `substrate_not_ready_requeue` self-route string is overloaded across two opposite cases (under-sampled vs competence-blocked) — a diagnostic-instrumentation debt.
4. MECH-309's "collapse" framing may be slightly mis-specified: the observed failure is "failure to convert candidate diversity into *competent state-appropriate* commitment," which can present as high-but-useless entropy, not only low entropy. Recorded as a granularity note (the coarse conversion ceiling was **already** decomposed via `f_dominance_conversion_ceiling` / MECH-448/449 — no new `/claim-synthesis` spawned; this refinement feeds the substrate build).

**Repair pathway (user-gated 2026-07-08):**
- **Immediate next step — competence-localization diagnostic (`/queue-experiment`, brake-EXEMPT).** Ask a *different question* — WHY is the all-ON agent incompetent: thin P1 training budget vs frozen-encoder-in-P1 vs all-ON mechanism interference (ablate mechanism groups / vary P1 budget / unfreeze encoder). This is a new measurement, not another letter circling the ceiling, so it is not the re-test the brake forbids. It localizes the lever before any speculative build.
- **Eventual build — `/implement-substrate`** on the localized competence/training-regime gap (the re-derive-brake-mandated end state). Do NOT build blind before localization.
- **Substrate queue — AMEND** `f_dominance_conversion_ceiling` with the 719a competence failure record (see JSON `recommended_substrate_queue_entry`). No new SD entry: this is the owning entry for the conversion ceiling and already unblocks ARC-062/MECH-309.

**Re-derive brake — FIRED.** 21st `substrate_ceiling`/`non_contributory` autopsy tagging ARC-062 (20th for MECH-309). **Refused:** V3-EXQ-722 (parked SELECTION-face falsifier) and any 719b — both are same-claim behavioural re-tests that would hit the identical competence wall. The competence-localization diagnostic is the exempt exception (different question).

**V3-EXQ-722 disposition (user-gated):** keep parked, **re-gate on the competence substrate** (not moot — branch B is rejected, so the falsifier retains a target — but blocked on competence). The `trusting-elgamal-f8c2e8` claim's resume rule resolves to its case (c) inconclusive, with the added constraint that the SELECTION-face DV is undefined until competence exists.

---

## 8. Draft `evidence_quality_note` (governance writes this VERBATIM to ARC-062 and MECH-309; status UNCHANGED)

> 2026-07-08 (failure_autopsy_V3-EXQ-719a_2026-07-08 CONFIRMED -> non_contributory; claim UNWEAKENED). V3-EXQ-719a (tick-budget re-queue of 719; diagnostic, PROMOTES/DEMOTES NOTHING) fixed 719's sampling starvation — all MI-estimability readiness gates now MET (6005 ticks/seed, 6-10 bins, 3/3 seeds estimable). Result: the dissociation is UNDEFINED, and the self-routed `substrate_not_ready_requeue` label is a MISLABEL (readiness is met; the code's else-branch reused the under-sampled string for the pre-registered "evidence against either conclusion" case — more ticks will not change it). Branch B (decisive_state_appropriate_commitment / metric-artifact reframe) REJECTED: debiased MI clears the 0.05 floor on 1/3 seeds, competence below the 1.0 resources/ep floor on 0/3. Branch A (genuine_monomodal_collapse) NOT cleanly supported: raw MI above the shuffle null on 3/3 seeds (committed action not state-independent) and marginal committed-class entropy moderate-to-high (0.69-1.41 nats), not low. First direct competence measurement: the integrated all-ON agent forages at 0.065/0.0/0.455 resources/ep — genuinely below floor (counter verified firing). Dominant diagnosis substrate_ceiling: a behavioural-competence / training-regime ceiling (thin P1 = 90-ep bias-head-only REINFORCE on a frozen encoder; all-ON mechanism interference a live alternative), NOT a further selection lever (MECH-448/449 built + selection-face lifted on GAP-A). This reframes the downstream behavioural-retest wall (654h/485i/625e/460h/460i substrate_not_ready) as the same competence root. pending_retest_after_substrate retained; ceiling_decision stays deferred. Re-derive brake FIRED (21st/20th) -> competence-localization diagnostic first (brake-exempt: different question), then /implement-substrate on the localized gap; same-claim behavioural re-tests (V3-EXQ-722, 719b) REFUSED.
