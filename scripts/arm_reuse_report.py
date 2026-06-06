#!/usr/bin/env python3
"""
arm_reuse_report.py -- Phase 0 measurement for the arm-reuse fingerprint plan.

Design plan: evidence/planning/arm_reuse_fingerprint_plan.md

READ-ONLY. Scans evidence/experiments/*.json and reports how much experiment
compute is spent re-running baseline/control arms that another experiment has
(very likely) already computed. NOTHING here reuses, caches, edits, or skips
anything -- it only measures the opportunity so we can decide whether Phase 1 is
worth building.

Two analyses:

  [EXACT]  Group arm rows that carry an `arm_fingerprint` (emitted going forward
           by experiments/_lib/arm_fingerprint.py) by that fingerprint. A group
           of size N means (N-1) cells were provably the same random variable
           and (under a future phase) need not have been re-run. There are 0 of
           these today; this section grows as instrumented experiments land.

  [APPROX] For the historical corpus (no fingerprints, no substrate hash), build
           a best-effort cross-experiment key from the recorded config and arm
           flags and cluster baseline-like arm rows. This is a HEURISTIC upper
           bound on redundancy -- it deliberately CANNOT and MUST NOT drive any
           reuse decision (no substrate hash exists to prove the cells match).
           It exists only to size the opportunity.

ASCII-only output. Stdlib only.
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
from collections import defaultdict
from typing import Any, Dict, List, Optional, Tuple

_HERE = os.path.dirname(os.path.abspath(__file__))
_ASSEMBLY = os.path.dirname(_HERE)
_EXP_DIR = os.path.join(_ASSEMBLY, "evidence", "experiments")

_BASELINE_TOKENS = ("baseline", "control", "_off", "off_", "arm_a", "arm_0",
                    "replicat", "_a_", "off")


def _stable_hash(obj: Any) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"),
                   ensure_ascii=True, default=str).encode("utf-8")
    ).hexdigest()[:12]


def _is_baselineish(row: Dict[str, Any]) -> bool:
    """Heuristic: is this arm row a baseline/control/OFF condition?"""
    lab = str(row.get("label", "")).lower()
    aid = str(row.get("arm_id", "")).lower()
    if any(t in lab for t in _BASELINE_TOKENS):
        return True
    if any(t in aid for t in _BASELINE_TOKENS):
        return True
    # explicit "everything off" flags
    for k, v in row.items():
        if k.startswith("use_") and v is False:
            return True
    return False


def _extract_arm_rows(d: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Pull per-arm rows out of the heterogeneous manifest schemas."""
    rows: List[Dict[str, Any]] = []
    ar = d.get("arm_results")
    if isinstance(ar, list):
        rows.extend([r for r in ar if isinstance(r, dict)])
    return rows


def _config_signature(d: Dict[str, Any]) -> str:
    """Approximate cross-experiment config signature (env + schedule).

    Deliberately EXCLUDES the substrate version (none is recorded historically)
    -- which is exactly why this is APPROX and cannot drive reuse.
    """
    cfg = d.get("config") if isinstance(d.get("config"), dict) else {}
    keep: Dict[str, Any] = {}
    for k in ("env_kwargs", "p0_warmup_episodes", "p1_measurement_episodes",
              "steps_per_episode", "sd056_weight", "curiosity_bias_scale",
              "curiosity_weight"):
        if k in cfg:
            keep[k] = cfg[k]
    return _stable_hash(keep) if keep else ""


def _arm_flag_signature(row: Dict[str, Any]) -> str:
    """Signature of the arm's own configuration knobs."""
    flags = {k: v for k, v in row.items()
             if k.startswith("use_") or k.endswith("_gain")
             or k.endswith("_weight") or k.endswith("_scale")}
    return _stable_hash(flags)


def load_manifests(exp_dir: str) -> List[Tuple[str, Dict[str, Any]]]:
    out = []
    for f in sorted(glob.glob(os.path.join(exp_dir, "*.json"))):
        try:
            with open(f) as fh:
                d = json.load(fh)
        except Exception:
            continue
        if isinstance(d, dict):
            out.append((os.path.basename(f), d))
    return out


def report_exact(manifests) -> List[str]:
    groups: Dict[str, List[Tuple[str, str]]] = defaultdict(list)
    for fname, d in manifests:
        for row in _extract_arm_rows(d):
            fp = row.get("arm_fingerprint")
            if isinstance(fp, dict):
                fp = fp.get("arm_fingerprint")
            if isinstance(fp, str) and fp:
                eligible = True
                if isinstance(row.get("arm_fingerprint"), dict):
                    eligible = bool(row["arm_fingerprint"].get("reuse_eligible", True))
                groups[fp].append((d.get("experiment_type", fname),
                                   "eligible" if eligible else "INELIGIBLE"))
    lines = ["=" * 70, "[EXACT] fingerprint-grouped arm rows (forward-looking)", "=" * 70]
    if not groups:
        lines.append("  0 arm rows carry an arm_fingerprint yet.")
        lines.append("  (Section populates as instrumented experiments land.)")
        return lines
    dup = {k: v for k, v in groups.items() if len(v) > 1}
    lines.append("  fingerprints seen: %d   with >1 occurrence: %d" % (len(groups), len(dup)))
    redundant = sum(len(v) - 1 for v in dup.values())
    lines.append("  provably-redundant re-runs (N-1 per group): %d" % redundant)
    for fp, occ in sorted(dup.items(), key=lambda kv: -len(kv[1]))[:20]:
        elig = all(s == "eligible" for _, s in occ)
        lines.append("   %s x%d  %s  [%s]" % (
            fp[:16], len(occ), "REUSABLE" if elig else "blocked(ineligible)",
            ", ".join(sorted({e for e, _ in occ}))[:60]))
    return lines


def report_approx(manifests) -> List[str]:
    # key = (config_sig, arm_flag_sig, seed) across DISTINCT experiment_types
    clusters: Dict[Tuple[str, str, Any], List[Dict[str, Any]]] = defaultdict(list)
    for fname, d in manifests:
        csig = _config_signature(d)
        if not csig:
            continue
        etype = d.get("experiment_type", fname)
        elapsed = d.get("elapsed_seconds")
        for row in _extract_arm_rows(d):
            if not _is_baselineish(row):
                continue
            seed = row.get("seed")
            key = (csig, _arm_flag_signature(row), seed)
            clusters[key].append({
                "etype": etype, "fname": fname,
                "arm_id": row.get("arm_id"), "label": row.get("label"),
                "seed": seed, "elapsed": elapsed,
            })

    cross = {}
    for key, occ in clusters.items():
        etypes = {o["etype"] for o in occ}
        if len(etypes) > 1:  # baseline-ish cell shared across distinct experiments
            cross[key] = occ

    lines = ["", "=" * 70,
             "[APPROX] historical baseline-arm redundancy (HEURISTIC -- not a reuse signal)",
             "=" * 70]
    if not cross:
        lines.append("  No baseline-arm cells matched across distinct experiments")
        lines.append("  on (config-sig, arm-flags, seed). Either too few structured")
        lines.append("  manifests, or baselines genuinely differ. (config dicts: %d)"
                     % sum(1 for _, d in manifests if isinstance(d.get("config"), dict)))
        return lines
    redundant_cells = sum(len(v) - 1 for v in cross.values())
    lines.append("  cross-experiment baseline clusters: %d" % len(cross))
    lines.append("  approx redundant baseline re-runs (N-1 per cluster): %d" % redundant_cells)
    lines.append("  NOTE: upper bound -- no substrate hash exists historically, so")
    lines.append("        these are NOT confirmed-identical and drive NO reuse.")
    lines.append("")
    for key, occ in sorted(cross.items(), key=lambda kv: -len(kv[1]))[:25]:
        csig, fsig, seed = key
        etypes = sorted({o["etype"] for o in occ})
        lines.append("  cluster cfg=%s flags=%s seed=%s  x%d cells across %d exps:"
                     % (csig, fsig, seed, len(occ), len(etypes)))
        for et in etypes[:6]:
            lines.append("      - %s" % et)
        if len(etypes) > 6:
            lines.append("      - ... +%d more" % (len(etypes) - 6))
    return lines


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--exp-dir", default=_EXP_DIR,
                    help="evidence/experiments dir (default: repo-relative)")
    args = ap.parse_args()

    manifests = load_manifests(args.exp_dir)
    print("arm-reuse report (Phase 0, READ-ONLY)  --  %d manifests" % len(manifests))
    print("source: %s" % args.exp_dir)
    print()
    for ln in report_exact(manifests):
        print(ln)
    for ln in report_approx(manifests):
        print(ln)
    print()
    print("Reminder: Phase 0 is measurement only. No reuse is executed anywhere.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
