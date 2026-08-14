#!/usr/bin/env python3
"""One-shot: normalise the residual literature drift INSIDE the `source` object.

Third and last pass of the 2026-08-14 literature reconciliation:

  f9a5ea65c0  widened `source` where corpus usage showed a real convention
              (605 -> 107 failures of 2189), and wrote the DIRECTION into the
              schema's own `source` description.
  6368e3129f  normalised everything OUTSIDE `source`      (107 -> 37).
  4e2ec3d24a  ditto.
  (siblings)  folded the nested `source.citation` block into the declared
              fields, and resolved the null `source.year`  (37 -> 16).
  THIS PASS   the residual 16, all inside `source`.

Nothing here is an open judgment about DIRECTION. f9a5ea65c0 already settled it
in the schema text, and this pass only applies it:

  (a) denormalised renderings of fields declared separately -- a merged
      `volume_pages`, a `pubmed_url` that is a URL spelling of `pmid` -- are
      SPLIT BACK ONTO the declared fields, losslessly.
  (b) prose -- provenance notes, metadata corrections, retrieval caveats,
      code/data availability -- moves to the entry's summary.md.

The one place this pass DID have to decide is the 2026-08-01 identifier
cluster; see `fix_availability` for the reasoning and the evidence, because
that decision is the one a later session is most likely to want to revisit.

Idempotent: re-running is a no-op. `--dry-run` prints the plan and writes
nothing. Prose moved to summary.md is appended under the same dated marker the
sibling pass used, and the marker is what makes the move detectable on a re-run
-- `append_summary` is IMPORTED from that pass rather than reimplemented, so
the two cannot drift into writing different markers.
"""

import argparse
import json
import re
import sys
from pathlib import Path

# Reuse the sibling pass's summary.md writer + marker rather than restating
# them. A second copy would silently diverge on the marker string, and the
# marker is the whole idempotency mechanism.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from normalize_literature_drift_2026_08_14 import (  # noqa: E402
    MARKER, append_summary, records, save,
)

REPO = Path(__file__).resolve().parent.parent
LIT = REPO / "evidence" / "literature"

assert MARKER  # imported for provenance; append_summary writes it


# --------------------------------------------------------------------------
# (a) volume_pages -- 5 records, ONE dir, 2026-06-05
# --------------------------------------------------------------------------

# `114:58-66` and `24(7):964-974`. Anchored and total over the 5 live values;
# a value that does not match is REPORTED and skipped, never guessed at.
VOLUME_PAGES_RE = re.compile(r"^(\d+)(?:\((\d+)\))?:(\d+(?:-\d+)?)$")


def fix_volume_pages(dry, log):
    """A merged in-publication locator, split back onto the declared fields.

    The schema names this exact shape as rejected -- "denormalised renderings
    of fields already declared separately (... a merged `volume_pages`)" -- and
    declares `volume`, `issue` and `pages` to receive the parts. So this is
    mechanical, not a judgment.

    The three targets are asserted ABSENT-or-null before writing. All five live
    records carry them as explicit nulls (the corpus's "checked, none exists"
    spelling), so a non-null target would mean the merged string CONTRADICTS a
    declared field -- stop and report rather than pick a side.
    """
    for path, rec in records():
        src = rec.get("source")
        if not isinstance(src, dict) or "volume_pages" not in src:
            continue
        raw = str(src["volume_pages"]).strip()
        m = VOLUME_PAGES_RE.match(raw)
        if not m:
            log(f"volume_pages SKIPPED (unparseable {raw!r})", path)
            continue
        volume, issue, pages = m.groups()
        parts = {"volume": volume, "issue": issue, "pages": pages}
        conflict = [k for k, v in parts.items()
                    if v is not None and src.get(k) is not None and str(src[k]) != v]
        if conflict:
            log(f"volume_pages SKIPPED (conflicts with declared {conflict})", path)
            continue
        src.pop("volume_pages")
        for key, value in parts.items():
            if value is None:
                src.pop(key, None)  # no issue in the merged string -> do not assert one
            else:
                src[key] = value
        save(path, rec, dry)
        log("volume_pages -> volume/issue/pages", path)


# --------------------------------------------------------------------------
# (b) pubmed_url -- 1 record, 2026-08-01
# --------------------------------------------------------------------------

PUBMED_URL_RE = re.compile(r"^https?://pubmed\.ncbi\.nlm\.nih\.gov/(\d+)/?$")


def fix_pubmed_url(dry, log):
    """A URL spelling of `pmid`, which IS declared. Collapse onto it.

    Same class as the `source.citation` block a sibling pass folded: the value
    is not new information, it is a rendering of a declared field. `pmid` is
    documented in the schema as "the primary verification handle for a
    biomedical source", and this record had none while carrying the id inside a
    URL -- so the collapse ADDS the machine-readable handle rather than costing
    one. The URL form is not preserved: it is reconstructible from the pmid,
    which is exactly what makes it denormalised.
    """
    for path, rec in records():
        src = rec.get("source")
        if not isinstance(src, dict) or "pubmed_url" not in src:
            continue
        raw = str(src["pubmed_url"]).strip()
        m = PUBMED_URL_RE.match(raw)
        if not m:
            log(f"pubmed_url SKIPPED (unrecognised {raw!r})", path)
            continue
        pmid = m.group(1)
        if src.get("pmid") not in (None, pmid):
            log(f"pubmed_url SKIPPED (conflicts with pmid {src['pmid']!r})", path)
            continue
        src.pop("pubmed_url")
        src["pmid"] = pmid
        save(path, rec, dry)
        log(f"pubmed_url -> pmid {pmid}", path)


# --------------------------------------------------------------------------
# (c) prose in `source` -- 7 records, 4 dirs, 2026-02-27..2026-07-18
# --------------------------------------------------------------------------

PROSE_HEADINGS = {
    "note": "Source note (from record.json)",
    "notes": "Source note (from record.json)",
    "citation_note": "Citation caveat (from record.json)",
    "metadata_note": "Metadata note (from record.json)",
}

# An in-publication locator sitting INSIDE one of those prose values, for the
# two records where the prose opens with (or contains) a full, unambiguous
# citation rendering while the declared locator fields are empty.
#
# Deliberately an explicit per-record table asserted against the live text,
# NOT a regex swept over arbitrary prose. Two records is not enough to justify
# a general extractor, and a general extractor over free text is precisely how
# a page range gets invented. If the asserted substring is absent -- because
# the prose was edited since -- this DIES rather than guessing.
LOCATORS = {
    "targeted_review_arc_022/entries/"
    "2026-04-04_arc_022_corticocortical_loops_prediction_residuals_mumford1992": {
        "assert": "Biological Cybernetics 66(3):241-251.",
        "volume": "66", "issue": "3", "pages": "241-251",
    },
    "targeted_review_q_019/entries/2026-02-27_q019_crick_1984": {
        # en-dash in the prose; corpus `pages` convention is a plain hyphen.
        "assert": "PNAS 81(14):4586–4590, 1984",
        "volume": "81", "issue": "14", "pages": "4586-4590",
    },
}


def fix_source_prose(dry, log):
    """Prose out of `source`, into summary.md -- the schema's stated convention.

    "prose -- provenance notes, metadata corrections, retrieval caveats --
    ... belong in the entry's summary.md, the dominant corpus convention."

    All seven values are exactly that: two PMID corrections, a PubMed-outage
    metadata caveat, an unverified-citation caveat, a related-works pointer, a
    conference-version note, and a lineage note about a predecessor paper.
    They move VERBATIM -- nothing is summarised, so the move is reversible.

    Before the move, a locator listed in LOCATORS is folded onto the declared
    `volume`/`issue`/`pages`. That is the same collapse as `volume_pages`
    above, just with the merged string embedded in a sentence: keeping the
    prose while ALSO leaving the declared fields empty would discard structured
    data the record already holds. The prose still moves in full, so the
    provenance narrative these two values are actually about stays intact.
    """
    for path, rec in records():
        src = rec.get("source")
        if not isinstance(src, dict):
            continue
        present = [k for k in PROSE_HEADINGS if k in src]
        if not present:
            continue

        key = str(path.parent.relative_to(LIT))
        loc = LOCATORS.get(key)
        if loc:
            blob = " ".join(str(src[k]) for k in present)
            if loc["assert"] not in blob:
                raise SystemExit(
                    f"LOCATORS entry for {key} no longer matches the record prose "
                    f"(expected {loc['assert']!r}); re-verify before folding."
                )
            for field in ("volume", "issue", "pages"):
                if src.get(field) is not None and str(src[field]) != loc[field]:
                    raise SystemExit(
                        f"{key}: prose locator {field}={loc[field]!r} contradicts "
                        f"declared {field}={src[field]!r}; resolve by hand."
                    )
                src[field] = loc[field]
            log("prose locator -> volume/issue/pages", path)

        # `note` and `notes` share a heading, and append_summary dedupes on
        # (heading, marker) -- so two same-heading fields on one record would
        # pop both and write only the first. No live record has that shape;
        # assert it rather than trust it, because the loss would be silent.
        headings = [PROSE_HEADINGS[f] for f in present]
        if len(set(headings)) != len(headings):
            raise SystemExit(
                f"{path}: fields {present} share a summary.md heading; merge them "
                f"by hand -- appending both under one heading would drop one."
            )
        for field in present:
            append_summary(path.parent, PROSE_HEADINGS[field], str(src.pop(field)), dry)
            log(f"source.{field} -> summary.md", path)
        save(path, rec, dry)


# --------------------------------------------------------------------------
# (d) the 2026-08-01 identifier cluster -- 4 records, 4 dirs, ONE date
# --------------------------------------------------------------------------

# Rendered as a labelled list in summary.md. Order is the display order.
AVAILABILITY_LABELS = [
    ("preprint_doi", "Preprint DOI"),
    ("pubmed_preprint", "Preprint PMID"),
    ("pmcid_preprint", "Preprint PMC ID"),
    ("code_repository", "Code"),
    ("code_url", "Code"),
    ("zenodo", "Data (Zenodo)"),
    ("data_url", "Data"),
    ("data_repositories", "Data"),
    ("data_and_code", "Data and code"),
    ("license", "License"),
    ("secondary_trigger", "Secondary trigger (how this paper surfaced)"),
]


def fix_availability(dry, log):
    """The one REAL judgment in this pass. Both halves normalise; here is why.

    By the enumeration rule in ``audit_literature_schema.py`` this whole cluster
    is drift on its face -- 12 distinct keys, 4 directories, a SINGLE date
    (2026-08-01), never used before or since. But the rule is a heuristic, and
    half of these keys are stable external identifiers, which is a category
    `source` exists to hold. So the two halves were checked SEPARATELY against
    the corpus rather than dispatched together.

    HALF 1 -- preprint identifiers (`preprint_doi` x2, `pubmed_preprint`,
    `pmcid_preprint`). NORMALISED, i.e. the schema is NOT widened, for two
    reasons that are independent of the date-cluster heuristic:

      * SCOPE. `source` is declared as "bibliographic provenance for the CITED
        WORK". A preprint DOI identifies a DIFFERENT artifact -- an earlier
        version -- and all four records cite the journal version (`doi`
        10.1038/...). Declaring `preprint_*` beside `doi`/`pmid`/`pmc` would
        make `source` hold identifiers for two works at once, with nothing in
        the key names saying which is which for a consumer.
      * CONVENTION, measured over the whole corpus, not sampled. 33 records
        outside this cluster carry preprint information -- and every one of
        them carries it as PROSE (`confidence_rationale`, `mapping`, or
        summary.md); 37 summary.md files mention a preprint or bioRxiv. Only
        these 4 records use a dedicated `source` key. Separately, the 8 records
        whose cited work genuinely IS the preprint simply put the 10.1101 DOI
        in `doi`, which is the already-declared way to cite a preprint.

    HALF 2 -- code/data availability, license, and the press link that
    triggered the pull (`code_repository`, `code_url`, `zenodo`, `data_url`,
    `data_repositories`, `data_and_code`, `license`, `secondary_trigger`).
    NORMALISED, and this half is not close: none of it is bibliographic
    provenance for the cited work. `secondary_trigger` is provenance about the
    PULL SESSION, not about the paper at all. Note the shape of the drift
    itself -- four records on one day produced `code_repository` AND `code_url`
    for the same concept, and `zenodo` / `data_url` / `data_repositories` /
    `data_and_code` for another. Four spellings of one field in one session is
    what an unsettled convention looks like; blessing any one of them would be
    picking a winner among synonyms coined the same afternoon.

    NOTHING IS LOST -- every value moves verbatim into summary.md under a
    labelled list, including the full 9-entry `data_repositories` array. If a
    later session wants these machine-readable, the case to make is a
    corpus-wide convention (or a separate `availability` object with its own
    scoping sentence), not a re-litigation of these four records.
    """
    for path, rec in records():
        src = rec.get("source")
        if not isinstance(src, dict):
            continue
        present = [(k, label) for k, label in AVAILABILITY_LABELS if k in src]
        if not present:
            continue
        lines = []
        for key, label in present:
            value = src.pop(key)
            if isinstance(value, list):
                lines.append(f"- {label} (`{key}`):")
                lines.extend(f"  - {v}" for v in value)
            else:
                lines.append(f"- {label} (`{key}`): {value}")
        append_summary(path.parent, "Availability and source identifiers (from record.json)",
                       "\n".join(lines), dry)
        save(path, rec, dry)
        log(f"availability x{len(present)} -> summary.md", path)


STEPS = {
    "volume_pages": fix_volume_pages,
    "pubmed_url": fix_pubmed_url,
    "prose": fix_source_prose,
    "availability": fix_availability,
}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", action="append", choices=sorted(STEPS),
                    help="run only these steps (repeatable)")
    args = ap.parse_args()

    counts = {}

    def log(label, path):
        counts[label] = counts.get(label, 0) + 1
        print(f"  {label:42s} {path.relative_to(LIT)}")

    for name in (args.only or list(STEPS)):
        print(f"== {name}")
        STEPS[name](args.dry_run, log)

    print("\n== summary" + (" (DRY RUN -- nothing written)" if args.dry_run else ""))
    for label, n in sorted(counts.items()):
        print(f"  {n:4d}  {label}")
    if not counts:
        print("  (nothing to do)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
