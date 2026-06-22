# Failure Autopsy — V3-EXQ-485m (P3-ofc valuation prong: OFC devaluation decoupled head)

- **Generated:** 2026-06-22T14:44:45Z
- **Scope:** single
- **Status:** confirmed (user gate answered 2026-06-22)
- **Target run_id:** `v3_exq_485m_sd033b_devaluation_decoupled_head_behavioural_20260622T143349Z_v3`
- **queue_id:** V3-EXQ-485m — **supersedes** V3-EXQ-485l
- **claim_ids:** SD-033b, MECH-263 (both `substrate_conditional`, candidate)
- **Outcome:** FAIL — recommended `non_contributory` (claim **UNWEAKENED**)
- **Campaign node:** `conversion_ceiling_campaign:P3-ofc` (valuation face) → **face-validated; folds into FULLSTACK arm**

## 1. Facts (no interpretation)

ARM_2 (trained OFC head + MECH-448 demotion ON + MECH-449 Go/No-Go ON) is the prong's real arm. Per seed:

| Criterion | Result | Per-seed evidence | 
|---|---|---|
| **C1** devaluation behavioural shift | **PASS 3/3** | `devaluation_selection_shift = 1.0` on all 3 seeds |
| **C1b** value-vector inversion (l2_shift>0.1 ∧ cosine<0) | **FAIL 1/3** | cosine = **+0.717, −0.456, +0.983** (only seed-1 inverts); l2 = 3.20, 2.03, 0.19 |
| **C2** committed-class discrimination separation | **FAIL 1/3** | sep-ratio = 0, **1e6**, 0 ; between-context TV = 0, **1.0**, 0 |
| **C3** silence control | **PASS 3/3** | clean — no spurious shift with no devaluation signal |

`acceptance.pass = False`. All 6 readiness preconditions **met** (head trained 3/3, devaluation head trained 3/3, devalued range supra-floor 3/3 — `max_test_bias_range_devalued` 1.037, high-threat range supra-floor 3/3, MECH-448 F-eligibility excluded 3/3, MECH-449 No-Go engaged **2/3** — `go_nogo_n_soft_applied` 0/1/1). **Non-vacuous** (seed-1 is an existence proof that the metric can fire: sep-ratio 1e6, TV 1.0, No-Go fired).

**Failed criterion class:** discrimination (C1b + C2). Negative control (C3) and absolute shift (C1) both pass — the substrate-ceiling fingerprint.

## 2. What the decouple changed (vs 485l)

485l's autopsy (`failure_autopsy_V3-EXQ-485l_2026-06-22`) fired the re-derive brake and routed to `implement-substrate`: the single shared `state_bias_head` under the ±0.5 clamp had no feasible gain band (485k gain 4.0 saturated the devalued range to 0; 485l gain 1.5 undershot the 0.05 readout floor at 0.031) because the same head must also carry the C2 high-threat discrimination range — devalued magnitude was traded against C2. The named upstream substrate (a **decoupled** `devaluation_bias_head` with an independent ±2.0 clamp) was built (ree-v3 main `758956f`). **485m is the legitimate, brake-exempt retest on that built substrate** — not another letter circling the shared-clamp ceiling.

**The decouple worked for what it targeted:** magnitude is now adequate (l2 shifts 3.2/2.0/0.19, devalued range 1.037 supra-floor), the No-Go viability trigger now fires 2/3 (was 1/3 in 485l), and the C1 selection-shift is now robust **3/3** (was magnitude-starved in 485l).

**But it exposed a deeper blocker.** With magnitude no longer the constraint, the devaluation head **shifts committed selection (C1 3/3) without consistently inverting the value vector**: 2/3 seeds have the high-threat and devalued bias vectors *positively* correlated (cosine +0.72, +0.98 — it scales the value landscape rather than flipping it), and committed-class discrimination separates only 1/3. The 485l clamp-starvation explanation for the C2 failure is now **ruled out**; the residual blocker is the conversion itself, localised to vector-inversion-robustness + committed-class separation.

## 3. Claim-layer mapping

- **SD-033b** (OFC-analog specific-outcome prediction + task-structure cognitive map; `design_decision`, `substrate_conditional`, candidate) — **intact / UNWEAKENED.** C1 3/3 shows the OFC devaluation representation genuinely expresses a behavioural shift; the claim's mechanism is exercised, not falsified.
- **MECH-263** (OFC-analog state-space + specific-outcome representation; `mechanism_hypothesis`, `substrate_conditional`, `v3_pending`, candidate) — **intact / UNWEAKENED**, with a **noted measurement nuance**: the head shifting selection without inverting the value vector (2/3 seeds) is a candidate signature of a representational shortcut bearing specifically on the *specific-outcome* clause. Not falsifying (C1 fires); flagged for the leave-one-out ablation to watch if the full-stack arm fails.

Both claims are already `substrate_conditional` → promote/demote suppressed. This autopsy does not change their status; it appends a failure record and a face-validation note.

## 4. Biological-reference triage

- **Closest reference mechanism:** OFC outcome-specific value representation and outcome-devaluation re-ranking of action selection (action–outcome / goal-directed control via OFC + dorsomedial striatum). **Faithful biological translation, not a formal-definition import.**
- **Dependencies in real brains:** outcome devaluation does not restructure the action repertoire on its own — it acts *through* the striatal Go/No-Go pathways and eligibility/credit machinery (i.e., the assembled basal-ganglia selection stack).
- **Does the failure match a missing-dependency signature?** **Yes.** A valuation signal that moves behaviour (C1) but fails to convert to committed-class diversity in isolation is exactly what you'd expect if a known dependency — the *assembled* BG selection stack — is only partially present (demotion + Go/No-Go engaged but not co-armed/tuned as a stack; root-C commit-duration absent). This is a discovered/strengthened-prerequisite signal, **not** falsification.
- **lit_status:** present/partial (mechanism is well-evidenced biology). Routing is **not** `/lit-pull`.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | C1 3/3 lets the claim express itself; UNWEAKENED |
| Biological reference | clear | OFC outcome-devaluation / A-O control; faithful, not formal import |
| Prerequisites / dependencies | partially present | assembled BG stack (demotion+Go/No-Go+floor+root-C) is the dependency; only partly co-armed |
| Implementation completeness | complete (for the prong) | decoupled `devaluation_bias_head` built (758956f); trains, biases, No-Go fires; 485l clamp gap fixed |
| Environment adequacy | adequate | — |
| Measurement adequacy | adequate | C1/C1b/C2/C3 well-posed, per-seed gated; seed-1 existence proof confirms non-degeneracy. Nuance: C1b reveals shift-without-inversion |
| **Integration adequacy** | **isolated / partially coupled** | **dominant layer** — single valuation face does not convert; conversion hypothesised emergent from the assembled stack |
| Scale / capacity | adequate | 120 grad updates, ~1880 loss terms/arm |

**Dominant diagnosis → epistemic_category `substrate_conditional`** (the conversion the claims need depends on the planned-but-not-yet-assembled full-stack arm). Keep the existing classification.

## 6. Convergent-pattern read (the load-bearing signal)

485m is the **3rd convergent "fails-C2-alone" data point**, across structurally-different faces:

| Experiment | Face | Lever | C2 (committed-class separation) alone |
|---|---|---|---|
| V3-EXQ-654i | selection | MECH-448 demotion | FAIL alone |
| V3-EXQ-654j | selection | MECH-449 Go/No-Go | FAIL alone |
| **V3-EXQ-485m** | **valuation** | **OFC devaluation (decoupled head)** | **FAIL alone (1/3)** |

This is **one structural property, not three independent bugs:** no single face converts per-candidate diversity to committed-class diversity in isolation. It is the direct motivation for the `conversion_ceiling_campaign` full-stack arm — conversion is hypothesised **emergent from the co-armed assembled stack** (the full basal-ganglia function set), which is exactly the campaign hypothesis under construction.

## 7. Learning extracted

1. **Decoupling the devaluation head removed clamp-starvation as the C2 blocker.** With adequate magnitude and an engaged No-Go, the valuation face still fails C2 alone — so the conversion ceiling is not an instrumentation/magnitude artifact at the valuation face.
2. **C1 3/3 face-validates P3-ofc** as a behaviour-mover — the prong robustly shifts committed selection on devaluation, which is what the full-stack arm needs from the valuation face.
3. **Shift-without-inversion (C1b 1/3, cosine +0.7/+0.98 on 2/3 seeds)** is a noted weakness in the OFC valuation representation (possible shortcut on the specific-outcome clause of MECH-263) — carried as a watch item for the full-stack leave-one-out ablation, not a blocker to folding in.
4. Third convergent confirmation that **conversion is emergent from the assembled stack**, not any single face.

## 8. Routing — user gate answered

**User decision (2026-06-22):** *Yes — fold P3 in; C1 3/3 suffices.* Mark `conversion_ceiling_campaign:P3-ofc` **face-validated**; amend the substrate entry; **no new isolated valuation-face experiment**.

- **Re-derive brake: FIRED** — 11th `substrate_ceiling`/`non_contributory` autopsy tagging MECH-263/SD-033b (priors: 485e, 485g, 485h, 485i, 485j, 485k, 485l, batch9, f-dominance-conversion-cluster, 695-696-f-dominance-cluster). **Refuses a 485n** isolated valuation-face re-queue.
- **Routing:** `implement-substrate` — fold P3-ofc into the `conversion_ceiling_campaign:FULLSTACK` arm (co-armed demotion + Go/No-Go + adaptive-floor + [root-C, once built] + **OFC-decouple ON**, sweep `use_candidate_rule_field`, DV = committed-class entropy C2). A redesign testing a *different* mechanism (outcome-specific encoding) would be brake-exempt (new EXQ); another 485 letter is not.
- **Substrate write (for `/governance`):** `amend` substrate entry `f_dominance_conversion_ceiling` — append the 485m failure record and advance the P3-ofc prong line to face-validated/composition-ready so the campaign full-stack arm can include the OFC-decouple lever.

### Draft `evidence_quality_note` (governance to write; do not write here)

> 2026-06-22 (failure_autopsy_V3-EXQ-485m CONFIRMED -> non_contributory; claim UNWEAKENED): V3-EXQ-485m (ree-cloud-4) supersedes 485l; FAIL/non_contributory/non_degenerate on the DECOUPLED devaluation_bias_head (ree-v3 758956f). Decouple fixed 485l clamp-starvation: C1 devaluation behavioural shift now 3/3 and No-Go engages 2/3, but C1b vector-inversion 1/3 (cosine +0.72/+0.98 on 2/3 seeds = shift-without-inversion) and C2 committed-class separation 1/3. Ruling out magnitude artifact, the valuation face does not convert in isolation. Claim mechanism EXERCISED not falsified (C1 3/3); status unchanged (substrate_conditional). P3-ofc face-validated (user gate 2026-06-22) -> folds into conversion_ceiling_campaign:FULLSTACK arm. 3rd convergent fails-C2-alone datum (654i demotion, 654j Go/No-Go, 485m OFC) = conversion is emergent from the assembled stack. Re-derive brake FIRED (11th substrate_ceiling reading on SD-033b/MECH-263): a 485n isolated valuation-face re-queue is REFUSED; next test is the co-armed full-stack arm.

## 9. Supersession

V3-EXQ-485m supersedes V3-EXQ-485l. `/governance` should set `evidence_direction: superseded` on the 485l manifest (with note) so it stops scoring, per the supersession policy.
