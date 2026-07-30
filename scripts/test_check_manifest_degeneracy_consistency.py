#!/usr/bin/env python3
"""Tests for scripts/check_manifest_degeneracy_consistency.py.

Time-independent (no wall-clock reads anywhere; every corpus fixture is pinned to
a git SHA rather than to the live working tree) and filesystem-isolated (every
manifest is written to a tempdir and passed in by path).

THE MUTATION CHECK IS THE POINT. A consistency checker that never fires is
indistinguishable from one that is broken, so the incident's PRE-FIX manifest --
fetched verbatim from `eabe9c453b^` -- is the positive control, and the same file
at `eabe9c453b` is the negative control. If a refactor makes the checker vacuous,
TestIncidentReplay fails; the synthetic tests alone would not catch that.

Pinning the corpus fixtures to SHAs rather than reading evidence/experiments/ is
deliberate twice over: it keeps the suite time-independent, and it stops a future
edit to those manifests from silently flipping a regression test into agreement.
One live-tree test (TestLiveCorpus) checks the trio as it stands TODAY, and skips
rather than fails when the files are absent.

Run:
    /opt/local/bin/python3 scripts/test_check_manifest_degeneracy_consistency.py
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_manifest_degeneracy_consistency as mod  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]

# The incident. eabe9c453b is the fix; its parent is the defective state.
FIX_SHA = "eabe9c453b"
PRE_SHA = "eabe9c453b^"
EXPERIMENT_TYPE = "v3_exq_673_mech171_vicious_cycle_sleep_disruption"

# The three RECOVERED runs that carried the false "their arms differ" assertion.
CORRECTED_TRIO = [
    f"{EXPERIMENT_TYPE}_20260611T224744Z_v3",
    f"{EXPERIMENT_TYPE}_20260612T010234Z_v3",
    f"{EXPERIMENT_TYPE}_20260612T033246Z_v3",
]

# The three ORIGINALLY-COMMITTED siblings, which always set non_degenerate:false,
# plus the 7th run admitted 2026-07-30. None of these ever carried the defect.
CLEAN_SIBLINGS = [
    f"{EXPERIMENT_TYPE}_20260611T230231Z_v3",
    f"{EXPERIMENT_TYPE}_20260612T032233Z_v3",
    f"{EXPERIMENT_TYPE}_20260612T044809Z_v3",
    f"{EXPERIMENT_TYPE}_20260612T005615Z_v3",
]


def flat_path(run_id: str) -> str:
    return f"evidence/experiments/{run_id}.json"


def pack_path(run_id: str) -> str:
    return f"evidence/experiments/{EXPERIMENT_TYPE}/runs/{run_id}/manifest.json"


def git_show(sha: str, path: str) -> dict | None:
    """Fetch a manifest at a pinned revision, or None when git cannot serve it."""
    try:
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "show", f"{sha}:{path}"],
            capture_output=True, check=False)
    except OSError:
        return None
    if out.returncode != 0:
        return None
    try:
        return json.loads(out.stdout.decode("utf-8"))
    except ValueError:
        return None


class Harness(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        self._n = 0

    def write(self, manifest: dict, name: str | None = None) -> Path:
        self._n += 1
        path = self.tmp / (name or f"m{self._n}.json")
        path.write_text(json.dumps(manifest), encoding="utf-8")
        return path

    def check(self, flat: dict | None = None, pack: dict | None = None,
              run_id: str = "run_x", **kw) -> dict:
        forms = {}
        if flat is not None:
            forms["flat"] = (self.write(flat, "flat.json"), flat)
        if pack is not None:
            forms["pack"] = (self.write(pack, "pack.json"), pack)
        return mod.check_run(run_id, forms, **kw)

    def kinds(self, res: dict) -> list[str]:
        return sorted(f["kind"] for f in res["findings"])

    def assertClean(self, res: dict, msg: str = ""):
        self.assertEqual(res["findings"], [],
                         f"{msg} unexpected findings: {res['findings']}")

    def assertFlagged(self, res: dict, kind: str, msg: str = ""):
        self.assertIn(kind, self.kinds(res),
                      f"{msg} expected {kind}, got {self.kinds(res)} / notes {res['notes']}")


# --- fixture builders --------------------------------------------------------

def shape_a(values: dict[str, list[float]], seeds=(42, 49, 56), **extra) -> dict:
    """Shape A: `per_seed_comparisons` with arm_<id>_<metric> keys.

    `values` maps metric -> [arm_a, arm_b, arm_c] value for EVERY seed.
    """
    rows = []
    for seed in seeds:
        row: dict = {"seed": seed}
        for metric, per_arm in values.items():
            for arm, value in zip("abc", per_arm):
                row[f"arm_{arm}_{metric}"] = value
        rows.append(row)
    return {"run_id": "run_x", "per_seed_comparisons": rows, **extra}


def shape_b(arms: dict[str, dict[str, list]], seeds=(42, 49, 56), **extra) -> dict:
    """Shape B: `all_results` mapping arm label -> per-seed row list."""
    out = {}
    for arm, metrics in arms.items():
        out[arm] = [dict({"seed": s}, **{m: v[i] for m, v in metrics.items()})
                    for i, s in enumerate(seeds)]
    return {"run_id": "run_x", "all_results": out, **extra}


def shape_c(arms: dict[str, dict[str, list]], seeds=(42, 49, 56),
            label="arm_id", **extra) -> dict:
    """Shape C: `arm_results` as a flat row list carrying an arm-label field."""
    rows = []
    for arm, metrics in arms.items():
        for i, s in enumerate(seeds):
            rows.append(dict({label: arm, "seed": s},
                             **{m: v[i] for m, v in metrics.items()}))
    return {"run_id": "run_x", "arm_results": rows, **extra}


# --- (a) degenerate but unflagged --------------------------------------------

class TestDegenerateUnflagged(Harness):
    def test_shape_a_all_arms_identical_is_flagged(self):
        """POSITIVE CONTROL: the incident's own shape and signature."""
        res = self.check(shape_a({
            "slot_diversity": [0.8678829669952393] * 3,
            "eval_harm": [0.06460066178039198] * 3,
            "late_pred_loss": [0.0] * 3,
        }))
        self.assertFlagged(res, "degenerate_unflagged")

    def test_shape_b_all_arms_identical_is_flagged(self):
        res = self.check(shape_b({
            "ARM_A_HEALTHY": {"slot_diversity": [0.5, 0.6, 0.7], "harm": [0.1, 0.2, 0.3]},
            "ARM_B_EARLY": {"slot_diversity": [0.5, 0.6, 0.7], "harm": [0.1, 0.2, 0.3]},
            "ARM_C_LATE": {"slot_diversity": [0.5, 0.6, 0.7], "harm": [0.1, 0.2, 0.3]},
        }))
        self.assertFlagged(res, "degenerate_unflagged")

    def test_shape_c_all_arms_identical_is_flagged(self):
        res = self.check(shape_c({
            "A0_MAP_NAV": {"harm_per_step": [0.1, 0.2, 0.3], "reward": [1.0, 2.0, 3.0]},
            "A1_MAP_ABLATED": {"harm_per_step": [0.1, 0.2, 0.3], "reward": [1.0, 2.0, 3.0]},
        }))
        self.assertFlagged(res, "degenerate_unflagged")

    def test_arm_label_spelled_arm_not_arm_id(self):
        """Arm-label field discovery must not depend on one spelling."""
        res = self.check(shape_c({
            "ON": {"rv": [0.1, 0.2, 0.3]}, "OFF": {"rv": [0.1, 0.2, 0.3]},
        }, label="arm"))
        self.assertFlagged(res, "degenerate_unflagged")

    def test_arm_label_spelled_condition(self):
        res = self.check(shape_c({
            "HEAD_ON": {"crps": [0.1, 0.2, 0.3]}, "HEAD_OFF": {"crps": [0.1, 0.2, 0.3]},
        }, label="condition"))
        self.assertFlagged(res, "degenerate_unflagged")

    def test_unknown_container_name_is_still_discovered(self):
        """Container names are read off the data, never matched against a list."""
        rows = [{"arm": a, "seed": s, "dv": 0.5}
                for a in ("X", "Y") for s in (1, 2, 3)]
        res = self.check({"run_id": "run_x", "a_container_nobody_has_seen": rows})
        self.assertFlagged(res, "degenerate_unflagged")

    def test_non_degenerate_false_suppresses(self):
        """NEGATIVE CONTROL: correctly annotated degeneracy is not a finding."""
        res = self.check(shape_a({"dv": [1.0] * 3}, non_degenerate=False,
                                 degeneracy_reason="All arms identical"))
        self.assertClean(res)

    def test_non_degenerate_per_claim_false_suppresses(self):
        res = self.check(shape_a({"dv": [1.0] * 3, "dv2": [2.0] * 3},
                                 non_degenerate_per_claim={"MECH-1": False, "MECH-2": True}))
        self.assertClean(res)

    def test_non_degenerate_true_does_not_suppress(self):
        """A `true` flag on identical arms is exactly the defect being hunted."""
        res = self.check(shape_a({"dv": [1.0] * 3, "dv2": [2.0] * 3}, non_degenerate=True))
        self.assertFlagged(res, "degenerate_unflagged")

    def test_annotation_on_the_other_copy_suppresses(self):
        """A degeneracy recorded in EITHER copy is a decision already taken."""
        data = shape_a({"dv": [1.0] * 3, "dv2": [2.0] * 3})
        res = self.check(flat=dict(data, non_degenerate=False,
                                   degeneracy_reason="All arms identical"),
                         pack=data)
        self.assertClean(res)

    def test_partial_equality_is_not_degeneracy(self):
        """One discriminating metric vetoes the finding (constraint: unambiguous)."""
        res = self.check(shape_a({"same": [1.0] * 3, "differs": [1.0, 2.0, 3.0]}))
        self.assertClean(res)

    def test_one_discriminating_container_vetoes_the_others(self):
        manifest = shape_a({"dv": [1.0] * 3})
        manifest["arm_results"] = [
            {"arm_id": "A", "seed": 42, "dv2": 1.0},
            {"arm_id": "B", "seed": 42, "dv2": 9.0},
        ]
        self.assertClean(self.check(manifest))

    def test_equality_on_a_single_comparison_is_below_the_floor(self):
        res = self.check(shape_a({"dv": [1.0] * 3}, seeds=(42,)))
        self.assertClean(res)
        self.assertTrue(any("min-comparisons" in n for n in res["notes"]), res["notes"])

    def test_dry_run_smoke_pack_is_a_note_not_a_finding(self):
        res = self.check(shape_a({"dv": [1.0] * 3, "dv2": [2.0] * 3},
                                 params={"dry_run": True}))
        self.assertClean(res)
        self.assertTrue(any("dry_run" in n for n in res["notes"]), res["notes"])

    def test_single_arm_run_is_a_note_not_a_finding(self):
        res = self.check({"run_id": "run_x",
                          "arm_results": [{"arm_id": "ONLY", "seed": s, "dv": 1.0}
                                          for s in (1, 2, 3)]})
        self.assertClean(res)
        self.assertEqual(res["n_tables"], 0)
        self.assertTrue(any("no comparable per-arm structure" in n for n in res["notes"]))

    def test_literature_style_manifest_is_a_note(self):
        res = self.check({"run_id": "lit_x", "evidence_class": "literature",
                          "outcome": "PASS", "claim_ids": ["MECH-1"]})
        self.assertClean(res)
        self.assertEqual(res["n_tables"], 0)

    def test_float_noise_is_neither_identical_nor_different(self):
        """The dead zone must produce silence in BOTH directions, not a coin flip.

        The delta has to be REPRESENTABLE to test anything: 1.0 + 1e-17 rounds
        straight back to 1.0 (float64 eps at 1.0 is ~2.2e-16), so it is bit-equal
        and exercises nothing. 1e-15 is representable and still far below the
        material threshold of 1e-9 * 1.0, which is exactly the gap being tested.
        """
        noisy = 1.0 + 1e-15
        self.assertNotEqual(noisy, 1.0, "fixture is vacuous -- delta not representable")
        res = self.check(shape_a({"dv": [1.0, noisy, 1.0], "dv2": [2.0] * 3}))
        self.assertClean(res, "(a) must not fire on a bit-unequal pair:")
        res_b = self.check(shape_a({"dv": [1.0, noisy, 1.0]}, non_degenerate=False,
                                   degeneracy_reason="All arms identical on every metric."))
        self.assertClean(res_b, "(b) must not fire on an immaterial delta:")

    def test_bool_and_int_are_not_conflated(self):
        """`True == 1` in Python; an arm type change must not read as identity."""
        res = self.check(shape_a({"gate": [True, 1, True], "dv": [2.0] * 3}))
        self.assertClean(res)

    def test_list_valued_fields_are_not_compared(self):
        """A long identical series must not dominate an otherwise thin verdict."""
        manifest = shape_a({"dv": [1.0, 2.0, 3.0]})
        for row in manifest["per_seed_comparisons"]:
            row["arm_a_trace"] = [1, 2, 3]
            row["arm_b_trace"] = [1, 2, 3]
        self.assertClean(self.check(manifest))

    def test_arm_metric_key_splits_on_the_first_token_only(self):
        res = self.check(shape_a({"late_pred_loss": [0.0] * 3, "eval_harm": [0.5] * 3}))
        self.assertFlagged(res, "degenerate_unflagged")
        table = mod.discover_arm_tables(
            shape_a({"late_pred_loss": [0.0] * 3}))[0]
        self.assertEqual(sorted(table.arm_ids), ["a", "b", "c"])
        self.assertIn("late_pred_loss", table.by_metric())


# --- (b) flagged but discriminative ------------------------------------------

class TestFlaggedButDiscriminative(Harness):
    def test_global_identity_claim_contradicted_is_flagged(self):
        """POSITIVE CONTROL for the costlier direction."""
        res = self.check(shape_a(
            {"dv": [1.0, 5.0, 9.0], "dv2": [2.0, 6.0, 10.0]},
            non_degenerate=False,
            degeneracy_reason="All arms identical (ARM_A==ARM_B==ARM_C on every metric)"))
        self.assertFlagged(res, "flagged_but_discriminative")

    def test_arm_equation_alone_is_enough_when_tokens_resolve(self):
        res = self.check(shape_b(
            {"ARM_A_HEALTHY": {"dv": [1.0, 1.0, 1.0]},
             "ARM_B_EARLY": {"dv": [5.0, 5.0, 5.0]}},
            non_degenerate=False,
            degeneracy_reason="Vacuous: ARM_A==ARM_B on the readout."))
        self.assertFlagged(res, "flagged_but_discriminative")

    def test_arm_equation_with_unresolvable_tokens_does_not_fire(self):
        """Self-validation: prose containing '==' is not an arm-identity claim."""
        res = self.check(shape_b(
            {"ARM_A_HEALTHY": {"dv": [1.0] * 3}, "ARM_B_EARLY": {"dv": [5.0] * 3}},
            non_degenerate=False,
            degeneracy_reason="Gate unmet: threshold==floor and budget==cap."))
        self.assertClean(res)

    def test_named_metric_claim_contradicted_is_flagged(self):
        res = self.check(shape_c(
            {"A": {"harm_discrimination": [1.0, 2.0, 3.0], "other": [1.0, 1.0, 1.0]},
             "B": {"harm_discrimination": [9.0, 9.0, 9.0], "other": [1.0, 1.0, 1.0]}},
            non_degenerate=False,
            degeneracy_reason="harm_discrimination byte-identical across all 4 sleep arms: "
                              "the readout is seed-fixed and arm-invariant."))
        self.assertFlagged(res, "flagged_but_discriminative")

    def test_named_metric_claim_upheld_is_clean(self):
        """The v3_exq_670 shape: the named DV IS identical; other columns differ."""
        res = self.check(shape_c(
            {"A": {"harm_discrimination": [1.0, 1.0, 1.0], "rem_enabled": [1, 1, 1]},
             "B": {"harm_discrimination": [1.0, 1.0, 1.0], "rem_enabled": [0, 0, 0]}},
            non_degenerate=False,
            degeneracy_reason="harm_discrimination byte-identical across all 4 sleep arms: "
                              "the readout is seed-fixed and arm-invariant."))
        self.assertClean(res)

    def test_non_arm_identity_reason_is_out_of_scope(self):
        """Readiness / non-vacuity / zero-spread flags are not adjudicated here."""
        for reason in (
            "readiness below floor (GAP-A pool / curiosity per-candidate range)",
            "substrate_not_ready: P0 readiness unmet: r1_grad_cosine_not_net_negative",
            "Non-vacuity gate RED in EVERY arm: arm 'A0' failed precision_manipulation_took",
            "harm_class_fraction_on: zero spread (constant=1, spread=0<=eps=1e-09)",
            "superseded predecessor (672a is the corrected run)",
        ):
            res = self.check(shape_a({"dv": [1.0, 5.0, 9.0]},
                                     non_degenerate=False, degeneracy_reason=reason),
                             run_id=f"r_{reason[:10]}")
            self.assertClean(res, f"reason {reason!r}:")

    def test_trailing_prose_about_identity_is_not_an_assertion(self):
        """The live v3_exq_805 counter-example: an unanchored 'contains' test fires."""
        reason = ("ARC-016 recalibration gate RED: Non-vacuity gate RED in EVERY arm: arm "
                  "'A0_TRAIN_BASELINE' failed precision_manipulation_took. A threshold that "
                  "never engages, or a perturbation that did not raise variance, makes every "
                  "arm identical -- exactly the state that voided EXQ-396a/b.")
        res = self.check(shape_a({"dv": [1.0, 5.0, 9.0]},
                                 non_degenerate=False, degeneracy_reason=reason))
        self.assertClean(res)

    def test_flag_without_reason_is_a_note(self):
        res = self.check(shape_a({"dv": [1.0, 5.0, 9.0]}, non_degenerate=False))
        self.assertClean(res)
        self.assertTrue(any("no degeneracy_reason" in n for n in res["notes"]), res["notes"])

    def test_named_metric_absent_from_the_data_is_a_note(self):
        res = self.check(shape_a(
            {"dv": [1.0, 5.0, 9.0]}, non_degenerate=False,
            degeneracy_reason="nowhere_metric identical across arms: the readout is fixed."))
        self.assertClean(res)
        self.assertTrue(any("nowhere_metric" in n for n in res["notes"]), res["notes"])

    def test_identity_claim_upheld_is_clean(self):
        res = self.check(shape_a({"dv": [1.0] * 3, "dv2": [2.0] * 3}, non_degenerate=False,
                                 degeneracy_reason="All arms identical on every metric."))
        self.assertClean(res)


class TestReasonClassification(unittest.TestCase):
    ARMS = ["ARM_A_HEALTHY", "ARM_B_EARLY", "ARM_C_LATE"]

    def test_the_incidents_own_reason_classifies_global(self):
        kind, metric = mod.classify_reason(
            "All arms identical (ARM_A==ARM_B==ARM_C on every metric) and late_pred_loss==0.0",
            self.ARMS)
        self.assertEqual((kind, metric), ("global", None))

    def test_named_metric_lead(self):
        kind, metric = mod.classify_reason(
            "harm_discrimination byte-identical across all 4 sleep arms: run_sleep_cycle "
            "never trains e3.harm_eval_head.", self.ARMS)
        self.assertEqual((kind, metric), ("metric", "harm_discrimination"))

    def test_global_lead_is_not_read_as_a_metric_named_All(self):
        kind, metric = mod.classify_reason("All arms identical across every readout", self.ARMS)
        self.assertEqual((kind, metric), ("global", None))

    def test_empty_and_none(self):
        for reason in ("", None, "   "):
            self.assertEqual(mod.classify_reason(reason, self.ARMS), ("other", None))

    def test_arm_token_normalisation_bridges_spellings(self):
        """'ARM_A' in prose must resolve to 'a' (shape A) and 'ARM_A_HEALTHY' (shape B)."""
        self.assertTrue(mod._arm_token_matches("ARM_A", ["a", "b", "c"]))
        self.assertTrue(mod._arm_token_matches("ARM_A", self.ARMS))
        self.assertFalse(mod._arm_token_matches("threshold", self.ARMS))


# --- flat / pack -------------------------------------------------------------

class TestFlatPack(Harness):
    def test_both_annotated_and_both_present_but_conflicting_is_a_finding(self):
        data = shape_a({"dv": [1.0, 5.0, 9.0]})
        res = self.check(
            flat=dict(data, non_degenerate=False, degeneracy_reason="readiness below floor"),
            pack=dict(data, non_degenerate=True, evidence_direction_note="scored"))
        self.assertFlagged(res, "flat_pack_disagreement")

    def test_field_absent_from_the_pack_is_overlay_lag_not_a_finding(self):
        """The systemic producer-lag shape: 241 live runs, all resolved by the overlay."""
        data = shape_a({"dv": [1.0, 5.0, 9.0]})
        res = self.check(
            flat=dict(data, non_degenerate=True, evidence_direction_note="scored"),
            pack=dict(data, evidence_direction_note="scored"))
        self.assertClean(res)
        self.assertEqual(res.get("overlay_lag"), ["non_degenerate"])

    def test_degeneracy_reason_prose_difference_is_not_direction_bearing(self):
        data = shape_a({"dv": [1.0, 5.0, 9.0]})
        res = self.check(
            flat=dict(data, non_degenerate=False, degeneracy_reason="floor unmet (reworded)"),
            pack=dict(data, non_degenerate=False, degeneracy_reason="floor unmet"))
        self.assertClean(res)

    def test_arm_data_is_read_from_whichever_copy_carries_it(self):
        """The pack is a MAPPED projection and usually drops the arm containers."""
        res = self.check(flat=shape_a({"dv": [1.0] * 3, "dv2": [2.0] * 3}),
                         pack={"run_id": "run_x", "outcome": "FAIL"})
        self.assertFlagged(res, "degenerate_unflagged")
        self.assertEqual(res["data_source"], "flat")

    def test_copies_disagreeing_on_the_arm_data_fire_nothing(self):
        res = self.check(flat=shape_a({"dv": [1.0] * 3, "dv2": [2.0] * 3}),
                         pack=shape_a({"dv": [1.0, 5.0, 9.0], "dv2": [2.0] * 3}))
        self.assertClean(res)
        self.assertTrue(any("DISAGREE" in n for n in res["notes"]), res["notes"])

    def test_effective_annotation_mirrors_the_indexer_rule(self):
        annotated = {"degeneracy_reason": "x"}
        plain: dict = {}
        self.assertIs(mod.effective_annotation(annotated, plain)[0], annotated)
        self.assertIs(mod.effective_annotation(annotated, annotated)[0], annotated)
        self.assertIs(mod.effective_annotation(plain, annotated)[0], annotated)
        self.assertIs(mod.effective_annotation(plain, plain)[0], plain)


# --- the incident, replayed from pinned git objects --------------------------

class TestIncidentReplay(unittest.TestCase):
    """The mutation check: PRE-FIX must be FLAGGED, POST-FIX must be CLEAN.

    Without this, a refactor that made the checker vacuous would pass every
    synthetic test above.
    """

    def _check(self, sha: str, run_id: str) -> dict | None:
        flat = git_show(sha, flat_path(run_id))
        if flat is None:
            return None
        forms = {"flat": (Path(flat_path(run_id)), flat)}
        pack = git_show(sha, pack_path(run_id))
        if pack is not None:
            forms["pack"] = (Path(pack_path(run_id)), pack)
        return mod.check_run(run_id, forms)

    def test_pre_fix_trio_is_flagged(self):
        seen = 0
        for run_id in CORRECTED_TRIO:
            res = self._check(PRE_SHA, run_id)
            if res is None:
                continue
            seen += 1
            kinds = sorted(f["kind"] for f in res["findings"])
            self.assertIn("degenerate_unflagged", kinds,
                          f"{run_id} at {PRE_SHA} should be flagged; got {kinds} "
                          f"/ notes {res['notes']}")
        if not seen:
            self.skipTest(f"git could not serve the {PRE_SHA} fixtures")

    def test_post_fix_trio_is_clean(self):
        seen = 0
        for run_id in CORRECTED_TRIO:
            res = self._check(FIX_SHA, run_id)
            if res is None:
                continue
            seen += 1
            self.assertEqual(res["findings"], [],
                             f"{run_id} at {FIX_SHA} should be clean; got {res['findings']}")
        if not seen:
            self.skipTest(f"git could not serve the {FIX_SHA} fixtures")

    def test_originally_committed_siblings_and_seventh_run_are_clean(self):
        seen = 0
        for run_id in CLEAN_SIBLINGS:
            for sha in (PRE_SHA, FIX_SHA):
                res = self._check(sha, run_id)
                if res is None:
                    continue
                seen += 1
                self.assertEqual(res["findings"], [],
                                 f"{run_id} at {sha} should be clean; got {res['findings']}")
        if not seen:
            self.skipTest("git could not serve the sibling fixtures")

    def test_pre_fix_finding_names_the_measured_signature(self):
        """The finding must carry the evidence, not just a verdict."""
        res = self._check(PRE_SHA, CORRECTED_TRIO[0])
        if res is None:
            self.skipTest(f"git could not serve {PRE_SHA}")
        finding = next(f for f in res["findings"] if f["kind"] == "degenerate_unflagged")
        self.assertGreaterEqual(finding["n_comparisons"], 9)  # 3 metrics x 3 seeds, minimum
        self.assertIn("per_seed_comparisons", finding["shape"])


class TestLiveCorpus(unittest.TestCase):
    """The trio as it stands in the working tree TODAY. Skips if absent."""

    def test_corrected_trio_is_clean_on_disk(self):
        base = REPO_ROOT / "evidence" / "experiments"
        seen = 0
        for run_id in CORRECTED_TRIO + CLEAN_SIBLINGS:
            path = base / f"{run_id}.json"
            if not path.exists():
                continue
            manifest = mod._load(path)
            if manifest is None:
                continue
            seen += 1
            forms = {"flat": (path, manifest)}
            pack = base / EXPERIMENT_TYPE / "runs" / run_id / "manifest.json"
            if pack.exists():
                pm = mod._load(pack)
                if pm is not None:
                    forms["pack"] = (pack, pm)
            res = mod.check_run(run_id, forms)
            self.assertEqual(res["findings"], [],
                             f"{run_id} on disk should be clean; got {res['findings']}")
        if not seen:
            self.skipTest("V3-EXQ-673 manifests not present in this checkout")


class TestAsciiOutput(unittest.TestCase):
    def test_source_stdout_strings_are_ascii(self):
        """Repo convention: nothing reaching a terminal may be non-ASCII."""
        for name in ("check_manifest_degeneracy_consistency.py",
                     "test_check_manifest_degeneracy_consistency.py"):
            text = (REPO_ROOT / "scripts" / name).read_text(encoding="utf-8")
            for i, line in enumerate(text.splitlines(), 1):
                try:
                    line.encode("ascii")
                except UnicodeEncodeError:
                    self.fail(f"{name}:{i} non-ASCII: {line!r}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
