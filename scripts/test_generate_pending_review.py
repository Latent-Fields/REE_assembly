#!/usr/bin/env python3
"""Unit tests for verdict resolution in generate_pending_review.py.

Regression cover for the dict-shaped-`result` silent drop (2026-07-20): a
manifest carrying `result` as a dict short-circuited the `or` chain in
_manifest_pass_fail, resolved to None, and was skipped outright by
load_unclaimed_manifests -- so an unclaimed terminal FAIL never reached
pending_review.md. Confirmed on
v3_exq_728_trained_allon_capability_point_20260720T155414Z_v3.
"""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent / "generate_pending_review.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("ree_gen_pending", SCRIPT_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Shape of the 728 manifest: dict `result` AND a top-level string `outcome`.
DICT_RESULT_MANIFEST = {
    "run_id": "v3_exq_728_trained_allon_capability_point_20260720T155414Z_v3",
    "experiment_type": "v3_exq_728_trained_allon_capability_point",
    "queue_id": "V3-EXQ-728",
    "claim_ids": [],
    "evidence_direction": "non_contributory",
    "timestamp_utc": "20260720T155414Z",
    "result": {
        "outcome": "FAIL",
        "overall_direction": "non_contributory",
        "interpretation_label": "substrate_not_ready_requeue",
        "interpretation": {"label": "substrate_not_ready_requeue"},
    },
    "outcome": "FAIL",
}


class ManifestPassFailTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def test_dict_shaped_result_resolves_to_inner_outcome(self):
        """The defect: truthy dict short-circuited the or-chain -> None."""
        self.assertEqual(
            self.mod._manifest_pass_fail(DICT_RESULT_MANIFEST), "FAIL")

    def test_dict_shaped_result_pass(self):
        self.assertEqual(
            self.mod._manifest_pass_fail({"result": {"outcome": "PASS"}}), "PASS")

    def test_bare_string_result_still_resolves(self):
        self.assertEqual(self.mod._manifest_pass_fail({"result": "PASS"}), "PASS")
        self.assertEqual(self.mod._manifest_pass_fail({"outcome": "FAIL"}), "FAIL")

    def test_metrics_fallback_still_reached(self):
        self.assertEqual(
            self.mod._manifest_pass_fail({"metrics": {"overall_pass": False}}), "FAIL")

    def test_error_manifests_still_resolve_to_none(self):
        """ERROR stays None so load_error_manifests keeps ownership of it."""
        self.assertIsNone(self.mod._manifest_pass_fail({"result": "ERROR"}))
        self.assertIsNone(
            self.mod._manifest_pass_fail({"result": {"outcome": "ERROR"}}))
        self.assertIsNone(self.mod._manifest_pass_fail({}))

    def test_error_result_does_not_fall_through_to_sibling_field(self):
        """First-present-wins, as the original `or` chain did."""
        self.assertIsNone(
            self.mod._manifest_pass_fail({"result": "ERROR", "outcome": "FAIL"}))


class LoadUnclaimedManifestsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def test_dict_result_manifest_surfaces_as_unclaimed(self):
        with tempfile.TemporaryDirectory() as td:
            evidence = Path(td)
            (evidence / "v3_exq_728_dict_result_v3.json").write_text(
                json.dumps(DICT_RESULT_MANIFEST))
            orig = self.mod.EVIDENCE_DIR
            self.mod.EVIDENCE_DIR = evidence
            try:
                out = self.mod.load_unclaimed_manifests(
                    reviewed=set(), discussed=set(), indexed_run_ids=set())
            finally:
                self.mod.EVIDENCE_DIR = orig

        self.assertEqual(len(out), 1, "dict-shaped result manifest was dropped")
        self.assertEqual(out[0]["run_id"], DICT_RESULT_MANIFEST["run_id"])
        self.assertEqual(out[0]["result"], "FAIL")


def _block(**kw):
    """A z_goal_stream block with the producer's key set; override per test."""
    b = {"ticks_total": 12000, "ticks_active": 0, "writer_calls": 0,
         "active_frac": 0.0, "writer_defect": True,
         "goal_state_present": True, "n_agents": 6}
    b.update(kw)
    return b


class ZGoalWriterDefectTests(unittest.TestCase):
    """The interpretation rules for the dead-z_goal-stream flag.

    Getting these wrong makes the surface WORSE than nothing: the false
    positives below are all legitimate, common readings, and flagging them
    would bury the two real cases (V3-EXQ-626, V3-EXQ-830) in noise.
    """

    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def test_writer_defect_true_is_flagged(self):
        """The real signature: agent stepped, update_z_goal never called."""
        self.assertTrue(self.mod._z_goal_writer_defect(
            {"z_goal_stream": _block()}))

    def test_zero_active_frac_with_writer_calls_is_NOT_flagged(self):
        """Correctly wired, benefit gate never opened -- the agent met no
        resource. MEASURED on a StepHarness run, which pins the update_z_goal
        call as an invariant and so structurally CANNOT carry the defect.
        Flagging it would send a reader hunting for a call that is already
        there."""
        self.assertFalse(self.mod._z_goal_writer_defect(
            {"z_goal_stream": _block(writer_calls=12000, writer_defect=False)}))

    def test_goal_off_parity_arm_reading_zero_is_NOT_flagged(self):
        """A goal-OFF parity arm / negative control (V3-EXQ-626b's
        ARM_NO_BENEFIT) reads active_frac 0.0 CORRECTLY."""
        self.assertFalse(self.mod._z_goal_writer_defect(
            {"z_goal_stream": _block(ticks_total=0, active_frac=None,
                                     writer_defect=None,
                                     goal_state_present=False)}))

    def test_absent_block_is_unmeasured_not_a_defect(self):
        """The historical corpus carries no block at all. UNMEASURED must never
        render as measured-zero, and must never be flagged."""
        self.assertFalse(self.mod._z_goal_writer_defect({}))
        self.assertFalse(self.mod._z_goal_writer_defect({"z_goal_stream": {}}))
        self.assertFalse(self.mod._z_goal_writer_defect({"z_goal_stream": None}))

    def test_malformed_block_is_not_a_defect(self):
        """A non-dict block is bad data, not evidence of a dead stream."""
        self.assertFalse(self.mod._z_goal_writer_defect({"z_goal_stream": "true"}))
        self.assertFalse(self.mod._z_goal_writer_defect({"z_goal_stream": []}))

    def test_writer_defect_null_is_not_a_defect(self):
        """The producer writes None when nothing was measured (ticks_total 0).
        `is True` and not truthiness is what keeps that out of the section."""
        self.assertFalse(self.mod._z_goal_writer_defect(
            {"z_goal_stream": _block(writer_defect=None)}))
        self.assertFalse(self.mod._z_goal_writer_defect(
            {"z_goal_stream": _block(writer_defect=False)}))

    def test_active_frac_alone_can_never_flag(self):
        """The load-bearing negative: no value of active_frac flags a run whose
        writer_defect is not True. active_frac is NOT the signal."""
        for frac in (0.0, None, 0.5, 1.0):
            self.assertFalse(
                self.mod._z_goal_writer_defect(
                    {"z_goal_stream": _block(active_frac=frac,
                                             writer_defect=False)}),
                f"active_frac={frac!r} flagged without writer_defect")


class ZGoalSectionRenderTests(unittest.TestCase):
    """The rendered section is a record, not a gate."""

    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def _render(self, runs, unclaimed=()):
        import io
        from contextlib import redirect_stdout
        written = {}

        class _FakeOut:
            """Captures the rendered markdown instead of writing evidence/."""

            def __init__(self, store):
                self.store = store

            def write_text(self, text):
                self.store["text"] = text

            def relative_to(self, _root):
                return "evidence/experiments/pending_review.md"

        orig = self.mod.OUTPUT
        self.mod.OUTPUT = _FakeOut(written)
        try:
            with redirect_stdout(io.StringIO()):
                self.mod.write_pending_review(
                    list(runs), [], list(unclaimed), [], "2026-07-27T00:00:00Z")
        finally:
            self.mod.OUTPUT = orig
        return written.get("text", "")

    def _run(self, run_id="v3_exq_626_x_20260101T000000Z_v3", **kw):
        r = {"run_id": run_id, "timestamp_utc": "2026-07-27T10:00:00Z",
             "status": "PASS", "claims": ["MECH-288"], "failure_signatures": [],
             "adjudication": "n/a", "interpretation_label": "",
             "recorded_preconditions_unmet": [], "preconditions_scope_note": "",
             "z_goal_stream": {}}
        r.update(kw)
        return r

    def test_defective_run_gets_its_own_section(self):
        text = self._render([self._run(z_goal_stream=_block())])
        self.assertIn("Dead z_goal stream", text)
        self.assertIn("v3_exq_626_x_20260101T000000Z_v3", text)
        self.assertIn("record, not a gate", text)

    def test_clean_and_unmeasured_runs_produce_no_section(self):
        """No block, and a measured-but-fine block, both stay silent -- the
        section must not appear for the whole historical corpus."""
        text = self._render([
            self._run(run_id="unmeasured_20260101T000000Z_v3"),
            self._run(run_id="wired_20260101T000000Z_v3",
                      z_goal_stream=_block(writer_calls=99, writer_defect=False)),
        ])
        self.assertNotIn("Dead z_goal stream", text)

    def test_unclaimed_manifest_with_defect_is_surfaced(self):
        """Both confirmed defects were claim-less readiness diagnostics, which
        can land outside claim_evidence entirely -- the likeliest carrier."""
        unclaimed = [{
            "manifest_stem": "v3_exq_830_probe_20260727T120000Z_v3",
            "run_id": "v3_exq_830_probe_20260727T120000Z_v3",
            "result": "FAIL", "experiment_type": "v3_exq_830_probe",
            "evidence_direction": "", "timestamp_utc": "2026-07-27T12:00:00Z",
            "queue_id": "V3-EXQ-830", "z_goal_stream": _block(),
        }]
        text = self._render([], unclaimed=unclaimed)
        self.assertIn("Dead z_goal stream", text)
        self.assertIn("v3_exq_830_probe_20260727T120000Z_v3", text)
        # Unclaimed entries carry `result`, not `status` -- render, don't crash.
        self.assertNotIn("| ? |", text.split("Dead z_goal stream")[1][:2000])

    def test_section_does_not_change_pending_counts(self):
        """Membership is non-blocking: it must not inflate the pending total or
        move a run between the PASS/FAIL tables."""
        clean = self._render([self._run()])
        dead = self._render([self._run(z_goal_stream=_block())])
        for text in (clean, dead):
            self.assertIn("Pending: **1** item(s)", text)
            self.assertIn("1 PASS, 0 FAIL", text)


if __name__ == "__main__":
    unittest.main()
