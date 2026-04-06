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

## Sweep Helper

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

This folder is intentionally separate from canonical documentation.
