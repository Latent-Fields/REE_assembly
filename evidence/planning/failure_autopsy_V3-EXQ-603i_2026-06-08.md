# Failure Autopsy: V3-EXQ-603i

**Date:** 2026-06-08T22:10:50Z
**Status:** confirmed (interactive gate passed)
**Scope:** single
**Experiment:** V3-EXQ-603i -- relief/safety escape-affordance bridge validation (diagnostic)
**Result:** FAIL | self-route `substrate_not_ready_requeue` | indexer flag `precondition_unmet`
**Validates (weights no claim):** SD-059 (architecture) + MECH-358 (bridge mechanism). `claim_ids: []`.
**Depends on:** V3-EXQ-603h. Retest of the `escape-affordance-bridge` substrate entry created by `failure_autopsy_V3-EXQ-603h_2026-06-08`.
**Supersedes:** `provisional_failure_autopsy_V3-EXQ-603i_2026-06-08.md` (manual scaffold).

---

## 1. Facts (no interpretation)

5 arms x 3 seeds [42, 43, 44], all on the 603h-INTACT base (MECH-279 PAG + SD-058/MECH-357 ilPFC gate + driver + fed harm stream + SD-056 e2 warmup).

| Arm | G_H frac | relief credit | safety credit | hazard median (per seed) |
|---|---|---|---|---|
| ARM_BASE_IA_ONLY | 0.00 | 0/3 | 0/3 | 45.0, 13.5, 25.5 |
| ARM_RELIEF_BRIDGE | 0.00 | **2/3** | 0/3 | 26.0, 14.5, 15.5 |
| ARM_SAFETY_BRIDGE | 0.00 | 0/3 | **0/3** | 26.0, 11.0, 18.5 |
| ARM_RELIEF_SAFETY_BRIDGE | 0.00 | **2/3** | **0/3** | 27.0, 12.0, 17.0 |
| ARM_NAV_CONTROL (spawn-in-reef, safety handed) | **0.00** | 0/3 | 0/3 | 36.0, 10.5, 26.5 |

Readiness preconditions: PAG freeze on base **3/3 (met)**; ilPFC gate engaged **3/3 (met)**; Stage-0 z_goal forced-feed control **2/3 (met)**; `each_enabled_bridge_half_fires_nonvacuously` **UNMET** (measured 0.0 vs 0.667 -- safety half 0/3).

**Two failures, neither a bridge verdict:**
1. The load-bearing failed precondition: the **safety half credited 0/3 in every arm** (relief half credited 2/3). The bridge could not be tested as designed.
2. The **nav-competence positive control (ARM_NAV_CONTROL) also returned G_H = 0.0** -- best hazard median ~36 steps vs the >=75 gate. Even with navigation-to-safety handed (spawn in the reef refuge), survival to the gate is unreachable.

Failed criterion class: **negative_control / readiness** (non-vacuity precondition + nav-competence positive control), not a discrimination criterion against the bridge.

## 2. Claim-layer map

`claim_ids: []` is correct: this is a substrate-readiness diagnostic that validates SD-059/MECH-358 *wiring* and weights no claim. SD-059 (architectural, `v3_pending`) and MECH-358 (mechanistic, `v3_pending`) both remain `candidate`. The test did **not** let either claim express itself -- so neither is weakened nor strengthened. The base defensive chain (SD-058/MECH-357 gate, MECH-279 PAG) is intact and engaged. The safety half draws on MECH-303/304 (response-produced / contextual safety), which are themselves `v3_pending` and whose predictor is not yet wired into the bridge.

## 3. Biological-reference triage (the core move)

Closest mechanism: **amygdala LA/BA -> NAcc relief/safety action-credit for active avoidance** (Moscarello & LeDoux 2013), with ilPFC freeze-suppression gating (SD-058/MECH-357), PAG execution (Tovote 2016), and gradual acquisition (Debiec & Sullivan 2017). The bridge is a **faithful biological translation, not a formal-definition import** -- so biology is a live existence proof for the mechanism *class*. Lit status: **present** (no `/lit-pull` commission needed).

Does the failure resemble a missing dependency of the reference mechanism? **Yes.** A relief/safety credit system with intact affect heads but no navigation-to-safety competence is the animal that has the credit machinery but cannot execute a directed escape route -- the FAIL is a **discovered prerequisite (navigation/survival competence)**, not a falsification.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (untested) | bridge never adjudicable; SD-059/MECH-358 unchanged |
| Biological reference | clear | Moscarello & LeDoux 2013; failure = missing navigation prerequisite signature |
| Prerequisites | missing | (a) nav/survival competence (scaffolded_sd054_onboarding P1/Stage-H, G1 0/3); (b) safety-half threat-absence predictor (MECH-303/304) unwired |
| Implementation | partial | relief half functional (2/3); safety half present but starved (no functional input) |
| Environment | wrong pressures / short budget | Stage-H survival >=75 unreachable even with safety handed |
| Measurement | adequate | nav-competence control + per-half non-vacuity gate are the right instruments |
| Integration | partially coupled | base chain coupled; bridge->escape->survival leg not, because nav competence absent |
| Scale / capacity | likely insufficient | Stage-H survival budget under-resourced (best median ~45) |

**Recommended epistemic_category: `substrate_ceiling`.** (Recommendation only -- not written to any manifest.)

## 5. Adjudication of the self-route

Per the diagnostic-adjudication gate, the `precondition_unmet` flag asks: was the precondition genuinely unmet (then the label may mislabel the *cause*), or is the precondition test wrong? Here the precondition (safety half non-vacuity) was **genuinely unmet** (0/3), so `substrate_not_ready_requeue` is honest -- do not treat as a bridge verdict. The autopsy's value-add is **naming the dominant blocker**: the nav-competence positive control failing proves that even if both halves credited, G_H is unscoreable until Stage-H survival competence clears. The route is therefore confirmed and **refined to nav-competence-primary**.

## 6. Learning extracted

- Navigation/survival competence is a hard prerequisite upstream of the relief/safety escape-affordance bridge; the nav-competence positive control failing is the load-bearing new datum vs 603h.
- The relief half is functional (2/3); the safety half is structurally starved (0/3) for lack of a trained threat-absence (MECH-303/304) predictor.
- Keep the nav-competence positive control + per-half non-vacuity gate in any retest harness -- they are what separate "bridge insufficient" from "competence ceiling."

## 7. Repair pathway / routing

**Routing: `implement-substrate` (amend, x2) -> then re-queue via the in-flight readiness predecessor.** No demotion (claim untested), no `/lit-pull` (biology present), no new substrate entry (both gaps already queued).

1. **AMEND `scaffolded_sd054_onboarding`** (PRIMARY) -- append the 603i ARM_NAV_CONTROL failure record (nav/survival-competence ceiling). The Stage-H survival leg (G1 >= 2/3, median >= 75) must clear before any bridge retest can score G_H.
2. **AMEND `escape-affordance-bridge`** (SECONDARY) -- append the 603i safety-half starvation failure record; the safety half needs the MECH-303/304 threat-absence predictor wired.
3. **Re-queue** the SD-059/MECH-358 bridge retest only after both clear. **V3-EXQ-653** (`e2_escape_affordance_linker_readiness_microdiagnostic`, queued by a parallel session) is the in-flight readiness predecessor -- do not mint a duplicate successor.

Draft `evidence_quality_note` for governance to write: see the `recommended_evidence_quality_note` field in the companion JSON (verbatim).

## 8. Coordination notes

- An active **governance cycle** (`governance-cycle-20260608T2151Z`) holds `substrate_queue.json` / `pending_review.md` / `claims.yaml` -- it is the intended consumer that will apply the two amends and mark 603i reviewed. This autopsy only produces the diagnosis artifact; it writes none of those files.
- **V3-EXQ-653** is already being queued by `queue-experiment-653-...` -- the re-queue routing points at it.
