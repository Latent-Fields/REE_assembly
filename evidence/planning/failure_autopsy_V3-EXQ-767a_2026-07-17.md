# Failure Autopsy (ADJUDICATION) — V3-EXQ-767a (SD-025 curiosity-drive, continuous CEM score-margin)

- **Generated (UTC):** 2026-07-17T06:18:01Z
- **Scope:** single (diagnostic PASS adjudication)
- **Status:** confirmed
- **Skill:** `/failure-autopsy` (diagnostic adjudication path)
- **Verdict:** **REAL / non-vacuous PASS.** `evidence_direction: supports` confirmed. Route to `/governance`.
- **Analysis + handoff only.** No edits to `claims.yaml` / manifests / `substrate_queue.json`. SD-025 stays `candidate` until `/governance` acts on this artifact.

---

## 0. Why this needs adjudication

A diagnostic PASS's self-route (`interpretation.label`) is a hypothesis, not a verdict — it cannot drive an SD-025 governance action until adjudicated. 767a additionally **supersedes V3-EXQ-767**, which was adjudicated **vacuous / `measurement_degeneracy`** in the confirmed cluster autopsy `failure_autopsy_767-768-cluster_2026-07-16` (applied governance 2026-07-16d, REE_assembly `e40362ebb7`): 767's binary `pref_dense` argmin gate saturated at exactly 1.0 with zero cross-seed variance. The central adjudication question is therefore: **did the continuous re-operationalization actually resolve the degeneracy, or does the margin gate re-flag vacuous under a new guise?**

---

## 1. Target

| | V3-EXQ-767a |
|---|---|
| run_id | `v3_exq_767a_sd025_curiosity_drive_selection_bias_margin_20260716T201116Z_v3` |
| claim | SD-025 (`hippocampal_module.curiosity_drive`, design_decision, **candidate**, 2nd component of ARC-057) |
| purpose | diagnostic, 8 seeds |
| machine | ree-worker-3 (cloud, linux-x86_64-py3.10) |
| supersedes | `v3_exq_767_sd025_curiosity_drive_selection_bias` (adjudicated vacuous, 2026-07-16d) |
| outcome (self-routed) | PASS / `supports` |
| **adjudication (this autopsy)** | **REAL / non-vacuous — supports** |

Recording provenance **complete** — `substrate_hash` (`be9a4d7f2cae…`), full `config`, explicit `seeds [0..7]`, `machine` / `machine_class`, `elapsed_seconds` all present; `ree-v3/validate_recording.py` → 0 always-core gaps, 0 thin-pack drops. **No recording gap.**

---

## 2. Facts — the load-bearing statistics

767a replaces 767's saturating binary `pref_dense` argmin-fraction with the **continuous CEM score-margin** `margin = mean_trials[min(sparse-heading score) − min(dense-heading score)]` — a quantity already computed per-candidate inside `_pref_dense` (`experiments/v3_exq_767a…_margin.py:291`) and previously discarded. CEM minimises score, so `margin > 0` ⇔ the dense region wins the argmin; its **magnitude** reflects drive strength (`w · density_gap`). Same `cand_seed` replays identical candidates across arms (only scoring differs); counterbalanced across an A-dense and B-dense field so the harm-terrain geometry cancels and the OFF margin averages to a clean ~0.

| Criterion | Load-bearing | Meaning | Measured | Floor | Read |
|---|---|---|---|---|---|
| L1a margin_on | ✅ | dense is CEM elite by a graded margin | **39.26** (per-seed 26.95–45.61) | ≥1.0 | variance-bearing ✅ |
| L1b margin propagation-δ | ✅ | margin_on − margin_off; drive shifts the margin | **39.26** (OFF null = 0.0) | ≥1.0 | ✅ |
| L1c weight-independence | ✅ | zero benefit-value weights → margin unchanged (rel) | **0.0** | ≤0.1 | null by design ✓ |
| L2a antiperseveration margin | ✅ | WAKING familiarization drops margin toward familiarized region | **20.05** | ≥1.0 | ✅ |
| L2b MECH-094 replay-no-shift | (context) | non-waking replay must NOT raise familiarity | **0.0** | ≤0.5 | null by design ✓ |

Readiness preconditions **met**: `density_read_discriminates` = 58.32 (≥0.5); `selection_margin_responds_to_curiosity` positive control (curiosity_weight=3.0) = 78.76 (≥1.0).

Non-degeneracy guard (`:538–546`): `criteria_non_degenerate` = {`margin_on_varies_across_seeds`: **True**, `density_a_exceeds_b`: **True**, `on_margin_exceeds_off`: **True**} → `non_degenerate: true`.

**Pipeline cross-check:** regenerated `pending_review.md` (2026-07-17T06:19:53Z) reports **"0 diagnostic self-route(s) flagged for adjudication"** — 767a sits in the plain **PASS (verify & close)** section, **not** re-flagged `vacuous_pass`. The indexer's mechanical vacuity check (which flagged 767) passed here.

---

## 3. Why this is non-vacuous where 767 was vacuous

767's binary argmin `pref_dense` saturated at **exactly 1.0 on all 8 seeds, zero cross-seed variance** → it carried the drive's *sign* but no *magnitude* / effect-size. 767a's load-bearing statistic is the continuous margin, whose **sign is exactly the old binary decision** but whose **magnitude scales with `w · (density gap)`** — and the density gap already varies 58–80 across seeds. Result: `margin_on` varies **26.95–45.61**, carrying the effect-size the binary discarded.

Three structural facts make the PASS load-bearing rather than trivially-clearable:
1. The OFF null is a **hard 0.0 by counterbalance construction** (curiosity_weight 0 → no density term → the A-dense/B-dense margins cancel), not a noisy empirical baseline — so the 39.26 propagation-delta is measured against a zero-variance null.
2. The two "null-by-design" load-bearing/context criteria (L1c 0.0, L2b 0.0) sit exactly where a working mechanism predicts, discriminating the density path from the value path and waking from replay.
3. The `criteria_non_degenerate` guard **requires** `margin_on` to vary across seeds; the run cleared it on real variance, so the gate structurally cannot re-flag vacuous.

*(Effect-size-gate note: this is a drive-propagation **readiness diagnostic**, not a noisy-baseline effect-size promotion gate. The fixed absolute floor of 1.0 against an exact-0 counterbalanced null is appropriate; the SD-of-delta scaling rule that applies to noisy empirical baselines is not implicated here.)*

---

## 4. Claim-layer mapping

- **SD-025** — `design_decision`, `subject: hippocampal_module.curiosity_drive`, **status candidate**, `depends_on: SD-024, SD-004, ARC-057, MECH-111, INV-051`. Tags accurate (not inherited).

**Did the test let the claim express itself? Yes — and it expressed as the biology predicts.** The claim's scope is the **DRIVE MECHANISM only**. Its three asserted sub-mechanisms are each independently confirmed:
1. **Propagation** — the curiosity term propagates into hippocampal CEM elite selection as a graded score-margin (L1a/L1b). This is the propagation the broken MECH-111 broadcast-novelty→E3 path could not achieve (EXQ-141b / 590a).
2. **Weight-independent density read** — zeroing the benefit-value weights leaves the density-driven margin unchanged (L1c = 0.0; ARC-007-strict): selection routes on **density**, not on benefit **value**.
3. **Familiarity-discount anti-perseveration** — a WAKING-only familiarity EMA drops the margin toward a familiarized region (L2a = 20.05), while non-waking replay does not (L2b = 0.0, MECH-094 control).

Claim alignment: **strengthened**. Not a falsification of anything; a validation of the drive mechanism.

---

## 5. Biological-reference triage

| | closest mechanism | formal import? | divergence | lit status |
|---|---|---|---|---|
| SD-025 | curiosity / novelty-seeking drive biasing hippocampal trajectory selection toward representationally richer regions, discounted by a waking-only familiarity EMA | **no** — faithful drive instantiation | none | **present** (`targeted_review_sd_025`, landed 2026-07-17) |

No `/lit-pull` commission owed. Because this is a PASS, there is no missing-dependency signature to match — the mechanism expressed exactly as the reference predicts.

---

## 6. Four-layer diagnosis (all healthy; resolved layer bolded)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **strengthened** | drive mechanism validated; test let the claim express itself |
| Biological reference | clear | faithful drive instantiation; lit present |
| Prerequisites | present | SD-024 verified (766a); SD-004 implemented |
| Implementation | complete | drive + weight-independent read + familiarity EMA all functional |
| Environment | adequate | env-free selection test (drive-mechanism scope) |
| **Measurement** | **adequate (RESOLVED)** | continuous CEM score-margin is variance-bearing — this is the fix that resolved 767's `measurement_degeneracy` |
| Integration | coupled | curiosity term → CEM selection → familiarity EMA; works |
| Scale | adequate | 8 seeds; the fix was to the metric, not the sample |

**Recommended `epistemic_category`:** N/A (clean PASS — not a failure category). The prior failure category `measurement_degeneracy` (from 767) is **resolved** by the re-operationalization. **Recommended `evidence_direction`: `supports`** (confirmed, non-vacuous).

---

## 7. Learning + routing

**Learning extracted:**
- The 767→767a re-operationalization is a validated instance of the `mystery (known data)` repair: the data (per-candidate continuous scores, per-seed density gaps) already existed; only the readout frame (binary pref threshold) was wrong. Reframing to the continuous margin — *not* gathering more runs, *not* building substrate — resolved the degeneracy. This confirms the cluster autopsy's routing decision was correct.
- SD-025's drive mechanism is validated at the diagnostic level: curiosity propagates into hippocampal CEM elite selection with a graded, drive-strength-scaled margin, reads density weight-independently (ARC-007-strict), and is discounted by a waking-only familiarity EMA (anti-perseveration).

**Debt token:** none open — the `mystery (known data)` node the cluster autopsy identified is now **closed** by 767a.

**Routing: `/governance`.** Hand the confirmed-real `supports` evidence to the governance walk for the SD-025 `candidate` status decision. Governance owns any `claims.yaml` change.

- **Re-derive brake: NOT fired** — 0 prior `substrate_ceiling` / `non_contributory` autopsies tagging SD-025; and this is a confirmed PASS, not a ceiling reading.
- **Granularity-debt trigger: NOT fired** — the one prior autopsy on this target (`failure_autopsy_767-768-cluster`) is *resolved* here, not recurring with a new failure signature. A PASS confirming a re-op is not the granularity-debt pattern (which is recurring FAILs circling a claim in structurally different ways).
- **Scope guard:** validates the **single-drive mechanism only**. Does **NOT** promote ARC-057 (the env-constrained approach-emergence claim + the SD-024×SD-025 interaction; that is the sibling V3-EXQ-768a, still running on ree-cloud-4). 767a stands alone as the SD-025 drive validation.
- **`recommended_substrate_queue_entry.action = none`** — no substrate gap.

### Draft `evidence_quality_note` (for `/governance` to write on SD-025 — do not write here)

> 2026-07-17 governance (failure_autopsy_V3-EXQ-767a): V3-EXQ-767a — the continuous CEM score-margin re-operationalization of the vacuous V3-EXQ-767 — adjudicated **REAL / non-vacuous** (`supports`). The re-op resolved 767's `measurement_degeneracy`: the load-bearing statistic is now the continuous CEM score-margin `min(sparse) − min(dense)`, variance-bearing (margin_on 39.26, varies 26.95–45.61 across 8 seeds) and clearing the `criteria_non_degenerate` guard. All four load-bearing criteria PASS — propagation (margin_on 39.26 vs OFF null 0.0; propagation-δ 39.26), weight-independent density read (L1c 0.0 ≤ 0.1: zeroing benefit value leaves the margin unchanged → routes on density not value, ARC-007-strict), and waking-only familiarity-discount anti-perseveration (L2a 20.05; MECH-094 replay control L2b 0.0). Readiness met (density discrim 58.32; positive control margin 78.76). Recording complete (substrate_hash be9a4d7f; config; 8 seeds). This ADVANCES SD-025 drive-mechanism validation. Scope: DRIVE MECHANISM only — NOT the env-constrained ARC-057 approach-emergence claim; does not itself promote ARC-057 (interaction is V3-EXQ-768a). Supersedes 767's `inconclusive` note.

---

## 8. Routing summary for `/governance`

| Target | Adjudication | evidence_direction | epistemic_category | Route | Claim status |
|---|---|---|---|---|---|
| V3-EXQ-767a (SD-025) | REAL / non-vacuous | supports | N/A (PASS; 767 `measurement_degeneracy` resolved) | `/governance` (act on SD-025 supports) | stays candidate until governance acts |

*User scientific judgment (Step 8 gate, 2026-07-17): confirmed — margin PASS is REAL/non-vacuous, validates the SD-025 drive mechanism, route to /governance for the SD-025 supports evidence; governance owns any claims.yaml status change.*
