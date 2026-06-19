# Failure Autopsy — V3-EXQ-485g (trained-OFC-head behavioural; SD-033b / MECH-263)

- **Generated (UTC):** 2026-06-19T15:20:52Z
- **Run:** `v3_exq_485g_sd033b_trained_ofc_head_behavioural_20260619T145454Z_v3`
- **Outcome:** FAIL · `evidence_direction: non_contributory` (both SD-033b and MECH-263)
- **Self-route:** `sd033b_behavioural_functional_signature_absent` — **ADJUDICATED → substrate_ceiling (conversion / threat-conditioning gap), NOT a weakens**
- **Scope:** single (continuation of the 485e/485f lineage)
- **Status:** confirmed (interactive gate answered 2026-06-19; routing = 485h disambiguating redesign + amend SD-033b failure_record; NO /claim-synthesis)
- **Predecessors:** 485b/485c (representation-level PASS), 485d (trained-head readiness), 485e (non_contributory, range-starved — `failure_autopsy_V3-EXQ-485e_2026-06-11`), 485f (non_contributory, vacuous-readiness-gate, superseded without autopsy)

---

## 1. Facts (no interpretation)

485g is the **first non-vacuous** behavioural test of the trained SD-033b OFC `state_bias_head` in the 485-series. The two predecessors that ran to completion failed on test-design, not the claim:
- **485e** — readiness gate `bias_range > 1e-3` cleared on only 1/3 seeds; cross-candidate bias range floor-starved (the statistic every DV routes on). `substrate_not_ready_requeue` (confirmed autopsy).
- **485f** — readiness floor `1e-3` cleared at `max_trained_bias_range = 0.00898`, ~50x BELOW the 0.05 the devaluation DV requires → a vacuous "ready" certifying a test that could not fire.

485g makes two fixes: (a) the readiness floor is re-aligned `1e-3 → 0.05` (== `DEVAL_SHIFT_MARGIN`), so "ready" can no longer certify a vacuous DV; (b) the under-driving shared-return REINFORCE is replaced by an outcome-coupled, threat-conditioned, **per-candidate** REINFORCE-over-candidates (`adv_k = gain * threat * (mean_harm - harm_k)`, applied over all K), with LR `5e-4 → 2e-3` and P1 `60 → 120` ep.

**Acceptance (per seed, then majority of 3):** READINESS (trained-head bias cross-candidate RANGE at the high-threat positive control `> 0.05` AND head weight-delta `> floor`); **C1** `devaluation_selection_shift > 0.05` beyond the frozen control; **C2** discrimination `separation_ratio >= min` AND `between_context_tv >= 0.05`; **C3** frozen-head silent.

**Result:**

| field | value |
|---|---|
| `readiness_met` | **true** (ready_seeds 2/3) |
| `max_trained_bias_range` | **0.1706** (≫ 0.05 floor) |
| `max_trained_head_delta` | **6.318** (genuinely trained) |
| C1 `devaluation_selection_shift` (ARM_1, per seed) | **{0.00122, 0.0, 0.01021}** — all ≪ 0.05; **n_c1_seeds = 0** |
| C2 `between_context_selection_tv` (ARM_1) | **{0.0113, 0.0257, 0.0012}** ~0; `criteria_non_degenerate.C2 = false`; **n_c2_seeds = 0** |
| C3 frozen-head silent | **PASS 3/3** (`n_c3_seeds = 3`) |
| `discrimination_separation_ratio` (ARM_1) | 457 / 47.6 / 7.79 — degenerate (tiny/tiny), flagged non-degenerate=false |

**Which criterion failed:** the **discrimination criteria (C1 + C2)** failed substantively, with readiness MET and the negative control (C3) passing. This is the **"negative control passes + readiness passes, every discrimination criterion fails" substrate-ceiling fingerprint** — and, unlike 485e/485f, it is **not** a vacuity artifact: the trained head produced a genuine 0.17 cross-candidate bias range.

**Expected vs observed.** Expected: a trained, devaluation-sensitive / task-role-discriminative OFC head shifts/separates its candidate selection. Observed: the head produced a real cross-candidate bias **range** (0.17) but **zero behavioural conversion** — selection at the high-threat state ≈ selection at the devalued state (C1), and selection across perceptually-matched task-role contexts barely separates (C2).

---

## 2. Claim-layer mapping

- **SD-033b** (`design_decision`, candidate, `v3_pending=false`, `pending_retest_after_substrate=true`; `depends_on` SD-033/MECH-263/MECH-261). The behavioural validation that would take it candidate→provisional (commitment_closure:GAP-8) is precisely this experiment.
- **MECH-263** (`mechanism_hypothesis`, candidate, `v3_pending=true`, `pending_retest_after_substrate=true`). Signatures (a) devaluation sensitivity + (b) task-role discrimination — the two DVs that failed.

**Did the test let the claims express?** Readiness was MET (the bias range is real and non-vacuous), so unlike 485e/485f the claim was given a *non-vacuous* opportunity. But the test **cannot distinguish** a genuine conversion failure from a driver/measurement gap (see §4). `claim_ids` are accurate — the experiment directly tests SD-033b + MECH-263, no inherited-tag contamination (the EXQ-048/MECH-057b failure mode does not apply).

---

## 3. Biological-reference triage

Closest mechanism: OFC outcome-value / specific-outcome coding driving candidate-differentiated action bias (Rudebeck & Murray 2018; Stalnaker 2021; Wilson-Niv 2014 cognitive map; SD-033b lit_conf 0.863). This is a **faithful biological translation**, NOT a formal-definition import (not the SD-003 two-pass-counterfactual class). The dependency the mechanism needs — that a learned value-bias **convert** into a selection shift under outcome devaluation — is exactly what is absent. Biologically, an intact OFC value signal that cannot influence the action gate is a **missing-dependency / integration signature**, not OFC-mechanism falsification. **Demotion threshold (tested fairly + biology supports + still fails) NOT reached** — the test was not yet a fair conversion test (the driver trains range under threat but supplies zero anti-range gradient at low threat, the exact suppression C1 measures; the script docstring concedes this).

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | Non-vacuous test, but conversion not isolated; non_contributory, not weakens. |
| Biological reference | **clear** | OFC value coding; faithful translation; failure = missing conversion dependency. |
| Prerequisites / dependency | **partial** | Trained head + non-vacuous range present (the 485e/485f starvation is fixed); the threat-CONDITIONING of that range is unverified. |
| Implementation | **partial** | Head genuinely trains (Δ 6.32), produces a 0.17 range; but the outcome-coupled driver gives zero gradient at low threat, so the head is **not trained on the devaluation-suppression** C1 measures. |
| Environment | adequate | SD-054 / aversive-devaluation pressure present. |
| Measurement | **under-instrumented** | The decisive disambiguator — OFC bias range *at the devalued state* and *per task-role context* — was NOT recorded. C2 sep-ratio degenerate (caught by `criteria_non_degenerate`). |
| Integration | isolated (by design) | OFC is the SOLE bias channel; modulatory-bias-selection-authority deliberately OFF. The readout is `softmax(-compute_bias(bank)/T)`, **not** the live E3 selector. |
| Scale / capacity | adequate | P1=120 ep, head trained fine; the zero-conversion is structural, not under-training. |

**Recommended `epistemic_category`: `substrate_ceiling`** (continuing 485e). V3-tractable in principle, but the current readout/driver cannot convert the bias range into the behavioural signatures.

### The two live readings (485g cannot adjudicate between them)

- **(T) threat-conditioning gap** *(lead reading)*: the head learned a candidate-identity bias under threat but a threat-**invariant** one (the driver supplies no anti-range gradient at low threat), so devaluing z_harm barely changes `compute_bias` → `devaluation_selection_shift ~ 0`. Continuous with the 485e/485f substrate-readout lineage; SD-033b-specific.
- **(F) F-dominance conversion ceiling (MECH-439)** *(manifest self-route)*: plausible by analogy to the broader conversion-ceiling pattern (the OFC is the Nth upstream channel producing real signal without committed conversion), but **NOT directly measurable in 485g**: the readout is the isolated OFC softmax, so the E3 primary score F is **not in this loop**. Routing to MECH-439 on this run would over-read.

The decisive disambiguator is the **OFC bias range at the devalued state**: if it stays ~0.17 at devaluation → (T) the head learned a threat-invariant bias; if it collapses to ~0 but selection still doesn't shift → (F) conversion ceiling. The manifest reports `bias_range_high_threat` (0.17) but not the devalued-state range, so the question is open. **485h is designed to record exactly this.**

---

## 5. Learning extracted

1. **First non-vacuous 485 result.** The 485e (range-starved) → 485f (vacuous-readiness) → 485g lineage is a sequence of *test-instrumentation* fixes; 485g is the first run where readiness is genuinely met (0.17 range, 2/3 seeds) and the claim still does not convert. The substrate-readout starvation is fixed; the wall moved downstream to **conversion**.
2. **The manifest's F-dominance self-route over-reads its own loop.** The behavioural DV is `softmax(-ofc.compute_bias(bank)/T)` with the modulatory selection authority OFF — F is not in this loop, so MECH-439 cannot be the *measured* proximate mechanism here. It remains a credible *broader-pattern* hypothesis to be tested by routing the OFC bias through the live E3 selector (485h optional arm).
3. **The outcome-coupled driver is a hard-by-construction test of C1.** `adv_k = gain*threat*(mean_harm - harm_k)` is zero at threat~0, so the head receives no signal to *flatten* range when devalued — exactly the suppression C1 measures. A non-circular fix is to add an explicit paired high-threat/devalued contrast (or low-threat anti-range) term to the driver.
4. **The missing measurement is load-bearing.** Without the devalued-state bias range (and per-task-role-context range), T and F are indistinguishable; the autopsy cannot pick, and neither should governance.

---

## 6. Repair pathway (user-confirmed)

**Routing: `/queue-experiment` → V3-EXQ-485h disambiguating redesign.** Same scientific question (SD-033b/MECH-263 behavioural signatures), alphabetic suffix (implementation/test-design fix, not a new question). 485h adds:
1. **Record the OFC bias range at the devalued state and per task-role context** — the T-vs-F disambiguator the 485-series has never measured.
2. **Close the driver gap**: train the head on the threat-conditioned suppression C1 measures (an explicit paired high-threat/devalued contrast term, or a low-threat anti-range signal), so a passing C1 is non-circular and a failing C1 with readiness met is an honest result.
3. **Optional live-E3 arm**: route the OFC bias through the real E3 selector (modulatory-bias-selection-authority ON) to test the F-dominance reading directly. If the bias reaches the accumulator but does not move committed selection there, **then** 485g/485h join the MECH-439 conversion-ceiling cluster (becoming positive-adjacent evidence for MECH-439). Not before — defer the F-vs-T call to that data.

**`recommended_substrate_queue_entry`: `amend` SD-033b.** SD-033b is `implementation_status: implemented` with an empty `failure_record: []`. Append a failure record documenting that the implemented OFC head produced a genuine 0.17 cross-candidate bias range with zero behavioural conversion (first non-vacuous test) — so the implemented substrate's failure history is linkable from the IGW workset. Do **not** create a MECH-439 substrate entry from this run (the conversion-ceiling cluster owns that, driven by the 625d/654g/689 composite results; minting it on undisambiguated 485g data is premature).

**Granularity-debt recurrence:** this is the 2nd autopsy on SD-033b/MECH-263 (485e was 1st). User-confirmed reading: **NOT** granularity debt — 485e was a vacuous-instrumentation diagnosis and 485g is the first real test, so the series is fixes converging, not distinct falsification signatures circling a coarse claim. No `/claim-synthesis` routing. Surfaced here for the audit trail.

---

## 7. Draft `evidence_quality_note` (governance writes; do not write here)

> V3-EXQ-485g (first non-vacuous trained-OFC-head behavioural test): readiness MET (cross-candidate bias range 0.171 >= 0.05 floor, 2/3 seeds; head weight-delta 6.32, genuinely trained), C3 frozen-head silence control PASS, but C1 devaluation shift {0.001,0.0,0.010} << 0.05 (0/3) and C2 between-context TV ~0 (degenerate) — a genuine 0.17 bias RANGE with ZERO behavioural conversion. Adjudicated substrate_ceiling / non_contributory, NOT a weakens: the OFC mechanism is a faithful translation (lit_conf 0.863) and was not given a fair conversion test (the outcome-coupled driver supplies zero anti-range gradient at low threat — the suppression C1 measures — and the devalued-state bias range, the decisive conversion-vs-conditioning disambiguator, was not recorded). The manifest's MECH-439 F-dominance self-route is an analogy to the broader conversion-ceiling pattern, NOT a mechanism measurable in 485g's isolated-OFC-softmax loop (F is absent from this readout). Routed to V3-EXQ-485h (disambiguating redesign: record devalued-state bias range + per-task-role-context range, close the driver gap with a paired high-threat/devalued contrast, optional live-E3-selector arm to test F-dominance directly). SD-033b + MECH-263 stay candidate / pending_retest_after_substrate — sole genuine experimental entry for both; do not let this define exp_conf.
