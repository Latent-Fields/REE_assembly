#!/usr/bin/env python3
"""Tests for check_claim_phase_consistency.py's graph-integrity checks.

Time-independent and self-contained: every fixture is a synthetic claim list
built in-process. Nothing here reads docs/claims/claims.yaml, so these tests do
not drift as the live registry changes -- which matters because the registry is
edited continuously by governance sessions and a test pinned to live counts
would fail for reasons unrelated to this module.

Roughly half of these are NEGATIVE controls. That is deliberate: the failure mode
for a graph checker is not missing a defect, it is widening its predicate until it
fires on ordinary work and gets ignored (the same reasoning recorded for
ref_move_guard.py in REE_Working/CLAUDE.md).

Run:  /opt/local/bin/python3 scripts/test_check_claim_phase_consistency.py
      (or: pytest scripts/test_check_claim_phase_consistency.py)
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_claim_phase_consistency import (  # noqa: E402
    reciprocal_prerequisite_cycles,
    reclassification_candidates,
    render_human,
    render_warn,
    stale_derived_provenance,
)


def claim(cid, **kw):
    """A minimal claim that qualifies as a V3 build commitment unless overridden."""
    base = {
        "id": cid,
        "status": "candidate",
        "claim_type": "mechanism_hypothesis",
        "polarity": "asserts",
        "implementation_phase": "v3",
    }
    base.update(kw)
    return base


def pairs(cycles):
    return {tuple(c["pair"]) for c in cycles}


def by_pair(cycles, a, b):
    key = sorted((a, b))
    for c in cycles:
        if c["pair"] == key:
            return c
    raise AssertionError(f"no cycle recorded for {a} <-> {b}")


# --------------------------------------------------------------------------
# reciprocal_prerequisite_cycles -- detection
# --------------------------------------------------------------------------


def test_reciprocal_pair_is_detected():
    cs = [claim("A", depends_on=["B"]), claim("B", depends_on=["A"])]
    assert pairs(reciprocal_prerequisite_cycles(cs)) == {("A", "B")}


def test_one_directional_edge_is_not_a_cycle():
    """NEGATIVE CONTROL: the overwhelmingly common shape must never fire."""
    cs = [claim("A", depends_on=["B"]), claim("B")]
    assert reciprocal_prerequisite_cycles(cs) == []


def test_emergent_from_counts_as_a_prerequisite_direction():
    """emergent_from is a prerequisite edge (module docstring), so it can close a cycle."""
    cs = [claim("A", emergent_from=["B"]), claim("B", depends_on=["A"])]
    rec = by_pair(reciprocal_prerequisite_cycles(cs), "A", "B")
    assert rec["edge_kinds"]["A->B"] == "emergent_from"
    assert rec["edge_kinds"]["B->A"] == "depends_on"


def test_instantiates_target_does_not_close_a_cycle():
    """NEGATIVE CONTROL: instantiates is registration, not a prerequisite, and
    prerequisite_edges() strips it from depends_on. A parent/child pair that
    declares both directions this way is the SD-033e shape, not a defect."""
    cs = [
        claim("CHILD", instantiates=["PARENT"], depends_on=["PARENT"]),
        claim("PARENT", depends_on=["CHILD"]),
    ]
    assert reciprocal_prerequisite_cycles(cs) == []


def test_dead_claims_are_excluded():
    """NEGATIVE CONTROL: a superseded claim is out of the live graph entirely."""
    cs = [claim("A", depends_on=["B"]), claim("B", depends_on=["A"], status="superseded")]
    assert reciprocal_prerequisite_cycles(cs) == []


def test_each_pair_reported_once():
    cs = [claim("A", depends_on=["B"]), claim("B", depends_on=["A"])]
    assert len(reciprocal_prerequisite_cycles(cs)) == 1


def test_three_cycle_is_not_reported():
    """Scope is deliberately 2-cycles only: they are unambiguous and cheap. A
    longer cycle is a different (and much noisier) judgement call."""
    cs = [
        claim("A", depends_on=["B"]),
        claim("B", depends_on=["C"]),
        claim("C", depends_on=["A"]),
    ]
    assert reciprocal_prerequisite_cycles(cs) == []


# --------------------------------------------------------------------------
# reciprocal_prerequisite_cycles -- load-bearing grading
# --------------------------------------------------------------------------


def test_load_bearing_when_cycle_produces_a_root_leak():
    cs = [
        claim("DRIVER", depends_on=["LATE"]),
        claim("LATE", depends_on=["DRIVER"], implementation_phase="v4"),
    ]
    rec = by_pair(reciprocal_prerequisite_cycles(cs), "DRIVER", "LATE")
    assert rec["load_bearing"] is True
    assert "ROOT leak" in " ".join(rec["reasons"])


def test_load_bearing_when_cycle_already_drove_a_reclassification():
    """The confirmed ARC-039 shape: the pull was APPLIED, so the claim is now v3
    and invisible to the candidate report -- the cycle is the only trace left."""
    cs = [
        claim("DRIVER", status="stable", depends_on=["PULLED"]),
        claim(
            "PULLED",
            depends_on=["DRIVER"],
            phase_provenance="derived",
            phase_derived_from="DRIVER",
        ),
    ]
    rec = by_pair(reciprocal_prerequisite_cycles(cs), "DRIVER", "PULLED")
    assert rec["load_bearing"] is True
    assert "phase_derived_from: DRIVER" in " ".join(rec["reasons"])


def test_latent_cycle_is_reported_but_not_load_bearing():
    """Same defect, but both sides share a phase lane so no phase moves today."""
    cs = [claim("A", depends_on=["B"]), claim("B", depends_on=["A"])]
    rec = by_pair(reciprocal_prerequisite_cycles(cs), "A", "B")
    assert rec["load_bearing"] is False
    assert rec["reasons"] == []


def test_non_driver_does_not_make_a_cycle_load_bearing():
    """NEGATIVE CONTROL: an open_question is not a build commitment, so it cannot
    force a prerequisite to V3 (module docstring, 'Driver gating')."""
    cs = [
        claim("Q", claim_type="open_question", polarity="asks", depends_on=["LATE"]),
        claim("LATE", depends_on=["Q"], implementation_phase="v4"),
    ]
    assert by_pair(reciprocal_prerequisite_cycles(cs), "Q", "LATE")["load_bearing"] is False


def test_load_bearing_sorts_first():
    cs = [
        claim("ZA", depends_on=["ZB"]),
        claim("ZB", depends_on=["ZA"]),
        claim("MA", depends_on=["MB"]),
        claim("MB", depends_on=["MA"], implementation_phase="v4"),
    ]
    out = reciprocal_prerequisite_cycles(cs)
    assert out[0]["pair"] == ["MA", "MB"] and out[0]["load_bearing"] is True


# --------------------------------------------------------------------------
# stale_derived_provenance
# --------------------------------------------------------------------------


def test_supported_derivation_is_not_flagged():
    """NEGATIVE CONTROL, and it is the live ARC-039 state: the derivation IS
    still supported by the graph. Detecting ARC-039 is the cycle check's job --
    this check must stay silent on it, or the two would double-report."""
    cs = [
        claim("DRIVER", status="stable", depends_on=["PULLED"]),
        claim("PULLED", phase_provenance="derived", phase_derived_from="DRIVER"),
    ]
    assert stale_derived_provenance(cs) == []


def test_severed_edge_is_flagged():
    cs = [
        claim("DRIVER", status="stable"),
        claim("PULLED", phase_provenance="derived", phase_derived_from="DRIVER"),
    ]
    (rec,) = stale_derived_provenance(cs)
    assert rec["id"] == "PULLED" and rec["reason"] == "no_prerequisite_edge"


def test_missing_driver_claim_is_flagged():
    cs = [claim("PULLED", phase_provenance="derived", phase_derived_from="GONE")]
    (rec,) = stale_derived_provenance(cs)
    assert rec["reason"] == "missing_driver"


def test_unset_driver_field_is_flagged():
    cs = [claim("PULLED", phase_provenance="derived")]
    (rec,) = stale_derived_provenance(cs)
    assert rec["reason"] == "missing_driver" and rec["phase_derived_from"] == []


def test_driver_no_longer_a_v3_commitment_is_flagged():
    cs = [
        claim("DRIVER", implementation_phase="v4", depends_on=["PULLED"]),
        claim("PULLED", phase_provenance="derived", phase_derived_from="DRIVER"),
    ]
    (rec,) = stale_derived_provenance(cs)
    assert rec["reason"] == "driver_not_v3_driver"


def test_assigned_provenance_is_never_flagged():
    """NEGATIVE CONTROL: only `derived` claims carry a derivation to go stale."""
    cs = [claim("X", phase_provenance="assigned"), claim("Y")]
    assert stale_derived_provenance(cs) == []


def test_one_live_driver_is_enough():
    """A claim derived from several drivers stays justified while any one holds."""
    cs = [
        claim("D1", status="stable", depends_on=["PULLED"]),
        claim("D2"),
        claim("PULLED", phase_provenance="derived", phase_derived_from=["D1", "D2"]),
    ]
    assert stale_derived_provenance(cs) == []


def test_dead_derived_claim_is_not_flagged():
    cs = [claim("PULLED", status="retracted", phase_provenance="derived")]
    assert stale_derived_provenance(cs) == []


# --------------------------------------------------------------------------
# Report wiring / backward compatibility
# --------------------------------------------------------------------------


def test_report_keeps_its_existing_contract():
    """The importable API is consumed by governance.sh and the workset generator;
    the new keys must be additive."""
    rep = reclassification_candidates([claim("A", depends_on=["B"]), claim("B", depends_on=["A"])])
    for key in ("candidates", "informational", "dangling_deps", "stats"):
        assert key in rep
    assert rep["stats"]["reciprocal_cycles"] == 1
    assert rep["stats"]["reciprocal_cycles_load_bearing"] == 0
    assert rep["stats"]["stale_derived_provenance"] == 0


def test_integrity_sections_render_even_with_no_candidates():
    """The candidate report early-returns when clean; the integrity findings must
    survive that path, or a registry with zero leaks hides its own cycles."""
    rep = reclassification_candidates([claim("A", depends_on=["B"]), claim("B", depends_on=["A"])])
    assert rep["candidates"] == {}
    text = render_human(rep)
    assert "No phase leaks" in text
    assert "latent: 1" in text


def test_warn_emits_load_bearing_cycles_only():
    cs = [
        claim("DRIVER", depends_on=["LATE"]),
        claim("LATE", depends_on=["DRIVER"], implementation_phase="v4"),
        claim("QUIET_A", depends_on=["QUIET_B"]),
        claim("QUIET_B", depends_on=["QUIET_A"]),
    ]
    warn = render_warn(reclassification_candidates(cs))
    assert "reciprocal-prerequisite DRIVER <-> LATE" in warn
    assert "QUIET_A" not in warn


def test_warn_emits_stale_derived_provenance():
    cs = [
        claim("DRIVER", status="stable"),
        claim("PULLED", phase_provenance="derived", phase_derived_from="DRIVER"),
    ]
    assert "stale-derived-phase PULLED" in render_warn(reclassification_candidates(cs))


def test_output_is_ascii_only():
    """REE_Working/CLAUDE.md: printed output must survive a cp1252 terminal."""
    cs = [
        claim("DRIVER", depends_on=["LATE"]),
        claim("LATE", depends_on=["DRIVER"], implementation_phase="v4"),
        claim("PULLED", phase_provenance="derived", phase_derived_from="GONE"),
    ]
    rep = reclassification_candidates(cs)
    for text in (render_human(rep), render_warn(rep)):
        text.encode("ascii")


def test_arc039_incident_replay():
    """End-to-end replay of the confirmed 2026-08-08 case.

    MECH-261 reached status:stable in V3 while ARC-039's entorhinal circuit was
    never built, so it cannot have been a prerequisite -- yet the reversed edge
    reclassified ARC-039 out of its authored v4 scope, and the applied result is
    invisible to the candidate report. Assert exactly that: no candidate, one
    load-bearing cycle.
    """
    cs = [
        claim("MECH-261", status="stable", depends_on=["ARC-038", "ARC-039", "SD-033a"]),
        claim(
            "ARC-039",
            claim_type="architectural_commitment",
            depends_on=["ARC-038", "MECH-092", "MECH-261"],
            phase_provenance="derived",
            phase_derived_from="MECH-261",
        ),
        claim("ARC-038"),
        claim("MECH-092"),
        claim("SD-033a"),
    ]
    rep = reclassification_candidates(cs)
    assert "ARC-039" not in rep["candidates"], "already reclassified -- invisible, as in production"
    assert rep["stats"]["reciprocal_cycles_load_bearing"] == 1
    rec = by_pair(rep["reciprocal_cycles"], "ARC-039", "MECH-261")
    assert rec["load_bearing"] is True


def main() -> int:
    tests = [(n, o) for n, o in sorted(globals().items()) if n.startswith("test_") and callable(o)]
    failed = []
    for name, fn in tests:
        try:
            fn()
        except Exception as exc:  # noqa: BLE001
            failed.append((name, exc))
            print(f"FAIL {name}: {exc}")
    print(f"\n{len(tests) - len(failed)}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
