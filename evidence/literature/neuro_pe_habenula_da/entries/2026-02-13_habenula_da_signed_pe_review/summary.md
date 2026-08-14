# Literature Summary: 2026-02-13_habenula_da_signed_pe_review

> **PROVENANCE NOTE (2026-08-14, chip `chip-20260814-lit-unrecoverable-identifiers`). NO field was
> changed; there is no source to recover, and the entry is flagged for governance (GFLAG-0031).**
> This record does not cite a real work. Its `source` block is a template placeholder end to end:
> `authors` are `["Example Author A", "Example Author B"]`, `doi` is the literal
> `10.0000/example-doi`, `url` is `https://example.org/habenula-da-review`, and `venue` is the
> generic string `"Neuroscience Review"`. The summary below carries no findings, methods, sample or
> citations, so there is nothing in the content to identify a paper *from* — unlike the other records
> in this chip, where a wrong identifier sat on top of a real, identifiable study. No replacement
> identifier was invented, and the placeholder DOI was deliberately left in place rather than nulled,
> so that `scripts/audit_literature_bibliographic_accuracy.py` keeps reporting it until governance
> disposes of the entry.
>
> This is not a provenance defect. The entry asserts `evidence_direction: supports` at
> `confidence: 0.74` for MECH-053 and MECH-054 on the basis of a source that does not exist, and it
> is live in the derived index (`evidence/experiments/claim_evidence.v1.json`), so it is currently
> contributing to those two claims' evidence. `confidence`, `evidence_direction`, `mapping` and
> `claim_ids_tested` were not touched.

- Scope: habenula-midbrain dopamine interactions and aversive/benefit prediction-error partitioning.
- Claim linkage:
  - `MECH-053` (habenula-like aversive PE gate)
  - `MECH-054` (signed harm/benefit PE precision)
- Direction: supports
- Confidence: 0.74
- Caveat: this is a review-level synthesis and not a direct one-to-one architecture validation.
