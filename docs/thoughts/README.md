# Thought Intake

This folder is the **raw capture** stage of a two-stage thought pipeline.

## Stage 1: Raw Capture (this folder)

Raw thoughts, concerns, or new understandings about REE. Often written on the go from mobile --
no structure required beyond a filename and the thought itself.

### Rules

- Do not delete or overwrite existing notes.
- Each thought should be its own file.
- Use a stable filename format: `YYYY-MM-DD_short-title.md`.
- Each thought file should end with a short list of possible affected components
  (E1/E2/E3/L-space/control plane/etc.) when practical, but this is not required for
  on-the-go capture.

## Stage 2: Structured Analysis (`evidence/planning/thought_intake_*`)

When a raw thought is discussed in a session, the structured analysis goes to
`evidence/planning/thought_intake_YYYY-MM-DD_short-title.md`. These files contain:

- Verbatim prompt (the original thought)
- What's New vs. Existing REE Docs (novelty table)
- Key formulations
- Affected existing claims
- Candidate claims (for future registration)
- Next steps (lit pulls, architecture docs, claim registration)

A thought intake file should reference its source via `Raw thought file:` in the header.

## Linking the Two Stages

When a structured intake is written from a raw thought:

1. Mark the raw thought as processed -- add at the top:
   ```
   Status: processed
   Intake: evidence/planning/thought_intake_YYYY-MM-DD_short-title.md
   ```
2. If claims were registered, also list claim IDs in the status header.
3. The thought sweep (`thought_sweep.py`) tracks processing status from these markers.

Not every raw thought needs a structured intake. Some are processed directly into canonical
docs or claims -- in that case, link to the doc/claim IDs as before.

## Sweep Helper (Stage 1 only)

Use the deterministic sweep helper to identify unprocessed thought files and formatting gaps:

```bash
python3 docs/thoughts/scripts/thought_sweep.py
```

Generated outputs:

- `docs/thoughts/thought_sweep.v1.json`
- `docs/thoughts/SWEEP_REPORT.md`

Optional strict mode (fails if any unprocessed thought exists):

```bash
python3 docs/thoughts/scripts/thought_sweep.py --check-unprocessed
```

**This checks Stage 1 ONLY, and only by a marker convention** (`Status: processed`). It cannot
tell you whether a Stage 2 structured intake's candidate claims were ever actually registered
into `claims.yaml`, and it cannot tell you whether an old `Processed in:` link still points at a
real claim. Use the intake audit below for that -- see "Two Checks, Not One" below for why both
exist and neither substitutes for the other.

## Intake Audit Helper (BOTH stages, ground-truth checked)

```bash
python3 docs/thoughts/scripts/thought_intake_audit.py
```

Generated outputs:

- `docs/thoughts/thought_intake_audit.v1.json`
- `docs/thoughts/INTAKE_AUDIT_REPORT.md`

Optional strict mode (fails if any Stage 1 broken link or Stage 2 orphan is found):

```bash
python3 docs/thoughts/scripts/thought_intake_audit.py --check-clean
```

Unlike the sweep helper, this checks the actual claim IDs mentioned in each file against
`docs/claims/claims.yaml` directly -- not a marker or keyword. It reports, for **Stage 1**, any
`Processed in:` link whose claim ID no longer exists (renamed, merged, retracted since the link
was written -- invisible to `thought_sweep.py`, which only checks the link block exists). For
**Stage 2**, it classifies every `evidence/planning/thought_intake_*.md` file's "Candidate
claims"-shaped section as: all named IDs registered, some/all missing (orphaned -- needs
registering), no concrete ID named yet (needs a human read -- often a non-claim tracking scheme
like `EXQ-`/`EVB-`/ad hoc numbering, or genuinely still-prose candidates), or no candidate-claims
section at all (nothing to check).

**Read this before trusting either report's silence as "nothing to do":** neither check can prove
a raw thought or a structured intake never proposed an idea that was never given ANY claim-shaped
ID at all (real or placeholder) -- that failure mode needs an actual read of the "needs a human
read" bucket, or a full manual pass, neither of which either script does for you. "0 orphans"
means "0 named-but-unregistered candidates," not "0 unprocessed ideas."

### Two Checks, Not One

A single keyword sweep (e.g. `grep -L REGISTERED`) badly over-states orphans in this codebase:
audited 2026-08-06, it flagged 66 of 75 Stage 2 files, while the ground-truth ID check found
exactly 1 genuine orphan (`thought_intake_2026-04-05_developmental_coupling_progression.md`,
unregistered 4 months, since fixed as INV-094/MECH-484/ARC-122) -- the other 65 were processed by
means the README already sanctions (folded into canonical docs, or registered without the literal
word). Trust the ID cross-check, not a keyword grep, when auditing this folder by hand.

This folder is intentionally separate from canonical documentation.
