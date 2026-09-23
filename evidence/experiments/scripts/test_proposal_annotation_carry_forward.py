"""Regression tests: hand-written proposal annotations must survive a regen.

THE DEFECT (GFLAG-0401, chip-20260923-proposal-regen-audit-gap). The status
carry-forward in build_experiment_indexes.py registers only rows whose status is
not "proposed", and carries only _PROPOSAL_STATUS_CARRY_FORWARD_FIELDS. So two
shapes of governance correction were dropped by the next regen:

  (a) annotation fields documenting a correction -- withdrawn_note (R7
      withdrawals), status_correction_note_<date> + executed_by_retracted_<date>
      (executed -> proposed reverts), governance_note (GFLAG-0317 blocks),
      release_note_<date> -- lost whatever the row's status;
  (b) the gating record on a row RELEASED to "proposed" ("RELEASED 2026-09-23
      (GFLAG-0401): the prior gating premise ... is FALSE") -- lost because a
      "proposed" row was never registered at all.

MEASURED, 2026-09-23, regen of origin/master in a throwaway worktree: 13 of the
69 rows hand-fixed in REE_assembly f578fcdb7c lost a field, plus both GFLAG-0317
rows of be4523acb8e. With the fix, 11 of those 13 survive; the remaining 2
(EXP-0440 / EXP-0585) are re-stamped from SD-056's claims.yaml experiment_gate by
apply_claim_queue_gate on purpose -- a claim-side source, flagged separately.

WHAT MUST NOT BE CARRIED onto a released row: release_condition / blocked_by /
blocked_note. scripts/proposal_feasibility.py FILTER G treats a recorded
release_condition on a non-ran row as a live do-not-mint block (confirmed on
EXP-0755 / MECH-018 the same day), so carrying one would silently re-block the
claim the release was meant to free. ReleasedRowTest pins that.

Run directly:  /opt/local/bin/python3 test_proposal_annotation_carry_forward.py
Or via pytest: /opt/local/bin/python3 -m pytest test_proposal_annotation_carry_forward.py
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build_experiment_indexes as b  # noqa: E402


def _register(records):
    """Build the annotation maps exactly as main() builds them."""
    ann_map, lanes = {}, {}
    for rec in records:
        keys = b._proposal_identity_keys(rec)
        ann = b.proposal_annotation_fields(rec) if keys else {}
        if not ann:
            continue
        lane = b._proposal_lane(rec)
        for k in keys:
            ann_map[(k, lane)] = ann
            lanes.setdefault(k, set()).add(lane)
    return ann_map, lanes


def _fresh(pid, claim, backlog, ptype="experimental"):
    """A freshly generated row: always minted "proposed", no annotations."""
    return {"proposal_id": pid, "claim_id": claim, "backlog_id": backlog,
            "proposal_type": ptype, "status": "proposed", "objective": "derived"}


# The live key names from f578fcdb7c / be4523acb8e -- the regex must match all.
LIVE_ANNOTATION_KEYS = (
    "withdrawn_note",
    "governance_note",
    "governance_note_2026_09_23",
    "status_correction_note_2026_09_23",
    "executed_by_retracted_2026_09_23",
    "release_condition_note_2026_09_23",
    "release_note_2026_09_23",
)


class AnnotationKeyShapeTest(unittest.TestCase):
    def test_every_live_annotation_key_is_recognised(self):
        for k in LIVE_ANNOTATION_KEYS:
            self.assertTrue(b._PROPOSAL_ANNOTATION_KEY_RE.match(k), k)

    def test_status_family_is_left_to_the_status_carry_forward(self):
        # blocked_note matches the shape but is status-family: the annotation
        # layer must not become a second, unguarded path for it.
        row = {"proposal_id": "EXP-1", "backlog_id": "EVB-1", "status": "blocked_substrate",
               "blocked_note": "x", "withdrawn_note": "y"}
        self.assertEqual(b.proposal_annotation_fields(row), {"withdrawn_note": "y"})

    def test_derived_fields_are_not_annotations(self):
        for k in ("objective", "why_now", "status", "priority", "notes_count"):
            self.assertFalse(b._PROPOSAL_ANNOTATION_KEY_RE.match(k), k)

    def test_blank_values_never_fill(self):
        row = {"proposal_id": "EXP-1", "status": "withdrawn", "withdrawn_note": ""}
        self.assertEqual(b.proposal_annotation_fields(row), {})


class WithdrawnRowTest(unittest.TestCase):
    """Shape (a): EXP-1011 / MECH-384, withdrawn with a withdrawn_note."""

    OLD = {"proposal_id": "EXP-1011", "claim_id": "MECH-384", "backlog_id": "EVB-1011",
           "proposal_type": "experimental", "status": "withdrawn",
           "withdrawn_note": "Withdrawn 2026-09-23 (GFLAG-0401; ... MECH-384 R7)"}

    def test_note_survives(self):
        ann_map, lanes = _register([self.OLD])
        item = _fresh("EXP-1011", "MECH-384", "EVB-1011")
        item["status"] = "withdrawn"  # what the status carry-forward already restores
        got = b.lookup_existing_proposal_status(item, ann_map, lanes)
        self.assertEqual(b.apply_proposal_annotation_carry_forward(item, got), ["withdrawn_note"])
        self.assertEqual(item["withdrawn_note"], self.OLD["withdrawn_note"])

    def test_the_status_carry_forward_alone_drops_it(self):
        """The blind spot, measured: the pre-fix path carried only these fields."""
        self.assertNotIn("withdrawn_note", b._PROPOSAL_STATUS_CARRY_FORWARD_FIELDS)


class ReleasedRowTest(unittest.TestCase):
    """Shape (b): EXP-0415 / ARC-001 released to proposed; EXP-0755 / MECH-018."""

    RELEASED = {"proposal_id": "EXP-0415", "claim_id": "ARC-001", "backlog_id": "EVB-0415",
                "proposal_type": "experimental", "status": "proposed",
                "gating_reason": "RELEASED 2026-09-23 (GFLAG-0401): premise FALSE",
                "gated_by_session": "confident-franklin-c8e403"}
    RELEASED_WITH_BLOCK_RESIDUE = {
        "proposal_id": "EXP-0755", "claim_id": "MECH-018", "backlog_id": "EVB-0755",
        "proposal_type": "experimental", "status": "proposed",
        "gating_reason": "EXP-0755 REFUSED at Step 2.5",
        "release_condition": "ALL THREE land",
        "blocked_by": ["MECH-018"], "blocked_note": "integrate() no gradient step",
        "release_note_2026_09_23": "All three release_condition parts met",
    }

    def test_gating_record_survives_on_a_proposed_row(self):
        ann_map, lanes = _register([self.RELEASED])
        item = _fresh("EXP-0415", "ARC-001", "EVB-0415")
        b.apply_proposal_annotation_carry_forward(
            item, b.lookup_existing_proposal_status(item, ann_map, lanes))
        self.assertEqual(item["status"], "proposed")
        self.assertTrue(item["gating_reason"].startswith("RELEASED 2026-09-23"))
        self.assertEqual(item["gated_by_session"], "confident-franklin-c8e403")

    def test_block_signals_are_not_resurrected(self):
        ann_map, lanes = _register([self.RELEASED_WITH_BLOCK_RESIDUE])
        item = _fresh("EXP-0755", "MECH-018", "EVB-0755")
        b.apply_proposal_annotation_carry_forward(
            item, b.lookup_existing_proposal_status(item, ann_map, lanes))
        for k in ("release_condition", "blocked_by", "blocked_note"):
            self.assertNotIn(k, item, k)
        self.assertIn("release_note_2026_09_23", item)
        self.assertEqual(item["status"], "proposed")


class NoClobberAndNoBleedTest(unittest.TestCase):
    def test_existing_value_wins(self):
        item = {"withdrawn_note": "manual row's own note"}
        self.assertEqual(
            b.apply_proposal_annotation_carry_forward(item, {"withdrawn_note": "old"}), [])
        self.assertEqual(item["withdrawn_note"], "manual row's own note")

    def test_exp_note_does_not_bleed_onto_lit_twin(self):
        # EXP-0971 / LIT-0972 share EVB-1506 (GFLAG-0317): the EXP row's
        # governance_note must stay on the EXP lane.
        old_exp = {"proposal_id": "EXP-0971", "claim_id": "MECH-328", "backlog_id": "EVB-1506",
                   "proposal_type": "experimental", "status": "blocked_substrate",
                   "governance_note": "GFLAG-0317 proposed -> blocked_substrate"}
        ann_map, lanes = _register([old_exp])
        lit = _fresh("LIT-0972", "MECH-328", "EVB-1506", ptype="literature_review")
        got = b.lookup_existing_proposal_status(lit, ann_map, lanes)
        self.assertEqual(b.apply_proposal_annotation_carry_forward(lit, got), [])
        self.assertNotIn("governance_note", lit)


if __name__ == "__main__":
    unittest.main()
