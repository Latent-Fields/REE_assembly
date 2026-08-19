#!/usr/bin/env python3
"""D-002 -- orphan V3 claim: live V3 work excluded from the V3 denominator.

THE DEFECT. A claim the registry calls live V3 work (`implementation_phase: v3`
and/or `v3_pending: true`) whose owning closure nodes are ALL in a status that
generate_closure_snapshot.py drops from the V3 progress denominator. The claim is
then not done, not remaining, and not visible as a gap -- it is simply absent
from closure accounting, with nothing anywhere reporting that absence.

ORIGIN. SD-031 sat in exactly this state for ten weeks: `implementation_phase:
v3`, `v3_pending: true`, and its only owning node self_attribution:GAP-5 was
`deferred`. It was found by hand on 2026-08-15 and fixed by splitting GAP-6 out
(closure 72.6% -> 71.9% -- a correction, not a regression: the number falls
because the correction surfaces hidden remaining work). Nothing about DETECTING
it required judgement, which is the entire thesis of the Steward: detection is
deterministic and free, and the model is for adjudication only.

VALIDATION. Run against REE_assembly at 2026-08-15 this detector surfaced four
further instances, all four adjudicated genuine (precision 4/4, chip
chip-20260815-orphan-v3-claims-adjudicate, landed REE_assembly 7478ffe8ad):
MECH-316 + MECH-317 (arc_062_rule_apprehension:GAP-I-absorption, a half-applied
2026-06-23 reclassification that set `deferred` immediately while explicitly
declining the matching claims.yaml change), MECH-314a
(behavioral_diversity_isolation:GAP-G) and MECH-091 (commitment_closure:GAP-7).

DO NOT ADD A SIGNAL-STRENGTH ESCALATION GATE. An earlier revision gated
escalation on `v3_pending`, which demoted MECH-091 and MECH-314a to list-only.
Adjudication refuted that: MECH-314a is a real stale node, and the gate would
have withheld it indefinitely. `severity` and `signal` RANK findings when the
escalation budget is contended; they never withhold one. The general rule is
that a precision floor is legitimate only for a detector whose findings are
noisy -- never for one whose MISSES are silent, and every miss here is silent by
construction (that is the defect being detected).

EXPECT THE COUNT TO FALL. The adjudication PROPOSED un-deferring the three owning
nodes to /governance rather than applying it (changing a pre-existing node status
was outside that session's authority). When governance acts, these findings
disappear -- that is correct RESOLVED behaviour, not a regression. Assert the
classification logic, never a literal count.

READ ONLY. This detector never edits claims.yaml, any node status, or the queue.
"""

from __future__ import annotations

from ._common import DEFERRED_STATUSES, Context, finding

DETECTOR_ID = "D-002"
DETECTOR_TITLE = "Orphan V3 claim (live V3 work outside the V3 denominator)"
# T1: detection is deterministic, but whether the NODE status is wrong (the
# SD-031 outcome) or the CLAIM phase is wrong is a disposition, not a
# mechanical fix -- see the finding detail below. Matches docs/DETECTORS.md
# and README.md's detector table ("D-002 | T1"). Until 2026-08-18 this was
# never passed, so every finding silently emitted _common.finding()'s default
# T2 instead -- see chip-20260817-steward-emitted-tier-vs-designed-tier.
TIER = "T1"


def _is_live_v3(claim: dict) -> bool:
    phase = str(claim.get("implementation_phase") or "").strip().lower()
    return phase == "v3" or claim.get("v3_pending") is True


def run(ctx: Context) -> tuple[list[dict], dict]:
    findings: list[dict] = []
    n_live_v3 = 0
    n_unowned = 0

    for claim in ctx.claims:
        cid = str(claim.get("id") or "")
        if not cid or not _is_live_v3(claim):
            continue
        n_live_v3 += 1

        owners = ctx.v3_owners(cid)
        if not owners:
            # No V3-generation node owns this claim at all. That is a DIFFERENT
            # defect (the generation axis, not the status axis) and belongs to
            # D-001 -- reporting it here too would double-count one claim under
            # two detectors and make both look noisier than they are.
            n_unowned += 1
            continue

        if not all(n.status in DEFERRED_STATUSES for n in owners):
            continue  # at least one owner is not deferred

        # NOTE the predicate is DEFERRED_STATUSES, deliberately NOT the wider
        # "excluded from the denominator" set (weight None), even though the
        # harm -- absence from closure accounting -- is identical. The wider set
        # also contains `assembling`, which means "required for v3, actively
        # under construction, leave it alone": the anti-forcing status that
        # exists so unhurried assembly is not scored as failure, and which IS
        # reported on its own assembly-frontier axis. Measured on the
        # 2026-08-16 tree, widening the predicate adds exactly three claims
        # (ARC-108, MECH-450, SD-033b), all owned by `assembling` nodes, none of
        # them orphaned -- pure false positives against work the design
        # deliberately protects, and they would dilute a detector whose
        # precision is its whole value (4/4 adjudicated). The wider
        # silent-exclusion surface is real and is owned by D-010, which reports
        # it as a standing surface rather than as per-claim defects.

        # Every owning V3 node is excluded from the denominator.
        v3_pending = claim.get("v3_pending") is True
        # The registry asserting "held pending V3 substrate" while every owner is
        # deferred is a direct self-contradiction, so it ranks above a claim that
        # merely carries implementation_phase: v3. Both still escalate.
        #
        # The weak tier is P1/0.8, not P2/0.6, and the reason is evidential
        # rather than cosmetic: every finding this detector has ever produced was
        # adjudicated genuine (4/4), so even its weak tier carries more evidence
        # than an unvalidated detector's strong tier. Ranked any lower, D-001's
        # P1 findings displace MECH-091 and MECH-314a out of the escalation
        # budget on a first run -- which is the same withholding-by-signal the
        # adjudication already refuted once, arriving through the ranking door
        # instead of the gate door.
        severity = "P0" if v3_pending else "P1"
        signal = "strong" if v3_pending else "weak"
        confidence = 0.95 if v3_pending else 0.8

        owner_desc = ", ".join(
            "%s (%s, %s)" % (n.node_id, n.status, n.plan_file) for n in owners
        )
        findings.append(finding(
            detector=DETECTOR_ID,
            subject=cid,
            title="%s reads as live V3 but every owning closure node is outside "
                  "the V3 denominator" % cid,
            detail=(
                "Claim %s: status=%s, implementation_phase=%s, v3_pending=%s. "
                "Owning V3 closure node(s): %s. Every one of those is deferred, "
                "so all are excluded from the closure denominator and this claim is "
                "neither done, nor remaining, nor visible as a gap. Same class as "
                "SD-031. Adjudicate whether the NODE status is wrong (the SD-031 "
                "and MECH-316/317 outcome) or the CLAIM phase is wrong -- the "
                "inversion runs both ways and the detector deliberately does not "
                "guess."
                % (cid, claim.get("status"), claim.get("implementation_phase"),
                   claim.get("v3_pending"), owner_desc)
            ),
            severity=severity,
            confidence=confidence,
            signal=signal,
            escalate=True,
            tier=TIER,
            evidence={
                "claim_status": claim.get("status"),
                "implementation_phase": claim.get("implementation_phase"),
                "v3_pending": claim.get("v3_pending"),
                "owners": [
                    {"node_id": n.node_id, "status": n.status,
                     "plan_file": n.plan_file, "plan_id": n.plan_id}
                    for n in owners
                ],
            },
        ))

    summary = {
        "detector": DETECTOR_ID,
        "title": DETECTOR_TITLE,
        "n_findings": len(findings),
        "live_v3_claims_scanned": n_live_v3,
        "live_v3_claims_with_no_v3_owner": n_unowned,
        "note": "Claims with no V3-generation owner at all are counted here but "
                "reported by D-001, not D-002, to avoid double-counting.",
    }
    return findings, summary
