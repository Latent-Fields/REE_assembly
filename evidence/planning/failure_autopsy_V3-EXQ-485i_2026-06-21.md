# Failure Autopsy -- V3-EXQ-485i (SD-033b / MECH-263 trained-OFC-head behavioural, MECH-448 demotion-enabled selector)

- **Run:** `v3_exq_485i_sd033b_demotion_enabled_behavioural_20260621T124253Z_v3`
- **Generated:** 2026-06-21T16:48:04Z
- **Status:** confirmed (interactive gate answered 2026-06-21: self-route correct; routing = implement-substrate amend + re-queue 485j; no /claim-synthesis)
- **Claims:** SD-033b, MECH-263 (both candidate, `substrate_ceiling`, promote/demote suppressed)
- **Outcome:** FAIL / `evidence_direction: non_contributory` / `non_degenerate: false` (already `scoring_excluded` -- carries **no governance weight**)
- **Supersedes:** V3-EXQ-485h
- **Self-route on manifest:** `substrate_not_ready_requeue`

---

## 1. Verdict (one line)

The self-route is **correct** -- the test was **genuinely vacuous**. The MECH-448 F->eligibility demotion lever **silently did not engage** on the 485i behavioural candidate bank (`f_eligibility_excluded_count == 0`, envelope admitted all 8 candidates on every seed), so the demotion-enabled selector reduced to the demotion-off arm and the behavioural DVs never ran through a genuinely-demoted selector. **Not** a SD-033b/MECH-263 weakens.

---

## 2. Facts reconstruction (no interpretation)

ARM_2 (`trained head + demotion ON`, the test arm) per-seed at the high-threat positive-control state:

| Readiness precondition | measured | threshold | met |
|---|---|---|---|
| 1. OFC bias cross-candidate **range** (max-min over the real bank) | **0.368** | 0.05 | yes |
| 2. `state_bias_head` weight-delta-from-init L2 | **5.39** | 0.001 | yes |
| 3. **MECH-448 non-degeneracy** `f_eligibility_excluded_count > 0` | **0.0** | 0.0 | **no** |

On all three ARM_2 seeds: `f_eligibility_envelope_size = 8`, `f_eligibility_excluded_count = 0`, `f_eligibility_demotion_active = true`, `f_eligibility_winner_neq_f_argmin = true`. `raw_score_range_high` per seed: **4.64 / 393689.4 / 4.57**. ARM_0 (frozen head + demotion) shows the same `excluded_count = 0`.

The script's config under test is the **exact** MECH-448 ARM_ON config that VALIDATED under V3-EXQ-689d: `use_f_eligibility_demotion=True`, `f_eligibility_envelope_floor=0.30`, `f_eligibility_dn_sigma=0.0` (script lines 202-204).

`criteria_non_degenerate`: C1 false, C2 false, C3 true. The ARM_2 `devaluation_selection_shift=1.0` / `between_context_selection_tv=1.0` values are therefore **non-scoring** -- they were not produced through a genuinely-demoted selector.

**Which criterion failed:** a **negative-control / non-degeneracy** criterion (precond 3), not a discrimination criterion. The behavioural discrimination DVs (C1, C2) never ran a fair test.

---

## 3. Why the self-route is correct (the test is genuinely vacuous)

The 3-arm dissociation attributes conversion to the **conjunction** trained-head AND demotion: ARM_2 (trained + demotion-on) must convert where ARM_1 (trained, demotion-off = F-dominance ceiling) and ARM_0 (frozen + demotion = silence) do not. With `excluded_count == 0`, the MECH-448 eligible set = **all 8 candidates**, so "F removed from the argmin within the F-eligible set" collapses to "modulatory arbitration over the whole pool" -- which is exactly **ARM_1's** reach. **ARM_2 == ARM_1.** A dissociation whose test arm is identical to its ceiling control cannot speak to SD-033b/MECH-263. `non_contributory`, never a weakens, is the right call (and the manifest's own `non_degenerate: false` already excludes it from scoring).

---

## 4. Root cause of `excluded_count == 0` (code-confirmed)

`E3TrajectorySelector._f_eligibility_envelope` (`ree-v3/ree_core/predictors/e3_selector.py:745`):

```
merit[i] = clamp(raw_scores.max() - raw_scores[i], min=0)   # F is a cost; best = highest merit
pooled   = f_eligibility_dn_sigma + merit.sum()              # sigma = 0.0
elig[i]  = merit[i] / pooled                                 # share of the competing field
eligible = { i : elig[i] >= f_eligibility_envelope_floor }   # ABSOLUTE share floor = 0.30
# if eligible set is empty  ->  fall back to ALL candidates  (excluded_count == 0)
```

`excluded_count == 0` here is the **`eligible_idx.numel() == 0 -> fallback ALL`** branch: **no candidate's merit-share reached the 0.30 absolute floor**, so the floor admitted nobody and the envelope fell back to all 8. The 485i OFC-isolated SD-054 reef/forage candidate bank produces a **spread (non-divergent) F distribution** -- the merit is divided across ~7 near-tied "good" candidates so the best holds **< 30%** of the total share. Both observed F regimes produce the same fallback:

- **Graded F** (seeds 0/2, `raw_range ~4.6`): roughly even merit across candidates -> best share ~0.25 < 0.30.
- **Single catastrophic outlier** (seed 1, `raw_range 393689`): one candidate enormously worse, the other 7 near-tied at ~1/7 = 0.14 share each < 0.30.

### Why 689d engaged and 485i did not -- the new signature

V3-EXQ-689d (MECH-448's own falsifier, **PASS**) ran the **identical** config (floor 0.30, dn_sigma 0.0) on the **GAP-A foraging substrate** with **SD-056-trained `e2.world_forward` + `candidate_summary_source=e2_world_forward`** -> a **divergent, peaked** F pool where one/few candidates hold > 30% merit share (mean `excluded_count` 0.152 > 0). 485i used the OFC-isolated bank **as-is** and never armed that divergent-pool construction. So the absolute share-floor is calibrated to 689d's peaked pool, not the spread behavioural bank.

This is a **new signature -- harness/state-dependent envelope engagement** -- distinct from 485h's **F-dominance conversion-ceiling** signature (there the trained OFC bias reached the E3 accumulator with real authority but the F-monopolised argmin never moved; **here the demotion lever that was supposed to lift that monopoly silently did not engage at all**). It is the ~10th self-route in the SD-033b / f_dominance-conversion-ceiling lineage and the first whose proximate cause is the demotion **envelope's** non-engagement rather than F-dominance per se.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | SD-033b/MECH-263 never tested through a demotion-capable selector; the OFC mechanism is fine. `non_contributory`, not weakens. |
| Biological reference | clear | BG hyperdirect conflict-grade / divisive normalisation (Frank 2006; Carandini & Heeger 2012). Envelope-floor mis-engagement is substrate tuning, not biology divergence. |
| Prerequisites | **missing** | The divergent-pool non-vacuity precondition 689d established (a peaked F over the bank, via SD-056-trained `e2.world_forward` + `candidate_summary_source=e2_world_forward`) was NOT armed in the 485i OFC-isolated harness. |
| Implementation | complete but **mis-calibrated** | `f_eligibility_envelope_floor=0.30` calibrated to 689d's peaked pool, not the behavioural bank's spread merit-share. |
| Environment | wrong pressures for this lever | OFC-isolated SD-054 reef/forage CEM bank yields a spread (non-divergent) F pool over the 8 candidates. |
| Measurement | **adequate** | The MECH-448 non-degeneracy gate (`excluded_count>0`) caught the no-op and self-routed -- the gate working exactly as designed. |
| Integration | -- | The MECH-448 selector x OFC behavioural harness interaction surfaced a bank-dependence in envelope engagement. |
| Scale / capacity | adequate | P1 budget fine; the no-op is structural, not under-training. |

**Recommended `epistemic_category`: `substrate_ceiling`** (continues 485e/485g/485h), pinned to the demotion-envelope-engagement substrate within the ARC-107 selector constitution.

---

## 6. The supersession (why no /claim-synthesis)

The active direction is the **ARC-107 BG-selector constitution**: **MECH-448** rank-preserving F->eligibility demotion (the LEAD lever, validated by 689d and **promoted candidate->provisional 2026-06-21**) + **MECH-449** Go/No-Go eligibility governance (follow-on). This **supersedes** the MECH-439 F-variance-**rebalance** / MECH-447 conflict-grade near-tie pathway, which the `f_dominance_conversion_ceiling` entry records as **"EXHAUSTED by V3-EXQ-689a"**.

So 485i is **not** another "diversity drowns under F-dominance" instance (the superseded rebalance frame). It is a **non-vacuity-precondition / behavioural-harness calibration gap in the new, superseding direction**: the demotion envelope needs a divergent (peaked) candidate pool to engage, and 485i did not arm one.

**Recurrence audit.** 485i is the ~5th autopsy circling SD-033b/MECH-263 (485e, 485g, 485h, the 695-696 cluster, now 485i). The granularity-debt hook fires on count -- but **no /claim-synthesis** is recommended:

1. Every diagnosis pins the blocker to the shared **selector locus**, not to SD-033b being too coarse (mirrors the explicit 485h decision).
2. That locus has **already been decomposed** by ARC-107 (MECH-448 demotion + MECH-449 Go/No-Go). A synthesis would re-derive an existing decomposition.
3. The recurrence is now a **harness-calibration** issue on the superseding lever, not a missing finer mechanism.

Recorded for the audit trail only.

---

## 7. Learning extracted

- The MECH-448 F->eligibility demotion is **bank-dependent**: with an absolute merit-share floor it engages only on a **peaked (divergent)** candidate pool; a spread pool sends the envelope to its all-admit fallback (`excluded_count==0`), making the lever a structural no-op.
- The 689d-validated config is **not portable** to a different candidate-bank construction without re-establishing the divergent-pool non-vacuity precondition. The precondition is a property of the **candidate source** (`e2_world_forward` divergent summaries), not of the demotion flags.
- The MECH-448 non-degeneracy gate (`excluded_count>0`) is **load-bearing** -- it converted a would-be false weakens into an honest substrate_not_ready_requeue.

---

## 8. Routing (user-confirmed)

**`implement-substrate`** -- amend the existing `f_dominance_conversion_ceiling` substrate_queue entry with the 485i failure record + an **envelope-engagement retune hint**, then re-queue **V3-EXQ-485j** (NEW letter, supersedes 485i) after the tune. Verdict `non_contributory` + `pending_retest_after_substrate=true` for both SD-033b and MECH-263 (the manifest's own `non_degenerate:false` already excludes it from scoring).

### `recommended_substrate_queue_entry` (action: amend, target: `f_dominance_conversion_ceiling`)

For the 485j re-queue:

1. **Arm the divergent-pool non-vacuity precondition** 689d used -- SD-056-trained `e2.world_forward` + `candidate_summary_source=e2_world_forward` -- so the candidate bank's F pool is **peaked** enough that the floor=0.30 envelope excludes; **and/or**
2. **Measure the behavioural-bank max per-candidate merit-share first** and calibrate `f_eligibility_envelope_floor` below it. KEEP an **absolute** share floor (a fraction-of-max degenerates to the margin shortlist); KEEP `dn_sigma=0.0` (raising sigma tightens further toward all-admit).
3. KEEP **precond-3 (`excluded_count>0` on >=2/3 seeds) as a HARD readiness gate** that must pass **before** the C1/C2 DVs run, so a non-engaging envelope self-routes `substrate_not_ready_requeue` rather than producing a misattributed shift.

This is a behavioural-harness calibration on the **superseding constitutional lever (MECH-448)**, NOT a MECH-439 F-variance rebalance.

### Draft `evidence_quality_note` (for governance to write -- not written here)

> V3-EXQ-485i (SD-033b/MECH-263 trained-OFC-head behavioural retest on the MECH-448 demotion-enabled E3 selector; supersedes V3-EXQ-485h) self-routed substrate_not_ready_requeue (non_contributory; non_degenerate:false / scoring_excluded -- no governance weight). Trained-head readiness PASSED (OFC bias cross-candidate range 0.368>=0.05; head weight-delta 5.39) but the MECH-448 non-degeneracy gate FAILED: f_eligibility_excluded_count==0 on all 3 seeds (envelope_size=8). The 689d-validated ARM_ON demotion config (floor=0.30, dn_sigma=0.0) admitted EVERY candidate because the OFC-isolated SD-054 behavioural bank has a SPREAD (non-divergent) F distribution -- no candidate's merit-share cleared the absolute 0.30 floor -> all-admit fallback -> the F->eligibility demotion was a STRUCTURAL no-op (ARM_2==ARM_1) -> the behavioural DVs never ran through a demoted selector. NEW signature: harness/state-dependent envelope engagement (distinct from 485h's F-dominance conversion-ceiling). NOT a SD-033b/MECH-263 weakens. The only "support" in the 485 series remains the representation-level 485b/485c PASS (a different level). pending_retest_after_substrate.

### `/claim-synthesis`

**None.** The conversion-ceiling family is already decomposed by the superseding ARC-107 selector-constitution (MECH-448 demotion + MECH-449 Go/No-Go). Recurrence recorded for the audit trail only.
