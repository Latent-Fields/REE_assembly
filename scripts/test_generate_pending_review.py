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

    def test_pinned_goal_reading_writer_defect_null_is_NOT_flagged(self):
        """V3-EXQ-642a/642b's shape: the driver deliberately pins z_goal outside
        `update_z_goal` (`experiments/_lib/z_goal_stream.py`'s `goal_pinned=True`).
        `active_frac` reads 1.0 -- unlike the goal-OFF/unmeasured None case above --
        but `writer_defect` is still None, not True, and must not be flagged. This
        is the false positive V3-EXQ-642b actually hit in pending_review.md."""
        self.assertFalse(self.mod._z_goal_writer_defect(
            {"z_goal_stream": _block(writer_calls=0, active_frac=1.0,
                                     writer_defect=None, goal_pinned=True)}))

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


class LoadConfirmedAutopsyRunIdsTests(unittest.TestCase):
    """load_confirmed_autopsy_run_ids() -- the diagnostic-autopsy-gate's index."""

    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def _with_planning(self, files):
        td = tempfile.TemporaryDirectory()
        root = Path(td.name)
        planning = root / "evidence" / "planning"
        planning.mkdir(parents=True)
        for name, content in files.items():
            (planning / name).write_text(json.dumps(content))
        return td, root

    def test_confirmed_target_run_id_is_indexed(self):
        td, root = self._with_planning({
            "failure_autopsy_V3-EXQ-1_2026-08-07.json": {
                "status": "confirmed",
                "targets": [{"run_id": "v3_exq_1_x_20260101T000000Z_v3"}],
            },
        })
        orig = self.mod.ROOT
        self.mod.ROOT = root
        try:
            ids = self.mod.load_confirmed_autopsy_run_ids()
        finally:
            self.mod.ROOT = orig
            td.cleanup()
        self.assertIn("v3_exq_1_x_20260101T000000Z_v3", ids)

    def test_draft_autopsy_target_is_excluded(self):
        """Only status == 'confirmed' counts -- a draft is not adjudication."""
        td, root = self._with_planning({
            "failure_autopsy_V3-EXQ-2_2026-08-07.json": {
                "status": "draft",
                "targets": [{"run_id": "v3_exq_2_x_20260101T000000Z_v3"}],
            },
        })
        orig = self.mod.ROOT
        self.mod.ROOT = root
        try:
            ids = self.mod.load_confirmed_autopsy_run_ids()
        finally:
            self.mod.ROOT = orig
            td.cleanup()
        self.assertNotIn("v3_exq_2_x_20260101T000000Z_v3", ids)

    def test_confirmed_excluded_dry_run_id_is_indexed(self):
        """excluded_dry_run_ids counts as adjudication (2026-08-08 gap fix).

        A run determined dry by CONTENT inspection (pre-2026-07 manifests often
        carry no `dry_run` boolean) and recorded in excluded_dry_run_ids was
        previously invisible to both this set and load_dry_run_run_ids(), so it
        could never clear the reviewed-FAIL blind-spot net.
        """
        td, root = self._with_planning({
            "failure_autopsy_grandfathered-cluster_2026-08-08.json": {
                "status": "confirmed",
                "targets": [{"run_id": "v3_exq_3_x_20260101T000000Z_v3"}],
                "excluded_dry_run_ids": [
                    "v3_exq_4_dry_20260101T000000Z_v3",
                ],
            },
        })
        orig = self.mod.ROOT
        self.mod.ROOT = root
        try:
            ids = self.mod.load_confirmed_autopsy_run_ids()
        finally:
            self.mod.ROOT = orig
            td.cleanup()
        self.assertIn("v3_exq_4_dry_20260101T000000Z_v3", ids)
        # the target run_id collection must be unaffected
        self.assertIn("v3_exq_3_x_20260101T000000Z_v3", ids)

    def test_draft_excluded_dry_run_id_is_not_indexed(self):
        """Negative control -- a draft's exclusion list is not adjudication."""
        td, root = self._with_planning({
            "failure_autopsy_V3-EXQ-5_2026-08-08.json": {
                "status": "draft",
                "targets": [],
                "excluded_dry_run_ids": ["v3_exq_5_dry_20260101T000000Z_v3"],
            },
        })
        orig = self.mod.ROOT
        self.mod.ROOT = root
        try:
            ids = self.mod.load_confirmed_autopsy_run_ids()
        finally:
            self.mod.ROOT = orig
            td.cleanup()
        self.assertNotIn("v3_exq_5_dry_20260101T000000Z_v3", ids)

    def test_excluded_dry_run_ids_absent_or_malformed_is_tolerated(self):
        """The field is optional; non-string members are skipped, not fatal."""
        td, root = self._with_planning({
            "failure_autopsy_V3-EXQ-6_2026-08-08.json": {
                "status": "confirmed",
                "targets": [{"run_id": "v3_exq_6_x_20260101T000000Z_v3"}],
            },
            "failure_autopsy_V3-EXQ-7_2026-08-08.json": {
                "status": "confirmed",
                "targets": [],
                "excluded_dry_run_ids": [None, "", 7,
                                         "v3_exq_7_dry_20260101T000000Z_v3"],
            },
        })
        orig = self.mod.ROOT
        self.mod.ROOT = root
        try:
            ids = self.mod.load_confirmed_autopsy_run_ids()
        finally:
            self.mod.ROOT = orig
            td.cleanup()
        self.assertEqual(ids, {"v3_exq_6_x_20260101T000000Z_v3",
                               "v3_exq_7_dry_20260101T000000Z_v3"})


class DiagnosticAutopsyRequiredSectionTests(unittest.TestCase):
    """The blanket experiment_purpose=='diagnostic' gate (2026-08-07).

    Confirmed live during the 2026-08-07 governance cycle: a diagnostic PASS
    with no `adjudication` flag (both its own preconditions cleared) sailed
    into the ordinary PASS table with zero signal it needed /failure-autopsy.
    This section is the purpose-keyed net that catches it regardless of
    adjudication flag or whether it visibly "routes a decision".
    """

    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def _render(self, runs, root):
        import io
        from contextlib import redirect_stdout
        written = {}

        class _FakeOut:
            def __init__(self, store):
                self.store = store

            def write_text(self, text):
                self.store["text"] = text

            def relative_to(self, _root):
                return "evidence/experiments/pending_review.md"

        orig_out = self.mod.OUTPUT
        orig_root = self.mod.ROOT
        self.mod.OUTPUT = _FakeOut(written)
        self.mod.ROOT = root
        try:
            with redirect_stdout(io.StringIO()):
                self.mod.write_pending_review(
                    list(runs), [], [], [], "2026-07-27T00:00:00Z")
        finally:
            self.mod.OUTPUT = orig_out
            self.mod.ROOT = orig_root
        return written.get("text", "")

    def _run(self, run_id, experiment_purpose, **kw):
        r = {"run_id": run_id, "timestamp_utc": "2026-08-07T10:00:00Z",
             "status": "PASS", "claims": ["MECH-1"], "failure_signatures": [],
             "adjudication": "n/a", "interpretation_label": "some_label",
             "experiment_purpose": experiment_purpose,
             "recorded_preconditions_unmet": [], "preconditions_scope_note": "",
             "z_goal_stream": {}}
        r.update(kw)
        return r

    def _empty_planning_root(self):
        td = tempfile.TemporaryDirectory()
        root = Path(td.name)
        (root / "evidence" / "planning").mkdir(parents=True)
        return td, root

    def test_uncovered_diagnostic_pass_is_flagged(self):
        td, root = self._empty_planning_root()
        try:
            text = self._render(
                [self._run("v3_exq_866b_x_20260101T000000Z_v3", "diagnostic")],
                root)
        finally:
            td.cleanup()
        self.assertIn("Diagnostic -- autopsy required", text)
        self.assertIn("v3_exq_866b_x_20260101T000000Z_v3", text)
        self.assertIn("1 diagnostic run(s) with no confirmed autopsy", text)
        # Non-exclusionary: it must still appear in the ordinary PASS table.
        self.assertIn("## PASS (verify & close)", text)
        pass_section = text.split("## PASS")[1].split("## Diagnostic")[0]
        self.assertIn("v3_exq_866b_x_20260101T000000Z_v3", pass_section)

    def test_diagnostic_covered_by_confirmed_autopsy_is_not_flagged(self):
        td, root = self._empty_planning_root()
        (root / "evidence" / "planning" / "failure_autopsy_V3-EXQ-866b_2026-08-07.json").write_text(
            json.dumps({
                "status": "confirmed",
                "targets": [{"run_id": "v3_exq_866b_x_20260101T000000Z_v3"}],
            }))
        try:
            text = self._render(
                [self._run("v3_exq_866b_x_20260101T000000Z_v3", "diagnostic")],
                root)
        finally:
            td.cleanup()
        self.assertNotIn("Diagnostic -- autopsy required", text)

    def test_evidence_purpose_run_is_never_flagged(self):
        td, root = self._empty_planning_root()
        try:
            text = self._render(
                [self._run("v3_exq_888_x_20260101T000000Z_v3", "evidence")],
                root)
        finally:
            td.cleanup()
        self.assertNotIn("Diagnostic -- autopsy required", text)

    def test_indexer_flagged_diagnostic_is_not_double_counted(self):
        """A run in the narrower `flagged` bucket (adjudication flag) that is
        ALSO an uncovered diagnostic appears in both sections (they answer
        different questions) but the summary counts are independent."""
        td, root = self._empty_planning_root()
        try:
            text = self._render(
                [self._run("v3_exq_1_x_20260101T000000Z_v3", "diagnostic",
                            adjudication="precondition_unmet")],
                root)
        finally:
            td.cleanup()
        self.assertIn("Diagnostic adjudication required", text)
        self.assertIn("Diagnostic -- autopsy required", text)
        self.assertIn("1 diagnostic self-route(s) flagged for adjudication", text)
        self.assertIn("1 diagnostic run(s) with no confirmed autopsy", text)


class LoadReviewedFailWithoutAutopsyTests(unittest.TestCase):
    """The reviewed-FAIL-without-autopsy blind-spot net (2026-08-08).

    The ARC-017 V3-EXQ-129/135 gap: a claim-tagged, evidence-purpose FAIL was
    marked reviewed (which excludes it from load_pending_entries) but never
    autopsied, so it vanished from every section for ~131 days. This scanner is
    reviewed-INDEPENDENT: being reviewed no longer exempts a FAIL from needing
    an autopsy.
    """

    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def _with_claim_evidence(self, entries, unlinked=()):
        """Point the module at a temp claim_evidence.v1.json; reset its cache."""
        td = tempfile.TemporaryDirectory()
        path = Path(td.name) / "claim_evidence.v1.json"
        path.write_text(json.dumps({"entries": entries,
                                    "unlinked_runs": list(unlinked)}))
        self.mod.CLAIM_EVIDENCE = path
        self.mod._CLAIM_EVIDENCE_CACHE = None
        return td

    def _entry(self, run_id, claim_id="ARC-017", status="FAIL",
               purpose="evidence", **kw):
        e = {"run_id": run_id, "claim_id": claim_id, "status": status,
             "source_type": "experimental", "experiment_purpose": purpose,
             "timestamp_utc": "2026-03-29T03:19:33Z"}
        e.update(kw)
        return e

    def _load(self, reviewed, dry=frozenset(), autopsy=frozenset()):
        return self.mod.load_reviewed_fail_without_autopsy(
            set(reviewed), set(dry), set(autopsy))

    def test_arc017_shape_reviewed_fail_is_flagged(self):
        """The exact blind-spot shape: reviewed, claim-tagged, evidence FAIL,
        no confirmed autopsy -> surfaced."""
        rid = "v3_exq_129_arc017_stream_tag_pair_20260329T031933Z_v3"
        td = self._with_claim_evidence([self._entry(rid)])
        try:
            out = self._load(reviewed={rid})
        finally:
            td.cleanup()
        self.assertEqual([r["run_id"] for r in out], [rid])
        self.assertEqual(out[0]["claims"], ["ARC-017"])

    def test_confirmed_autopsy_excludes_it(self):
        """Once ARC-017 has a confirmed autopsy target it must NOT re-flag."""
        rid = "v3_exq_129_arc017_stream_tag_pair_20260329T031933Z_v3"
        td = self._with_claim_evidence([self._entry(rid)])
        try:
            out = self._load(reviewed={rid}, autopsy={rid})
        finally:
            td.cleanup()
        self.assertEqual(out, [])

    def test_unreviewed_fail_is_not_this_nets_job(self):
        """An un-reviewed FAIL is still surfaced by the FAIL section; this net
        only owns the reviewed blind-spot state."""
        rid = "v3_exq_x_20260101T000000Z_v3"
        td = self._with_claim_evidence([self._entry(rid)])
        try:
            out = self._load(reviewed=set())
        finally:
            td.cleanup()
        self.assertEqual(out, [])

    def test_diagnostic_purpose_is_excluded(self):
        """Diagnostic FAILs are owned by the two diagnostic-autopsy nets."""
        rid = "v3_exq_diag_20260101T000000Z_v3"
        td = self._with_claim_evidence(
            [self._entry(rid, purpose="diagnostic")])
        try:
            out = self._load(reviewed={rid})
        finally:
            td.cleanup()
        self.assertEqual(out, [])

    def test_pass_is_excluded(self):
        rid = "v3_exq_pass_20260101T000000Z_v3"
        td = self._with_claim_evidence([self._entry(rid, status="PASS")])
        try:
            out = self._load(reviewed={rid})
        finally:
            td.cleanup()
        self.assertEqual(out, [])

    def test_dry_run_is_excluded(self):
        rid = "v3_exq_dry_20260101T000000Z_v3"
        td = self._with_claim_evidence([self._entry(rid)])
        try:
            out = self._load(reviewed={rid}, dry={rid})
        finally:
            td.cleanup()
        self.assertEqual(out, [])

    def test_claimless_entry_is_excluded(self):
        """A blank claim_id is not claim-tagged (unlinked_runs owns those)."""
        rid = "v3_exq_noclaim_20260101T000000Z_v3"
        td = self._with_claim_evidence([self._entry(rid, claim_id="")])
        try:
            out = self._load(reviewed={rid})
        finally:
            td.cleanup()
        self.assertEqual(out, [])

    def test_multiple_claim_entries_collapse_to_one_run(self):
        rid = "v3_exq_multi_20260101T000000Z_v3"
        td = self._with_claim_evidence([
            self._entry(rid, claim_id="ARC-017"),
            self._entry(rid, claim_id="MECH-9"),
        ])
        try:
            out = self._load(reviewed={rid})
        finally:
            td.cleanup()
        self.assertEqual(len(out), 1)
        self.assertEqual(sorted(out[0]["claims"]), ["ARC-017", "MECH-9"])


class FailAutopsyGrandfatherTests(unittest.TestCase):
    """First-run seeding must grandfather the legacy corpus, not dump it."""

    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def _tmp_grandfather(self):
        td = tempfile.TemporaryDirectory()
        self.mod.FAIL_AUTOPSY_GRANDFATHER = Path(td.name) / "gf.json"
        return td

    def test_unseeded_returns_none(self):
        td = self._tmp_grandfather()
        try:
            self.assertIsNone(self.mod.load_fail_autopsy_grandfather())
        finally:
            td.cleanup()

    def test_seed_then_load_roundtrips(self):
        td = self._tmp_grandfather()
        try:
            self.mod.seed_fail_autopsy_grandfather({"b", "a", "c"})
            self.assertTrue(self.mod.FAIL_AUTOPSY_GRANDFATHER.exists())
            self.assertEqual(self.mod.load_fail_autopsy_grandfather(),
                             {"a", "b", "c"})
        finally:
            td.cleanup()

    def test_malformed_file_treated_as_unseeded(self):
        td = self._tmp_grandfather()
        try:
            self.mod.FAIL_AUTOPSY_GRANDFATHER.write_text("{ not json")
            self.assertIsNone(self.mod.load_fail_autopsy_grandfather())
        finally:
            td.cleanup()


class ReviewedFailSectionRenderTests(unittest.TestCase):
    """Rendering + the grandfather non-dump guarantee."""

    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def _render(self, fail_needs_autopsy, grandfathered_outstanding=0):
        import io
        from contextlib import redirect_stdout
        written = {}

        class _FakeOut:
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
                    [], [], [], [], "2026-08-08T00:00:00Z",
                    fail_needs_autopsy=fail_needs_autopsy,
                    grandfathered_outstanding=grandfathered_outstanding)
        finally:
            self.mod.OUTPUT = orig
        return written.get("text", "")

    def _fna(self, run_id):
        return {"run_id": run_id, "timestamp_utc": "2026-03-29T03:19:33Z",
                "claims": ["ARC-017"]}

    def test_flagged_run_renders_section_and_counts(self):
        rid = "v3_exq_129_arc017_stream_tag_pair_20260329T031933Z_v3"
        text = self._render([self._fna(rid)])
        self.assertIn("Reviewed FAIL with no confirmed autopsy", text)
        self.assertIn(rid, text)
        self.assertIn("1 reviewed FAIL(s) with no confirmed autopsy", text)
        self.assertIn("Pending: **1** item(s)", text)

    def test_grandfathered_only_does_not_dump_rows(self):
        """First-run shape: 0 flagged, N grandfathered -> the section body does
        NOT render a table, and the pending TOTAL excludes the legacy debt, but
        the count is still visible in the summary header."""
        text = self._render([], grandfathered_outstanding=541)
        self.assertNotIn("| Run ID | Timestamp | Claims |",
                         text.split("How to mark")[0]
                             .split("Reviewed FAIL with no confirmed autopsy")[-1])
        self.assertIn("541 legacy reviewed-FAIL(s) grandfathered", text)
        self.assertIn("Pending: **0** item(s)", text)

    def test_grandfathered_note_shown_alongside_flagged(self):
        text = self._render([self._fna("v3_exq_new_20260808T000000Z_v3")],
                            grandfathered_outstanding=540)
        self.assertIn("540", text)
        self.assertIn("remain un-autopsied", text)


if __name__ == "__main__":
    unittest.main()
