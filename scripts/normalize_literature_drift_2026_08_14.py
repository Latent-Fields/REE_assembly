#!/usr/bin/env python3
"""One-shot: normalise literature record drift OUTSIDE the `source` object.

Companion to the 2026-08-14 ``source`` reconciliation (REE_assembly f9a5ea65c0),
which widened the schema where corpus usage showed a real convention. This pass
handles the residual drift, and the enumeration in
``scripts/audit_literature_schema.py --drift`` pointed the OTHER way for almost
all of it: every field below is confined to ONE ``literature_type`` directory
from ONE pull session on ONE date, and none has been used since. That is drift,
so the records are normalised onto the existing convention rather than the
schema being widened to bless a one-off.

The single exception -- ``evidence_direction_per_claim`` -- is handled by
widening the schema instead, because it is not local drift: it is an
established cross-corpus convention, mandated by CLAUDE.md for EXPERIMENT
manifests carrying more than one claim, consumed by ``serve.py`` and by the
indexer's experiment path. See the schema description for that field.

Idempotent: re-running is a no-op. ``--dry-run`` prints the plan and writes
nothing. Prose moved to ``summary.md`` is appended under a dated marker, and the
marker is what makes the move detectable on a re-run.
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LIT = REPO / "evidence" / "literature"
MARKER = "<!-- normalized-from-record-json 2026-08-14 -->"


def load(path):
    return json.loads(path.read_text())


def save(path, rec, dry):
    if not dry:
        path.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n")


def slugify(value):
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", str(value).lower())).strip("_")


def add_tag(rec, tag):
    tags = rec.setdefault("tags", [])
    if tag not in tags:
        tags.append(tag)


def append_summary(entry_dir, heading, body, dry):
    """Append prose to the entry's summary.md under a dated marker."""
    summary = entry_dir / "summary.md"
    if not summary.exists():
        raise SystemExit(f"no summary.md to receive prose: {summary}")
    text = summary.read_text()
    block = f"\n{MARKER}\n\n## {heading}\n\n{body.strip()}\n"
    if heading in text and MARKER in text:
        return False
    if not dry:
        summary.write_text(text.rstrip() + "\n" + block)
    return True


def records(pattern="*/entries/*/record.json"):
    for path in sorted(LIT.glob(pattern)):
        yield path, load(path)


# --------------------------------------------------------------------------
# (a) top-level annotation fields -- fold into `tags`, or move prose to summary
# --------------------------------------------------------------------------

def fix_class_surveyed(dry, log):
    """12 records, one dir, 2026-07-14. A survey-class label -> a prefixed tag.

    `prefix:value` is already a corpus tag convention (`candidate:...` in
    targeted_review_proxy_progress_goal_maintenance), so this keeps the value
    recoverable rather than dissolving it into free tags.
    """
    for path, rec in records():
        if "class_surveyed" not in rec:
            continue
        add_tag(rec, f"class_surveyed:{slugify(rec.pop('class_surveyed'))}")
        save(path, rec, dry)
        log("class_surveyed", path)


def fix_support_tag(dry, log):
    """7 records, one dir, 2026-04-26. Value carries real content not in `tags`."""
    for path, rec in records():
        if "support_tag" not in rec:
            continue
        add_tag(rec, f"support_tag:{slugify(rec.pop('support_tag'))}")
        save(path, rec, dry)
        log("support_tag", path)


def fix_tag(dry, log):
    """6 records, one dir, 2026-04-26. PURE DUPLICATION -- delete, losslessly.

    Every value ('a'/'b'/'c') is already present in `tags` in expanded form
    (`tag_a_direct_support`, `tag_b_liking_encoding`, ...). Asserted below
    rather than assumed: a record whose letter is NOT already in `tags` is left
    alone and reported, so a silent data loss is impossible.
    """
    for path, rec in records():
        if "tag" not in rec:
            continue
        letter = str(rec["tag"]).strip().lower()
        expanded = [t for t in rec.get("tags", []) if t.startswith(f"tag_{letter}_")]
        if not expanded:
            log("tag SKIPPED (not duplicated in tags)", path)
            continue
        rec.pop("tag")
        save(path, rec, dry)
        log(f"tag (dup of {expanded[0]})", path)


def fix_prose_fields(dry, log):
    """retag_note (3), evidence_direction_correction_note (2), metadata_correction (1).

    All are audit-trail prose about an edit made to the record itself. The
    schema's `source` description already states the corpus convention for
    exactly this class of content -- "prose -- provenance notes, metadata
    corrections, retrieval caveats -- belong in the entry's summary.md" -- and
    this applies the same rule one level up. Confirmed by the newest instance:
    `metadata_correction` in targeted_review_connectome_mech_100 duplicates a
    far fuller correction block already written into that entry's summary.md,
    i.e. the summary.md convention was followed and the record field added on
    top of it.
    """
    HEADINGS = {
        "retag_note": "Retagging note",
        "evidence_direction_correction_note": "Evidence-direction correction",
        "metadata_correction": "Metadata correction",
    }
    for path, rec in records():
        for field, heading in HEADINGS.items():
            if field not in rec:
                continue
            value = rec.pop(field)
            body = value if isinstance(value, str) else (
                "```json\n" + json.dumps(value, indent=2, ensure_ascii=False) + "\n```"
            )
            append_summary(path.parent, heading, body, dry)
            save(path, rec, dry)
            log(field, path)


# --------------------------------------------------------------------------
# (b) bespoke confidence_components -- 11 records, 2026-04-04..2026-04-21
# --------------------------------------------------------------------------

CANON = {"source_quality", "mapping_fidelity", "transfer_risk"}


def fix_confidence_components(dry, log):
    """2132 of 2143 records with the object use the canonical three EXACTLY.

    The three are also a specified required output of
    `evidence/planning/scripts/build_connectome_literature_pull.py`. So the
    convention is not in doubt and the schema is NOT weakened to admit 11
    records from a dead 17-day April window.

    The decomposition is preserved verbatim in `confidence_rationale` rather
    than mapped onto the canonical three. Mapping would require inventing
    numbers -- and in one direction inverting them, since `transfer_risk` is a
    RISK (higher is worse) while the bespoke `species_relevance_to_human` is a
    relevance (higher is better). Re-scoring evidence is a governance
    adjudication, not a schema fix, so nothing numeric is invented here.
    `confidence` itself -- the field consumers actually read -- is untouched.
    """
    for path, rec in records():
        comps = rec.get("confidence_components")
        if not isinstance(comps, dict):
            continue
        if CANON <= (set(comps) - {"notes"}):
            continue  # canonical (possibly plus notes) -- leave alone
        rendered = ", ".join(
            f"{k} {v}" for k, v in comps.items() if k != "notes" and isinstance(v, (int, float))
        )
        note = str(comps.get("notes", "")).strip()
        addendum = (
            "Confidence decomposition as originally recorded (domain-specific "
            f"components, not the canonical source_quality/mapping_fidelity/transfer_risk): {rendered}."
        )
        if note:
            addendum += f" {note}"
        rec["confidence_rationale"] = (
            str(rec.get("confidence_rationale", "")).strip() + " " + addendum
        ).strip()
        rec.pop("confidence_components")
        save(path, rec, dry)
        log("confidence_components (bespoke)", path)


# --------------------------------------------------------------------------
# (c) pre-contract records -- targeted_review_mech_059, 2026-04-04
# --------------------------------------------------------------------------

CITATION_TO_SOURCE = {
    "journal": "venue", "arXiv": "arxiv_id", "arxiv": "arxiv_id",
    "title": "title", "authors": "authors", "year": "year",
    "doi": "doi", "pmid": "pmid", "url": "url",
    "volume": "volume", "issue": "issue", "pages": "pages",
}


def _reorder_author(name):
    """'Kendall, Alex' -> 'Alex Kendall'. Corpus convention is 'First Last'."""
    if name.count(",") == 1:
        last, first = (p.strip() for p in name.split(","))
        if first and first.lower() not in {"jr", "sr", "et al", "et al."}:
            return f"{first} {last}"
    return name


def fix_pre_contract(dry, log):
    """5 records predating the v1 contract entirely: no `source`, no
    `evidence_class`, no `confidence`, no `confidence_rationale`.

    MIGRATED to the contract, not accommodated by it. Every field is derived
    mechanically from what the record already holds:

      citation{journal,arXiv,...}  -> source{venue,arxiv_id,...}
      evidence_type               -> evidence_class
      notes                       -> confidence_rationale
      relevance_to_claim          -> mapping.ree_translation
      key_quotes                  -> summary.md

    `confidence` is the one required field with no source in the record. It is
    set to **0.6 -- the exact value `build_experiment_indexes.py` already
    substitutes** for a literature record with no `confidence`
    (`_normalize_confidence(record.get("confidence"), default=0.6)`), so the
    migration is evidence-NEUTRAL: `claim_evidence.v1.json` sees the same
    number after as before. Deriving a number from `evidence_strength`
    ("strong"/"moderate") instead would silently re-weight MECH-059's evidence,
    which is a governance adjudication and deliberately not done here.
    """
    for path, rec in records("targeted_review_mech_059/entries/*/record.json"):
        if "citation" not in rec:
            continue
        cit = rec.pop("citation")
        source = {}
        for key, value in cit.items():
            mapped = CITATION_TO_SOURCE.get(key)
            if mapped is None:
                raise SystemExit(f"unmapped citation key {key!r} in {path}")
            source[mapped] = value
        source["authors"] = [_reorder_author(a) for a in source.get("authors", [])]
        rec["source"] = source

        rec["evidence_class"] = rec.pop("evidence_type", "review")
        rec["confidence"] = 0.6
        rec["confidence_rationale"] = (
            f"Migrated 2026-08-14 from the pre-contract record shape. Originally recorded as "
            f"evidence_strength '{rec.pop('evidence_strength', 'unspecified')}' with no numeric "
            f"confidence; 0.6 is the value the indexer already substituted for this record, so the "
            f"migration does not re-weight the evidence. {rec.pop('notes', '')}"
        ).strip()
        rec.setdefault("summary_path", "summary.md")

        relevance = rec.pop("relevance_to_claim", "")
        if relevance:
            rec["mapping"] = {
                "source_claim_statement": f"See summary.md for the source's own claim; "
                                          f"this entry predates the mapping convention.",
                "ree_translation": relevance,
                "mapping_caveat": "Migrated from a pre-contract record that recorded relevance as a "
                                  "single prose field; the source-faithful statement and the caveat "
                                  "were never separated out and are not reconstructed here.",
            }
        quotes = rec.pop("key_quotes", [])
        if quotes:
            append_summary(path.parent, "Key quotes (from the pre-contract record)",
                           "\n".join(f"> {q}\n" for q in quotes), dry)
        save(path, rec, dry)
        log("pre-contract migration", path)


# --------------------------------------------------------------------------
# (d) singletons
# --------------------------------------------------------------------------

def fix_refines(dry, log):
    """`evidence_direction: "refines"` -- 1 record, not in the enum.

    Do NOT widen the enum. `_normalize_direction` in
    build_experiment_indexes.py does not know the token either, so it already
    coerces this record to "unknown" -- widening the schema alone would make the
    record VALID while leaving it MIS-INGESTED, which is worse than rejecting
    it. Set to "mixed", which is what the record's own rationale describes: the
    paper supports the reinitiation hypothesis and disconfirms the repair
    hypothesis, "refines rather than contradicts". This does change the ingested
    direction (unknown -> mixed) for ARC-049 / Q-035 / DEV-NEED-009 -- flagged
    in the commit message, since it is a real scoring change and not cosmetic.
    """
    for path, rec in records():
        if rec.get("evidence_direction") != "refines":
            continue
        rec["evidence_direction"] = "mixed"
        rec["confidence_rationale"] = (
            str(rec.get("confidence_rationale", "")).rstrip()
            + " [2026-08-14: evidence_direction was recorded as the non-enum token 'refines', which"
              " build_experiment_indexes._normalize_direction silently coerced to 'unknown'. Set to"
              " 'mixed' to match this rationale -- the study supports the reinitiation reading and"
              " disconfirms the repair reading.]"
        )
        save(path, rec, dry)
        log("evidence_direction refines -> mixed", path)


def fix_ree_translation_note(dry, log):
    """`mapping.ree_translation_note` -- 1 record. Reads as a direct continuation
    of `ree_translation`; appended to it rather than given its own key."""
    for path, rec in records():
        mapping = rec.get("mapping")
        if not isinstance(mapping, dict) or "ree_translation_note" not in mapping:
            continue
        mapping["ree_translation"] = (
            mapping.get("ree_translation", "").rstrip() + " " + mapping.pop("ree_translation_note").strip()
        ).strip()
        save(path, rec, dry)
        log("mapping.ree_translation_note", path)


def fix_summary_path(dry, log):
    """28 records omit the required `summary_path`, across 7 dirs and many dates.

    Not drift and not a judgment: all 28 have `summary.md` present on disk, the
    required directory shape mandates it, 2161 records declare it, and the
    indexer already defaults the field to "summary.md". Writing the default
    explicitly is the whole fix. Beyond the four buckets this pass was scoped
    to; kept separate in its own commit so it can be reverted alone.
    """
    for path, rec in records():
        if "summary_path" in rec:
            continue
        if not (path.parent / "summary.md").exists():
            log("summary_path SKIPPED (no summary.md on disk)", path)
            continue
        rec["summary_path"] = "summary.md"
        save(path, rec, dry)
        log("summary_path", path)


STEPS = {
    "class_surveyed": fix_class_surveyed,
    "support_tag": fix_support_tag,
    "tag": fix_tag,
    "prose": fix_prose_fields,
    "confidence_components": fix_confidence_components,
    "pre_contract": fix_pre_contract,
    "refines": fix_refines,
    "ree_translation_note": fix_ree_translation_note,
    "summary_path": fix_summary_path,
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
