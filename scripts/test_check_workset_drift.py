#!/usr/bin/env python3
"""Regression test for check_workset_drift.py's proposal-item title regex.

Confirmed 2026-08-02: _PROPOSAL_TITLE_RE was written for the OLD title format
"Proposal EXP-0199 (ARC-050)" (proposal_id + claim_id in parens) and was never
updated when generate_inter_governance_workset.py switched to claim-keyed
titles -- "Proposal for <claim_id>" (commit 0e409601fd) and, for the
literature-review lane, "Literature proposal for <claim_id>" (commit
478ba069c5). The old regex never matched either current format, so every
ready proposal item silently fell through to the generic owner_exq-only
check at the bottom of check(), skipping the claim-status /
epistemic-category / experimental-evidence-already-exists validations the
proposal branch exists to do. Confirmed live: re-running check_workset_drift
after the fix surfaced 2 real stale-proposal findings
(IGW-20260802-219/EXP-0342/MECH-166, IGW-20260802-221/EXP-0361/MECH-025b)
that the old regex was silently missing.

Run: /opt/local/bin/python3 scripts/test_check_workset_drift.py
"""

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent


def _load_module(name, filename):
    path = SCRIPTS_DIR / filename
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


class ProposalTitleRegexTest(unittest.TestCase):
    """_PROPOSAL_TITLE_RE must match the CURRENT claim-keyed title formats
    emitted by generate_inter_governance_workset._proposal_title(), and must
    NOT match any other item title shape that also appears in a ready
    workset (those are handled by earlier branches in check())."""

    @classmethod
    def setUpClass(cls):
        cls.CWD = _load_module("ree_check_workset_drift_regex_test", "check_workset_drift.py")

    def test_matches_experiment_lane_title(self):
        m = self.CWD._PROPOSAL_TITLE_RE.match("Proposal for Q-088")
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "Q-088")

    def test_matches_lit_lane_title(self):
        m = self.CWD._PROPOSAL_TITLE_RE.match("Literature proposal for Q-088")
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "Q-088")

    def test_matches_unclaimed_experiment(self):
        m = self.CWD._PROPOSAL_TITLE_RE.match("Proposal (unclaimed)")
        self.assertIsNotNone(m)
        self.assertIsNone(m.group(1))

    def test_matches_unclaimed_lit(self):
        m = self.CWD._PROPOSAL_TITLE_RE.match("Literature proposal (unclaimed)")
        self.assertIsNotNone(m)
        self.assertIsNone(m.group(1))

    def test_does_not_match_other_item_titles(self):
        non_proposal_titles = [
            "Retest after substrate: Q-088",
            "Diagnose ERROR: V3-EXQ-1",
            "Implement substrate: SD-001 (unblocks Q-088)",
            "Substrate ready: SD-001",
            "Confirm evidence: Q-088 (lit 0.60, exp ~0)",
            "Governance decision: Q-088",
            "Held pending substrate: Q-088",
        ]
        for title in non_proposal_titles:
            with self.subTest(title=title):
                self.assertIsNone(self.CWD._PROPOSAL_TITLE_RE.match(title))

    def test_old_title_format_no_longer_matches(self):
        # This is the bug itself: the OLD (proposal_id + claim_id-in-parens)
        # shape must not match, so a future format drift can't be masked the
        # same way this one was.
        self.assertIsNone(self.CWD._PROPOSAL_TITLE_RE.match("Proposal EXP-0199 (ARC-050)"))


class ProposalBranchIntegrationTest(unittest.TestCase):
    """check() must actually route a current-format ready proposal item
    through the proposal-specific validation, not the generic owner_exq
    fallback -- i.e. it must flag a proposal whose claim already has
    experimental evidence, and dedupe on repeated proposal_ids."""

    @classmethod
    def setUpClass(cls):
        cls.CWD = _load_module("ree_check_workset_drift_integration_test", "check_workset_drift.py")

    def setUp(self):
        cwd, g = self.CWD, self.CWD.g
        self._orig = {
            "_load_workset": cwd._load_workset,
            "g._substrate_by_id": g._substrate_by_id,
            "g._load_claims_meta": g._load_claims_meta,
            "g._load_queue": g._load_queue,
            "g._queued_retest_coverage": g._queued_retest_coverage,
            "g._claims_with_experimental_evidence": g._claims_with_experimental_evidence,
        }

    def tearDown(self):
        cwd, g = self.CWD, self.CWD.g
        cwd._load_workset = self._orig["_load_workset"]
        g._substrate_by_id = self._orig["g._substrate_by_id"]
        g._load_claims_meta = self._orig["g._load_claims_meta"]
        g._load_queue = self._orig["g._load_queue"]
        g._queued_retest_coverage = self._orig["g._queued_retest_coverage"]
        g._claims_with_experimental_evidence = self._orig["g._claims_with_experimental_evidence"]

    def _stub(self, claims_meta, exp_evidence):
        cwd, g = self.CWD, self.CWD.g
        g._substrate_by_id = lambda: {}
        g._load_claims_meta = lambda: claims_meta
        g._load_queue = lambda: []
        g._queued_retest_coverage = lambda queue_items: {}
        g._claims_with_experimental_evidence = lambda: exp_evidence

    def test_proposal_with_existing_evidence_is_flagged(self):
        claim_id = "TEST-DRIFT-001"
        workset = {
            "items": [
                {
                    "id": "IGW-TEST-1",
                    "status": "ready",
                    "lane": "experiment",
                    "title": f"Proposal for {claim_id}",
                    "claim_ids": [claim_id],
                    "owner_proposal_id": "EXP-TEST-1",
                },
            ]
        }
        self.CWD._load_workset = lambda: workset
        self._stub(
            claims_meta={claim_id: {"status": "candidate", "epistemic_category": "standard"}},
            exp_evidence={claim_id},
        )

        findings = self.CWD.check()
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["item_id"], "IGW-TEST-1")
        self.assertIn("already has experimental evidence", findings[0]["reason"])

    def test_proposal_with_no_drift_is_clean(self):
        claim_id = "TEST-DRIFT-002"
        workset = {
            "items": [
                {
                    "id": "IGW-TEST-2",
                    "status": "ready",
                    "lane": "lit",
                    "title": f"Literature proposal for {claim_id}",
                    "claim_ids": [claim_id],
                    "owner_proposal_id": "LIT-TEST-2",
                },
            ]
        }
        self.CWD._load_workset = lambda: workset
        self._stub(
            claims_meta={claim_id: {"status": "candidate", "epistemic_category": "standard"}},
            exp_evidence=set(),
        )

        self.assertEqual(self.CWD.check(), [])

    def test_duplicate_proposal_id_flagged(self):
        claim_id = "TEST-DRIFT-003"
        workset = {
            "items": [
                {
                    "id": "IGW-TEST-3a",
                    "status": "ready",
                    "lane": "experiment",
                    "title": f"Proposal for {claim_id}",
                    "claim_ids": [claim_id],
                    "owner_proposal_id": "EXP-TEST-DUP",
                },
                {
                    "id": "IGW-TEST-3b",
                    "status": "ready",
                    "lane": "experiment",
                    "title": f"Proposal for {claim_id}",
                    "claim_ids": [claim_id],
                    "owner_proposal_id": "EXP-TEST-DUP",
                },
            ]
        }
        self.CWD._load_workset = lambda: workset
        self._stub(
            claims_meta={claim_id: {"status": "candidate", "epistemic_category": "standard"}},
            exp_evidence=set(),
        )

        findings = self.CWD.check()
        self.assertEqual(len(findings), 1)
        self.assertIn("duplicate proposal_id", findings[0]["reason"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
