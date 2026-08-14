# Literature corpus — bibliographic accuracy audit, 2026-08-14

**Status: FINDINGS REPORT. The repairs described in "Repairs applied" below HAVE been
committed. Everything under "Left unrepaired" has NOT been changed and needs a human —
start with item 0, which is the only finding that touches evidence rather than provenance.
No `confidence`, `evidence_direction`, `mapping`, or `claim_ids_tested` field was touched
anywhere in this work.**

Chip: `chip-20260814-lit-bibliographic-accuracy`.
Tool: `scripts/audit_literature_bibliographic_accuracy.py` (committed; `--fetch` then `--report`).

> **UPDATE 2026-08-14T07:05Z — "Left unrepaired" items 1, 2 and 3 have since been worked**
> by follow-on chip `chip-20260814-lit-unrecoverable-identifiers` (REE_assembly `ec4467bcf4`).
> Four of the six records were repaired, two were escalated instead, and two further defects
> surfaced in the process. See the new **"Disposition of items 1-3"** section at the bottom.
> Item 0 (MECH-186 / GFLAG-0027) is **still open** and is still where a reader should start.

> **UPDATE 2026-08-14T08:04Z — BOTH RECOMMENDATIONS BELOW ARE NOW BUILT**, by follow-on chip
> `chip-20260814-lit-identifier-verification-gate`. Findings and design:
> [`literature_identifier_cross_resolution_findings_2026-08-14.md`](literature_identifier_cross_resolution_findings_2026-08-14.md).
>
> - **Recommendation 1 (DOI↔PMID cross-resolution)** — `scripts/verify_literature_identifiers.py
>   --cross-check`. Found **7 further misidentified records** across the 491 that carry both
>   identifiers, all repaired (`b22155a885`); the sweep now reports 0. **Four of the seven are wrong
>   PMIDs, which is a defect class THIS audit structurally cannot see** — it resolves the DOI and,
>   once that resolves, never consults the PMID. So the ~2% figure below is an *under*-count of
>   identifier defects, not an over-count.
> - **Recommendation 2 (pull-time gate)** — wired as stage 2 of `scripts/precommit_literature.sh`,
>   scoped to the records a commit touches, blocking by default, and failing open on every network
>   condition. Whole-corpus baseline is **1 record of 2072** (the habenula placeholder, GFLAG-0031,
>   deliberately unwaived).
>
> The instruction below — *do not* turn `audit_literature_bibliographic_accuracy.py --exit-nonzero`
> into a commit gate — **still stands and was followed**: the new checker holds only the conclusive
> subset of this audit's evidence, and this audit remains a report a human triages. The four false
> positives listed under "Known false positives of the detector" are pinned as negative-control tests
> there, and one of them (**subtitle truncation, in its short-title form**) turned out to fire in the
> new checker's first cut and is now fixed.

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

---

## Disposition of items 1-3 (2026-08-14T07:05Z, chip `chip-20260814-lit-unrecoverable-identifiers`)

Follow-on to the six records above. **Provenance only**; no `confidence`, `evidence_direction`,
`mapping` or `claim_ids_tested` field was touched. Commit: REE_assembly `ec4467bcf4` (12 files —
4 `record.json` repairs plus a `PROVENANCE NOTE` block in each of 7 `summary.md`, the location the
v1 schema designates for provenance prose). Method: read each entry's `summary.md` first to
establish what the content actually describes, recover the identifier, then fetch the proposal back
and compare title, first author and year before writing. Every replacement below was verified that
way.

**Two of the six were NOT repaired.** In both, the identifier could not be settled without deciding
a question about the *evidence* rather than the provenance, so nothing was written and the defect
was escalated instead — the same handling item 0 got.

| record | outcome |
|---|---|
| `mech_033_hippocampal_sequences_wikenheiser2015` | **repaired** + GFLAG-0028 |
| `arc_032_frontal_theta_hippocampus_reward_hyman2010` | **not repaired** → GFLAG-0029 |
| `arc049_inv059_gergely_watson1996_social_biofeedback` | **repaired** |
| `q035_arc049_murray_trevarthen_1985_double_video` | **repaired** |
| `devrobotics_play_signals_punctuation_bekoff1995` | **repaired** + GFLAG-0030 |
| `arc049_bekoff1995_play_signals_canids_punctuation` | **repaired** + GFLAG-0030 |
| `habenula_da_signed_pe_review` | **not repaired** → GFLAG-0031 |

### Item 1a — `wikenheiser2015`: repaired from its own PMID; content mismatch escalated

The declared title is **fabricated** — a Crossref bibliographic search for it returns nothing
resembling it — and `10.1038/nn.3945` is Zhang et al., *"Dopaminergic and glutamatergic microdomains
in a subset of rodent mesoaccumbens axons"*. The record's own **`pmid` `25559082` was already
correct** and recovered the work: Wikenheiser & Redish, *"Hippocampal theta sequences reflect current
goals"*, Nat Neurosci 18(2):289-294, `10.1038/nn.3909`. Declared authors, year and venue already
matched it, so only `title` and `doi` were wrong.

**This is the third confirmed instance of the report's own Class-1 detector recommendation** (§Class 1,
"where a record carries both identifiers, they can be resolved against each other with no external
ground truth") — after `mech_153` and `mech_186_5ht_reward_value_seymour2012`. It is also the *only*
one of the six that had such an anchor, and the difference in outcome between this record and
`hyman2010` is entirely down to having one. That is a direct argument for building the
DOI-vs-PMID cross-resolution check the Recommendation section ranks first.

**GFLAG-0028 (open, MECH-033):** the summary's methods section does not describe nn.3909. It
describes a T-maze with probabilistic reward and vicarious-trial-and-error head-scanning at a
stationary choice point — the Johnson & Redish (2007) paradigm. nn.3909 used a circular-track
delay-foraging task (three feeders, fixed per-session delays, rats free to wait or skip) and reports
theta look-ahead extending farther toward more distant goals and predicting the destination. The
prose was left unedited pending governance, as for item 0.

### Item 1b — `hyman2010`: no field written; the entry has no recoverable source

Every identifier on this record is wrong **and they disagree with each other**:

- the title is fabricated (a PubMed author search for Hyman JM + Hasselmo ME + theta returns five
  papers, none of them it);
- `10.1002/hipo.20709` is Christie, *"Exercising some control over the hippocampus"* (2009);
- the `url`'s PMID 19489006 is Hill et al. on cannabinoid signalling and exercise-induced
  progenitor proliferation — also unrelated;
- the declared author list is real but shared by **two** papers, and `year` and `venue` point at
  different ones: Hyman et al. **2005**, Hippocampus 15:739-749 (`10.1002/hipo.20106`) matches the
  venue; Hyman et al. **2010**, Front Integr Neurosci 4:2 (`10.3389/neuro.07.002.2010`) matches the
  year.

**Neither Hyman paper is the study the summary describes**, which is what makes this unrepairable
rather than merely ambiguous. Hyman 2010 used an operant lever-press DNMS task and reports that
theta *entrainment of mPFC units* fell on error trials while firing rates did not; Hyman 2005 used
linear-track running and open-field foraging with no working-memory component. The summary's account
— simultaneous HPC/mPFC **LFPs**, spatial alternation, coherence elevated specifically in the *stem*
of the maze, mPFC theta phase leading hippocampal theta — is the signature of **Jones & Wilson
(2005)**, *"Theta rhythms coordinate hippocampal-prefrontal interactions in a spatial memory task"*
(PLoS Biol 3:e402), a paper Hyman 2010 itself cites. Writing that DOI would change the evidence, not
the provenance, so the record was left byte-identical and **GFLAG-0029** raised. The audit will keep
reporting it in bucket (b), which is correct.

### Item 2 — the two "book chapter" records: both were `null`-DOI cases, and one is not a chapter

Neither needed the edition judgement the original item anticipated, because in neither case does a
chapter-level DOI exist at all. Both now carry `doi: null`, which the v1 schema defines as *"checked,
none exists"* — more informative than deleting the key.

- **`gergely_watson1996`** is **not a book chapter**: it is a 1996 *International Journal of
  Psycho-Analysis* article, 77(6):1181-1212, exactly as its own `venue` said. Its DOI
  (`10.1097/00004583-198903000-00016`) was Cohn & Tronick 1989. PubMed carries no `doi` articleid
  for the article and Crossref has no record, so `doi` → `null` and the verified **`pmid`
  `9119582`** was added as the record's identifier. The 2018 Routledge reprint
  (`10.4324/9780429471643-7`) was deliberately **not** used: different title, credited to the book's
  authors (Fonagy et al.), so citing it would misstate which text the entry read.
- **`murray_trevarthen_1985`** is a genuine chapter — *Social Perception in Infants*, Field & Fox
  (eds), Ablex, 1985 — with no chapter DOI in Crossref and no PubMed record. Its DOI
  (`10.2307/1130922`) was Zelazo & Shultz, *"Concepts of Potency and Resistance in Causal
  Prediction"* (Child Development 60:1307, 1989). `doi` and `pmid` → `null`, and the containing
  volume's **ISBN `9780893912314`** added instead (verified via OpenLibrary), which the schema
  declares for exactly this case. The Crossref-proposed `10.4324/9781315802572-8` (*"Intonation in
  Discourse"*) is a different chapter and was not used.

In both, the summary content matches the cited work, so this was pure provenance.

### Item 3a — the Bekoff pair: one real DOI, and a duplicate entry nobody had noticed

Both 404 DOIs were fabricated. The real identifier is **`10.1163/156853995X00649`** — Bekoff,
*"Play Signals as Punctuation: the Structure of Social Play in Canids"*, Behaviour 132(5-6):419-429
(1995) — verified against Crossref on title, author and year, and now on both records.

Repairing them is what made the second defect visible, and it is the more consequential one.
**GFLAG-0030 (open, ARC-049 / INV-059 / Q-035 / MECH-196): this single study is entered twice**, in
two different `literature_type` reviews, with different confidences (0.72 and 0.88) and overlapping
`claim_ids_tested`. Both appear in the derived `evidence/experiments/claim_evidence.v1.json`, so one
paper currently counts as two independent evidence items toward ARC-049 and INV-059. Deduplication
is a governance call and was not made here. Note the generalisation: **two fabricated DOIs for the
same paper masked the duplication from any identifier-keyed check** — a corpus-wide duplicate scan
keyed on the *repaired* DOIs is now worth running, and is cheap.

### Item 3b — `habenula_da_signed_pe_review`: a fully synthetic record, not a bad identifier

This one is a category apart from the rest of the audit and should not be read as a provenance
finding. The `source` block is a **template placeholder end to end** — `authors`
`["Example Author A", "Example Author B"]`, `doi` `10.0000/example-doi`, `url`
`https://example.org/habenula-da-review`, `venue` the generic string `"Neuroscience Review"` — and
the `summary.md` carries no findings, methods, sample or citations. Unlike every other record in this
chip, there is nothing in the content from which to identify a paper, so no identifier was invented.
The placeholder DOI was deliberately **left in place** rather than nulled, so the audit keeps
reporting it until the entry is disposed of.

**GFLAG-0031 (open, MECH-053 / MECH-054):** the entry asserts `evidence_direction: supports` at
`confidence: 0.74` for both claims on the basis of a source that does not exist, and it is live in
`claim_evidence.v1.json`, so it is currently contributing to them. Governance needs to decide
whether to delete it or commission a real habenula/dopamine signed-PE review in its place.

### Effect on the audit, and what remains

Re-run after the repairs (`--fetch` then `--report`), against `validate_literature.py` reporting
**0 findings of 2189**:

| bucket | before | after | note |
|---|---|---|---|
| (b) first author differs | 8 | **5** | the 4 residual besides `hyman2010` are all documented false positives (Høydal/Rodríguez diacritics, Cushing name change, CURL author order) |
| (c) identifier does not resolve | 13 | **11** | both Bekoff 404s cleared; the placeholder DOI retained on purpose |
| (a) year mismatch | 31 | 31 | untouched, per item 4 |

So the only remaining bucket-(b) entry that is *not* a known false positive is `hyman2010`, and the
only remaining bucket-(c) entry that is not benign is the habenula placeholder — both now carrying an
open governance flag rather than sitting unattributed. **Five open flags came out of the two audit
chips together: GFLAG-0027 (item 0, MECH-186), 0028, 0029, 0030 and 0031.**
