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

Vacuity audit (2026-08-18, chip-20260816-igw-test-oracle-vacuity-audit): the
fixture classes here carry literal oracles and are immune by construction --
`ConfirmedIncidentReplayTest`'s negative control asserts an exact expected list,
so over-suppression goes red. `LiveSubstrateQueueTest` did NOT: it built its
oracle from `_substrate_ready_items()` over the live corpus with no guard, and
was verified GREEN-while-asserting-nothing under four separate corpus failures.
See that class's docstring; do not re-derive its oracle from a predicate under
test.

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


class ProsePendingVetoTest(unittest.TestCase):
    """FM4 (chip-20260808-igw202): the "pending" veto is HEAD-scoped, not a
    whole-string substring test.

    The scaffolded-curriculum-hazard-rebalance entry carried a ~1200-char
    provenance status whose primary token is terminal but whose trailing
    narrative contained "...stayed stale at pending_implementation only
    because...". The old whole-string veto read that prose "pending" as a live
    token and could never classify the entry resolved, so it re-staged as
    "Substrate ready" every generation. The fix consults only the status HEAD.
    """

    # A genuine terminal status with the word "pending" only in trailing prose.
    PROSE = (
        "closed_no_substrate_change_warranted_2026-08-08. Adjudicated and "
        "USER-CONFIRMED. Previously stayed stale at pending_implementation only "
        "because the file was under another session's active claim at diagnosis "
        "time."
    )

    def test_prose_pending_does_not_veto_a_terminal_status(self):
        self.assertTrue(GEN._status_terminal(self.PROSE))
        self.assertFalse(
            GEN._status_pending_vetoed(self.PROSE),
            "'pending' in trailing narrative must not veto",
        )

    def test_head_pending_token_still_vetoes_both_directions(self):
        """Every genuine `*pending*` status keeps its head-token veto -- this is
        the FM3 family, which `_status_implementation_complete` relies on still
        vetoing here. Widening the veto to `"pending" not in s` would break it."""
        for st in (
            "implemented_pending_validation",
            "pending_implementation",
            "candidate_v3_pending",
            "substrate_landed_pending_behavioural_validation",
            "blocked_pending_discrimination",
            "parked_pending_env_entropy_precondition",
        ):
            with self.subTest(status=st):
                self.assertTrue(GEN._status_pending_vetoed(st))
                self.assertFalse(GEN._status_resolved(st))
                self.assertFalse(GEN._status_terminal(st))

    def test_head_is_first_token_before_space_or_period(self):
        self.assertEqual(
            GEN._status_head("diagnosis_done_x_2026-08-08. Adjudicated by chip"),
            "diagnosis_done_x_2026-08-08",
        )
        self.assertEqual(
            GEN._status_head("implemented_pending_validation"),
            "implemented_pending_validation",
        )

    def test_fm3_family_stays_build_complete_but_unresolved(self):
        """Regression guard on the FM3 interaction: head-scoping the veto must
        not flip `implemented_pending_validation` to fully-resolved (that is the
        FM1 failure -- unblocking retests of unvalidated substrate)."""
        entry = {"sd_id": "X", "status": "implemented_pending_validation", "ready": True}
        self.assertFalse(GEN._substrate_resolved(dict(entry)))
        self.assertTrue(GEN._substrate_implementation_complete(dict(entry)))


class NoSubstrateChangeWarrantedTerminalTest(_TempSubstrateQueue):
    """FM4: an adjudicated `no_substrate_change_warranted` disposition is
    terminal for both questions -- nothing to implement, and not a retest blocker
    (no build to wait on). It must not surface as "Substrate ready"."""

    def test_disposition_is_resolved_and_not_ready(self):
        self._write(
            [
                {
                    "sd_id": "adjudicated-no-change",
                    "status": "diagnosis_done_no_substrate_change_warranted_2026-08-08. prose with pending_implementation clause.",
                    "ready": True,
                    "depends_on_unresolved": [],
                },
                {"sd_id": "genuinely-unbuilt", "status": "pending_implementation", "ready": True},
            ]
        )
        ready = self._ready_ids()
        self.assertNotIn("adjudicated-no-change", ready)
        self.assertIn("genuinely-unbuilt", ready, "the veto must not over-fire")
        # Terminal for blocker purposes too.
        entry = {
            "sd_id": "adjudicated-no-change",
            "status": "diagnosis_done_no_substrate_change_warranted_2026-08-08",
            "ready": True,
        }
        self.assertTrue(GEN._substrate_resolved(entry))

    def test_diagnosis_done_alone_is_not_terminal(self):
        """Negative control: `diagnosis_done` WITHOUT the no-change token is NOT
        terminal -- a diagnosis can conclude a change IS warranted. Only the
        specific no_substrate_change_warranted phrase resolves."""
        self.assertFalse(GEN._status_terminal("diagnosis_done_change_needed_2026"))
        self.assertFalse(GEN._status_resolved("diagnosis_done_change_needed_2026"))


class LiveSubstrateQueueTest(unittest.TestCase):
    """Against the real file on disk -- the incident items must be gone.

    NON-VACUITY GUARDS (added 2026-08-18 by the IGW test-oracle vacuity audit,
    chip-20260816-igw-test-oracle-vacuity-audit). Every assertion in this class
    is an `assertNotIn` against a set built BY THE FUNCTIONS UNDER TEST, over a
    LIVE corpus -- the same shape as the confirmed FM11d defect in
    test_backfill_failure_record_run_role.py (REE_assembly 48bae8be81), where
    the oracle came from the function whose revert the test was supposed to
    catch, so the set emptied and every assertion passed against nothing.

    Here the emptying route is `_load_substrate_queue()`, which fails OPEN --
    returning [] on a missing, renamed or unparseable file. That is correct for
    the generator (a broken input must not wedge the workset) and fatal for a
    test that reads its output as an oracle. Verified by injection: with the
    queue file missing, empty, unparseable, or with the five incident ids
    stripped out, BOTH tests below were GREEN while asserting nothing at all.

    The guards therefore read the RAW committed JSON directly and compare
    against a hand-authored build-landed vocabulary (stem tokens, see
    `BUILD_LANDED_STEM_TOKENS`), calling no generator predicate -- so the
    oracle cannot be emptied by the same defect the assertions exist to catch.
    """

    #: Build-landed status STEM tokens, matched by substring against the raw
    #: committed status. Was a literal-string frozenset until 2026-09-01
    #: (chip-20260901-igw-substrate-status-vocab-drift): governance amends
    #: (REE_assembly 54dbe477be, "3 substrate_queue amends") gave SD-091/
    #: SD-092/SD-094/mech090-arc071-attick-persistent-handle-fix free-text
    #: diagnostic statuses -- e.g.
    #: "implemented_smoke_pass_falsifier_designed_blocked_substrate_harness_confound" --
    #: that a small literal enum can never keep up with; substrate_queue.json
    #: has no documented status enum to restore instead (its own
    #: `_schema_notes` describe status as free prose). Stem matching is still
    #: an INDEPENDENT check, NOT derived from `_status_implementation_complete()`:
    #: that is the predicate under test, and sourcing the oracle from it is
    #: precisely the FM11d bug. This list is its own hand-authored judgement
    #: call about what "build landed" means in status prose, not an import of
    #: the SUT's token list (which happens to overlap -- both are naming the
    #: same domain concept from the same committed vocabulary).
    BUILD_LANDED_STEM_TOKENS = (
        "implemented",
        "landed",
        "validated",
        "superseded",
        "subsumed",
        "closed",
    )

    @classmethod
    def _looks_build_landed(cls, raw_status: str) -> bool:
        """True if the raw status string reads as build-landed.

        `partial` is excluded so a real-build-work-remains status (e.g.
        `partially_implemented_pending_consumer_wiring`) does not falsely
        satisfy this premise check -- mirroring, not calling, the SUT's own
        `partial` guard in `_status_implementation_complete`.
        """
        s = (raw_status or "").strip().lower()
        if not s or "partial" in s:
            return False
        return any(tok in s for tok in cls.BUILD_LANDED_STEM_TOKENS)

    #: The four confirmed FM3 incident items plus SD-094. Each must be present
    #: in the live corpus AND carry a build-landed status, or `assertNotIn`
    #: below is asserting nothing.
    INCIDENT_IDS = (
        "SD-091",
        "SD-092",
        "SD-094",
        "SD-modulatory-channel-route-decomp-gate-fix",
        "mech090-arc071-attick-persistent-handle-fix",
    )

    SCAFFOLDED_ID = "scaffolded-curriculum-hazard-rebalance"

    #: FM4 adjudication marker, matched on the status HEAD only -- the live
    #: status carries a long prose tail that will keep being edited.
    SCAFFOLDED_STATUS_HEAD = "diagnosis_done_NO_SUBSTRATE_CHANGE_WARRANTED"

    @classmethod
    def setUpClass(cls):
        """Parse the live queue RAW -- no generator helper, so a parse failure
        surfaces as a failure rather than as an empty oracle."""
        cls._raw_path = Path(GEN.SUBSTRATE_QUEUE)
        cls._raw_error = None
        cls._raw = {}
        try:
            payload = json.loads(cls._raw_path.read_text(encoding="utf-8"))
            cls._raw = {
                e["sd_id"]: e
                for e in (payload.get("queue") or [])
                if isinstance(e, dict) and e.get("sd_id")
            }
        except Exception as exc:  # reported below, never swallowed
            cls._raw_error = "%s: %s" % (type(exc).__name__, exc)

    def _assert_corpus_loaded(self):
        """An empty oracle is a FAILURE in this class, never a quiet pass."""
        self.assertIsNone(
            self._raw_error,
            "live substrate_queue at %s did not parse (%s) -- every assertion "
            "in this class would otherwise pass against an empty set"
            % (self._raw_path, self._raw_error),
        )
        self.assertTrue(
            self._raw,
            "live substrate_queue at %s holds no entries -- this class asserts "
            "over the live corpus and is now vacuous; re-point it at a fixture "
            "corpus rather than letting it pass quietly" % (self._raw_path,),
        )

    def test_the_live_corpus_is_actually_loaded(self):
        """Standalone non-vacuity check, so the failure names the real cause
        instead of surfacing as a confusing pass elsewhere."""
        self._assert_corpus_loaded()
        self.assertEqual(
            len(self._raw),
            len(GEN._substrate_by_id()),
            "a raw read of %s and the generator's own loader disagree on entry "
            "count -- one of them is dropping entries silently"
            % (self._raw_path,),
        )

    def test_no_landed_incident_item_is_ready(self):
        self._assert_corpus_loaded()
        ready = {it.get("sd_id") for it in GEN._substrate_ready_items()}
        for sd in self.INCIDENT_IDS:
            with self.subTest(sd_id=sd):
                # Independent oracle: presence and status read from the raw
                # file and compared to literals -- no predicate under test.
                self.assertIn(
                    sd,
                    self._raw,
                    "%s is no longer in the live substrate_queue -- the "
                    "assertion below would pass against nothing; re-point this "
                    "test at a fixture corpus rather than deleting it" % (sd,),
                )
                raw_status = (self._raw[sd].get("status") or "").strip()
                self.assertTrue(
                    self._looks_build_landed(raw_status),
                    "%s's committed status is %r, which does not read as "
                    "build-landed (no BUILD_LANDED_STEM_TOKENS match, or "
                    "'partial' present). This test asserts the item is "
                    "suppressed BECAUSE its build landed, so a status outside "
                    "that vocabulary invalidates the premise -- update "
                    "BUILD_LANDED_STEM_TOKENS or re-point the test" % (sd, raw_status),
                )
                self.assertNotIn(sd, ready)

    def test_scaffolded_curriculum_rebalance_is_resolved(self):
        """FM4 incident item: adjudicated no-substrate-change-warranted, must no
        longer surface as an /implement-substrate task.

        The absence branch was `skipTest` until the 2026-08-18 audit. A skip is
        a silent stand-down, and the corpus quietly ceasing to contain the item
        is indistinguishable from the fix having been reverted -- so it is now
        a loud failure carrying the re-point instruction.
        """
        self._assert_corpus_loaded()
        self.assertIn(
            self.SCAFFOLDED_ID,
            self._raw,
            "%s is no longer in the live substrate_queue -- this test can no "
            "longer verify the FM4 adjudication; re-point it at a fixture "
            "corpus rather than skipping" % (self.SCAFFOLDED_ID,),
        )
        raw_status = (self._raw[self.SCAFFOLDED_ID].get("status") or "").strip()
        self.assertTrue(
            raw_status.startswith(self.SCAFFOLDED_STATUS_HEAD),
            "%s's committed status head is %r, expected it to start with %r -- "
            "the FM4 adjudication this test asserts on is no longer recorded"
            % (self.SCAFFOLDED_ID, raw_status[:80], self.SCAFFOLDED_STATUS_HEAD),
        )
        entry = GEN._substrate_by_id().get(self.SCAFFOLDED_ID)
        self.assertIsNotNone(
            entry,
            "%s is in the raw file but the generator's loader dropped it"
            % (self.SCAFFOLDED_ID,),
        )
        self.assertTrue(GEN._substrate_resolved(entry))
        ready = {it.get("sd_id") for it in GEN._substrate_ready_items()}
        self.assertNotIn(self.SCAFFOLDED_ID, ready)


if __name__ == "__main__":
    unittest.main(verbosity=2)
