# Failure Autopsy — V3-EXQ-654j

- **Generated (UTC):** 2026-06-22T14:12:44Z
- **Scope:** single
- **Status:** confirmed (user-approved routing, interactive gate 2026-06-22)
- **Run:** `v3_exq_654j_arc062_gapb_rule_apprehension_nogo_behavioural_falsifier_20260622T135939Z_v3` (ree-cloud-2)
- **Queue:** V3-EXQ-654j — supersedes V3-EXQ-654i
- **Claims tested:** MECH-309, ARC-062
- **Outcome:** FAIL · manifest self-route `evidence_direction: non_contributory`, label `conversion_ceiling_persists_despite_active_nogo_route_next_arc107_ledger_component`

> **RECONCILED 2026-06-22T14:30Z (session reconcile-factorb-refuted-689c-routing).** The routing
> below (§5–§7) names **Factor B near-tie commit-temperature** as the user-approved next ARC-107
> ledger component. That route is **SUPERSEDED** — Factor B was already **refuted at the selection
> face** the day before, by the dedicated Factor-B-alone gap-scaled commit-T isolation
> **V3-EXQ-689c** (manifest
> `v3_exq_689c_mech439_factor_b_gap_scaled_t_isolation_20260621T022028Z_v3.json`, landed
> 2026-06-21, reviewed): **FAIL / non_contributory / `conversion_ceiling_persists_despite_conflict_grade`**,
> readiness ALL met (route-range 0.2158, e2 pairwise 0.0633, t_eff varies 3/3), **C_PRIMARY 1/3**
> (a0b1 selected-entropy 0.6646 vs collapsed ~0.6503; need 2/3) and **C_GAPBLIND_B 0/3** (the flat-hot
> control ARM_FIXED_HOT_T 0.6684 was *higher* than gap-scaled a0b1 0.6646 → the lift is not
> gap-scaling). The 654j interactive-gate decision did not fold in 689c. A `/queue-experiment`
> session on 2026-06-22 correctly **declined to queue the planned 654k Factor-B GAP-B falsifier**
> because its selection-face gate (689c) was unmet. **Corrected next route:** the conflict-grade
> near-tie parametric family is fully exhausted (Factor A inert per 689a + Factor B refuted per
> 689c); the live routes for the conversion ceiling are the **root-C commit/release-DURATION face
> (rung 6 of `f_dominance_conversion_ceiling`, PARKED 2026-06-22 awaiting the closure-exclusive
> de-commit eval substrate)** or the **V4 rungs 3–5** — **NOT** another GAP-B eligibility/commit-T
> behavioural letter. This reconcile PROMOTES NOTHING; MECH-309/ARC-062 remain
> substrate_ceiling / `pending_retest_after_substrate`, UNWEAKENED.

## 1. Facts (self-route adjudicated, not merely trusted)

654j ports the GAP-B committed-class behavioural falsifier onto the **MECH-449 active Go/No-Go
eligibility constitution** (ARC-107 opponency leg), armed as a matched-stack constant on BOTH arms
on top of the MECH-448 demotion stack; the only swept variable is `use_candidate_rule_field`.
Primary DV: committed-class entropy. Phased P0(200 e2-train)/P1(90 frozen-encoder bias-head
REINFORCE)/P2(60 frozen measure).

All seven C1 readiness / non-degeneracy gates **MET and non-degenerate**:

| Gate | Met | Measured / threshold |
|---|---|---|
| C1a committed-class axis exercisable, both arms | ✅ | 1.0 / 0.3 |
| C1b GAP-A consumed-summary divergence, both arms | ✅ | (majority-of-seeds gate satisfied) |
| C1c ARM_ON rule field differentiated + matured | ✅ | 0.975 / 0.30 frac-active |
| C1d propagation non-vacuity (ON bias ≠ OFF bias) | ✅ | 0.0606 / 0.001 |
| C1e MECH-448 demotion live + excluding, both arms | ✅ | 17.76 excluded / >0 |
| **C1f MECH-449 active No-Go live + suppressing, both arms** | ✅ | **1.549 / >0** |

The single **load-bearing C2 committed-class entropy lift FAILED**:

- Requirement: paired lift ≥ 0.05 nats on ≥ 2 of 3 seeds.
- Observed per-seed lift: **seed42 +0.1876, seed43 +0.0001, seed44 −0.0227** → only **1/3** seeds.
- ARM_OFF mean committed-class entropy 0.9559 vs ARM_ON 1.0110 (mean +0.055, carried entirely by
  seed42; not reproducible across seeds).

This is the **pre-registered FAIL(C1 holds, C2 fails)** branch. By the experiment's own three-branch
no-weakens map this is **NOT a falsification** of MECH-309/ARC-062 — the claims are UNWEAKENED.

654j was the **legitimately brake-sanctioned successor**: the 654i autopsy fired the re-derive brake
and permitted exactly one next test — "engage MECH-449 active No-Go as the ARM_ON manipulation, gated
behind V3-EXQ-689g confirming MECH-449 at the selection face." 689g PASSED 3/3 and MECH-449 was
promoted candidate→provisional (2026-06-22); 654j ran that sanctioned test. The brake-release was valid.

## 2. The load-bearing new signal

654i (MECH-448 rank-preserving demotion) and 654j (MECH-449 active Go/No-Go) have now tested the
**two main constitutional eligibility-governance legs** of ARC-107. Both **PASS at the selection
face** (689d 0.938 vs 0.371; 689g 3/3) yet **neither converts to committed-class behavioural
diversity** at the C2 face. This is independent cross-leg corroboration that the conversion ceiling
is **structural and downstream of selection** — selection-level eligibility governance is intact and
live, but the differentiated rule-apprehension bias does not propagate to committed-class diversity.

Per the ARC-107 component table, the remaining components are: Factor A conflict-graded width
(**inert** per 689a), Factor B near-tie commit-temperature (**REFUTED at the selection face** — see
the RECONCILED banner above: 689a's 2/3-alone read was overturned by the dedicated isolation
**V3-EXQ-689c**, C_PRIMARY 1/3 / C_GAPBLIND_B 0/3, so it is *not* a live next lever), and the
post-commit latch (assigned to **root C of `f_dominance_conversion_ceiling`**,
commit-entry-decisiveness — rung 6, currently PARKED awaiting the closure-exclusive de-commit
substrate). With Factor A inert and Factor B refuted, the conflict-grade near-tie parametric family is
fully exhausted at the selection face.

## 3. Claim-layer map

- **MECH-309 / ARC-062:** claims tested under conditions where they could express themselves (all C1
  readiness + non-vacuity gates met, non-degenerate). The FAIL is on the load-bearing discrimination
  criterion (C2), pre-registered as a non-weakens branch. Claims **intact** — substrate_ceiling,
  `pending_retest_after_substrate`.
- claim_ids accuracy: MECH-309 + ARC-062 correctly reflect what 654j tested (the GAP-B committed-class
  behavioural conversion of the rule-apprehension bias). No inherited-tag contamination.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | pre-registered non-weakens; claims unweakened |
| Biological reference | clear | BG selector constitution (ARC-107, L2-grounded); Go/No-Go opponency faithful (Kravitz 2010, Mink 1996). Failure resembles intact action-*selection* that does not reach varied *committed* programs — a commit/latch-face bottleneck, not an eligibility-governance deficit |
| Prerequisites | missing | commit-entry-decisiveness / post-commit latch (root C of f_dominance_conversion_ceiling) is the unbuilt dependency that the selection→commit conversion needs |
| Implementation | complete (eligibility legs) | MECH-448 demotion + MECH-449 Go/No-Go both built, live, suppressing |
| Environment | adequate | C1a/C1b confirm the committed-class axis is exercisable + non-degenerate on both arms |
| Measurement | adequate | C2 is the correct DV; non-degenerate (C2_paired_lift variance present, seed42 +0.19) |
| Integration | gap at selection→commit | live eligibility-governance legs do not propagate to committed-class behaviour |
| Scale | adequate | matured rule pool (frac-active 0.975), full-scale P0/P1/P2 |

**Recommended epistemic_category:** `substrate_ceiling`.

## 5. Re-derive brake

**Fired: true.** This is the **18th** prior substrate_ceiling/non_contributory autopsy tagging
MECH-309 (**19th** for ARC-062). Threshold is 2.

**User decision at the interactive gate (2026-06-22) — SUPERSEDED 2026-06-22, see the RECONCILED
banner at top:** route to the **literal next ARC-107 ledger component** — queue Factor B near-tie
commit-temperature as the next ARM_ON behavioural falsifier. This exercised the brake's
**different-mechanism exemption**: Factor B is a structurally different ARC-107 lever from the two
now-exhausted eligibility-governance legs (demotion, Go/No-Go), and it matched the manifest's own
pre-registered "route to next ARC-107 ledger component." **[CORRECTION:]** the brake now **DOES refuse
this re-queue** — Factor B was already refuted at the selection face by V3-EXQ-689c (FAIL; C_PRIMARY
1/3, C_GAPBLIND_B 0/3), so the section-7 selection-face gate is unmet and the 654k Factor-B letter was
declined 2026-06-22. The brake continues to refuse any further *eligibility-governance* letter as
well; the conflict-grade near-tie parametric family (Factor A + Factor B) is exhausted at the
selection face.

## 6. Learning extracted

- The two main ARC-107 eligibility-governance legs — MECH-448 rank-preserving demotion (654i) and
  MECH-449 active Go/No-Go (654j) — both PASS at the selection face but NEITHER converts a
  differentiated rule-apprehension bias into committed-class behavioural diversity (C2). Independent
  cross-leg corroboration that the conversion ceiling is structural and **downstream of selection**.
- C1f confirms the MECH-449 active No-Go was genuinely live and suppressing (1.55 > 0) on both arms —
  so this is not an inert-No-Go artifact. The active No-Go leg alone is insufficient for behavioural
  conversion.
- The eligibility-governance face of ARC-107 is now exhausted for GAP-B conversion. The remaining
  ARC-107 components are Factor A (inert per 689a), Factor B (near-tie commit-temperature — **REFUTED
  at the selection face by V3-EXQ-689c**, see the RECONCILED banner; not a live next lever), and the
  post-commit latch (owned by root C, rung-6 PARKED). Continued eligibility-leg letters are braked,
  and the conflict-grade near-tie parametric family is exhausted — the corrected next route is root-C
  rung-6 (PARKED) or V4, NOT another GAP-B eligibility/commit-T letter.

## 7. Routing

**[SUPERSEDED 2026-06-22 — see the RECONCILED banner at the top.]** The original routing below sent
the next test to a Factor-B near-tie commit-temperature falsifier. That route is dead: it explicitly
required gating the Factor-B falsifier "behind its selection-face validation (689a/689c Factor-B
isolation)", and **689c failed that gate** (FAIL/non_contributory; C_PRIMARY 1/3, C_GAPBLIND_B 0/3,
flat-hot control higher than gap-scaled). The selection-face precondition is therefore UNMET, so no
Factor-B GAP-B behavioural letter (654k or otherwise) is warranted — the `/queue-experiment` session
on 2026-06-22 correctly declined to queue it.

**Corrected routing:** no `/queue-experiment` dispatch on the conflict-grade near-tie parametric
family (Factor A inert + Factor B refuted = exhausted at the selection face). The conversion ceiling's
live routes are **(a) the root-C commit/release-DURATION face** — rung 6 of
`f_dominance_conversion_ceiling`, currently **PARKED** (2026-06-22, design-rethink V3-EXQ-460j)
awaiting a **closure-exclusive de-commit eval substrate** (an `/implement-substrate` BUILD chip owns
this; not a `/queue-experiment` item) — **or (b) the V4 rungs 3–5** (divisive-normalisation pooled
denominator / output-null preparatory subspace / cross-tick quality-diversity archive). MECH-309 /
ARC-062 stay `substrate_ceiling` / `pending_retest_after_substrate`, UNWEAKENED. PROMOTES NOTHING.

---

### Original routing (preserved for the record — DO NOT ACT ON; superseded above)

**`queue-experiment`** (must go through the `/queue-experiment` skill) — next ARC-107 ledger
component: **Factor B near-tie commit-temperature** as the swept ARM_ON, same GAP-B committed-class
behavioural DV, same three-branch no-weakens map (PASS → supports MECH-309/ARC-062 + closes
behavioral_diversity_isolation:GAP-I; FAIL C1-holds/C2-fails → route to next component, NOT a
weakens; FAIL C1-fails → substrate_not_ready_requeue). Gate the Factor-B falsifier behind its
selection-face validation (689a/689c Factor-B isolation) exactly as 654j was gated behind 689g, and
carry the C1f-style non-vacuity gate (Factor B must be live + actually hotting near-ties on both
arms). `/queue-experiment` decides letter-vs-number (different mechanism argues for a new number; same
DV/claim argues for a 654-lineage letter).

### Draft `evidence_quality_note` (for /governance to write — NOT written here)

> V3-EXQ-654j (FAIL, non_contributory, failure_autopsy_V3-EXQ-654j_2026-06-22): pre-registered
> FAIL(C1 holds, C2 fails) clean substrate-ceiling. All seven C1 readiness/non-vacuity gates met &
> non-degenerate — incl. C1f confirming the MECH-449 active No-Go live & suppressing (1.55) on both
> arms — but the load-bearing C2 committed-class entropy lift FAILED (1/3 seeds; +0.19/+0.0001/−0.02).
> The two main ARC-107 eligibility-governance legs (MECH-448 demotion @654i, MECH-449 Go/No-Go @654j)
> both PASS at the selection face yet NEITHER converts to committed-class behavioural diversity:
> conversion ceiling is structural and downstream of selection. Claims UNWEAKENED
> (substrate_ceiling / pending_retest_after_substrate). Re-derive brake fired (18th MECH-309 / 19th
> ARC-062); further eligibility-governance letters refused. RECONCILED 2026-06-22: the
> originally-recorded next route (Factor B near-tie commit-temperature) is SUPERSEDED — Factor B was
> refuted at the selection face by V3-EXQ-689c (FAIL/non_contributory; C_PRIMARY 1/3, C_GAPBLIND_B 0/3,
> flat-hot control 0.6684 > a0b1 0.6646), so the conflict-grade near-tie parametric family (Factor A
> inert + Factor B refuted) is exhausted at the selection face. Corrected next route: root-C
> commit/release-DURATION face (rung 6, PARKED) or V4 rungs 3–5, NOT another GAP-B eligibility/commit-T
> letter.
