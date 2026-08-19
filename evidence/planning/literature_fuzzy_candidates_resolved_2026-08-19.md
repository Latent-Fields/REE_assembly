# Literature fuzzy-title candidates -- resolution (2026-08-19)

chip `chip-20260818-lit-fuzzy-title-candidates`, follow-on to
`evidence/planning/literature_duplicate_entries_2026-08-14.md` ("The three unconfirmed
candidates" section) and to `chip-20260816-lit-duplicate-dedup-indexer`
(`evidence/experiments/scripts/build_experiment_indexes.py`, commit `f8ec8b33b0`), which fixed
per-(claim,paper) literature dedup using EXACT doi/pmid/title matching only and deliberately left
these 3 fuzzy-title-matched candidates for manual/agent resolution.

## Summary of verdicts

| Pair | Verdict | Live double-count? | Action taken |
|---|---|---|---|
| Achille 2019 (`inv_074`, `sd_087`, `q_088`) -- all three | Same paper (ICLR 2019, arXiv:1711.08856) | No -- disjoint claim sets (INV-074/SD-087/Q-088) | Added missing `doi` to `sd_087` and `q_088` records |
| Andrews-Hanna 2010, Neuron vs. J Neurophysiol (both in `targeted_review_connectome_mech_029`) | **Different papers** | N/A -- confirmed not the same work | Repaired hallucinated PMIDs; the J Neurophysiol record's title/authors were also fabricated (copied from the Neuron sibling) and are now corrected |

No governance flag was raised -- neither pair is a live double-count once resolved, which is the
one condition under which this chip's brief called for `governance_flag.py raise`.

## 1-2. Achille et al. 2019, "Critical Learning Periods in Deep Networks" / "...in Deep Neural Networks"

**Verdict: same paper**, confirmed via web search (arXiv abstract page, dblp record) -- ICLR 2019,
arXiv:1711.08856. "Critical Learning Periods in Deep Neural Networks" is the arXiv listing title;
"Critical Learning Periods in Deep Networks" is the ICLR camera-ready / dblp title. This is an
ordinary preprint-vs-camera-ready title variation, not a hallucination -- the audit's own note
("almost certainly the same ICLR 2019 paper") is correct.

This is **not a live double-count**: the three entries citing it test three disjoint claims
(`INV-074`, `SD-087`, `Q-088`), each legitimately citing the paper once for its own claim. No
merge, no governance flag.

**Repair:** `inv_074`'s entry already carried `doi: "10.48550/arXiv.1711.08856"`. The `sd_087`
entry had no `doi` field at all, and `q_088`'s was explicit `null`. Both were filled in with the
same DOI (verified consistent with the arXiv ID via web search; not independently re-resolved
through the arXiv API, which was unreachable from this environment -- the value matches the
already-corpus-established identifier on the sibling `inv_074` entry, which is the convention
`verify_literature_identifiers.py` gate accepts). `verify_literature_identifiers.py --paths` on
all three now reports 0 conclusive findings.

Files touched:
- `evidence/literature/targeted_review_sd_087/entries/2026-08-02_sd_087_critical_learning_periods_achille2019/record.json` (+doi)
- `evidence/literature/targeted_review_sd_087/entries/2026-08-02_sd_087_critical_learning_periods_achille2019/summary.md` (+provenance note)
- `evidence/literature/targeted_review_q_088/entries/2026-08-02_q_088_critical_learning_periods_dnn_achille2019/record.json` (doi: null -> value)
- `evidence/literature/targeted_review_q_088/entries/2026-08-02_q_088_critical_learning_periods_dnn_achille2019/summary.md` (+provenance note)

## 3. Andrews-Hanna 2010 -- Neuron vs. Journal of Neurophysiology

**Verdict: two genuinely different papers**, confirming the audit's own suspicion ("different
venues, same author/year -- likely two different papers"). Both are real, both first-authored by
Jessica R. Andrews-Hanna with Randy L. Buckner as last author, both published in 2010:

| | Neuron entry | J Neurophysiol entry |
|---|---|---|
| Real title | Functional-Anatomic Fractionation of the Brain's Default Network | Evidence for the Default Network's Role in Spontaneous Cognition |
| Authors | Andrews-Hanna, Reidler, **Sepulcre**, **Poulin**, Buckner | Andrews-Hanna, Reidler, **Huang**, Buckner |
| Venue | Neuron 65(4):550-562 | J Neurophysiol 104(1):322-335 |
| PMID | 20188659 | 20463201 |
| DOI | 10.1016/j.neuron.2010.02.005 | 10.1152/jn.00830.2009 |
| PMC | PMC2848443 | PMC2904225 |

Verified via NCBI eutils `esummary` (authoritative, not just a web-search summary) for both PMIDs
in one call -- confirms distinct titles, distinct page ranges, and a non-overlapping third
co-author (Sepulcre/Poulin vs. Huang). Both entries legitimately support `MECH-029` (DMN
subsystem fractionation), so this is **not** a double-count and no governance flag was needed.

**Repair (both records had wrong identifiers -- neither original PMID pointed at the real paper):**

- **Neuron entry**: `source.url` carried PMID `20547162`, which does not identify this paper
  (a hallucinated near-miss, per the same defect class `verify_literature_identifiers.py`'s
  docstring describes). Title/authors/venue/year were already correct. Corrected `pmid`, `doi`,
  `pmc`, `volume`/`issue`/`pages`, `url`.
- **J Neurophysiol entry**: this record was worse -- `source.title` and `source.authors` were not
  just a wrong identifier but a **verbatim copy of the Neuron sibling's** title and author list,
  and `source.url` carried PMID `20147401`, which resolves to an unrelated virology paper. The
  prose in the summary (source wording / REE translation / mapping caveat) already described this
  paper's actual content (spontaneous cognition and DMN subsystems) correctly, so only the
  `source` block needed fixing: title, authors, `pmid`, `doi`, `pmc`, `volume`/`issue`/`pages`,
  `url`.

Both repairs follow the corpus's established bibliographic-repair convention (commits `461da94faa`,
`b22155a885`, `ec4467bcf4`): fields corrected in `record.json`, a `PROVENANCE NOTE` block added at
the top of `summary.md` naming what was wrong and what it was corrected to, and no
`confidence`/`evidence_direction`/`mapping`/`claim_ids_tested` field touched.

Files touched:
- `evidence/literature/targeted_review_connectome_mech_029/entries/2026-02-21_mech029_fractionation_default_network_neuron2010/record.json`
- `evidence/literature/targeted_review_connectome_mech_029/entries/2026-02-21_mech029_fractionation_default_network_neuron2010/summary.md`
- `evidence/literature/targeted_review_connectome_mech_029/entries/2026-02-21_mech029_spontaneous_cognition_jneurophysiol2010/record.json`
- `evidence/literature/targeted_review_connectome_mech_029/entries/2026-02-21_mech029_spontaneous_cognition_jneurophysiol2010/summary.md`

## Verification run

```
$ python3 scripts/validate_literature.py
validate_literature: OK (2213 records checked, 0 findings)

$ python3 scripts/verify_literature_identifiers.py --paths <the 4 touched record.json paths> --exit-nonzero
verify_literature_identifiers: OK (4 record(s) checked, 0 conclusive findings)
```

## Disposition of the source audit doc

`evidence/planning/literature_duplicate_entries_2026-08-14.md`'s "The three unconfirmed
candidates" section is now resolved by this document. That file is left as-is (a dated audit
snapshot, not something this chip's resource claim covers for editing) -- this document is the
follow-up record; a future governance pass may want to add a one-line pointer from that section to
this file.
