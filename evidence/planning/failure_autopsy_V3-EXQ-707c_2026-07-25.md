# Failure Autopsy — V3-EXQ-707c (weakens ARC-110)

**Generated:** 2026-07-25T17:59:14Z
**Scope:** single · **Status:** confirmed (user-gated)
**Run:** `v3_exq_707c_arc110_loop_segregation_c2_release_repair_20260723T151429Z_v3`
**Queue:** V3-EXQ-707c (supersedes V3-EXQ-707b) · diagnostic · PROMOTES NOTHING
**Claim:** ARC-110 · **Outcome:** FAIL · **Direction:** weakens (narrow)
**Substrate:** `172ba39e…` · machine ree-cloud-4 · 8 seeds · recording-core complete

---

## 1. Facts

Four arms on the matched GAP-A reef-bipartite foraging substrate — A0_SINGLE_ARENA / A1_LOOPS / ARM_NOISE (S2 in-layer same-layer null) / ARM_DROP_LIMBIC — with loop segregation as the only swept factor. **Every readiness precondition passed:** crf_matured (8/8 per arm), enough_divergent_seeds (4/4), loops_carry_live_cross_loop_variance (min flip/disagree frac 0.41), named_channel_routing_live, limbic_graded_competition_live (worst A1 cell 4.28 ≫ 0.05 floor), fresh_selects_sufficient (worst cell 922 ≫ 30), in_layer_null_live, learning_engaged. Both criteria non-degenerate.

- **C1_A1_loops_strict_above_A0_and_in_layer_null (load-bearing): FAILED.** A1_LOOPS committed-class conversion did not clear strict-above max(A0, the LIVE null) + margin.
- **C2_limbic_loop_load_bearing (non-load-bearing): FAILED** (moot given C1).

Pre-registered reading fired: **valid null + loops vary + no conversion → the F-dominance conversion ceiling is INTRINSIC, not a single-arena-collapse artefact → weakens ARC-110's narrow sub-hypothesis.**

## 2. Why this run exists (instrument repair)

`failure_autopsy_V3-EXQ-707b_2026-07-20` (confirmed, user-gated) **withdrew** 707b's weakens on ARC-110 as a `measurement_test_design_defect`: the load-bearing DV `committed_class_entropy_nats` was accumulated per env-step over a **hold-weighted histogram** (no e3-tick guard), with arm exposure differing by up to +97.6% — a distribution-shape statistic that does not cancel under exposure imbalance, leaving the decisive A1-vs-null contrast sign-inconsistent across all three divergent seeds and 8× below the contamination floor. It commissioned an instrument-repaired re-run. **707c is that re-run** — the DV is now accumulated only on verified-fresh E3 selections, with fresh-select-sufficiency + divergence-headroom + graded-limbic-competition guards and exposure telemetry. It reproduces the weakens on a clean instrument.

> **Stale note in claims.yaml.** ARC-110's `evidence_quality_note` still carries the withdrawn 707b-2026-06-29 weakens text. Governance never replaced it after the 2026-07-20 withdrawal. Section 6 supplies the replacement.

## 3. Claim-layer mapping — the load-bearing distinction

ARC-110 bundles two claims:

- **(a) Architectural assertion** — parallel segregated cortico-BG-thalamic loops (motor / associative / limbic) are biologically real and load-bearing (Alexander/DeLong/Strick; a *functional* translation, not anatomical mimicry). **NOT falsified by 707c.**
- **(b) Narrow sub-hypothesis** (assembly-map A.2 / s.D) — the F-dominance conversion ceiling (MECH-439) is *partly an artefact of the single-arena collapse.* **This is what 707c weakens.**

The 707 lineage only ever tested (b). 707c settles it on a valid instrument: segregating the loops on a fully-live substrate does **not** lift F-dominance, so the ceiling is intrinsic to something other than arena-collapse.

## 4. Biological-reference triage

The parallel-loop organisation is a faithful functional translation, and the loops in real brains are **integrated by dopamine** (Haber ascending spiral) — an integration that **learns**. The current build has segregation + within-loop competition but a **static arithmetic** cross-loop arbitration. Biology therefore *predicts* segregation-without-learned-integration would not lift F-dominance — precisely what is observed. The FAIL matches a **missing-dependency signature**: learned DA-gated cross-loop arbitration (MECH-448/449/ARC-107).

**But that rescue path is substrate-exhausted.** It was built and tested three times — 709 (learned cross-loop arbitration), 711 (ascending-spiral gain), 713 (bounded-parity controller) — **all confirmed `substrate_ceiling`** (degenerate/saturated arbitration regime; the conversion question could not be validly measured). ARC-110's re-derive-brake tally stands at **3**.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **weakened (narrow only)** | narrow sub-hyp weakened; architectural assertion intact |
| Biological reference | **clear** | Alexander/DeLong/Strick + Haber spiral; failure matches missing-learned-integration signature |
| Prerequisites | **missing but exhausted** | learned DA-gated arbitration; 709/711/713 substrate_ceiling |
| Implementation | **complete & live** | all readiness gates passed; static arbitration is a design fact |
| Environment | **adequate** | matched GAP-A substrate; only loop segregation swept |
| Measurement | **adequate (repaired)** | fresh-select-gated DV — the point of 707c |
| Integration | **coupled but static** | loops integrate via non-learning arithmetic arbitration |
| Scale | **adequate** | not the binding constraint |

**Recommended `epistemic_category`: `standard`** — NOT substrate_ceiling. The substrate was live and the instrument valid; the narrow sub-hyp was fairly tested and weakened. **Do not count this run toward the ARC-110 ceiling tally.**

**Granularity-debt recurrence trigger: does NOT fire.** Reader over targets tagging ARC-110: alignment distribution unclear=4, intact=2, weakened=1. The single active `weakened` is 707c itself; the ceiling readings (709/711/713) form a coherent "rescue path substrate-blocked" narrative, not structurally-different signatures of a coarse claim. This is substrate/measurement debt, not granularity debt.

## 6. Draft `evidence_quality_note` (governance to write — replaces the stale 707b-2026-06-29 text)

> V3-EXQ-707c (2026-07-23, C2-release VALIDATION on a REPAIRED instrument; supersedes 707b; confirmed failure_autopsy_V3-EXQ-707c_2026-07-25; diagnostic; PROMOTES NOTHING) → weakens (NARROW). Replaces the stale withdrawn 707b-2026-06-29 note. CONTEXT: the 707b-2026-06-29 weakens was WITHDRAWN 2026-07-20 as a measurement_test_design_defect (hold-weighted entropy DV, +97.6% exposure imbalance); 707c recovers the question on a clean instrument (DV accumulated only on verified-fresh E3 selections). DECISIVE pre-registered test on a FULLY-LIVE substrate: all readiness gates passed. Load-bearing C1 FAILED: A1_LOOPS did not convert strict-above max(A0, the live null). Per ARC-110's pre-registered grid → the F-dominance conversion ceiling is INTRINSIC, NOT a single-arena-collapse artefact. WEAKENS the narrow single-arena-artefact SUB-hypothesis ONLY; does NOT falsify the architectural assertion. NARROWED (re-established on a valid instrument): loop segregation is necessary-but-not-sufficient; alone (with static arithmetic cross-loop arbitration) it does not lift the F-dominance ceiling. The missing dependency (learned DA-gated cross-loop arbitration, MECH-448/449/ARC-107) is SUBSTRATE-EXHAUSTED: 709/711/713 all substrate_ceiling. Do NOT re-queue another same-claim learned-arbitration validation letter. ARC-110 stays candidate / substrate_conditional / implementation_phase=v3.

## 7. Routing (user-confirmed)

**Governance-apply.** Replace the stale note; keep ARC-110 candidate/substrate_conditional. **No re-queue** (rescue path exhausted 709/711/713). **No substrate build** (exhausted path already built; a genuinely-different arbitration substrate is not yet articulated and is out of scope here). A redesign testing a *different* mechanism (new EXQ number, different claim_ids) remains allowed.

## 8. Hypothesis-space ledger (Step 9b): skipped cleanly

707c emits no `fanout_recommendation` and is not a pre-registered leg of any registry question owned by ARC-110. Noted cross-link: the registry's `conversion_ceiling_root` question (owned by MECH-457/ARC-065) carries an `H-f-dominance` leg that 707c reinforces (F-dominance is a real intrinsic ceiling, not a collapse artefact) — but force-mapping an ARC-110-tagged run onto a MECH-457/ARC-065 leg risks over-attribution. Recorded for a future MECH-457/ARC-065 governance/synthesis pass.
