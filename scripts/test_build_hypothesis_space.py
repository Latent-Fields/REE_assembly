#!/usr/bin/env python3
"""Regression test for build_hypothesis_space.py's total_confirmed aggregate.

Added 2026-08-02 alongside check_hypothesis_space_integrity.py's confirmed-drop
fix: a `confirmed` resolution legitimately removes a hypothesis from
`surviving` (per _question_rollup below, `surviving == alive` whenever
`alive > 0`), exactly like an elimination does for `resolved_out` -- but
nothing before this change tracked a `total_confirmed` aggregate the integrity
audit could credit against a surviving-count drop. Confirmed false positive
2026-08-02: H-zworld-trained-instrument moved alive -> confirmed via
V3-EXQ-819a, and the 2026-07-29 -> 2026-07-30 timeseries drop was flagged as
"unbacked" because only total_resolved_out was ever compared.

This test covers only the NEW aggregation (per-question `confirmed` count and
its sum into `total_confirmed`), not the whole _question_rollup surface.

Run: /opt/local/bin/python3 scripts/test_build_hypothesis_space.py
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
    spec.loader.exec_module(mod)
    return mod


def _hyp(hid, state, **extra):
    resolution = {"state": state}
    resolution.update(extra)
    return {"hid": hid, "resolution": resolution}


class QuestionRollupConfirmedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module("ree_build_hypothesis_space", "build_hypothesis_space.py")

    def test_confirmed_count_tallies_confirmed_state_only(self):
        q = {
            "qid": "q1",
            "initial_frozen_count": 4,
            "hypotheses": [
                _hyp("h1", "alive"),
                _hyp("h2", "confirmed"),
                _hyp("h3", "confirmed"),
                _hyp("h4", "eliminated"),
            ],
        }
        rollup = self.mod._question_rollup(q)
        self.assertEqual(rollup["confirmed"], 2)
        self.assertEqual(rollup["resolved_out"], 1)
        self.assertEqual(rollup["alive"], 1)

    def test_alive_to_confirmed_transition_drops_surviving_with_no_elimination(self):
        """The exact mechanism behind the confirmed 2026-08-02 false positive:
        a question with one OTHER alive leg sees `surviving` (== alive, per
        _question_rollup) drop by 1 when a sibling leg is confirmed, with
        resolved_out completely unchanged."""
        before = {
            "qid": "q2", "initial_frozen_count": 2,
            "hypotheses": [_hyp("h1", "alive"), _hyp("h2", "alive")],
        }
        after = {
            "qid": "q2", "initial_frozen_count": 2,
            "hypotheses": [_hyp("h1", "alive"), _hyp("h2", "confirmed")],
        }
        r_before = self.mod._question_rollup(before)
        r_after = self.mod._question_rollup(after)
        self.assertEqual(r_before["surviving"], 2)
        self.assertEqual(r_after["surviving"], 1)  # dropped...
        self.assertEqual(r_before["resolved_out"], r_after["resolved_out"])  # ...with NO elimination
        self.assertEqual(r_after["confirmed"] - r_before["confirmed"], 1)  # but total_confirmed rose

    def test_total_confirmed_sums_across_questions(self):
        questions = [
            {"qid": "q1", "initial_frozen_count": 2,
             "hypotheses": [_hyp("a1", "confirmed"), _hyp("a2", "alive")]},
            {"qid": "q2", "initial_frozen_count": 3,
             "hypotheses": [_hyp("b1", "confirmed"), _hyp("b2", "confirmed"),
                             _hyp("b3", "eliminated")]},
        ]
        rollups = [self.mod._question_rollup(q) for q in questions]
        total_confirmed = sum(r["confirmed"] for r in rollups)
        self.assertEqual(total_confirmed, 3)


if __name__ == "__main__":
    unittest.main()
