#!/usr/bin/env python3
"""Contract tests: EXP-/LIT- proposal ids are STABLE across regens.

THE PROPERTY UNDER TEST. Regenerating over an unchanged proposal set must
produce byte-identical proposal_ids, and a regen that ADDS or RETIRES proposals
must leave every OTHER proposal_id untouched. Nothing pinned this before, and
it was violated continuously.

INCIDENT. `proposal_id` was handed out by a bare monotonic counter walking
`backlog_items` in sort order, so the id was POSITIONAL -- adding or retiring
one proposal renumbered every proposal after it.

  * 2026-09-02, REE_assembly 275bc8d0b4: a lit-pull regen that legitimately
    dropped exactly ONE proposal (LIT-0520) moved 718 of 916 backlog_ids to a
    different proposal_id, with zero backlog_ids added or removed.
  * 2026-09-03, REE_assembly 64cf65ce3e: +359/-360 ids churned in one rebuild.
  * 2026-09-04: of the 181 open chip-proposal-exp-* chips minted 2026-09-02,
    122 named an EXP id that no longer existed and 50 named an id whose claim
    had MOVED -- the silent direction, where a stale reference resolves to a
    different claim rather than failing loudly. All 172 were withdrawn.

EXP-/LIT- ids are referenced from outside the proposal files -- TASK_CHIPS.json
(496 references at the time of measurement), igw_routine_ledger.json,
igw_assignments.json, failure-autopsy artifacts, structure_review dossiers,
planning prose -- so every renumber silently re-points all of them.

WHY CARRY-FORWARD RATHER THAN A CONTENT HASH. A content-derived id would
renumber the entire corpus exactly once, invalidating all ~570 external
references in a single step -- strictly worse than the drift it cures. The
allocation is instead PERSISTED and keyed on the stable identity
(backlog_id, lane), and the first run on a tree with no sidecar adopts the ids
already on disk. That adoption is the migration, and it is what the
`test_seed_adopts_existing_ids_verbatim` case pins.

Run: /opt/local/bin/python3 scripts/test_proposal_id_stability.py
"""

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

INDEXER_PATH = (
    Path(__file__).resolve().parents[1]
    / "evidence" / "experiments" / "scripts" / "build_experiment_indexes.py"
)


def _load_indexer():
    spec = importlib.util.spec_from_file_location("ree_indexer_pidstab", INDEXER_PATH)
    mod = importlib.util.module_from_spec(spec)
    # Register before exec so @dataclass can resolve the module via sys.modules.
    sys.modules["ree_indexer_pidstab"] = mod
    spec.loader.exec_module(mod)
    return mod


IDX = _load_indexer()


def _item(backlog_id, proposal_id, proposal_type):
    return {
        "backlog_id": backlog_id,
        "proposal_id": proposal_id,
        "proposal_type": proposal_type,
        "claim_id": "MECH-001",
    }


def _mint(allocator, backlog_ids, *, lanes=("experimental", "literature")):
    """Simulate one regen: walk the backlog and mint an id per (item, lane).

    Mirrors main()'s two mint sites, which is the whole reason the allocator is
    a module-level class rather than a closure.
    """
    out = {}
    for bid in backlog_ids:
        for lane in lanes:
            prefix = "EXP" if lane == "experimental" else "LIT"
            out[(bid, lane)] = f"{prefix}-{allocator.assign(bid, lane):04d}"
    return out


class TestUnchangedSetIsByteIdentical(unittest.TestCase):
    """The headline contract: same set in, same ids out."""

    def test_regen_over_unchanged_set_reproduces_every_id(self):
        backlog = [f"EVB-{n:04d}" for n in range(1, 25)]

        first = _mint(IDX.ProposalIdAllocator(), backlog)
        # Second regen starts from the persisted allocation the first produced.
        alloc = IDX.ProposalIdAllocator()
        _mint(alloc, backlog)
        second = _mint(IDX.ProposalIdAllocator(alloc.allocations), backlog)

        self.assertEqual(first, second)

    def test_regen_is_order_independent(self):
        """Re-sorting the backlog must not move a single id.

        The positional counter was sensitive to sort order as well as to set
        size -- `backlog_items` is sorted on conflict_ratio, which moves as
        evidence lands, so ids drifted even when nothing was added or removed.
        """
        backlog = [f"EVB-{n:04d}" for n in range(1, 25)]
        alloc = IDX.ProposalIdAllocator()
        first = _mint(alloc, backlog)

        reshuffled = list(reversed(backlog))
        second = _mint(IDX.ProposalIdAllocator(alloc.allocations), reshuffled)

        self.assertEqual(first, second)


class TestAddAndRetireLeaveOthersAlone(unittest.TestCase):
    """The measured failure mode, both directions."""

    def test_retiring_one_proposal_moves_no_other_id(self):
        backlog = [f"EVB-{n:04d}" for n in range(1, 25)]
        alloc = IDX.ProposalIdAllocator()
        before = _mint(alloc, backlog)

        # Drop one from the MIDDLE -- the positional counter renumbered
        # everything after the gap.
        survivors = [b for b in backlog if b != "EVB-0012"]
        after = _mint(IDX.ProposalIdAllocator(alloc.allocations), survivors)

        for key, pid in after.items():
            self.assertEqual(before[key], pid, f"{key} moved: {before[key]} -> {pid}")

    def test_adding_one_proposal_moves_no_other_id(self):
        backlog = [f"EVB-{n:04d}" for n in range(1, 25)]
        alloc = IDX.ProposalIdAllocator()
        before = _mint(alloc, backlog)

        grown = backlog + ["EVB-0500"]
        after = _mint(IDX.ProposalIdAllocator(alloc.allocations), grown)

        for key, pid in before.items():
            self.assertEqual(pid, after[key], f"{key} moved: {pid} -> {after[key]}")
        self.assertNotIn(after[("EVB-0500", "experimental")], set(before.values()))

    def test_a_retired_id_is_never_recycled(self):
        """A retired proposal's index is burnt, not handed to someone else.

        Recycling is what turns a stale external reference from DANGLING (loud,
        someone notices) into POINTING AT A DIFFERENT CLAIM (silent) -- the
        50-chip half of the 2026-09-04 measurement. One permanently-burnt index
        per retirement is the intended cost.
        """
        alloc = IDX.ProposalIdAllocator()
        first = _mint(alloc, ["EVB-0001", "EVB-0002", "EVB-0003"])
        retired = first[("EVB-0002", "experimental")]

        second_alloc = IDX.ProposalIdAllocator(alloc.allocations)
        second = _mint(second_alloc, ["EVB-0001", "EVB-0003", "EVB-0009"])

        self.assertNotIn(retired, set(second.values()))

    def test_a_retired_proposal_that_returns_gets_its_id_back(self):
        alloc = IDX.ProposalIdAllocator()
        first = _mint(alloc, ["EVB-0001", "EVB-0002", "EVB-0003"])

        gone = IDX.ProposalIdAllocator(alloc.allocations)
        _mint(gone, ["EVB-0001", "EVB-0003"])
        back = _mint(IDX.ProposalIdAllocator(gone.allocations),
                     ["EVB-0001", "EVB-0002", "EVB-0003"])

        self.assertEqual(first[("EVB-0002", "experimental")],
                         back[("EVB-0002", "experimental")])


class TestTwinLanesDoNotCollide(unittest.TestCase):
    """backlog_id is stable but NOT unique -- see _proposal_lane."""

    def test_experimental_and_literature_twins_get_distinct_indices(self):
        alloc = IDX.ProposalIdAllocator()
        exp = alloc.assign("EVB-0001", "experimental")
        lit = alloc.assign("EVB-0001", "literature")
        self.assertNotEqual(exp, lit)

    def test_lane_spelling_is_normalised_through_the_seed(self):
        """A manual `literature` and a generated `literature_review` are one key.

        Without normalisation a manual literature proposal's id would stop
        carrying forward the moment this key went in -- turning a lane mix-up
        into a silent renumber, the strictly worse direction.
        """
        alloc = IDX.ProposalIdAllocator()
        alloc.seed_from_items([_item("EVB-0001", "LIT-0042", "literature")])
        self.assertEqual(alloc.assign("EVB-0001", "literature"), 42)


class TestSeedIsALosslessMigration(unittest.TestCase):
    def test_seed_adopts_existing_ids_verbatim(self):
        """First run on a tree with no sidecar must not renumber anything."""
        existing = [
            _item("EVB-0001", "EXP-0007", "experimental"),
            _item("EVB-0001", "LIT-0008", "literature_review"),
            _item("EVB-0002", "EXP-0019", "experimental"),
        ]
        alloc = IDX.ProposalIdAllocator()
        alloc.seed_from_items(existing)
        minted = _mint(alloc, ["EVB-0001", "EVB-0002"])

        self.assertEqual(minted[("EVB-0001", "experimental")], "EXP-0007")
        self.assertEqual(minted[("EVB-0001", "literature")], "LIT-0008")
        self.assertEqual(minted[("EVB-0002", "experimental")], "EXP-0019")

    def test_sidecar_wins_over_the_proposals_file(self):
        """The persisted map is authoritative; the file only fills gaps."""
        alloc = IDX.ProposalIdAllocator({"EVB-0001|experimental": 7})
        alloc.seed_from_items([_item("EVB-0001", "EXP-0999", "experimental")])
        self.assertEqual(alloc.assign("EVB-0001", "experimental"), 7)

    def test_manual_ids_are_reserved_but_not_adopted(self):
        """A hand-assigned manual id blocks its index without becoming the key's.

        Adopting it would stamp a freshly generated auto proposal with the
        manual proposal's id -- a duplicate, which is the failure the
        pre-existing manual-reservation block already exists to prevent.
        """
        alloc = IDX.ProposalIdAllocator(reserved_idx={85})
        alloc.seed_from_items(
            [_item("EVB-0001", "EXP-0085", "experimental")],
            exclude_ids={"EXP-0085"},
        )
        idx = alloc.assign("EVB-0001", "experimental")
        self.assertNotEqual(idx, 85)

    def test_items_without_a_backlog_id_are_skipped(self):
        alloc = IDX.ProposalIdAllocator()
        alloc.seed_from_items([{"proposal_id": "EXP-0003", "proposal_type": "experimental"}])
        self.assertEqual(alloc.allocations, {})


class TestSidecarRoundTrip(unittest.TestCase):
    def test_load_returns_empty_when_absent(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertEqual(IDX.load_proposal_id_allocations(Path(td)), {})

    def test_load_fails_soft_on_malformed_json(self):
        """A corrupt sidecar must never block a regen -- the seed re-derives it."""
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / IDX._PROPOSAL_ID_ALLOC_FILENAME
            p.write_text("{not json", encoding="utf-8")
            self.assertEqual(IDX.load_proposal_id_allocations(Path(td)), {})

    def test_load_reads_back_what_the_indexer_writes(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / IDX._PROPOSAL_ID_ALLOC_FILENAME
            p.write_text(
                json.dumps({"allocations": {"EVB-0001|experimental": 7}}),
                encoding="utf-8",
            )
            self.assertEqual(
                IDX.load_proposal_id_allocations(Path(td)),
                {"EVB-0001|experimental": 7},
            )


class TestNoDuplicateIdsWithinOneRegen(unittest.TestCase):
    def test_every_minted_id_is_distinct(self):
        alloc = IDX.ProposalIdAllocator(reserved_idx={3, 4, 5})
        minted = _mint(alloc, [f"EVB-{n:04d}" for n in range(1, 40)])
        self.assertEqual(len(set(minted.values())), len(minted))

    def test_reserved_indices_are_never_handed_out(self):
        alloc = IDX.ProposalIdAllocator(reserved_idx={1, 2, 3})
        self.assertEqual(alloc.assign("EVB-0001", "experimental"), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
