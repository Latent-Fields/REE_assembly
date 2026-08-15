#!/usr/bin/env python3
"""Tests for `backfill_failure_record_run_role.py` -- the FM11d schema backfill.

Time-independent (no `now()` anywhere in the module under test) and fixture-driven,
plus a handful of assertions against the live committed corpus that go red if the
backfill is ever partially reverted or if a new failure_record item lands unmarked.

Roughly half are NEGATIVE CONTROLS, and they are the load-bearing half: the
classifier is heuristic on the free-text path, so what stops a later session widening
it until it mislabels a gap-characterisation run as `post_build` is a test that says
"this must NOT be read as a landing".

    python3 -m pytest scripts/test_backfill_failure_record_run_role.py -q
"""

from __future__ import annotations

import json
import os
import sys
import unittest
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import backfill_failure_record_run_role as B  # noqa: E402
import generate_inter_governance_workset as G  # noqa: E402

QUEUE_PATH = B.QUEUE_PATH


def _utc(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def _rec(stamp: str, **kw) -> dict:
    return dict({"run_id": f"v3_exq_000_thing_{stamp}_v3"}, **kw)


class ParseTsTest(unittest.TestCase):
    def test_iso_z(self):
        self.assertEqual(_utc("2026-08-04T07:15:41Z"),
                         B.parse_ts("2026-08-04T07:15:41Z"))

    def test_run_stamp(self):
        self.assertEqual(_utc("2026-08-04T07:15:41Z"),
                         B.parse_ts("v3_exq_436d_x_20260804T071541Z_v3"))

    def test_bare_date_is_midnight_utc(self):
        """Accepted HERE but not by the generator's parser -- a bare date is a
        usable landing bound for a pre/post split, and is why `same_day` items are
        flagged for audit."""
        self.assertEqual(_utc("2026-07-07T00:00:00Z"), B.parse_ts("2026-07-07"))

    def test_unparseable_is_none_never_epoch(self):
        for bad in ("", None, "junk", "2026-13-45", 17, {}, []):
            self.assertIsNone(B.parse_ts(bad), repr(bad))


class ClassifyTest(unittest.TestCase):
    """R1..R5, each in isolation."""

    def test_R1_item_substrate_built_utc_overrides_the_entry(self):
        """The phased-build case, and the live worked example: SD-035's
        v3_exq_894a POSTDATES the 2026-04-21 BLA/CeA landing but PREDATES the
        2026-08-09 trainable-attribution-head build it motivated."""
        entry = {"implemented_utc": "2026-04-21T00:00:00Z"}
        rec = _rec("20260808T101157Z", substrate_built_utc="2026-08-09T07:45:00Z")
        role, basis = B.classify(entry, rec)
        self.assertEqual(B.RUN_ROLE_PRE, role)
        self.assertIn("R1", basis)

    def test_R1_can_also_yield_post_build(self):
        entry = {"implemented_utc": "2026-04-21T00:00:00Z"}
        rec = _rec("20260810T000000Z", substrate_built_utc="2026-08-09T07:45:00Z")
        self.assertEqual(B.RUN_ROLE_POST, B.classify(entry, rec)[0])

    def test_R2_undatable_run_id_is_unknown(self):
        entry = {"implemented_utc": "2026-04-21T00:00:00Z"}
        role, basis = B.classify(entry, {"run_id": "v3_exq_085 cluster (085a..085g)"})
        self.assertEqual(B.RUN_ROLE_UNKNOWN, role)
        self.assertIn("R2", basis)

    def test_R3_run_before_the_landing_is_pre_build(self):
        entry = {"implemented_utc": "2026-04-21T00:00:00Z"}
        self.assertEqual(B.RUN_ROLE_PRE,
                         B.classify(entry, _rec("20260408T231126Z"))[0])

    def test_R3_run_after_the_landing_is_post_build(self):
        entry = {"implemented_utc": "2026-04-21T00:00:00Z"}
        self.assertEqual(B.RUN_ROLE_POST,
                         B.classify(entry, _rec("20260508T135638Z"))[0])

    def test_R4_an_entry_with_no_build_can_have_no_post_build_run(self):
        entry = {"status": "proposed_GATED_on_autopsy_DO_NOT_BUILD_YET"}
        role, basis = B.classify(entry, _rec("20260727T170539Z"))
        self.assertEqual(B.RUN_ROLE_PRE, role)
        self.assertIn("R4", basis)

    def test_R5_landed_but_undatable_is_unknown_not_a_guess(self):
        entry = {"status": "implemented"}
        role, basis = B.classify(entry, _rec("20260727T170539Z"))
        self.assertEqual(B.RUN_ROLE_UNKNOWN, role)
        self.assertIn("R5", basis)

    def test_same_day_post_build_is_flagged_for_audit(self):
        entry = {"implemented_utc": "2026-04-25"}
        role, basis = B.classify(entry, _rec("20260425T141932Z"))
        self.assertEqual(B.RUN_ROLE_POST, role)
        self.assertIn("same_day", basis,
                      "a bare landing date is read as 00:00Z, so a same-day run "
                      "comes out post_build on 24h of slack -- say so")


class EarliestLandingTest(unittest.TestCase):
    """R3 answers "when did this substrate FIRST exist", not "most recently"."""

    def test_a_later_amend_date_does_not_move_the_landing(self):
        """THE REGRESSION THIS POLICY EXISTS FOR.

        Taking the LATEST date read MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION as
        landing 2026-08-14 (a bug-fix note) when its own implementation_note opens
        "IMPLEMENTED 2026-08-02" -- which relabelled the 861a validation run
        `pre_build`, erased ARC-045's cutoff, and with it the coverage by
        v3_exq_436d that is the confirmed FM11 incident.
        """
        entry = {
            "implementation_note": "IMPLEMENTED 2026-08-02 (/implement-substrate). "
                                   "Novelty-reference bug FIXED 2026-08-14.",
        }
        when, _basis = B.entry_landing(entry)
        self.assertEqual(_utc("2026-08-02T00:00:00Z"), when)
        self.assertEqual(B.RUN_ROLE_POST,
                         B.classify(entry, _rec("20260802T215005Z"))[0])

    def test_earliest_wins_across_structured_and_freetext_sources(self):
        entry = {"validated_utc": "2026-07-30",
                 "implementation_note": "LANDED 2026-07-21 (ree-v3 909292c)."}
        when, basis = B.entry_landing(entry)
        self.assertEqual(_utc("2026-07-21T00:00:00Z"), when)
        self.assertIn("freetext", basis)

    def test_nested_implementation_log_stamps_are_found(self):
        entry = {"implementation_log": [{"utc": "2026-06-12T23:26:37Z"}]}
        when, basis = B.entry_landing(entry)
        self.assertEqual(_utc("2026-06-12T23:26:37Z"), when)
        self.assertIn("implementation_log", basis)


class FreetextIsNarrowTest(unittest.TestCase):
    """NEGATIVE CONTROLS on the one heuristic that could invent a landing.

    Every phrase here is real substrate_queue prose. If a later session widens
    `_FREETEXT_LANDING_RE` until one of these parses as a landing, gap runs start
    being labelled `post_build` and the cutoff drifts LATER -- back to the FM11
    re-staging pathology.
    """

    def _is_landing(self, text: str) -> bool:
        return B.entry_landing({"implementation_note": text})[0] is not None

    def test_queued_is_not_a_landing(self):
        self.assertFalse(self._is_landing("V3-EXQ-514j queued 2026-05-20"))

    def test_a_bare_date_alone_is_not_a_landing(self):
        self.assertFalse(self._is_landing("governance-cycle 2026-05-10, see notes"))

    def test_a_gated_proposal_is_not_a_landing(self):
        self.assertFalse(self._is_landing(
            "proposed 2026-08-08, GATED on the V3-EXQ-829 autopsy -- DO NOT BUILD"))

    def test_the_date_must_be_near_the_landing_verb(self):
        self.assertFalse(self._is_landing(
            "IMPLEMENTED -- see the design doc, the runner notes, the autopsy "
            "index, and the surrounding governance discussion for 2026-05-03"))

    def test_an_explicit_landing_phrase_IS_accepted(self):
        """Positive control, so the four above cannot pass by the regex being
        broken outright."""
        self.assertTrue(self._is_landing("IMPLEMENTED 2026-05-03 in ree_core/."))


class BackfillIsIdempotentTest(unittest.TestCase):
    def test_running_twice_changes_nothing(self):
        doc = {"queue": [{"sd_id": "X", "implemented_utc": "2026-04-21T00:00:00Z",
                          "failure_record": [_rec("20260508T135638Z")]}]}
        first, _c, _r = B.backfill(doc)
        self.assertEqual(1, first)
        second, _c, _r = B.backfill(doc)
        self.assertEqual(0, second, "a re-run must be a no-op")

    def test_malformed_failure_record_rows_are_skipped_not_fatal(self):
        doc = {"queue": [{"sd_id": "X", "failure_record": [None, "s", 3]},
                         {"sd_id": "Y", "failure_record": None},
                         {"sd_id": "Z"}]}
        changed, counts, rows = B.backfill(doc)
        self.assertEqual((0, []), (changed, rows))
        self.assertEqual(0, sum(counts.values()))


class LiveCorpusTest(unittest.TestCase):
    """Against the committed `substrate_queue.json`."""

    @classmethod
    def setUpClass(cls):
        with open(QUEUE_PATH, encoding="utf-8") as fh:
            cls.raw = fh.read()
        cls.doc = json.loads(cls.raw)
        cls.items = [r for e in cls.doc["queue"]
                     for r in (e.get("failure_record") or []) if isinstance(r, dict)]

    def test_every_failure_record_item_is_marked(self):
        """Goes red when a new failure_record item lands unmarked. That is not a
        correctness failure -- unmarked reads as `unknown` and is inert -- but it
        silently costs that entry its landing bound, so it should be noticed."""
        unmarked = [r.get("run_id") for r in self.items if not r.get("run_role")]
        self.assertEqual(
            [], unmarked,
            "unmarked failure_record item(s); re-run "
            "`python3 scripts/backfill_failure_record_run_role.py --apply`",
        )

    def test_every_value_is_in_the_allowed_set(self):
        allowed = {B.RUN_ROLE_PRE, B.RUN_ROLE_POST, B.RUN_ROLE_UNKNOWN}
        self.assertEqual(set(), {r["run_role"] for r in self.items} - allowed)

    def test_every_marked_item_records_how_it_was_derived(self):
        self.assertEqual([], [r.get("run_id") for r in self.items
                              if not r.get("run_role_basis")])

    def test_the_backfill_is_stable_on_the_committed_corpus(self):
        """Re-deriving from the committed file must reproduce it exactly -- if it
        does not, the committed labels were hand-edited or the classifier moved."""
        changed, _counts, _rows = B.backfill(json.loads(self.raw))
        self.assertEqual(0, changed)

    def test_the_writer_round_trips_the_file_byte_identically(self):
        """`json.dump(doc, indent=2)` reproduces the committed bytes. Without this,
        `--apply` would re-serialise all 157 entries and bury the change."""
        self.assertEqual(self.raw, json.dumps(self.doc, indent=2) + "\n")

    def test_the_three_named_fm11_claims_are_covered_by_a_post_build_cutoff(self):
        """The live cases the fix was approved for: MECH-074d
        (SD-035.failure_record == v3_exq_894c), MECH-151 and MECH-152 (both
        SD-016.failure_record == v3_exq_922). Each rendered `ready` before FM11d
        because its own newest evidence defined the cutoff and was then excluded."""
        substrate = G._substrate_by_id()
        for claim in ("MECH-074d", "MECH-151", "MECH-152"):
            cover = G._completed_retest_coverage(claim, substrate)
            self.assertIsNotNone(cover, f"{claim}: self-cancelling cutoff is back")
            self.assertTrue(cover["cutoff_is_validation_run"], claim)
            self.assertEqual(
                cover["cutoff_utc"], cover["timestamp_utc"],
                f"{claim}: the covering run IS the cutoff-defining run -- that is "
                "the self-cancelling shape, and counting it is the fix",
            )
            self.assertIn("failure_record", cover["cutoff_source"], claim)

    def test_no_claim_is_dated_by_a_pre_build_run(self):
        """The whole point, asserted at the corpus level rather than per case."""
        substrate = G._substrate_by_id()
        stamps = {}
        for entry in substrate.values():
            for rec in entry.get("failure_record") or []:
                if not isinstance(rec, dict):
                    continue
                if G._failure_record_run_role(rec) == B.RUN_ROLE_POST:
                    continue
                when = G._parse_evidence_ts(rec.get("run_id"))
                if when is not None:
                    stamps.setdefault(entry.get("sd_id"), set()).add(when)
        claims = sorted({c for e in substrate.values()
                         for c in (e.get("unblocks_claims") or [])})
        for claim in claims:
            cutoff, source, is_run = G._substrate_landing_cutoff(claim, substrate)
            if cutoff is None or not is_run:
                continue
            sid = source.split(".")[0]
            self.assertNotIn(cutoff, stamps.get(sid, set()),
                             f"{claim}: cutoff came from a non-post_build stamp")


if __name__ == "__main__":
    unittest.main()
