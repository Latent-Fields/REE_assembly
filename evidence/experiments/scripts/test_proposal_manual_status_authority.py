"""Regression tests: a hand-recorded proposal status must survive a regen.

THE DEFECT (confirmed 2026-09-07, session IGW-20260907-211;
chip-20260907-proposal-status-revert-regen). build_experiment_indexes.py resolved
each proposal's status from the PREVIOUS GENERATED experiment_proposals.v1.json
and applied it unconditionally (`_p.update(_carried)`), then wrote the same
resolution back into manual_proposals.v1.json. So a session that hand-edited only
manual_proposals.v1.json -- the curated source, whose own docstring presents
itself as the place to add and curate items -- had its edit reverted on the very
next governance regen, with no error and no warning, because the DERIVED file's
prior status outranked the CURATED one.

CONFIRMED INSTANCE, the shape pinned here. IGW-20260904-214 recorded ARC-019 /
EVB-1189 as blocked_substrate in manual_proposals.v1.json (REE_assembly
dcfa8ddc24, 2026-09-04T22:19:08Z). The regen five hours later (8d9fe1c714)
reverted it to "executed" and injected executed_by / executed_queue_id =
V3-EXQ-591g -- an ERROR run.

WHY IT MATTERS BEYOND THE ONE FIELD. generate_inter_governance_workset.py's
retest lane suppresses a pending_retest_after_substrate claim only while its
proposal is in _PROPOSAL_BLOCKED_SUBSTRATE_STATUSES. Reverting the status
silently RE-ARMED the auto-spawn: the identical ARC-019 retest respawned three
days later as IGW-20260907-211 and re-derived the same four-condition
investigation from scratch.

SCOPE, measured 2026-09-07 and deliberately not overstated: ARC-019 was the only
live row in this state (the data was repaired in 52e37f8ec4; manual and generated
statuses agree on all 122 manual rows today). This is a latent trap that fires
whenever a blocked proposal's lineage also carries an executed queue_id -- so
these tests, not a live diff, are what hold the fix.

NOT A MUTE OF THE WRITE-BACK. The write-back was built 2026-08-02 (session
determined-ritchie-55a3a6) to clear manual rows frozen at a permanently-stale
"proposed" long after the work landed. That path must keep working, and
StaleProposedWriteBackStillWorksTest is what separates this fix from a mute.

Run directly:  /opt/local/bin/python3 test_proposal_manual_status_authority.py
Or via pytest: /opt/local/bin/python3 -m pytest test_proposal_manual_status_authority.py
"""
import copy
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build_experiment_indexes as b  # noqa: E402


# --- fixtures: the ARC-019 / EVB-1189 board ---------------------------------

# What IGW-20260904-214 wrote into manual_proposals.v1.json.
MANUAL_ARC_019 = {
    "proposal_id": "EXP-1189",
    "backlog_id": "EVB-1189",
    "claim_id": "ARC-019",
    "proposal_type": "experimental",
    "priority": "medium",
    "objective": "Retest ARC-019 once the substrate lands.",
    "status": "blocked_substrate",
    "gating_reason": (
        "Four-condition investigation: the lineage's only run V3-EXQ-591g ERRORed; "
        "no substrate change since. Do not re-queue."
    ),
    "source": "manual",
}

# What the PREVIOUS GENERATED experiment_proposals.v1.json carried for it.
CARRIED_EXECUTED = {
    "status": "executed",
    "executed_by": "V3-EXQ-591g",
    "executed_queue_id": "V3-EXQ-591g",
}


def _register(records):
    """Build the two maps main() builds, from OLD (pre-regen) resolved records."""
    status_map, lanes_by_key = {}, {}
    for rec in records:
        keys = b._proposal_identity_keys(rec)
        if not keys or rec.get("status", "proposed") == "proposed":
            continue
        payload = {
            k: rec[k] for k in b._PROPOSAL_STATUS_CARRY_FORWARD_FIELDS if k in rec
        }
        lane = b._proposal_lane(rec)
        for k in keys:
            status_map[(k, lane)] = payload
            lanes_by_key.setdefault(k, set()).add(lane)
    return status_map, lanes_by_key


class ManualStatusIsAuthoritativeTest(unittest.TestCase):
    """The predicate, in isolation."""

    def test_blocked_substrate_beats_a_carried_executed(self):
        self.assertTrue(
            b.manual_status_is_authoritative(MANUAL_ARC_019, CARRIED_EXECUTED)
        )

    def test_every_blocked_substrate_spelling_is_covered(self):
        for st in b._PROPOSAL_BLOCKED_SUBSTRATE_STATUSES:
            self.assertTrue(
                b.manual_status_is_authoritative({"status": st}, CARRIED_EXECUTED),
                f"{st} is a retest-lane suppressor -- losing it re-arms an auto-spawn",
            )

    def test_every_manual_adjudication_status_is_covered(self):
        for st in b._PROPOSAL_MANUAL_ADJUDICATED_STATUSES:
            self.assertTrue(
                b.manual_status_is_authoritative({"status": st}, CARRIED_EXECUTED)
            )

    def test_proposed_never_wins(self):
        """THE SCOPING ASSERTION. `proposed` is the generated default and the
        stale value the write-back exists to clear -- if it won, the 2026-08-02
        defect returns and every manual row freezes at `proposed` forever."""
        self.assertFalse(
            b.manual_status_is_authoritative({"status": "proposed"}, CARRIED_EXECUTED)
        )

    def test_absent_status_never_wins(self):
        self.assertFalse(b.manual_status_is_authoritative({}, CARRIED_EXECUTED))
        self.assertFalse(
            b.manual_status_is_authoritative({"status": None}, CARRIED_EXECUTED)
        )
        self.assertFalse(
            b.manual_status_is_authoritative({"status": "  "}, CARRIED_EXECUTED)
        )

    def test_agreement_is_not_a_win(self):
        """When both say the same thing the carry-forward is not a reversion --
        let it run so the companion fields (blocked_note, gating_reason) still
        come across."""
        self.assertFalse(
            b.manual_status_is_authoritative(
                {"status": "blocked_substrate"}, {"status": "blocked_substrate"}
            )
        )

    def test_case_and_whitespace_are_normalised_on_both_sides(self):
        self.assertFalse(
            b.manual_status_is_authoritative(
                {"status": " Blocked_Substrate "}, {"status": "blocked_substrate"}
            )
        )

    def test_no_carried_record_is_not_a_win(self):
        self.assertFalse(b.manual_status_is_authoritative(MANUAL_ARC_019, None))
        self.assertFalse(b.manual_status_is_authoritative(MANUAL_ARC_019, {}))


class CarryForwardTest(unittest.TestCase):
    """The generated-side loop: `_p.update(_carried)`."""

    def test_arc_019_stays_blocked_substrate(self):
        item = copy.deepcopy(MANUAL_ARC_019)
        smap, lanes = _register([dict(MANUAL_ARC_019, **CARRIED_EXECUTED)])
        carried = b.lookup_existing_proposal_status(item, smap, lanes)
        won = b.apply_proposal_status_carry_forward(item, carried)
        self.assertTrue(won)
        self.assertEqual("blocked_substrate", item["status"])

    def test_the_execution_provenance_is_not_grafted_on(self):
        """The whole update is skipped, not just the status field -- executed_by
        on a blocked_substrate row is what made the corruption look real."""
        item = copy.deepcopy(MANUAL_ARC_019)
        b.apply_proposal_status_carry_forward(item, CARRIED_EXECUTED)
        self.assertNotIn("executed_by", item)
        self.assertNotIn("executed_queue_id", item)

    def test_the_manual_gating_reason_survives(self):
        item = copy.deepcopy(MANUAL_ARC_019)
        b.apply_proposal_status_carry_forward(item, CARRIED_EXECUTED)
        self.assertIn("Do not re-queue", item["gating_reason"])

    def test_a_generated_proposed_row_still_carries_forward(self):
        """The ordinary path, untouched: a freshly generated row is minted
        `proposed` and must pick up the resolution from the previous file."""
        item = {"backlog_id": "EVB-2000", "proposal_type": "experimental",
                "status": "proposed"}
        won = b.apply_proposal_status_carry_forward(item, CARRIED_EXECUTED)
        self.assertFalse(won)
        self.assertEqual("executed", item["status"])
        self.assertEqual("V3-EXQ-591g", item["executed_queue_id"])

    def test_agreeing_rows_still_receive_the_companion_fields(self):
        item = {"backlog_id": "EVB-2001", "proposal_type": "experimental",
                "status": "blocked_substrate"}
        carried = {"status": "blocked_substrate",
                   "blocked_note": "MECH-457 unbuilt", "blocked_by": ["MECH-457"]}
        self.assertFalse(b.apply_proposal_status_carry_forward(item, carried))
        self.assertEqual(["MECH-457"], item["blocked_by"])
        self.assertEqual("MECH-457 unbuilt", item["blocked_note"])


class WriteBackTest(unittest.TestCase):
    """The manual_proposals.v1.json side."""

    def test_the_manual_row_is_left_untouched(self):
        row = copy.deepcopy(MANUAL_ARC_019)
        before = copy.deepcopy(row)
        changed, won = b.apply_manual_proposal_write_back(row, CARRIED_EXECUTED)
        self.assertTrue(won)
        self.assertFalse(changed, "a reversion must not mark the file dirty")
        self.assertEqual(before, row)

    def test_stale_proposed_write_back_still_works(self):
        """THE ANTI-MUTE ASSERTION. This is the path the write-back was built
        for (2026-08-02): a manual row frozen at `proposed` long after the work
        landed must still be cleared."""
        row = {"proposal_id": "EXP-0500", "claim_id": "Q-007",
               "proposal_type": "experimental", "status": "proposed"}
        changed, won = b.apply_manual_proposal_write_back(row, CARRIED_EXECUTED)
        self.assertFalse(won)
        self.assertTrue(changed)
        self.assertEqual("executed", row["status"])
        self.assertEqual("V3-EXQ-591g", row["executed_by"])

    def test_no_resolution_is_a_no_op(self):
        row = copy.deepcopy(MANUAL_ARC_019)
        self.assertEqual((False, False), b.apply_manual_proposal_write_back(row, None))
        self.assertEqual((False, False), b.apply_manual_proposal_write_back(row, {}))

    def test_an_already_matching_row_reports_no_change(self):
        row = {"proposal_id": "EXP-0501", "status": "executed",
               "executed_by": "V3-EXQ-591g", "executed_queue_id": "V3-EXQ-591g"}
        changed, won = b.apply_manual_proposal_write_back(row, CARRIED_EXECUTED)
        self.assertFalse(changed)
        self.assertFalse(won)


class BothSitesShareOnePredicateTest(unittest.TestCase):
    """The two sites drifting apart is how a half-fix would look identical to a
    fix: the status would hold in memory and still be reverted on disk (or the
    reverse). Assert they agree rather than trusting the call sites."""

    CASES = [
        (MANUAL_ARC_019, CARRIED_EXECUTED),
        ({"status": "proposed"}, CARRIED_EXECUTED),
        ({"status": "gated"}, {"status": "executed"}),
        ({"status": "executed"}, {"status": "executed"}),
        ({}, CARRIED_EXECUTED),
        ({"status": "blocked_substrate"}, None),
    ]

    def test_carry_forward_and_write_back_agree_on_every_case(self):
        for item, carried in self.CASES:
            a = b.apply_proposal_status_carry_forward(copy.deepcopy(item), carried)
            _, c = b.apply_manual_proposal_write_back(copy.deepcopy(item), carried)
            self.assertEqual(a, c, f"sites disagree on {item.get('status')!r}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
