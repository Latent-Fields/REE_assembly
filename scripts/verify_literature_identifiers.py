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

plus one that needs no network at all:

4. ``placeholder_identifier`` -- ``10.0000/example-doi`` and friends. Cheap,
   syntactic, and there is one in the corpus today.

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

USAGE
-----
    # corpus-wide DOI<->PMID cross-resolution (the audit's recommendation 1)
    verify_literature_identifiers.py --cross-check --fetch
    verify_literature_identifiers.py --cross-check --offline --json out.json

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

    def __init__(self, cache_dir, offline=False, budget=None, timeout=None):
        self.cache_dir = Path(cache_dir)
        self.offline = offline
        self.budget = budget
        self.spent = 0
        self.skipped = []
        self.errors = []
        self.timeout = timeout
        self._crossref = audit.RateLimiter(audit.CROSSREF_RATE)
        self._ncbi = audit.RateLimiter(audit.NCBI_RATE)

    def _may_fetch(self, label):
        if self.offline:
            self.skipped.append((label, "offline"))
            return False
        if self.budget is not None and self.spent >= self.budget:
            self.skipped.append((label, "network budget spent"))
            return False
        self.spent += 1
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
        """(view, via) for a DOI, or (None, reason)."""
        cached = audit.load_cached(self.cache_dir, "crossref", doi)
        if cached is None:
            if not self._may_fetch("doi:%s" % doi):
                return None, "unfetched"
            self._with_timeout(audit.fetch_crossref, doi, self.cache_dir, self._crossref)
            cached = audit.load_cached(self.cache_dir, "crossref", doi)
        if cached and cached.get("ok"):
            return audit.crossref_view(cached["message"]), "crossref"

        # Crossref only knows Crossref-registered DOIs; an arXiv DOI is DataCite
        # and 404s there while being perfectly good. doi.org content negotiation
        # reaches whichever agency owns the prefix.
        neg = audit.load_cached(self.cache_dir, "doiorg", doi)
        if neg is None:
            if not self._may_fetch("doi.org:%s" % doi):
                return None, "unfetched"
            self._with_timeout(audit.fetch_doiorg, doi, self.cache_dir, self._crossref)
            neg = audit.load_cached(self.cache_dir, "doiorg", doi)
        if neg and neg.get("ok"):
            return audit.csl_view(neg["message"]), "doi.org"
        return None, "unresolvable"

    def pubmed_record(self, pmid):
        """The raw esummary record for a PMID, or None."""
        cached = audit.load_cached(self.cache_dir, "pubmed", str(pmid))
        if cached is None:
            if not self._may_fetch("pmid:%s" % pmid):
                return None
            self._with_timeout(audit.fetch_pubmed, str(pmid), self.cache_dir, self._ncbi)
            cached = audit.load_cached(self.cache_dir, "pubmed", str(pmid))
        if cached and cached.get("ok"):
            return cached["message"]
        return None

    def pmid_view(self, pmid):
        rec = self.pubmed_record(pmid)
        return (audit.pubmed_view(rec), "pubmed") if rec else (None, "unresolvable")

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
        if AID_TRANSLATION_MARKER not in (message.get("querytranslation") or ""):
            # Hits from a query PubMed did not read as an identifier lookup.
            # Never seen in this corpus; treated as unusable rather than trusted.
            return None, "untranslated_query"
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
        out["status"] = "unfetched" if why == "unfetched" else (
            "untranslated_query" if why == "untranslated_query" else "esearch_failed")
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


def waiver_for(entry_name, doi=None, pmid=None):
    for waiver in WAIVERS:
        if waiver.get("entry") != entry_name:
            continue
        if waiver.get("doi") and normalise_doi(waiver["doi"]) == normalise_doi(doi):
            return waiver
        if waiver.get("pmid") and str(waiver["pmid"]) == str(pmid or ""):
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


CHECKS_NETWORKED = (
    check_doi_pmid_mismatch,
    check_crossview,
    check_declared_vs_identifier,
)


def verify_target(target, resolver):
    """Every conclusive verdict for one record, waivers applied."""
    verdicts = []
    placeholder = check_placeholder(target)
    if placeholder is not None:
        verdicts.append(placeholder)
    for check in CHECKS_NETWORKED:
        verdict = check(target, resolver)
        if verdict is not None:
            verdicts.append(verdict)

    kept = []
    for verdict in verdicts:
        waiver = waiver_for(target["entry"], target["doi"], target["pmid"])
        if waiver is not None:
            verdict.kind = "waived:" + verdict.kind
            verdict.detail = "%s  [WAIVED: %s]" % (verdict.detail, waiver["reason"])
        kept.append(verdict)
    return kept


# --------------------------------------------------------------------------
# target collection


def _target_from(path, source):
    return {
        "path": path,
        "rel": str(Path(path).relative_to(REPO)) if str(path).startswith(str(REPO))
               else str(path),
        "entry": Path(path).parent.name,
        "source": source,
        "doi": source.get("doi"),
        "pmid": source.get("pmid"),
    }


def collect_all_targets():
    """Every record carrying an identifier. Delegates to the audit's collector."""
    return [_target_from(t["path"], t["source"]) for t in audit.collect_targets()]


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
        if not source.get("doi") and not source.get("pmid"):
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
    targets = collect_all_targets()
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
    print("records with an identifier      : %d" % len(targets))
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
    findings = buckets.get("names_a_different_paper", [])
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

    if findings:
        print("\nCONCLUSIVE (title AND first author both disagree): %d" % len(findings))
        for result in findings:
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
    if args.doi_crosswalk:
        return cmd_doi_crosswalk(args)
    if args.cross_check:
        return cmd_cross_check(args)
    parser.error("one of --cross-check, --doi-crosswalk or --paths is required")


if __name__ == "__main__":
    sys.exit(main())
