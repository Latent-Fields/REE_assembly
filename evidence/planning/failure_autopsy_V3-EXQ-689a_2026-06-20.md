# Failure autopsy: V3-EXQ-689a (MECH-439 conflict-grade gap-blind falsifier)

**Generated:** 2026-06-20T18:02:50Z
**Scope:** single | **Status:** confirmed (user-adjudicated Step-8 gate 2026-06-20)
**Target:** `v3_exq_689a_mech439_conflict_grade_gapblind_falsifier_20260620T175346Z_v3`
**Claim:** MECH-439 (F-dominance bounds committed-action diversity) | **Outcome:** FAIL / non_contributory | **Failed criterion:** discrimination
**Routing (user-confirmed):** implement-substrate (PRIMARY) + /claim-synthesis (secondary)

---

## 1. Facts (no interpretation)

689a is the keystone falsifier for MECH-439's proposed conflict-grade conversion fix, superseding V3-EXQ-689 (which self-routed `substrate_not_ready_requeue` on an uncomputable near-tie-pinned gap-spread regression; 689a replaced that regression with a **gap-blind ARM contrast**).

**Readiness ALL met, non-degenerate** (`non_degenerate: true`):

- `a1b1_modulatory_channel_route_range` = 0.624 (floor 0.01) — the modulatory bias reaches the selector with real cross-candidate range.
- `a1b1_e2_world_forward_prediction_spread` = 0.187 (floor 0.03) — the candidate pool is genuinely divergent (SD-056 trained).
- `grading_levers_engaged` = 3/3 seeds (k varies AND t_eff varies) — both conflict-grade levers actually acted.

**The pre-registered load-bearing gate (ARM_A1B1, both levers) FAILED:**

- `C_PRIMARY` (strict-above both collapsed-proposer controls): **0/3 seeds** — committed entropy 0.387 = baseline.
- `C_GAPBLIND` (strict-above both gap-blind controls): **0/3 seeds**.
- `C1` (e2-divergent non-vacuity): PASS. `C_FGAP` (quantile slope correlates with F-gap; secondary, non-gating): PASS (slope -0.716, gap-concentrated).
- Self-route label: `conversion_ceiling_persists_despite_conflict_grade` → the script's grid pre-registers this as `non_contributory`, "OFF-RAMP to V4 directions, NOT a falsification."

**The 2x2 dissociation (manifest `two_by_two_dissociation`, flagged informational/non-gating — but load-bearing):**

| arm | lever config | committed entropy | seeds strict-above collapsed | seeds strict-above gap-blind |
|---|---|---|---|---|
| ARM_A0B0 | both off (baseline) | 0.371 | 1/3 | 0/3 |
| ARM_A1B0 | Factor A only (graded shortlist width) | 0.440 | 0/3 | 0/3 |
| **ARM_A0B1** | **Factor B only (gap-scaled commit-T)** | **0.850** | **2/3** | **2/3** |
| ARM_A1B1 | both on (the gated hypothesis) | 0.387 | 0/3 | 0/3 |
| ARM_FIXED_KMAX | gap-blind A (flat k=6) | 0.546 | 1/3 | 0/3 |
| ARM_FIXED_HOT_T | gap-blind B (flat T=2.5) | 0.591 | 1/3 | 0/3 |
| ARM_PROPOSER_CTRL / ARM_MATCHED_NOISE | collapsed channel | 0.677 | — | — |

**Factor B (gap-scaled commit-T) alone converts** (0.850, 2/3 above both control sets). **Factor A (graded shortlist width) alone is inert** (0.440). **Combining them is destructive** — A1B1 (0.387) collapses back to the A0B0 baseline, far below A0B1. The pre-registered both-levers gate landed on the cancelling cell.

---

## 2. Claim-layer map

| Claim | Read | Why |
|---|---|---|
| MECH-439 core (F-dominance bounds committed diversity) | **intact** | the ceiling persists under the conflict-grade both-levers form = consistent with F-dominance; non_contributory, NOT a weakens. (The A0B1 lift shows the ceiling is not *absolute* — convertibility exists — but that is positive-adjacent, not a falsification.) |
| MECH-447 (conflict-grade near-tie lever sufficiency) | **weakened + needs split** | the both-levers form is refuted; but the commit-T leg converts alone (2/3). The "lever" is two dissociable levers with a destructive interaction — re-grain via /claim-synthesis. |
| MECH-448 (only rank-preserving F→eligibility demotion lifts) | **counter-evidenced + now the lead build** | a non-demotion commit-T lever lifted 2/3 — mild counter to "ONLY demotion lifts" — but demotion is the user-elected lead constitutional lever; the claim text needs the A0B1 caveat. |
| ARC-107 / MECH-449 / Q-078 (BG selector constitution) | **elevated** | the destructive A×B interaction is a constitutional/integration signal; instantiation gate moves toward "build." |

`claim_ids` accuracy: the manifest tags only `[MECH-439]` (correct — the experiment gates on the F-dominance conversion ceiling). The MECH-447/448/449/ARC-107/Q-078 implications are downstream and routed via the substrate amend + /claim-synthesis, not as new tags on this manifest.

---

## 3. Biological-reference triage (the core move)

- **Closest reference:** the basal-ganglia action-selection bottleneck — hyperdirect cortico-STN conflict-graded **hold** (Factor A graded shortlist width ≈ STN threshold-raise) + pallidal output **disinhibition gain** (Factor B gap-scaled commit-T).
- **Not a formal-definition import** — it is a functional BG translation; the lit-pull `targeted_review_connectome_mech_439` already exists (Frank Hold-your-horses; Cavanagh & Frank STN conflict-threshold; Bogacz MSPRT; Carandini & Heeger + Louie/Khaw/Glimcher divisive normalisation). **lit_status: present** — no new /lit-pull needed.
- **Does the failure match a known-dependency signature?** Yes — and biologically it explains the destructive interaction: **raising the STN hold threshold suppresses the very near-ties the pallidal commit-gain would diversify.** The two near-tie levers are *not independent*. The biologically-faithful translation is therefore **one permission-to-commit constitution** (rank-preserving F→eligibility demotion / divisive normalisation + Go/No-Go eligibility governance), **not two stacked near-tie patches**. This is precisely the constitutional reading ARC-107 captures.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (439 core) / weakened+split (447) / counter-evidenced (448) / elevated (449/107/Q-078) | the ceiling persists under both-levers; a single lever converts |
| Biological reference | clear / present | BG STN-hold + pallidal-gain; lit exists; the cancellation has a biological reading |
| Prerequisites | present | readiness 3/3; not substrate_not_ready |
| Implementation | complete (gated levers) / absent (demotion + Go-NoGo) | Factor A/B built + engaged; the constitutional legs are unbuilt |
| Environment | adequate | 603n foraging; F-gap near-tie-pinned BY the F-dominance under test |
| Measurement | adequate but **mis-gated** | 689a fixed 689's gap-spread gap; the *gate* (A1B1-only) landed on the cancelling cell, masking A0B1 |
| **Integration** | **coupled-but-unstable** | **the load-bearing finding: destructive A×B interaction** |
| Scale | adequate | 3 seeds, full curriculum |

**Recommended `epistemic_category`:** substrate_ceiling (the near-tie parametric family cannot convert; the ceiling is attacked by the constitutional build, not more tuning). **Recommended `evidence_direction`:** non_contributory. **pending_retest_after_substrate: true.**

---

## 5. Learning extracted

1. The conflict-grade near-tie "lever" is **not monolithic** — commit-T (Factor B) converts alone (2/3), shortlist-width (Factor A) is inert, and the two interact **destructively** (A1B1 collapses to baseline). The pre-registered both-levers gate happened to be the cancelling combination.
2. A single conflict-grade lever **does** convert committed diversity above both control sets (2/3) — the ceiling is **not absolute**. Positive-adjacent for convertibility, not a falsification of F-dominance.
3. MECH-448's "ONLY F→eligibility demotion lifts" is mildly counter-evidenced (a commit-T lever lifted without demotion) — but demotion is the user-elected lead lever; re-grain the claim text.
4. The destructive A×B interaction is a **constitutional/integration signal** (ARC-107 / Q-078): combining two BG-like levers cancels because STN-hold suppresses near-ties pallidal-gain would diversify — the faithful translation is one permission-to-commit constitution.
5. **Granularity-debt recurrence:** this is the Nth autopsy circling MECH-439 (689, 569g, 569h, 654g, 485h, 460h, the cluster doc + `claim_synthesis_MECH-439` already commissioned). The conflict-grade "lever" is really ≥2 dissociable levers → /claim-synthesis re-grain warranted alongside the build.

---

## 6. Repair pathway (user-confirmed: ELEVATE CONSTITUTIONAL BUILD)

**PRIMARY — implement-substrate (amend `f_dominance_conversion_ceiling`).** The conflict-grade near-tie *parametric* lever family is exhausted. Build the BG-constitution legs (ARC-107):

- **Lead lever — MECH-448 rank-preserving F→eligibility demotion:** remove F from the final committed argmin, use it only as a graded **eligibility envelope** (rank-preserving renormalisation against the competing field; divisive-normalisation grounded), so a modulatory/diversity channel arbitrates within the F-eligible set **without disinhibiting harmful classes** (order preserved on the numerators). Behind a no-op-default flag in `e3_selector.py`.
- **Broader follow-on — MECH-449 Go/No-Go eligibility governance.**
- **Falsifier for the build:** committed-action-class entropy strict-above both control sets on ≥2/3 seeds, order preserved on the numerators, no global disinhibition of harmful classes.

**SECONDARY — /claim-synthesis (granularity-debt hook).** Re-grain MECH-447 into the commit-T leg (converts), the shortlist-width leg (inert), and the destructive interaction; fold the A0B1-lifts-without-demotion finding into MECH-448. Proposal-first, parallel to the build, not blocking.

**Substrate_queue amend (recommended, governance applies):** `f_dominance_conversion_ceiling` status `lead_lever_built_experiment_in_flight_v3_exq_689a` → conflict-grade-family-insufficient / build-the-eligibility-demotion-lever; append the 689a failure_record; add MECH-448/449/ARC-107/Q-078 to `unblocks_claims`. Full structured entry in the sibling `.json`.

**Draft `evidence_quality_note` for MECH-439** (governance writes; do not write here): see `recommended_evidence_quality_note` in the sibling `.json`.

---

## 7. Governance handoff

- Mark V3-EXQ-689a reviewed; set `evidence_direction: non_contributory` + the `evidence_quality_note` above; MECH-439 stays candidate/substrate_ceiling, `pending_retest_after_substrate: true`. (689 already superseded by 689a.)
- Amend `f_dominance_conversion_ceiling` per the sibling `.json` `recommended_substrate_queue_entry` (action: amend).
- Surface the /claim-synthesis re-grain of MECH-447/448/449 as the secondary route.
- Analysis + handoff only — this autopsy edits no claims.yaml / manifest / review_tracker / substrate_queue; governance applies.
