#!/usr/bin/env python3
"""evidence_strip_data.py -- DRAFT data layer for the docs-site "evidence strip".

STATUS: draft only. Not wired into any repo. Nothing under REE_Working is
written or committed by this file or by importing it.

Pattern copied from REE_assembly/scripts/generate_current_front.py: every
extraction has a labelled, independent fallback. A missing file, a renamed
heading, a malformed YAML/JSON document, or an absent directory degrades that
one figure to "absent" -- it never raises, and it never substitutes 0 for
"could not derive". 0 is only ever emitted when the source was read
successfully and genuinely reports zero.

Output key names match the sibling presentation-layer draft already sitting
in this scratchpad (evidence_strip_markup.md's render_evidence_strip(data)):

    closure_pct, closure_done, closure_remaining, closure_total,
    claims_total, claims_active, claims_provisional, claims_candidate,
    runs_logged

plus one extra, additive key not in that contract -- claims_by_status (the
full per-status breakdown the brief asked for; the presentation layer only
reads three named statuses out of it, but the fuller map is cheap to carry
and may be useful later). See NOTES_data_layer.md for the full reasoning,
parse-strategy choices, and brittleness notes.
"""

import json
import os
import re

try:
    import yaml
except ImportError:  # pragma: no cover -- exercised only if PyYAML is absent
    yaml = None


CLOSURE_REL = os.path.join("evidence", "planning", "closure_status.md")
CLAIMS_REL = os.path.join("docs", "claims", "claims.yaml")
EXPERIMENTS_REL = os.path.join("evidence", "experiments")

# A flat-layout file counts as a result manifest only if it carries a run_id
# AND at least one field that actually links it to claim evidence. This is
# what separates the ~1000 real manifests in evidence/experiments/ from the
# ~8 index/tracker files that also live there flat (review_tracker.json,
# runner_status.json, substrate_status_snapshot.json, arm_fingerprint_index.json,
# claim_evidence.v1.json, fail_autopsy_grandfather.json, ...) -- none of those
# carry any of these four keys.
_EVIDENCE_MARKER_KEYS = ("outcome", "evidence_direction", "claim_ids", "claim_ids_tested")

# Auxiliary state directories directly under evidence/experiments/ that are
# NOT experiment directories and must not be walked into when hunting for
# nested manifest.json files.
_EXP_AUX_DIR_NAMES = {".derived", "_partial", "_runner_signals"}


def _read_text(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return None


def _load_json_soft(path):
    """Best-effort JSON load. None on any read/parse error -- never raises."""
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def _search(pattern, text, group=1, flags=0):
    m = re.search(pattern, text, flags)
    if not m:
        return None
    try:
        return m.group(group).strip()
    except IndexError:
        return None


# ---------------------------------------------------------------------------
# 1. v3 closure -- evidence/planning/closure_status.md
# ---------------------------------------------------------------------------

def _gather_closure(root):
    """Each of the four figures is extracted independently -- a reworded
    line loses only that one figure, not the whole group."""
    text = _read_text(os.path.join(root, CLOSURE_REL))
    if not text:
        return {}

    out = {}

    pct = _search(r"Weighted progress:\s*\*\*([\d.]+)%\*\*", text)
    if pct is not None:
        try:
            out["closure_pct"] = float(pct)
        except ValueError:
            pass

    total = _search(r"across\s+(\d+)\s+non-deferred nodes", text)
    if total is not None:
        try:
            out["closure_total"] = int(total)
        except ValueError:
            pass

    remaining = _search(r"Remaining\s*\([^)]*\)\s*:\s*\*\*(\d+)\*\*", text)
    if remaining is not None:
        try:
            out["closure_remaining"] = int(remaining)
        except ValueError:
            pass

    # "- Done: 64 nodes." -- deliberately NOT bold-wrapped in the source
    # (unlike the weighted-progress and remaining lines above), so this one
    # regex does not require the ** markers the others do.
    done = _search(r"^-\s*Done:\s*(\d+)\s*nodes\.", text, flags=re.MULTILINE)
    if done is not None:
        try:
            out["closure_done"] = int(done)
        except ValueError:
            pass

    return out


# ---------------------------------------------------------------------------
# 2. claims -- docs/claims/claims.yaml
# ---------------------------------------------------------------------------

def _gather_claims(root):
    """Full yaml.safe_load, not a line-scan. See NOTES_data_layer.md for the
    measurement and reasoning; short version: yaml.safe_load takes ~2.7s on
    the live 1103-entry / 7MB file, which is acceptable for a governance-run
    batch script (this is not a per-page-load path), and it is the only
    strategy that survives claims.yaml's documented inline-comment-on-enum
    hazard (project memory: reference_claims_yaml_no_inline_comments_on_enum_fields)
    without extra bespoke stripping logic -- e.g. one live entry reads
    'status: active   # RATE/consumption leg is substrate_conditional ...',
    which a naive '^  status: (\\S+)' line-scan resolves to the wrong,
    comment-glued token unless the comment is stripped first."""
    if yaml is None:
        return {}

    path = os.path.join(root, CLAIMS_REL)
    try:
        with open(path, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
    except (OSError, ValueError, UnicodeDecodeError):
        return {}
    except Exception:  # pragma: no cover -- belt-and-braces: any yaml.* error
        return {}

    if not isinstance(data, list):
        return {}

    by_status = {}
    total = 0
    for entry in data:
        if not isinstance(entry, dict):
            continue
        status = entry.get("status")
        if not isinstance(status, str) or not status:
            continue
        by_status[status] = by_status.get(status, 0) + 1
        total += 1

    if total == 0:
        return {}

    out = {
        "claims_total": total,
        "claims_by_status": by_status,
        # Explicit, presentation-contract keys. Defaulted to 0 (not omitted)
        # because the parse as a whole succeeded -- a status genuinely
        # absent from the registry is real information ("0 candidates"),
        # distinguishable from "claims.yaml could not be read at all"
        # (which instead omits every claims_* key, handled above).
        "claims_active": by_status.get("active", 0),
        "claims_provisional": by_status.get("provisional", 0),
        "claims_candidate": by_status.get("candidate", 0),
    }
    return out


# ---------------------------------------------------------------------------
# 3. logged experiment runs -- evidence/experiments/
# ---------------------------------------------------------------------------

def _gather_experiment_runs(root):
    """Counts UNIQUE run_id values found across BOTH manifest layouts that
    coexist under evidence/experiments/:

      (a) flat top-level '<run_id>.json' files directly in evidence/experiments/
          (~1000 on the live repo; a handful of non-manifest index/tracker
          files also live here flat and are excluded via _EVIDENCE_MARKER_KEYS)
      (b) nested 'manifest.json' files, overwhelmingly under
          evidence/experiments/<exp_dir>/runs/<run_id>/manifest.json (the
          dominant modern layout -- ~2925 on the live repo, ~3x the flat
          count) plus a handful of older per-experiment layouts that skip the
          'runs/' segment entirely.

    A run that has BOTH a flat mirror and a nested pack copy (the common
    case -- ~982 of the ~1000 flat manifests on the live repo) is counted
    ONCE, by run_id. See NOTES_data_layer.md for the measurement that
    established this is the right union, not double-counting."""
    exp_dir = os.path.join(root, EXPERIMENTS_REL)
    if not os.path.isdir(exp_dir):
        return {}

    run_ids = set()

    try:
        names = os.listdir(exp_dir)
    except OSError:
        names = []
    for name in names:
        if not name.endswith(".json"):
            continue
        fpath = os.path.join(exp_dir, name)
        if not os.path.isfile(fpath):
            continue
        d = _load_json_soft(fpath)
        if not isinstance(d, dict):
            continue
        rid = d.get("run_id")
        if isinstance(rid, str) and rid and any(k in d for k in _EVIDENCE_MARKER_KEYS):
            run_ids.add(rid)

    try:
        for dirpath, dirnames, filenames in os.walk(exp_dir):
            rel = os.path.relpath(dirpath, exp_dir)
            if rel == ".":
                # prune the auxiliary state dirs so os.walk never descends
                # into them at all (not just skips their manifest.json)
                dirnames[:] = [d for d in dirnames if d not in _EXP_AUX_DIR_NAMES]
            if "manifest.json" in filenames:
                d = _load_json_soft(os.path.join(dirpath, "manifest.json"))
                if isinstance(d, dict):
                    rid = d.get("run_id")
                    if isinstance(rid, str) and rid:
                        run_ids.add(rid)
    except OSError:
        pass

    # A directory that exists but truly has nothing in it is a real zero,
    # not "unknown" -- so this branch returns {"runs_logged": 0} rather than
    # {}. {} is reserved for "evidence/experiments/ does not exist at all"
    # (the isdir() guard above).
    return {"runs_logged": len(run_ids)}


CLAIM_EVIDENCE_REL = os.path.join("evidence", "experiments", "claim_evidence.v1.json")


def _gather_claim_evidence(root):
    """Derive figures from the claim/evidence join, NOT from claim status.

    WHY THIS EXISTS, and why status counts are not a substitute: status and
    experimental evidence are substantially decoupled in this registry.
    Measured 2026-09-07: only 25 of 68 `active` and 60 of 97 `provisional`
    claims carry a supporting experimental entry, while 98 `candidate`
    claims do. So "active + provisional" would BOTH overclaim (about half
    of that set has no supporting experimental result) and undercount (it
    silently drops those 98 candidates). Anything the page says about
    evidence must therefore be read off this join, which is regenerated by
    the governance run, and never inferred from a status tally.
    """
    path = os.path.join(root, CLAIM_EVIDENCE_REL)
    doc = _load_json_soft(path)
    if not isinstance(doc, dict):
        return {}
    entries = doc.get("entries")
    if not isinstance(entries, list):
        return {}

    supporting_claims = set()
    linked_claims = set()
    directions = {}
    for e in entries:
        if not isinstance(e, dict):
            continue
        cid = e.get("claim_id")
        if cid:
            linked_claims.add(cid)
        direction = e.get("evidence_direction")
        if direction:
            directions[direction] = directions.get(direction, 0) + 1
        klass = e.get("evidence_class") or ""
        if cid and klass.startswith("exp") and direction == "supports":
            supporting_claims.add(cid)

    out = {
        "evidence_entries": len(entries),
        "evidence_claims_linked": len(linked_claims),
        "claims_with_supporting_evidence": len(supporting_claims),
    }
    if "supports" in directions:
        out["evidence_supports"] = directions["supports"]
    if "weakens" in directions:
        out["evidence_weakens"] = directions["weakens"]
    return out


# ---------------------------------------------------------------------------
# public entry point
# ---------------------------------------------------------------------------

def gather_evidence_figures(root):
    """root = absolute path to the REE_assembly repo. Returns a dict of
    figures, or None.

    Fail-open per source: closure / claims / experiments are each gathered
    independently inside their own try/except, so a crash in one extractor
    (an unanticipated OS error, a library surprise, anything) can never take
    the other two down with it, and never propagates out of this function.

    Absent vs zero: a key is present only when its source was read AND
    parsed; a genuinely-zero count from a successfully-read source is
    reported as 0, never omitted. A key is omitted (not set to 0) whenever
    its source could not be found or parsed at all.

    Returns None only when NOT A SINGLE figure could be derived from any of
    the three sources.
    """
    figures = {}

    try:
        figures.update(_gather_closure(root))
    except Exception:
        pass

    try:
        figures.update(_gather_claims(root))
    except Exception:
        pass

    try:
        figures.update(_gather_experiment_runs(root))
    except Exception:
        pass

    try:
        figures.update(_gather_claim_evidence(root))
    except Exception:
        pass

    return figures or None


if __name__ == "__main__":
    import sys

    root_arg = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "REE_assembly"
    )
    root_arg = os.path.abspath(root_arg)
    result = gather_evidence_figures(root_arg)
    print("root: %s" % root_arg)
    print(json.dumps(result, indent=2, sort_keys=True))
