# Literature per-paper deduplication -- indexer fix + before/after measurement

**Status: LANDED.** Chip `chip-20260816-lit-duplicate-dedup-indexer`, implementing the
governance-cycle-2026-08-16 decision recorded on **GFLAG-0032** (and, as subsumed by it,
**GFLAG-0030**). Findings this fix acts on:
`evidence/planning/literature_duplicate_entries_2026-08-14.md`.

---

## What changed

`REE_assembly/evidence/experiments/scripts/build_experiment_indexes.py` -- the
`claim_to_entries` join point in `_write_claim_evidence_matrix` -- now deduplicates
literature evidence **per (claim, paper)** before an entry is allowed to count toward a
claim's scored evidence. Confirmed while working this flag: the indexer previously had
**no dedup and no exclusion path at all** for literature (the comment above the join point
read "Literature entries are not epoch-filtered or excluded for now").

**No literature record is edited, merged or deleted.** A duplicate is not a defect in
either entry -- two independently-authored reviews of the same paper are both legitimate
curation work -- so the fix lives entirely at the join point: the excluded entry keeps its
own recorded `confidence`/`evidence_direction` untouched in `matrix["entries"]` (the full
audit log), and only its contribution to `claim_to_entries` (the list that feeds
confidence/conflict scoring) is withheld, via a new `scoring_excluded:
"duplicate_literature_entry"` reason -- the same mechanism already used for
`stale_epoch` / `superseded` / `degenerate` / `stale_substrate` / diagnostic probes.

## Design decisions

**Dedup key / fallback chain.** Records are grouped by a union-find over three EXACT
routes, transitively unioned so one paper yields one group even when the evidence for it
is mixed: normalised DOI, normalised PMID, exact normalised title. This is the identical
grouping design already validated in `scripts/audit_literature_duplicate_entries.py`
(measured clean over the 2189-record corpus) -- reused by design, not by import (see
"Why reimplemented locally, not imported" below). **Fuzzy title matching is deliberately
NOT used**: the audit measured 7 of 9 fuzzy-title-agreeing pairs in this corpus to be
DIFFERENT papers by the same author (the Craig 2002/2003 "Interoception" pair is the
sharpest case -- containment matches at full confidence on two genuinely different
papers), so a fuzzy route here would silently merge two independent studies and make one
of them vanish from a claim's scored evidence -- the opposite of what this fix exists to
prevent.

**Which entry survives.** The earliest entry by `(timestamp, literature_type, entry_id)`
sort order -- i.e. the first review of that paper for that claim. This is not an
arbitrary tie-break: it is the same framing the source audit already uses ("a surplus
evidence item is one entry BEYOND THE FIRST"), so the fix does not introduce a new
convention, it operationalises the existing one. It also avoids the alternative that the
audit explicitly flagged as NOT mechanical -- picking the higher of two disagreeing
confidences (the Bekoff pair is 0.72 vs 0.88) is not automatically the better-reasoned
review, so nothing here optimises for the highest number.

**Disagreeing confidence/evidence_direction across a duplicate pair.** Nothing is
resolved or picked as a "winning value" -- each entry keeps exactly what it says. The
kept entry's own confidence feeds scoring (because it is the one entry that survives into
`claim_to_entries`); the excluded entry's original confidence/direction remain visible,
unaltered, in `matrix["entries"]` for audit, tagged `duplicate_of` (which entry superseded
it) and `duplicate_route` (which of doi/pmid/title connected them).

**Per-claim, not global.** Dedup is keyed on `(claim_id, paper_group)`, not on
`paper_group` alone -- a paper legitimately supporting two different claims still counts
once per claim (`test_claim_evidence_no_dedup_across_different_claims`). A group of
4 duplicate records citing 1 paper for 1 claim (the MECH-058 BYOL case) collapses to 1
scored entry; the same paper cited for a second claim elsewhere is unaffected.

**Why reimplemented locally, not imported cross-directory.** The canonical
normalisation functions live in `REE_assembly/scripts/verify_literature_identifiers.py`
(`normalise_doi`), `.../audit_literature_duplicate_entries.py` (`normalise_pmid`) and
`.../audit_literature_bibliographic_accuracy.py` (`norm_title`). Those three modules pull
in `urllib`/network-capable code (live DOI/PubMed resolution) that this indexer --
stdlib-only per its own module docstring, run on every commit and by several concurrent
writers -- must not depend on. The three functions were copied byte-for-byte into
`build_experiment_indexes.py` as `_lit_normalise_doi` / `_lit_normalise_pmid` /
`_lit_norm_title`, and `test_build_experiment_indexes.py` loads the canonical originals
by file path and asserts byte-identical output over a case battery (including the
legacy-APA double-slash DOI form, which the audit script's own docstring calls "not
guessable") so the two copies cannot silently drift.

## Tests

`REE_assembly/evidence/experiments/scripts/test_build_experiment_indexes.py`, 20 new
tests (171 total in the file, all passing):

- 3 drift-pin tests against the canonical DOI/PMID/title normalisers.
- 6 `_group_literature_by_paper` union-find tests: doi-only merge, pmid-fallback merge,
  title-fallback merge, transitive union across all three routes, no-shared-identity
  stays singleton, **no fuzzy-title merge** (mirrors the Craig 2002/2003 false positive).
- 8 end-to-end `_write_claim_evidence_matrix` tests covering the Bekoff-pair shape
  (2 records), the MECH-058 shape (4 records, 1 claim), per-claim independence, and:
  - `test_claim_evidence_no_dedup_different_papers_same_claim` -- the **mandatory
    negative control**: two genuinely different papers (disjoint doi/pmid/title) cited
    for the same claim must both count. Confirmed: does not dedup.
  - `test_claim_evidence_dedup_no_identity_never_merges` -- two records with no
    doi/pmid/title at all never merge.
  - `test_claim_evidence_dedup_end_to_end_from_disk` -- exercises the real
    disk-parsing path (`record.json` -> `_scan_literature` -> normalise -> dedup), not
    just in-memory `LiteratureRecord` construction, including a case-insensitive DOI
    match (`10.1000/dup` vs `10.1000/DUP`).

Run: `cd REE_assembly/evidence/experiments/scripts && python3 -m pytest
test_build_experiment_indexes.py -q` -- 171 passed. This is the umbrella's own
`REE_assembly` corpus, not `ree-v3`'s contract suite, so `scripts/remote_pytest.sh`
(which targets `ree-v3` specifically) does not apply; run was executed locally on this
cloud worker (not the Mac), consistent with CLAUDE.md's "route off the Mac" intent.

## Before/after measurement (mandatory per the chip brief)

Measured by scanning the real corpus once (`_scan_runs` + `_scan_literature` against the
committed `evidence/` tree, no records modified) and calling
`_write_claim_evidence_matrix` twice against that same scanned data -- once with the new
dedup code, once with it monkeypatched to a no-op (every literature record its own
singleton group, reproducing pre-fix behaviour exactly) -- so the only variable between
"before" and "after" is the dedup logic itself. Neither run wrote to any tracked path;
both wrote to disposable temp directories. Measured 2026-08-18T21:52:49Z.

**Aggregate: 35 claims changed, 78 surplus literature evidence items removed** (59
distinct (claim, paper) duplicate groups collapsed -- higher than the audit's 48 raw
paper-groups because one physical duplicate group can span more than one affected claim,
e.g. the Mattar & Daw 2018 group double-counts on ARC-018, MECH-033 and MECH-056 alike).
This matches the audit report's predicted scale exactly (48 duplicate groups / 78
surplus items / 35 claims / ARC-018 +8, MECH-060 +6, MECH-033 +5, MECH-058 +5).

| claim | lit before | lit after | surplus removed | lit_conf before | lit_conf after | overall before | overall after |
|---|---|---|---|---|---|---|---|
| ARC-018 | 27 | 19 | 8 | 0.861 | 0.851 | 0.732 | 0.727 |
| MECH-060 | 18 | 12 | 6 | 0.815 | 0.813 | 0.755 | 0.754 |
| MECH-033 | 22 | 17 | 5 | 0.837 | 0.832 | 0.780 | 0.777 |
| MECH-058 | 9 | 4 | 5 | 0.826 | 0.815 | 0.826 | 0.815 |
| MECH-059 | 11 | 7 | 4 | 0.789 | 0.788 | 0.736 | 0.735 |
| Q-017 | 11 | 7 | 4 | 0.840 | 0.831 | 0.840 | 0.831 |
| MECH-092 | 16 | 13 | 3 | 0.859 | 0.864 | 0.819 | 0.822 |
| MECH-317 | 9 | 6 | 3 | 0.871 | 0.870 | 0.871 | 0.870 |
| SD-033e | 12 | 9 | 3 | 0.870 | 0.866 | 0.870 | 0.866 |
| ARC-065 | 50 | 48 | 2 | 0.859 | 0.859 | 0.847 | 0.847 |
| MECH-056 | 15 | 13 | 2 | 0.839 | 0.841 | 0.773 | 0.774 |
| MECH-057 | 7 | 5 | 2 | 0.799 | 0.793 | 0.799 | 0.793 |
| MECH-075 | 12 | 10 | 2 | 0.703 | 0.676 | 0.650 | 0.637 |
| MECH-264 | 7 | 5 | 2 | 0.873 | 0.857 | 0.873 | 0.857 |
| MECH-265 | 8 | 6 | 2 | 0.871 | 0.861 | 0.871 | 0.861 |
| MECH-285 | 16 | 14 | 2 | 0.849 | 0.843 | 0.799 | 0.794 |
| MECH-318 | 8 | 6 | 2 | 0.819 | 0.799 | 0.819 | 0.799 |
| Q-011 | 4 | 2 | 2 | 0.802 | 0.694 | 0.802 | 0.694 |
| SD-011 | 36 | 34 | 2 | 0.847 | 0.860 | 0.751 | 0.757 |
| SD-032b | 16 | 14 | 2 | 0.866 | 0.857 | 0.866 | 0.857 |
| ARC-006 | 16 | 15 | 1 | 0.847 | 0.844 | 0.847 | 0.844 |
| ARC-007 | 30 | 29 | 1 | 0.839 | 0.837 | 0.731 | 0.730 |
| ARC-032 | 7 | 6 | 1 | 0.836 | 0.833 | 0.663 | 0.661 |
| ARC-042 | 5 | 4 | 1 | 0.812 | 0.810 | 0.549 | 0.548 |
| ARC-049 | 27 | 26 | 1 | 0.862 | 0.859 | 0.862 | 0.859 |
| INV-059 | 18 | 17 | 1 | 0.860 | 0.856 | 0.860 | 0.856 |
| MECH-040 | 2 | 1 | 1 | 0.754 | 0.705 | 0.754 | 0.705 |
| MECH-044 | 7 | 6 | 1 | 0.839 | 0.834 | 0.839 | 0.834 |
| MECH-045 | 15 | 14 | 1 | 0.846 | 0.843 | 0.789 | 0.787 |
| MECH-057a | 5 | 4 | 1 | 0.824 | 0.825 | 0.762 | 0.762 |
| MECH-089 | 10 | 9 | 1 | 0.850 | 0.839 | 0.706 | 0.701 |
| MECH-102 | 9 | 8 | 1 | 0.820 | 0.819 | 0.697 | 0.697 |
| MECH-122 | 4 | 3 | 1 | 0.867 | 0.808 | 0.718 | 0.673 |
| MECH-189 | 11 | 10 | 1 | 0.815 | 0.813 | 0.795 | 0.794 |
| MECH-457 | 22 | 21 | 1 | 0.827 | 0.827 | 0.614 | 0.614 |

ARC-049 and INV-059 (GFLAG-0030's Bekoff pair) both show `surplus_removed=1` as expected
-- confirming that flag is genuinely subsumed rather than merely relabelled.

**Largest single-claim shifts in `overall_confidence`**: Q-011 (-0.108, going from 4
literature entries -- 3 of them one paper -- to 2), MECH-040 (-0.049, its only 2
literature entries were a duplicate pair), MECH-122 (-0.045). Every other affected claim
moved by <0.02. No claim's direction of movement is uniform -- 3 of the 35
(MECH-092, MECH-056, SD-011) moved UP, because removing a lower-confidence duplicate
entry can raise the remaining average, which is itself evidence nothing here silently
biases toward demotion.

**This report is the measurement, not a disposition.** Whether any of these 35 claims'
`claims.yaml` status should change as a result is a governance call for the next
`/governance` cycle, same as any other confidence movement -- this chip's job (per its
brief, and per GFLAG-0032's resolution note) was to build the fix and measure its effect,
not to apply it to `claim_evidence.v1.json` or `claims.yaml` unreviewed. The measurement
above was computed against disposable temp output; the code fix itself is landed, so the
next real `build_experiment_indexes.py` run (governance regen or otherwise) will produce
these numbers as the committed `claim_evidence.v1.json`.
