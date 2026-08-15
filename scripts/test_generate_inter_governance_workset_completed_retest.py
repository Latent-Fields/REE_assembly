#!/usr/bin/env python3
"""Regression tests for FM11 + FM11b -- the IGW retest RE-STAGING LOOP
(chip-20260808-igw-arc045-retest-restage-loop).

Confirmed incident: "Retest after substrate: ARC-045" (stable_hash 7aac4893a7c6)
was staged as an IGW worktree and GC-reaped unused THREE times --
IGW-20260803-212, IGW-20260806-207, IGW-20260807-217 -- for a retest that was
queued as V3-EXQ-436d on 2026-08-03 (ree-v3 1df184c) and RAN on 2026-08-04
(v3_exq_436d_sd017_mech166_writepath_retest_20260804T071541Z_v3, FAIL, weakens,
claim_ids SD-017/ARC-045/MECH-166).

TWO defects, both in the retest lane's notion of "this work is already covered",
and they interact -- which is why the item oscillated rather than re-staging
every tick.

FM11 -- QUEUE-KEYED COVERAGE IS TRANSIENT BY CONSTRUCTION.
    `_queued_retest_coverage` suppresses a pending_retest_after_substrate claim
    that has a matching entry in ree-v3/experiment_queue.json. Correct while the
    experiment is PENDING -- and both FAIL and ERROR remove the entry from the
    queue the instant the run finishes (CLAUDE.md, "Queue completion
    behaviour"). So the coverage evaporates exactly when the work is done and
    the item flips back to `ready` for the hourly auto-spawn routine.
    The FM8 fix (2026-08-03, 5aa0d3267a) absorbed this item CORRECTLY AT THE
    TIME -- 436d was then still pending. No fix keyed on the queue could have
    survived the run completing.
    Fix: `_completed_retest_coverage` -- coverage is also satisfied by
    experimental evidence that POSTDATES the substrate landing.

FM11b -- FM8's UNION RESURRECTS COMPLETED EXPERIMENTS AS PENDING.
    `_merge_queue_snapshots` keeps a worktree-only entry on the premise that it
    is "an experiment queued locally and not yet pushed". True of a checkout
    that is AHEAD; false of one that is BEHIND, where the extras are entries
    origin REMOVED on completion. Measured 2026-08-08: ree-v3 was 43 commits
    behind, its queue held 9 entries against origin's 2, and ALL NINE extras had
    a completed run manifest. Five claims were being falsely suppressed by those
    ghosts (ARC-045, SD-014, MECH-321, MECH-471, SD-017/MECH-166), and
    "Queue depth low" was reading 5 phantom pending items instead of 1 real one.
    Fix: `_drop_completed_worktree_ghosts`.

    A third, quieter defect fell out of fixing FM11b: `build_workset` had its
    OWN inline copy of the read-and-merge (so it could report the snapshot
    counts), so `_load_queue` was dead code from its point of view and the first
    version of the guard changed NOTHING in the generated artifact. That is the
    same second-reader drift FM9 fixed in the confirmer lane. Both now route
    through `_load_queue_detailed`, and `OneQueueLoaderTest` pins it.

WHY FM11 HOLDS THE ITEM RATHER THAN SUPPRESSING IT -- and why that asymmetry
with queued coverage is deliberate. A queued retest vanishes from the workset
because it WILL complete and the item legitimately returns. Completed-evidence
coverage persists until new substrate lands, so suppressing on it would hide
the claim indefinitely, including the fact that its claims.yaml flag may now be
stale. `blocked` stops the auto-spawn (igw_routine_tick stages `ready` only)
while keeping the evidence pointer on /workset for a human. On ARC-045 the flag
is legitimately STILL TRUE: 436d FAILed and
failure_autopsy_V3-EXQ-436d-methodology-check_2026-08-07 confirmed the FAIL is a
metric confound, not an interpretable null. A retest is genuinely owed; what is
not owed is an auto-spawned worktree re-running the confounded design.

NEGATIVE CONTROLS ARE THE POINT OF THIS FILE, not decoration. Both fixes are
suppression changes, and a suppression change that over-fires is strictly worse
than the staleness it replaces -- it hides real work instead of showing stale
work. `NoCompletedEvidenceStillSurfacesTest`, `UndatableSubstrateFailsOpenTest`
and `GhostFilterNegativeControlsTest` are what distinguish a fix from a mute.

Time-independent: no clock, no network, no sleep. Every timestamp is a literal.

Run: /opt/local/bin/python3 scripts/test_generate_inter_governance_workset_completed_retest.py
"""

import importlib.util
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent


def _load_generator():
    path = SCRIPTS_DIR / "generate_inter_governance_workset.py"
    spec = importlib.util.spec_from_file_location(
        "ree_igw_generator_completed_retest_test", path
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


G = _load_generator()


def _utc(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


# --- fixtures ---------------------------------------------------------------
# Shapes taken from the live artifacts on 2026-08-08.

# substrate_queue.json row that unblocks ARC-045. Note implemented_utc is null --
# 70 of 145 rows are, which is why failure_record run stamps have to be a source.
SUB_ARC045 = {
    "sd_id": "MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION",
    "status": "implemented_validation_failed_needs_followup_fix",
    "implemented_utc": None,
    "unblocks_claims": ["MECH-180", "MECH-122", "SD-017", "ARC-045", "MECH-166"],
    # The live row (2026-08-08), plus the `run_role` values the 2026-08-15 FM11d
    # backfill wrote onto it. The entry's own implementation_note opens
    # "IMPLEMENTED 2026-08-02", so 861 (2026-08-01T20:56) predates the build and
    # the other two do not. The third entry is what makes the cutoff
    # 2026-08-02T22:16:21Z, and it is also 436c itself -- so the boundary case
    # below ("evidence exactly AT the cutoff") is a real one, not a contrived one.
    "failure_record": [
        {"run_id": "v3_exq_861_mech180_ecological_novelty_sleep_consolidation"
                   "_decoupled_diversity_20260801T205600Z_v3",
         "run_role": "pre_build"},
        {"run_id": "v3_exq_861a_mech180_mech122_spindle_content_selection"
                   "_validation_20260802T215005Z_v3",
         "run_role": "post_build"},
        {"run_id": "v3_exq_436c_sd017_mech166_repr_confirmer_20260802T221621Z_v3",
         "run_role": "post_build"},
    ],
}
# The SAME row as it looked BEFORE the FM11d backfill -- no `run_role` anywhere.
# Pins the default: an unmarked item is `unknown`, so it cannot supply a cutoff,
# so nothing is covered. This is what protects the corpus from an item a future
# session adds without the field.
SUB_ARC045_UNMARKED = {
    **SUB_ARC045,
    "failure_record": [{"run_id": r["run_id"]} for r in SUB_ARC045["failure_record"]],
}
# Every failure_record run marked pre_build: the gap-characterisation shape. No
# candidate at all, so no cutoff -- the wrong-HOLD exposure the fix removes.
SUB_ARC045_ALL_PRE = {
    **SUB_ARC045,
    "failure_record": [dict(r, run_role="pre_build")
                       for r in SUB_ARC045["failure_record"]],
}
# A row with an explicit landing stamp instead.
SUB_STAMPED = {
    "sd_id": "SD-hazard-aware-policy-decomposition",
    "status": "implemented",
    "implemented_utc": "2026-08-01T00:00:00Z",
    "unblocks_claims": ["MECH-321"],
    "failure_record": [],
}
# A row nothing can date: no implemented_utc, no failure_record run stamps.
SUB_UNDATABLE = {
    "sd_id": "SD-undatable",
    "status": "implemented",
    "implemented_utc": None,
    "unblocks_claims": ["MECH-999"],
    "failure_record": [{"metric": "free text with no run_id"}],
}

SUBSTRATE_BY_ID = {
    e["sd_id"]: e for e in (SUB_ARC045, SUB_STAMPED, SUB_UNDATABLE)
}

# claim_evidence.v1.json `entries` rows -- one per (claim_id, run_id).
E_436D_ARC045 = {
    "claim_id": "ARC-045",
    "source_type": "experimental",
    "evidence_class": "exp:simulation",
    "evidence_direction": "weakens",
    "status": "FAIL",
    "run_id": "v3_exq_436d_sd017_mech166_writepath_retest_20260804T071541Z_v3",
    "timestamp_utc": "2026-08-04T07:15:41Z",
}
E_436C_ARC045 = {   # PRE-substrate: 2026-08-02T22:16 is the cutoff itself
    "claim_id": "ARC-045",
    "source_type": "experimental",
    "status": "FAIL",
    "run_id": "v3_exq_436c_sd017_mech166_repr_confirmer_20260802T221621Z_v3",
    "timestamp_utc": "2026-08-02T22:16:21Z",
}
E_436B_ARC045 = {   # clearly pre-substrate
    "claim_id": "ARC-045",
    "source_type": "experimental",
    "status": "FAIL",
    "run_id": "v3_exq_436b_sd017_mech166_repr_confirmer_20260802T035312Z_v3",
    "timestamp_utc": "2026-08-02T03:53:12Z",
}
E_LIT_ARC045 = {    # literature, dated AFTER the cutoff -- must not count
    "claim_id": "ARC-045",
    "source_type": "literature",
    "evidence_class": "lit:computational_theory",
    "status": "PASS",
    "run_id": "2026-08-05_arc_045_some_review",
    "timestamp_utc": "2026-08-05T00:00:00Z",
}
E_OTHER_CLAIM = {   # right date, wrong claim
    "claim_id": "MECH-166",
    "source_type": "experimental",
    "status": "FAIL",
    "run_id": "v3_exq_436d_sd017_mech166_writepath_retest_20260804T071541Z_v3",
    "timestamp_utc": "2026-08-04T07:15:41Z",
}

INCIDENT_ENTRIES = [
    E_436B_ARC045, E_436C_ARC045, E_436D_ARC045, E_LIT_ARC045, E_OTHER_CLAIM,
]


class _WithEntries:
    """Swap the module's evidence-index reader for a literal fixture list."""

    def _use(self, entries):
        self._orig = G._claim_evidence_entries
        G._claim_evidence_entries = lambda: entries
        self.addCleanup(lambda: setattr(G, "_claim_evidence_entries", self._orig))


class ParseEvidenceTsTest(unittest.TestCase):
    """The date parser both halves of FM11 stand on."""

    def test_iso_z(self):
        self.assertEqual(_utc("2026-08-04T07:15:41Z"),
                         G._parse_evidence_ts("2026-08-04T07:15:41Z"))

    def test_run_id_stamp(self):
        self.assertEqual(
            _utc("2026-08-04T07:15:41Z"),
            G._parse_evidence_ts(
                "v3_exq_436d_sd017_mech166_writepath_retest_20260804T071541Z_v3"),
        )

    def test_result_is_timezone_aware(self):
        """Naive-vs-aware comparison raises TypeError, which inside the coverage
        loop would look like 'no coverage' -- i.e. a silent un-fix."""
        self.assertIsNotNone(G._parse_evidence_ts("2026-08-04T07:15:41Z").tzinfo)

    def test_unparseable_is_none_never_epoch(self):
        for bad in ("", None, "junk", "2026-13-45T99:99:99Z", 17, {}):
            self.assertIsNone(G._parse_evidence_ts(bad), repr(bad))

    def test_none_is_not_confused_with_a_real_zero_date(self):
        """None must stay distinguishable from a datetime, or 'cannot date this'
        collapses into 'landed at the epoch' and suppresses everything."""
        self.assertIsNone(G._parse_evidence_ts("no stamp here"))


class SubstrateLandingCutoffTest(unittest.TestCase):
    def test_latest_post_build_failure_record_run_wins(self):
        cutoff, source, is_run = G._substrate_landing_cutoff(
            "ARC-045", SUBSTRATE_BY_ID)
        self.assertEqual(_utc("2026-08-02T22:16:21Z"), cutoff)
        self.assertIn("MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION", source)
        self.assertIn("failure_record", source)
        self.assertTrue(is_run, "a failure_record cutoff is a validation-run stamp")

    def test_explicit_implemented_utc_is_used(self):
        cutoff, source, is_run = G._substrate_landing_cutoff(
            "MECH-321", SUBSTRATE_BY_ID)
        self.assertEqual(_utc("2026-08-01T00:00:00Z"), cutoff)
        self.assertIn("implemented_utc", source)
        self.assertFalse(is_run, "a landing stamp is not a run, so it stays exclusive")

    def test_latest_of_both_sources_wins(self):
        entry = dict(SUB_ARC045, implemented_utc="2026-08-03T00:00:00Z")
        cutoff, source, is_run = G._substrate_landing_cutoff("ARC-045", {"x": entry})
        self.assertEqual(_utc("2026-08-03T00:00:00Z"), cutoff)
        self.assertIn("implemented_utc", source)
        self.assertFalse(is_run)

    def test_undatable_substrate_returns_none(self):
        self.assertEqual((None, "", False),
                         G._substrate_landing_cutoff("MECH-999", SUBSTRATE_BY_ID))

    def test_claim_with_no_substrate_entry_returns_none(self):
        self.assertEqual((None, "", False),
                         G._substrate_landing_cutoff("NOPE-001", SUBSTRATE_BY_ID))

    def test_malformed_rows_do_not_raise(self):
        junk = {"a": {"unblocks_claims": ["ARC-045"], "failure_record": [None, "s", 3]},
                "b": {"unblocks_claims": None},
                "c": {}}
        self.assertEqual((None, "", False),
                         G._substrate_landing_cutoff("ARC-045", junk))


class RunRoleGatesTheCutoffTest(unittest.TestCase):
    """FM11d: only `run_role: post_build` run stamps may date a landing.

    The defect: `_substrate_landing_cutoff` read EVERY failure_record run stamp as a
    post-build validation run. Measured on the live corpus 2026-08-15, 37 of the 97
    items datable against their own entry's `implemented_utc` PREDATE it -- 38% are
    gap-characterisation runs that motivated the build. When such an entry has no
    `implemented_utc` (79 of 157 do not) that stamp became the cutoff, below the real
    landing, so pre-substrate evidence satisfied "a retest has run since the
    substrate landed": a wrong HOLD.
    """

    def test_pre_build_runs_never_date_a_landing(self):
        cutoff, source, is_run = G._substrate_landing_cutoff(
            "ARC-045", {"x": SUB_ARC045_ALL_PRE})
        self.assertEqual((None, "", False), (cutoff, source, is_run),
                         "a gap-characterisation run is a LOWER bound on the "
                         "landing, not an upper one -- it must not set the bar")

    def test_absent_run_role_reads_as_unknown_not_post_build(self):
        """THE DEFAULT, and the whole safety property.

        An item a future session adds without `run_role` -- or one this backfill
        missed -- must not silently move the cutoff.
        """
        self.assertEqual(
            (None, "", False),
            G._substrate_landing_cutoff("ARC-045", {"x": SUB_ARC045_UNMARKED}),
            "unmarked must read as `unknown`; reading it as post_build is exactly "
            "the pre-2026-08-15 behaviour this fix removes",
        )

    def test_an_unparseable_run_role_is_unknown_not_a_crash(self):
        entry = {**SUB_ARC045,
                 "failure_record": [dict(r, run_role=v) for r, v in zip(
                     SUB_ARC045["failure_record"], ["POST", 17, None])]}
        self.assertEqual((None, "", False),
                         G._substrate_landing_cutoff("ARC-045", {"x": entry}))

    def test_run_role_is_case_and_whitespace_tolerant(self):
        """The field is hand-written by /governance and /failure-autopsy too."""
        self.assertEqual("post_build", G._failure_record_run_role(
            {"run_role": "  POST_BUILD "}))

    def test_implemented_utc_still_works_when_every_run_is_pre_build(self):
        """NEGATIVE CONTROL: gating the run stamps must not disable the explicit
        landing stamp, which is the signal that was never in doubt."""
        entry = dict(SUB_ARC045_ALL_PRE, implemented_utc="2026-08-03T00:00:00Z")
        cutoff, source, is_run = G._substrate_landing_cutoff("ARC-045", {"x": entry})
        self.assertEqual(_utc("2026-08-03T00:00:00Z"), cutoff)
        self.assertIn("implemented_utc", source)
        self.assertFalse(is_run)


class CompletedRetestCoverageTest(_WithEntries, unittest.TestCase):
    """FM11 proper: the incident replay."""

    def test_arc045_is_covered_by_the_run_that_already_happened(self):
        self._use(INCIDENT_ENTRIES)
        cover = G._completed_retest_coverage("ARC-045", SUBSTRATE_BY_ID)
        self.assertIsNotNone(
            cover,
            "FM11 regression: v3_exq_436d ran 2026-08-04, after the substrate "
            "landing bound 2026-08-02T22:16:21Z. Without this the item re-stages "
            "an IGW worktree every tick (3x confirmed, all GC-reaped unused).",
        )
        self.assertEqual(E_436D_ARC045["run_id"], cover["run_id"])
        self.assertEqual("FAIL", cover["status"])
        self.assertEqual("weakens", cover["evidence_direction"])
        self.assertEqual("2026-08-02T22:16:21Z", cover["cutoff_utc"])

    def test_newest_qualifying_run_is_reported(self):
        extra = dict(E_436D_ARC045,
                     run_id="v3_exq_436e_later_20260806T000000Z_v3",
                     timestamp_utc="2026-08-06T00:00:00Z")
        self._use(INCIDENT_ENTRIES + [extra])
        cover = G._completed_retest_coverage("ARC-045", SUBSTRATE_BY_ID)
        self.assertEqual("v3_exq_436e_later_20260806T000000Z_v3", cover["run_id"])

    def test_other_claims_on_the_same_manifest_are_covered_too(self):
        """436d tags SD-017/ARC-045/MECH-166; the index carries one row each, so
        every one of them must absorb -- they re-staged together."""
        self._use(INCIDENT_ENTRIES)
        self.assertIsNotNone(G._completed_retest_coverage("MECH-166", SUBSTRATE_BY_ID))

    def test_malformed_entries_do_not_raise(self):
        self._use([None, "x", 5, {}, {"claim_id": "ARC-045"}] + INCIDENT_ENTRIES)
        self.assertIsNotNone(G._completed_retest_coverage("ARC-045", SUBSTRATE_BY_ID))


class NoCompletedEvidenceStillSurfacesTest(_WithEntries, unittest.TestCase):
    """NEGATIVE CONTROL -- the assertion the chip explicitly asked for, and the
    one that separates this fix from a mute.

    A claim whose substrate has landed but which has NO post-substrate run must
    keep surfacing. If a broadened predicate ever swallows it, the retest lane
    has stopped showing real work.
    """

    def test_claim_with_no_evidence_at_all_is_not_covered(self):
        self._use([])
        self.assertIsNone(G._completed_retest_coverage("ARC-045", SUBSTRATE_BY_ID))

    def test_claim_with_only_pre_substrate_evidence_is_not_covered(self):
        self._use([E_436B_ARC045])
        self.assertIsNone(
            G._completed_retest_coverage("ARC-045", SUBSTRATE_BY_ID),
            "436b runs strictly before the substrate landing bound -- it is "
            "exactly the stale evidence the retest exists to replace",
        )

    def test_evidence_exactly_AT_an_implemented_utc_cutoff_is_not_covered(self):
        """Strictly-after for a LANDING STAMP: a run at the bound could have
        started before the substrate landed.

        RE-POINTED 2026-08-15 (FM11d). This assertion used to be unconditional --
        `test_evidence_exactly_AT_the_cutoff_is_not_covered`. The boundary rule is
        now source-dependent, and the sibling test below asserts the other half.
        """
        entry = dict(SUB_ARC045_ALL_PRE, implemented_utc="2026-08-02T22:16:21Z")
        self._use([E_436C_ARC045])
        self.assertIsNone(G._completed_retest_coverage("ARC-045", {"x": entry}))

    def test_literature_after_the_cutoff_is_not_coverage(self):
        """A lit pull is not a retest. E_LIT_ARC045 is dated 2026-08-05, later
        than the real 436d run, so a source_type-blind reader passes the other
        tests and fails this one."""
        self._use([E_436B_ARC045, E_LIT_ARC045])
        self.assertIsNone(G._completed_retest_coverage("ARC-045", SUBSTRATE_BY_ID))

    def test_another_claims_run_is_not_coverage(self):
        self._use([E_OTHER_CLAIM])
        self.assertIsNone(G._completed_retest_coverage("ARC-045", SUBSTRATE_BY_ID))

    def test_undated_evidence_row_is_not_coverage(self):
        self._use([dict(E_436D_ARC045, timestamp_utc="")])
        self.assertIsNone(G._completed_retest_coverage("ARC-045", SUBSTRATE_BY_ID))


class UndatableSubstrateFailsOpenTest(_WithEntries, unittest.TestCase):
    """NEGATIVE CONTROL -- an unreadable date must never suppress.

    If the cutoff cannot be established, the honest answer is "I don't know",
    and the item keeps its status. A generator that muted an item because it
    could not read a date would be a worse failure than the re-staging.
    """

    def test_undatable_substrate_yields_no_coverage(self):
        self._use([{
            "claim_id": "MECH-999", "source_type": "experimental",
            "status": "PASS", "run_id": "v3_exq_999_x_20260807T000000Z_v3",
            "timestamp_utc": "2026-08-07T00:00:00Z",
        }])
        self.assertIsNone(G._completed_retest_coverage("MECH-999", SUBSTRATE_BY_ID))

    def test_claim_with_no_substrate_row_yields_no_coverage(self):
        self._use([{
            "claim_id": "NOPE-001", "source_type": "experimental",
            "status": "PASS", "run_id": "v3_exq_000_x_20260807T000000Z_v3",
            "timestamp_utc": "2026-08-07T00:00:00Z",
        }])
        self.assertIsNone(G._completed_retest_coverage("NOPE-001", SUBSTRATE_BY_ID))


# --- FM11b ------------------------------------------------------------------
# The 2026-08-08 board: worktree 43 commits behind, 9 entries against origin's 2.

WORKTREE_QUEUE_20260808 = [
    {"queue_id": "V3-EXQ-875a", "status": "claimed", "claim_id": "MECH-471"},
    {"queue_id": "V3-EXQ-887", "status": "pending", "claim_id": "SD-014"},
    {"queue_id": "V3-EXQ-848b", "status": "claimed", "claim_ids": ["ARC-005"]},
    {"queue_id": "V3-EXQ-873a", "status": "pending", "claim_id": "MECH-322"},
    {"queue_id": "V3-EXQ-882a", "status": "pending", "claim_ids": ["MECH-472"]},
    {"queue_id": "V3-EXQ-888", "status": "pending", "claim_id": "MECH-074"},
    {"queue_id": "V3-EXQ-867b", "status": "claimed", "claim_id": "MECH-321"},
    {"queue_id": "V3-EXQ-436d", "status": "pending",
     "claim_ids": ["ARC-045", "MECH-166", "SD-017"]},
    {"queue_id": "V3-EXQ-149b", "status": "claimed", "claim_ids": ["Q-004"]},
]
COMMITTED_QUEUE_20260808 = [
    {"queue_id": "V3-EXQ-892", "status": "claimed", "claim_id": "MECH-322"},
    {"queue_id": "V3-EXQ-895", "status": "pending", "claim_id": "MECH-074c"},
]
# Every one of the 9 worktree-only ids had a run manifest on 2026-08-08; neither
# committed id did.
RAN_ON_20260808 = {i["queue_id"] for i in WORKTREE_QUEUE_20260808}


def _has_run(qid):
    return qid in RAN_ON_20260808


class DropCompletedWorktreeGhostsTest(unittest.TestCase):
    """FM11b: a BEHIND checkout's extras are removed-since ghosts."""

    def test_the_incident_board_loses_all_nine_ghosts(self):
        kept = G._drop_completed_worktree_ghosts(
            WORKTREE_QUEUE_20260808, COMMITTED_QUEUE_20260808, has_run=_has_run)
        self.assertEqual(
            [], kept,
            "FM11b regression: all 9 worktree-only entries had completed run "
            "manifests. Keeping them resurrects finished experiments as pending "
            "and falsely suppresses ARC-045, SD-014, MECH-321, MECH-471, "
            "SD-017 and MECH-166.",
        )

    def test_436d_specifically_stops_masking_the_retest(self):
        merged = G._merge_queue_snapshots(
            G._drop_completed_worktree_ghosts(
                WORKTREE_QUEUE_20260808, COMMITTED_QUEUE_20260808,
                has_run=_has_run),
            COMMITTED_QUEUE_20260808,
        )
        self.assertNotIn("ARC-045", G._queued_retest_coverage(merged))

    def test_queue_depth_premise_is_repaired(self):
        """The same ghosts made 'Queue depth low' read 5 phantom pending items."""
        def pending(items):
            return [i for i in items
                    if i.get("status") == "pending" and not i.get("claimed_by")]
        # 5 ghosts (887, 873a, 882a, 888, 436d) + the 1 real one (895).
        self.assertEqual(6, len(pending(
            G._merge_queue_snapshots(WORKTREE_QUEUE_20260808,
                                     COMMITTED_QUEUE_20260808))))
        self.assertEqual(1, len(pending(
            G._merge_queue_snapshots(
                G._drop_completed_worktree_ghosts(
                    WORKTREE_QUEUE_20260808, COMMITTED_QUEUE_20260808,
                    has_run=_has_run),
                COMMITTED_QUEUE_20260808))))


class GhostFilterNegativeControlsTest(unittest.TestCase):
    """NEGATIVE CONTROLS -- FM11b must not eat a genuinely-local queue entry.

    That is the whole reason FM8 made the merge a union in the first place.
    """

    def test_locally_queued_entry_with_no_run_survives(self):
        local = [{"queue_id": "V3-EXQ-NEW", "status": "pending",
                  "claim_id": "MECH-999"}]
        kept = G._drop_completed_worktree_ghosts(
            local, COMMITTED_QUEUE_20260808, has_run=_has_run)
        self.assertEqual(local, kept)

    def test_entry_present_in_committed_is_never_dropped(self):
        """Only WORKTREE-ONLY entries are candidates. An entry origin still
        carries is live by definition, whatever runs exist for it."""
        both = [{"queue_id": "V3-EXQ-895", "status": "pending",
                 "claim_id": "MECH-074c"}]
        kept = G._drop_completed_worktree_ghosts(
            both, COMMITTED_QUEUE_20260808, has_run=lambda q: True)
        self.assertEqual(both, kept)

    def test_nothing_is_dropped_when_no_run_exists(self):
        kept = G._drop_completed_worktree_ghosts(
            WORKTREE_QUEUE_20260808, COMMITTED_QUEUE_20260808,
            has_run=lambda q: False)
        self.assertEqual(len(WORKTREE_QUEUE_20260808), len(kept))

    def test_entries_without_a_queue_id_survive(self):
        junk = [{"status": "pending"}, "not-a-dict", None]
        self.assertEqual(junk, G._drop_completed_worktree_ghosts(
            junk, COMMITTED_QUEUE_20260808, has_run=lambda q: True))

    def test_filter_never_invents_an_entry(self):
        kept = G._drop_completed_worktree_ghosts(
            WORKTREE_QUEUE_20260808, COMMITTED_QUEUE_20260808, has_run=_has_run)
        for item in kept:
            self.assertIn(item, WORKTREE_QUEUE_20260808)


class QueueIdRunMatchTest(unittest.TestCase):
    """The queue_id -> run_id prefix convention FM11b's default probe relies on."""

    def _with_runs(self, names):
        orig = G._recorded_run_names
        G._recorded_run_names = lambda: set(names)
        self.addCleanup(lambda: setattr(G, "_recorded_run_names", orig))

    def test_matches_the_conventional_run_id(self):
        self._with_runs({
            "v3_exq_436d_sd017_mech166_writepath_retest_20260804T071541Z_v3"})
        self.assertTrue(G._queue_id_has_recorded_run("V3-EXQ-436d"))

    def test_prefix_does_not_bleed_across_ids(self):
        """The trailing underscore is load-bearing: without it V3-EXQ-43 matches
        v3_exq_436d_... and would drop a live entry."""
        self._with_runs({
            "v3_exq_436d_sd017_mech166_writepath_retest_20260804T071541Z_v3"})
        self.assertFalse(G._queue_id_has_recorded_run("V3-EXQ-43"))
        self.assertFalse(G._queue_id_has_recorded_run("V3-EXQ-436"))

    def test_letter_suffixes_are_distinct(self):
        self._with_runs({"v3_exq_436d_x_20260804T071541Z_v3"})
        self.assertTrue(G._queue_id_has_recorded_run("V3-EXQ-436d"))
        self.assertFalse(G._queue_id_has_recorded_run("V3-EXQ-436e"))

    def test_no_runs_means_no_match(self):
        self._with_runs(set())
        self.assertFalse(G._queue_id_has_recorded_run("V3-EXQ-436d"))

    def test_blank_queue_id_never_matches(self):
        self._with_runs({"v3_exq_436d_x_v3"})
        for bad in ("", None, "   "):
            self.assertFalse(G._queue_id_has_recorded_run(bad), repr(bad))


class OneQueueLoaderTest(unittest.TestCase):
    """build_workset must NOT re-implement the read-and-merge.

    It did, which is why the first FM11b guard landed in `_load_queue` and
    changed nothing in the generated artifact -- `_load_queue` was dead code
    from build_workset's point of view. Same second-reader drift FM9 fixed in
    the confirmer lane.
    """

    def test_load_queue_delegates_to_the_detailed_loader(self):
        calls = []
        orig = G._load_queue_detailed
        try:
            G._load_queue_detailed = lambda: (calls.append(1) or
                                              {"items": ["sentinel"]})
            self.assertEqual(["sentinel"], G._load_queue())
        finally:
            G._load_queue_detailed = orig
        self.assertEqual(1, len(calls))

    def test_build_workset_reads_the_queue_through_the_detailed_loader(self):
        """Executes the real build with the loader stubbed: if build_workset
        ever grows a second inline reader, the sentinel counts stay at zero and
        the queue-derived summary stops matching."""
        calls = []
        orig = G._load_queue_detailed
        try:
            G._load_queue_detailed = lambda: (
                calls.append(1) or {
                    "items": list(COMMITTED_QUEUE_20260808),
                    "worktree": list(WORKTREE_QUEUE_20260808),
                    "committed": list(COMMITTED_QUEUE_20260808),
                    "ghosts_dropped": 9,
                    "behind_by": 2,
                })
            data = G.build_workset()
        finally:
            G._load_queue_detailed = orig
        self.assertEqual(1, len(calls), "build_workset must call it exactly once")
        snap = data["summary"]["queue_snapshot"]
        self.assertEqual(9, snap["worktree_ghosts_dropped"])
        self.assertEqual(2, snap["worktree_behind_by"])
        self.assertEqual(2, snap["merged_items"])

    def test_detailed_loader_fails_open_when_the_committed_ref_is_unreadable(self):
        orig_git = G._queue_from_git
        orig_wt = G._queue_from_worktree
        try:
            G._queue_from_git = lambda *a, **k: None
            G._queue_from_worktree = lambda: list(WORKTREE_QUEUE_20260808)
            got = G._load_queue_detailed()
        finally:
            G._queue_from_git = orig_git
            G._queue_from_worktree = orig_wt
        self.assertEqual(9, len(got["items"]),
                         "no authority to compare against -> filter nothing")
        self.assertIsNone(got["committed"])
        self.assertEqual(0, got["ghosts_dropped"])

    def test_behind_by_counts_what_the_worktree_was_missing(self):
        """Not (merged - worktree): once ghosts are dropped that goes negative on
        a badly stale checkout and clamps to a reassuring 0."""
        orig_git = G._queue_from_git
        orig_wt = G._queue_from_worktree
        orig_has = G._queue_id_has_recorded_run
        try:
            G._queue_from_git = lambda *a, **k: list(COMMITTED_QUEUE_20260808)
            G._queue_from_worktree = lambda: list(WORKTREE_QUEUE_20260808)
            G._queue_id_has_recorded_run = _has_run
            got = G._load_queue_detailed()
        finally:
            G._queue_from_git = orig_git
            G._queue_from_worktree = orig_wt
            G._queue_id_has_recorded_run = orig_has
        self.assertEqual(9, got["ghosts_dropped"])
        self.assertEqual(2, got["behind_by"])
        self.assertEqual(2, len(got["items"]))


class EvidenceIndexReaderTest(unittest.TestCase):
    """The `entries` reader FM11 consumes, and the shared-parse refactor."""

    def test_entries_and_claims_come_from_one_parse(self):
        calls = []
        orig = G._claim_evidence_doc
        try:
            G._claim_evidence_doc = lambda: (calls.append(1) or
                                             {"claims": {"X": {}}, "entries": [1]})
            self.assertEqual({"X": {}}, G._claim_evidence_claims())
            self.assertEqual([1], G._claim_evidence_entries())
        finally:
            G._claim_evidence_doc = orig
        self.assertEqual(2, len(calls))  # memoization lives inside _claim_evidence_doc

    def test_malformed_document_degrades_to_empty(self):
        orig = G._claim_evidence_doc
        try:
            for junk in ({}, {"claims": "nope", "entries": "nope"}):
                G._claim_evidence_doc = lambda j=junk: j
                self.assertEqual({}, G._claim_evidence_claims())
                self.assertEqual([], G._claim_evidence_entries())
        finally:
            G._claim_evidence_doc = orig

    def test_live_index_is_readable_and_has_the_incident_row(self):
        """Integration smoke against the real artifact -- the fixtures above are
        only worth anything if the shapes they copy are the real ones."""
        entries = G._claim_evidence_entries()
        self.assertTrue(entries, "claim_evidence.v1.json entries must be readable")
        hit = [e for e in entries
               if isinstance(e, dict) and e.get("claim_id") == "ARC-045"
               and "436d" in str(e.get("run_id", ""))]
        self.assertEqual(1, len(hit))
        self.assertEqual("experimental", hit[0]["source_type"])
        self.assertEqual("2026-08-04T07:15:41Z", hit[0]["timestamp_utc"])


class SelfCancellingCutoffIsFixedTest(_WithEntries, unittest.TestCase):
    """FM11d, the second half: a POST-BUILD cutoff run is its own coverage.

    WAS `SelfCancellingCutoffIsRecordedNotFixedTest`, which pinned the opposite --
    deliberately, so that changing it would be an act rather than a side effect.
    This is that act (2026-08-15, user-approved option (b) from
    chip-20260815-igw-fm11-cutoff-boundary).

    The pathology it recorded: when a claim's ONLY post-substrate evidence is the
    very run that defined the cutoff, `when <= cutoff` made that run set the bar and
    fail it, so the claim rendered `ready` and the auto-spawn could stage it again --
    FM11 arriving one mechanism over. Live on 2026-08-15 for MECH-074d
    (SD-035.failure_record == v3_exq_894c), MECH-151 and MECH-152 (both
    SD-016.failure_record == v3_exq_922): three of the four claims that reached FM11
    at all.

    Why it could not be fixed by relaxing the comparison alone -- the chip's
    explicit instruction, and the reason the two halves shipped together. With every
    failure_record stamp read as post-build, `<` would have let a PRE-build stamp
    both set the cutoff and satisfy it, making the wrong-HOLD exposure strictly
    worse. Gating the cutoff on `run_role` is what makes the relaxed comparison
    safe: an at-the-cutoff row can now only be a run that postdates a real landing.
    """

    def test_claim_whose_only_evidence_defined_the_cutoff_IS_covered(self):
        self._use([E_436C_ARC045])
        cover = G._completed_retest_coverage("ARC-045", SUBSTRATE_BY_ID)
        self.assertIsNotNone(
            cover,
            "FM11d regression: 436c is marked post_build on the substrate row, so "
            "it ran against the landed substrate and IS the retest -- excluding it "
            "makes the cutoff self-cancelling and the item re-stages",
        )
        self.assertEqual(E_436C_ARC045["run_id"], cover["run_id"])
        self.assertTrue(cover["cutoff_is_validation_run"])

    def test_a_strictly_later_run_still_wins(self):
        """Negative control: the boundary run is coverage of last resort, not a
        preferred answer -- the NEWEST qualifying run is still reported."""
        self._use([E_436C_ARC045, E_436D_ARC045])
        cover = G._completed_retest_coverage("ARC-045", SUBSTRATE_BY_ID)
        self.assertIsNotNone(cover)
        self.assertEqual(E_436D_ARC045["run_id"], cover["run_id"])

    def test_the_boundary_run_is_not_coverage_when_it_is_PRE_build(self):
        """NEGATIVE CONTROL, and the exact hazard the chip warned against.

        Relax `<=` to `<` WITHOUT the run_role gate and this is what you get: a
        gap-characterisation run setting a cutoff below the real landing and then
        satisfying it -- a wrong HOLD on evidence that predates the build. Here
        every stamp is pre_build, so there is no cutoff and nothing is covered.
        """
        self._use([E_436C_ARC045, E_436D_ARC045])
        self.assertIsNone(
            G._completed_retest_coverage("ARC-045", {"x": SUB_ARC045_ALL_PRE}))


class RetestLaneEvaluationTest(unittest.TestCase):
    """The chain extracted from build_workset's retest loop (FM11c).

    Deterministic, fixture-driven: the live tests below prove the mechanism is
    wired up, these prove it decides correctly.
    """

    def _eval(self, cid, entries, substrate=None, meta=None, proposals=None):
        orig = G._claim_evidence_entries
        G._claim_evidence_entries = lambda: entries
        self.addCleanup(lambda: setattr(G, "_claim_evidence_entries", orig))
        return G._retest_lane_evaluation(
            cid, substrate if substrate is not None else SUBSTRATE_BY_ID,
            meta or {}, proposals or {},
        )

    def test_completed_evidence_holds_the_item_and_names_the_run(self):
        got = self._eval("ARC-045", INCIDENT_ENTRIES)
        self.assertEqual("blocked", got["status"])
        self.assertIsNotNone(got["evidence_cover"])
        self.assertEqual(E_436D_ARC045["run_id"], got["evidence_cover"]["run_id"])
        self.assertTrue(any("436d" in b for b in got["blocker_strs"]),
                        "the blocker must name the run that already happened")
        self.assertIn("ALREADY RUN", got["why_now"])

    def test_no_post_substrate_evidence_stays_ready(self):
        """NEGATIVE CONTROL: FM11 holds, it does not sweep the lane."""
        got = self._eval("ARC-045", [E_436B_ARC045])
        self.assertEqual("ready", got["status"])
        self.assertIsNone(got["evidence_cover"])
        self.assertEqual([], got["blocker_strs"])

    def test_an_earlier_blocker_wins_and_fm11_is_not_consulted(self):
        """FM11 is last in the chain on purpose -- reaching it is what proves the
        cutoff is being computed against LANDED substrate."""
        unresolved = dict(SUB_ARC045, status="proposed", ready=False)
        got = self._eval("ARC-045", INCIDENT_ENTRIES,
                         substrate={unresolved["sd_id"]: unresolved})
        self.assertEqual("blocked", got["status"])
        self.assertIsNone(got["evidence_cover"],
                          "FM11 must not date a build that has not landed")


class LiveIncidentReplayTest(unittest.TestCase):
    """End-to-end against the real repo inputs: the ARC-045 item must not be
    `ready`, and must still be PRESENT (held, not suppressed).

    RE-POINTED 2026-08-15. This class used to additionally assert that ARC-045's
    blocker NAMED the completed run and that ARC-045 appeared in
    `evidence_covered_retests` -- i.e. that FM11 specifically was what held it.
    Both stopped being true for a CORPUS reason, not a code one: on 2026-08-08 the
    MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION row read
    `implemented_validation_failed_needs_followup_fix`, which `_status_resolved`
    accepts, so ARC-045 had no substrate blocker and fell through to FM11.
    Governance later moved that row to `implemented_pending_validation`, which
    `_status_resolved` hard-vetoes on the "pending" substring (deliberately -- see
    FM3 in the generator header), so ARC-045 is now held one step EARLIER in the
    chain, by the substrate prerequisite. The hold that matters is unchanged and
    is still asserted below; what moved is which mechanism supplies it.

    The FM11-specific assertions now live in
    `Fm11IsLiveOnTheRealCorpusTest`, keyed on the mechanism rather than on one
    claim that can drift out from under it.
    """

    def test_arc045_retest_is_blocked_not_ready_and_not_gone(self):
        data = G.build_workset()
        items = [i for i in data["items"]
                 if i["title"] == "Retest after substrate: ARC-045"]
        self.assertEqual(1, len(items), "the item must stay on the board")
        item = items[0]
        self.assertEqual(
            "blocked", item["status"],
            "igw_routine_tick stages `ready` items only -- `blocked` is what "
            "stops the worktree re-staging loop",
        )
        self.assertTrue(item["blocked_by"],
                        "a blocked item must say what is holding it")

    def test_arc045_fm11_coverage_is_still_computable_from_live_inputs(self):
        """The ORIGINAL incident assertion, kept at the level that still holds.

        ARC-045 is held by its substrate prerequisite today, so FM11 is not what
        stops the re-staging for it right now. When that prerequisite resolves,
        FM11 is what must take over -- and the three confirmed re-stages
        (IGW-20260803-212 / -20260806-207 / -20260807-217) return if it cannot.
        So assert the input side directly: a post-substrate run for ARC-045 is
        findable in the live evidence index. This is the assertion that goes red
        if claim_evidence.v1.json moves, is renamed, or loses its timestamps --
        the failure mode the item-level test could no longer distinguish from an
        ordinary corpus shift.
        """
        cover = G._completed_retest_coverage("ARC-045", G._substrate_by_id())
        self.assertIsNotNone(
            cover,
            "FM11 cannot see ANY post-substrate run for ARC-045 -- if the "
            "substrate blocker clears, the item goes `ready` and re-stages",
        )
        self.assertTrue(cover["run_id"].startswith("v3_exq_436"),
                        f"unexpected covering run: {cover['run_id']}")


class Fm11IsLiveOnTheRealCorpusTest(unittest.TestCase):
    """THE ASSERTION THAT WOULD HAVE CAUGHT THIS (chip requirement 3).

    `summary.evidence_covered_retests` was exactly `{}` on 2026-08-15 -- not one
    claim drifting, the whole FM11 mechanism contributing nothing -- and nothing
    said so. The only signal was an unrelated-looking failure in the class above,
    which read as "the test needs updating". These tests are keyed on the
    mechanism producing output at all, so inertness cannot be mistaken for drift.
    """

    def test_evidence_covered_retests_is_not_empty(self):
        data = G.build_workset()
        covered = data["summary"]["evidence_covered_retests"]
        self.assertTrue(
            covered,
            "FM11 is INERT: no retest claim anywhere in the lane was held by "
            "completed post-substrate evidence. Queue-keyed coverage is "
            "transient by design (a finished run leaves the queue), so FM11 is "
            "the only thing standing between a completed retest and the "
            "auto-spawn re-staging it. Do NOT 'fix' this by relaxing the "
            "assertion -- find out why the mechanism stopped contributing.",
        )

    def test_every_covered_claim_names_a_real_run(self):
        data = G.build_workset()
        for cid, run_id in data["summary"]["evidence_covered_retests"].items():
            self.assertTrue(run_id and run_id != "?",
                            f"{cid} held by an unnamed run")
            rows = [e for e in G._claim_evidence_entries()
                    if isinstance(e, dict) and e.get("claim_id") == cid
                    and e.get("run_id") == run_id]
            self.assertTrue(
                rows, f"{cid} is held by {run_id}, which is not an evidence row")
            self.assertEqual("experimental", rows[0].get("source_type"),
                             f"{cid} held by a non-experimental row -- a lit "
                             f"pull is not a retest")

    def test_fm11_is_evaluated_for_every_retest_claim_not_just_the_board_window(self):
        """FM11c regression, and the proximate cause of the empty accounting.

        The retest loop emits a capped window (`retest[:10]`) of an
        ALPHABETICALLY sorted list -- a cap applied before any claim's status is
        known. FM11 is last in the blocker chain, so evaluating inside that window
        made it reachable only by an alphabetically early claim. On the
        2026-08-15 corpus all four claims that reach FM11 (MECH-074d, MECH-151,
        MECH-152, Q-081 -- indices 16/23/24/69 of 82) fell outside it, and every
        one of the ten emitted claims was held earlier in the chain. Hence `{}`.

        Counting the calls rather than inspecting the output keeps this keyed on
        the structure that broke, so it stays meaningful whatever the corpus does.
        """
        calls: list[str] = []
        orig = G._retest_lane_evaluation
        try:
            def counting(cid, *a, **k):
                calls.append(cid)
                return orig(cid, *a, **k)
            G._retest_lane_evaluation = counting
            G.build_workset()
        finally:
            G._retest_lane_evaluation = orig
        retest_all = sorted(G._claim_retest_ids())
        self.assertGreater(len(retest_all), 10,
                           "corpus too small for this test to mean anything")
        self.assertGreater(
            len(calls), 10,
            f"FM11 was evaluated for only {len(calls)} claim(s) -- the emission "
            f"cap is gating the blocker chain again, so a covered claim outside "
            f"the alphabetically-first window is never asked and silently "
            f"renders `ready`",
        )
        self.assertEqual(
            sorted(calls), sorted(set(calls)),
            "each retest claim must be evaluated exactly once",
        )

    def test_no_completed_evidence_claims_are_still_ready_or_substrate_blocked(self):
        """NEGATIVE CONTROL at the whole-artifact level: FM11 must not have
        swept the lane. Some retest item must still exist that is NOT held by
        evidence coverage."""
        data = G.build_workset()
        retests = [i for i in data["items"]
                   if i["title"].startswith("Retest after substrate:")]
        self.assertGreaterEqual(len(retests), 5)
        held = set(data["summary"]["evidence_covered_retests"])
        unheld = [i for i in retests if not (set(i["claim_ids"]) & held)]
        self.assertTrue(unheld, "every retest item was held -- that is a mute, "
                                "not a fix")


if __name__ == "__main__":
    unittest.main(verbosity=2)
