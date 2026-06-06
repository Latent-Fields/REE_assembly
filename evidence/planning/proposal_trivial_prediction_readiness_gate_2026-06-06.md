# Proposal: Readiness / Non-Degeneracy Auto-Detection -- catch the trivial-prediction self-route the author cannot see

- **Status:** ACCEPTED 2026-06-06 -- user confirmed all four leans (Section 7): (Q1) reuse the
  landed `preconditions[]` (readiness-kind entries carry `measured`+`threshold`; indexer recomputes
  `met`) rather than a new `readiness[]` array; (Q2) `SUBSTRATE_VERDICT_LABELS =
  {substrate_ceiling, substrate_conditional, does_not_support}` + suffix patterns
  `*_nondiscriminative` / `*_unmeetable`, excluding `non_contributory`; (Q3) WARN-then-ERROR (ERROR
  gated on a cycle of real post-convention diagnostics, per the parent proposal's condition);
  (Q4) defer the Part-4 retrospective sweep. Implementation chip spawned; NOT yet built -- this doc
  records the design + sign-off; the implement session will flip this to IMPLEMENTED.
  NOTE on Q1: because we reuse `preconditions[]`, the convention's field is a precondition entry of
  the *readiness kind* carrying `measured`+`threshold`+`control`; Section 3's `readiness[]` examples
  should be read as that specialization, not a separate array.
- **Author session:** proposal-trivial-prediction-readiness-gate-20260606T0945Z
- **Generated (UTC):** 2026-06-06T09:45:34Z
- **Parent:** `proposal_diagnostic_adjudication_gate_2026-06-06.md` (ACCEPTED + IMPLEMENTED
  2026-06-06). This is its **deferred Q2 half**, made specific to one recurring signature.
- **Motivating evidence:** `retrospective_diagnostic_selfroute_audit_2026-06-06.md` Section 5
  cross-cutting finding -- the trivial-prediction signature recurs across **V3-EXQ-642, 264, 620**.
- **Scope:** governance machinery only. One manifest convention + one static-lint script + one
  indexer function. No claim-confidence math, no lit/exp, no `ree_core` change. Backward-compatible.

---

## 1. The gap the landed gate does NOT close

The diagnostic-adjudication gate that landed today (`_compute_adjudication` in
`build_experiment_indexes.py:120-157`) is **entirely author-dependent**: it fires
`precondition_unmet` only if the script author populated `interpretation.preconditions[].met = false`,
and `vacuous_pass` only if the author populated `criteria_non_degenerate{...: false}`. A legacy or
careless manifest with neither structure is silently `unverified` -- surfaced, not blocked.

The **trivial-prediction signature is precisely the case the author will not flag**, because the
degenerate number looks *fine* (or even good) at authoring time:

| Run | The degenerate measurement | What it *looked* like | The self-route it drove |
|---|---|---|---|
| **V3-EXQ-642** | `pred_mag < 0.05` floor every step -> `outcome_mismatch == 0` by construction | `wf_mse ~ 2e-5` -- looked like an *excellent* forward-model fit | `substrate_ceiling_comparator_nondiscriminative` (mint enrichment task) |
| **V3-EXQ-264** | `pred_norm_nontrivial > 0.01 == false` (E2_harm_s forward predictions ~0) | a clean 3-criterion FAIL | `does_not_support` on ARC-033 (record contaminant) |
| **V3-EXQ-620** | pooled consumer-input distributions **identically zero** | a definite, reproducible "axis (a) unmeetable" | justified the entire axis-(b) sustained-threat curriculum plan |

In all three an **untrained / undertrained / mis-configured substrate produced a degenerate
measurement, and a self-route read that degeneracy as a scientific verdict** (ceiling /
does-not-support / unmeetable). The common root: a discrimination criterion was read off a
**learned or measured quantity that never cleared its own non-triviality floor**. The author had no
reason to write `met: false` -- the low `wf_mse` actively *masked* the problem.

The V3-EXQ-642 autopsy already prescribed the fix **for 642a specifically**: a P0 readiness gate that
asserts `pred_mag` clears the floor *before* reading C0. This proposal **generalizes that one-off
prescription into a rule + machine check** so the next 264/620 cannot route silently.

A second, related signature the audit surfaced (V3-EXQ-621a): `overall_pass == true` while the
**load-bearing criterion failed** (`C2_z_goal_floor_met == false`, PASS carried by C1 6/12 + C3). The
author's own `overall_pass` aggregation hid a failed substantive gate. Author-supplied
`criteria_non_degenerate` would not catch this either -- the criteria were non-degenerate; the
*aggregation* was the problem.

---

## 2. Design principle

- **Do not trust the author's boolean; recompute it.** Where a readiness quantity is exposed in a
  canonical manifest field, the indexer recomputes `met = (measured >= threshold)` itself. An author
  who emits `met: true` wrongly (or omits it) is caught.
- **Require the readiness declaration only for the high-stakes label class.** A diagnostic that
  self-routes to a *substrate-verdict* label (`substrate_ceiling`, `substrate_conditional`,
  `does_not_support`, `*_nondiscriminative`, `*_unmeetable`) is making a claim that the substrate
  is the limit -- which is **only legitimate on a substrate that was trained to the level the claim
  presupposes**. That class must declare a readiness precondition. Benign smoke / onboarding /
  wiring diagnostics are untouched (they route to landing labels, not verdict labels).
- **Self-route below-floor to re-queue, never to a verdict.** A measured quantity below its floor
  means "substrate not ready," whose only correct route is re-queue at an adequate P0 -- exactly the
  642 -> 642a decision.
- **Backward-compatible + proportionate.** New fields optional; enforcement is warn-then-error
  (mirrors the `epistemic_category` precedent); legacy `unverified` stays surfaced-not-blocked.

---

## 3. The machinery (three parts, exact insertion points)

### Part 1 -- Author-side P0 readiness-assert convention (`/queue-experiment`)

Generalize the 642a prescription into a standing rule. Any diagnostic that reads a discrimination
criterion off a **learned or measured quantity** (forward-model prediction magnitude, comparator
mismatch, cross-arm distribution variance, event/contact counts) MUST, in P0/setup, measure that
quantity on a **known-positive control** and emit it under a canonical field:

```jsonc
"interpretation": {
  "label": "...",
  "readiness": [
    {
      "name": "world_forward_pred_mag_supra_floor",
      "measured": 0.013,
      "threshold": 0.05,
      "control": "known-successful move in P0",   // what makes this a positive control
      "met": false                                 // indexer RECOMPUTES from measured/threshold
    }
  ],
  // existing landed fields unchanged:
  "preconditions": [ ... ],
  "criteria_non_degenerate": { ... }
}
```

- `readiness[]` is a **specialization of the landed `preconditions[]`** carrying `measured` +
  `threshold` so the indexer can recompute `met`. (Implementation choice for sign-off: a new
  `readiness[]` array, OR a convention that `preconditions[]` entries of the readiness kind always
  carry `measured`+`threshold`. The latter reuses the landed gate verbatim -- see Q1.)
- If any `met` is false, the script self-routes to a **`substrate_not_ready_requeue`** label, NOT to
  a substrate-verdict label.
- `/queue-experiment` Step-3.5 checklist gains one question: *"Does this diagnostic read a criterion
  off a learned/measured quantity? If so, does it measure that quantity on a positive control in P0
  and emit it under `readiness[]` with measured+threshold, and self-route below-floor to re-queue?"*

### Part 2 -- Static-lint enforcement (`ree-v3/validate_experiments.py`)

Per the parent proposal's own Status note, presence-enforcement belongs in the static script-lint
(`validate_experiments.py`), NOT `validate_queue.py` (queue items carry no `interpretation`). Add a
rule:

- Scan each `experiment_purpose in {diagnostic, baseline}` script's emitted/declared interpretation
  grid. If any grid branch routes to a label in the registered **`SUBSTRATE_VERDICT_LABELS`** set
  (`substrate_ceiling`, `substrate_conditional`, `does_not_support`, and `*_nondiscriminative` /
  `*_unmeetable` suffix patterns) AND the script does not emit a `readiness[]` entry, emit a
  **WARN** (then ERROR after the field stabilises -- the `epistemic_category` warn-then-error
  precedent).
- Also require, for that label class, that at least one criterion carries `load_bearing: true`
  (feeds Part 3b).

This closes the silent-`unverified` gap for **exactly** the high-stakes label class, without firing
on the hundreds of benign landing/smoke diagnostics.

### Part 3 -- Indexer auto-detector (`build_experiment_indexes.py`, extend `_compute_adjudication`)

Two author-free signals, added ahead of the existing author-trusted checks:

**3a -- Readiness recompute (defends against a wrong/missing `met`).** For each `readiness[]` entry
with numeric `measured`+`threshold`, recompute `met := measured >= threshold`. If any recomputes
false -> `precondition_unmet` (regardless of the author's boolean). This is the direct 642/264/620
catch: a below-floor magnitude is detected from the *numbers*, not the author's say-so.

**3b -- Aggregation-vacuity (the 621a pattern).** If `overall_pass == true` (or `outcome == PASS`)
while any criterion tagged `load_bearing: true` is false -> `vacuous_pass`. This catches a PASS
carried by structural/partial criteria while the substantive gate failed. Gated on the explicit
`load_bearing` tag (Part 2 requires it for the verdict class) so it never over-fires on legitimate
M-of-N passes.

```python
# inside _compute_adjudication, before the existing preconditions/crit checks:
readiness = interp.get("readiness")
for r in (readiness if isinstance(readiness, list) else []):
    m, t = r.get("measured"), r.get("threshold")
    if isinstance(m, (int, float)) and isinstance(t, (int, float)) and m < t:
        return label, "precondition_unmet"          # 3a -- below-floor by the numbers
# 3b -- aggregation vacuity (621a): PASS while a load-bearing criterion is false
if str(status).upper() == "PASS":
    for c in interp.get("criteria", []) if isinstance(interp.get("criteria"), list) else []:
        if c.get("load_bearing") is True and c.get("passed") is False:
            return label, "vacuous_pass"
```

Both compose with the landed author-trusted checks (which remain as the fallback for diagnostics that
declare `met`/`criteria_non_degenerate` directly but expose no numeric `measured`).

### (Optional) Part 4 -- One-time retrospective sweep

A standalone, **non-blocking** best-effort script that scans the legacy diagnostic record for the
signature where it is machine-discoverable (a numeric magnitude/variance field at or near zero on a
run that self-routed to a verdict label) and lists candidates for `/failure-autopsy`. The audit found
642/264/620 by hand; this would surface any others the manual pass missed. Heuristic only -- it
WARNs, it does not edit the record.

---

## 4. Worked examples under the new machinery

| Run | Today | With this proposal |
|---|---|---|
| **642** | author would have had to write `met:false` (didn't; `wf_mse` looked great) | Part 1 emits `readiness:[{pred_mag, measured 0.0, threshold 0.05}]`; Part 3a recomputes `met=false` -> `precondition_unmet` **from the numbers**; Part 2 would have WARNed the original script for routing to `substrate_ceiling` with no readiness entry |
| **264** | clean 3-criterion FAIL -> `does_not_support` on the record | Part 1 emits a forward-model-pred readiness entry; `pred_norm < 0.01` -> `precondition_unmet` -> self-route `substrate_not_ready_requeue`, never `does_not_support` |
| **620** | identically-zero distribution -> "axis (a) unmeetable" -> spawned axis-(b) plan | Part 1 readiness on cross-arm distribution variance == 0 -> `precondition_unmet`; the plan would have been gated pending a non-degenerate re-measure |
| **621a** | `overall_pass=true` cleared a gate while C2 z_goal floor failed | Part 2 requires `load_bearing` tags; Part 3b sees `overall_pass=true` + C2 `load_bearing` false -> `vacuous_pass` -> blocked from clearing the gate |

---

## 5. What this is NOT

- **Not a re-litigation of the landed gate.** It extends `_compute_adjudication` with two checks
  ahead of the existing ones; the author-trusted path stays as the fallback.
- **Not autopsy-everything.** Enforcement (Part 2) fires only for the `SUBSTRATE_VERDICT_LABELS`
  class. Smoke / onboarding / wiring diagnostics are untouched.
- **Not a floor-tuning exercise.** Thresholds live in each experiment's own config (e.g.
  `blocked_agency_predicted_effect_floor`); this proposal standardizes *where the measured value is
  recorded*, not what the floor is.

---

## 6. Rollout (backward-compatible, staged)

1. **Part 3a+3b first (indexer, read-only).** Recompute fires only when `readiness[]`/`load_bearing`
   are present -> zero effect on the legacy record; immediate signal on new diagnostics.
2. **Part 1 (`/queue-experiment` convention)** so new verdict-class diagnostics emit `readiness[]`.
3. **Part 2 (`validate_experiments.py`) as WARN**, then ERROR after a cycle of real post-convention
   diagnostics -- the parent proposal's stated gating condition (a) is now partially met by the
   in-flight 642a.
4. **Part 4 sweep** any time -- independent, non-blocking.

No step changes claim confidence math, lit/exp decoupling, or `ree_core`.

---

## 7. Open questions for sign-off

1. **New `readiness[]` array vs. reuse `preconditions[]`.** Reusing the landed `preconditions[]`
   (require readiness-kind entries to carry `measured`+`threshold`; recompute `met`) avoids a new
   field and needs no `RunRecord` change. A separate `readiness[]` is clearer but is more surface.
   *(I lean reuse `preconditions[]` -- smallest diff, the landed gate already reads `.met`.)*
2. **`SUBSTRATE_VERDICT_LABELS` membership.** Confirm the set:
   `{substrate_ceiling, substrate_conditional, does_not_support}` + suffix patterns
   `*_nondiscriminative`, `*_unmeetable`. Add `non_contributory`? *(I lean NOT -- non_contributory is
   already a "carries no weight" outcome, lower stakes.)*
3. **Enforcement strength of Part 2.** WARN-then-ERROR (epistemic_category precedent) vs WARN-only
   indefinitely. *(I lean warn-then-error, ERROR gated on the parent proposal's stated condition.)*
4. **Part 4 retrospective sweep -- build now or defer?** It is independent and non-blocking; the
   manual audit already covered the high-stakes set. *(I lean defer -- low marginal value now; build
   if a Section-2 autopsy from the audit surfaces a systemic miss.)*

---

## 8. References

- `proposal_diagnostic_adjudication_gate_2026-06-06.md` -- parent; this is its deferred Q2 half.
- `retrospective_diagnostic_selfroute_audit_2026-06-06.md` -- Section 5 cross-cutting finding; the
  642/264/620/621a evidence.
- `failure_autopsy_V3-EXQ-642_2026-06-06.md` -- the 642a P0-readiness-gate prescription this rule
  generalizes.
- Insertion points: `evidence/experiments/scripts/build_experiment_indexes.py:120-157`
  (`_compute_adjudication`); `ree-v3/validate_experiments.py` (new lint rule);
  `.claude/skills/queue-experiment/SKILL.md` + `.agents/` mirror (Step-3.5 checklist).
- Memory: `feedback_diagnostic_self_route_is_hypothesis`, `feedback_diagnostic_experiment_descriptions`,
  `feedback_biology_before_formal_definitions`.
