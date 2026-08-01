"""Tests for `default_off_drift_guard.py`.

These pin the parts that would rot SILENTLY -- the config.py field parse, the
claim->knob attribution grading, and above all the enablement counter, which is the
load-bearing discriminator. A guard whose counter drifts does not fail loudly; it just
stops distinguishing drift from benign config-default-off, which is the whole point.

Fast by construction: every test runs against SYNTHETIC in-memory / tmp fixtures, never
the ~1340-file live corpus. One real-config smoke (`test_real_config_parses`) parses the
live config.py (cheap) but does NOT scan the corpus.

Run: /opt/local/bin/python3 -m pytest REE_assembly/scripts/test_default_off_drift_guard.py -q
"""

import ast
import importlib.util
import sys
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve().parent
_SPEC = importlib.util.spec_from_file_location(
    "default_off_drift_guard", _HERE / "default_off_drift_guard.py"
)
g = importlib.util.module_from_spec(_SPEC)
# Register before exec: @dataclass resolves cls.__module__ via sys.modules.
sys.modules["default_off_drift_guard"] = g
_SPEC.loader.exec_module(g)


# --------------------------------------------------------------------------- #
# _literal_value / _classify_rhs -- the on/off/unresolved verdict               #
# --------------------------------------------------------------------------- #


def _rhs(src, env=None):
    """Classify the RHS of `x = <src>`."""
    node = ast.parse("x = " + src).body[0].value
    return g._classify_rhs(node, env or {})


def test_classify_literals_on_off():
    assert _rhs("True") == "on"
    assert _rhs("False") == "off"
    assert _rhs("None") == "off"
    assert _rhs("0") == "off"
    assert _rhs("0.0") == "off"
    assert _rhs("1") == "on"
    assert _rhs("0.5") == "on"
    assert _rhs("2.0") == "on"
    assert _rhs("-1") == "on"          # non-zero, even if negative
    assert _rhs("1e-3") == "on"
    assert _rhs("0e0") == "off"


def test_classify_unresolved_when_no_env():
    # A bare name / attribute / expression the scanner cannot evaluate.
    assert _rhs("env.action_dim") == "unresolved"
    assert _rhs("some_param") == "unresolved"
    assert _rhs("a + b") == "unresolved"


def test_classify_resolves_module_constant():
    # The SD-035 false-positive shape: knob set to a module constant = 1.0.
    assert _rhs("ARM3_GAIN", {"ARM3_GAIN": 1.0}) == "on"
    # An OFF-arm constant must resolve to off, NOT be counted as enablement.
    assert _rhs("ARM0_GAIN", {"ARM0_GAIN": 0.0}) == "off"
    assert _rhs("USE_IT", {"USE_IT": True}) == "on"
    assert _rhs("USE_IT", {"USE_IT": False}) == "off"


def test_module_constants_collects_literals_only():
    tree = ast.parse(
        "A = 1.0\n"
        "B = 0\n"
        "C = True\n"
        "D = env.action_dim\n"   # not a literal -> absent
        "E: float = 2.5\n"
        "F = -3\n"
    )
    env = g._module_constants(tree)
    assert env == {"A": 1.0, "B": 0, "C": True, "E": 2.5, "F": -3}
    assert "D" not in env


# --------------------------------------------------------------------------- #
# _file_knob_sites -- kwarg / dict / assignment forms                          #
# --------------------------------------------------------------------------- #

KNOBS = {"use_x", "gain_y", "dim_z"}


def _sites(src):
    tree = ast.parse(src)
    env = g._module_constants(tree)
    return g._file_knob_sites(tree, KNOBS, env)


def test_sites_keyword_arg():
    assert _sites("REEConfig(use_x=True)")["use_x"] == {"on"}


def test_sites_dict_literal():
    assert _sites('cfg = {"gain_y": 0.5}')["gain_y"] == {"on"}


def test_sites_off_arm_not_enablement():
    # Explicit default value is present as a site but classified OFF.
    assert _sites("REEConfig(gain_y=0.0)")["gain_y"] == {"off"}


def test_sites_module_const_resolution():
    src = "ARM = 1.0\nREEConfig(gain_y=ARM)\n"
    assert _sites(src)["gain_y"] == {"on"}


def test_sites_unresolved_variable():
    assert _sites("REEConfig(dim_z=env.action_dim)")["dim_z"] == {"unresolved"}


def test_sites_attribute_assignment():
    assert _sites("cfg.use_x = True")["use_x"] == {"on"}


def test_sites_ignores_unknown_names():
    assert "not_a_knob" not in _sites("REEConfig(not_a_knob=True)")


# --------------------------------------------------------------------------- #
# count_enablements -- the file-level on/unresolved buckets                    #
# --------------------------------------------------------------------------- #


def _corpus(tmp_path, files):
    root = tmp_path / "experiments"
    root.mkdir()
    for name, body in files.items():
        (root / name).write_text(body)
    return [("exp", root), ("test", tmp_path / "tests")]  # tests/ absent -> skipped


def test_count_on_vs_off_vs_unresolved(tmp_path):
    roots = _corpus(
        tmp_path,
        {
            "a.py": "REEConfig(gain_y=0.5)",              # on
            "b.py": "REEConfig(gain_y=0.0)",              # off -> not counted
            "c.py": "REEConfig(gain_y=env.dim)",          # unresolved
            "d.py": "ARM = 0.0\nREEConfig(gain_y=ARM)",   # off-arm const -> not counted
        },
    )
    counts = g.count_enablements(roots, KNOBS)
    assert counts["exp"]["gain_y"] == {"on": 1, "unresolved": 1}


def test_count_on_wins_over_unresolved_in_same_file(tmp_path):
    roots = _corpus(
        tmp_path, {"a.py": "REEConfig(gain_y=0.5)\nOther(gain_y=env.dim)"}
    )
    counts = g.count_enablements(roots, KNOBS)
    assert counts["exp"]["gain_y"] == {"on": 1, "unresolved": 0}


def test_count_skips_unparseable_file(tmp_path):
    roots = _corpus(tmp_path, {"good.py": "REEConfig(use_x=True)", "bad.py": "def ("})
    counts = g.count_enablements(roots, KNOBS)
    assert counts["exp"]["use_x"] == {"on": 1, "unresolved": 0}


# --------------------------------------------------------------------------- #
# extract_claim_ids -- decl vs mention (the MECH-104 failure mode)             #
# --------------------------------------------------------------------------- #


def test_attribution_decl_when_id_heads_comment():
    # "# SD-007: ReafferencePredictor ..." -> decl
    assert g.extract_claim_ids(["SD-007: ReafferencePredictor for z_world."]) == {
        "SD-007": "decl"
    }


def test_attribution_multi_id_header_all_decl():
    # "# MECH-112 / MECH-117: wanting weight" -> BOTH decl (the ^-anchor bug fix).
    graded = g.extract_claim_ids(["MECH-112 / MECH-117: wanting signal weight"])
    assert graded == {"MECH-112": "decl", "MECH-117": "decl"}


def test_attribution_mention_when_mid_prose():
    # MECH-104 named mid-sentence, not heading -> mention (the false positive).
    graded = g.extract_claim_ids(
        ["Reuses the MECH-104 volatility-surprise lit basis (Aston-Jones 2005)."]
    )
    assert graded == {"MECH-104": "mention"}


def test_attribution_decl_beats_mention_across_lines():
    graded = g.extract_claim_ids(
        ["SD-020: precision-weighted PE target.", "Chen 2023 backs SD-020 further."]
    )
    assert graded["SD-020"] == "decl"


# --------------------------------------------------------------------------- #
# parse_knobs -- default-off extraction + from_dims exclusion                  #
# --------------------------------------------------------------------------- #


def test_parse_knobs_defaults_and_exclusions(tmp_path):
    src = (
        "from dataclasses import dataclass\n"
        "@dataclass\n"
        "class C:\n"
        "    # SD-001: a flag.\n"
        "    use_flag: bool = False\n"
        "    # SD-002: a weight.\n"
        "    weight: float = 0.0\n"
        "    count: int = 0\n"
        "    on_by_default: bool = True\n"      # excluded (not default-off)
        "    nonzero: float = 0.5\n"            # excluded (not default-off)\n"
        "    def from_dims(self):\n"
        "        use_flag = False\n"            # inside a method -> excluded\n"
    )
    cfg = tmp_path / "config.py"
    cfg.write_text(src)
    knobs = g.parse_knobs(cfg)
    assert set(knobs) == {"use_flag", "weight", "count"}
    assert knobs["use_flag"].default == "False"
    assert knobs["weight"].default == "0.0"
    assert knobs["count"].default == "0"
    assert knobs["use_flag"].claim_ids == {"SD-001": "decl"}


# --------------------------------------------------------------------------- #
# Row.gating -- unresolved experiment sites suppress a FAIL                    #
# --------------------------------------------------------------------------- #


def _row(status="stable", claim="SD-999", exp_on=0, exp_unres=0, knob="k"):
    kn = g.Knob(name=knob, lineno=1, owner="C", default="False")
    kn.exp_files, kn.exp_unresolved = exp_on, exp_unres
    return g.Row(
        claim_id=claim, status=status, knob=kn, evidence_from="run",
        evidence_verdict="", inertness="-", attr="decl",
    )


def test_gating_true_on_zero_enablement_stable():
    assert _row(status="stable", exp_on=0, exp_unres=0).gating is True


def test_gating_false_when_confirmed_enablement():
    assert _row(exp_on=3).gating is False


def test_gating_false_when_unresolved_present():
    # The SD-035 / override_pfc_eta_gain shape: no confirmed ON, but an unresolved
    # site that might be one -> do NOT FAIL.
    assert _row(exp_on=0, exp_unres=1).gating is False


def test_gating_false_for_provisional_status():
    assert _row(status="provisional", exp_on=0).gating is False


def test_gating_respects_allowlists():
    assert _row(claim="ARC-007", exp_on=0).gating is False        # allowlisted claim
    assert _row(knob="use_differentiable_cem", exp_on=0).gating is False  # allowlisted knob


# --------------------------------------------------------------------------- #
# Real config smoke (cheap -- parse only, no corpus scan)                      #
# --------------------------------------------------------------------------- #


def test_real_config_parses():
    base = Path(g.os.environ.get("REE_WORKING", Path(g.__file__).resolve().parents[2]))
    cfg = base / "ree-v3/ree_core/utils/config.py"
    if not cfg.exists():
        pytest.skip("live config.py not present")
    knobs = g.parse_knobs(cfg)
    # Sanity: a healthy number of default-off fields, many claim-tagged.
    assert len(knobs) > 100
    assert sum(1 for k in knobs.values() if k.claim_ids) > 50
    # Known default-off knobs from the source audit are present with the right default.
    assert knobs["harm_surprise_pe_enabled"].default == "False"
    assert knobs["pacc_offline_decay"].default == "0.0"
    # from_dims mirror is excluded: no knob should be attributed to that method body.
    # (Spot-check: the parse found only dataclass fields, so counts are plausible.)
    assert "use_differentiable_cem" in knobs


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
