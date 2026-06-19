#!/usr/bin/env python3
"""Strict-YAML lint for closure-plan frontmatter.

WHY THIS EXISTS (incident 2026-06-19, fixed by commit 4c0313b052):
The explorer closure-map (`serve.py` `read_closure` -> `_parse_plan_frontmatter`,
which calls `yaml.safe_load`) rendered `commitment_closure_plan.md` as an empty
"frontmatter pending" placeholder card because its GAP-8 `owner_exq:` value was a
long UNQUOTED prose string containing `': '` (colon-space) sequences (e.g.
`...the 485f vacuity fix worked: OFC bias...`). `yaml.safe_load` raised a
ScannerError ("mapping values are not allowed here"), so `_parse_plan_frontmatter`
returned None and the WHOLE plan was dropped to `frontmatter_pending:True` despite
being at 87%. The static snapshot (`closure_status.md`) still showed 87% because it
is a stale on-disk artifact regenerated out-of-band, so only the LIVE explorer
surfaced the break.

THE GAP this closes: nothing warned when a plan doc's frontmatter FAILS the strict
`yaml.safe_load` that the live explorer uses. Governance / failure-autopsy sessions
routinely append long prose to scalar fields (`owner_exq`, `resume_condition`,
`title`, `completion_note`, `governance_*`) and an unquoted `': '` silently breaks
the explorer until someone happens to load the closure map.

WHAT THIS DOES: for every `evidence/planning/*_plan.md` that carries a
`closure_plan:` frontmatter block, run the EXACT strict parse `serve.py` uses
(slice the leading `---\n ... \n---\n` block, `yaml.safe_load` it) and emit a
WARNING -- with filename, line/col, and the best-effort offending key -- when the
strict parse fails. It also auto-suggests the usual fix (double-quote the value).

This is a governance HINT, never a gate: it exits 0 regardless of findings (unless
`--strict` is passed) so it can run warn-only inside `governance.sh`. ASCII-only
stdout per repo convention.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/check_plan_frontmatter.py            # warn-only, exit 0
    /opt/local/bin/python3 scripts/check_plan_frontmatter.py --strict   # exit 1 on any failure
    /opt/local/bin/python3 scripts/check_plan_frontmatter.py --file PATH # lint one file
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover -- yaml is a hard dep of the pipeline
    yaml = None

REPO_ROOT = Path(__file__).resolve().parents[1]
PLANNING_DIR = REPO_ROOT / "evidence" / "planning"
SERVE_PY = REPO_ROOT / "serve.py"

# A frontmatter line that opens a mapping key, e.g. "owner_exq:" or
# "      governance_2026_06_18: ...". Used to attribute a parse error to the key
# whose value was the offender.
_KEY_RE = re.compile(r"^(\s*)([A-Za-z0-9_\-]+)\s*:")


def load_known_plans() -> list[str]:
    """Re-derive serve.py's CLOSURE_KNOWN_PLANS so coverage stays in lockstep.

    Parsed from the source text (not imported) -- importing serve.py would pull
    in its server-side deps and side effects. Returns [] if the list can't be
    found, in which case the caller falls back to globbing every *_plan.md.
    """
    if not SERVE_PY.exists():
        return []
    try:
        text = SERVE_PY.read_text(encoding="utf-8")
    except OSError:
        return []
    m = re.search(r"CLOSURE_KNOWN_PLANS\s*=\s*\[(.*?)\]", text, re.DOTALL)
    if not m:
        return []
    return re.findall(r"['\"]([^'\"]+_plan\.md)['\"]", m.group(1))


def extract_frontmatter(text: str) -> str | None:
    """Return the raw YAML frontmatter block exactly as serve.py slices it.

    serve.py._parse_plan_frontmatter requires the doc to START with '---\\n' and
    finds the closing '\\n---\\n'; the block is text[4:end]. Mirror that byte-for-
    byte so this lint sees what the explorer sees.
    """
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    return text[4:end]


def has_closure_plan(fm_text: str) -> bool:
    """True if the (possibly unparseable) frontmatter declares a closure_plan block.

    Detected from the RAW text via a top-level `closure_plan:` line, because the
    whole point is that the block may not parse -- we cannot rely on parsed output
    to know it is a closure plan.
    """
    for line in fm_text.splitlines():
        if re.match(r"^closure_plan\s*:", line):
            return True
    return False


def offending_key(fm_text: str, line_no: int) -> str | None:
    """Best-effort: the mapping key whose value caused a parse error at line_no.

    YAML's problem_mark points at the column where it tripped (typically the
    spurious ': ' inside an unquoted prose value). Walk back from that line to the
    nearest line that opens a key, and return that key name.
    """
    lines = fm_text.splitlines()
    if not (1 <= line_no <= len(lines)):
        return None
    for i in range(line_no - 1, -1, -1):
        m = _KEY_RE.match(lines[i])
        if m:
            return m.group(2)
    return None


def suggest_fix(fm_text: str, line_no: int) -> str | None:
    """Suggest the canonical fix: double-quote the offending scalar value."""
    lines = fm_text.splitlines()
    if not (1 <= line_no <= len(lines)):
        return None
    line = lines[line_no - 1]
    m = re.match(r"^(\s*)([A-Za-z0-9_\-]+)\s*:\s*(.*)$", line)
    if not m:
        return None
    indent, key, value = m.group(1), m.group(2), m.group(3)
    value = value.strip()
    if not value or value.startswith(("'", '"', "[", "{", "|", ">")):
        return None  # already quoted / a flow collection / block scalar
    escaped = value.replace('"', '\\"')
    return f'{indent}{key}: "{escaped}"'


def check_file(path: Path) -> dict | None:
    """Lint one plan doc. Returns a finding dict on strict-parse failure, else None.

    Skips files with no frontmatter or no closure_plan block (they are simply not
    closure-map plans). A file that has closure_plan frontmatter AND parses cleanly
    returns None too.
    """
    if yaml is None:
        return None
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return {"file": path.name, "kind": "unreadable", "message": str(exc)}
    fm_text = extract_frontmatter(text)
    if fm_text is None:
        return None
    if not has_closure_plan(fm_text):
        return None
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as exc:
        mark = getattr(exc, "problem_mark", None)
        # problem_mark line/col are 0-based and relative to fm_text. The doc's
        # absolute line for the operator = +1 (to 1-based) +1 (the leading '---').
        fm_line = (mark.line + 1) if mark is not None else 0
        col = (mark.column + 1) if mark is not None else 0
        doc_line = (fm_line + 1) if fm_line else 0
        problem = getattr(exc, "problem", None) or str(exc).splitlines()[0]
        return {
            "file": path.name,
            "kind": "parse_error",
            "fm_line": fm_line,
            "doc_line": doc_line,
            "col": col,
            "problem": str(problem).strip(),
            "key": offending_key(fm_text, fm_line) if fm_line else None,
            "suggestion": suggest_fix(fm_text, fm_line) if fm_line else None,
        }
    # Parsed, but closure_plan must be a dict for serve.py to use it.
    if not isinstance(fm, dict) or not isinstance(fm.get("closure_plan"), dict):
        return {
            "file": path.name,
            "kind": "not_a_dict",
            "message": "frontmatter parsed but closure_plan is not a mapping",
        }
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any closure plan fails strict parse")
    ap.add_argument("--file", type=str, default=None,
                    help="lint a single plan file instead of the whole dir")
    args = ap.parse_args()

    if yaml is None:
        print("check_plan_frontmatter: PyYAML not available -- skipping (warn-only)")
        return 0

    if args.file:
        targets = [Path(args.file)]
    else:
        if not PLANNING_DIR.exists():
            print(f"check_plan_frontmatter: {PLANNING_DIR} not found -- nothing to check")
            return 0
        targets = sorted(PLANNING_DIR.glob("*_plan.md"))

    # Coverage cross-check: every serve.py-whitelisted plan should be on disk.
    known = set(load_known_plans())
    on_disk = {p.name for p in PLANNING_DIR.glob("*_plan.md")} if PLANNING_DIR.exists() else set()
    missing_known = sorted(known - on_disk) if not args.file else []

    findings = []
    n_closure = 0
    for path in targets:
        try:
            text = path.read_text(encoding="utf-8")
            fm_text = extract_frontmatter(text)
            if fm_text is not None and has_closure_plan(fm_text):
                n_closure += 1
        except OSError:
            pass
        result = check_file(path)
        if result is not None:
            findings.append(result)

    print("=== check_plan_frontmatter: strict-YAML lint for closure-plan frontmatter ===")
    print(f"Scanned {len(targets)} plan file(s); {n_closure} carry closure_plan frontmatter.")
    if missing_known:
        print(f"NOTE: {len(missing_known)} serve.py CLOSURE_KNOWN_PLANS not on disk: "
              + ", ".join(missing_known))

    if not findings:
        print("OK: all closure-plan frontmatter parses under strict yaml.safe_load.")
        return 0

    for f in findings:
        if f["kind"] == "parse_error":
            loc = f"line {f['doc_line']}, col {f['col']}" if f["doc_line"] else "unknown location"
            key = f.get("key")
            keytxt = f" (offending key: '{key}')" if key else ""
            print("")
            print(f"WARNING: {f['file']}: strict yaml.safe_load FAILED at {loc}{keytxt}")
            print(f"  problem: {f['problem']}")
            print("  -> serve.py._parse_plan_frontmatter would return None, so the explorer")
            print("     closure-map drops this whole plan to frontmatter_pending:True.")
            if f.get("suggestion"):
                print("  suggested fix (double-quote the value):")
                print(f"    {f['suggestion']}")
            else:
                print("  fix: double-quote the offending scalar value (wrap it in \"...\").")
        elif f["kind"] == "not_a_dict":
            print("")
            print(f"WARNING: {f['file']}: {f['message']}")
        elif f["kind"] == "unreadable":
            print("")
            print(f"WARNING: {f['file']}: unreadable -- {f['message']}")

    print("")
    print(f"check_plan_frontmatter: {len(findings)} closure plan(s) FAIL strict parse.")
    if args.strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
