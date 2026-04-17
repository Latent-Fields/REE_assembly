# Session B Prompt — Invariant Classification Audit

> **Usage:** Hand this file to a fresh session (e.g. "Read
> `REE_assembly/docs/governance/session_b_prompt.md` and execute Session
> B."). The prompt is self-contained — you do not need prior conversation
> context.

---

## 1. What Session B Is

You are executing **Session B** of a multi-session governance cycle that
introduces a `universal | emergent | grey_zone` classification to every
invariant in the REE claims registry. The cycle distinguishes invariants
that hold regardless of substrate (universal) from those that are only
well-formed given a specific substrate design (emergent), plus a
grey_zone placeholder for entries the audit cannot confidently classify.

Session A (already done, commit a12dd1bb0) laid the foundations:
architecture doc, validator, schema header, the first emergent
invariant (INV-012 on SD-026), pipeline wiring. Validator currently
reports 1 emergent, 71 unclassified.

**Session B's job:** single pass through all 72 `claim_type: invariant`
entries, produce a three-bucket classification registry, apply clear
classifications directly to `claims.yaml`, leave ambiguous entries as
`grey_zone` placeholders for later per-invariant sessions.

Session B does **not** resolve grey zones, does **not** flip the
validator to strict, does **not** touch `generate_pending_review.py`
(that's Session D), does **not** modify any non-invariant claim.

---

## 2. Read These First (In Order)

1. `REE_assembly/docs/architecture/invariant_types.md` — the canonical
   schema and classification criteria. This is the source of truth.
2. `REE_assembly/docs/thoughts/2026-04-17_invariant_types_governance.md`
   — planning doc with resolved Q&A (§7), audit mechanics (§3), and
   execution order (§8). Your task is Session B as described there.
3. The INV-012 entry in `REE_assembly/docs/claims/claims.yaml` (search
   for `id: INV-012`) — the one worked example already classified. Use
   it as a template for formatting emergent entries.

Do **not** read all 72 invariants in one go before classifying. Process
them in order (INV-001 through INV-072). Keep working memory limited to
the entry in hand plus what you need to judge it.

---

## 3. Classification Criteria (Inline — Do Not Rely On Memory)

**Universal** if the invariant would still be stateable and defensible:
- under a substantially different E1/E2/E3 substrate,
- without committing to any specific SD-xxx or ARC-xxx,
- using only information-theoretic, thermodynamic, decision-theoretic,
  or logical vocabulary.

Example hypotheses (verify, do not trust): INV-009 (information-flow
constraint), generic conservation-style claims.

**Emergent** if any of the following is true:
- the invariant references a representation that only exists because a
  specific SD introduced it (z_world, z_harm, z_goal, residue field,
  commitment boundary, hypothesis tag, stored/active goal distinction,
  etc.),
- the invariant references a functional role that is only well-formed
  given a substrate design (e.g., "prospective attention", "commitment",
  "residue geometry"),
- retracting a specific SD/ARC would leave the invariant's subject
  ill-defined, not merely unevidenced.

Example hypotheses (verify, do not trust): INV-012 (commitment/
responsibility on SD-026), INV-034 (goal maintenance — references
z_goal), INV-037/038 (stored/active distinction, EVR pattern).

**Grey zone** if any of:
- the invariant could be restated in universal terms but as currently
  written references REE-specific machinery (candidate: re-write or
  classify emergent — defer to per-invariant session),
- the substrate it appears to reference has ambiguous status itself,
- you are not confident in either direction after reading the entry and
  the claims it depends on.

**The default when in doubt is `grey_zone`.** Marking something grey is a
legitimate first-class outcome, not a failure. Forcing a classification
you are not confident in corrupts the registry. Better to mark 20 grey
zones honestly than to mis-classify 5 as universal or emergent.

---

## 4. Output: The Audit Registry

Create `REE_assembly/docs/governance/invariant_classification_audit.md`
with the following structure. One entry per invariant, grouped into
three sections.

```markdown
# Invariant Classification Audit

**Session:** Session B of invariant-types governance cycle
**Date:** <UTC date, get via: date -u +"%Y-%m-%d">
**Auditor session:** <your session id>
**Total invariants audited:** 72

Schema reference: `docs/architecture/invariant_types.md`
Planning doc: `docs/thoughts/2026-04-17_invariant_types_governance.md`

---

## Summary

- Clear universal: N
- Clear emergent: N
- Grey zone: N
- Sum: 72

Retroactive flag count (pending_substrate_reconfirmation): N
Checkpoint threshold triggered: yes | no

---

## Clear Universal

### INV-XXX
- **Title:** <copy from claims.yaml>
- **Rationale:** <one sentence — why this is substrate-independent>

### INV-YYY
- **Title:** ...
- **Rationale:** ...

...

---

## Clear Emergent

### INV-XXX
- **Title:** <copy from claims.yaml>
- **emergent_from:** [SD-.., ARC-..]
- **Rationale:** <one sentence — why this invariant's subject matter
  requires these substrates>
- **Substrate status at audit:** <candidate | provisional | active>
- **pending_substrate_reconfirmation applied:** yes | no

...

---

## Grey Zone

### INV-XXX
- **Title:** <copy from claims.yaml>
- **Why ambiguous:** <2–3 sentences>
- **Candidate classifications:**
  - universal (if re-stated as: ...)
  - emergent on: [SD-.., ARC-..]
- **Follow-up prompt for Session C_n:** <self-contained paragraph that
  a fresh session can execute to resolve this one invariant>

...
```

The follow-up prompts in the grey-zone section must be fully
self-contained — assume the Session C_n auditor has never seen this
conversation. Include the invariant ID, its current text, the candidate
classifications, and what question needs to be answered.

---

## 5. Apply Clear Classifications to claims.yaml

For each entry in the "Clear universal" section:
- Add `invariant_type: universal` to the YAML entry.
- Do **not** add `emergent_from`.
- Do **not** add `pending_substrate_reconfirmation`.

For each entry in the "Clear emergent" section:
- Add `invariant_type: emergent`.
- Add `emergent_from: [SD-.., ARC-..]`.
- Every ID in `emergent_from` MUST also appear in `depends_on` — if it
  doesn't, add it to `depends_on` and note why in the entry's `notes`
  field (or move the invariant to grey_zone if you're not sure the
  dependency is real).
- Look up the current `status` of each substrate in `emergent_from`. If
  **any** listed substrate is not `active` (i.e. is `candidate`,
  `provisional`, `retracted`, or `superseded`), add
  `pending_substrate_reconfirmation: true`.
- Add a brief `notes` entry: "Classified emergent 2026-04-17 (Session B
  of invariant-types governance cycle)."

For each entry in the "Grey zone" section:
- Add `invariant_type: grey_zone`.
- Optionally add `candidate_emergent_from: [SD-.., ARC-..]` if you had
  a leading hypothesis.
- Do **not** add `pending_substrate_reconfirmation` — grey zones are
  deferred.
- Add a brief `notes` entry: "Grey-zone placeholder 2026-04-17 (Session
  B); resolution deferred to Session C_n per audit registry."

Field placement: put `invariant_type` immediately after `claim_type:
invariant`, then `emergent_from`, then
`pending_substrate_reconfirmation`. Match the style of INV-012 exactly.

---

## 6. Substrate Status Lookup

To apply rule 5's `pending_substrate_reconfirmation` correctly, you need
each substrate's current `status`. Substrates are the `claim_type:
design_decision`, `claim_type: architectural_commitment`, and
`claim_type: architecture_hypothesis` entries in claims.yaml.

Efficient approach: before classifying, grep every SD/ARC status once
and cache it. Example:

```
grep -E "^  - id: (SD-|ARC-)|^  status:" claims.yaml | ...
```

Or use the Grep tool with pattern `^- id: (SD|ARC)-\d+` and look at the
following lines. Do not re-lookup per invariant; it wastes tokens.

Known current statuses (verify, do not trust — may have changed):
- SD-001 through SD-028: mostly `candidate`, some `provisional`.
- SD-026, SD-027, SD-028: all `candidate` at time of Session A.
- Most ARC-020s: `candidate`.

If an `emergent_from` entry points at a substrate you cannot find in
claims.yaml, that is a registry error — move the invariant to grey_zone
and flag the missing ID in the registry's follow-up prompt.

---

## 7. Checkpoint Rule (Q4)

After applying all clear classifications and retroactive flags, count:
1. How many invariants you classified as emergent.
2. How many of those got `pending_substrate_reconfirmation: true`.

**If the flagged count exceeds 10, OR exceeds 20% of the clear-emergent
count, pause before committing.** Add a "CHECKPOINT REACHED" section at
the top of the audit registry summarising:
- total emergent,
- total flagged,
- which substrates are driving the flags (e.g., "SD-011 alone drives 6
  flags"),
- your recommendation (proceed / refine the rule / ask user).

Then stop and hand control back to the user for review. Do not commit
the claims.yaml changes yet (the registry file is fine to commit).

If the threshold is not exceeded, proceed to commit.

---

## 8. Commit Protocol

Assuming checkpoint not triggered (or user approved after checkpoint):

From `REE_assembly/` root:

1. Run `/opt/local/bin/python3 scripts/validate_claims.py` — should now
   show every invariant classified (universal + emergent + grey_zone =
   72), with 0 errors.
2. Run `/opt/local/bin/python3 scripts/validate_claims.py --audit` —
   verify the bucket counts match your registry summary.
3. Run `/opt/local/bin/python3 scripts/build_claims_json.py` — rebuild
   claims.json. Should report "Written 486 claims" (or whatever the
   total is).
4. Spot-check 2–3 invariants in the rebuilt
   `docs/assets/data/claims.json` to verify `invariant_type` and
   `emergent_from` are emitted correctly.

Stage and commit:

```
git add docs/governance/invariant_classification_audit.md \
        docs/claims/claims.yaml \
        docs/assets/data/claims.json
git commit -m "Session B: invariant classification audit (N universal, M emergent, K grey-zone)"
git push origin HEAD:master
```

Then in `REE_Working/`:
- Update `WORKSPACE_STATE.md` Recent Work with a Session B entry.
- Update your `TASK_CLAIMS.json` entry `status: "done"`.
- Commit and the REE_Working umbrella (local commit only — no remote).

---

## 9. Out of Scope (Do Not Do)

- Do not attempt to resolve grey-zone entries in this session — that's
  Sessions C_n, each with dedicated context.
- Do not flip `validate_claims.py` to `--strict` — that's Session D.
- Do not update `generate_pending_review.py` to emit a substrate-change
  section — that's Session D.
- Do not touch non-invariant claims (SD-xxx, ARC-xxx, MECH-xxx, etc.).
- Do not change any invariant's `status` (active/candidate/...). This
  session only adds classification fields.
- Do not edit `depends_on` except where an `emergent_from` entry is
  missing from it (rule 5) — and if you have to edit depends_on,
  consider moving the invariant to grey_zone instead.
- Do not queue or run any experiments.
- Do not re-write `claims.yaml` in full. Use targeted `Edit` calls per
  invariant to avoid accidental data loss.

---

## 10. Session Setup Checklist

Before starting:

1. Get UTC timestamp: `date -u +"%Y-%m-%dT%H:%M:%SZ"`.
2. Check `REE_Working/TASK_CLAIMS.json` for conflicts on
   `REE_assembly/docs/claims/claims.yaml`. If another session has an
   active claim on it, pause and show both claims to the user.
3. Add your own claim to `TASK_CLAIMS.json` with:
   - `session_label: "session-b-<date>-invariant-audit"`
   - `task: "Session B: single-pass invariant classification audit"`
   - `resources: ["REE_assembly/docs/governance/invariant_classification_audit.md", "REE_assembly/docs/claims/claims.yaml", "REE_assembly/docs/assets/data/claims.json", "REE_Working/WORKSPACE_STATE.md"]`
   - `status: "active"`.
4. Confirm you can find INV-012 in claims.yaml and see its three
   new fields — this is your template.
5. Confirm `scripts/validate_claims.py --audit` runs cleanly.

Then start with INV-001.

---

## 11. Key Artefacts You Will Produce

- `REE_assembly/docs/governance/invariant_classification_audit.md`
  (new) — the three-bucket registry with rationale per entry and
  follow-up prompts for grey zones.
- `REE_assembly/docs/claims/claims.yaml` (edited) — classification
  fields added to 72 invariants.
- `REE_assembly/docs/assets/data/claims.json` (rebuilt).
- `REE_Working/WORKSPACE_STATE.md` (Recent Work entry added).
- `REE_Working/TASK_CLAIMS.json` (claim entry added then marked done).

Commit message template:
```
Session B: invariant classification audit (N universal, M emergent, K grey-zone)

Single-pass audit over all 72 invariants. Classified N as universal,
M as emergent (of which X flagged pending_substrate_reconfirmation),
K as grey_zone (deferred to Sessions C_n).

Audit registry with rationale per entry and follow-up prompts for
grey zones: docs/governance/invariant_classification_audit.md

Plan: docs/thoughts/2026-04-17_invariant_types_governance.md
Schema: docs/architecture/invariant_types.md
```

---

## 12. Final Notes

- The registry doc is the deliverable governance will review. Rationale
  lines must be specific enough for a reviewer who hasn't read the
  invariant to understand why the classification landed where it did.
- Follow-up prompts for grey-zone entries are the load-bearing artifact
  for Sessions C_n. Invest real effort in making them self-contained.
- If you finish the audit and have fewer than 5 grey zones, that's a
  signal to revisit the classifications — the criteria are designed to
  produce grey zones on genuinely ambiguous cases, and a suspiciously
  clean audit often means you were too confident.
- If you finish and have more than 25 grey zones, that's also a signal —
  you may be being too cautious. Consider a second pass on grey zones
  asking "is there really ambiguity, or am I hesitating?"

Good luck.
