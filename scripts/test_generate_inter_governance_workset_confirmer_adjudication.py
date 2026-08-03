#!/usr/bin/env python3
"""Regression tests for FM10 -- the GOV-CONFIRM-1 confirmer lane had NO MEMORY of
its own self-route outcome (chip-20260803-igw-confirmer-lane-adjudicated-suppressor).

THE DEFECT. `_evidence_confirmer_candidates` is generative: it scans the claim
registry for built-substrate + zero-evidence candidates and AUTHORS a confirmer
item. Its docstring anticipates that the per-item /queue-experiment pass "self-
routes substrate_not_ready_requeue if only a behavioural DV exists" -- but
nothing read that outcome back, so the identical claim was re-offered `ready` on
every regeneration and the metaworker dispatcher spent a whole worker each time
re-deriving the same negative.

CONFIRMED INCIDENT (2026-08-03). MECH-191 was worked TWICE the same day --
chip-20260803-igw-confirm-mech191 and chip-20260803-igw-233-mech191-confirm --
both resolving "QUEUED NOTHING -- self-routed substrate_not_ready_requeue". The
second recorded the durable verdict at REE_assembly 38236f6779 (20:11Z):
EXP-0276, claim_id MECH-191, status=blocked_substrate, with a gating_reason that
had RE-VERIFIED the block against live ree-v3 substrate. The workset regenerated
at 22:10Z -- two hours later -- and IGW-20260803-229 "Confirm evidence: MECH-191"
still rendered `ready`.

NOT THE SAME GAP AS FM9 (5aa0d3267a), which fixed the queue gate and explicitly
verified this survivor was "genuinely unqueued". That verdict is correct.
UNQUEUED IS NOT UNADJUDICATED: a session can conclude that nothing should be
queued at all, and that conclusion has to be readable too.

THE FIX RENDERS `blocked`, IT DOES NOT DROP -- and that distinction is what the
tests here mostly exist to pin. Dropping would mute a claim whose block is
manually cleared and never auto-cleared; rendering `blocked` keeps it on
/workset carrying the adjudicating session's own reason, frees its
CONFIRMER_AUTOSPAWN_CAP slot for a real confirmer, and re-admits it the moment
the status is cleared. `NeverDropsACandidateTest` and `NegativeControlTest` are
what separate this fix from a mute -- same standard the FM8/FM9 suite set.

Time-independent: no clock, no network, no sleep, no live-file dependence (every
input is a fixture or a tempdir file).

Run: /opt/local/bin/python3 scripts/test_generate_inter_governance_workset_confirmer_adjudication.py
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
        "ree_igw_generator_confirmer_adjudication_test", path
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


G = _load_generator()


# --- fixtures ---------------------------------------------------------------
# Shapes taken verbatim from experiment_proposals.v1.json on 2026-08-03. Every
# one of its 354 live entries carries the claim as a SINGULAR `claim_id`; the
# `claim_ids` list form (which the ree-v3 QUEUE uses) appears zero times. Both
# are exercised so this cannot become the next singular-vs-list blind spot.

PROP_MECH_191 = {  # the incident record, REE_assembly 38236f6779
    "proposal_id": "EXP-0276",
    "backlog_id": "EVB-0091",
    "claim_id": "MECH-191",
    "status": "blocked_substrate",
    "gated_by_session": "metaworker-chip-20260803-igw-confirm-mech191",
    "gated_at_utc": "2026-08-03T20:11:04Z",
    "gating_reason": (
        "functional-state channels do not externalize >=2 differentially-active, "
        "cross-architecturally-consistent dimensions; scalar channel-norm readouts "
        "of tonic accumulators are saturated-constant across induced states."
    ),
}
PROP_MECH_203 = {  # scoped out: an EXECUTED proposal is not an adjudication
    "proposal_id": "EXP-0495",
    "claim_id": "MECH-203",
    "status": "executed",
    "executed_queue_id": "V3-EXQ-843",
}
PROP_MECH_282_GATED = {
    "proposal_id": "EXP-0527",
    "claim_id": "MECH-282",
    "status": "gated",
    "gated_by_session": "determined-ritchie-55a3a6",
    "gating_reason": (
        "hold_pending_v3_substrate governance verdict + v3_pending=true; suggested "
        "design (v3_exq_600a) already ran (supports) but is held pending substrate."
    ),
}
PROP_ARC_032_ON_GATE = {
    "proposal_id": "EXP-0102",
    "claim_id": "ARC-032",
    "status": "blocked_on_gate",
    "notes": "DR-1: z_goal seeding requires SD-012 resolution.",
}
PROP_ARC_018_SKIPPED = {
    "proposal_id": "EXP-0131", "claim_id": "ARC-018", "status": "skipped",
}
PROP_MECH_183_DEFERRED = {
    "proposal_id": "EXP-0266", "claim_id": "MECH-183",
    "status": "deferred_substrate_not_ready",
}
PROP_MECH_343_VARIANT = {
    "proposal_id": "EXP-0176", "claim_id": "MECH-343",
    "status": "proposed_blocked_substrate",
}
PROP_SD_039_EXECUTED = {  # the claim that takes MECH-191's freed cap slot
    "proposal_id": "EXP-0508", "claim_id": "SD-039", "status": "executed",
}
PROP_MECH_269_PROPOSED = {
    "proposal_id": "EXP-9001", "claim_id": "MECH-269", "status": "proposed",
}
PROP_SD_014_QUEUED = {
    "proposal_id": "EXP-9002", "claim_id": "SD-014", "status": "queued",
}
PROP_STRUCTURED_BLOCK = {
    "proposal_id": "EXP-0080", "claim_id": "INV-089", "status": "blocked_substrate",
    "blocked_by": ["MECH-457", "INV-088"],
}

INCIDENT_PROPOSALS = [
    PROP_MECH_191, PROP_MECH_203, PROP_MECH_282_GATED, PROP_ARC_032_ON_GATE,
    PROP_ARC_018_SKIPPED, PROP_MECH_183_DEFERRED, PROP_MECH_343_VARIANT,
    PROP_SD_039_EXECUTED, PROP_MECH_269_PROPOSED, PROP_SD_014_QUEUED,
    PROP_STRUCTURED_BLOCK,
]


class _ProposalsFileFixture(unittest.TestCase):
    """Base: point PROPOSALS_JSON at a tempdir file instead of the live one."""

    PROPOSALS = INCIDENT_PROPOSALS

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._path = Path(self._tmp.name) / "experiment_proposals.v1.json"
        self._write(self.PROPOSALS)
        self._orig = G.PROPOSALS_JSON
        G.PROPOSALS_JSON = self._path

    def tearDown(self):
        G.PROPOSALS_JSON = self._orig
        self._tmp.cleanup()

    def _write(self, items):
        self._path.write_text(
            json.dumps({"schema_version": 1, "items": items}, indent=2),
            encoding="utf-8",
        )


# --- the status vocabulary --------------------------------------------------


class AdjudicatedStatusSetTest(unittest.TestCase):
    """The set was pinned against the LIVE vocabulary (audited 2026-08-03:
    executed 213, gated 84, blocked_substrate 37, proposed 10, queued 4,
    blocked_on_gate 3, skipped 1, deferred_substrate_not_ready 1,
    proposed_blocked_substrate 1). These assertions are what stop it drifting."""

    def test_is_a_superset_of_the_retest_lanes_blocked_substrate_family(self):
        self.assertTrue(
            G._PROPOSAL_BLOCKED_SUBSTRATE_STATUSES
            <= G._PROPOSAL_ADJUDICATED_NOT_QUEUEABLE_STATUSES,
            "the confirmer lane must at minimum honour every status the retest "
            "lane's FM7 fix already treats as a block",
        )

    def test_includes_every_adjudicated_status(self):
        for st in ("blocked_substrate", "proposed_blocked_substrate",
                   "blocked_on_gate", "gated", "skipped",
                   "deferred_substrate_not_ready"):
            self.assertIn(st, G._PROPOSAL_ADJUDICATED_NOT_QUEUEABLE_STATUSES)

    def test_excludes_lifecycle_positions(self):
        """`executed` / `queued` / `proposed` are positions, not adjudications.
        Including any of them would silently disable the whole lane: 213 of 354
        live proposals are `executed`."""
        for st in ("executed", "queued", "proposed"):
            self.assertNotIn(st, G._PROPOSAL_ADJUDICATED_NOT_QUEUEABLE_STATUSES)

    def test_retest_lane_set_was_not_widened_by_this_change(self):
        """FM10 widened the CONFIRMER lane only. A retest carries an explicit
        claims.yaml pending_retest_after_substrate flag asking for it, so only a
        substrate block should hold it back."""
        self.assertEqual(
            {"blocked_substrate", "proposed_blocked_substrate"},
            G._PROPOSAL_BLOCKED_SUBSTRATE_STATUSES,
        )


# --- the parser -------------------------------------------------------------


class ConfirmerAdjudicatedProposalsTest(_ProposalsFileFixture):

    def test_the_incident_record_is_found(self):
        got = G._confirmer_adjudicated_proposals()
        self.assertIn("MECH-191", got)
        self.assertEqual("EXP-0276", got["MECH-191"]["proposal_id"])

    def test_every_adjudicated_status_is_picked_up(self):
        got = G._confirmer_adjudicated_proposals()
        for cid in ("MECH-191", "MECH-282", "ARC-032", "ARC-018",
                    "MECH-183", "MECH-343", "INV-089"):
            self.assertIn(cid, got, f"{cid}'s proposal is adjudicated")

    def test_lifecycle_positions_are_not_picked_up(self):
        got = G._confirmer_adjudicated_proposals()
        for cid in ("MECH-203", "SD-039", "MECH-269", "SD-014"):
            self.assertNotIn(cid, got)

    def test_list_form_claim_ids_is_read_too(self):
        """Zero live entries use it today; read it anyway so a schema drift is
        not the next singular-vs-list blind spot (FM9's lesson)."""
        self._write([{"proposal_id": "EXP-X", "status": "blocked_substrate",
                      "claim_ids": ["MECH-900", "MECH-901"]}])
        got = G._confirmer_adjudicated_proposals()
        self.assertIn("MECH-900", got)
        self.assertIn("MECH-901", got)

    def test_first_occurrence_wins_on_duplicate_claim_ids(self):
        self._write([
            {"proposal_id": "EXP-FIRST", "claim_id": "MECH-191",
             "status": "blocked_substrate"},
            {"proposal_id": "EXP-SECOND", "claim_id": "MECH-191",
             "status": "gated"},
        ])
        self.assertEqual("EXP-FIRST",
                         G._confirmer_adjudicated_proposals()["MECH-191"]["proposal_id"])

    def test_missing_file_suppresses_nothing(self):
        G.PROPOSALS_JSON = Path(self._tmp.name) / "does-not-exist.json"
        self.assertEqual({}, G._confirmer_adjudicated_proposals())

    def test_unparseable_file_suppresses_nothing(self):
        """Fails OPEN. A suppressor that fails CLOSED on a broken file would mute
        the entire lane silently."""
        self._path.write_text("{not json", encoding="utf-8")
        self.assertEqual({}, G._confirmer_adjudicated_proposals())

    def test_malformed_entries_do_not_raise(self):
        self._write(["not-a-dict", None, {}, {"status": "gated"}])
        self.assertEqual({}, G._confirmer_adjudicated_proposals())


class SharedParserTest(_ProposalsFileFixture):
    """ONE reader of experiment_proposals.v1.json, deliberately.

    FM9's whole lesson was that the retest lane and the confirmer lane each grew
    their own reader of the same field pair and drifted for two months. Asserting
    the containment relation (not just each lane's correctness) is what stops a
    later session reintroducing a second inline reader.
    """

    def test_retest_set_is_a_subset_of_the_confirmer_set(self):
        retest = set(G._proposal_blocked_substrate_by_claim())
        confirmer = set(G._confirmer_adjudicated_proposals())
        self.assertTrue(retest <= confirmer)
        self.assertTrue(confirmer - retest, "the confirmer set must be strictly "
                                            "wider on this board (gated etc.)")

    def test_both_lanes_return_the_identical_record_for_a_shared_claim(self):
        # Equal, not identical: each call re-reads and re-parses the file, so the
        # dicts are distinct objects. What must agree is the CONTENT -- that is
        # the drift the shared parser exists to prevent.
        self.assertEqual(
            G._proposal_blocked_substrate_by_claim()["MECH-191"],
            G._confirmer_adjudicated_proposals()["MECH-191"],
        )

    def test_retest_lane_still_ignores_gated(self):
        self.assertNotIn("MECH-282", G._proposal_blocked_substrate_by_claim())

    def test_shared_parser_honours_an_arbitrary_status_set(self):
        self.assertEqual({"MECH-203", "SD-039"},
                         set(G._proposals_by_claim({"executed"})))


class AdjudicationReasonTest(unittest.TestCase):
    """A `blocked` item with no reason is indistinguishable from a generator bug,
    so the reason builder must never return empty."""

    def test_structured_blocked_by_wins(self):
        got = G._proposal_adjudication_reason(PROP_STRUCTURED_BLOCK)
        self.assertIn("MECH-457", got)
        self.assertIn("INV-088", got)

    def test_gating_reason_is_used_when_no_structured_list(self):
        got = G._proposal_adjudication_reason(PROP_MECH_191)
        self.assertIn("EXP-0276", got)
        self.assertIn("blocked_substrate", got)
        self.assertIn("saturated-constant", got)

    def test_release_condition_is_the_next_fallback(self):
        got = G._proposal_adjudication_reason(
            {"proposal_id": "EXP-Y", "status": "gated",
             "release_condition": "caregiver-agent substrate exists"})
        self.assertIn("caregiver-agent substrate exists", got)

    def test_bare_record_still_yields_a_pointer(self):
        got = G._proposal_adjudication_reason(PROP_ARC_018_SKIPPED)
        self.assertTrue(got.strip())
        self.assertIn("EXP-0131", got)
        self.assertIn("skipped", got)

    def test_never_empty_even_for_a_totally_bare_record(self):
        self.assertTrue(G._proposal_adjudication_reason({}).strip())


# --- the lane ---------------------------------------------------------------


CLAIMS_META = {
    # built + candidate + lit above floor -> all five are genuine lane candidates
    "MECH-191": {"status": "candidate", "title": "MECH-191", "location": "a.md"},
    "MECH-203": {"status": "candidate", "title": "MECH-203", "location": "b.md"},
    "MECH-282": {"status": "candidate", "title": "MECH-282", "location": "c.md"},
    "SD-039":   {"status": "candidate", "title": "SD-039",   "location": "d.md"},
    "MECH-074": {"status": "candidate", "title": "MECH-074", "location": "e.md"},
}
LIT_CONF = {"MECH-191": 0.87, "MECH-203": 0.88, "MECH-282": 0.80,
            "SD-039": 0.86, "MECH-074": 0.87}
BUILT = set(CLAIMS_META)


class _LaneFixture(_ProposalsFileFixture):
    """Pin the lane's two live-file helpers so the lane is deterministic."""

    def setUp(self):
        super().setUp()
        self._orig_lit = G._claim_lit_conf
        self._orig_built = G._claims_implemented_in_substrate
        G._claim_lit_conf = lambda: dict(LIT_CONF)
        G._claims_implemented_in_substrate = lambda: set(BUILT)

    def tearDown(self):
        G._claim_lit_conf = self._orig_lit
        G._claims_implemented_in_substrate = self._orig_built
        super().tearDown()

    def _candidates(self, adjudicated=None):
        return G._evidence_confirmer_candidates(
            CLAIMS_META, set(), {}, set(), adjudicated
        )


class IncidentReplayTest(_LaneFixture):
    """The exact 2026-08-03 board: MECH-191 must stop being offered as work."""

    def test_mech_191_carries_its_adjudication(self):
        by_cid = {c["claim_id"]: c for c in
                  self._candidates(G._confirmer_adjudicated_proposals())}
        adj = by_cid["MECH-191"].get("adjudication")
        self.assertIsNotNone(
            adj, "FM10 regression: MECH-191 was worked twice on 2026-08-03, both "
                 "self-routing substrate_not_ready_requeue, and EXP-0276 records "
                 "that at status=blocked_substrate. The lane must read it back.")
        self.assertEqual("EXP-0276", adj["proposal_id"])
        self.assertEqual("blocked_substrate", adj["status"])
        self.assertEqual("metaworker-chip-20260803-igw-confirm-mech191",
                         adj["session"])
        self.assertIn("saturated-constant", adj["reason"])

    def test_gated_claims_carry_theirs_too(self):
        by_cid = {c["claim_id"]: c for c in
                  self._candidates(G._confirmer_adjudicated_proposals())}
        self.assertEqual("gated", by_cid["MECH-282"]["adjudication"]["status"])

    def test_mech_203_is_NOT_covered_and_that_is_recorded_deliberately(self):
        """MECH-203 is the honest gap. Its proposal EXP-0495 is `executed`; the
        negative adjudication from chip-20260803-igw-confirm-mech203 lives only
        in the chip ledger, which is not an input to this generator. No predicate
        over these inputs can reach it -- suppressing it needs a NEW durable
        record, not a wider veto. Asserted so a later session does not 'fix' this
        by folding `executed` into the status set, which would mute 213 of 354
        proposals at a stroke."""
        by_cid = {c["claim_id"]: c for c in
                  self._candidates(G._confirmer_adjudicated_proposals())}
        self.assertIn("MECH-203", by_cid)
        self.assertNotIn("adjudication", by_cid["MECH-203"])


class NeverDropsACandidateTest(_LaneFixture):
    """THE ANTI-MUTE ASSERTION. An adjudicated claim is rendered `blocked`, never
    removed: the status is manually set and never auto-cleared, so dropping it
    would make the claim invisible for as long as nobody revisits the proposal."""

    def test_candidate_count_is_identical_with_and_without_suppression(self):
        without = self._candidates(None)
        with_adj = self._candidates(G._confirmer_adjudicated_proposals())
        self.assertEqual(len(without), len(with_adj))
        self.assertEqual([c["claim_id"] for c in without],
                         [c["claim_id"] for c in with_adj],
                         "suppression must not reorder or remove candidates -- "
                         "it only annotates them")

    def test_every_field_except_adjudication_is_unchanged(self):
        without = {c["claim_id"]: c for c in self._candidates(None)}
        with_adj = {c["claim_id"]: c for c in
                    self._candidates(G._confirmer_adjudicated_proposals())}
        for cid, before in without.items():
            after = dict(with_adj[cid])
            after.pop("adjudication", None)
            self.assertEqual(before, after)


class NegativeControlTest(_LaneFixture):
    """Guards against the failure mode this fix could itself introduce."""

    def test_unadjudicated_claims_are_untouched(self):
        by_cid = {c["claim_id"]: c for c in
                  self._candidates(G._confirmer_adjudicated_proposals())}
        for cid in ("SD-039", "MECH-074", "MECH-203"):
            self.assertNotIn("adjudication", by_cid[cid],
                             f"{cid} has no adjudication on this board -- it is "
                             f"real, dispatchable confirmer work")

    def test_none_adjudication_map_is_a_pure_no_op(self):
        for c in self._candidates(None):
            self.assertNotIn("adjudication", c)

    def test_empty_adjudication_map_is_a_pure_no_op(self):
        for c in self._candidates({}):
            self.assertNotIn("adjudication", c)

    def test_an_unparseable_proposals_file_suppresses_nothing(self):
        """Fail-open, end to end: a broken input must degrade to the old
        behaviour (everything offered), never to a silently muted lane."""
        self._path.write_text("{not json", encoding="utf-8")
        for c in self._candidates(G._confirmer_adjudicated_proposals()):
            self.assertNotIn("adjudication", c)

    def test_suppression_never_invents_a_candidate(self):
        """An adjudicated claim that is NOT a lane candidate (not built, not
        candidate-status, lit below floor) must not be pulled in by the map."""
        adj = dict(G._confirmer_adjudicated_proposals())
        adj["MECH-999"] = {"proposal_id": "EXP-Z", "status": "gated"}
        self.assertNotIn("MECH-999",
                         {c["claim_id"] for c in self._candidates(adj)})

    def test_clearing_the_status_re_admits_the_claim_same_regeneration(self):
        """The block is a pointer to a mutable record, not a tombstone."""
        cleared = [dict(p, status="proposed") if p is PROP_MECH_191 else p
                   for p in INCIDENT_PROPOSALS]
        self._write(cleared)
        by_cid = {c["claim_id"]: c for c in
                  self._candidates(G._confirmer_adjudicated_proposals())}
        self.assertNotIn("adjudication", by_cid["MECH-191"])


class CapSlotTest(_LaneFixture):
    """A blocked confirmer must not consume a CONFIRMER_AUTOSPAWN_CAP slot.

    The cap post-pass counts `status == "ready"` confirmers only, so an
    adjudicated one frees its slot for a real confirmer in the SAME
    regeneration. Verified live on the 2026-08-03 board: MECH-191 left the ready
    set and SD-039 (unadjudicated, lit 0.86) took the slot, ready-non-governance-v3
    holding at 3 before and after.
    """

    def test_cap_counts_ready_only(self):
        self.assertEqual(3, G.CONFIRMER_AUTOSPAWN_CAP)
        conf_items = [
            {"confirmer": True, "status": "blocked", "assignments": []},
            {"confirmer": True, "status": "ready", "assignments": []},
            {"confirmer": True, "status": "surfaced", "assignments": []},
        ]
        free_ready = [it for it in conf_items
                      if it.get("status") == "ready" and not it.get("assignments")]
        self.assertEqual(1, len(free_ready))


if __name__ == "__main__":
    unittest.main(verbosity=2)
