#!/usr/bin/env python3
"""Detect closure_plan staleness across evidence/planning/*_plan.md.

A closure_plan node is *drifted* when its `status` is non-terminal
(in-progress / blocked / upstream-blocked / partial) but its `owner_exq`
has reached a terminal state -- the experiment has either left the
ree-v3/experiment_queue.json queue with a manifest in
REE_assembly/evidence/experiments/, or has a confirmed
failure_autopsy_<exq>_*.json artifact under evidence/planning/.

Two suppressors keep legitimate-but-non-terminal nodes out of the
"drifted" bucket (they are recorded in a separate "Suppressed" section
so suppression is auditable, never silent):

  1. Case 3 self-tag: the node carries a governance_<date> entry whose
     value contains the substring "Case 3 in closure-drift terms". This
     is the convention plans use to mark a node as legitimately
     non-terminal pending an upstream substrate or successor EXQ.

  2. Owner-exq manifest is non-contributory: the manifest exists but
     its `evidence_direction` field is in {non_contributory, superseded,
     inconclusive}. The experiment ran to completion but did not
     produce closure-grade evidence.

The owner_exq comparison above keys ENTIRELY on the node's recorded
`owner_exq`, which let goal_pipeline:GAP-2 hide on 2026-06-03: its
owner_exq pinned a stale lineage letter (514g) while the consequential
evidence (514l FAIL + 632/634 autopsies) landed on later letters and on
the node's `unblocks_claims` (MECH-229/230 reclassified substrate_ceiling)
-- none of which the owner_exq check looks at, and the 514g manifest's
non_contributory direction would only have parked it in Suppressed. So a
second, date-aware pass runs for EVERY non-terminal node (including ones
the rules above suppress) and reports them under "Stale since last
update" when either signal fires:

  A. Lineage-advanced: a later-lettered sibling of owner_exq (same EXQ
     number, lexically greater letter) has terminal evidence (manifest or
     failure_autopsy) -- the owner_exq pointer is behind its own lineage.

  B. Claims-reclassified-since: a CONFIRMED failure_autopsy whose
     targets[].claim_ids intersect the node's `unblocks_claims` is dated
     (generated_utc, else filename date) strictly AFTER the node's
     `last_updated` -- a governance decision the plan node has not yet
     absorbed. Same-day counts as reconciled (strict >), so a node updated
     in the same governance cycle that produced the autopsy stays clean.

These are review hints, not drift: a node can legitimately appear here
and still be correct (e.g. the maintainer judged the new evidence does
not change the node). They surface the "did the plan absorb today's
governance?" question that the owner_exq-only check could not ask.

Output is a markdown report at
REE_assembly/evidence/planning/closure_drift.md. The script exits 0
regardless of findings -- it is a governance hint, not a gate.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/check_closure_drift.py
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required.", file=sys.stderr)
    sys.exit(0)

# status_history_plane:SHP-2 -- the status-plane drift check re-projects `live`
# via the SAME code path the shadow projector / collapse tool use, so a stored
# `live:` that has gone stale vs the event log is flagged. Guarded so this drift
# script still runs (skipping only the status-plane section) if the projector is
# unavailable.
try:
    import project_status_head as _psh
except Exception:  # pragma: no cover - projector optional
    _psh = None


REPO_ROOT = Path(__file__).resolve().parents[1]
PLANNING_DIR = REPO_ROOT / "evidence" / "planning"
EXPERIMENTS_DIR = REPO_ROOT / "evidence" / "experiments"
QUEUE_FILE = REPO_ROOT.parent / "ree-v3" / "experiment_queue.json"
DRIFT_REPORT = PLANNING_DIR / "closure_drift.md"
# Machine-readable sidecar consumed by serve.py to flag drifted / stale-since
# nodes directly on the closure map (the markdown report is human-facing only).
DRIFT_JSON = PLANNING_DIR / "closure_drift.json"

# Auto-discovered (glob), NOT a hand-maintained whitelist -- fixed 2026-08-13
# after this used to be a literal `KNOWN_PLANS` list that had silently gone
# stale: `global_workspace_jlens_plan.md` and `arc_005_control_plane_routing_plan.md`
# are both real `generation: v3` plans with non-deferred remaining work (visible
# in closure_status.md's own "Plans" table), but neither was ever added to the
# list, so this drift checker had been silently skipping them since they were
# created -- while `generate_closure_snapshot.py` and serve.py's `read_closure()`
# both auto-discover via `PLANNING_DIR.glob("*_plan.md")` (serve.py's
# `CLOSURE_KNOWN_PLANS` is only an ordering hint, always glob-supplemented; see
# `read_closure()`'s `candidates = list(CLOSURE_KNOWN_PLANS)` + glob top-up) and
# so never missed them. This function makes the three plan-discovery paths agree
# structurally instead of by someone remembering to update a fourth list every
# time a new `*_plan.md` is registered -- the class of bug, not just the instance,
# is what needed fixing (see check_closure_links.py's `_candidate_plan_files()`
# for the same pattern already used for link-dangling checks).
def _discover_plan_files() -> list[str]:
    if not PLANNING_DIR.exists():
        return []
    return [p.name for p in sorted(PLANNING_DIR.glob("*_plan.md"))]

NON_TERMINAL_STATUSES = {
    "in_progress",
    "in-progress",
    "blocked",
    "upstream_blocked",
    "upstream-blocked",
    "partial",
    "tracked",
    "open",
    # Plan-doc node sits at this status when its owner_exq has reached a
    # terminal state but the closure needs a governance-level decision that
    # cannot come out of the standard pipeline (e.g. R4.b on diagnostic-probe
    # evidence where scoring_excluded prevents auto-promotion). Added 2026-05-29
    # after behavioral_diversity_isolation:GAP-D was missed by this script for
    # 24h while parked here. Flagging it for the drift report makes the next
    # /governance cycle see it.
    "pending_governance_stamp",
}

# Assembling / open-by-design nodes are a STABLE RESTING STATE, not drift. They
# are deliberately NOT in NON_TERMINAL_STATUSES, so the drifted / stale-since
# passes skip them entirely -- a node whose substrate is under construction is
# never nagged, and never needs a recurring Case-3 re-stamp to stay quiet (the
# asymmetry that made "keep assembling" the highest-maintenance choice). They are
# still surfaced, auditably, in their own report section, and a node can opt into
# a resume trigger via `revisit_after: YYYY-MM-DD` -- once that date passes the
# node is flagged `revisit_due` for review (the only thing that disturbs its
# rest). See evidence/planning/assembly_vs_closure_plan.md.
ASSEMBLING_STATUSES = {"assembling", "open_by_design"}

EXQ_RE = re.compile(r"V3-EXQ-(\d+[a-z]?)", re.IGNORECASE)


def parse_plan_frontmatter(path: Path) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    try:
        fm = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    if not isinstance(fm, dict):
        return None
    return fm


def load_queue_ids() -> set[str]:
    if not QUEUE_FILE.exists():
        return set()
    try:
        data = json.loads(QUEUE_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return set()
    items = data.get("items", data) if isinstance(data, dict) else data
    out: set[str] = set()
    if isinstance(items, list):
        for it in items:
            if isinstance(it, dict) and isinstance(it.get("queue_id"), str):
                out.add(it["queue_id"].upper())
    return out


def find_terminal_manifest(exq_id: str) -> Path | None:
    """Look for evidence/experiments/v3_exq_<num>_*_v3.json (flat or in subdir)."""
    m = EXQ_RE.search(exq_id)
    if not m:
        return None
    suffix = m.group(1).lower()
    pattern = f"v3_exq_{suffix}_"
    if not EXPERIMENTS_DIR.exists():
        return None
    # flat manifests at top of experiments/
    for p in EXPERIMENTS_DIR.glob(f"{pattern}*_v3.json"):
        return p
    # nested under per-experiment dirs
    for p in EXPERIMENTS_DIR.glob(f"{pattern}*/*_v3.json"):
        return p
    return None


CASE_3_MARKER = "Case 3 in closure-drift terms"
NON_CONTRIBUTORY_DIRECTIONS = {"non_contributory", "superseded", "inconclusive"}


def node_is_case_3(node: dict) -> bool:
    """True if any governance_<date> field on the node carries the Case-3 marker."""
    for k, v in node.items():
        if not isinstance(k, str) or not k.startswith("governance_"):
            continue
        if isinstance(v, str) and CASE_3_MARKER in v:
            return True
    return False


def manifest_evidence_direction(manifest_path: Path) -> str | None:
    """Read the manifest's evidence_direction field, lowercased. None on read error."""
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    direction = data.get("evidence_direction")
    if not isinstance(direction, str):
        return None
    return direction.strip().lower()


def find_failure_autopsy(exq_id: str) -> Path | None:
    if not PLANNING_DIR.exists():
        return None
    m = EXQ_RE.search(exq_id)
    if not m:
        return None
    suffix = m.group(1)
    for p in PLANNING_DIR.glob(f"failure_autopsy_V3-EXQ-{suffix}_*.json"):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return p  # presence is the signal even if unreadable
        status = (data.get("status") or "").lower()
        if status in {"confirmed", "complete", "completed"}:
            return p
        return p
    return None


# --- Date-aware "stale since last update" pass (signals A + B) ----------------

CONFIRMED_AUTOPSY_STATUSES = {"confirmed", "complete", "completed"}
_AUTOPSY_NAME_RE = re.compile(r"failure_autopsy_V3-EXQ-(\d+)([a-z]?)_(\d{4}-\d{2}-\d{2})", re.IGNORECASE)
_MANIFEST_NAME_RE = re.compile(r"v3_exq_(\d+)([a-z]?)_", re.IGNORECASE)

# A run_id / manifest / dir name is `v3_exq_<num><letter>_<descriptive...>` with an
# optional trailing `_<YYYYMMDDTHHMMSSZ>_v3`. The *lineage stem* is the first
# underscore-delimited token of the descriptive part -- the claim/SD/script family
# the experiment belongs to (e.g. `sd049`, `stageh`, `escape`, `scaffolded`). This
# is the signal that distinguishes genuine same-lineage successors (which share a
# stem) from unrelated experiments that merely share an EXQ *number* stem with
# letter suffixes. See `lineage_advanced` for why a number stem alone is unsafe.
_EXQ_PREFIX_RE = re.compile(r"^v3_exq_\d+[a-z]?_", re.IGNORECASE)
_RUNID_TS_SUFFIX_RE = re.compile(r"_\d{8}T\d{6}Z(?:_v3)?$", re.IGNORECASE)
_RUNID_EXQ_RE = re.compile(r"^v3_exq_(\d+)([a-z]?)_", re.IGNORECASE)


def _descriptive_root(name: str) -> str | None:
    """Strip the `v3_exq_<num><letter>_` prefix, file extension, and trailing
    `_<timestamp>_v3` from a manifest filename / dir name / run_id, leaving the
    descriptive body. None if `name` doesn't look like a V3 experiment name."""
    if not isinstance(name, str):
        return None
    s = re.sub(r"\.(json|md)$", "", name, flags=re.IGNORECASE)
    s = _RUNID_TS_SUFFIX_RE.sub("", s)
    s = re.sub(r"_v3$", "", s, flags=re.IGNORECASE)
    m = _EXQ_PREFIX_RE.match(s)
    if not m:
        return None
    body = s[m.end():]
    return body or None


def _lineage_stem(name: str) -> str | None:
    """Leading claim/SD/script token of a V3 experiment name's descriptive root.

    `v3_exq_514l_sd049_phase3_..._v3` -> `sd049`;
    `v3_exq_603k_stageh_harm_pathway_readiness` -> `stageh`. None when no root.
    """
    root = _descriptive_root(name)
    if not root:
        return None
    return root.split("_", 1)[0].lower()


def _autopsy_lineage_stem(path: Path, num: int, letter: str) -> str | None:
    """Lineage stem for an autopsy artifact. The autopsy *filename* carries no
    descriptive root, so read `targets[].run_id` -- prefer the target whose
    embedded EXQ number+letter matches this autopsy, else fall back to the first
    target with a parseable run_id. None if unreadable / no usable run_id."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    targets = data.get("targets") if isinstance(data, dict) else None
    if not isinstance(targets, list):
        return None
    fallback: str | None = None
    for t in targets:
        if not isinstance(t, dict):
            continue
        rid = t.get("run_id")
        if not isinstance(rid, str):
            continue
        mm = _RUNID_EXQ_RE.match(rid)
        if not mm:
            continue
        if fallback is None:
            fallback = _lineage_stem(rid)
        if int(mm.group(1)) == num and mm.group(2).lower() == letter:
            return _lineage_stem(rid)
    return fallback


def _to_date(value):
    """Coerce a YAML date/datetime or ISO/YYYY-MM-DD string to a date. None on failure."""
    if isinstance(value, datetime):
        return value.date()
    # yaml.safe_load turns an unquoted YYYY-MM-DD into datetime.date already
    if hasattr(value, "year") and hasattr(value, "month") and not isinstance(value, str):
        return value
    if isinstance(value, str) and len(value) >= 10:
        try:
            return datetime.strptime(value[:10], "%Y-%m-%d").date()
        except ValueError:
            return None
    return None


def _exq_num_letter(exq_id: str):
    """('514g') -> (514, 'g'); ('582') -> (582, ''). None if not an EXQ id."""
    m = EXQ_RE.search(exq_id or "")
    if not m:
        return None
    mm = re.match(r"(\d+)([a-z]?)$", m.group(1).lower())
    if not mm:
        return None
    return int(mm.group(1)), mm.group(2)


def collect_terminal_lineage() -> dict[int, list[tuple[str, str | None, str]]]:
    """Map EXQ number -> [(letter, lineage_stem, signal_str)] for every terminal
    manifest / autopsy.

    Used to detect when a node's owner_exq pins an earlier lineage letter than
    the latest letter that has actually produced terminal evidence. The
    `lineage_stem` (claim/SD/script family token, None when underivable) lets
    `lineage_advanced` reject later letters that merely share the EXQ *number*
    stem but belong to a different experiment family.
    """
    fam: dict[int, list[tuple[str, str | None, str]]] = {}

    def add(num: int, letter: str, stem: str | None, signal: str) -> None:
        fam.setdefault(num, []).append((letter, stem, signal))

    if EXPERIMENTS_DIR.exists():
        for p in EXPERIMENTS_DIR.glob("v3_exq_*_v3.json"):
            mm = _MANIFEST_NAME_RE.match(p.name)
            if mm:
                add(int(mm.group(1)), mm.group(2).lower(), _lineage_stem(p.name),
                    f"manifest `{p.name}`")
        # run-pack dirs (manifest may be runs/<id>/manifest.json, not *_v3.json)
        for d in EXPERIMENTS_DIR.glob("v3_exq_*"):
            if d.is_dir():
                mm = _MANIFEST_NAME_RE.match(d.name)
                if mm:
                    add(int(mm.group(1)), mm.group(2).lower(), _lineage_stem(d.name),
                        f"manifest dir `{d.name}`")
    if PLANNING_DIR.exists():
        for p in PLANNING_DIR.glob("failure_autopsy_V3-EXQ-*_*.json"):
            mm = _AUTOPSY_NAME_RE.match(p.name)
            if mm:
                num, letter = int(mm.group(1)), mm.group(2).lower()
                add(num, letter, _autopsy_lineage_stem(p, num, letter),
                    f"autopsy `{p.name}`")
    return fam


def collect_confirmed_autopsies() -> list[dict]:
    """Confirmed failure-autopsies as {date, claim_ids:set, path} for signal B."""
    out: list[dict] = []
    if not PLANNING_DIR.exists():
        return out
    for p in PLANNING_DIR.glob("failure_autopsy_V3-EXQ-*_*.json"):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if (data.get("status") or "").strip().lower() not in CONFIRMED_AUTOPSY_STATUSES:
            continue
        claim_ids: set[str] = set()
        for t in data.get("targets") or []:
            if isinstance(t, dict):
                for c in t.get("claim_ids") or []:
                    if isinstance(c, str):
                        claim_ids.add(c.strip().upper())
        adate = _to_date(data.get("generated_utc"))
        if adate is None:
            mm = _AUTOPSY_NAME_RE.match(p.name)
            if mm:
                adate = _to_date(mm.group(3))
        out.append({"path": p.name, "date": adate, "claim_ids": claim_ids})
    return out


def lineage_advanced(
    owner_exq: str, fam: dict[int, list[tuple[str, str | None, str]]]
) -> str | None:
    """If a later-lettered sibling *of the same experiment lineage* as owner_exq
    has terminal evidence, describe it.

    A later EXQ *letter* under the same *number* is NOT sufficient: distinct,
    unrelated experiment families routinely share a number stem with letter
    suffixes (confirmed case: V3-EXQ-603k is the behavioral_diversity:GAP-C
    harm-pathway leg `stageh_harm_pathway_readiness`, while V3-EXQ-603m is the
    goal_pipeline:GAP-2 `scaffolded_sd054_full_curriculum_readiness` experiment
    -- they only both start with "603"). Keying on the number alone re-flagged
    GAP-C as lineage-advanced every governance cycle, desensitising the operator
    to the very "Stale since last update" signal that exists to catch the real
    goal_pipeline:GAP-2 miss (2026-06-03).

    Fix: a successor counts only if its lineage stem (the claim/SD/script family
    token) matches owner_exq's own lineage stem. We derive owner_exq's stem from
    its OWN terminal evidence. When owner_exq has no terminal evidence to derive
    a stem from (e.g. interrupted / never landed -- exactly the 514g profile of
    the 2026-06-03 goal_pipeline miss, where owner_exq pinned a stalled letter
    while later same-lineage letters landed), we cannot disambiguate, so we fall
    back to the prior number-only behaviour and keep all later-lettered siblings
    as candidates. That conservative fallback preserves the true-positive signal;
    the stem check only ever *removes* the false positives where owner_exq's own
    family is known and differs.
    """
    nl = _exq_num_letter(owner_exq)
    if nl is None:
        return None
    num, letter = nl
    entries = fam.get(num, [])

    # owner_exq's own lineage stem, from its own terminal evidence (if any).
    owner_stem: str | None = None
    for (lt, stem, _sig) in entries:
        if lt == letter and stem:
            owner_stem = stem
            break

    successors = [(lt, stem, sig) for (lt, stem, sig) in entries if lt > letter]
    if not successors:
        return None

    if owner_stem is not None:
        genuine = [(lt, stem, sig) for (lt, stem, sig) in successors if stem == owner_stem]
        lineage_note = ""
    else:
        # Cannot confirm lineage from owner_exq's own evidence -- be conservative.
        genuine = successors
        lineage_note = " (lineage unconfirmed -- owner_exq has no terminal evidence)"
    if not genuine:
        return None

    best_letter, _best_stem, best_sig = max(genuine, key=lambda t: t[0])
    return (
        f"owner_exq pins V3-EXQ-{num}{letter or '(base)'} but later same-lineage "
        f"sibling V3-EXQ-{num}{best_letter} has terminal evidence ({best_sig})"
        f"{lineage_note}"
    )


def claims_reclassified_since(node: dict, autopsies: list[dict]):
    """Confirmed autopsies touching this node's unblocks_claims, dated after last_updated."""
    unblocks = {
        str(c).strip().upper()
        for c in (node.get("unblocks_claims") or [])
        if isinstance(c, str)
    }
    if not unblocks:
        return None
    lu = _to_date(node.get("last_updated"))
    hits: list[str] = []
    for a in autopsies:
        if a["date"] is None:
            continue
        if lu is not None and not (a["date"] > lu):
            continue  # same-day or older == already reconciled
        overlap = sorted(a["claim_ids"] & unblocks)
        if overlap:
            hits.append(f"{a['path']} ({a['date'].isoformat()}) reclassified {', '.join(overlap)}")
    if not hits:
        return None
    # cap the rendered list so one ancient node can't flood the row
    shown = hits[:3]
    if len(hits) > 3:
        shown.append(f"(+{len(hits) - 3} more)")
    return "; ".join(shown)


def assembly_frontier_record(node: dict, today) -> dict | None:
    """If `node` is an assembling / open-by-design frontier node, return an audit
    record; else None. `revisit_due` is True only when an optional `revisit_after`
    date is set and has passed `today` -- the one signal that disturbs its rest.

    Pure + `today`-parameterised so it is unit-testable without a system clock."""
    status = (node.get("status") or "").strip().lower().replace(" ", "_")
    if status not in ASSEMBLING_STATUSES:
        return None
    revisit = _to_date(node.get("revisit_after"))
    revisit_due = revisit is not None and today is not None and revisit <= today
    return {
        "node_id": node.get("id"),
        "node_status": node.get("status"),
        "awaiting": node.get("awaiting"),
        "assembly_status": node.get("assembly_status"),
        "revisit_after": node.get("revisit_after"),
        "revisit_due": revisit_due,
        "last_updated": node.get("last_updated"),
    }


# --- Status-plane drift (status_history_plane:SHP-2) --------------------------


def _stored_live_view_from_plan(live_block) -> dict:
    """Coerce a plan node's stored `live:` block to the same shape the projector's
    `stored_live_view` emits, so the two are directly comparable."""
    if not isinstance(live_block, dict) or _psh is None:
        return {}
    out = {k: live_block.get(k) for k in _psh.STORED_LIVE_FIELDS}
    if live_block.get("needs_review") and live_block.get("needs_review_reasons"):
        out["needs_review_reasons"] = list(live_block["needs_review_reasons"])
    return out


def _stored_join_view_from_plan(join_block) -> dict:
    """Coerce a plan node's stored `join:` block to the same shape the projector's
    `stored_join_view` emits, so the two are directly comparable."""
    if not isinstance(join_block, dict) or _psh is None:
        return {}
    return {k: list(join_block.get(k) or []) for k in _psh.STORED_JOIN_FIELDS}


def _join_diff(stored: dict, projected: dict) -> list[str]:
    """Field-level mismatches between a stored and a projected join view.

    Both fields are ordered lists. `bears_on` is projector-sorted and
    `scope_claims` preserves the authored order, so list equality is the right
    comparison for both -- and a pure REORDER of the plan-level `scope_claims:`
    list is reported, since the re-stamp would rewrite it anyway (leaving it
    unflagged would mean the healer never converges)."""
    diffs: list[str] = []
    for f in _psh.STORED_JOIN_FIELDS:
        sv, pv = list(stored.get(f) or []), list(projected.get(f) or [])
        if sv == pv:
            continue
        missing = [x for x in pv if x not in sv]
        extra = [x for x in sv if x not in pv]
        if missing or extra:
            diffs.append(f"join.{f}: missing={missing} unexpected={extra}")
        else:
            diffs.append(f"join.{f}: same members, order differs")
    return diffs


def _live_diff(stored: dict, projected: dict) -> list[str]:
    """Field-level mismatches between a stored and a projected live view.
    Scalars compared as strings; needs_review as bool; reasons as ordered lists."""
    fields = list(_psh.STORED_LIVE_FIELDS) + ["needs_review_reasons"]
    diffs: list[str] = []
    for f in fields:
        sv, pv = stored.get(f), projected.get(f)
        if f == "needs_review":
            if bool(sv) != bool(pv):
                diffs.append(f"{f}: stored={bool(sv)} projected={bool(pv)}")
        elif f == "needs_review_reasons":
            if list(sv or []) != list(pv or []):
                diffs.append(f"{f}: stored={sv or []} projected={pv or []}")
        else:
            if (None if sv is None else str(sv)) != (None if pv is None else str(pv)):
                diffs.append(f"{f}: stored={sv!r} projected={pv!r}")
    return diffs


def status_plane_drift() -> tuple[list[dict], int, str | None]:
    """Re-project every collapsed node's `live` head and compare to the stored one.

    Returns (drifted, n_checked, note). `drifted` lists nodes where the stored
    two-plane `live:` block no longer matches the projection from the append-only
    event log -- i.e. the plan needs re-projection. governance.sh Step 3c-pre-heal
    (scripts/heal_status_plane_drift.py) now re-stamps every fully-collapsed
    drifted plan in place BEFORE this check runs, so in a governance cycle this
    section reports the post-heal residual -- typically only mixed plans that still
    carry un-collapsed blob nodes (collapse-migration stays a human step). Run
    standalone it is still a pure warn-only hint. `note` is a skip reason when the
    projector is unavailable."""
    if _psh is None:
        return [], 0, "project_status_head unavailable -- status-plane check skipped"
    planning_dir = REPO_ROOT / "evidence" / "planning"
    try:
        plans, _skipped = _psh.load_plans(str(planning_dir))
        events, _counts = _psh.load_events(str(REPO_ROOT))
        projections = _psh.build_projections(plans, events, _psh.DEFAULT_BRAKE_THRESHOLD)
    except Exception as e:  # pragma: no cover - defensive
        return [], 0, f"status-plane projection failed: {e}"

    # stored `live:` blocks live in the raw frontmatter (load_plans drops them).
    drifted: list[dict] = []
    n_checked = 0
    for path in sorted(planning_dir.glob("*_plan.md")):
        fm = parse_plan_frontmatter(path)
        plan = fm.get("closure_plan") if isinstance(fm, dict) else None
        if not isinstance(plan, dict):
            continue
        for node in plan.get("nodes", []) or []:
            if not isinstance(node, dict):
                continue
            live_block = node.get("live")
            if not isinstance(live_block, dict):
                continue  # not a two-plane (collapsed) node -- nothing to check
            nid = node.get("id")
            pr = projections.get(nid)
            if pr is None:
                continue
            n_checked += 1
            stored = _stored_live_view_from_plan(live_block)
            projected = _psh.stored_live_view(pr["live"])
            diffs = _live_diff(stored, projected)

            # History-plane half. Checked even when `live:` matches: editing the
            # plan-level `scope_claims:` list re-scopes the join of EVERY node in
            # the plan, and when that edit moves no node's live head a live-only
            # check sees nothing at all -- so the stored joins go stale with no
            # signal and the healer never fires. Because the healer re-stamps by
            # PLAN (any drifted node re-stamps the whole file, and the re-stamp
            # compares the full live:+join: block), surfacing join drift here is
            # what makes a plan-level scope edit self-heal on the next cycle.
            join_block = node.get("join")
            if isinstance(join_block, dict):
                diffs = diffs + _join_diff(
                    _stored_join_view_from_plan(join_block),
                    _psh.stored_join_view(pr),
                )

            if diffs:
                drifted.append({
                    "plan": path.name,
                    "node_id": nid,
                    "diffs": diffs,
                    "projected_from": projected.get("from"),
                    "stored_from": stored.get("from"),
                })
    return drifted, n_checked, None


def main() -> int:
    today = datetime.now(timezone.utc).date()
    queue_ids = load_queue_ids()
    terminal_fam = collect_terminal_lineage()
    confirmed_autopsies = collect_confirmed_autopsies()
    findings: list[dict] = []
    suppressed: list[dict] = []
    stale_since: list[dict] = []
    assembly_frontier: list[dict] = []
    missing_plan_last_updated: list[str] = []

    for plan_name in _discover_plan_files():
        path = PLANNING_DIR / plan_name
        fm = parse_plan_frontmatter(path)
        plan = fm.get("closure_plan") if isinstance(fm, dict) else None
        if not isinstance(plan, dict):
            continue

        # Drift checking is V3-only. V4/V5 forward-roadmap plans have no
        # experiments yet (no owner_exq), so terminal-state drift is undefined
        # for them; skip so they can never be false-flagged.
        if str(plan.get("generation") or "v3").strip().lower() != "v3":
            continue

        if not plan.get("last_updated"):
            missing_plan_last_updated.append(plan_name)

        for node in plan.get("nodes", []) or []:
            if not isinstance(node, dict):
                continue
            status = (node.get("status") or "").strip().lower().replace(" ", "_")
            # Assembling nodes are restful: collect for the audit section, then
            # skip the drifted / stale-since passes entirely (they are not in
            # NON_TERMINAL_STATUSES, so the gate below already skips them -- this
            # collection just makes them visible without nagging).
            af = assembly_frontier_record(node, today)
            if af is not None:
                af["plan"] = plan_name
                assembly_frontier.append(af)
            if status not in NON_TERMINAL_STATUSES:
                continue

            # Date-aware stale-since pass: runs for EVERY non-terminal node,
            # independent of whether the owner_exq pass below suppresses it.
            owner_raw = node.get("owner_exq")
            owner_str = owner_raw.strip() if isinstance(owner_raw, str) else ""
            reasons: list[str] = []
            if owner_str:
                la = lineage_advanced(owner_str, terminal_fam)
                if la:
                    reasons.append(la)
            cr = claims_reclassified_since(node, confirmed_autopsies)
            if cr:
                reasons.append(cr)
            if reasons:
                stale_since.append({
                    "plan": plan_name,
                    "node_id": node.get("id"),
                    "node_status": node.get("status"),
                    "owner_exq": owner_str or None,
                    "node_last_updated": node.get("last_updated"),
                    "reasons": reasons,
                })

            owner_exq = node.get("owner_exq")
            if not isinstance(owner_exq, str):
                continue
            exq_id = owner_exq.strip()
            if not EXQ_RE.search(exq_id):
                continue

            still_queued = exq_id.upper() in queue_ids
            manifest = find_terminal_manifest(exq_id)
            autopsy = find_failure_autopsy(exq_id)

            if still_queued:
                continue
            if not manifest and not autopsy:
                continue

            manifest_direction = manifest_evidence_direction(manifest) if manifest else None
            suppress_reason: str | None = None
            if node_is_case_3(node):
                suppress_reason = "case_3_self_tag"
            elif manifest_direction in NON_CONTRIBUTORY_DIRECTIONS:
                suppress_reason = f"manifest_evidence_direction={manifest_direction}"

            record = {
                "plan": plan_name,
                "node_id": node.get("id"),
                "node_status": node.get("status"),
                "owner_exq": exq_id,
                "node_last_updated": node.get("last_updated"),
                "manifest": manifest.relative_to(REPO_ROOT).as_posix() if manifest else None,
                "autopsy": autopsy.relative_to(REPO_ROOT).as_posix() if autopsy else None,
                "title": (node.get("title") or "")[:120],
                "suppress_reason": suppress_reason,
            }
            if suppress_reason:
                suppressed.append(record)
            else:
                findings.append(record)

    status_drifted, status_checked, status_note = status_plane_drift()

    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines: list[str] = []
    lines.append(f"# Closure-Plan Drift Report")
    lines.append("")
    lines.append(f"Generated: {now_iso}")
    lines.append("")
    lines.append(
        "This report flags closure_plan nodes whose `owner_exq` has reached a "
        "terminal state (manifest landed and / or failure_autopsy artifact "
        "present) but whose `status` is still non-terminal. Nodes that "
        "self-tag as Case 3 (legitimately non-terminal pending upstream "
        "substrate or successor EXQs) and nodes whose owner_exq manifest is "
        "non-contributory / superseded / inconclusive are recorded under "
        "Suppressed instead, not Drifted. A separate date-aware section, "
        "`Stale since last update`, flags non-terminal nodes (including "
        "suppressed ones) where a later-lettered owner_exq sibling reached "
        "terminal state or a confirmed failure_autopsy touching the node's "
        "`unblocks_claims` post-dates the node's `last_updated` -- the class "
        "of staleness that hid goal_pipeline:GAP-2 on 2026-06-03. The report "
        "also flags plans missing a top-level `closure_plan.last_updated` field."
    )
    lines.append("")
    lines.append("Warn-only -- this script never blocks the governance pipeline.")
    lines.append("")

    lines.append(f"## Drifted nodes ({len(findings)})")
    lines.append("")
    if not findings:
        lines.append("_None._")
        lines.append("")
    else:
        lines.append("| plan | node | status | owner_exq | node last_updated | terminal signal |")
        lines.append("|------|------|--------|-----------|-------------------|-----------------|")
        for f in findings:
            signal_parts = []
            if f["manifest"]:
                signal_parts.append(f"manifest `{f['manifest']}`")
            if f["autopsy"]:
                signal_parts.append(f"autopsy `{f['autopsy']}`")
            lines.append(
                "| {plan} | `{node}` | {status} | {exq} | {lu} | {sig} |".format(
                    plan=f["plan"],
                    node=f["node_id"] or "?",
                    status=f["node_status"] or "?",
                    exq=f["owner_exq"],
                    lu=f["node_last_updated"] or "_unset_",
                    sig=" + ".join(signal_parts) or "?",
                )
            )
        lines.append("")

    lines.append(f"## Suppressed (legitimately non-terminal) ({len(suppressed)})")
    lines.append("")
    if not suppressed:
        lines.append("_None._")
        lines.append("")
    else:
        lines.append(
            "Nodes whose `owner_exq` reached a terminal state but where "
            "suppression rules say the node is legitimately non-terminal "
            "(Case-3 self-tag or non-contributory manifest evidence_direction). "
            "Listed here for audit; not counted as drift."
        )
        lines.append("")
        lines.append("| plan | node | status | owner_exq | suppress reason |")
        lines.append("|------|------|--------|-----------|-----------------|")
        for s in suppressed:
            lines.append(
                "| {plan} | `{node}` | {status} | {exq} | {reason} |".format(
                    plan=s["plan"],
                    node=s["node_id"] or "?",
                    status=s["node_status"] or "?",
                    exq=s["owner_exq"],
                    reason=s["suppress_reason"] or "?",
                )
            )
        lines.append("")

    # Drifted nodes already carry the strongest "go fix me" call; don't repeat
    # them in the review section. Suppressed nodes DO belong here -- suppression
    # on owner_exq is exactly what hid GAP-2.
    drifted_keys = {(f["plan"], f["node_id"]) for f in findings}
    stale_review = [s for s in stale_since if (s["plan"], s["node_id"]) not in drifted_keys]

    lines.append(f"## Stale since last update -- review ({len(stale_review)})")
    lines.append("")
    if not stale_review:
        lines.append("_None._")
        lines.append("")
    else:
        lines.append(
            "Non-terminal nodes (including ones Suppressed above) where newer "
            "evidence landed that the node frontmatter may not have absorbed: a "
            "later-lettered owner_exq sibling reached terminal state (lineage "
            "advanced), and / or a confirmed failure_autopsy touching the node's "
            "`unblocks_claims` is dated after the node's `last_updated`. Review "
            "each: update owner_exq / status / resume_condition and bump "
            "`last_updated`, or (if the new evidence genuinely does not change the "
            "node) bump `last_updated` to acknowledge it. Not counted as drift."
        )
        lines.append("")
        lines.append("| plan | node | status | owner_exq | node last_updated | why |")
        lines.append("|------|------|--------|-----------|-------------------|-----|")
        for s in stale_review:
            exq_disp = s["owner_exq"] or "_none_"
            if len(exq_disp) > 60:
                exq_disp = exq_disp[:57] + "..."
            lines.append(
                "| {plan} | `{node}` | {status} | {exq} | {lu} | {why} |".format(
                    plan=s["plan"],
                    node=s["node_id"] or "?",
                    status=s["node_status"] or "?",
                    exq=exq_disp,
                    lu=s["node_last_updated"] or "_unset_",
                    why="; ".join(s["reasons"]),
                )
            )
        lines.append("")

    revisit_due = [a for a in assembly_frontier if a.get("revisit_due")]
    lines.append(
        f"## Assembly frontier -- resting, not drift ({len(assembly_frontier)}"
        + (f"; {len(revisit_due)} due for revisit" if revisit_due else "")
        + ")"
    )
    lines.append("")
    lines.append(
        "Nodes with status `assembling` / `open_by_design`: required for v3 but "
        "under construction. They are a stable resting state -- NOT counted as "
        "drift or stale, and they need no recurring re-stamp to stay quiet. Listed "
        "here for visibility only. A node flagged **revisit_due** has passed its "
        "optional `revisit_after` date and should be reviewed (resume / re-state / "
        "extend the date)."
    )
    lines.append("")
    if not assembly_frontier:
        lines.append("_None._")
        lines.append("")
    else:
        lines.append("| plan | node | status | awaiting | assembly_status | revisit_after | revisit_due |")
        lines.append("|------|------|--------|----------|-----------------|---------------|-------------|")
        for a in assembly_frontier:
            lines.append(
                "| {plan} | `{node}` | {status} | {aw} | {asx} | {rv} | {due} |".format(
                    plan=a["plan"],
                    node=a["node_id"] or "?",
                    status=a["node_status"] or "?",
                    aw=str(a.get("awaiting") or "")[:60] or "_unset_",
                    asx=a.get("assembly_status") or "_unset_",
                    rv=a.get("revisit_after") or "_none_",
                    due="**yes**" if a.get("revisit_due") else "no",
                )
            )
        lines.append("")

    # --- Status-plane drift (status_history_plane:SHP-2) ----------------------
    lines.append(
        f"## Status-plane drift -- projected `live` != stored `live` "
        f"({len(status_drifted)} of {status_checked} collapsed node(s))"
    )
    lines.append("")
    lines.append(
        "SHP-2 two-plane nodes carry a stored `live:` head that is a pure "
        "projection over the append-only event log. This section re-projects each "
        "and flags any whose stored head has gone stale vs the events (a new "
        "autopsy / PASS manifest / decision landed, or the reconcile / brake state "
        "moved). In a governance cycle it is self-healing: Step 3c-pre-heal "
        "(scripts/heal_status_plane_drift.py) re-stamps every fully-collapsed "
        "drifted plan IN PLACE before this check runs (leaving the edited plan "
        "file uncommitted for a human to review + commit pathspec-limited), so a "
        "residual count here is normally a MIXED plan that still has un-collapsed "
        "blob nodes -- re-stamp it manually with "
        "`scripts/shp2_collapse_and_verify.py --plan <plan>` once collapsed (the "
        "collapse step re-projects already-collapsed drifted nodes in place, then "
        "re-runs this check as gate 4), or `scripts/shp2_collapse_plan.py --plan "
        "<plan>` for the re-stamp without the gates. Both regenerate `live:`+`join:` "
        "via the one projection path and are byte-identical no-ops on up-to-date "
        "nodes. Nodes with no `live:` block are not yet collapsed and are not "
        "checked here."
    )
    lines.append("")
    if status_note:
        lines.append(f"_Skipped: {status_note}._")
        lines.append("")
    elif not status_drifted:
        lines.append("_None -- every collapsed node's stored `live` matches its projection._")
        lines.append("")
    else:
        lines.append("| plan | node | stored from | projected from | drifted fields |")
        lines.append("|------|------|-------------|----------------|----------------|")
        for d in status_drifted:
            lines.append(
                "| {plan} | `{node}` | {sf} | {pf} | {fields} |".format(
                    plan=d["plan"],
                    node=d["node_id"] or "?",
                    sf=d["stored_from"] or "_none_",
                    pf=d["projected_from"] or "_none_",
                    fields="; ".join(d["diffs"]),
                )
            )
        lines.append("")

    lines.append(f"## Plans missing `closure_plan.last_updated` ({len(missing_plan_last_updated)})")
    lines.append("")
    if not missing_plan_last_updated:
        lines.append("_None._")
    else:
        for name in missing_plan_last_updated:
            lines.append(f"- `evidence/planning/{name}`")
    lines.append("")

    DRIFT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # JSON sidecar for the closure map. `drifted` and `stale_since` are the two
    # non-overlapping buckets the map marks (stale_review already excludes nodes
    # already counted as drifted). Suppressed nodes are intentionally NOT marked
    # -- they are legitimately non-terminal.
    drift_payload = {
        "generated_at": now_iso,
        "counts": {
            "drifted": len(findings),
            "stale_since": len(stale_review),
            "suppressed": len(suppressed),
            "assembling": len(assembly_frontier),
            "assembling_revisit_due": len(revisit_due),
            "status_plane_drifted": len(status_drifted),
            "status_plane_checked": status_checked,
        },
        "status_plane_drift": {
            "checked": status_checked,
            "skipped_reason": status_note,
            "drifted": status_drifted,
        },
        "assembly_frontier": [
            {
                "node_id": a["node_id"],
                "plan": a["plan"],
                "node_status": a["node_status"],
                "awaiting": a.get("awaiting"),
                "assembly_status": a.get("assembly_status"),
                "revisit_after": a.get("revisit_after"),
                "revisit_due": a.get("revisit_due"),
            }
            for a in assembly_frontier
        ],
        "drifted": [
            {
                "node_id": f["node_id"],
                "plan": f["plan"],
                "node_status": f["node_status"],
                "owner_exq": f["owner_exq"],
                "manifest": f["manifest"],
                "autopsy": f["autopsy"],
            }
            for f in findings
        ],
        "stale_since": [
            {
                "node_id": s["node_id"],
                "plan": s["plan"],
                "node_status": s["node_status"],
                "owner_exq": s["owner_exq"],
                "node_last_updated": s["node_last_updated"],
                "reasons": s["reasons"],
            }
            for s in stale_review
        ],
    }
    DRIFT_JSON.write_text(
        json.dumps(drift_payload, indent=2, default=str) + "\n", encoding="utf-8")

    print(f"Closure drift report written: {DRIFT_REPORT.relative_to(REPO_ROOT)}")
    print(
        f"  drifted_nodes={len(findings)}  "
        f"suppressed={len(suppressed)}  "
        f"stale_since_review={len(stale_review)}  "
        f"assembling={len(assembly_frontier)} (revisit_due={len(revisit_due)})  "
        f"status_plane_drift={len(status_drifted)}/{status_checked}  "
        f"plans_missing_last_updated={len(missing_plan_last_updated)}"
    )
    return 0


def _self_test() -> int:
    """Regression fixtures for the lineage-advanced stem check. Run with
    `--self-test`; exits non-zero on any failure.

    Anchors:
      * NEGATIVE (the bug, 2026-06-10): V3-EXQ-603k (stageh_harm_pathway) must
        NOT be flagged lineage-advanced by V3-EXQ-603m (scaffolded_sd054) or
        603l (escape_affordance) -- distinct families that merely share "603".
      * POSITIVE (the signal to preserve, 2026-06-03): goal_pipeline:GAP-2 owner
        V3-EXQ-514g (sd049 family) MUST still flag when later sd049 letters
        (514l) landed terminal evidence -- both when 514g has its own evidence
        (stem match) and when it has none (conservative fallback, the real
        interrupted-514g profile).
    """
    failures: list[str] = []

    def check(name: str, cond: bool) -> None:
        if cond:
            print(f"  ok   {name}")
        else:
            failures.append(name)
            print(f"  FAIL {name}")

    # --- name/stem parsing on the real artifact names -------------------------
    check(
        "stem(603k manifest)==stageh",
        _lineage_stem("v3_exq_603k_stageh_harm_pathway_readiness_20260609T181419Z_v3.json")
        == "stageh",
    )
    check(
        "stem(603m manifest)==scaffolded",
        _lineage_stem(
            "v3_exq_603m_scaffolded_sd054_full_curriculum_readiness_20260610T133806Z_v3.json"
        )
        == "scaffolded",
    )
    check(
        "stem(603m run-pack dir)==scaffolded",
        _lineage_stem("v3_exq_603m_scaffolded_sd054_full_curriculum_readiness")
        == "scaffolded",
    )
    check(
        "stem(514g manifest)==sd049",
        _lineage_stem("v3_exq_514g_sd049_bg_gating_wider_seeds_stepharness") == "sd049",
    )
    check(
        "stem(514l run_id)==sd049",
        _lineage_stem(
            "v3_exq_514l_sd049_phase3_mech229_wanting_liking_identity_20260602T170106Z_v3"
        )
        == "sd049",
    )
    check("stem(non-exq name) is None", _lineage_stem("failure_autopsy_V3-EXQ-603l_2026-06-10") is None)

    # --- lineage_advanced fixtures -------------------------------------------
    # NEGATIVE: 603k owns a stageh manifest; 603l (escape) + 603m (scaffolded)
    # are later letters but different families -> must NOT flag.
    fam_603 = {
        603: [
            ("k", "stageh", "manifest `v3_exq_603k_stageh_harm_pathway_readiness_..._v3.json`"),
            ("l", "escape", "autopsy `failure_autopsy_V3-EXQ-603l_2026-06-10.json`"),
            ("m", "scaffolded", "manifest `v3_exq_603m_scaffolded_sd054_..._v3.json`"),
        ]
    }
    check(
        "603k NOT flagged by 603m/603l (stem mismatch)",
        lineage_advanced("V3-EXQ-603k", fam_603) is None,
    )

    # POSITIVE-A: 514g owns an sd049 manifest; 514l (sd049) is a later same-family
    # letter -> must flag and cite 514l.
    fam_514_with_owner = {
        514: [
            ("g", "sd049", "manifest `v3_exq_514g_sd049_bg_gating_wider_seeds_stepharness_..._v3.json`"),
            ("l", "sd049", "autopsy `failure_autopsy_V3-EXQ-514l_2026-06-03.json`"),
        ]
    }
    res_a = lineage_advanced("V3-EXQ-514g", fam_514_with_owner)
    check("514g flagged by 514l (stem match)", res_a is not None and "514l" in res_a)

    # POSITIVE-B: the real 2026-06-03 profile -- 514g was interrupted and has NO
    # terminal evidence of its own; only later sd049 letters landed. Owner stem
    # is underivable -> conservative fallback must still flag.
    fam_514_no_owner = {
        514: [
            ("l", "sd049", "autopsy `failure_autopsy_V3-EXQ-514l_2026-06-03.json`"),
        ]
    }
    res_b = lineage_advanced("V3-EXQ-514g", fam_514_no_owner)
    check(
        "514g flagged by 514l when owner has no own evidence (conservative fallback)",
        res_b is not None and "514l" in res_b,
    )

    # GUARD: a cross-family later letter must NOT flag when owner's stem is known,
    # even if no same-family successor exists (the precise 603 false-positive shape).
    fam_mixed = {
        603: [
            ("k", "stageh", "manifest stageh"),
            ("m", "scaffolded", "manifest scaffolded"),
        ]
    }
    check(
        "known-owner-stem + only cross-family successor -> no flag",
        lineage_advanced("V3-EXQ-603k", fam_mixed) is None,
    )

    # --- assembly_frontier_record fixtures -----------------------------------
    today = datetime(2026, 6, 21).date()  # fixed date literal (deterministic, not a clock read)
    check(
        "in_progress node is NOT an assembly-frontier record",
        assembly_frontier_record({"id": "X", "status": "in_progress"}, today) is None,
    )
    rec_no_rv = assembly_frontier_record(
        {"id": "GAP-8", "status": "assembling", "awaiting": "MECH-449"}, today)
    check(
        "assembling node -> record, restful (revisit_due False with no revisit_after)",
        rec_no_rv is not None and rec_no_rv["revisit_due"] is False
        and rec_no_rv["awaiting"] == "MECH-449",
    )
    check(
        "open_by_design alias -> record",
        assembly_frontier_record({"id": "Y", "status": "open_by_design"}, today) is not None,
    )
    rec_past = assembly_frontier_record(
        {"id": "Z", "status": "assembling", "revisit_after": "2026-06-01"}, today)
    check(
        "past revisit_after -> revisit_due True",
        rec_past is not None and rec_past["revisit_due"] is True,
    )
    rec_future = assembly_frontier_record(
        {"id": "W", "status": "assembling", "revisit_after": "2026-12-31"}, today)
    check(
        "future revisit_after -> revisit_due False (still resting)",
        rec_future is not None and rec_future["revisit_due"] is False,
    )

    # --- _join_diff fixtures (history-plane drift) ----------------------------
    # Anchor (2026-07-18): a plan-level `scope_claims:` edit re-scopes the join of
    # EVERY node in the plan while moving no live head. A live-only check saw
    # nothing, so the healer never fired and the stored joins went silently stale.
    # Verified end-to-end in a sandbox: adding one claim to the plan-level list
    # flagged 7/7 nodes (live-only: 0) and the healer re-stamped the whole plan.
    if _psh is not None:
        check(
            "join_diff: identical join -> no drift",
            _join_diff({"bears_on": ["a"], "scope_claims": ["M-1"]},
                       {"bears_on": ["a"], "scope_claims": ["M-1"]}) == [],
        )
        added = _join_diff({"bears_on": [], "scope_claims": ["M-1"]},
                           {"bears_on": [], "scope_claims": ["M-1", "M-2"]})
        check(
            "join_diff: plan-level scope ADD is drift (the 2026-07-18 blind spot)",
            len(added) == 1 and "missing=['M-2']" in added[0],
        )
        removed = _join_diff({"bears_on": [], "scope_claims": ["M-1", "M-2"]},
                             {"bears_on": [], "scope_claims": ["M-1"]})
        check(
            "join_diff: scope REMOVE is drift",
            len(removed) == 1 and "unexpected=['M-2']" in removed[0],
        )
        check(
            "join_diff: bears_on drift reported under its own field",
            _join_diff({"bears_on": ["a"], "scope_claims": []},
                       {"bears_on": ["a", "b"], "scope_claims": []})[0].startswith(
                           "join.bears_on:"),
        )
        reordered = _join_diff({"bears_on": [], "scope_claims": ["M-2", "M-1"]},
                               {"bears_on": [], "scope_claims": ["M-1", "M-2"]})
        check(
            "join_diff: pure REORDER is drift (else the re-stamp never converges)",
            len(reordered) == 1 and "order differs" in reordered[0],
        )
        # The stored view must round-trip what the projector emits, or the two
        # halves disagree and the healer loops re-stamping the same value.
        check(
            "stored_join_view round-trips through _stored_join_view_from_plan",
            _stored_join_view_from_plan(
                _psh.stored_join_view({"join_bears_on": ["a"],
                                       "node_scope_claims": ["M-1"]}))
            == {"bears_on": ["a"], "scope_claims": ["M-1"]},
        )
        check(
            "stored_join_view uses the NODE scope, not the plan scope",
            _psh.stored_join_view(
                {"join_bears_on": [], "node_scope_claims": ["M-9"]})["scope_claims"]
            == ["M-9"],
        )

    print()
    if failures:
        print(f"SELF-TEST FAILED: {len(failures)} failure(s): {', '.join(failures)}")
        return 1
    print("SELF-TEST PASSED")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(_self_test())
    sys.exit(main())
