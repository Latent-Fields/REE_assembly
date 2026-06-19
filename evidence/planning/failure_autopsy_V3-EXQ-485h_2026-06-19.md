# Failure Autopsy -- V3-EXQ-485h (trained-OFC-head behavioural; SD-033b / MECH-263)

- **Generated (UTC):** 2026-06-19T20:24:49Z
- **Run:** `v3_exq_485h_sd033b_trained_ofc_head_behavioural_20260619T192735Z_v3` (ree-cloud-2)
- **Outcome:** FAIL - manifest provisional `evidence_direction: weakens`; **ADJUDICATED -> `non_contributory`** (both SD-033b and MECH-263)
- **Self-route:** `sd033b_behavioural_functional_signature_absent` / disambiguation reading `devalued_range_collapsed_isolated_loop_route_live_E3` -- **the script deliberately defers the weakens/non_contributory call to this autopsy**
- **Scope:** single (terminus of the 485b/c/d/e/f/g/h lineage)
- **Status:** confirmed (interactive gate answered 2026-06-19: verdict `non_contributory + pending_retest`; routing = MECH-439 F-rebalance first, no 485i now)
- **Predecessors:** 485b/485c (representation-level PASS), 485d (trained-head readiness), 485e (`non_contributory`, range-starved -- `failure_autopsy_V3-EXQ-485e_2026-06-11`), 485f (`non_contributory`, vacuous-readiness, superseded without autopsy), 485g (`non_contributory`/`substrate_ceiling`, first non-vacuous test, T-vs-F **left open** -- `failure_autopsy_V3-EXQ-485g_2026-06-19`)

---

## 1. Facts (no interpretation)

485h is the **disambiguating run 485g explicitly designed and handed off to**. 485g produced a genuine 0.17 cross-candidate OFC bias range at the high-threat state with **zero behavioural conversion** and could not distinguish **(T)** a threat-invariant bias (head learned a candidate-identity bias that does not respond to outcome value) from **(F)** the F-dominance conversion ceiling (MECH-439). The decisive disambiguator 485g named was *the OFC bias range at the devalued state* plus a *live-E3 conversion test*. 485h records exactly these.

**Pre-registered acceptance** (per seed, then >= 2/3): READINESS (ARM_1 trained-head cross-candidate bias RANGE at the high-threat positive control `> BIAS_RANGE_FLOOR = 0.05` AND head weight-delta `> floor`); **C1** `devaluation_selection_shift > 0.05` and `> ARM_0 + 0.05`; **C2** `separation_ratio >= 3.0` AND `between_context_tv >= 0.05`; **C3** frozen-head silent. The driver is now a PAIRED threat-conditioned signal (outcome-coupled spread @ high-threat state_code + anti-range variance penalty @ devalued state_code), closing the 485g threat-conditioning gap.

**Result:**

| field | value |
|---|---|
| `readiness_met` | **true** (ready_seeds **3/3**) |
| `max_trained_head_delta` | **5.628** (genuinely trained) |
| `max_trained_bias_range` (high-threat) | **0.5007** (>> 0.05 floor) |
| `max_trained_bias_range_devalued` | **0.0155** |
| `max_collapse_ratio` (devalued/high) | **0.1197** (min 0.0) |
| C1 `devaluation_selection_shift` (ARM_1) | {0.0171, 0.0796, 0.0124} -> only seed1 > 0.05 -> **n_c1 = 1/3 FAIL** |
| C2 `between_context_selection_tv` (ARM_1) | {0.00355, 0.00642, 0.01055} all << 0.05 -> **n_c2 = 0/3 FAIL** |
| C3 frozen-head silent control | **PASS 3/3** |
| `discrimination_separation_ratio` (ARM_1) | 2.79 / 4.59 / **10546** -- seed2 degenerate (near-zero denominator), `criteria_non_degenerate.C2 = false` |
| `n_threat_invariant_seeds` | **0** |
| `n_range_collapsed_seeds` | **3** |
| `n_f_dominance_seeds` (live-E3) | **1** (seed1 `f_dominance_positive_adjacent`) |

**Live-E3 conversion test (per seed, ARM_1):**

| seed | authority_active | authority_range_high | committed_shift_devaluation | committed_shift_vs_f_only | live_e3_label |
|---|---|---|---|---|---|
| 0 | true | 0.153 | 0.0188 | 0.0188 | `live_e3_inconclusive` |
| 1 | true | **0.501** | **0.0** | **0.0** | **`f_dominance_positive_adjacent`** |
| 2 | true | 0.130 | 0.0157 | 0.0866 | `live_e3_inconclusive` |

**Which criterion failed:** the **discrimination criteria (C1 + C2)** failed substantively, with **readiness MET (3/3)** and the **negative control (C3) PASS (3/3)**. The "negative-control passes + readiness passes, every discrimination criterion fails" substrate-ceiling fingerprint -- and, like 485g and unlike 485e/485f, **not** a vacuity artifact (the trained head produced a real 0.50 cross-candidate range).

**Expected vs observed.** Expected: a trained, devaluation-sensitive / task-role-discriminative OFC head shifts/separates its candidate selection. Observed: the head produced a strong **state-conditioned** bias range -- 0.50 at high-threat, **collapsing to ~0.015 at the devalued state** (collapse ratio 0.12) -- that reaches E3 accumulator authority (range 0.50) but does **not** move committed selection (seed1 explicit F-dominance: authority 0.50, committed shift 0.0).

---

## 2. Claim-layer mapping

- **SD-033b** (`design_decision`, candidate, `epistemic_category: substrate_ceiling`, `v3_pending=false`, `pending_retest_after_substrate=true`; `depends_on` SD-033/MECH-263/MECH-261). The behavioural validation that would take it candidate -> provisional (commitment_closure:GAP-8) is precisely this experiment; `failure_record` empty.
- **MECH-263** (`mechanism_hypothesis`, candidate, `substrate_ceiling`, `v3_pending=true`, `pending_retest_after_substrate=true`, `depends_on` SD-033b/MECH-261). Signatures (a) devaluation sensitivity + (b) task-role discrimination -- the two DVs.
- **MECH-439** (`mechanism_hypothesis`, candidate, `standard`, `depends_on` ARC-065/MECH-309/ARC-062/MECH-294). The F-dominance conversion ceiling (the LIVE ROOT of the committed-action-diversity conversion ceiling: F monopolises ~88-89% of E3 committed-selection variance). `failure_record` empty.

**Did the test let the claims express?** At the **representation level, yes and positively** -- the bias range is real, non-vacuous, and *state-conditioned* (collapses at devaluation = the MECH-263 devaluation signature **a** at the representation level). At the **behaviour level, no** -- the conversion path to committed selection is monopolised by F (MECH-439), and the *proven* F-bypass (569i top-k shortlist conversion; ARC-065 ceiling lifted) was **not** in the live-E3 loop. So the behavioural claim has not yet been tested through a conversion-capable selector. `claim_ids` are accurate (the experiment directly tests SD-033b + MECH-263; the live-E3 leg additionally bears on MECH-439). No inherited-tag contamination (EXQ-048/MECH-057b mode does not apply).

---

## 3. Biological-reference triage

Closest mechanism: OFC outcome-value / specific-outcome coding driving candidate-differentiated action bias (Rudebeck & Murray 2018; Stalnaker 2021; Wilson-Niv 2014 cognitive map; SD-033b `lit_conf 0.863`). This is a **faithful biological translation**, NOT a formal-definition import (not the SD-003 two-pass-counterfactual class). Biologically, an intact, value-modulated OFC signal that reaches the action-selection accumulator but **cannot win against a dominant default controller** is a textbook **integration / conversion signature**, not OFC-mechanism falsification. The failure matches "what happens when a known downstream dependency (a selection stage that can be moved by the modulatory bias) is absent / saturated by another driver." **Demotion threshold (tested fairly + biology supports the mechanism + still fails) NOT reached** -- the conversion path was F-monopolised and the proven bypass was not exercised.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | behavioural expression blocked by a *different* claim (MECH-439), not by the OFC mechanism; `non_contributory`, not weakens |
| Biological reference | **clear** | OFC value coding; faithful translation; failure = missing/saturated conversion dependency |
| Prerequisites / dependency | **present** | 485e/f range-starvation AND 485g threat-conditioning gap both now closed (state-conditioned range, n_threat_invariant=0) |
| Implementation | **complete** | head trains (delta 5.63), range real (0.50) and correctly state-conditioned (collapses at devaluation) |
| Environment | adequate | SD-054 reef / aversive-devaluation pressure present |
| Measurement | **adequate** | the 485g-prescribed disambiguators (devalued-state range + live-E3 conversion) were finally recorded; C2 sep-ratio degeneracy caught by `criteria_non_degenerate` |
| Integration | **coupled but blocked** | OFC bias reaches E3 accumulator authority (range 0.50) but F monopolises committed selection (seed1 committed shift 0.0) |
| Scale / capacity | adequate | P1 budget fine; zero-conversion is structural (F-dominance), not under-training |

**Recommended `epistemic_category`: `substrate_ceiling`** (continuing 485e/485g), now **pinned to a specific substrate**: the MECH-439 F-dominance conversion ceiling. V3-tractable in principle -- the bypass (ARC-065 569i top-k) is proven -- but the retest is gated on the F-rebalance landing.

### The T-vs-F adjudication (485h's load-bearing output)

- **(T) threat-invariant bias -- REFUTED.** `n_threat_invariant_seeds = 0`; the bias range *collapses* at the devalued state (collapse ratio 0.12, `n_range_collapsed_seeds = 3`). The paired threat-conditioned driver did its job: the head is genuinely outcome-value-conditioned, not threat-invariant. This closes 485g's lead reading.
- **(F) F-dominance conversion ceiling (MECH-439) -- IMPLICATED as the proximate cause.** The live-E3 leg (which 485g could not run -- F was absent from its isolated-OFC-softmax loop) shows the OFC bias reaching accumulator authority (range up to 0.50) with **zero committed conversion** on the explicit F-dominance seed (seed1), corroborated by near-zero committed shifts on the inconclusive seeds 0/2 and the small isolated-loop C1. Strength is **single-seed-explicit + 2-seed-corroborating**, not a clean 3/3 -- so it is **positive-adjacent** evidence for MECH-439, not a counted "supports."

---

## 5. Cluster shape (485h joins the conversion-ceiling cluster)

| Run | Channel | Range carried in representation | Reached committed selection | Read |
|---|---|---|---|---|
| 569f / 661 / 654a / 654f | world-summary / rule_state / coherence / CRF | yes | nothing (flattened at the consuming selector) | conversion ceiling |
| 643 / 614e | curiosity / committed-class | (collapsed cand pool) | nothing | candidate-pool collapse |
| 485e | OFC trained head | head trained, range floor-starved | n/a (vacuous) | range starvation (fixed) |
| 485g | OFC trained head | real 0.17 high-threat range | zero, isolated loop | undisambiguated (T-vs-F open) |
| **485h** | **OFC trained head** | **real 0.50 state-conditioned range, reaches E3 authority** | **zero committed (F-dominance, live-E3)** | **F-dominance conversion ceiling (MECH-439)** |

**Structural property, not N independent bugs:** the F-dominance conversion ceiling (MECH-439, ~88-89% of E3 committed-selection variance) drowns *every* upstream modulatory channel that produces real differentiated signal. 485h is the OFC instance, and the first in this series to *measure the conversion step directly* via the live E3 selector. The 485e->485g->485h lineage is a converging instrumentation-fix sequence (range-starvation -> undisambiguated-conversion -> F-dominance-conversion-ceiling), now **terminated** in a single clean diagnosis -- the failure walked downstream, it did not circle the claim.

---

## 6. Granularity-debt recurrence check

This is the **3rd** autopsy on SD-033b/MECH-263 (485e 1st, 485g 2nd). Per the skill's proactive `/claim-synthesis` hook this recurrence is surfaced -- but it is **NOT granularity debt**:

- The three autopsies are **not** structurally-different falsification signatures circling a coarse claim; they are a *converging instrumentation-fix sequence* that has now resolved to one cause.
- The failure does not implicate SD-033b/MECH-263 being too coarse -- it implicates a **different, independently-established claim (MECH-439)** as the behavioural blocker. The OFC claim is fine; its behavioural expression is gated on the conversion ceiling.
- 485g's autopsy already adjudicated this (user-confirmed): "fixes converging, not distinct falsification signatures." 485h is the terminus of that convergence.

**No `/claim-synthesis` routing.** Surfaced here for the audit trail.

---

## 7. Learning extracted

1. **T is refuted, F is implicated.** The paired threat-conditioned driver closed the 485g threat-conditioning gap (the head is now genuinely state-conditioned: range collapses at devaluation, `n_threat_invariant=0`). The remaining wall is the F-dominance conversion ceiling -- isolated and measured for the first time via the live-E3 leg.
2. **The OFC channel joins the MECH-439 conversion-ceiling cluster as positive-adjacent evidence** (single-seed-explicit + 2-seed-corroborating; weak, not a counted supports).
3. **The MECH-263 devaluation signature (a) is positively shown at the representation level** -- the bias range collapses at devaluation, i.e. it *is* outcome-value-modulated. What fails is the *behavioural conversion*, not the representation.
4. **The manifest's provisional `weakens` is the script's pre-registered placeholder**, deliberately deferred to this autopsy by the disambiguation note ("...BEFORE stamping a SD-033b weakens"). Adjudicated **`non_contributory`**: the behaviour was blocked by MECH-439, and the proven F-bypass (569i top-k) was not in the loop, so the behavioural claim has not been fairly tested.
5. **The proven bypass is the natural retest, but it is sequenced behind the F-rebalance** (user decision) -- do not mint a 485i now; reprice the OFC behavioural test *after* the MECH-439 conversion ceiling is addressed (ARC-065 569i top-k / GAP-B 654g / 689a / 625e chain), so the retest reads a selector that can actually convert.

---

## 8. Routing (user-confirmed)

**Verdict: `non_contributory` + `pending_retest_after_substrate=true`** for both SD-033b and MECH-263 (override the manifest's provisional `weakens`). This is the **sole genuine behavioural experimental entry** for both claims (485e/f vacuous; 485g non-vacuous-but-non_contributory) -- it must **not** define exp_conf as a weakens. The non_contributory recommendation is paired with `pending_retest_after_substrate` per the skill's anti-illusory-resolution rule; the only "support" in the series is the representation-level 485b/485c PASS, which is a *different level* and is not displaced.

**Routing: MECH-439 F-rebalance first (no new experiment now).** Per the user, 485h becomes a conversion-ceiling data point and the OFC behavioural retest is **sequenced behind** the existing F-dominance / conversion-ceiling resolution chain (ARC-065 569i top-k -- ceiling lifted; GAP-B falsifier V3-EXQ-654g; 689a conflict-grade; 625e). Do **not** queue a 485i top-k-bypass run yet -- reprice the OFC behavioural test after the F-rebalance lands so it reads a conversion-capable selector. The deferred 485i design (route the OFC bias through the 569i top-k shortlist channel; convert -> confirm SD-033b/MECH-263 behavioural, still-fail -> *then* a genuine weakens) is recorded here as the pre-registered next test for when the gate clears.

**`recommended_substrate_queue_entry`: `amend` SD-033b.** SD-033b has a substrate_queue entry (status `?`, `unblocks_claims [MECH-261, MECH-263]`) with no failure trajectory. Append a failure record + metric-trajectory observation: the implemented trained OFC head produces a genuine 0.50 *state-conditioned* cross-candidate bias range (collapsing at devaluation) that reaches E3 accumulator authority but achieves **zero committed conversion** (F-dominance, live-E3 seed1) -- so its behavioural validation is gated on the MECH-439 / modulatory-bias-selection-authority conversion ceiling (the proven 569i top-k bypass, ARC-065 ceiling lifted, not yet routed through the OFC channel). Do **not** create a new MECH-439 substrate entry -- the conversion-ceiling cluster already owns that work (654g / 689a / 625e in flight); record 485h there only as a corroborating, *positive-adjacent* failure record (weak: single-seed-explicit).

**Governance posture:** SD-033b + MECH-263 stay **candidate / `substrate_ceiling` / `pending_retest_after_substrate=true`**. `evidence_direction = non_contributory` (both). No weakens, no demotion, no `v3_pending` change. MECH-439 stays **candidate / standard** -- record 485h as positive-adjacent corroboration, do **not** flip status or count a supports on single-seed data.

---

## 9. Draft `evidence_quality_note` (for `/governance` to apply -- not written here)

> See `recommended_evidence_quality_note` in `failure_autopsy_V3-EXQ-485h_2026-06-19.json`.
