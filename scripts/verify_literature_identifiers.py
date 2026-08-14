#!/usr/bin/env python3
"""Verify that a literature record's IDENTIFIERS name the work the record describes.

This is the third literature checker and the three do not overlap. Know which
one you want before adding anything here:

    validate_literature.py       does the record use the declared keys with the
                                 declared types, and do its filesystem pointers
                                 resolve?  (schema + structure; the commit gate)
    audit_literature_bibliographic_accuracy.py
                                 do the declared fields describe the paper the
                                 identifier points at?  (three axes reported
                                 SEPARATELY for a human to triage; run by hand)
    THIS FILE                    is the identifier itself wrong -- CONCLUSIVELY,
                                 without needing any external notion of what the
                                 record "should" say?  (gate-grade verdicts only)

WHY A THIRD ONE, AND WHY IT HAD TO BE A DIFFERENT SHAPE
-------------------------------------------------------
The 2026-08-14 audit (evidence/planning/literature_bibliographic_accuracy_audit_2026-08-14.md)
found ~2% of the 2073 identifier-carrying records misidentify the work, with one
dominant class: HALLUCINATED NEAR-MISS DOIs. A well-formed DOI, right journal,
right year, final digits altered, resolving to a real but DIFFERENT paper --

    10.1016/j.conb.2010.02.014  recorded for Engel & Fries, beta status quo
    10.1016/j.conb.2010.02.015  the actual paper

-- which is invisible to every syntactic check, because the identifier is valid
and resolves successfully. The corpus grows by automated pull, so the class keeps
arriving.

The audit cannot be the gate. Its output is a FLAG for a human ("year mismatch,
author agrees"), it has a documented false-positive list, and it carries a
residue of known-unrepairable records -- so `--exit-nonzero` on the commit path
would fire on ordinary work and get switched off, which is strictly worse than no
gate. Same reasoning as audit_literature_schema.py, and stated in that audit's
own docstring. So this file exists to hold the subset of that evidence which is
CONCLUSIVE, and to refuse only on that.

THE THREE CONCLUSIVE VERDICTS
-----------------------------
1. ``doi_pmid_mismatch`` -- the record carries BOTH identifiers and PubMed's own
   ``articleids`` for that PMID names a DIFFERENT DOI. Needs no notion of what
   the record should say: the record's two identifiers contradict each other, so
   one of them is wrong. This is the check the audit recommended first, and it is
   the only one that catches a hallucinated DOI whose TITLE happens to be right
   (mech_061_commitment_error_routing_cingulate_michelet2007: declared title and
   PubMed title agree verbatim, and the DOI is still wrong).

2. ``crossview_title_mismatch`` -- both identifiers resolve, and the two
   AUTHORITATIVE records describe different works. Catches the case where PubMed
   serves no DOI at all for the PMID, so verdict 1 cannot fire
   (sd_019_interoception_insula_craig2003: DOI is Craig, *Interoception*; PMID
   12894801 is a French history-of-pharmacy article).

3. ``identifier_names_a_different_paper`` -- one identifier only, and the
   declared title AND the declared first author BOTH disagree with what it
   resolves to. Both axes are required: either alone is a documented false
   positive of the audit (see AVOIDING THE KNOWN FALSE POSITIVES).

plus two that need no network at all:

4. ``placeholder_identifier`` -- ``10.0000/example-doi`` and friends. Cheap,
   syntactic, and there is one in the corpus today.

4b. ``malformed_identifier`` -- an ISBN whose CHECK DIGIT does not verify. Same
   class as a placeholder and equally conclusive: an ISBN that fails its own
   checksum is not an ISBN, so the record names no verifiable work. Costs
   nothing and needs no external notion of what the record should say. Baseline
   0 of the 5 ISBN-carrying records (measured 2026-08-14).

THE SECONDARY IDENTIFIERS -- arxiv_id, pmc, isbn
------------------------------------------------
The v1 schema declares three more resolvable identifiers, and until 2026-08-14
none was checked, so a wrong one entered the corpus unnoticed. Two of the three
are now gate verdicts, and the CHEAPEST AND STRONGEST FORM WAS AVAILABLE FOR
BOTH -- a crosswalk against an authority the gate is already talking to, needing
no title comparison and, for pmc, no extra network call at all:

5. ``pmc_pmid_mismatch`` -- the record carries BOTH ``pmc`` and ``pmid``, and
   PubMed's own ``articleids`` for that PMID names a DIFFERENT PMC id. Exactly
   verdict 1's shape one identifier over: record-internal, conclusive, no notion
   of what the record should say. It reuses the esummary record verdict 1 has
   already fetched, so its marginal network cost is ZERO. All 80 pmc-carrying
   records in this corpus also carry a pmid, so this route reaches every one of
   them; ``check_pmc_declared_vs_identifier`` is the (currently unused, 0
   records) fallback for a future pmc-without-pmid record.

6. ``arxiv_doi_mismatch`` -- the record carries ``arxiv_id`` AND a DataCite arXiv
   DOI (``10.48550/arXiv.<id>``), which ENCODES the arXiv id, and the two
   disagree. Record-internal, conclusive, and needs no network at all -- the
   contradiction is visible in the record's own two fields. 3 of the 5
   arXiv-carrying records are reachable this way.

7. ``arxiv_names_a_different_paper`` -- verdict 3's shape against the arXiv API
   (``export.arxiv.org/api/query?id_list=``), for the arXiv ids that have no
   DOI to cross-resolve against. BOTH axes required, same conjunction and same
   reused comparators as verdict 3. Skipped entirely when verdict 6's crosswalk
   already CONFIRMS the id, which is what keeps the added call count at 2
   records rather than 5. Near-miss arXiv ids resolve to real, different papers
   exactly as near-miss DOIs do -- ``1703.04978`` is *"Lectures on EW Standard
   Model"* where ``1703.04977`` is Kendall & Gal -- so the defect class the audit
   documented for DOIs is reachable here too.

AND TWO THAT ARE DELIBERATELY NOT GATE VERDICTS
-----------------------------------------------
8. ``isbn_names_a_different_work`` (``--secondary-check``) -- report-only, and
   this is a MEASURED "not worth gating" rather than caution. An ISBN identifies
   a VOLUME, not a chapter, so a CORRECT ISBN on a chapter record legitimately
   resolves to a different title and a different first author (the volume's
   EDITORS) -- i.e. it trips verdict 3's conjunction on a record with nothing
   wrong with it. That is not hypothetical: of the 5 ISBN-carrying records,
   ``q035_arc049_murray_trevarthen_1985_double_video`` is exactly this shape
   (declared *"Emotional regulation of interactions between two-month-olds and
   their mothers"* by Murray; ISBN 9780893912314 is *"Social perception in
   infants"* edited by Field & Fox), and it fires. The only thing that rescues
   it is accepting the declared ``venue`` as an alternative title -- a predicate
   fitted to n=1 of a 5-record population, which is precisely what CLAUDE.md's
   held-out rule warns against shipping as a general gate. Coverage is weak from
   the other end too: 1 of the 5 (Bratman 1987) is absent from OpenLibrary
   entirely. So the comparison is implemented, measured and reportable, and it
   stays off the commit path until the population is large enough to say
   something about. FLIP CONDITION: >= 15 ISBN-carrying records, of which the
   chapter-shaped ones are separable by a rule that was not written from them.
   The network-free checksum half (4b) does gate, because it has none of this
   trouble.

9. ``doi_crosswalk_names_a_different_paper`` (``--doi-crosswalk``) -- the
   crosswalk run the OTHER way: ask PubMed which PMID it holds for a DOI
   (``esearch <doi>[AID]``), which is the only route that reaches the 1579
   records carrying a DOI and no PMID. Verdicts 1 and 2 structurally cannot fire
   there, having nothing to cross-resolve against.

   It is NOT in CHECKS_NETWORKED, and that is a MEASURED decision rather than
   caution -- see the crosswalk section of the findings doc. Its whole-corpus
   baseline is 0 live findings (1 waived: hyman2010, GFLAG-0029, which it
   re-derived independently of the route that first found it), which is clean
   enough to block on. What stops it is that its MARGINAL coverage over verdict 3
   is also 0: the blind spot it would uniquely cover is "the DOI resolves through
   neither Crossref nor doi.org", and all 10 such records are absent from PubMed
   too. Wiring it in would spend up to two extra calls per record against a
   budget-bounded gate to buy nothing, taking that budget out of the checks that
   do fire. Re-measure before assuming that still holds; it is a property of the
   corpus, not of this code.

   Its value is as a SWEEP, and there it is substantial: 1409 of 1579 DOI-only
   records were positively confirmed against a second authoritative source that
   had never been consulted for them.

MEASURED, NOT ASSERTED
----------------------
Verdict 3's conjunction was evaluated against the 21 records whose DOI the audit
had already proven wrong, using each record's PRE-REPAIR ``source`` block (the
diffs of REE_assembly 461da94faa and ded51143ff):

    fires on 21 of 21                      -- highest title ratio seen: 0.47
    fires on 0 of the 2060 resolved records of the REPAIRED corpus,
      other than 4 the audit itself lists as unrepairable

Verdict 1 was evaluated across all 491 both-identifier records: 9 disagreements,
of which 2 were the legacy APA double-slash DOI form (``10.1037//0022-006x...``,
normalised away here) and 7 are real. Verdict 2 adds 1 more that verdict 1
structurally cannot see. Those findings are recorded in
evidence/planning/literature_identifier_cross_resolution_findings_2026-08-14.md
and were deliberately NOT waived -- they were repairable, and a waiver list that
absorbs repairable defects is how a gate stops meaning anything. All 7 were
repaired in REE_assembly b22155a885, so ``--cross-check`` now reports 0.

WHAT THE WHOLE-CORPUS GATE BASELINE ACTUALLY IS (measured 2026-08-14, after that
repair, over all 2072 identifier-carrying records with every verdict enabled):

    1 live verdict, over 1 record  -- the habenula placeholder DOI, which is a
                                      synthetic record and SHOULD block
    1 waived                       -- hyman2010, GFLAG-0029

That is the number the commit gate's blocking default rests on, and it is the
same flip condition precommit_literature.sh states for its own schema half. It
is worth re-measuring (the one-liner is in that script's header) before assuming
it still holds, because it is a property of the corpus, not of this code.

The SECONDARY verdicts were measured the same way before any of them was allowed
to block (``--secondary-check``, whole corpus, 2026-08-14, over the 90 records
carrying an arxiv_id, a pmc or an isbn):

    pmc_pmid_mismatch          0 of  80   all 80 also carry a pmid, all 80
                                          cross-resolve, 0 extra network calls
    arxiv_doi_mismatch         0 of   3   (the 3 carrying a DataCite arXiv DOI)
    arxiv_names_a_different_paper
                               0 of   5   all 5 resolve on arXiv, titles and
                                          first authors agree
    malformed_identifier       0 of   5   all 5 ISBN check digits verify
    isbn_names_a_different_work
                               0 of   5   AS SHIPPED -- but 1 of 5 WITHOUT the
                                          venue disjunction, and that 1 is a
                                          false positive on a correct record.
                                          REPORT-ONLY; see verdict 8

Read the last row carefully, because it is the one that decided a design
question rather than confirming one. Measured per record, with the disjunction
disabled:

    frankfurt2004  title_ok=True   author_ok=True    agrees
    frankfurt1999  title_ok=True   author_ok=True    agrees
    axelrod1984    title_ok=True   author_ok=True    agrees  (hyphenated ISBN)
    murray1985     title_ok=FALSE  author_ok=FALSE   FIRES -- and is CORRECT
    bratman1987    unresolvable                      OpenLibrary holds no such
                                                     ISBN -> fails open

So the raw verdict-3 conjunction, which measures 0 false positives in 2060
records on the DOI path, produces ONE in FIVE here -- because the conjunction is
not the problem; the identifier's SEMANTICS are. That is the whole argument for
verdict 8 being report-only, and it is a measurement rather than a worry.

AVOIDING THE KNOWN FALSE POSITIVES -- STRUCTURALLY, NOT BY THRESHOLD
--------------------------------------------------------------------
The audit documents four false-positive modes. Each is handled by a property of
the comparison rather than by a tuned cut-off, because a tuned cut-off fitted to
this corpus is a cut-off that drifts as the corpus grows:

  * SUBTITLE TRUNCATION. Crossref stores only the main title for many
    publishers, so *"The p Factor"* vs *"The p Factor: One General
    Psychopathology Factor..."* scores 0.24. Handled by ``titles_agree``, which
    accepts CONTAINMENT in either direction, not just a ratio. This also fires
    between two authoritative sources (Crossref *"The Unengaged Mind"* vs PubMed
    *"The Unengaged Mind: Defining Boredom in Terms of Attention"*, ratio 0.48),
    which is why verdict 2 needs it as much as verdict 3 does. Both of those
    examples are SHORT, and getting them right needs the affix form of
    containment specifically -- see TITLE_AFFIX_MIN_CHARS, which is where the
    first version of this file got it wrong and shipped a live false positive.
  * NON-ASCII SURNAMES. ``strip_accents`` normalises combining diacritics but
    not distinct letters, so Hoydal/Hoydal and Rodriguez/Rodriguez read as a
    mismatch. Handled by ``fold_special_letters``, which maps the
    non-decomposable Latin letters (o-slash, d-stroke, l-stroke, dotless i, the
    ligatures) onto their ASCII transliterations.
  * AUTHOR NAME CHANGES (Benthem SD -> Sarah D. Cushing, same person) and
    PREPRINT AUTHOR ORDER (CURL is Srinivas-first on arXiv, Laskin-first at
    ICML). Neither is reachable by any name normalisation. Handled by verdict 3
    requiring the TITLE to disagree as well -- in both cases the title is
    verbatim correct, so no verdict fires.

Those four are pinned as tests in scripts/test_verify_literature_identifiers.py
alongside the 21 true positives, so a later widening of any predicate fails on
the false-positive half before it ships.

FAILING OPEN IS A DESIGN REQUIREMENT, NOT A CONCESSION
------------------------------------------------------
On the commit path this check needs the network, which no other commit gate in
this repo does. It therefore treats EVERY non-verdict condition as a pass and
says so: unreachable API, HTTP error, unresolvable identifier, an API record
carrying no title or no author list, a record declaring no title or no authors,
and the per-invocation network budget being spent. A gate that blocks a commit
because NCBI was rate-limiting is a gate that gets uninstalled by lunchtime.
The only thing that blocks is a positive contradiction.

A THIRD API IS A THIRD WAY TO BE UNREACHABLE, so the secondary verdicts were
shaped to add as little of that as possible, and the arithmetic is worth stating
because "one more identifier, one more lookup" was NOT what shipping them cost:

    pmc     0 extra calls   -- the crosswalk is inside the esummary record
                               verdict 1 already fetched
    arxiv   0 extra calls    when a DataCite arXiv DOI confirms the id
            1 extra call     otherwise (2 of the 5 records in this corpus), and
                             capped at ARXIV_FETCH_BUDGET per invocation on top
                             of the shared --network-budget, because arXiv's own
                             guidance is a slow request rate and a bulk pull must
                             not inherit it
    isbn    0 extra calls   -- OpenLibrary is never contacted on the gate path;
                               the ISBN comparison is report-only (verdict 8) and
                               the half that DOES gate is a checksum

Every one of them fails open in the same directions as the rest: an arXiv id
that returns no entry is ``unresolvable``, an arXiv API that will not answer is
``unfetched``, and both are named rather than dropped.

USAGE
-----
    # corpus-wide DOI<->PMID cross-resolution (the audit's recommendation 1)
    verify_literature_identifiers.py --cross-check --fetch
    verify_literature_identifiers.py --cross-check --offline --json out.json

    # the secondary identifiers: arxiv_id, pmc, isbn (the whole-corpus baseline
    # that every one of those verdicts had to clear before it was allowed to block)
    verify_literature_identifiers.py --secondary-check --network-budget 0
    verify_literature_identifiers.py --secondary-check --offline --json out.json

    # the other direction, for the DOI-only records (~1600 esearch calls, cached)
    verify_literature_identifiers.py --doi-crosswalk --network-budget 0
    verify_literature_identifiers.py --doi-crosswalk --offline --json out.json

    # gate: only the records these paths implicate (the audit's recommendation 2)
    verify_literature_identifiers.py --paths evidence/literature/.../record.json
    verify_literature_identifiers.py --paths ... --exit-nonzero      # block

Exit 0 even with findings by default, so it chains -- same convention as
audit_stashes.py, audit_vendored_copies.py and validate_literature.py.
``--exit-nonzero`` is what precommit_literature.sh passes.
"""

import argparse
import json
import os
import re
import socket
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

# Every fetcher, cache path, view normaliser and title/name helper is reused from
# the audit rather than reimplemented. The cache is shared too (~/lit_bib_cache is
# already populated for every DOI in the corpus), so the Crossref half of a
# cross-check costs nothing and a re-commit of an unchanged record costs nothing.
import audit_literature_bibliographic_accuracy as audit  # noqa: E402

REPO = audit.REPO
DEFAULT_CACHE = audit.DEFAULT_CACHE


def set_repo(repo_root):
    """Point this module AND the audit module it borrows from at `repo_root`.

    Both have to move together. ``collect_all_targets`` delegates to
    ``audit.collect_targets``, which globs ``audit.LIT_ROOT`` -- so setting only
    this module's REPO would leave the corpus scan pointed at the real
    REE_assembly checkout while path-relativisation used the override. That is a
    silent wrong answer rather than an error, which is exactly the shape of bug
    the tests exist to catch, so it must not be possible to set one without the
    other.

    Needed for two callers: precommit_literature.sh, which passes the
    git-resolved repo root so both of its stages agree about which checkout they
    are gating (it matters in a `git worktree add` checkout); and the tests,
    which build a throwaway corpus in a tempdir.
    """
    global REPO
    REPO = Path(repo_root).resolve()
    audit.REPO = REPO
    audit.LIT_ROOT = REPO / "evidence" / "literature"
    return REPO

# The audit's own bucket boundary, kept identical so the two tools agree about
# what "the titles disagree" means. Containment (below) is what actually keeps
# this off the false positives; the ratio only has to separate the tail, and the
# measured margin is wide (worst true positive 0.47, best false positive 0.48
# before containment, 1.00 after).
TITLE_RATIO_MIN = 0.60

# Below this many normalised characters, one title being a substring of another
# is coincidence rather than a subtitle relationship ("Pain" in "Pain and the
# Brain"). Titles this short are rare and fall through to the ratio.
TITLE_CONTAINMENT_MIN_CHARS = 20

# The same floor for the AFFIX form -- the shorter title being a whole-word
# PREFIX or SUFFIX of the longer. It is lower than the free-substring floor on
# purpose: a subtitle relationship is always an affix relationship, never a
# mid-string one, so an affix hit is much stronger evidence than a substring hit
# and can be trusted at a shorter length.
#
# 20 was the ONLY floor when this file was written, and it produced a live false
# positive in its own corpus: `norm_title("The Unengaged Mind")` is 18
# characters, so containment was refused and the pair fell through to a 0.48
# ratio -- exactly the subtitle-truncation false positive the docstring above
# says containment exists to prevent, and the very case it names. The audit's
# own documented example ("The p Factor", 12 characters) failed for the same
# reason. Measured A/B over the 21 pre-repair true positives (the diffs of
# 461da94faa and ded51143ff): 21/21 still fire with the affix rule added, and 3
# false positives stop firing. Short-prefix traps stay rejected by the floor
# ("Pain" in "Pain and the Brain", "Learning" in "Learning to see the wood for
# the trees" -- both 4-8 characters, both still False).
TITLE_AFFIX_MIN_CHARS = 12

# Uncached identifiers this invocation is allowed to fetch before it stops
# checking and says what it skipped. A bulk pull commit touching 300 new records
# must not turn `git commit` into a three-minute wait -- that is how a gate gets
# uninstalled. Whatever is skipped is named, never silently dropped.
DEFAULT_NETWORK_BUDGET = 60

# Per-request socket timeout on the gate path. The audit's helpers hardcode 30s,
# which is right for an unattended sweep and much too long in front of a commit.
GATE_SOCKET_TIMEOUT = 8.0

PLACEHOLDER_DOI_PATTERNS = (
    r"^10\.0000/",          # the reserved-for-nothing prefix; one in the corpus
    r"\bexample\b",
    r"\bplaceholder\b",
    r"\btodo\b",
    r"\bxxxx+\b",
    r"^10\.\d{4,9}/$",      # prefix with an empty suffix
)

# Uncached arXiv ids ONE INVOCATION may fetch, on top of the shared
# --network-budget. arXiv's API guidance is a slow request rate (its own
# documentation asks for roughly one request every three seconds when
# harvesting), and a gate must not inherit that: a bulk pull adding 60 arXiv
# records would otherwise spend minutes in front of `git commit`, which is how a
# gate gets uninstalled. Whatever is skipped is NAMED, never silently dropped,
# exactly like the shared budget. This corpus holds 5 arXiv records in total and
# 3 of them need no call at all (verdict 6 confirms them record-internally), so
# the cap is not reached in practice -- it is there for the pull that changes
# that. Set to 0 for "no per-kind cap" (what --secondary-check passes).
ARXIV_FETCH_BUDGET = 8

# One request per second, everywhere. Slower than Crossref's 4/s and slower than
# NCBI's 2/s, because arXiv asks for it; not the full 1-per-3s of the harvesting
# guidance, because ARXIV_FETCH_BUDGET already bounds this to a handful of
# requests rather than a harvest.
ARXIV_RATE = 1.0

# OpenLibrary is only ever reached from --secondary-check (verdict 8 is
# report-only and NOT on the gate path), so this rate is a sweep rate, not a
# commit-path one.
OPENLIBRARY_RATE = 2.0

ARXIV_API_URL = "https://export.arxiv.org/api/query"
ARXIV_CACHE_KIND = "arxiv"
ATOM_NS = "{http://www.w3.org/2005/Atom}"

OPENLIBRARY_URL = "https://openlibrary.org/api/books"
OPENLIBRARY_CACHE_KIND = "openlibrary"

PMC_ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
PMC_CACHE_KIND = "pmc"

# The DataCite DOI prefix arXiv mints for every submission. The suffix IS the
# arXiv id, which is what makes ``arxiv_doi_mismatch`` record-internal.
ARXIV_DOI_RE = re.compile(r"^10\.48550/arxiv\.(.+)$", re.IGNORECASE)


# --------------------------------------------------------------------------
# normalisation deltas over the audit's helpers
#
# These live here rather than in the audit module on purpose. The audit's
# false-positive counts are quoted by number in the 2026-08-14 report, and
# folding these letters into its own comparisons would change those numbers and
# make the report unreproducible. The audit stays bit-identical; this file is
# where the stricter normalisation is applied.


# Latin letters NFKD does not decompose, because the diacritic is part of the
# letter rather than a combining mark. Without these, a perfectly correct ASCII
# transliteration in the record reads as a first-author mismatch -- 2 records in
# the corpus today (Hoydal/Hoydal, Rodriguez/Rodriguez).
SPECIAL_LETTERS = {
    "ø": "o", "Ø": "O",      # o-slash
    "đ": "d", "Đ": "D",      # d with stroke
    "ł": "l", "Ł": "L",      # l with stroke
    "ı": "i", "İ": "I",      # dotless i / I with dot
    "æ": "ae", "Æ": "AE",
    "œ": "oe", "Œ": "OE",
    "ß": "ss", "ẞ": "SS",
    "þ": "th", "Þ": "TH",    # thorn
    "ð": "d", "Ð": "D",      # eth
    "ħ": "h", "Ħ": "H",
    "ŧ": "t", "Ŧ": "T",
    "ŋ": "n", "Ŋ": "N",
    "ə": "e", "Ə": "E",      # schwa
    "̈": "",                       # stray combining diaeresis after NFKD
}


def fold_special_letters(text):
    """Map the non-decomposable Latin letters onto ASCII transliterations."""
    if not isinstance(text, str):
        return ""
    return "".join(SPECIAL_LETTERS.get(ch, ch) for ch in text)


def folded_name_tokens(name):
    """``audit.name_tokens`` with the non-decomposable letters folded first.

    Returns a SET for the same reason the audit's version does: the corpus mixes
    'Nathaniel D. Daw', 'Colosio M' and 'Murray, Lynne', so which token is the
    family name cannot be guessed reliably. Matching by intersection means a
    spurious hit makes a verdict DISAPPEAR rather than appear, which is the safe
    direction for a gate.
    """
    return audit.name_tokens(fold_special_letters(name or ""))


def titles_agree(a, b):
    """True / False / None -- do these two titles name the same work?

    None when either side is empty (nothing to compare; the caller passes).

    Containment is checked BEFORE the ratio and is the load-bearing half. Many
    publishers register only the main title with Crossref, so the authoritative
    title is legitimately a prefix of the declared one (or the reverse -- PubMed
    prepends section headings: 'Social psychology. Just think: ...'). A ratio
    alone puts those at 0.24-0.48, i.e. squarely inside the true-positive range,
    which is exactly the audit's documented subtitle-truncation false positive.

    Containment is tested in two forms, and the split is what makes the shorter
    floor safe (see TITLE_AFFIX_MIN_CHARS):

      AFFIX      the shorter title is a whole-word prefix or suffix of the
                 longer. This is the shape a dropped subtitle or a prepended
                 section heading actually takes, so it is trusted from 12
                 normalised characters.
      SUBSTRING  the shorter appears whole-word ANYWHERE in the longer. Weaker
                 evidence, so it keeps the 20-character floor.

    Whole-word matching in both, via space padding: without it, 'the p factor'
    would also be contained in 'the p factorial design', which is a different
    work.
    """
    na, nb = audit.norm_title(a), audit.norm_title(b)
    if not na or not nb:
        return None
    if na == nb:
        return True
    short, long_ = (na, nb) if len(na) <= len(nb) else (nb, na)
    if len(short) >= TITLE_AFFIX_MIN_CHARS and (
            long_.startswith(short + " ") or long_.endswith(" " + short)):
        return True
    if len(short) >= TITLE_CONTAINMENT_MIN_CHARS and (
            " " + short + " ") in (" " + long_ + " "):
        return True
    ratio = audit.title_ratio(a, b)
    if ratio is None:
        return None
    return ratio >= TITLE_RATIO_MIN


def first_authors_agree(declared_authors, authoritative_authors):
    """True / False / None for the first author of each list."""
    if not declared_authors or not authoritative_authors:
        return None
    d = folded_name_tokens(declared_authors[0])
    a = folded_name_tokens(authoritative_authors[0])
    if not d or not a:
        return None
    return bool(d & a)


def normalise_doi(doi):
    """Comparison form for a DOI. Never used to REWRITE a record's field.

    Case-folded (DOIs are case-insensitive), resolver prefix stripped, and runs
    of slashes collapsed -- the last of which is not cosmetic: PubMed serves the
    legacy APA form ``10.1037//0022-006x.64.2.295`` for DOIs the corpus records
    as ``10.1037/0022-006x.64.2.295``, and without collapsing them 2 of the 9
    cross-check disagreements are that and nothing else.
    """
    if not doi:
        return None
    text = str(doi).strip().lower()
    text = re.sub(r"^https?://(dx\.)?doi\.org/", "", text)
    text = re.sub(r"^doi:\s*", "", text)
    text = re.sub(r"/{2,}", "/", text)
    return text.rstrip(". ") or None


def is_placeholder_doi(doi):
    if not doi:
        return False
    text = str(doi).strip().lower()
    return any(re.search(p, text) for p in PLACEHOLDER_DOI_PATTERNS)


def pubmed_declared_doi(rec):
    """The DOI PubMed itself asserts for a PMID, or None.

    ``articleids`` is the documented mapping and is present on nearly every
    record (489 of 491 in this corpus). ``elocationid`` is the fallback for the
    handful that carry the DOI only there.
    """
    for entry in rec.get("articleids") or []:
        if entry.get("idtype") == "doi":
            value = (entry.get("value") or "").strip()
            if value:
                return value
    match = re.search(r"(10\.\d{4,9}/\S+)", str(rec.get("elocationid") or ""))
    return match.group(1) if match else None


# --------------------------------------------------------------------------
# the secondary identifiers -- arxiv_id, pmc, isbn
#
# All three are declared by the literature_evidence/v1 schema and all three are
# resolvable. Until 2026-08-14 none of them was checked at all, so a wrong one
# entered the corpus unnoticed -- the same gap the doi/pmid work had just closed
# for the other two.
#
# Each is verified against its OWN authority, but the SHAPE was chosen per
# identifier rather than uniformly, because the cheapest form is not the same
# one in each case (see the module docstring, verdicts 5-8):
#
#   pmc    a crosswalk inside a record the gate already fetched  (0 network)
#   arxiv  a crosswalk inside the record's own two fields where a DataCite arXiv
#          DOI is present (0 network), else the arXiv API      (1 call)
#   isbn   a checksum (0 network, gates) plus an OpenLibrary title comparison
#          that is REPORT-ONLY because an ISBN names a volume, not a chapter


def normalise_pmc(value):
    """Comparison form for a PMC id: ``PMC`` + digits. Never rewrites a record.

    The corpus writes ``PMC2801761``; PubMed's ``articleids`` serves the same
    thing under idtype ``pmc``, and under idtype ``pmcid`` wrapped in prose
    (``pmc-id: PMC8497431;manuscript-id: NIHMS1731801;``). Reducing both to the
    digits is what lets those be compared without caring which field served it.
    """
    if not value:
        return None
    digits = re.sub(r"[^0-9]", "", str(value))
    return ("PMC" + digits) if digits else None


def pubmed_declared_pmc(rec):
    """The PMC id PubMed itself asserts for a PMID, or None.

    ``pmc`` is the clean field and is present whenever a record is in PMC at
    all. ``pmcid`` carries the same id inside a prose string and is read as a
    fallback for the same reason ``pubmed_declared_doi`` falls back to
    ``elocationid``: a handful of records serve one and not the other, and a
    missing crosswalk costs coverage silently.

    None is a REAL and common answer -- most PubMed records are not in PMC at
    all -- and must fail open rather than read as a contradiction.
    """
    for entry in rec.get("articleids") or []:
        if entry.get("idtype") == "pmc":
            value = normalise_pmc(entry.get("value"))
            if value:
                return value
    for entry in rec.get("articleids") or []:
        if entry.get("idtype") == "pmcid":
            match = re.search(r"PMC\d+", str(entry.get("value") or ""),
                              re.IGNORECASE)
            if match:
                return normalise_pmc(match.group(0))
    return None


def fetch_pmc(pmc, cache_dir, limiter, timeout=30):
    """esummary one record from ``db=pmc``. Returns the payload, or None if cached.

    Only ever reached by ``check_pmc_declared_vs_identifier``, the fallback for
    a pmc-carrying record with no pmid -- 0 records in this corpus, so this
    fetcher is currently dead weight ON PURPOSE (see that function's docstring).
    It caches an answer, not a transport failure, same split as ``fetch_arxiv``.
    """
    key = normalise_pmc(pmc) or str(pmc)
    path = audit.cache_path(cache_dir, PMC_CACHE_KIND, key)
    if path.exists():
        return None
    numeric = re.sub(r"[^0-9]", "", key)
    url = (PMC_ESUMMARY_URL + "?db=pmc&retmode=json&id="
           + urllib.parse.quote(numeric, safe=""))
    try:
        limiter.wait()
        body = audit.http_get(url, timeout=timeout)
        rec = (json.loads(body).get("result") or {}).get(numeric)
        payload = ({"ok": True, "message": rec} if rec and "error" not in rec
                   else {"ok": False, "error": "not_found"})
    except urllib.error.HTTPError as exc:
        return {"ok": False, "error": "http_%d" % exc.code}
    except Exception as exc:
        return {"ok": False, "error": type(exc).__name__ + ": " + str(exc)[:200]}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")
    return payload


def normalise_arxiv_id(value):
    """Comparison form for an arXiv id. Never used to REWRITE a record's field.

    Strips the ``arXiv:`` prefix, an abs/pdf URL wrapper, and the VERSION suffix
    -- the last of which is load-bearing rather than cosmetic. The API answers a
    query for ``2307.07176`` with ``http://arxiv.org/abs/2307.07176v3``, so
    without dropping ``v3`` the round-trip fidelity check below would refuse
    every hit it was given. Old-style ids (``cs.LG/0701001``) are lower-cased
    and otherwise left alone; the version suffix is only stripped when what
    precedes it ends in a digit, so a genuine ``.../v1abc``-shaped suffix is not
    eaten.
    """
    if not value:
        return None
    text = str(value).strip().lower()
    text = re.sub(r"^https?://(www\.)?arxiv\.org/(abs|pdf)/", "", text)
    text = re.sub(r"^arxiv[:/]\s*", "", text)
    text = re.sub(r"\.pdf$", "", text)
    text = re.sub(r"(?<=\d)v\d+$", "", text)
    return text or None


def arxiv_id_from_doi(doi):
    """The arXiv id a DataCite arXiv DOI encodes, or None for any other DOI.

    ``10.48550/arXiv.2106.03443`` IS ``2106.03443``, which is why a record
    carrying both an ``arxiv_id`` and one of these DOIs can be checked for
    self-contradiction with no network at all.
    """
    if not doi:
        return None
    text = str(doi).strip()
    text = re.sub(r"^https?://(dx\.)?doi\.org/", "", text)
    match = ARXIV_DOI_RE.match(text)
    return normalise_arxiv_id(match.group(1)) if match else None


def canonical_isbn(value):
    """An ISBN reduced to its digits (plus a trailing X), or None.

    The corpus writes both ``9780674458086`` and ``978-0-465-02122-2``, so the
    separators have to go before anything can be compared or checksummed.
    """
    if not value:
        return None
    text = re.sub(r"[^0-9Xx]", "", str(value)).upper()
    return text or None


def isbn_check_digit_ok(value):
    """True / False / None -- does this ISBN's own check digit verify?

    None for anything that is not 10 or 13 characters, because that is a
    SHAPE problem rather than a checksum one and validate_literature.py owns
    the schema. False is CONCLUSIVE: an ISBN whose check digit does not verify
    is not an ISBN, so the record names no verifiable work -- the same class of
    finding as a placeholder DOI, and equally free.
    """
    text = canonical_isbn(value)
    if not text:
        return None
    if len(text) == 13:
        if not text.isdigit():
            return None
        total = sum((1 if i % 2 == 0 else 3) * int(c)
                    for i, c in enumerate(text[:12]))
        return (10 - total % 10) % 10 == int(text[12])
    if len(text) == 10:
        if "X" in text[:9]:
            return None            # X is only legal as the check digit
        if not text[:9].isdigit():
            return None
        total = sum((10 - i) * int(text[i]) for i in range(9))
        total += 10 if text[9] == "X" else int(text[9])
        return total % 11 == 0
    return None


def _parse_arxiv_atom(body):
    """The first entry of an arXiv Atom feed, as a plain dict, or None.

    ``None`` covers both "no entry" (a well-formed but nonexistent id -- the API
    answers 200 with ``totalResults=0``) and an unparseable body. Both fail open.
    """
    import xml.etree.ElementTree as ET
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return None
    entry = root.find(ATOM_NS + "entry")
    if entry is None:
        return None
    authors = []
    for node in entry.findall(ATOM_NS + "author"):
        name = " ".join((node.findtext(ATOM_NS + "name") or "").split())
        if name:
            authors.append(name)
    return {
        "id": " ".join((entry.findtext(ATOM_NS + "id") or "").split()),
        "title": " ".join((entry.findtext(ATOM_NS + "title") or "").split()),
        "authors": authors,
        "published": (entry.findtext(ATOM_NS + "published") or "").strip(),
    }


def arxiv_view(msg):
    """Normalise an arXiv entry into the (years, authors, title, venue) shape.

    Deliberately the SAME shape ``audit.crossref_view`` / ``pubmed_view`` /
    ``csl_view`` return, so ``titles_agree`` and ``first_authors_agree`` can be
    reused verbatim rather than restated -- which is what stops the documented
    false positives coming back through a second door.
    """
    years = []
    match = re.search(r"(19\d\d|20\d\d)", str(msg.get("published") or ""))
    if match:
        years.append(int(match.group(1)))
    return {
        "years": sorted(set(years)),
        "authors": list(msg.get("authors") or []),
        "title": msg.get("title") or "",
        "venue": "arXiv",
        "type": "posted-content",
        "volume": None, "issue": None, "page": None,
    }


def arxiv_entry_is_faithful(msg, arxiv_id):
    """Did arXiv answer about the id that was ASKED about?

    The same guard, and for the same reason, as ``aid_query_is_faithful`` on the
    PubMed side: an authority that quietly answers about a NEIGHBOURING record
    turns a fail-open miss into a confident wrong answer, and the near-miss
    identifier is this corpus's dominant defect class. It fails OPEN -- an
    unfaithful answer is refused, never asserted -- so a future change in how
    arXiv echoes ids costs coverage rather than correctness.
    """
    returned = normalise_arxiv_id(msg.get("id"))
    return bool(returned) and returned == normalise_arxiv_id(arxiv_id)


def fetch_arxiv(arxiv_id, cache_dir, limiter, timeout=30):
    """Fetch one arXiv record. Returns the payload, or None if already cached.

    Caches an ANSWER (including "no such id"), never a TRANSPORT FAILURE --
    the same split, and for the same reason, as ``fetch_pubmed_aid``: an HTTP
    503 persisted as though it were an answer would silently remove that record
    from every future check with no way to tell it apart from a real miss.
    """
    path = audit.cache_path(cache_dir, ARXIV_CACHE_KIND,
                            normalise_arxiv_id(arxiv_id) or str(arxiv_id))
    if path.exists():
        return None
    url = (ARXIV_API_URL + "?max_results=1&id_list="
           + urllib.parse.quote(str(normalise_arxiv_id(arxiv_id)), safe=""))
    try:
        limiter.wait()
        body = audit.http_get(url, timeout=timeout)
        entry = _parse_arxiv_atom(body)
        payload = ({"ok": True, "message": entry} if entry
                   else {"ok": False, "error": "not_found"})
    except urllib.error.HTTPError as exc:
        return {"ok": False, "error": "http_%d" % exc.code}
    except Exception as exc:
        return {"ok": False, "error": type(exc).__name__ + ": " + str(exc)[:200]}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")
    return payload


def openlibrary_view(msg):
    """Normalise an OpenLibrary book record into the shared view shape.

    ``authors`` for a book is whoever OpenLibrary lists, which for an edited
    volume is the EDITORS -- the reason verdict 8 is report-only. The view does
    not try to hide that; the caller is where the volume-vs-chapter question is
    reasoned about, and it is reasoned about explicitly.
    """
    years = []
    match = re.search(r"(1[5-9]\d\d|20\d\d)", str(msg.get("publish_date") or ""))
    if match:
        years.append(int(match.group(1)))
    title = msg.get("title") or ""
    if msg.get("subtitle"):
        title = title + ": " + msg["subtitle"]
    publishers = msg.get("publishers") or []
    venue = ""
    if publishers and isinstance(publishers[0], dict):
        venue = publishers[0].get("name") or ""
    return {
        "years": sorted(set(years)),
        "authors": [a.get("name") for a in (msg.get("authors") or [])
                    if a.get("name")],
        "title": title,
        "venue": venue,
        "type": "book",
        "volume": None, "issue": None, "page": None,
    }


def fetch_openlibrary(isbn, cache_dir, limiter, timeout=30):
    """Fetch one ISBN from OpenLibrary. Returns the payload, or None if cached.

    OpenLibrary answers an unknown ISBN with ``{}`` and HTTP 200 -- an ANSWER
    ("we hold no such book"), cached as ``not_found``. Transport failures are
    not cached, same split as ``fetch_arxiv`` / ``fetch_pubmed_aid``.

    NOT reachable from the gate path: verdict 8 is not in CHECKS_NETWORKED, so
    a commit never waits on OpenLibrary.
    """
    key = canonical_isbn(isbn) or str(isbn)
    path = audit.cache_path(cache_dir, OPENLIBRARY_CACHE_KIND, key)
    if path.exists():
        return None
    url = (OPENLIBRARY_URL + "?format=json&jscmd=data&bibkeys=ISBN:"
           + urllib.parse.quote(key, safe=""))
    try:
        limiter.wait()
        body = audit.http_get(url, timeout=timeout)
        data = json.loads(body) or {}
        record = data.get("ISBN:" + key)
        if not record and data:
            # OpenLibrary echoes the bibkey it was GIVEN; if it ever normalises
            # the key differently, take the single record rather than miss it.
            values = list(data.values())
            record = values[0] if len(values) == 1 else None
        payload = ({"ok": True, "message": record} if record
                   else {"ok": False, "error": "not_found"})
    except urllib.error.HTTPError as exc:
        return {"ok": False, "error": "http_%d" % exc.code}
    except Exception as exc:
        return {"ok": False, "error": type(exc).__name__ + ": " + str(exc)[:200]}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")
    return payload


# --------------------------------------------------------------------------
# the DOI -> PMID crosswalk (esearch `<doi>[AID]`)
#
# ``pubmed_declared_doi`` above answers "which DOI does PubMed hold for this
# PMID". This is the same question asked the other way round, and it is the only
# route that reaches the 1579 records carrying a DOI and no PMID -- for which
# ``doi_pmid_mismatch`` and ``crossview_title_mismatch`` structurally cannot
# fire, there being nothing to cross-resolve against.
#
# WHAT IT CAN AND CANNOT ADD, stated plainly because the obvious reading is too
# generous. The comparison this enables is against the record's OWN declared
# title and first author, so it is verdict 3's shape, not verdict 1's: it is not
# record-internal, and it is not conclusive in verdict 1's sense. What it
# genuinely adds over verdict 3 is a SECOND, INDEPENDENT authoritative view of
# the same DOI -- reaching the cases where Crossref and doi.org resolve nothing
# at all (so verdict 3 fails open and the record goes unchecked entirely), or
# resolve to a record carrying no title or no author list.

PUBMED_AID_CACHE_KIND = "pubmed_aid"

ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

# PubMed answers a `<doi>[AID]` term in one of two visibly different ways, and
# the difference is the reliable hit/miss signal -- more reliable than a
# non-empty idlist alone. A DOI it INDEXES is rewritten into a tokenised phrase
# search over the Publisher ID field:
#
#     term 10.1523/JNEUROSCI.4718-06.2007[AID]
#       -> "10 1523 jneurosci 4718 06 2007"[Publisher ID]      count=1
#
# A DOI it does NOT index comes back with the term UNTRANSLATED and a
# `phrasesnotfound` entry:
#
#     term 10.48550/arXiv.2004.04136[AID]
#       -> 10.48550/arXiv.2004.04136[AID]                      count=0
#
# Requiring the marker is what keeps a DOI made of ordinary English words from
# being silently reinterpreted as a free-text search whose hits would then be
# read as a crosswalk. Measured against the corpus, an untranslated query never
# returns ids -- so this is a belt-and-braces guard, and it is cheap.
AID_TRANSLATION_MARKER = "[Publisher ID]"

# ...and the marker alone is NOT enough, which was learned from this corpus
# rather than reasoned out in advance. PubMed sometimes translates a DOI to only
# a FRAGMENT of itself, dropping every leading token:
#
#     10.1207/s15516709cog1401_3  ->  "3"[Publisher ID]           8446 hits
#     10.24963/ijcai.2023/454     ->  "454"[Publisher ID]         1070 hits
#     10.2307/1130099             ->  "1130099"[Publisher ID]        1 hit
#
# The third is the dangerous shape: a truncated query that happens to be unique
# returns ONE confident-looking PMID for an unrelated paper (36860389, a 2023
# Front Public Health article, for a Diamond 1985 child-development study). The
# `count > 1` rule does not catch it and neither does the marker.
#
# So the translated phrase must tokenise to EXACTLY the DOI's own tokens. This
# fires on 3 of the 1413 indexed DOIs in the corpus, and it fails OPEN (the
# mapping is refused, not asserted), so a future change in PubMed's normalisation
# costs coverage rather than correctness -- the safe direction for a gate.
AID_PHRASE_RE = re.compile(r'^"([^"]*)"\s*\[Publisher ID\]$')


def _id_tokens(text):
    """PubMed's own tokenisation of an identifier: lowercase alphanumeric runs."""
    return [t for t in re.split(r"[^a-z0-9]+", str(text).lower()) if t]


def aid_query_is_faithful(querytranslation, doi):
    """Did PubMed search for the WHOLE DOI, or only a fragment of it?"""
    match = AID_PHRASE_RE.match(str(querytranslation).strip())
    if not match:
        return False
    return _id_tokens(match.group(1)) == _id_tokens(doi)


def aid_cache_key(doi):
    """Cache key for the crosswalk. Lower-cased, like the other DOI-keyed kinds.

    NOT ``normalise_doi``: that is the COMPARISON form and collapses slash runs,
    so keying on it would serve one cached answer for two DOIs that were queried
    as different strings. The value actually sent to PubMed is what gets cached.
    """
    return str(doi).strip().lower()


def fetch_pubmed_aid(doi, cache_dir, limiter, timeout=30):
    """esearch the PubMed AID index for one DOI. Returns the payload, or None if cached.

    DELIBERATELY DOES NOT CACHE FAILURES, which is a departure from
    ``audit.fetch_crossref`` / ``fetch_pubmed`` and the reason is worth stating.
    Those cache a failure so a permanently-dead identifier is not re-fetched on
    every sweep, which is right when the failure is a 404 about a specific work.
    Here the common answer is a legitimate MISS (``count=0``, "this DOI is not a
    PubMed record") and that IS cached -- it is an answer. What must not be
    cached is a TRANSPORT failure: an HTTP 429 from NCBI's rate limiter or a
    dropped connection, persisted as though it were an answer, would silently
    remove that record from every future sweep with no way to tell it apart from
    a real miss. Failures are returned to the caller, counted, and named.
    """
    path = audit.cache_path(cache_dir, PUBMED_AID_CACHE_KIND, aid_cache_key(doi))
    if path.exists():
        return None
    url = (ESEARCH_URL + "?db=pubmed&retmode=json&term="
           + urllib.parse.quote(str(doi) + "[AID]", safe=""))
    try:
        limiter.wait()
        body = audit.http_get(url, timeout=timeout)
        result = (json.loads(body).get("esearchresult") or {})
        payload = {"ok": True, "message": {
            "count": str(result.get("count", "0")),
            "idlist": [str(i) for i in (result.get("idlist") or [])],
            "querytranslation": str(result.get("querytranslation") or ""),
        }}
    except urllib.error.HTTPError as exc:
        return {"ok": False, "error": "http_%d" % exc.code}
    except Exception as exc:
        return {"ok": False, "error": type(exc).__name__ + ": " + str(exc)[:200]}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")
    return payload


def pubmed_holds_doi(rec, doi):
    """True / False / None -- does PubMed's record for this PMID declare this DOI?

    The round trip that makes a crosswalk hit trustworthy, and it is not
    ceremonial. ``[AID]`` is a tokenised PHRASE search, so a query is contained
    by any longer Publisher ID with the same leading tokens -- a DOI recorded
    with a suffix (``...014.suppl``) can match a query for its stem. Confirming
    that PubMed's own ``articleids`` for the returned PMID names the DOI that was
    asked about rules that out completely.

    None when PubMed serves no DOI for that record at all, which is a real
    condition (it is why ``crossview_title_mismatch`` has to exist) and must fail
    open rather than read as a contradiction.
    """
    declared = pubmed_declared_doi(rec)
    if not declared:
        return None
    return normalise_doi(declared) == normalise_doi(doi)


# --------------------------------------------------------------------------
# resolution


class Resolver:
    """Cache-first identifier resolution with an explicit network budget.

    ``budget`` counts NETWORK fetches, not lookups: a cached identifier is free
    and unbudgeted, which is what makes re-committing an unchanged record cost
    nothing. When the budget runs out, ``skipped`` records every identifier that
    went unchecked so the caller can name them (CLAUDE.md, "No silent caps").
    """

    def __init__(self, cache_dir, offline=False, budget=None, timeout=None,
                 arxiv_budget=ARXIV_FETCH_BUDGET):
        self.cache_dir = Path(cache_dir)
        self.offline = offline
        self.budget = budget
        self.spent = 0
        self.skipped = []
        self.errors = []
        self.timeout = timeout
        # Per-KIND caps, on top of the shared budget. Only arXiv has one today
        # and the reason is its request-rate guidance rather than its cost --
        # see ARXIV_FETCH_BUDGET. 0 (or None) means no per-kind cap, which is
        # what the whole-corpus sweep passes.
        self.kind_budget = {"arxiv": arxiv_budget or None}
        self.kind_spent = {}
        self._crossref = audit.RateLimiter(audit.CROSSREF_RATE)
        self._ncbi = audit.RateLimiter(audit.NCBI_RATE)
        self._arxiv = audit.RateLimiter(ARXIV_RATE)
        self._openlibrary = audit.RateLimiter(OPENLIBRARY_RATE)

    def _may_fetch(self, label, kind=None):
        if self.offline:
            self.skipped.append((label, "offline"))
            return False
        if self.budget is not None and self.spent >= self.budget:
            self.skipped.append((label, "network budget spent"))
            return False
        cap = self.kind_budget.get(kind)
        if cap is not None and self.kind_spent.get(kind, 0) >= cap:
            self.skipped.append((label, "%s fetch budget spent" % kind))
            return False
        self.spent += 1
        if kind:
            self.kind_spent[kind] = self.kind_spent.get(kind, 0) + 1
        return True

    def _with_timeout(self, fn, *args):
        if self.timeout is None:
            return fn(*args)
        prev = socket.getdefaulttimeout()
        socket.setdefaulttimeout(self.timeout)
        try:
            return fn(*args)
        finally:
            socket.setdefaulttimeout(prev)

    def doi_view(self, doi):
        """(view, via) for a DOI, or (None, reason).

        A TRANSPORT failure gets its own reason and is recorded in
        ``skipped``/``errors``, never collapsed into ``unresolvable``. Both fail
        open at the gate, but ``unresolvable`` asserts the question was asked
        and answered, and a record dropped from coverage by a 429 must not be
        able to hide inside that word. Same handling ``arxiv_view`` /
        ``pmc_view`` / ``isbn_view`` already give their own fetchers -- it could
        not be written for DOIs until ``audit.fetch_crossref`` / ``fetch_doiorg``
        stopped CACHING transport failures, since until then the failure was
        indistinguishable from a real negative on the very next read.
        """
        failure = None
        cached = audit.load_cached(self.cache_dir, "crossref", doi)
        if cached is None:
            if not self._may_fetch("doi:%s" % doi):
                return None, "unfetched"
            payload = self._with_timeout(
                audit.fetch_crossref, doi, self.cache_dir, self._crossref)
            cached = audit.load_cached(self.cache_dir, "crossref", doi)
            if cached is None:
                failure = (payload or {}).get("error") or "crossref_fetch_failed"
        if cached and cached.get("ok"):
            return audit.crossref_view(cached["message"]), "crossref"

        # Crossref only knows Crossref-registered DOIs; an arXiv DOI is DataCite
        # and 404s there while being perfectly good. doi.org content negotiation
        # reaches whichever agency owns the prefix. Still worth trying when
        # Crossref transport-failed: it is the broader resolver, not a fallback
        # conditional on the first one having answered.
        neg = audit.load_cached(self.cache_dir, "doiorg", doi)
        if neg is None:
            if not self._may_fetch("doi.org:%s" % doi):
                return None, "unfetched"
            payload = self._with_timeout(
                audit.fetch_doiorg, doi, self.cache_dir, self._crossref)
            neg = audit.load_cached(self.cache_dir, "doiorg", doi)
            if neg is None:
                failure = (payload or {}).get("error") or "doiorg_fetch_failed"
        if neg and neg.get("ok"):
            return audit.csl_view(neg["message"]), "doi.org"
        if failure is not None:
            # Reached when EITHER lookup transport-failed and nothing resolved,
            # including the case where doi.org then returned a real 404. That
            # 404 is conclusive on its own, so naming this a skip is marginally
            # over-cautious -- deliberately, since the error it avoids is
            # claiming a record was checked when it was not.
            self.errors.append(("doi:%s" % doi, failure))
            self.skipped.append(("doi:%s" % doi, "doi fetch failed"))
            return None, failure
        return None, "unresolvable"

    def pubmed_record(self, pmid):
        """The raw esummary record for a PMID, or None.

        Returns None for BOTH "PubMed holds no such record" and "the fetch
        failed", because every caller fails open on either. The two are still
        told apart for REPORTING: a transport failure is recorded in
        ``skipped``/``errors`` so the record is named as unchecked rather than
        silently counted as covered. See ``doi_view``.
        """
        cached = audit.load_cached(self.cache_dir, "pubmed", str(pmid))
        if cached is None:
            if not self._may_fetch("pmid:%s" % pmid):
                return None
            payload = self._with_timeout(
                audit.fetch_pubmed, str(pmid), self.cache_dir, self._ncbi)
            cached = audit.load_cached(self.cache_dir, "pubmed", str(pmid))
            if cached is None:
                why = (payload or {}).get("error") or "pubmed_fetch_failed"
                self.errors.append(("pmid:%s" % pmid, why))
                self.skipped.append(("pmid:%s" % pmid, "pubmed fetch failed"))
                return None
        if cached and cached.get("ok"):
            return cached["message"]
        return None

    def pmid_view(self, pmid):
        rec = self.pubmed_record(pmid)
        return (audit.pubmed_view(rec), "pubmed") if rec else (None, "unresolvable")

    def arxiv_view(self, arxiv_id):
        """(view, via) for an arXiv id, or (None, reason).

        ``unfaithful_answer`` is its own reason rather than being folded into
        ``unresolvable``: they fail open identically, but one of them means the
        API answered about a DIFFERENT record, which is worth being able to
        count separately if it ever starts happening.
        """
        key = normalise_arxiv_id(arxiv_id)
        if not key:
            return None, "unresolvable"
        cached = audit.load_cached(self.cache_dir, ARXIV_CACHE_KIND, key)
        if cached is None:
            if not self._may_fetch("arxiv:%s" % key, kind="arxiv"):
                return None, "unfetched"
            payload = self._with_timeout(
                fetch_arxiv, key, self.cache_dir, self._arxiv)
            cached = audit.load_cached(self.cache_dir, ARXIV_CACHE_KIND, key)
            if cached is None:
                why = (payload or {}).get("error") or "arxiv_fetch_failed"
                self.errors.append(("arxiv:%s" % key, why))
                self.skipped.append(("arxiv:%s" % key, "arxiv fetch failed"))
                return None, why
        if not cached.get("ok"):
            return None, "unresolvable"
        message = cached.get("message") or {}
        if not arxiv_entry_is_faithful(message, key):
            return None, "unfaithful_answer"
        return arxiv_view(message), "arxiv"

    def pmc_view(self, pmc):
        """(view, via) for a PMC id via ``db=pmc`` esummary, or (None, reason).

        Not reached on the gate path -- ``check_pmc_declared_vs_identifier`` is
        report-only, because every pmc record in this corpus is already covered
        for free by the pmid crosswalk.
        """
        key = normalise_pmc(pmc)
        if not key:
            return None, "unresolvable"
        cached = audit.load_cached(self.cache_dir, PMC_CACHE_KIND, key)
        if cached is None:
            if not self._may_fetch("pmc:%s" % key, kind="pmc"):
                return None, "unfetched"
            payload = self._with_timeout(
                fetch_pmc, key, self.cache_dir, self._ncbi)
            cached = audit.load_cached(self.cache_dir, PMC_CACHE_KIND, key)
            if cached is None:
                why = (payload or {}).get("error") or "pmc_fetch_failed"
                self.errors.append(("pmc:%s" % key, why))
                self.skipped.append(("pmc:%s" % key, "pmc fetch failed"))
                return None, why
        if not cached.get("ok"):
            return None, "unresolvable"
        # db=pmc esummary is the same record SHAPE as db=pubmed, so the audit's
        # own view function reads it unchanged rather than being restated.
        return audit.pubmed_view(cached.get("message") or {}), "pmc"

    def isbn_view(self, isbn):
        """(view, via) for an ISBN via OpenLibrary, or (None, reason).

        Never reached from the gate path -- verdict 8 is report-only, so no
        commit ever waits on OpenLibrary.
        """
        key = canonical_isbn(isbn)
        if not key:
            return None, "unresolvable"
        cached = audit.load_cached(self.cache_dir, OPENLIBRARY_CACHE_KIND, key)
        if cached is None:
            if not self._may_fetch("isbn:%s" % key, kind="openlibrary"):
                return None, "unfetched"
            payload = self._with_timeout(
                fetch_openlibrary, key, self.cache_dir, self._openlibrary)
            cached = audit.load_cached(self.cache_dir, OPENLIBRARY_CACHE_KIND, key)
            if cached is None:
                why = (payload or {}).get("error") or "openlibrary_fetch_failed"
                self.errors.append(("isbn:%s" % key, why))
                self.skipped.append(("isbn:%s" % key, "openlibrary fetch failed"))
                return None, why
        if not cached.get("ok"):
            return None, "unresolvable"
        return openlibrary_view(cached.get("message") or {}), "openlibrary"

    def pmids_for_doi(self, doi):
        """(pmids, why) -- which PMIDs PubMed holds for this DOI.

        The three return shapes are deliberately distinct and callers must not
        collapse them:

            ([], "not_in_pubmed")   asked and answered -- PubMed indexes no
                                    record for this DOI. This is the COMMON
                                    case, not a finding: arXiv preprints, ML
                                    conference papers, book chapters and
                                    monographs are all legitimately absent.
            ([pmid, ...], "ok")     asked and answered with a mapping.
            (None, <reason>)        the question could not be asked -- offline,
                                    budget spent, transport failure. Fail open.
        """
        key = aid_cache_key(doi)
        cached = audit.load_cached(self.cache_dir, PUBMED_AID_CACHE_KIND, key)
        if cached is None:
            if not self._may_fetch("aid:%s" % doi):
                return None, "unfetched"
            payload = self._with_timeout(
                fetch_pubmed_aid, doi, self.cache_dir, self._ncbi)
            cached = audit.load_cached(self.cache_dir, PUBMED_AID_CACHE_KIND, key)
            if cached is None:
                why = (payload or {}).get("error") or "esearch_failed"
                self.errors.append(("aid:%s" % doi, why))
                self.skipped.append(("aid:%s" % doi, "esearch failed"))
                return None, why
        if not cached.get("ok"):
            return None, cached.get("error") or "esearch_failed"
        message = cached.get("message") or {}
        idlist = [str(i) for i in (message.get("idlist") or [])]
        if not idlist:
            return [], "not_in_pubmed"
        translation = message.get("querytranslation") or ""
        if AID_TRANSLATION_MARKER not in translation:
            # Hits from a query PubMed did not read as an identifier lookup.
            # Never seen in this corpus; treated as unusable rather than trusted.
            return None, "untranslated_query"
        if not aid_query_is_faithful(translation, doi):
            # PubMed searched a FRAGMENT of the DOI. Its hits are about some
            # other paper whose identifier merely ends the same way.
            return None, "truncated_query"
        return idlist, "ok"


# The crosswalk outcomes that are NOT findings. Every one of them is a reason the
# question could not be answered, or was answered "no such record" -- and the
# first of those is the common case by a wide margin. Named here so the sweep can
# report them by bucket instead of dropping them (CLAUDE.md, "No silent caps").
CROSSWALK_NON_FINDING_STATUSES = (
    "placeholder",              # already reported by check_placeholder
    "not_in_pubmed",            # THE COMMON CASE -- arXiv, ML venues, books
    "unfetched",                # offline, or the network budget is spent
    "esearch_failed",           # transport failure; not cached, retried later
    "untranslated_query",       # PubMed did not read the term as an identifier
    "truncated_query",          # PubMed searched only a FRAGMENT of the DOI
    "ambiguous",                # >1 PMID for one DOI
    "pmid_unresolvable",        # esummary has nothing for the returned PMID
    "unconfirmed_mapping",      # the round trip could not confirm it
    "no_declared_fields",       # the record declares no title or no authors
    "agrees",                   # crosswalk confirms the record. The good case.
)


def crosswalk_doi(target, resolver):
    """Resolve one record's DOI through PubMed's AID index.

    Returns a dict carrying ``status`` (one of CROSSWALK_NON_FINDING_STATUSES,
    or ``"names_a_different_paper"``) plus whatever was learned along the way.
    Written as one function returning a status rather than as a predicate,
    because the sweep needs the buckets as much as it needs the findings: the
    ratio of ``not_in_pubmed`` to everything else is what tells a later reader
    whether this check is worth its ~1600 calls.
    """
    out = {"rel": target["rel"], "entry": target["entry"], "doi": target["doi"],
           "pmid": None, "status": None, "why": None,
           "title_ok": None, "author_ok": None,
           "pubmed_title": None, "pubmed_first_author": None,
           "doi_resolves_elsewhere": None}
    doi = target["doi"]
    if not doi:
        out["status"] = "no_doi"
        return out
    if is_placeholder_doi(doi):
        out["status"] = "placeholder"
        return out

    pmids, why = resolver.pmids_for_doi(doi)
    out["why"] = why
    if pmids is None:
        out["status"] = why if why in CROSSWALK_NON_FINDING_STATUSES \
            else "esearch_failed"
        return out
    if not pmids:
        out["status"] = "not_in_pubmed"
        return out
    if len(pmids) > 1:
        # One DOI, several PubMed records (a duplicate deposit, or a preprint and
        # its published version). Which one the record MEANT is exactly the
        # external judgement this tool refuses to make.
        out["status"] = "ambiguous"
        out["pmid"] = ",".join(pmids)
        return out

    pmid = pmids[0]
    out["pmid"] = pmid
    rec = resolver.pubmed_record(pmid)
    if rec is None:
        out["status"] = "pmid_unresolvable"
        return out
    if pubmed_holds_doi(rec, doi) is not True:
        out["status"] = "unconfirmed_mapping"
        return out

    view = audit.pubmed_view(rec)
    out["pubmed_title"] = view["title"]
    out["pubmed_first_author"] = (view["authors"] or [None])[0]

    source = target["source"]
    declared_title = source.get("title")
    declared_authors = source.get("authors") or []
    if not declared_title or not declared_authors:
        out["status"] = "no_declared_fields"
        return out

    out["title_ok"] = titles_agree(declared_title, view["title"])
    out["author_ok"] = first_authors_agree(declared_authors, view["authors"])
    if out["title_ok"] is False and out["author_ok"] is False:
        out["status"] = "names_a_different_paper"
    else:
        out["status"] = "agrees"
    return out


def check_doi_crosswalk(target, resolver):
    """The crosswalk as a verdict: this DOI names a paper the record does not describe.

    BOTH axes are required, for exactly the reason verdict 3 requires both --
    title alone is the subtitle-truncation false positive, first author alone is
    the name-change / preprint-order / non-ASCII one. This reuses ``titles_agree``
    and ``first_authors_agree`` rather than restating the comparison, so the
    documented false positives cannot come back through a second door.

    NOT in CHECKS_NETWORKED, and therefore not on the commit-gate path. That is
    deliberate and is a standing constraint, not an oversight: a new blocking
    verdict may not be wired in ahead of a whole-corpus baseline measurement, the
    way verdict 3's conjunction was measured at 21/21 before it was trusted. See
    the crosswalk section of
    evidence/planning/literature_identifier_cross_resolution_findings_2026-08-14.md.
    """
    result = crosswalk_doi(target, resolver)
    if result["status"] != "names_a_different_paper":
        return None
    return Verdict(
        "doi_crosswalk_names_a_different_paper",
        target["rel"],
        "PubMed indexes doi %s as pmid %s, %r by %s -- but the record declares "
        "%r by %s. Title AND first author both disagree, so the DOI names a "
        "different paper from the one this entry describes"
        % (target["doi"], result["pmid"], (result["pubmed_title"] or "")[:110],
           result["pubmed_first_author"],
           (target["source"].get("title") or "")[:110],
           (target["source"].get("authors") or ["?"])[0]),
        declared={"doi": target["doi"],
                  "title": target["source"].get("title"),
                  "first_author": (target["source"].get("authors") or [None])[0]},
        authoritative={"via": "pubmed_aid_crosswalk", "pmid": result["pmid"],
                       "title": result["pubmed_title"],
                       "first_author": result["pubmed_first_author"]})


def batch_fetch_pubmed(pmids, cache_dir, limiter, batch=100, verbose=True):
    """Populate the pubmed cache in batches, in the audit's own cache format.

    esummary accepts comma-separated ids, so 491 PMIDs is 5 requests rather than
    491. That is NCBI's own guidance and it is the polite form; each record is
    still written to ``cache_path(..., 'pubmed', pmid)`` with the same
    ``{"ok": ..., "message": ...}`` payload ``audit.fetch_pubmed`` writes, so
    ``audit.load_cached`` reads them interchangeably and the single-record
    fetcher stays the one used on the gate path (one call per new record).

    Returns (n_cached, n_failed_batches).
    """
    cache_dir = Path(cache_dir)
    todo = []
    seen = set()
    for pmid in pmids:
        key = str(pmid)
        if key in seen:
            continue
        seen.add(key)
        if not audit.cache_path(cache_dir, "pubmed", key).exists():
            todo.append(key)

    if not todo:
        if verbose:
            print("pubmed cache is complete -- nothing to fetch")
        return 0, 0

    if verbose:
        print("pubmed identifiers to fetch: %d (in batches of %d)" % (len(todo), batch))
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    n_cached = 0
    n_failed = 0
    for start in range(0, len(todo), batch):
        chunk = todo[start:start + batch]
        data = urllib.parse.urlencode(
            {"db": "pubmed", "retmode": "json", "id": ",".join(chunk)}
        ).encode("ascii")
        request = urllib.request.Request(
            url, data=data, headers={"User-Agent": audit.USER_AGENT}
        )
        try:
            limiter.wait()
            with urllib.request.urlopen(request, timeout=60) as resp:
                body = resp.read().decode("utf-8", "replace")
            result = json.loads(body).get("result", {})
        except Exception as exc:
            n_failed += 1
            if verbose:
                print("  batch at %d FAILED: %s: %s"
                      % (start, type(exc).__name__, str(exc)[:120]), flush=True)
            time.sleep(2.0)
            continue
        for pmid in chunk:
            rec = result.get(pmid)
            if rec and "error" not in rec:
                payload = {"ok": True, "message": rec}
            else:
                payload = {"ok": False, "error": "not_found"}
            path = audit.cache_path(cache_dir, "pubmed", pmid)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(payload), encoding="utf-8")
            n_cached += 1
        if verbose:
            print("  cached %d/%d" % (min(start + batch, len(todo)), len(todo)),
                  flush=True)
    return n_cached, n_failed


# --------------------------------------------------------------------------
# waivers
#
# Pinned to (entry directory, identifier VALUE) on purpose. A waiver keyed on the
# path alone would silently absorb the NEXT wrong identifier written into the
# same record; keyed on the value, a new defect in a waived record still blocks.
# Every entry must name a reason and where it was adjudicated.

WAIVERS = [
    {
        "entry": "2026-03-29_arc_032_frontal_theta_hippocampus_reward_hyman2010",
        "doi": "10.1002/hipo.20709",
        "reason": (
            "Audit 2026-08-14 'Left unrepaired' item 1b, GFLAG-0029 (open): the "
            "DOI resolves to Christie, 'Exercising some control over the "
            "hippocampus' (2009). The declared title is fabricated, and the "
            "content the summary describes is Jones & Wilson (2005), not either "
            "candidate Hyman paper -- so writing an identifier would change the "
            "EVIDENCE, not the provenance. The record carries no PMID to "
            "cross-resolve against. Undeterminable pending governance, which is "
            "a different thing from unrepaired."
        ),
    },
]

# TWO FURTHER WAIVERS WERE WRITTEN HERE AND HAVE BEEN REMOVED AS DEAD, which is
# the value-keying above working exactly as intended rather than a regression.
# They covered the DOIs `10.1163/156853995X00822`
# (q035_arc049_murray_trevarthen_1985_double_video) and `10.1163/156853995X00101`
# (arc049_inv059_gergely_watson1996_social_biofeedback), on the audit's then-open
# "book chapter, needs an edition judgement" reading. REE_assembly ec4467bcf4
# settled both the other way -- neither work has a chapter-level DOI at all, so
# both records now carry `doi: null` ("checked, none exists"), one with a verified
# PMID and one with the containing volume's ISBN. A waiver keyed on a DOI VALUE
# that no longer appears anywhere can never match again, so keeping it would only
# mislead a later reader into thinking those records are still exempt. Confirmed
# against the live records before removal.
#
# The habenula placeholder (`10.0000/example-doi`,
# neuro_pe_habenula_da/.../2026-02-13_habenula_da_signed_pe_review, GFLAG-0031)
# is deliberately NOT waived, even though it is known and open. It is the one
# record in the corpus that trips this gate today, and it SHOULD: the entry cites
# no real work, so a commit touching it ought to stop and read the flag. It also
# costs nothing in practice -- disposing of the entry means DELETING it, and a
# deleted record.json resolves to no target at all (collect_scoped_targets skips
# paths that do not exist), so the gate cannot obstruct its own remedy.


def waiver_for(entry_name, doi=None, pmid=None, arxiv_id=None, pmc=None,
               isbn=None):
    """The waiver covering this record and one of these identifier VALUES, or None.

    The secondary identifiers are matched through the SAME normalisers the
    verdicts compare with (``normalise_arxiv_id``, ``normalise_pmc``,
    ``canonical_isbn``) rather than by raw string equality. Otherwise a waiver
    written as ``PMC2801761`` would silently stop covering a record that spells
    it ``pmc2801761``, or an ISBN waiver would stop covering the hyphenated
    form of the same ISBN -- a waiver that quietly stops matching is a waiver
    that quietly starts blocking, which is the failure direction a gate can
    least afford.

    Value-keying itself is deliberate and is explained at WAIVERS above: keyed
    on the entry path alone, a waiver would absorb the NEXT wrong identifier
    written into the same record.
    """
    for waiver in WAIVERS:
        if waiver.get("entry") != entry_name:
            continue
        if waiver.get("doi") and normalise_doi(waiver["doi"]) == normalise_doi(doi):
            return waiver
        if waiver.get("pmid") and str(waiver["pmid"]) == str(pmid or ""):
            return waiver
        if (waiver.get("arxiv_id")
                and normalise_arxiv_id(waiver["arxiv_id"])
                == normalise_arxiv_id(arxiv_id)):
            return waiver
        if (waiver.get("pmc")
                and normalise_pmc(waiver["pmc"]) == normalise_pmc(pmc)):
            return waiver
        if (waiver.get("isbn")
                and canonical_isbn(waiver["isbn"]) == canonical_isbn(isbn)):
            return waiver
    return None


# --------------------------------------------------------------------------
# verdicts


class Verdict:
    """A CONCLUSIVE identifier finding. Everything softer than this is the audit's."""

    __slots__ = ("kind", "path", "detail", "declared", "authoritative")

    def __init__(self, kind, path, detail, declared=None, authoritative=None):
        self.kind = kind
        self.path = path
        self.detail = detail
        self.declared = declared
        self.authoritative = authoritative

    def as_dict(self):
        return {
            "kind": self.kind,
            "path": self.path,
            "detail": self.detail,
            "declared": self.declared,
            "authoritative": self.authoritative,
        }


def check_placeholder(target):
    doi = target["doi"]
    if not is_placeholder_doi(doi):
        return None
    return Verdict(
        "placeholder_identifier",
        target["rel"],
        "source.doi=%r is a placeholder, not an identifier -- it cannot resolve "
        "and the record therefore names no verifiable work" % doi,
        declared={"doi": doi},
    )


def check_doi_pmid_mismatch(target, resolver):
    """Verdict 1: the record's own two identifiers contradict each other."""
    doi, pmid = target["doi"], target["pmid"]
    if not doi or not pmid:
        return None
    if is_placeholder_doi(doi):
        return None          # already reported as a placeholder
    rec = resolver.pubmed_record(pmid)
    if rec is None:
        return None          # unresolvable / unfetched -> fail open
    pm_doi = pubmed_declared_doi(rec)
    if not pm_doi:
        return None          # PubMed serves no DOI -> verdict 2's job
    if normalise_doi(pm_doi) == normalise_doi(doi):
        return None
    return Verdict(
        "doi_pmid_mismatch",
        target["rel"],
        "PubMed's own articleids for pmid %s name doi %s, but the record "
        "declares %s -- the record's two identifiers point at different works, "
        "so one of them is wrong" % (pmid, pm_doi, doi),
        declared={"doi": doi, "pmid": str(pmid)},
        authoritative={"pubmed_doi": pm_doi, "pubmed_title": rec.get("title")},
    )


def check_crossview(target, resolver):
    """Verdict 2: the two identifiers resolve to different works."""
    doi, pmid = target["doi"], target["pmid"]
    if not doi or not pmid or is_placeholder_doi(doi):
        return None
    doi_view, _ = resolver.doi_view(doi)
    pmid_view, _ = resolver.pmid_view(pmid)
    if not doi_view or not pmid_view:
        return None
    agree = titles_agree(doi_view["title"], pmid_view["title"])
    if agree is not False:
        return None          # agrees, or nothing to compare -> fail open
    return Verdict(
        "crossview_title_mismatch",
        target["rel"],
        "doi %s resolves to %r; pmid %s resolves to %r -- two authoritative "
        "sources describing different works, so one identifier is wrong"
        % (doi, (doi_view["title"] or "")[:120], pmid,
           (pmid_view["title"] or "")[:120]),
        declared={"doi": doi, "pmid": str(pmid)},
        authoritative={"doi_title": doi_view["title"],
                       "pmid_title": pmid_view["title"],
                       "doi_first_author": (doi_view["authors"] or [None])[0],
                       "pmid_first_author": (pmid_view["authors"] or [None])[0]},
    )


def check_declared_vs_identifier(target, resolver):
    """Verdict 3: the identifier resolves to a paper this record does not describe.

    BOTH axes are required. Title alone is the subtitle-truncation false
    positive; first author alone is the name-change / preprint-order / non-ASCII
    false positive. Requiring the conjunction is what took this from "a flag a
    human triages" to "a verdict a gate can act on" -- measured at 21/21 true
    positives and 0 false positives over the repaired corpus.
    """
    source = target["source"]
    declared_title = source.get("title")
    declared_authors = source.get("authors") or []
    if not declared_title or not declared_authors:
        return None          # nothing to compare -> validate_literature.py's job

    view = via = None
    if target["doi"] and not is_placeholder_doi(target["doi"]):
        view, via = resolver.doi_view(target["doi"])
    if view is None and target["pmid"]:
        view, via = resolver.pmid_view(target["pmid"])
    if view is None:
        return None          # unresolvable / unfetched -> fail open

    title_ok = titles_agree(declared_title, view["title"])
    author_ok = first_authors_agree(declared_authors, view["authors"])
    if title_ok is not False or author_ok is not False:
        return None

    return Verdict(
        "identifier_names_a_different_paper",
        target["rel"],
        "the identifier resolves to %r by %s, but the record declares %r by %s "
        "-- title AND first author both disagree, so the identifier points at a "
        "different paper"
        % ((view["title"] or "")[:110], (view["authors"] or ["?"])[0],
           declared_title[:110], declared_authors[0]),
        declared={"doi": target["doi"], "pmid": target["pmid"],
                  "title": declared_title, "first_author": declared_authors[0]},
        authoritative={"via": via, "title": view["title"],
                       "first_author": (view["authors"] or [None])[0],
                       "years": view["years"]},
    )


# --------------------------------------------------------------------------
# the secondary-identifier verdicts (5-8)


def check_pmc_pmid_mismatch(target, resolver):
    """Verdict 5: the record's own pmc and pmid contradict each other.

    Verdict 1's shape, one identifier over, and it is the CHEAPEST verdict in
    this file: the crosswalk lives inside the esummary record that
    ``check_doi_pmid_mismatch`` has already fetched and cached, so this costs
    ZERO additional network calls. Every one of the 80 pmc-carrying records in
    this corpus also carries a pmid, so this route reaches all of them.

    Fails open in three places, each of which is a real condition rather than a
    theoretical one: no pmid to cross-resolve against, an unresolvable or
    unfetched pmid, and a PubMed record that names no PMC id at all (the common
    case across PubMed as a whole -- most records are not in PMC).
    """
    pmc, pmid = target.get("pmc"), target.get("pmid")
    if not pmc or not pmid:
        return None
    declared = normalise_pmc(pmc)
    if not declared:
        return None          # not PMC-shaped -> validate_literature.py's job
    rec = resolver.pubmed_record(pmid)
    if rec is None:
        return None          # unresolvable / unfetched -> fail open
    pm_pmc = pubmed_declared_pmc(rec)
    if not pm_pmc:
        return None          # PubMed serves no PMC id -> fail open
    if pm_pmc == declared:
        return None
    return Verdict(
        "pmc_pmid_mismatch",
        target["rel"],
        "PubMed's own articleids for pmid %s name %s, but the record declares "
        "pmc %s -- the record's two identifiers point at different works, so "
        "one of them is wrong" % (pmid, pm_pmc, pmc),
        declared={"pmc": pmc, "pmid": str(pmid)},
        authoritative={"pubmed_pmc": pm_pmc, "pubmed_title": rec.get("title")},
    )


def check_pmc_declared_vs_identifier(target, resolver):
    """The pmc fallback for a record with no pmid to cross-resolve against.

    DELIBERATELY NOT IN ``CHECKS_NETWORKED``, and the reason is arithmetic
    rather than caution: it reaches 0 records. All 80 pmc-carrying records in
    this corpus also carry a pmid, so ``check_pmc_pmid_mismatch`` -- which is
    conclusive AND free -- already covers every one of them, while this would
    spend an esummary call per record to reach a strictly weaker (verdict-3
    shape, not record-internal) conclusion. It is implemented and tested so the
    coverage exists the day a pmc-only record arrives; wiring it in before then
    would cost budget and buy nothing.

    Re-measure before assuming that still holds -- it is a property of the
    corpus, not of this code. The one-liner is in the findings doc.
    """
    pmc, pmid = target.get("pmc"), target.get("pmid")
    if not pmc or pmid:
        return None          # the pmid route is better; let verdict 5 have it
    view, via = resolver.pmc_view(pmc)
    if view is None:
        return None          # unresolvable / unfetched -> fail open
    source = target["source"]
    declared_title = source.get("title")
    declared_authors = source.get("authors") or []
    if not declared_title or not declared_authors:
        return None
    if (titles_agree(declared_title, view["title"]) is not False
            or first_authors_agree(declared_authors, view["authors"]) is not False):
        return None
    return Verdict(
        "pmc_names_a_different_paper",
        target["rel"],
        "pmc %s resolves to %r by %s, but the record declares %r by %s -- "
        "title AND first author both disagree, so the PMC id points at a "
        "different paper"
        % (pmc, (view["title"] or "")[:110], (view["authors"] or ["?"])[0],
           declared_title[:110], declared_authors[0]),
        declared={"pmc": pmc, "title": declared_title,
                  "first_author": declared_authors[0]},
        authoritative={"via": via, "title": view["title"],
                       "first_author": (view["authors"] or [None])[0]},
    )


def check_arxiv_doi_mismatch(target, resolver=None):
    """Verdict 6: the record's arxiv_id and its arXiv DOI encode different ids.

    Record-internal, conclusive, and FREE -- a DataCite arXiv DOI
    (``10.48550/arXiv.<id>``) contains the arXiv id, so the contradiction is
    visible in the record's own two fields with nothing fetched. This is the
    crosswalk shape ``doi_pmid_mismatch`` uses, and it is preferred here for
    exactly the same reason: it needs no external notion of what the record
    should say, and no title comparison at all.

    ``resolver`` is accepted and unused so this can sit in the same check lists
    as the networked verdicts.
    """
    arxiv_id, doi = target.get("arxiv_id"), target.get("doi")
    declared = normalise_arxiv_id(arxiv_id)
    from_doi = arxiv_id_from_doi(doi)
    if not declared or not from_doi or declared == from_doi:
        return None
    return Verdict(
        "arxiv_doi_mismatch",
        target["rel"],
        "the record's doi %s is the arXiv DOI for %s, but the record declares "
        "arxiv_id %s -- the record's two identifiers point at different "
        "preprints, so one of them is wrong" % (doi, from_doi, arxiv_id),
        declared={"arxiv_id": arxiv_id, "doi": doi},
        authoritative={"arxiv_id_encoded_in_doi": from_doi},
    )


def check_arxiv_names_a_different_paper(target, resolver):
    """Verdict 7: the arXiv id resolves to a preprint this record does not describe.

    Verdict 3's shape and verdict 3's conjunction, against the arXiv API. BOTH
    axes are required for the reasons verdict 3 documents, and it reuses
    ``titles_agree`` / ``first_authors_agree`` rather than restating the
    comparison so the four documented false positives cannot come back through
    a second door. The preprint-author-order false positive (CURL is
    Srinivas-first on arXiv and Laskin-first at ICML) is if anything MORE likely
    here than on the DOI path, which is another reason the title has to disagree
    too.

    SKIPPED ENTIRELY when the record's own DOI already confirms the arXiv id.
    That is not an optimisation for its own sake: verdict 6 has then established
    the id record-internally, and verdict 3 is already comparing the same
    declared fields against the same work through the DOI, so the call would
    buy nothing. It is what keeps this at 2 of the 5 arXiv records in this
    corpus rather than 5.
    """
    arxiv_id = target.get("arxiv_id")
    declared_id = normalise_arxiv_id(arxiv_id)
    if not declared_id:
        return None
    if arxiv_id_from_doi(target.get("doi")) == declared_id:
        return None          # confirmed record-internally; verdict 6 owns it

    source = target["source"]
    declared_title = source.get("title")
    declared_authors = source.get("authors") or []
    if not declared_title or not declared_authors:
        return None          # nothing to compare -> validate_literature.py's job

    view, via = resolver.arxiv_view(arxiv_id)
    if view is None:
        return None          # unresolvable / unfetched / unfaithful -> fail open

    if (titles_agree(declared_title, view["title"]) is not False
            or first_authors_agree(declared_authors, view["authors"]) is not False):
        return None
    return Verdict(
        "arxiv_names_a_different_paper",
        target["rel"],
        "arxiv_id %s resolves to %r by %s, but the record declares %r by %s -- "
        "title AND first author both disagree, so the arXiv id points at a "
        "different preprint"
        % (arxiv_id, (view["title"] or "")[:110], (view["authors"] or ["?"])[0],
           declared_title[:110], declared_authors[0]),
        declared={"arxiv_id": arxiv_id, "title": declared_title,
                  "first_author": declared_authors[0]},
        authoritative={"via": via, "title": view["title"],
                       "first_author": (view["authors"] or [None])[0],
                       "years": view["years"]},
    )


def check_isbn_malformed(target, resolver=None):
    """Verdict 4b: this ISBN's own check digit does not verify.

    Network-free, conclusive and in the same class as ``placeholder_identifier``
    -- a string that fails the ISBN checksum is not an ISBN, so the record names
    no verifiable work, and no external notion of what the record should say is
    needed to know it. Unlike verdict 8 it has none of the volume-vs-chapter
    trouble, which is why this half gates and that half does not.

    Only 10- and 13-character forms are judged; anything else returns None from
    ``isbn_check_digit_ok`` and fails open, because a wrong LENGTH is a schema
    problem and validate_literature.py owns the schema.
    """
    isbn = target.get("isbn")
    if not isbn:
        return None
    if isbn_check_digit_ok(isbn) is not False:
        return None
    return Verdict(
        "malformed_identifier",
        target["rel"],
        "source.isbn=%r fails its own ISBN check digit, so it is not a valid "
        "ISBN and cannot resolve -- the record therefore names no verifiable "
        "work" % isbn,
        declared={"isbn": isbn},
    )


def check_isbn_names_a_different_work(target, resolver):
    """Verdict 8: the ISBN resolves to a book this record does not describe.

    REPORT-ONLY. Not in ``CHECKS_NETWORKED``, not reachable from the commit
    gate, and that is a MEASURED decision -- see the module docstring, verdict 8,
    for the numbers and the flip condition. In short: an ISBN names a VOLUME,
    so a correct ISBN on a CHAPTER record legitimately resolves to a different
    title by different people (the volume's editors), and 1 of the 5
    ISBN-carrying records in this corpus is exactly that shape.

    The ``venue`` disjunction below is what rescues that record, and it is
    honest about being a patch rather than a principle: a chapter record's
    ``venue`` is conventionally the containing volume's title, so accepting it
    as an alternative title separates "chapter of the right book" from "wrong
    book" -- but the convention is not enforced by the schema, and the rule was
    written from the single record it rescues. That is why this reports rather
    than blocks.
    """
    isbn = target.get("isbn")
    if not isbn or isbn_check_digit_ok(isbn) is False:
        return None          # malformed -> verdict 4b already said so
    source = target["source"]
    declared_title = source.get("title")
    declared_authors = source.get("authors") or []
    if not declared_title or not declared_authors:
        return None

    view, via = resolver.isbn_view(isbn)
    if view is None:
        return None          # not in OpenLibrary / unfetched -> fail open

    title_ok = titles_agree(declared_title, view["title"])
    # The volume-vs-chapter disjunction. `venue` for a chapter record is the
    # containing volume, which is what the ISBN actually identifies.
    if title_ok is False and source.get("venue"):
        if titles_agree(source["venue"], view["title"]) is not False:
            title_ok = True
    if title_ok is not False:
        return None
    if first_authors_agree(declared_authors, view["authors"]) is not False:
        return None
    return Verdict(
        "isbn_names_a_different_work",
        target["rel"],
        "isbn %s resolves to %r by %s, but the record declares %r by %s (venue "
        "%r) -- title AND first author both disagree, so the ISBN names a "
        "different volume"
        % (isbn, (view["title"] or "")[:110], (view["authors"] or ["?"])[0],
           declared_title[:110], declared_authors[0], source.get("venue")),
        declared={"isbn": isbn, "title": declared_title,
                  "venue": source.get("venue"),
                  "first_author": declared_authors[0]},
        authoritative={"via": via, "title": view["title"],
                       "first_author": (view["authors"] or [None])[0],
                       "years": view["years"]},
    )


# Every verdict that needs no network at all. Checked first and unconditionally,
# because they cost nothing and stay correct on a box with no outbound route.
CHECKS_OFFLINE = (
    check_placeholder,
    check_arxiv_doi_mismatch,
    check_isbn_malformed,
)

CHECKS_NETWORKED = (
    check_doi_pmid_mismatch,
    check_crossview,
    check_declared_vs_identifier,
    check_pmc_pmid_mismatch,
    check_arxiv_names_a_different_paper,
)

# Implemented, tested, and DELIBERATELY off the gate path. Each one's reason is
# in its own docstring and none of them is "we did not get round to it":
# check_pmc_declared_vs_identifier reaches 0 records that verdict 5 does not
# already cover for free; check_isbn_names_a_different_work has a measured
# false positive built into the identifier's semantics;
# check_doi_crosswalk buys 0 marginal coverage over verdict 3. A later session
# may promote any of them -- after measuring a whole-corpus baseline, which is
# the standing rule this file has followed for every verdict it does run.
CHECKS_REPORT_ONLY = (
    check_pmc_declared_vs_identifier,
    check_isbn_names_a_different_work,
)

# The verdict KINDS those checks emit. Stated separately because a sweep sorts
# its output by kind and has to know which findings are advisory before it can
# say so -- and because getting this wrong in the SAFE direction (a gating kind
# missing from this set) would silently print a blocking finding under a
# "never blocks" heading. Pinned by
# test_report_only_kinds_covers_every_report_only_check, which runs each
# report-only check against a fixture that makes it fire and asserts the kind it
# produces is listed here, so adding a check without adding its kind fails.
REPORT_ONLY_KINDS = frozenset({
    "pmc_names_a_different_paper",
    "isbn_names_a_different_work",
    "doi_crosswalk_names_a_different_paper",
})


def verify_target(target, resolver, extra_checks=()):
    """Every conclusive verdict for one record, waivers applied.

    ``extra_checks`` is how a SWEEP runs the report-only verdicts
    (``CHECKS_REPORT_ONLY``) without them ever being reachable from the gate,
    which calls this with the default empty tuple.
    """
    verdicts = []
    for check in CHECKS_OFFLINE:
        verdict = check(target)
        if verdict is not None:
            verdicts.append(verdict)
    for check in tuple(CHECKS_NETWORKED) + tuple(extra_checks):
        verdict = check(target, resolver)
        if verdict is not None:
            verdicts.append(verdict)

    kept = []
    for verdict in verdicts:
        waiver = waiver_for(target["entry"], target["doi"], target["pmid"],
                            target.get("arxiv_id"), target.get("pmc"),
                            target.get("isbn"))
        if waiver is not None:
            verdict.kind = "waived:" + verdict.kind
            verdict.detail = "%s  [WAIVED: %s]" % (verdict.detail, waiver["reason"])
        kept.append(verdict)
    return kept


# --------------------------------------------------------------------------
# target collection


# Every identifier this file knows how to verify. Order matters only for the
# report; membership is what decides whether a record is a target at all.
IDENTIFIER_KEYS = ("doi", "pmid", "arxiv_id", "pmc", "isbn")


def _target_from(path, source):
    target = {
        "path": path,
        "rel": str(Path(path).relative_to(REPO)) if str(path).startswith(str(REPO))
               else str(path),
        "entry": Path(path).parent.name,
        "source": source,
    }
    for key in IDENTIFIER_KEYS:
        target[key] = source.get(key)
    return target


def collect_all_targets(keys=IDENTIFIER_KEYS):
    """Every record carrying one of ``keys``.

    NOT ``audit.collect_targets()`` any more, and the reason is worth stating
    because delegating to it was right until 2026-08-14. That collector filters
    on doi/pmid ONLY, so a record whose only identifier is an arxiv_id or an
    isbn -- 7 of them in this corpus -- was invisible to every mode of this
    tool, including the sweep that measures the baselines. The audit module is
    left bit-identical on purpose (its false-positive counts are quoted by
    number in the 2026-08-14 report and must stay reproducible), so the wider
    scan lives here instead.

    ``keys`` exists so ``--cross-check`` can still ask the doi/pmid question
    over the doi/pmid population and print the same 2072 it printed before.
    """
    targets = []
    for path, data, err in audit.iter_records():
        if err:
            continue
        source = (data or {}).get("source") or {}
        if not any(source.get(key) for key in keys):
            continue
        targets.append(_target_from(path, source))
    return targets


def collect_scoped_targets(raw_paths):
    """Records implicated by arbitrary literature paths.

    Resolves any file inside an entry directory up to that entry's record.json,
    the same way validate_literature.resolve_scope_paths does, so the commit gate
    can hand over whatever `git diff --cached` listed.
    """
    seen = []
    ordered = set()
    for raw in raw_paths:
        path = Path(raw)
        if not path.is_absolute():
            path = REPO / path
        candidates = []
        if path.name == "record.json":
            candidates.append(path)
        node = path
        while node != node.parent:
            if node.parent.name == "entries":
                candidates.append(node / "record.json")
                break
            node = node.parent
        for candidate in candidates:
            key = str(candidate)
            if key not in ordered:
                ordered.add(key)
                seen.append(candidate)

    targets = []
    for record_path in seen:
        if not record_path.exists():
            continue
        try:
            data = json.loads(record_path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue     # validate_literature.py owns unparseable records
        source = (data or {}).get("source") or {}
        # Any of the five identifiers makes this a target. It was doi/pmid only
        # until 2026-08-14, which meant a commit adding a record whose only
        # identifier was an arxiv_id or an isbn was not gated at all -- the
        # record simply fell out of scope, silently and with an OK line.
        if not any(source.get(key) for key in IDENTIFIER_KEYS):
            continue
        targets.append(_target_from(record_path, source))
    return targets


# --------------------------------------------------------------------------
# commands


def _print_verdicts(verdicts, stream=None):
    stream = sys.stdout if stream is None else stream
    by_kind = {}
    for verdict in verdicts:
        by_kind.setdefault(verdict.kind, []).append(verdict)
    for kind in sorted(by_kind):
        group = by_kind[kind]
        print("\n  %4d  %s" % (len(group), kind), file=stream)
        for verdict in group:
            print("        %s" % verdict.path, file=stream)
            print("            %s" % verdict.detail, file=stream)


def cmd_cross_check(args):
    """Corpus-wide DOI<->PMID cross-resolution."""
    cache_dir = Path(args.cache)
    # doi/pmid only, so the "records with an identifier" line keeps printing the
    # 2072 the 2026-08-14 findings doc quotes. The wider population is what
    # --secondary-check reports.
    targets = collect_all_targets(keys=("doi", "pmid"))
    both = [t for t in targets if t["doi"] and t["pmid"]]

    if args.fetch and not args.offline:
        limiter = audit.RateLimiter(audit.NCBI_RATE)
        batch_fetch_pubmed([t["pmid"] for t in both], cache_dir, limiter)

    resolver = Resolver(cache_dir, offline=args.offline,
                        budget=None if args.fetch else args.network_budget)
    verdicts = []
    n_checked = 0
    for target in both:
        if resolver.pubmed_record(target["pmid"]) is None:
            continue
        n_checked += 1
        for verdict in verify_target(target, resolver):
            if verdict.kind.endswith(("doi_pmid_mismatch", "crossview_title_mismatch")):
                verdicts.append(verdict)

    live = [v for v in verdicts if not v.kind.startswith("waived:")]
    waived = [v for v in verdicts if v.kind.startswith("waived:")]

    print("=" * 78)
    print("LITERATURE IDENTIFIER CROSS-RESOLUTION (DOI <-> PMID)")
    print("=" * 78)
    print("records with a doi or pmid      : %d" % len(targets))
    print("records carrying BOTH           : %d" % len(both))
    print("cross-resolved (pmid available) : %d" % n_checked)
    print("conclusive disagreements        : %d" % len(live))
    print("waived (see WAIVERS)            : %d" % len(waived))
    if resolver.skipped:
        print("NOT CHECKED (%d): %s"
              % (len(resolver.skipped),
                 ", ".join("%s [%s]" % s for s in resolver.skipped[:8])))
    if live or waived:
        _print_verdicts(live + waived)

    if args.json:
        Path(args.json).write_text(json.dumps({
            "n_records_with_identifier": len(targets),
            "n_both_identifiers": len(both),
            "n_cross_resolved": n_checked,
            "verdicts": [v.as_dict() for v in live],
            "waived": [v.as_dict() for v in waived],
            "not_checked": [{"identifier": s[0], "why": s[1]}
                            for s in resolver.skipped],
        }, indent=1), encoding="utf-8")
        print("\nwrote %s" % args.json)

    return 1 if (args.exit_nonzero and live) else 0


SECONDARY_KEYS = ("arxiv_id", "pmc", "isbn")


def cmd_secondary_check(args):
    """Whole-corpus sweep of arxiv_id / pmc / isbn.

    THIS IS THE BASELINE MEASUREMENT, and it is the reason the secondary
    verdicts were allowed to block. The standing rule this file follows is that
    a new blocking verdict may not be wired in ahead of a whole-corpus count --
    verdict 3's conjunction was measured at 21/21 true positives and 0 false
    positives before it was trusted, and the gate blocks by default only because
    the corpus number came out at 1 of 2072. Anything measured here that fires
    on more than a handful of correct records has to ship report-only with its
    flip condition stated, or the whole gate gets switched off and protects
    nothing.

    It runs the REPORT-ONLY verdicts as well (``CHECKS_REPORT_ONLY``), because
    the point of the sweep is to see what they WOULD do -- which is exactly how
    verdict 8's false positive was found rather than shipped.
    """
    cache_dir = Path(args.cache)
    targets = collect_all_targets()
    scope = [t for t in targets if any(t.get(k) for k in SECONDARY_KEYS)]

    resolver = Resolver(cache_dir, offline=args.offline,
                        budget=args.network_budget,
                        timeout=None if args.offline else args.timeout,
                        # No per-kind cap on a sweep -- ARXIV_FETCH_BUDGET is a
                        # commit-path protection, and applying it here would
                        # silently truncate the very measurement the gate's
                        # blocking default rests on.
                        arxiv_budget=0)

    verdicts = []
    for target in scope:
        verdicts.extend(verify_target(target, resolver,
                                      extra_checks=CHECKS_REPORT_ONLY))

    live = [v for v in verdicts if not v.kind.startswith("waived:")]
    waived = [v for v in verdicts if v.kind.startswith("waived:")]
    gating = [v for v in live if v.kind not in REPORT_ONLY_KINDS]
    reporting = [v for v in live if v.kind in REPORT_ONLY_KINDS]

    counts = {}
    for key in SECONDARY_KEYS:
        counts[key] = len([t for t in scope if t.get(key)])
    counts["arxiv_id (with an arXiv DOI to cross-resolve)"] = len(
        [t for t in scope if arxiv_id_from_doi(t.get("doi"))])
    counts["pmc (with a pmid to cross-resolve)"] = len(
        [t for t in scope if t.get("pmc") and t.get("pmid")])

    print("=" * 78)
    print("LITERATURE SECONDARY IDENTIFIERS (arxiv_id / pmc / isbn)")
    print("=" * 78)
    print("records with any identifier     : %d" % len(targets))
    print("records in scope here           : %d" % len(scope))
    for label in sorted(counts):
        print("  %-46s : %d" % (label, counts[label]))
    print("GATING verdicts                 : %d" % len(gating))
    print("report-only verdicts            : %d" % len(reporting))
    print("waived                          : %d" % len(waived))
    if resolver.skipped:
        print("NOT CHECKED (%d): %s"
              % (len(resolver.skipped),
                 ", ".join("%s [%s]" % s for s in resolver.skipped[:8])))
    if resolver.errors:
        print("transport failures              : %d (NOT cached; re-run to retry)"
              % len(resolver.errors))
    if gating:
        print("\nGATING (these BLOCK a commit touching the record):")
        _print_verdicts(gating)
    if reporting:
        print("\nREPORT-ONLY (never blocks; see CHECKS_REPORT_ONLY for why):")
        _print_verdicts(reporting)
    if waived:
        print("\nWAIVED:")
        _print_verdicts(waived)

    if args.json:
        Path(args.json).write_text(json.dumps({
            "n_records_with_identifier": len(targets),
            "n_secondary": len(scope),
            "counts": counts,
            "gating": [v.as_dict() for v in gating],
            "report_only": [v.as_dict() for v in reporting],
            "waived": [v.as_dict() for v in waived],
            "not_checked": [{"identifier": s[0], "why": s[1]}
                            for s in resolver.skipped],
            "errors": [{"identifier": e[0], "error": e[1]}
                       for e in resolver.errors],
        }, indent=1), encoding="utf-8")
        print("\nwrote %s" % args.json)

    # Only the GATING verdicts can set exit 1, so a report-only finding cannot
    # be turned into a blocking one by putting --exit-nonzero on this command.
    return 1 if (args.exit_nonzero and gating) else 0


def cmd_gate(args):
    """Scoped check of the records some set of paths implicates."""
    cache_dir = Path(args.cache)
    targets = collect_scoped_targets(args.paths)
    if not targets:
        # An explicit empty scope means "these paths implicate no record with an
        # identifier" -- a no-op. Getting this backwards would make a commit
        # gate sweep the whole corpus on every unrelated commit.
        print("verify_literature_identifiers: OK (0 records with an identifier "
              "in scope)")
        return 0

    resolver = Resolver(cache_dir, offline=args.offline,
                        budget=args.network_budget,
                        timeout=None if args.offline else args.timeout)
    verdicts = []
    for target in targets:
        verdicts.extend(verify_target(target, resolver))

    live = [v for v in verdicts if not v.kind.startswith("waived:")]
    waived = [v for v in verdicts if v.kind.startswith("waived:")]

    if not live:
        note = ""
        if resolver.skipped:
            note = " (%d identifier(s) NOT checked: %s)" % (
                len(resolver.skipped),
                ", ".join(sorted({why for _, why in resolver.skipped})))
        if waived:
            note += " (%d waived)" % len(waived)
        print("verify_literature_identifiers: OK (%d record(s) checked, "
              "0 conclusive findings)%s" % (len(targets), note))
        return 0

    print("verify_literature_identifiers: %d CONCLUSIVE finding(s) in %d of %d "
          "record(s)" % (len(live), len({v.path for v in live}), len(targets)))
    _print_verdicts(live)
    if waived:
        print("\n  %d waived finding(s) (known-undeterminable; see WAIVERS in "
              "%s)" % (len(waived), Path(__file__).name))
    if resolver.skipped:
        print("\n  NOT CHECKED: %d identifier(s) -- %s"
              % (len(resolver.skipped),
                 ", ".join(sorted({why for _, why in resolver.skipped}))))
    return 1 if args.exit_nonzero else 0


PROVENANCE_NOTE_HEADING = "## PROVENANCE NOTE"


def write_pmid_into_record(record_path, pmid, doi, note_line, dry_run=False):
    """Add ``source.pmid`` to a record that has none, plus a summary.md note.

    Refuses rather than overwrites: a record that already carries a PMID is not
    this function's business, and a silent overwrite of an identifier is exactly
    the class of edit the 2026-08-14 findings insist must be verified by round
    trip first. Returns a short status string.

    ``source.pmid`` is inserted immediately after ``source.doi`` because that is
    where every both-identifier record in this corpus carries it -- key order in
    a JSON object is not semantic, but a 1000-record diff that also reshuffles
    key order is a diff nobody reads.
    """
    data = json.loads(Path(record_path).read_text(encoding="utf-8"))
    source = data.get("source") or {}
    if source.get("pmid"):
        return "already_has_pmid"
    if normalise_doi(source.get("doi")) != normalise_doi(doi):
        return "doi_changed_under_us"

    rebuilt = {}
    for key, value in source.items():
        rebuilt[key] = value
        if key == "doi":
            rebuilt["pmid"] = str(pmid)
    if "pmid" not in rebuilt:
        rebuilt["pmid"] = str(pmid)
    data["source"] = rebuilt

    summary_path = Path(record_path).parent / (data.get("summary_path")
                                               or "summary.md")
    if dry_run:
        return "would_write"

    Path(record_path).write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if summary_path.exists():
        text = summary_path.read_text(encoding="utf-8")
        if not text.endswith("\n"):
            text += "\n"
        summary_path.write_text(
            text + "\n" + PROVENANCE_NOTE_HEADING + "\n\n" + note_line + "\n",
            encoding="utf-8")
    return "written"


def cmd_doi_crosswalk(args):
    """The other direction of the crosswalk: ask PubMed which PMID it holds for a DOI.

    Reaches the 1579 DOI-only records that ``--cross-check`` structurally cannot,
    there being nothing in those records to cross-resolve a DOI against.
    """
    cache_dir = Path(args.cache)
    targets = collect_all_targets()
    scope = [t for t in targets if t["doi"] and not t["pmid"]]

    resolver = Resolver(cache_dir, offline=args.offline,
                        budget=args.network_budget,
                        timeout=None if args.offline else args.timeout)

    # Pass A -- esearch only. Kept separate from the evaluation so pass B can be
    # served entirely from cache, which is what makes the esummary half BATCHED
    # (100 ids per request) rather than one request per candidate.
    print("DOI-only records to crosswalk: %d" % len(scope), flush=True)
    candidates = []
    for i, target in enumerate(scope, 1):
        if is_placeholder_doi(target["doi"]):
            continue
        pmids, _ = resolver.pmids_for_doi(target["doi"])
        if pmids and len(pmids) == 1:
            candidates.append(pmids[0])
        if args.progress and i % args.progress == 0:
            print("  esearch %d/%d  (fetched %d, mapped %d)"
                  % (i, len(scope), resolver.spent, len(candidates)), flush=True)

    if candidates and not args.offline:
        batch_fetch_pubmed(candidates, cache_dir,
                           audit.RateLimiter(audit.NCBI_RATE))

    # Pass B -- evaluate, cache-only.
    offline_resolver = Resolver(cache_dir, offline=True)
    results = [crosswalk_doi(t, offline_resolver) for t in scope]

    buckets = {}
    for result in results:
        buckets.setdefault(result["status"], []).append(result)
    # Waivers apply here exactly as they do to every other verdict -- a record
    # adjudicated as undeterminable by governance must not be re-reported as a
    # live finding just because a second route reached it.
    scope_by_rel = {t["rel"]: t for t in scope}
    all_findings = buckets.get("names_a_different_paper", [])
    waived, findings = [], []
    for result in all_findings:
        target = scope_by_rel[result["rel"]]
        (waived if waiver_for(target["entry"], target["doi"], target["pmid"])
         else findings).append(result)
    agreeing = buckets.get("agrees", [])

    print("=" * 78)
    print("LITERATURE DOI -> PMID CROSSWALK (esearch <doi>[AID])")
    print("=" * 78)
    print("records with an identifier      : %d" % len(targets))
    print("DOI-only records (the scope)    : %d" % len(scope))
    for status in sorted(buckets, key=lambda k: -len(buckets[k])):
        print("  %-26s : %d" % (status, len(buckets[status])))
    if resolver.errors:
        print("esearch transport failures      : %d (NOT cached; re-run to retry)"
              % len(resolver.errors))

    for label, group in (("CONCLUSIVE (title AND first author both disagree)",
                          findings),
                         ("WAIVED (see WAIVERS; adjudicated, not re-litigated)",
                          waived)):
        if not group:
            continue
        print("\n%s: %d" % (label, len(group)))
        for result in group:
            print("  %s" % result["rel"])
            print("      doi %s -> pmid %s: %r by %s"
                  % (result["doi"], result["pmid"],
                     (result["pubmed_title"] or "")[:100],
                     result["pubmed_first_author"]))

    # Agreement with one axis dissenting is NOT a finding -- each single-axis
    # disagreement is a documented false-positive class -- but it is the right
    # hand-triage queue, so it is named rather than folded into "agrees".
    soft = [r for r in agreeing if r["title_ok"] is False or r["author_ok"] is False]
    if soft:
        print("\nONE AXIS DISAGREES (not a finding; hand-triage queue): %d" % len(soft))
        for result in soft[:args.show_soft]:
            print("  %s  [title_ok=%s author_ok=%s]"
                  % (result["rel"], result["title_ok"], result["author_ok"]))
            print("      doi %s -> pmid %s: %r by %s"
                  % (result["doi"], result["pmid"],
                     (result["pubmed_title"] or "")[:100],
                     result["pubmed_first_author"]))
        if len(soft) > args.show_soft:
            print("  ... and %d more (--show-soft N, or read --json)"
                  % (len(soft) - args.show_soft))

    written = []
    if args.write_pmid != "none":
        # Only ever writes a PMID that the round trip CONFIRMED and whose title
        # agrees. `unresolvable` is the narrow default and the one with a real
        # coverage argument behind it -- see the findings doc: for a DOI Crossref
        # and doi.org both fail to resolve, the record is currently unreachable
        # by every networked verdict, and a confirmed PMID is the only thing that
        # brings it back inside them. `all` is a derived-pair bulk write and its
        # cost is argued there too.
        stamp = time.strftime("%Y-%m-%d", time.gmtime())
        for result in agreeing:
            if result["title_ok"] is not True or not result["pmid"]:
                continue
            target = next(t for t in scope if t["rel"] == result["rel"])
            if args.write_pmid == "unresolvable":
                view, _ = Resolver(cache_dir, offline=args.offline,
                                   budget=args.network_budget).doi_view(result["doi"])
                if view is not None:
                    continue
            note = ("`source.pmid` was added on %s by "
                    "`scripts/verify_literature_identifiers.py --doi-crosswalk "
                    "--write-pmid`. It is PubMed's own answer to "
                    "`esearch %s[AID]`, round-trip verified: PubMed's "
                    "`articleids` for pmid %s names that same DOI, and the "
                    "PubMed title agrees with the declared title. Provenance "
                    "only -- no `confidence`, `evidence_direction`, `mapping` or "
                    "`claim_ids_tested` field was touched. Note the pair is "
                    "DERIVED from the DOI, so it is not independent "
                    "corroboration of it."
                    % (stamp, result["doi"], result["pmid"]))
            status = write_pmid_into_record(target["path"], result["pmid"],
                                            result["doi"], note,
                                            dry_run=args.dry_run)
            written.append((result["rel"], result["pmid"], status))
        print("\nPMID backfill (%s, mode=%s): %d record(s)"
              % ("DRY RUN" if args.dry_run else "written", args.write_pmid,
                 len(written)))
        for rel, pmid, status in written:
            print("  %-8s %s -> pmid %s" % (status, rel, pmid))

    if args.json:
        Path(args.json).write_text(json.dumps({
            "n_records_with_identifier": len(targets),
            "n_doi_only": len(scope),
            "buckets": {k: len(v) for k, v in buckets.items()},
            "findings": findings,
            "waived": waived,
            "one_axis_disagrees": soft,
            "esearch_errors": [{"identifier": e[0], "error": e[1]}
                               for e in resolver.errors],
            "backfilled": [{"rel": r, "pmid": p, "status": s}
                           for r, p, s in written],
        }, indent=1), encoding="utf-8")
        print("\nwrote %s" % args.json)

    return 1 if (args.exit_nonzero and findings) else 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__.split("\n")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo", default=None,
                        help="REE_assembly repo root (default: this script's "
                             "repo). Same spelling as validate_literature.py's, "
                             "so precommit_literature.sh can hand both stages "
                             "one identical argument list.")
    parser.add_argument("--cross-check", action="store_true",
                        help="corpus-wide DOI<->PMID cross-resolution")
    parser.add_argument("--secondary-check", action="store_true",
                        help="corpus-wide sweep of the secondary identifiers "
                             "(arxiv_id, pmc, isbn), including the REPORT-ONLY "
                             "verdicts. This is the baseline measurement every "
                             "gating verdict had to clear before it was allowed "
                             "to block")
    parser.add_argument("--doi-crosswalk", action="store_true",
                        help="the other direction: ask PubMed which PMID it "
                             "holds for each DOI-only record's DOI "
                             "(esearch '<doi>[AID]')")
    parser.add_argument("--write-pmid", choices=("none", "unresolvable", "all"),
                        default="none",
                        help="with --doi-crosswalk, backfill a confirmed PMID "
                             "into records that carry none. 'unresolvable' "
                             "(the narrow, argued case) writes only where the "
                             "DOI resolves through NEITHER Crossref nor "
                             "doi.org, so the record is currently unreachable "
                             "by every networked verdict; 'all' is a bulk "
                             "derived-pair write (default: none)")
    parser.add_argument("--dry-run", action="store_true",
                        help="with --write-pmid, report what would be written "
                             "and write nothing")
    parser.add_argument("--progress", type=int, default=100, metavar="N",
                        help="print a progress line every N records during the "
                             "esearch pass (0 = silent; default: 100)")
    parser.add_argument("--show-soft", type=int, default=25, metavar="N",
                        help="how many one-axis-disagreement records to print "
                             "(default: 25)")
    parser.add_argument("--paths", nargs="*", metavar="PATH",
                        help="gate mode: check only the records these paths "
                             "implicate (repo-relative or absolute; a "
                             "record.json, or any file in an entry directory)")
    parser.add_argument("--fetch", action="store_true",
                        help="with --cross-check, batch-populate the pubmed "
                             "cache first (unbudgeted)")
    parser.add_argument("--offline", action="store_true",
                        default=os.environ.get("REE_LIT_BIB_OFFLINE") == "1",
                        help="never touch the network; cache only (also "
                             "REE_LIT_BIB_OFFLINE=1, which is how a box with no "
                             "outbound network, and the test suite, keep the "
                             "commit-gate path off the wire without having to "
                             "thread a flag through precommit_literature.sh)")
    parser.add_argument("--cache",
                        default=os.environ.get("REE_LIT_BIB_CACHE")
                        or str(DEFAULT_CACHE),
                        help="response cache directory (also REE_LIT_BIB_CACHE); "
                             "lives outside the repo -- ~2000 API responses are "
                             "not repo content (default: %s)" % DEFAULT_CACHE)
    parser.add_argument("--network-budget", type=int,
                        default=DEFAULT_NETWORK_BUDGET,
                        help="max uncached identifiers to fetch (0 = unlimited); "
                             "whatever is skipped is named, never silently "
                             "dropped (default: %d)" % DEFAULT_NETWORK_BUDGET)
    parser.add_argument("--timeout", type=float, default=GATE_SOCKET_TIMEOUT,
                        help="per-request socket timeout on the gate path "
                             "(default: %.1fs)" % GATE_SOCKET_TIMEOUT)
    parser.add_argument("--json", help="write findings to this path")
    parser.add_argument("--exit-nonzero", action="store_true",
                        help="exit 1 on a conclusive finding (default: exit 0, "
                             "chains safely)")
    args = parser.parse_args(argv)

    if args.repo:
        set_repo(args.repo)
    if args.network_budget == 0:
        args.network_budget = None

    if args.paths is not None:
        return cmd_gate(args)
    if args.secondary_check:
        return cmd_secondary_check(args)
    if args.doi_crosswalk:
        return cmd_doi_crosswalk(args)
    if args.cross_check:
        return cmd_cross_check(args)
    parser.error("one of --cross-check, --secondary-check, --doi-crosswalk or "
                 "--paths is required")


if __name__ == "__main__":
    sys.exit(main())
