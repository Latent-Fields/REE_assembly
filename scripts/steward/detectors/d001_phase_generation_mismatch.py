#!/usr/bin/env python3
"""D-001 -- claim implementation_phase vs owning plan generation.

THE DEFECT. A claim's `implementation_phase` disagrees with the `generation` of
every plan that owns it. The sharp case is a claim labelled `v3` whose owning
nodes all live in `v4` / `v5` / `v6` / `clinical` / `deferred` plans:
generate_closure_snapshot.py segments non-v3 plans out of the V3 closure map
entirely, so the claim is invisible to V3 accounting for a reason nothing
reports. That is the same denominator-invisibility failure as D-002, reached
along the GENERATION axis instead of the STATUS axis.

WHY "EVERY owner" AND NOT "ANY owner". The literal any-owner reading fires 63
times on the 2026-08-16 tree, and most of those are benign: a V4 roadmap plan
routinely back-points at the V3 claims it builds on, which is a forward
reference, not a defect. Requiring that NO owner sits in a v3-generation plan
cuts that to 27 and keeps only the claims that are actually unreachable from V3
closure. This detector's findings ARE noisy, so a precision floor is legitimate
here -- unlike D-002, whose misses are silent. The 36 filtered pairs are reported
as a count in the summary rather than dropped silently.

NOT A DUPLICATE of scripts/check_claim_phase_consistency.py. That script walks
the claim->claim dependency graph and asks whether a v4+ claim is reachable from
a V3 build commitment (phase label follows dependency). This one asks whether a
claim's phase agrees with the plan that OWNS it. Different graph, different edge
semantics, complementary answers.

KNOWN CLUSTERING, and why it is not pre-suppressed here. Of the 27 findings on
the 2026-08-16 tree, 10 come from a single `generation: clinical` plan
(psychiatric_failure_modes_plan.md) and 3 from a single `generation: deferred`
plan -- systematic whole-plan back-pointer patterns rather than 13 independent
defects. Collapsing those is a DISPOSITION, which stage 1 has no authority to
make; the right home is a whole-plan entry in state/suppressions.yaml added by
governance. The ledger this detector feeds is what calibrates that.

READ ONLY.
"""

from __future__ import annotations

from ._common import DEFAULT_GENERATION, Context, finding

DETECTOR_ID = "D-001"
DETECTOR_TITLE = "Claim phase vs owning plan generation mismatch"

# LIST-ONLY DEMOTION -- 2026-08-18, chip-20260817-d001-unowned-v3-claims.
#
# All 27 findings on base b3b95d7938 were adjudicated per claim: 3 confirmed
# (ARC-053, ARC-054, MECH-270 -- real phase-tag drift, see below), 24 false
# positive. Precision 3/27 = 0.11, below the SKILL.md 0.6 floor, so this
# detector is demoted to list-only: it still REPORTS every finding, it just
# never consumes escalation budget. That is the floor's own remedy ("reported,
# never escalated, until refined"), and it is appropriate here for the reason
# SKILL.md gives -- D-001's misses are NOT silent. An unowned v3 claim still
# appears in the registry, unlike D-002's orphans, which are invisible by
# construction. So a floor is safe here and is NOT safe for D-002.
#
# WHY THE PREDICATE ITSELF WAS NOT TIGHTENED. The dominant false-positive mode
# is a DELIBERATE cross-generation arrangement that the owning plan documents in
# prose -- the clinical lane holding one syndrome's claims across several
# generations at once, and v4/v5/v6 roadmap nodes naming their V3-era
# prerequisites. None of that is legible to frontmatter alone, so no sharper
# structural predicate separates it. One was measured rather than assumed: a
# "partial reconcile" rule (fire only when a SIBLING claim co-listed in the same
# owning node has already been reassigned off v3) cuts 27 -> 9 and keeps all 3
# confirmed, but precision only reaches 3/9 = 0.33 -- still under the floor.
# Tightening further would mean fitting the predicate to the same 3 cases it was
# just validated on, which GOV-HELDOUT-1 exists to forbid. So the disposition
# lives in state/suppressions.yaml, where it is per-claim, reasoned, and
# reversible, and the detector keeps its honest recall.
#
# THE 3 CONFIRMED FINDINGS ARE REAL AND ARE NOT SUPPRESSED. ARC-053/ARC-054
# (deferred_by_commitment:DEF-1) and MECH-270 (DEF-2) are a half-finished
# reassignment: their co-listed siblings ARC-055 and MECH-225/226/228 were moved
# to implementation_phase v4 and these were not, and BOTH node notes name the
# drift and point at a "held-reassignment batch" that never ran. Fixing them is
# a claims.yaml edit, which is governance's to make -- proposed in
# evidence/planning/d001_adjudication_staged_20260818.md.
#
# RESUME CONDITION. Restore escalation once those 3 are dispositioned by
# governance AND one full cycle has run with the suppressions live, if the
# unsuppressed residue then measures >= 0.6 precision. Flip this one constant.
LIST_ONLY_ESCALATE = False


def run(ctx: Context) -> tuple[list[dict], dict]:
    findings: list[dict] = []
    raw_pairs = 0
    filtered_benign = 0

    for claim in ctx.claims:
        cid = str(claim.get("id") or "")
        phase = str(claim.get("implementation_phase") or "").strip().lower()
        if not cid or not phase:
            continue
        owners = ctx.owners.get(cid, [])
        if not owners:
            continue

        gens = {n.generation for n in owners}
        raw_pairs += sum(1 for n in owners if n.generation != phase)

        if phase in gens:
            # At least one owning plan agrees with the declared phase; any other
            # generation owning it too is a forward back-pointer, not a defect.
            filtered_benign += sum(1 for n in owners if n.generation != phase)
            continue

        v3_pending = claim.get("v3_pending") is True
        if phase == DEFAULT_GENERATION:
            # v3 claim with no v3-generation owner -> invisible to V3 closure.
            severity = "P1" if v3_pending else "P3"
            confidence = 0.75 if v3_pending else 0.4
            signal = "strong" if v3_pending else "weak"
            title = ("%s is implementation_phase v3 but no v3-generation plan "
                     "owns it" % cid)
            detail = (
                "Claim %s declares implementation_phase=v3 (v3_pending=%s) but "
                "every owning closure node lives in a plan of generation %s. "
                "Non-v3 plans are segmented out of the V3 closure map, so this "
                "claim cannot appear in V3 progress, remaining work, or gaps. "
                "Adjudicate which side is stale: the claim's phase label, or the "
                "owning plan's generation."
                % (cid, claim.get("v3_pending"), sorted(gens))
            )
        elif gens != {DEFAULT_GENERATION}:
            # Cross-generation label drift with no denominator consequence: e.g.
            # a v4 claim owned only by a `deferred`- or `v5`-generation plan. The
            # claim is outside V3 accounting under BOTH readings, so neither
            # side's staleness changes what closure reports. Measured on the
            # 2026-08-16 tree this is 8 pairs, and reporting them would be pure
            # noise -- a detector that fires on things with no consequence is
            # how the escalation budget gets spent on nothing. Counted in the
            # summary, not dropped silently.
            filtered_benign += sum(1 for n in owners if n.generation != phase)
            continue

        else:
            # Non-v3 claim owned ONLY by v3-generation plans -> it IS inside the
            # V3 denominator despite being declared later-generation work, so it
            # inflates the V3 backlog with work nobody intends to do for v3.
            severity = "P2"
            confidence = 0.55
            signal = "weak"
            title = ("%s is implementation_phase %s but is owned only by "
                     "v3-generation plan(s)" % (cid, phase))
            detail = (
                "Claim %s declares implementation_phase=%s but every owning "
                "closure node lives in a v3-generation plan, so it is inside the "
                "V3 closure denominator. Either the phase label is stale or the "
                "owning node belongs in a forward-roadmap plan."
                % (cid, phase)
            )

        findings.append(finding(
            detector=DETECTOR_ID,
            subject=cid,
            title=title,
            detail=detail,
            severity=severity,
            confidence=confidence,
            signal=signal,
            escalate=LIST_ONLY_ESCALATE,
            evidence={
                "implementation_phase": phase,
                "v3_pending": claim.get("v3_pending"),
                "claim_status": claim.get("status"),
                "owner_generations": sorted(gens),
                "owners": [
                    {"node_id": n.node_id, "status": n.status,
                     "plan_file": n.plan_file, "generation": n.generation}
                    for n in owners
                ],
            },
        ))

    summary = {
        "detector": DETECTOR_ID,
        "title": DETECTOR_TITLE,
        "n_findings": len(findings),
        "raw_owner_pairs_mismatched": raw_pairs,
        "benign_forward_backpointers_filtered": filtered_benign,
        "note": "A claim with at least one owning plan of its own generation is "
                "not reported; the filtered count is stated here so the "
                "narrowing is auditable rather than silent.",
    }
    return findings, summary
