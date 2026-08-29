#!/usr/bin/env python3
"""Audit evidence/literature/**/entries/**/record.json against the v1 schema.

Two jobs, and the second is the one that matters:

1. Validate the whole corpus and report the failing set (``--list-failures``).
2. For every field the schema does NOT declare, report WHERE it is used --
   how many records, which ``literature_type`` directories, and over what date
   range (``--drift``). That is the evidence that decides direction:

     corpus-wide, many directories, still current  -> convention. Widen the schema.
     one directory, one pull session, one date     -> drift. Normalise the records.

   Deciding from a sample instead of the full corpus is how the wrong call gets
   made; two prior reconciliations (2026-08-14, ``source`` then top-level) both
   rebuilt this enumeration from scratch in /tmp because it was never committed.

``--baseline <ref>`` validates against the schema as of a git ref as well, and
reports the failing-set DELTA -- newly-failing records are regressions and the
schema change should not land with any.

``--exit-nonzero`` turns the report into a gate (exit 1 on any failing record).
Default is exit 0 even with findings, so the audit chains safely -- same
convention as ``audit_stashes.py`` and ``audit_vendored_copies.py``. The corpus
reached **0 failing of 2189 on 2026-08-14**, which is what makes the flag usable
at all: a gate that fires on every commit gets turned off, so this must not be
switched on again while a backlog exists. Note the COMMIT gate is
``scripts/precommit_literature.sh`` -> ``scripts/validate_literature.py``, which
is scoped to the records a commit actually touches; this flag is the
WHOLE-CORPUS gate, for a scheduled or manual sweep.

The installed jsonschema is not uniform across the fleet -- measured 2026-08-29,
3.2.0 on the hub ree-cloud-1 but 4.26.0 on ree-cloud-4, where it arrived in
~/.local user-site as a transitive dependency of the `mcp` package and shadows
the system copy. ``get_validator_cls`` therefore PREFERS ``Draft202012Validator``
and falls back to ``Draft7Validator``; do not re-assert one fleet-wide version.
The fallback is faithful because the schema declares 2020-12 but uses no keyword
that postdates draft-07.
"""

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import jsonschema

REPO = Path(__file__).resolve().parent.parent
LIT_ROOT = REPO / "evidence" / "literature"
SCHEMA_REL = "evidence/literature/schemas/v1/literature_evidence.schema.json"


def get_validator_cls():
    for name in ("Draft202012Validator", "Draft7Validator"):
        cls = getattr(jsonschema, name, None)
        if cls is not None:
            return cls
    raise SystemExit("no usable jsonschema validator class")


def load_records():
    """Return [(relpath, record_dict)] for every entry record in the corpus."""
    out = []
    for path in sorted(LIT_ROOT.glob("*/entries/*/record.json")):
        try:
            out.append((str(path.relative_to(REPO)), json.loads(path.read_text())))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"UNREADABLE {path.relative_to(REPO)}: {exc}", file=sys.stderr)
    return out


def load_schema(ref=None):
    if ref is None:
        return json.loads((REPO / SCHEMA_REL).read_text())
    blob = subprocess.run(
        ["git", "-C", str(REPO), "show", f"{ref}:{SCHEMA_REL}"],
        capture_output=True, text=True, check=True,
    ).stdout
    return json.loads(blob)


def failing_set(records, schema):
    """-> {relpath: [error messages]} for records that do not validate."""
    validator = get_validator_cls()(schema)
    failures = {}
    for rel, rec in records:
        errs = sorted(validator.iter_errors(rec), key=lambda e: list(e.path))
        if errs:
            failures[rel] = [
                f"{'/'.join(str(p) for p in e.absolute_path) or '<root>'}: {e.message}"
                for e in errs
            ]
    return failures


def declared_keys(schema, pointer):
    """Declared property names at a schema location ('' = top level, 'source', ...)."""
    node = schema
    for part in [p for p in pointer.split("/") if p]:
        node = node["properties"][part]
    return set(node.get("properties", {}))


def drift_report(records, schema, pointer=""):
    """Undeclared keys at `pointer`, with usage evidence for each."""
    declared = declared_keys(schema, pointer)
    parts = [p for p in pointer.split("/") if p]
    usage = defaultdict(lambda: {"count": 0, "dirs": defaultdict(int), "dates": []})

    for rel, rec in records:
        node = rec
        for part in parts:
            node = node.get(part) if isinstance(node, dict) else None
            if node is None:
                break
        if not isinstance(node, dict):
            continue
        lit_type = rec.get("literature_type") or rel.split("/")[2]
        ts = str(rec.get("timestamp_utc", ""))[:10]
        for key in node:
            if key in declared:
                continue
            u = usage[key]
            u["count"] += 1
            u["dirs"][lit_type] += 1
            if ts:
                u["dates"].append(ts)
    return usage


def print_drift(usage, label):
    print(f"\n=== undeclared keys at {label} ===")
    if not usage:
        print("(none)")
        return
    for key, u in sorted(usage.items(), key=lambda kv: -kv[1]["count"]):
        dates = sorted(u["dates"])
        span = f"{dates[0]}..{dates[-1]}" if dates else "?"
        n_dirs = len(u["dirs"])
        verdict = "CONVENTION?" if n_dirs > 3 else "drift"
        print(f"  {key:44s} n={u['count']:4d}  dirs={n_dirs:3d}  {span}  [{verdict}]")
        for d, c in sorted(u["dirs"].items(), key=lambda kv: -kv[1])[:6]:
            print(f"      {c:4d}  {d}")
        if n_dirs > 6:
            print(f"      ... {n_dirs - 6} more dir(s)")


def print_enum_drift(records, schema):
    """Values outside a declared string enum -- same decide-the-direction question."""
    print("\n=== values outside declared enums ===")
    found = False
    for field, spec in schema.get("properties", {}).items():
        allowed = spec.get("enum")
        if not allowed:
            continue
        seen = defaultdict(list)
        for rel, rec in records:
            val = rec.get(field)
            if val is not None and val not in allowed:
                seen[val].append(rel)
        for val, rels in sorted(seen.items(), key=lambda kv: -len(kv[1])):
            found = True
            print(f"  {field}={val!r}  n={len(rels)}")
            for r in rels[:5]:
                print(f"      {r}")
    if not found:
        print("(none)")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--drift", action="store_true", help="report undeclared keys + enum drift")
    ap.add_argument("--list-failures", action="store_true", help="print each failing record")
    ap.add_argument("--baseline", metavar="REF",
                    help="also validate against the schema at REF and diff the failing sets")
    ap.add_argument("--pointer", action="append", default=None,
                    help="schema location for --drift (repeatable; default: top level and source)")
    ap.add_argument("--exit-nonzero", action="store_true",
                    help="exit 1 if any record fails (default: exit 0, chains safely)")
    args = ap.parse_args()

    records = load_records()
    schema = load_schema()
    failures = failing_set(records, schema)
    print(f"corpus: {len(records)} records, {len(failures)} failing against HEAD schema")

    if args.baseline:
        base_failures = failing_set(records, load_schema(args.baseline))
        fixed = set(base_failures) - set(failures)
        regressed = set(failures) - set(base_failures)
        print(f"baseline {args.baseline}: {len(base_failures)} failing")
        print(f"  fixed:      {len(fixed)}")
        print(f"  REGRESSED:  {len(regressed)}")
        for r in sorted(regressed):
            print(f"      {r}")
            for msg in failures[r]:
                print(f"        {msg}")

    if args.drift:
        for pointer in args.pointer or ["", "source", "mapping", "confidence_components"]:
            print_drift(drift_report(records, schema, pointer),
                        pointer or "<top level>")
        print_enum_drift(records, schema)

    if args.list_failures:
        print("\n=== failing records ===")
        by_reason = defaultdict(list)
        for rel, msgs in sorted(failures.items()):
            print(f"\n{rel}")
            for msg in msgs:
                print(f"    {msg}")
                by_reason[re.sub(r"'[^']*'", "'X'", msg.split(":")[-1].strip())].append(rel)
        print("\n=== failure reasons, by frequency ===")
        for reason, rels in sorted(by_reason.items(), key=lambda kv: -len(kv[1])):
            print(f"  {len(rels):4d}  {reason[:110]}")

    if args.baseline and set(failures) - set(base_failures):
        return 1
    return 1 if (args.exit_nonzero and failures) else 0


if __name__ == "__main__":
    sys.exit(main())
