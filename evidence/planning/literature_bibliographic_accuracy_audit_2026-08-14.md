# Literature corpus — bibliographic accuracy audit, 2026-08-14

**Status: FINDINGS REPORT. The repairs described in "Repairs applied" below HAVE been
committed. Everything under "Left unrepaired" has NOT been changed and needs a human —
start with item 0, which is the only finding that touches evidence rather than provenance.
No `confidence`, `evidence_direction`, `mapping`, or `claim_ids_tested` field was touched
anywhere in this work.**

Chip: `chip-20260814-lit-bibliographic-accuracy`.
Tool: `scripts/audit_literature_bibliographic_accuracy.py` (committed; `--fetch` then `--report`).

---

## What this audit is, and why the schema audit cannot do it

`scripts/audit_literature_schema.py` asks whether a record uses the declared keys with the
declared types. This audit asks whether **the declared fields describe the paper the record's
own identifiers point at**. A record can be 100% schema-valid and name the wrong paper — the
corpus reached 0 schema failures of 2189 on 2026-08-14 (REE_assembly `77f58c89f7`), and every
finding below survived that.

Method: for each record carrying `source.doi` or `source.pmid`, resolve the identifier against
Crossref, doi.org content negotiation (which reaches DataCite, i.e. arXiv), or NCBI esummary,
and compare the authoritative record on three independent axes — **year**, **first-author family
name**, **title similarity**. The three are compared separately because the *combination* is
what triages a finding:

| title | authors | reading |
|---|---|---|
| agrees | disagrees | the identifier is right, the provenance fields are wrong (the confirmed `77f58c89f7` shape) |
| disagrees | disagrees | the identifier points at a different paper — a bad DOI |
| disagrees | agrees | usually a subtitle Crossref does not store — a false positive |

---

## Headline numbers

2189 records; **2073 carry an identifier**; **2060 resolved** (99.4% of those with one).

| bucket | n | % of resolved |
|---|---|---|
| (a) year mismatch, first author agrees | 30 | 1.5% |
| (b) first author differs entirely | 47 | 2.3% |
| (c) identifier does not resolve at all | 13 | 0.6% |

**After individual review, the material finding is ~40 records — about 2% of the corpus — whose
`source` block misidentifies the work.** That splits into two distinct defect classes with
different causes and different fixes, and neither was previously known to exist:

### Class 1 — hallucinated near-miss DOIs (~25 records)

The record's title and authors describe a real, correctly-cited paper. The DOI is well-formed,
in the right journal, in the right year — and points at a **different** paper. The corrected DOI
is almost always in the immediate numeric neighbourhood of the wrong one:

```
10.1016/j.conb.2010.02.014   ->  10.1016/j.conb.2010.02.015     Engel & Fries, beta status quo
10.1016/j.neuron.2012.01.032 ->  10.1016/j.neuron.2011.11.032   Leventhal, BG beta
10.1006/nimg.2001.0994       ->  10.1006/nimg.2001.1009         Farrer & Frith, agency
10.1002/hipo.22659           ->  10.1002/hipo.22656             Law, context representations
10.1523/JNEUROSCI.5053-11.2012 -> 10.1523/JNEUROSCI.0053-12.2012 Seymour, 5HT reward value
10.1523/JNEUROSCI.3699-05.2005 -> 10.1523/JNEUROSCI.2329-05.2005 Pecina & Berridge, hedonic hotspot
10.1093/cercor/bhac250       ->  10.1093/cercor/bhac266         Rolls, PPC connectome
10.1016/j.cell.2025.03.041   ->  10.1016/j.cell.2025.03.038     vmPFC cognitive map
```

This is the signature of an identifier generated from plausibility rather than looked up. It is
**invisible to every existing check**: the DOI is syntactically valid, resolves successfully, and
lands on a real paper in the expected venue.

**A cheap, self-contained detector exists and is worth building.** In two of these records
(`mech_153`, `mech_186_5ht_reward_value_seymour2012`) the `pmid` was *already correct* while the
`doi` was hallucinated. Where a record carries both identifiers, they can be resolved against
each other with no external ground truth about what the record "should" say — a disagreement is
conclusive. 490 records carry both today.

### Class 2 — wrong author list against a correct identifier (~14 records)

Title, DOI, venue and (usually) year are correct; `source.authors` belongs to a **different
paper**, typically one sharing a topic and sometimes an author. This is exactly the confirmed
`77f58c89f7` instance (Ploner et al. 2002 PNAS carrying Timmermann et al. 2001 J Neurophysiol's
author list and year), and it is not a one-off — 14 more were found.

**The scientific content is the DOI's paper in every case checked.** `summary.md` describes the
correct study; only the attribution is wrong. That is the good outcome: the evidence is not
misattributed to the wrong findings, so `confidence` and `evidence_direction` remain valid and
were deliberately left untouched, exactly as in the `77f58c89f7` repair.

**But the wrong attribution is in the PROSE as well as in `source.authors`** — summaries open
"Opendak, Sullivan, and Sullivan examine…", "Staresina and colleagues reveal…", "Zago et al.
(2021)". Both were repaired together; a `record.json`-only fix would have left the record
still asserting the wrong authorship in the text a human actually reads.

A sub-class is worse than conflation: **some author names are fabricated outright**, not borrowed
from a real paper. `arc023_thalamic_circuits_signal_noise_nature2021` carried
`["Adam S. Bhatt", "Michael M. Bhatt", "Karl Bhatt"]` against Mukherjee, Lam, Wimmer & Halassa
(Nature 2021). The surname "Bhatt" recurs across 6 unrelated records as an apparent substitute
for a real surname, including the garbled `"Ileana L. Bhatt-Hangya"` for Ileana L. Hanganu-Opatz.
All were born that way in their originating pull commit (e.g. `95cc0d0e80`), so this is
**pull-time fabrication, not later corruption**.

---

## Repairs applied

Provenance only. One commit per coherent group; the authoritative source is named in each commit
message. See `git log --grep="lit-bib:"` in `REE_assembly`.

**Group 1 — corrected DOI/PMID, content and authors already correct (15 records).**
Each replacement DOI was fetched and re-verified on title, first author and year before use.

**Group 2 — corrected DOI *and* author list (6 records).** Both fields were wrong; the record's
title was the reliable field and was used to recover the work.

**Group 3 — corrected author list against a correct DOI (13 records).** `source.authors` replaced
with the Crossref list, and the attribution corrected in `summary.md` prose.

**Group 4 — author-order corrections (5 records).** Yu & Dayan 2005 (3 entries, declared as
"Dayan, Yu") and Walker & van der Helm 2009 (2 entries, declared reversed).

**Group 5 — prose attribution in 16 `summary.md` files.** The wrong author list was asserted in
the text as well as in `source.authors`. Attribution only; no scientific content changed.

**Effect, measured by re-running the audit on the repaired corpus:** bucket (b) **47 → 8**. All
8 residual flags are accounted for below — 4 unrepairable, 4 known false positives. Bucket (a)
went 30 → 31: the new entry is `mech_029_moral_neuroscience_social_decisionmaking_2019`, whose
online-first/issue year discrepancy only became visible once its DOI was corrected. The schema
audit still reports **0 failing of 2189**.

Commits: `461da94faa` (g1), `ded51143ff` (g2), `b062ceaf58` (g3), `64995256a7` (g4),
`01ad824153` (g5).

---

## Left unrepaired — needs a human

**0. THE ONE FINDING THAT IS NOT PROVENANCE — a summary describing a different paper than
its own identifier. This is the "much bigger deal" case and it was NOT touched.**

`targeted_review_connectome_mech_186/entries/2026-04-09_mech_186_5ht_valence_model_based_huys2015/summary.md`

Every other record checked had the right content under the wrong name. This one is a **blend of
two papers**, and the blend runs through the evidence, not just the byline:

- The record's `title` and `doi` (`10.1038/mp.2015.46`) are **Worbe, Palminteri, Savulich, Daw,
  Fernandez-Egea, Robbins & Voon (2016) Molecular Psychiatry**, *"Valence-dependent influence of
  serotonin depletion on model-based choice strategy"* — an ATD study whose reward/punishment
  asymmetry is exactly what MECH-186 is being supported by, and whose venue the summary's own
  confidence reasoning correctly names ("Molecular Psychiatry").
- But the heading, the "What the paper did" section and the limitations section describe
  **Huys et al., *"Interplay of approximate planning strategies"*** — *"a large-scale study
  (n=1,762 online participants)"*, *"the ATD subsample (n=38)"*, *"The online sample (n=1,762) is
  not the ATD sample"*. Those sample sizes are not the Worbe study's.

So the **stated methodological basis for `confidence: 0.62` is partly drawn from a study the
entry is not citing**, and one of the limitations ("the large N is correlational") is a caveat
about a sample that is not in the cited paper at all. `source.authors` was corrected to Worbe et
al. (the title and DOI already agreed, so the author list was the outlier) — but the **summary
prose was deliberately left alone**, and `confidence` / `evidence_direction` were not touched.

**What a human needs to decide:** whether the MECH-186 support rests on the Worbe result (in
which case the summary needs rewriting against that paper, and the sample-size claims deleted)
or on Huys et al. (in which case this should be two entries, and the Huys one needs its own
correct identifier). Either way `confidence: 0.62` should be re-derived, because its recorded
reasoning cites both.

**Two more records may have the same shape but could not be settled from Crossref** (no abstract
is served for either DOI), so they were also left prose-uncorrected:
- `arc_041/entries/2026-04-02_arc_041_ofc_vmpfc_representational_spaces_2024` — title and DOI are
  Moneta, Grossman & Schuck (TiNS 2024), but the summary's content (lateral-OFC credit assignment
  vs medial-OFC value-guided choice, *"across primate species"*) reads as Rudebeck & Murray, who
  were the declared authors.
- `arc_041/entries/2026-04-02_arc_041_vmpfc_cognitive_map_value_2025` — title and DOI are Veselic
  et al. (Cell 2025); the summary describes macaque single-unit recordings, which is consistent
  with that author list but was not independently confirmed.

**1. Two records whose correct identifier could not be determined.**
   - `2026-03-29_mech_033_hippocampal_sequences_wikenheiser2015` — declared title
     *"Decoupled traversals of the hippocampal sequence reflect decisions about the future"*
     does not match any Wikenheiser & Redish work found; `10.1038/nn.3945` resolves to an
     unrelated dopamine paper. The declared title may itself be fabricated.
   - `2026-03-29_arc_032_frontal_theta_hippocampus_reward_hyman2010` — `10.1002/hipo.20709`
     resolves to Christie, *"Exercising some control over the hippocampus"* (2009). The declared
     title matches Hyman et al. but the year and DOI do not disambiguate which Hyman paper.

**2. Two book-chapter records** (`gergely_watson1996_social_biofeedback`,
   `murray_trevarthen_1985_double_video`) whose DOIs resolve to unrelated works. Crossref
   proposed Routledge reprint DOIs; the proposal for Murray & Trevarthen was clearly wrong
   (*"Intonation in Discourse"*). Chapter-level DOIs for reprinted classics need a judgement
   about which edition the entry means.

**3. The 13 unresolvable identifiers (bucket c).** Mostly benign — `10.5555/*` are ACM Digital
   Library handles that were never registered DOIs, and several `10.1146`/`10.1016` entries are
   pre-1997 articles Crossref does not index. Two are not benign:
   - `10.0000/example-doi` — a literal placeholder, in
     `neuro_pe_habenula_da/entries/2026-02-13_habenula_da_signed_pe_review`.
   - `10.1163/156853995X00822` and `10.1163/156853995X00101` — two entries with the *same*
     declared title (*"Play Signals as Punctuation"*) and *different* DOIs, both 404. At least
     one is fabricated.

**4. The 30 bucket-(a) year mismatches were reviewed and NOT repaired — they are almost all
   legitimate.** 24 of 30 are arXiv-preprint-year vs published-year (`eysenbach2019` /[2018],
   `hafner`/[2018], `kipf2022`/[2021]) or online-first vs print issue
   (`barrett2017`/[2016] — *The theory of constructed emotion*, SCAN, online 2016, issue 2017).
   The corpus convention is to cite the publication the entry actually read. **Do not "fix"
   these**; a future run of this audit will re-flag them and should re-reach the same conclusion.

---

## Known false positives of the detector (do not chase these)

- **Subtitle truncation.** Crossref stores only the main title for many publishers, so
  *"The p Factor: One General Psychopathology Factor…"* vs *"The p Factor"* scores 0.24. 14
  records. Harmless; the author check carries these.
- **Non-ASCII surnames.** `strip_accents` normalises combining diacritics but not distinct
  letters — `Hoydal` vs `Høydal`, `Rodriguez` vs `Rodrı́guez` — so an entirely correct ASCII
  transliteration reads as a first-author mismatch. 2 records.
- **Author name changes.** `mech_172_swr_dw_coupling_3xtg_benthem2020` declares "Benthem SD";
  Crossref carries "Sarah D. Cushing" for the same person. The other 8 authors match in order.
  Left alone.
- **Preprint author-order differences.** CURL (`sd_009_curl_contrastive_unsupervised_rl_laskin2020`)
  is "Srinivas, Laskin, Abbeel" on arXiv and "Laskin, Srinivas, Abbeel" at ICML (equal
  contribution). Left alone.

---

## Recommendation

The ~2% misidentification rate is high enough to justify a standing check, and the corpus is
still growing by automated pull. Two candidates, in order of cost-effectiveness:

1. **DOI-vs-PMID cross-resolution** for the 490 records carrying both. No external notion of
   correctness is needed, the signal is conclusive when it fires, and it would have caught two
   of the hallucinated DOIs above outright.
2. **A pull-time gate**: resolve the identifier once at record-creation time and refuse a record
   whose declared first author and title do not match what the identifier returns. This is the
   only measure that stops the defect entering, and it is cheap at pull time (one API call per
   new record) versus 2073 at audit time.

Do **not** turn `audit_literature_bibliographic_accuracy.py --exit-nonzero` into a commit gate
while the residue above is unrepaired — a gate that fires on every commit gets turned off. Same
convention, and the same reasoning, as `audit_literature_schema.py`.
