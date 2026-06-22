# Failure Autopsy — V3-EXQ-654i (staging draft)

- **Run ID:** `v3_exq_654i_arc062_gapb_rule_apprehension_behavioural_falsifier_20260622T014706Z_v3`
- **Generated (UTC):** 2026-06-22T04:47:35Z
- **Mode:** staging / headless (scheduled `failure-autopsy-owed-sweep`) — `status: awaiting_human_confirmation`. Routing is a draft for the next interactive `/governance` walk; nothing auto-applies.
- **Scope:** single (but a load-bearing **cluster corroboration** of V3-EXQ-485k; see §6)
- **Outcome under autopsy:** `status: FAIL`, `evidence_direction: non_contributory`, self-route label `conversion_ceiling_persists_despite_demotion_route_mech449`
- **Claims tested:** MECH-309, ARC-062 (both `candidate` / `epistemic_category: substrate_ceiling` / `v3_pending: True`)
- **Supersedes:** V3-EXQ-654h (MECH-448 envelope all-admit no-op, `excluded_count==0` on the arc_062 bank)

---

## 1. Why this is the owed experiment

`pending_review.md` (generated 2026-06-21T19:28Z) lists only V3-EXQ-485k — which was **already autopsied earlier today** (`failure_autopsy_V3-EXQ-485k_2026-06-21`, confirmed/closed 19:51Z). It is **not** owed.

V3-EXQ-654i landed **after** that pending_review generation (result manifest committed `40646a3b79`, run timestamp 2026-06-22T01:47:06Z) and has **no autopsy artifact on disk**. It FAILed `non_contributory`. It is the single owed experiment at fire time.

## 2. Facts — reconstruction (no interpretation)

The script (`experiments/v3_exq_654i_arc062_gapb_rule_apprehension_behavioural_falsifier.py`) is a 2-arm × 3-seed × 350-ep behavioural falsifier. **ARM_ON** sweeps the candidate rule field (`use_candidate_rule_field=True`, `crf_persist=True` → LateralPFCAnalog rule-state bias) — the MECH-309 / ARC-062 manipulation under test. **MECH-448 F→eligibility demotion is ARMED as a matched constant on BOTH arms** (`use_f_eligibility_demotion=True`, floor 0.30 + 485j-style per-(arm,seed) `_calibrate_envelope_floor`). The script does **not** engage the MECH-449 Go/No-Go constitution (it was written/queued 2026-06-21 before MECH-449 was built; the label's "mech449" names the route the author flagged, not an active arm).

Pre-registered acceptance (from the script's `=== INTERPRETATION GRID ===`):
- **C1 (readiness / non-vacuity):** axis exercisable, GAP-A divergence real & bounded, ARM_ON rule field differentiated & matured, propagation non-vacuous, MECH-448 demotion live & actually excluding.
- **C2 (PRIMARY falsifier):** paired-by-seed committed-class-entropy lift of ARM_ON over ARM_OFF ≥ margin on ≥2/3 seeds.

Observed (`interpretation.preconditions` / `criteria_non_degenerate`):

| Gate | measured | threshold | met |
|---|---|---|---|
| C1a committed-class axis exercisable | 1.0 | ≥0.3 | ✅ |
| C1b GAP-A consumed-summary divergence | 0.0668 | ≥0.05 | ✅ |
| C1b consumed-summary bounded | 0.4416 | ≤1e6 | ✅ |
| C1c ARM_ON rule field differentiated & matured | 0.9128 | ≥0.3 | ✅ |
| C1d propagation non-vacuity (ARM_ON bias ≠ ARM_OFF) | 0.0270 | ≥0.001 | ✅ |
| C1e MECH-448 demotion live & excluding | 18.41 excl | >0 | ✅ |
| **C2 committed-class entropy lift (load-bearing)** | — | strict-above-by-margin | ❌ |

**Failed criterion: discrimination (C2).** Every readiness / non-vacuity gate passes; the single load-bearing discrimination criterion fails. This is the canonical **substrate-ceiling fingerprint** — and here it is unusually clean: the test is demonstrably non-degenerate (C1c–C1e all true), so this is **not** a vacuous-PASS or precondition-unmet self-route. The manipulation genuinely matured, genuinely propagated into the selection bias, and the demotion lever genuinely excluded candidates — yet committed-class diversity did not lift.

This matches the script's own pre-registered **FAIL(C1 holds, C2 fails)** branch verbatim: "the matured + maintained + differentiated rule pool's bias REACHES committed action AND the demotion lever is LIVE … but the differentiated rule_state STILL does not lift committed-class diversity EVEN UNDER the MECH-448 demotion lever that lifted the ceiling on GAP-A → `conversion_ceiling_persists_despite_demotion`; non_contributory; route to the MECH-449 Go/No-Go constitution follow-on. NOT a MECH-309/ARC-062 falsification."

## 3. Claim-layer mapping — did the test let the claim express itself?

- **MECH-309** (rule-apprehension mechanism) and **ARC-062** (rule-apprehension architectural slot) are both `candidate`, already `epistemic_category: substrate_ceiling`, `v3_pending: True`. `depends_on` includes SD-054, SD-029, MECH-256/269, ARC-062/063/077.
- The test exercised the claims **fairly at the apprehension/selection layer** (rule field matured, distinct rules minted, bias propagated). What it could **not** exercise is the *conversion* from a differentiated selection bias into committed-action class diversity — because the only conversion lever present (MECH-448 rank-preserving demotion) structurally cannot express the active No-Go *withdrawal* that committed-class carving requires. The FAIL therefore weighs against the **conversion substrate**, not against MECH-309/ARC-062. Pre-registered as `non_contributory`; **do not weaken the claims.**

## 4. Biological-reference triage

- **Closest mechanism:** basal-ganglia **Go/No-Go opponency** over an action-eligibility set. MECH-448 is the rank-preserving (indirect-pathway-like) demotion of an over-dominant channel; the missing complement is the **active No-Go** that *withdraws* commitment from lawfully-eligible-but-undesirable candidates (the direct/indirect opponency, MECH-260 generalised → MECH-449).
- **Is this a formal-definition import?** No — it is a biologically-grounded translation (BG opponency, ARC-107 constitution). So the autopsy output is **not** a `/lit-pull` commission.
- **Missing-dependency signature:** yes. Biologically, gating *eligibility* without an opponent No-Go cannot carve committed action — exactly the observed shape (eligibility demoted/excluded, bias differentiated, yet committed-class entropy flat). The FAIL is a **discovered prerequisite** (active No-Go needed), i.e. positive evidence for the MECH-449 dependency, not a falsification of the rule-apprehension claims.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | test fair at apprehension/selection layer; FAIL is conversion-substrate, not claim |
| Biological reference | clear | BG Go/No-Go opponency; demotion-without-active-No-Go is the missing-dependency signature |
| Prerequisites | missing | conversion needs the active No-Go (MECH-449), not engaged here |
| Implementation completeness | partial | MECH-448 demotion complete & live; MECH-449 built 2026-06-21 but not in this run |
| Environment adequacy | adequate | arc_062 spread F bank exercised; demotion excluded 18.4 candidates |
| Measurement adequacy | adequate | C2 is the right DV; non-degeneracy gates confirm it was measurable |
| Integration adequacy | partially coupled | rule field → bias coupling works; bias → committed-class conversion does not |
| Scale / capacity | adequate | matured pool, 350 ep, propagation non-vacuous |

**Recommended `epistemic_category`: `substrate_ceiling`** (recommendation only — governance applies).

## 6. Cluster pattern — the load-bearing signal

| Experiment | Claim(s) | Negative-control / readiness | Discrimination | Read |
|---|---|---|---|---|
| V3-EXQ-485k | MECH-263, SD-033b (devaluation face) | readiness/aggregate met | both DVs vacuous; C2 OFC regressed | demotion alone cannot express active No-Go *withdrawal* → MECH-449 |
| **V3-EXQ-654i** | MECH-309, ARC-062 (rule-apprehension face) | **all C1 met & non-degenerate** | C2 committed-class lift fails | same — demotion live & excluding, bias differentiated, conversion still blocked → MECH-449 |

**This is one structural property, not two independent bugs.** Two structurally different claim families (OFC devaluation vs lateral-PFC rule apprehension), tested through different substrates, converge on the identical conclusion: **MECH-448 rank-preserving demotion lifts the GAP-A foraging selection-face ceiling but does not generalise to behavioural conversion on the GAP-B composite — the residual is the F-dominance conversion ceiling (MECH-439), and the named fix is the MECH-449 active Go/No-Go opponency leg.** 654i is the cleanest instance yet: it is the only one with *all* non-degeneracy gates true, so it cannot be dismissed as a vacuous test.

## 7. Re-derive brake — FIRED (hard gate)

Prior `substrate_ceiling` / `non_contributory` autopsies tagging these claims (threshold = 2):
- **MECH-309: 16** prior (543f/h/i/k/l, 654/b/c/d/f/g/h, f-dominance-conversion-cluster, 695-696-cluster, 569f-661-654a, 543i).
- **ARC-062: 17** prior (same set + 690).

This is the modal 7–12× lettered-iteration burn the brake exists to stop. 654i is yet another letter circling the same ceiling against a demotion-only substrate.

**Brake actions (recorded in the JSON `re_derive_brake` field):**
- `route_to: implement-substrate` on `upstream_substrate` = the MECH-449 Go/No-Go constitution. **Already BUILT 2026-06-21** (ree-v3 `829e51e`; status `candidate`/`substrate_conditional`; selection-face falsifier V3-EXQ-689g queued). So the build half is satisfied.
- **REFUSE a same-claim test re-queue.** Do **NOT** queue a 654j that re-runs the MECH-448-only (demotion) stack against MECH-309/ARC-062 — that is precisely the loop the brake forbids. `/queue-experiment` Step 2.5 enforces the consumer half until the upstream substrate is built; it is now built, so the *only* permitted next test is one that engages MECH-449 **active No-Go** as the ARM_ON manipulation — a different mechanism (gate it behind V3-EXQ-689g confirming MECH-449 works at the selection face, mirroring how the 485 lineage's 485l is gated behind the MECH-449 build).

## 8. Learning extracted

1. MECH-448 rank-preserving demotion, even when **live and excluding 18.4 candidates on a non-degenerate bank**, does not convert a differentiated rule-apprehension bias into committed-action class diversity on the GAP-B composite — confirming the conversion ceiling is **structural** (the F-dominance/MECH-439 monopoly), not a calibration artifact of the 654h all-admit no-op.
2. Independent cross-substrate corroboration of the 485k devaluation-face finding: **demotion ≠ active No-Go.** Two faces, one fix (MECH-449).
3. The 654 lineage's re-derive loop is now formally braked: no further demotion-only letter on MECH-309/ARC-062.

## 9. Routing (DRAFT — awaiting human confirmation)

- **Routing:** `implement-substrate` (build half done) + gate any MECH-449-active retest behind V3-EXQ-689g. **No `/queue-experiment` for a same-substrate 654j.**
- **substrate_queue:** `action: amend` the existing `f_dominance_conversion_ceiling` entry (already records the MECH-449 build + 689g pending; unblocks MECH-309/ARC-062) with a 654i failure record.
- **claims.yaml:** no edit. MECH-309/ARC-062 stay `candidate`/`substrate_ceiling`/`v3_pending`; mark `pending_retest_after_substrate` (after MECH-449 validated). MECH-448 untouched (it fired and excluded correctly; this is not a MECH-448 weakens).
- **`/claim-synthesis`:** not triggered. The recurrence here is the *same-granularity re-derive* (brake territory), not granularity debt — MECH-309/ARC-062 are not coarse claims masking finer mechanisms; the conversion ceiling is already owned by ARC-107/MECH-449.

### Draft `evidence_quality_note` (for governance to write, verbatim)

> V3-EXQ-654i (arc_062 GAP-B rule-apprehension behavioural falsifier, 2026-06-22) FAILed non_contributory on the pre-registered FAIL(C1 holds, C2 fails) branch: all C1 readiness/non-vacuity gates met and non-degenerate (rule field matured 0.913, propagation non-vacuous 0.027, MECH-448 demotion live & excluding 18.4 candidates) yet the load-bearing C2 committed-class entropy lift failed — the differentiated rule-apprehension bias reaches committed action but does not convert to committed-class diversity even under the live MECH-448 demotion lever. Conversion ceiling persists despite demotion; NOT a MECH-309/ARC-062 falsification (claims unweakened, pending_retest_after_substrate behind MECH-449). Cross-substrate corroboration of V3-EXQ-485k (devaluation face): demotion alone cannot express the active No-Go withdrawal; route to the MECH-449 Go/No-Go opponency leg (built 2026-06-21, falsifier V3-EXQ-689g queued). Re-derive brake FIRED (16-17 prior substrate_ceiling autopsies on these claims): refuse a same-substrate 654j re-queue; next test must engage MECH-449 active No-Go.
