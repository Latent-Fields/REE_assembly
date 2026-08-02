#!/usr/bin/env python3
"""Regression test for the retest-lane blocked_substrate blind spot in
generate_inter_governance_workset.py (chip-20260802-igw-generator-blocked-
substrate-check).

Confirmed incident: INV-089's retest was investigated and closed 2026-07-31
(session inv089-retest-exq-subagent), which traced the real blocker to two
unbuilt CLAIMS (MECH-457, INV-088) -- not a substrate_queue row -- and
recorded status=blocked_substrate on the backing proposal (EXP-0080,
claim_id INV-089) in experiment_proposals.v1.json. The retest lane's
readiness check (_retest_blockers + the epistemic_category substrate_ceiling
fallback) only ever walks substrate_queue, so it found nothing and the
generator re-surfaced INV-089 as `ready` the very next regen
(IGW-20260802-220, 2026-08-02), wasting a second investigation.

Fix: _proposal_blocked_substrate_by_claim() reads experiment_proposals.v1.json
and the retest loop in build_workset() now forces `blocked` (with a
blocked_by descriptor) whenever a claim's backing proposal carries a
blocked_substrate-family status, regardless of what _retest_blockers /
_resolve_epistemic_category conclude.

Run: /opt/local/bin/python3 scripts/test_generate_inter_governance_workset_blocked_substrate.py
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
        "ree_igw_generator_blocked_substrate_test", path
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


GEN = _load_generator()


class ProposalBlockedSubstrateByClaimUnitTest(unittest.TestCase):
    """_proposal_blocked_substrate_by_claim() is a pure function over
    experiment_proposals.v1.json -- test it directly."""

    def setUp(self):
        self._orig = GEN.PROPOSALS_JSON
        self._tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
        self._tmp.close()
        GEN.PROPOSALS_JSON = Path(self._tmp.name)

    def tearDown(self):
        GEN.PROPOSALS_JSON = self._orig
        Path(self._tmp.name).unlink(missing_ok=True)

    def _write(self, items):
        Path(self._tmp.name).write_text(
            json.dumps({"schema_version": "experiment_proposals/v1", "items": items}),
            encoding="utf-8",
        )

    def test_blocked_substrate_status_is_picked_up(self):
        self._write([
            {
                "proposal_id": "EXP-TEST-A",
                "claim_id": "TEST-001",
                "status": "blocked_substrate",
                "blocked_by": ["MECH-999", "INV-999"],
            }
        ])
        out = GEN._proposal_blocked_substrate_by_claim()
        self.assertIn("TEST-001", out)
        self.assertEqual(out["TEST-001"]["proposal_id"], "EXP-TEST-A")

    def test_proposed_blocked_substrate_variant_is_picked_up(self):
        self._write([
            {"proposal_id": "EXP-TEST-B", "claim_id": "TEST-002",
             "status": "proposed_blocked_substrate"},
        ])
        out = GEN._proposal_blocked_substrate_by_claim()
        self.assertIn("TEST-002", out)

    def test_plain_proposed_status_is_not_picked_up(self):
        self._write([
            {"proposal_id": "EXP-TEST-C", "claim_id": "TEST-003", "status": "proposed"},
        ])
        out = GEN._proposal_blocked_substrate_by_claim()
        self.assertNotIn("TEST-003", out)

    def test_first_occurrence_wins_on_duplicate_claim_id(self):
        self._write([
            {"proposal_id": "EXP-TEST-D1", "claim_id": "TEST-004", "status": "blocked_substrate"},
            {"proposal_id": "EXP-TEST-D2", "claim_id": "TEST-004", "status": "blocked_substrate"},
        ])
        out = GEN._proposal_blocked_substrate_by_claim()
        self.assertEqual(out["TEST-004"]["proposal_id"], "EXP-TEST-D1")

    def test_missing_file_returns_empty(self):
        Path(self._tmp.name).unlink()
        self.assertEqual(GEN._proposal_blocked_substrate_by_claim(), {})


class RetestLaneBlockedSubstrateIntegrationTest(unittest.TestCase):
    """Integration-level, over the real build_workset() retest loop: a
    pending_retest_after_substrate claim whose backing proposal carries
    status=blocked_substrate must render `blocked` even though
    _retest_blockers (empty substrate_queue) and the testability gate (a
    plain candidate claim, no epistemic_category) would both otherwise say
    `ready` -- the exact INV-089 shape."""

    def setUp(self):
        self._tmpdir = tempfile.TemporaryDirectory()
        tmp = Path(self._tmpdir.name)

        self._orig_claims_yaml = GEN.CLAIMS_YAML
        self._orig_substrate_queue = GEN.SUBSTRATE_QUEUE
        self._orig_proposals_json = GEN.PROPOSALS_JSON
        self._orig_ree_v3_queue = GEN.REE_V3_QUEUE

        GEN.CLAIMS_YAML = tmp / "claims.yaml"
        GEN.SUBSTRATE_QUEUE = tmp / "substrate_queue.json"
        GEN.PROPOSALS_JSON = tmp / "experiment_proposals.v1.json"
        GEN.REE_V3_QUEUE = tmp / "experiment_queue.json"

        # Empty substrate_queue -- _retest_blockers() must find nothing.
        GEN.SUBSTRATE_QUEUE.write_text(json.dumps({"queue": []}), encoding="utf-8")
        # Empty ree-v3 queue -- no claimed/queued coverage to absorb the retest.
        GEN.REE_V3_QUEUE.write_text(json.dumps({"items": []}), encoding="utf-8")

    def tearDown(self):
        GEN.CLAIMS_YAML = self._orig_claims_yaml
        GEN.SUBSTRATE_QUEUE = self._orig_substrate_queue
        GEN.PROPOSALS_JSON = self._orig_proposals_json
        GEN.REE_V3_QUEUE = self._orig_ree_v3_queue
        self._tmpdir.cleanup()

    def _write_claims_yaml(self, claim_id, extra_lines=""):
        GEN.CLAIMS_YAML.write_text(
            f"- id: {claim_id}\n"
            f"  status: candidate\n"
            f"  pending_retest_after_substrate: true\n"
            f"{extra_lines}",
            encoding="utf-8",
        )

    def _write_proposals(self, items):
        GEN.PROPOSALS_JSON.write_text(
            json.dumps({"schema_version": "experiment_proposals/v1", "items": items}),
            encoding="utf-8",
        )

    def _retest_item(self, data, claim_id):
        for it in data["items"]:
            if it.get("title") == f"Retest after substrate: {claim_id}":
                return it
        return None

    def test_blocked_substrate_proposal_forces_blocked_despite_no_substrate_blockers(self):
        claim_id = "TEST-RETEST-INV089-SHAPE"
        self._write_claims_yaml(claim_id)
        self._write_proposals([
            {
                "proposal_id": "EXP-TEST-INV089",
                "backlog_id": "EVB-TEST-0445",
                "claim_id": claim_id,
                "status": "blocked_substrate",
                "blocked_by": ["MECH-999", "INV-999"],
            }
        ])

        data = GEN.build_workset()
        item = self._retest_item(data, claim_id)
        self.assertIsNotNone(item, "expected a 'Retest after substrate' IGW item")
        self.assertEqual(item["status"], "blocked")
        self.assertTrue(
            any("blocked_substrate" in b and "MECH-999" in b for b in item["blocked_by"]),
            item["blocked_by"],
        )

    def test_without_blocked_substrate_proposal_same_claim_renders_ready(self):
        """Control: with everything else identical but no blocked_substrate
        proposal, the same claim shape renders `ready` -- proving the block
        above comes from the new check, not from some other gate."""
        claim_id = "TEST-RETEST-CONTROL-READY"
        self._write_claims_yaml(claim_id)
        self._write_proposals([])  # no backing proposal at all

        data = GEN.build_workset()
        item = self._retest_item(data, claim_id)
        self.assertIsNotNone(item)
        self.assertEqual(item["status"], "ready")

    def test_plain_proposed_status_does_not_force_blocked(self):
        claim_id = "TEST-RETEST-STILL-PROPOSED"
        self._write_claims_yaml(claim_id)
        self._write_proposals([
            {"proposal_id": "EXP-TEST-STILL-PROPOSED", "claim_id": claim_id, "status": "proposed"},
        ])

        data = GEN.build_workset()
        item = self._retest_item(data, claim_id)
        self.assertIsNotNone(item)
        self.assertEqual(item["status"], "ready")


if __name__ == "__main__":
    unittest.main(verbosity=2)
