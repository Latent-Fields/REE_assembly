# Literature duplicate-entry scan — 2026-08-14

**Status: FINDINGS REPORT. No literature record was modified, merged or deleted by this
chip. Deduplication is a governance decision and was not made here.**

Chip `chip-20260814-lit-duplicate-entry-scan`, follow-on to
`chip-20260814-lit-unrecoverable-identifiers` and to **GFLAG-0030**.

Tool built by this chip: `scripts/audit_literature_duplicate_entries.py`
(REE_assembly `59d544cc01`), tests `scripts/test_audit_literature_duplicate_entries.py`
(38, time-independent, no network). Machine-readable output:
`audit_literature_duplicate_entries.py --json <path>`.

---

## Headline

**The Bekoff pair is not the only duplicate. It is 1 of 48.**

GFLAG-0030 recorded that Bekoff (1995), *"Play Signals as Punctuation"*, is entered twice
and therefore counts as two independent evidence items toward ARC-049 and INV-059. That
finding is confirmed by this scan and is correct — but it substantially **under**-bounds the
problem rather than bounding it. Across the 2189-record corpus:

| | count |
|---|---|
| records scanned | 2189 |
| duplicate groups (same paper, 2+ records) | **286** |
| records inside some duplicate group | **797** (36% of the corpus) |
| groups where a claim is **double-counted and live in the derived index** | **48** |
| groups where a claim is double-counted but not live in the index | 0 |
| groups whose records cite the paper for **disjoint** claim sets (not a defect) | 238 |
| unconfirmed fuzzy-title candidates (not graded, need a human) | 3 |

Restricted to the part that actually inflates evidence today:

| | count |
|---|---|
| distinct claims receiving inflated literature evidence | **35** |
| **surplus evidence items** in `claim_evidence.v1.json` | **78** |
| of those, from the Feb-2026 `_followup` / `_lit-NNNN_completion` backfill | 17 |
| of those, where 2+ entries carry an **identical** `confidence` | 22 |

A "surplus evidence item" is one entry beyond the first that reaches
`evidence/experiments/claim_evidence.v1.json` for the same claim from the same underlying
paper. 78 is the number of literature evidence items that would disappear from the derived
index if every group in this report were deduplicated to one entry per (paper, claim).

**797 records involved is NOT 797 defects.** 238 of the 286 groups are one paper legitimately
cited by several reviews for *different* claims, which is ordinary and correct. The 48 is the
actionable number.

---

## What the scan does, and the one thing it deliberately refuses to do

Records are grouped by three routes, unioned transitively so that one work yields one group:

1. **normalised DOI** — case-folded, resolver prefix stripped, legacy APA double-slash
   collapsed. Reuses `verify_literature_identifiers.normalise_doi` rather than
   reimplementing it.
2. **PMID**.
3. **exact normalised title** — accent-, markup- and punctuation-normalised
   (`audit.norm_title`).

The union is load-bearing: an arXiv preprint and its journal version share a title and not a
DOI; a null-DOI record and a good one share only a PMID. Alexander (1986) is entered under
two DOIs differing in their final digits (`...002041` and `...002001`) — the hallucinated
near-miss class — and only the title route joins them.

**Fuzzy title matching is reported separately as UNCONFIRMED CANDIDATES and is barred from
merging a group or producing a grade.** This is a measurement, not caution. Run as a
grouping route over this corpus, `titles_agree` (subtitle containment, then a 0.60 ratio)
produced 9 groups of which **7 were plainly different papers by the same author**, and 3 of
those were graded as live double-counting:

| pair | route that misfired |
|---|---|
| Crapse 2008, *"Corollary discharge across the animal kingdom"* vs *"...circuits in the primate brain"* | ratio |
| Craig 2002, *"How do you feel? Interoception: the sense of the physiological condition of the body"* vs Craig 2003, *"Interoception: the sense of the physiological condition of the body"* | **containment** |
| Holt-Lunstad 2010 vs 2015; Johnson *Source monitoring* 1993 vs *Reality monitoring* 1981; Momennejad 2017 vs 2018; Ploner 2002 vs 2004; DiCarlo 2007 vs 2012 | ratio |

The Craig pair is the instructive one: the 2003 title is contained in the 2002 title
verbatim, so the containment branch fires at full confidence on two genuinely different
papers. `titles_agree` was built for a question that already has an anchor — "this
identifier resolves to *this* record; do the two titles describe one work?" — where the only
variation to absorb is formatting drift. Duplicate detection has no anchor, so the same
predicate is asked to separate two papers one author wrote on one topic, which it cannot do.

Exact-title matching measured **clean** over the same corpus (21 groups, all genuine).
So the line is drawn between exact and fuzzy, not between title and identifier.

Candidates survive three guards — no conflicting non-null DOIs, no conflicting non-null
PMIDs, and years within 2 — which reduce 9 pairs to 3. What survives is emitted as a
question, never as a finding.

---

## The three unconfirmed candidates

| pair | verdict needed |
|---|---|
| Achille 2019, *"Critical Learning Periods in Deep Neural Networks"* (`inv_074`, arXiv DOI) vs *"Critical Learning Periods in Deep Networks"* (`sd_087`, no DOI) | almost certainly the same ICLR 2019 paper; claim sets disjoint |
| the same `sd_087` record vs `q_088`'s *"Critical Learning Periods in Deep Neural Networks"* | same, second half of the same trio |
| Andrews-Hanna 2010, *"Functional-Anatomic Fractionation of the Brain's Default Network"* (Neuron) vs *"Spontaneous thought and the default network: functional-anatomic fractionation of the brain's default mode"* (J Neurophysiol) | **different venues, same author, same year — likely two different papers.** Both are in `targeted_review_connectome_mech_029` and both cite MECH-029, so if they ARE one paper this is a live double-count |

---

## Class 1 — the Feb-2026 backfill (17 surplus items, the cleanest to act on)

A distinct generator artifact from **2026-02-14/15**: entries suffixed `_followup` and
`_lit-NNNN_completion` that duplicate a parent entry, citing **the same paper for the same
claim at the same confidence**. These are not independent re-reviews; there is nothing in
them that a second reviewer contributed.

The clearest case, MECH-058 — one paper (BYOL, `10.48550/arXiv.2006.07733`), four records,
one claim, one confidence:

```
targeted_review_mech_058           2026-02-14_mech058_byol_ema_target_predictor_separation   0.78  [MECH-058]
targeted_review_mech_058           2026-02-15_mech058_byol_target_anchor_followup            0.78  [MECH-058]
targeted_review_mech_058           2026-02-15_mech058_lit-0017_completion                    0.78  [MECH-058]
targeted_review_connectome_mech_058 2026-02-15_mech058_connectome_byol_target_predictor_..   0.78  [MECH-058]
```

MECH-058 currently carries **4** literature evidence items from **1** paper.

Same shape elsewhere: MECH-059 (Kendall & Gal 2017, 4 records at 0.67/0.67/0.67/0.60),
Q-017 (Yu & Dayan 2005, 4 records at 0.79/0.79/0.79/0.78), MECH-060 (Kerns et al. 2004,
3 records all at 0.78, **all three in one `literature_type`** — the only group in the corpus
entirely contained in a single review), MECH-056 (Mattar & Daw 2018, 3 records all at 0.73),
Q-011 (Ambrose, Pfeiffer & Foster 2016, 3 records all at 0.72).

30 `_followup` / `_completion` records sit inside duplicate groups in total.

## Class 2 — landmark papers reviewed many times over

Three papers are each entered 15-18 times across 13-17 different `literature_type` reviews:

| paper | records | reviews | double-counted claims |
|---|---|---|---|
| Pfeiffer & Foster 2013, *"Hippocampal place-cell sequences depict future paths to remembered goals"* | 18 | 17 | ARC-018, ARC-032, MECH-033 |
| Mattar & Daw 2018, *"Prioritized memory access explains planning and hippocampal replay"* | 17 | 13 | ARC-018, MECH-033, MECH-056 |
| Aston-Jones & Cohen 2005, *"An integrative theory of locus coeruleus-norepinephrine function"* | 15 | 14 | MECH-040, Q-017 |

**Most of each group is legitimate** — each review tests a different claim, which is the
`disjoint_claims` case. The defect is the minority of records within each that land on a
claim another record in the group already covers. ARC-018 is the worst affected claim in the
corpus: **6 entries** from the Mattar & Daw group plus **3** from the Pfeiffer & Foster group
(+8 surplus across 3 groups).

For comparison, the largest group of all is `disjoint_claims` and entirely benign: Peng
(2011), *"Reproducible Research in Computational Science"*, cited 11 times across 11
reviews for 11 different claims.

## Class 3 — ordinary two-review overlaps

The long tail: 2-3 records, two reviews, overlapping claim sets, differing confidences.
The Bekoff pair (0.72 / 0.88 on ARC-049 + INV-059) is exactly this shape, as are e.g.
Kempadoo 2016 on MECH-075, Staresina 2015 on MECH-122, Bengio 2009 on ARC-042.
These are the cases where governance has a genuine judgement to make about which
confidence to keep, because two reviewers reached different numbers on the same paper.

---

## Per-claim surplus (35 claims, 78 surplus items)

| claim | surplus | groups |
|---|---|---|
| ARC-018 | +8 | 3 |
| MECH-060 | +6 | 4 |
| MECH-033 | +5 | 3 |
| MECH-058 | +5 | 2 |
| Q-017 | +4 | 2 |
| MECH-059 | +4 | 2 |
| SD-033e, MECH-317, MECH-092 | +3 each | 3 each |
| MECH-056, MECH-057, MECH-265, MECH-075, ARC-065, SD-032b, MECH-285, Q-011, SD-011, MECH-264, MECH-318 | +2 each | 1-2 each |
| ARC-006, ARC-007, ARC-032, ARC-042, ARC-049, INV-059, MECH-040, MECH-044, MECH-045, MECH-057a, MECH-089, MECH-102, MECH-122, MECH-189, MECH-457 | +1 each | 1 each |

---

## Governance decisions this report does NOT make

1. **Whether to merge, or to keep both entries and mark one non-independent.** Two reviews
   reaching 0.72 and 0.88 on one paper is information about the reviews, and deleting one
   discards it. A `superseded`-style `evidence_direction`, or an explicit
   non-independence marker, may be better than a merge. There is no such marker in the
   `literature_evidence/v1` schema today.
2. **Which confidence survives a merge.** Not mechanical: the higher number is not
   automatically the better-reasoned one.
3. **Whether the posterior model should discount within-paper repeats structurally**, rather
   than this being repaired entry-by-entry. `claim_evidence.v1.json`'s `lit_posterior`
   treats each entry as an independent observation; nothing in the pipeline knows that four
   MECH-058 entries are one paper. A per-paper deduplication inside the indexer would fix
   the whole class at once and keep the reviews intact — **this is probably the higher-value
   route** and is `complicated (buildable)`, not probe-gated.
4. **The Class-1 backfill entries specifically.** They look safe to retire wholesale, but
   they were generated by something, and whatever generated them may still run.

## Flags

- **GFLAG-0030** (already open) covers ARC-049 / INV-059 — the Bekoff pair. Confirmed by
  this scan; **no second flag was raised for it**.
- **One new flag** raised by this chip for the remaining **33** claims, flag type
  `evidence_discrepancy`.
