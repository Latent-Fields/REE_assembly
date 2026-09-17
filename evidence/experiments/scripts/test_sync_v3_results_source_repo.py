"""Contract tests for sync_v3_results.build_runpack_docs provenance projection.

WHY THIS EXISTS. build_runpack_docs is a WHITELIST: it maps a flat manifest onto
the run-pack byte shape by naming each field explicitly. The indexer scores the
PACK, so a field the whitelist forgets dies at the flat manifest and reaches no
scored surface at all. That omission shape has now recurred five times --
machine_class (2026-07-16), claim_ids_tested (2026-08-08),
enabled_default_off_flags (2026-09-01), the always-core four (2026-09-09), and
source_repo.commit (2026-09-17, the V3-EXQ-1036 autopsy). Each time the flat
carried the field the whole time and the mapping simply never read it.

Two jobs:

1. PROJECTION on synthetic flats: a flat carrying substrate_commit produces a
   pack whose source_repo.commit is that sha (not ""), and a flat carrying none
   still produces the honestly-falsy "" rather than a truthy "unknown" -- see the
   rationale comment at the fix site. The empty-string case also pins
   byte-identity with the pre-fix output.

2. DELIBERATE OMISSIONS stay omitted: criteria / arm_results / readout are NOT
   projected into the pack manifest, on purpose (build_experiment_indexes globs
   arm_results from the flats, reads top-level criteria nowhere, and takes scalar
   readouts through metrics.json `values`). This test pins that decision so the
   next reader who measures the gap finds a failing assertion explaining it
   rather than re-deriving the whole consumer audit.

Run directly:  python test_sync_v3_results_source_repo.py
Or via pytest:  pytest test_sync_v3_results_source_repo.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sync_v3_results import build_runpack_docs  # noqa: E402

SHA = "6558770b7404e3647fbc54089909e5227eac0d34"


def _flat(**extra):
    base = {
        "run_id": "v3_exq_9999_probe_20260917T101112Z_v3",
        "status": "PASS",
        "timestamp_utc": "20260917T101112Z",
        "claim_ids_tested": ["MECH-999"],
    }
    base.update(extra)
    return base


def test_substrate_commit_populates_source_repo_commit():
    manifest, _, _ = build_runpack_docs(
        _flat(substrate_commit={"commit": SHA, "dirty": False, "branch": "main"}),
        "v3_exq_9999_probe",
    )
    assert manifest["source_repo"]["commit"] == SHA, manifest["source_repo"]
    assert manifest["source_repo"]["branch"] == "main"
    assert manifest["source_repo"]["name"] == "ree-v3"


def test_substrate_commit_branch_is_carried_when_not_main():
    manifest, _, _ = build_runpack_docs(
        _flat(substrate_commit={"commit": SHA, "dirty": True, "branch": "integration/x"}),
        "v3_exq_9999_probe",
    )
    assert manifest["source_repo"]["branch"] == "integration/x"
    # `dirty` is deliberately NOT folded into source_repo (schema is
    # {name, commit, branch}); it survives in full on the substrate_commit block.
    assert "dirty" not in manifest["source_repo"]
    assert manifest["substrate_commit"]["dirty"] is True


def test_absent_substrate_commit_keeps_falsy_empty_string():
    """NOT "unknown": generate_experiment_profile tests `if not commit` to decide
    whether to report the provenance gap, so a truthy placeholder would silence a
    real finding. Also pins byte-identity with the pre-2026-09-17 output."""
    manifest, _, _ = build_runpack_docs(_flat(), "v3_exq_9999_probe")
    assert manifest["source_repo"] == {"name": "ree-v3", "commit": "", "branch": "main"}


def test_malformed_substrate_commit_is_ignored():
    for bad in ("not-a-dict", {"commit": ""}, {"commit": "   "}, {}, None):
        manifest, _, _ = build_runpack_docs(
            _flat(substrate_commit=bad), "v3_exq_9999_probe"
        )
        assert manifest["source_repo"]["commit"] == "", bad


def test_rich_blocks_are_deliberately_not_projected():
    """Pins the documented decision -- see the DELIBERATE OMISSIONS comment in
    build_runpack_docs and the block above _PACK_PROVENANCE_KEYS in ree-v3
    validate_recording.py. If you are here because you measured these missing
    from a pack: that is expected, and the consumer audit is in those comments."""
    manifest, metrics, _ = build_runpack_docs(
        _flat(
            criteria=[{"name": "c1", "load_bearing": True, "passed": True}],
            arm_results=[{"arm": "on", "score": 1.0}],
            readout={"latched_fraction": 0.5},
        ),
        "v3_exq_9999_probe",
    )
    for key in ("criteria", "arm_results", "readout", "per_seed_dv"):
        assert key not in manifest, f"{key} unexpectedly projected into the pack"
    # ...but the scalar readout DOES reach the pack, via metrics.json `values`.
    assert metrics["values"] == {"latched_fraction": 0.5}


def test_interpretation_block_is_projected():
    """The counterpart to the test above: `interpretation` IS carried, which is
    why top-level `criteria` need not be -- every criteria read in
    build_experiment_indexes is interp.get("criteria")."""
    interp = {"label": "diagnostic", "criteria": [{"name": "c1", "passed": True}]}
    manifest, _, _ = build_runpack_docs(
        _flat(interpretation=interp), "v3_exq_9999_probe"
    )
    assert manifest["interpretation"] == interp


if __name__ == "__main__":
    import traceback

    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"PASS {name}")
            except Exception:
                failures += 1
                print(f"FAIL {name}")
                traceback.print_exc()
    print(f"\n{'OK' if not failures else str(failures) + ' FAILURE(S)'}")
    sys.exit(1 if failures else 0)
