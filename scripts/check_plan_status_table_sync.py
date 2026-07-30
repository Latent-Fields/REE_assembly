#!/usr/bin/env python3
"""Detect disagreement between a closure plan's YAML frontmatter nodes and the
markdown "Status table" rows in the same file.

WHY THIS EXISTS (measured root cause, 2026-07-29 docs reconcile, commit 7e60b8a675):
Six plan-of-record docs under evidence/planning/ were found describing
already-completed work as outstanding. In EVERY case the YAML frontmatter node
record was CURRENT and only the markdown Status table was stale.

The asymmetry is STRUCTURAL, not incidental. Every /governance cycle writes a
`governance_<date>` key into the node frontmatter and bumps its `last_updated`
-- that is mechanical, and the closure-map / closure-drift tooling reads it. But
nothing at all obliges a session to update the parallel markdown table, which is
nonetheless the artifact each plan labels "The resume primitive" and is what a
cold-start session reads first. So the two representations diverge in one
direction only, and the stale one is the one humans and fresh sessions trust.

Confirmed instances fixed by 7e60b8a675 (regression fixtures for this checker):
  - goal_pipeline:GAP-7      row blocked_pending_substrate/2026-06-10 vs node done/2026-06-15
  - commitment_closure:GAP-8 row in-progress/2026-06-03            vs node assembling/2026-06-23
  - arc_062:GAP-D            row in-progress                       vs node done
  - arc_062:GAP-I            row partial                           vs node blocked_pending_substrate
  - arc_062:GAP-J            row open                              vs node blocked
  - arc_062:GAP-I-absorption in frontmatter since 2026-06-23 with NO table row at all
  - self_attribution GAP-1/2/3 rows named three upstream gates, two since closed

WHAT THIS CHECKS (three cheap, high-signal comparisons -- nothing else):
  1. MEMBERSHIP  -- every frontmatter node id has a Status-table row, and every
                    Status-table row has a frontmatter node. (This alone catches
                    the missing GAP-I-absorption row.)
  2. STATUS      -- the row's Status cell equals the node's `status`.
  3. DATE        -- the row's "Last updated" cell is not OLDER than the node's
                    `last_updated`. A row date that is NEWER is fine and normal:
                    that is what the `2026-07-29 (row reconcile; node record
                    2026-06-15)` marker convention records.

WHAT THIS DELIBERATELY DOES NOT CHECK: the prose cells ("Blocking on", "Next
action", "Owner-EXQ"). Freeform text comparison against a node's prose fields
would be all false positives, and a checker that cries wolf gets ignored -- see
the NOTE-vs-finding split in scripts/audit_vendored_copies.py for the same
reasoning applied to vendored copies.

DESIGN NOTES that matter if you edit this:

  * Table shape varies by plan, so columns are located BY HEADER NAME, never by
    fixed index. Two shapes exist today:
        | Gap | Phase | Status | Blocking on | Next action | Owner-EXQ | Last updated |
        | Gap | Status | Owner EXQ | Last updated |
    A "Status table" section whose table is not node-keyed (no Gap-like column,
    or no Status column) is SKIPPED as out of scope, not flagged. Three plans are
    in that bucket today (behavioral_diversity_isolation, e3_fresh_select_migration,
    ree_ai_design_critique) -- their tables key on Theory / Call site / WS.

  * SOME ROWS CONTAIN LITERAL '|' CHARACTERS INSIDE CELLS and this parser must
    neither choke on them nor "fix" them. Confirmed pre-existing: arc_062 GAP-B
    carries the math notation |PE_t-PE_{t-K}| in its "Next action" cell (10 pipes
    on a 7-column row) and sleep_substrate GAP-2 carries two such pairs (12
    pipes). In every observed case the overflow sits in a middle PROSE column,
    strictly after Status and strictly before Last-updated. So cells are anchored
    from BOTH ENDS: key/status columns are indexed from the left, the date column
    from the right. When the pipe count does not match the header, that fact is
    reported as a parse NOTE so the anchoring assumption stays auditable rather
    than silently producing a wrong comparison.

  * A plan that has closure_plan nodes but NO node-keyed Status table is a NOTE,
    not a finding. Most plans (~44 of 50) are in that bucket -- there is no second
    representation, so there is nothing to disagree. Flagging them would bury the
    real findings under 40+ lines of noise.

  * Status comparison is STRICT equality after normalisation (case, whitespace,
    '_' vs '-', a trailing generation qualifier like "deferred V4", and a trailing
    parenthetical or ';' clause). No semantic coarsening: table `blocked` is NOT
    accepted for node `blocked_pending_substrate`. That is deliberate and is what
    the repair convention already does -- 7e60b8a675 fixed arc_062 GAP-I by
    writing the exact node status `blocked_pending_substrate` into the row, and
    infant_substrate GAP-14 carries it too. Aliasing the coarse form would mask
    exactly the drift this checker exists to find.

Exit code: 0 by default even with findings (advisory, chains safely inside
governance.sh), matching scripts/check_closure_links.py and
scripts/check_closure_drift.py. Pass --exit-nonzero to gate.

ASCII-only stdout per repo convention.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/check_plan_status_table_sync.py
    /opt/local/bin/python3 scripts/check_plan_status_table_sync.py --file evidence/planning/goal_pipeline_plan.md
    /opt/local/bin/python3 scripts/check_plan_status_table_sync.py --exit-nonzero   # gate
    /opt/local/bin/python3 scripts/check_plan_status_table_sync.py --quiet-notes    # findings only
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover -- yaml is a hard dep of the pipeline
    yaml = None

REPO_ROOT = Path(__file__).resolve().parents[1]
PLANNING_DIR = REPO_ROOT / "evidence" / "planning"

# --- header column identification -------------------------------------------
# Matched against the normalised header cell text (lowercased, markdown
# emphasis stripped, whitespace collapsed).
KEY_HEADERS = {"gap", "gap id", "gapid", "node", "node id", "nodeid", "id"}
STATUS_HEADERS = {"status"}
DATE_HEADERS = {"last updated", "last update", "lastupdated", "updated"}

# A heading that introduces the status table. The phrase must be at the START of
# the heading text (after an optional section number), NOT merely contained in
# it. A "contains" test wrongly matches the decision-log entries these plans
# carry -- "### 2026-07-29 - Status-table reconcile: five rows were reporting
# completed work as outstanding" is a live example in arc_062 -- and bounding the
# search to one of those would read the wrong table or none at all.
# Observed real headings: "## Status table", "## 5. Status table",
# "## Status table (resume primitive)".
_STATUS_HEADING_RE = re.compile(
    r"^(#{1,6})\s+(?:\d+[.)]\s*)?status[ -]table\b", re.IGNORECASE)
_HEADING_RE = re.compile(r"^(#{1,6})\s+")

# Leading node key in a table's key cell. Tolerates a trailing title or note in
# the same cell (infant_substrate rows read "GAP-1 Harm gradient env"), and
# preserves a trailing hyphen (arc_062 carries a literal "GAP-I-" row key, which
# must NOT be silently normalised to "GAP-I" -- that would collide with the real
# GAP-I row and hide a genuine truncated-key defect).
_KEY_TOKEN_RE = re.compile(r"^([A-Za-z][A-Za-z0-9]*(?:-[A-Za-z0-9]*)+|[A-Za-z][A-Za-z0-9]*)")

_DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")

# Known status vocabulary, used only to strip trailing prose from a status cell
# ("done (lit gate); see below" -> "done"). Longest-first matching so that
# "blocked-pending-substrate" is never truncated to "blocked".
STATUS_VOCAB = [
    "blocked-pending-substrate",
    "blocked-pending-upstream",
    "upstream-blocked",
    "not-started",
    "in-progress",
    "superseded",
    "assembling",
    "deferred",
    "complete",
    "blocked",
    "partial",
    "tracked",
    "paused",
    "queued",
    "closed",
    "done",
    "open",
]
STATUS_VOCAB_SORTED = sorted(STATUS_VOCAB, key=len, reverse=True)

# A trailing generation qualifier on a table status cell ("deferred V4"). The
# node record spells the same state without it.
_GEN_SUFFIX_RE = re.compile(r"\s+v[45678]\b")


def strip_md(text: str) -> str:
    """Strip the markdown decoration that shows up in table cells."""
    out = text.replace("**", "").replace("`", "").replace("*", "")
    return out.strip()


def norm_header(text: str) -> str:
    return re.sub(r"\s+", " ", strip_md(text).lower()).strip().rstrip(":")


def norm_status(text: str) -> str:
    """Normalise a status value from either representation.

    Case, surrounding whitespace and '_' vs '-' are noise. A trailing
    parenthetical / ';' clause and a generation qualifier ("deferred V4") are
    commentary the node record does not carry. Everything else is preserved --
    there is deliberately no semantic coarsening here (see module docstring).
    """
    s = strip_md(str(text)).lower()
    s = s.split("(")[0]
    s = s.split(";")[0]
    s = s.split("[")[0]
    s = s.replace("_", "-")
    s = re.sub(r"\s+", " ", s).strip()
    s = _GEN_SUFFIX_RE.sub("", s).strip()
    for v in STATUS_VOCAB_SORTED:
        if s == v:
            return v
        if s.startswith(v) and not s[len(v):len(v) + 1].isalnum() and s[len(v):len(v) + 1] != "-":
            return v
    return s


def parse_date(value) -> _dt.date | None:
    """Parse a date from a node field or a table cell.

    YAML auto-parses a bare `2026-06-15` to a datetime.date, so both types
    arrive here. Table cells carry the reconcile-marker form
    `2026-07-29 (row reconcile; node record 2026-06-15)` -- take the LEADING
    date, which is when the row was last touched.
    """
    if value is None:
        return None
    if isinstance(value, _dt.datetime):
        return value.date()
    if isinstance(value, _dt.date):
        return value
    m = _DATE_RE.search(str(value))
    if not m:
        return None
    try:
        return _dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def parse_frontmatter(text: str) -> dict | None:
    """Mirror serve.py._parse_plan_frontmatter byte-for-byte.

    Strict `yaml.safe_load` over text[4:end] of the leading '---\\n...\\n---\\n'
    block, so this checker sees exactly what the explorer closure-map sees. A
    plan whose frontmatter fails strict parse is already the business of
    scripts/check_plan_frontmatter.py -- return None and let that lint own it.
    """
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    try:
        fm = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    return fm if isinstance(fm, dict) else None


def find_status_table(lines: list[str]) -> tuple[dict | None, str | None]:
    """Locate the node-keyed Status table.

    Returns (table, None) on success or (None, reason) when there is nothing in
    scope. `table` carries the header column indices, the header width, the raw
    row lines and their 1-based line numbers.

    Search is bounded to the "Status table" section (up to the next heading at
    the same or a higher level) so a later table in another section can never be
    mistaken for it. Within the section, the first contiguous block of '|' lines
    whose header has BOTH a Gap-like key column and a Status column wins; other
    tables in the same section (arc_062 has a `| master | ... | output |` config
    table there) are skipped by that test rather than by position.

    EVERY candidate heading is tried, not just the first. So a heading that
    matches the pattern but introduces no node-keyed table costs nothing -- the
    search falls through to the next candidate instead of giving up.
    """
    candidates = [(i, len(m.group(1)))
                  for i, line in enumerate(lines)
                  if (m := _STATUS_HEADING_RE.match(line))]
    if not candidates:
        return None, "no 'Status table' heading"

    for head_i, level in candidates:
        start = head_i + 1
        end = len(lines)
        for i in range(start, len(lines)):
            hm = _HEADING_RE.match(lines[i])
            if hm and len(hm.group(1)) <= level:
                end = i
                break

        i = start
        while i < end:
            if not lines[i].lstrip().startswith("|"):
                i += 1
                continue
            block_start = i
            while i < end and lines[i].lstrip().startswith("|"):
                i += 1
            block = lines[block_start:i]
            if len(block) < 2:
                continue
            header = [norm_header(c) for c in block[0].strip().strip("|").split("|")]
            key_idx = next((n for n, h in enumerate(header) if h in KEY_HEADERS), None)
            status_idx = next((n for n, h in enumerate(header) if h in STATUS_HEADERS), None)
            date_idx = next((n for n, h in enumerate(header) if h in DATE_HEADERS), None)
            if key_idx is None or status_idx is None:
                continue  # not a node-keyed status table -- out of scope
            rows = []
            for off, raw in enumerate(block[1:], start=1):
                if re.match(r"^\s*\|[\s:|-]*\|\s*$", raw):
                    continue  # the |---|---| separator
                rows.append((block_start + off + 1, raw))
            return {
                "header": header,
                "ncols": len(header),
                "key_idx": key_idx,
                "status_idx": status_idx,
                "date_idx": date_idx,
                "rows": rows,
                "line": block_start + 1,
            }, None

    return None, "'Status table' section has no node-keyed table (no Gap+Status columns)"


def split_row(raw: str, table: dict) -> tuple[list[str], bool]:
    """Split a table row into cells, tolerating literal '|' inside cells.

    Returns (cells, overflow). `cells` is the raw split; callers index it via
    cell_at(), which anchors from the left for early columns and from the right
    for the date column. `overflow` is True when the row has more cells than the
    header declares -- reported as a parse NOTE so the anchoring assumption is
    auditable (see module docstring).
    """
    cells = raw.strip()
    if cells.startswith("|"):
        cells = cells[1:]
    if cells.endswith("|"):
        cells = cells[:-1]
    parts = [c.strip() for c in cells.split("|")]
    return parts, len(parts) != table["ncols"]


def cell_at(parts: list[str], idx: int, table: dict) -> str | None:
    """Fetch column `idx` from a possibly-overflowed row.

    The date column is the last header column, so index it from the RIGHT; every
    other column of interest (key, status) precedes the prose columns where
    in-cell pipes occur, so index it from the LEFT. If the two anchors would
    cross, the row is too mangled to read and None is returned rather than a
    guess.
    """
    ncols = table["ncols"]
    from_right = idx >= ncols - 1
    if from_right:
        pos = len(parts) - (ncols - idx)
    else:
        pos = idx
    if pos < 0 or pos >= len(parts):
        return None
    if from_right and pos <= table["status_idx"]:
        return None  # overflow ate the columns we need to keep distinct
    return parts[pos]


def row_key(cell: str) -> str | None:
    """Extract the node key from a table key cell."""
    m = _KEY_TOKEN_RE.match(strip_md(cell))
    return m.group(1) if m else None


def node_key(node_id: str, plan_id: str | None) -> str:
    """The table-facing key of a frontmatter node id ('goal_pipeline:GAP-1' -> 'GAP-1')."""
    return node_id.split(":", 1)[1].strip() if ":" in node_id else node_id.strip()


def near_miss(key: str, others: list[str]) -> str | None:
    """Prefix-relationship hint for a likely truncated / extended key.

    Turns the confusing pair (orphan row 'GAP-I-', missing node
    'GAP-I-absorption') into one actionable line.

    Picks the LONGEST prefix relation, so 'GAP-11b' hints at 'GAP-11' rather
    than the equally-valid-but-useless 'GAP-1'.
    """
    best = None
    for o in others:
        if o == key:
            continue
        if o.startswith(key) or key.startswith(o):
            if best is None or len(o) > len(best):
                best = o
    return best


def check_plan(path: Path) -> dict:
    """Compare one plan's frontmatter nodes against its Status table rows."""
    res = {"file": path.name, "findings": [], "notes": [], "n_nodes": 0, "n_rows": 0}
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        res["notes"].append(f"unreadable -- {exc}")
        return res

    fm = parse_frontmatter(text)
    plan = fm.get("closure_plan") if isinstance(fm, dict) else None
    if not isinstance(plan, dict):
        return res  # not a closure plan (or frontmatter broken -- check_plan_frontmatter owns that)

    nodes = {}
    for node in plan.get("nodes") or []:
        if not isinstance(node, dict):
            continue
        nid = node.get("id")
        if not isinstance(nid, str) or not nid.strip():
            continue
        nodes[node_key(nid, plan.get("id"))] = node
    res["n_nodes"] = len(nodes)
    if not nodes:
        return res

    table, reason = find_status_table(text.splitlines())
    if table is None:
        res["notes"].append(f"{reason} -- {len(nodes)} node(s) have no second representation to disagree with")
        return res

    rows: dict[str, dict] = {}
    for lineno, raw in table["rows"]:
        parts, overflow = split_row(raw, table)
        kc = cell_at(parts, table["key_idx"], table)
        key = row_key(kc) if kc else None
        if not key:
            res["notes"].append(f"line {lineno}: row key unreadable -- skipped")
            continue
        if overflow:
            res["notes"].append(
                f"line {lineno} ({key}): row has {len(parts)} cells for a {table['ncols']}-column "
                f"header (literal '|' inside a cell) -- key/status read from the left, "
                f"date from the right"
            )
        sc = cell_at(parts, table["status_idx"], table)
        dc = cell_at(parts, table["date_idx"], table) if table["date_idx"] is not None else None
        if key in rows:
            res["findings"].append({
                "kind": "duplicate_row", "node": key, "line": lineno,
                "detail": f"second Status-table row for '{key}' (first at line {rows[key]['line']})",
            })
            continue
        rows[key] = {"line": lineno, "status": sc, "date": dc}
    res["n_rows"] = len(rows)

    # 1. membership, both directions
    for key in sorted(set(nodes) - set(rows)):
        hint = near_miss(key, list(rows))
        res["findings"].append({
            "kind": "missing_row", "node": key, "line": table["line"],
            "node_status": nodes[key].get("status"),
            "detail": (f"frontmatter node has NO Status-table row"
                       + (f" (nearest row key: '{hint}' -- likely the same node, mis-keyed)" if hint else "")),
        })
    for key in sorted(set(rows) - set(nodes)):
        hint = near_miss(key, list(nodes))
        res["findings"].append({
            "kind": "orphan_row", "node": key, "line": rows[key]["line"],
            "detail": (f"Status-table row has NO frontmatter node"
                       + (f" (nearest node id: '{hint}' -- likely the same node, mis-keyed)" if hint else "")),
        })

    # 2. status, 3. date -- only for nodes present on both sides
    for key in sorted(set(nodes) & set(rows)):
        node, row = nodes[key], rows[key]

        n_status_raw = node.get("status")
        if row["status"] is None:
            res["notes"].append(f"line {row['line']} ({key}): Status cell unreadable -- status not compared")
        elif n_status_raw is None:
            res["notes"].append(f"{key}: frontmatter node has no 'status' -- status not compared")
        else:
            n_status, r_status = norm_status(n_status_raw), norm_status(row["status"])
            if n_status != r_status:
                res["findings"].append({
                    "kind": "status_mismatch", "node": key, "line": row["line"],
                    "row_value": strip_md(row["status"]), "node_value": str(n_status_raw).strip(),
                    "detail": f"row status '{strip_md(row['status'])}' != node status '{str(n_status_raw).strip()}'",
                })
            unknown = [s for s in (n_status, r_status) if s not in STATUS_VOCAB]
            if unknown:
                res["notes"].append(
                    f"{key}: status value(s) outside the known vocabulary: "
                    + ", ".join(sorted(set(unknown)))
                )

        if table["date_idx"] is None:
            continue
        n_date, r_date = parse_date(node.get("last_updated")), parse_date(row["date"])
        if n_date is None:
            res["notes"].append(f"{key}: frontmatter 'last_updated' missing/unparseable -- date not compared")
        elif r_date is None:
            res["notes"].append(
                f"line {row['line']} ({key}): row 'Last updated' missing/unparseable "
                f"({(row['date'] or '')[:40]!r}) -- date not compared"
            )
        elif r_date < n_date:
            res["findings"].append({
                "kind": "date_stale", "node": key, "line": row["line"],
                "row_value": r_date.isoformat(), "node_value": n_date.isoformat(),
                "detail": (f"row 'Last updated' {r_date.isoformat()} is OLDER than node "
                           f"last_updated {n_date.isoformat()} ({(n_date - r_date).days} days behind)"),
            })

    return res


KIND_LABEL = {
    "missing_row": "MISSING ROW",
    "orphan_row": "ORPHAN ROW",
    "duplicate_row": "DUPLICATE ROW",
    "status_mismatch": "STATUS MISMATCH",
    "date_stale": "STALE ROW DATE",
}


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Detect closure_plan frontmatter vs markdown Status-table disagreement.")
    ap.add_argument("--file", type=str, default=None,
                    help="check a single plan file instead of the whole planning dir")
    ap.add_argument("--exit-nonzero", action="store_true",
                    help="exit 1 if any finding is reported (default exits 0 -- advisory)")
    ap.add_argument("--quiet-notes", action="store_true",
                    help="suppress the NOTE section (findings only)")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = ap.parse_args()

    if yaml is None:
        print("check_plan_status_table_sync: PyYAML not available -- skipping (advisory)")
        return 0

    if args.file:
        targets = [Path(args.file)]
        if not targets[0].is_absolute():
            cand = REPO_ROOT / args.file
            if cand.exists():
                targets = [cand]
    else:
        if not PLANNING_DIR.exists():
            print(f"check_plan_status_table_sync: {PLANNING_DIR} not found -- nothing to check")
            return 0
        targets = sorted(PLANNING_DIR.glob("*_plan.md"))

    results = [check_plan(p) for p in targets]
    checked = [r for r in results if r["n_rows"]]
    no_table = [r for r in results if r["n_nodes"] and not r["n_rows"]]
    findings = [(r, f) for r in results for f in r["findings"]]

    if args.json:
        print(json.dumps({
            "scanned": len(targets),
            "compared": [r["file"] for r in checked],
            "no_status_table": [r["file"] for r in no_table],
            "findings": [dict(f, file=r["file"]) for r, f in findings],
            "notes": [{"file": r["file"], "note": n} for r in results for n in r["notes"]],
        }, indent=2, sort_keys=True))
        return 1 if (findings and args.exit_nonzero) else 0

    print("=== check_plan_status_table_sync: frontmatter nodes vs markdown Status table ===")
    print(f"Scanned {len(targets)} plan file(s); {len(checked)} carry a node-keyed Status table "
          f"({sum(r['n_rows'] for r in checked)} rows vs {sum(r['n_nodes'] for r in checked)} nodes).")
    if no_table:
        print(f"NOTE: {len(no_table)} plan(s) have closure_plan nodes but no node-keyed Status table "
              f"(no second representation -- nothing to disagree).")

    if not findings:
        print("OK: every Status-table row agrees with its frontmatter node "
              "(membership, status, last-updated).")
    else:
        by_file: dict[str, list] = {}
        for r, f in findings:
            by_file.setdefault(r["file"], []).append(f)
        for fname in sorted(by_file):
            print("")
            print(f"--- {fname}")
            for f in sorted(by_file[fname], key=lambda x: (x["kind"], x["node"])):
                print(f"  {KIND_LABEL.get(f['kind'], f['kind'].upper())}: {f['node']} "
                      f"(line {f['line']})")
                print(f"    {f['detail']}")
                if f["kind"] in ("status_mismatch", "date_stale"):
                    print("    -> the node record is authoritative in every confirmed case; "
                          "reconcile the ROW.")

    notes = [(r["file"], n) for r in results for n in r["notes"]]
    if notes and not args.quiet_notes:
        print("")
        print(f"NOTES ({len(notes)}) -- parse caveats and uncompared fields, not findings:")
        for fname, n in notes:
            print(f"  {fname}: {n}")

    print("")
    print(f"check_plan_status_table_sync: {len(findings)} finding(s) across "
          f"{len({r['file'] for r, _ in findings})} plan(s).")
    if findings:
        print("Reconcile the markdown ROW to the frontmatter node, not the reverse: every /governance")
        print("cycle bumps the node record and nothing obliges it to touch the table, so the row is")
        print("the stale side by construction. Convention for a reconciled row's date cell:")
        print("  2026-07-29 (row reconcile; node record 2026-06-15)")
    if findings and args.exit_nonzero:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
