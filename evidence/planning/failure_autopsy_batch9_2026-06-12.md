# Failure Autopsy — Batch of 9 unreviewed FAILs (2026-06-12)

- **Generated (UTC):** 2026-06-12T06:20:20Z
- **Scope:** cluster (9 targets, two convergent structural patterns + per-target diagnoses)
- **Status:** confirmed (user-adjudicated Step-8, 2026-06-12)
- **Skill:** `/failure-autopsy` — analysis + handoff only. No claims.yaml / manifest / review_tracker / substrate_queue edits made here; governance / queue-experiment / claim-synthesis apply the routing below.

Source: `evidence/experiments/pending_review.md` (generated 2026-06-12T01:47Z) listed 9 unreviewed FAIL manifests. All 9 ran to completion (no ERROR/UNKNOWN), so all are autopsy-eligible.

---

## Triage summary

| # | Queue | Claim(s) | Manifest dir | Direction (as landed) | Verdict | Routing |
|---|-------|----------|------|-----------|---------|---------|
| 1 | V3-EXQ-569g | ARC-065 | r1a_entropy_only_artefact | weakens | **genuine adverse on validated substrate** | `/claim-synthesis` (granularity debt) |
| 2 | V3-EXQ-590b | MECH-314a | mech314a_no_exploratory_benefit | does_not_support | **genuine adverse on validated substrate** | `/claim-synthesis` (granularity debt) |
| 3 | V3-EXQ-485f | SD-033b, MECH-263 | sd033b_…signature_absent | weakens | **readiness-gate miscalibration (50x gap)** | `/queue-experiment` 485g (not a weakens) |
| 4 | V3-EXQ-670 | INV-048 | inv048_pharm_sleep | weakens | **degenerate** (harm_eval_head untrained) | reclassify non_contributory + `/queue-experiment` 670a |
| 5 | V3-EXQ-671 | MECH-025b | mech025b_precision_responsibility | mixed | **degenerate** (residue field inert) | reclassify non_contributory + `/queue-experiment` 671a |
| 6 | V3-EXQ-673 | MECH-171 | mech171_vicious_cycle_sleep | does_not_support | **degenerate + out-of-domain claim** | reclassify non_contributory + MECH-171 → `out_of_domain` + queue cleanup |
| 7 | V3-EXQ-666b | (none) | arc063_crf_…fracgate | non_contributory | **designed self-route (below floor)** | `/governance` mark-reviewed + substrate amend (ready stays FALSE) |
| 8 | V3-EXQ-603o | SD-059, MECH-358 | escape_affordance_bridge_redesign | non_contributory | **designed self-route (below floor)** | `/governance` mark-reviewed + substrate amend |
| 9 | V3-EXQ-514n | MECH-229 | sd049_phase2_object_bound_wl | non_contributory | **designed self-route (below floor)** | `/governance` mark-reviewed + substrate amend |

---

## Structural pattern 1 — "vacuous read on an unwritten/untrained channel" (non-degeneracy gap)

Targets **670 / 671 / 673**. Each is a FAIL whose adverse direction is an artifact of reading a discriminative DV off a channel that was never written or trained, with **no non-vacuity gate** in the script to catch it. The PASS/FAIL produced is a property of the test design, not evidence about the claim.

| Exp | DV read | Why it can't move | Fingerprint |
|---|---|---|---|
| 670 / INV-048 | `harm_discrimination` from `e3.harm_eval_head(randn prototypes)` | `run_sleep_cycle()` runs SWS + REM passes but **never trains `e3.harm_eval_head`** → output fixed by seed init | harm_discrimination **byte-identical across all 4 arms** (A=B=C=D); slot_diff A≡B, C≡D |
| 671 / MECH-025b | C1 precision↔residue correlation; C2 high/low precision residue ratio | `ResidueField.total_residue` never moves across 778 committed harm-events → residue_delta uniformly 0 | C1 **= 0.0** and C2 **= 0.0** exactly; "mixed" is only the 4/6 arithmetic (the 4 passes are health/sample preconditions C3–C6) |
| 673 / MECH-171 | slot_diversity, eval_harm, late_pred_loss across early/late disruption arms | sleep-compression knob doesn't propagate into the readouts | **ARM_A ≡ ARM_B ≡ ARM_C** on every metric; **`late_pred_loss ≡ 0.0`** all arms/seeds |

This is the exact failure mode the new `_experiment_lib.check_degeneracy()` / `non_degenerate` manifest net (landed 2026-06-11) was built to catch — but these three scripts predate or don't call it. Same family as V3-EXQ-514m (valence channel never written), V3-EXQ-642 (z_block on an untrained encoder), V3-EXQ-666a (count-gate cleared by differentiation alone).

**Biological-reference note (670):** the 4-arm design (normal / REM-suppressed ≈ antidepressants / SWS-suppressed ≈ benzodiazepines / no-sleep) is a *faithful* operationalisation of INV-048's phase-fidelity-vs-cause-agnostic prediction. The translation is sound; only the harm-attribution readout is wired to an untrained head. Fix = train the harm-VALUATION pathway in the sleep cycle (the `scaffold_train_harm_pathway` / 603k pattern from the Stage-H harm-pathway work) before measuring, then re-run as **670a**.

**Process defect (673):** ran **3× under one EXQ** (manifests 23:02Z / 03:22Z / 04:48Z, content-identical reruns; all three **untracked** in git). Queue entry **V3-EXQ-673 still `status: pending`** in `experiment_queue.json` (never retired). This is the forbidden same-EXQ silent-rerun anti-pattern — the three manifests must not multi-count; retire the queue entry.

**INV-048 standing:** NOT an invariant. Reclassified `invariant → derived_prediction` (prediction_domain `clinical_pharmacology`) on 2026-04-17. The sleep "offline phases are a mathematical necessity" capstone is **INV-049**, not INV-048. So "weakens on an invariant" is moot — but the manifest weakens is still vacuous and must not press the derived prediction.

---

## Structural pattern 2 — "validated modulatory substrate, but per-claim retests still fail in structurally-different ways" (granularity debt)

Targets **569g / 590b** (and 485f as a related-but-distinct sub-case). The `modulatory-bias-selection-authority` substrate is now `ready: true` (validated by `v3_exq_643a_modulatory_authority_validation`, 2026-06-07). These are the **first per-claim behavioural retests on that ready substrate**. All cleared their (strong) readiness gates — the channel demonstrably reaches and moves the E3 argmin — yet each returned an adverse direction, **and each failed in a structurally different way**:

| Exp | Claim | Readiness gate (cleared) | Adverse result | Failure signature |
|---|---|---|---|---|
| 569g | ARC-065 (GAP-A R1.b) | route_range **0.18** ≫ floor 0.01; C1 e2_world_forward divergent PASS 3/3 | selected-entropy ARM_1_E2WF **0.615 < ARM_2 matched-noise 0.704** | range reaches selection but **carves no extra diversity vs noise** (1/3 seeds strict-above) |
| 590b | MECH-314a | curiosity_bias_range 0.0123 ≫ floor 1e-4; H_pos range across gains **0.283** ≫ floor 0.05 | best nonzero arm H_pos **0.4188 < gain=0 control 0.4200** | authority moves behaviour but **every gain matches or degrades exploration** (no Goldilocks lift) |

**Why granularity debt, not demotion (user-confirmed Step-8):** ARC-065 has **≥4 prior autopsies** (643 → 604a-624a-630 → 614e → 569f-661-654a), MECH-314a **≥3** (604/605 → 604a-624a-630 → 648/gapA-cluster). Each circles the same coarse claim with a *different* failure signature. Pre-substrate, all routed to `implement-substrate` (build the modulatory-authority substrate). That substrate is now built and ready — **the substrate excuse is spent** — and the claims still fail, differently each time. That recurrence-with-varied-signature is the granularity-debt fingerprint: the coarse parents (ARC-065 "diversity is load-bearing"; MECH-314a "novelty Goldilocks buys exploration") are not falsified, they are *under-specified* — there is a finer mechanism (range-reaches-selection ≠ range-carves-behaviour; authority-moves-argmin ≠ signal-is-adaptive) the broad claims don't name. Parents keep their confidence (ARC-065 provisional exp_conf ~0.97, 46 supports; MECH-314a candidate_substrate_landed); the cluster goes to `/claim-synthesis` for proposal-first, lit-grounded decomposition into testable children.

**485f is a distinct sub-case (NOT this cluster, NOT a weakens).** Its readiness gate (`bias_range > 1e-3`) cleared *by a hair* (max 0.00898) but that is **~50× below** the 0.05 the behavioural DVs (devaluation_shift, between_context_tv) require. The readiness floor and the DV-significance floor are 50× apart, so "ready" did not certify a fair test — the OFC bias that cleared readiness still has no authority to move the selection softmax (devaluation_shift 5e-5…2.6e-4). The three 485e→485f fixes all took effect (ofc_bias_scale 0.5 defeated clamp-saturation; SD-056 contrastive lifted bank_zworld_spread off zero; absolute TV floor correctly caught the C2 vacuity), but the resulting range is still under-powered. SD-033b/MECH-263 have only **1 prior autopsy** (485e) → not yet a granularity-debt pattern. Route = **re-queue 485g** with the readiness floor aligned to the DV-significance floor (bias_range must reach ~0.05, not 1e-3), so a future FAIL is a fair falsification rather than an underpowered-channel artifact.

---

## Designed self-routes (governance, not deep autopsy)

All three fired their pre-registered non-vacuity gate below floor exactly as designed → `non_contributory` / `substrate_not_ready_requeue`. They carry no information against their claims; route to `/governance` mark-reviewed + substrate amend.

- **666b / ARC-063 CRF availability-maintenance** (claims=[]; supersedes 666a). Non-vacuity gate `e2ctx_full_pool_differentiated` fired below floor (ARM_1 differentiated **0/3**, max_pairwise_dist 0.000). **Load-bearing nuance: this does NOT support flipping `crf-availability-maintenance` ready=true.** Per-arm `crf_frac_maintained`: ARM_0 0.0 / ARM_1 **0.0 (0/3 differentiated)** / ARM_2 0.8125 (2/3 ≥0.625). ARM_2 cleared its gate in isolation, but ARM_1 regressed to a fully undifferentiated pool (vs 666a's 0.125–0.438), tripping non-vacuity and starving the isolating contrast. 666b's longer context-absent gap regime collapsed the ARM_1 baseline. **Amend** the substrate entry with the ARM_1-collapse record; **ready stays false**; re-gate (666c) needs a regime where ARM_1 still differentiates so the maintenance contrast is non-vacuous.
- **603o / SD-059 + MECH-358 escape-affordance bridge** (supersedes 603l). Gate `harm_landscape_discriminative_on_base` fired below floor (harm_eval_range 1/3 seeds < 0.667 floor) — the redesigned 603o env produced a flat harm landscape on 2/3 seeds. Blocked on the 603k harm-pathway-training substrate on the 603o env. Amend; route a successor that restores harm-landscape discriminability on the harder env.
- **514n / MECH-229 object-bound wanting≠liking** (successor to 514m). WL non-vacuity gate leg-2 (`run_bank_populated_two_tokens_differing_drive`) fired below floor (0.0 < 0.667); leg-1 positive control **passed** (instrument works). The SD-049 run-bank still doesn't populate ≥2 drive-differentiated tokens at consumption — the same bank-population substrate gap. Amend; this is a clean below-floor self-route, NOT a MECH-229 weakens.

---

## Four-layer diagnosis (dominant layer per target)

| Target | Dominant failing layer | Reading |
|---|---|---|
| 569g (ARC-065) | Claim alignment — coarse | Test fair, substrate ready; claim under-specified → granularity debt |
| 590b (MECH-314a) | Claim alignment — coarse | Test fair, authority operative; claim under-specified → granularity debt |
| 485f (SD-033b/MECH-263) | Measurement (readiness gate too loose) | 50× gap between readiness floor and DV floor → underpowered, re-queue |
| 670 (INV-048) | Implementation (untrained head) + Measurement (no non-vacuity gate) | Degenerate; faithful design, broken readout |
| 671 (MECH-025b) | Implementation (inert residue) + Measurement (no non-vacuity gate) | Degenerate; first run; residue substrate inert under committed harm |
| 673 (MECH-171) | Environment/Scale (out-of-domain) + Measurement (degenerate) | Clinical AD staging not instantiable in grid-world; readout collapsed |
| 666b / 603o / 514n | Prerequisites (substrate not ready) | Designed self-route below floor; substrate amend |

---

## Routing decisions (user-confirmed 2026-06-12)

1. **569g + 590b → `/claim-synthesis`.** Hand the ARC-065 + MECH-314a cluster for proposal-first decomposition. No demotion of the high-conf parents. Record the specific sub-hypothesis failures (569g R1.b entropy-lift-over-matched-noise; 590b Goldilocks-no-benefit) as the discrimination signal the synthesis works from.
2. **485f → `/queue-experiment` 485g.** Re-queue with readiness floor aligned to the 0.05 DV-significance floor (bias_range competitive with the selection softmax). NOT a weakens; SD-033b/MECH-263 stay candidate, no demotion. `/governance` reclassify the 485f manifest weakens → non_contributory (readiness-gate-miscalibration / measurement_test_design_defect), `pending_retest_after_substrate` retained.
3. **670 → reclassify non_contributory (degenerate) + `/queue-experiment` 670a.** Set `non_degenerate: false` (harm_discrimination arm-invariant; degeneracy_reason = harm_eval_head untrained by run_sleep_cycle). 670a trains the harm-VALUATION pathway in the sleep cycle + adds a non-vacuity gate (arms must produce distinct harm_discrimination before the verdict). INV-048 untouched (derived_prediction, no demotion).
4. **671 → reclassify non_contributory (degenerate) + `/queue-experiment` 671a.** Set `non_degenerate: false` (C1/C2 = 0.0 on an inert residue field). 671a adds a positive-control gate (residue must accumulate under committed harm before the precision↔residue correlation is read). MECH-025b untouched (first run, no demotion; depends_on SD-003/ARC-016 not confirmed operative).
5. **673 → reclassify non_contributory (degenerate) + MECH-171 → `out_of_domain` + queue cleanup.** Set `non_degenerate: false` on the authoritative manifest (arms identical, late_pred_loss≡0). Recommend MECH-171 `epistemic_category: out_of_domain` (sibling-consistent with MECH-172, governance_2026_06_10 — clinical AD multi-year staging not instantiable in a 300-episode grid-world). Retire/letter-bump V3-EXQ-673 in `experiment_queue.json`; the 3 untracked reruns must not multi-count.
6. **666b / 603o / 514n → `/governance` mark-reviewed + substrate amend** (no claim edits). 666b: amend `crf-availability-maintenance` with the ARM_1-collapse record, **ready stays false**. 603o: amend the escape-affordance / 603k harm-pathway substrate. 514n: amend the SD-049 bank-population substrate. All `pending_retest_after_substrate` retained.
7. **Systemic (user-confirmed):** spawn a background task to retrofit `_experiment_lib.check_degeneracy()` / the `non_degenerate` self-report across pre-net experiment scripts as a class, so the "vacuous read on an unwritten channel" family (670/671/673/514m/642/666a) is caught at measurement time rather than by manual autopsy.

## Draft `evidence_quality_note` strings for governance

- **ARC-065** (append): "V3-EXQ-569g (route-range matched-entropy falsifier, 2026-06-11): on the now-validated modulatory-bias-selection-authority substrate (643a, ready=true) the route-range channel reached the E3 accumulator (route_range 0.18, C1 PASS) but selected-action entropy (ARM_1_E2WF 0.615) did NOT strictly exceed the matched-noise control (0.704); 1/3 seeds strict-above. Range reaches selection but carves no extra committed-action diversity vs noise. NOT a demotion (provisional, 46 supports). Routed to /claim-synthesis as granularity debt (≥4 prior autopsies, distinct signatures) — the coarse 'diversity is load-bearing' claim under-names the range-reaches ≠ range-carves distinction."
- **MECH-314a** (append): "V3-EXQ-590b (novelty Goldilocks behavioural calibration, 2026-06-11): on the validated authority substrate, the gain knob moves H_pos by 0.283 across gains (authority operative, not zero) but every nonzero gain matched or degraded exploration vs the gain=0 control (best 0.4188 < 0.4200). No Goldilocks lift. NOT a demotion. Routed to /claim-synthesis as granularity debt — 'novelty buys exploration' under-names authority-moves-argmin ≠ signal-is-adaptive."
- **SD-033b / MECH-263** (append): "V3-EXQ-485f (trained-OFC-head behavioural, 2026-06-11): readiness gate (bias_range>1e-3) cleared by a hair (0.00898) but ~50x below the 0.05 the devaluation/between-context DVs require; behavioural signatures vacuously ~0. Readiness-gate miscalibration, not a fair falsification → manifest weakens reclassified non_contributory; pending_retest_after_substrate retained; retest V3-EXQ-485g with readiness floor aligned to the DV-significance floor. No demotion."
- **INV-048** (append): "V3-EXQ-670 (pharmacological sleep-disruption equivalence, 2026-06-11): degenerate — harm_discrimination byte-identical across all 4 arms because run_sleep_cycle never trains e3.harm_eval_head (seed-fixed readout). Faithful 4-arm design, broken readout. non_degenerate=false; carries no information on the derived prediction. Retest V3-EXQ-670a trains the harm-valuation pathway in the sleep cycle + adds a non-vacuity gate."
- **MECH-025b** (append): "V3-EXQ-671 (precision-responsibility, 2026-06-11): degenerate — C1 precision↔residue correlation and C2 high/low-precision residue ratio both exactly 0.0 across 778 committed harm-events because ResidueField.total_residue never accumulates under committed harm. 'mixed' is 4/6 arithmetic (the passes are health/sample preconditions). First MECH-025b run; carries no information against the claim. Retest V3-EXQ-671a adds a residue-accumulation positive-control gate."
- **MECH-171** (set epistemic_category + note): "V3-EXQ-673 (vicious-cycle sleep disruption, 2026-06-11): degenerate (all arms identical, late_pred_loss≡0; 3 untracked reruns under one EXQ). MECH-171 asserts clinical-Alzheimer's staged progression (multi-year vicious cycle, critical intervention window, schema-scaffold collapse) not faithfully instantiable in a 300-episode grid-world. epistemic_category: out_of_domain (parallel to MECH-172, governance_2026_06_10). Retire V3-EXQ-673."
