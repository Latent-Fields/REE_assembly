# Failure autopsy -- V3-EXQ-1038a (ARC-131 / SD-091)

**STATUS: `confirmed`** -- interactive Step 8 gate held 2026-09-17.

| | |
|---|---|
| run_id | `v3_exq_1038a_arc131_coalition_recruitment_commensurability_probe_20260917T001717Z_v3` |
| queue_id | V3-EXQ-1038a |
| claims | ARC-131 |
| purpose | `diagnostic` (excluded from scoring) |
| outcome | **PASS** -- F1 passed, F2 failed, exactly-one -> routed here |
| self-route | `commensurability_partially_collapses_scale_spread` |
| machine | DLAPTOP-4.local, `darwin-arm64-py3.13-torch2.12.0`, 11798 s |
| predecessor | `failure_autopsy_V3-EXQ-1038_2026-09-14` (confirmed) |

This run is the probe the CONFIRMED 1038 autopsy **gated the SD-091 build on**. It has returned.

---

## 1. Is the PASS real or degenerate? Both, separably.

**The OUTCOME scalar is vacuous by design, and the manifest says so.** G0 -- the only `load_bearing` criterion -- is a `1e6` margin-threshold guaranteed-fire control against observed margins never exceeding ~131. Once the 8 instrument/premise gates clear, `outcome = PASS` unconditionally of the science. PASS means "a valid instrument-verified measurement was obtained", nothing more, and **must not be read as evidence for ARC-131**.

**Two further gates are near-circular** -- found at Step 7c, not in the first draft. `eligibility_fraction` is the empirical **CDF at 0.05** of a cell's margin samples; it is regressed against the **median of those same samples**. Spearman between a median and a CDF-at-a-fixed-point is monotone by construction unless cell shapes cross. So:

- **G3b** (off-arm |rho| 0.991 vs a 0.6 floor) is close to an arithmetic identity, not evidence the OFF arm is "scale-determined".
- **F2** could only pass if the operator equalised the cells almost exactly.
- **The non-circular form of F2 flips it.** Regressing the OFF-arm median (intrinsic scale, *before* the operator) against ON eligibility gives **|rho| = 0.321, which PASSES the 0.4 bar.**

**What survives, on non-circular statistics only:** F1's measured collapse (cross-seed median-margin ratio **783.81 -> 4.67**), a residual ON-arm eligibility spread of **5.48x** with CV **0.449**, and the pre-registered post-hoc below.

## 2. The pre-registered post-hoc -- run at autopsy, zero compute

The driver pre-registered this **for this autopsy** (`scale_association_detail.post_hoc_for_autopsy`) and the first draft never ran it. Re-thresholding the run's **own banked margin samples** at `0.05 * (cell_median / pooled_ON_median)`:

| | CV | spread max/min | \|rho\| vs median |
|---|---|---|---|
| fixed 0.05 (as shipped) | 0.4488 | 5.483 | 0.9643 |
| **scale-relative** | **0.1240** | **1.446** | **0.2111** |

**This is the load-bearing evidence for the routing** -- a non-circular, zero-compute existence proof that the residual *is* scale and that a scale-relative threshold is the repair. It replaces a mechanism that was false (W1).

## 3. The adjudication the driver asked for -- "which half and why"

**WHICH HALF:** F1 (magnitude) moved. F2 as implemented did not -- but F2 as implemented is near-circular and its non-circular form passes.

**WHY:** commensurability equalises channels, but the recruitment DV is the top-2 gap of the **summed** score, and each channel is divided by a *different* divisor before summing -- a reweighted, not monotone, transform. It **reshuffles** which seeds are large (cross-arm rank rho **0.143**; **0 of 7 seeds keep their rank**) and leaves a 4.67x residual spread that a **constant 0.05 gate** still reads. The gap is the fixed gate, not the operator's failure to normalise.

## 4. Four-layer diagnosis

| Layer | Status |
|---|---|
| Claim alignment | not exercised as a test of ARC-131; informative about SD-091 |
| Biological reference | partial -- real circuits pair normalisation with **adaptive** thresholds; this substrate pairs it with a constant |
| Prerequisites | present, but **weaker than first graded**: G3 is genuinely empirical, **G3b is not** |
| Implementation | complete for the manipulation (enable path asserted per-arm; warmup crossed; DV moved on every seed) |
| Environment | adequate (7 seeds x 2 arms x 20 episodes x 250 ticks) |
| Measurement | **adequate** for the routed DV -- the predecessor's verification criterion is met (worst cell 4 against a ceiling of 5) |
| Integration | coupled and stable for this question |
| Scale | adequate |

**Failure location (GOV-FAILLOC-1):** mechanism `not_established`, measures **`established`**, environment `established`, REE **false**. **Net: MIXED**, and explicitly not a REE-level failure -- what failed is the *pairing* of a magnitude normaliser with a fixed gate, a design gap.

## 5. Routing

**`implement-substrate`** -- debt class **`complicated (buildable)`**. The probe has returned and resolved the open question; the post-hoc already demonstrates the repair on banked data.

**Substrate queue: `amend` SD-091.**
- `depends_on_unresolved` is the **UNION**, retaining `f_dominance_conversion_ceiling (status build_owed, severity corrupting)` -- an amend supplying a list in full **replaces**, so omitting it would silently drop a dependency CONFIRMED governance placed there. It does not block the reclassification (that entry is itself `complicated (buildable)`).
- `severity` / `substrate_paths` deliberately unchanged.
- **Title flagged, not changed:** the live title still describes the star-topology primitive and does not describe the owed build at all; the 1038 autopsy proposed a better one that **appears never to have been applied**. Governance's call.

**REFUSED,** with a number rather than an assertion: a further commensurability re-pose (longer warmup, tuned EMA). The post-hoc shows the residual is removed by changing the **threshold**, not the operator.

## 6. Gates

- **Re-derive brake: DOES NOT FIRE.** ARC-131 count **0** (1 tagging target, 0 counting hits).
- **Granularity-debt trigger: DOES NOT FIRE.** 1 target, alignment `other=1`, no `weakened` reading -- checked by hand, not just by the reader's bucket.
- **Step 7b: 0 fires**, and C1/C2/C3 were *applicable*, so this is a genuine clean report.
- **Step 7c: `CONTESTED`**, run on the **session model (Opus 5) -- a SAME-MODEL pass** (fable unavailable, monthly spend limit; skill's stated fallback). 6 verdict-moving findings, **all accepted and applied**; 7 items verified correct.

## 7. Withdrawn arguments

**W1 -- "commensurability is order-preserving."** **Falsified.** Cross-arm rank rho 0.143; 0 of 7 seeds keep rank; seed 5 moves smallest -> 5th, seed 1 largest -> 3rd. The operator's docstring says rank-preserving *within a channel*; the DV is the top-2 gap of the summed score. The general "normaliser + fixed gate" fingerprint must **not** be exported to other operators on this basis.

**W2 -- "F1 and F2 are two strongly-separated measurements."** Withdrawn for F2 (near-circular; its non-circular form passes). F1's collapse stands.

**W3 -- "the premise gates could have failed"** as applied to G3b. Withdrawn; retained for G3, G1, G1b, G1c, G2.

**W4 -- "the 1038 instruction was superseded."** Withdrawn as a misreading: the instruction was a disjunction ("report requests per ELIGIBLE OPPORTUNITY, **and/or** raise TICKS_PER_EPISODE"), and `eligibility_fraction` is precisely its first branch. Nothing was superseded.

## 8. Frozen ledger

New question `arc131_sd091_recruitment_scale_invariance` (Mode A + same-cycle Mode B). 3 legs across three distinct axis families: **H-comm-suffices** (representation) **ELIMINATED**; H-scale-relative-threshold-owed (arbitration) alive; H-operator-amplifies (substrate) alive, owned by the OPEN V3-EXQ-1012a. Growth-restriction check inapplicable -- new question.

**User decision at the gate:** keep the elimination with `met_elimination_bar: true` on a basis rewritten onto **non-circular statistics only** (residual spread 5.48x, CV 0.449, and the post-hoc), with an explicit circularity caveat recorded on the leg. F2's 0.964, G3b's 0.991, and F2's non-degeneracy certificate (which is gated on G3b) are **not** relied upon.

## 9. Owed to `/governance`

1. Apply `per_claim_recommendation` -- ARC-131: direction and category stand; `diagnostic_evidence_adjudicated` is **already true**, so the applicable edit is the **citation stamp** plus the drafted note.
2. Amend SD-091 per section 5, **including the union dependency list**.
3. Decide the title discrepancy.
4. Mark the run reviewed.
5. Chip the SD-091 build. This session spawned no chip off its own unreviewed routing.
