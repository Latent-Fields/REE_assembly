#!/usr/bin/env python3
"""Contract tests: a queue-gated claim's EXPERIMENTAL proposal is BORN blocked.

THE PROPERTY UNDER TEST (chip-20260904-indexer-mints-gated-claims-as-blocked).
A claim carrying a claims.yaml experiment queue gate -- the structured
`experiment_gate: {gated: true, ...}` mapping, or the anchored literal
`GATED: DO NOT QUEUE` in its notes -- must never have build_experiment_indexes
mint its experimental proposal at status "proposed". Both proposal PRODUCERS
honoured the gate since 2026-09-04 (igw_routine_tick.claim_queue_gate_reason);
the indexer kept re-minting the row "proposed" every regen, and ARC-113's
EXP-0486 / EXP-0274 / EXP-0278 were re-adjudicated by hand each cycle.

Three things are pinned:
  1. _load_claim_registry reads both carriers, and ONLY the anchored literal
     (a loose "DO NOT QUEUE" scan matched 67 claims on 2026-09-04, one of them
     INV-012 quoting another claim's hold).
  2. apply_claim_queue_gate blocks a "proposed" experimental row with
     blocked_by / gating_reason / blocked_note, leaves literature rows and
     manual dispositions alone, and LIFTS only the rows it blocked itself.
  3. The composed reason is format-identical to igw_routine_tick's, so a
     human reads one sentence in both places.

Loads the indexer via importlib like test_proposal_id_stability.py.
Run: /opt/local/bin/python3 scripts/test_proposal_gate_mint.py
"""

import importlib.util
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

INDEXER_PATH = (
    Path(__file__).resolve().parents[1]
    / "evidence" / "experiments" / "scripts" / "build_experiment_indexes.py"
)


def _load_indexer():
    spec = importlib.util.spec_from_file_location("ree_indexer_gatemint", INDEXER_PATH)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["ree_indexer_gatemint"] = mod
    spec.loader.exec_module(mod)
    return mod


IDX = _load_indexer()

ARC113_STYLE_YAML = textwrap.dedent('''\
    - id: ARC-113
      status: candidate
      claim_type: architectural_commitment
      epistemic_category: substrate_ceiling
      experiment_gate:
        gated: true
        gating_claim: "ARC-062 GAP-B"
        release_condition: "ARC-062 GAP-B resolved (arc_062_rule_apprehension:GAP-B); the ablation may be queued only then"
        set_by: "governance-20260905 (C5 schema adoption)"
      live_status:
        phase: v3
      notes: >
        Long prose. *** GATED: DO NOT QUEUE THE ABLATION WHILE ARC-062 GAP-B IS
        UNRESOLVED. *** More prose.
    - id: IMPL-026
      status: candidate
      claim_type: reference_note
      experiment_gate:
        gated: true
        release_condition: "reference document -- no experiment is defined for it; do not mint experiment proposals"
        set_by: "governance-20260905 (C5 schema decision)"
      notes: >
        A reference table.
    - id: INV-012
      status: candidate
      claim_type: invariant
      notes: "the 'do not queue until SD-014 >= provisional' hold in SD-026's own note is being honored -- DO NOT QUEUE is quoted here, not asserted"
    - id: MECH-001
      status: candidate
      claim_type: mechanism_hypothesis
      experiment_gate:
        gated: false
        release_condition: "was gated once"
      notes: |
        Nothing gated. GATED: DO NOT QUEUE appears only in this block scalar.
    - id: MECH-002
      status: candidate
      claim_type: mechanism_hypothesis
      notes: plain
''')


def _registry(yaml_text):
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "claims.yaml"
        p.write_text(yaml_text)
        return IDX._load_claim_registry(p)


class RegistryGateParsingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reg = _registry(ARC113_STYLE_YAML)

    def test_structured_gate_with_gating_claim(self):
        r = self.reg["ARC-113"]
        self.assertEqual(r["queue_gate_claim"], "ARC-062 GAP-B")
        self.assertTrue(r["queue_gate_release"].startswith("ARC-062 GAP-B resolved"))
        self.assertEqual(
            r["queue_gate_reason"],
            "gated on ARC-062 GAP-B; release: " + r["queue_gate_release"])
        # the gate block did not swallow the sibling fields that follow it
        self.assertEqual(r["status"], "candidate")
        self.assertEqual(r["epistemic_category"], "substrate_ceiling")

    def test_structured_gate_without_gating_claim(self):
        r = self.reg["IMPL-026"]
        self.assertEqual(r["queue_gate_claim"], "")
        self.assertTrue(r["queue_gate_reason"].startswith("release: reference document"))

    def test_loose_do_not_queue_in_notes_does_not_gate(self):
        self.assertEqual(self.reg["INV-012"]["queue_gate_reason"], "")

    def test_gated_false_is_ungated_but_block_scalar_marker_gates(self):
        # gated: false -> the structured carrier says no; the anchored literal in
        # the block-scalar notes is the transitional carrier and still fires.
        r = self.reg["MECH-001"]
        self.assertEqual(r["queue_gate_claim"], "")
        self.assertEqual(r["queue_gate_release"], "")
        self.assertTrue(r["queue_gate_reason"].startswith("GATED: DO NOT QUEUE"))

    def test_plain_claim_is_ungated(self):
        self.assertEqual(self.reg["MECH-002"]["queue_gate_reason"], "")

    def test_reason_format_mirrors_igw_routine_tick(self):
        """The tick's _resolve_queue_gate composes 'gated on X; release: Y' /
        'experiment_gate.gated' / the 200-char notes excerpt. Pin the same."""
        f = IDX._compose_queue_gate_reason
        self.assertEqual(f(True, "X", "Y", ""), "gated on X; release: Y")
        self.assertEqual(f(True, "", "", ""), "experiment_gate.gated")
        self.assertEqual(f(False, "", "", "pre GATED: DO NOT QUEUE tail"),
                         "GATED: DO NOT QUEUE tail")
        self.assertEqual(f(False, "", "", "do not queue"), "")


def _exp(status="proposed", **extra):
    p = {"proposal_id": "EXP-0486", "backlog_id": "EVB-0001", "claim_id": "ARC-113",
         "proposal_type": "experimental", "status": status}
    p.update(extra)
    return p


GATED = {"queue_gate_reason": "gated on ARC-062 GAP-B; release: GAP-B resolved",
         "queue_gate_claim": "ARC-062 GAP-B", "queue_gate_release": "GAP-B resolved"}
UNGATED = {"queue_gate_reason": "", "queue_gate_claim": "", "queue_gate_release": ""}


class ApplyGateTests(unittest.TestCase):
    def test_proposed_experimental_row_is_born_blocked(self):
        p = _exp()
        self.assertEqual(IDX.apply_claim_queue_gate(p, GATED), "minted")
        self.assertEqual(p["status"], "blocked_substrate")
        self.assertEqual(p["blocked_by"], ["ARC-062 GAP-B"])
        self.assertEqual(p["gating_reason"], GATED["queue_gate_reason"])
        self.assertEqual(p["release_condition"], "GAP-B resolved")
        self.assertEqual(p["gated_by_session"], IDX._GATE_MINT_MARKER)
        self.assertIn("ARC-113", p["blocked_note"])
        for k in ("blocked_by", "blocked_note", "gating_reason", "gated_by_session",
                  "release_condition"):
            self.assertIn(k, IDX._PROPOSAL_STATUS_CARRY_FORWARD_FIELDS, k)

    def test_gate_without_gating_claim_blocks_with_empty_blocked_by(self):
        p = _exp(claim_id="IMPL-026")
        meta = {"queue_gate_reason": "release: reference document", "queue_gate_claim": "",
                "queue_gate_release": "reference document"}
        self.assertEqual(IDX.apply_claim_queue_gate(p, meta), "minted")
        self.assertEqual(p["blocked_by"], [])

    def test_literature_row_is_never_touched(self):
        p = _exp(proposal_type="literature_review", proposal_id="LIT-0487")
        self.assertEqual(IDX.apply_claim_queue_gate(p, GATED), "")
        self.assertEqual(p["status"], "proposed")

    def test_manual_disposition_outranks_the_gate(self):
        for status in ("executed", "skipped", "blocked_substrate", "superseded"):
            p = _exp(status=status, blocked_note="hand-written")
            self.assertEqual(IDX.apply_claim_queue_gate(p, GATED), "", status)
            self.assertEqual(p["status"], status)
            self.assertEqual(p["blocked_note"], "hand-written")

    def test_ungated_claim_leaves_proposed_row_alone(self):
        p = _exp()
        self.assertEqual(IDX.apply_claim_queue_gate(p, UNGATED), "")
        self.assertEqual(IDX.apply_claim_queue_gate(p, {}), "")
        self.assertEqual(IDX.apply_claim_queue_gate(p, None), "")
        self.assertEqual(p["status"], "proposed")
        self.assertNotIn("blocked_by", p)

    def test_gate_lifts_only_its_own_rows(self):
        minted = _exp()
        IDX.apply_claim_queue_gate(minted, GATED)
        self.assertEqual(IDX.apply_claim_queue_gate(minted, UNGATED), "lifted")
        self.assertEqual(minted["status"], "proposed")
        for k in ("blocked_by", "blocked_note", "gating_reason", "gated_by_session",
                  "release_condition"):
            self.assertNotIn(k, minted)
        # a hand-blocked row (no marker, or a session's own marker) is not lifted
        manual = _exp(status="blocked_substrate", blocked_by=["MECH-036"],
                      blocked_note="Step 2.5 stop", gated_by_session="igw-244")
        self.assertEqual(IDX.apply_claim_queue_gate(manual, UNGATED), "")
        self.assertEqual(manual["status"], "blocked_substrate")
        self.assertEqual(manual["blocked_by"], ["MECH-036"])

    def test_regen_is_a_fixed_point_while_gated(self):
        p = _exp()
        IDX.apply_claim_queue_gate(p, GATED)
        before = dict(p)
        self.assertEqual(IDX.apply_claim_queue_gate(p, GATED), "")
        self.assertEqual(p, before)

    def test_reason_refresh_on_a_carried_gate_minted_row(self):
        p = _exp()
        IDX.apply_claim_queue_gate(p, GATED)
        newer = dict(GATED, queue_gate_reason="gated on ARC-062 GAP-B; release: reworded")
        self.assertEqual(IDX.apply_claim_queue_gate(p, newer), "")
        self.assertEqual(p["gating_reason"], newer["queue_gate_reason"])
        self.assertEqual(p["status"], "blocked_substrate")


class LiveRegistryTests(unittest.TestCase):
    """Against the real claims.yaml: the gate carriers the chip names must parse."""

    @classmethod
    def setUpClass(cls):
        cls.path = INDEXER_PATH.parents[3] / "docs" / "claims" / "claims.yaml"
        cls.reg = IDX._load_claim_registry(cls.path) if cls.path.exists() else {}

    def test_arc_113_is_gated_on_arc_062_gap_b(self):
        if "ARC-113" not in self.reg:
            self.skipTest("ARC-113 not in this checkout's registry")
        r = self.reg["ARC-113"]
        self.assertTrue(r["queue_gate_reason"], "ARC-113 must read as gated")
        self.assertIn("ARC-062 GAP-B", r["queue_gate_reason"])

    def test_no_loose_over_fire(self):
        if not self.reg:
            self.skipTest("no registry")
        gated = sorted(k for k, v in self.reg.items() if v["queue_gate_reason"])
        # 3 structured gates + the ARC-113 notes copy on 2026-09-07; the loose
        # scan's 67 is the failure this pins against.
        self.assertLess(len(gated), 15, gated)


if __name__ == "__main__":
    unittest.main()
