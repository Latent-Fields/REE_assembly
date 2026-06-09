#!/usr/bin/env python3
"""
check_claim_phase_consistency.py -- enforce the "phase label follows dependency"
principle on docs/claims/claims.yaml.

PRINCIPLE (project canon, see docs/architecture/claim_phase_provenance.md and
memory/feedback_phase_label_follows_dependency.md):

    implementation_phase (v3 / v4 / v5 ...) is a PREDICTION about when a claim
    is expected to be built -- it is NOT a permission gate. If a V3-scope claim
    genuinely DEPENDS ON a claim labelled v4+, that dependency reclassifies the
    DEPENDENCY to V3 by definition. Only the sequencing / readiness is open,
    never the scope-permission.

    Conversely a v4 claim whose only reverse-dependents are themselves v4, and
    which merely INSTANTIATES a v3 parent cluster, stays v4 (canonical example:
    SD-033e -- a frontopolar module whose reverse-dependents MECH-264 / MECH-265
    are both v4; it instantiates the v3 parent SD-033 but nothing v3 depends on
    it, so it stays v4. Its V3 obligation is graph-registration, a SEPARATE axis
    from implementation phase -- see commitment_closure_plan.md GAP-9).

This script walks the claim dependency graph transitively and reports, for every
v4+ claim that is reachable from a V3-scope BUILD COMMITMENT via a prerequisite
(depends_on / emergent_from) edge, that the claim is a RECLASSIFICATION CANDIDATE
(v3-necessary). It NEVER edits claims.yaml -- it reports candidates for human
governance review only.

Edge semantics (what propagates "phase pressure" from a needer to a need):
  * depends_on        : YES -- a prerequisite edge. EXCEPT an edge to the claim's
                        `instantiates` target, which is a parent-cluster
                        registration relation, not a build prerequisite, and is
                        skipped (this is what keeps SD-033e from being over-pulled
                        and what keeps a v3 child that instantiates a v3 parent
                        from spuriously "needing" the parent built first).
  * emergent_from     : YES, and STRONGER -- the invariant's subject is
                        ill-formed without the substrate (subset of depends_on;
                        elevates the candidate's strength to `strong`).
  * instantiates      : NO -- never a phase-pulling edge, in either direction.

Driver gating (which claims may DRIVE a reclassification):
  A claim is a V3-scope driver only if it is a build commitment expected in V3:
    effective_phase == 3  (implementation_phase v3, OR v3_pending true with no
                           later explicit phase)
    AND claim_type is not open_question
    AND polarity not in {asks, open, open_question}
    AND status not in {resolved, superseded, deprecated, retracted, withdrawn}.
  Open questions and pure answer-state claims do NOT force their prerequisites to
  be built -- being "V3" for a question means "we want to answer it in V3", which
  a deferred-substrate answer satisfies. They are reported separately as
  informational (low confidence), never as reclassification candidates.

Outcomes per v4+ claim reachable from a V3 driver:
  RECLASSIFY  -- not phase_locked: propose implementation_phase: v3,
                 phase_provenance: derived, phase_derived_from: <driver(s)>.
  CONFLICT    -- phase_locked: true but a V3 build commitment needs it. The lock
                 and the dependency contradict; a human must either sever/replace
                 the dependency or clear the lock. Not auto-reclassifiable.

ASCII-only output (Windows cp1252 safety; see REE_Working/CLAUDE.md).

Usage (from REE_assembly root):
    python scripts/check_claim_phase_consistency.py            # human report, exit 0
    python scripts/check_claim_phase_consistency.py --json     # machine report, exit 0
    python scripts/check_claim_phase_consistency.py --warn     # governance.sh WARN lines, exit 0
    python scripts/check_claim_phase_consistency.py --strict   # exit 1 if any RECLASSIFY/CONFLICT

Importable API (for generate_inter_governance_workset.py / governance.sh):
    from check_claim_phase_consistency import reclassification_candidates
    report = reclassification_candidates(load_claims())
    leak_ids = set(report["candidates"])     # {claim_id: {...}}
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CLAIMS_YAML = REPO_ROOT / "docs" / "claims" / "claims.yaml"

# Statuses that take a claim out of the live graph (neither a driver nor a need).
DEAD_STATUSES = {"resolved", "superseded", "deprecated", "retracted", "withdrawn"}

# Polarities / claim_types that are NOT build commitments -- they pose a question
# rather than commit to building a substrate, so they do not drive reclassification.
NON_COMMITMENT_POLARITIES = {"asks", "open", "open_question"}
NON_COMMITMENT_CLAIM_TYPES = {"open_question"}

_PHASE_RE = re.compile(r"^v?(\d+)")


def load_claims(path: Path = CLAIMS_YAML) -> list[dict]:
    if not path.exists():
        print(f"ERROR: {path} not found", file=sys.stderr)
        sys.exit(2)
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, list):
        print("ERROR: claims.yaml top level must be a list", file=sys.stderr)
        sys.exit(2)
    return [c for c in data if isinstance(c, dict) and c.get("id")]


def phase_num(claim: dict) -> int | None:
    """Numeric implementation phase from a free-text-tolerant field, or None.

    Tolerates the registry's messy values: 'v3', 'v4', 'v4)', 'v4).', 'v5',
    and long free-text records that begin with the phase token
    (e.g. 'v3 retained as a factual record ...').
    """
    raw = str(claim.get("implementation_phase") or "").strip().lower()
    m = _PHASE_RE.match(raw)
    return int(m.group(1)) if m else None


def effective_phase(claim: dict) -> int | None:
    """The phase a claim is committed to: explicit implementation_phase wins;
    else v3_pending:true implies V3; else unphased (None)."""
    pn = phase_num(claim)
    if pn is not None:
        return pn
    if claim.get("v3_pending") is True:
        return 3
    return None


def _as_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(v) for v in value]
    return []


def is_v3_driver(claim: dict) -> bool:
    """True if the claim is a V3-scope build commitment that may force its
    prerequisites to V3. See module docstring 'Driver gating'."""
    if claim.get("status") in DEAD_STATUSES:
        return False
    if effective_phase(claim) != 3:
        return False
    if (claim.get("claim_type") or "").strip().lower() in NON_COMMITMENT_CLAIM_TYPES:
        return False
    if (claim.get("polarity") or "").strip().lower() in NON_COMMITMENT_POLARITIES:
        return False
    return True


def is_phase_locked(claim: dict) -> bool:
    return bool(claim.get("phase_locked"))


def prerequisite_edges(claim: dict) -> list[tuple[str, str]]:
    """Return [(dep_id, edge_kind)] of phase-pulling prerequisite edges from a
    claim to its needs.

    edge_kind in {'emergent_from', 'depends_on'}. The `instantiates` target is
    removed from depends_on (registration, not a build prerequisite). emergent_from
    edges are reported with their own kind so the caller can mark them STRONG;
    they are a subset of depends_on so we de-duplicate.
    """
    instantiates = set(_as_list(claim.get("instantiates")))
    emergent_from = [d for d in _as_list(claim.get("emergent_from")) if d not in instantiates]
    depends_on = [d for d in _as_list(claim.get("depends_on")) if d not in instantiates]
    seen: set[str] = set()
    edges: list[tuple[str, str]] = []
    for dep in emergent_from:
        if dep not in seen:
            seen.add(dep)
            edges.append((dep, "emergent_from"))
    for dep in depends_on:
        if dep not in seen:
            seen.add(dep)
            edges.append((dep, "depends_on"))
    return edges


def reclassification_candidates(claims: list[dict]) -> dict:
    """Core analysis. Returns a structured report dict:

    {
      "candidates": {
         "<claim_id>": {
            "current_phase": 4,
            "verdict": "RECLASSIFY" | "CONFLICT",
            "kind": "root" | "cascade",
            "strength": "strong" | "standard",
            "direct_drivers": ["<v3 claim id>", ...],   # v3 build commitments with a
                                                         # DIRECT prerequisite edge (root cause)
            "follows_from": ["<root v4 id>", ...],       # cascade only: the root candidate(s)
                                                         # whose reclassification pulls this one
            "example_path": ["<driver>", "...", "<candidate>"],
            "via_emergent_from": bool,
         }, ...
      },
      "informational": { ... v4+ under a V3 open-question/answer-state seed; not a leak ... },
      "dangling_deps": [ "<missing dep id> (referenced by <claim id>)", ... ],
      "stats": { ... },
    }

    Two-phase model (keeps root cause separate from its consequences):

      ROOT     -- a V3-scope BUILD COMMITMENT depends DIRECTLY (one prerequisite
                  edge) on a v4+ claim. This is the actual phase leak. Its
                  `direct_drivers` are the v3 claims responsible, and is what a
                  human acts on first.
      CASCADE  -- a v4+ claim that is NOT directly needed by any v3 build
                  commitment, but becomes v3-necessary once a ROOT is reclassified
                  to v3 (it is a prerequisite of a root, reached through other v4
                  nodes we intend to reclassify). `follows_from` names the root(s).
                  Cascade closure stops at phase_locked nodes (a contested node
                  must not silently cascade).

    A phase_locked v4+ ROOT is reported as CONFLICT, not RECLASSIFY: the lock and
    the V3 dependency contradict and a human must resolve them.
    """
    by_id = {c["id"]: c for c in claims}

    # Detect dangling dependency references (claims.yaml hygiene, informational).
    dangling: list[str] = []
    for c in claims:
        for dep, _kind in prerequisite_edges(c):
            if dep not in by_id:
                dangling.append(f"{dep} (referenced by {c['id']})")

    def _live_later(dep: str) -> dict | None:
        """Return the dep claim if it is live and phase v4+, else None."""
        d = by_id.get(dep)
        if d is None or d.get("status") in DEAD_STATUSES:
            return None
        dp = phase_num(d)
        return d if (dp is not None and dp >= 4) else None

    # --- Phase 1: ROOT leaks -- direct v3-build-commitment -> v4+ edges. ---
    seeds = {True: [], False: []}  # is_build -> seeds
    for c in claims:
        if c.get("status") in DEAD_STATUSES:
            continue
        if effective_phase(c) != 3:
            continue
        # open-question / answer-state V3 seeds drive only the informational pass
        seeds[is_v3_driver(c)].append(c)

    def direct_roots(seed_list: list[dict]) -> dict[str, dict]:
        roots: dict[str, dict] = {}
        for seed in seed_list:
            for dep, kind in prerequisite_edges(seed):
                dep_claim = _live_later(dep)
                if dep_claim is None:
                    continue
                emergent = kind == "emergent_from"
                rec = roots.get(dep)
                if rec is None:
                    roots[dep] = {
                        "current_phase": phase_num(dep_claim),
                        "verdict": "CONFLICT" if is_phase_locked(dep_claim) else "RECLASSIFY",
                        "kind": "root",
                        "strength": "strong" if emergent else "standard",
                        "direct_drivers": {seed["id"]},
                        "follows_from": set(),
                        "example_path": [seed["id"], dep],
                        "via_emergent_from": emergent,
                    }
                else:
                    rec["direct_drivers"].add(seed["id"])
                    if emergent:
                        rec["strength"] = "strong"
                        rec["via_emergent_from"] = True
        return roots

    roots = direct_roots(seeds[True])

    # --- Phase 2: CASCADE closure -- prerequisites pulled along by reclassified
    # roots. Walk prerequisite edges from each (unlocked) root through v4 nodes;
    # any further v4+ claim reached that is not itself a root is a cascade
    # candidate. Stop traversing at phase_locked nodes. ---
    cascade: dict[str, dict] = {}
    for root_id, root_rec in roots.items():
        if root_rec["verdict"] == "CONFLICT":
            continue  # locked root does not cascade
        queue: list[tuple[str, list[str], bool]] = [
            (root_id, [root_id], root_rec["via_emergent_from"])
        ]
        visited: set[str] = {root_id}
        while queue:
            node_id, path, had_emergent = queue.pop(0)
            node = by_id.get(node_id)
            if node is None:
                continue
            for dep, kind in prerequisite_edges(node):
                if dep in visited:
                    continue
                dep_claim = by_id.get(dep)
                if dep_claim is None or dep_claim.get("status") in DEAD_STATUSES:
                    continue
                visited.add(dep)
                new_path = path + [dep]
                edge_emergent = had_emergent or kind == "emergent_from"
                later = _live_later(dep)
                if later is None:
                    # v3/unphased intermediate -- keep walking for deeper v4 deps.
                    queue.append((dep, new_path, edge_emergent))
                    continue
                if dep in roots:
                    # another root: it has its own direct attribution; traverse
                    # through it (if unlocked) but do not record as cascade.
                    if not is_phase_locked(dep_claim):
                        queue.append((dep, new_path, edge_emergent))
                    continue
                rec = cascade.get(dep)
                if rec is None:
                    cascade[dep] = {
                        "current_phase": phase_num(later),
                        "verdict": "CONFLICT" if is_phase_locked(later) else "RECLASSIFY",
                        "kind": "cascade",
                        "strength": "strong" if edge_emergent else "standard",
                        "direct_drivers": set(),
                        "follows_from": {root_id},
                        "example_path": new_path,
                        "via_emergent_from": edge_emergent,
                    }
                else:
                    rec["follows_from"].add(root_id)
                    if len(new_path) < len(rec["example_path"]):
                        rec["example_path"] = new_path
                    if edge_emergent:
                        rec["strength"] = "strong"
                        rec["via_emergent_from"] = True
                if not is_phase_locked(later):
                    queue.append((dep, new_path, edge_emergent))

    candidates = dict(roots)
    candidates.update(cascade)

    # --- Informational pass: v4+ DIRECTLY needed by a V3 open-question seed. ---
    informational: dict[str, dict] = {}
    for rid, rrec in direct_roots(seeds[False]).items():
        if rid in candidates:
            continue
        informational[rid] = rrec

    def _finalize(d: dict[str, dict]) -> dict[str, dict]:
        out: dict[str, dict] = {}
        for cid, rec in sorted(d.items()):
            rec = dict(rec)
            rec["direct_drivers"] = sorted(rec["direct_drivers"])
            rec["follows_from"] = sorted(rec["follows_from"])
            out[cid] = rec
        return out

    candidates = _finalize(candidates)
    informational = _finalize(informational)

    n_reclassify = sum(1 for r in candidates.values() if r["verdict"] == "RECLASSIFY")
    n_conflict = sum(1 for r in candidates.values() if r["verdict"] == "CONFLICT")
    n_root = sum(1 for r in candidates.values() if r["kind"] == "root")
    stats = {
        "total_claims": len(claims),
        "v3_build_drivers": len(seeds[True]),
        "root_leaks": n_root,
        "cascade_candidates": len(candidates) - n_root,
        "reclassify_candidates": n_reclassify,
        "conflict_candidates": n_conflict,
        "informational_candidates": len(informational),
        "dangling_dep_refs": len(dangling),
    }
    return {
        "candidates": candidates,
        "informational": informational,
        "dangling_deps": sorted(set(dangling)),
        "stats": stats,
    }


def _fmt_path(path: list[str]) -> str:
    return " -> ".join(path)


def _fmt_capped(ids: list[str], cap: int = 8) -> str:
    if len(ids) <= cap:
        return ", ".join(ids)
    return ", ".join(ids[:cap]) + f", ... (+{len(ids) - cap} more)"


def render_human(report: dict) -> str:
    s = report["stats"]
    lines = [
        "=== Claim phase-consistency check ===",
        "",
        f"Claims scanned:            {s['total_claims']}",
        f"V3 build-commitment seeds: {s['v3_build_drivers']:>4}",
        f"ROOT leaks:                {s['root_leaks']:>4}  (v3 build commitment depends DIRECTLY on a v4+ claim)",
        f"CASCADE candidates:        {s['cascade_candidates']:>4}  (v4+ pulled along once a root is reclassified)",
        f"Total RECLASSIFY:          {s['reclassify_candidates']:>4}  (root + cascade, not phase_locked)",
        f"Total CONFLICT:            {s['conflict_candidates']:>4}  (phase_locked v4+ needed by V3 -- human must resolve)",
        f"Informational (questions): {s['informational_candidates']:>4}  (v4+ under a V3 open-question seed; not a leak)",
        f"Dangling dep references:   {s['dangling_dep_refs']:>4}",
        "",
    ]
    roots = {k: v for k, v in report["candidates"].items() if v["kind"] == "root"}
    cascades = {k: v for k, v in report["candidates"].items() if v["kind"] == "cascade"}
    if not report["candidates"]:
        lines.append("No phase leaks: every V3 build commitment's prerequisites are V3-scope.")
        return "\n".join(lines)

    lines.append("--- ROOT leaks (act on these first) ---")
    lines.append("")
    for cid, rec in roots.items():
        strong = " [STRONG: emergent_from]" if rec["via_emergent_from"] else ""
        dd = rec["direct_drivers"]
        lines.append(f"* {cid}  (currently v{rec['current_phase']})  -> {rec['verdict']}{strong}")
        lines.append(
            f"    directly needed by {len(dd)} V3 build commitment(s): {_fmt_capped(dd)}"
        )
        lines.append(f"    example edge: {_fmt_path(rec['example_path'])}")
        if rec["verdict"] == "RECLASSIFY":
            lines.append(
                "    proposed: implementation_phase: v3 | phase_provenance: derived "
                f"| phase_derived_from: {dd[0]}"
            )
        else:
            lines.append(
                "    ACTION: phase_locked=true contradicts a V3 dependency -- sever/replace "
                "the dependency or clear the lock (do NOT auto-reclassify)."
            )
        lines.append("")

    if cascades:
        lines.append("--- CASCADE candidates (become V3-necessary once the roots above are reclassified) ---")
        lines.append("")
        for cid, rec in cascades.items():
            strong = " [STRONG: emergent_from]" if rec["via_emergent_from"] else ""
            lines.append(
                f"* {cid}  (currently v{rec['current_phase']})  -> {rec['verdict']}{strong}"
            )
            lines.append(f"    follows from root(s): {_fmt_capped(rec['follows_from'])}")
            lines.append(f"    example path: {_fmt_path(rec['example_path'])}")
            lines.append("")

    if report["informational"]:
        lines.append("--- Informational: v4+ directly under a V3 open-question seed (not a leak) ---")
        for cid, rec in report["informational"].items():
            lines.append(
                f"  {cid} (v{rec['current_phase']}) under question(s) "
                f"{_fmt_capped(rec['direct_drivers'])}: {_fmt_path(rec['example_path'])}"
            )
        lines.append("")
    if report["dangling_deps"]:
        lines.append("--- Dangling dependency references (claims.yaml hygiene) ---")
        for d in report["dangling_deps"]:
            lines.append(f"  {d}")
        lines.append("")
    return "\n".join(lines)


def render_warn(report: dict) -> str:
    """One WARN line per ROOT leak, suitable for governance.sh log scraping.

    Only roots are emitted -- cascades are consequences of roots and would be
    noise in a governance log; the human report shows them in full.
    """
    out = []
    for cid, rec in report["candidates"].items():
        if rec["kind"] != "root":
            continue
        out.append(
            f"WARN: phase-leak {rec['verdict']} {cid} (v{rec['current_phase']}) "
            f"directly needed by V3 build commitment {rec['direct_drivers'][0]} "
            f"(+{len(rec['direct_drivers']) - 1} more)"
            if len(rec["direct_drivers"]) > 1
            else f"WARN: phase-leak {rec['verdict']} {cid} (v{rec['current_phase']}) "
            f"directly needed by V3 build commitment {rec['direct_drivers'][0]}"
        )
    if not out:
        out.append("OK: no claim phase leaks (v3->v4+ direct prerequisite) detected.")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true", help="emit JSON report to stdout")
    ap.add_argument("--warn", action="store_true", help="emit governance.sh WARN lines, exit 0")
    ap.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 if any RECLASSIFY or CONFLICT candidate is found",
    )
    ap.add_argument("--claims", default=str(CLAIMS_YAML), help="path to claims.yaml")
    args = ap.parse_args()

    claims = load_claims(Path(args.claims))
    report = reclassification_candidates(claims)

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    elif args.warn:
        print(render_warn(report))
    else:
        print(render_human(report))

    if args.strict and (report["candidates"]):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
