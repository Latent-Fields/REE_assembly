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

    def test_getattr_pattern_recognized_disabled(self):
        # The DOMINANT gate idiom in ree_core (622 occurrences measured 2026-08-03),
        # not an edge case -- e.g. ree_core/goal.py:990
        # `if not getattr(self.config, "use_hierarchical_goal_credit", False): return {}`.
        node = _test_expr('getattr(self.config, "use_foo", False)')
        self.assertFalse(MOD._eval_flag_formula(node, self.KNOBS, {"use_foo": False}))

    def test_getattr_pattern_recognized_enabled(self):
        node = _test_expr('getattr(self.config, "use_foo", False)')
        self.assertTrue(MOD._eval_flag_formula(node, self.KNOBS, {"use_foo": True}))

    def test_getattr_pattern_unresolved_flag_is_unknown(self):
        node = _test_expr('getattr(self.config, "use_foo", False)')
        self.assertIsNone(MOD._eval_flag_formula(node, self.KNOBS, {}))

    def test_getattr_unrelated_name_arg_is_unknown(self):
        node = _test_expr('getattr(self.config, "not_a_knob", False)')
        self.assertIsNone(MOD._eval_flag_formula(node, self.KNOBS, {"use_foo": False}))

    def test_getattr_non_constant_name_arg_is_unknown(self):
        # getattr(obj, some_variable, default) -- the name isn't statically known at all.
        node = _test_expr("getattr(self.config, name_var, False)")
        self.assertIsNone(MOD._eval_flag_formula(node, self.KNOBS, {"use_foo": False}))

    def test_getattr_in_not_and_real_guard_clause_shape(self):
        # The EXACT real shape: `if not getattr(self.config, "use_foo", False):` -- this is
        # the condition of an early-return guard clause (handled by inert_line_ranges
        # elsewhere; here just confirming the formula itself evaluates right).
        node = _test_expr('not getattr(self.config, "use_foo", False)')
        self.assertTrue(MOD._eval_flag_formula(node, self.KNOBS, {"use_foo": False}))

    def test_other_call_is_still_unknown(self):
        # Only getattr is special-cased -- an arbitrary call remains a disqualifying Unknown.
        node = _test_expr("some_function(self.config)")
        self.assertIsNone(MOD._eval_flag_formula(node, self.KNOBS, {"use_foo": False}))


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


class CallTargetNameTests(unittest.TestCase):
    def test_attribute_call(self):
        call = _test_expr("self.goal_state.credit_subgoal_attainment(rep, credit=1.0)")
        self.assertEqual(MOD._call_target_name(call), "credit_subgoal_attainment")

    def test_bare_name_call(self):
        call = _test_expr("some_function(x)")
        self.assertEqual(MOD._call_target_name(call), "some_function")

    def test_subscript_call_is_unresolvable(self):
        call = _test_expr("handlers[key](x)")
        self.assertIsNone(MOD._call_target_name(call))


class HasDisqualifyingSideEffectTests(unittest.TestCase):
    def _func(self, src):
        tree = ast.parse(src)
        return tree.body[0]

    def test_local_assignment_only_is_fine(self):
        f = self._func("def f(self, x):\n    rep = x\n    return rep\n")
        self.assertFalse(MOD._has_disqualifying_side_effect(f))

    def test_self_attribute_assignment_disqualifies(self):
        f = self._func("def f(self, x):\n    self.x = x\n    return self.x\n")
        self.assertTrue(MOD._has_disqualifying_side_effect(f))

    def test_subscript_assignment_disqualifies(self):
        f = self._func("def f(self, d, k, v):\n    d[k] = v\n")
        self.assertTrue(MOD._has_disqualifying_side_effect(f))

    def test_augmented_attribute_assignment_disqualifies(self):
        f = self._func("def f(self):\n    self.count += 1\n")
        self.assertTrue(MOD._has_disqualifying_side_effect(f))

    def test_nested_function_own_effects_do_not_count(self):
        # A nested function's own body is its own business -- it is not executed just by
        # being defined, so it must not disqualify the OUTER function.
        f = self._func("def f(self):\n    def inner():\n        self.x = 1\n    return 0\n")
        self.assertFalse(MOD._has_disqualifying_side_effect(f))

    def test_call_only_is_fine(self):
        f = self._func("def f(self):\n    return self.goal_state.credit(1.0)\n")
        self.assertFalse(MOD._has_disqualifying_side_effect(f))


class GuardClauseConfirmsInertTests(unittest.TestCase):
    KNOBS = {"use_foo"}

    def _func(self, src):
        tree = ast.parse(src)
        return tree.body[0]

    def test_real_shape_confirmed_inert(self):
        # The ACTUAL credit_subgoal_attainment shape (ree_core/goal.py:990).
        f = self._func(
            'def credit(self, rep, credit=1.0):\n'
            '    """docstring."""\n'
            '    if not getattr(self.config, "use_foo", False):\n'
            '        return {}\n'
            '    return {"applied": True}\n'
        )
        self.assertTrue(MOD._guard_clause_confirms_inert(f, self.KNOBS, {"use_foo": False}))

    def test_flag_enabled_not_confirmed_inert(self):
        f = self._func(
            'def credit(self):\n'
            '    if not getattr(self.config, "use_foo", False):\n'
            '        return {}\n'
            '    return {"applied": True}\n'
        )
        self.assertFalse(MOD._guard_clause_confirms_inert(f, self.KNOBS, {"use_foo": True}))

    def test_flag_unknown_not_confirmed_inert(self):
        f = self._func(
            'def credit(self):\n'
            '    if not getattr(self.config, "use_foo", False):\n'
            '        return {}\n'
            '    return {"applied": True}\n'
        )
        self.assertFalse(MOD._guard_clause_confirms_inert(f, self.KNOBS, {}))

    def test_no_leading_if_is_not_inert(self):
        f = self._func("def f(self):\n    x = 1\n    return x\n")
        self.assertFalse(MOD._guard_clause_confirms_inert(f, self.KNOBS, {"use_foo": False}))

    def test_guard_with_else_is_not_inert(self):
        # An else-branch means the function does not ALWAYS return at the guard.
        f = self._func(
            'def f(self):\n'
            '    if not getattr(self.config, "use_foo", False):\n'
            '        return {}\n'
            '    else:\n'
            '        return {"x": 1}\n'
        )
        self.assertFalse(MOD._guard_clause_confirms_inert(f, self.KNOBS, {"use_foo": False}))

    def test_guard_body_with_more_than_return_is_not_inert(self):
        f = self._func(
            'def f(self):\n'
            '    if not getattr(self.config, "use_foo", False):\n'
            '        x = 1\n'
            '        return {}\n'
        )
        self.assertFalse(MOD._guard_clause_confirms_inert(f, self.KNOBS, {"use_foo": False}))

    def test_return_value_with_a_call_is_not_provably_cheap(self):
        f = self._func(
            'def f(self):\n'
            '    if not getattr(self.config, "use_foo", False):\n'
            '        return compute_default()\n'
        )
        self.assertFalse(MOD._guard_clause_confirms_inert(f, self.KNOBS, {"use_foo": False}))


class FunctionIsOneHopInertTests(unittest.TestCase):
    KNOBS = {"use_foo"}

    def _index_from(self, src):
        tree = ast.parse(src)
        index = {}
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                index.setdefault(node.name, []).append(node)
        return index

    def test_real_shape_one_hop_inert(self):
        # notify_subgoal_attainment (caller) + credit_subgoal_attainment (callee), the
        # ACTUAL real-world case P1d exists for.
        caller_src = (
            'def notify(self, transition_type, rep=None, credit=1.0):\n'
            '    if self.goal_state is None:\n'
            '        return {}\n'
            '    if transition_type not in ("waypoint", "sequence_complete"):\n'
            '        return {}\n'
            '    if rep is None:\n'
            '        if self._current_latent is None:\n'
            '            return {}\n'
            '        rep = self._current_latent.z_world\n'
            '    return self.goal_state.credit_subgoal_attainment(rep, credit=credit)\n'
        )
        callee_src = (
            'def credit_subgoal_attainment(self, rep, credit=1.0):\n'
            '    if not getattr(self.config, "use_foo", False):\n'
            '        return {}\n'
            '    return {"applied": True}\n'
        )
        caller = ast.parse(caller_src).body[0]
        index = self._index_from(callee_src)
        self.assertTrue(MOD._function_is_one_hop_inert(caller, index, self.KNOBS, {"use_foo": False}))

    def test_disqualifying_side_effect_blocks_it(self):
        src = (
            'def notify(self, rep):\n'
            '    self.last_rep = rep\n'
            '    return self.goal_state.credit_subgoal_attainment(rep)\n'
        )
        callee_src = (
            'def credit_subgoal_attainment(self, rep):\n'
            '    if not getattr(self.config, "use_foo", False):\n'
            '        return {}\n'
        )
        caller = ast.parse(src).body[0]
        index = self._index_from(callee_src)
        self.assertFalse(MOD._function_is_one_hop_inert(caller, index, self.KNOBS, {"use_foo": False}))

    def test_unresolved_call_blocks_it(self):
        src = 'def notify(self, rep):\n    return self.goal_state.nonexistent_method(rep)\n'
        caller = ast.parse(src).body[0]
        self.assertFalse(MOD._function_is_one_hop_inert(caller, {}, self.KNOBS, {"use_foo": False}))

    def test_ambiguous_name_requires_all_candidates_to_qualify(self):
        # Two different classes both define "step" -- one inert, one not. Conservative: the
        # call must NOT be treated as inert since we cannot tell which one is meant.
        caller_src = 'def notify(self):\n    return self.thing.step()\n'
        callee_src = (
            'class A:\n'
            '    def step(self):\n'
            '        if not getattr(self.config, "use_foo", False):\n'
            '            return {}\n'
            'class B:\n'
            '    def step(self):\n'
            '        return {"always": True}\n'
        )
        caller = ast.parse(caller_src).body[0]
        index = self._index_from(callee_src)
        self.assertEqual(len(index["step"]), 2)
        self.assertFalse(MOD._function_is_one_hop_inert(caller, index, self.KNOBS, {"use_foo": False}))

    def test_no_calls_at_all_is_not_one_hop_inert(self):
        # This extension is specifically for call-mediated inertness -- a function with no
        # calls at all isn't what it's for (Phase 1b's in-place check is the right tool then).
        src = 'def f(self):\n    return 1\n'
        caller = ast.parse(src).body[0]
        self.assertFalse(MOD._function_is_one_hop_inert(caller, {}, self.KNOBS, {"use_foo": False}))


class OneHopInertLineRangesTests(unittest.TestCase):
    def test_real_shape_end_to_end_line_range(self):
        knobs = {"use_foo"}
        caller_src = (
            'def notify(self, rep):\n'                    # line 1
            '    if self.goal_state is None:\n'            # line 2
            '        return {}\n'                          # line 3
            '    return self.goal_state.credit(rep)\n'      # line 4
        )
        index = {}
        callee_src = (
            'def credit(self, rep):\n'
            '    if not getattr(self.config, "use_foo", False):\n'
            '        return {}\n'
        )
        tree = ast.parse(callee_src)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                index.setdefault(node.name, []).append(node)
        ranges = MOD.one_hop_inert_line_ranges(caller_src, index, knobs, {"use_foo": False})
        self.assertEqual(ranges, [(1, 4)])

    def test_syntax_error_yields_empty(self):
        self.assertEqual(MOD.one_hop_inert_line_ranges("def f(:\n", {}, set(), {}), [])


class BuildFunctionIndexTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name) / "repo"
        self.repo.mkdir()
        _git(self.repo, "init", "-b", "main")
        _git(self.repo, "config", "user.email", "test@example.com")
        _git(self.repo, "config", "user.name", "Test")
        (self.repo / "ree_core").mkdir()
        (self.repo / "ree_core" / "a.py").write_text("def foo():\n    return 1\n")
        (self.repo / "ree_core" / "b.py").write_text(
            "def bar():\n    return 2\n\ndef foo():\n    return 3\n")
        (self.repo / "outside_scope.py").write_text("def foo():\n    return 99\n")
        _git(self.repo, "add", "-A")
        _git(self.repo, "commit", "-m", "seed")

    def tearDown(self):
        self._tmp.cleanup()

    def test_indexes_by_name_across_files_within_scope_only(self):
        index = MOD.build_function_index(self.repo, "main", ["ree_core/**/*.py"])
        self.assertEqual(len(index.get("foo", [])), 2)  # a.py + b.py, NOT outside_scope.py
        self.assertEqual(len(index.get("bar", [])), 1)
        self.assertNotIn("outside_scope", str(index))

    def test_unresolvable_ref_yields_empty(self):
        index = MOD.build_function_index(self.repo, "0" * 40, ["ree_core/**/*.py"])
        self.assertEqual(index, {})


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


# ---------------------------------------------------------------------------------------- #
# Phase 1e -- cached-state-check data-flow tracking, and non-executable changed lines        #
# ---------------------------------------------------------------------------------------- #


def _only_class(src: str) -> ast.ClassDef:
    """The single ClassDef in `src` -- the fixture shape every Phase 1e test below uses."""
    tree = ast.parse(src)
    classes = [n for n in tree.body if isinstance(n, ast.ClassDef)]
    assert len(classes) == 1, "fixture must declare exactly one class"
    return classes[0]


# The REAL shape from ree-v3/ree_core/agent.py (self.coalition, lines ~654-664 at the time of
# writing), reduced to its skeleton: an unconditional None init, then a build under a
# getattr() flag gate, then a cached-state check at a use site. This is the positive control
# the whole of Phase 1e exists for -- if it ever stops being classified, the extension is dead.
REAL_COALITION_SHAPE = '''
class REEAgent:
    def __init__(self, config):
        self.coalition: Optional[CoalitionController] = None
        if getattr(config, "use_coalition_controller", False):
            self.coalition = CoalitionController(
                CoalitionControllerConfig(enabled=True),
            )

    def reset(self):
        if self.coalition is not None:
            self.coalition.reset()
            self._coalition_ticks = 0
'''


class FlagGatedNoneAttributesTests(unittest.TestCase):
    """Which `self.<attr>` names are provably always None. A FALSE POSITIVE here is the
    dangerous direction -- it would mark genuinely-live changed lines inert and wrongly
    downgrade a real drift candidate -- so most of these are negative controls."""

    KNOBS = {"use_coalition_controller", "use_dacc", "use_other"}
    OFF = {"use_coalition_controller": False, "use_dacc": False, "use_other": False}

    def _proven(self, src, knobs=None, status=None):
        return MOD.flag_gated_none_attributes(
            _only_class(src), knobs if knobs is not None else self.KNOBS,
            status if status is not None else self.OFF)

    def test_real_coalition_shape_is_the_positive_control(self):
        self.assertIn("coalition", self._proven(REAL_COALITION_SHAPE))

    def test_unconditional_assignment_is_not_flag_gated(self):
        """The primary negative control: an attribute built unconditionally must NEVER be
        classified, or every `if self.x is not None:` in the file becomes a false verdict."""
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        self.thing = Thing()
'''
        self.assertNotIn("thing", self._proven(src))

    def test_gate_on_unknown_flag_is_not_claimed(self):
        """A flag absent from knob_names evaluates Unknown, so the assignment stays reachable."""
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        if getattr(config, "use_not_a_known_knob", False):
            self.thing = Thing()
'''
        self.assertNotIn("thing", self._proven(src))

    def test_gate_on_enabled_flag_is_not_claimed(self):
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        if getattr(config, "use_dacc", False):
            self.thing = Thing()
'''
        proven = self._proven(src, status={"use_dacc": True, "use_coalition_controller": False,
                                           "use_other": False})
        self.assertNotIn("thing", proven)

    def test_second_unconditional_assignment_in_another_method_disqualifies(self):
        """The gated __init__ build is inert, but a later method assigns unconditionally --
        the attribute is not always None and must not be claimed."""
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        if getattr(config, "use_dacc", False):
            self.thing = Thing()

    def late_bind(self):
        self.thing = Thing()
'''
        self.assertNotIn("thing", self._proven(src))

    def test_assignment_in_orelse_of_confirmed_false_gate_is_reachable(self):
        """`else` of a False test RUNS. Getting this arm backwards is the easiest way to
        introduce a silent false positive."""
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        if getattr(config, "use_dacc", False):
            pass
        else:
            self.thing = Thing()
'''
        self.assertNotIn("thing", self._proven(src))

    def test_assignment_in_orelse_of_confirmed_true_gate_is_unreachable(self):
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        if not getattr(config, "use_dacc", False):
            pass
        else:
            self.thing = Thing()
'''
        self.assertIn("thing", self._proven(src))

    def test_no_assignment_at_all_is_not_claimed(self):
        """An attribute only ever READ may be set from outside, or may not exist. Requiring at
        least one reachable assignment is what stops the analysis vouching for either."""
        src = '''
class A:
    def use(self):
        if self.thing is not None:
            self.thing.go()
'''
        self.assertEqual(self._proven(src), frozenset())

    def test_bare_annotation_is_neither_assignment_nor_poison(self):
        src = '''
class A:
    def __init__(self, config):
        self.thing: Optional[Thing]
        if getattr(config, "use_dacc", False):
            self.thing = Thing()
'''
        # no reachable assignment exists -> not claimed, but also not an error
        self.assertNotIn("thing", self._proven(src))

    def test_augmented_assignment_poisons(self):
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        if getattr(config, "use_dacc", False):
            self.thing = Thing()

    def bump(self):
        self.thing += 1
'''
        self.assertNotIn("thing", self._proven(src))

    def test_delete_poisons(self):
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        if getattr(config, "use_dacc", False):
            self.thing = Thing()

    def drop(self):
        del self.thing
'''
        self.assertNotIn("thing", self._proven(src))

    def test_for_loop_target_poisons(self):
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        if getattr(config, "use_dacc", False):
            self.thing = Thing()

    def loop(self, items):
        for self.thing in items:
            pass
'''
        self.assertNotIn("thing", self._proven(src))

    def test_with_target_poisons(self):
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        if getattr(config, "use_dacc", False):
            self.thing = Thing()

    def ctx(self, cm):
        with cm as self.thing:
            pass
'''
        self.assertNotIn("thing", self._proven(src))

    def test_walrus_cannot_target_an_attribute_at_all(self):
        """`(self.thing := ...)` is a SyntaxError ("cannot use assignment expressions with
        attribute"), so the NamedExpr poisoning arm is unreachable defence, not a live path.
        Pinned so nobody removes the arm believing it fires, or adds a fixture that cannot
        parse. A walrus on a local NAME is legal and must not poison anything."""
        with self.assertRaises(SyntaxError):
            ast.parse("(self.thing := Thing())")
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        if getattr(config, "use_dacc", False):
            self.thing = Thing()

    def walrus(self):
        if (local := compute()) is not None:
            return local
'''
        self.assertIn("thing", self._proven(src))

    def test_tuple_unpack_counts_as_a_non_none_assignment(self):
        """The unpacked value is unknown, so this is a reachable non-None assignment."""
        src = '''
class A:
    def __init__(self, config, pair):
        self.thing = None
        self.thing, self.other = pair
'''
        self.assertNotIn("thing", self._proven(src))

    def test_setattr_with_constant_name_poisons_only_that_attribute(self):
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        self.safe = None
        if getattr(config, "use_dacc", False):
            self.thing = Thing()
            self.safe = Thing()

    def late(self):
        setattr(self, "thing", Thing())
'''
        proven = self._proven(src)
        self.assertNotIn("thing", proven)
        self.assertIn("safe", proven)

    def test_setattr_with_dynamic_name_poisons_the_whole_class(self):
        src = '''
class A:
    def __init__(self, config, name):
        self.thing = None
        if getattr(config, "use_dacc", False):
            self.thing = Thing()
        setattr(self, name, Thing())
'''
        self.assertEqual(self._proven(src), frozenset())

    def test_nested_class_assignment_does_not_leak_into_the_outer_class(self):
        """A nested class binds its own `self`; its unconditional write must not disqualify
        the outer class's attribute of the same name."""
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        if getattr(config, "use_dacc", False):
            self.thing = Thing()

    class Inner:
        def __init__(self):
            self.thing = Thing()
'''
        self.assertIn("thing", self._proven(src))

    def test_assignment_nested_two_gates_deep_stays_unreachable(self):
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        if getattr(config, "use_dacc", False):
            if getattr(config, "use_other", False):
                self.thing = Thing()
'''
        self.assertIn("thing", self._proven(src))

    def test_outer_gate_unknown_inner_confirmed_false_still_unreachable(self):
        """Only ONE enclosing confirmed-False gate is needed, at any depth."""
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        if getattr(config, "use_not_a_known_knob", False):
            if getattr(config, "use_dacc", False):
                self.thing = Thing()
'''
        self.assertIn("thing", self._proven(src))

    def test_assignment_inside_try_body_under_a_gate_is_unreachable(self):
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        if getattr(config, "use_dacc", False):
            try:
                self.thing = Thing()
            except Exception:
                self.thing = Fallback()
'''
        self.assertIn("thing", self._proven(src))

    def test_ungated_assignment_inside_try_is_reachable(self):
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        try:
            self.thing = Thing()
        except Exception:
            pass
'''
        self.assertNotIn("thing", self._proven(src))

    def test_other_object_attribute_is_never_recorded(self):
        """`obj.thing = ...` is not `self.thing = ...` and must not be modelled as one."""
        src = '''
class A:
    def __init__(self, config, obj):
        self.thing = None
        obj.thing = Thing()
'''
        self.assertIn("thing", self._proven(src))

    def test_dotted_self_attribute_is_not_recorded(self):
        """`self.a.b = ...` writes through `self.a`; it is not an assignment to a self attr."""
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        self.thing.inner = Thing()
'''
        self.assertIn("thing", self._proven(src))


class EvalFlagFormulaNoneAttrsTests(unittest.TestCase):
    """The `none_attrs` arm of the Kleene evaluator."""

    KNOBS = {"use_foo"}
    NONE_ATTRS = frozenset({"coalition"})

    def _ev(self, src, none_attrs=None):
        return MOD._eval_flag_formula(
            _test_expr(src), self.KNOBS, {"use_foo": False},
            self.NONE_ATTRS if none_attrs is None else none_attrs)

    def test_is_not_none_on_proven_attr_is_false(self):
        self.assertIs(self._ev("self.coalition is not None"), False)

    def test_is_none_on_proven_attr_is_true(self):
        self.assertIs(self._ev("self.coalition is None"), True)

    def test_bare_truthiness_on_proven_attr_is_false(self):
        self.assertIs(self._ev("self.coalition"), False)

    def test_negation_inverts(self):
        self.assertIs(self._ev("not (self.coalition is not None)"), True)

    def test_and_with_unknown_still_resolves_false(self):
        self.assertIs(self._ev("self.coalition is not None and whatever(x)"), False)

    def test_or_with_unknown_is_unknown(self):
        self.assertIsNone(self._ev("self.coalition is not None or whatever(x)"))

    def test_empty_none_attrs_keeps_pre_phase1e_behaviour(self):
        """Back-compat control: every pre-1e caller passes no none_attrs and must be
        bit-identical -- a cached-state check stays Unknown, exactly as before."""
        self.assertIsNone(self._ev("self.coalition is not None", frozenset()))

    def test_unproven_attribute_is_unknown(self):
        self.assertIsNone(self._ev("self.salience is not None"))

    def test_other_object_attribute_is_unknown(self):
        """`other.coalition` is a different object -- the proof is about `self`."""
        self.assertIsNone(self._ev("other.coalition is not None"))

    def test_equality_comparison_is_not_treated_as_identity(self):
        """`== None` can be overloaded by __eq__; only `is`/`is not` are decidable here."""
        self.assertIsNone(self._ev("self.coalition == None"))

    def test_comparison_against_non_none_is_unknown(self):
        self.assertIsNone(self._ev("self.coalition is not sentinel"))

    def test_chained_comparison_is_unknown(self):
        self.assertIsNone(self._ev("self.coalition is not None is not False"))


class InertLineRangesPhase1eTests(unittest.TestCase):
    """inert_line_ranges end-to-end with the cached-state rule, including its class scoping
    and the externally_assigned kill-switch."""

    KNOBS = {"use_coalition_controller"}
    OFF = {"use_coalition_controller": False}

    def _covered(self, src, externally_assigned=frozenset()):
        ranges = MOD.inert_line_ranges(src, self.KNOBS, self.OFF, externally_assigned)
        return {n for lo, hi in ranges for n in range(lo, hi + 1)}

    def test_cached_state_check_body_becomes_inert(self):
        covered = self._covered(REAL_COALITION_SHAPE)
        lines = REAL_COALITION_SHAPE.splitlines()
        reset_body = [i + 1 for i, ln in enumerate(lines) if "self.coalition.reset()" in ln]
        self.assertTrue(reset_body)
        for lineno in reset_body:
            self.assertIn(lineno, covered)

    def test_disabled_when_externally_assigned_is_none(self):
        """None means "driver unresolvable" -- the whole cached-state rule is off, and the
        result must match pre-1e behaviour exactly."""
        with_rule = self._covered(REAL_COALITION_SHAPE, frozenset())
        without = self._covered(REAL_COALITION_SHAPE, None)
        legacy = MOD.inert_line_ranges(REAL_COALITION_SHAPE, self.KNOBS, self.OFF)
        self.assertEqual({n for lo, hi in legacy for n in range(lo, hi + 1)}, without)
        self.assertNotEqual(with_rule, without)

    def test_attribute_the_driver_assigns_is_excluded(self):
        covered = self._covered(REAL_COALITION_SHAPE, {"coalition"})
        lines = REAL_COALITION_SHAPE.splitlines()
        reset_body = [i + 1 for i, ln in enumerate(lines) if "self.coalition.reset()" in ln]
        for lineno in reset_body:
            self.assertNotIn(lineno, covered)

    def test_class_scoping_no_leak_between_two_classes(self):
        """B builds `thing` unconditionally. A's proof must not apply inside B, or B's live
        code would be marked inert."""
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        if getattr(config, "use_coalition_controller", False):
            self.thing = Thing()

    def use_a(self):
        if self.thing is not None:
            a_only_line()


class B:
    def __init__(self, config):
        self.thing = Thing()

    def use_b(self):
        if self.thing is not None:
            b_only_line()
'''
        covered = self._covered(src)
        lines = src.splitlines()
        a_line = next(i + 1 for i, ln in enumerate(lines) if "a_only_line()" in ln)
        b_line = next(i + 1 for i, ln in enumerate(lines) if "b_only_line()" in ln)
        self.assertIn(a_line, covered)
        self.assertNotIn(b_line, covered)

    def test_orelse_of_a_cached_state_check_is_not_inert(self):
        """`if self.thing is not None: ... else: ...` -- the ELSE branch is what actually runs."""
        src = '''
class A:
    def __init__(self, config):
        self.thing = None
        if getattr(config, "use_coalition_controller", False):
            self.thing = Thing()

    def use(self):
        if self.thing is not None:
            dead_line()
        else:
            live_line()
'''
        covered = self._covered(src)
        lines = src.splitlines()
        dead = next(i + 1 for i, ln in enumerate(lines) if "dead_line()" in ln)
        live = next(i + 1 for i, ln in enumerate(lines) if "live_line()" in ln)
        self.assertIn(dead, covered)
        self.assertNotIn(live, covered)

    def test_syntax_error_yields_no_ranges(self):
        self.assertEqual(MOD.inert_line_ranges("def (:", self.KNOBS, self.OFF, frozenset()), [])


class DriverAssignedAttributesTests(unittest.TestCase):
    """The external-mutation kill-switch. Returning None (= disable the rule) is the safe
    answer whenever the driver cannot be read precisely."""

    def test_plain_attribute_assignment_is_reported(self):
        self.assertEqual(MOD.driver_assigned_attributes("agent.dacc = Thing()"), {"dacc"})

    def test_self_assignment_is_not_reported(self):
        """A driver's own class writing its own state says nothing about the agent."""
        self.assertEqual(
            MOD.driver_assigned_attributes("class D:\n    def f(self):\n        self.dacc = 1\n"),
            set())

    def test_augmented_delete_for_and_unpack_targets_are_reported(self):
        """Every write shape that is not a plain `=`. (A walrus cannot target an attribute --
        see FlagGatedNoneAttributesTests.test_walrus_cannot_target_an_attribute_at_all.)"""
        src = (
            "agent.a += 1\n"
            "del agent.b\n"
            "for agent.c in items:\n    pass\n"
            "agent.e, agent.f = pair\n"
        )
        self.assertEqual(MOD.driver_assigned_attributes(src), {"a", "b", "c", "e", "f"})

    def test_annotated_assignment_is_reported(self):
        self.assertEqual(MOD.driver_assigned_attributes("agent.dacc: Thing = Thing()"), {"dacc"})

    def test_setattr_with_constant_name_is_reported(self):
        self.assertEqual(
            MOD.driver_assigned_attributes('setattr(agent, "dacc", Thing())'), {"dacc"})

    def test_setattr_with_dynamic_name_disables_the_rule(self):
        self.assertIsNone(MOD.driver_assigned_attributes("setattr(agent, name, Thing())"))

    def test_unparseable_driver_disables_the_rule(self):
        self.assertIsNone(MOD.driver_assigned_attributes("def (:"))

    def test_absent_driver_disables_the_rule(self):
        self.assertIsNone(MOD.driver_assigned_attributes(None))
        self.assertIsNone(MOD.driver_assigned_attributes(""))

    def test_read_only_driver_reports_nothing(self):
        self.assertEqual(
            MOD.driver_assigned_attributes("x = agent.dacc\nif agent.dacc is not None:\n    pass\n"),
            set())


class NonExecutableLineNumbersTests(unittest.TestCase):
    """Phase 1e(b). Uses tokenize precisely so that a `#` in a string is not a comment."""

    def test_comment_and_blank_lines_are_non_executable(self):
        src = "x = 1\n# a comment\n\ny = 2\n"
        self.assertEqual(MOD.non_executable_line_numbers(src), {2, 3})

    def test_trailing_comment_on_a_code_line_is_executable(self):
        src = "x = 1  # trailing\n"
        self.assertEqual(MOD.non_executable_line_numbers(src), set())

    def test_hash_inside_a_string_is_not_a_comment(self):
        src = 'x = 1\ny = "# not a comment"\n'
        self.assertEqual(MOD.non_executable_line_numbers(src), set())

    def test_blank_line_inside_a_triple_quoted_string_is_executable(self):
        src = 'x = """line one\n\nline three"""\n'
        self.assertEqual(MOD.non_executable_line_numbers(src), set())

    def test_docstring_counts_as_executable(self):
        """Conservative on purpose -- a STRING token is a real token."""
        src = 'def f():\n    """doc"""\n    return 1\n'
        self.assertEqual(MOD.non_executable_line_numbers(src), set())

    def test_untokenizable_source_claims_nothing(self):
        self.assertEqual(MOD.non_executable_line_numbers('x = "unterminated\n'), set())

    def test_continuation_lines_are_executable(self):
        src = "x = (\n    1,\n)\n# tail\n"
        self.assertEqual(MOD.non_executable_line_numbers(src), {4})


class FileIsDefaultOffOnlyPhase1eTests(unittest.TestCase):
    """The two Phase 1e(b) verdicts that need a REAL git diff: a comment-only change is
    provably inert, and the same change beside a pure deletion is NOT."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name) / "ree-v3"
        self.repo.mkdir()
        _git(self.repo, "init", "-q", "-b", "main")
        _git(self.repo, "config", "user.email", "t@t")
        _git(self.repo, "config", "user.name", "t")

    def tearDown(self):
        self._tmp.cleanup()

    def _commit(self, body, message):
        (self.repo / "mod.py").write_text(body)
        _git(self.repo, "add", "mod.py")
        _git(self.repo, "commit", "-q", "-m", message)
        return _git(self.repo, "rev-parse", "HEAD").strip()

    def test_comment_only_change_is_provably_inert(self):
        base = self._commit("def f():\n    return 1\n", "base")
        self._commit("def f():\n    # explain\n    return 1\n", "comment")
        verdict = MOD.file_is_default_off_only(
            self.repo, base, "HEAD", "mod.py", {"use_foo"}, {"use_foo": False},
            None, frozenset())
        self.assertIs(verdict, True)

    def test_code_replaced_by_a_comment_is_not_claimed(self):
        """The only post-image line is a comment, but the line it replaced was a real call.
        A post-image-only test reads this as a comment-only change; checking the REMOVED line
        against the OLD file is what catches it."""
        base = self._commit("def f():\n    side_effect()\n    return 1\n", "base")
        self._commit("def f():\n    # explain\n    return 1\n", "comment+delete")
        verdict = MOD.file_is_default_off_only(
            self.repo, base, "HEAD", "mod.py", {"use_foo"}, {"use_foo": False},
            None, frozenset())
        self.assertIsNot(verdict, True)

    def test_comment_only_change_beside_a_pure_code_deletion_is_not_claimed(self):
        """Same hazard via a separate pure-deletion hunk rather than an in-place replacement."""
        base = self._commit(
            "def f():\n    return 1\n\n\ndef g():\n    side_effect()\n    return 2\n", "base")
        self._commit(
            "def f():\n    # explain\n    return 1\n\n\ndef g():\n    return 2\n", "comment+del")
        verdict = MOD.file_is_default_off_only(
            self.repo, base, "HEAD", "mod.py", {"use_foo"}, {"use_foo": False},
            None, frozenset())
        self.assertIsNot(verdict, True)

    def test_comment_rewritten_in_place_is_still_provably_inert(self):
        """The negative control for the deletion guard: a comment REPLACING a comment removes
        a line too, and must not be swept up as a code deletion."""
        base = self._commit("def f():\n    # old wording\n    return 1\n", "base")
        self._commit("def f():\n    # new wording\n    return 1\n", "reword")
        verdict = MOD.file_is_default_off_only(
            self.repo, base, "HEAD", "mod.py", {"use_foo"}, {"use_foo": False},
            None, frozenset())
        self.assertIs(verdict, True)

    def test_live_code_change_is_still_reported(self):
        base = self._commit("def f():\n    return 1\n", "base")
        self._commit("def f():\n    return 2\n", "live")
        verdict = MOD.file_is_default_off_only(
            self.repo, base, "HEAD", "mod.py", {"use_foo"}, {"use_foo": False},
            None, frozenset())
        self.assertIs(verdict, False)


if __name__ == "__main__":
    unittest.main()
