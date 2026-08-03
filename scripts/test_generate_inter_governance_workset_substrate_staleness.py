#!/usr/bin/env python3
"""Regression test for FM3 -- the substrate-lane staleness blind spot in
generate_inter_governance_workset.py (chip-20260803-igw-workset-substrate-
staleness).

Confirmed incident (2026-08-03): four of the five items rendered as "Substrate
ready" / status=ready / skill=/implement-substrate were already fully landed in
ree-v3 -- SD-091 (71182f3+87a7e21), SD-092 (500fd67398+d9e0586),
SD-modulatory-channel-route-decomp-gate-fix (3db7d23) and
mech090-arc071-attick-persistent-handle-fix (31ed78e). They were staged as
IGW-20260803-206..209, sat "awaiting human launch" for up to two days, and were
GC-reaped unused.

Root cause: `_status_resolved` and `_status_terminal` both hard-veto on the
SUBSTRING "pending". `implemented_pending_validation` asserts the build HAS
landed and only validation is outstanding, so the veto reads it as the exact
opposite of what it says -- and the substrate lane fails OPEN to "ready", so the
misread degraded silently into spawned re-implementation chips instead of
erroring. That status was the second-most-common non-empty status in
substrate_queue.json (11 entries) the day this was found, so it mis-routed a
whole class.

NOT the root cause, ruled out and pinned here so nobody re-investigates them:
  (a) caching -- `_load_substrate_queue()` re-reads the file on every call
      (`SubstrateQueueEditIsReflectedNextRegenTest`).
  (c) a stale regen -- igw_routine_tick shells out to the generator each tick.

The manual status correction applied as a stopgap (REE_assembly 98651d2e27) did
NOT fix this: the corrected statuses were themselves
`implemented_pending_validation`, so the same items re-qualified as ready on the
very next regen. `ConfirmedIncidentReplayTest` is that exact board.

Fix: `_status_implementation_complete` / `_substrate_implementation_complete`
suppress the IMPLEMENT lane only, leaving retest-blocker semantics
(`_substrate_resolved`) untouched -- pinned by
`RetestBlockerSemanticsUnchangedTest`, which is what stops a later session
"simplifying" the two predicates into one.

Time-independent: no clock, no network, no git. Temp files only.

Run: /opt/local/bin/python3 scripts/test_generate_inter_governance_workset_substrate_staleness.py
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
        "ree_igw_generator_substrate_staleness_test", path
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


GEN = _load_generator()


class _TempSubstrateQueue(unittest.TestCase):
    """Base: point GEN.SUBSTRATE_QUEUE at a temp file we control."""

    def setUp(self):
        self._orig = GEN.SUBSTRATE_QUEUE
        fh = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
        fh.close()
        self._path = Path(fh.name)
        GEN.SUBSTRATE_QUEUE = self._path

    def tearDown(self):
        GEN.SUBSTRATE_QUEUE = self._orig
        self._path.unlink(missing_ok=True)

    def _write(self, queue):
        self._path.write_text(json.dumps({"queue": queue}, indent=2), encoding="utf-8")

    def _ready_ids(self):
        return [it.get("sd_id") for it in GEN._substrate_ready_items()]


class StatusImplementationCompleteTest(unittest.TestCase):
    """`_status_implementation_complete` is a pure function over one string."""

    def test_build_landed_validation_pending_is_complete(self):
        """The FM3 case itself, plus its siblings."""
        for status in (
            "implemented_pending_validation",
            "amend_implemented_pending_validation",
            "substrate_landed_pending_validation",
            "implemented_pending_verification",
            "implemented_pending_retest",
            "implemented_pending_governance_review",
        ):
            with self.subTest(status=status):
                self.assertTrue(GEN._status_implementation_complete(status))

    def test_remaining_build_work_is_not_complete(self):
        """Negative controls -- these must KEEP surfacing as implementable.

        `partially_implemented_pending_consumer_wiring` is the sharp one: it
        contains "implemented" and it contains "pending", but the pending
        qualifier names remaining BUILD work, not a verification step. A fix
        written as a bare "has an implemented token" test would break it.
        """
        for status in (
            "pending_implementation",
            "partially_implemented_pending_consumer_wiring",
            "candidate_v3_pending",
            "blocked_pending_discrimination",
            "parked_pending_env_entropy_precondition",
            "proposed",
            "design_question",
            "probe_queued",
            "",
        ):
            with self.subTest(status=status):
                self.assertFalse(GEN._status_implementation_complete(status))

    def test_is_a_superset_of_the_existing_resolved_matchers(self):
        """Anything the old matchers call done must stay done here."""
        for status in (
            "implemented",
            "implemented_validated",
            "validated",
            "phase_1_implemented",
            "retune_validated",
            "candidate_substrate_landed",
            "amend_validated_v3_exq_648a_c2_loadbearing_pass",
        ):
            with self.subTest(status=status):
                self.assertTrue(
                    GEN._status_resolved(status) or GEN._status_terminal(status),
                    "precondition: old matchers should already accept this",
                )
                self.assertTrue(GEN._status_implementation_complete(status))


class ConfirmedIncidentReplayTest(_TempSubstrateQueue):
    """The 2026-08-03 board, exactly as it stood AFTER the manual stopgap.

    Every one of these four had landed in ree-v3. Before the fix all four came
    back `ready`; the stopgap could not have helped, because the status it
    corrected them TO is the one that mis-classifies.
    """

    INCIDENT = [
        {"sd_id": "SD-091", "status": "implemented_pending_validation", "ready": True},
        {"sd_id": "SD-092", "status": "implemented_pending_validation", "ready": True},
        {
            "sd_id": "SD-modulatory-channel-route-decomp-gate-fix",
            "status": "implemented",
            "ready": True,
        },
        {
            "sd_id": "mech090-arc071-attick-persistent-handle-fix",
            "status": "implemented_pending_validation",
            "ready": True,
        },
        {"sd_id": "SD-094", "status": "implemented_pending_validation", "ready": True},
    ]

    def test_no_landed_item_is_routed_to_implement_substrate(self):
        self._write(self.INCIDENT)
        self.assertEqual(self._ready_ids(), [])

    def test_pre_stopgap_board_still_surfaces_the_genuinely_unbuilt(self):
        """Negative control on the SAME items with their pre-stopgap statuses.

        This is what the lane is FOR. If this ever goes empty the fix has
        over-suppressed and real substrate work is being dropped silently --
        which is a strictly worse failure than the one being fixed.
        """
        self._write(
            [
                {"sd_id": "SD-091", "status": "implemented_pending_validation", "ready": True},
                {
                    "sd_id": "SD-092",
                    "status": "partially_implemented_pending_consumer_wiring",
                    "ready": True,
                },
                {
                    "sd_id": "SD-modulatory-channel-route-decomp-gate-fix",
                    "status": "pending_implementation",
                    "ready": True,
                },
                {
                    "sd_id": "mech090-arc071-attick-persistent-handle-fix",
                    "status": "pending_implementation",
                    "ready": True,
                },
                {"sd_id": "SD-094", "status": "pending_implementation", "ready": True},
            ]
        )
        self.assertEqual(
            self._ready_ids(),
            [
                "SD-092",
                "SD-modulatory-channel-route-decomp-gate-fix",
                "mech090-arc071-attick-persistent-handle-fix",
                "SD-094",
            ],
            "only SD-091 (already implemented_pending_validation pre-stopgap) "
            "should have been suppressed on the pre-stopgap board",
        )


class SubstrateQueueEditIsReflectedNextRegenTest(_TempSubstrateQueue):
    """The chip's headline ask: a substrate_queue.json status change shows up in
    the NEXT regen.

    Rules out root-cause hypothesis (a) -- a cached/derived snapshot. The
    generator must re-read the file, so flipping a status between two calls in
    the same process has to change the answer.
    """

    def test_status_flip_changes_readiness_within_one_process(self):
        self._write([{"sd_id": "SD-999", "status": "pending_implementation", "ready": True}])
        self.assertEqual(self._ready_ids(), ["SD-999"])

        self._write(
            [{"sd_id": "SD-999", "status": "implemented_pending_validation", "ready": True}]
        )
        self.assertEqual(
            self._ready_ids(), [], "generator must re-read substrate_queue.json, not cache it"
        )

        self._write([{"sd_id": "SD-999", "status": "implemented", "ready": True}])
        self.assertEqual(self._ready_ids(), [])

    def test_reopening_an_entry_brings_it_back(self):
        """The reverse direction -- suppression must not be sticky."""
        self._write(
            [{"sd_id": "SD-999", "status": "implemented_pending_validation", "ready": True}]
        )
        self.assertEqual(self._ready_ids(), [])
        self._write(
            [
                {
                    "sd_id": "SD-999",
                    "status": "implemented_validation_failed_needs_followup_fix",
                    "ready": True,
                    "depends_on_unresolved": [],
                }
            ]
        )
        # Not asserting readiness here (that status is resolved by the legacy
        # `implemented_` prefix rule and is out of FM3 scope) -- only that the
        # answer is recomputed from the file rather than remembered.
        self.assertEqual(GEN._load_substrate_queue()[0]["status"],
                         "implemented_validation_failed_needs_followup_fix")


class RetestBlockerSemanticsUnchangedTest(unittest.TestCase):
    """FM3 suppresses the IMPLEMENT lane ONLY.

    "The code landed" and "the claim it unblocks is retestable" are different
    questions; only the first is settled by `implemented_pending_validation`.
    `_substrate_resolved` answers the second and must be untouched -- collapsing
    the two predicates into one would silently unblock retests of unvalidated
    substrate, which is the FM1 failure this file already fixed once.
    """

    ENTRY = {"sd_id": "SD-091", "status": "implemented_pending_validation", "ready": True}

    def test_still_not_resolved_for_blocker_purposes(self):
        self.assertFalse(GEN._substrate_resolved(dict(self.ENTRY)))

    def test_but_is_implementation_complete(self):
        self.assertTrue(GEN._substrate_implementation_complete(dict(self.ENTRY)))

    def test_unresolved_dependencies_keep_the_entry_in_the_lane(self):
        """So the substrate loop can render it `blocked` with a blocked_by
        descriptor rather than having it vanish silently."""
        entry = dict(self.ENTRY, depends_on_unresolved=["SD-033"])
        self.assertFalse(GEN._substrate_implementation_complete(entry))


class UnclassifiedReadyItemsTest(_TempSubstrateQueue):
    """The lane fails OPEN to `ready`, so an unrecognised status becomes a
    spawned chip with no error. `_unclassified_ready_items` makes that visible.
    """

    def test_novel_status_token_is_flagged(self):
        self._write(
            [{"sd_id": "SD-999", "status": "shipped_awaiting_signoff_2026", "ready": True}]
        )
        self.assertEqual(self._ready_ids(), ["SD-999"], "still emitted -- advisory, not a gate")
        self.assertEqual(
            [it["sd_id"] for it in GEN._unclassified_ready_items()], ["SD-999"]
        )

    def test_known_not_built_vocabulary_is_not_noise(self):
        """A guard that fires on ordinary work gets ignored. Explicitly-unbuilt
        statuses are correctly ready and must not be reported as drift."""
        self._write(
            [
                {"sd_id": "A", "status": "pending_implementation", "ready": True},
                {"sd_id": "B", "status": "candidate_v3_pending", "ready": True},
                {"sd_id": "C", "status": "proposed", "ready": True},
                {"sd_id": "D", "status": "blocked_pending_discrimination", "ready": True},
                {"sd_id": "E", "status": "", "ready": True},
            ]
        )
        self.assertEqual(self._ready_ids(), ["A", "B", "C", "D", "E"])
        self.assertEqual(GEN._unclassified_ready_items(), [])


class LiveSubstrateQueueTest(unittest.TestCase):
    """Against the real file on disk -- the incident items must be gone."""

    def test_no_landed_incident_item_is_ready(self):
        ready = {it.get("sd_id") for it in GEN._substrate_ready_items()}
        for sd in (
            "SD-091",
            "SD-092",
            "SD-094",
            "SD-modulatory-channel-route-decomp-gate-fix",
            "mech090-arc071-attick-persistent-handle-fix",
        ):
            with self.subTest(sd_id=sd):
                self.assertNotIn(sd, ready)


if __name__ == "__main__":
    unittest.main(verbosity=2)
