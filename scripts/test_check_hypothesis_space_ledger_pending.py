#!/usr/bin/env python3
"""Tests for check_hypothesis_space_integrity.py's `n_ledger_pending` scan.

Added 2026-09-03 with the scan itself. `/failure-autopsy` in staging mode drafts
its Step 9b edits into a `hypothesis_space_ledger_pending` block on the autopsy
artifact rather than writing the live registry -- and until this scan existed,
nothing applied those blocks and nothing checked that anything had. 34 confirmed
artifacts carried one, the oldest from 2026-07-19; the concrete failure was
V3-EXQ-980 adjudicating `H-readout-regime`, a leg V3-EXQ-976's block had drafted
but never registered.

The load-bearing case is `test_drafted_resolve_never_applied` -- the POSITIVE
control. Every other test here asserts the scan stays QUIET, and a scan that is
quiet because it is broken would pass all of them. That test is what
distinguishes "no gaps" from "no scan".

Run: /opt/local/bin/python3 scripts/test_check_hypothesis_space_ledger_pending.py
"""

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent


def _load_module(name, filename):
    path = SCRIPTS_DIR / filename
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


M = _load_module("_chsi_under_test", "check_hypothesis_space_integrity.py")


def _registry(state="alive"):
    """One question, one leg, whose resolution state the caller chooses."""
    return {"questions": [{
        "qid": "q_present",
        "initial_frozen_count": 1,
        "initial_frozen_count_at_registration": 1,
        "hypotheses": [{"hid": "H-present", "pre_registered_utc": "2026-08-01",
                        "resolution": {"state": state}}],
    }]}


class LedgerPendingScanTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def write(self, name, block, status="confirmed"):
        art = {"status": status, "hypothesis_space_ledger_pending": block}
        (self.dir / f"failure_autopsy_{name}.json").write_text(
            json.dumps(art), encoding="utf-8")

    def scan(self, registry=None):
        return M.scan_ledger_pending(registry or _registry(), planning_dir=self.dir)

    # ---- POSITIVE CONTROL: the scan must actually fire ---------------------
    def test_drafted_resolve_never_applied(self):
        """The 861f shape: `intended: {"<hid>": {"resolution": {...}}}`.

        The hid is a dict KEY here, not a value, so the ordinary hid-valued
        clauses never see it. This is the shape that sat unapplied for nine days.
        """
        self.write("case", {"qid": "q_present", "intended": {
            "H-present": {"resolution": {"state": "eliminated"}}}})
        msgs = self.scan()
        self.assertEqual(len(msgs), 1, msgs)
        self.assertIn("H-present", msgs[0])
        self.assertIn("eliminated", msgs[0])
        self.assertIn("alive", msgs[0])

    def test_hid_as_value_with_nested_resolution(self):
        """The 976/934 shape: a list of {hid, resolution:{state}} records."""
        self.write("case", {"mode_b_resolve": [
            {"qid": "q_present", "hid": "H-present",
             "resolution_patch": {"state": "confirmed"}}]})
        self.assertEqual(len(self.scan()), 1)

    def test_proposed_state_and_hypothesis_aliases(self):
        """The 436d shape uses `hypothesis`/`proposed_state`, not `hid`/`state`."""
        self.write("case", {"proposed_resolutions": [
            {"question": "q_present", "hypothesis": "H-absent",
             "proposed_state": "eliminated"}]})
        msgs = self.scan()
        self.assertEqual(len(msgs), 1, msgs)
        self.assertIn("H-absent", msgs[0])

    def test_missing_question_flagged(self):
        self.write("case", {"qid": "q_never_registered"})
        msgs = self.scan()
        self.assertEqual(len(msgs), 1, msgs)
        self.assertIn("q_never_registered", msgs[0])

    # ---- the scan must stay QUIET in these cases --------------------------
    def test_applied_block_is_quiet(self):
        self.write("case", {"qid": "q_present", "intended": {
            "H-present": {"resolution": {"state": "eliminated"}}}})
        self.assertEqual(self.scan(_registry("eliminated")), [])

    def test_supersession_direction_not_flagged(self):
        """Block drafted `alive`; a later autopsy confirmed the leg. Not a gap.

        The 816c-822 case: flagging a registry that has moved FURTHER than the
        draft would make the section fire on ordinary progress.
        """
        self.write("case", {"question_qid": "q_present",
                            "leg": {"hid": "H-present", "state": "alive"}})
        self.assertEqual(self.scan(_registry("confirmed")), [])

    def test_declined_alternative_is_pruned(self):
        """A block's `if_the_confirming_session_disagrees` is NOT an owed edit."""
        self.write("case", {"applicable": False, "if_the_confirming_session_disagrees": {
            "candidate_qid": "q_never_registered",
            "candidate_hypotheses": [{"hid": "H-absent",
                                      "proposed_resolution_state": "confirmed"}]}})
        self.assertEqual(self.scan(), [])

    def test_optional_sketch_and_cosmetic_pruned(self):
        self.write("sketch", {"recommended_action": "none",
                              "optional_new_question_sketch": {"qid": "q_never_registered"}})
        self.write("cosmetic", {"optional_cosmetic_corroboration": {
            "qid": "q_never_registered", "hid": "H-absent", "required": False}})
        self.assertEqual(self.scan(), [])

    def test_no_op_block_is_quiet(self):
        """The commonest shape: {action, reason} naming no question at all."""
        self.write("case", {"action": "deferred", "reason": "no qid names MECH-022"})
        self.assertEqual(self.scan(), [])

    def test_unconfirmed_artifact_not_owed(self):
        """A staging draft still at its own Step 8 gate is pending, not missing."""
        self.write("case", {"qid": "q_never_registered"},
                   status="awaiting_human_confirmation")
        self.assertEqual(self.scan(), [])

    def test_settled_markers_suppress(self):
        for marker in ("applied", "registry_written"):
            with self.subTest(marker=marker):
                self.setUp()
                self.write("case", {"qid": "q_never_registered", marker: True})
                self.assertEqual(self.scan(), [])
        for marker in ("applied_utc", "superseded_by"):
            with self.subTest(marker=marker):
                self.setUp()
                self.write("case", {"qid": "q_never_registered", marker: "2026-08-21T01:56:34Z"})
                self.assertEqual(self.scan(), [])

    def test_null_applied_utc_does_not_suppress(self):
        """`"applied_utc": null` asserts the OPPOSITE of applied -- truthiness matters.

        861f carried exactly this and would have been suppressed by a `in block`
        membership test rather than a truthiness one.
        """
        self.write("case", {"qid": "q_never_registered", "applied_utc": None})
        self.assertEqual(len(self.scan()), 1)

    def test_artifact_without_block_ignored(self):
        (self.dir / "failure_autopsy_none.json").write_text(
            json.dumps({"status": "confirmed"}), encoding="utf-8")
        (self.dir / "failure_autopsy_empty.json").write_text(
            json.dumps({"status": "confirmed",
                        "hypothesis_space_ledger_pending": {}}), encoding="utf-8")
        self.assertEqual(self.scan(), [])

    def test_unparseable_artifact_does_not_crash(self):
        (self.dir / "failure_autopsy_bad.json").write_text("{not json", encoding="utf-8")
        self.write("case", {"qid": "q_never_registered"})
        self.assertEqual(len(self.scan()), 1)

    # ---- the bucket is ADVISORY -------------------------------------------
    def test_bucket_is_advisory(self):
        """Must never be counted into the flag total -- this script gates nothing."""
        self.assertIn("n_ledger_pending", M.ADVISORY_BUCKETS)
        flags = {"a_unbacked_drop": [], "b_enlargement": [],
                 "c_confirmed_no_control": [], "d_bar_violation": [],
                 "n_ledger_pending": ["one", "two"]}
        total = sum(len(v) for k, v in flags.items() if k not in M.ADVISORY_BUCKETS)
        self.assertEqual(total, 0)

    def test_report_renders_both_ways(self):
        reg = _registry()
        for pend, expect in (([], "_No confirmed autopsy carries"),
                             (["`x.json`: question `q` absent"], "x.json")):
            flags = M.audit(reg, [])
            flags["n_ledger_pending"] = pend
            body = M.render_report(flags, reg, [], "2026-09-03T00:00:00Z")
            self.assertIn("drafted ledger edits not reflected", body)
            self.assertIn(expect, body)


if __name__ == "__main__":
    unittest.main(verbosity=2)
