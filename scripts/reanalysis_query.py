#!/usr/bin/env python3
"""
reanalysis_query.py -- the tooling half of GOV-REUSE-1 (reanalysis-first rule).

Governance rule: docs/claims/claims.yaml GOV-REUSE-1.
Standard:        evidence/planning/experimental_recording_standard_2026-07-12.md (3c/5).
Authoring gate:  /queue-experiment Step 2.4 (existing-evidence / reanalysis-first check).

WHAT THIS IS FOR
----------------
Before a new experiment is queued, GOV-REUSE-1 asks: is the decisive readout the
experiment would produce ALREADY recorded -- or derivable post-hoc -- in existing
manifests on a COMPATIBLE substrate? This script is the mechanical helper for that
check. It does two things:

  query   Scan evidence/experiments/*.json and report which manifests carry a named
          readout (a metric key, matched as a substring of any key path in the
          manifest), grouped by substrate_hash, with a compatibility verdict against
          a substrate_hash you are asking about. READ-ONLY.

  emit    Write a RECORDED post-hoc reanalysis artifact (schema reanalysis/v1) that
          cites the source run_ids and records the computed answer, its decisive
          readout, and the substrate-compatibility basis -- so a reanalysis is a
          durable, auditable evidence object rather than a throwaway note. Writes ONE
          json file under evidence/reanalysis/ (creating the dir if needed).

SUBSTRATE COMPATIBILITY IS THE KEY. A readout only answers the question if it came
from a compatible substrate. This script reads substrate_hash from the top level
(post-stamper, manifest_core.stamp_recording_core) OR hoists it from
arm_results[i].arm_fingerprint.substrate_hash (the pre-stamper arm-fingerprint
machinery). A manifest with NO recoverable substrate_hash is reported as
UNVERIFIABLE -- you cannot confirm which substrate it ran against, so per GOV-REUSE-1
you treat it as "not recoverable" (run, or re-record), never as a silent match. Most
pre-2026-07-12 flat manifests fall here (0% carried a substrate_hash).

This script does NOT decide anything, run any experiment, or feed confidence scoring
(the reanalysis artifact is recorded but wiring it into build_experiment_indexes.py
confidence math is a deliberate deferred follow-up -- same posture as the recording
standard's deferred-hardening items). It surfaces the opportunity and records the
result; the human + /governance weigh it.

ASCII-only output. Stdlib only.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import warnings
from collections import defaultdict
from datetime import datetime
from typing import Any, Dict, List, Optional, Set, Tuple

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)  # REE_assembly/
EXPERIMENTS_DIR = os.path.join(REPO, "evidence", "experiments")
REANALYSIS_DIR = os.path.join(REPO, "evidence", "reanalysis")

RECORDING_SCHEMA = "rec/v1"
REANALYSIS_SCHEMA = "reanalysis/v1"


# ----------------------------------------------------------------------------
# manifest reading
# ----------------------------------------------------------------------------
def _load(path: str) -> Optional[Dict[str, Any]]:
    try:
        with open(path) as fh:
            d = json.load(fh)
        return d if isinstance(d, dict) else None
    except Exception:
        return None


def extract_substrate_hash(manifest: Dict[str, Any]) -> Tuple[Optional[str], Optional[str]]:
    """Return (substrate_hash, source) where source is 'top_level' (post-stamper) or
    'hoisted_arm_fingerprint' (pre-stamper machinery), or (None, None) if none is
    recoverable. All arms of one run share a substrate, so the first present arm
    hash is authoritative."""
    sh = manifest.get("substrate_hash")
    if isinstance(sh, str) and sh:
        return sh, "top_level"
    arms = manifest.get("arm_results")
    if isinstance(arms, list):
        for cell in arms:
            if isinstance(cell, dict):
                fp = cell.get("arm_fingerprint")
                if isinstance(fp, dict):
                    s = fp.get("substrate_hash")
                    if isinstance(s, str) and s:
                        return s, "hoisted_arm_fingerprint"
    return None, None


def collect_key_names(obj: Any, out: Set[str], depth: int = 0, maxdepth: int = 7) -> None:
    """Collect every dict-key NAME appearing anywhere in the manifest (recursing into
    dicts fully; for lists, sampling the first element only -- per-seed / per-arm rows
    share their keys). Used for substring readout matching."""
    if depth > maxdepth:
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            out.add(str(k))
            collect_key_names(v, out, depth + 1, maxdepth)
    elif isinstance(obj, list) and obj:
        collect_key_names(obj[0], out, depth + 1, maxdepth)


def manifest_summary(path: str) -> Optional[Dict[str, Any]]:
    m = _load(path)
    if m is None:
        return None
    sh, sh_src = extract_substrate_hash(m)
    keys: Set[str] = set()
    collect_key_names(m, keys)
    return {
        "path": path,
        "file": os.path.basename(path),
        "run_id": m.get("run_id") or m.get("experiment_type") or os.path.basename(path),
        "claim_ids": m.get("claim_ids") or [],
        "experiment_purpose": m.get("experiment_purpose"),
        "outcome": m.get("outcome") or m.get("status"),
        "machine_class": m.get("machine_class"),
        "substrate_hash": sh,
        "substrate_hash_source": sh_src,
        "key_names": keys,
    }


def scan_manifests() -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for p in sorted(glob.glob(os.path.join(EXPERIMENTS_DIR, "*.json"))):
        # skip the derived index / aggregate files, not per-run manifests
        base = os.path.basename(p)
        if base in ("claim_evidence.v1.json", "arm_fingerprint_index.json"):
            continue
        s = manifest_summary(p)
        if s is not None:
            out.append(s)
    return out


def _readout_hits(summary: Dict[str, Any], readout: str) -> List[str]:
    rl = readout.lower()
    return sorted(k for k in summary["key_names"] if rl in k.lower())


def _compat(summary: Dict[str, Any], target_hash: Optional[str]) -> str:
    """Compatibility verdict of a candidate manifest against a target substrate_hash."""
    sh = summary["substrate_hash"]
    if sh is None:
        return "UNVERIFIABLE"          # no recoverable substrate_hash -> treat as not-recoverable
    if target_hash is None:
        return "HAS_HASH"              # no target asked; just note it carries one
    if sh == target_hash:
        return "MATCH"
    if target_hash and sh.startswith(target_hash):
        return "MATCH"                 # allow a short target prefix
    return "INCOMPATIBLE"


# ----------------------------------------------------------------------------
# query
# ----------------------------------------------------------------------------
def cmd_query(args: argparse.Namespace) -> int:
    rows = scan_manifests()
    readout = args.readout

    # filters
    def keep(s: Dict[str, Any]) -> bool:
        if args.claim and args.claim not in (s["claim_ids"] or []):
            return False
        if args.purpose and s["experiment_purpose"] != args.purpose:
            return False
        return True

    rows = [s for s in rows if keep(s)]

    # annotate
    annotated = []
    for s in rows:
        hits = _readout_hits(s, readout) if readout else []
        if args.require_readout and not hits:
            continue
        annotated.append((s, hits, _compat(s, args.substrate_hash)))

    # group by substrate_hash (None -> "<no-substrate_hash>")
    groups: Dict[str, List[Tuple[Dict[str, Any], List[str], str]]] = defaultdict(list)
    for s, hits, compat in annotated:
        groups[s["substrate_hash"] or "<no-substrate_hash>"].append((s, hits, compat))

    if args.json:
        payload = {
            "readout": readout,
            "target_substrate_hash": args.substrate_hash,
            "n_manifests_scanned": len(rows),
            "n_matched": len(annotated),
            "groups": {
                gh: [
                    {
                        "run_id": s["run_id"],
                        "file": s["file"],
                        "claim_ids": s["claim_ids"],
                        "outcome": s["outcome"],
                        "experiment_purpose": s["experiment_purpose"],
                        "machine_class": s["machine_class"],
                        "substrate_hash": s["substrate_hash"],
                        "substrate_hash_source": s["substrate_hash_source"],
                        "readout_key_hits": hits,
                        "compatibility": compat,
                    }
                    for (s, hits, compat) in members
                ]
                for gh, members in groups.items()
            },
        }
        print(json.dumps(payload, indent=2))
        return 0

    print("[reanalysis_query] scanned %d manifests under evidence/experiments/"
          % len(rows))
    if readout:
        print("[reanalysis_query] readout substring: %r" % readout)
    if args.substrate_hash:
        print("[reanalysis_query] target substrate_hash: %s" % args.substrate_hash)
    print("[reanalysis_query] %d manifest(s) matched the filters%s"
          % (len(annotated), " + carry the readout" if args.require_readout else ""))
    print("")

    # print groups: substrate-carrying groups first, no-hash group last
    def group_sort_key(item: Tuple[str, List[Any]]) -> Tuple[int, str]:
        gh = item[0]
        return (1 if gh == "<no-substrate_hash>" else 0, gh)

    for gh, members in sorted(groups.items(), key=group_sort_key):
        carrying = sum(1 for (_s, hits, _c) in members if hits)
        label = gh if gh == "<no-substrate_hash>" else gh[:16] + "..."
        print("=== substrate_hash %s  (%d manifest(s), %d carry readout) ==="
              % (label, len(members), carrying))
        for (s, hits, compat) in sorted(members, key=lambda t: t[0]["run_id"]):
            flag = "READOUT" if hits else "       "
            print("  [%s][%-13s] %s" % (flag, compat, s["run_id"]))
            print("             claims=%s outcome=%s purpose=%s class=%s src=%s"
                  % (",".join(s["claim_ids"]) or "-", s["outcome"],
                     s["experiment_purpose"], s["machine_class"],
                     s["substrate_hash_source"]))
            if hits:
                shown = hits[:8]
                more = "" if len(hits) <= 8 else "  (+%d more)" % (len(hits) - 8)
                print("             readout keys: %s%s" % (", ".join(shown), more))
        print("")

    print("REMINDER (GOV-REUSE-1): a readout answers your question ONLY on a MATCH"
          " (compatible substrate_hash). UNVERIFIABLE = no recoverable substrate_hash"
          " -> treat as not-recoverable (run, or re-record). Then `emit` a reanalysis"
          " artifact if the recorded data settles it.")
    return 0


# ----------------------------------------------------------------------------
# emit
# ----------------------------------------------------------------------------
def _slug(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower()).strip("_")
    return s[:48] or "reanalysis"


def _find_manifest_by_run_id(run_id: str, rows: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    for s in rows:
        if s["run_id"] == run_id or s["file"].startswith(run_id):
            return s
    return None


def cmd_emit(args: argparse.Namespace) -> int:
    rows = scan_manifests()
    source_ids = [r.strip() for r in args.sources.split(",") if r.strip()]
    if not source_ids:
        print("ERROR: --sources must list at least one source run_id")
        return 2

    src_hashes: Dict[str, Optional[str]] = {}
    src_missing: List[str] = []
    for rid in source_ids:
        s = _find_manifest_by_run_id(rid, rows)
        if s is None:
            print("ERROR: source run_id not found under evidence/experiments/: %s" % rid)
            return 2
        src_hashes[rid] = s["substrate_hash"]
        if s["substrate_hash"] is None:
            src_missing.append(rid)

    # substrate compatibility basis
    present = [h for h in src_hashes.values() if h]
    if args.substrate_invariant:
        compat = "invariant_asserted"
    elif src_missing:
        compat = "unverifiable"
    elif len(set(present)) == 1:
        compat = "matched"
    else:
        compat = "mixed"

    if compat in ("unverifiable", "mixed") and not args.force:
        print("REFUSING to emit: substrate compatibility is %r." % compat)
        if src_missing:
            print("  sources with NO recoverable substrate_hash: %s"
                  % ", ".join(src_missing))
        if compat == "mixed":
            print("  sources span differing substrate_hashes: %s"
                  % json.dumps(src_hashes, indent=2))
        print("  Per GOV-REUSE-1 an unverifiable/mixed-substrate reanalysis does not"
              " safely answer the question. Pass --substrate-invariant if the readout"
              " is provably substrate-independent, or --force to record anyway with the"
              " caveat stamped.")
        return 3

    # answer payload: raw string, or parse as JSON if it looks like JSON
    answer: Any = args.answer
    try:
        answer = json.loads(args.answer)
    except Exception:
        pass

    # utcnow() per the repo timestamp convention; wrap to keep CLI output clean of the
    # py3.12 deprecation warning without changing the sanctioned call.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    rid = "reanalysis_%s_%s" % (_slug(args.slug or args.question), stamp)

    artifact = {
        "schema_version": REANALYSIS_SCHEMA,
        "recording_schema": RECORDING_SCHEMA,
        "artifact_type": "post_hoc_reanalysis",
        "reanalysis_id": rid,
        "generated_utc": now,
        "gov_rule": "GOV-REUSE-1",
        "question": args.question,
        "claim_ids": [c.strip() for c in (args.claims or "").split(",") if c.strip()],
        "decisive_readout": args.readout,
        "source_run_ids": source_ids,
        "source_substrate_hashes": src_hashes,
        "substrate_compatibility": compat,
        "substrate_invariant_asserted": bool(args.substrate_invariant),
        "answer": answer,
        "method_note": args.method or "",
        "verdict": args.verdict,
        "notes": args.notes or "",
        "caveat": ("substrate compatibility %s -- recorded under --force; interpret with care"
                   % compat) if (args.force and compat in ("unverifiable", "mixed")) else "",
    }

    os.makedirs(REANALYSIS_DIR, exist_ok=True)
    out_path = os.path.join(REANALYSIS_DIR, rid + ".json")
    if os.path.exists(out_path) and not args.force:
        print("ERROR: %s already exists (pass --force to overwrite)" % out_path)
        return 2
    with open(out_path, "w") as fh:
        json.dump(artifact, fh, indent=2)
    print("[reanalysis_query] wrote %s" % out_path)
    print("  compatibility=%s  sources=%s  readout=%s"
          % (compat, ",".join(source_ids), args.readout))
    print("  cite this reanalysis_id in the /queue-experiment note (instead of queuing"
          " a run), and surface it at the next /governance walk.")
    return 0


# ----------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="GOV-REUSE-1 reanalysis-first helper: query recorded manifests by "
                    "readout + substrate_hash, and emit a recorded reanalysis artifact.")
    sub = p.add_subparsers(dest="cmd", required=True)

    q = sub.add_parser("query", help="find manifests carrying a readout, grouped by substrate_hash")
    q.add_argument("--readout", default=None,
                   help="readout metric name (substring-matched against any key path in the manifest)")
    q.add_argument("--substrate-hash", default=None,
                   help="target substrate_hash (full or prefix) to check compatibility against")
    q.add_argument("--claim", default=None, help="only manifests tagging this claim_id")
    q.add_argument("--purpose", default=None,
                   help="only manifests with this experiment_purpose (evidence/diagnostic/baseline)")
    q.add_argument("--require-readout", action="store_true",
                   help="only show manifests that actually carry the readout")
    q.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    q.set_defaults(func=cmd_query)

    e = sub.add_parser("emit", help="write a recorded post-hoc reanalysis artifact")
    e.add_argument("--question", required=True, help="the scientific question being answered")
    e.add_argument("--readout", required=True, help="the decisive readout the answer rests on")
    e.add_argument("--sources", required=True,
                   help="comma-separated source run_ids the answer is derived from")
    e.add_argument("--answer", required=True,
                   help="the computed answer (a string, or inline JSON, recorded verbatim)")
    e.add_argument("--claims", default=None, help="comma-separated claim_ids this bears on")
    e.add_argument("--verdict", default=None,
                   help="optional verdict tag (e.g. supports/weakens/mixed/inconclusive)")
    e.add_argument("--method", default=None, help="how the answer was derived from the sources")
    e.add_argument("--notes", default=None, help="free-text notes")
    e.add_argument("--slug", default=None, help="short slug for the filename (default: from question)")
    e.add_argument("--substrate-invariant", action="store_true",
                   help="assert the readout is substrate-independent (allows unverifiable/mixed sources)")
    e.add_argument("--force", action="store_true",
                   help="record even when substrate compatibility is unverifiable/mixed (stamps a caveat)")
    e.set_defaults(func=cmd_emit)
    return p


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
