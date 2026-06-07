"""Contract tests for build_experiment_indexes.py adjudication logic.

Focus: the (3a) diagnostic-adjudication readiness recompute in
`_compute_adjudication` must respect each precondition's bound DIRECTION.

A FLOOR precondition (the default) is unmet when measured < threshold.
An UPPER-bound / CEILING precondition (e.g. rolled_out_zworld_*_bounded,
"stayed below the 643a explosion ceiling", threshold 1e6) is unmet only when
measured > threshold -- measured << threshold means the ceiling check PASSED.

Regression target: 2026-06-07 directionality bug where the recompute treated
EVERY numeric measured/threshold precondition as a floor (`m < t`), false-flagging
V3-EXQ-648a and V3-EXQ-649 `precondition_unmet`.

Run directly:  python test_build_experiment_indexes.py
Or via pytest:  pytest test_build_experiment_indexes.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build_experiment_indexes as b  # noqa: E402


def _floor(measured, threshold, met=True):
    return {"name": "spread_supra_floor", "kind": "readiness",
            "measured": measured, "threshold": threshold, "met": met}


def _ceiling(measured, threshold, met=True, tag="direction"):
    p = {"name": "magnitude_bounded", "kind": "readiness",
         "measured": measured, "threshold": threshold, "met": met}
    if tag == "direction":
        p["direction"] = "upper"
    elif tag == "comparator":
        p["comparator"] = "<="
    return p


def _interp(preconditions, label="x", criteria=None):
    d = {"label": label, "preconditions": preconditions}
    if criteria is not None:
        d["criteria"] = criteria
    return d


# --- _precondition_direction ----------------------------------------------

def test_direction_defaults_to_lower():
    assert b._precondition_direction({"measured": 1, "threshold": 2}) == "lower"


def test_direction_explicit_upper():
    assert b._precondition_direction({"direction": "upper"}) == "upper"
    assert b._precondition_direction({"direction": "ceiling"}) == "upper"
    assert b._precondition_direction({"direction": "max"}) == "upper"


def test_direction_explicit_lower():
    assert b._precondition_direction({"direction": "lower"}) == "lower"
    assert b._precondition_direction({"direction": "floor"}) == "lower"


def test_comparator_resolves_direction():
    assert b._precondition_direction({"comparator": "<="}) == "upper"
    assert b._precondition_direction({"comparator": "<"}) == "upper"
    assert b._precondition_direction({"comparator": ">="}) == "lower"
    assert b._precondition_direction({"comparator": ">"}) == "lower"


def test_comparator_wins_over_unknown_direction():
    assert b._precondition_direction({"comparator": "<=", "direction": "??"}) == "upper"


# --- (3a) recompute: the load-bearing regression ---------------------------

def test_upper_bound_precondition_that_passes_is_not_flagged():
    """The core regression: a ceiling far below its threshold is VERIFIED, not
    precondition_unmet (V3-EXQ-648a / V3-EXQ-649 signature)."""
    interp = _interp([_ceiling(0.190288, 1_000_000.0)])
    label, flag = b._compute_adjudication(interp, "PASS", "diagnostic")
    assert flag == "verified", flag


def test_upper_bound_via_comparator_tag_also_passes():
    interp = _interp([_ceiling(0.19, 1_000_000.0, tag="comparator")])
    _, flag = b._compute_adjudication(interp, "PASS", "diagnostic")
    assert flag == "verified", flag


def test_upper_bound_genuinely_violated_is_flagged():
    """A ceiling ABOVE its threshold must still flag precondition_unmet."""
    interp = _interp([_ceiling(2_000_000.0, 1_000_000.0, met=True)])
    _, flag = b._compute_adjudication(interp, "PASS", "diagnostic")
    assert flag == "precondition_unmet", flag


def test_floor_below_threshold_still_flagged():
    """Default floor semantics preserved: measured < threshold -> unmet."""
    interp = _interp([_floor(0.02, 0.05, met=True)])
    _, flag = b._compute_adjudication(interp, "FAIL", "diagnostic")
    assert flag == "precondition_unmet", flag


def test_floor_above_threshold_passes():
    interp = _interp([_floor(0.149, 0.05)])
    _, flag = b._compute_adjudication(interp, "PASS", "diagnostic")
    assert flag == "verified", flag


def test_mixed_floors_and_ceiling_all_clear():
    """V3-EXQ-648a shape: two floors cleared + one upper-bound ceiling cleared."""
    interp = _interp([
        _floor(0.149011, 0.05),
        _floor(0.02061524, 0.0001),
        _ceiling(0.315368, 1_000_000.0),
    ], criteria=[{"name": "C2", "load_bearing": True, "passed": True}])
    _, flag = b._compute_adjudication(interp, "PASS", "diagnostic")
    assert flag == "verified", flag


def test_ceiling_clears_but_floor_fails_is_flagged():
    """Direction is per-entry: one floor failing still flags even if the
    ceiling is fine."""
    interp = _interp([
        _floor(0.01, 0.05, met=True),       # below floor -> unmet
        _ceiling(0.3, 1_000_000.0),         # fine
    ])
    _, flag = b._compute_adjudication(interp, "FAIL", "diagnostic")
    assert flag == "precondition_unmet", flag


def test_non_diagnostic_is_na():
    interp = _interp([_floor(0.01, 0.05)])
    _, flag = b._compute_adjudication(interp, "FAIL", "evidence")
    assert flag == "n/a", flag


def _run_all():
    fns = [v for k, v in sorted(globals().items())
           if k.startswith("test_") and callable(v)]
    failed = 0
    for fn in fns:
        try:
            fn()
            print(f"PASS {fn.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL {fn.__name__}: {e}")
    print(f"\n{len(fns) - failed}/{len(fns)} passed")
    return failed


if __name__ == "__main__":
    sys.exit(1 if _run_all() else 0)
