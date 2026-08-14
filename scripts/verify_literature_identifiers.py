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
structurally cannot see. Those 7 findings are recorded in
evidence/planning/literature_identifier_cross_resolution_findings_2026-08-14.md
and are deliberately NOT waived -- they are repairable, and a waiver list that
absorbs repairable defects is how a gate stops meaning anything.

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
    which is why verdict 2 needs it as much as verdict 3 does.
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
    """
    na, nb = audit.norm_title(a), audit.norm_title(b)
    if not na or not nb:
        return None
    short, long_ = (na, nb) if len(na) <= len(nb) else (nb, na)
    if len(short) >= TITLE_CONTAINMENT_MIN_CHARS and short in long_:
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
            "Audit 2026-08-14 'Left unrepaired' item 1: the DOI resolves to "
            "Christie, 'Exercising some control over the hippocampus' (2009). "
            "The declared title matches Hyman et al. but neither the year nor "
            "the DOI disambiguates WHICH Hyman paper, and the record carries no "
            "PMID to cross-resolve against. Undeterminable, not unrepaired."
        ),
    },
    {
        "entry": "2026-05-16_q035_arc049_murray_trevarthen_1985_double_video",
        "doi": "10.1163/156853995X00822",
        "reason": (
            "Audit 2026-08-14 'Left unrepaired' item 2: book chapter whose DOI "
            "resolves to an unrelated work; Crossref's proposed Routledge "
            "reprint DOI was clearly wrong ('Intonation in Discourse'). Needs a "
            "human judgement about which edition the entry means."
        ),
    },
    {
        "entry": "2026-05-16_arc049_inv059_gergely_watson1996_social_biofeedback",
        "doi": "10.1163/156853995X00101",
        "reason": (
            "Audit 2026-08-14 'Left unrepaired' item 2: same shape as the "
            "Murray & Trevarthen chapter above -- chapter-level DOI for a "
            "reprinted classic, resolves to an unrelated work."
        ),
    },
]


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


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__.split("\n")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cross-check", action="store_true",
                        help="corpus-wide DOI<->PMID cross-resolution")
    parser.add_argument("--paths", nargs="*", metavar="PATH",
                        help="gate mode: check only the records these paths "
                             "implicate (repo-relative or absolute; a "
                             "record.json, or any file in an entry directory)")
    parser.add_argument("--fetch", action="store_true",
                        help="with --cross-check, batch-populate the pubmed "
                             "cache first (unbudgeted)")
    parser.add_argument("--offline", action="store_true",
                        help="never touch the network; cache only")
    parser.add_argument("--cache", default=str(DEFAULT_CACHE))
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

    if args.network_budget == 0:
        args.network_budget = None

    if args.paths is not None:
        return cmd_gate(args)
    if args.cross_check:
        return cmd_cross_check(args)
    parser.error("one of --cross-check or --paths is required")


if __name__ == "__main__":
    sys.exit(main())
