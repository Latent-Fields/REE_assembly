"""Regression tests: proposal status carry-forward must not cross the EXP/LIT lane.

`backlog_id` (EVB-NNNN) is the STABLE proposal identity across governance
regens -- `proposal_id` (EXP-/LIT-NNNN) is positional and renumbers -- but it
is NOT UNIQUE. Measured 2026-09-02 over the live 1150 items in
experiment_proposals.v1.json: 915 distinct backlog_ids, 234 duplicate groups.
One EVB legitimately backs TWO proposals on the same claim, an `experimental`
one and a `literature_review` twin (EVB-1183 -> EXP-0421 + LIT-0422).

Keying the status carry-forward on the identity key alone collapsed those two
onto one dict slot, so a resolved EXPERIMENTAL proposal's status was carried
onto its LITERATURE twin. Confirmed damage, same date: six literature reviews
carried `status: blocked_substrate` with a byte-identical blocked_by /
blocked_note copied from their experimental twin (EVB-1185, -1398, -1401,
-1408, -1583, and MECH-474's pair) -- suppressed from the workset even though
a literature review is never blocked by absent V3 substrate.

Run directly:  python test_proposal_lane_carry_forward.py
Or via pytest:  pytest test_proposal_lane_carry_forward.py
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build_experiment_indexes as b  # noqa: E402


def _register(records):
    """Build the two maps main() builds, from OLD (pre-regen) resolved records."""
    status_map, lanes_by_key = {}, {}
    for rec in records:
        keys = b._proposal_identity_keys(rec)
        if not keys or rec.get("status", "proposed") == "proposed":
            continue
        payload = {
            k: rec[k]
            for k in b._PROPOSAL_STATUS_CARRY_FORWARD_FIELDS
            if k in rec
        }
        lane = b._proposal_lane(rec)
        for k in keys:
            status_map[(k, lane)] = payload
            lanes_by_key.setdefault(k, set()).add(lane)
    return status_map, lanes_by_key


class TestProposalLane(unittest.TestCase):
    def test_literature_spellings_collapse_to_one_lane(self):
        # manual_proposals.v1.json spells it "literature" (12 live items); the
        # generated file spells it "literature_review" (523). If these did not
        # collapse, adding the lane key would SILENTLY WIPE manual literature
        # resolutions -- strictly worse than the bleed it fixes.
        self.assertEqual(b._proposal_lane({"proposal_type": "literature"}), "literature")
        self.assertEqual(
            b._proposal_lane({"proposal_type": "literature_review"}), "literature"
        )

    def test_experimental_is_its_own_lane(self):
        self.assertEqual(
            b._proposal_lane({"proposal_type": "experimental"}), "experimental"
        )
        self.assertNotEqual(
            b._proposal_lane({"proposal_type": "experimental"}),
            b._proposal_lane({"proposal_type": "literature_review"}),
        )

    def test_missing_type_does_not_raise(self):
        self.assertEqual(b._proposal_lane({}), "?")
        self.assertEqual(b._proposal_lane({"proposal_type": None}), "?")


class TestTwinCollision(unittest.TestCase):
    """The bug itself: EVB-1185-shaped pair, one resolved, one not."""

    OLD = [
        {
            "backlog_id": "EVB-1185",
            "proposal_id": "EXP-0424",
            "proposal_type": "experimental",
            "claim_id": "MECH-999",
            "status": "blocked_substrate",
            "blocked_by": ["MECH-054"],
            "blocked_note": "no precision->DV channel in ree_core",
        },
        {
            "backlog_id": "EVB-1185",
            "proposal_id": "LIT-0425",
            "proposal_type": "literature_review",
            "claim_id": "MECH-999",
            "status": "proposed",
        },
    ]

    def test_experimental_twin_still_carries_its_own_block(self):
        smap, lanes = _register(self.OLD)
        fresh = {
            "backlog_id": "EVB-1185",
            "proposal_id": "EXP-0424",
            "proposal_type": "experimental",
            "status": "proposed",
        }
        got = b.lookup_existing_proposal_status(fresh, smap, lanes)
        self.assertIsNotNone(got, "the experimental block must survive a regen")
        self.assertEqual(got["status"], "blocked_substrate")
        self.assertEqual(got["blocked_by"], ["MECH-054"])

    def test_literature_twin_does_NOT_inherit_the_block(self):
        # The regression. A literature review is never blocked by absent V3
        # substrate -- the papers can be read whatever the substrate does.
        smap, lanes = _register(self.OLD)
        fresh = {
            "backlog_id": "EVB-1185",
            "proposal_id": "LIT-0425",
            "proposal_type": "literature_review",
            "status": "proposed",
        }
        got = b.lookup_existing_proposal_status(fresh, smap, lanes)
        self.assertIsNone(
            got,
            "literature twin inherited its experimental twin's status -- "
            "the EVB-1185 collision has regressed",
        )

    def test_both_lanes_resolved_keeps_each_lane_distinct(self):
        old = [
            dict(self.OLD[0]),
            {
                "backlog_id": "EVB-1185",
                "proposal_id": "LIT-0425",
                "proposal_type": "literature_review",
                "status": "executed",
                "executed_by": "LIT-RUN-1",
            },
        ]
        smap, lanes = _register(old)
        exp = b.lookup_existing_proposal_status(
            {"backlog_id": "EVB-1185", "proposal_type": "experimental"}, smap, lanes
        )
        lit = b.lookup_existing_proposal_status(
            {"backlog_id": "EVB-1185", "proposal_type": "literature_review"},
            smap,
            lanes,
        )
        self.assertEqual(exp["status"], "blocked_substrate")
        self.assertEqual(lit["status"], "executed")


class TestUnambiguousFallbackPreserved(unittest.TestCase):
    """Negative controls: the fix must not WIPE ordinary carry-forward.

    Wiping is the strictly worse direction -- a cross-lane bleed mislabels one
    proposal, a wipe loses every resolution on the next regen (which is exactly
    what chip-20260817-blocked-note-not-carried-forward had to repair once).
    """

    def test_sole_lane_still_matches_when_fresh_type_is_absent(self):
        old = [
            {
                "backlog_id": "EVB-2000",
                "proposal_id": "EXP-0500",
                "proposal_type": "experimental",
                "status": "executed",
                "executed_by": "V3-EXQ-901",
            }
        ]
        smap, lanes = _register(old)
        fresh = {"backlog_id": "EVB-2000", "proposal_id": "EXP-0500"}  # no type
        got = b.lookup_existing_proposal_status(fresh, smap, lanes)
        self.assertIsNotNone(got, "unambiguous key must still match lane-agnostically")
        self.assertEqual(got["executed_by"], "V3-EXQ-901")

    def test_manual_literature_spelling_matches_generated_spelling(self):
        old = [
            {
                "backlog_id": "EVB-2001",
                "proposal_id": "LIT-0501",
                "proposal_type": "literature",  # manual_proposals.v1.json spelling
                "status": "executed",
            }
        ]
        smap, lanes = _register(old)
        fresh = {
            "backlog_id": "EVB-2001",
            "proposal_id": "LIT-0501",
            "proposal_type": "literature_review",  # generated spelling
        }
        got = b.lookup_existing_proposal_status(fresh, smap, lanes)
        self.assertIsNotNone(got, "lane spellings must collapse, or manual "
                                  "literature resolutions are silently wiped")
        self.assertEqual(got["status"], "executed")

    def test_transitional_proposal_id_match_before_backlog_id_minted(self):
        # _proposal_identity_keys' documented transition: old record written
        # under proposal_id only; fresh item now also carries a backlog_id.
        old = [
            {
                "proposal_id": "EXP-0502",
                "proposal_type": "experimental",
                "status": "gated",
                "gating_reason": "awaiting ARC-007",
            }
        ]
        smap, lanes = _register(old)
        fresh = {
            "backlog_id": "EVB-2002",  # newly minted
            "proposal_id": "EXP-0502",
            "proposal_type": "experimental",
        }
        got = b.lookup_existing_proposal_status(fresh, smap, lanes)
        self.assertIsNotNone(got)
        self.assertEqual(got["status"], "gated")

    def test_unrelated_backlog_id_never_matches(self):
        smap, lanes = _register(
            [{"backlog_id": "EVB-3000", "proposal_type": "experimental",
              "status": "executed"}]
        )
        got = b.lookup_existing_proposal_status(
            {"backlog_id": "EVB-3001", "proposal_type": "experimental"}, smap, lanes
        )
        self.assertIsNone(got)

    def test_proposed_records_are_never_registered(self):
        smap, lanes = _register(
            [{"backlog_id": "EVB-4000", "proposal_type": "experimental",
              "status": "proposed"}]
        )
        self.assertEqual(smap, {})
        self.assertEqual(lanes, {})


if __name__ == "__main__":
    unittest.main(verbosity=2)
