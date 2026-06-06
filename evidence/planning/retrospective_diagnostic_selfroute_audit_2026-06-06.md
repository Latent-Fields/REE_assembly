# Retrospective Audit -- Legacy Diagnostic/Baseline Self-Routes That Drove a Governance Action

- **Generated (UTC):** 2026-06-06T09:31:29Z
- **Author session:** retro-diagnostic-selfroute-audit-20260606T0931Z
- **Type:** survey / triage memo (analysis + handoff only -- NO claims.yaml / manifest / substrate_queue / review_tracker edits)
- **Motivation:** the diagnostic-adjudication-gate (landed 2026-06-06, REE_assembly `5903c3bf72`;
  design `proposal_diagnostic_adjudication_gate_2026-06-06.md`; principle in
  `failure_autopsy_V3-EXQ-642_2026-06-06.md`) only flags diagnostics that carry the NEW manifest
  fields (`interpretation.preconditions[]` + `criteria_non_degenerate`). Every pre-existing
  diagnostic lacks those fields and is silently classed `adjudication="unverified"`, so it is never
  surfaced. This audit looks BACKWARD at that legacy population for the two proven-real failure modes:
  - **PRECONDITION_UNMET** -- a self-routed branch silently assumed a condition the run did not meet
    (canonical: V3-EXQ-642 routed `substrate_ceiling` on a FROZEN RANDOM ENCODER with SD-056 OFF, so
    the comparator was floored to 0 *by construction*; the correct route was re-queue, not a
    substrate-enrichment task).
  - **VACUOUS_PASS** -- an overall PASS rested on a degenerate criterion (arms bit-identical, zero
    variance, n below a floor) and that PASS cleared a v3_pending gate / marked a claim promotable.

---

## 1. Method and population

Enumerated from flat manifests `evidence/experiments/*.json` with
`experiment_purpose in {diagnostic, baseline}`, cross-referenced against
`claim_evidence.v1.json` `unlinked_runs` (90 entries).

| Population | Count |
|---|---|
| Flat diagnostic/baseline manifests | 119 |
| Unique EXQ tokens (NNN[letter]) | 96 |
| Tokens with an existing `failure_autopsy_*` artifact (EXCLUDED) | 20 |
| **Unaudited diagnostic/baseline tokens** | **76** |

"Drove an action" = the run is cited as the *justification* (not a forward-pointing validation target)
in one of: (a) `substrate_queue.json` `failure_record` / `implementation_log` (substrate task minted
or amended); (b) `claims.yaml` `evidence_quality_note` / `implementation_note` clearing `v3_pending`
or gating a promotion / code merge; (c) a `*_plan.md` / `thought_intake_*.md` node closed or routed.
Forward-pointing `validation_experiment` / "queued" citations were excluded -- those are the planned
check, not a self-route that already drove a decision.

The 642 failure mode requires a SELF-ROUTE that DROVE an action. The bulk of the 76 are
substrate-**landing** readiness diagnostics whose only "action" is unblocking a downstream behavioural
run -- low stakes (see Section 3). The high-stakes subset (Section 2) is where a self-route flipped a
gate, merged code, or minted/amended a substrate task.

---

## 2. Drove-an-action & unaudited -- per-run verdicts

Verdict legend: **sound** (self-route premise holds) / **suspect** (premise questionable, light concern)
/ **needs-full-autopsy** (642-style precondition/vacuity risk on a real action).

| Run (token) | Action it drove | Outcome / self-route | Verdict | Concern |
|---|---|---|---|---|
| **V3-EXQ-621a** | governance-cycle "cleared substrate-readiness diagnostic"; superseded V3-EXQ-621 (SD-054 scaffold) | PASS (`overall_pass=true`) | **needs-full-autopsy** | **VACUOUS_PASS-adjacent.** `overall_pass=true` while the load-bearing **`C2_z_goal_floor_met=false`** and `C1` only **6/12 cells completed**. The PASS is routed via C1-partial + C3 cascade; the substantive scientific gate (z_goal floor) FAILED. A partial triage exists (`z_goal_collapse_triage_2026-05-31.md`) but no full autopsy; the gate clear rests on the non-substantive criteria. |
| **V3-EXQ-608** | merged code to master + R2.a rule promotion path (`behavioral_diversity_isolation_plan.md`) | PASS diagnostic, self-route `R2a_e3_collapse_confirmed_large_gap` | **suspect** | Drove a **master merge** on a majority-label vote. Per-seed `top2_class_gap` is heterogeneous (0.0076 .. 0.52); one seed is near-zero. The "large_gap" majority is genuinely non-zero (not vacuous) but the routing should be re-checked for whether the near-zero seed undercuts "confirmed". |
| **V3-EXQ-611 / 611c** | MECH-341 rule R2.c promotion path + behavioural-successor routing | 611 FAIL -> 611c PASS (retune), self-route `R2a..._large_gap` | **suspect** | Same gap-measurement family as 608; 611c `mean_top2_class_gap` per seed 0.41 / 0.27 / 1.96 -- real spread, majority on 2 seeds. Non-degenerate, but the FAIL->retune->PASS chain drove a rule promotion; verify the retune did not simply move the threshold under the data. |
| **V3-EXQ-485** (SD-033b) | **`v3_pending` flipped true->false** (2026-04-28 governance) | PASS substrate-LANDING (UC1-UC5) | **suspect** | The only explicit `v3_pending` flip driven by a legacy diagnostic. It cleared a **wiring/landing** gate (instantiation, gate-modulates-update, bias-zero-at-init, backward-compat, reset). Mitigant: claim stays `candidate`; behavioural validation explicitly deferred to a successor; the flip cleared "is wired," not a promotion. Residual risk: UC2 ("gate modulates update") non-degeneracy is unverifiable from the flat manifest (`acceptance_checks={}` on the canonical run); UC3 ("bias zero at init") is by-construction. Low stakes, but it is a gate flip on an unverified self-route. |
| **V3-EXQ-522** | "substrate-ceiling demonstration"; cited in `infant_substrate_plan.md`, `arc_062_rule_apprehension_plan.md`, MECH cluster notes | PASS / supports | **suspect** | The ceiling was demonstrated **under a hand-coded reef-aware avoidance heuristic** (an oracle), not the trained agent. If any downstream node reads "522 PASS" as "the substrate is capable," the precondition (trained-agent capability) is unmet -- the oracle only shows the *task* is solvable. claims.yaml frames the heuristic-vs-trained gap honestly (L27250), which contains the risk; confirm no plan node treats it as substrate-capability evidence. |
| **V3-EXQ-264** (ARC-033) | tagged `does_not_support` on ARC-033 evidence record | FAIL, `C2_pred_norm_nontrivial_gt_0.01=false` | **suspect (evidence-record only)** | **Same trivial-prediction signature as 642** (`pred_norm` below the non-triviality floor -> all criteria fail by construction; likely an under-trained `E2_harm_s` forward model, not a real falsification). It did **not** drive a status action: ARC-033 is `architectural_commitment` (epistemic_category `substrate_coherence` -> promote/demote suppressed). So the harm is a latent `does_not_support` contaminant in the record, not a governance decision. Re-tag candidate if a trained-substrate re-run is ever done. |
| **V3-EXQ-592g** | "VALIDATED by V3-EXQ-592g" (MECH-342 maintenance-release) | PASS / supports | **sound** | Criteria are genuinely non-degenerate: `mech342_fires=1`, `decommit_transition_count=2`, `suppression beta_drop 0.4-0.6` over `*_below_floor_count=10` -- a real differential against the V3-EXQ-592f zero baseline. No vacuity signature. |
| **V3-EXQ-545** (MECH-314) | substrate-landed implementation_log (pending_validation) | reclassified `non_contributory` | **sound (self-aware)** | The note explicitly states "UC1-UC5 confirm API wiring but do NOT test the load-bearing claim ... behavioural validation required" -- it did not over-clear. Honestly scoped. |
| **V3-EXQ-620** (SD-037 axis-a) | justified the axis-(b) sustained-threat env-curriculum plan | PASS -> **superseded** | **resolved (already adjudicated)** | Already corrected via `/diagnose-errors` (2026-06-01, via V3-EXQ-625): the "identically-zero consumer-input distributions" read as "axis-(a) empirically unmeetable" were a **config artifact** (same-config bug) -- a textbook PRECONDITION_UNMET, but it was caught and superseded by 620b. No autopsy file, but adjudicated. *Handoff: confirm the axis-(b) curriculum plan it spawned is re-anchored on 620b, not 620.* |
| **V3-EXQ-470** (SD-029) | `substrate_queue` `failure_record` (candidate_v3_pending) | `None`/`weakens` | **sound (understood)** | Part of the known SD-029 monomodal-policy-cannot-balance issue (memory `V3 Current State`: EXQ-433/470 reclassified `non_contributory` because a monostrategy policy cannot generate balanced agent-vs-env distributions). Already understood; held pending MECH-269 V_s. |

---

## 3. The substrate-landing-PASS class (lower stakes -- summarized, not per-run)

~15 unaudited tokens drove a `candidate_substrate_landed` / `*_pending_validation` status or a
`v3_pending` "implemented" note purely as **substrate-landing readiness diagnostics**:
`542a, 544, 546, 547, 548, 568, 571, 576, 613, 617, 620b, 621, 626b, 461, 493`.

These are UC-style wiring checks (module instantiates, flag toggles, bit-identical OFF, reset clears
state). Their "action" is unblocking a *downstream behavioural* experiment, not promoting a claim.
Spot-check (568, 542a, 545) shows the pattern is self-aware -- notes repeatedly say "confirms API
wiring but does NOT test the load-bearing claim." **Class verdict: low priority.** The vacuity risk
here is bounded because none promotes a scientific claim; the worst case is a wiring PASS that lets a
behavioural successor run prematurely, which the successor itself then catches. Recommend a *sampling*
re-check (2-3 of these) rather than per-run autopsies, only if Section-2 items surface a systemic
pattern.

Not investigated (PASS diagnostics with no traced action, or pure forward-validation citations):
`214, 244a, 263a, 263b, 265, 265a, 332a, 385a, 418a, 418f, 418h, 432, 449, 449a, 449b, 477, 481b,
485a/b/c, 500, 500a, 519b, 521, 561, 563, 563a/b/c, 570, 577a, 578, 579, 580, 583, 584, 586, 609,
613, 614d, 618, 620b, 625, 625c, 626b, 634c, 635, 636, 637, 639, 641a`. Most are recent PASS readiness
probes or already-reclassified `non_contributory` rows; none traced to a gate-flip / merge / mint via
a self-route in this pass.

---

## 4. Prioritized full-`/failure-autopsy` candidates

Ordered by stakes x vacuity/precondition risk (highest first):

1. **V3-EXQ-621a** -- *highest*. A governance-cycle gate clear + supersession where `overall_pass=true`
   with the load-bearing **C2 z_goal floor FAILED** and C1 only 6/12. This is the closest legacy
   analogue to the 642 VACUOUS_PASS pattern that actually moved governance. The existing
   `z_goal_collapse_triage` memo is a starting point, not a closure.
2. **V3-EXQ-608** (and the **611/611c** chain) -- a self-route that **merged code to master** + drove a
   MECH-341 rule-promotion path on a majority-label vote with a near-zero seed in the spread. Verify the
   "large_gap confirmed" majority is robust to the low seed and that the 611c retune did not move the
   threshold under the data.
3. **V3-EXQ-485** (SD-033b) -- the only legacy **v3_pending flip** driven by a diagnostic. Lower stakes
   (landing gate, claim stays candidate) but worth a light confirmation that UC2 "gate modulates update"
   produced a non-zero differential and was not a 642-style bit-identical pass.
4. **V3-EXQ-522** -- confirm no downstream plan node treats the **oracle/heuristic** ceiling demo as
   trained-substrate-capability evidence (precondition-unmet risk if it does).

**Lower / no autopsy:** 592g (sound), 545/470 (self-aware / understood), 264 (evidence-record contaminant
only -- ARC-033 gating is suppressed; re-tag if re-run), 620 (already adjudicated via /diagnose-errors;
just re-anchor the axis-b plan on 620b).

---

## 5. Cross-cutting observations

- **The trivial-prediction signature recurs.** 642 (`pred_mag < floor`), 264 (`pred_norm_nontrivial
  > 0.01 = false`), and the 620 identically-zero distributions are the same shape: an untrained /
  undertrained substrate produces a degenerate measurement that a self-route then mis-reads as a
  scientific verdict (ceiling / unmeetable / does_not_support). A **P0 readiness gate** (assert the
  measured quantity clears its non-triviality floor *before* reading the criterion) -- exactly what the
  642 autopsy prescribed for 642a -- would have caught all three. This is the strongest argument for the
  proposal's `criteria_non_degenerate{}` field becoming a *validator* requirement (proposal Q2), not just
  an advisory manifest convention.
- **"overall_pass=true with the headline criterion false"** (621a) is a distinct, machine-detectable
  vacuity: a PASS carried by structural/partial criteria while the substantive one fails. Worth adding to
  the indexer's `_compute_adjudication` non-degeneracy heuristics (flag when `overall_pass` is true but a
  criterion tagged load-bearing is false).
- **Substrate-landing diagnostics are mostly self-aware** -- the "confirms wiring, not the claim" note is
  common, which bounds the legacy blast radius to a handful of Section-2 items rather than the full 76.

---

## 6. Scope note

This is a triage survey. No `/failure-autopsy` was run; no claims.yaml / manifest / substrate_queue /
review_tracker edits were made. The user / governance decides which Section-4 candidates get a full
autopsy. Priority-1 (V3-EXQ-621a) and Priority-2 (V3-EXQ-608 / 611c) are the two that moved real
governance state (a gate clear and a master merge) on a questionable self-route premise.
