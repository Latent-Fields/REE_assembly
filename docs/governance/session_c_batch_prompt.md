# Session C Batch Prompt — All Grey-Zone Resolutions

> **Usage:** Hand this file to a fresh session: "Read
> `REE_assembly/docs/governance/session_c_batch_prompt.md` and execute."
> This prompt is self-contained. It replaces running 14 individual
> Session C_n sessions with a single batched pass. The template's
> single-focus discipline is preserved by resolving one entry at a
> time sequentially and committing per entry.

---

## 1. What this session does

Work through all 14 grey-zone invariants identified by Session B:

INV-004, INV-005, INV-006, INV-019, INV-020, INV-021, INV-024,
INV-047, INV-048, INV-051, INV-061, INV-062, INV-063, INV-064

For each entry, apply the Session C_n decision procedure and land one
of the five outcomes (universal | emergent | re-state | retract |
reclassify claim_type). Commit per entry so each decision is
separately reviewable. At the end, verify the audit registry is
coherent and all 14 entries resolved (or explicit narrower grey-zone
follow-ups recorded for any that cannot be decided).

---

## 2. Read these first (once, up front)

1. `REE_assembly/docs/governance/session_c_template.md` — decision
   framework and outcome application rules. **This is the canonical
   procedure**; the batch prompt does not replace it, only drives it.
2. `REE_assembly/docs/architecture/invariant_types.md` — schema.
3. `REE_assembly/docs/governance/invariant_classification_audit.md` —
   Session B's per-entry reasoning and follow-up prompts.
4. `REE_assembly/docs/thoughts/2026-04-17_invariant_types_governance.md`
   — planning doc (for escalation judgment if needed).

Do **not** read all 14 invariant YAML entries at the start — read
each one only when you get to it, to keep judgments clean per the
template's single-focus rule.

---

## 3. Session setup

1. Get UTC timestamp: `date -u +"%Y-%m-%dT%H:%M:%SZ"`.
2. Check `REE_Working/TASK_CLAIMS.json` for active claims on
   `docs/claims/claims.yaml` or
   `docs/governance/invariant_classification_audit.md`. Pause if
   conflict.
3. Add your claim:
   - `session_label: "session-c-batch-<date>-grey-zone-resolution"`
   - `task: "Session C batch: resolve 14 grey-zone invariants"`
   - `resources: ["REE_assembly/docs/claims/claims.yaml", "REE_assembly/docs/governance/invariant_classification_audit.md", "REE_assembly/docs/assets/data/claims.json", "REE_Working/WORKSPACE_STATE.md"]`
   - `status: "active"`

---

## 4. Execution order (grouped by theme)

Resolve in this order. Grouping is for your reading efficiency — the
template's "don't read other grey-zones in the same session" rule
still applies to the *judgment* for each entry. It is fine to process
grouped entries one-after-another when the underlying substrate
question is identical.

### Group 1: clinical/phenomenological predictions (4 entries)

INV-047, INV-048, INV-061, INV-062.

These were flagged by user review (2026-04-17) as predictions that
presume REE models human cognition — candidate for the
**reclassify claim_type** outcome. Start with INV-047. If you conclude
reclassification is correct:

- Check whether `docs/claims/claims.yaml` schema already supports a
  `prediction` or `derived_prediction` `claim_type`. Grep for other
  `claim_type:` values in use.
- If such a type exists, apply the reclassification per template §4
  "Outcome: reclassify claim_type."
- If no such type exists: **halt the batch and surface the schema
  gap to the user.** Do not invent a type. Write the gap report into
  the audit registry's INV-047 entry and stop the batch. Governance
  (you + user) decides the schema before continuing.

If the user (or you) concludes these should stay as invariants after
all, apply the emergent-on-SD-017 / ARC-049 outcomes per template.

Decide INV-047 first; INV-048/061/062 should follow the same decision
since the objection is shared. Commit the four as a single commit if
the decision is uniform.

### Group 2: axiom-aware invariants (3 entries)

INV-004, INV-005, INV-006.

All three are about post-commit responsibility / trace recording and
have empty `depends_on`. Candidate outcomes:
- universal (responsibility is substrate-independent)
- emergent on ARC-013 (residue field) or SD-010 (harm stream)

Read the audit registry entries for each and apply the template. These
are independent judgments — commit separately unless they genuinely
decide identically.

### Group 3: agency / commitment invariants (3 entries)

INV-019, INV-020, INV-021.

All three concern agency, counterfactual attribution, or commitment.
Candidate substrates: SD-003 (self-attribution via counterfactual E2),
ARC-016 (commitment boundary), SD-005 (z_self/z_world split). Read
each audit registry entry; these are likely all emergent but on
different substrate combinations. Commit separately.

### Group 4: single-entry judgments (4 entries)

INV-024, INV-051, INV-063, INV-064.

Read each audit registry entry and apply the template. These are
not thematically grouped; each is its own judgment. Commit
separately.

---

## 5. Per-entry workflow

For each grey-zone entry:

1. **Re-read**: the invariant's section in the audit registry; its
   YAML entry; any `location` or `source` doc listed.
2. **Decide**: work through template §3 Q1–Q5.
3. **Apply**: edit claims.yaml per template §4. Edit the audit
   registry per template §5 (move entry to the correct bucket,
   update Summary counts).
4. **Validate**:
   ```
   /opt/local/bin/python3 scripts/validate_claims.py
   /opt/local/bin/python3 scripts/validate_claims.py --audit
   ```
   Bucket counts must match what the audit registry Summary says.
5. **Rebuild**: `/opt/local/bin/python3 scripts/build_claims_json.py`.
6. **Commit and push**:
   ```
   git add docs/claims/claims.yaml \
           docs/assets/data/claims.json \
           docs/governance/invariant_classification_audit.md
   git commit -m "Session C_n: resolve INV-XXX (<outcome>)"
   git push origin HEAD:master
   ```
   One commit per entry (or per uniform-decision group). Do not batch
   all 14 into one commit — per-entry commits make each decision
   independently reviewable and revertible.

If an entry cannot be decided confidently: apply the **narrower
grey-zone** outcome per template §4, update the audit registry with
a sharper follow-up question, and move on. Do not force a
classification.

---

## 6. Halt conditions

Stop the batch and surface to user if:

- **Schema gap** (Group 1 clinical entries): no prediction claim_type
  exists in the schema. Governance decision needed before proceeding.
- **Validator strict-mode error** on any entry (shouldn't occur since
  strict mode isn't enabled yet, but any validator error below WARN
  halts).
- **Substrate assertion wrong**: you find that a substrate listed in
  `emergent_from` for Session B's classification does not actually
  underwrite the invariant's subject. Update the entry (move back to
  grey zone with a sharper question) and note in commit.
- **~4 consecutive entries forced into "narrower grey-zone"**: suggests
  the template needs revision, not more sessions. Halt and report.

Do **not** halt for routine ambiguity — that's what the narrower
grey-zone outcome is for.

---

## 7. Completion

After all 14 are resolved (or explicitly deferred via narrower
grey-zone):

1. Verify audit registry Summary counts:
   - Grey Zone count should be 0 (or equal to the number of
     deliberately-deferred narrower grey-zone entries).
   - Universal + Emergent + Retracted + Reclassified counts should
     sum to 72 (universal + emergent + reclassified + retracted =
     72 - residual_grey_zone).
2. Run `validate_claims.py --audit` one final time; confirm counts
   match the registry.
3. Run `bash scripts/governance.sh` to confirm the pipeline still
   runs cleanly end-to-end.
4. Update `REE_Working/WORKSPACE_STATE.md` with a single Recent Work
   entry summarizing the batch — list outcomes per entry as a bullet
   summary, not full reasoning (reasoning lives in the audit
   registry).
5. Mark your TASK_CLAIMS.json entry `status: "done"`.
6. Final summary to user: counts, any halts, any residual grey zones
   with rationale.

---

## 8. Out of scope for this batch

- Session D tasks (validator strict mode, substrate-change reporting).
  That is a separate session after this batch lands.
- Modifying substrate (SD/ARC) entries. If a decision reveals a
  substrate needs re-scoping, note it in the commit message and move
  on.
- Revisiting Session B's universal or emergent classifications.
  Only the 14 grey zones are in scope.
- Adding new invariants, new substrates, or new MECHs.

---

## 9. Key principle

The batched format is a scheduling convenience, not a license to
rush. Each of the 14 decisions is still a single-focus judgment
governed by `session_c_template.md`. The batch succeeds if each entry
gets the same quality of decision a dedicated Session C_n would have
produced. If that requires pausing the batch to think, pause the
batch.

The registry is more valuable with 10 well-resolved entries + 4
honest narrower grey-zones than with 14 forced classifications.
