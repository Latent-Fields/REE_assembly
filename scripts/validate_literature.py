#!/usr/bin/env python3
"""
Validate evidence/literature/**/entries/**/record.json against literature_evidence/v1.

WHY THIS EXISTS
---------------
The v1 schema's own description said it plainly until this script landed:
"NOTHING MECHANICALLY ENFORCES THIS SCHEMA TODAY -- no hook, no CI job, no
indexer check validates a record against it, so it documents convention rather
than gating it, and a new record can drift without anything failing."

That is not a hypothetical. The `source` object had been violated by 605 of 2189
records (27.6%) for six months before anyone looked, and the reason it stayed
invisible for six months is that no consumer reads the schema:

  - there was no literature validator anywhere under scripts/ (validate_claims.py
    is for docs/claims/claims.yaml).
  - build_experiment_indexes._scan_literature ingests every record but never
    touches the `source` object at all, and DEFAULTS summary_path when absent --
    so a record can violate the schema several ways and index perfectly.

This script is the thing that reads the schema, so that a re-drift fails loudly
instead of accumulating for another six months.

RELATIONSHIP TO scripts/audit_literature_schema.py -- DIFFERENT JOBS
--------------------------------------------------------------------
audit_literature_schema.py answers "the corpus and the schema disagree; which one
is wrong?" -- it enumerates undeclared keys with usage evidence (how many records,
how many literature_type dirs, what date range) so a human can decide whether to
widen the schema or normalise the records. It is a reconciliation instrument, run
occasionally, by a person.

This script answers "does this corpus conform, yes or no?" -- it is a gate, run on
every commit that touches evidence/literature/, and it has no opinion about which
side is wrong. Keep both. Do not merge them: a gate that also proposes schema
changes is a gate people argue with instead of fixing.

WHAT IT CHECKS BEYOND THE SCHEMA
--------------------------------
A JSON Schema validates a document in isolation. It cannot see the filesystem, so
it cannot catch the defects that actually cost evidence here:

  * unreachable_record       -- a record.json the INDEXER'S GLOB NEVER REACHES.
                                It contributes zero evidence to every claim it
                                names, and until now nothing reported it. This is
                                the single most important check in the file,
                                because the record looks completely fine.
  * entry_dir_without_record -- an entry directory with no record.json at all.
                                Same consequence, opposite shape.
  * literature_type_mismatch -- the `literature_type` field disagrees with the
                                parent directory. The indexer derives the type
                                from the DIRECTORY and ignores the field, so a
                                mismatch means the field is a lie that a human
                                reading the record will believe.
  * entry_id_mismatch        -- `entry_id` disagrees with the entry directory.
                                The indexer prefers the FIELD, so cross-referencing
                                by directory name silently misses the entry.
  * summary_missing          -- summary_path names a file that is not on disk.
                                The indexer defaults this field when absent and
                                never stats it, so a dangling pointer is invisible.
  * timestamp_not_rfc3339    -- the schema declares `"format": "date-time"` on
                                timestamp_utc, and that declaration is COMPLETELY
                                INERT. jsonschema only enforces `format` when a
                                FormatChecker is passed AND a backend for the
                                format is installed; `date-time` needs
                                rfc3339-validator / strict-rfc3339, neither of
                                which is present on these boxes. Verified: a
                                Draft7Validator with a FormatChecker accepts the
                                literal string "not-a-date". So the check is done
                                explicitly here rather than pretended at in the
                                schema.

JSONSCHEMA VERSION -- MIXED ACROSS THE FLEET; THE FALLBACK IS DELIBERATE
------------------------------------------------------------------------
The installed jsonschema is NOT uniform across the fleet, so the validator class
is chosen at runtime (Draft202012Validator when present, else Draft7Validator)
rather than assuming either. Measured 2026-08-29: 3.2.0 on the hub ree-cloud-1
(system dist-packages) but 4.26.0 on ree-cloud-4, pulled into ~/.local user-site
as a transitive dependency of the `mcp` package (the ree-working MCP server) and
shadowing the 3.2.0 system copy for every python3 run as `ree` on that box. Do
not re-assert a single fleet-wide version here.

Where 3.2.0 is the copy that gets imported, the Draft7Validator fallback is
faithful rather than a compromise: the schema uses only
type, required, properties, additionalProperties, const, enum, minimum/maximum,
minLength, uniqueItems and format -- every one of which predates draft-07 and is
unchanged in 2020-12. REQUIRING the 2020-12 class would change nothing
about the verdict while adding an install step to every box in the fleet for
zero coverage, which is why it stays a preference rather than a dependency. If a future schema revision starts using a genuinely 2020-12
keyword (prefixItems, dependentSchemas, unevaluatedProperties), THAT is the moment
to revisit -- and the fallback will silently ignore it, so add it to the
`_POST_DRAFT7_KEYWORDS` guard below, which fails loudly instead.

EXIT CODES
----------
0 by default even with findings, so this chains safely -- same convention as
audit_stashes.py and audit_vendored_copies.py. --exit-nonzero turns it into a gate.

The gate is deliberately NOT on by default in the commit path. The corpus has a
non-zero baseline (see --baseline-note), and a gate that fires on every commit
gets disabled, which is worse than no gate. Turn on blocking once the count is at
or near zero.

Usage:
  validate_literature.py                      # report-only, whole corpus
  validate_literature.py --list-failures      # every finding, not just examples
  validate_literature.py --exit-nonzero       # gate: exit 1 if any finding
  validate_literature.py --paths a/b/record.json ...   # scope to given records
  validate_literature.py --json               # machine-readable
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import jsonschema
except ImportError:  # pragma: no cover - environment guard
    print("validate_literature: jsonschema not installed; cannot validate",
          file=sys.stderr)
    sys.exit(3)

REPO_ROOT = Path(__file__).resolve().parent.parent
LITERATURE_REL = "evidence/literature"
SCHEMA_REL = "evidence/literature/schemas/v1/literature_evidence.schema.json"

# Keywords that exist in 2020-12 but NOT in draft-07. Draft7Validator ignores
# these SILENTLY, which would make this script pass a record the schema author
# meant to reject. If the schema ever grows one, we refuse rather than degrade.
_POST_DRAFT7_KEYWORDS = {
    "prefixItems", "dependentSchemas", "dependentRequired",
    "unevaluatedProperties", "unevaluatedItems", "$defs", "$dynamicRef",
    "$dynamicAnchor", "minContains", "maxContains",
}

# RFC 3339 date-time, which is what JSON Schema's `date-time` format means.
# Accepts 'Z' or a numeric offset, and optional fractional seconds.
_RFC3339 = re.compile(
    r"^\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}(\.\d+)?([Zz]|[+-]\d{2}:\d{2})$"
)

# Ordered so the structural (filesystem) classes -- the ones a JSON Schema can
# never catch, and the reason this script is not just `jsonschema -i` -- print
# before the schema classes.
CLASS_ORDER = [
    "unreachable_record",
    "entry_dir_without_record",
    "unparseable_json",
    "literature_type_mismatch",
    "entry_id_mismatch",
    "summary_missing",
    "timestamp_not_rfc3339",
]


class Finding:
    __slots__ = ("cls", "path", "detail")

    def __init__(self, cls, path, detail):
        self.cls = cls
        self.path = path
        self.detail = detail

    def as_dict(self):
        return {"class": self.cls, "path": self.path, "detail": self.detail}


def get_validator_cls():
    """Draft 2020-12 when the installed jsonschema has it, else draft-07.

    See the module docstring: this is a deliberate degrade for jsonschema 3.2.0,
    not an oversight, and it is faithful for the keywords this schema uses.
    """
    for name in ("Draft202012Validator", "Draft7Validator"):
        cls = getattr(jsonschema, name, None)
        if cls is not None:
            return cls, name
    raise SystemExit("validate_literature: no usable jsonschema validator class")


def _walk_schema_keywords(node, out):
    if isinstance(node, dict):
        for key, value in node.items():
            out.add(key)
            _walk_schema_keywords(value, out)
    elif isinstance(node, list):
        for item in node:
            _walk_schema_keywords(item, out)


def schema_needs_2020_12(schema):
    """Post-draft-07 keywords present in the schema, which draft-07 would ignore."""
    keywords = set()
    _walk_schema_keywords(schema, keywords)
    return sorted(keywords & _POST_DRAFT7_KEYWORDS)


def iter_record_paths(literature_root):
    """Every record.json, split by whether the INDEXER would ingest it.

    Returns (ingested, unreachable) as lists of Path.

    The ingested predicate is a deliberate transcription of
    build_experiment_indexes._scan_literature -- the same glob AND the same
    `entry_dir.parent.name != "entries"` skip. It is written this way so the
    validator's notion of "a record" cannot drift from the consumer's: if the
    indexer would not ingest it, this script must not call it valid, however
    well-formed its JSON is.

    `unreachable` is the union of two shapes with the same consequence (zero
    evidence contributed) and different remedies:
      - matched by the glob but skipped by the guard (nested too deep under
        entries/, e.g. entries/a/b/record.json)
      - not matched by the glob at all (not under an entries/ directory, e.g. a
        record.json at the literature_type root)
    """
    ingested, unreachable = [], []
    if not literature_root.exists():
        return ingested, unreachable

    globbed = set()
    for record_path in sorted(literature_root.glob("**/entries/**/record.json")):
        globbed.add(record_path)
        if record_path.parent.parent.name != "entries":
            unreachable.append(record_path)
        else:
            ingested.append(record_path)

    for record_path in sorted(literature_root.glob("**/record.json")):
        if record_path not in globbed:
            unreachable.append(record_path)

    return ingested, sorted(set(unreachable))


def iter_entry_dirs(literature_root):
    """Entry directories the indexer would look in (immediate children of entries/)."""
    if not literature_root.exists():
        return []
    out = []
    for entries_dir in sorted(literature_root.glob("**/entries")):
        if not entries_dir.is_dir():
            continue
        for child in sorted(entries_dir.iterdir()):
            if child.is_dir():
                out.append(child)
    return out


def _normalize_message(message):
    """Collapse a jsonschema message to a class label by blanking literals.

    The list-arity collapse matters more than it looks. Without it, one defect --
    undeclared keys on `source` -- splits into four classes that differ only by
    how many keys each record happened to carry ('X' was unexpected; 'X', 'X'
    were unexpected; ...), which is precisely the fragmentation that makes a
    report unreadable and a drift invisible. The offending keys are still named
    verbatim on each finding's detail line, so nothing is lost.
    """
    # additionalProperties gets its own rule rather than a generic list collapse:
    # its message embeds both the key list AND a was/were agreement that varies
    # with the list length, so a generic rule leaves the arity split in place.
    message = re.sub(
        r"^Additional properties are not allowed \(.*\)$",
        "Additional properties are not allowed (...)", message)
    message = re.sub(r"'[^']*'", "'X'", message)
    message = re.sub(r"\b\d+(\.\d+)?\b", "N", message)
    return message


def structural_findings(repo_root, record_path):
    """Filesystem/consistency checks a JSON Schema structurally cannot make."""
    rel = str(record_path.relative_to(repo_root))
    entry_dir = record_path.parent
    literature_type = entry_dir.parent.parent.name

    try:
        record = json.loads(record_path.read_text())
    except (OSError, ValueError) as exc:
        return None, [Finding("unparseable_json", rel, str(exc))]

    if not isinstance(record, dict):
        return None, [Finding("unparseable_json", rel,
                              "top level is %s, expected object"
                              % type(record).__name__)]

    findings = []

    declared_type = record.get("literature_type")
    if declared_type is not None and str(declared_type) != literature_type:
        findings.append(Finding(
            "literature_type_mismatch", rel,
            "record says %r, directory says %r (the indexer uses the DIRECTORY)"
            % (declared_type, literature_type)))

    declared_id = record.get("entry_id")
    if declared_id is not None and str(declared_id) != entry_dir.name:
        findings.append(Finding(
            "entry_id_mismatch", rel,
            "record says %r, directory is %r (the indexer prefers the FIELD)"
            % (declared_id, entry_dir.name)))

    # The indexer defaults this to "summary.md" when absent and never stats it,
    # so an absent field is a schema finding (it is `required`) while a present
    # one pointing nowhere is invisible to every consumer -- check both shapes.
    summary_rel = record.get("summary_path", "summary.md")
    if isinstance(summary_rel, str) and summary_rel:
        if not (entry_dir / summary_rel).exists():
            findings.append(Finding(
                "summary_missing", rel,
                "summary_path=%r does not exist on disk" % summary_rel))

    timestamp = record.get("timestamp_utc")
    if isinstance(timestamp, str) and not _RFC3339.match(timestamp):
        findings.append(Finding(
            "timestamp_not_rfc3339", rel,
            "timestamp_utc=%r is not an RFC 3339 date-time (the schema's "
            "`format` declaration is not enforced by jsonschema here)"
            % timestamp))

    return record, findings


def collect_findings(repo_root, schema=None, scope=None):
    """All findings for the corpus (or `scope`, a set of record.json Paths)."""
    literature_root = repo_root / LITERATURE_REL
    if schema is None:
        schema = json.loads((repo_root / SCHEMA_REL).read_text())

    unsupported = schema_needs_2020_12(schema)
    validator_cls, validator_name = get_validator_cls()
    if unsupported and validator_name != "Draft202012Validator":
        raise SystemExit(
            "validate_literature: the schema uses %s, which %s IGNORES SILENTLY. "
            "Records would be reported valid without being checked. Install a "
            "jsonschema with Draft202012Validator, or remove the keyword."
            % (", ".join(unsupported), validator_name))
    validator = validator_cls(schema)

    ingested, unreachable = iter_record_paths(literature_root)
    entry_dirs = iter_entry_dirs(literature_root)

    if scope is not None:
        scope = {Path(p).resolve() for p in scope}
        ingested = [p for p in ingested if p.resolve() in scope]
        unreachable = [p for p in unreachable if p.resolve() in scope]
        entry_dirs = [d for d in entry_dirs
                      if (d / "record.json").resolve() in scope]

    findings = []

    for record_path in unreachable:
        rel = str(record_path.relative_to(repo_root))
        if record_path.parent.parent.name == "entries":
            why = "not under an entries/ directory"
        else:
            why = ("nested below entries/%s/, so the indexer's "
                   "`entry_dir.parent.name != 'entries'` guard skips it"
                   % record_path.parent.parent.name)
        findings.append(Finding(
            "unreachable_record", rel,
            "%s -- build_experiment_indexes._scan_literature never ingests this "
            "record, so it contributes ZERO evidence to every claim it names" % why))

    for entry_dir in entry_dirs:
        if not (entry_dir / "record.json").exists():
            findings.append(Finding(
                "entry_dir_without_record",
                str(entry_dir.relative_to(repo_root)),
                "entry directory has no record.json, so it contributes no evidence"))

    for record_path in ingested:
        rel = str(record_path.relative_to(repo_root))
        record, structural = structural_findings(repo_root, record_path)
        findings.extend(structural)
        if record is None:
            continue
        for error in sorted(validator.iter_errors(record),
                            key=lambda e: list(e.absolute_path)):
            location = "/".join(str(p) for p in error.absolute_path) or "<root>"
            findings.append(Finding(
                "schema:%s: %s" % (location, _normalize_message(error.message)),
                rel, error.message))

    return findings, len(ingested)


def resolve_scope_paths(repo_root, raw_paths):
    """Map arbitrary literature paths to the record.json files they implicate.

    The commit gate hands us whatever `git diff --cached` listed, which is not
    only record.json files. A staged summary.md DELETION breaks the summary_path
    of a record that is not itself staged, so scoping naively to staged
    record.json files would miss exactly the defect the deletion caused. Each
    input therefore resolves to the enclosing entry's record.json.

    Returns a de-duplicated, order-stable list of Paths (which may not exist --
    collect_findings intersects against the corpus, so a stale path is a no-op).
    """
    out, seen = [], set()

    def add(path):
        if path not in seen:
            seen.add(path)
            out.append(path)

    for raw in raw_paths:
        path = Path(raw)
        if not path.is_absolute():
            path = repo_root / path
        if path.name == "record.json":
            add(path)
        # Walk up to the entry directory (the one whose parent is `entries`) and
        # take its record. Covers summary.md, and any other per-entry file.
        node = path
        while node != node.parent:
            if node.parent.name == "entries":
                add(node / "record.json")
                break
            node = node.parent
    return out


def _class_sort_key(cls):
    try:
        return (0, CLASS_ORDER.index(cls), cls)
    except ValueError:
        return (1, 0, cls)


def report(findings, n_records, list_failures=False, examples=3, stream=None):
    """Grouped by failure class with a count per class.

    Deliberately NOT one line per record. 107 individual lines is unreadable, and
    an unreadable report is how a six-month drift stays invisible even after
    someone runs the checker.

    `stream` is resolved at CALL time, not bound as a default: a
    `stream=sys.stdout` default captures the interpreter's stdout at import and
    silently ignores any later redirection, which makes the output untestable.
    """
    stream = sys.stdout if stream is None else stream
    if not findings:
        print("validate_literature: OK (%d records checked, 0 findings)"
              % n_records, file=stream)
        return

    by_class = defaultdict(list)
    for finding in findings:
        by_class[finding.cls].append(finding)

    n_paths = len({f.path for f in findings})
    print("validate_literature: %d finding(s) in %d of %d record(s), "
          "%d failure class(es)"
          % (len(findings), n_paths, n_records, len(by_class)), file=stream)

    for cls in sorted(by_class, key=_class_sort_key):
        group = by_class[cls]
        print("\n  %4d  %s" % (len(group), cls), file=stream)
        shown = group if list_failures else group[:examples]
        for finding in shown:
            print("        %s" % finding.path, file=stream)
            if finding.detail and finding.detail != finding.cls:
                print("            %s" % finding.detail, file=stream)
        if not list_failures and len(group) > len(shown):
            print("        ... %d more (--list-failures for all)"
                  % (len(group) - len(shown)), file=stream)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo", default=str(REPO_ROOT),
                        help="REE_assembly repo root (default: this script's repo)")
    parser.add_argument("--paths", nargs="*", default=None, metavar="PATH",
                        help="scope to the records these paths implicate "
                             "(repo-relative or absolute; a record.json, or any "
                             "file inside an entry directory). Used by the commit "
                             "gate to check only what a commit actually touches.")
    parser.add_argument("--list-failures", action="store_true",
                        help="print every finding, not the first few per class")
    parser.add_argument("--exit-nonzero", action="store_true",
                        help="exit 1 if any finding (default: exit 0, chains safely)")
    parser.add_argument("--json", action="store_true",
                        help="machine-readable findings on stdout")
    args = parser.parse_args(argv)

    repo_root = Path(args.repo).resolve()

    scope = None
    if args.paths is not None:
        scope = resolve_scope_paths(repo_root, args.paths)
        # An explicit empty scope means "this commit touched no records" -- a
        # no-op, not "check everything". Getting this backwards would make the
        # gate scan the whole corpus on every unrelated commit.
        if not scope:
            if args.json:
                print(json.dumps({"records_checked": 0, "findings": []}))
            else:
                print("validate_literature: OK (0 records in scope)")
            return 0

    findings, n_records = collect_findings(repo_root, scope=scope)

    if args.json:
        print(json.dumps({
            "records_checked": n_records,
            "findings": [f.as_dict() for f in findings],
        }, indent=2))
    else:
        report(findings, n_records, list_failures=args.list_failures)

    return 1 if (args.exit_nonzero and findings) else 0


if __name__ == "__main__":
    sys.exit(main())
