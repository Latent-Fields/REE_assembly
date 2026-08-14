#!/usr/bin/env python3
"""Find the SAME PAPER entered under more than one literature record.

This is the fourth literature checker. The other three all ask a question about
ONE record in isolation; this one is the only one that asks a question about the
RELATIONSHIP between records, which is why none of them could ever have found
what it finds:

    validate_literature.py       does the record use the declared keys with the
                                 declared types, and do its filesystem pointers
                                 resolve?  (schema + structure; the commit gate)
    audit_literature_bibliographic_accuracy.py
                                 do the declared fields describe the paper the
                                 identifier points at?  (three axes reported
                                 SEPARATELY for a human to triage; run by hand)
    verify_literature_identifiers.py
                                 is the identifier itself wrong -- CONCLUSIVELY?
                                 (gate-grade verdicts only)
    THIS FILE                    is one study entered TWICE, so that it counts as
                                 two independent evidence items toward the same
                                 claim?  (report only; deduplication is a
                                 governance call, never made here)

WHY IT EXISTS, AND WHY IT COULD NOT HAVE BEEN RUN BEFORE 2026-08-14
-------------------------------------------------------------------
The motivating case is GFLAG-0030. Bekoff (1995), "Play Signals as Punctuation:
the Structure of Social Play in Canids", Behaviour 132:419-429, is entered twice
-- under `targeted_review_devrobotics_play_signals` and under
`targeted_review_arc_049` -- with different confidences (0.72 and 0.88) and
overlapping `claim_ids_tested`. Both reach the derived
`evidence/experiments/claim_evidence.v1.json`, so one paper counts as two
independent evidence items toward ARC-049 and INV-059.

**The duplication was invisible to every identifier-keyed check because the two
records carried two DIFFERENT FABRICATED DOIs for the same work.** It became
findable only once both were repaired to the real
`10.1163/156853995X00649` (audit 2026-08-14, item 3a). ~40 identifiers were
repaired that day, so other pairs may have been exposed by the same repair --
which is the whole reason this scan is worth running now rather than earlier.

THE GROUPING, AND WHY IT IS A UNION RATHER THAN THREE SEPARATE REPORTS
----------------------------------------------------------------------
Records are grouped by three routes and the routes are then UNIONED
transitively, so one work yields one group even when the evidence for it is
mixed:

  1. ``doi``    -- normalised DOI. Reuses ``verify_literature_identifiers.normalise_doi``
                   rather than reimplementing it: case-folding, resolver-prefix
                   stripping and the legacy APA double-slash collapse
                   (``10.1037//0022-006x...``) are all load-bearing, and the
                   last of those is not guessable.
  2. ``pmid``   -- string-normalised PubMed id.
  3. ``title``  -- EXACT normalised title equality (``audit.norm_title``:
                   accent-stripped, markup-stripped, punctuation-collapsed).

The union matters. An arXiv preprint and its journal version carry different
DOIs and the same title; a record with a null DOI and a record with a good one
share only a PMID. Reporting the three routes separately would split one work
into three half-findings, and each route's own report would understate the group
size. Each edge records WHICH route produced it, so a group is auditable back to
its evidence.

WHY FUZZY TITLE MATCHING IS A SEPARATE, UNGRADED SECTION -- MEASURED, NOT ASSUMED
---------------------------------------------------------------------------------
``verify_literature_identifiers.titles_agree`` (subtitle CONTAINMENT in either
direction, then a 0.60 ratio) is reused here, but its output is reported as
``unconfirmed_candidates`` and is deliberately NOT allowed to merge a group or
to produce a ``double_counted`` grade.

That is not caution, it is a measurement. Run as a grouping route over this
corpus it produced 9 groups, of which **7 were plainly different papers by the
same author**:

    Crapse 2008, "Corollary discharge across the animal kingdom" (Nat Rev
      Neurosci) vs "Corollary discharge circuits in the primate brain" (Curr
      Opin Neurobiol)                                        -- ratio route
    Craig 2002, "How do you feel? Interoception: the sense of the physiological
      condition of the body" vs Craig 2003, "Interoception: the sense of the
      physiological condition of the body"                   -- CONTAINMENT route
    Holt-Lunstad 2010 vs 2015; Johnson "Source monitoring" 1993 vs "Reality
      monitoring" 1981; Momennejad 2017 vs 2018; Ploner 2002 vs 2004;
      DiCarlo 2007 vs 2012

Three of those were graded ``double_counted`` on a live claim. The reason is
structural rather than a bad threshold: ``titles_agree`` was built for a
question that already has an anchor -- "this identifier resolves to THIS record,
do the two titles describe one work?" -- where the only variation to absorb is
formatting drift. Duplicate detection has no anchor, so the same predicate is
being asked to distinguish two papers an author wrote on one topic, which it
cannot do. The Craig pair shows containment failing in exactly the way it is
supposed to succeed for the identifier verifier.

Exact-title matching, by contrast, measured clean over the same corpus (21
groups: arXiv/published pairs, null-DOI ML papers, author-name reformatting, and
one genuine near-miss-DOI pair -- Alexander 1986 entered under both
``...002041`` and ``...002001``). So the line is drawn between exact and fuzzy,
not between title and identifier.

Candidates are still worth emitting, so three guards cut the noise without
pretending to resolve it: a pair is dropped when both records carry DIFFERENT
non-null DOIs, or different non-null PMIDs (two registered identifiers are
strong evidence of two works, and it kills all 7 false positives above except
Borbely), or when their years differ by more than ``CANDIDATE_MAX_YEAR_GAP``
(which kills Borbely 1982 vs 2016 while leaving the preprint/published gap
intact). What survives is reported as a question, never as a finding.

The fuzzy pass is BLOCKED ON FIRST-AUTHOR SURNAME rather than run pairwise over
the corpus. That is a cost decision (2189 records is 2.4M difflib ratios
otherwise) but it is also the right correctness frame: the discriminating
negative control -- two genuinely different papers by the same author in the
same year -- lands INSIDE a block, where it is tested rather than avoided.

FINDING STRENGTH: THE INTERSECTION IS THE FINDING, NOT THE GROUP
-----------------------------------------------------------------
A paper legitimately cited by two reviews for two DIFFERENT claims is not a
double-count. It is one study contributing to two claims, which is ordinary and
correct. What is a defect is one study contributing TWICE to the SAME claim. So
every group is graded, and the grade is reported rather than the groups being
merged into one undifferentiated list:

  ``double_counted``  -- some claim_id is named by 2+ records of the group AND
                         at least one of those records reaches
                         claim_evidence.v1.json for it. Real inflation, live in
                         the derived index today.
  ``overlapping``     -- some claim_id is named by 2+ records of the group, but
                         none of them reaches the derived index for it. The
                         defect exists in the corpus but is not currently
                         weighting anything.
  ``disjoint_claims`` -- the same paper, cited for claim sets that do not
                         overlap. Reported because it is worth knowing that the
                         entries describe one study, NOT because it is wrong.

``double_counted_claims`` is per-claim (a claim named by >= 2 of the group's
records), not the whole-group set intersection. For a PAIR the two are the same
thing. For a group of 3+ they are not, and the intersection is the wrong one: a
claim named by 2 of 3 records is double-counted whether or not the third record
also names it, and the all-group intersection silently drops exactly that case.
Both are emitted -- ``claim_intersection`` for continuity with how GFLAG-0030
was described, ``double_counted_claims`` as the actionable set.

CONVENTIONS
-----------
Exit 0 even with findings, so it chains -- same as audit_stashes.py,
audit_vendored_copies.py, validate_literature.py and the two literature checkers
above. ``--exit-nonzero`` is available for a caller that wants to gate on it.

**This is deliberately NOT wired into the commit gate**, and should not be. A
duplicate is a governance question with more than one right answer (merge,
demote one entry's confidence, keep both and mark one non-independent), it is
not repairable by the session that trips over it, and the corpus carries a large
standing population of them -- so a gate here would fire on ordinary unrelated
work and be switched off, which is strictly worse than no gate. Same reasoning
as audit_literature_schema.py and as the audit's own docstring.

No record is read for anything but its `source`, `claim_ids_tested`,
`literature_type`, `confidence` and `evidence_direction`, and nothing is ever
written to a record. Deduplication is a governance decision.

USAGE
-----
    audit_literature_duplicate_entries.py                     # full report
    audit_literature_duplicate_entries.py --only-overlapping  # just the defects
    audit_literature_duplicate_entries.py --json out.json
    audit_literature_duplicate_entries.py --keys doi,pmid     # skip title fuzz
    audit_literature_duplicate_entries.py --exit-nonzero      # gate (not wired)
"""

import argparse
import json
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

# Every normalisation helper is reused from the identifier verifier, which in
# turn reuses the audit's. Reimplementing normalise_doi here would fork the
# legacy-APA double-slash rule, which is the one piece of DOI normalisation
# nobody would think to write from scratch.
import audit_literature_bibliographic_accuracy as audit  # noqa: E402
import verify_literature_identifiers as ident  # noqa: E402

REPO = audit.REPO
DEFAULT_LIT_ROOT = audit.LIT_ROOT
DEFAULT_CLAIM_EVIDENCE = REPO / "evidence" / "experiments" / "claim_evidence.v1.json"

# Routes that MERGE records into a graded group, plus the one that only ever
# proposes a candidate. `title_fuzzy` is listed here so `--keys doi,pmid` turns
# it off along with everything else title-shaped.
GROUPING_KEYS = ("doi", "pmid", "title")
ALL_KEYS = GROUPING_KEYS + ("title_fuzzy",)

# Grades, strongest first. Report order and --only-overlapping both key off this.
GRADE_ORDER = ("double_counted", "overlapping", "disjoint_claims")

# A preprint and its published version are commonly 1-2 years apart in this
# corpus; 34 years apart (Borbely 1982 vs the 2016 "reappraisal") is a different
# paper. Only applied when BOTH records declare a year.
CANDIDATE_MAX_YEAR_GAP = 2


def normalise_pmid(pmid):
    """Comparison form for a PMID. Never used to rewrite a record's field."""
    if pmid is None:
        return None
    text = str(pmid).strip().lower()
    text = text.replace("pmid:", "").strip()
    text = text.lstrip("0") or text
    return text or None


# --------------------------------------------------------------------------
# record collection


def load_records(lit_root):
    """Every literature record, with the fields this scan reasons about.

    Unparseable records are SKIPPED rather than reported: validate_literature.py
    owns that defect and reports it as a schema failure. Duplicating the finding
    here would put the same record in two reports with two different framings.
    """
    records = []
    root = Path(lit_root)
    for path in sorted(root.glob("**/entries/**/record.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if not isinstance(data, dict):
            continue
        source = data.get("source") or {}
        if not isinstance(source, dict):
            source = {}
        try:
            rel = str(path.relative_to(REPO))
        except ValueError:
            rel = str(path)
        authors = source.get("authors") or []
        if not isinstance(authors, list):
            authors = []
        claim_ids = data.get("claim_ids_tested") or []
        if not isinstance(claim_ids, list):
            claim_ids = []
        records.append({
            "path": str(path),
            "rel": rel,
            "entry": path.parent.name,
            "entry_id": data.get("entry_id") or path.parent.name,
            "literature_type": data.get("literature_type"),
            "claim_ids": [str(c) for c in claim_ids],
            "confidence": data.get("confidence"),
            "evidence_direction": data.get("evidence_direction"),
            "title": source.get("title"),
            "authors": [a for a in authors if isinstance(a, str)],
            "year": source.get("year"),
            "venue": source.get("venue"),
            "doi": ident.normalise_doi(source.get("doi")),
            "pmid": normalise_pmid(source.get("pmid")),
        })
    return records


# --------------------------------------------------------------------------
# grouping


class Union:
    """Union-find that remembers WHY each merge happened.

    The route evidence is not decoration. A group merged only by a fuzzy title
    ratio is a materially weaker claim than one merged by an identical DOI, and
    a reader triaging 260 groups needs to see which without re-deriving it.
    """

    def __init__(self, n):
        self.parent = list(range(n))
        self.edges = []

    def find(self, i):
        while self.parent[i] != i:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def union(self, i, j, route, detail):
        self.edges.append({"a": i, "b": j, "route": route, "detail": detail})
        ri, rj = self.find(i), self.find(j)
        if ri != rj:
            self.parent[rj] = ri

    def groups(self):
        buckets = {}
        for i in range(len(self.parent)):
            buckets.setdefault(self.find(i), []).append(i)
        return [sorted(v) for v in buckets.values() if len(v) > 1]


def _link_exact(union, records, field, route):
    """Merge every pair sharing an identical value of one field."""
    seen = {}
    for i, rec in enumerate(records):
        value = rec.get(field)
        if not value:
            continue
        if value in seen:
            union.union(seen[value], i, route, "%s=%s" % (route, value))
        else:
            seen[value] = i


def _title_blocks(records):
    """Block indices by first-author surname token, for the fuzzy title pass.

    ``folded_name_tokens`` returns a SET (the corpus mixes 'Nathaniel D. Daw',
    'Colosio M' and 'Murray, Lynne'), so a record joins every block its first
    author's tokens name. That over-generates blocks rather than under-
    generating them, which is the safe direction: a missed block is a missed
    duplicate, whereas a spurious block only costs comparisons that then fail.

    A record with no usable author token is blocked on its year alone, so a
    duplicate pair with an empty author list is still reachable.
    """
    blocks = {}
    for i, rec in enumerate(records):
        if not rec["title"]:
            continue
        tokens = ident.folded_name_tokens(rec["authors"][0]) if rec["authors"] else set()
        if not tokens:
            tokens = {"year:%s" % rec.get("year")}
        for token in tokens:
            blocks.setdefault(token, []).append(i)
    return blocks


def _link_titles(union, records):
    """Exact normalised-title equality. Measured clean; see the module docstring."""
    exact = {}
    for i, rec in enumerate(records):
        key = audit.norm_title(rec["title"])
        if not key:
            continue
        if key in exact:
            union.union(exact[key], i, "title",
                        "identical normalised title: %r" % key[:90])
        else:
            exact[key] = i


def _identifiers_conflict(a, b):
    """True when the two records carry DIFFERENT non-null DOIs or PMIDs.

    Two separately registered identifiers are strong evidence of two distinct
    works, and this single guard removes 6 of the 7 measured fuzzy-title false
    positives. It is only ever used to SUPPRESS a candidate, never to split a
    group already merged by an exact route -- a shared DOI and a conflicting
    PMID means one identifier is wrong, which is
    verify_literature_identifiers.py's finding, not this file's.
    """
    if a["doi"] and b["doi"] and a["doi"] != b["doi"]:
        return True
    if a["pmid"] and b["pmid"] and a["pmid"] != b["pmid"]:
        return True
    return False


def _years_too_far(a, b):
    try:
        ya, yb = int(a["year"]), int(b["year"])
    except (TypeError, ValueError):
        return False          # a missing/unparseable year cannot suppress
    return abs(ya - yb) > CANDIDATE_MAX_YEAR_GAP


def find_fuzzy_candidates(records, union):
    """Pairs whose titles AGREE fuzzily but which no exact route merged.

    Returns proposals, not findings. Nothing here merges a group or feeds a
    grade -- see the module docstring for the measurement behind that.
    """
    candidates = []
    seen_pairs = set()
    for token, members in sorted(_title_blocks(records).items()):
        if len(members) < 2:
            continue
        for a_pos in range(len(members)):
            for b_pos in range(a_pos + 1, len(members)):
                i, j = members[a_pos], members[b_pos]
                if i > j:
                    i, j = j, i
                if (i, j) in seen_pairs:
                    continue
                seen_pairs.add((i, j))
                if union.find(i) == union.find(j):
                    continue          # already a group by an exact route
                a, b = records[i], records[j]
                if ident.titles_agree(a["title"], b["title"]) is not True:
                    continue
                if _identifiers_conflict(a, b) or _years_too_far(a, b):
                    continue
                ratio = audit.title_ratio(a["title"], b["title"])
                shared = sorted(set(a["claim_ids"]) & set(b["claim_ids"]))
                candidates.append({
                    "block": token,
                    "title_ratio": round(ratio, 3) if ratio is not None else None,
                    "shared_claim_ids": shared,
                    "records": [{
                        "path": rec["rel"],
                        "literature_type": rec["literature_type"],
                        "confidence": rec["confidence"],
                        "claim_ids_tested": sorted(rec["claim_ids"]),
                        "doi": rec["doi"],
                        "pmid": rec["pmid"],
                        "title": rec["title"],
                        "first_author": rec["authors"][0] if rec["authors"] else None,
                        "year": rec["year"],
                        "venue": rec["venue"],
                    } for rec in (a, b)],
                })
    candidates.sort(key=lambda c: (not c["shared_claim_ids"],
                                   -(c["title_ratio"] or 0),
                                   c["records"][0]["path"]))
    return candidates


def build_groups(records, keys=GROUPING_KEYS):
    union = Union(len(records))
    if "doi" in keys:
        _link_exact(union, records, "doi", "doi")
    if "pmid" in keys:
        _link_exact(union, records, "pmid", "pmid")
    if "title" in keys:
        _link_titles(union, records)
    return union


# --------------------------------------------------------------------------
# derived-index cross-reference


def load_claim_evidence(path):
    """(literature_type, entry_id) -> set of claim_ids reaching the derived index.

    Returns None when the index is absent or unreadable, which the caller
    reports rather than treating as "nothing reaches the index" -- silently
    downgrading every finding because a derived artifact was missing would be
    the wrong failure direction for a report whose top grade is defined by it.
    """
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    reach = {}
    for entry in data.get("entries") or []:
        if entry.get("source_type") != "literature":
            continue
        key = (entry.get("experiment_type"), entry.get("run_id"))
        reach.setdefault(key, set()).add(str(entry.get("claim_id")))
    return reach


def _reaches(rec, reach):
    if reach is None:
        return set()
    return reach.get((rec["literature_type"], rec["entry_id"]), set())


# --------------------------------------------------------------------------
# grading


def grade_group(members, records, reach):
    """One group -> the finding dict the report and the JSON both render."""
    group = [records[i] for i in members]

    counts = {}
    for rec in group:
        for claim in set(rec["claim_ids"]):
            counts[claim] = counts.get(claim, 0) + 1
    double_counted = sorted(c for c, n in counts.items() if n > 1)

    claim_sets = [set(rec["claim_ids"]) for rec in group]
    intersection = sorted(set.intersection(*claim_sets)) if claim_sets else []

    live = sorted({claim for claim in double_counted
                   if sum(1 for rec in group if claim in _reaches(rec, reach)) > 1})

    if live:
        grade = "double_counted"
    elif double_counted:
        grade = "overlapping"
    else:
        grade = "disjoint_claims"

    types = sorted({rec["literature_type"] for rec in group if rec["literature_type"]})
    return {
        "grade": grade,
        "size": len(group),
        "same_literature_type": len(types) == 1,
        "literature_types": types,
        "double_counted_claims": double_counted,
        "claim_intersection": intersection,
        "double_counted_claims_live_in_index": live,
        "records": [{
            "path": rec["rel"],
            "entry_id": rec["entry_id"],
            "literature_type": rec["literature_type"],
            "confidence": rec["confidence"],
            "evidence_direction": rec["evidence_direction"],
            "claim_ids_tested": sorted(rec["claim_ids"]),
            "claim_ids_in_derived_index": sorted(_reaches(rec, reach)),
            "doi": rec["doi"],
            "pmid": rec["pmid"],
            "title": rec["title"],
            "first_author": rec["authors"][0] if rec["authors"] else None,
            "year": rec["year"],
        } for rec in group],
    }


def analyse(records, keys=ALL_KEYS, claim_evidence=DEFAULT_CLAIM_EVIDENCE):
    reach = load_claim_evidence(claim_evidence)
    union = build_groups(records, keys)
    candidates = (find_fuzzy_candidates(records, union)
                  if "title_fuzzy" in keys else [])

    by_group = {}
    for edge in union.edges:
        by_group.setdefault(union.find(edge["a"]), []).append(edge)

    findings = []
    for members in union.groups():
        finding = grade_group(members, records, reach)
        edges = by_group.get(union.find(members[0]), [])
        finding["routes"] = sorted({e["route"] for e in edges})
        finding["route_evidence"] = [e["detail"] for e in edges]
        findings.append(finding)

    findings.sort(key=lambda f: (GRADE_ORDER.index(f["grade"]),
                                 -len(f["double_counted_claims"]),
                                 -f["size"],
                                 f["records"][0]["path"]))
    return findings, candidates, reach


# --------------------------------------------------------------------------
# rendering -- ASCII only (CLAUDE.md)


def _fmt_conf(value):
    return "n/a" if value is None else ("%.2f" % value if isinstance(value, (int, float))
                                        else str(value))


def render(findings, candidates, records, reach, only_overlapping=False,
           max_groups=None, stream=None):
    out = sys.stdout if stream is None else stream
    counts = {g: sum(1 for f in findings if f["grade"] == g) for g in GRADE_ORDER}

    print("=" * 78, file=out)
    print("LITERATURE DUPLICATE-ENTRY SCAN (same paper, more than one record)", file=out)
    print("=" * 78, file=out)
    print("records scanned                     : %d" % len(records), file=out)
    print("duplicate groups                    : %d" % len(findings), file=out)
    print("records involved                    : %d"
          % sum(f["size"] for f in findings), file=out)
    print("  double_counted  (live inflation)  : %d" % counts["double_counted"], file=out)
    print("  overlapping     (not in index)    : %d" % counts["overlapping"], file=out)
    print("  disjoint_claims (not a defect)    : %d" % counts["disjoint_claims"], file=out)
    print("unconfirmed fuzzy-title candidates  : %d  (NOT graded -- see below)"
          % len(candidates), file=out)
    if reach is None:
        print("NOTE: claim_evidence.v1.json unreadable -- no group could be graded", file=out)
        print("      double_counted; treat every 'overlapping' as ungraded.", file=out)

    shown = [f for f in findings
             if not only_overlapping or f["grade"] != "disjoint_claims"]
    dropped = 0
    if max_groups is not None and len(shown) > max_groups:
        dropped = len(shown) - max_groups
        shown = shown[:max_groups]

    for finding in shown:
        print("", file=out)
        print("-" * 78, file=out)
        header = "[%s] %d records" % (finding["grade"].upper(), finding["size"])
        if finding["same_literature_type"]:
            header += "  -- ALL IN ONE literature_type (%s)" % finding["literature_types"][0]
        print(header, file=out)
        if finding["double_counted_claims"]:
            print("  double-counted claim(s)   : %s"
                  % ", ".join(finding["double_counted_claims"]), file=out)
        if finding["claim_intersection"] != finding["double_counted_claims"]:
            print("  all-group intersection    : %s"
                  % (", ".join(finding["claim_intersection"]) or "(none)"), file=out)
        if finding["double_counted_claims_live_in_index"]:
            print("  LIVE in claim_evidence    : %s"
                  % ", ".join(finding["double_counted_claims_live_in_index"]), file=out)
        print("  matched via               : %s" % ", ".join(finding["routes"]), file=out)
        for rec in finding["records"]:
            print("    %s" % rec["path"], file=out)
            print("        type=%s conf=%s dir=%s"
                  % (rec["literature_type"], _fmt_conf(rec["confidence"]),
                     rec["evidence_direction"]), file=out)
            print("        claims=%s" % (", ".join(rec["claim_ids_tested"]) or "(none)"),
                  file=out)
            if rec["doi"] or rec["pmid"]:
                print("        doi=%s pmid=%s" % (rec["doi"], rec["pmid"]), file=out)
        for detail in sorted(set(finding["route_evidence"]))[:4]:
            print("  evidence: %s" % detail, file=out)

    if candidates:
        print("", file=out)
        print("=" * 78, file=out)
        print("UNCONFIRMED CANDIDATES (fuzzy title agreement -- NOT a finding)", file=out)
        print("=" * 78, file=out)
        print("These pairs were NOT merged and are NOT graded. Measured over this", file=out)
        print("corpus, most fuzzy-title pairs are different papers by one author", file=out)
        print("(see the module docstring). Each needs a human to confirm or reject.", file=out)
        for cand in candidates:
            print("", file=out)
            print("  ratio=%s  shared claims: %s"
                  % (cand["title_ratio"],
                     ", ".join(cand["shared_claim_ids"]) or "(none)"), file=out)
            for rec in cand["records"]:
                print("    %s" % rec["path"], file=out)
                print("        %r" % (rec["title"] or "")[:96], file=out)
                print("        %s (%s) venue=%s doi=%s"
                      % (rec["first_author"], rec["year"], rec["venue"], rec["doi"]),
                      file=out)

    if dropped:
        # CLAUDE.md, "No silent caps": say what was left out, never truncate quietly.
        print("", file=out)
        print("NOTE: %d further group(s) not shown (--max-groups). Use --json for all."
              % dropped, file=out)
    if only_overlapping and counts["disjoint_claims"]:
        print("", file=out)
        print("NOTE: %d disjoint_claims group(s) hidden by --only-overlapping."
              % counts["disjoint_claims"], file=out)
    return counts


# --------------------------------------------------------------------------


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__.split("\n")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--lit-root", default=str(DEFAULT_LIT_ROOT),
                        help="literature corpus root (default: %(default)s)")
    parser.add_argument("--claim-evidence", default=str(DEFAULT_CLAIM_EVIDENCE),
                        help="derived index used to grade double_counted "
                             "(default: %(default)s)")
    parser.add_argument("--keys", default=",".join(ALL_KEYS),
                        help="comma-separated grouping routes from %s "
                             "(default: all)" % ",".join(ALL_KEYS))
    parser.add_argument("--only-overlapping", action="store_true",
                        help="hide disjoint_claims groups (same paper, different "
                             "claims -- reported by default because it is worth "
                             "knowing, but it is not a defect)")
    parser.add_argument("--max-groups", type=int, default=None,
                        help="cap the number of groups printed; whatever is "
                             "dropped is named, never silently truncated")
    parser.add_argument("--json", help="write the full findings to this path")
    parser.add_argument("--exit-nonzero", action="store_true",
                        help="exit 1 when any double_counted or overlapping "
                             "group exists; unconfirmed candidates never gate "
                             "(default: exit 0, chains safely)")
    args = parser.parse_args(argv)

    keys = tuple(k.strip() for k in args.keys.split(",") if k.strip())
    unknown = [k for k in keys if k not in ALL_KEYS]
    if unknown:
        parser.error("unknown --keys value(s): %s (choose from %s)"
                     % (", ".join(unknown), ", ".join(ALL_KEYS)))

    records = load_records(args.lit_root)
    findings, candidates, reach = analyse(records, keys=keys,
                                          claim_evidence=args.claim_evidence)
    counts = render(findings, candidates, records, reach,
                    only_overlapping=args.only_overlapping,
                    max_groups=args.max_groups)

    if args.json:
        Path(args.json).write_text(json.dumps({
            "n_records": len(records),
            "keys": list(keys),
            "claim_evidence_readable": reach is not None,
            "counts": counts,
            "n_unconfirmed_candidates": len(candidates),
            "groups": findings,
            "unconfirmed_candidates": candidates,
        }, indent=1), encoding="utf-8")
        print("\nwrote %s" % args.json)

    if args.exit_nonzero and (counts["double_counted"] or counts["overlapping"]):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
