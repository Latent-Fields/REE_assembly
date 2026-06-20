# MECH-442 decide-whether-to-build — decision packet (2026-06-19)

**Status:** DECISION = **(b) DESIGN GAP — do not build yet; route two specific open questions.**
**Author:** session `mech442-decide-to-build-20260619T1907Z`. **Decision time:** 2026-06-19T19:10Z.
**Changes no claim status.** MECH-442 stays `candidate / substrate_conditional / generation:v3 / ceiling_decision:deferred`, OFF the V3 critical path. This packet is the durable resume primitive for the deferred decide-whether-to-build step.

---

## 0. The question

MECH-442 (claims.yaml, registered 2026-06-18) proposes a behavioral-descriptor eligible-set **ARCHIVE** (Quality-Diversity / MAP-Elites analog) upstream of the E3 winner-take-all commit, to convert per-candidate diversity into committed-action diversity. It targets the MECH-439 F-dominance conversion ceiling (F = 88–89% of E3 committed-selection variance, V3-EXQ-571). The validated V3-EXQ-569i top-k shortlist is the **descriptor-free degenerate instance**; the archive is the principled generalization.

The build was deferred for a genuine circularity: the pre-registered 2×2 `(F-de-collapse) × (archive vs top-k)` discriminator can't run until a minimal archive exists. User framing: *"if it is just to build then build away; but if there are things about the build to be decided then we need to ask convergence or lit-pull or something else."*

**Answer: there are things to be decided, and a fresh result (V3-EXQ-689, completed 18:59Z today) materially reprices the build. Do not just-build. Route the open questions (Section 3).**

---

## 1. The load-bearing input — top-k is THIN and FRAGILE (quantified)

### V3-EXQ-569i (TOP-K shortlist, PASS — the validated conversion substrate)
`v3_exq_569i_gapa_conversion_topk_shortlist_falsifier_20260616T224009Z_v3.json`, claim ARC-065, machine ree-cloud-2.

Committed selected-action-class entropy (nats), per-arm mean:

| arm | entropy mean |
|---|---|
| ARM_0_PROPOSER (collapsed baseline) | **0.650347** |
| ARM_2_MATCHED_NOISE (proposer @ T=2.5) | **0.650347** ← *bit-identical to baseline* |
| ARM_1_E2WF_TOPK (conversion under test) | **0.711149** |

- **Mean lift over both controls: +0.0608 nats (~9.4% relative).**
- **Passes exactly at the 2/3 floor** (`arm1_seeds_strict_above_both = 2`, `min_seeds_for_pass = 2`).
- **Per-seed (ARM_1 vs ARM_0; control == ARM_0 each seed):**
  - seed 42: 1.2322 vs 1.1292 → **+0.103 ✓**
  - seed 43: **0.000 vs 0.0047 → ARM_1 BELOW** (collapsed to a single committed class, entropy 0 — *worse than baseline's 2 classes*) ✗
  - seed 44: 0.9012 vs 0.8172 → **+0.084 ✓**
- **Trajectory-class count barely moves:** ARM_0 2.973 → ARM_1 2.984 (**+0.011**).
- **The matched-noise control was inert** (it collapsed to bit-identical-to-proposer; `matched_noise_lift_seeds_over_proposer = 0`; manifest flags it "informational sanity only, does NOT gate the verdict"). So C_R1B "strict-above BOTH" reduces in practice to "strict-above proposer" — the noise leg passed trivially, so it was **not a stringent hardness test**.

### V3-EXQ-569g (route-range, no top-k — predecessor FAIL)
`v3_exq_569g_..._20260611T224954Z_v3.json`, reclassified non_contributory.
- ARM_0 0.7041, ARM_1_E2WF **0.6150 (below baseline)**, ARM_2 noise 0.7041. `r1b seeds strict-above-both = 1/3`.

**top-k's entire contribution = converting the 569g 1/3 FAIL (ARM_1 below baseline) into a 569i 2/3 PASS.** It is the first thing that crossed the bar — but it is thin (+0.061 nats), fragile (clears at the floor; one of three seeds collapses to monostrategy), near-zero on trajectory-class count (+0.011), and its noise-control leg was inert.

### Available headroom is LARGE (conversion ceiling unresolved)
- Per-candidate first-action diversity (ARM_0 569i): `candidate_unique_first_action_classes_mean` ≈ 4.10 / 2.00 / 2.83 (seeds 42/43/44).
- Committed realized: entropy 0.71 vs ceiling ln(5)=1.609 → **44% of max**; ~3 of ~4 candidate classes survive into committed trajectories.
- F-dominance (88–89% of selection variance, V3-EXQ-571) caps the rest.

**Verdict on the load-bearing question:** top-k does **NOT** capture most of the available diversity conversion. It is **marginal/thin/fragile**. → The archive is NOT low-value (rules out **(c)**); there is real headroom for a better converter.

---

## 2. THE FRESH, DECISIVE INPUT — V3-EXQ-689 (MECH-439 conflict-grade), completed 18:59Z today

`v3_exq_689_mech439_conflict_grade_2factor_falsifier_20260619T185949Z_v3.json`, claim MECH-439, outcome **FAIL / non_contributory**, label **`substrate_not_ready_requeue`**.

This is the FIRST falsifier of the just-landed (2026-06-18) MECH-439 conflict-grade levers — the **cheaper structural generalization of top-k on the SAME F-dominance root** (Factor A = conflict-graded shortlist width replacing fixed-k; Factor B = gap-scaled commit-T). It is the nearest competitor to the archive. It **just ran**, and it matters two ways:

### (i) It self-routed on a NON-VACUITY gate — the substrate didn't present convertible variation
- Readiness `readiness_ok = False`. The route-range and e2-divergence preconditions PASSED (route_range 0.566, pairwise_dist 0.164, both 3/3), but the load-bearing one FAILED:
  - `a1b1_grading_quantities_and_gap_distribution_non_vacuous`: **met = False** (`gap_spread_seeds = 0`).
- I.e. the normalized top-F gap **did not vary enough across ticks** for the conflict-grade levers to engage meaningfully, so the load-bearing C_FGAP gap-slope falsifier was **non-computable** (`fgap_computable = False`). It self-routed to requeue → **no verdict on MECH-439**.

### (ii) Descriptively, the conflict-grade levers did NOT beat plain top-k
Committed selected-action-class entropy, per-arm mean:

| arm | levers | entropy mean |
|---|---|---|
| ARM_PROPOSER_CTRL | — | 0.650347 |
| ARM_MATCHED_NOISE | — | 0.650347 |
| **ARM_A0B0** | fixed-k=3 + hard argmin (**= the 569i top-k**) | **0.711149** |
| ARM_A1B0 | conflict-graded k + hard argmin | 0.350089 *(collapsed, worse)* |
| ARM_A0B1 | fixed-k + gap-scaled commit-T | 0.664618 |
| **ARM_A1B1** | **both levers** | **0.624048** *(BELOW top-k 0.711)* |

`c_primary` "passed" 2/3 seeds strict-above the two **collapsed** controls (0.650) — but A1B1 (0.624) is **below plain top-k (0.711)**, and the gap-correlation falsifier was non-computable.

**Why this is decisive for MECH-442:** the campaign's recurring blocker (569g → 569h → 569i → 689) is the SAME — getting a substrate where the committed-relevant signal **varies enough at the commit to be converted**. top-k (569i) barely cleared; the conflict-grade lever (689) couldn't even engage non-vacuously. **The archive is a richer selection structure facing the identical wall.** Building it before establishing that ANY committed-selection-structure lever converts on a gap-spreading substrate risks the same `substrate_not_ready_requeue`.

---

## 3. Design-parameter audit — SETTLED vs OPEN

| parameter | status | basis |
|---|---|---|
| **Behavioral descriptor choice** (first-action class / committed-action class / e2.world_forward strategy signature) | **OPEN** | The convergence intake itself flagged this unresolved: comparison_table QD-Q-001 (descriptor choice + standing-vs-per-tick), QD-P-002 (descriptor-granularity → coverage). First-action class is the minimal/near-settled axis (discrete, already MECH-341's partition), but the *principled* generalization (e2.world_forward strategy signature) is the part that makes the archive more than a top-k rename, and it is undecided. |
| **Niche resolution / discretisation** | **OPEN** *(for the strategy-signature descriptor)* / SETTLED *(for first-action class: 5 discrete classes = 5 niches, no hyperparameter)* | Continuous descriptor needs CVT-style discretisation + a standing-vs-per-tick archive decision (QD-Q-001). |
| **Coverage-aware commit rule** | **SUBSTANTIALLY SETTLED** | MECH-341 `stratified_select` (one F-best representative per first-action class) + the entropy_bonus (per-candidate coverage pressure) already implement within-tick coverage. The archive's novel piece is **cross-tick standing** persistence, not a new rule. |
| **Per-niche-elite F-quality safety envelope / bound** | **SETTLED (in principle)** | = the top-k "only the k F-best are eligible" guarantee. Already implemented by MECH-439 Factor-A (F gates eligibility only) + `gap_scaled_commit_harm_floor`. The specific bound value is a calibration knob, decided at build. |
| **Pairing with MECH-313 active variability generator** | **SETTLED** | MECH-313 NoiseFloor is built (2026-05-10); the lit-pull (`targeted_review_connectome_mech_442`, 5 PubMed, SUPPORTED-with-refinement) explicitly added MECH-313 to depends_on. Pairing = config composition. |

**Net:** the *minimal first-action-class* archive is ~settled — but it is so close to the already-built MECH-341 (stratified) + MECH-439 (conflict-grade) + MECH-313 (noise) machinery that its only novel contribution is cross-tick standing niche persistence, and its falsifier bar ("beyond top-k 2/3") is precisely what the 689-successor is about to retest with a cheaper lever. The genuinely *principled* archive (strategy-signature descriptor) has **one real open design fork**.

---

## 4. Recommendation — (b) DESIGN GAP. Route two questions; do not build yet.

Not **(a) JUST BUILD**: a real descriptor/resolution fork remains open, and 689 just showed the immediate blocker is upstream of the selection structure (the substrate isn't presenting convertible committed-relevant variation — `gap_spread_seeds = 0`).
Not **(c) DON'T BUILD**: top-k is thin/fragile with large unconverted headroom; the conversion ceiling is unresolved, not captured.

### Open Q1 → focused REE_convergence query (descriptor + resolution + inner-vs-outer-loop scope)
**Question:** which MAP-Elites variant resolves (a) the behavioral-descriptor choice (first-action class vs e2.world_forward strategy signature), (b) the niche discretisation, and (c) the **standing-archive-vs-per-tick-rederivation** scope, for REE's **small discrete-action per-tick INNER-loop** selection — as opposed to QD's outer-loop population search (the comparison_table's own QD-LIM-001 scope mismatch)?
- Candidate variants to disambiguate: **CVT-MAP-Elites** (descriptor discretisation), **MAP-Elites with archive distillation** / **CMA-ME** (the per-niche elite update inside a per-tick loop).
- This is exactly the unresolved probe set the convergence intake already named (QD-Q-001 / QD-P-002 / QD-LIM-001) — it was registered but not answered.

### Open Q2 → sequencing gate: the MECH-439 689-successor must land FIRST
**Why:** 689 self-routed because the F-gap didn't spread; until a committed-selection-structure lever is shown to convert on a **gap-spreading** substrate, the archive (a richer lever on the same substrate) cannot be expected to clear its non-vacuity gate either.
- If the 689-successor (requeued on a gap-spreading substrate) shows conflict-grade **beats** plain top-k → the archive's pre-registered bar rises from "beyond top-k" to "beyond conflict-grade"; re-justify the archive's marginal value before building.
- If the 689-successor **also** fails to convert → the bottleneck is upstream (substrate doesn't present convertible committed-relevant variation); route to **substrate enrichment**, not the archive — the archive would hit the same wall.

### Optional / secondary → targeted /lit-pull
The `targeted_review_connectome_mech_442` lit-pull already answered the architecture (upstream eligible-set restriction + variability generator; Markowitz 2018 striatal module repertoire; Ponzi 2007 WTA commit is biologically faithful). It did **not** pin **standing-archive vs per-tick re-derivation** (does the striatal behavioral-module repertoire imply a cross-tick persistent archive?). A small follow-on lit-pull on that one biological parameter is a *secondary* input, lower priority than Q1/Q2.

---

## 5. Concrete next actions (await user confirmation before executing)

1. **(Q1)** Open a focused REE_convergence query: *"MAP-Elites variant for a small discrete-action per-tick inner-loop committed-selection archive — descriptor (first-action vs e2.world_forward signature), niche discretisation (CVT?), and standing-vs-per-tick scope; resolve QD-Q-001/QD-P-002/QD-LIM-001."*
2. **(Q2)** Track the MECH-439 689-successor (the conflict-grade requeue on a gap-spreading substrate). Re-open this decision when it lands — its margin reprices the archive.
3. **Do NOT** queue a minimal-archive experiment yet (the 2×2 discriminator) — it would duplicate the 689-successor's test surface and faces the same `gap_spread_seeds=0` non-vacuity risk.

**MECH-442 disposition unchanged:** candidate / substrate_conditional / generation:v3 / ceiling_decision:deferred; OFF the V3 critical path; AMENDS behavioral_diversity_isolation:GAP-B. This packet replaces the prose "decide-whether-to-build is a later governance step" with a concrete, routed decision.

---

## 6. 689a verdict (2026-06-20) — Q2 resolved: conflict-grade FAILED, but a cheaper sub-lever surfaced

The Q2 gating run completed. **V3-EXQ-689 self-routed `substrate_not_ready_requeue`** (F-gap near-tie-pinned, gap-bin regression uncomputable). Its autopsy (`failure_autopsy_V3-EXQ-689_2026-06-19`, user-ratified) **redesigned it gap-blind** as **V3-EXQ-689a** — replacing the uncomputable per-gap-bin regression with an **arm-contrast** (does the both-levers cell beat the *flat* controls `FIXED_KMAX` / `FIXED_HOT_T`, isolating gap-CONCENTRATED lift from "a bigger fixed shortlist / hotter flat softmax"). 689a ran 8 arms × 3 seeds (~21h, on `DLAPTOP-4.local`, swap-contended).

**Result: `FAIL` / `non_contributory` / `conversion_ceiling_persists_despite_conflict_grade`** (`v3_exq_689a_..._20260620T175346Z_v3.json`). NON-VACUOUS (readiness PASSED: route_range 0.624 3/3, e2-pairwise 0.187 3/3, levers engaged k 3/3 + t_eff 3/3) — so this is a *real* verdict, not a self-route.

Per-arm committed-action-class entropy (mean; per-seed 42/43/44):

| arm | mean | s42 | s43 | s44 |
|---|---|---|---|---|
| PROPOSER_CTRL / MATCHED_NOISE (collapsed) | 0.677 | 1.276 | 0.005 | 0.750 |
| A0B0 (top-k baseline, divergent pool) | 0.371 | 0.480 | 0.098 | 0.536 |
| A1B0 (Factor A: graded-k) | 0.440 | — | — | — |
| **A0B1 (Factor B alone: gap-scaled commit-T)** | **0.850** | **1.360** | **0.569** | 0.620 |
| **A1B1 (BOTH levers — pre-registered PRIMARY)** | **0.387** | 0.655 | **0.005** | 0.502 |
| FIXED_KMAX (gap-blind Factor-A control) | 0.546 | 1.148 | 0.179 | 0.311 |
| FIXED_HOT_T (gap-blind Factor-B control) | 0.591 | 1.018 | 0.009 | 0.745 |

- **The pre-registered PRIMARY `A1B1` (both levers, 0.387) lost to everything** — below both gap-blind controls (0.546, 0.591) AND below the collapsed baseline (0.677). `C_GAPBLIND` and `C_PRIMARY` both FAIL, **0/3 seeds**. The combined "grade the commit by the top-F gap" mechanism does **not** convert. (Not a *weakens* of MECH-439 — the pre-registered off-ramp; `evidence_direction: non_contributory`.)
- **DECOMPOSITION (the load-bearing new finding): Factor B alone (`A0B1`, gap-scaled commit-temperature) is the only converter** — mean 0.850, the highest arm; strictly above its OWN flat-hot control (`FIXED_HOT_T`) AND the proposer on **2/3 seeds**, and on seed-43 it **held 0.569 while every other arm monostrategy-collapsed to ~0.005**. Because it beats `FIXED_HOT_T` (a flat-hot softmax over the same divergent pool), the lift is the **gap-SCALING**, not merely a hotter temperature.
- **Factor A (conflict-graded shortlist width) is HARMFUL** — `A1B0` (0.440) barely clears top-k, and adding A to B (`A1B1` 0.387) *destroys* B's benefit (re-introduces the seed-43 collapse B alone prevented).

### Repriced MECH-442 disposition

This is the **FAIL branch of Q2 — but with a twist that changes the routing:**

1. The **combined 2-factor conflict-grade FAILED**, so it does **NOT** raise the archive's pre-registered bar to "beyond conflict-grade" (conflict-grade never established itself as a converter).
2. **BUT the F-keyed approach is NOT exhausted** — `A0B1` (gap-scaled commit-T alone) is a **live, cheaper V3 lever** that lifted on 2/3 seeds and resisted collapse. So the strict "→ rank_preserving_F_to_eligibility_demotion / V4 directions / archive case strengthens" off-ramp is **premature**: there is a cheaper intermediate probe.
3. **Next step before building the archive: a Factor-B-alone retest** (a 689-successor with `A0B1` as the *primary* cell — gap-scaled commit-T ON, conflict-graded-k OFF — vs top-k + the flat-hot control, pre-registered for ≥2/3 strict-above + collapse-resistance). If Factor-B-alone **robustly converts**, it is the cheapest fix to the conversion ceiling and the archive stays deferred indefinitely. If it **also fails** (≤1/3 robust), *then* the F-keyed family is genuinely exhausted and the behavioral-descriptor archive (CDQ-006) becomes the justified path.

**Net:** MECH-442 **stays deferred** (candidate / substrate_conditional / ceiling_decision:deferred — unchanged). The build is **not** triggered. CDQ-006 (the convergence descriptor-variant query) **stays queued** as the eventual fallback. The immediate live work moved from "the archive" to **"retest Factor-B-alone (gap-scaled commit-T) as the standalone converter"** — a result the gating run handed us for free. No claim status changed; MECH-439 stays candidate (non_contributory, pre-registered off-ramp — neither promoted nor weakened).

## 7. Correction — biological-fidelity steer (2026-06-20, supersedes the Section-6 framing)

**User steer (2026-06-20, strong, anti-shortcut):** build REE with *biological fidelity*. Do **not** pursue cheap parametric near-tie levers as a substitute for — or a reason to skip — the biologically-faithful build, *even when the lever moves the metric*. The fidelity is load-bearing for the psychiatry-model and complexity-layering goals (ARC-106 anti-shortcut corollary). My Section-6 framing ("next step before the archive = a Factor-B-alone retest"; "if Factor-B-alone robustly converts it is the *cheapest fix* and the archive stays deferred indefinitely") was the rejected shortcut reasoning and **does not govern**.

**Corrected disposition:**

1. **The faithful conversion path is the ARC-107 BG-constitution — MECH-448 (rank-preserving F→eligibility / Go-No-Go demotion: F removed from the final argmin, used only as a graded basal-ganglia disinhibitory envelope).** This is the build, **regardless of what V3-EXQ-689c shows.** It is already in flight (`implement-substrate-mech-448`).

2. **V3-EXQ-689c (the Factor-B-alone retest) is PURE NO-AUTHORITY CONFIRMATORY DATA** (user decision 2026-06-20: keep it queued as an observation). A 689c **PASS does NOT lower the bar** for skipping the faithful build, and does **NOT** make MECH-442's archive "deferred indefinitely." It records the parametric fact for the divergence ledger; nothing more.

3. **MECH-442 (the QD behavioral-descriptor archive) decision is re-anchored to biological fidelity,** not "whichever lever is cheapest to make committed-action-class entropy move." The decide-to-build question is now subordinate to: *does the faithful BG-constitution (MECH-448) resolve the F-dominance conversion ceiling?* — not *can a thin near-tie lever pass a metric?*

4. **No claim status changed** (MECH-439 / MECH-442 stay candidate). Substrate_queue / claims.yaml routing edits are owned by the parallel governance / implement-substrate sessions (disjoint resources).
