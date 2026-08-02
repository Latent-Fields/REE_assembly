#!/usr/bin/env python3
"""Regression test for the proposal_type -> lane/skill routing bug in
generate_inter_governance_workset.py (found 2026-08-02, worktree
elastic-merkle-e0cca8).

Confirmed 2026-08-01: IGW-20260801-219 and IGW-20260801-220 were both tagged
lane="experiment" / skill="/queue-experiment" despite backing TWO DIFFERENT
proposal types under the SAME owner_backlog_id (EVB-0481/Q-086) in
experiment_proposals.v1.json -- an "experimental" proposal (EXP-0318) and a
"literature_review" proposal (LIT-0319). Landing IGW-220 correctly required
/lit-pull, not /queue-experiment.

The fix: _proposal_lane_skill() derives lane/skill from the individual
proposal's OWN proposal_type field, not from owner_backlog_id (which the old
code implicitly assumed was 1:1 with a single proposal_type).

Run: /opt/local/bin/python3 scripts/test_generate_inter_governance_workset_proposal_lane.py
"""

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent


def _load_generator():
    path = SCRIPTS_DIR / "generate_inter_governance_workset.py"
    spec = importlib.util.spec_from_file_location(
        "ree_igw_generator_proposal_lane_test", path
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


GEN = _load_generator()


class ProposalLaneSkillUnitTest(unittest.TestCase):
    """_proposal_lane_skill is a pure function -- test it directly against
    every proposal_type value observed in experiment_proposals.v1.json."""

    def test_experimental_routes_to_queue_experiment(self):
        self.assertEqual(
            GEN._proposal_lane_skill("experimental"),
            ("experiment", "/queue-experiment"),
        )

    def test_literature_review_routes_to_lit_pull(self):
        self.assertEqual(
            GEN._proposal_lane_skill("literature_review"),
            ("lit", "/lit-pull"),
        )

    def test_literature_routes_to_lit_pull(self):
        # Older proposals use the bare "literature" tag rather than
        # "literature_review" -- both must route the same way.
        self.assertEqual(
            GEN._proposal_lane_skill("literature"),
            ("lit", "/lit-pull"),
        )

    def test_case_and_whitespace_insensitive(self):
        self.assertEqual(
            GEN._proposal_lane_skill("  Literature_Review  "),
            ("lit", "/lit-pull"),
        )

    def test_unknown_or_missing_defaults_to_experiment(self):
        # Fail-open: an unrecognised or absent proposal_type must not silently
        # vanish from the workset -- it keeps the pre-existing default lane.
        self.assertEqual(
            GEN._proposal_lane_skill(None),
            ("experiment", "/queue-experiment"),
        )
        self.assertEqual(
            GEN._proposal_lane_skill(""),
            ("experiment", "/queue-experiment"),
        )
        self.assertEqual(
            GEN._proposal_lane_skill("implementation"),
            ("experiment", "/queue-experiment"),
        )


class SharedBacklogIdDifferentProposalTypeTest(unittest.TestCase):
    """Integration-level: two proposals sharing one owner_backlog_id (and one
    claim_id) but with different proposal_type must come back from
    _proposed_experiments() and route to DIFFERENT lane/skill tags -- the
    exact EVB-0481/Q-086 shape from the confirmed incident."""

    def setUp(self):
        self._orig_proposals_json = GEN.PROPOSALS_JSON
        self._tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        )
        self._tmp.close()
        GEN.PROPOSALS_JSON = Path(self._tmp.name)

    def tearDown(self):
        GEN.PROPOSALS_JSON = self._orig_proposals_json
        Path(self._tmp.name).unlink(missing_ok=True)

    def _write_proposals(self, items):
        Path(self._tmp.name).write_text(
            json.dumps({"schema_version": "experiment_proposals/v1", "items": items}),
            encoding="utf-8",
        )

    def test_two_proposal_types_one_backlog_id(self):
        claim_id = "TEST-PROP-001"
        backlog_id = "EVB-TEST-0001"
        self._write_proposals([
            {
                "proposal_id": "EXP-TEST-A",
                "backlog_id": backlog_id,
                "claim_id": claim_id,
                "proposal_type": "experimental",
                "status": "proposed",
                "why_now": ["test"],
            },
            {
                "proposal_id": "LIT-TEST-B",
                "backlog_id": backlog_id,
                "claim_id": claim_id,
                "proposal_type": "literature_review",
                "status": "proposed",
                "why_now": ["test"],
            },
        ])
        claims_meta = {
            claim_id: {
                "status": "candidate",
                "epistemic_category": "standard",
            }
        }

        props = GEN._proposed_experiments(claims_meta, exp_evidence=set())
        by_pid = {p["proposal_id"]: p for p in props}
        self.assertIn("EXP-TEST-A", by_pid)
        self.assertIn("LIT-TEST-B", by_pid)

        exp_lane, exp_skill = GEN._proposal_lane_skill(
            by_pid["EXP-TEST-A"].get("proposal_type")
        )
        lit_lane, lit_skill = GEN._proposal_lane_skill(
            by_pid["LIT-TEST-B"].get("proposal_type")
        )

        self.assertEqual((exp_lane, exp_skill), ("experiment", "/queue-experiment"))
        self.assertEqual((lit_lane, lit_skill), ("lit", "/lit-pull"))
        # The whole point of the bug: same backlog_id, same claim_id, must NOT
        # collapse to the same lane/skill tag.
        self.assertNotEqual((exp_lane, exp_skill), (lit_lane, lit_skill))


if __name__ == "__main__":
    unittest.main(verbosity=2)
