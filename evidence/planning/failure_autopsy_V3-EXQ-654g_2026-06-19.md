# Failure Autopsy — V3-EXQ-654g (arc_062_rule_apprehension:GAP-B behavioural falsifier)

- **Generated (UTC):** 2026-06-19T21:48:41Z
- **Status:** confirmed (user-ratified at the interactive gate)
- **Scope:** single (cross-claim convergence with GAP-A / MECH-439 surfaced; 2nd channel after 485h)
- **Run:** `v3_exq_654g_arc062_gapb_rule_apprehension_behavioural_falsifier_20260619T213118Z_v3` (ree-cloud-4)
- **Queue:** V3-EXQ-654g, `experiment_purpose=evidence`, `supersedes=V3-EXQ-654f`
- **Claims tested:** MECH-309, ARC-062 (bears-on ARC-063)
- **Outcome:** FAIL / `non_contributory` (per-claim MECH-309 + ARC-062 both `non_contributory`); weights nothing.
- **Self-route label (under `result.interpretation`):** `shared_selection_authority_conversion_ceiling_route_implement_substrate`

## Headline

**654g closes the escape hatch that 654f left open.** 654f's conversion-ceiling reading
could be dismissed because 654f armed the *wrong* (superseded additive `ARM_STD_G2`)
conversion lever — leaving "maybe the 569i-validated top-k fix rescues it." 654g ports the
GAP-B committed-class-entropy falsifier onto the **569i-validated TOP-K shortlist conversion**
(`use_modulatory_shortlist_then_modulate` + `mode=top_k` + `k=3`), constant on both arms — the
actual fix that worked for the GAP-A modulatory-bias channel (V3-EXQ-569i PASS/supports;
ARC-065 promoted stable). The CRF stack is fully matured. **C1 cleared all five preconditions;
C2 still failed.** This is the pre-registered **branch (b)**: a deeper *shared* selection-authority
conversion ceiling (MECH-439 F-dominance, the live root), **not** an MECH-309 / ARC-062
falsification and **not** a weakens. 654g is the **2nd independent channel** — after the same-day
V3-EXQ-485h (OFC valuation bias) — to reach the E3 accumulator and fail to convert at the shared
F-dominated selector.

## 1. Facts (no interpretation)

**C1 (non-vacuity) = TRUE — all five preconditions met:**

| Precondition | Measured | Gate |
|---|---|---|
| committed-class axis exercisable (both arms) | frac_pre_ge2 = 1.0 (3/3) | ≥0.30 ✅ |
| GAP-A consumed-summary divergence (both arms) | 0.080 / 0.171 / 0.188 (OFF), 0.122 / 0.176 / 0.188 (ON) | ≥0.05 ✅ |
| consumed-summary bounded (no 643a explosion) | max 0.289 | <1e6 ✅ |
| ARM_ON CRF differentiated + matured | `crf_frac_active` **0.581 / 0.942 / 0.783**; minted 16 / 16 / 12; `crf_differentiated` True | ≥0.30 ✅ |
| propagation non-vacuity (ARM_ON bias ≠ ARM_OFF) | paired diff 0.0469 / 0.0132 / 0.0170 | >0.001 ✅ |
| within-ARM_ON rule_state counterfactual nonzero | 2/3 (s42 0.00246, s44 0.00376, s43 ~4.8e-5) | majority ✅ |

**C2 (PRIMARY — committed-class entropy lift) = FALSE:**
- `C2_paired_lifts_by_seed` = `{42: −0.012996, 43: +0.047011, 44: 0.000000}`; **0/3** cleared the
  +0.05-nat margin (need ≥2/3).
- ARM_ON mean committed-class entropy **0.672757** ≈ ARM_OFF **0.661419** (+0.011 nats).
- Per seed: s42 OFF 1.2145 → ON 1.2015 (5 classes, lift **−0.013**); s43 OFF 0.0043 → ON 0.0513
  (2-class monostrategy, lift **+0.047**, sub-margin); s44 OFF 0.7655 → ON 0.7655 (3 classes, lift **0.000**).
- **Seed 44 is the purest signature in the whole lineage:** ARM_ON `committed_class_counts`
  `{0:16, 2:237, 4:384}` is **byte-identical** to ARM_OFF (same entropy 0.765501, same n_p2_ticks
  637, same within-class-rep entropy) — *despite* CRF being active on 78% of ticks
  (`crf_frac_active` 0.783, `crf_mean_n_matched` 3.36) with a nonzero within-arm counterfactual
  (0.00376). A fully live, matured, differentiated channel produced **zero** behavioural conversion.
- ARM_ON `mean_lateral_pfc_bias_abs` is *lower* than ARM_OFF on 2/3 seeds (s42 0.0215 vs 0.0683;
  s44 0.0377 vs 0.0547) — the rule_state reaches and *changes* the bias; the change does not move
  the F-dominated committed argmax.

**Failed criterion: discrimination (C2).** DV is **non-degenerate** (committed-class entropy
ranges 0.004–1.21 across seeds — it can and does move; it just does not move *between arms within
a seed*). Negative control (within-class-rep entropy ARM_ON ≈ ARM_OFF) behaved as designed,
confirming the rule-creator's signal lives in the committed-class axis (the load-bearing C2 DV).

## 2. The load-bearing finding

654g **eliminates the wrong-lever confound** that qualified the 654f conversion-ceiling read:

1. **654f armed the superseded additive lever** (`ARM_STD_G2`), which GAP-A's V3-EXQ-569h had
   already shown insufficient (1/3 seeds). So 654f's C2-fail was ambiguous: ceiling, or wrong fix?
2. **654g arms the 569i-validated top-k shortlist** (`mode=top_k`, `k=3`), constant on both arms —
   the same fix that PASSED for the GAP-A modulatory-bias channel ("diversity reaches committed
   action"). **It still fails at the GAP-B / CRF-rule_state locus.**

Therefore: the 569i top-k conversion fix is **channel-specific** — it rescued the GAP-A
modulatory-bias channel but **does not transfer** to the CRF rule_state channel. The residual is
the **shared selection-authority conversion ceiling** (`behavioral_diversity_isolation:GAP-A`;
failure_autopsy_V3-EXQ-569g / V3-EXQ-682; **MECH-439 F-dominance live root**, F ≈ 88–89% of E3
score variance per V3-EXQ-571). The manifest pre-registered this exact outcome as the
**KNOWN OPEN RISK**: "the 569i top-k 2/3-seed margin is thin … may not survive the GAP-B composite;
if C2 fails, that is branch (b) — a deeper shared selection-authority conversion ceiling … NOT a
falsification, NOT a weakens."

**Convergence (the durable signal).** 654g is the **2nd channel today** to demonstrate the same
shared ceiling on independent substrate:
- **V3-EXQ-485h** (same day) — OFC valuation bias reaches accumulator authority 0.50 with **zero**
  committed conversion; routed MECH-439 F-rebalance first.
- **V3-EXQ-569g / 682** — GAP-A modulatory-bias channel range reaches the accumulator, doesn't move
  the committed argmax (the original diagnosis; later partially rescued only by top-k on *that*
  channel).
- **V3-EXQ-654g** (this run) — CRF rule_state channel, matured + differentiated + top-k-armed,
  reaches the bias, moves zero committed actions.

Three structurally-different channels (OFC valuation, modulatory bias, CRF rule_state) all reach
the E3 accumulator and all fail to convert at the **same** F-dominated selector. This is the
load-bearing output: **MECH-439 F-dominance rebalance is the single shared blocker**, and
channel-specific wiring (top-k, gain, etc.) is **not sufficient** to clear it.

## 3. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | C2 never adjudicated MECH-309 / ARC-062 — they are gated behind a downstream ceiling they do not own. No evidence for or against. |
| Biological reference | clear | PFC rule abstraction (Collins & Frank 2014; Mansouri rule-maintenance) is *achieved* — the CRF matures and propagates. The block is downstream BG/PFC action-selection authority (the F-dominated argmax MECH-439 / GAP-A own). |
| Prerequisites | **present** | CRF matured (frac_active 0.58–0.94); the 569i top-k conversion lever — the single gap in 654f — is now ARMED and constant on both arms. |
| Implementation completeness | **complete** (cleanest GAP-B stack to date) | Full CRF stack (persist + 666c maintenance + gate-amend levers) + e2_world_forward context + trained-bias-head P1 + 569i top-k, all constant; single-variable `use_candidate_rule_field`. |
| Environment | adequate | SD-054 bipartite reef, foraging-competent. |
| Measurement | adequate | committed-class entropy is the correct class-keyed DV; within-class-rep is the negative control (behaved as designed). |
| Integration | **coupled, ceiling at the argmax** | bias reaches accumulator, does not move the F-dominated commit (seed-44 byte-identical is the purest demonstration). |
| Scale | adequate | 200-ep P0; pool matured. |

Recommended `epistemic_category`: **substrate_ceiling** (unchanged). Recommended
`evidence_direction`: **non_contributory** per-claim (already set on the manifest). Pair with
`pending_retest_after_substrate` (already set). **NO weakens.**

## 4. Granularity-debt recurrence check (7th 654 autopsy)

This is the ~7th autopsy on the 654 / `arc_062:GAP-B` target
(654 → 654a[cluster] → 654b → 654c → 654d → 654f → 654g). Per the skill's recurrence trigger this
is checked explicitly. **Determination: NOT granularity debt. No `/claim-synthesis`.**

- The failure signatures **converged**, they did not diverge: per-episode CRF cold-start
  (654/654b/654c) → CRF conflict-gate lockout (654d) → CRF fixed but *wrong* conversion lever
  (654f) → CRF fixed + *right* (top-k) lever, ceiling persists (654g). A single localizing
  sequence honing in on one blocker — the opposite of N distinct shapes circling a coarse claim.
- 654g localizes the blocker to a **shared downstream ceiling (MECH-439 F-dominance)** that
  MECH-309 / ARC-062 **do not own**. The claims were never adjudicated; there is nothing coarse
  about them to decompose.
- The user re-confirmed this framing 2026-06-16 (recorded in the 654d / 654f autopsies):
  substrate-maturation, not claim-granularity debt. 654g corroborates.

## 5. Routing (user-confirmed at the interactive gate, 2026-06-19T21:48Z)

1. **Verdict:** `non_contributory`, **NO weakens** (branch b). MECH-309 / ARC-062 / ARC-063 stay
   **candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate** — *not weakened,
   not promoted.*
2. **Next experiment:** **No 654h now.** GAP-B is blocked at the shared F-dominated selector; it is
   **sequenced behind the MECH-439 F-dominance rebalance** (the existing 689a falsifier chain +
   GAP-A's conversion amend), mirroring the same-day 485h decision. A 654h that re-runs the GAP-B
   committed-class-entropy falsifier is **pre-registered for after the conversion ceiling lifts**.
3. **Substrate-queue action: `none`.** The CRF substrate (`crf-availability-maintenance`) is
   **complete** and already carries a 2026-06-19 note recording 654g ("C1 fully met … C2
   non_contributory … residual is the shared MECH-439 F-dominance conversion ceiling, 2nd channel
   after 485h OFC, NOT a CRF fault; this substrate entry is complete; no further CRF amend owed").
   No F-dominance-rebalance substrate_queue entry exists yet — that work is **pre-substrate** (689a
   is diagnosing *whether* conflict-grading converts before any substrate is committed). No
   substrate_queue write is owed from this autopsy.
4. **Granularity:** **No `/claim-synthesis`** (Section 4).

### Governance hand-off (applies; this autopsy does not edit these)

- Mark `...654g..._v3` reviewed in `review_tracker.json` (the active governance session
  20260619T2141Z holds this file and is walking pending experiments — left to it).
- 654g manifest is already `non_contributory` (script-set). Per supersession policy, set the
  superseded **654f** manifest `evidence_direction: superseded` for hygiene (654f was already
  `non_contributory` / reviewed, so this changes no scoring).
- Repoint `arc_062_rule_apprehension:GAP-B` plan-frontmatter `owner_exq` from V3-EXQ-654f →
  V3-EXQ-654g; refresh `resume_condition` to the *post-MECH-439-rebalance 654h* path; status stays
  `in-progress` (gated on the shared conversion ceiling). Derive-only-adjacent frontmatter edit.

### Draft `evidence_quality_note` (governance writes; do not write here)

> V3-EXQ-654g (arc_062 GAP-B behavioural falsifier; MECH-309 / ARC-062) — FAIL / non_contributory.
> C1 fully met 5/5 (crf_frac_active 0.58–0.94, propagation non-vacuous); C2 committed-class-entropy
> lift FAILED (paired {−0.013, +0.047, 0.0}, 0/3 clear margin; +0.011 nats mean; seed-44 ARM_ON==
> ARM_OFF byte-identical despite live CRF). 654g armed the 569i-validated TOP-K shortlist conversion
> (the lever 654f lacked) and the ceiling persisted — the top-k fix is channel-specific (GAP-A
> modulatory-bias only) and does not transfer to the CRF rule_state channel. This is the shared
> MECH-439 F-dominance conversion ceiling (branch b, pre-registered), the 2nd channel after V3-EXQ-485h
> OFC. MECH-309 / ARC-062 never adjudicated — gated behind a downstream ceiling they do not own.
> Stay candidate / substrate_ceiling / pending_retest_after_substrate; NOT weakened. Retest = a 654h
> after the MECH-439 F-dominance rebalance lifts the conversion ceiling. CRF substrate complete.
