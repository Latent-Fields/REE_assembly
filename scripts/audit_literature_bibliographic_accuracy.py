#!/usr/bin/env python3
"""Audit evidence/literature/**/entries/**/record.json for BIBLIOGRAPHIC ACCURACY.

This is a different defect class from ``audit_literature_schema.py`` and neither
can find the other's findings. That one asks: does the record use the declared
keys with the declared types? This one asks: **do the declared fields describe
the paper the record's own identifiers point at?** A record can be 100%
schema-valid and still name the wrong paper.

The confirmed instance (fixed in REE_assembly 77f58c89f7) is the shape to keep
in mind::

    entries/2026-04-05_sd_011_first_second_pain_cortex_timmermann2002/record.json
      title/doi/pmid/venue/volume/issue/pages -> Ploner, Gross, Timmermann &
                                                 Schnitzler (2002) PNAS 99(19)
      source.authors / source.year            -> Timmermann, Ploner, Haucke,
                                                 Schmitz, Baltissen & Schnitzler
                                                 (2001) J Neurophysiol 86(3)

Two papers sharing an author and a topic, conflated by an automated pull.
``year: 2001`` is a valid integer >= 1800, so the schema audit calls it CLEAN.
It surfaced only incidentally.

METHOD. For every record carrying a ``source.doi`` or ``source.pmid``, resolve
the identifier against Crossref (no key needed) or NCBI esummary, and compare
the authoritative record against the declared one on three independent axes:

    year          issued / published-print / published-online / created
    first author  family name of author[0]
    title         normalised similarity ratio

The three axes are compared SEPARATELY and reported together, because the
combination is what triages a finding. Title agrees but authors do not -> the
identifier is right and the provenance fields are wrong (the Ploner shape).
Neither agrees -> the identifier itself may point somewhere else entirely.

A MISMATCH IS A FLAG, NOT A VERDICT. Known-legitimate sources of disagreement,
all observed in this corpus: preprint-vs-journal versions genuinely differ in
year; online-first articles carry a print year one later; some venues backdate;
author-name transliteration varies (Nikulin/Nikoulin); Crossref author lists are
sometimes empty or hold only a consortium name; book chapters and datasets
carry the editor or depositor rather than the author. Every flag needs a human
to look at it before anything is rewritten.

USAGE. Fetching is separated from reporting so a re-run costs nothing and so a
long sweep can be run in foreground chunks::

    audit_literature_bibliographic_accuracy.py --fetch --limit 300   # populate cache
    audit_literature_bibliographic_accuracy.py --report              # read cache only
    audit_literature_bibliographic_accuracy.py --report --json out.json

``--report`` never touches the network, so it is safe to iterate on. The cache
lives OUTSIDE the repo (``--cache``, default ``~/lit_bib_cache``) -- ~2000 API
responses are not repo content, and keeping them out means the audit can be
re-run cheaply without committing a snapshot of two public APIs.

Exit 0 even with findings, so the audit chains safely -- same convention as
``audit_literature_schema.py``, ``audit_stashes.py`` and
``audit_vendored_copies.py``. ``--exit-nonzero`` turns it into a gate; do not
switch that on while a backlog exists.
"""

import argparse
import difflib
import json
import os
import re
import sys
import threading
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LIT_ROOT = REPO / "evidence" / "literature"
DEFAULT_CACHE = Path.home() / "lit_bib_cache"

USER_AGENT = (
    "REE-literature-bibliographic-audit/1.0 "
    "(https://github.com/Latent-Fields/REE_assembly; mailto:nooarche@pm.me)"
)

# Politeness. Crossref's polite pool tolerates far more than this; NCBI without
# an API key is 3 req/s. Stay well under both -- the corpus is only ~2100 ids
# and a slow sweep that nobody has to apologise for is worth the extra minutes.
CROSSREF_RATE = 4.0   # requests/sec, global across threads
NCBI_RATE = 2.0
N_WORKERS = 3


class RateLimiter:
    """Global minimum-interval limiter, shared across worker threads."""

    def __init__(self, per_sec):
        self._interval = 1.0 / per_sec
        self._lock = threading.Lock()
        self._next = 0.0

    def wait(self):
        with self._lock:
            now = time.monotonic()
            if now < self._next:
                delay = self._next - now
            else:
                delay = 0.0
                self._next = now
            self._next += self._interval
        if delay > 0:
            time.sleep(delay)


# --------------------------------------------------------------------------
# name / title normalisation


def strip_accents(text):
    return "".join(
        c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c)
    )


def norm_token(text):
    return re.sub(r"[^a-z]", "", strip_accents(text).lower())


PARTICLES = {
    "van", "von", "de", "der", "den", "del", "della", "di", "da", "dos", "du",
    "la", "le", "el", "al", "bin", "ibn", "ter", "ten", "op", "st",
}


def is_initial(token):
    """True for 'M', 'M.', 'VV', 'J-P' -- an initial cluster, not a surname."""
    bare = re.sub(r"[^A-Za-z]", "", token)
    if not bare:
        return True
    if len(bare) <= 2 and bare.isupper():
        return True
    if len(bare) == 1:
        return True
    if token.endswith(".") and len(bare) <= 3:
        return True
    return False


def name_tokens(name):
    """Candidate surname tokens for one author string.

    The corpus mixes at least three conventions -- 'Nathaniel D. Daw',
    'Colosio M', 'Murray, Lynne' -- so this deliberately returns a SET rather
    than guessing which token is the family name. Matching is by intersection;
    a spurious hit (a given name equal to some other author's surname) makes a
    flag disappear, never appear, so the failure direction is toward silence
    rather than toward noise. Both are checked by a human anyway.
    """
    if not isinstance(name, str):
        return set()
    name = name.strip()
    if not name:
        return set()
    if "," in name:
        name = name.split(",", 1)[0]
    out = set()
    parts = [p for p in re.split(r"[\s]+", name) if p]
    for p in parts:
        if is_initial(p):
            continue
        t = norm_token(p)
        if len(t) >= 2 and t not in PARTICLES:
            out.add(t)
    # Also keep a particle-joined form: 'van der Meer' -> 'vandermeer'.
    joined = norm_token("".join(parts))
    if len(joined) >= 4:
        out.add(joined)
    return out


def norm_title(title):
    if not isinstance(title, str):
        return ""
    t = strip_accents(title).lower()
    t = re.sub(r"<[^>]+>", " ", t)          # crossref titles carry markup
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return " ".join(t.split())


def title_ratio(a, b):
    a, b = norm_title(a), norm_title(b)
    if not a or not b:
        return None
    return difflib.SequenceMatcher(None, a, b).ratio()


# --------------------------------------------------------------------------
# fetching


def cache_path(cache_dir, kind, ident):
    safe = urllib.parse.quote(ident, safe="")
    # DOIs are long and contain slashes; quote() handles it, but keep the
    # filename bounded on filesystems with a 255-byte limit.
    if len(safe) > 180:
        import hashlib

        safe = safe[:120] + "_" + hashlib.sha1(ident.encode()).hexdigest()[:16]
    return Path(cache_dir) / kind / (safe + ".json")


def http_get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", "replace")


def fetch_crossref(doi, cache_dir, limiter):
    path = cache_path(cache_dir, "crossref", doi.lower())
    if path.exists():
        return None
    path.parent.mkdir(parents=True, exist_ok=True)
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    try:
        limiter.wait()
        body = http_get(url)
        payload = {"ok": True, "message": json.loads(body).get("message", {})}
    except urllib.error.HTTPError as exc:
        payload = {"ok": False, "error": "http_%d" % exc.code}
    except Exception as exc:  # network flake, malformed json, timeout
        payload = {"ok": False, "error": type(exc).__name__ + ": " + str(exc)[:200]}
    path.write_text(json.dumps(payload), encoding="utf-8")
    return payload


def fetch_pubmed(pmid, cache_dir, limiter):
    path = cache_path(cache_dir, "pubmed", str(pmid))
    if path.exists():
        return None
    path.parent.mkdir(parents=True, exist_ok=True)
    url = (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        "?db=pubmed&retmode=json&id=" + urllib.parse.quote(str(pmid))
    )
    try:
        limiter.wait()
        body = http_get(url)
        data = json.loads(body)
        rec = data.get("result", {}).get(str(pmid))
        if not rec or "error" in rec:
            payload = {"ok": False, "error": "not_found"}
        else:
            payload = {"ok": True, "message": rec}
    except urllib.error.HTTPError as exc:
        payload = {"ok": False, "error": "http_%d" % exc.code}
    except Exception as exc:
        payload = {"ok": False, "error": type(exc).__name__ + ": " + str(exc)[:200]}
    path.write_text(json.dumps(payload), encoding="utf-8")
    return payload


def load_cached(cache_dir, kind, ident):
    path = cache_path(cache_dir, kind, ident.lower() if kind == "crossref" else str(ident))
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


# --------------------------------------------------------------------------
# authoritative-record extraction


def crossref_view(msg):
    """Normalise a Crossref work into (years, authors, title, venue)."""
    years = []
    for key in ("published-print", "published-online", "issued", "created", "published"):
        node = msg.get(key) or {}
        parts = node.get("date-parts") or []
        if parts and parts[0] and parts[0][0]:
            years.append(int(parts[0][0]))
    authors = []
    for a in msg.get("author") or []:
        fam = a.get("family") or a.get("name") or ""
        if fam:
            authors.append(fam)
    titles = msg.get("title") or []
    container = msg.get("container-title") or []
    return {
        "years": sorted(set(years)),
        "authors": authors,
        "title": titles[0] if titles else "",
        "venue": container[0] if container else "",
        "type": msg.get("type", ""),
        "volume": msg.get("volume"),
        "issue": msg.get("issue"),
        "page": msg.get("page"),
    }


def pubmed_view(rec):
    years = []
    for key in ("pubdate", "epubdate", "sortpubdate"):
        val = rec.get(key) or ""
        m = re.search(r"(1[5-9]\d\d|20\d\d)", str(val))
        if m:
            years.append(int(m.group(1)))
    authors = []
    for a in rec.get("authors") or []:
        nm = a.get("name") or ""
        if nm and a.get("authtype", "Author") == "Author":
            authors.append(nm)
    return {
        "years": sorted(set(years)),
        "authors": authors,
        "title": rec.get("title") or "",
        "venue": rec.get("fulljournalname") or rec.get("source") or "",
        "type": "journal-article",
        "volume": rec.get("volume"),
        "issue": rec.get("issue"),
        "page": rec.get("pages"),
    }


# --------------------------------------------------------------------------


def iter_records():
    for path in sorted(LIT_ROOT.glob("**/entries/**/record.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            yield path, None, str(exc)
            continue
        yield path, data, None


def collect_targets():
    """Every record with a resolvable identifier, plus the ids to fetch."""
    targets = []
    for path, data, err in iter_records():
        if err:
            continue
        src = (data or {}).get("source") or {}
        doi = src.get("doi")
        pmid = src.get("pmid")
        if not doi and not pmid:
            continue
        targets.append({"path": path, "source": src, "doi": doi, "pmid": pmid})
    return targets


def cmd_fetch(args):
    cache_dir = Path(args.cache)
    targets = collect_targets()
    cr_limiter = RateLimiter(CROSSREF_RATE)
    nc_limiter = RateLimiter(NCBI_RATE)

    todo = []
    for t in targets:
        if t["doi"] and not cache_path(cache_dir, "crossref", t["doi"].lower()).exists():
            todo.append(("crossref", t["doi"]))
        elif not t["doi"] and t["pmid"]:
            if not cache_path(cache_dir, "pubmed", str(t["pmid"])).exists():
                todo.append(("pubmed", str(t["pmid"])))
    # De-duplicate: the same DOI legitimately appears in more than one entry.
    seen = set()
    uniq = []
    for kind, ident in todo:
        key = (kind, ident.lower())
        if key in seen:
            continue
        seen.add(key)
        uniq.append((kind, ident))

    print("targets with an identifier: %d" % len(targets))
    print("uncached identifiers      : %d" % len(uniq))
    if args.limit:
        uniq = uniq[: args.limit]
        print("this chunk                : %d" % len(uniq))
    if not uniq:
        print("cache is complete -- nothing to fetch")
        return 0

    done = [0]
    lock = threading.Lock()
    t0 = time.time()

    def work(item):
        kind, ident = item
        if kind == "crossref":
            fetch_crossref(ident, cache_dir, cr_limiter)
        else:
            fetch_pubmed(ident, cache_dir, nc_limiter)
        with lock:
            done[0] += 1
            if done[0] % 50 == 0 or done[0] == len(uniq):
                rate = done[0] / max(1e-6, time.time() - t0)
                print(
                    "  %d/%d  (%.1f/s)" % (done[0], len(uniq), rate),
                    flush=True,
                )

    with ThreadPoolExecutor(max_workers=N_WORKERS) as pool:
        list(pool.map(work, uniq))
    print("fetched %d in %.1fs" % (len(uniq), time.time() - t0))
    return 0


def compare(src, view):
    """Compare a declared source block against an authoritative view."""
    out = {}
    year = src.get("year")
    out["declared_year"] = year
    out["authoritative_years"] = view["years"]
    if isinstance(year, int) and view["years"]:
        out["year_match"] = year in view["years"]
        out["year_delta"] = min(abs(year - y) for y in view["years"])
    else:
        out["year_match"] = None
        out["year_delta"] = None

    declared_authors = src.get("authors") or []
    out["declared_first_author"] = declared_authors[0] if declared_authors else None
    out["authoritative_first_author"] = view["authors"][0] if view["authors"] else None
    if declared_authors and view["authors"]:
        d0 = name_tokens(declared_authors[0])
        a0 = name_tokens(view["authors"][0])
        out["first_author_match"] = bool(d0 & a0)
        # Whole-list overlap: the strongest single signal for a conflation,
        # because two papers sharing one author still differ across the list.
        d_all = set()
        for n in declared_authors:
            d_all |= name_tokens(n)
        a_all = set()
        for n in view["authors"]:
            a_all |= name_tokens(n)
        denom = min(len(declared_authors), len(view["authors"])) or 1
        out["author_overlap"] = round(len(d_all & a_all) / denom, 3)
    else:
        out["first_author_match"] = None
        out["author_overlap"] = None

    ratio = title_ratio(src.get("title"), view["title"])
    out["title_ratio"] = None if ratio is None else round(ratio, 3)
    out["authoritative_title"] = view["title"]
    out["authoritative_venue"] = view["venue"]
    out["authoritative_type"] = view["type"]
    return out


def cmd_report(args):
    cache_dir = Path(args.cache)
    targets = collect_targets()
    rows = []
    unresolved = []
    uncached = []

    for t in targets:
        view = None
        via = None
        if t["doi"]:
            cached = load_cached(cache_dir, "crossref", t["doi"])
            if cached is None:
                # fall through to pubmed if we have one cached
                pass
            elif cached.get("ok"):
                view, via = crossref_view(cached["message"]), "crossref"
            else:
                pm = load_cached(cache_dir, "pubmed", str(t["pmid"])) if t["pmid"] else None
                if pm and pm.get("ok"):
                    view, via = pubmed_view(pm["message"]), "pubmed"
                else:
                    unresolved.append(
                        {
                            "path": str(t["path"].relative_to(REPO)),
                            "doi": t["doi"],
                            "pmid": t["pmid"],
                            "error": cached.get("error"),
                            "title": (t["source"].get("title") or "")[:120],
                        }
                    )
                    continue
        if view is None and t["pmid"]:
            pm = load_cached(cache_dir, "pubmed", str(t["pmid"]))
            if pm and pm.get("ok"):
                view, via = pubmed_view(pm["message"]), "pubmed"
            elif pm is not None:
                unresolved.append(
                    {
                        "path": str(t["path"].relative_to(REPO)),
                        "doi": t["doi"],
                        "pmid": t["pmid"],
                        "error": pm.get("error"),
                        "title": (t["source"].get("title") or "")[:120],
                    }
                )
                continue
        if view is None:
            uncached.append(str(t["path"].relative_to(REPO)))
            continue

        cmp_ = compare(t["source"], view)
        cmp_["path"] = str(t["path"].relative_to(REPO))
        cmp_["doi"] = t["doi"]
        cmp_["pmid"] = t["pmid"]
        cmp_["via"] = via
        cmp_["declared_title"] = t["source"].get("title")
        cmp_["declared_authors"] = t["source"].get("authors")
        cmp_["authoritative_authors"] = view["authors"]
        rows.append(cmp_)

    # Buckets, per the chip brief.
    bucket_a = [
        r for r in rows
        if r["year_match"] is False and r["first_author_match"] is True
    ]
    bucket_b = [r for r in rows if r["first_author_match"] is False]
    bucket_c = unresolved
    year_only_unknown_author = [
        r for r in rows
        if r["year_match"] is False and r["first_author_match"] is None
    ]

    print("=" * 78)
    print("LITERATURE BIBLIOGRAPHIC ACCURACY AUDIT")
    print("=" * 78)
    print("records with an identifier : %d" % len(targets))
    print("resolved and compared      : %d" % len(rows))
    print("still uncached (run --fetch): %d" % len(uncached))
    print()
    print("(a) year mismatch, first author agrees   : %d" % len(bucket_a))
    print("    ... of which delta == 1              : %d"
          % len([r for r in bucket_a if r["year_delta"] == 1]))
    print("    ... of which delta >= 2              : %d"
          % len([r for r in bucket_a if r["year_delta"] and r["year_delta"] >= 2]))
    print("(b) first author differs entirely        : %d" % len(bucket_b))
    print("    ... of which title also disagrees    : %d"
          % len([r for r in bucket_b
                 if r["title_ratio"] is not None and r["title_ratio"] < 0.6]))
    print("(c) identifier does not resolve          : %d" % len(bucket_c))
    print("    year mismatch, no author list to check: %d" % len(year_only_unknown_author))
    print()

    def show(rows_, label, n):
        print("-" * 78)
        print("%s (showing %d of %d)" % (label, min(n, len(rows_)), len(rows_)))
        print("-" * 78)
        for r in rows_[:n]:
            print(r.get("path", r.get("doi")))
            if "declared_year" in r:
                print("   declared    : %s | %s"
                      % (r["declared_year"], r["declared_first_author"]))
                print("   authoritative: %s | %s  (via %s, title_ratio=%s)"
                      % (r["authoritative_years"], r["authoritative_first_author"],
                         r["via"], r["title_ratio"]))
                print("   declared title : %s" % (r["declared_title"] or "")[:110])
                print("   authoritative  : %s" % (r["authoritative_title"] or "")[:110])
            else:
                print("   doi=%s pmid=%s error=%s" % (r["doi"], r["pmid"], r["error"]))
            print()

    if bucket_b:
        show(sorted(bucket_b, key=lambda r: (r["title_ratio"] or 0)),
             "(b) FIRST AUTHOR DIFFERS -- possible wrong-paper conflation", args.show)
    if bucket_a:
        show(sorted(bucket_a, key=lambda r: -(r["year_delta"] or 0)),
             "(a) YEAR MISMATCH, author agrees", args.show)
    if bucket_c:
        show(bucket_c, "(c) IDENTIFIER DOES NOT RESOLVE", args.show)

    if args.json:
        payload = {
            "n_records_with_identifier": len(targets),
            "n_resolved": len(rows),
            "n_uncached": len(uncached),
            "bucket_a_year_mismatch": bucket_a,
            "bucket_b_first_author_differs": bucket_b,
            "bucket_c_unresolved": bucket_c,
            "year_mismatch_no_author_list": year_only_unknown_author,
            "all_rows": rows if args.json_all else [],
        }
        Path(args.json).write_text(json.dumps(payload, indent=1), encoding="utf-8")
        print("wrote %s" % args.json)

    if args.exit_nonzero and (bucket_a or bucket_b or bucket_c):
        return 1
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--fetch", action="store_true", help="populate the cache")
    ap.add_argument("--report", action="store_true", help="report from the cache only")
    ap.add_argument("--limit", type=int, default=0, help="max identifiers per --fetch chunk")
    ap.add_argument("--cache", default=str(DEFAULT_CACHE))
    ap.add_argument("--show", type=int, default=25, help="rows to print per bucket")
    ap.add_argument("--json", help="write the full findings to this path")
    ap.add_argument("--json-all", action="store_true", help="include every compared row")
    ap.add_argument("--exit-nonzero", action="store_true")
    args = ap.parse_args(argv)

    if not args.fetch and not args.report:
        args.report = True
    rc = 0
    if args.fetch:
        rc = cmd_fetch(args) or rc
    if args.report:
        rc = cmd_report(args) or rc
    return rc


if __name__ == "__main__":
    sys.exit(main())
