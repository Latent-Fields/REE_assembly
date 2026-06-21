# Failure Autopsy — V3-EXQ-485j (SD-033b demotion-envelope-calibrated behavioural)

- **generated_utc:** 2026-06-21T18:09:30Z
- **status:** confirmed (user-adjudicated 2026-06-21)
- **scope:** single
- **run_id:** v3_exq_485j_sd033b_demotion_envelope_calibrated_behavioural_20260621T180033Z_v3
- **queue_id:** V3-EXQ-485j  (machine ree-cloud-2)
- **claim_ids (manifest):** SD-033b, MECH-263
- **manifest self-route:** FAIL / evidence_direction=weakens / interpretation.label=`conversion_ceiling_persists_despite_demotion` — **DOWNGRADED by this autopsy** (see §7).

---

## 1. One-line verdict

The MECH-448 BG F->eligibility demotion lever **generalises off the GAP-A foraging substrate to the OFC valuation channel** — the C2 task-role-discrimination signature **converted** (2/3 seeds, cleanly dissociated against the F-dominance control). The overall FAIL is driven entirely by **C1 devaluation**, which did not convert because the OFC trained head's bias range **collapses to ~0.02 (below the 0.05 non-vacuity floor) at the devalued state** — a channel-specific SD-033b devalued-head / test-design gap, **orthogonal to the demotion envelope** (which fired correctly) and **not** evidence against MECH-448 generalisation.

The autopsy question posed a binary — (a) recalibrate the demotion-envelope floor for OFC's F-distribution, or (b) MECH-448 does not generalise → escalate. **Both are wrong.** The answer is **(c)**: the lever generalises (C2); the residual is the devaluation-signature substrate/test design.

---

## 2. Facts — reconstruction (no interpretation)

### Acceptance (the FAIL is C1-only)

| Criterion | load-bearing | per-seed | n_seeds | verdict |
|---|---|---|---|---|
| C1_devaluation_behavioural_shift | yes | 0.0 / 0.0 / 0.0 | 0/3 | **FAIL** |
| C2_discrimination_behavioural_separation | yes | TV 1.0 / 0.0 / 1.0 | 2/3 | **PASS** |
| C3_silence_control | yes | held | 3/3 | PASS |

`pass=false` only because C1 (load-bearing) fails. C2 and C3 pass.

### Preconditions (all reported MET)

| precondition | measured | threshold | met |
|---|---|---|---|
| `ofc_trained_head_bias_cross_candidate_range_supra_dv_floor` (**high-threat** state) | 0.3771 | 0.05 | True |
| `ofc_head_weight_delta_supra_floor` | 5.4266 | 0.001 | True |
| `mech448_f_eligibility_excluded_count_supra_zero` | 5.0 | 0.0 | True |

### Three-arm dissociation (the load-bearing C2 signal)

| arm | head trained? | demotion? | `between_context_selection_tv` (s0/s1/s2) | `devaluation_selection_shift` |
|---|---|---|---|---|
| ARM_0 frozen + demotion-on | no | on | 0.0 / 0.0 / 0.0 (silence) | 0.0 / 0.0 / 0.0 |
| ARM_1 trained + demotion-off (**F-dominance ceiling control**) | yes | off | **0.0 / 0.0 / 0.0** | 1.0 / 0.0 / 0.0 |
| ARM_2 trained + demotion-on (**test**) | yes | on | **1.0 / 0.0 / 1.0** | 0.0 / 0.0 / 0.0 |

ARM_2 converts discrimination where ARM_1 (same trained head, F left dominant) does **not**, and ARM_0 (no trained valuation) is silent → the conjunction **trained-head AND demotion** is what carries the discrimination conversion. `discrimination_separation_ratio` = 1e6 on the converting seeds (between=1, within=0).

### The C1 devaluation channel (why shift=0)

| arm/seed | `bias_range_high_threat` | `bias_range_devalued` | collapse ratio | excluded_count | winner≠F-argmin |
|---|---|---|---|---|---|
| ARM_2 s0 | 0.1559 | **0.0203** | 0.130 | 5 | True |
| ARM_2 s1 | 0.3771 | **0.0000** | 0.000 | 5 | True |
| ARM_2 s2 | 0.0986 | **0.0180** | 0.182 | 4 | False |

`max_test_bias_range_devalued = 0.0203` (vs the 0.05 `DEVAL_SHIFT_MARGIN` floor). The OFC head produces a strong candidate-differentiated bias at the **high-threat** positive control but the bias **collapses to near-flat at the devalued state**. A flat OFC bias at devalued gives the (correctly-firing) demotion selector nothing to re-rank → committed argmin unchanged → `devaluation_selection_shift`=0.

**Which criterion failed:** discrimination (C1's `devaluation_selection_shift`) — but the failure is a *non-vacuity floor breach on the devalued-state range*, not a fair-test falsification (see §3, §7).

### Script mechanism (code-confirmed)

- C1 measures `TV(onehot(idx_high), onehot(idx_low))` where idx_high is the committed selection after settling to the high-threat state_code and idx_low after settling to the devalued (low-threat) state_code (`experiments/v3_exq_485j_…py:848-884`).
- The paired training driver applies `DEVALUED_ANTIRANGE_WEIGHT = 0.5` — an **anti-range variance penalty at the devalued state_code** (line 209, 621-631). It explicitly trains the head to produce **low range (flat) at the devalued state**, not a *re-ranking* bias that would shift the committed action.
- The C1 readiness precondition (`_bias_range` at the high-threat state, line 851) gates the **high-threat** range. The **devalued-state** range (line 880) — which the C1 DV actually routes on — is recorded but **not gated**.

---

## 3. Claim-layer mapping (did the test let each claim express itself?)

| claim | status / category | tested fairly? |
|---|---|---|
| **MECH-448** (rank-preserving F->eligibility demotion) | provisional (689d PASS) | The manifest does **not** tag MECH-448. As a downstream OFC generalisation test, 485j *positively corroborates* it: C2 conversion is dissociated against the F-dominance control (ARM_1=0). Not weakened. |
| **MECH-263** sig-b (task-role discrimination) | candidate / substrate_ceiling / v3_pending / pending_retest | Tested fairly and **converted** (C2). Narrow-supports. |
| **MECH-263** sig-a (devaluation sensitivity) | (same claim; sig-a enumerated separately in the claim text) | **Not** tested under conditions where it could express itself: the devalued-state OFC range (0.02) is below the same-statistic non-vacuity floor (0.05), and the precondition that should have caught this gates the high-threat state instead. → substrate_not_ready, not a fair weakens. |
| **SD-033b** (OFC substrate) | candidate / substrate_ceiling / pending_retest | Same split: discrimination half supports; devaluation half non_contributory pending the devalued-head fix. |

The manifest's blanket "weakens against SD-033b + MECH-263" conflates a C2 conversion **success** with a C1 devaluation **non-vacuity floor breach**. Adjudicated split (§7).

---

## 4. Biological-reference triage

OFC outcome-devaluation (Rudebeck & Murray 2014; Dickinson & Balleine) is a faithful biological target, not a formal-definition import — no `/lit-pull` commission needed. The mammalian devaluation signature is a **re-ranking**: devalue an outcome and the agent shifts *away* from the action that leads to it. The REE translation gap is precise: the current driver renders devaluation as a *range collapse* (flatten the bias) rather than a *re-ranking* (actively down-bias the previously-preferred candidate / up-bias an alternative). A flat valuation removes OFC influence but does not, by itself, move a committed selection — so the behavioural readout cannot register a shift even when the underlying valuation is "correctly" devalued. This is a discovered prerequisite (devalued-state head must re-rank), not a falsification of MECH-263 sig-a.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **strengthened (C2) / unclear (C1)** | MECH-448 generalisation + MECH-263 sig-b corroborated; sig-a not fairly tested |
| Biological reference | clear | devaluation = re-ranking; driver renders it as range collapse |
| Prerequisites / dependency | present | demotion envelope, trained head, threat-conditioning all engaged (excluded_count=5) |
| Implementation completeness | **partial** | devalued-state head trains flat (anti-range), not re-ranking; C1 precondition gates the wrong state |
| Environment adequacy | adequate | OFC-isolated SD-054 bipartite reef/forage bank |
| **Measurement adequacy** | **under-instrumented (load-bearing)** | C1 readiness precondition keys the high-threat range, not the devalued-state range the DV routes on (V3-EXQ-642 same-statistic miss) |
| Integration adequacy | coupled | demotion + OFC arbitration compose; C2 confirms the path works |
| Scale / capacity | adequate | — |

Dominant diagnosis → **substrate_ceiling** (devalued-state OFC head re-ranking) compounded by a **measurement gap** (C1 precondition mis-targeted).

---

## 6. The recurrence (autopsy-stream signal)

This is the **5th** autopsy circling the SD-033b/MECH-263 OFC behavioural conversion:

| run | signature | route |
|---|---|---|
| 485e | range-starved bank | instrumentation |
| 485g | first non-vacuous; discrimination FAIL | queue-experiment |
| 485h | threat-invariant REFUTED (paired driver closed the gap) | implement-substrate |
| 485i | MECH-448 envelope all-admit no-op (excluded_count==0) | implement-substrate (calibrate floor) |
| **485j** | demotion engaged (excluded_count=5); **C2 converted**, C1 devalued-range collapse | **queue-experiment (this autopsy)** |

The lineage is a **convergent sequence of test-instrumentation / substrate-engagement fixes**, not divergent claim-pressure: each fixed a real gap, and 485j is the milestone where demotion finally engaged on the OFC channel AND a DV (discrimination) converted. MECH-263 is **already decomposed** into sig-a (devaluation) + sig-b (discrimination), so this is **not** granularity debt requiring `/claim-synthesis`; the residual is the narrow devaluation-signature test design. (`/claim-synthesis` hook noted and discharged.)

---

## 7. Learning + routing (user-confirmed 2026-06-21)

**Learning extracted:**
1. MECH-448 F->eligibility demotion **generalises off GAP-A foraging to the OFC channel** — first cross-substrate corroboration, via a clean 3-arm dissociation on the discrimination signature.
2. The OFC devaluation signature does not register a behavioural shift when the devalued-state head trains **flat (anti-range)** rather than **re-ranking** — a flat valuation removes OFC influence but cannot move a committed argmin.
3. A readiness precondition that gates a **different state** than the load-bearing DV routes on (high-threat range vs devalued-state range) lets a below-floor devalued arm masquerade as a fair `weakens` (the V3-EXQ-642 pattern). The same-statistic non-vacuity gate must key the **devalued-state** range for the C1 DV.

**Routing: `/queue-experiment` — corrected SD-033b devaluation behavioural arm (V3-EXQ-485k).** Two coupled fixes:
- (i) Devalued-state OFC head driver that produces a **re-ranking** differentiated bias at the devalued state (so devaluation moves the committed selection), **and/or** a C1 DV that reads the high-vs-devalued **bias-vector change** rather than a committed-argmax shift through a flat bias.
- (ii) **Re-target the C1 readiness precondition to the devalued-state bias range**, so a below-floor devalued range self-routes `substrate_not_ready_requeue` (non_contributory) instead of a false weakens.
- **NOT** envelope-floor recalibration (option a — the envelope fired correctly: excluded_count=5, winner≠F-argmin). **NOT** MECH-448 escalation (option b — contradicts the C2 conversion + ARM_1 dissociation).

**Governance impact (split per signature; MECH-448 NOT weakened):**
- **MECH-448 generalisation:** NOT weakened. C2 is positive corroboration that the demotion lever converts a downstream OFC channel. No governance debit.
- **SD-033b / MECH-263 sig-b (discrimination):** narrow-supports (C2 converted, ARM_1 control fails). Single-pathway caveat: this is the discrimination pathway only; pair with `pending_retest_after_substrate` (both claims already carry it).
- **SD-033b / MECH-263 sig-a (devaluation):** **non_contributory / substrate_not_ready_requeue**, `pending_retest_after_substrate` — **downgrade** the manifest's blanket `weakens`. Set `evidence_direction: superseded`/`non_contributory` with the note below; do not let it weight conflict ratio.
- **behavioral_diversity_isolation:GAP-I** (closes on the FIRST downstream conversion): reconcile to **PARTIAL conversion** — the discrimination signature converted (the demotion lever's OFC generalisation is demonstrated); the devaluation signature is pending V3-EXQ-485k. Surface to the user whether GAP-I's "first conversion" bar is met by the discrimination conversion or requires the full SD-033b behavioural PASS (both signatures).
- **commitment_closure:GAP-8** (SD-033b candidate→provisional behavioural evidence): unchanged — promotion still needs the full behavioural PASS (devaluation half pending 485k).

**Draft `evidence_quality_note` for governance to write on the 485j manifest / SD-033b+MECH-263 (do NOT write here):**
> V3-EXQ-485j (2026-06-21, ree-cloud-2): split result, manifest self-route `weakens / conversion_ceiling_persists_despite_demotion` DOWNGRADED by failure_autopsy_V3-EXQ-485j_2026-06-21. C2 task-role discrimination CONVERTED on the MECH-448 demotion-enabled E3 selector (between-context TV 1.0 on 2/3 seeds; ARM_1 demotion-off F-dominance control = 0.0 all seeds; ARM_0 silent) — first cross-substrate corroboration that the BG F->eligibility demotion lever generalises off GAP-A foraging to the OFC channel; MECH-448 NOT weakened. C1 devaluation did NOT convert because the OFC trained head's bias range collapses to ~0.02 (< the 0.05 non-vacuity floor) at the devalued state (anti-range driver trains flat-at-devalued, not re-ranking); the demotion envelope fired correctly (excluded_count=5, winner≠F-argmin) so this is orthogonal to f_eligibility_envelope_floor/dn_sigma. The C1 readiness precondition gated the high-threat range (0.377), not the devalued-state range (0.020) the DV routes on, so the devaluation arm is below the same-statistic non-vacuity floor → substrate_not_ready_requeue, NOT a weakens. Sig-b (discrimination): narrow-supports. Sig-a (devaluation): non_contributory, pending_retest_after_substrate; corrected re-queue = V3-EXQ-485k (re-ranking devalued-state head driver + C1 precondition retargeted to the devalued-state range).
