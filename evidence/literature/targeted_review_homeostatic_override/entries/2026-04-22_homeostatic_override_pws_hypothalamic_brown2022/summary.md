# Brown et al 2022 -- PWS Hypothalamic Volume

## Source
Brown SSG, Manning KE, Fletcher P, Holland A. "In vivo neuroimaging evidence of hypothalamic alteration in Prader-Willi syndrome." Brain Communications 2022;4(5):fcac229. DOI: 10.1093/braincomms/fcac229. PMID: 36147452

## Key claim
Adults with Prader-Willi syndrome show hypothalamic volume reductions that correlate with BMI. PWS is the canonical clinical model of pathological insatiable hunger; the hypothalamic structural alteration is consistent with the long-standing clinical hypothesis of impaired satiety / drive-regulation failure.

## Why this matters for REE V3
PWS is the human pathology equivalent of an SD-036/SD-012 regulator failure. The clinical phenotype tells V3 what regulator failure looks like in the wild:
- drive_level saturated (insatiable hunger)
- no shutdown signal despite metabolic surplus (obesity)
- the failure mode is NOT zero drive (which would be safe) -- it is SATURATED drive (which is pathological).

This argues that the V3 regulator layer must be bidirectional: shutdown-after-need-met AND override-when-need-overrides-fear. The SD-036 fix to V3-EXQ-471 should be evaluated against PWS as a failure scenario for the regulator going the wrong direction.

## Failure signatures supporting REE
- **Saturated drive failure mode**: Absence of regulator produces stuck-at-max, not stuck-at-zero. Implementation implication: the regulator's failure mode matters as much as its normal function.
- **Graded substrate alteration**: Volume changes correlate with behavioural severity; supports graded regulator function rather than all-or-nothing.

## Caveats
- PWS is multi-system and genetic; volume changes could be cause, consequence, or correlate.
- Imaging-behaviour link is correlational.

## PROVENANCE NOTE

`source.title` and `source.authors` were corrected on 2026-08-14, and
`source.pmid` added, by the DOI -> PMID crosswalk
(`scripts/verify_literature_identifiers.py --doi-crosswalk`). Provenance only --
no `confidence`, `evidence_direction`, `mapping` or `claim_ids_tested` field was
touched, and the entry's substantive content is unchanged.

The DOI was never in question: `10.1093/braincomms/fcac229` is confirmed by
Crossref and by PubMed independently, and both name the same work. What was wrong
was the record's own description of it. The declared title, *"Hypothalamic volume
is associated with body mass index in patients with Prader-Labhart-Willi
syndrome"*, matches **no** PubMed record at all (exact-title search, count 0) --
it is a plausible-sounding paraphrase of this paper's central result rather than
any real paper's title. The declared author list was a garbled version of the
real one: `Brown` and `Manning KE` are genuine, `Fletcher` and `Holland` were
missing, and `Anna Manning` / `Anthony P Goldstone` appear on no version of this
paper. Authors are recorded in PubMed's own form rather than expanded to full
given names, because inventing an expansion is the same confabulation class this
repair exists to remove.

The **evidence is unaffected**, which is why this is a provenance fix and not a
governance flag. The abstract of PMID 36147452 states the summary's key claim
directly: *"Lower whole hypothalamus volume was significantly associated with
higher body mass index in Prader-Willi syndrome (P < 0.05)"*, alongside
significantly smaller hypothalamic nuclei throughout the PWS group. The record
describes this paper correctly; it merely cited it under a title that does not
exist.

Note that `pmid` here is DERIVED from the DOI via PubMed's AID index (round-trip
verified: PubMed's own `articleids` for 36147452 names this DOI). It is a useful
handle, but it is not independent corroboration of the DOI -- see
`evidence/planning/literature_identifier_cross_resolution_findings_2026-08-14.md`.
