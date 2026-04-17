# Session D Prompt — Invariant-Types Pipeline Completion

> **Usage:** Hand this file to a fresh session (e.g. "Read
> `REE_assembly/docs/governance/session_d_prompt.md` and execute
> Session D.") once Sessions A, B, and all C_n have completed. The
> prompt is self-contained — you do not need prior conversation
> context.

---

## 1. What Session D Is

Session D is the **final session** of the invariant-types governance
cycle. It flips the validator to strict mode and wires the
substrate-change signal into the governance pipeline. By the end of
this session, the registry enforces the `invariant_type` schema at
every entry point and surfaces dependent-invariant flags on every
governance run.

Prerequisites (check before starting):
- Session A committed (schema, validator, architecture doc, INV-012).
- Session B committed (audit registry + classifications applied).
- All Session C_n committed — i.e. the audit registry's grey-zone
  count is either 0 or the user has explicitly authorized flipping
  strict mode with residual grey zones.

Session D does **not** classify any invariants (that's C_n), does
**not** resolve grey zones, does **not** modify substrate claims.

---

## 2. Read These First

1. `REE_assembly/docs/architecture/invariant_types.md` — schema and
   governance rules, especially §"Governance Cycle".
2. `REE_assembly/docs/thoughts/2026-04-17_invariant_types_governance.md`
   — planning doc, especially §5 (pipeline changes) and §8
   (execution order: Session D is the last entry).
3. `REE_assembly/docs/governance/invariant_classification_audit.md` —
   verify the grey-zone count. If non-zero, confirm user authorization
   before proceeding.
4. `REE_assembly/scripts/validate_claims.py` — current warn-only
   implementation.
5. `REE_assembly/scripts/generate_pending_review.py` — current
   implementation. You will add a new section without disturbing the
   existing logic.
6. `REE_assembly/scripts/governance.sh` — pipeline entry point.
7. One recent run of `evidence/experiments/promotion_demotion_recommendations.md`
   to understand the output format you will be extending.

---

## 3. Tasks

### Task 1. Flip validator to strict in governance.sh

Edit `scripts/governance.sh` so that the validator runs in strict mode
as a gate before any other step. Target location: the very top of the
pipeline, before index builds, so a malformed registry blocks the
whole run.

Required behaviour:
- `validate_claims.py --strict` is invoked.
- Non-zero exit halts the pipeline with a clear error.
- The existing warn-only invocation inside `build_claims_json.py`
  remains (defence in depth — the gate also fires on site rebuilds
  that bypass governance.sh).

If `governance.sh` does not already call `validate_claims.py`, add the
invocation. Do not restructure other parts of the script.

### Task 2. Add substrate-change section to generate_pending_review.py

Extend `scripts/generate_pending_review.py` so that when it builds
`promotion_demotion_recommendations.md`, it emits a new section titled
**"Substrate changes with dependent invariants"**. Behaviour:

- For every substrate (claim_type `design_decision`,
  `architectural_commitment`, or `architecture_hypothesis`) whose
  status changed since the prior governance run, list the emergent
  invariants that reference it in `emergent_from`.
- Per invariant, show: current `status`, `pending_substrate_reconfirmation`
  flag state, one-line governance prompt ("re-confirm", "transfer to
  successor", "re-derive", or "retract").
- If no substrate status changed this run, emit the section header
  with body "No substrate status changes this run. No dependent
  invariants flagged."

Implementation guidance:
- Source of truth for substrate status: `docs/claims/claims.yaml`.
- Source of truth for prior run: whatever artifact
  `generate_pending_review.py` already uses for change detection (read
  the script to find it). If no such artifact exists, emit the full
  list of current substrate → dependent-invariants on every run, and
  leave change detection as a TODO with a clear comment.
- Do not modify how invariants themselves are promoted/demoted — this
  is a reporting section only, not a decision pipeline.

### Task 3. Wire pending_substrate_reconfirmation into validator

Currently the validator does not check whether
`pending_substrate_reconfirmation` is consistent with substrate status.
Add a warning-level rule (not error-level):

- If an invariant has `pending_substrate_reconfirmation: true` but all
  substrates in `emergent_from` are currently `active`, emit WARN:
  "invariant INV-XXX flag is stale — all substrates now active, flag
  can be cleared."
- If an invariant has `pending_substrate_reconfirmation: false` (or
  field absent) but at least one substrate in `emergent_from` is below
  `active`, emit WARN: "invariant INV-XXX should be flagged — substrate
  SD-YYY is <status>."

These are warnings, not errors, because the flag can legitimately be
cleared or applied by explicit governance decision (e.g., an invariant
a human confirmed on a candidate substrate may not need a flag).
Warnings surface the drift; governance decides.

### Task 4. Verify the full pipeline runs cleanly

From `REE_assembly/` root:
```
bash scripts/governance.sh
```

Expected:
- Validator runs strict and passes.
- Experiment indexes rebuild.
- `pending_review.md` regenerates.
- `promotion_demotion_recommendations.md` regenerates with the new
  "Substrate changes with dependent invariants" section.
- `claims.json` rebuilds via `build_claims_json.py`.

If the validator fails strict, do **not** silently downgrade to
warn-only. Investigate — some invariant is mis-classified or has a
field error. Fix it in claims.yaml or, if the fix is non-trivial,
report the error to the user and stop.

### Task 5. Update docs

- `REE_assembly/CLAUDE.md`: update the "Invariant Types" subsection —
  remove the "currently warn-only" wording, note that the validator
  is now strict.
- `REE_assembly/docs/architecture/invariant_types.md`: add a "Pipeline
  Status" footnote near the end noting that Session D completed on
  `<date>` and the validator is now strict.
- `REE_Working/CLAUDE.md`: no changes needed if the pointer added in
  Session A still reads correctly.

### Task 6. Cleanup check

- Verify the audit registry is coherent — the Summary counts match
  the entries.
- Verify no `grey_zone` entries remain (or that the user has
  authorized proceeding with residuals).
- Verify every claim entry with `claim_type: invariant` has
  `invariant_type` set (strict validator would have caught this, but
  confirm explicitly).

---

## 4. Out of Scope

- Do not resolve residual grey-zone entries. If any remain, that's
  Session C_n.
- Do not modify the classification of any invariant.
- Do not change the schema of `invariant_type`, `emergent_from`, or
  `pending_substrate_reconfirmation`. The schema is set.
- Do not add new governance stages, decision rules, or status values.
- Do not touch experiment files or substrate claims.

---

## 5. Session Setup Checklist

1. Get UTC timestamp: `date -u +"%Y-%m-%dT%H:%M:%SZ"`.
2. Check `REE_Working/TASK_CLAIMS.json` for conflicts on `governance.sh`,
   `generate_pending_review.py`, `validate_claims.py`. Pause if any
   are actively claimed by another session.
3. Add your own claim:
   - `session_label: "session-d-<date>-invariant-pipeline"`
   - `task: "Session D: flip validator to strict, add substrate-change section, wire pending flag check"`
   - `resources: ["REE_assembly/scripts/governance.sh", "REE_assembly/scripts/generate_pending_review.py", "REE_assembly/scripts/validate_claims.py", "REE_assembly/CLAUDE.md", "REE_assembly/docs/architecture/invariant_types.md", "REE_Working/WORKSPACE_STATE.md"]`
   - `status: "active"`.
4. Run `validate_claims.py --audit` and record the counts — these
   should match the audit registry Summary.

---

## 6. Commit Protocol

Single commit, or split into two if the generate_pending_review.py
change is large:

```
git add scripts/governance.sh \
        scripts/generate_pending_review.py \
        scripts/validate_claims.py \
        CLAUDE.md \
        docs/architecture/invariant_types.md
git commit -m "Session D: invariant-types pipeline strict + substrate-change reporting"
git push origin HEAD:master
```

Then in `REE_Working/`:
- Add Recent Work entry to `WORKSPACE_STATE.md`.
- Mark TASK_CLAIMS.json entry done.
- Commit locally (no remote).

Optional (if natural): update `MEMORY.md` to reflect that the cycle
is now fully active — one line under the existing
`feedback_invariant_types.md` pointer noting Session D completion.

---

## 7. Success Criteria

- `bash scripts/governance.sh` runs cleanly on a fresh checkout.
- Every invariant in claims.yaml has `invariant_type` set.
- `promotion_demotion_recommendations.md` contains the new section
  (populated or empty-but-present).
- The validator strict gate is in place; future malformed invariants
  block governance runs.
- The flag-drift warnings surface mismatches between
  `pending_substrate_reconfirmation` and substrate status.
- No grey zones remain (or user explicitly authorized residuals).

---

## 8. Final Notes

- Session D is intentionally small. If you find yourself doing more
  than ~200 lines of code changes across the three scripts, step back
  and ask whether you are expanding scope.
- The substrate-change section is a reporting feature, not a decision
  rule. Governance decides what to do with a flagged invariant; the
  pipeline only surfaces the flag.
- The flag-drift warnings are informational. Do not auto-clear or
  auto-set `pending_substrate_reconfirmation` based on substrate
  status. The flag is a governance artifact, not a derived value.
