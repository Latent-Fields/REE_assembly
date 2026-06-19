# Failure Autopsy — V3-EXQ-445h (SD-032b / MECH-258 / MECH-260 dACC-analog adaptive control)

- **Generated (UTC):** 2026-06-19T14:23:23Z
- **Session:** failure-autopsy-445h-sd032b-20260619T1423Z
- **Scope:** cluster (whole V3-EXQ-445 series; single failure shape)
- **Status:** confirmed (user-adjudicated at the Step-8 gate 2026-06-19)
- **Target run:** `v3_exq_445h_sd032b_dacc_reef_20260508T002953Z_v3` (+ duplicate run `…063313Z`); FAIL, run-level `weakens`
- **Corroborates:** `2026-05-25_sd_032_baseline_contamination_cluster.md` + `failure_autopsy_V3-EXQ-455a_2026-05-25` (same monostrategy cause; that note's recommended structured field was never applied — this autopsy applies it).

---

## 1. Facts (no interpretation)

445h pass-criteria summary: **c1_mech258 PASS (2 wins) · c2_sd032b FAIL (0 wins) · c3_mech260 PASS (3 wins)** → run-level FAIL driven **solely by c2**.

Per-seed results (both 445h runs, all three seeds, both arms OFF / ON_INDEPENDENT):

| metric | value |
|---|---|
| `action_class_entropy` | **0.0 in every seed and every arm, including the OFF control** |
| `action_counts` | concentrated on a single action class per seed (≈134–1889 steps) |
| `harm_a_forward_r2` (ON) | ≈0.94 (seeds 42, 7); −0.89 (seed 13) → c1 = 2/3 wins |
| `mean_score_bias_abs` | **2.0 ON vs 0.0 OFF** (dACC bias applied at the clipped budget) |

Script criteria (`v3_exq_445h_sd032b_dacc_reef.py`):
- c1 (MECH-258): `harm_a_forward_r2 ≥ 0.3` in ≥2/3 seeds
- c2 (SD-032b): `|entropy_ON − entropy_OFF| ≥ 0.1` in ≥2/3 seeds
- c3 (MECH-260): `entropy_ON ≥ entropy_OFF` in ≥2/3 seeds

The whole 445-series (445 / 445a / 445b / 445c / 445f / 445g / 445h ×2 = 11 SD-032b manifests) shows `action_class_entropy = 0.0` across **every** seed and arm.

## 2. Open Question 1 — per-criterion split honoured? ✅ verified

The indexer applies `evidence_direction_per_claim` (`build_experiment_indexes.py:770`); per-claim keys override the run-level direction. Scored `claim_evidence.v1.json` confirmed (pre-correction): MECH-258→supports, MECH-260→supports, SD-032b→weakens. **MECH-258 and MECH-260 are NOT read as weakened by this run.** The run-level `weakens` does not bleed onto them.

## 3. Open Question 2 — adjudicating the SD-032b FAIL → precondition_unmet → **degenerate criterion**

`action_class_entropy = 0.0` in **all arms including the OFF control**, so c2's metric `|entropy_ON − entropy_OFF|` is **floor-locked at 0** and can never reach the 0.1 threshold regardless of whether SD-032b works. This is a vacuous / degenerate criterion (`CLAUDE.md` "Degenerate (vacuous-criterion) runs").

The dACC substrate **is functional**: `mean_score_bias_abs = 2.0` ON vs `0.0` OFF (the precision-weighted conflict bias is computed and applied at the clipped budget), and `harm_a_forward_r2 ≈ 0.94` ON. The applied bias simply **cannot move the committed action class** under the monostrategy — the F-dominance conversion ceiling (V3-EXQ-571: the primary harm/goal score F monopolises ~88–89 % of E3 committed-selection variance; "diversity must act at/after E3 scoring"). The dACC bias reaches the E3 accumulator but is drowned at the F-dominated committed argmin.

**Symmetric finding:** MECH-260's c3 PASS (`entropy_ON ≥ entropy_OFF`, won 3/3) is **vacuously true** (`0.0 ≥ 0.0`) for the same monostrategy reason. It is *not genuine support*. Only MECH-258's c1 (forward-model R², entropy-independent) is a genuinely contributory criterion in this run.

This is **not** a genuine weakening of SD-032b: the experiment did not test the claim under conditions where it could express itself.

## 4. Four-layer diagnosis (SD-032b / c2)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | the test could not let SD-032b express; not falsified |
| Biological reference | clear | dACC/aMCC adaptive control (Shackman 2011; Shenhav 2013 EVC; Seymour 2019 precision-weighted pain). Functional. |
| Prerequisites | **missing** | committed-action diversity (ARC-065 / MECH-439) absent — the upstream conversion ceiling |
| Implementation | complete | bias=2.0 applied; forward-model R²≈0.94 |
| Environment | adequate | reef-enriched 14×14; not the issue |
| Measurement | **misleading** | c2 (and c3) entropy criteria floor-locked by monostrategy — degenerate |
| Integration | partially coupled | bias composed into E3 score_bias but cannot move the F-dominated argmin |
| Scale | adequate | — |

**Recommended `epistemic_category` for SD-032b: `substrate_ceiling`** (V3-tractable in principle; the substrate is too coarse to deliver the behavioural-shift distinction the criterion needs — matches MECH-260's existing category).

## 5. Cluster pattern

| Experiment | Claim(s) | Negative-control / absolute | Discrimination | Read |
|---|---|---|---|---|
| 445 / a / b / c / f / g / h (×2) | SD-032b (c2), MECH-260 (c3) | OFF-arm `action_class_entropy = 0.0` | entropy-differential / entropy≥ both pinned at 0 | one structural property, not N bugs |

This is **one structural property** — every 445-series iteration was tested under a monostrategy regime where the OFF arm could not produce behaviourally diverse rollouts, so any entropy-based discrimination criterion is degenerate by construction. (Identical shape to the 2026-05-25 SD-032 baseline-contamination cluster; this autopsy applies the structured manifest field that note recommended but that was never written.)

## 6. Per-claim verdicts & promotion paths (the three claims are NOT in the same boat)

- **SD-032b** — c2 FAIL is **non-contributory (degenerate)**, not weakening. After correction, SD-032b has **no uncontaminated V3 experimental evidence either way** (exp_conf 0.413 → **0.0**; lit_conf 0.882; `plausible_unproven`). Remains gated on a **fixed-substrate c2 retest** once committed-action diversity is demonstrated.
- **MECH-258** — c1 (forward-model R²) is a **genuine support**, entropy-independent. exp_conf **0.89** (`confirmed_established`). Its only hold is the governance **`v3_pending` gate** (a human decision) — **not** missing evidence, and **not** gated on a fixed SD-032b validation. **Clean path to promotion.**
- **MECH-260** — c3 PASS is **vacuous** (excluded). exp_conf 0.951 → **0.799** (`confirmed_established`; driven by V3-EXQ-463, not 445). Status unaffected; already carries `substrate_ceiling` + `pending_retest_after_substrate`.
- **ARC-058** (shared-trunk vs independent) — **not tagged in 445h** (which ran only OFF vs ON_INDEPENDENT). exp_conf **0.0**, **untested**. 445h does **not** unblock it; it needs a dedicated shared-trunk-vs-independent arm.

## 7. Learning extracted

1. The dACC-analog conflict/precision substrate works (bias applied, forward model trained) but is **subordinate to the F-dominated committed argmin** — the same conversion ceiling MECH-439 / ARC-065 GAP-A attack.
2. A behavioural-shift criterion (committed-action entropy) is **degenerate on any pre-conversion-ceiling substrate** — the whole 445-series c2/c3 is non-contributory.
3. The 2026-05-25 cluster note's structured-field recommendation was never applied; the contaminated `weakens`/`mixed` had been dragging SD-032b's exp_conf down for ~6 weeks. **Now applied.**
4. MECH-258 already has the evidence its promotion needs; the framing that it is "blocked on V3 evidence" is incorrect — it is blocked on the governance gate.

## 8. Routing

| Target | Routing | Rationale |
|---|---|---|
| SD-032b | **queue-experiment** (gated) | fixed-substrate c2 retest under GAP-A top-k / MECH-439 conflict-grade, once committed-action diversity is demonstrated (V3-EXQ-569i PASS, V3-EXQ-689 queued). New EXQ letter/number — **never** re-run under 445h. |
| MECH-258 | **governance** | surface for promotion review; clean exp evidence; only the `v3_pending` gate holds it. |
| MECH-260 | **governance note** | vacuous 445 support excluded; status unaffected. |
| ARC-058 | **queue-experiment** | dedicated shared-trunk-vs-independent arm; not provided by 445h. |

Substrate: **no new substrate_queue entry** — the committed-action-diversity gap SD-032b's c2 needs is already owned by `modulatory-bias-selection-authority` / ARC-065 GAP-A / MECH-439 (V3-EXQ-569i PASS; V3-EXQ-689 queued). SD-032b's c2 retest is the downstream beneficiary.

## 9. Manifest correction applied (this session)

On all 11 SD-032b 445-series manifests (top-level flat overlay `evidence/experiments/<run_id>.json`, faithful to the pack direction + the correction fields):
- `non_degenerate_per_claim: {"SD-032b": false, "MECH-260": false}`
- `pending_retest_after_substrate_per_claim: ["SD-032b", "MECH-260"]`
- `degeneracy_reason: <monostrategy floor-lock; see §3>`

Index rebuilt. Effect: SD-032b 0.413 → 0.0; MECH-260 0.951 → 0.799; MECH-258 0.89 (preserved); ARC-033 0.708 (preserved); ARC-058 0.0 (unchanged). MECH-258's genuine c1 supports (445a/b/c/f/g/h) remain `excl=None`.

## 10. Governance recommendation (NOT applied — human-in-the-loop)

Surfaced for the user; **claims.yaml was not edited**:
- Set SD-032b `epistemic_category: substrate_ceiling` + `pending_retest_after_substrate: true` (mirrors MECH-260).
- Draft `evidence_quality_note` for SD-032b: *"All V3-EXQ-445-series c2 evidence is non-contributory — the committed-action-entropy criterion is floor-locked by the pre-conversion-ceiling monostrategy (F-dominance, V3-EXQ-571). The dACC substrate is functional (bias applied, forward model trained) but cannot move committed action until ARC-065 GAP-A / MECH-439 demonstrate committed-action diversity. pending_retest_after_substrate."*
- MECH-258: consider promotion review (exp_conf 0.89 confirmed_established; held only by the v3_pending gate).
- ARC-058: remains untested; queue a shared-trunk-vs-independent experiment.
