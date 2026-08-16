#!/usr/bin/env python3
"""Contract tests for the Steward T0 auto-fix lane (D-006, D-008).

Run from REE_assembly/ root:
    /opt/local/bin/python3 -m pytest scripts/steward/test_autofix.py -q

Every test builds a SYNTHETIC tree in a tmpdir, for the reason stated in
test_run_detectors.py: the live counts are expected to fall as governance acts,
and a test pinned to them fails on a CORRECT fix and teaches the next session to
weaken the detector. Two tests deliberately read the SHIPPED registry, and both
assert a property that must hold no matter what it contains (no fix on a
dispositioned duplicate; a byte-identical JSON round-trip) rather than a count.

THE SHAPE OF THIS FILE. Roughly half the tests are NEGATIVE CONTROLS -- cases
where the fixer must do NOTHING. That ratio is deliberate and load-bearing: a
T0 auto-fix that fires too eagerly is worse than no auto-fix at all, because it
edits shared, human-adjudicated evidence files unattended. The tests that pin
"does not fire" are what stop a later session widening a predicate until the
lane starts overwriting dispositions.

Time-independent: no sleeps, no wall-clock dependence, no network.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

_STEWARD = Path(__file__).resolve().parent
if str(_STEWARD) not in sys.path:
    sys.path.insert(0, str(_STEWARD))

from detectors import d006_duplicate_governance_flag as D006  # noqa: E402
from detectors import d008_plan_frontmatter_date_drift as D008  # noqa: E402
from detectors._common import load_context  # noqa: E402

NOW = "2026-08-16T12:00:00Z"


def _load_runner():
    spec = importlib.util.spec_from_file_location(
        "steward_run_detectors_autofix", _STEWARD / "run_detectors.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["steward_run_detectors_autofix"] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


runner = _load_runner()


# ---------------------------------------------------------------------------
# fixture helpers
# ---------------------------------------------------------------------------

def make_tree(root: Path) -> Path:
    (root / "docs" / "claims").mkdir(parents=True, exist_ok=True)
    (root / "evidence" / "planning").mkdir(parents=True, exist_ok=True)
    (root / "docs" / "claims" / "claims.yaml").write_text(
        yaml.safe_dump([], sort_keys=False), encoding="utf-8")
    return root


def flag(fid, claims, ftype="stale_note", raised="2026-08-08T06:28:25Z",
         summary="the same raise, written twice", status="open",
         resolution_note=None, resolved_at=None):
    return {"flag_id": fid, "claim_ids": list(claims), "flag_type": ftype,
            "summary": summary, "raised_by_session": "sess",
            "raised_at": raised, "status": status,
            "resolved_at": resolved_at, "resolution_note": resolution_note}


def write_flags(root: Path, items: list[dict]) -> Path:
    p = root / "evidence" / "planning" / "governance_flags.v1.json"
    p.write_text(json.dumps(
        {"schema_version": "governance_flags/v1", "items": items},
        indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return p


def write_plan(root: Path, name: str, plan_lu: str, node_dates: list[str],
               extra_head: str = "") -> Path:
    nodes = "\n".join(
        '    - id: "%s:GAP-%d"\n      title: "n%d"\n      status: open\n'
        '      last_updated: %s' % (name, i + 1, i + 1, d)
        for i, d in enumerate(node_dates))
    body = ("---\n"
            "closure_plan:\n"
            "  id: %s\n"
            '  title: "%s"\n'
            "  registered: 2026-05-08\n"
            "  last_updated: %s\n"
            "%s"
            "  nodes:\n%s\n"
            "---\n\n# %s\n" % (name, name, plan_lu, extra_head, nodes, name))
    p = root / "evidence" / "planning" / ("%s_plan.md" % name)
    p.write_text(body, encoding="utf-8")
    return p


def ctx_for(root: Path):
    return load_context(root)


def read_flags(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))["items"]


# ===========================================================================
# D-006 -- duplicate governance flags
# ===========================================================================

def test_d006_clean_tree_is_a_noop(tmp_path):
    """No duplicates -> no findings, no fixes, file untouched."""
    root = make_tree(tmp_path / "repo")
    p = write_flags(root, [flag("GFLAG-0001", ["ARC-033"]),
                           flag("GFLAG-0002", ["MECH-100"], ftype="promotion_review")])
    before = p.read_text(encoding="utf-8")
    ctx = ctx_for(root)
    findings, summary = D006.run(ctx)
    assert findings == []
    assert D006.fix(ctx, NOW, dry_run=True) == []
    assert D006.fix(ctx, NOW, dry_run=False) == []
    assert p.read_text(encoding="utf-8") == before


def test_d006_seeded_duplicate_produces_exactly_one_reversible_edit(tmp_path):
    root = make_tree(tmp_path / "repo")
    p = write_flags(root, [
        flag("GFLAG-0011", ["MECH-264", "SD-033e"]),
        flag("GFLAG-0012", ["MECH-264", "SD-033e"]),   # the retry-loop twin
    ])
    ctx = ctx_for(root)

    planned = D006.fix(ctx, NOW, dry_run=True)
    assert len(planned) == 1
    assert planned[0]["subject"] == "GFLAG-0012"
    assert planned[0]["dry_run"] is True
    assert "reverse" in planned[0]
    # dry run must not have touched the file
    assert read_flags(p)[1]["status"] == "open"

    applied = D006.fix(ctx_for(root), NOW, dry_run=False)
    assert len(applied) == 1
    items = read_flags(p)
    assert len(items) == 2, "rows must never be deleted -- annotate only"
    assert items[0]["status"] == "open", "canonical is left alone"
    assert items[1]["status"] == "superseded"
    assert "GFLAG-0011" in items[1]["resolution_note"]
    assert items[1]["resolved_at"] == NOW


def test_d006_is_idempotent(tmp_path):
    """Second --fix must be a no-op: the twin is now dispositioned."""
    root = make_tree(tmp_path / "repo")
    write_flags(root, [flag("GFLAG-0011", ["MECH-264"]),
                       flag("GFLAG-0012", ["MECH-264"])])
    D006.fix(ctx_for(root), NOW, dry_run=False)
    assert D006.fix(ctx_for(root), NOW, dry_run=False) == []


def test_d006_does_not_touch_an_already_dispositioned_duplicate(tmp_path):
    """The live GFLAG-0015 shape: a real duplicate a human marked `resolved`.

    Its note says "resolved together". Flipping it to `superseded` would be the
    detector second-guessing an adjudication whose reasoning it cannot see.
    """
    root = make_tree(tmp_path / "repo")
    p = write_flags(root, [
        flag("GFLAG-0014", ["MECH-321"], ftype="evidence_discrepancy"),
        flag("GFLAG-0015", ["MECH-321"], ftype="evidence_discrepancy",
             status="resolved",
             resolution_note="Duplicate of GFLAG-0014 -- resolved together."),
    ])
    before = p.read_text(encoding="utf-8")
    ctx = ctx_for(root)
    assert D006.fix(ctx, NOW, dry_run=True) == []
    assert p.read_text(encoding="utf-8") == before
    # ...and it is not reported as a defect either: nothing is left to do.
    assert D006.run(ctx)[0] == []


def test_d006_does_not_fix_a_same_key_entry_with_a_different_summary(tmp_path):
    """Same claim + type + day can be two GENUINELY different findings."""
    root = make_tree(tmp_path / "repo")
    p = write_flags(root, [
        flag("GFLAG-0020", ["MECH-500"], summary="first, about the encoder"),
        flag("GFLAG-0021", ["MECH-500"], summary="second, about the readout"),
    ])
    before = p.read_text(encoding="utf-8")
    ctx = ctx_for(root)
    assert D006.fix(ctx, NOW, dry_run=True) == []
    assert p.read_text(encoding="utf-8") == before

    findings, _ = D006.run(ctx)
    assert len(findings) == 1
    assert findings[0]["tier"] == "T1", "ambiguous -> demoted, not guessed"
    assert findings[0]["autofix"] is False
    assert findings[0]["escalate"] is True


def test_d006_does_not_fix_when_raised_at_differs_by_time(tmp_path):
    """Same date, different second = two raises, not one retried."""
    root = make_tree(tmp_path / "repo")
    p = write_flags(root, [
        flag("GFLAG-0030", ["MECH-600"], raised="2026-08-08T06:00:00Z"),
        flag("GFLAG-0031", ["MECH-600"], raised="2026-08-08T18:00:00Z"),
    ])
    before = p.read_text(encoding="utf-8")
    assert D006.fix(ctx_for(root), NOW, dry_run=True) == []
    assert p.read_text(encoding="utf-8") == before


def test_d006_canonical_is_earliest_then_lowest_id(tmp_path):
    root = make_tree(tmp_path / "repo")
    p = write_flags(root, [
        flag("GFLAG-0099", ["MECH-700"], raised="2026-08-08T06:00:00Z"),
        flag("GFLAG-0011", ["MECH-700"], raised="2026-08-08T06:00:00Z"),
        flag("GFLAG-0055", ["MECH-700"], raised="2026-08-08T06:00:00Z"),
    ])
    D006.fix(ctx_for(root), NOW, dry_run=False)
    by_id = {i["flag_id"]: i for i in read_flags(p)}
    assert by_id["GFLAG-0011"]["status"] == "open", "lowest id wins the tie"
    assert by_id["GFLAG-0055"]["status"] == "superseded"
    assert by_id["GFLAG-0099"]["status"] == "superseded"


def test_d006_never_deletes_rows(tmp_path):
    root = make_tree(tmp_path / "repo")
    p = write_flags(root, [flag("GFLAG-000%d" % i, ["MECH-800"])
                           for i in range(1, 5)])
    D006.fix(ctx_for(root), NOW, dry_run=False)
    assert len(read_flags(p)) == 4


def test_d006_shipped_registry_round_trips_byte_identically():
    """The write-back must not reformat 79KB of shared evidence.

    CLAUDE.md "Narrow Edits Only": a fix intended to change one field that
    instead rewrites the whole file is the failure mode, not the fix.
    """
    live = Path(__file__).resolve().parents[2] / D006.REGISTRY_REL
    if not live.exists():
        pytest.skip("live registry not present")
    orig = live.read_text(encoding="utf-8")
    out = json.dumps(json.loads(orig), indent=2, ensure_ascii=False) + "\n"
    assert out == orig


def test_d006_shipped_registry_needs_no_fixes():
    """Clean-tree no-op against the REAL registry (acceptance criterion).

    Every duplicate on the tree is already dispositioned, so the correct number
    of automatic edits is zero. Asserted as a PROPERTY ("nothing undispositioned
    is auto-fixable"), which stays true however the registry grows.
    """
    repo = Path(__file__).resolve().parents[2]
    if not (repo / D006.REGISTRY_REL).exists():
        pytest.skip("live registry not present")
    assert D006.fix(load_context(repo), NOW, dry_run=True) == []


# ===========================================================================
# D-008 -- plan frontmatter date drift
# ===========================================================================

def test_d008_in_sync_plan_is_a_noop(tmp_path):
    root = make_tree(tmp_path / "repo")
    p = write_plan(root, "alpha", "2026-06-16", ["2026-06-14", "2026-06-16"])
    before = p.read_text(encoding="utf-8")
    ctx = ctx_for(root)
    assert D008.run(ctx)[0] == []
    assert D008.fix(ctx, NOW, dry_run=False) == []
    assert p.read_text(encoding="utf-8") == before


def test_d008_plan_newer_than_nodes_is_not_drift(tmp_path):
    """drives_motivation_v4_plan.md's shape -- a legitimate plan-level edit."""
    root = make_tree(tmp_path / "repo")
    p = write_plan(root, "beta", "2026-08-05", ["2026-06-14"])
    before = p.read_text(encoding="utf-8")
    ctx = ctx_for(root)
    assert D008.run(ctx)[0] == []
    assert D008.fix(ctx, NOW, dry_run=False) == []
    assert p.read_text(encoding="utf-8") == before


def test_d008_seeded_drift_changes_exactly_one_line(tmp_path):
    root = make_tree(tmp_path / "repo")
    p = write_plan(root, "gamma", "2026-06-04", ["2026-07-29", "2026-06-01"])
    before = p.read_text(encoding="utf-8").split("\n")

    planned = D008.fix(ctx_for(root), NOW, dry_run=True)
    assert len(planned) == 1
    assert planned[0]["change"] == "closure_plan.last_updated 2026-06-04 -> 2026-07-29"
    assert p.read_text(encoding="utf-8").split("\n") == before, "dry run wrote"

    applied = D008.fix(ctx_for(root), NOW, dry_run=False)
    assert len(applied) == 1 and applied[0]["dry_run"] is False
    after = p.read_text(encoding="utf-8").split("\n")

    assert len(after) == len(before)
    diff = [i for i in range(len(before)) if before[i] != after[i]]
    assert len(diff) == 1, "exactly one line may change"
    assert before[diff[0]] == "  last_updated: 2026-06-04"
    assert after[diff[0]] == "  last_updated: 2026-07-29"


def test_d008_is_idempotent_and_monotonic(tmp_path):
    root = make_tree(tmp_path / "repo")
    p = write_plan(root, "delta", "2026-06-04", ["2026-07-29"])
    D008.fix(ctx_for(root), NOW, dry_run=False)
    assert D008.fix(ctx_for(root), NOW, dry_run=False) == []
    assert "  last_updated: 2026-07-29" in p.read_text(encoding="utf-8")


def test_d008_never_moves_the_date_backwards(tmp_path):
    """Monotonicity: the field can only ever be moved FORWARD."""
    root = make_tree(tmp_path / "repo")
    for name, plan_lu, nodes in [("a", "2026-08-01", ["2026-07-01"]),
                                 ("b", "2026-06-01", ["2026-07-01"])]:
        write_plan(root, name, plan_lu, nodes)
    planned = D008.fix(ctx_for(root), NOW, dry_run=True)
    assert len(planned) == 1, "only the backwards-drifting plan is a candidate"
    for rec in planned:
        # "closure_plan.last_updated <old> -> <new>"
        old, _, new = rec["change"].split()[-3:]
        assert new > old, "last_updated must only ever move forward"
        assert rec["subject"] == "b_plan.md"


def test_d008_ambiguous_edit_site_is_reported_not_fixed(tmp_path):
    """Two indent-2 last_updated lines -> the site is not determined."""
    root = make_tree(tmp_path / "repo")
    p = write_plan(root, "eps", "2026-06-04", ["2026-07-29"],
                   extra_head="  last_updated: 2026-06-05\n")
    before = p.read_text(encoding="utf-8")
    ctx = ctx_for(root)

    assert D008.fix(ctx, NOW, dry_run=True) == []
    assert p.read_text(encoding="utf-8") == before

    findings, _ = D008.run(ctx)
    assert len(findings) == 1
    assert findings[0]["tier"] == "T1" and findings[0]["autofix"] is False


def test_d008_ignores_node_dates_at_deeper_indent(tmp_path):
    """Node-level last_updated (indent 6) must never be the edit target."""
    root = make_tree(tmp_path / "repo")
    p = write_plan(root, "zeta", "2026-06-04", ["2026-07-29"])
    D008.fix(ctx_for(root), NOW, dry_run=False)
    text = p.read_text(encoding="utf-8")
    assert "      last_updated: 2026-07-29" in text, "node line untouched"
    assert "  last_updated: 2026-07-29\n" in text


def test_d008_plan_with_no_node_dates_is_skipped(tmp_path):
    root = make_tree(tmp_path / "repo")
    p = write_plan(root, "eta", "2026-06-04", [])
    before = p.read_text(encoding="utf-8")
    assert D008.fix(ctx_for(root), NOW, dry_run=False) == []
    assert p.read_text(encoding="utf-8") == before


def test_d008_findings_are_t0_and_do_not_escalate(tmp_path):
    """A T0 finding must not wake a model -- --fix repairs it."""
    root = make_tree(tmp_path / "repo")
    write_plan(root, "theta", "2026-06-04", ["2026-07-29"])
    findings, _ = D008.run(ctx_for(root))
    assert len(findings) == 1
    assert findings[0]["tier"] == "T0"
    assert findings[0]["autofix"] is True
    assert findings[0]["escalate"] is False


# ===========================================================================
# runner wiring
# ===========================================================================

def _full_run(root: Path, state: Path, **kw) -> dict:
    state.mkdir(parents=True, exist_ok=True)
    ctx = load_context(root)
    ctx.git_repos = [root]          # not a git repo -> git lane skips cleanly
    report = runner.build_report(ctx, state, NOW, 0.0)
    report["autofixes"] = runner.apply_fixes(ctx, NOW, **kw)
    return report


def test_runner_dry_run_writes_nothing(tmp_path):
    root = make_tree(tmp_path / "repo")
    p = write_plan(root, "iota", "2026-06-04", ["2026-07-29"])
    before = p.read_text(encoding="utf-8")
    report = _full_run(root, tmp_path / "state", dry_run=True)
    assert len(report["autofixes"]) == 1
    assert report["autofixes"][0]["applied"] is False
    assert p.read_text(encoding="utf-8") == before


def test_runner_apply_writes_and_ledgers_every_autofix(tmp_path):
    root = make_tree(tmp_path / "repo")
    write_plan(root, "kappa", "2026-06-04", ["2026-07-29"])
    write_flags(root, [flag("GFLAG-1", ["MECH-1"]), flag("GFLAG-2", ["MECH-1"])])
    state = tmp_path / "state"

    report = _full_run(root, state, dry_run=False)
    assert len(report["autofixes"]) == 2
    assert all(r["applied"] for r in report["autofixes"])

    runner.append_ledger(state, report, NOW)
    lines = [json.loads(l) for l in
             (state / runner.LEDGER_FILE).read_text(encoding="utf-8").splitlines()]
    assert lines[0]["action"] == "run"
    autofix = [l for l in lines if l["action"] == "autofix"]
    assert len(autofix) == 2, "every applied fix must appear in the ledger"
    assert {l["detector"] for l in autofix} == {"D-006", "D-008"}
    for l in autofix:
        assert l["ts"] == NOW and l["reverse"] and l["path"]


def test_runner_refuses_to_fix_a_file_with_uncommitted_changes(tmp_path):
    """The read-modify-write guard: never write over a live session's edit."""
    import subprocess
    root = make_tree(tmp_path / "repo")
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    subprocess.run(["git", "-C", str(root), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(root), "-c", "user.email=t@t",
                    "-c", "user.name=t", "commit", "-qm", "base"], check=True)

    p = write_plan(root, "lam", "2026-06-04", ["2026-07-29"])
    subprocess.run(["git", "-C", str(root), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(root), "-c", "user.email=t@t",
                    "-c", "user.name=t", "commit", "-qm", "plan"], check=True)

    # someone else's uncommitted edit
    p.write_text(p.read_text(encoding="utf-8") + "\nlocal wip\n", encoding="utf-8")
    before = p.read_text(encoding="utf-8")

    report = _full_run(root, tmp_path / "state", dry_run=False)
    assert len(report["autofixes"]) == 1
    assert report["autofixes"][0]["applied"] is False
    assert "uncommitted" in report["autofixes"][0]["skipped"]
    assert p.read_text(encoding="utf-8") == before


def test_runner_autofix_is_opt_in(tmp_path):
    """A plain run must not edit anything -- --fix is deliberate."""
    root = make_tree(tmp_path / "repo")
    p = write_plan(root, "mu", "2026-06-04", ["2026-07-29"])
    before = p.read_text(encoding="utf-8")
    ctx = load_context(root)
    ctx.git_repos = [root]
    runner.build_report(ctx, tmp_path / "state", NOW, 0.0)
    assert p.read_text(encoding="utf-8") == before


def test_finding_rejects_autofix_outside_t0():
    """The 'demote rather than guess' rule is enforced by the schema."""
    from detectors._common import finding
    with pytest.raises(ValueError):
        finding("D-000", "s", "t", "d", tier="T1", autofix=True)
    with pytest.raises(ValueError):
        finding("D-000", "s", "t", "d", tier="T9")
