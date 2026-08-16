"""Steward integrity detectors (stages 1-3).

Each detector module exposes:

    DETECTOR_ID     str, e.g. "D-002"
    DETECTOR_TITLE  str
    TIER            str, "T0" | "T1" | "T2" (optional, defaults T2)
    run(ctx) -> (list[finding_dict], summary_dict)

A T0 detector MAY additionally expose:

    fix(ctx, now, dry_run=True) -> list[fix_record]

Findings are built with _common.finding() so the schema cannot drift between
detectors.

THE TIERS
=====================================================================
T0  Deterministic detection AND a mechanical, single, reversible repair. The
    runner can apply it with --fix; no model is woken. A T0 detector may still
    emit a T1 finding for an instance that turns out ambiguous -- "if a fix is
    ever ambiguous it is not T0, demote it rather than guessing" is enforced in
    finding() rather than left to discipline.
T1  Detection is deterministic, the disposition is not. Escalates.
T2  Reported for action taken elsewhere. The git lane is T2 BY CONSTRUCTION:
    it classifies a divergence and never touches a ref, index or worktree on a
    shared checkout other machines push to.

Registry order is report order, and it is load-bearing in one place: D-101 must
precede D-102, because D-102's tail check re-verifies the pins D-101 published.
"""

from . import (  # noqa: F401
    d001_phase_generation_mismatch,
    d002_orphan_v3_claim,
    d006_duplicate_governance_flag,
    d008_plan_frontmatter_date_drift,
    d010_denominator_integrity,
    d101_divergence_content_equivalence,
    d102_moving_ref_guard,
)

# Keep D-002 first: it is the validated detector (precision 4/4) and the one
# the tier exists for. D-101 before D-102 -- see the module docstring.
DETECTORS = [
    d002_orphan_v3_claim,
    d001_phase_generation_mismatch,
    d006_duplicate_governance_flag,
    d008_plan_frontmatter_date_drift,
    d010_denominator_integrity,
    d101_divergence_content_equivalence,
    d102_moving_ref_guard,
]

# Detectors offering a mechanical repair, in application order.
FIXABLE = [
    d006_duplicate_governance_flag,
    d008_plan_frontmatter_date_drift,
]
