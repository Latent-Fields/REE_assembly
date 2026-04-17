# Session C_n Template — Grey-Zone Invariant Resolution

> **Usage:** This is the shared framework for per-invariant grey-zone
> resolution sessions (one C_n per grey-zone entry identified by
> Session B). Individual C_n prompts live in the follow-up-prompt
> section of `docs/governance/invariant_classification_audit.md` and
> should reference this template by pointing at it. Each C_n prompt
> supplies the specific invariant context; this template supplies the
> framework every C_n session must follow.

---

## 1. What a Session C_n Is

Each Session C_n resolves **exactly one** grey-zone invariant flagged
by Session B. The session produces a governance decision:

- **universal** — the invariant is substrate-independent after all.
  Either the original wording was fine, or a minor re-statement shows
  it is.
- **emergent on [SD-.., ARC-..]** — the invariant genuinely depends on
  specific substrates.
- **re-state** — the invariant should be re-worded to make a universal
  reading work. Commit the re-wording and classify as universal.
- **retract** — the invariant is ill-formed regardless of substrate
  and should be withdrawn. Status moves to `retracted`, `invariant_type`
  stays `grey_zone` with a retraction note.

Only one of these outcomes lands per session. If the session cannot
reach a clear outcome after genuine effort, the correct result is a
narrower grey-zone entry with a sharper follow-up question — not a
forced classification.

---

## 2. Read These First

1. This template (you are here).
2. `REE_assembly/docs/architecture/invariant_types.md` — schema and
   classification criteria.
3. The relevant section of
   `REE_assembly/docs/governance/invariant_classification_audit.md` —
   Session B's reasoning about this specific invariant, including the
   candidate classifications and the follow-up question.
4. The invariant's current YAML entry in
   `REE_assembly/docs/claims/claims.yaml` (search for the INV- ID).
5. Any reference doc listed in the invariant's `location` or `source`
   fields — often `docs/invariants.md` or `docs/processed/...`. Read
   the surrounding context to understand what the invariant was meant
   to capture when it was written.
6. If the invariant's candidate emergent substrates are listed, read
   the relevant SD/ARC entries and any `docs/architecture/*.md` doc
   that defines them.

Do **not** read other grey-zone invariants in the same session. Each
C_n is deliberately single-focus to keep judgment clean.

---

## 3. Decision Procedure

Work through these questions in order:

### Q1. Subject test
If the claim's subject (what it is *about*) references REE-specific
machinery (z_goal, z_world, z_harm, residue field, commitment boundary,
hypothesis tag, stored/active distinction, etc.), ask: could the
subject be re-stated in substrate-neutral terms without loss of
meaning?

- Yes, re-statable cleanly → likely **universal** (with possible
  re-wording).
- No, the machinery is load-bearing → likely **emergent**.
- Not sure the subject has meaning at all under alternative substrates
  → likely **emergent** or **retract**.

### Q2. Retract-and-check
Imagine retracting the candidate substrate(s) one by one. For each:

- Does the invariant become *falsified* (evidence says it's wrong) →
  this is an evidence question, not a type question. The invariant
  stays well-formed; classify based on whether other substrates
  underwrite its subject.
- Does the invariant become *unevidenced* → this is also an evidence
  question. Same answer.
- Does the invariant become *ill-formed* (the subject loses coherence)
  → the substrate is genuinely underwriting the claim. **emergent_from**
  should list that substrate.

A common error: treating "unevidenced" as "ill-formed." Evidence
questions are about whether the claim is true; type questions are
about whether the claim's subject exists. Keep these separate.

### Q3. Substrate plurality
If the invariant's subject is underwritten by two or more substrates
(e.g., commitment requires both a commitment boundary and a
prospective attention channel), list all of them in `emergent_from`.
An emergent invariant with multiple underwriters is normal.

### Q4. Universal-but-REE-flavored
If the invariant is universal in principle but currently worded in
REE-specific vocabulary, choose:
- **re-state** — rewrite the title/body in substrate-neutral terms,
  commit the rewrite, classify as universal.
- **classify emergent** — accept the REE-specific wording as the canonical
  form, point at the substrate(s). Usually the right call if the
  REE-specific terms have become load-bearing for the project's
  reasoning, even if a universal version exists in principle.

Prefer re-statement when the universal form is genuinely cleaner and
doesn't lose precision. Prefer emergent when the REE-specific wording
is doing real work.

### Q5. Cannot decide
If after all of the above you still cannot classify confidently, the
correct outcome is a **narrower grey-zone entry** with a sharper
follow-up question. Write the narrower question, update the audit
registry, and stop. This is not a failure — it is honest reporting.

Do **not** coin-flip between universal and emergent to "make progress."

---

## 4. Applying the Decision

### Outcome: universal (no re-wording)

In claims.yaml, for the target invariant:
- Replace `invariant_type: grey_zone` with `invariant_type: universal`.
- Remove `candidate_emergent_from` if present.
- Update `notes` with: "Resolved universal in Session C_n
  <YYYY-MM-DD>. Rationale: <one sentence>."

### Outcome: universal (with re-wording)

- Edit `title` (and any relevant body text) to the substrate-neutral
  form. Keep the ID.
- Replace `invariant_type: grey_zone` with `invariant_type: universal`.
- Update `notes` with: "Re-stated and resolved universal in Session
  C_n <YYYY-MM-DD>. Prior wording: '<old title>'. Rationale: <one
  sentence>."
- If the re-wording changes the reference doc, also edit
  `docs/invariants.md` (or whatever is listed in `location`).

### Outcome: emergent

- Replace `invariant_type: grey_zone` with `invariant_type: emergent`.
- Add `emergent_from: [SD-.., ARC-..]`. Every ID in `emergent_from`
  must also appear in `depends_on` — if missing, add it to
  `depends_on` too.
- If any substrate in `emergent_from` is below `active` status, add
  `pending_substrate_reconfirmation: true`.
- Remove `candidate_emergent_from` if present.
- Update `notes` with: "Resolved emergent in Session C_n <YYYY-MM-DD>.
  Rationale: <one sentence>."

### Outcome: retract

- Leave `invariant_type: grey_zone` in place (so it shows up in future
  audits as "was grey, now retracted").
- Change `status` to `retracted`.
- Update `notes` with: "Retracted in Session C_n <YYYY-MM-DD>.
  Rationale: <two sentences — what was ill-formed and why no substrate
  choice fixes it>."

### Outcome: narrower grey-zone (cannot decide)

- Leave `invariant_type: grey_zone` in place.
- Update `candidate_emergent_from` if the narrower question changed it.
- Update the entry's note in the audit registry with the sharper
  follow-up question for Session C_n+1.

---

## 5. Update the Audit Registry

In `docs/governance/invariant_classification_audit.md`:

- Move the resolved invariant out of the "Grey Zone" section into
  "Clear Universal" or "Clear Emergent" as appropriate (retractions
  get a new "Retracted" section at the bottom).
- Replace its section body with:
  - **Resolved:** <YYYY-MM-DD> in Session C_n
  - **Outcome:** universal | emergent on [SD-..] | re-stated universal | retracted
  - **Rationale:** <one-to-two-sentence summary>
- Decrement the Grey Zone count in the Summary.
- Increment the appropriate bucket count in the Summary.

If the outcome was "narrower grey-zone," leave the entry in place but
update its follow-up question.

---

## 6. Validation and Commit

1. `/opt/local/bin/python3 scripts/validate_claims.py` — confirm 0
   errors (or that any remaining errors are pre-existing and unrelated
   to the entry you just edited).
2. `/opt/local/bin/python3 scripts/build_claims_json.py` — rebuild.
3. Spot-check the target entry in `docs/assets/data/claims.json`.

Commit:
```
git add docs/claims/claims.yaml \
        docs/assets/data/claims.json \
        docs/governance/invariant_classification_audit.md
# plus docs/invariants.md if re-worded
git commit -m "Session C_n: resolve INV-XXX (<outcome>)"
git push origin HEAD:master
```

In `REE_Working/`: add a brief Recent Work entry to `WORKSPACE_STATE.md`
and mark your TASK_CLAIMS.json entry `status: "done"`.

---

## 7. Scope Discipline

A Session C_n touches:
- one invariant entry in claims.yaml,
- that invariant's section in the audit registry,
- claims.json (rebuilt),
- possibly docs/invariants.md (only if the invariant was re-worded),
- WORKSPACE_STATE.md and TASK_CLAIMS.json.

It does **not** touch:
- other invariants,
- substrate claims (SD/ARC),
- other docs,
- the validator script,
- `generate_pending_review.py`,
- any experiment files.

If while resolving one grey-zone entry you notice that another grey-zone
entry's follow-up question is wrong, do **not** fix it in this session.
Note the issue in your commit message and move on. The next C_n session
can address it.

---

## 8. Key Principle

The goal of Session C_n is not to clear the grey zone at all costs.
The goal is to produce a defensible governance decision for one
invariant. If the honest outcome is "still ambiguous, here is a
sharper question," that is a successful session.

The registry is more valuable with 5 honest grey zones than with 5
forced classifications that governance will have to undo later.
