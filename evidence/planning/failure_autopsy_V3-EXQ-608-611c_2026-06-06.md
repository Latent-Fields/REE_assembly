# Failure Autopsy -- V3-EXQ-608 + V3-EXQ-611 / 611c (MECH-341 E3 score-diversity chain)

- **Generated (UTC):** 2026-06-06T09:50:16Z
- **Author session:** failure-autopsy-V3-EXQ-608-611c-20260606T0950Z
- **Scope:** cluster (3 runs, one shape)
- **Status:** confirmed (interactive gate answered 2026-06-06 -- "Accept as stated")
- **Targets:**
  - `v3_exq_608_mech341_e3_score_collapse_diagnostic_20260526T025832Z_v3` (V3-EXQ-608) -- PASS, self-route `R2a_e3_collapse_confirmed_large_gap`
  - `v3_exq_611_mech341_substrate_readiness_4arm_20260527T130213Z_v3` (V3-EXQ-611) -- FAIL (substrate-readiness)
  - `v3_exq_611c_mech341_retune_6arm_20260529T184549Z_v3` (V3-EXQ-611c, supersedes 611b) -- PASS
- **All three:** `experiment_purpose=diagnostic`, `evidence_direction=non_contributory`, `claim_ids=["MECH-341"]` but **non-weighting** in confidence / conflict scoring.
- **Bears on (cited, not weighted):** MECH-341 (`candidate`, `v3_pending=true` throughout -- never promoted by this chain), ARC-065, behavioral_diversity_isolation_plan.md R2.a/R2.c rules.
- **Motivation:** priority #2 in `retrospective_diagnostic_selfroute_audit_2026-06-06.md` (Section 2 rows for 608 + 611/611c; Section 4 item 2). The 608 self-route drove the MECH-341 substrate landing + master merge; the 611->611c retune chain drove R2.c routing to the behavioural successor.

---

## 1. Verdict (one line)

The 608 self-route is **sound in direction but produced by an ill-posed labeling
metric**; the 611c PASS is a **vacuous-pass-adjacent substrate-readiness clear**
(gate satisfied on a wiring criterion + a near-vacuous diversity criterion while
the load-bearing efficacy criterion FAILED); the **master merge was an
appropriately-scoped substrate landing** (claim never promoted); and the **R2.c
routing premise was questionable but caused no durable harm and was
self-corrected downstream** (614a/614b/616/614d + the modulatory-bias-selection-
authority substrate). No claim was ever falsely promoted; no demotion, re-queue,
lit-pull, or new substrate is warranted.

The audit's specific concern -- "a near-zero seed (~0.0076) undercuts the
large-gap majority" -- is **factually incorrect** (the 0.0076 is a single
per-TICK gap value, not a per-seed figure; no seed is near-zero). But it pointed
at a real, different defect: the `frac_e3_collapse` label is driven by a
**self-referential per-seed epsilon** that is **non-monotonic in gap magnitude**.

---

## 2. Facts reconstruction (no interpretation)

### V3-EXQ-608 (the diagnostic)

Per-seed (P1 measurement window; SP-CEM main path, `frac_pre_ge2=1.0` every seed):

| seed | n_p1_pre_ge2 | mean_top2_class_gap | score_gap_epsilon | frac_e3_collapse_above_eps | frac_near_tie | label |
|------|--------------|---------------------|-------------------|----------------------------|---------------|-------|
| 42 | 1060 | 0.378 | 0.090 | 0.858 | 0.142 | R2a_collapse_confirmed_large_gap |
| 43 | 7249 | 0.269 | 0.030 | 0.990 | 0.010 | R2a_collapse_confirmed_large_gap |
| 44 | 248  | 0.597 | 0.116 | 0.762 | 0.238 | inconclusive_resample_heavier |

- `cross_seed_interpretation.majority_label = R2a_e3_collapse_confirmed_large_gap`, 2 of 3, not unanimous.
- Committed-class counts vary **across** ticks: seed 42 `{0:426,1:99,2:90,3:443,4:2}`; seed 43 `{1:2820,2:4429}`; seed 44 `{2:9,4:239}`. The selected/committed class is **not** the same every tick (the noise-floor / MECH-313 resampling produces cross-tick variety); the "collapse" the metric scores is **within-tick** (one class wins that tick's scoring by a margin).
- Per-tick `top2_class_gap` spans ~0.008 .. 1.12 within a single seed (e.g. seed 42 tick 25 = 0.00759 -- this is the audit's "0.0076", a per-tick value).

### V3-EXQ-611 (substrate-readiness, FAIL)

ARM_0_ALL_OFF (reproduces the 608 R2.a baseline), per-seed:

| seed | mean_top2_class_gap | score_gap_epsilon | frac_e3_collapse | selected_entropy_nats | label |
|------|---------------------|-------------------|------------------|-----------------------|-------|
| 42 | 0.411 | 0.078 | 0.843 | 0.959 | R2a_collapse_confirmed_large_gap |
| 43 | 0.280 | 0.029 | 0.983 | 0.343 | R2a_collapse_confirmed_large_gap |
| 44 | **1.969** | **1.330** | **0.281** | 0.385 | **R2b_e3_preserves_diversity** |

- Acceptance: `C1_substrate_fires_in_on_arms=FALSE` (the FAIL cause), C2/C3/C4/R2c TRUE.
- Root cause of C1 FALSE (per claims.yaml MECH-341 implementation_note + CLAUDE.md retune entry): ARM_2 `n_stratified_fired=0` across all 3 seeds -- `stratified_select` was gated to the **committed** branch, never entered during measurement; ARM_1/3 `entropy_bonus_max_abs` 0.023-0.044 << observed gap 0.27-1.96 (fires but cannot move selection at `bias_scale=0.1`).

### V3-EXQ-611c (retune, PASS, supersedes 611b)

Acceptance criteria (verbatim from manifest):
- `C1_stratified_fires_all_on_arms = TRUE` (all four ON arms fire)
- `C2_entropy_bonus_scale_commensurate = FALSE` (all entropy arms)
- `C3_single_arm_produces_diversity = TRUE` (all arms)
- `C4_both_scale_monotone = TRUE`, `R2c_readiness = TRUE`

Per-arm `mean_selected_class_entropy_nats`:

| arm | cfg | majority_label | mean_selected_entropy |
|-----|-----|----------------|-----------------------|
| ARM_1 OPT1 scale 1.0 | entropy_bonus | R2a_collapse_confirmed | 0.582877 |
| ARM_2 OPT1 scale 2.0 | entropy_bonus | R2a_collapse_confirmed | **0.582877** (identical to ARM_1) |
| ARM_3 OPT2 scale 1.0 | stratified | R2a_collapse_confirmed | 0.581949 |
| ARM_4 OPT2 scale 2.0 | stratified | R2a_collapse_confirmed | **0.581949** (identical to ARM_3) |
| ARM_5 BOTH scale 1.0 | both | R2a_collapse_confirmed | 0.590220 |
| ARM_6 BOTH scale 2.0 | both | R2a_collapse_confirmed | **0.590220** (identical to ARM_5) |

- PASS gate (script:797-802): `total_completed >= 9 AND c1_holds AND (c2_holds OR c3_holds)` = TRUE AND (FALSE OR TRUE) = **TRUE**.
- `decision_rule_thresholds` are **byte-identical** to 611 (0.8 / 0.5 / 0.2 / 0.05).
- Post-PASS (claims.yaml implementation_note): defaults bumped `entropy_lambda 0.05->0.5`, `bias_scale 0.1->1.0` -- an **unvalidated config change made after the validating run**.

---

## 3. Claim-layer mapping

- MECH-341 (`ethics_engine_3.scoring_trajectory_class_diversity_preservation`): `claim_type: mechanism_hypothesis`, `status: candidate`, `v3_pending: true`, `implementation_phase: v3`. **Status unchanged across the entire 608/611/611c chain** -- these are diagnostics, `non_contributory`, tagged but non-weighting. The "rule promotion path" routes the next *experiment*, not the claim status.
- `claim_ids` accuracy: the MECH-341 tag is on a diagnostic that does not weight the claim; no inherited-tag contamination of confidence. (One adjacent hygiene note already actioned by governance: V3-EXQ-610b dropped a mis-applied MECH-341 tag, per claims.yaml.)
- Did the experiments let the claim express itself? Partly. 608 measured the gap MECH-341 targets (large within-tick score gap with `frac_pre_ge2=1.0`) -- correctly motivating substrate work. 611c measured only that the substrate **fires** + that >=2 classes are selected; it did **not** test that MECH-341 **preserves** diversity (the efficacy criterion C2 failed).

---

## 4. Biological-reference triage

- Closest mechanisms: A3C-style entropy regularisation adapted to the local candidate-pool first-action categorical axis (Mnih 2016) for Option 1; OFC value-comparison that preserves option-distinct value signals through the comparison stage (Padoa-Schioppa & Conen 2017) for Option 2. Both are valid biological renderings; the substrate is **not** a formal-definition import with an unexamined divergence. **No lit-pull commission warranted.**
- The failure does not resemble a missing biological dependency. It is a **measurement / acceptance-logic** defect, not a substrate or claim defect.

---

## 5. Root-cause mechanics

### 5a. The 608/611 `frac_e3_collapse` self-referential epsilon (measurement defect)

`script:537-539`: `score_range = max(top2_gaps_pre_ge2) - min(top2_gaps_pre_ge2);
epsilon = max(score_range * 0.05, 1e-6)`. The docstring claims the threshold is
"pre-registered, never derived from this run" -- true of the **multiplier** (0.05),
**false** of the operative **epsilon value**, which is 5% of each seed's **own**
observed gap range. Consequence: `frac_e3_collapse_above_eps` measures
**gap-distribution dispersion shape**, not absolute gap magnitude. A seed with
tightly-clustered moderate gaps (611 seed 43: epsilon 0.029) scores
`frac_e3_collapse=0.98`; a seed with widely-dispersed gaps including some large
ones (611 seed 44: epsilon 1.33) scores `frac_e3_collapse=0.28` **even though its
mean gap (1.97) is ~7x larger** -- and is therefore labeled
`R2b_e3_preserves_diversity`. **The seed with the largest gaps is classed as
preserving diversity.** The metric is non-monotonic in the very quantity its
label names.

The *scientific* conclusion (E3 has a decisive within-tick class winner by a
margin that dwarfs the proposed bias magnitudes; selection entropy 0.34-0.96 nats
is low) is **robust** -- it holds on every seed regardless of the epsilon. Only
the *label* that converts it to `R2a` vs `R2b` is fragile. The 608 routing
decision ("do MECH-341 substrate work") was correct; the labeling apparatus that
produced it is ill-posed and should not be reused as-is.

### 5b. The 611c `(C2 OR C3)` acceptance disjunction (vacuous-pass)

PASS gate = `c1_holds AND (c2_holds OR c3_holds)`:
- **C1** = `stratified_select` fires on all ON arms -- a **wiring / reachability** check.
- **C2** = `entropy_bonus_max_abs >= 0.7 * scale` on a majority of seeds -- the **efficacy** criterion (can the bonus actually compete with the score gap). **FALSE.**
- **C3** = some arm has >=2 selected classes on a majority of seeds -- **near-vacuous**: the OFF baseline (608 seed 42, 611 ARM_0) already selects 4 classes per seed. C3 is a property of the candidate pool + downstream noise-floor resampling, **not** of the MECH-341 substrate.

The disjunction lets the near-vacuous C3 substitute for the failed efficacy C2.
The PASS narrative ("substrate either drives meaningful score perturbation OR
substrate-natural pool diversity survives selection") conflates "diversity
survives" (true even with the substrate OFF) with "the substrate makes diversity
survive." Decisive tell: `mean_selected_class_entropy` is **byte-identical across
`bias_scale` 1.0 vs 2.0** in every arm and barely above the OFF baseline (~0.58 vs
~0.56); the scale knob has **zero causal effect**, and every arm **still routes
`R2a_collapse_confirmed`**. The 611c PASS validated "wired and fires," not
"preserves diversity."

### 5c. Why the 611->611c retune is NOT threshold-fitting

The `decision_rule_thresholds` are byte-identical across 611 and 611c. The 611
FAIL was an instrumentation failure (`stratified_select` reachable only on a
never-entered branch). The retune (call-site expansion to both branches) is a
legitimate bug fix that makes the substrate reachable. The defect is not a moved
threshold; it is that the **acceptance logic itself** (the `(C2 OR C3)`
disjunction) lets a wiring + near-vacuous-diversity PASS read as efficacy
validation. The post-PASS 10x default bump (`lambda 0.05->0.5`,
`bias_scale 0.1->1.0`) is a separate, unvalidated parameter change riding on that
vacuous pass.

### 5d. Master merge + R2.c routing

- The **master merge** is a substrate **landing** (`e3_score_diversity.py` +
  `e3_selector.py` call-site expansion): contracts pass, bit-identical OFF, claim
  stays candidate/v3_pending. Appropriately scoped; rests on "the code is correct
  and wired," not on the diagnostic interpretation. This is the low-stakes
  substrate-landing class (audit Section 3).
- The **R2.c routing** to the behavioural successor (V3-EXQ-614) rested on the
  questionable 611c "fires => preserves" premise -- but it was load-bearing on no
  claim status and was **self-corrected downstream**:
  - 614a: `PASS_C2_C3_only_mech341_load_bearing_in_stack_only` (B_only does not independently produce diversity).
  - 614b / 616: in-isolation Rung-1 clearance is structurally bounded at the proposer layer; "uniform additive bias cannot move a single-class CEM proposer output."
  - 614c / **614d (2026-06-03)**: the within-class lever is "ACTIVE but has ZERO authority at committed-action selection -- a THIRD convergent instance of the **modulatory-bias-selection-authority** gap (cf. 604a curiosity_bias, 624a vigor)."
  - The real fix -- the **modulatory-bias-selection-authority** substrate (2026-06-03, gap-relative scaling, `ready=true`) -- now lists **MECH-341 in `unblocks_claims`**. The MECH-341 committed-diversity efficacy re-test is already gated there.

---

## 6. Four-layer diagnosis (cluster)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | MECH-341 candidate/v3_pending throughout; correctly recharacterised "score-layer preserver, not in-isolation generator". Not weakened, not falsely promoted. |
| Biological reference | clear | Mnih 2016 entropy reg / Padoa-Schioppa OFC preservation; no formal-import divergence; no lit-pull needed. |
| Prerequisites / dependency | present | SP-CEM upstream supplies >=2 classes (`frac_pre_ge2=1.0`); the substrate has its inputs. |
| Implementation completeness | complete | code wired, reachable, fires (611c C1=TRUE). The defect is in the *acceptance logic*, not the substrate. |
| Environment adequacy | adequate | SD-054 reef env, matched to 543k/605 main-path wiring. |
| Measurement adequacy | **under-instrumented / misleading** | 608/611 `frac_e3_collapse` self-referential epsilon (non-monotonic in gap); 611c `(C2 OR C3)` disjunction lets near-vacuous C3 carry the PASS. |
| Integration adequacy | partially coupled but inert | small additive bias drowned by raw score gap -- the convergent cluster finding (604a/624a/614d). |
| Scale / capacity | n/a | not a capacity question. |

**Recommended epistemic_category:** `vacuous_pass` adjudication on the **611c**
gate (cleared on a wiring criterion + a near-vacuous diversity criterion while
the load-bearing efficacy criterion was FALSE); `measurement_test_design_defect`
on the **608/611** `frac_e3_collapse` metric. No `substrate_ceiling`, no
falsification. (Recommendations only; not written to any manifest by this skill.)

---

## 7. Cluster pattern

| Run | Criterion that "passed" | Criterion that actually failed / was vacuous | Read |
|---|---|---|---|
| 608 | majority `R2a_large_gap` (2/3) | label is non-monotonic in gap magnitude (seed-44 inversion in 611 ARM_0) | sound science, ill-posed label |
| 611 | C2/C3/C4/R2c | C1 (substrate fires) -- instrumentation gap | honest FAIL; routed the legitimate call-site fix |
| 611c | C1 (fires) + C3 (>=2 classes, near-vacuous) | C2 (scale-commensurate efficacy) FALSE; entropy scale-invariant | vacuous-pass: wiring + near-vacuous diversity read as efficacy |

**Structural property (not 3 independent bugs):** the additive score-diversity
biases (entropy bonus, stratified select, and later the within-class temperature)
**fire but have no authority over the committed argmin** because they are small
additive perturbations on a primary score whose raw gap is much larger. This is
one structural property -- the **modulatory-bias-selection-authority** gap -- that
608/611c are early, under-adjudicated members of, alongside 604a (curiosity),
624a (vigor), and 614d (within-class temperature). The gap-relative-authority
substrate (2026-06-03) is the structural fix.

---

## 8. Learning extracted

1. **The 608/611 `frac_e3_collapse` metric is ill-posed for reuse.** Its epsilon
   is 5% of each seed's own gap range, making the `R2a`/`R2b` label non-monotonic
   in gap magnitude (the seed-44 inversion: largest gap -> "preserves diversity").
   Before this R2-style metric stack is ever reused, replace the self-referential
   per-seed epsilon with an absolute / fixed-reference threshold (e.g. epsilon
   tied to the candidate-bias magnitude or a fixed score-range reference), so the
   "collapse" label tracks collapse magnitude rather than dispersion shape.
2. **"Substrate fires" is not "substrate works."** The 611c `(C2 OR C3)`
   disjunction let a wiring criterion (C1) + a near-vacuous diversity criterion
   (C3, true even OFF) carry a PASS while the load-bearing efficacy criterion (C2)
   FAILED. This is exactly the `vacuous_pass` failure mode the
   diagnostic-adjudication gate (2026-06-06) names; the byte-identical
   entropy-across-`bias_scale` is the machine-detectable tell.
3. **The convergent finding is already actioned.** 608/611c are early members of
   the modulatory-bias-selection-authority cluster; the substrate that fixes it
   (gap-relative scaling, 2026-06-03) already lists MECH-341 in `unblocks_claims`,
   so the MECH-341 committed-diversity efficacy re-test is already gated. No new
   substrate is needed.

---

## 9. Routing decision (user-confirmed: "Accept as stated")

**Primary route: governance-record only.** No claim status change, no demotion,
no re-queue, no lit-pull, no new substrate.

- `recommended_substrate_queue_entry.action = "none"` -- the
  **modulatory-bias-selection-authority** substrate already exists
  (`ready=true`, 2026-06-03) and already lists MECH-341 in its `unblocks_claims`;
  the committed-diversity efficacy re-test is already gated there per the 614d
  review. Minting a new substrate entry would duplicate it.
- `pending_retest_after_substrate: true` (MECH-341 stays candidate / v3_pending;
  efficacy re-test gated on the modulatory-authority substrate).

**Handoff notes carried (user deferred to autopsy judgment; 1 + 3 included,
2 skipped):**

1. **Flag the 608/611 epsilon as ill-posed** (Section 8.1) -- the one finding no
   other artifact captures; a metric-design caveat for any future reuse of the
   R2 readiness-diagnostic metric stack.
2. *(skipped)* A fresh MECH-341 `evidence_quality_note` addendum flagging 611c as
   wiring-not-efficacy would be **redundant** -- the existing note already records
   `C2=False`, and 614a/614b/616/614d already recharacterise MECH-341 as a
   "score-layer preserver, not in-isolation generator." No new information.
3. **Confirm the linkage** (Section 8.3) -- record that 608/611c belong to the
   modulatory-bias-selection-authority convergent cluster, justifying
   `action=none` and preventing a duplicate substrate mint.

**No `claims.yaml` / manifest / `evidence_direction` / `review_tracker.json` /
`substrate_queue.json` edits from this autopsy** (analysis + handoff only;
governance owns any later record).

**Draft `evidence_quality_note` for governance (do NOT write here; optional --
the existing MECH-341 note already covers the substance):**
> V3-EXQ-608/611/611c failure autopsy (failure_autopsy_V3-EXQ-608-611c_2026-06-06):
> the 608 `R2a_e3_collapse_confirmed_large_gap` self-route is sound in direction
> (large within-tick score gap, low selection entropy) but produced by an
> ill-posed `frac_e3_collapse` metric whose per-seed epsilon (5% of the seed's
> own gap range) is non-monotonic in gap magnitude. The 611c PASS is
> vacuous-pass-class: gate = C1(substrate fires) AND (C2 OR C3); C2 (efficacy)
> FALSE, C3 (>=2 classes) near-vacuous (true OFF), entropy byte-identical across
> bias_scale 1.0/2.0. Master merge was an appropriately-scoped substrate landing;
> MECH-341 was never promoted (candidate/v3_pending throughout). The convergent
> drowning finding is already actioned by the modulatory-bias-selection-authority
> substrate (2026-06-03), which lists MECH-341 in unblocks_claims;
> pending_retest_after_substrate=true.

---

## 10. Cross-references

- Manifests: `REE_assembly/evidence/experiments/v3_exq_608_mech341_e3_score_collapse_diagnostic_20260526T025832Z_v3.json`, `..._v3_exq_611_mech341_substrate_readiness_4arm_20260527T130213Z_v3.json`, `..._v3_exq_611c_mech341_retune_6arm_20260529T184549Z_v3.json`.
- Scripts: `ree-v3/experiments/v3_exq_608_mech341_e3_score_collapse_diagnostic.py` (epsilon: lines 537-539), `..._v3_exq_611c_mech341_retune_6arm.py` (PASS gate: lines 797-802; C2/C3 defs: 742, 753-759).
- Claim: `REE_assembly/docs/claims/claims.yaml` MECH-341 (status candidate/v3_pending; implementation_note records the 611c C2=False + the 614a/614b/616/614c/614d trail + the modulatory-bias-selection-authority linkage).
- Substrate: `ree-v3/CLAUDE.md` "modulatory-bias-selection-authority" (2026-06-03; MECH-341 in unblocks_claims), "MECH-341" cluster entries.
- Audit: `REE_assembly/evidence/planning/retrospective_diagnostic_selfroute_audit_2026-06-06.md` (Section 2 rows 608 + 611/611c; Section 4 item 2).
- Method precedent: `REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-642_2026-06-06.md` (the self-route-is-a-hypothesis precedent).
