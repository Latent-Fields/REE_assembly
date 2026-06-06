# Proposal: Diagnostic Adjudication Gate -- verify the self-route before it drives governance

- **Status:** ACCEPTED + IMPLEMENTED 2026-06-06. User signed off the design and all four open questions (Section 7) on the recommended path: (Q1) keep `/failure-autopsy`, add `/diagnostic-autopsy` alias; (Q2) checklist-first enforcement (harden to `validate_queue.py` later); (Q3) gate all three actions incl. thought-intake; (Q4) cover `diagnostic` + `baseline`. Implemented in session `implement-diagnostic-adjudication-gate-20260606T0828Z`. **Implementation note (discovered during build):** the indexer reads the *sync-normalized* `runs/**/manifest.json`, not the flat script manifest, so `interpretation` had to be carried through `sync_v3_results.py` (a 5th edit beyond the 4 parts below); governance.sh Step 2 DOES run that sync (its "no sync needed" comment is stale). Parts B+C+sync are read-only/backward-compatible and landed in code; Parts A+D landed in the three skills (both `.claude` + `.agents`). The validator-hardening (Q2 step 2) and the optional governance.sh hard-block remain future work.
- **Author session:** proposal-diagnostic-adjudication-gate-20260606T0825Z
- **Generated (UTC):** 2026-06-06T08:24:58Z
- **Motivating run:** V3-EXQ-642 (`failure_autopsy_V3-EXQ-642_2026-06-06.{md,json}`)
- **Scope:** governance machinery only. No `ree_core` change. Three skill edits + one manifest convention + two pipeline-script edits, all backward-compatible.

---

## 1. The gap (one paragraph)

A diagnostic experiment (`experiment_purpose: diagnostic`, `claim_ids: []`) writes a
self-routed `interpretation.label` computed by a grid the author pre-registered **at queue
time, before the run**. That label is a **hypothesis about what the run means, not a
verdict.** It can be wrong in two structural ways, and **both appeared in the single
V3-EXQ-642 manifest**:

1. **Unmet precondition.** A grid branch silently assumes a condition the run did not
   satisfy. 642's branch "C0 fail -> `substrate_ceiling`" assumed a *trained* substrate; P0
   trained `world_forward` on a frozen random encoder with SD-056 OFF, so `pred_mag` stayed
   below the `0.05` floor and the comparator was floored to 0 by construction. The self-route
   labelled an **untrained-substrate test-design artifact** as a substrate ceiling. Only a
   manual `/failure-autopsy` caught it; an unquestioning governance walk would have minted an
   unnecessary substrate-enrichment task and parked MECH-353 `v3_pending` on a wrong cause.
2. **Vacuous PASS.** A criterion passes for a degenerate reason. 642's C3 passed 2/3 seeds
   only because `z_block` was identically 0, making both arms bit-identical -> "no withdrawal
   / no suffering" trivially true. Generalize this: a diagnostic whose *overall* PASS rests on
   vacuous criteria would **clear a `v3_pending` gate on nothing** -- the higher-stakes
   direction, because clearing a gate flips a claim from held to promotable.

**Adjudication depth is asymmetric.** FAIL has a deep dedicated skill (`/failure-autopsy`);
crash has `/diagnose-errors`; PASS-clears-gate has only the lightweight `/governance` walk,
which pauses (governance SKILL lines 156/169) but is **not structured** to check precondition
satisfaction or non-vacuity. And the grid is **prose in the docstring** -- nothing in the
pipeline asserts "this PASS's gating criterion fired non-vacuously" or "this FAIL's routed
branch had its precondition satisfied."

---

## 2. What already exists (do not rebuild)

| Path | Covers | Gap |
|---|---|---|
| `/failure-autopsy` | deep adjudication of FAIL diagnostics | FAIL-only by guard ("FAIL only ... ERROR -> /diagnose-errors"); no PASS path |
| `/diagnose-errors` | crash / ERROR / UNKNOWN / no-output | not for ran-to-completion diagnostics |
| `/governance` diagnostic step | surfaces PASS + FAIL diagnostics (unlinked runs), pauses for user, evidence-vs-diagnostic classification | unstructured re: preconditions + vacuity; framed around smoke/onboard PASS |
| `feedback_diagnostic_experiment_descriptions` | requires an interpretation grid (one row per outcome) in every diagnostic docstring | the grid is not machine-checked; branches may carry unstated preconditions |
| indexer `unlinked_runs` (`build_experiment_indexes.py:1314-1324`) | records claimless runs with `status` | carries no interpretation label, no precondition/vacuity signal |
| `generate_pending_review.load_pending_entries` | flags unreviewed PASS/FAIL incl. unlinked | no "PASS via unmet precondition / vacuous criterion" flag |

The interpretation-grid *requirement* already exists. What is missing is **verification of
the grid's own assumptions**, and a place to record that the verification happened.

---

## 3. Design principle (what this is and is NOT)

- **The self-route is a claim to be verified, not accepted.** The fix records, per diagnostic,
  whether (a) the self-route's preconditions were met and (b) the gating criteria fired
  non-degenerately -- BEFORE the diagnostic drives a governance action.
- **A governance action means:** clear/keep a `v3_pending` gate, mint or AMEND a
  `substrate_queue` entry, or close/route a thought-intake. A diagnostic that drives none of
  these (pure context) needs no gate.
- **NOT "autopsy everything."** Proportionate + stakes-scaled. A clean PASS with met
  preconditions and non-vacuous criteria clears at the governance walk in one line. Deep
  adjudication (the `/failure-autopsy` move, now applicable to PASS too) is reserved for the
  cases the automated flag cannot clear.
- **Backward-compatible.** Every new manifest field is optional; absence == "not asserted"
  (legacy diagnostics are surfaced as `adjudication: unverified`, not blocked).

---

## 4. The machinery (four parts, exact insertion points)

### Part A -- Manifest convention (authored in `/queue-experiment`)

Every `experiment_purpose: diagnostic` (and `baseline`) script SHOULD emit, alongside the
existing `interpretation` block, two machine-checkable structures:

```jsonc
"interpretation": {
  "label": "substrate_ceiling_comparator_nondiscriminative",
  "preconditions": [
    {
      "name": "world_forward_trained_supra_floor",
      "description": "pred_mag on a known successful move clears predicted_effect_floor",
      "measured": 0.013,
      "threshold": 0.05,
      "met": false                       // <-- the load-bearing field
    }
  ],
  "criteria_non_degenerate": {
    "C0": true, "C1": true, "C2": true,
    "C3": false                          // passed only because both arms were bit-identical
  }
}
```

- **`preconditions[]`** -- each branch of the grid that has an unstated assumption names it
  here, with the measured value, threshold, and `met`. A self-route to a branch whose
  precondition is `met: false` is **not trustworthy** and must escalate.
- **`criteria_non_degenerate{}`** -- per pre-registered criterion, did it discriminate, or
  did it pass/fail for a trivial reason (e.g. both arms identical, zero variance, n<min
  samples)? The script author writes the degeneracy test (it is usually one line: "arms
  differed" / "signal had non-zero variance" / "n_events >= floor").

The `/queue-experiment` **Step 3.5 code-review checklist** (skill SKILL.md ~line 220) gains
two questions:
- *Does each interpretation-grid branch with an unstated assumption name it in
  `preconditions[]` with a measurable `met` test?*
- *Does each PASS criterion have a `criteria_non_degenerate` test that would be `false` if it
  passed vacuously (arms identical / zero variance / sub-threshold n)?*

### Part B -- Indexer auto-flag (`build_experiment_indexes.py`)

At the `unlinked_runs` append site (`:1314-1324`), carry the new fields and derive a flag:

```python
matrix["unlinked_runs"].append({
    "source_type": "experimental",
    "experiment_type": run.experiment_type,
    "run_id": run.run_id,
    "timestamp_utc": run.timestamp_raw,
    "status": run.final_status,
    "interpretation_label": run.interpretation_label,          # NEW
    "adjudication": _adjudication_flag(run),                   # NEW
})
```

`_adjudication_flag(run)` returns one of:
- `"verified"` -- all `preconditions[].met` true AND every PASS criterion
  `criteria_non_degenerate` true;
- `"precondition_unmet"` -- any precondition `met: false`;
- `"vacuous_pass"` -- overall PASS but a load-bearing criterion is degenerate;
- `"unverified"` -- legacy manifest with neither structure present (backward-compat default).

(Claim-tagged diagnostics are rare, but the same flag can be attached to their entry too.)

### Part C -- pending_review surfacing (`generate_pending_review.py`)

`load_pending_entries` (`:106-133`) already lists unlinked PASS/FAIL. Add an
`adjudication != "verified"` column and a dedicated section header so the governance walk
sees, e.g.:

```
## Diagnostic adjudication required (self-route unverified)
| Run ID | label | adjudication |
| v3_exq_642_..._v3 | substrate_ceiling_comparator_nondiscriminative | precondition_unmet |
```

A `"verified"` diagnostic still appears for review but needs only a one-line clear; a
`precondition_unmet` / `vacuous_pass` one must be adjudicated before its self-route drives an
action.

### Part D -- Governance gate + `/failure-autopsy` generalization

- **`/governance` (SKILL ~lines 117-135, 460-467):** the diagnostic-handling step gains a
  **symmetric pre-action checklist**. Before a diagnostic clears/keeps a `v3_pending`, mints
  or AMENDs a `substrate_queue` entry, or closes/routes a thought-intake, governance must
  confirm: (i) `adjudication == "verified"`, OR (ii) a `/failure-autopsy` adjudication
  artifact exists for that run. A `precondition_unmet` / `vacuous_pass` diagnostic **cannot**
  drive the action until adjudicated.
- **`/failure-autopsy`:** relax the FAIL-only guard ("Confirm the target is a FAIL")
  to **"ran to completion"** so a flagged **PASS-clears-gate** target can be deep-adjudicated
  by the same skill (crashes still route to `/diagnose-errors`). The four-layer table and the
  biology triage apply unchanged; the new question for a PASS target is "did the gate clear
  for a real reason, or a vacuous one?" Rename the concept in the doc to *diagnostic
  adjudication* (FAIL + flagged-PASS); the file/skill name can stay `failure-autopsy` to avoid
  churn, or alias.

---

## 5. Worked example -- V3-EXQ-642 under the new machinery

| Stage | Today | With the gate |
|---|---|---|
| Manifest | `label: substrate_ceiling...` only | + `preconditions:[{world_forward_trained_supra_floor, measured 0.0, threshold 0.05, met:false}]`, `criteria_non_degenerate:{C3:false}` |
| Indexer | unlinked run, `status:FAIL` | `adjudication: "precondition_unmet"` |
| pending_review | "1 FAIL (no claim tags)" | listed under **Diagnostic adjudication required** with `precondition_unmet` |
| Governance | could trust `substrate_ceiling` -> mint enrichment task | **blocked** from minting until adjudicated; routes to `/failure-autopsy` |
| Outcome | needed a human to notice | the pipeline names the exact reason the self-route is untrustworthy |

The C3 vacuity (`criteria_non_degenerate.C3 = false`) is the PASS-side proof-of-concept of the
same mechanism on the higher-stakes direction.

---

## 6. Rollout (backward-compatible, staged)

1. **Land Parts B+C first (read-only flags).** Legacy manifests -> `adjudication: "unverified"`;
   nothing is blocked. The pipeline starts *surfacing* the distinction immediately.
2. **Land Part A in `/queue-experiment`** so new diagnostics emit `preconditions[]` +
   `criteria_non_degenerate`. Existing diagnostics are unaffected.
3. **Land Part D (governance gate + autopsy generalization) last**, once a cycle's worth of
   diagnostics carry the new fields, so the gate has real signal to act on. Until then the
   gate treats `"unverified"` as "user decides at the walk" (status quo).
4. Optional later hardening: elevate `precondition_unmet` on a `v3_pending`-clearing PASS from
   warn to a hard block in `governance.sh`.

No step changes claim confidence math, the lit/exp decoupling, or any `ree_core` behaviour.

---

## 7. Open questions for sign-off

1. **Naming:** keep `/failure-autopsy` (aliased) or rename to `/diagnostic-autopsy`? (I lean
   keep + alias -- less churn, the file is heavily cross-referenced.)
2. **Enforcement strength of Part A:** code-review *checklist question* (author judgement) vs
   a `validate_queue.py` hard requirement that diagnostic manifests declare `preconditions`.
   (I lean checklist first; harden to validator after the field stabilises -- mirrors the
   `epistemic_category` warn-then-error precedent.)
3. **Scope of "drives a governance action":** is closing/routing a thought-intake in scope, or
   only `v3_pending` + `substrate_queue`? (I lean all three -- a vacuous diagnostic closing an
   intake is the same failure mode.)
4. **baseline experiments:** apply the same machinery to `experiment_purpose: baseline`
   (oracle/random-walk) or diagnostics only? (I lean both -- a baseline can also be vacuous.)

---

## 8. References

- `failure_autopsy_V3-EXQ-642_2026-06-06.{md,json}` -- the motivating adjudication (both
  failure modes in one run).
- `feedback_diagnostic_self_route_is_hypothesis` (memory) -- the principle.
- `feedback_diagnostic_experiment_descriptions`, `feedback_governance_interactive`,
  `feedback_nonstandard_directions`, `feedback_illusory_conflict_resolution` (memory) --
  related governance feedback.
- Insertion points: `evidence/experiments/scripts/build_experiment_indexes.py:1314-1333`;
  `scripts/generate_pending_review.py:106-133`; `.claude/skills/queue-experiment/SKILL.md`
  (~159-172 purpose/manifest, ~220 code-review); `.claude/skills/governance/SKILL.md`
  (~117-135, ~460-467); `.claude/skills/failure-autopsy/SKILL.md` ("Before starting" FAIL-only
  guard).
