#!/usr/bin/env python3
"""Regression tests for FM10b/FM10c -- the GOV-CONFIRM-1 confirmer lane could not
see EITHER durable record of an already-adjudicated zero-evidence signal
(chip-20260906-confirmer-lane-diagnostic-adjudicated-flag).

THE INCIDENT. MECH-489 was auto-spawned into the confirmer lane THREE times (the
2026-08-03 lineage, IGW-20260826-235, IGW-20260906-241). Every session correctly
concluded DO-NOT-QUEUE and burned a whole worker doing it. Two durable records of
that verdict existed and neither could reach this generator:

  (i) claims.yaml MECH-489 carries `diagnostic_evidence_adjudicated: true` -- the
      governance-ratified flag from chip-20260826-sd099-diagnostic-adjudicated-flag,
      meaning "the genuine_exp_count of 0 is already adjudicated; the runs exist
      and are correctly scoring_excluded as diagnostic probes".
      build_experiment_indexes.py genuinely consumes it. But `_load_claims_meta()`
      is a line parser with an explicit `keys` ALLOWLIST that did not contain the
      field, so it was structurally invisible to EVERY workset lane.

  (ii) experiment_proposals.v1.json EXP-0057 (claim MECH-489) carries the written
      verdict in `gating_reason` -- an "ADJUDICATED DO-NOT-QUEUE 2026-08-26"
      section and a "SECOND ADJUDICATED DO-NOT-QUEUE 2026-09-06" one. Its status
      is `executed`, and _PROPOSAL_ADJUDICATED_NOT_QUEUEABLE_STATUSES
      DELIBERATELY excludes `executed`. That exclusion is CORRECT in general (213
      of 354 live proposals are executed; an executed-then-FAILED proposal may
      want a successor) and must not be removed -- see
      test_generate_inter_governance_workset_confirmer_adjudication.py
      ::test_excludes_lifecycle_positions, which this suite does not contradict.

THE FIX IS OPT-IN ON BOTH SIDES, and that is what these tests mostly pin. The
flag is a field a governance session sets deliberately; the marker is a phrase an
adjudicating session writes deliberately. Neither is an inference from a status,
and an `executed` proposal WITHOUT the marker is still not an adjudication.

Rendering `blocked` rather than dropping is the FM7/FM10 precedent, unchanged
here: the claim stays on /workset carrying its verdict, consumes no
CONFIRMER_AUTOSPAWN_CAP slot, and re-enters the eligible set the moment the flag
or the marker is cleared.

Time-independent: no clock, no network, no live-file dependence (every input is a
fixture or a tempdir file).

Run: /opt/local/bin/python3 scripts/test_generate_inter_governance_workset_diagnostic_adjudicated.py
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
        "ree_igw_generator_diagnostic_adjudicated_test", path
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


G = _load_generator()


# --- fixtures ---------------------------------------------------------------

# EXP-0057's real shape, trimmed. The gating_reason keeps the ORDER of the live
# record: a "RELEASED" preamble first, the DO-NOT-QUEUE sections appended after.
# That order is load-bearing -- a naive first-200-characters excerpt renders
# "RELEASED", the opposite of the operative verdict.
PROP_MECH_489 = {
    "proposal_id": "EXP-0057",
    "backlog_id": "EVB-0610",
    "claim_id": "MECH-489",
    "status": "executed",
    "executed_by": "V3-EXQ-910b",
    "executed_queue_id": "V3-EXQ-910b",
    "gated_by_session": "metaworker-chip-20260817-sd-orienting-decision-scale-amend",
    "gating_reason": (
        "RELEASED 2026-08-21. This proposal's own release_condition is now "
        "satisfied in all three parts and the retest is RE-QUEUED as V3-EXQ-910b.\n\n"
        "ADJUDICATED DO-NOT-QUEUE 2026-08-26 (igw-235-confirm-evidence-mech-489-lit-0). "
        "Status stays `executed` -- that is a true lifecycle fact. THE CONFIRMER "
        "SIGNAL IS A FALSE POSITIVE, NOT MISSING EVIDENCE.\n\n"
        "SECOND ADJUDICATED DO-NOT-QUEUE 2026-09-06 (igw-241-confirm-evidence-mech-489-lit-0). "
        "A re-run would be vacuous on both halves: defensive_orienting.py is "
        "byte-identical since c1c24c6."
    ),
}
# The honest negative control from the FM10 suite: executed, no marker.
PROP_MECH_203_EXECUTED = {
    "proposal_id": "EXP-0495", "claim_id": "MECH-203", "status": "executed",
    "executed_queue_id": "V3-EXQ-843",
}
PROP_SD_039_EXECUTED = {
    "proposal_id": "EXP-0508", "claim_id": "SD-039", "status": "executed",
}
PROP_MECH_191_BLOCKED = {
    "proposal_id": "EXP-0276", "claim_id": "MECH-191", "status": "blocked_substrate",
    "gating_reason": "scalar channel-norm readouts are saturated-constant.",
}

BOARD = [PROP_MECH_489, PROP_MECH_203_EXECUTED, PROP_SD_039_EXECUTED,
         PROP_MECH_191_BLOCKED]

# claims.yaml block for the flag parser. MECH-489 carries the flag; MECH-203 does
# not; SD-011 carries it in the `true` spelling a yaml scalar actually produces.
CLAIMS_YAML_TEXT = """\
- id: MECH-489
  title: Defensive orienting valence gating
  status: candidate
  claim_type: mechanism_hypothesis
  location: docs/architecture/pag.md
  diagnostic_evidence_adjudicated: true
  notes: |
    three diagnostic probes, all scoring_excluded
- id: MECH-203
  title: A claim with no flag
  status: candidate
  claim_type: mechanism_hypothesis
  location: docs/architecture/b.md
- id: SD-011
  title: Flag written with a trailing comment
  status: candidate
  claim_type: design_decision
  location: docs/architecture/c.md
  diagnostic_evidence_adjudicated: true   # set by governance-20260903T2013
- id: SD-039
  title: Explicitly false is not set
  status: candidate
  claim_type: design_decision
  location: docs/architecture/d.md
  diagnostic_evidence_adjudicated: false
"""


class _FilesFixture(unittest.TestCase):
    """Point PROPOSALS_JSON / CLAIMS_YAML at tempdir files, not the live ones."""

    PROPOSALS = BOARD
    CLAIMS = CLAIMS_YAML_TEXT

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        root = Path(self._tmp.name)
        self._props = root / "experiment_proposals.v1.json"
        self._claims = root / "claims.yaml"
        self._write(self.PROPOSALS)
        self._claims.write_text(self.CLAIMS, encoding="utf-8")
        self._orig_props, self._orig_claims = G.PROPOSALS_JSON, G.CLAIMS_YAML
        G.PROPOSALS_JSON = self._props
        G.CLAIMS_YAML = self._claims

    def tearDown(self):
        G.PROPOSALS_JSON = self._orig_props
        G.CLAIMS_YAML = self._orig_claims
        self._tmp.cleanup()

    def _write(self, items):
        self._props.write_text(
            json.dumps({"schema_version": 1, "items": items}, indent=2),
            encoding="utf-8",
        )


# --- (i) the claims.yaml allowlist ------------------------------------------


class ClaimsMetaAllowlistTest(_FilesFixture):
    """THE ROOT GAP. `keys` is an allowlist: a field absent from it is invisible
    to every lane no matter what that lane intends to do with it."""

    def test_the_key_is_in_the_parser_allowlist(self):
        meta = G._load_claims_meta()
        self.assertEqual("true",
                         meta["MECH-489"]["diagnostic_evidence_adjudicated"])

    def test_flag_resolves_truthy_like_the_indexer_does(self):
        meta = G._load_claims_meta()
        self.assertTrue(G._claim_diagnostic_evidence_adjudicated(meta["MECH-489"]))

    def test_inline_comment_is_stripped_before_the_truth_test(self):
        meta = G._load_claims_meta()
        self.assertTrue(G._claim_diagnostic_evidence_adjudicated(meta["SD-011"]))

    def test_absent_and_explicit_false_are_both_falsey(self):
        meta = G._load_claims_meta()
        self.assertFalse(G._claim_diagnostic_evidence_adjudicated(meta["MECH-203"]))
        self.assertFalse(G._claim_diagnostic_evidence_adjudicated(meta["SD-039"]))

    def test_missing_meta_is_falsey_not_an_exception(self):
        self.assertFalse(G._claim_diagnostic_evidence_adjudicated(None))
        self.assertFalse(G._claim_diagnostic_evidence_adjudicated({}))

    def test_pre_existing_keys_still_parse(self):
        """Adding a key must not disturb the ones the other lanes depend on."""
        meta = G._load_claims_meta()
        self.assertEqual("candidate", meta["MECH-489"]["status"])
        self.assertEqual("mechanism_hypothesis", meta["MECH-489"]["claim_type"])
        self.assertEqual("docs/architecture/pag.md", meta["MECH-489"]["location"])


# --- (ii) the executed + DO-NOT-QUEUE marker route --------------------------


class ExecutedDoNotQueueMarkerTest(_FilesFixture):

    def test_mech_489_is_admitted_by_the_marker(self):
        got = G._confirmer_adjudicated_proposals()
        self.assertIn("MECH-489", got)
        self.assertEqual("EXP-0057", got["MECH-489"]["proposal_id"])

    def test_executed_without_the_marker_is_still_not_an_adjudication(self):
        """The scoping assertion. `executed` stays OUT of the status set; only
        the explicit written marker admits an executed proposal."""
        got = G._confirmer_adjudicated_proposals()
        self.assertNotIn("MECH-203", got)
        self.assertNotIn("SD-039", got)
        self.assertNotIn("executed", G._PROPOSAL_ADJUDICATED_NOT_QUEUEABLE_STATUSES)

    def test_the_marker_is_honoured_on_executed_only(self):
        """A live `proposed`/`queued` proposal carries intent. A stale sentence
        in its free text must not suppress work someone is actively planning."""
        self._write([dict(PROP_MECH_489, claim_id="MECH-900", status="proposed"),
                     dict(PROP_MECH_489, claim_id="MECH-901", status="queued")])
        got = G._confirmer_adjudicated_proposals()
        self.assertNotIn("MECH-900", got)
        self.assertNotIn("MECH-901", got)

    def test_the_retest_lane_is_not_widened(self):
        """FM10b touches the CONFIRMER lane only -- the retest lane still asks
        for a substrate block and nothing else."""
        self.assertNotIn("MECH-489", G._proposal_blocked_substrate_by_claim())

    def test_arbitrary_status_set_reads_are_unchanged_without_a_predicate(self):
        self.assertEqual({"MECH-489", "MECH-203", "SD-039"},
                         set(G._proposals_by_claim({"executed"})))

    def test_reason_shows_the_last_do_not_queue_section_not_the_preamble(self):
        reason = G._proposal_adjudication_reason(PROP_MECH_489)
        self.assertIn("SECOND ADJUDICATED DO-NOT-QUEUE 2026-09-06", reason)
        self.assertNotIn("RELEASED 2026-08-21", reason)

    def test_reason_is_unchanged_for_a_record_without_the_marker(self):
        reason = G._proposal_adjudication_reason(PROP_MECH_191_BLOCKED)
        self.assertIn("saturated-constant", reason)


# --- the lane, end to end ---------------------------------------------------


LIT_CONF = {"MECH-489": 0.82, "MECH-203": 0.88, "SD-039": 0.86, "SD-011": 0.80}


class _LaneFixture(_FilesFixture):

    def setUp(self):
        super().setUp()
        self._orig_lit = G._claim_lit_conf
        self._orig_built = G._claims_implemented_in_substrate
        G._claim_lit_conf = lambda: dict(LIT_CONF)
        G._claims_implemented_in_substrate = lambda: set(LIT_CONF)

    def tearDown(self):
        G._claim_lit_conf = self._orig_lit
        G._claims_implemented_in_substrate = self._orig_built
        super().tearDown()

    def _candidates(self, adjudicated=None):
        return G._evidence_confirmer_candidates(
            G._load_claims_meta(), set(), {}, set(), adjudicated
        )

    def _by_cid(self, adjudicated=None):
        return {c["claim_id"]: c for c in self._candidates(adjudicated)}


class Mech489IncidentReplayTest(_LaneFixture):
    """THE MOTIVATING SHAPE: flag set + genuine_exp_count 0 + built substrate
    must render `blocked`, not `ready`. Measured live on 2026-09-07: the only
    workset delta was IGW-20260907-241 ready -> blocked, ready 30 -> 29."""

    def test_mech_489_carries_an_adjudication_from_the_proposal_marker(self):
        adj = self._by_cid(G._confirmer_adjudicated_proposals())["MECH-489"]["adjudication"]
        self.assertEqual("EXP-0057", adj["proposal_id"])
        self.assertEqual("executed", adj["status"])
        self.assertIn("DO-NOT-QUEUE", adj["reason"])

    def test_the_flag_alone_is_enough_when_no_proposal_record_exists(self):
        """FM10c standing on its own: with the proposals file empty, the
        claims.yaml flag still blocks the item. This is what stops the next
        flagged claim needing its own proposal record first."""
        self._write([])
        adj = self._by_cid(G._confirmer_adjudicated_proposals())["MECH-489"]["adjudication"]
        self.assertEqual("diagnostic_evidence_adjudicated", adj["status"])
        self.assertIn("diagnostic_evidence_adjudicated", adj["reason"])
        self.assertIn("MECH-489", adj["reason"])

    def test_the_proposal_record_wins_when_both_are_present(self):
        """The proposal carries a session's own written reasoning; the flag is a
        one-bit fact. Prefer the more specific record."""
        adj = self._by_cid(G._confirmer_adjudicated_proposals())["MECH-489"]["adjudication"]
        self.assertEqual("EXP-0057", adj["proposal_id"])

    def test_the_call_site_renders_blocked_for_either_route(self):
        """Mirrors generate_workset's `if adj:` branch -- an adjudication key of
        any origin takes the blocked path, so no call-site change was needed."""
        for adjudicated in (G._confirmer_adjudicated_proposals(), None):
            conf = self._by_cid(adjudicated)["MECH-489"]
            self.assertIn("adjudication", conf)
            self.assertTrue(conf["adjudication"]["reason"].strip())


class NeverDropsACandidateTest(_LaneFixture):
    """THE ANTI-MUTE ASSERTION, re-pinned for the flag route. Both the flag and
    the marker are manually set and never auto-cleared, so dropping would make
    the claim invisible until somebody happened to revisit it."""

    def test_candidate_set_is_identical_with_and_without_the_flag(self):
        with_flag = [c["claim_id"] for c in
                     self._candidates(G._confirmer_adjudicated_proposals())]
        self.CLAIMS = CLAIMS_YAML_TEXT.replace(
            "  diagnostic_evidence_adjudicated: true\n", "")
        self._claims.write_text(self.CLAIMS, encoding="utf-8")
        self._write([])
        without = [c["claim_id"] for c in self._candidates(None)]
        self.assertEqual(sorted(without), sorted(with_flag),
                         "adjudication must annotate, never remove or reorder")

    def test_unflagged_claims_are_untouched(self):
        by_cid = self._by_cid(G._confirmer_adjudicated_proposals())
        for cid in ("MECH-203", "SD-039"):
            self.assertNotIn("adjudication", by_cid[cid],
                             f"{cid} is real, dispatchable confirmer work")

    def test_clearing_the_flag_re_admits_the_claim_same_regeneration(self):
        self._claims.write_text(
            CLAIMS_YAML_TEXT.replace(
                "  diagnostic_evidence_adjudicated: true\n", "", 1),
            encoding="utf-8")
        self._write([])
        self.assertNotIn("adjudication", self._by_cid(None)["MECH-489"])

    def test_a_missing_claims_file_suppresses_nothing(self):
        """Fail-open: a broken input degrades to the old behaviour (everything
        offered), never to a silently muted lane."""
        G.CLAIMS_YAML = Path(self._tmp.name) / "does-not-exist.yaml"
        self.assertEqual({}, G._load_claims_meta())

    def test_an_unparseable_proposals_file_suppresses_nothing_via_the_marker(self):
        self._props.write_text("{not json", encoding="utf-8")
        self.assertEqual({}, G._confirmer_adjudicated_proposals())

    def test_adjudication_never_invents_a_candidate(self):
        """A flagged claim that is NOT a lane candidate (not built) must not be
        pulled in."""
        G._claims_implemented_in_substrate = lambda: set()
        self.assertEqual([], self._candidates(G._confirmer_adjudicated_proposals()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
