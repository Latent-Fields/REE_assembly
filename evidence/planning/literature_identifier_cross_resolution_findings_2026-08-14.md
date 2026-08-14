# Literature identifier cross-resolution — findings and the pull-time gate, 2026-08-14

**Status: FINDINGS REPORT. All 7 findings below HAVE been repaired (REE_assembly `b22155a885`),
provenance only — no `confidence`, `evidence_direction`, `mapping` or `claim_ids_tested` field was
touched anywhere in this work. The cross-resolution check now reports 0 over the whole corpus.**

Chip: `chip-20260814-lit-identifier-verification-gate`.
Tool: `scripts/verify_literature_identifiers.py` (`--cross-check` for the sweep, `--paths` for the gate).
Tests: `scripts/test_verify_literature_identifiers.py` (70, time-independent, offline).
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

## What remains open

Nothing from this chip. The two open flags this touches were both raised earlier and are unchanged:

- **GFLAG-0029** (`arc_032 hyman2010`) — every identifier wrong and mutually inconsistent, and the
  content the summary describes is Jones & Wilson (2005), not either candidate Hyman paper. Writing an
  identifier would change the *evidence*, not the provenance. Waived here so it does not block, and
  the whole-corpus audit keeps reporting it, which is correct.
- **GFLAG-0031** (`habenula_da_signed_pe_review`) — a fully synthetic record contributing to MECH-053
  and MECH-054 in `claim_evidence.v1.json`. Deliberately unwaived, so it blocks.

Two things a later session could usefully do, neither started here:

- **Extend the crosswalk to the 1579 DOI-only records** by asking PubMed for each DOI (`esearch`
  `<doi>[AID]`) and comparing the PMID it returns against the record. That would catch a hallucinated
  DOI whose *title happens to be right* on a record with no PMID to cross-resolve against — the
  `mech_061` shape without the anchor that made `mech_061` repairable. ~1600 esearch calls, one-off.
- **The gate does not yet cover `arxiv_id`, `pmc` or `isbn`.** All three are resolvable and none is
  checked today, so a wrong one enters unnoticed.
