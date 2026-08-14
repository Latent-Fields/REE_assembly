# Literature identifier cross-resolution — findings and the pull-time gate, 2026-08-14

**Status: FINDINGS REPORT. All 7 findings below HAVE been repaired (REE_assembly `b22155a885`),
provenance only — no `confidence`, `evidence_direction`, `mapping` or `claim_ids_tested` field was
touched anywhere in this work. The cross-resolution check now reports 0 over the whole corpus.**

Chip: `chip-20260814-lit-identifier-verification-gate`, extended by
`chip-20260814-lit-doi-only-pmid-crosswalk` and `chip-20260814-lit-gate-secondary-identifiers`
(see the two closing sections).
Tool: `scripts/verify_literature_identifiers.py` — `--cross-check` (DOI<->PMID sweep),
`--doi-crosswalk` (the other direction), `--secondary-check` (arxiv_id / pmc / isbn),
`--paths` (the gate).
Tests: `scripts/test_verify_literature_identifiers.py` (213, time-independent, offline).
Wired into: `scripts/precommit_literature.sh` as stage 2.

This implements both recommendations of
[`literature_bibliographic_accuracy_audit_2026-08-14.md`](literature_bibliographic_accuracy_audit_2026-08-14.md):
recommendation 1 is the cross-resolution sweep below, recommendation 2 is the commit gate.

---

## Why a third checker, and what it can say that the audit cannot

There are now four literature checkers and none of them can find another's findings:

| tool | question | run by |
|---|---|---|
| `validate_literature.py` | does the record use the declared keys with the declared types, and do its filesystem pointers resolve? | commit gate, stage 1 |
| `audit_literature_bibliographic_accuracy.py` | do the declared fields describe the paper the identifier points at? (three axes, reported separately) | a human, by hand |
| `verify_literature_identifiers.py` | is the identifier **conclusively** wrong? | commit gate, stage 2 |
| `audit_literature_duplicate_entries.py` | is one study entered twice? | report only |

The audit cannot be the gate, and this is the load-bearing design point. Its output is a *flag for a
human* ("year mismatch, author agrees"), it has a documented false-positive list, and it carries a
residue of known-unrepairable records — so `--exit-nonzero` on the commit path would fire on ordinary
work and get switched off, which is strictly worse than no gate. Same reasoning, and the same
convention, as `audit_literature_schema.py`. This tool exists to hold the subset of that evidence
which is **conclusive**, and to refuse only on that.

**"Conclusive" means: needing no external notion of what the record *should* say.** When a record
carries both a DOI and a PMID, the two can be resolved against each other, and a disagreement proves
one of them is wrong without anyone deciding which paper was intended. 491 of the 2072
identifier-carrying records carry both.

---

## The sweep: 491 both-identifier records, 7 defects

Two independent routes, because neither subsumes the other:

1. **`doi_pmid_mismatch`** — PubMed's own `articleids` for the declared PMID names a different DOI.
   This is the direct crosswalk and the strongest signal available. It is also the only route that
   catches a wrong identifier whose **title is verbatim correct** (`mech_061 michelet2007`: declared
   title and PubMed title agree word for word, and the DOI is still wrong).
2. **`crossview_title_mismatch`** — both identifiers resolve and the two authoritative records
   describe different works. Needed because PubMed serves no DOI at all for some PMIDs, so route 1
   structurally cannot fire (`sd_019 craig2003`).

**Raw output was 9 disagreements on route 1. Two were a false positive worth recording**: the legacy
APA double-slash DOI form. PubMed serves `10.1037//0022-006x.64.2.295` for DOIs the corpus records as
`10.1037/0022-006x.64.2.295` (`inv_054 jacobson1996`, `inv_054 tang1999`). That is one identifier
written two ways, not two identifiers — `normalise_doi` collapses slash runs, and this is not
guessable in advance, so it is pinned as a test.

### The 7 real findings

**Four are wrong PMIDs — a defect class the existing audit structurally cannot see.** The audit
resolves the DOI and, once that resolves, never consults the PMID. So a record with a good DOI and a
hallucinated PMID is invisible to it, and all four of these sat in a corpus the audit had just
reported clean:

| record | wrong PMID | resolves to | correct |
|---|---|---|---|
| `arc_036 berridge2009` | `19336238` | a *different* Berridge 2009 (Physiol Behav) | `19162544` |
| `mech_295 smith2011` | `21525253` | a J Nutr study on high-oleic ground beef | `21670308` |
| `mech_317 martiros2018` | `29452904` | a plant-biology review on leaf nodule symbiosis | `29429614` |
| `q_033 ferrand2022` | `35456302` | a cervical-spine paper in the same journal *and issue* | `35456294` |

**Two are hallucinated DOIs recovered from the record's own correct PMID** — the shape the audit
predicted this check would catch, and it did:

- `mech_153 schoenbaum2007` — `10.1146/annurev.neuro.30.051606.094479` (404) →
  `10.1196/annals.1401.001`. `venue` was also wrong: *Annual Review of Neuroscience* → **Annals of
  the New York Academy of Sciences** 1121:320-335. The paper, its findings and its relevance to
  MECH-153 are unchanged; only the journal it appeared in was misrecorded.
- `mech_061 michelet2007` — `10.1523/JNEUROSCI.1883-07.2007` (404) →
  `10.1523/JNEUROSCI.4718-06.2007`.

**One had both identifiers wrong, and they disagreed with each other:**

- `sd_019 craig2003` — `doi 10.1038/nrn1153` is *"In This Issue"*, the front-matter item at Nat Rev
  Neurosci 4(6):425; `pmid 12894801` is a French history-of-pharmacy article about the Boulduc
  dynasty of Parisian apothecaries. Neither is a Craig paper. The work is **Craig, "How do you feel?
  Interoception: the sense of the physiological condition of the body", Nature Reviews Neuroscience
  3(8):655-666 (2002)**, `10.1038/nrn894`, PMID `12154366`.

  This one needed the summary read, not just the identifiers resolved. The declared title is the real
  title with its *"How do you feel?"* opening dropped — which makes it a verbatim match for a
  **different** Craig review (*Current Opinion in Neurobiology* 13:500-505, 2003), and the entry_id
  says `craig2003`. What settles it is the summary's own citation line, which gives issue 8 and pages
  655-666: those are the 2002 NRN paper's exactly, and the Curr Opin Neurobiol paper's are 500-505.
  The content agrees (lamina I → VMpo → insula, "the material me", the global emotional moment), and
  so does the confidence reasoning, which names *Nature Reviews Neuroscience*. `title`, `year`,
  `doi`, `pmid` and the locators were corrected. **`entry_id` was deliberately not renamed off
  `craig2003`** — the indexer keys on it and `claim_evidence.v1.json` carries it, so renaming is a
  separate and riskier change than a provenance fix.

**Method for every repair**: resolve both identifiers, compare each against the record's own declared
title and authors to establish which side is right, recover the other from the correct one, then
**verify by round-trip** — the replacement is accepted only if the PubMed record's own `articleids`
DOI equals the DOI being kept. A `PROVENANCE NOTE` block was added to each of the 7 `summary.md`
files, per the v1 schema convention that provenance prose lives there. Two summaries also asserted a
stale identifier **in the prose** (`mech_317`'s "PMID 29452904", `sd_019`'s citation line and DOI
link) and were corrected there too: a `record.json`-only fix leaves the wrong identifier in the text
a human actually reads.

### Note the near-miss shape on the PMIDs

`35456302` vs `35456294`; `29452904` vs `29429614`; `21525253` vs `21670308`. This is the same
signature the audit documented for DOIs — an identifier generated from plausibility rather than
looked up — and it now has a second, independent instance class. Both halves of a citation are being
confabulated, not just the DOI.

---

## The gate: `precommit_literature.sh` stage 2

The only measure that stops the defect **entering**. One API call per new record at pull time, against
2073 at audit time. Scoped to the records the commit touches (`--paths`), never the whole corpus, so a
future backlog cannot wedge an unrelated commit.

**Four verdicts block. Nothing else does.**

| verdict | needs network | what it proves |
|---|---|---|
| `placeholder_identifier` | no | `10.0000/example-doi` and friends — the record names no verifiable work |
| `doi_pmid_mismatch` | yes | the record's own two identifiers contradict each other |
| `crossview_title_mismatch` | yes | both identifiers resolve, to different works |
| `identifier_names_a_different_paper` | yes | declared title **and** declared first author both disagree |

**The conjunction in the last one is what makes it gate-grade**, and it was measured rather than
assumed. Evaluated against the 21 records whose DOI the audit had already proven wrong, using each
record's *pre-repair* `source` block (the diffs of `461da94faa` and `ded51143ff`): fires on **21 of
21**, highest title ratio seen 0.47. Either axis alone is a documented false positive of the audit,
so either alone would fire on correct records.

### Whole-corpus gate baseline: 1 record of 2072

Measured after the repairs, with every verdict enabled:

```
1 live verdict, over 1 record  -- the habenula placeholder DOI (GFLAG-0031)
1 waived                      -- hyman2010 (GFLAG-0029)
```

That measurement, not optimism, is why stage 2 **blocks by default** — it is the same flip condition
`precommit_literature.sh` records for its own stage 1 ("once the corpus baseline is at zero"). It is a
property of the corpus rather than of the code, so re-measure before assuming it still holds.

> **Denominator moved, verdict did not.** The scoping fix later on this page brought 7 secondary-only
> records into scope, so the *current* gate figure is **1 of 2079** — same single live verdict, same
> single waiver. Re-measured 2026-08-14 after the cache fix; see "Baselines re-measured, and
> unchanged" at the end. `--cross-check` still prints 2072 by design.

The habenula placeholder is deliberately **not** waived. It is a synthetic record that cites no real
work, so a commit touching it ought to stop and read the flag — and it costs nothing in practice,
because disposing of the entry means *deleting* it, and a deleted `record.json` resolves to no target
at all. The gate cannot obstruct its own remedy.

### Failing open is a design requirement, not a concession

Stage 2 is the only commit gate in this repo that needs the network. It treats **every** non-verdict
condition as a pass and says so: unreachable API, HTTP error, unresolvable identifier (11 records
legitimately carry one — ACM handles, pre-1997 articles Crossref never indexed), a record declaring no
title or no authors, and the per-invocation network budget being spent. Whatever went unchecked is
**named**, never silently dropped. It gets a short socket timeout and a bounded budget so a bulk pull
cannot turn `git commit` into a three-minute wait, and cached identifiers are free, so re-committing
an unchanged record costs nothing. A gate that blocks a commit because NCBI was rate-limiting is a
gate that gets uninstalled by lunchtime.

Escape hatches, both temporary and both worth explaining in the commit message:
`REE_LITERATURE_IDENTIFIER_GATE_BLOCK=0` (report only), `REE_LITERATURE_IDENTIFIER_GATE=0` (skip
stage 2 entirely, e.g. a box with no outbound network).

---

## Two defects found in the checker itself, and one in the repo

Recorded because both are the kind of thing that passes review and then quietly costs coverage.

**1. A live false positive from a threshold, in the very case the docstring cited.** `titles_agree`
accepts containment in either direction, to absorb the audit's documented subtitle-truncation false
positive (Crossref stores only the main title for many publishers). Its floor was 20 normalised
characters — and `norm_title("The Unengaged Mind")` is **18**, so containment was refused, the pair
fell through to a 0.48 ratio, and `arc_067 unengaged_mind_eastwood2012` produced a
`crossview_title_mismatch` on a perfectly correct record. The audit's own worked example, *"The p
Factor"*, is 12 characters and failed the same way.

Fixed by splitting containment into two forms: **affix** (the shorter title is a whole-word prefix or
suffix of the longer — the shape a dropped subtitle or a prepended section heading actually takes)
trusted from 12 characters, and free **substring** keeping the 20-character floor. Re-measured A/B
over the 21 pre-repair true positives: **21/21 still fire**, and three false positives stop. Short
prefixes stay rejected by the floor (*"Pain"* in *"Pain and the Brain"*, *"Learning"* in *"Learning to
see the wood for the trees"*), and whole-word matching is required, so *"The p Factor"* does not match
*"The p Factorial Design"*. All of those are now tests.

**2. Two of the three waivers were already dead.** They covered the book-chapter DOIs
`10.1163/156853995X00822` and `10.1163/156853995X00101` on the audit's then-open "needs an edition
judgement" reading. `ec4467bcf4` settled both the other way — neither work has a chapter-level DOI at
all, so both records now carry `doi: null` — and a waiver keyed on a DOI *value* that no longer
appears anywhere can never match again. Removed. **This is the value-keying working as intended, not a
regression**: keying on the entry path alone would have silently absorbed the *next* wrong identifier
written into those records, which is exactly what a waiver must not do. Pinned by
`test_waiver_does_not_cover_a_different_identifier_value`.

**3. `origin/master` carried a committed importer for an untracked module.**
`scripts/audit_literature_duplicate_entries.py` landed with `import verify_literature_identifiers as
ident`, while that module existed only as an **untracked file** in the shared Mac checkout, left there
by a dead earlier attempt of this chip. Any fresh clone or cloud worker therefore `ImportError`ed on
the duplicate-entry scan. Landed as `5446e883b2`, before any of the follow-up work, because an absent
module is strictly worse than an imperfect one. Worth noting as a shape: an untracked file in a shared
checkout is indistinguishable from a tracked one to everything except git, so a sibling session can
build on it and land a dependency that only works on that one machine.

---

## The crosswalk run the other way: 1579 DOI-only records

Chip: `chip-20260814-lit-doi-only-pmid-crosswalk`, the first of the two follow-ups listed below,
now done. Mode: `verify_literature_identifiers.py --doi-crosswalk`. 1413 esearch calls at 2 req/s
against `esearch.fcgi?term=<doi>[AID]`, plus a batched esummary pass; every response cached under
`~/lit_bib_cache/pubmed_aid`, so the sweep is a one-off and a re-run is free.

Everything above reaches only the records carrying **both** identifiers. This asks the same question
from the other end — *which PMID does PubMed hold for this DOI?* — and is the only route that reaches
the 1579 records carrying a DOI and no PMID, for which routes 1 and 2 have nothing to cross-resolve
against.

**Be clear about what class this is in.** The comparison it enables is against the record's own
declared title and first author, so it is **verdict 3's shape, not verdict 1's** — it is not
record-internal, and it is not conclusive in the sense the top of this document defines. What it
genuinely adds over verdict 3 is a *second, independent authoritative view* of the same DOI, reaching
the cases where Crossref and doi.org resolve nothing at all.

### What the sweep found

| bucket | n | what it means |
|---|---|---|
| `agrees` | 1409 | PubMed's record for this DOI describes the work the entry declares |
| `not_in_pubmed` | 165 | **the common case, not a finding** — arXiv, ML venues, book chapters |
| `truncated_query` | 3 | PubMed searched only a *fragment* of the DOI (see below) |
| `placeholder` | 1 | the habenula record, GFLAG-0031, already reported by verdict 4 |
| `names_a_different_paper` | 1 | `arc_032 hyman2010` — **waived, GFLAG-0029** |

**0 live findings. No new defect exists in the 1579 DOI-only records.** The single hit is hyman2010,
which the crosswalk re-derived *independently* of the route that first found it: PubMed maps
`10.1002/hipo.20709` to pmid `19743303`, Christie, *"Exercising some control over the hippocampus"* —
the same wrong paper GFLAG-0029 already records, reached by a different question. That is a positive
control for the check working, not a new problem.

The 1409 confirmations are the actual product. Those records had never been checked against PubMed at
all, and each is now positively corroborated by a source independent of the one the audit used.

### PubMed truncates some `[AID]` queries, and one of them nearly fabricated a mapping

Not guessable in advance, and worth the same status as the legacy APA double-slash form above.
`[AID]` is a tokenised **phrase** search, and PubMed sometimes translates a DOI to only a fragment of
itself, dropping every leading token:

```
10.1207/s15516709cog1401_3  ->  "3"[Publisher ID]         8446 hits
10.24963/ijcai.2023/454     ->  "454"[Publisher ID]       1070 hits
10.2307/1130099             ->  "1130099"[Publisher ID]      1 hit
```

The third is the dangerous shape: a truncated query that happens to be **unique** returns one
confident-looking PMID for an unrelated paper — here `36860389`, a 2023 *Front Public Health* article,
for a Diamond 1985 child-development study. A `count > 1` rule does not catch it, and neither does
requiring the `[Publisher ID]` marker.

Two independent guards now stop it, and it is worth keeping both because they fail differently:

1. **Round-trip confirmation** — PubMed's own `articleids` for the returned PMID must name the DOI that
   was asked about. This caught the Diamond case live, before the fidelity guard existed, and it is
   what makes any hit trustworthy at all.
2. **Query fidelity** (`aid_query_is_faithful`) — the translated phrase must tokenise to exactly the
   DOI's own tokens. This names the mechanism instead of absorbing it, and it also covers the two
   many-hit cases that the round trip would only have reported as "ambiguous".

Both fail **open** — the mapping is refused, never asserted — so a future change in PubMed's
normalisation costs coverage rather than correctness.

### Two decisions taken against the obvious reading, both on measurement

**1. The verdict is NOT wired into the commit gate.** Its whole-corpus baseline is 0 live findings,
which is clean enough to block on — cleaner than the 1-of-2072 the gate already blocks on. It stays
off for a different reason: its **marginal** coverage over verdict 3 is *also* zero. The blind spot it
would uniquely cover is "the DOI resolves through neither Crossref nor doi.org", and all **10** such
records in this corpus turn out to be absent from PubMed as well. So wiring it in would spend up to two
extra network calls per record against a budget-bounded gate, buy nothing, and take that budget out of
the coverage of the checks that do fire. Pinned by `TestCrosswalkIsNotOnTheGatePath`, whose docstring
carries this reasoning so a later reader does not "fix" it. **Re-measure before assuming it holds** —
one future record whose DOI is unresolvable but PubMed-indexed flips the arithmetic.

**2. The 1409 confirmed PMIDs were NOT bulk-written into the records**, though the chip proposed
considering it. Three reasons, in order of weight:

- **A derived pair is not independent corroboration, and it makes `doi_pmid_mismatch` VACUOUS on
  exactly those records.** That check asks whether a record's two identifiers contradict each other. A
  PMID obtained *from* the DOI and round-trip-verified *against* the DOI cannot contradict it — by
  construction, forever. Writing 1409 of them would not "bring those records inside the cheap existing
  check"; it would enlarge the both-identifier population with pairs that can never fail, diluting the
  one corpus statistic the gate's blocking default rests on. Detectability would not fall (verdict 3
  is unaffected), but the number would stop meaning what it says.
- **The narrow, genuinely-valuable subset is empty.** The one backfill with a real coverage argument is
  the record whose DOI resolves nowhere else, which a stored PMID would return to the reach of every
  networked verdict. Measured: **0 such records**, for the same reason decision 1 came out as it did.
- **Churn.** ~1409 `record.json` files plus a `PROVENANCE NOTE` in each `summary.md` is ~2800 files
  against CLAUDE.md's "Narrow Edits Only", for a change whose measured value is the two points above.

The capability is implemented, tested and dry-runnable — `--write-pmid {none,unresolvable,all}`,
defaulting to `none` — so a later governance decision can act on it deliberately and scoped. It writes
only where the round trip confirmed the mapping **and** the title agrees; a record whose title
disagrees is never given a PMID, because that would bury a wrong DOI behind a self-consistent-looking
pair.

### One repair, from the hand-triage queue rather than the verdict

`homeostatic_override brown2022` surfaced in the "one axis disagrees" bucket — title disagreed, first
author agreed — which is not a finding by design, and is exactly why that bucket is printed rather than
folded into `agrees`.

The DOI `10.1093/braincomms/fcac229` was never in question; Crossref and PubMed independently name the
same work. The record's *description* of it was wrong. The declared title, *"Hypothalamic volume is
associated with body mass index in patients with Prader-Labhart-Willi syndrome"*, matches **no** PubMed
record (exact-title search, count 0) — a plausible-sounding paraphrase of the paper's central result
rather than any real paper's title. The declared author list was a garble: `Brown` and `Manning KE` are
genuine, `Fletcher` and `Holland` were missing, and `Anna Manning` / `Anthony P Goldstone` appear on no
version of it.

**Repaired as provenance, not flagged**, because the evidence is unaffected and was checked rather than
assumed: the abstract of PMID `36147452` states the summary's key claim directly — *"Lower whole
hypothalamus volume was significantly associated with higher body mass index in Prader-Willi syndrome
(P < 0.05)"*. `title`, `authors` and the summary's own citation line were corrected and `pmid` added;
no `confidence`, `evidence_direction`, `mapping` or `claim_ids_tested` field was touched. Authors are
recorded in PubMed's own form rather than expanded to full given names — inventing an expansion is the
same confabulation class the repair removes.

This is a **third** instance of the near-miss signature, and the first where the *title* is the
confabulated half while the identifier is sound. The audit documented it for DOIs; the cross-resolution
sweep found it for PMIDs; it is now also attested for the descriptive fields.

---

## What remains open

Nothing from this chip. The two open flags this touches were both raised earlier and are unchanged:

- **GFLAG-0029** (`arc_032 hyman2010`) — every identifier wrong and mutually inconsistent, and the
  content the summary describes is Jones & Wilson (2005), not either candidate Hyman paper. Writing an
  identifier would change the *evidence*, not the provenance. Waived here so it does not block, and
  the whole-corpus audit keeps reporting it, which is correct.
- **GFLAG-0031** (`habenula_da_signed_pe_review`) — a fully synthetic record contributing to MECH-053
  and MECH-054 in `claim_evidence.v1.json`. Deliberately unwaived, so it blocks.

**DONE (2026-08-14, `chip-20260814-lit-gate-secondary-identifiers`):** the gate now covers
`arxiv_id`, `pmc` and `isbn` — see the section below.

**DONE (2026-08-14, `chip-20260814-lit-doi-only-pmid-crosswalk`):** extending the crosswalk to the
1579 DOI-only records — see the section above. The motivating hope, that it would catch a hallucinated
DOI whose *title happens to be right* on a record with no PMID to cross-resolve against, found **no
such record**: 0 live findings, 1409 positive confirmations, and one title-side defect from the
hand-triage queue rather than from the verdict.

---

## The secondary identifiers: `arxiv_id`, `pmc`, `isbn`

Chip: `chip-20260814-lit-gate-secondary-identifiers`, the second of the two follow-ups listed above,
now done. Mode: `verify_literature_identifiers.py --secondary-check`. Code:
REE_assembly `44bb62c9a8`.

The v1 schema declares five resolvable identifiers and the gate checked two. So a wrong
`arxiv_id`, `pmc` or `isbn` entered the corpus unnoticed — precisely the gap the doi/pmid work had
just closed for the other two, left open on three fields that are no less resolvable.

**The population, and why it decided the design.** 90 records of 2189 carry one of the three:

| identifier | n | also carries | reachable by a crosswalk? |
|---|---|---|---|
| `pmc` | 80 | **all 80** carry a `pmid` | yes — PubMed's `articleids` |
| `arxiv_id` | 5 | 3 carry a DataCite arXiv DOI | yes, for those 3 — the DOI *encodes* the id |
| `isbn` | 5 | none carries a doi or pmid | no |

Note the first row is not a lucky coincidence to be relied on; it is a fact about *this* corpus that
`--secondary-check` re-measures. But while it holds, the pmc check is free.

### Three gating verdicts, all crosswalk-first, all measured at 0

The chip's instruction was to prefer the crosswalk shape — a contradiction between two of the
record's *own* identifiers, conclusive with no title comparison at all, like `doi_pmid_mismatch` —
and reach for title/author comparison only where no crosswalk exists. That turned out to be
available for **both** gating axes, which is why adding three identifiers did **not** add three
lookups per record:

| verdict | baseline | network | what it proves |
|---|---|---|---|
| `pmc_pmid_mismatch` | **0 of 80** | **none** | PubMed's own `articleids` for the declared pmid name a different PMC id |
| `arxiv_doi_mismatch` | **0 of 3** | **none** | `10.48550/arXiv.<id>` *is* the arXiv id, and it disagrees with the declared one |
| `arxiv_names_a_different_paper` | **0 of 5** | 1 call, for 2 records | verdict 3's conjunction against the arXiv API |
| `malformed_identifier` (isbn) | **0 of 5** | **none** | the ISBN's own check digit does not verify |

`pmc_pmid_mismatch` costs nothing because the crosswalk is *inside the esummary record verdict 1 has
already fetched* — the `pmc` and `pmcid` fields sit alongside the `doi` field that check reads.
`arxiv_names_a_different_paper` is **skipped entirely** when the record's own arXiv DOI already
confirms the id, which is what takes it from 5 records to 2. A test asserts `resolver.spent == 0` in
both cases, so a later change that quietly starts fetching fails rather than slowing the commit path.

**The near-miss defect class reaches arXiv too**, which is the reason verdict 7 exists at all rather
than being waved off as a 5-record population: `1703.04977` is Kendall & Gal, and `1703.04978` is
*"Lectures on EW Standard Model"* by Godbole. A confabulated final digit resolves to a real,
different paper here exactly as it does for a DOI. That pair is a test fixture.

### ISBN: a measured "not worth gating", which is the finding rather than a shortfall

`isbn_names_a_different_work` is implemented, tested and **report-only**. The reason is a property
of the identifier, not of the comparison: **an ISBN names a VOLUME, not a chapter.** So a *correct*
ISBN on a chapter record resolves to a different title by different people — the volume's **editors**
— and trips verdict 3's conjunction on a record with nothing wrong with it.

Measured per record, with the venue disjunction disabled:

| record | title | first author | outcome |
|---|---|---|---|
| `arc_026 frankfurt2004` | agrees | agrees | agrees |
| `inv_029 frankfurt1999` | agrees | agrees | agrees |
| `mech_102 axelrod1984` | agrees | agrees | agrees (hyphenated ISBN, normalised) |
| `q035_arc049 murray_trevarthen_1985` | **disagrees** | **disagrees** | **FIRES — and the record is correct** |
| `arc_026 bratman1987` | — | — | OpenLibrary holds no such ISBN → fails open |

The same conjunction measures **0 false positives in 2060 records** on the DOI path and **1 in 5**
here. The declared title is the chapter (*"Emotional regulation of interactions between
two-month-olds and their mothers"*); ISBN 9780893912314 is *"Social perception in infants"*, edited
by Field & Fox.

What rescues it is accepting the declared `venue` as an alternative title — a chapter record's
`venue` is conventionally the containing volume. That works, and it is shipped, but it is **a rule
written from the single record it rescues**, which is exactly what CLAUDE.md's held-out check warns
against putting on a commit gate. `venue` is also not schema-enforced, so the rescue is not general
(a test pins that a chapter record with no `venue` is *not* rescued). And coverage is weak from the
other end: 1 of the 5 is absent from OpenLibrary entirely.

So the comparison reports and does not block. **Flip condition: >= 15 ISBN-carrying records, of which
the chapter-shaped ones are separable by a rule that was not written from them.** The network-free
half — the checksum — *does* gate, because it has none of this trouble.

This is the same treatment, and the same standing rule, as `doi_crosswalk_names_a_different_paper`
above: a verdict may be implemented and left off the gate path with its reason recorded, rather than
being either shipped blocking or dropped.

### `check_pmc_declared_vs_identifier` is implemented and deliberately unwired, for a different reason

The chip named `db=pmc` esummary as the pmc authority, and it is implemented against it. But it
reaches **0 records**: all 80 pmc-carrying records also carry a pmid, so `pmc_pmid_mismatch` already
covers every one of them *conclusively and for free*, while this would spend an esummary call per
record to reach a strictly weaker (verdict-3 shaped, not record-internal) conclusion. It is tested
so the coverage exists the day a pmc-only record arrives. Same arithmetic as the DOI crosswalk's:
implemented, 0 marginal coverage, therefore off the gate — re-measure, do not assume.

### A scoping gap the new verdicts exposed, which was worse than the missing checks

`collect_scoped_targets` and `collect_all_targets` both filtered on **doi/pmid only**. So a record
whose *only* identifier was an `arxiv_id` or an `isbn` — **7 records** in this corpus — was not a
gate target at all: the gate printed its `OK (0 records with an identifier in scope)` line having
checked **nothing**, which reads as a pass. Both collectors now take a record carrying **any** of
the five. `collect_all_targets(keys=("doi", "pmid"))` preserves the doi/pmid population so
`--cross-check` still prints the 2072 this document quotes.

`audit_literature_bibliographic_accuracy.collect_targets` was deliberately **left bit-identical** —
its false-positive counts are quoted by number in the 2026-08-14 audit and must stay reproducible —
so the wider scan lives in the verifier instead of being pushed down into the audit module.

### The fail-open contract, re-verified rather than assumed

A third API in the commit path is a third way to be unreachable, and that was the constraint to
respect rather than the box to tick. It was answered structurally: **OpenLibrary is never contacted
on the gate path at all** (verdict 8 is report-only), and two of the three gating axes make no call.
Only arXiv is added to the wire, for the records whose id no DOI confirms, and it carries its own
per-invocation cap (`ARXIV_FETCH_BUDGET`, 8) on top of the shared `--network-budget`, because arXiv's
request-rate guidance must not become something `git commit` inherits.

Verified live against the real corpus rather than only in fixtures:

```
budget exhausted   -> OK (5 records checked, 0 findings) (4 NOT checked: network budget spent)  exit 0
API unreachable    -> OK (5 records checked, 0 findings) (2 NOT checked: arxiv fetch failed)    exit 0
13 secondary records, warm cache                                                          0.084s
```

Both name what went unchecked, and both exit 0 under `--exit-nonzero`. An arXiv answer about a
*different* id than the one asked for is refused rather than trusted (`arxiv_entry_is_faithful`,
the twin of the PubMed-side `aid_query_is_faithful` that caught the Diamond case above) — it fails
open, so a future change in how arXiv echoes ids costs coverage rather than correctness.

### Tests

143 new (213 in `scripts/test_verify_literature_identifiers.py`, 314 across the four literature
suites), offline and time-independent. **Roughly half are negative controls**, one per false-positive
shape each new axis brings: a PubMed record not in PMC at all (the common case across PubMed); an
ordinary journal DOI sitting beside an `arxiv_id`, which is the *normal* shape for a published
preprint and must never read as a crosswalk; a version suffix; preprint author order (the CURL case,
likelier on this axis than on the DOI one since the arXiv version *is* the preprint); an
initials-only declared author against arXiv's full given names; and the ISBN chapter case, asserted
in both directions — that it *would* fire without the venue disjunction, and that it does not with it.

Five mutations of the implementation were each confirmed to fail a specific new test (venue
disjunction removed; pmc verdict made to fetch; scoped collection reverted to doi/pmid; arXiv
fidelity guard removed; the doi-confirms shortcut removed), so the suite is differential rather than
merely green.

## The shared cache could persist a transport failure as an answer (fixed 2026-08-14)

Found while extending the gate to the secondary identifiers, and left unfixed there on purpose: the
audit module's caching is what its published false-positive counts are measured through, so changing
it belonged in its own careful commit rather than a drive-by.

`fetch_crossref`, `fetch_doiorg` and `fetch_pubmed` each ended in an **unconditional**
`path.write_text(json.dumps(payload))` that ran for every exception, including a bare transport
failure. Every one of them also returns early on `path.exists()` and never re-asks. So an HTTP 429
from NCBI's rate limiter, a 503, or a dropped connection was written into `~/lit_bib_cache` as a
**permanent verdict about that identifier**, on every box that holds the cache, for every mode of
every literature checker that reads it. `doi_view` and `pubmed_record` then read `ok is False` and
returned `unresolvable` forever, and the gate failed open for that record **silently** — the record
was not even named in `resolver.skipped`, because from the resolver's point of view the question had
been asked and answered.

Reproduced before fixing, against a dead proxy over the five arxiv-bearing records: six cache entries
written, all `{"ok": false, "error": "URLError: ... Connection refused"}`, against three real and
perfectly good DOIs — and the run reported only *two* identifiers unchecked, silently swallowing the
three DOIs into `unresolvable`. Post-fix, the same command writes **nothing** and names all five.

The fix is the split `fetch_pubmed_aid` already documented and the 2026-08-14 secondary fetchers
already followed — cache an ANSWER, return a TRANSPORT failure to the caller uncached — applied to
the three originals. The answer sets are **per-endpoint**, because "which HTTP status is an answer"
is a fact about each API, not a global:

| endpoint | HTTP statuses that are an ANSWER | why |
|---|---|---|
| Crossref | `404` | "I do not know this DOI" is a real answer, and caching it is what stops every dead DOI being re-fetched on every sweep |
| doi.org | `404` | conclusive: doi.org negotiates against every registration agency, so "no such DOI" here means registered nowhere |
| NCBI eutils | *(none)* | eutils does not 404 an unknown id — it answers `200` with an `error` field, already cached as `not_found`. A 404 here means the request or the service is wrong, not the PMID |

`401`/`403` are **not** answers anywhere: none of these endpoints requires authentication, so a
401/403 is about the requester — rate limiting dressed as a 403, a WAF, an intercepting proxy —
never about the identifier. `410` is excluded on the asymmetry that decides every borderline case
here: being wrong in the not-an-answer direction costs one re-fetch; being wrong in the other
direction is silent, permanent loss of coverage.

A transport failure is now also **named** rather than collapsed into `unresolvable`. Both still fail
open, so no verdict changes — what changes is what the run *says*. `unresolvable` asserts the
question was asked and answered, and a record dropped from coverage by a 429 must not be able to
hide inside that word. This could not be written for DOIs until the fetchers stopped caching the
failure, since until then it was indistinguishable from a real negative on the very next read.

### The live cache was clean: 0 poisoned entries of 4477

Audited before deciding anything, because a large count would have been the finding and would have
changed what the baselines below mean:

```
crossref     1635   1552 ok    83 not-ok   -- all http_404
doiorg         83     65 ok    18 not-ok   -- all http_404
pubmed       1467   1467 ok     0 not-ok
arxiv           2      2 ok     0 not-ok
openlibrary     5      4 ok     1 not-ok   -- not_found
pubmed_aid   1285   1285 ok     0 not-ok
```

Every not-ok entry is a genuine answer (`http_404` for the two DOI endpoints, `not_found` for the
200-shaped ones). Nothing was deleted, and nothing needed to be. **This is one box** (`ree-cloud-5`);
the same audit is worth re-running anywhere else that holds a `lit_bib_cache`, and it is a two-line
scan over `ok is false and error not in ("http_404", "not_found")`.

### Baselines re-measured, and unchanged

Offline, against a copy of the warm cache:

```
gate (--paths, whole corpus) : 1 conclusive finding in 1 of 2079 records, 1 waived
--cross-check                : 2072 records, 492 carrying both, 0 conclusive disagreements
--secondary-check            : 90 in scope, 0 gating, 0 report-only
```

Same live verdict (the habenula placeholder) and same waiver (hyman2010) as when the gate's blocking
default was set. **The gate denominator is 2079, not the 2072 quoted above** — the two differ by
exactly the 7 secondary-only records the scoping fix brought into scope, and `--cross-check` still
prints 2072 because it preserves the doi/pmid population deliberately.

### The audit's own output is bit-identical on a warm cache

The constraint on this change was that the audit must keep reporting what its documented
false-positive counts say it reports. Verified rather than asserted: pre-fix and post-fix modules run
against two copies of the same warm cache produce **byte-identical** `--json` findings and identical
stdout (the only textual difference is the `--json` path each was told to write), neither run mutates
its cache, and `--fetch` on that cache reports `0 uncached identifiers / cache is complete` — so on a
warm cache the changed code paths are never entered at all.

### Tests for the split

21 in `TestPrimaryFetcherCaching` and `TestTransportFailureIsReportedNotSilent`, offline and
time-independent, copying the shape of `TestFetchPubmedAidCaching` and `TestSecondaryFetchers`.
**Differential, not merely green**: run against the pre-fix modules, 13 of the 21 fail. The 8 that
pass on both are the negative controls, and they are the half that matters most — a real 404 IS
cached, a success IS cached, eutils' `not_found` IS cached, a cached identifier still returns `None`
without re-fetching, and a DOI both resolvers genuinely do not know is still `unresolvable` and still
absent from `skipped`. Refusing to cache a real 404 would be its own regression; the bug was never
"it caches failures", it was "it cannot tell the two apart".
