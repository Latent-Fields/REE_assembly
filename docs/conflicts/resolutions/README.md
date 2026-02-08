# Conflict Resolutions (Decisions and Rationale)

This folder contains resolution notes for conflicts documented in `docs/conflicts/`.

## Rules

- Do not delete or overwrite conflict files.
- Each resolution should be its own file, referencing the conflict file path(s) and claim IDs.
- Use a stable filename format: `YYYY-MM-DD_conflict-short-title.md`.

## Required Sections

- Conflict reference(s)
- Resolution decision (free text)
- Claims affected (IDs)
- Superseded claims (mark as legacy in `claims.yaml`)
- Canonical docs updated (paths)
- Open follow-ups (if any)

After resolution:
- Update the original conflict file with a brief resolution summary and link to the resolution note.
- Update `docs/claims/claims.yaml`, `docs/claims/claim_index.md`, and `docs/changelog.md`.
