#!/usr/bin/env python3
"""Derived, disposable SQLite read-model over the git evidence tree.

Plan of record: REE_assembly/evidence/planning/derived_evidence_index_plan.md
(node `derived_evidence_index:P1`). Schema is that plan's section 4, with the two
deliberate deviations recorded in "DEVIATIONS FROM THE PLAN AS WRITTEN" below.

WHAT THIS IS, AND WHAT IT IS NOT
--------------------------------
It is a READ MODEL. The git-tracked experiment manifests under
`evidence/experiments/` remain the authoritative scientific record; this file is a
projection of them plus `claim_evidence.v1.json`, is gitignored, is rebuilt from
scratch by every indexer run, and is safe to delete at any moment. Nothing in the
repository may treat a row here as evidence of anything: a mutable row asserting
`outcome=PASS` is strictly weaker than a signed commit, which is the whole reason
the evidence plane was NOT migrated into a database (plan section 1).

Consequently this module NEVER writes back to a manifest, a claim registry, or
`review_tracker.json`, and holds no state that cannot be regenerated.

WHERE IT HOOKS
--------------
`build_experiment_indexes.py` already holds the complete structure in memory at the
moment it writes `claim_evidence.v1.json`. This is an ADDITIONAL WRITER at that same
point (plan section 6) -- not a refactor of the indexer, and the JSON artifact is
written unchanged either way. If this module raises, the indexer prints the failure
and carries on: a derived read-model going missing must never cost a governance run.

DEVIATIONS FROM THE PLAN AS WRITTEN (both deliberate, both narrowing)
--------------------------------------------------------------------
1. THE SKEW GATE REFUSES ON `tracked-but-absent`, NOT ON `on_disk != in_git`.
   The plan states the invariant as `n_manifests_on_disk != n_manifests_in_git ->
   BUILD REFUSES`. Taken literally that fires on the NORMAL state of a live box: a
   run that finished five minutes ago is on disk and not yet committed, so the two
   counts legitimately differ in the harmless direction on essentially every build.
   A gate that fires on ordinary work gets disabled, which is worse than no gate.
   The direction that actually caused the 2026-07-18 SD-068 incident is the other
   one -- files git TRACKS that were never materialised on disk after a
   `git reset <remote-ref>` -- and that is what is enforced here (`n_tracked_absent
   > 0 -> refuse`). Both counts are still recorded in `build_meta` so the benign
   direction stays visible and auditable.

   This is belt-and-braces, not the primary defence: the indexer's own
   `_guard_worktree_materialised()` already performs the same set-difference before
   any read or write and exits 3. This module recomputes it independently and
   records the verdict AS DATA, so a consumer querying the DB can tell whether the
   build it is reading was integrity-checked rather than having to assume it.

2. `review` / `discussed_dirs` ARE READ-ONLY MIRRORS, NOT THE WRITE TARGET.
   Plan section 3 proposes `INSERT INTO discussed_dirs` as the fix for the
   `POST /api/review/discuss` lost update. That fix would move canonical state --
   `review_tracker.json` is documented in CLAUDE.md as the SOLE source of truth for
   whether an experiment has been discussed -- into a gitignored, disposable,
   rebuilt-from-scratch artifact, where deleting the file (which this module's own
   contract says is always safe) would destroy review history that is derivable
   from nothing. So the lost update is fixed IN PLACE instead, by making the JSON
   read-modify-write atomic and serialised (serve.py `_review_tracker_lock`), and
   these two tables carry a mirror for the query surface only. They are rebuilt
   from the JSON on every build and are never written outside a build.

ASCII-only output (repo rule). Stdlib only.
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable, Mapping, Optional, Sequence

# Bumped whenever the SCHEMA below changes in a way a consumer could notice.
# Recorded in build_meta so a consumer can refuse a DB older than it understands
# rather than silently mis-reading a renamed column.
SCHEMA_VERSION = 1

DERIVED_DIRNAME = ".derived"
DB_FILENAME = "evidence.sqlite"


class DerivedIndexSkewError(RuntimeError):
    """Refusal: git-tracked evidence is absent from the working tree.

    See deviation 1 above. Raised BEFORE any table is populated, so a refusal
    leaves any previously-built DB exactly as it was rather than truncating it to
    a silently-smaller one -- the same posture as the indexer's own skew guard.
    """


SCHEMA = """
CREATE TABLE runs (
    run_id                          TEXT PRIMARY KEY,
    experiment_type                 TEXT,
    timestamp_utc                   TEXT,
    outcome                         TEXT,
    machine                         TEXT,
    machine_class                   TEXT,
    architecture_epoch              TEXT,
    manifest_path                   TEXT,
    experiment_purpose              TEXT,
    evidence_class                  TEXT,
    evidence_level                  TEXT,
    evidence_direction              TEXT,
    adjudication                    TEXT,
    queue_id                        TEXT,
    canonical_profile               TEXT,
    substrate_hash                  TEXT,
    substrate_commit                TEXT,
    superseded_by_substrate         TEXT,
    -- Provenance-coverage columns. `has_enabled_default_off_flags` is 1/0 and
    -- NOT nullable-collapsed on purpose: 0 means "measured nothing enabled" is
    -- impossible to express, so the 1/0 here means MEASURED-AT-ALL, and
    -- n_enabled_default_off_flags carries how many were on. That keeps the
    -- never-measured / measured-empty distinction queryable, which is the whole
    -- point of the field (see manifest_core.enabled_default_off_flags_for_agents).
    has_enabled_default_off_flags   INTEGER,
    n_enabled_default_off_flags     INTEGER
);
CREATE INDEX idx_runs_type      ON runs(experiment_type);
CREATE INDEX idx_runs_ts        ON runs(timestamp_utc);
CREATE INDEX idx_runs_outcome   ON runs(outcome);
CREATE INDEX idx_runs_commit    ON runs(substrate_commit);

CREATE TABLE entries (
    claim_id            TEXT NOT NULL,
    run_id              TEXT NOT NULL,
    source_type         TEXT,
    evidence_direction  TEXT,
    evidence_class      TEXT,
    evidence_level      TEXT,
    confidence          REAL,
    status              TEXT,
    experiment_purpose  TEXT,
    experiment_type     TEXT,
    architecture_epoch  TEXT,
    adjudication        TEXT,
    timestamp_utc       TEXT,
    scoring_excluded    TEXT
);
CREATE INDEX idx_entries_claim     ON entries(claim_id);
CREATE INDEX idx_entries_run       ON entries(run_id);
CREATE INDEX idx_entries_direction ON entries(evidence_direction);
CREATE INDEX idx_entries_scoring   ON entries(scoring_excluded);

CREATE TABLE claim_rollup (
    claim_id                            TEXT PRIMARY KEY,
    genuine_exp_count                   INTEGER,
    pass_runs                           INTEGER,
    fail_runs                           INTEGER,
    evidence_quadrant                   TEXT,
    overall_confidence                  REAL,
    experimental_confidence             REAL,
    experimental_confidence_decoupled   REAL,
    literature_confidence               REAL,
    literature_confidence_parallel      REAL,
    entries_total                       INTEGER,
    runs_total                          INTEGER,
    latest_run_id                       TEXT,
    latest_timestamp_utc                TEXT,
    confidence_rationale                TEXT,
    exp_posterior_json                  TEXT,
    lit_posterior_json                  TEXT,
    direction_counts_json               TEXT,
    -- Stored VERBATIM rather than recomputed with a `ORDER BY timestamp LIMIT 5`
    -- over `entries`. The matrix builds this as `ordered_entries[-5:]` over its
    -- OWN ordering, including scoring-excluded rows; re-deriving it in SQL would
    -- either change /api/timeline/events' payload or duplicate that truncation
    -- rule in a second place, where the two could silently diverge. Copying the
    -- list makes the timeline cutover byte-identical by construction.
    recent_entries_json                 TEXT
);
CREATE INDEX idx_rollup_quadrant ON claim_rollup(evidence_quadrant);
CREATE INDEX idx_rollup_expconf  ON claim_rollup(experimental_confidence);

CREATE TABLE unlinked_runs (
    run_id           TEXT,
    experiment_type  TEXT,
    source_type      TEXT,
    status           TEXT,
    timestamp_utc    TEXT
);

-- READ-ONLY MIRRORS of review_tracker.json. See deviation 2 in the module
-- docstring: review_tracker.json stays canonical and these are rebuilt from it.
CREATE TABLE review (
    run_id       TEXT PRIMARY KEY,
    reviewed_at  TEXT
);
CREATE TABLE discussed_dirs (
    dir           TEXT PRIMARY KEY,
    discussed_at  TEXT
);

CREATE TABLE build_meta (
    key    TEXT PRIMARY KEY,
    value  TEXT
);
"""


# --------------------------------------------------------------------------
# manifest census -- the integrity input
# --------------------------------------------------------------------------

def _is_indexer_read_path(rel_path: str) -> bool:
    """Mirror of build_experiment_indexes._is_indexer_read_path.

    Duplicated rather than imported ON PURPOSE: this module must be runnable
    (and testable) standalone against any evidence dir, and the indexer is an
    8k-line module whose import has side effects. The two are pinned to agree by
    test_derived_evidence_db.py, which asserts equality on a shared corpus of
    path shapes rather than trusting the copy.
    """
    parts = rel_path.split("/")
    if len(parts) == 1:
        return rel_path.endswith(".json")
    return "runs" in parts[:-1]


def _git_tracked_paths(base_dir: Path) -> Optional[list[str]]:
    """Paths git tracks under base_dir, relative to base_dir; None when not a repo.

    None means the guard is genuinely NOT APPLICABLE (no git, not a checkout),
    not that it was skipped -- the HEAD/worktree skew it defends against cannot
    occur outside a checkout.
    """
    try:
        proc = subprocess.run(
            ["git", "-C", str(base_dir), "ls-files", "-z", "--", "."],
            capture_output=True, check=False,
        )
    except (OSError, ValueError):
        return None
    if proc.returncode != 0:
        return None
    decoded = proc.stdout.decode("utf-8", errors="replace")
    return [p for p in decoded.split("\0") if p]


def manifest_census(base_dir: Path) -> dict[str, Any]:
    """Count evidence files on disk vs in git, and list the tracked-but-absent ones.

    `git_applicable` False means there is no checkout to compare against -- the
    counts are still reported, `n_manifests_in_git` is None, and the skew gate
    cannot fire. That is the honest shape: absent beats a fabricated zero, which
    would read as "checked, clean".
    """
    # rglob("*"), NOT rglob("*.json"): _is_indexer_read_path admits ANY file under
    # a `runs/` directory (metrics.csv, summary.md, the adapter-signals sidecar),
    # matching the indexer's own definition. Enumerating only *.json here made the
    # on-disk count 7,885 against an in-git count of 10,777 -- a 2,892 "gap" that
    # was pure measurement mismatch, with zero files actually missing. The two
    # sides of an integrity comparison must enumerate the same population.
    on_disk = sorted(
        rel for rel in (
            str(f.relative_to(base_dir)).replace(os.sep, "/")
            for f in base_dir.rglob("*") if f.is_file()
        )
        if _is_indexer_read_path(rel)
    )
    tracked = _git_tracked_paths(base_dir)
    if tracked is None:
        return {
            "git_applicable": False,
            "n_manifests_on_disk": len(on_disk),
            "n_manifests_in_git": None,
            "tracked_absent": [],
            "n_tracked_absent": 0,
        }
    tracked_evidence = [rel for rel in tracked if _is_indexer_read_path(rel)]
    absent = sorted(rel for rel in tracked_evidence if not (base_dir / rel).exists())
    return {
        "git_applicable": True,
        "n_manifests_on_disk": len(on_disk),
        "n_manifests_in_git": len(tracked_evidence),
        "tracked_absent": absent,
        "n_tracked_absent": len(absent),
    }


def _git_head(base_dir: Path) -> Optional[str]:
    try:
        proc = subprocess.run(
            ["git", "-C", str(base_dir), "rev-parse", "HEAD"],
            capture_output=True, check=False, text=True,
        )
    except (OSError, ValueError):
        return None
    if proc.returncode != 0:
        return None
    head = (proc.stdout or "").strip()
    return head or None


# --------------------------------------------------------------------------
# build
# --------------------------------------------------------------------------

def derived_db_path(base_dir: Path) -> Path:
    return Path(base_dir) / DERIVED_DIRNAME / DB_FILENAME


def _num(value: Any) -> Optional[float]:
    return value if isinstance(value, (int, float)) and not isinstance(value, bool) else None


def _run_rows(by_experiment: Optional[Mapping[str, Sequence[Any]]], base_dir: Path) -> list[tuple]:
    """Project the indexer's in-memory RunRecords into `runs` rows.

    Duck-typed via getattr so this module never imports the indexer (see
    _is_indexer_read_path). A caller with no RunRecords at all (the standalone
    rebuild path) simply gets an empty `runs` table; `entries` and
    `claim_rollup` -- which every consumer in plan section 7 actually reads --
    are built from the matrix and are complete either way.
    """
    rows: list[tuple] = []
    if not by_experiment:
        return rows
    seen: set[str] = set()
    for runs in by_experiment.values():
        for r in runs:
            run_id = str(getattr(r, "run_id", "") or "")
            if not run_id or run_id in seen:
                continue
            seen.add(run_id)
            mpath = getattr(r, "manifest_path", None)
            try:
                mrel = str(Path(mpath).relative_to(base_dir)).replace(os.sep, "/") if mpath else ""
            except (ValueError, TypeError):
                mrel = str(mpath) if mpath else ""
            flags = getattr(r, "enabled_default_off_flags", None)
            rows.append((
                run_id,
                str(getattr(r, "experiment_type", "") or ""),
                str(getattr(r, "timestamp_raw", "") or ""),
                str(getattr(r, "final_status", "") or ""),
                str(getattr(r, "machine", "") or ""),
                str(getattr(r, "machine_class", "") or ""),
                str(getattr(r, "architecture_epoch", "") or ""),
                mrel,
                str(getattr(r, "experiment_purpose", "") or ""),
                str(getattr(r, "evidence_class", "") or ""),
                str(getattr(r, "evidence_level", "") or ""),
                str(getattr(r, "evidence_direction", "") or ""),
                str(getattr(r, "adjudication", "") or ""),
                str(getattr(r, "queue_id", "") or ""),
                str(getattr(r, "canonical_profile", "") or ""),
                str(getattr(r, "substrate_hash", "") or ""),
                str(getattr(r, "substrate_commit", "") or ""),
                str(getattr(r, "superseded_by_substrate", "") or ""),
                1 if isinstance(flags, dict) else 0,
                len(flags) if isinstance(flags, dict) else None,
            ))
    return rows


def _load_review_tracker(base_dir: Path) -> dict[str, Any]:
    path = base_dir / "review_tracker.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def build_derived_db(
    base_dir: Path,
    matrix: Mapping[str, Any],
    *,
    by_experiment: Optional[Mapping[str, Sequence[Any]]] = None,
    generated_at: str = "",
    indexer_version: str = "",
    census: Optional[Mapping[str, Any]] = None,
    allow_missing_runs: bool = False,
) -> dict[str, Any]:
    """Build (or rebuild) the derived SQLite read-model. Returns a summary dict.

    Raises DerivedIndexSkewError when git-tracked evidence is absent from the
    working tree and `allow_missing_runs` is not set -- BEFORE writing anything,
    so a previously-built DB survives a refusal intact.
    """
    base_dir = Path(base_dir).resolve()
    cen = dict(census) if census is not None else manifest_census(base_dir)

    if cen.get("n_tracked_absent") and not allow_missing_runs:
        absent = cen.get("tracked_absent") or []
        shown = ", ".join(absent[:5])
        raise DerivedIndexSkewError(
            "derived-evidence-db REFUSING to build: %d evidence file(s) tracked by "
            "git are ABSENT from the working tree (HEAD/worktree skew). e.g. %s. "
            "Remedy: `git -C <REE_assembly> checkout -- .` then rebuild."
            % (cen["n_tracked_absent"], shown or "(none listed)")
        )

    out_path = derived_db_path(base_dir)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = out_path.with_name(f"{out_path.name}.tmp-{os.getpid()}")
    if tmp_path.exists():
        tmp_path.unlink()

    claims = matrix.get("claims") or {}
    entries = matrix.get("entries") or []
    unlinked = matrix.get("unlinked_runs") or []

    conn = sqlite3.connect(str(tmp_path))
    try:
        conn.executescript(SCHEMA)

        conn.executemany(
            "INSERT OR REPLACE INTO runs VALUES (%s)" % ",".join("?" * 20),
            _run_rows(by_experiment, base_dir),
        )

        conn.executemany(
            "INSERT INTO entries VALUES (%s)" % ",".join("?" * 14),
            [(
                str(e.get("claim_id") or ""),
                str(e.get("run_id") or ""),
                str(e.get("source_type") or ""),
                str(e.get("evidence_direction") or ""),
                str(e.get("evidence_class") or ""),
                str(e.get("evidence_level") or ""),
                _num(e.get("confidence")),
                str(e.get("status") or ""),
                str(e.get("experiment_purpose") or ""),
                str(e.get("experiment_type") or ""),
                str(e.get("architecture_epoch") or ""),
                str(e.get("adjudication") or ""),
                str(e.get("timestamp_utc") or ""),
                str(e.get("scoring_excluded") or ""),
            ) for e in entries if isinstance(e, dict)],
        )

        conn.executemany(
            "INSERT OR REPLACE INTO claim_rollup VALUES (%s)" % ",".join("?" * 19),
            [(
                cid,
                c.get("genuine_exp_count") or 0,
                c.get("pass_runs") or 0,
                c.get("fail_runs") or 0,
                str(c.get("evidence_quadrant") or ""),
                _num(c.get("overall_confidence")),
                _num(c.get("experimental_confidence")),
                _num(c.get("experimental_confidence_decoupled")),
                _num(c.get("literature_confidence")),
                _num(c.get("literature_confidence_parallel")),
                c.get("entries_total") or 0,
                c.get("runs_total") or 0,
                str(c.get("latest_run_id") or ""),
                str(c.get("latest_timestamp_utc") or ""),
                str(c.get("confidence_rationale") or ""),
                json.dumps(c.get("exp_posterior") or {}, sort_keys=True),
                json.dumps(c.get("lit_posterior") or {}, sort_keys=True),
                json.dumps(c.get("direction_counts") or {}, sort_keys=True),
                json.dumps(c.get("recent_entries") or []),
            ) for cid, c in claims.items() if isinstance(c, dict)],
        )

        conn.executemany(
            "INSERT INTO unlinked_runs VALUES (?,?,?,?,?)",
            [(
                str(u.get("run_id") or ""),
                str(u.get("experiment_type") or ""),
                str(u.get("source_type") or ""),
                str(u.get("status") or ""),
                str(u.get("timestamp_utc") or ""),
            ) for u in unlinked if isinstance(u, dict)],
        )

        tracker = _load_review_tracker(base_dir)
        reviewed_at = str(tracker.get("last_review_utc") or "")
        conn.executemany(
            "INSERT OR REPLACE INTO review VALUES (?,?)",
            [(str(rid), reviewed_at) for rid in (tracker.get("reviewed_run_ids") or []) if rid],
        )
        conn.executemany(
            "INSERT OR REPLACE INTO discussed_dirs VALUES (?,?)",
            [(str(d), reviewed_at) for d in (tracker.get("discussed_experiment_dirs") or []) if d],
        )

        meta = {
            "schema_version": str(SCHEMA_VERSION),
            "generated_at_utc": generated_at or str(matrix.get("generated_at_utc") or ""),
            "source_commit": _git_head(base_dir) or "",
            "indexer_version": indexer_version,
            "matrix_schema_version": str(matrix.get("schema_version") or ""),
            "n_manifests_on_disk": str(cen.get("n_manifests_on_disk")),
            "n_manifests_in_git": (
                "" if cen.get("n_manifests_in_git") is None else str(cen.get("n_manifests_in_git"))
            ),
            "n_tracked_absent": str(cen.get("n_tracked_absent") or 0),
            "skew_gate": (
                "not_applicable_no_git" if not cen.get("git_applicable")
                else ("bypassed_allow_missing_runs" if cen.get("n_tracked_absent") else "ok")
            ),
            "n_entries": str(len(entries)),
            "n_claims": str(len(claims)),
            "n_runs": str(len(_run_rows(by_experiment, base_dir))),
            "n_unlinked_runs": str(len(unlinked)),
        }
        conn.executemany("INSERT OR REPLACE INTO build_meta VALUES (?,?)", sorted(meta.items()))
        conn.commit()
    finally:
        conn.close()

    os.replace(str(tmp_path), str(out_path))
    return {"path": out_path, "meta": meta, "census": cen}


# --------------------------------------------------------------------------
# read side
# --------------------------------------------------------------------------

def open_readonly(base_dir: Path) -> Optional[sqlite3.Connection]:
    """Open the derived DB read-only, or None when it has not been built.

    Every consumer MUST tolerate None: the DB is disposable by contract, so
    "absent" is a normal state (a fresh clone, a deleted file, a checkout that
    has not run the indexer yet) and never an error.
    """
    path = derived_db_path(base_dir)
    if not path.exists():
        return None
    try:
        conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error:
        return None


def build_meta(conn: sqlite3.Connection) -> dict[str, str]:
    try:
        return {r["key"]: r["value"] for r in conn.execute("SELECT key, value FROM build_meta")}
    except sqlite3.Error:
        return {}


def claim_summary_rows(conn: sqlite3.Connection) -> dict[str, dict[str, Any]]:
    """The four-plus fields explorer.html used to download 12 MB of JSON for.

    Plan section 7's first row. Kept deliberately narrow: this is the payload
    replacement, not a general claim view.
    """
    out: dict[str, dict[str, Any]] = {}
    try:
        cur = conn.execute(
            "SELECT claim_id, genuine_exp_count, evidence_quadrant, "
            "experimental_confidence_decoupled, literature_confidence_parallel "
            "FROM claim_rollup"
        )
    except sqlite3.Error:
        return out
    for r in cur:
        out[r["claim_id"]] = {
            "genuine_exp_count": r["genuine_exp_count"] or 0,
            "evidence_quadrant": r["evidence_quadrant"] or None,
            "experimental_confidence_decoupled": r["experimental_confidence_decoupled"],
            "literature_confidence_parallel": r["literature_confidence_parallel"],
        }
    return out


def claim_rollup_map(conn: sqlite3.Connection) -> dict[str, dict[str, Any]]:
    """The `claims` map of claim_evidence.v1.json, restricted to what serve.py reads.

    Shaped to be a DROP-IN for the sub-dict `_load_claim_evidence_claims()`
    returns, so the two /api consumers (brain-map's 5 scalars, the timeline's
    confidence series) can switch source without changing a single field read.
    It is deliberately NOT the whole matrix: the 12 MB `entries` list is what
    made that file expensive, and nothing in serve.py wanted it.
    """
    out: dict[str, dict[str, Any]] = {}
    try:
        cur = conn.execute(
            "SELECT claim_id, genuine_exp_count, pass_runs, fail_runs, "
            "evidence_quadrant, overall_confidence, experimental_confidence, "
            "experimental_confidence_decoupled, literature_confidence, "
            "literature_confidence_parallel, entries_total, runs_total, "
            "latest_run_id, latest_timestamp_utc, recent_entries_json "
            "FROM claim_rollup"
        )
    except sqlite3.Error:
        return out
    for r in cur:
        try:
            recent = json.loads(r["recent_entries_json"] or "[]")
        except Exception:
            recent = []
        out[r["claim_id"]] = {
            "genuine_exp_count": r["genuine_exp_count"] or 0,
            "pass_runs": r["pass_runs"] or 0,
            "fail_runs": r["fail_runs"] or 0,
            "evidence_quadrant": r["evidence_quadrant"] or "",
            "overall_confidence": r["overall_confidence"],
            "experimental_confidence": r["experimental_confidence"],
            "experimental_confidence_decoupled": r["experimental_confidence_decoupled"],
            "literature_confidence": r["literature_confidence"],
            "literature_confidence_parallel": r["literature_confidence_parallel"],
            "entries_total": r["entries_total"] or 0,
            "runs_total": r["runs_total"] or 0,
            "latest_run_id": r["latest_run_id"] or "",
            "latest_timestamp_utc": r["latest_timestamp_utc"] or "",
            "recent_entries": recent,
        }
    return out


def query_entries(
    conn: sqlite3.Connection,
    *,
    claim_id: Optional[str] = None,
    evidence_direction: Optional[str] = None,
    source_type: Optional[str] = None,
    min_confidence: Optional[float] = None,
    include_excluded: bool = False,
    limit: int = 500,
) -> list[dict[str, Any]]:
    """The query surface plan section 1 names as the genuinely missing capability.

    Parameterised throughout -- there is deliberately NO free-text SQL entry point
    reachable from the HTTP layer, because the explorer binds on all interfaces
    behind WireGuard and an arbitrary-SQL endpoint over a file the server can read
    is a data-exfiltration surface, not a convenience. Ad-hoc SQL belongs at the
    CLI (`python derived_evidence_db.py sql "..."`), where the caller already has
    the filesystem.
    """
    where: list[str] = []
    params: list[Any] = []
    if claim_id:
        where.append("claim_id = ?")
        params.append(claim_id)
    if evidence_direction:
        where.append("evidence_direction = ?")
        params.append(evidence_direction)
    if source_type:
        where.append("source_type = ?")
        params.append(source_type)
    if min_confidence is not None:
        where.append("confidence >= ?")
        params.append(float(min_confidence))
    if not include_excluded:
        where.append("(scoring_excluded IS NULL OR scoring_excluded = '')")
    sql = "SELECT * FROM entries"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY timestamp_utc DESC, claim_id, run_id LIMIT ?"
    params.append(max(1, min(int(limit), 5000)))
    try:
        return [dict(r) for r in conn.execute(sql, params)]
    except sqlite3.Error:
        return []


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def _default_base_dir() -> Path:
    return Path(__file__).resolve().parents[1]


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", type=Path, default=_default_base_dir(),
                    help="Path to evidence/experiments")
    sub = ap.add_subparsers(dest="cmd")

    p_build = sub.add_parser("build", help="Rebuild from claim_evidence.v1.json on disk")
    p_build.add_argument("--allow-missing-runs", action="store_true", default=False)

    sub.add_parser("meta", help="Print build_meta")

    p_sql = sub.add_parser("sql", help="Run a read-only SQL query")
    p_sql.add_argument("statement")

    p_claim = sub.add_parser("claim", help="Show entries + rollup for one claim")
    p_claim.add_argument("claim_id")
    p_claim.add_argument("--direction", default=None)
    p_claim.add_argument("--min-confidence", type=float, default=None)
    p_claim.add_argument("--include-excluded", action="store_true", default=False)

    args = ap.parse_args(argv)
    base_dir = args.root.resolve()
    cmd = args.cmd or "meta"

    if cmd == "build":
        matrix_path = base_dir / "claim_evidence.v1.json"
        if not matrix_path.exists():
            print(f"ERROR: {matrix_path} not found -- run the indexer first", file=sys.stderr)
            return 2
        matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
        try:
            res = build_derived_db(
                base_dir, matrix,
                generated_at=str(matrix.get("generated_at_utc") or ""),
                indexer_version="standalone-rebuild",
                allow_missing_runs=args.allow_missing_runs,
            )
        except DerivedIndexSkewError as exc:
            print(str(exc), file=sys.stderr)
            return 3
        size = Path(res["path"]).stat().st_size
        print(f"built {res['path']} ({size} bytes)")
        for k, v in sorted(res["meta"].items()):
            print(f"  {k}: {v}")
        return 0

    conn = open_readonly(base_dir)
    if conn is None:
        print("derived DB not built (run: derived_evidence_db.py build)", file=sys.stderr)
        return 1
    try:
        if cmd == "meta":
            for k, v in sorted(build_meta(conn).items()):
                print(f"{k}: {v}")
        elif cmd == "sql":
            for row in conn.execute(args.statement):
                print(json.dumps(dict(row), sort_keys=True, default=str))
        elif cmd == "claim":
            roll = conn.execute(
                "SELECT * FROM claim_rollup WHERE claim_id = ?", (args.claim_id,)
            ).fetchone()
            print(json.dumps(dict(roll) if roll else {}, indent=2, sort_keys=True))
            rows = query_entries(
                conn, claim_id=args.claim_id, evidence_direction=args.direction,
                min_confidence=args.min_confidence, include_excluded=args.include_excluded,
            )
            print(f"-- {len(rows)} entr(ies) --")
            for r in rows:
                print(f"  {r['timestamp_utc'][:19]:20s} {r['evidence_direction']:10s} "
                      f"conf={r['confidence']} {r['run_id']}")
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
