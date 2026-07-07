# Failure Autopsy -- V3-EXQ-714 (FULLSTACK selection+valuation conversion falsifier)

- **Generated:** 2026-07-07T16:37:57Z
- **Scope:** single
- **Status:** confirmed (user gate 2026-07-07: "Confirm as recommended")
- **Run:** `v3_exq_714_fullstack_selection_valuation_conversion_falsifier_20260706T143256Z_v3`
- **Queue:** V3-EXQ-714 (experiment_purpose=evidence; supersedes none -- new composite number)
- **Claims:** ARC-062 (rule-apprehension architectural slot, weak reading), MECH-309 (monomodal policy collapse is the no-rule-layer equilibrium)
- **Outcome:** FAIL; self-routed `substrate_not_ready_requeue`; `evidence_direction: non_contributory` (per-claim ARC-062 / MECH-309 both non_contributory)

---

## 1. Facts (no interpretation)

The falsifier sweeps exactly one variable -- `use_candidate_rule_field` (ARM_OFF = legacy collapsed rule_state; ARM_ON = matured differentiated CRF). Everything else -- MECH-448 F->eligibility demotion, MECH-449 Go/No-Go, dACC perseveration, and the P3 OFC devaluation valuation face -- is a matched-stack constant on both arms. Phases P0 (200 ep, e2/SD-056) -> P1 (90 ep, encoder frozen, lateral_pfc bias head AND OFC devaluation head trained) -> P2 (60 ep, all frozen, OFC viability injected). Primary DV = `committed_class_entropy_nats` (C2 falsifier).

**Which criterion failed, and its category:** the C2 falsifier was **never scored**. Two C1 **readiness / non-vacuity** gates failed, forcing the pre-registered `substrate_not_ready_requeue` route:

- **C1b `gapa_consumed_summary_divergence_both_arms`** (readiness/non-vacuity): measured `0.004163` vs floor `0.05`; non-vacuous on only **1 of 3 seeds per arm**.
- **C1g `ofc_valuation_face_live_and_nonvacuous_both_arms`** (readiness/non-vacuity): OFC head trained (delta 0.80 OFF / 1.00 ON, >> `1e-3`) but the differentiated devalued **RANGE** measured `0.000701` vs floor `0.05`; non-vacuous on only **seed 44**.

C1 gates that **passed** non-degenerately: C1a class-axis exercisable (`frac_pre_ge2=1.0`), C1c ARM_ON CRF matured (`crf_frac_active=0.989`, 12-16 rules minted), C1d propagation non-vacuity (`0.043 > 1e-3`, 2/3), C1e MECH-448 demotion live+excluding (both arms 3/3), C1f MECH-449 Go/No-Go live+suppressing (both arms 3/3). So the **selection** stack (demotion, Go/No-Go, CRF maturation, propagation) is fully live; the two gates that fail are both **divergence / valuation-range** gates that depend on the summaries actually diverging.

**The C2 statistic (computed, not load-bearing given C1 fail):** no lift on any seed. Paired ARM_ON - ARM_OFF committed-class entropy: seed 42 = 0.0, seed 43 = -0.001, seed 44 = -0.087; ON mean 1.0265 <= OFF mean 1.0559; 0/3 seeds cleared the 0.05-nat margin.

**Key fact:** GAP-A consumed-summary divergence and OFC devalued-range were non-vacuous on **only seed 44** in both arms -- and the run used the **full P0=200**, not the toy P0=8 config the queue note flagged as the starvation risk. The prediction ("satisfiable at full P0=200") did not hold.

## 2. Claim-layer mapping

- **ARC-062** -- `architectural_commitment`, `candidate`, `v3_pending: true`, `epistemic_category: substrate_ceiling`; depends_on MECH-309, SD-054, MECH-269, SD-029. No lit/exp numeric confidence field. Prior evidence: a long non_contributory / substrate_ceiling chain (543e/h/i/k/l, 654a/f/g/i/j, 690), re-derive brake FIRED at 654j (19th ARC-062); claim consistently UNWEAKENED, zero reliable contributory PASS.
- **MECH-309** -- `mechanism_hypothesis`, `candidate`, `v3_pending: true`, `epistemic_category: substrate_ceiling`; depends_on SD-054, SD-029, MECH-256, MECH-269, ARC-062, ARC-063, ARC-077. One narrow contributory support (543l, strong-reading collapse survival, single-pathway / narrow_supports_flag); 654 lineage all non_contributory; brake FIRED at 654j (18th MECH-309).

**Did the test let the claims express themselves?** No. The falsifier reads a marginal-committed-diversity DV that only becomes interpretable once the differentiated rule field produces a divergent, valuation-differentiated policy. The readiness abort means the substrate never presented that condition on 2/3 seeds -- so nothing was falsified. This is the pre-registered NO-weakens branch; both claims stay unweakened.

## 3. Biological-reference triage

- **Closest mechanism:** a rule-apprehension / policy-mode-proposing layer (PFC/BG gated-policy architecture) feeding differentiated committed modes to the updaters. The dependency it presupposes is a substrate that can *hold divergent policy modes long enough to be valued differently* -- which in REE requires the GAP-A consumed-summary divergence to survive selection.
- **Is it a formal import?** Partially -- MECH-309 is a claim about the *equilibrium* of a parametric policy (a dynamical-systems / optimisation statement). But the failure is not a formal-definition divergence; it is a substrate-expression failure.
- **Does the failure match a missing-dependency signature?** Yes -- the regime-scoping of GAP-A divergence (survives only on seed 44) is the exact fingerprint of the **F-dominance conversion ceiling (MECH-439)**: the F-driven natural commit monopolises selection, so the differentiated summaries only diverge in the rare regime where F does not dominate. This is the same ceiling that blocks the whole conversion campaign and the MECH-445 de-commit cluster.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | test could not let the claim express (readiness abort); NO-weakens branch fired as pre-registered |
| Biological reference | partial | rule-apprehension / gated-policy layer; failure matches the F-dominance missing-dependency signature |
| Prerequisites | missing | GAP-A consumed-summary divergence that survives moderate F (the conversion-ceiling root); currently regime-scoped to 1/3 seeds |
| Implementation | complete (selection stack) | demotion, Go/No-Go, CRF maturation, OFC head training all live; the composite assembled correctly |
| Environment | adequate-but-ceiling-limited | scaffolded_sd054_onboarding full curriculum; the pressure exists but the F-dominance ceiling suppresses summary divergence |
| Measurement | adequate | C1b/C1g are correct non-vacuity guards; they did their job (aborted rather than scoring a starved DV) |
| Integration | partially coupled | the valuation face (OFC range) is downstream of GAP-A divergence; when divergence is starved the whole valuation face is inert |
| Scale | adequate | full P0=200; the blocker is regime, not budget -- confirmed the starvation is NOT a toy-scale artifact |

**Recommended `epistemic_category`: substrate_ceiling.** The FULLSTACK selection+valuation face hits the conversion ceiling (MECH-439 / GAP-A-divergence starvation) at the **readiness layer** -- it cannot even reach the C2 falsifier because the differentiated summaries do not survive selection on 2/3 seeds.

## 5. Re-derive brake (MOVE-3)

**FIRED.** ARC-062 and MECH-309 each already carry a deep substrate_ceiling autopsy chain (543/654 lineage), with the brake previously fired at 654j (19th ARC-062 / 18th MECH-309). V3-EXQ-714 was queued with "brake RELEASED" asserted on the grounds that it was a *new composite question* with the upstream substrate BUILT+VALIDATED. That release did not hold: the composite did not escape the ceiling -- it hit the same GAP-A-divergence starvation wall at readiness. This is the 20th ARC-062 / 19th MECH-309 substrate-ceiling reading.

**REFUSAL:** do **not** re-queue another selection+valuation fullstack (or another lettered conversion falsifier) against the current substrate. Another letter would re-derive the same GAP-A-starvation readiness abort. A redesign that tests a *different* mechanism (new EXQ number, different claim_ids) or a commitment-free read is still allowed; another fullstack circling the conversion ceiling is not.

**Route:** `/implement-substrate` on `f_dominance_conversion_ceiling` -- specifically the GAP-A-divergence-survival / summary-differentiation face (a lever that lets differentiated consumed summaries survive moderate F, so the OFC valuation face has non-vacuous material to value). The entry already lists ARC-062 / MECH-309 / MECH-439 in `unblocks_claims`; this autopsy adds a failure record for the readiness-layer manifestation.

## 6. Campaign-level finding

This is the load-bearing output. The conversion-ceiling campaign's route of record after `failure_autopsy_V3-EXQ-713_2026-07-05` (arbitration-reweighting route EXHAUSTED) was the **selection-face + valuation-face** stack. V3-EXQ-714 assembled the full selection+valuation stack and found it **cannot clear the conversion ceiling at the readiness layer** -- the GAP-A summary divergence that both the C2 falsifier and the OFC valuation face require is itself starved by F-dominance on 2/3 seeds. The conversion ceiling (MECH-439 / GAP-A-divergence survival) is therefore **upstream of every face the campaign has tried** (arbitration -- exhausted; selection -- 654 lineage; valuation -- 485m; fullstack -- 714). The campaign's single owed build is the GAP-A-divergence-survival substrate; no further face-composition experiment will move it.

## 7. Draft `evidence_quality_note` (governance to write; NOT written here)

> V3-EXQ-714 (confirmed failure_autopsy_V3-EXQ-714_2026-07-07; FULLSTACK selection+valuation conversion falsifier, new composite) -> non_contributory + pending_retest_after_substrate (status UNCHANGED: candidate / v3_pending). Self-routed substrate_not_ready_requeue: C1b GAP-A consumed-summary divergence 0.004 < 0.05 floor (non-vacuous 1/3 seeds) and C1g OFC devalued-range 0.0007 < 0.05 floor (non-vacuous seed 44 only) FAILED at FULL P0=200 -- the C2 committed-class-entropy falsifier was never scored. NOT a falsification (pre-registered NO-weakens map). The selection stack is fully live (C1c/C1d/C1e/C1f all pass) but the differentiated summaries do not survive selection on 2/3 seeds -- the F-dominance conversion ceiling (MECH-439) resurfacing at the readiness layer, the same regime-scoping fingerprint as the MECH-445 de-commit cluster. 20th ARC-062 / 19th MECH-309 substrate-ceiling reading; RE-DERIVE BRAKE FIRED. Same-face fullstack re-queue REFUSED. CAMPAIGN FINDING: the full selection+valuation stack cannot clear the conversion ceiling at readiness; the ceiling (GAP-A-divergence survival) is upstream of every campaign face (arbitration exhausted 713, selection 654, valuation 485m, fullstack 714). Release condition: f_dominance_conversion_ceiling GAP-A-divergence-survival face -- differentiated consumed summaries that survive moderate F.

## 8. Routing summary

- **ARC-062:** non_contributory; status unchanged; pending_retest_after_substrate; brake fired; refuse fullstack re-queue.
- **MECH-309:** non_contributory; status unchanged; pending_retest_after_substrate; brake fired; refuse fullstack re-queue.
- **Substrate:** amend `f_dominance_conversion_ceiling` with the 714 readiness-layer failure record + GAP-A-divergence-survival build hint. `/implement-substrate` owns the build.
