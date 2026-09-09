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
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent / "generate_pending_review.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("ree_gen_pending", SCRIPT_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# The OTHER implementation of the same predicate, in a different repo subtree.
# chip-20260909-isdryrun-parity-gap pins the two against each other.
SYNC_PATH = (SCRIPT_PATH.parent.parent
             / "evidence" / "experiments" / "scripts" / "sync_v3_results.py")


def _load_sync_v3_results():
    spec = importlib.util.spec_from_file_location("ree_sync_v3_results", SYNC_PATH)
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


class ManifestEnumeratorTests(unittest.TestCase):
    """GFLAG-0117: the dry-run readers enumerate ALL THREE manifest shapes.

    Before 2026-09-07 `load_dry_run_run_ids` (and `check_dry_run_citations`'
    private copy of the same walk) scanned the top-level flat manifests and
    the canonical run packs only. The per-type flat shape
    `<experiment_type>/<run_id>.json` -- 797 files live -- was invisible, so a
    dry_run:true stamp there reached no guard. The absence of a test pinning
    the shape set is why it survived; this is that test.
    """

    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def _with_evidence(self, evidence, fn):
        orig = self.mod.EVIDENCE_DIR
        self.mod.EVIDENCE_DIR = evidence
        try:
            return fn()
        finally:
            self.mod.EVIDENCE_DIR = orig

    @staticmethod
    def _populate(evidence):
        """One dry manifest per shape, plus every exclusion the walk must honour."""
        def w(path, obj):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(obj))
        # shape 1: top-level flat
        w(evidence / "v3_exq_1_a_20260101T000000Z_v3.json",
          {"run_id": "v3_exq_1_a_20260101T000000Z_v3", "dry_run": True})
        # shape 2: canonical pack
        w(evidence / "v3_exq_2_b" / "runs" / "v3_exq_2_b_20260101T000000Z_v3" / "manifest.json",
          {"run_id": "v3_exq_2_b_20260101T000000Z_v3", "dry_run": "true"})
        # shape 3: per-type flat -- THE DEFECT
        w(evidence / "v3_exq_3_c" / "v3_exq_3_c_20260101T000000Z_v3.json",
          {"run_id": "v3_exq_3_c_20260101T000000Z_v3", "dry_run": 1})
        # a real (non-dry) per-type flat manifest: enumerated, not a dry id
        w(evidence / "v3_exq_4_d" / "v3_exq_4_d_20260101T000000Z_v3.json",
          {"run_id": "v3_exq_4_d_20260101T000000Z_v3", "result": "PASS"})
        # exclusions: non-manifest registry files at both depths, and a
        # stray *.json directly under a runs/ dir
        w(evidence / "claim_evidence.v1.json", {"entries": [], "dry_run": True})
        w(evidence / "v3_exq_5_e" / "review_tracker.json", {"dry_run": True})
        w(evidence / "runs" / "stray.json", {"run_id": "stray", "dry_run": True})
        return {
            "v3_exq_1_a_20260101T000000Z_v3",
            "v3_exq_2_b_20260101T000000Z_v3",
            "v3_exq_3_c_20260101T000000Z_v3",
        }

    def test_all_three_shapes_are_enumerated(self):
        with tempfile.TemporaryDirectory() as td:
            evidence = Path(td)
            self._populate(evidence)
            paths = self._with_evidence(
                evidence, lambda: [p.relative_to(evidence).as_posix()
                                   for p in self.mod._iter_manifest_paths()])
        self.assertIn("v3_exq_1_a_20260101T000000Z_v3.json", paths)
        self.assertIn("v3_exq_2_b/runs/v3_exq_2_b_20260101T000000Z_v3/manifest.json", paths)
        self.assertIn("v3_exq_3_c/v3_exq_3_c_20260101T000000Z_v3.json", paths,
                      "per-type flat manifest not enumerated (GFLAG-0117)")
        self.assertIn("v3_exq_4_d/v3_exq_4_d_20260101T000000Z_v3.json", paths)
        for excluded in ("claim_evidence.v1.json", "v3_exq_5_e/review_tracker.json",
                         "runs/stray.json"):
            self.assertNotIn(excluded, paths)

    def test_dry_run_ids_include_the_per_type_flat_shape(self):
        with tempfile.TemporaryDirectory() as td:
            evidence = Path(td)
            expected = self._populate(evidence)
            ids = self._with_evidence(evidence, self.mod.load_dry_run_run_ids)
        self.assertEqual(ids, expected)

    def test_missing_evidence_dir_yields_nothing(self):
        with tempfile.TemporaryDirectory() as td:
            missing = Path(td) / "absent"
            paths = self._with_evidence(
                missing, lambda: list(self.mod._iter_manifest_paths()))
            ids = self._with_evidence(missing, self.mod.load_dry_run_run_ids)
        self.assertEqual(paths, [])
        self.assertEqual(ids, set())

    def test_check_dry_run_citations_shares_the_enumerator(self):
        """The second reader must IMPORT the walk, never carry its own copy --
        two independent shape lists is how the third shape went missing."""
        import importlib.util
        import inspect
        import sys
        script = SCRIPT_PATH.parent / "check_dry_run_citations.py"
        if str(SCRIPT_PATH.parent) not in sys.path:
            sys.path.insert(0, str(SCRIPT_PATH.parent))
        spec = importlib.util.spec_from_file_location("ree_check_dry_cit", script)
        cdc = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cdc)
        src = Path(inspect.getsourcefile(cdc._iter_manifest_paths)).resolve()
        self.assertEqual(src, SCRIPT_PATH.resolve())
        self.assertNotIn("def _iter_manifest_paths", script.read_text())


class DryRunPredicateTests(unittest.TestCase):
    """chip-20260902-dryrun-scoring-exclusion-gap: a `_dry_<stamp>` run_id is
    dry even when the pre-pack_writer manifest carries no dry_run field."""

    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def test_flag_forms_still_detected(self):
        for v in (True, "true", "TRUE", 1, "1", "yes"):
            self.assertTrue(self.mod._is_dry_run({"dry_run": v}), v)
        for v in (False, "false", 0, "", None, "no"):
            self.assertFalse(self.mod._is_dry_run({"dry_run": v, "run_id": "x_20260101T000000Z_v3"}), v)

    def test_dry_shaped_run_id_without_flag_is_dry(self):
        # the live 2026-09-07 shape: no dry_run key at all
        for rid in ("v3_exq_329_arc033_e2_harm_s_counterfactual_dry_20260410T155945Z_v3",
                    "v3_exq_375_mech073_valence_geometry_probe_dry_20260413T074214Z_v3",
                    "v3_exq_395_mech220_harm_hub_dry_20260413T074905Z"):
            self.assertTrue(self.mod._is_dry_run({"run_id": rid}), rid)

    def test_bare_dry_substring_is_not_enough(self):
        """`harm_hub_dry` is a real experiment_type stem; the real run must not
        be swallowed by a loose substring match."""
        real = {"run_id": "v3_exq_395_mech220_harm_hub_dry_20260418T101010Z_v3"}
        self.assertTrue(self.mod._is_dry_run(real))  # this one IS the dry shape
        for rid in ("v3_exq_395_mech220_harm_hub_20260418T101010Z_v3",
                    "v3_exq_9_dryness_probe_20260418T101010Z_v3",
                    "v3_exq_9_dry_v3", "v3_exq_9_dry_1775167807_v3", ""):
            self.assertFalse(self.mod._is_dry_run({"run_id": rid}), rid)
        self.assertFalse(self.mod._is_dry_run({}))
        self.assertFalse(self.mod._is_dry_run({"run_id": None}))


class LoadDegenerateEvidenceRunReasonsTests(unittest.TestCase):
    """chip-20260908-pending-review-degenerate-evidence-pass, incident
    V3-EXQ-1007: an experiment_purpose 'evidence' PASS/FAIL whose flat
    manifest carries non_degenerate: false must be surfaced, not silently
    scoring_excluded with no reader-side signal at all."""

    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def _with_manifests(self, manifests):
        with tempfile.TemporaryDirectory() as td:
            evidence = Path(td)
            for name, body in manifests.items():
                (evidence / name).write_text(json.dumps(body))
            orig = self.mod.EVIDENCE_DIR
            self.mod.EVIDENCE_DIR = evidence
            try:
                return self.mod.load_degenerate_evidence_run_reasons()
            finally:
                self.mod.EVIDENCE_DIR = orig

    def test_top_level_non_degenerate_false_is_caught(self):
        out = self._with_manifests({
            "v3_exq_1007_x.json": {
                "run_id": "v3_exq_1007_mech536_eval_persistence_discriminator_20260907T072349Z_v3",
                "experiment_purpose": "evidence",
                "non_degenerate": False,
                "degeneracy_reason": "C2 pre-registered non-degeneracy check failed",
            },
        })
        self.assertEqual(
            out,
            {"v3_exq_1007_mech536_eval_persistence_discriminator_20260907T072349Z_v3":
             "C2 pre-registered non-degeneracy check failed"})

    def test_per_claim_false_is_caught_even_when_top_level_absent(self):
        out = self._with_manifests({
            "a.json": {
                "run_id": "run_a_20260101T000000Z_v3",
                "experiment_purpose": "evidence",
                "non_degenerate_per_claim": {"MECH-001": True, "MECH-002": False},
                "degeneracy_reason": "MECH-002 criterion pinned at floor",
            },
        })
        self.assertIn("run_a_20260101T000000Z_v3", out)

    def test_missing_degeneracy_reason_still_flags_with_placeholder(self):
        out = self._with_manifests({
            "a.json": {
                "run_id": "run_b_20260101T000000Z_v3",
                "experiment_purpose": "evidence",
                "non_degenerate": False,
            },
        })
        self.assertIn("no degeneracy_reason", out["run_b_20260101T000000Z_v3"])

    def test_diagnostic_purpose_is_not_double_counted(self):
        """The diagnostic vacuous_pass net already covers this purpose;
        this function is scoped to 'evidence' only."""
        out = self._with_manifests({
            "a.json": {
                "run_id": "run_c_20260101T000000Z_v3",
                "experiment_purpose": "diagnostic",
                "non_degenerate": False,
                "degeneracy_reason": "irrelevant here",
            },
        })
        self.assertEqual(out, {})

    def test_default_purpose_is_evidence(self):
        """experiment_purpose absent defaults to 'evidence' -- same default
        load_pending_entries and _accumulate_pending_run use."""
        out = self._with_manifests({
            "a.json": {
                "run_id": "run_d_20260101T000000Z_v3",
                "non_degenerate": False,
                "degeneracy_reason": "x",
            },
        })
        self.assertIn("run_d_20260101T000000Z_v3", out)

    def test_true_or_absent_non_degenerate_is_not_flagged(self):
        out = self._with_manifests({
            "a.json": {"run_id": "run_e_20260101T000000Z_v3",
                       "experiment_purpose": "evidence", "non_degenerate": True},
            "b.json": {"run_id": "run_f_20260101T000000Z_v3",
                       "experiment_purpose": "evidence"},
        })
        self.assertEqual(out, {})


class DegenerateEvidenceSectionRenderTests(unittest.TestCase):
    """The rendered section: non-exclusionary (stays in PASS/FAIL too), names
    the reason, and does not fire on a clean or non-evidence corpus."""

    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def _run(self, run_id="v3_exq_1007_x_20260907T072349Z_v3", status="PASS", **kw):
        r = {"run_id": run_id, "timestamp_utc": "2026-09-07T07:23:49Z",
             "status": status, "claims": ["MECH-536"], "failure_signatures": [],
             "adjudication": "n/a", "interpretation_label": "",
             "recorded_preconditions_unmet": [], "preconditions_scope_note": "",
             "z_goal_stream": {}}
        r.update(kw)
        return r

    def _render(self, runs, manifests):
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

        with tempfile.TemporaryDirectory() as td:
            evidence = Path(td)
            for name, body in manifests.items():
                (evidence / name).write_text(json.dumps(body))
            orig_evidence = self.mod.EVIDENCE_DIR
            orig_output = self.mod.OUTPUT
            self.mod.EVIDENCE_DIR = evidence
            self.mod.OUTPUT = _FakeOut(written)
            try:
                with redirect_stdout(io.StringIO()):
                    self.mod.write_pending_review(
                        list(runs), [], [], [], "2026-09-08T00:00:00Z")
            finally:
                self.mod.EVIDENCE_DIR = orig_evidence
                self.mod.OUTPUT = orig_output
        return written.get("text", "")

    def test_degenerate_evidence_pass_gets_flagged_and_stays_in_pass_table(self):
        rid = "v3_exq_1007_x_20260907T072349Z_v3"
        text = self._render(
            [self._run(run_id=rid)],
            {"m.json": {"run_id": rid, "experiment_purpose": "evidence",
                        "non_degenerate": False,
                        "degeneracy_reason": "C2 check failed"}})
        self.assertIn("flagged degenerate", text)
        self.assertIn("route to /failure-autopsy", text.lower())
        self.assertIn("C2 check failed", text)
        # Non-exclusionary: still present in the plain PASS table too.
        self.assertIn("## PASS (verify & close)", text)
        pass_section = text.split("## PASS (verify & close)")[1].split("##")[0]
        self.assertIn(rid, pass_section)

    def test_clean_evidence_run_produces_no_section(self):
        rid = "v3_exq_clean_20260101T000000Z_v3"
        text = self._render(
            [self._run(run_id=rid)],
            {"m.json": {"run_id": rid, "experiment_purpose": "evidence",
                        "non_degenerate": True}})
        self.assertNotIn("flagged degenerate", text)

    def test_no_manifest_on_disk_produces_no_section(self):
        text = self._render([self._run()], {})
        self.assertNotIn("flagged degenerate", text)

    def test_section_does_not_change_pending_counts(self):
        rid = "v3_exq_1007_x_20260907T072349Z_v3"
        clean = self._render([self._run(run_id=rid)], {})
        flagged = self._render(
            [self._run(run_id=rid)],
            {"m.json": {"run_id": rid, "experiment_purpose": "evidence",
                        "non_degenerate": False, "degeneracy_reason": "x"}})
        for text in (clean, flagged):
            self.assertIn("Pending: **1** item(s)", text)
            self.assertIn("1 PASS, 0 FAIL", text)


class DryRunArmParityTests(unittest.TestCase):
    """chip-20260909-isdryrun-parity-gap: the two dryness checks over the SAME
    corpus had DIFFERENT arms, and diverged silently for months.

    sync_v3_results._is_dry_run had three arms (flag / `_dry_` FILENAME prefix /
    bare `_dry` run_id suffix); generate_pending_review._is_dry_run had two
    (flag / `_dry_<stamp>` run_id regex). Measured 2026-09-09: 15 dry manifests
    leaked past pending_review and GOV-DRY-1 while sync kept every one of them
    out of claim_evidence.v1.json -- 14 carried an ASSERTING evidence_direction
    and 14 were already in reviewed_run_ids.

    The parity test below is the load-bearing one: pinning each arm separately
    would not have caught this defect, because each implementation was
    internally consistent. Only comparing them against each other does.
    """

    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()
        cls.sync = _load_sync_v3_results()

    # --- the two arms generate_pending_review was missing -------------------

    def test_bare_dry_suffix_run_id_is_dry(self):
        """No timestamp at all -- `_DRY_RUN_ID_RE` cannot express this."""
        for rid in ("v3_exq_324b_sd020_harm_surprise_pe_dry",
                    "v3_exq_259_wanting_gradient_navigation_dry",
                    "v3_exq_321a_mech090_bistable_gate_dry"):
            self.assertTrue(self.mod._is_dry_run({"run_id": rid}), rid)

    def test_dry_filename_prefix_is_dry_even_when_run_id_is_clean(self):
        """`pack_writer.write_flat_manifest` marks a smoke by PREFIXING the
        filename and leaves the run_id untouched -- the live 918a shape. No
        key-based arm can see it, which is why the path parameter exists."""
        rid = "v3_exq_918a_sd_residue_valence_bound_validation_20260909T062139Z_v3"
        d = {"run_id": rid}
        self.assertFalse(self.mod._is_dry_run(d), "run_id alone is clean")
        self.assertTrue(self.mod._is_dry_run(d, Path("_dry_%s.json" % rid)))

    def test_path_argument_is_optional(self):
        """Pre-existing callers pass no path; they must keep working."""
        self.assertTrue(self.mod._is_dry_run({"dry_run": True}))
        self.assertFalse(self.mod._is_dry_run({"run_id": "x_20260101T000000Z_v3"}))

    def test_widening_does_not_swallow_the_harm_hub_dry_near_miss(self):
        """`harm_hub_dry` is a real experiment_type STEM. It is always followed
        by the run's timestamp, so a genuine run never ENDS in `_dry` -- the
        documented false-positive risk for the bare-suffix arm."""
        for rid in ("v3_exq_395_mech220_harm_hub_20260418T101010Z_v3",
                    "v3_exq_9_dryness_probe_20260418T101010Z_v3",
                    "v3_exq_9_dry_v3", "v3_exq_9_dry_1775167807_v3"):
            self.assertFalse(self.mod._is_dry_run({"run_id": rid}), rid)
            self.assertFalse(
                self.mod._is_dry_run({"run_id": rid}, Path("%s.json" % rid)), rid)

    # --- the parity itself, which is the actual regression -----------------

    def test_the_two_implementations_agree_on_every_shape(self):
        """THE defect was silent divergence -- pin the agreement, not the arms.

        Any future edit that adds an arm to one side and not the other fails
        here, naming the shape it disagreed on.
        """
        stems = [
            # dry: bare suffix / timestamped / filename-prefixed / flagged
            "v3_exq_324b_sd020_harm_surprise_pe_dry",
            "v3_exq_395_mech220_harm_hub_dry_20260413T074905Z",
            "v3_exq_329_arc033_e2_harm_s_counterfactual_dry_20260410T155945Z_v3",
            # not dry, including the near-misses
            "v3_exq_395_mech220_harm_hub_20260418T101010Z_v3",
            "v3_exq_9_dryness_probe_20260418T101010Z_v3",
            "v3_exq_9_dry_v3",
            "v3_exq_9_dry_1775167807_v3",
            "",
        ]
        disagreements = []
        for rid in stems:
            for flag in ({}, {"dry_run": True}, {"dry_run": False}):
                for name in ("%s.json" % rid, "_dry_%s.json" % rid):
                    d = dict(flag)
                    if rid:
                        d["run_id"] = rid
                    p = Path(name)
                    mine = self.mod._is_dry_run(d, p)
                    theirs = self.sync._is_dry_run(d, p)
                    if mine != theirs:
                        disagreements.append(
                            "run_id=%r file=%r flag=%r: pending_review=%s sync=%s"
                            % (rid, name, flag.get("dry_run"), mine, theirs))
        self.assertEqual(disagreements, [], "\n".join(disagreements))

    def test_sync_arms_are_a_subset_of_ours(self):
        """Directional guard: whatever sync calls dry, we must call dry.

        sync is the side that (correctly) kept all 15 leakers out of
        claim_evidence.v1.json, so its arms are the floor.
        """
        for rid, name in (
                ("v3_exq_324b_sd020_harm_surprise_pe_dry", "x.json"),
                ("clean_run_20260909T000000Z_v3", "_dry_clean.json"),
        ):
            d = {"run_id": rid}
            p = Path(name)
            self.assertTrue(self.sync._is_dry_run(d, p), (rid, name))
            self.assertTrue(self.mod._is_dry_run(d, p), (rid, name))


class DryRunSharedHelperTests(unittest.TestCase):
    """"One truthiness check, three consumers" -- no inline re-spellings.

    `flat_only_silent_drop_guard` carried a FOURTH divergent copy of this
    predicate (flag + bare-suffix only) until chip-20260909-isdryrun-parity-gap.
    """

    def test_generate_pending_review_has_exactly_one_dryness_predicate(self):
        src = SCRIPT_PATH.read_text()
        self.assertEqual(src.count("def _is_dry_run"), 1)
        # the inline spelling: a dry_run truthiness test not routed through the helper
        self.assertNotIn('or str(run_id).endswith("_dry")', src)

    def test_every_call_site_passes_the_path(self):
        """The filename arm is unreachable from a call that drops the path."""
        import re as _re
        src = SCRIPT_PATH.read_text()
        calls = _re.findall(r"[^f]_is_dry_run\(([^)]*)\)", src)
        bare = [c for c in calls
                if c.strip() and "," not in c and "flat_path" not in c]
        self.assertEqual(bare, [], "call sites dropping the path: %r" % bare)

    def test_check_dry_run_citations_passes_the_path(self):
        """GOV-DRY-1 reads dryness transitively through this module."""
        p = SCRIPT_PATH.parent / "check_dry_run_citations.py"
        self.assertIn("_is_dry_run(d, f)", p.read_text())


def _load_consumer(name):
    """Load one of the scripts/ modules that consume the dryness predicate."""
    path = SCRIPT_PATH.parent / name
    spec = importlib.util.spec_from_file_location("ree_consumer_%s" % path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


class DryRunConsumerParityTests(unittest.TestCase):
    """chip-20260909-isdryrun-sixway-divergence: the SAME defect, wider scope.

    chip-20260909-isdryrun-parity-gap brought the two PRIMARY dryness checks
    (generate_pending_review, sync_v3_results) to four-arm parity. FOUR more
    independent definitions of the same predicate remained, each with a
    different arm subset. Measured against the 136 canonical dry manifests in
    the live corpus on 2026-09-09:

        audit_flat_only_orphaned_manifests    arms 1,2,3'   MISSED 26
        check_substrate_staleness_candidates  arm 1 only    MISSED 41
        check_unapplied_autopsy_recommendations arms 1,4    MISSED 15
        check_manifest_degeneracy_consistency arm 1 (no str-cast)
                                              + params.dry_run  MISSED 41

    Two consumers now IMPORT the canonical predicate outright and have no local
    definition at all. Two keep a thin local wrapper because each carries ONE
    arm the canonical predicate does not:

      * audit_flat_only_orphaned_manifests -- `path.stem.endswith("_dry")`, a
        FILENAME suffix (canonical's bare-suffix arm reads the RUN_ID). Kept
        because build_experiment_indexes._load_dry_run_run_ids (:1451) carries
        it and this audit mirrors that discovery path.
      * check_manifest_degeneracy_consistency -- nested `params.dry_run`. A live
        SHAPE (41 manifests carry the key) that is never True anywhere in the
        corpus, so it is kept local rather than promoted into canonical.

    Both wrappers are pinned below as SUPERSETS of canonical: never narrower,
    and the extra arm must stay demonstrably additive.
    """

    WRAPPER_CONSUMERS = (
        "audit_flat_only_orphaned_manifests.py",
        "check_manifest_degeneracy_consistency.py",
    )
    IMPORTING_CONSUMERS = (
        "check_substrate_staleness_candidates.py",
        "check_unapplied_autopsy_recommendations.py",
    )

    # Every shape the six implementations disagreed on, plus the near-misses.
    SHAPES = (
        # (run_id, filename, dry_run flag) -> canonical verdict is the oracle
        ("v3_exq_324b_sd020_harm_surprise_pe_dry", "x.json", None),
        ("v3_exq_259_wanting_gradient_navigation_dry", "x.json", None),
        ("v3_exq_395_mech220_harm_hub_dry_20260413T074905Z", "x.json", None),
        ("v3_exq_329_arc033_e2_harm_s_counterfactual_dry_20260410T155945Z_v3",
         "x.json", None),
        ("v3_exq_918a_sd_residue_valence_bound_validation_20260909T062139Z_v3",
         "_dry_v3_exq_918a.json", None),
        ("clean_run_20260909T000000Z_v3", "clean_run.json", None),
        ("clean_run_20260909T000000Z_v3", "clean_run.json", True),
        ("clean_run_20260909T000000Z_v3", "clean_run.json", "yes"),
        ("clean_run_20260909T000000Z_v3", "clean_run.json", 1),
        ("clean_run_20260909T000000Z_v3", "clean_run.json", False),
        # the documented false-positive risks for the bare-suffix arm
        ("v3_exq_395_mech220_harm_hub_20260418T101010Z_v3", "x.json", None),
        ("v3_exq_9_dryness_probe_20260418T101010Z_v3", "x.json", None),
        ("v3_exq_9_dry_v3", "x.json", None),
        ("v3_exq_9_dry_1775167807_v3", "x.json", None),
    )

    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def _cases(self):
        for rid, name, flag in self.SHAPES:
            d = {"run_id": rid}
            if flag is not None:
                d["dry_run"] = flag
            yield d, Path(name)

    # --- the two that import outright --------------------------------------

    def test_importing_consumers_have_no_local_definition(self):
        """A local `def _is_dry_run` here IS the divergence -- there must be none."""
        for name in self.IMPORTING_CONSUMERS:
            src = (SCRIPT_PATH.parent / name).read_text()
            self.assertEqual(
                src.count("def _is_dry_run"), 0,
                "%s re-spelled the predicate instead of importing it" % name)
            self.assertIn("from generate_pending_review import", src, name)

    def test_importing_consumers_bind_the_canonical_code(self):
        """Not merely a same-named function -- code DEFINED IN the canonical file.

        Identity against `_load_module()` cannot be used: that loads the canonical
        file under a fresh module name, so it yields a different function object
        than the consumer's real `import generate_pending_review`. Comparing the
        defining filename is both correct and stronger -- it fails for a local
        re-spelling that happens to share the name.
        """
        for name in self.IMPORTING_CONSUMERS:
            mod = _load_consumer(name)
            self.assertEqual(
                Path(mod._is_dry_run.__code__.co_filename).resolve(), SCRIPT_PATH,
                "%s binds a _is_dry_run defined outside the canonical module" % name)

    # --- the two that keep a documented local arm --------------------------

    def test_wrappers_are_supersets_of_canonical(self):
        """Whatever canonical calls dry, the wrapper must call dry.

        This is the direction that matters: a wrapper NARROWER than canonical is
        exactly the defect (a smoke read as evidence). Wider is allowed only for
        the one documented extra arm each.
        """
        failures = []
        for name in self.WRAPPER_CONSUMERS:
            mod = _load_consumer(name)
            for d, p in self._cases():
                if self.mod._is_dry_run(d, p) and not mod._is_dry_run(d, p):
                    failures.append("%s: %r %r" % (name, d, str(p)))
        self.assertEqual(failures, [], "\n".join(failures))

    def test_wrapper_extra_arms_are_the_documented_ones_only(self):
        """A wrapper may be WIDER than canonical only where it is documented.

        Any other over-firing shape means an undocumented arm crept in.
        """
        audit = _load_consumer("audit_flat_only_orphaned_manifests.py")
        degen = _load_consumer("check_manifest_degeneracy_consistency.py")

        # audit: the ONE extra arm is a filename stem ending `_dry`.
        clean = {"run_id": "clean_run_20260909T000000Z_v3"}
        self.assertFalse(self.mod._is_dry_run(clean, Path("some_run_dry.json")))
        self.assertTrue(audit._is_dry_run(clean, Path("some_run_dry.json")))
        for d, p in self._cases():
            if audit._is_dry_run(d, p) and not self.mod._is_dry_run(d, p):
                self.assertTrue(p.stem.endswith("_dry"),
                                "undocumented extra arm in audit: %r %r" % (d, str(p)))

        # degeneracy: the ONE extra arm is nested params.dry_run is True.
        self.assertFalse(self.mod._is_dry_run({"params": {"dry_run": True}}, Path("x.json")))
        self.assertTrue(degen._is_dry_run({"params": {"dry_run": True}}, Path("x.json")))
        for d, p in self._cases():
            if degen._is_dry_run(d, p) and not self.mod._is_dry_run(d, p):
                params = d.get("params")
                self.assertTrue(isinstance(params, dict) and params.get("dry_run") is True,
                                "undocumented extra arm in degeneracy: %r" % (d,))

    def test_degeneracy_wrapper_gained_the_str_cast(self):
        """It checked `dry_run is True` ONLY -- the corpus carries int/str too."""
        degen = _load_consumer("check_manifest_degeneracy_consistency.py")
        for flag in (True, 1, "true", "True", "yes", "1"):
            self.assertTrue(degen._is_dry_run({"dry_run": flag}, Path("x.json")), flag)
        for flag in (False, 0, "false", "no", ""):
            self.assertFalse(degen._is_dry_run({"dry_run": flag}, Path("x.json")), flag)

    # --- every consumer passes the path ------------------------------------

    def test_every_consumer_call_site_passes_the_path(self):
        """The `_dry_` FILENAME-prefix arm is unreachable from a pathless call.

        That arm is the only one that can see a smoke whose run_id pack_writer
        left untouched -- the live 918a shape, and one of the 15 leakers.
        """
        import re as _re
        offenders = []
        for name in self.WRAPPER_CONSUMERS + self.IMPORTING_CONSUMERS:
            src = (SCRIPT_PATH.parent / name).read_text()
            for call in _re.findall(r"[^f_]_is_dry_run\(([^)]*)\)", src):
                call = call.strip()
                if not call or "," in call or call.startswith("manifest: "):
                    continue
                offenders.append("%s: _is_dry_run(%s)" % (name, call))
        self.assertEqual(offenders, [], "\n".join(offenders))


if __name__ == "__main__":
    unittest.main()
