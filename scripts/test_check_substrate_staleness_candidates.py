#!/usr/bin/env python3
"""Contract tests for check_substrate_staleness_candidates.py (Phase 0 drift-candidate report).

Design plan: REE_assembly/evidence/planning/substrate_stability_and_drift_detection_plan.md

Unit tests cover the pure filtering helpers (_is_dry_run, _already_actioned,
load_flat_claim_tagged_manifests, _display_path). The end-to-end test builds REAL git repos
in a tempdir (a bare "origin" + a local clone standing in for the ree-v3 checkout) and copies
the ACTUAL ree-v3/experiments/_lib/arm_fingerprint.py into the fixture tree, so the test
exercises the real compute_substrate_hash rather than a reimplementation -- proving the
script's own selling point (never reimplement the hash algorithm) is true in practice, not
just asserted in a docstring.

Run: /opt/local/bin/python3 scripts/test_check_substrate_staleness_candidates.py
"""

from __future__ import annotations

import ast
import contextlib
import importlib.util
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]  # REE_assembly root
SCRIPT_PATH = REPO_ROOT / "scripts" / "check_substrate_staleness_candidates.py"
REAL_ARM_FINGERPRINT = REPO_ROOT.parent / "ree-v3" / "experiments" / "_lib" / "arm_fingerprint.py"
REAL_DEFAULT_OFF_GUARD = REPO_ROOT / "scripts" / "default_off_drift_guard.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("check_substrate_staleness_candidates", SCRIPT_PATH)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["check_substrate_staleness_candidates"] = mod
    spec.loader.exec_module(mod)
    return mod


MOD = _load_module()


def _run(cmd, cwd=None):
    proc = subprocess.run(cmd, cwd=str(cwd) if cwd else None, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)} failed: {proc.stderr}")
    return proc.stdout


def _git(repo, *args):
    return _run(["git"] + list(args), cwd=repo)


class IsDryRunTests(unittest.TestCase):
    def test_bool_true(self):
        self.assertTrue(MOD._is_dry_run({"dry_run": True}))

    def test_bool_false(self):
        self.assertFalse(MOD._is_dry_run({"dry_run": False}))

    def test_truthy_string(self):
        for s in ("true", "True", "1", "yes"):
            self.assertTrue(MOD._is_dry_run({"dry_run": s}), s)

    def test_falsey_string_and_absent(self):
        self.assertFalse(MOD._is_dry_run({"dry_run": "false"}))
        self.assertFalse(MOD._is_dry_run({}))


class AlreadyActionedTests(unittest.TestCase):
    def test_none_set(self):
        self.assertFalse(MOD._already_actioned({"claim_ids": ["X"]}))

    def test_superseded_direction(self):
        self.assertTrue(MOD._already_actioned({"evidence_direction": "superseded"}))

    def test_pending_retest_bool(self):
        self.assertTrue(MOD._already_actioned({"pending_retest_after_substrate": True}))
        self.assertFalse(MOD._already_actioned({"pending_retest_after_substrate": False}))

    def test_superseded_by_substrate_string(self):
        self.assertTrue(MOD._already_actioned({"superseded_by_substrate": "SD-070@2026-08-01"}))
        self.assertFalse(MOD._already_actioned({"superseded_by_substrate": ""}))

    def test_per_claim_list(self):
        self.assertTrue(MOD._already_actioned({"pending_retest_after_substrate_per_claim": ["MECH-1"]}))
        self.assertFalse(MOD._already_actioned({"pending_retest_after_substrate_per_claim": []}))

    def test_per_claim_dict(self):
        self.assertTrue(MOD._already_actioned({"superseded_by_substrate_per_claim": {"MECH-1": "SD-1@2026-01-01"}}))
        self.assertFalse(MOD._already_actioned({"superseded_by_substrate_per_claim": {}}))


class LoadFlatManifestsTests(unittest.TestCase):
    def test_filters_correctly(self):
        with tempfile.TemporaryDirectory() as d:
            exp_dir = Path(d)
            (exp_dir / "claim_tagged.json").write_text(json.dumps({"claim_ids": ["MECH-1"], "run_id": "a"}))
            (exp_dir / "no_claim.json").write_text(json.dumps({"claim_ids": [], "run_id": "b"}))
            (exp_dir / "dry_run.json").write_text(json.dumps({"claim_ids": ["MECH-2"], "dry_run": True, "run_id": "c"}))
            (exp_dir / "malformed.json").write_text("{not json")
            (exp_dir / "subdir").mkdir()
            (exp_dir / "subdir" / "nested.json").write_text(json.dumps({"claim_ids": ["MECH-3"]}))

            out = MOD.load_flat_claim_tagged_manifests(exp_dir)
            run_ids = sorted(m.get("run_id") for _, m in out)
            self.assertEqual(run_ids, ["a"])  # no_claim, dry_run, malformed, nested all excluded


class FileInScopeTests(unittest.TestCase):
    def test_exact_path(self):
        self.assertTrue(MOD._file_in_scope("ree_core/agent.py", ["ree_core/agent.py"]))
        self.assertFalse(MOD._file_in_scope("ree_core/goal.py", ["ree_core/agent.py"]))

    def test_recursive_glob_zero_intervening_dirs(self):
        # The dangerous direction: a naive '**' -> '*' substitution with a literal '/' on
        # both sides would REQUIRE an intervening path segment and miss this -- must not.
        self.assertTrue(MOD._file_in_scope(
            "ree_core/predictors/e1_deep.py", ["ree_core/predictors/**/*.py"]))

    def test_recursive_glob_one_intervening_dir(self):
        self.assertTrue(MOD._file_in_scope(
            "ree_core/predictors/sub/e2.py", ["ree_core/predictors/**/*.py"]))

    def test_recursive_glob_no_match_outside_prefix(self):
        self.assertFalse(MOD._file_in_scope(
            "ree_core/goal.py", ["ree_core/predictors/**/*.py"]))

    def test_recursive_glob_no_false_prefix_match(self):
        # "ree_core_other/..." must not match a "ree_core/**" scope (prefix, not substring).
        self.assertFalse(MOD._file_in_scope(
            "ree_core_other/foo.py", ["ree_core/**/*.py"]))

    def test_multiple_globs_any_match(self):
        scope = ["ree_core/agent.py", "experiments/_lib/allon_training.py"]
        self.assertTrue(MOD._file_in_scope("experiments/_lib/allon_training.py", scope))
        self.assertFalse(MOD._file_in_scope("ree_core/goal.py", scope))


class LoadClaimSubstrateScopesTests(unittest.TestCase):
    def test_loads_declared_scopes_only(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "claims.yaml"
            p.write_text(
                "claims:\n"
                "  - id: MECH-A\n"
                "    substrate_scope:\n"
                "      - ree_core/agent.py\n"
                "      - ree_core/goal.py\n"
                "  - id: MECH-B\n"
                "    title: no scope declared\n"
            )
            scopes = MOD.load_claim_substrate_scopes(p)
            self.assertEqual(scopes, {"MECH-A": ["ree_core/agent.py", "ree_core/goal.py"]})

    def test_missing_file_returns_empty(self):
        self.assertEqual(MOD.load_claim_substrate_scopes(Path("/no/such/claims.yaml")), {})

    def test_malformed_yaml_returns_empty(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "claims.yaml"
            p.write_text("not: [valid: yaml: at all")
            self.assertEqual(MOD.load_claim_substrate_scopes(p), {})


def _test_expr(src: str) -> ast.AST:
    return ast.parse(src, mode="eval").body


class EvalFlagFormulaTests(unittest.TestCase):
    """The tri-valued (Kleene) evaluator -- correctness here is safety-critical, since a wrong
    True/False verdict is what could wrongly downgrade a genuinely-relevant drift candidate."""

    KNOBS = {"use_foo", "use_bar"}

    def test_single_flag_disabled(self):
        node = _test_expr("self.config.use_foo")
        self.assertFalse(MOD._eval_flag_formula(node, self.KNOBS, {"use_foo": False}))

    def test_single_flag_unknown(self):
        node = _test_expr("self.config.use_foo")
        self.assertIsNone(MOD._eval_flag_formula(node, self.KNOBS, {}))  # not in flag_status

    def test_not_flag(self):
        node = _test_expr("not self.config.use_foo")
        self.assertTrue(MOD._eval_flag_formula(node, self.KNOBS, {"use_foo": False}))

    def test_and_short_circuits_on_confirmed_false(self):
        # False AND Unknown == False -- one confirmed-disabled flag is enough, regardless of
        # what the other, unresolved operand might be. This is the property Phase 1b needs.
        node = _test_expr("self.config.use_foo and self.config.use_bar")
        self.assertFalse(MOD._eval_flag_formula(node, self.KNOBS, {"use_foo": False}))

    def test_and_all_disabled_is_false(self):
        node = _test_expr("self.config.use_foo and self.config.use_bar")
        self.assertFalse(MOD._eval_flag_formula(
            node, self.KNOBS, {"use_foo": False, "use_bar": False}))

    def test_and_unknown_only_is_unknown(self):
        node = _test_expr("self.config.use_foo and self.config.use_bar")
        self.assertIsNone(MOD._eval_flag_formula(node, self.KNOBS, {}))

    def test_or_all_disabled_is_false(self):
        node = _test_expr("self.config.use_foo or self.config.use_bar")
        self.assertFalse(MOD._eval_flag_formula(
            node, self.KNOBS, {"use_foo": False, "use_bar": False}))

    def test_or_one_unknown_is_unknown(self):
        # Or(False, Unknown) == Unknown -- cannot rule out the Unknown side being True.
        node = _test_expr("self.config.use_foo or self.config.use_bar")
        self.assertIsNone(MOD._eval_flag_formula(node, self.KNOBS, {"use_foo": False}))

    def test_and_with_non_flag_leaf_still_short_circuits_on_confirmed_false(self):
        # Real Python "and" short-circuits on a False left operand -- it never evaluates the
        # right side at all, so "use_foo and some_runtime_check()" is DEFINITELY False when
        # use_foo is confirmed disabled, regardless of what the call would have returned.
        node = _test_expr("self.config.use_foo and some_runtime_check()")
        self.assertFalse(MOD._eval_flag_formula(node, self.KNOBS, {"use_foo": False}))

    def test_or_with_non_flag_leaf_and_no_confirmed_true_is_unknown(self):
        # Unlike "and", "or" genuinely depends on the unresolvable right side here -- correctly
        # Unknown, not a guess in either direction.
        node = _test_expr("self.config.use_foo or some_runtime_check()")
        self.assertIsNone(MOD._eval_flag_formula(node, self.KNOBS, {"use_foo": False}))

    def test_unrelated_name_disqualifies(self):
        node = _test_expr("some_unrelated_flag")
        self.assertIsNone(MOD._eval_flag_formula(node, self.KNOBS, {}))


class InertLineRangesTests(unittest.TestCase):
    SOURCE = (
        "def f(self):\n"
        "    x = 1\n"
        "    if self.config.use_foo:\n"
        "        y = 2\n"
        "        z = 3\n"
        "    w = 4\n"
        "    if some_runtime_check():\n"
        "        q = 5\n"
    )

    def test_confirmed_disabled_if_body_is_inert(self):
        ranges = MOD.inert_line_ranges(self.SOURCE, {"use_foo"}, {"use_foo": False})
        self.assertEqual(len(ranges), 1)
        lo, hi = ranges[0]
        # Line 3 is "if self.config.use_foo:" itself -- included because a newly-added if-line
        # whose condition is confirmed False is itself inert, not just its body (lines 4-5).
        self.assertEqual((lo, hi), (3, 5))

    def test_unrelated_if_is_not_inert(self):
        ranges = MOD.inert_line_ranges(self.SOURCE, {"use_foo"}, {"use_foo": False})
        # line 8 ("q = 5") must not be covered by any inert range
        self.assertFalse(any(lo <= 8 <= hi for lo, hi in ranges))

    def test_unknown_status_yields_no_inert_ranges(self):
        ranges = MOD.inert_line_ranges(self.SOURCE, {"use_foo"}, {})
        self.assertEqual(ranges, [])

    def test_syntax_error_yields_empty(self):
        self.assertEqual(MOD.inert_line_ranges("def f(:\n", {"use_foo"}, {"use_foo": False}), [])


class FlagStatusFromDriverSourceTests(unittest.TestCase):
    def test_absent_name_is_confirmed_disabled(self):
        status = MOD.flag_status_from_driver_source("agent = REEAgent()\n", {"use_foo"})
        self.assertEqual(status, {"use_foo": False})

    def test_present_name_is_omitted_not_guessed(self):
        status = MOD.flag_status_from_driver_source(
            "cfg = REEConfig(use_foo=True)\n", {"use_foo"})
        self.assertEqual(status, {})  # NOT {"use_foo": True} -- a substring hit proves nothing

    def test_word_boundary_avoids_partial_match(self):
        # "use_foobar" must not count as a mention of "use_foo".
        status = MOD.flag_status_from_driver_source("use_foobar = 1\n", {"use_foo"})
        self.assertEqual(status, {"use_foo": False})

    def test_none_source_yields_empty(self):
        self.assertEqual(MOD.flag_status_from_driver_source(None, {"use_foo"}), {})


class FlagStatusFromRecordedConfigTests(unittest.TestCase):
    """P1c consumer: substrate_stability_and_drift_detection_plan.md section 6."""

    def test_no_field_at_all_yields_empty(self):
        # {} here means "field absent" -- the caller's signal to fall back to the proxy.
        status = MOD.flag_status_from_recorded_config({}, {"use_foo", "use_bar"})
        self.assertEqual(status, {})

    def test_recorded_and_empty_confirms_every_knob_disabled(self):
        # A manifest that DID record (agent given, nothing enabled) must yield a full
        # entry per knob -- all False -- not {} (which would look like "never measured").
        manifest = {"enabled_default_off_flags": {}}
        status = MOD.flag_status_from_recorded_config(manifest, {"use_foo", "use_bar"})
        self.assertEqual(status, {"use_foo": False, "use_bar": False})

    def test_recorded_flag_is_confirmed_enabled(self):
        manifest = {"enabled_default_off_flags": {"use_foo": True}}
        status = MOD.flag_status_from_recorded_config(manifest, {"use_foo", "use_bar"})
        self.assertEqual(status, {"use_foo": True, "use_bar": False})

    def test_matches_on_trailing_dotted_segment(self):
        # manifest_core records nested paths (e.g. "goal.use_hierarchical_goal_credit");
        # knob_names from parse_knobs() are bare field names -- must still match.
        manifest = {"enabled_default_off_flags": {"goal.use_hierarchical_goal_credit": True}}
        status = MOD.flag_status_from_recorded_config(manifest, {"use_hierarchical_goal_credit"})
        self.assertEqual(status, {"use_hierarchical_goal_credit": True})

    def test_non_dict_field_yields_empty(self):
        self.assertEqual(MOD.flag_status_from_recorded_config({"enabled_default_off_flags": None}, {"use_foo"}), {})
        self.assertEqual(MOD.flag_status_from_recorded_config({"enabled_default_off_flags": "garbage"}, {"use_foo"}), {})


class LoadDefaultOffKnobNamesTests(unittest.TestCase):
    @unittest.skipUnless(REAL_DEFAULT_OFF_GUARD.exists(), "default_off_drift_guard.py not present")
    def test_real_guard_and_config_yield_a_nonempty_set(self):
        names = MOD.load_default_off_knob_names(REAL_DEFAULT_OFF_GUARD)
        self.assertIsInstance(names, set)
        self.assertGreater(len(names), 0)

    def test_missing_guard_path_yields_empty(self):
        self.assertEqual(MOD.load_default_off_knob_names(Path("/no/such/guard.py")), set())


class ChangedLineNumbersAndDefaultOffOnlyTests(unittest.TestCase):
    """A small, self-contained git repo (distinct from EndToEndDetectionTests' bigger fixture)
    to exercise changed_line_numbers' hunk-header parsing and file_is_default_off_only's full
    pipeline against real git diff output."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name) / "repo"
        self.repo.mkdir()
        _git(self.repo, "init", "-b", "main")
        _git(self.repo, "config", "user.email", "test@example.com")
        _git(self.repo, "config", "user.name", "Test")

        (self.repo / "ree_core").mkdir()
        (self.repo / "ree_core" / "gated.py").write_text(
            "def f(self):\n"
            "    x = 1\n"
            "    return x\n"
        )
        _git(self.repo, "add", "-A")
        _git(self.repo, "commit", "-m", "commit A")
        self.commit_a = _git(self.repo, "rev-parse", "HEAD").strip()

        # New commit adds an inert (default-off-gated) branch AND leaves the rest unchanged.
        (self.repo / "ree_core" / "gated.py").write_text(
            "def f(self):\n"
            "    x = 1\n"
            "    if self.config.use_foo:\n"
            "        x = 2\n"
            "    return x\n"
        )
        _git(self.repo, "add", "-A")
        _git(self.repo, "commit", "-m", "commit B -- adds an inert branch")
        self.commit_b = _git(self.repo, "rev-parse", "HEAD").strip()

    def tearDown(self):
        self._tmp.cleanup()

    def test_changed_line_numbers_matches_real_diff(self):
        lines = MOD.changed_line_numbers(self.repo, self.commit_a, self.commit_b, "ree_core/gated.py")
        self.assertEqual(sorted(lines), [3, 4])  # the two new lines in the post-image

    def test_changed_line_numbers_undiffable_ref_returns_none(self):
        lines = MOD.changed_line_numbers(self.repo, "0" * 40, self.commit_b, "ree_core/gated.py")
        self.assertIsNone(lines)

    def test_file_is_default_off_only_true_when_gated_and_unreferenced(self):
        verdict = MOD.file_is_default_off_only(
            self.repo, self.commit_a, self.commit_b, "ree_core/gated.py",
            {"use_foo"}, {"use_foo": False})
        self.assertTrue(verdict)

    def test_file_is_default_off_only_not_true_when_flag_status_unknown(self):
        # If the driver source MENTIONED use_foo, flag_status wouldn't map it at all --
        # simulate that: pass {} rather than {"use_foo": False}. The exact non-True value
        # (False or None) is an implementation detail the caller doesn't need to
        # distinguish -- both mean "stays a candidate" (see the function's own docstring).
        verdict = MOD.file_is_default_off_only(
            self.repo, self.commit_a, self.commit_b, "ree_core/gated.py",
            {"use_foo"}, {})
        self.assertIsNot(verdict, True)

    def test_file_is_default_off_only_false_for_non_py_file(self):
        verdict = MOD.file_is_default_off_only(
            self.repo, self.commit_a, self.commit_b, "ree_core/gated.txt",
            {"use_foo"}, {"use_foo": False})
        self.assertIsNone(verdict)

    def test_recorded_config_succeeds_where_the_proxy_has_nothing_to_read(self):
        # This fixture has no experiments/<type>.py driver at all, so
        # flag_status_from_driver_source(None, ...) can only ever return {} (Unknown).
        # A manifest that instead RECORDED enabled_default_off_flags (P1c) resolves the
        # gate with certainty regardless -- proving the two are genuinely independent
        # flag_status sources feeding the SAME downstream file_is_default_off_only.
        proxy_status = MOD.flag_status_from_driver_source(None, {"use_foo"})
        self.assertEqual(proxy_status, {})  # the proxy has nothing to work with here

        manifest = {"enabled_default_off_flags": {}}  # recorded: measured, nothing enabled
        recorded_status = MOD.flag_status_from_recorded_config(manifest, {"use_foo"})
        self.assertEqual(recorded_status, {"use_foo": False})

        verdict = MOD.file_is_default_off_only(
            self.repo, self.commit_a, self.commit_b, "ree_core/gated.py",
            {"use_foo"}, recorded_status)
        self.assertTrue(verdict)


class DisplayPathTests(unittest.TestCase):
    def test_relative_to_umbrella_root(self):
        p = REPO_ROOT / "evidence" / "experiments" / "foo.json"
        shown = MOD._display_path(p)
        self.assertFalse(shown.startswith("/"))
        self.assertIn("REE_assembly", shown)

    def test_falls_back_to_absolute_outside_umbrella(self):
        p = Path("/tmp/totally/unrelated/path.json")
        self.assertEqual(MOD._display_path(p), str(p))


@unittest.skipUnless(REAL_ARM_FINGERPRINT.exists(), "real ree-v3 checkout not present")
class EndToEndDetectionTests(unittest.TestCase):
    """Real git repos in a tempdir; copies the REAL arm_fingerprint.py so the hash comparison
    exercises the actual function this script depends on, not a stand-in."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.bare = self.root / "origin.git"
        self.clone = self.root / "ree-v3-clone"
        self.exp_dir = self.root / "evidence_experiments"
        self.exp_dir.mkdir()

        _run(["git", "init", "--bare", "-b", "main", str(self.bare)])

        seed = self.root / "seed"
        seed.mkdir()
        _git(seed, "init", "-b", "main")
        _git(seed, "config", "user.email", "test@example.com")
        _git(seed, "config", "user.name", "Test")

        (seed / "experiments" / "_lib").mkdir(parents=True)
        (seed / "ree_core").mkdir()
        shutil.copy(REAL_ARM_FINGERPRINT, seed / "experiments" / "_lib" / "arm_fingerprint.py")
        (seed / "ree_core" / "foo.py").write_text("VALUE = 1\n")
        (seed / "ree_core" / "bar.py").write_text("UNCHANGED = 1\n")  # never touched between A/B
        _git(seed, "add", "-A")
        _git(seed, "commit", "-m", "commit A -- initial substrate")
        commit_a = _git(seed, "rev-parse", "HEAD").strip()

        (seed / "ree_core" / "foo.py").write_text("VALUE = 2\n")
        _git(seed, "add", "-A")
        _git(seed, "commit", "-m", "commit B -- substrate changed")
        commit_b = _git(seed, "rev-parse", "HEAD").strip()

        _git(seed, "remote", "add", "origin", str(self.bare))
        _git(seed, "push", "origin", "main")

        _run(["git", "clone", str(self.bare), str(self.clone)])

        # Compute the REAL hash at each commit via a throwaway worktree per commit,
        # using the actual compute_substrate_hash -- never reimplemented here either.
        self.hash_a = self._real_hash_at(seed, commit_a)
        self.hash_b = self._real_hash_at(seed, commit_b)
        self.assertNotEqual(self.hash_a, self.hash_b, "fixture commits must differ in substrate")

        self.commit_a = commit_a
        self.commit_b = commit_b

        def manifest(name, **fields):
            (self.exp_dir / f"{name}.json").write_text(json.dumps(fields))

        manifest("current_run", claim_ids=["TEST-CURRENT"], run_id="current_run",
                  substrate_hash=self.hash_b, substrate_commit={"commit": commit_b})
        manifest("stale_run", claim_ids=["TEST-STALE"], run_id="stale_run",
                  substrate_hash=self.hash_a, substrate_commit={"commit": commit_a})
        manifest("actioned_run", claim_ids=["TEST-ACTIONED"], run_id="actioned_run",
                  substrate_hash=self.hash_a, substrate_commit={"commit": commit_a},
                  pending_retest_after_substrate=True)
        manifest("no_identity_run", claim_ids=["TEST-NOID"], run_id="no_identity_run")

        # Phase-1 scope-filter fixtures: same stale hash/commit, two claims tagged on one
        # manifest -- one whose declared scope covers the file that actually changed
        # (ree_core/foo.py), one whose scope covers only the untouched ree_core/bar.py.
        manifest("scoped_run", claim_ids=["TEST-IN-SCOPE", "TEST-OUT-OF-SCOPE"],
                  run_id="scoped_run", substrate_hash=self.hash_a,
                  substrate_commit={"commit": commit_a})

        self.claims_yaml = self.root / "claims.yaml"
        self.claims_yaml.write_text(
            "claims:\n"
            "  - id: TEST-IN-SCOPE\n"
            "    substrate_scope:\n"
            "      - ree_core/foo.py\n"
            "  - id: TEST-OUT-OF-SCOPE\n"
            "    substrate_scope:\n"
            "      - ree_core/bar.py\n"
        )

    def _real_hash_at(self, seed_repo, commit):
        with tempfile.TemporaryDirectory() as wtdir:
            wt = Path(wtdir) / "wt"
            _git(seed_repo, "worktree", "add", "--detach", str(wt), commit)
            try:
                spec = importlib.util.spec_from_file_location(
                    "arm_fp_fixture", wt / "experiments" / "_lib" / "arm_fingerprint.py")
                m = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(m)
                return m.compute_substrate_hash(repo_root=wt)["substrate_hash"]
            finally:
                _git(seed_repo, "worktree", "remove", "--force", str(wt))

    def tearDown(self):
        self._tmp.cleanup()

    def test_end_to_end_buckets(self):
        buf = io.StringIO()
        argv = [
            "check_substrate_staleness_candidates.py",
            "--exp-dir", str(self.exp_dir),
            "--ree-v3-root", str(self.clone),
            "--ref", "origin/main",
            "--claims-yaml", str(self.claims_yaml),
        ]
        old_argv = sys.argv
        sys.argv = argv
        try:
            with contextlib.redirect_stdout(buf):
                rc = MOD.main()
        finally:
            sys.argv = old_argv
        self.assertEqual(rc, 0)
        out = buf.getvalue()

        self.assertIn("1  current (matches origin/main)", out)
        self.assertIn("1  already actioned", out)
        self.assertIn("1  no substrate identity recorded", out)
        self.assertIn("2  drift candidate manifest(s)", out)  # stale_run + scoped_run
        self.assertIn("TEST-STALE", out)
        self.assertNotIn("TEST-CURRENT (", out)
        self.assertNotIn("TEST-ACTIONED (", out)
        self.assertIn("stale_run", out)
        self.assertIn("ree_core/foo.py", out)  # named in the changed-files diff

        # Phase 1: the claim whose declared scope covers the changed file stays a candidate...
        self.assertIn("TEST-IN-SCOPE (1 run(s)) -- substrate_scope declared", out)
        # ...the claim whose scope covers only the untouched file is filtered out of it. Split
        # on the SECTION HEADER specifically ("filtered OUTSIDE declared..."), not the summary
        # count line above it ("... filtered OUTSIDE A declared..." -- note the "a"), which also
        # contains the word sequence "filtered OUTSIDE" and would otherwise split too early.
        self.assertIn("filtered OUTSIDE declared substrate_scope", out)
        before, _, after = out.partition("filtered OUTSIDE declared substrate_scope")
        self.assertNotIn("TEST-OUT-OF-SCOPE (", before)
        self.assertIn("TEST-OUT-OF-SCOPE (1 run(s)", after)

        # No leftover worktree from the run under test.
        listing = _git(self.clone, "worktree", "list")
        self.assertEqual(listing.count("\n"), 1, listing)


if __name__ == "__main__":
    unittest.main()
