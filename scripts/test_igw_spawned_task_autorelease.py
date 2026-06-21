#!/usr/bin/env python3
"""Contract tests for the spawned_task auto-release reconcile in
generate_inter_governance_workset.py (added 2026-06-21, follow-up to the
Gap-2 spawned_task assignment mirror, session igw-chip-spawned-task-assign).

End-of-skill spawn_task chips are mirrored into igw_assignments.json under
agent kind "spawned_task". Until now that mirror was only released manually
(dismiss_task -> igw_chip_assign.py release). When the chipped work actually
LANDS, the underlying workset item drops out of the `ready` set but the
spawned_task assignment lingered as active -- keeping the IGW auto-spawn
routine skipping it forever and showing a stale "assigned" chip.

reconcile_spawned_task_assignments(items, now_iso=...) releases every active
spawned_task assignment whose stable_hash is no longer a `ready` workset item,
and leaves still-ready ones and other agents' assignments untouched. It must be
idempotent.

Run: /opt/local/bin/python3 scripts/test_igw_spawned_task_autorelease.py
"""

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
# igw_assignments_lib is imported by name inside the reconcile function, so the
# scripts dir must be importable.
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import igw_assignments_lib as ial  # noqa: E402


def _load_generator():
    path = SCRIPTS_DIR / "generate_inter_governance_workset.py"
    spec = importlib.util.spec_from_file_location("ree_igw_generator", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["ree_igw_generator"] = mod
    spec.loader.exec_module(mod)
    return mod


GEN = _load_generator()

# The append-only ledger collapses by latest assigned_at, so a release must be
# timestamped AFTER its assign (production satisfies this: the chip is assigned
# in an earlier session than the reconcile's workset-regen `generated` time).
ASSIGN_TS = "2026-06-21T07:00:00Z"
RECONCILE_TS = "2026-06-21T08:00:00Z"


def _item(iid, claim, status):
    """Minimal workset item with the fields stable_hash_item keys on."""
    it = {
        "id": iid,
        "title": f"Work item {iid}",
        "skill": "/queue-experiment",
        "lane": "experiment",
        "priority": 28,
        "owner_exq": None,
        "gap_ids": [],
        "claim_ids": [claim],
        "status": status,
    }
    it["stable_hash"] = ial.stable_hash_item(it)
    return it


class SpawnedTaskAutoReleaseTest(unittest.TestCase):
    def setUp(self):
        # Redirect the ledger to a throwaway temp file so the real
        # evidence/planning/igw_assignments.json is never touched.
        self._tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        )
        self._tmp.close()
        self._orig_path = ial.ASSIGNMENTS
        ial.ASSIGNMENTS = Path(self._tmp.name)
        ial.save({
            "schema_version": "igw_assignments/v1",
            "agent_kinds": sorted(ial.VALID_AGENTS),
            "entries": [],
        })

    def tearDown(self):
        ial.ASSIGNMENTS = self._orig_path
        Path(self._tmp.name).unlink(missing_ok=True)

    def _active_spawned_hashes(self):
        return {
            e["stable_hash"]
            for e in ial.active_entries()
            if e.get("agent") == "spawned_task"
        }

    def _active_agent_hashes(self, agent):
        return {
            e["stable_hash"]
            for e in ial.active_entries()
            if e.get("agent") == agent
        }

    def test_releases_only_non_ready_spawned_tasks(self):
        ready = _item("IGW-1", "ARC-100", "ready")
        blocked = _item("IGW-2", "ARC-200", "blocked")
        gone = _item("IGW-3", "ARC-300", "ready")  # assigned, then removed
        other = _item("IGW-4", "ARC-400", "blocked")  # claude_local, not ours

        # Mirror chips for the three spawned_task items.
        for it in (ready, blocked, gone):
            ial.assign(it, agent="spawned_task", source="session_land_chip", now_iso=ASSIGN_TS)
        # A different agent on a non-ready item must NOT be touched.
        ial.assign(other, agent="claude_local", source="igw_routine_tick", now_iso=ASSIGN_TS)

        # The workset this regen produced: `gone` has left entirely; `blocked`
        # and `other` are present but not ready.
        items = [ready, blocked, other]

        released = GEN.reconcile_spawned_task_assignments(
            items, now_iso=RECONCILE_TS
        )

        self.assertEqual(
            set(released), {blocked["stable_hash"], gone["stable_hash"]}
        )
        # Only the still-ready spawned_task survives.
        self.assertEqual(
            self._active_spawned_hashes(), {ready["stable_hash"]}
        )
        # The claude_local assignment is untouched.
        self.assertEqual(
            self._active_agent_hashes("claude_local"), {other["stable_hash"]}
        )
        # The release entries carry the agreed reason/actor.
        rels = [e for e in ial.load()["entries"] if e.get("released_at")]
        self.assertTrue(rels)
        for e in rels:
            self.assertEqual(e["released_by"], "reconcile")
            self.assertEqual(e["released_reason"], "work_landed_or_item_gone")

    def test_idempotent(self):
        blocked = _item("IGW-2", "ARC-200", "blocked")
        ial.assign(blocked, agent="spawned_task", source="session_land_chip", now_iso=ASSIGN_TS)
        items = [blocked]

        first = GEN.reconcile_spawned_task_assignments(
            items, now_iso=RECONCILE_TS
        )
        self.assertEqual(set(first), {blocked["stable_hash"]})

        before = json.dumps(ial.load(), sort_keys=True)
        second = GEN.reconcile_spawned_task_assignments(
            items, now_iso="2026-06-21T09:00:00Z"
        )
        after = json.dumps(ial.load(), sort_keys=True)

        self.assertEqual(second, [])  # nothing left to release
        self.assertEqual(before, after)  # ledger byte-identical

    def test_all_ready_releases_nothing(self):
        a = _item("IGW-1", "ARC-100", "ready")
        b = _item("IGW-2", "ARC-200", "ready")
        for it in (a, b):
            ial.assign(it, agent="spawned_task", source="session_land_chip", now_iso=ASSIGN_TS)

        released = GEN.reconcile_spawned_task_assignments(
            [a, b], now_iso=RECONCILE_TS
        )
        self.assertEqual(released, [])
        self.assertEqual(
            self._active_spawned_hashes(),
            {a["stable_hash"], b["stable_hash"]},
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
