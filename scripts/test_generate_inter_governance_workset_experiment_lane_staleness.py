#!/usr/bin/env python3
"""Regression tests for FM8 + FM9 -- the EXPERIMENT-lane staleness blind spots in
generate_inter_governance_workset.py (chip-20260803-igw-experiment-lane-staleness).

Confirmed incident (2026-08-03T21:55Z, metaworker-dispatch cycle 275, ree-cloud-5):
of 9 `status: "ready"`, non-governance, v3 workset items, 5 asked for work that
already existed. Two independent defects, in two different code paths:

FM8 -- STALE INPUT, not a bad predicate.
    `_load_queue()` read ONLY the ree-v3 working-tree copy of
    experiment_queue.json. That is a sibling repo this generator never syncs and
    no IGW tick pulls; on the incident box it was 26 commits behind origin/main
    and held 2 entries against the committed snapshot's 8. Consequences:
      * "Retest after substrate: ARC-045" rendered `ready` although V3-EXQ-436d
        (claim_ids ARC-045/SD-017/MECH-166) was pending. `_queued_retest_coverage`
        is CORRECT and absorbs it the moment it is shown the entry -- it never was.
      * "Queue depth low (0 pending)" against 4 genuinely-pending items.
    Established by running build_workset() twice on ONE code base, swapping only
    _load_queue's return: both items drop out under the committed snapshot and no
    new item appears. So the predicates were never the defect -- the INPUT was.
    Fix: _load_queue merges the working tree with the committed
    `origin/main:experiment_queue.json`, failing open to the old behaviour.

FM9 -- the confirmer lane could not see the singular `claim_id` form.
    The GOV-CONFIRM-1 anti-double-spawn set was an inline comprehension over
    `claim_ids` only. Singular `claim_id` is the COMMON form (7 of 8 live entries
    on 2026-08-03), so "Confirm evidence: SD-014" stayed `ready` while V3-EXQ-887
    -- `claim_id: "SD-014"`, no `claim_ids` -- sat pending. This is the SAME
    defect a 2026-06-04 audit fixed in `_queued_retest_coverage`, never propagated
    to this lane. Fix: `_confirmer_queued_claims` delegates to that one parser.
    NOTE this is the opposite of the diagnosis the chip proposed (it read
    `claim_ids: null` as "unreadable"); the entry is perfectly readable, the
    CONSUMER was looking at the wrong field.

SCOPED OUT, deliberately, and recorded here so nobody re-investigates:
  * "Confirm evidence: MECH-203" is genuinely NOT queued and has no
    generator-visible blocker -- its proposal EXP-0495 is `executed`. It was
    adjudicated blocked by chip-20260803-igw-confirm-mech203, a judgement that
    lives in the chip ledger only. No predicate over this generator's inputs can
    reach it; suppressing it would need a new input, not a new veto.
  * "Proposal for MECH-472" self-resolved: proposals EXP-0068 / EXP-0400 both
    reached `executed`, so the proposals lane already suppresses it.

NEGATIVE CONTROLS are the point of this file, not decoration. The 2026-08-03
substrate-lane fix (FM3) and this one are both suppression changes, and a
suppression change that over-fires is strictly worse than the staleness it
replaces -- it hides real work instead of showing stale work.
`NotYetQueuedClaimStillSurfacesTest` and `NegativeControlsTest` are what
distinguish a fix from a mute.

Time-independent: no clock, no network, no sleep. `CommittedSnapshotReadTest`
builds a real throwaway git repo in a tempdir (local refs only -- no fetch, no
remote), which is what makes the FM8 fix genuinely covered rather than only its
merge helper.

Run: /opt/local/bin/python3 scripts/test_generate_inter_governance_workset_experiment_lane_staleness.py
"""

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent


def _load_generator():
    path = SCRIPTS_DIR / "generate_inter_governance_workset.py"
    spec = importlib.util.spec_from_file_location(
        "ree_igw_generator_experiment_lane_staleness_test", path
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


G = _load_generator()


# --- fixtures ---------------------------------------------------------------
# Shapes taken verbatim from the live queue on 2026-08-03. The mix matters: the
# defect was invisible precisely because the LIST form (436d) worked while the
# far more common SINGULAR form (887) did not.

ENTRY_LIST_FORM = {           # V3-EXQ-436d: claim_ids list, no singular
    "queue_id": "V3-EXQ-436d",
    "status": "pending",
    "claim_ids": ["SD-017", "ARC-045", "MECH-166"],
}
ENTRY_SINGULAR_FORM = {       # V3-EXQ-887: singular claim_id, claim_ids ABSENT
    "queue_id": "V3-EXQ-887",
    "status": "pending",
    "claim_id": "SD-014",
}
ENTRY_SINGULAR_NULL_LIST = {  # same, but claim_ids explicitly null
    "queue_id": "V3-EXQ-873a",
    "status": "pending",
    "claim_ids": None,
    "claim_id": "MECH-322",
}
ENTRY_BOTH_FORMS = {
    "queue_id": "V3-EXQ-999",
    "status": "pending",
    "claim_ids": ["MECH-001"],
    "claim_id": "MECH-002",
}

INCIDENT_QUEUE = [
    {"queue_id": "V3-EXQ-875a", "status": "claimed", "claim_id": "MECH-471"},
    ENTRY_SINGULAR_FORM,
    {"queue_id": "V3-EXQ-848b", "status": "claimed", "claim_ids": ["ARC-005"]},
    ENTRY_SINGULAR_NULL_LIST,
    {"queue_id": "V3-EXQ-882a", "status": "pending", "claim_ids": ["MECH-472"]},
    {"queue_id": "V3-EXQ-867b", "status": "claimed", "claim_id": "MECH-321"},
    ENTRY_LIST_FORM,
    {"queue_id": "V3-EXQ-149b", "status": "claimed", "claim_ids": ["Q-004"]},
]

# What the 26-commits-behind working tree actually held on the incident box.
STALE_WORKTREE_QUEUE = [
    {"queue_id": "V3-EXQ-149b", "status": "claimed", "claim_ids": ["Q-004"]},
    {"queue_id": "V3-EXQ-867b", "status": "pending", "claim_id": "MECH-321"},
]


class ConfirmerQueuedClaimsReadsBothFormsTest(unittest.TestCase):
    """FM9: the confirmer gate must see singular `claim_id`, not only `claim_ids`."""

    def test_singular_claim_id_is_seen(self):
        got = G._confirmer_queued_claims([ENTRY_SINGULAR_FORM])
        self.assertIn(
            "SD-014", got,
            "FM9 regression: V3-EXQ-887 carries claim_id='SD-014' with no "
            "claim_ids, so a claim_ids-only reader misses it and 'Confirm "
            "evidence: SD-014' renders ready while its confirmer is queued.",
        )

    def test_singular_survives_explicit_null_claim_ids(self):
        # `claim_ids: null` must not short-circuit the singular read.
        self.assertIn("MECH-322", G._confirmer_queued_claims([ENTRY_SINGULAR_NULL_LIST]))

    def test_list_form_still_seen(self):
        got = G._confirmer_queued_claims([ENTRY_LIST_FORM])
        self.assertEqual({"SD-017", "ARC-045", "MECH-166"}, got)

    def test_both_forms_on_one_entry_are_unioned(self):
        self.assertEqual({"MECH-001", "MECH-002"},
                         G._confirmer_queued_claims([ENTRY_BOTH_FORMS]))

    def test_incident_board_covers_every_queued_claim(self):
        got = G._confirmer_queued_claims(INCIDENT_QUEUE)
        for cid in ("SD-014", "ARC-045", "MECH-472", "MECH-321", "MECH-322",
                    "MECH-471", "ARC-005", "SD-017", "MECH-166", "Q-004"):
            self.assertIn(cid, got, f"{cid} is queued on the incident board")

    def test_entries_without_any_claim_reference_are_ignored(self):
        self.assertEqual(set(), G._confirmer_queued_claims(
            [{"queue_id": "V3-EXQ-000", "status": "pending"}]))

    def test_malformed_entries_do_not_raise(self):
        self.assertEqual(set(), G._confirmer_queued_claims(
            ["not-a-dict", None, {}, {"claim_id": "X"}]))  # no queue_id -> skipped


class NotYetQueuedClaimStillSurfacesTest(unittest.TestCase):
    """NEGATIVE CONTROL -- the assertion that separates a fix from a mute.

    MECH-191 was `ready` in the incident workset and is genuinely NOT in the
    queue. If a broadened suppression ever swallows it, the confirmer lane has
    stopped surfacing real work and this must fail.
    """

    def test_unqueued_claim_is_not_suppressed(self):
        got = G._confirmer_queued_claims(INCIDENT_QUEUE)
        self.assertNotIn("MECH-191", got)
        self.assertNotIn("MECH-203", got)  # scoped out: unqueued, blocked elsewhere
        self.assertNotIn("MECH-074", got)

    def test_empty_queue_suppresses_nothing(self):
        self.assertEqual(set(), G._confirmer_queued_claims([]))


class ConfirmerAndRetestLanesAgreeTest(unittest.TestCase):
    """The two lanes must share ONE parser -- that is the whole FM9 fix.

    They drifted for two months because each read the queue itself. Asserting
    equality (not just correctness) is what stops a later session reintroducing a
    second inline reader in either lane.
    """

    def test_sets_are_identical_on_the_incident_board(self):
        self.assertEqual(
            set(G._queued_retest_coverage(INCIDENT_QUEUE)),
            G._confirmer_queued_claims(INCIDENT_QUEUE),
        )

    def test_sets_are_identical_on_mixed_shapes(self):
        board = [ENTRY_LIST_FORM, ENTRY_SINGULAR_FORM, ENTRY_BOTH_FORMS,
                 ENTRY_SINGULAR_NULL_LIST]
        self.assertEqual(set(G._queued_retest_coverage(board)),
                         G._confirmer_queued_claims(board))


class MergeQueueSnapshotsTest(unittest.TestCase):
    """FM8: union semantics of the working tree and the committed snapshot."""

    def test_committed_entries_are_included(self):
        merged = G._merge_queue_snapshots(STALE_WORKTREE_QUEUE, INCIDENT_QUEUE)
        self.assertEqual(8, len(merged))
        self.assertIn("V3-EXQ-436d", {i["queue_id"] for i in merged})
        self.assertIn("V3-EXQ-887", {i["queue_id"] for i in merged})

    def test_no_duplicate_queue_ids(self):
        merged = G._merge_queue_snapshots(STALE_WORKTREE_QUEUE, INCIDENT_QUEUE)
        qids = [i["queue_id"] for i in merged]
        self.assertEqual(len(qids), len(set(qids)))

    def test_committed_body_wins_on_conflict(self):
        # 867b is `pending` in the stale worktree and `claimed` on origin. The
        # committed snapshot is the coordinator's phase3-written truth.
        merged = G._merge_queue_snapshots(STALE_WORKTREE_QUEUE, INCIDENT_QUEUE)
        entry = next(i for i in merged if i["queue_id"] == "V3-EXQ-867b")
        self.assertEqual("claimed", entry["status"])

    def test_worktree_only_entry_is_kept(self):
        """An experiment queued locally and not yet pushed still counts as queued."""
        local = [{"queue_id": "V3-EXQ-NEW", "status": "pending", "claim_id": "MECH-999"}]
        merged = G._merge_queue_snapshots(local, INCIDENT_QUEUE)
        self.assertIn("V3-EXQ-NEW", {i["queue_id"] for i in merged})
        self.assertIn("MECH-999", G._confirmer_queued_claims(merged))

    def test_empty_committed_snapshot_preserves_worktree(self):
        merged = G._merge_queue_snapshots(STALE_WORKTREE_QUEUE, [])
        self.assertEqual(2, len(merged))


class IncidentReplayTest(unittest.TestCase):
    """The exact 2026-08-03 board: stale worktree vs committed snapshot.

    Asserts the claim coverage each input yields, which is precisely what the
    retest and confirmer lanes consume.
    """

    def test_stale_worktree_alone_misses_the_queued_work(self):
        got = G._confirmer_queued_claims(STALE_WORKTREE_QUEUE)
        for cid in ("ARC-045", "SD-014", "MECH-472"):
            self.assertNotIn(cid, got, "pre-fix behaviour: the stale checkout "
                                       "cannot see these, hence the false 'ready'")

    def test_merged_snapshot_sees_all_of_it(self):
        merged = G._merge_queue_snapshots(STALE_WORKTREE_QUEUE, INCIDENT_QUEUE)
        got = G._confirmer_queued_claims(merged)
        for cid in ("ARC-045", "SD-014", "MECH-472"):
            self.assertIn(cid, got)
        # ...and the retest lane's own absorber agrees.
        coverage = G._queued_retest_coverage(merged)
        self.assertEqual("V3-EXQ-436d", coverage["ARC-045"])
        self.assertEqual("V3-EXQ-887", coverage["SD-014"])

    def test_queue_depth_premise_is_repaired(self):
        """IGW-206 claimed '0 pending' against 4 genuinely-pending items."""
        def unclaimed_pending(items):
            return [i for i in items
                    if i.get("status") == "pending" and not i.get("claimed_by")]

        self.assertLess(len(unclaimed_pending(STALE_WORKTREE_QUEUE)), 3,
                        "stale input fires the 'queue depth low' item")
        merged = G._merge_queue_snapshots(STALE_WORKTREE_QUEUE, INCIDENT_QUEUE)
        self.assertGreaterEqual(len(unclaimed_pending(merged)), 3,
                                "merged input does not -- the premise was false")


class CommittedSnapshotReadTest(unittest.TestCase):
    """FM8 end-to-end: read the queue from a real git ref, and fail open.

    Builds a throwaway repo in a tempdir with a local branch standing in for the
    remote-tracking ref. No network, no fetch, no clock.
    """

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name) / "ree-v3"
        self.repo.mkdir()
        self._git("init", "-q", "-b", "main")
        self._git("config", "user.email", "test@example.com")
        self._git("config", "user.name", "Test")
        self._orig_queue_path = G.REE_V3_QUEUE
        G.REE_V3_QUEUE = self.repo / "experiment_queue.json"

    def tearDown(self):
        G.REE_V3_QUEUE = self._orig_queue_path
        self._tmp.cleanup()

    def _git(self, *args):
        env = dict(os.environ, GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_SYSTEM=os.devnull)
        return subprocess.run(["git", "-C", str(self.repo), *args],
                              capture_output=True, text=True, env=env, check=True)

    def _write_queue(self, items):
        (self.repo / "experiment_queue.json").write_text(
            json.dumps({"items": items}, indent=2), encoding="utf-8")

    def _commit_queue(self, items, ref="committed"):
        self._write_queue(items)
        self._git("add", "experiment_queue.json")
        self._git("commit", "-q", "-m", "queue")
        self._git("branch", "-f", ref, "HEAD")

    def test_reads_the_committed_ref_not_the_working_tree(self):
        self._commit_queue(INCIDENT_QUEUE)
        self._write_queue(STALE_WORKTREE_QUEUE)  # dirty the tree afterwards
        committed = G._queue_from_git(ref="committed")
        self.assertIsNotNone(committed)
        self.assertEqual(8, len(committed))
        self.assertEqual(2, len(G._queue_from_worktree()))

    def test_load_queue_merges_both(self):
        """End-to-end through the real _load_queue, with only the ref redirected."""
        self._commit_queue(INCIDENT_QUEUE)
        self._write_queue(STALE_WORKTREE_QUEUE)
        orig = G._queue_from_git
        try:
            G._queue_from_git = lambda ref="committed": orig(ref="committed")
            merged = G._load_queue()
        finally:
            G._queue_from_git = orig
        self.assertEqual(8, len(merged))
        self.assertIn("SD-014", G._confirmer_queued_claims(merged))

    def test_missing_ref_returns_none_not_empty(self):
        """None and [] must stay distinguishable, or fail-open collapses into
        'the queue is empty' -- which suppresses nothing and un-fixes FM8."""
        self._commit_queue(INCIDENT_QUEUE)
        self.assertIsNone(G._queue_from_git(ref="no-such-ref"))

    def test_load_queue_fails_open_to_the_working_tree(self):
        self._commit_queue(INCIDENT_QUEUE)
        self._write_queue(STALE_WORKTREE_QUEUE)
        orig = G._queue_from_git
        try:
            G._queue_from_git = lambda *a, **k: None   # simulate git unavailable
            self.assertEqual(2, len(G._load_queue()))
        finally:
            G._queue_from_git = orig

    def test_non_git_directory_returns_none(self):
        with tempfile.TemporaryDirectory() as d:
            qp = Path(d) / "experiment_queue.json"
            qp.write_text(json.dumps({"items": []}), encoding="utf-8")
            orig = G.REE_V3_QUEUE
            try:
                G.REE_V3_QUEUE = qp
                self.assertIsNone(G._queue_from_git())
            finally:
                G.REE_V3_QUEUE = orig

    def test_unparseable_blob_returns_none(self):
        (self.repo / "experiment_queue.json").write_text("{not json", encoding="utf-8")
        self._git("add", "experiment_queue.json")
        self._git("commit", "-q", "-m", "broken")
        self._git("branch", "-f", "committed", "HEAD")
        self.assertIsNone(G._queue_from_git(ref="committed"))


class NegativeControlsTest(unittest.TestCase):
    """Guards against the failure mode this fix could itself introduce."""

    def test_merge_never_invents_claims(self):
        merged = G._merge_queue_snapshots(STALE_WORKTREE_QUEUE, INCIDENT_QUEUE)
        from_inputs = (G._confirmer_queued_claims(STALE_WORKTREE_QUEUE)
                       | G._confirmer_queued_claims(INCIDENT_QUEUE))
        self.assertEqual(from_inputs, G._confirmer_queued_claims(merged),
                         "the merge must be a pure union -- no claim may appear "
                         "that neither snapshot named")

    def test_merge_never_drops_a_claim_either_snapshot_named(self):
        merged = G._merge_queue_snapshots(STALE_WORKTREE_QUEUE, INCIDENT_QUEUE)
        got = G._confirmer_queued_claims(merged)
        for cid in G._confirmer_queued_claims(STALE_WORKTREE_QUEUE):
            self.assertIn(cid, got)

    def test_retest_coverage_docstring_contract_is_untouched(self):
        """FM9 changed the CONSUMER, not the parser. If someone 'simplifies'
        _queued_retest_coverage to a claim_ids-only read, both lanes break at
        once now that they share it -- so pin its behaviour here too."""
        self.assertEqual({"SD-014": "V3-EXQ-887"},
                         G._queued_retest_coverage([ENTRY_SINGULAR_FORM]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
