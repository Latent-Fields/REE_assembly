#!/usr/bin/env python3
"""check_closure_links.py -- flag truly-dangling closure-map links.

The V3 closure map (closure.html, served via /api/closure -> serve.read_closure())
aggregates closure_plan frontmatter across evidence/planning/*_plan.md into
nodes/edges/cross_links. Each node carries `depends_on` and `cross_plan_link`
target lists. A target is VALID when it is either:

  * a node id   -- the fully-qualified "<plan_id>:<NODE>" form keyed in read_closure's
                   nodes_by_id (e.g. "object_representation_v4:OBJ-1"), OR
  * a plan id   -- a bare "<plan_id>" string naming a whole plan, which is an
                   intentional whole-plan reference (e.g. cross_plan_link: ["self_model_v4"]).

A target that is NEITHER is DANGLING: read_closure() still records the edge, but
because no node/plan with that id exists the link silently fails to render in
closure.html. On 2026-06-20 two such typos went undetected until a manual audit:
  - object_representation:OBJ-1   (missing the "_v4" -> plan is "object_representation_v4")
  - mirror_modelling              (vs the real plan id "mirror_modelling_other_self_v5")
Both dropped edges with no error. This script makes that failure mode loud at
build time.

It reuses serve.py's CLOSURE_KNOWN_PLANS + _parse_plan_frontmatter so it reads
EXACTLY what read_closure() reads (same plan set, same parser, all generations).

Exit code:
  0 -- no truly-dangling refs (the one exempt back-pointer below is allowed)
  1 -- one or more dangling refs (each printed as
         "<source_node> --<field>--> <target> (DANGLING)")
  2 -- could not load serve.py / parse plans (environment problem)

Wired into scripts/governance.sh as a warn-only step so future typos surface
without blocking the pipeline; can be run standalone as a strict gate.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Repo root on the path so `import serve` resolves (stdlib-only, side-effect-free:
# the server only binds under serve.py's `if __name__ == "__main__"`). Same pattern
# as scripts/generate_closure_snapshot.py.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
try:
    from serve import (
        CLOSURE_KNOWN_PLANS,
        PLANNING_DIR,
        _parse_plan_frontmatter,
    )
except Exception as exc:  # pragma: no cover - environment problem, not a data problem
    print(f"ERROR: could not import closure helpers from serve.py: {exc}", file=sys.stderr)
    sys.exit(2)


# Deliberate back-pointer retained per sleep_substrate_plan.md (2026-05-30
# decision-log): sleep_substrate:GAP-2 depends_on the arc_062 rule-apprehension
# substrate readiness, addressed as "arc_062_rule_apprehension:ARC-065-substrate".
# ARC-065-substrate is NOT a closure NODE (arc_062's nodes are GAP-A..GAP-H); it is
# a claim-readiness pointer kept intentionally so the dependency lineage is visible
# in the frontmatter even though it does not resolve to a renderable node. Exempt it
# here (and ONLY it) so the validator stays green while honouring that decision. Any
# OTHER dangling ref is a typo and must fail. Keyed by (source_node, field, target).
#
# behavioral_diversity_isolation:GAP-C / GAP-C-build cross_plan_link to
# "v4_loop_segregation:ARC-110" (added governance_2026_06_27 / reconcile_2026_07_10
# in behavioral_diversity_isolation_plan.md): v4_loop_segregation is tracked as a
# substrate_queue.json entry (sd_id v4_loop_segregation, V3-closure-required per its
# own reclassification_note_2026_07_03), not as a closure-map plan file -- there is
# no v4_loop_segregation_plan.md and none is owed (the substrate landed no-op-default
# 2026-06-27; the tracking lives in claims.yaml ARC-110 + the substrate_queue entry).
# The pointer is deliberate (names the live conversion-ceiling frontier for two
# sibling nodes) and not renderable as a node. Exempt both (/governance cycle
# queue-depth-low-ops-aac785, 2026-08-10).
DANGLING_ALLOWLIST = {
    ("sleep_substrate:GAP-2", "depends_on", "arc_062_rule_apprehension:ARC-065-substrate"),
    ("behavioral_diversity_isolation:GAP-C", "cross_plan_link", "v4_loop_segregation:ARC-110"),
    ("behavioral_diversity_isolation:GAP-C-build", "cross_plan_link", "v4_loop_segregation:ARC-110"),
}

# Fields on each node whose entries point at other nodes/plans.
LINK_FIELDS = ("depends_on", "cross_plan_link")


def _candidate_plan_files() -> list[str]:
    """Same plan-file set read_closure() walks: known plans first, then any other
    *_plan.md in PLANNING_DIR (preserves UI order, captures newly-added plans)."""
    candidates = list(CLOSURE_KNOWN_PLANS)
    if PLANNING_DIR.exists():
        for p in sorted(PLANNING_DIR.glob("*_plan.md")):
            if p.name not in candidates:
                candidates.append(p.name)
    return candidates


def collect_ids_and_links():
    """Parse every closure plan once. Returns (node_ids, plan_ids, links) where
    links is a list of (source_node_id, field, target) tuples across all plans."""
    node_ids: set[str] = set()
    plan_ids: set[str] = set()
    links: list[tuple[str, str, str]] = []

    for fname in _candidate_plan_files():
        path = PLANNING_DIR / fname
        if not path.exists():
            continue
        plan = _parse_plan_frontmatter(path)
        if plan is None:
            # No (or unparseable) closure_plan frontmatter -- read_closure() treats
            # this as frontmatter_pending and contributes no nodes/links. Skip.
            continue
        plan_id = str(plan.get("id") or fname.replace("_plan.md", ""))
        plan_ids.add(plan_id)
        for n in (plan.get("nodes") or []):
            if not isinstance(n, dict):
                continue
            nid = str(n.get("id") or "")
            if not nid:
                continue
            node_ids.add(nid)
            for field in LINK_FIELDS:
                for target in (n.get(field) or []):
                    links.append((nid, field, str(target)))

    return node_ids, plan_ids, links


def find_dangling(node_ids, plan_ids, links):
    """Return the list of (source, field, target) links whose target is neither a
    node id nor a plan id and is not on the exempt allowlist."""
    dangling = []
    for source, field, target in links:
        if target in node_ids or target in plan_ids:
            continue
        if (source, field, target) in DANGLING_ALLOWLIST:
            continue
        dangling.append((source, field, target))
    return dangling


def main() -> int:
    node_ids, plan_ids, links = collect_ids_and_links()
    if not node_ids:
        print(
            "ERROR: no closure nodes parsed from "
            f"{PLANNING_DIR} -- nothing to validate (environment problem?).",
            file=sys.stderr,
        )
        return 2

    dangling = find_dangling(node_ids, plan_ids, links)

    print(
        f"check_closure_links: {len(node_ids)} nodes / {len(plan_ids)} plans / "
        f"{len(links)} links scanned; "
        f"{len(DANGLING_ALLOWLIST)} exempt back-pointer(s) allowed."
    )

    if not dangling:
        print("OK: no truly-dangling closure-map links.")
        return 0

    print("", file=sys.stderr)
    print(
        f"FAIL: {len(dangling)} dangling closure-map link(s) "
        "(target is neither a node id nor a plan id):",
        file=sys.stderr,
    )
    for source, field, target in dangling:
        print(f"  {source} --{field}--> {target} (DANGLING)", file=sys.stderr)
    print("", file=sys.stderr)
    print(
        "Fix the target id in the owning plan's frontmatter (a typo in "
        "depends_on / cross_plan_link), or -- if it is a deliberate back-pointer "
        "-- add it to DANGLING_ALLOWLIST in scripts/check_closure_links.py with a "
        "comment.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
