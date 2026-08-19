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


class QuestionRollupSupersededTests(unittest.TestCase):
    """Regression test for the `superseded` state (added 2026-08-19 alongside the
    registry vocabulary itself, chip-20260819-hypothesis-registry-superseded-state).

    Before this state existed, a leg written with the literal (but unrecognised)
    string "superseded" fell through _question_rollup's alive/resolved_out/confirmed
    if/elif chain uncounted -- silently missing from every aggregate (the exact
    6-legs/5-accounted bug the motivating autopsy describes; see
    evidence/planning/failure_autopsy_mech321-hypothesis-legs-modeb_2026-08-18.md
    section 3). This test pins that `superseded` is now counted, and specifically
    that it is counted OUT of `surviving` -- the same direction as an elimination,
    but via a SEPARATE `superseded` tally rather than folding into `resolved_out`
    (RESOLVED_OUT_STATES stays disjoint from SUPERSEDED_STATES; see the sibling
    check_hypothesis_space_integrity.py's elimination-bar check for why)."""

    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module("ree_build_hypothesis_space", "build_hypothesis_space.py")

    def test_superseded_count_tallies_superseded_state_only(self):
        q = {
            "qid": "q1",
            "initial_frozen_count": 4,
            "hypotheses": [
                _hyp("h1", "alive"),
                _hyp("h2", "superseded"),
                _hyp("h3", "confirmed"),
                _hyp("h4", "eliminated"),
            ],
        }
        rollup = self.mod._question_rollup(q)
        self.assertEqual(rollup["superseded"], 1)
        self.assertEqual(rollup["alive"], 1)
        self.assertEqual(rollup["confirmed"], 1)
        self.assertEqual(rollup["resolved_out"], 1)

    def test_superseded_leg_not_silently_uncounted(self):
        """The exact motivating bug: a 6-leg question with one superseded leg must
        have all 6 legs land in alive+resolved_out+confirmed+superseded, not 5."""
        q = {
            "qid": "policy_decomposition_discrimination", "initial_frozen_count": 6,
            "hypotheses": [
                _hyp("h1", "alive"), _hyp("h2", "alive"), _hyp("h3", "alive"),
                _hyp("h4", "alive"), _hyp("h5", "confirmed"),
                _hyp("h6", "superseded"),
            ],
        }
        rollup = self.mod._question_rollup(q)
        accounted = rollup["alive"] + rollup["resolved_out"] + rollup["confirmed"] + rollup["superseded"]
        self.assertEqual(accounted, 6)
        self.assertEqual(rollup["surviving"], 4)  # the ratified reading, not 5

    def test_alive_to_superseded_transition_drops_surviving_with_no_elimination(self):
        """Mirrors test_alive_to_confirmed_transition_drops_surviving_with_no_elimination:
        a sibling alive leg going superseded drops `surviving` by 1 with resolved_out
        completely unchanged -- this is exactly the shape build_hypothesis_space.py
        needs check_hypothesis_space_integrity.py's total_superseded credit for."""
        before = {
            "qid": "q2", "initial_frozen_count": 2,
            "hypotheses": [_hyp("h1", "alive"), _hyp("h2", "alive")],
        }
        after = {
            "qid": "q2", "initial_frozen_count": 2,
            "hypotheses": [_hyp("h1", "alive"), _hyp("h2", "superseded")],
        }
        r_before = self.mod._question_rollup(before)
        r_after = self.mod._question_rollup(after)
        self.assertEqual(r_before["surviving"], 2)
        self.assertEqual(r_after["surviving"], 1)  # dropped...
        self.assertEqual(r_before["resolved_out"], r_after["resolved_out"])  # ...with NO elimination
        self.assertEqual(r_after["superseded"] - r_before["superseded"], 1)

    def test_all_resolved_fallback_excludes_superseded_from_surviving(self):
        """When alive == 0, surviving falls back to
        initial - resolved_out - confirmed - superseded. A question fully resolved
        via one eliminated leg and one superseded leg must read 0 surviving, not 1
        (the superseded leg re-appearing as a phantom survivor)."""
        q = {
            "qid": "q3", "initial_frozen_count": 2,
            "hypotheses": [_hyp("h1", "eliminated"), _hyp("h2", "superseded")],
        }
        rollup = self.mod._question_rollup(q)
        self.assertEqual(rollup["alive"], 0)
        self.assertEqual(rollup["surviving"], 0)

    def test_total_superseded_sums_across_questions(self):
        questions = [
            {"qid": "q1", "initial_frozen_count": 2,
             "hypotheses": [_hyp("a1", "superseded"), _hyp("a2", "alive")]},
            {"qid": "q2", "initial_frozen_count": 3,
             "hypotheses": [_hyp("b1", "superseded"), _hyp("b2", "superseded"),
                             _hyp("b3", "eliminated")]},
        ]
        rollups = [self.mod._question_rollup(q) for q in questions]
        total_superseded = sum(r["superseded"] for r in rollups)
        self.assertEqual(total_superseded, 3)

    def test_family_closes_via_superseded_leg(self):
        """axis_family_convergence must mark a family CLOSED when its only leg is
        superseded -- the second required behaviour from the chip prompt ("ALLOWS
        family closure"), and the reason RESOLVED_OUT_STATES/SUPERSEDED_STATES are
        both consulted in the `closed` test (not just in the alive/surviving tally)."""
        families = {"map": {"environment": "world", "policy": "process"}}
        q = {
            "qid": "policy_decomposition_discrimination",
            "hypotheses": [
                {"hid": "h_env", "axis": "environment",
                 "resolution": {"state": "superseded"}},
                {"hid": "h_policy", "axis": "policy",
                 "resolution": {"state": "alive"}},
            ],
        }
        conv = self.mod.axis_family_convergence(q, families)
        self.assertIn("world", conv["families_closed"])
        self.assertNotIn("process", conv["families_closed"])

    def test_family_does_not_close_via_bare_alive_superseded_mix(self):
        """Negative control: a family with one alive and one superseded leg is
        NOT closed -- closure requires EVERY leg in the family to be out
        (superseded/resolved_out) or confirmed."""
        families = {"map": {"environment": "world"}}
        q = {
            "qid": "q1",
            "hypotheses": [
                {"hid": "h1", "axis": "environment",
                 "resolution": {"state": "superseded"}},
                {"hid": "h2", "axis": "environment",
                 "resolution": {"state": "alive"}},
            ],
        }
        conv = self.mod.axis_family_convergence(q, families)
        self.assertNotIn("world", conv["families_closed"])


if __name__ == "__main__":
    unittest.main()
