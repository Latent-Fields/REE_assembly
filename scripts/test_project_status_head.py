#!/usr/bin/env python3
"""Regression test for project_status_head.py's autopsy-status filter.

Confirmed 2026-09-15: status_plane_drift() (check_closure_drift.py, SHP-2)
re-projects every collapsed closure-plan node's `live:` head via
project_status_head.build_projections(), which is fed by
project_status_head.load_autopsies(). That loader read every
failure_autopsy_*.json under evidence/** regardless of the artifact's own
top-level `status` field -- including a staging draft still
`awaiting_human_confirmation` (written mid-cycle by the autopsy-staging
tick, before a human ratifies it). failure_autopsy_V3-EXQ-1012a_2026-09-14
was exactly such a draft on 2026-09-15, and because it was the newest event
touching 69 of 99 collapsed nodes (arc_062_rule_apprehension GAP-A..GAP-L,
behavioral_diversity_isolation GAP-A, etc.), it became the projected `live:`
head for all of them -- an unratified finding driving governance state.

check_closure_drift.py's OWN terminal-owner path (collect_confirmed_autopsies())
already filters on CONFIRMED_AUTOPSY_STATUSES = {"confirmed", "complete",
"completed"}; the projection path did not honour the same filter. This test
pins that project_status_head.load_autopsies() now excludes any
failure_autopsy_*.json whose `status` is not in CONFIRMED_AUTOPSY_STATUSES
(and mirrors the set value itself, so the two modules cannot silently
diverge again).

Run: /opt/local/bin/python3 -m pytest scripts/test_project_status_head.py -q
"""

import importlib.util
import json
import os
import sys
import tempfile
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


def _write_autopsy(planning_dir, name, status, qid="V3-EXQ-9999", claim_ids=None,
                    routing="governance", generated_utc="2026-09-15T00:00:00Z"):
    payload = {
        "generated_utc": generated_utc,
        "status": status,
        "targets": [
            {
                "queue_id": qid,
                "claim_ids": claim_ids or ["MECH-999"],
                "bears_on": [],
                "routing": routing,
                "recommended_evidence_direction": "supports",
                "recommended_epistemic_category": None,
            }
        ],
    }
    (planning_dir / name).write_text(json.dumps(payload), encoding="utf-8")


class LoadAutopsiesConfirmedStatusFilterTest(unittest.TestCase):
    """load_autopsies() must only emit events for ratified autopsies."""

    @classmethod
    def setUpClass(cls):
        cls.PSH = _load_module("ree_project_status_head_confirmed_status_test",
                                "project_status_head.py")

    def test_confirmed_autopsy_statuses_matches_check_closure_drift(self):
        """The two modules must define the identical set -- check_closure_drift.py
        cannot import project_status_head's constant back without a circular
        import, so this pins them from drifting apart independently."""
        ccd = _load_module("ree_check_closure_drift_confirmed_status_test",
                            "check_closure_drift.py")
        self.assertEqual(self.PSH.CONFIRMED_AUTOPSY_STATUSES,
                          ccd.CONFIRMED_AUTOPSY_STATUSES)

    def test_unconfirmed_draft_never_becomes_an_event(self):
        with tempfile.TemporaryDirectory() as td:
            repo_root = Path(td)
            planning_dir = repo_root / "evidence" / "planning"
            planning_dir.mkdir(parents=True)
            _write_autopsy(planning_dir, "failure_autopsy_V3-EXQ-1012a_2026-09-14.json",
                            status="awaiting_human_confirmation", qid="V3-EXQ-1012a")
            _write_autopsy(planning_dir, "failure_autopsy_V3-EXQ-0001_2026-09-14.json",
                            status="confirmed", qid="V3-EXQ-0001")

            events = self.PSH.load_autopsies(str(repo_root))
            qids = {e.queue_id for e in events}

        self.assertIn("V3-EXQ-0001", qids)
        self.assertNotIn("V3-EXQ-1012a", qids)
        self.assertEqual(len(events), 1)

    def test_confirmed_status_variants_all_pass(self):
        with tempfile.TemporaryDirectory() as td:
            repo_root = Path(td)
            planning_dir = repo_root / "evidence" / "planning"
            planning_dir.mkdir(parents=True)
            for i, status in enumerate(("confirmed", "complete", "completed",
                                         "Confirmed", "  CONFIRMED  ")):
                _write_autopsy(planning_dir, f"failure_autopsy_V3-EXQ-200{i}_2026-09-14.json",
                               status=status, qid=f"V3-EXQ-200{i}")

            events = self.PSH.load_autopsies(str(repo_root))

        self.assertEqual(len(events), 5)

    def test_missing_or_other_status_excluded(self):
        with tempfile.TemporaryDirectory() as td:
            repo_root = Path(td)
            planning_dir = repo_root / "evidence" / "planning"
            planning_dir.mkdir(parents=True)
            # No `status` key at all (older-format autopsy artifacts).
            payload = {
                "generated_utc": "2026-09-15T00:00:00Z",
                "targets": [{"queue_id": "V3-EXQ-3001", "claim_ids": ["MECH-999"],
                              "bears_on": [], "routing": "governance",
                              "recommended_evidence_direction": "supports"}],
            }
            (planning_dir / "failure_autopsy_V3-EXQ-3001_2026-09-14.json").write_text(
                json.dumps(payload), encoding="utf-8")
            _write_autopsy(planning_dir, "failure_autopsy_V3-EXQ-3002_2026-09-14.json",
                            status="applied", qid="V3-EXQ-3002")
            _write_autopsy(planning_dir, "failure_autopsy_V3-EXQ-3003_2026-09-14.json",
                            status="resolved", qid="V3-EXQ-3003")

            events = self.PSH.load_autopsies(str(repo_root))

        self.assertEqual(events, [])


if __name__ == "__main__":
    unittest.main()
